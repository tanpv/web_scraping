const puppeteer = require('puppeteer');

async function findByLink(page, linkString) {
    const links = await page.$$('a')
    for (var i=0; i < links.length; i++) {
      let valueHandle = await links[i].getProperty('innerText');
      let linkText = await valueHandle.jsonValue();
      const text = getText(linkText);
      if (linkString == text) {
        console.log(linkString);
        console.log(text);
        console.log("Found");
        return links[i];
      }
    }
    return null;
}

(async () => {
    const browser = await puppeteer.launch({
                                            headless:false,
                                            args: ['--disable-notifications', '--start-maximized']
                                           });
    const page = await browser.newPage();
    await page.goto('https://facebook.com');
    await page.click('input[type="submit"]');
    await page.waitForNavigation();
    
    await page.waitForSelector('input[type="text"]', {visible: true});
    await page.type('input[type="text"]', 'python programming');
    await page.type('input[type="text"]', String.fromCharCode(13))
})()