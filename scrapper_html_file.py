from bs4 import BeautifulSoup

#Get HTML Source
file_path = r"C:\Users\Siddharth\Desktop\Whatsapp Chat Scrapper\netflix_tv_shows.html"
f = open(file_path, "r")
html_source = f.read()
f.close()

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

f2 = open(r"C:\Users\Siddharth\Desktop\Whatsapp Chat Scrapper\netflix_tv_shows.txt","w")        
for d in final_chat:
    f2.write(str(d)+'\n')
    
f2.close()

