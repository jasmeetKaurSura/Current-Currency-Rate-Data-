# This code scrape data for currency rate according to 1USD
import pandas as pd
import requests
from bs4 import BeautifulSoup
url="https://www.x-rates.com/table/?from=USD&amount=1"
page=requests.get(url)
content = page.content
soup = BeautifulSoup(content, "lxml")
TimeStamp= soup.find("span" ,{"class":"ratesTimestamp"}).text
print("conversion rate at the time of", TimeStamp)
print('1 USD =')
conversion_id= soup.find_all("td")
Currency=[]
Code=[]
USD=[]
inv=[]
rate=[]
    
for i in conversion_id:
    rate.append(i.text)
# for finding currency codes
    url_part = i.find('a')
    if (url_part != None):
        url_str = url_part.get('href')
        if not (url_str.endswith('USD')):
         Code.append( url_str[-3:])


for i in range(0,len(rate),3): 
    Currency.append(rate[i])
    USD.append(rate[i+1])
    inv.append(rate[i+2])
    

data = {" Currency":  pd.Series(Currency),
        "Code":  pd.Series(Code),
        " USD":  pd.Series(USD),
        "inv": pd.Series(inv)
        }

df = pd.DataFrame(data)
df.drop_duplicates(subset=None, inplace=True)
print(df)
