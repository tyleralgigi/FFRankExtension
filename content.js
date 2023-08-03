// content.js

// Function to modify the background color of all paragraph elements
function modifyParagraphBackground() {

    const innerScrollContainer =  document.querySelectorAll('div[class*="player-rank-item2"]');
    console.log("test");
    console.log(innerScrollContainer.length);

    innerScrollContainer.forEach((child , index)=>{
      var divElement = document.createElement("div");
      var spanElement = document.createElement("span");
      spanElement.textContent = "test";
      spanElement.className = "value"
      divElement.appendChild(spanElement);
      divElement.className = "adp col-sml stat-cell new";

      const targetElement = child.querySelector('.adp.col-sml.stat-cell')
      var myElem = child.querySelector('.adp.col-sml.stat-cell.new');
      if (myElem === null){
        targetElement.parentNode.insertBefore(divElement, targetElement);
      }
      
    })
    
  }
  

function contentChanged() {
  modifyParagraphBackground()
}

window.addEventListener('scroll', function(){ 
  contentChanged();
}, true);
