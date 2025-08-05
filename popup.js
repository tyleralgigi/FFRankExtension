document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('saveBtn').addEventListener('click', () => {
    const site = document.querySelector('input[name="siteBtn"]:checked')?.value;
    const fantasyStyle = document.querySelector('input[name="fantasyStyleBtn"]:checked')?.value;
    const type = document.querySelector('input[name="typeBtn"]:checked')?.value;

    console.log('New settings selected:', { site, fantasyStyle, type });

    // Store settings
    chrome.storage.sync.set({ site, fantasyStyle, type }, () => {
      console.log('Settings saved to Chrome storage');
    });

    // Send to content script so it updates immediately
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, {
        action: 'updateSettings',
        site,
        fantasyStyle,
        type
      });
    });
  });

  // Load stored settings on popup open
  chrome.storage.sync.get(['site', 'fantasyStyle', 'type'], (result) => {
    if (result.site) {
      document.getElementById(`btn${result.site}`)?.click();
    }
    if (result.fantasyStyle) {
      document.getElementById(`btn${result.fantasyStyle}`)?.click();
    }
    if (result.type) {
      document.getElementById(`btn${result.type}`)?.click();
    }
  });
});

// document.getElementById("saveBtn").addEventListener("click", saveSettings);



