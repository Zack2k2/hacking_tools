
(() => {
    /**
  * Check and set a global guard variable.
  * If this content script is injected into the same page again,
  * it will do nothing next time.
  */
    if (window.hasRun) {
        return;
    }
    window.hasRun = true;

    /**
     * Ruturns a Array of search links given a CSS selector
     * from the google search page.
     */
    function getSearchedLinks(css_selector) {
        return [...document.querySelectorAll(css_selector)].map(n => n.href);
    }

    /**
    * send a `line` to the localserver at the port `port`
    * by default the port is 8080 
    */
    async function sendLinkToLocalServer(line, port = 65535) {
        const url = 'http://127.0.0.1:'+String(port); // Replace with the URL of your server
        const postData = line; // Data to be sent in the POST request

        await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain',
            },
            body: postData,
        })
            .then(response => response.text())
            .then(data => {
                console.log(`Response from server: ${data}`);
            })
            .catch(error => {
                console.error('Error:', error);
            });

    }
    /**
     * linkset is the set of variables 
     */
    linkset = new Set();
    let scrollTimeout
    document.addEventListener("scroll", (event) =>
    {
        clearTimeout(scrollTimeout);

        scrollTimeout = setTimeout(
            ()=>{
            google_links=getSearchedLinks("div#center_col a");
            console.log(google_links)
                for(let index = 0; index < google_links.length; index++){
                    sendLinkToLocalServer(String(google_links[index]));
                }
            },1000);
    }
    
);
})();
