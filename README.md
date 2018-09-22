# general_scrapper

Prerequisites:
1. Python packages: selenium, bs4 (beautifulsoup)
2. Google Chrome Browser
3. Chrome Driver: https://chromedriver.storage.googleapis.com/index.html?path=2.42/

For dynamic scrapping, the script scrapper_chrome.py opens up the webpage to be scrapped using selenium, scroll down automatically to the bottom of the page until no fresh data is received, and thus extracts the html source. This source code is further parsed using BeautifulSoup library to obtain the list of all the tv shows which are embedded with class "fallback-text"

For static scrapping, the first step is to obtain the html source code of the webpage to be scrapped. This source code is saved locally and then selected through script scrapper_html_file.py. The class to be extracted is replaced and thus script gives the desired output.
