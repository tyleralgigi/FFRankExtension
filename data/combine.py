import re
from rapidfuzz import process, fuzz
import pandas as pd

# Load CSVs
fantasypros = pd.read_csv("data/FantasyPros_2025_Dynasty_OP_Rankings.csv")
pff_ranks = pd.read_csv("data/pff_ranks.csv")
roto_ranks = pd.read_csv("data/rotoballers.csv")

# Keep relevant columns
fantasypros = fantasypros[["RK", "TIERS", "PLAYER NAME", "AGE", "POS", "TEAM", "ECR VS. ADP"]]
pff_ranks = pff_ranks[["Rank", "Player", "Team"]]
roto_ranks = roto_ranks[["Rank", "Player Name"]]

# Cleaning function for fuzzy match (does not remove suffixes for display)
def clean_for_match(name):
    if pd.isna(name):
        return ""
    name = name.replace(".", "")
    return re.sub(r"\s+", " ", name).strip()

# Keep original names
fantasypros["Original Player"] = fantasypros["PLAYER NAME"]
roto_ranks["Original Player"] = roto_ranks["Player Name"]
pff_ranks["Original Player"] = pff_ranks["Player"]

# Create cleaned versions
fantasypros["Clean Name"] = fantasypros["PLAYER NAME"].apply(clean_for_match)
roto_ranks["Clean Name"] = roto_ranks["Player Name"].apply(clean_for_match)
pff_ranks["Clean Name"] = pff_ranks["Player"].apply(clean_for_match)

def initials_match(abbrev, choices):
    abbrev_parts = abbrev.split()
    if len(abbrev_parts) != 2:
        return None
    first_initial = abbrev_parts[0][0].upper()
    last_name = abbrev_parts[1].lower()

    for choice in choices:
        choice_parts = choice.split()
        if len(choice_parts) == 2:
            first_name, choice_last = choice_parts
            if first_name[0].upper() == first_initial and choice_last.lower() == last_name:
                return choice
    return None


def match_unique_no_team(abbrev_list, choices, score_cutoff=75):
    matched = []
    available = set(choices)

    for name in abbrev_list:
        if not available:
            matched.append(None)
            continue

        # Exact match
        if name in available:
            matched.append(name)
            available.remove(name)
            continue

        # Fuzzy match
        match = process.extractOne(name, list(available), scorer=fuzz.token_sort_ratio, score_cutoff=score_cutoff)
        if match:
            best_name = match[0]
            matched.append(best_name)
            available.remove(best_name)
        else:
            matched.append(None)
    return matched


def match_unique_with_team(abbrev_df, choices_df, score_cutoff=75):
    matched = []
    available = set(choices_df["Clean Name"].tolist())

    for _, row in abbrev_df.iterrows():
        name = row["Clean Name"]
        team = row["Team"]

        if not available:
            matched.append(None)
            continue

        # Filter candidates by team first
        team_choices = [
            cn for cn, tm in zip(choices_df["Clean Name"], choices_df["Team"])
            if tm == team and cn in available
        ]

        # Try exact match within team
        if name in team_choices:
            matched.append(name)
            available.remove(name)
            continue

        # Try initials match within team
        init_match = initials_match(name, team_choices)
        if init_match:
            matched.append(init_match)
            available.remove(init_match)
            continue

        # Fuzzy match within team first
        if team_choices:
            match = process.extractOne(name, team_choices, scorer=fuzz.token_sort_ratio, score_cutoff=score_cutoff)
            if match:
                best_name = match[0]
                matched.append(best_name)
                available.remove(best_name)
                continue

        # If no team match found, expand to all remaining
        match = process.extractOne(name, list(available), scorer=fuzz.token_sort_ratio, score_cutoff=score_cutoff)
        if match:
            best_name = match[0]
            matched.append(best_name)
            available.remove(best_name)
        else:
            matched.append(None)

    return matched

roto_ranks["Matched Clean"] = match_unique_no_team(
    roto_ranks["Clean Name"].tolist(),
    fantasypros["Clean Name"].tolist()
)

fantasypros["Team"] = fantasypros['TEAM']
pff_ranks["Matched Clean"] = match_unique_with_team(
    pff_ranks[["Clean Name", "Team"]],
    fantasypros[["Clean Name", "Team"]]
)

merged = pd.merge(
    fantasypros, roto_ranks,
    left_on="Clean Name", right_on="Matched Clean",
    how="outer", suffixes=("_FP", "_Roto")
)

merged = pd.merge(
    merged, pff_ranks,
    left_on="Clean Name_FP", right_on="Matched Clean",
    how="outer", suffixes=("", "_PFF")
)

final_df = merged[[
    "Original Player_FP",  # FantasyPros
    "Original Player_Roto",  # RotoBaller
    "Original Player",  # PFF
    "POS",
    "AGE",
    "TIERS",
    "RK",
    "Rank",
    "Rank_PFF"
]]

# print(final_df[final_df["Original Player"].notna()].head(15))


# Make sure all ranks are numeric
final_df["RK"] = pd.to_numeric(final_df["RK"], errors="coerce")
final_df["Rank"] = pd.to_numeric(final_df["Rank"], errors="coerce")
final_df["Rank_PFF"] = pd.to_numeric(final_df["Rank_PFF"], errors="coerce")

# Calculate composite rank as average of available ranks
final_df["Composite Rank"] = final_df[["RK", "Rank", "Rank_PFF"]].mean(axis=1, skipna=True).round(2)

# Optional: sort by composite rank
final_df = final_df.sort_values("Composite Rank")

print(final_df[["Original Player_FP", "TIERS", "RK", "Rank", "Rank_PFF", "Composite Rank"]].head(20))

final_df[["Original Player_FP", "POS", "AGE", "TIERS", "RK", "Rank", "Rank_PFF", "Composite Rank"]].to_csv('data/output.csv')