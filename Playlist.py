import bs4 as bs
import urllib.request
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pytube

path='C:\\Users\\Suprakash\\Anaconda3\\chromedriver.exe'
browser=webdriver.Chrome(executable_path=path)


url = "" #Mention the url of the playlist you wish to download

browser.get(url)
pg=browser.page_source

link_list = []
  
soup =BeautifulSoup(pg, 'html.parser')
links=soup.findAll('a',{'id':"video-title"})# Scrap out the videos

for i in links:
	vid_src = i.get('href')
	idx = vid_src.index("&") #The url obtained needs to be sliced to get the exact url
	new_link = "https://www.youtube.com" + vid_src[0:idx]
	link_list.append(new_link) 
       
print(link_list)

for link in link_list: 
    yt = pytube.YouTube(link) # Creates a YouTube object
    
    # The download type is set as progressive and the file extension is mentioned
    # They are put in a descending order according to the resolution and then the first one is chosen from the multiple available streams
    stream = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first() 
    try:
        stream.download()
        # printing the links downloaded
        print("Downloaded: ", link) 
    except:
        print('Some error in downloading: ', link)

print("Done")