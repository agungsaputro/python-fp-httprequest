import requests
from bs4 import BeautifulSoup

urlWeb = "https://indeks.kompas.com/headline"
res = requests.get(urlWeb)
html = BeautifulSoup(res.text, 'html.parser')
div = html.find_all(class_="article__link")

title = [title.text for title in div]
url = [url['href'] for url in div]

for index in range(5):
    result = list({title[index], url[index]})
    print(f"title: {result[1]} \n url: {result[0]} \n")