from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://analytics.usa.gov').content
soup = BeautifulSoup(r, "lxml")


# print(soup.prettify()[:1000])

for link in soup.find_all('a', attrs={'href':re.compile("^http")}):
    print(link.get('href'))