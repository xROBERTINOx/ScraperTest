# public.com/crypto is the website I am using for crypto prices, I am not using it with an account
import requests
# python -m pip install beautifulsoup4
from bs4 import BeautifulSoup

URL = "https://public.com/crypto/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="page-wrap")
cryptoStats = results.find_all("div", class_="content-wrap")

dictOfTickerToLastPrices = {}
dictOfNameToTicker = {}

# add check for price change of other times (week)
for cryptoStat in cryptoStats:
  lastPrice = cryptoStat.find("span", class_="last-price")
  name = cryptoStat.find("div", class_="name")
  ticker = cryptoStat.find("div", class_="label ticker")
  percent24hChange = cryptoStat.find("span", class_="change-percent")
  dictOfTickerToLastPrices[ticker.text.strip().lower()] = [
    lastPrice.text.strip(),percent24hChange.text.strip()
  ]
  dictOfNameToTicker[name.text.strip().lower()] = ticker.text.strip().lower()

while True:
  userInputNameOfCoin = input(
    "Which coin would you like to see the statistics for?: ").lower()
  if userInputNameOfCoin not in dictOfNameToTicker and userInputNameOfCoin not in dictOfTickerToLastPrices:
    print("That is not a valid coin name")
  elif userInputNameOfCoin not in dictOfTickerToLastPrices:
    ticker = dictOfNameToTicker[userInputNameOfCoin]
    print("The current price of " + userInputNameOfCoin.lower() + " is " + dictOfTickerToLastPrices[ticker][0] + ", and the % change in the last 24 hours is " + dictOfTickerToLastPrices[ticker][1])
  elif userInputNameOfCoin in dictOfTickerToLastPrices:
    print("The current price of " + userInputNameOfCoin.upper() + " is " + dictOfTickerToLastPrices[userInputNameOfCoin][0] + ", and the % change in the last 24 hours is " + dictOfTickerToLastPrices[userInputNameOfCoin][1])
