import requests
#python -m pip install beautifulsoup4
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

fromUser = int(input("What do you to find by:\n1 title\n2 company\n3 location"))
if fromUser == 1:
  byWhat = "title"
elif fromUser == 2:
  byWhat = "company"
elif fromUser == 3:
  byWhat = "location"
else:
  print("huh?")
  exit()

for job_element in job_elements:
  title_element = job_element.find("h2", class_="title")
  company_element = job_element.find("h3", class_="company")
  location_element = job_element.find("p", class_="location")
  print(title_element.text.strip())
  print(company_element.text.strip())
  print(location_element.text.strip())
  print()

