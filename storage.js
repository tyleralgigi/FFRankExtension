/*const PAGES_KEY = 'pages';

class PageService {

    static getPages = () => {
        return toPromise((resolve, reject) => {
            chrome.storage.local.get([PAGES_KEY], (result) => {
                if (chrome.runtime.lastError)
                    reject(chrome.runtime.lastError);

                const researches = result.pages ?? [];
                resolve(researches);
            });
        });
    }

    static savePage = async (title, url) => {
        const pages = await this.getPages();
        const updatedPages = [...pages, { title, url }];

        return toPromise((resolve, reject) => {

            chrome.storage.local.set({ [PAGES_KEY]: updatedPages }, () => {           
                if (chrome.runtime.lastError)
                    reject(chrome.runtime.lastError);
                resolve(updatedPages);
            });
        });
    }

    static clearPages = () => {
        return toPromise((resolve, reject) => {
            chrome.storage.local.remove([PAGES_KEY], () => {
                if (chrome.runtime.lastError)
                    reject(chrome.runtime.lastError);
                resolve();
            });
        });
    }
}*/

const SETTING_KEY = 'settings';


document.getElementById("siteBtn").addEventListener("click", SaveSettings.savePage);

class SaveSettings {

    static savePage = () => {
        let checkedValue = document.querySelector('input[name="siteBtn"]:checked').value;
        console.log(checkedValue);
        /*const updatedPages = [...pages, { title, url }];

        return toPromise((resolve, reject) => {

            chrome.storage.local.set({ [PAGES_KEY]: updatedPages }, () => {           
                if (chrome.runtime.lastError)
                    reject(chrome.runtime.lastError);
                resolve(updatedPages);
            });
        });*/
    }

}
