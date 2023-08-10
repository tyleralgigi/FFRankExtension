let siteValue = "";;
let typeValue = "";


document.addEventListener('DOMContentLoaded', async () => {
    chrome.storage.sync.get([
        'siteValue',
        'typeValue'
    ], function(items) {
        if (!chrome.runtime.error) {
            console.log("btn"+items.siteValue);
            console.log("btn"+items.typeValue);
            document.getElementById("btn"+items.siteValue).checked = true;
            document.getElementById("btn"+items.typeValue).checked = true;
        }else{
            console.log(items);
            document.getElementById("btnSleeper").checked = true;
            document.getElementById("btnPPR").checked = true;
        }
    });
    saveSettings()
});


document.getElementById("saveBtn").addEventListener("click", saveSettings);


function saveSettings(){
    siteValue = document.querySelector('input[name="siteBtn"]:checked').value;
    typeValue = document.querySelector('input[name="typeBtn"]:checked').value;
    console.log(siteValue);
    console.log(typeValue);

    chrome.storage.sync.set({ "siteValue" : siteValue, "typeValue" : typeValue }, function() {
        if (chrome.runtime.error) {
        console.log("Runtime error.");
        }
    });

}

