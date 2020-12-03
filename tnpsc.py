import re
import urllib
import requests
from bs4 import BeautifulSoup

URL = 'http://www.tnpsc.gov.in/answerkeys.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

for data in soup.find_all('td'):
    if data.find('a') != None:
        result = data.find('a').get_text().strip()
        # print(result)
        # txt = "The rain in Spain"
        x = re.search("2019", result)
        if x != None:
            final_url = "http://www.tnpsc.gov.in" + data.find('a')['href']
            print(final_url)
            # r = requests.get(final_url, stream=True)
            # print(r)
            with open('outfile.txt', 'wb') as outfile:
                outfile.write(final_url)
