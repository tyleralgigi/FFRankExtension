// content.js

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
      

      const targetElement = child.querySelector('.adp.col-sml.stat-cell')
      var myElem = child.querySelector('.adp.col-sml.stat-cell.new');

      if (myElem === null){
        targetElement.parentNode.insertBefore(divElement, targetElement);
        myElem = child.querySelector('.adp.col-sml.stat-cell.new');
      }
      


    });
    
  }
  

function contentChanged() {
  modifyParagraphBackground()
}

window.addEventListener('scroll', function(){ 
  contentChanged();
}, true);


window.addEventListener('load', function(){
  contentChanged();

  const innerScrollContainer =  document.querySelectorAll('div[class="header"]');
  const adpDivs = innerScrollContainer[2].querySelectorAll('.adp.col-sml');
  
  var divHeader = document.createElement("div");
  divHeader.textContent = "vFP";
  divHeader.className = "adp col-sml new";

  var divHeader1 = document.createElement("div");
  divHeader1.className = "adp col-sml new";

  adpDivs[1].parentNode.insertBefore(divHeader, adpDivs[1]);
  adpDivs[0].parentNode.insertBefore(divHeader1, adpDivs[0]);
}, true);




/*const data = `JFK, 40.63980103, -73.77890015
LAX, 33.94250107, -118.4079971
SEA, 47.44900131, -122.3089981`

const splitByLines = data.split(/\n/)
const splitByCommas = splitByLines.map(arr => arr.split(','))

const output = {}
splitByCommas.map(([loc, lat, lon ]) => {
  output[loc] = { lat, lon }
})

console.log(output)
*/