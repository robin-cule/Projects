## Importing the libraries
from bs4 import BeautifulSoup
import requests
import re


## Loading the page and parsing 
url= "https://www.tigerdirect.com/applications/SearchTools/item-details.asp?EdpNo=1501390"
user_agent = {'User-Agent':"Mozilla/5.0"}
page = requests.get(url, headers = user_agent)
soup = BeautifulSoup(page.text,'lxml')


## Storing the list price 
list_prices = soup.select('div.pdp-price p.list-price span.sr-only')
str1 = []
for i in list_prices:
    str1.append(i.text)
    
list_price = str1[0]
list_price 


## Storing the sale price 
sale_prices = soup.select('div.pdp-price p.final-price span.sr-only')
str2 = []
for i in sale_prices:
    str2.append(i.text)

sale_price = str2[0]


## Using the regex to clean the list price and sale price string
list_price_new = re.sub("(?s).([0-9]),([0-9]{3}).*([0-9]{2}).*",r"\1\2.\3",list_price_new)
list_price_new

sale_price_new = re.sub("(?s).([0-9]),([0-9]{3}).*([0-9]{2}).*",r"\1\2.\3",sale_price_new)
sale_price_new


# Printing the list price and sale price
print(list_price_new, sale_price_new,sep = "\n")




