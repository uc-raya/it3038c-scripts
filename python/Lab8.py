import requests
import re
from bs4 import BeautifulSoup

data = requests.get(
    "https://www.radioshack.com/collections/featured-products/products/quantum-starter-component-kit").content
soup = BeautifulSoup(data, "html.parser")
span = soup.find("h1")
title = span.text

span = soup.find("p", {"class": "price_range"})
price = span.text

span = soup.find("span", {"class": "vendor_wrapper"})
vendor = span.text

print("The Product: %s is from the following %s with a price of %s." % (title, vendor, price))