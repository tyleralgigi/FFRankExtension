// content.js
var data = [];

function loadDataFromSettings(site, fantasyStyle, type) {
  console.log(`${site}_${fantasyStyle}_${type}.json`);
  const dataFile = `${site}_${fantasyStyle}_${type}.json`;
  console.log("Loading data file:", dataFile);

  fetch(chrome.runtime.getURL(`data/${dataFile}`))
    .then(res => res.json())
    .then(newData => {
      window.playerData = newData;
      console.log(`Loaded data file: ${dataFile}`);
      modifyParagraphBackground();
    })
    .catch(err => console.error('Error loading new data file:', err));
}

// Listen for updates from popup
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'updateSettings') {
    console.log('Received new settings:', message);
    loadDataFromSettings(message.site, message.fantasyStyle, message.type);
  }
});

// Run on first load
chrome.storage.sync.get(['site', 'fantasyStyle', 'type'], (result) => {
  const site = result.site || 'Sleeper';        // default
  const fantasyStyle = result.fantasyStyle || 'ReDraft';
  const type = result.type || 'PPR';

  loadDataFromSettings(site, fantasyStyle, type);
});


// Function to modify the background color of all paragraph elements
function modifyParagraphBackground() {
    const innerScrollContainer = document.querySelectorAll('div[class*="player-rank-item2"]');

    innerScrollContainer.forEach((child, index) => {
        var divElement = document.createElement("div");
        var spanElement = document.createElement("span");
        spanElement.textContent = "test";
        spanElement.className = "value";
        divElement.appendChild(spanElement);
        divElement.className = "adp col-sml stat-cell new";

        var divElement1 = document.createElement("div");
        var spanElement1 = document.createElement("span");
        spanElement1.textContent = "test";
        spanElement1.className = "value";
        divElement1.appendChild(spanElement1);
        divElement1.className = "adp col-sml stat-cell new1";

        const nameWrapper = child.querySelector('.name-wrapper');
        if (!nameWrapper) return;

        const rank = child.querySelector('.rank');
        if (!rank) return;

        let rankInt = parseInt(rank.textContent.trim());
        // const nameOnly = nameWrapper.innerText.trim();
        function normalizeName(name) {
          return name.replace(/\s+/g, ' ').trim();
        }

        const nameOnly = Array.from(nameWrapper.childNodes)
          .filter(node => node.nodeType === Node.TEXT_NODE) // only text, no elements
          .map(node => node.textContent.trim())
          .join(' ')
          .trim();
        var obj = window.playerData.find(o => normalizeName(o.Player) === nameOnly);

        if (!obj) {
            spanElement.textContent = "N/A";
            spanElement1.textContent = "N/A";
            console.log("Sleeper Name:", `"${nameOnly}"`);
            console.log("First 5 JSON Names:", data.slice(0, 5).map(o => `"${o.Player}"`));
        } else {
            const compRank = obj["Composite Rank"];
            const diff = rankInt - compRank;

            spanElement.textContent = compRank.toFixed(2);
            spanElement1.textContent = diff.toFixed(2);

            // --- Color coding ---
            // For Composite Rank: highlight top 20 players
            if (compRank <= 20) {
                spanElement.style.color = "rgb(0, 200, 0)"; // green
            } else  if (compRank <= 50) {
                spanElement.style.color = "rgba(111, 163, 52, 1)"; // yellow
            } else  if (compRank <= 100) {
                spanElement.style.color = "rgb(200, 200, 0)"; // yellow
            } else  if (compRank <= 150) {
                spanElement.style.color = "rgba(214, 143, 37, 1)"; // yellow
            } else  if (compRank <= 250) {
                spanElement.style.color = "rgba(250, 106, 96, 1)"; // yellow
            }else {
                spanElement.style.color = "rgba(248, 51, 51, 1)"; // red
            }

            // For DIFF: green if positive, red if negative
            if (diff <= -10) {
                spanElement1.style.color = "rgb(200, 0, 0)"; // much worse
            } else if (diff <= -5) {
                spanElement1.style.color = "rgba(255, 174, 0, 1)"; // much worse
            } else if (diff >= 5) {
                spanElement1.style.color = "rgba(255, 174, 0, 1)"; // much worse
            } else if (diff >= 10) {
                spanElement1.style.color = "rgb(0, 200, 0)"; // much better
            } else {
                spanElement1.style.color = "rgb(180, 180, 180)"; // neutral
            }
        }

        const targetElement = child.querySelector('.adp.col-sml.stat-cell');
        if (!child.querySelector('.adp.col-sml.stat-cell.new1')) {
            targetElement.parentNode.insertBefore(divElement1, targetElement);
        }
        if (!child.querySelector('.adp.col-sml.stat-cell.new')) {
            targetElement.parentNode.insertBefore(divElement, targetElement);
        }

        const positionDiv = child.querySelector('.position');

        var spanElement2 = document.createElement("span");
        var divElement2 = document.createElement("div");
        spanElement2.className = "teir"
        spanElement2.style = "padding-left: 6px;"
        
        tierColors = {
          1: "rgba(223, 202, 18, 1);",
          2: "rgba(255, 165, 0, 1);",
          3: "rgba(136, 8, 8, 1);",
          4: "rgba(128, 128, 0, 1);",
          5: "rgba(0, 163, 108, 1);",
          6: "rgba(100, 149, 237, 1);",
          7: "rgba(20, 52, 164, 1);",
          8: "rgba(	128, 0, 128, 1);",
          9: "rgba(218, 112, 214, 1);",
          10: "rgba(255, 0, 255, 1);",
          11: "rgba(250, 160, 160, 1);",
          12: "rgba(150, 141, 106, 1);",
          13: "rgba(48, 25, 52, 1);",
          14: "rgba(	2, 48, 32, 1);",
          15: "rgba(	53, 57, 53, 1);",
        }

        divElement2.style = "display: flex; justify-content: center; align-items: center; width: 15px; height: 15px; font-size: 12px; font-weight: 800;border-radius: 2px; background-color:"+ tierColors[obj.TIERS] || "rgba(0, 0, 0, 1);"; // Default to white if no match
        divElement2.textContent = obj.TIERS;
        spanElement2.appendChild(divElement2);


        if (!positionDiv.querySelector('.teir')) {
            positionDiv.appendChild(spanElement2);
        }
    //       content.js:8555 Uncaught NotFoundError: Failed to execute 'insertBefore' on 'Node': The node before which the new node is to be inserted is not a child of this node.
    // at content.js:8555:38
    // at NodeList.forEach (<anonymous>)
    // at modifyParagraphBackground (content.js:8439:26)
    // at contentChanged (content.js:8640:3)
        
    });
}

function modifyHeader(retries = 5, delay = 500) {
  console.log("modifyHeader called");

  // First header row (blank cell)
  const headerRows1 = document.querySelector(
    "#root > div:nth-child(1) > div.draft-layout-container > div.draftboard-page.theme-dark > div.bottom-container > div.bottom-panel-wrapper > div.rankings > div > div.body-container > div.header > div:nth-child(1)"
  );

  if (!headerRows1) {
    console.warn("Header row 1 not found. Retrying...");
    if (retries > 0) {
      setTimeout(() => modifyHeader(retries - 1, delay), delay);
    }
    return;
  }

  // Insert blank header if not already added
  if (!headerRows1.querySelector(".adp.col-sml.new")) {
    const newHeaderBlankCRK = document.createElement("div");
    newHeaderBlankCRK.className = "adp col-sml new"; // C-RK blank

    const newHeaderBlankDiff = document.createElement("div");
    newHeaderBlankDiff.className = "adp col-sml new1"; // DIFF blank

    const referenceNodeBlank = headerRows1.children[2];
    if (referenceNodeBlank) {
      // Insert in correct order: C-RK, then DIFF
      headerRows1.insertBefore(newHeaderBlankDiff, referenceNodeBlank);
      headerRows1.insertBefore(newHeaderBlankCRK, newHeaderBlankDiff);
    } else {
      headerRows1.appendChild(newHeaderBlankCRK);
      headerRows1.appendChild(newHeaderBlankDiff);
    }
    console.log("Blank header added.");
  } else {
    console.log("Blank header already added.");
  }

  const headerRows2 = document.querySelector(
    "#root > div:nth-child(1) > div.draft-layout-container > div.draftboard-page.theme-dark > div.bottom-container > div.bottom-panel-wrapper > div.rankings > div > div.body-container > div.header > div:nth-child(2)"
  );

  if (!headerRows2) {
    console.warn("Header row 2 not found. Retrying...");
    if (retries > 0) {
      setTimeout(() => modifyHeader(retries - 1, delay), delay);
    }
    return;
  }

  if (!headerRows2.querySelector(".adp.col-sml.new")) {
    const newHeaderCRK = document.createElement("div");
    newHeaderCRK.textContent = "DIFF";
    newHeaderCRK.className = "adp col-sml new";

    const newHeaderDiff = document.createElement("div");
    newHeaderDiff.textContent = "C-RK";
    newHeaderDiff.className = "adp col-sml new1";

    const referenceNode = headerRows2.children[2];
    if (referenceNode) {
      // Insert in correct order: C-RK, then DIFF
      headerRows2.insertBefore(newHeaderDiff, referenceNode);
      headerRows2.insertBefore(newHeaderCRK, newHeaderDiff);
    } else {
      headerRows2.appendChild(newHeaderCRK);
      headerRows2.appendChild(newHeaderDiff);
    }
    console.log("Headers successfully added.");
  } else {
    console.log("Headers already added.");
  }
}

function handleSave() {
  console.log("Save button clicked!");
  
}

function contentChanged() {
  modifyParagraphBackground()
};

window.addEventListener('scroll', function(){ 
  contentChanged();
}, true);


window.addEventListener('load', function(){
  modifyHeader();
  contentChanged();
}, true);

window.addEventListener('DOMContentLoaded', () => {
  document.getElementById("saveBtn").addEventListener("click", handleSave);
});
