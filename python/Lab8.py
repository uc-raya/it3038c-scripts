import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'


uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, 'html.parser')


containers = page_soup.findAll('div', {'class':'item-container'})

filename = "products.csv"
f = open(filename, 'w')

headers = "Brands, Product, Shipping cost\n"

f.write(headers)

container = containers[1]

for container in containers:
    brand = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class':'item-title'})
    product_name = title_container[0].text
    ship_container = container.findAll('li', {'class':'price-ship'})
    
    shipping = ship_container[0].text.strip()

    print("Brand is:" + brand)
    print("Product:" + product_name)
    print("Shipping cost:" + shipping)

    f.write(brand + ',' + product_name.replace(',' , '|') + ',' + shipping + '\n')

f.close()