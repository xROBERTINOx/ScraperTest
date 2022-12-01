import requests
#python -m pip install beautifulsoup4
from bs4 import BeautifulSoup
URL = "https://public.com/crypto/"
page = requests.get(URL)
soup= BeautifulSoup(page.content, "html.parser")
results = soup.find(id="page-wrap")
cryptoStats = results.find_all("div", class_="content-wrap")

#add input from user for which coin and what stats user wants
for cryptoStat in cryptoStats:
  lastPrice = cryptoStat.find("span", class_="last-price")
  name = cryptoStat.find("div", class_="name")
  labelTicker = cryptoStat.find("div", class_="label ticker")
  print("The last price of " + str(name.text.strip()) + "(" + str(labelTicker.text.strip().upper()) + ")" + " is: " + str(lastPrice.text.strip()))
  print()

