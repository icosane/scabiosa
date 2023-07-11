from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import numpy as np
import re
import cloudscraper
import time

'''
Login into your livechart.me account and go to your list.
Select all or only some of your lists. Press F12 and find script id="library_entries". 
Open it and copy everything into a .txt file. 
If your currently selected list has multiple pages, you should do it for every page. 
Place .txt file and this script into same directory. 
Enter txt name into loadtxt.
Run the script.
After completion you'll find file animelist.txt with all your entries in the same path.
'''


f = np.loadtxt('livechart completed.txt', dtype="str", delimiter="\0").tolist()

num = re.compile(r'(?<=")\d+(?=")')
s = ''.join(str(x) for x in f)
m = num.findall(s)
scraper = cloudscraper.create_scraper(delay=12, browser='chrome')
dd = []

url = "https://www.livechart.me/anime/"

for i in range(len(m)):
	newurl = url + m[i]
	print(newurl)
	info = scraper.get(newurl).text
	soup = bs(info, 'lxml')
	temp = soup.select_one('title').text
	res = re.sub(r'\|.*', "", temp)
	dd.append(res)
	time.sleep(5)
print(dd)


df = pd.DataFrame(dd)
df.to_csv('animelist.txt', index=False, header=None)
