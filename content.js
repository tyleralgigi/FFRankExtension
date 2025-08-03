// content.js
const data = [
  {
    "Name": "Justin Jefferson",
    "SleepvFP": "0.00"
  },
  {
    "Name": "Christian McCaffrey",
    "SleepvFP": "-0.33"
  },
  {
    "Name": "Ja'Marr Chase",
    "SleepvFP": "0.50"
  },
  {
    "Name": "Austin Ekeler",
    "SleepvFP": "-0.43"
  },
  {
    "Name": "Travis Kelce",
    "SleepvFP": "-0.17"
  },
  {
    "Name": "Cooper Kupp",
    "SleepvFP": "0.50"
  },
  {
    "Name": "Tyreek Hill",
    "SleepvFP": "0.40"
  },
  {
    "Name": "Bijan Robinson",
    "SleepvFP": "-0.43"
  },
  {
    "Name": "Stefon Diggs",
    "SleepvFP": "0.13"
  },
  {
    "Name": "Saquon Barkley",
    "SleepvFP": "0.00"
  },
  {
    "Name": "Jonathan Taylor",
    "SleepvFP": "-0.31"
  },
  {
    "Name": "CeeDee Lamb",
    "SleepvFP": "0.33"
  },
  {
    "Name": "Patrick Mahomes",
    "SleepvFP": "-0.48"
  },
  {
    "Name": "A.J. Brown",
    "SleepvFP": "0.27"
  },
  {
    "Name": "Davante Adams",
    "SleepvFP": "0.25"
  },
  {
    "Name": "Nick Chubb",
    "SleepvFP": "-0.16"
  },
  {
    "Name": "Amon-Ra St. Brown",
    "SleepvFP": "0.31"
  },
  {
    "Name": "Derrick Henry",
    "SleepvFP": "-0.22"
  },
  {
    "Name": "Garrett Wilson",
    "SleepvFP": "0.27"
  },
  {
    "Name": "Jaylen Waddle",
    "SleepvFP": "0.11"
  },
  {
    "Name": "Josh Jacobs",
    "SleepvFP": "0.05"
  },
  {
    "Name": "Josh Allen",
    "SleepvFP": "-0.21"
  },
  {
    "Name": "Jalen Hurts",
    "SleepvFP": "-0.12"
  },
  {
    "Name": "Tony Pollard",
    "SleepvFP": "0.41"
  },
  {
    "Name": "Mark Andrews",
    "SleepvFP": "-0.14"
  },
  {
    "Name": "Breece Hall",
    "SleepvFP": "-0.19"
  },
  {
    "Name": "Rhamondre Stevenson",
    "SleepvFP": "0.00"
  },
  {
    "Name": "Chris Olave",
    "SleepvFP": "0.33"
  },
  {
    "Name": "Tee Higgins",
    "SleepvFP": "0.21"
  },
  {
    "Name": "Najee Harris",
    "SleepvFP": "-0.09"
  },
  {
    "Name": "DeVonta Smith",
    "SleepvFP": "0.41"
  },
  {
    "Name": "Travis Etienne",
    "SleepvFP": "-0.24"
  },
  {
    "Name": "DK Metcalf",
    "SleepvFP": "0.10"
  },
  {
    "Name": "Joe Burrow",
    "SleepvFP": "-0.15"
  },
  {
    "Name": "Lamar Jackson",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Jahmyr Gibbs",
    "SleepvFP": "-0.16"
  },
  {
    "Name": "Kenneth Walker",
    "SleepvFP": "-0.27"
  },
  {
    "Name": "Deebo Samuel",
    "SleepvFP": "0.06"
  },
  {
    "Name": "Keenan Allen",
    "SleepvFP": "0.26"
  },
  {
    "Name": "Aaron Jones",
    "SleepvFP": "0.14"
  },
  {
    "Name": "T.J. Hockenson",
    "SleepvFP": "-0.23"
  },
  {
    "Name": "Joe Mixon",
    "SleepvFP": "0.11"
  },
  {
    "Name": "Calvin Ridley",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Amari Cooper",
    "SleepvFP": "0.29"
  },
  {
    "Name": "Justin Fields",
    "SleepvFP": "-0.17"
  },
  {
    "Name": "George Kittle",
    "SleepvFP": "-0.23"
  },
  {
    "Name": "DeAndre Hopkins",
    "SleepvFP": "0.07"
  },
  {
    "Name": "Justin Herbert",
    "SleepvFP": "-0.14"
  },
  {
    "Name": "Terry McLaurin",
    "SleepvFP": "0.09"
  },
  {
    "Name": "J.K. Dobbins",
    "SleepvFP": "-0.21"
  },
  {
    "Name": "Dameon Pierce",
    "SleepvFP": "-0.26"
  },
  {
    "Name": "DJ Moore",
    "SleepvFP": "0.11"
  },
  {
    "Name": "Miles Sanders",
    "SleepvFP": "0.02"
  },
  {
    "Name": "Drake London",
    "SleepvFP": "0.32"
  },
  {
    "Name": "Jerry Jeudy",
    "SleepvFP": "0.20"
  },
  {
    "Name": "Christian Watson",
    "SleepvFP": "0.14"
  },
  {
    "Name": "Chris Godwin",
    "SleepvFP": "0.54"
  },
  {
    "Name": "Trevor Lawrence",
    "SleepvFP": "-0.11"
  },
  {
    "Name": "Kyle Pitts",
    "SleepvFP": "-0.19"
  },
  {
    "Name": "D'Andre Swift",
    "SleepvFP": "-0.22"
  },
  {
    "Name": "Alexander Mattison",
    "SleepvFP": "-0.15"
  },
  {
    "Name": "Dalvin Cook",
    "SleepvFP": "-0.47"
  },
  {
    "Name": "Dallas Goedert",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Cam Akers",
    "SleepvFP": "-0.03"
  },
  {
    "Name": "James Conner",
    "SleepvFP": "-0.03"
  },
  {
    "Name": "Michael Pittman",
    "SleepvFP": "0.20"
  },
  {
    "Name": "Darren Waller",
    "SleepvFP": "-0.26"
  },
  {
    "Name": "Marquise Brown",
    "SleepvFP": "0.11"
  },
  {
    "Name": "Brandon Aiyuk",
    "SleepvFP": "0.11"
  },
  {
    "Name": "Mike Williams",
    "SleepvFP": "0.21"
  },
  {
    "Name": "Tyler Lockett",
    "SleepvFP": "0.42"
  },
  {
    "Name": "Rachaad White",
    "SleepvFP": "0.06"
  },
  {
    "Name": "Alvin Kamara",
    "SleepvFP": "-0.14"
  },
  {
    "Name": "Christian Kirk",
    "SleepvFP": "0.30"
  },
  {
    "Name": "Isiah Pacheco",
    "SleepvFP": "-0.09"
  },
  {
    "Name": "Mike Evans",
    "SleepvFP": "0.19"
  },
  {
    "Name": "Javonte Williams",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Diontae Johnson",
    "SleepvFP": "0.32"
  },
  {
    "Name": "Jaxon Smith-Njigba",
    "SleepvFP": "0.04"
  },
  {
    "Name": "David Montgomery",
    "SleepvFP": "-0.01"
  },
  {
    "Name": "George Pickens",
    "SleepvFP": "0.09"
  },
  {
    "Name": "Treylon Burks",
    "SleepvFP": "0.09"
  },
  {
    "Name": "Jordan Addison",
    "SleepvFP": "0.04"
  },
  {
    "Name": "Jahan Dotson",
    "SleepvFP": "0.18"
  },
  {
    "Name": "Pat Freiermuth",
    "SleepvFP": "-0.09"
  },
  {
    "Name": "Dak Prescott",
    "SleepvFP": "-0.05"
  },
  {
    "Name": "Evan Engram",
    "SleepvFP": "-0.08"
  },
  {
    "Name": "James Cook",
    "SleepvFP": "-0.04"
  },
  {
    "Name": "Deshaun Watson",
    "SleepvFP": "0.07"
  },
  {
    "Name": "AJ Dillon",
    "SleepvFP": "-0.12"
  },
  {
    "Name": "Kadarius Toney",
    "SleepvFP": "0.05"
  },
  {
    "Name": "David Njoku",
    "SleepvFP": "-0.16"
  },
  {
    "Name": "Antonio Gibson",
    "SleepvFP": "-0.04"
  },
  {
    "Name": "Brandin Cooks",
    "SleepvFP": "0.12"
  },
  {
    "Name": "Tua Tagovailoa",
    "SleepvFP": "-0.08"
  },
  {
    "Name": "Quentin Johnston",
    "SleepvFP": "0.02"
  },
  {
    "Name": "Michael Thomas",
    "SleepvFP": "-0.04"
  },
  {
    "Name": "JuJu Smith-Schuster",
    "SleepvFP": "0.26"
  },
  {
    "Name": "Brian Robinson",
    "SleepvFP": "-0.01"
  },
  {
    "Name": "Gabe Davis",
    "SleepvFP": "0.14"
  },
  {
    "Name": "Jamaal Williams",
    "SleepvFP": "-0.09"
  },
  {
    "Name": "Rashaad Penny",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Anthony Richardson",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Samaje Perine",
    "SleepvFP": "-0.18"
  },
  {
    "Name": "Zach Charbonnet",
    "SleepvFP": "-0.15"
  },
  {
    "Name": "Zay Flowers",
    "SleepvFP": "0.07"
  },
  {
    "Name": "Dalton Schultz",
    "SleepvFP": "-0.18"
  },
  {
    "Name": "Khalil Herbert",
    "SleepvFP": "-0.08"
  },
  {
    "Name": "Kirk Cousins",
    "SleepvFP": "0.05"
  },
  {
    "Name": "Courtland Sutton",
    "SleepvFP": "0.39"
  },
  {
    "Name": "Rashod Bateman",
    "SleepvFP": "0.13"
  },
  {
    "Name": "Elijah Moore",
    "SleepvFP": "0.07"
  },
  {
    "Name": "Aaron Rodgers",
    "SleepvFP": "-0.08"
  },
  {
    "Name": "De'Von Achane",
    "SleepvFP": "-0.17"
  },
  {
    "Name": "Odell Beckham",
    "SleepvFP": "-0.06"
  },
  {
    "Name": "Jameson Williams",
    "SleepvFP": "-0.03"
  },
  {
    "Name": "Damien Harris",
    "SleepvFP": "0.01"
  },
  {
    "Name": "Chigoziem Okonkwo",
    "SleepvFP": "-0.13"
  },
  {
    "Name": "Cole Kmet",
    "SleepvFP": "-0.17"
  },
  {
    "Name": "Allen Lazard",
    "SleepvFP": "0.13"
  },
  {
    "Name": "Dalton Kincaid",
    "SleepvFP": "-0.27"
  },
  {
    "Name": "Jerick McKinnon",
    "SleepvFP": "0.02"
  },
  {
    "Name": "Geno Smith",
    "SleepvFP": "0.12"
  },
  {
    "Name": "Daniel Jones",
    "SleepvFP": "0.29"
  },
  {
    "Name": "Elijah Mitchell",
    "SleepvFP": "-0.02"
  },
  {
    "Name": "Adam Thielen",
    "SleepvFP": "-0.05"
  },
  {
    "Name": "Jakobi Meyers",
    "SleepvFP": "0.43"
  },
  {
    "Name": "Greg Dulcich",
    "SleepvFP": "-0.03"
  },
  {
    "Name": "Jared Goff",
    "SleepvFP": "0.02"
  },
  {
    "Name": "Tyler Allgeier",
    "SleepvFP": "-0.06"
  },
  {
    "Name": "Rondale Moore",
    "SleepvFP": "0.17"
  },
  {
    "Name": "Tyler Higbee",
    "SleepvFP": "0.01"
  },
  {
    "Name": "Darnell Mooney",
    "SleepvFP": "0.17"
  },
  {
    "Name": "Tyler Boyd",
    "SleepvFP": "0.11"
  },
  {
    "Name": "Russell Wilson",
    "SleepvFP": "0.08"
  },
  {
    "Name": "Devin Singletary",
    "SleepvFP": "-0.01"
  },
  {
    "Name": "Jonathan Mingo",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "D'Onta Foreman",
    "SleepvFP": "-0.11"
  },
  {
    "Name": "Skyy Moore",
    "SleepvFP": "0.08"
  },
  {
    "Name": "Kendre Miller",
    "SleepvFP": "-0.11"
  },
  {
    "Name": "Sam LaPorta",
    "SleepvFP": "-0.19"
  },
  {
    "Name": "Rashee Rice",
    "SleepvFP": "-0.26"
  },
  {
    "Name": "Bryce Young",
    "SleepvFP": "-0.12"
  },
  {
    "Name": "Romeo Doubs",
    "SleepvFP": "0.07"
  },
  {
    "Name": "Gerald Everett",
    "SleepvFP": "-0.04"
  },
  {
    "Name": "Ezekiel Elliott",
    "SleepvFP": "-0.29"
  },
  {
    "Name": "Roschon Johnson",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Kyler Murray",
    "SleepvFP": "-0.18"
  },
  {
    "Name": "Tank Bigsby",
    "SleepvFP": "-0.13"
  },
  {
    "Name": "Raheem Mostert",
    "SleepvFP": "0.01"
  },
  {
    "Name": "Nico Collins",
    "SleepvFP": "0.40"
  },
  {
    "Name": "Zay Jones",
    "SleepvFP": "0.42"
  },
  {
    "Name": "Michael Mayer",
    "SleepvFP": "-0.29"
  },
  {
    "Name": "Jaylen Warren",
    "SleepvFP": "0.11"
  },
  {
    "Name": "Derek Carr",
    "SleepvFP": "0.14"
  },
  {
    "Name": "Michael Gallup",
    "SleepvFP": "0.16"
  },
  {
    "Name": "Jordan Love",
    "SleepvFP": "0.06"
  },
  {
    "Name": "Irv Smith",
    "SleepvFP": "-0.03"
  },
  {
    "Name": "Jeff Wilson",
    "SleepvFP": "0.20"
  },
  {
    "Name": "Juwan Johnson",
    "SleepvFP": "0.07"
  },
  {
    "Name": "Matthew Stafford",
    "SleepvFP": "0.23"
  },
  {
    "Name": "Jalin Hyatt",
    "SleepvFP": "-0.06"
  },
  {
    "Name": "DJ Chark",
    "SleepvFP": "0.31"
  },
  {
    "Name": "Rashid Shaheed",
    "SleepvFP": "0.14"
  },
  {
    "Name": "C.J. Stroud",
    "SleepvFP": "-0.15"
  },
  {
    "Name": "Dawson Knox",
    "SleepvFP": "-0.10"
  },
  {
    "Name": "Jerome Ford",
    "SleepvFP": "-0.04"
  },
  {
    "Name": "Chase Brown",
    "SleepvFP": "-0.13"
  },
  {
    "Name": "K.J. Osborn",
    "SleepvFP": "0.27"
  },
  {
    "Name": "Tyjae Spears",
    "SleepvFP": "-0.13"
  },
  {
    "Name": "Mike Gesicki",
    "SleepvFP": "0.13"
  },
  {
    "Name": "Jayden Reed",
    "SleepvFP": "0.10"
  },
  {
    "Name": "Clyde Edwards-Helaire",
    "SleepvFP": "-0.09"
  },
  {
    "Name": "Kenny Pickett",
    "SleepvFP": "0.19"
  },
  {
    "Name": "John Metchie",
    "SleepvFP": "0.04"
  },
  {
    "Name": "Alec Pierce",
    "SleepvFP": "0.27"
  },
  {
    "Name": "Donovan Peoples-Jones",
    "SleepvFP": "0.36"
  },
  {
    "Name": "Chuba Hubbard",
    "SleepvFP": "0.12"
  },
  {
    "Name": "Leonard Fournette",
    "SleepvFP": "-0.09"
  },
  {
    "Name": "Hunter Renfrow",
    "SleepvFP": "0.31"
  },
  {
    "Name": "Zach Ertz",
    "SleepvFP": "-0.11"
  },
  {
    "Name": "Kareem Hunt",
    "SleepvFP": "-0.11"
  },
  {
    "Name": "Van Jefferson",
    "SleepvFP": "0.12"
  },
  {
    "Name": "Brock Purdy",
    "SleepvFP": "0.05"
  },
  {
    "Name": "Parris Campbell",
    "SleepvFP": "0.15"
  },
  {
    "Name": "Hayden Hurst",
    "SleepvFP": "0.00"
  },
  {
    "Name": "Curtis Samuel",
    "SleepvFP": "0.33"
  },
  {
    "Name": "Wan'Dale Robinson",
    "SleepvFP": "0.24"
  },
  {
    "Name": "Marvin Mims",
    "SleepvFP": "-0.01"
  },
  {
    "Name": "Gus Edwards",
    "SleepvFP": "0.04"
  },
  {
    "Name": "Cordarrelle Patterson",
    "SleepvFP": "0.08"
  },
  {
    "Name": "Isaiah Hodgins",
    "SleepvFP": "0.33"
  },
  {
    "Name": "Trey McBride",
    "SleepvFP": "0.27"
  },
  {
    "Name": "Sam Howell",
    "SleepvFP": "0.13"
  },
  {
    "Name": "Kenneth Gainwell",
    "SleepvFP": "0.41"
  },
  {
    "Name": "Robert Woods",
    "SleepvFP": "0.15"
  },
  {
    "Name": "Marquez Valdes-Scantling",
    "SleepvFP": "0.32"
  },
  {
    "Name": "Josh Downs",
    "SleepvFP": "0.13"
  },
  {
    "Name": "Tim Patrick",
    "SleepvFP": "0.15"
  },
  {
    "Name": "Desmond Ridder",
    "SleepvFP": "0.06"
  },
  {
    "Name": "Chase Claypool",
    "SleepvFP": "0.29"
  },
  {
    "Name": "Pierre Strong",
    "SleepvFP": "0.05"
  },
  {
    "Name": "Mac Jones",
    "SleepvFP": "0.16"
  },
  {
    "Name": "Noah Fant",
    "SleepvFP": "0.14"
  },
  {
    "Name": "Jimmy Garoppolo",
    "SleepvFP": "0.25"
  },
  {
    "Name": "Ryan Tannehill",
    "SleepvFP": "0.29"
  },
  {
    "Name": "Tyquan Thornton",
    "SleepvFP": "0.36"
  },
  {
    "Name": "Khalil Shakir",
    "SleepvFP": "0.18"
  },
  {
    "Name": "Michael Carter",
    "SleepvFP": "0.33"
  },
  {
    "Name": "Darius Slayton",
    "SleepvFP": "0.42"
  },
  {
    "Name": "Mecole Hardman",
    "SleepvFP": "0.34"
  },
  {
    "Name": "Allen Robinson",
    "SleepvFP": "0.29"
  },
  {
    "Name": "DeVante Parker",
    "SleepvFP": "0.45"
  },
  {
    "Name": "Terrace Marshall",
    "SleepvFP": "0.35"
  },
  {
    "Name": "Hunter Henry",
    "SleepvFP": "0.17"
  },
  {
    "Name": "Joshua Kelley",
    "SleepvFP": "0.25"
  },
  {
    "Name": "Joshua Palmer",
    "SleepvFP": "0.55"
  },
  {
    "Name": "Josh Reynolds",
    "SleepvFP": "0.23"
  },
  {
    "Name": "Richie James",
    "SleepvFP": "0.22"
  },
  {
    "Name": "Mack Hollins",
    "SleepvFP": "0.28"
  },
  {
    "Name": "Chase Edmonds",
    "SleepvFP": "0.27"
  },
  {
    "Name": "Corey Davis",
    "SleepvFP": "0.38"
  },
  {
    "Name": "Russell Gage",
    "SleepvFP": "0.40"
  }
];

// Function to modify the background color of all paragraph elements
function modifyParagraphBackground() {

    const innerScrollContainer =  document.querySelectorAll('div[class*="player-rank-item2"]');
    //console.log(innerScrollContainer.length);

    innerScrollContainer.forEach((child , index)=>{
      var divElement = document.createElement("div");
      var spanElement = document.createElement("span");
      spanElement.textContent = "test";
      spanElement.className = "value"

      divElement.appendChild(spanElement);
      divElement.className = "adp col-sml stat-cell new";

      var playerName = child.querySelector('.name-wrapper').textContent;
      var stringArray = playerName.split(/(\s+)/);
      playerName = stringArray[0] + " " + stringArray[2].substring(0, stringArray[2].length-2);
      
      var obj = data.find(o => o.Name === playerName);


      if(obj == undefined){
        spanElement.textContent = "N/A";
        
        
      }else{
        let resultRed = 255;
        let resultGreen = 255;
        let resultBlue = 255;
        
        
        if(obj.SleepvFP == 0.00){
          resultRed = 255;
          resultGreen = 255;
          resultBlue = 255;
        }else if(obj.SleepvFP > 0.000000000001){
          var temp = obj.SleepvFP  * (255);
          resultRed = 200 - temp;
          resultBlue = 200 - temp;
        }else{
          var temp = ((-1) * obj.SleepvFP  * (255));
          resultGreen = 200 - temp;
          resultBlue = 200 - temp;
          
        }

        spanElement.textContent = obj.SleepvFP;
        spanElement.style.color=`rgb(${resultRed},${resultGreen},${resultBlue})`;
        
      }

      const targetElement = child.querySelector('.adp.col-sml.stat-cell')
      var myElem = child.querySelector('.adp.col-sml.stat-cell.new');

      if (myElem === null){
        targetElement.parentNode.insertBefore(divElement, targetElement);
        myElem = child.querySelector('.adp.col-sml.stat-cell.new');
      }
      


    });
    
  }
  
function modifyHeader(retries = 5, delay = 500) {
  console.log("modifyHeader called");

  // First header row (blank cell)
  const headerRows1 = document.querySelector(
    "#root > div:nth-child(1) > div.draft-layout-container > div.draftboard-page.theme-dark > div.bottom-container > div.bottom-panel-wrapper > div.rankings > div > div.body-container > div.header > div:nth-child(1)"
  );

  // Retry if first header row is not found
  if (!headerRows1) {
    console.warn("Header row 1 not found. Retrying...");
    if (retries > 0) {
      setTimeout(() => modifyHeader(retries - 1, delay), delay);
    } else {
      console.error("Header row 1 still not found after retries.");
    }
    return;
  }

  // Insert blank header if not already added
  if (!headerRows1.querySelector(".adp.col-sml.new")) {
    const newHeaderBlank = document.createElement("div");
    newHeaderBlank.className = "adp col-sml new";
    const referenceNodeBlank = headerRows1.children[2];

    if (referenceNodeBlank) {
      headerRows1.insertBefore(newHeaderBlank, referenceNodeBlank);
    } else {
      headerRows1.appendChild(newHeaderBlank);
    }

    console.log("Blank header added.");
  } else {
    console.log("Blank header already added.");
  }

  // Second header row (with vFP text)
  const headerRows2 = document.querySelector(
    "#root > div:nth-child(1) > div.draft-layout-container > div.draftboard-page.theme-dark > div.bottom-container > div.bottom-panel-wrapper > div.rankings > div > div.body-container > div.header > div:nth-child(2)"
  );

  // Retry if second header row is not found
  if (!headerRows2) {
    console.warn("Header row 2 not found. Retrying...");
    if (retries > 0) {
      setTimeout(() => modifyHeader(retries - 1, delay), delay);
    } else {
      console.error("Header row 2 still not found after retries.");
    }
    return;
  }

  // Insert vFP header if not already added
  if (!headerRows2.querySelector(".adp.col-sml.new")) {
    const newHeader = document.createElement("div");
    newHeader.textContent = "vFP";
    newHeader.className = "adp col-sml new";

    const insertAt = 2;
    const referenceNode = headerRows2.children[insertAt];

    if (referenceNode) {
      headerRows2.insertBefore(newHeader, referenceNode);
    } else {
      headerRows2.appendChild(newHeader);
    }

    console.log("vFP header successfully added.");
  } else {
    console.log("vFP header already added.");
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
