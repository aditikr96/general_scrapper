from selenium import webdriver
from bs4 import BeautifulSoup
import time

PROFILE_PATH = "C:/Users/abc/AppData/Local/Google/Chrome"
EXECUTABLE_PATH = "C:/Program Files (x86)/Google/Chrome/Application"
DRIVER_PATH = "C:/Users/abc/Desktop/chromedriver.exe"

#Google Chrome initialization
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + PROFILE_PATH)
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

#Loading required website and extracting the html source
url="https://www.netflix.com/browse/genre/83?so=az"
driver.get(url)

#Scroll to the bottom of the webpage automatically in order to get the complete html source
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True
html_source = driver.page_source

#Creating soup object
soup = BeautifulSoup(html_source, "lxml")

#Extracting the required class
temp = soup.findAll("div", {"class":"fallback-text"})

#Parsing the data 
final_chat = []
for i, d in enumerate(temp):
    try:
        y = str(d)
        temp2 = (y.split('fallback-text">')[1]).split('</div>')[0]
        final_chat.insert(i, temp2)
    except:
        print("exception at line", i)

#Saving the output
f2 = open(r"C:\Users\abc\Desktop\scrapper\netflix_tv_shows(chrome).txt","w")        
for d in final_chat:
    f2.write(str(d)+'\n')
    
f2.close()


