"""
get links from news websites: a simple web scraper
author: lauren olson
"""


import requests
from bs4 import BeautifulSoup


f = open("breitbart_links.txt", "w")

urls = ["https://www.breitbart.com/tag/joe-biden/", "https://www.breitbart.com/tag/critical-race-theory/", "https://www.breitbart.com/tag/coronavirus/", "https://www.breitbart.com/tag/immigration/", "https://www.breitbart.com/tag/masters-of-the-universe/"]

tally = 0
for url in urls:

	page = requests.get(url)
	i = 2
	
	while(page.status_code == 200):
		soup = BeautifulSoup(page.content, 'html.parser')
	
		for o in soup.find_all("a"):
			link = o.get('href')
			
			if(link != None and link[0] != "#"):
				if(link[0] == "/"):
					link = "https://breitbart.com" + link
				f.write(link + "\n")
				tally += 1

		page = requests.get(url + "page/" + str(i) + "/")
		i += 1

print("you collected " + str(tally) + " links")
f.close()
