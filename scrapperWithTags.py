import requests
from bs4 import BeautifulSoup

#objetivo, recuperar  las quotes mediante el tag y recuperar tambien las de las demas paginas


URLBASE = "https://quotes.toscrape.com"
page = requests.get(URLBASE)
numberPage= 1

soup = BeautifulSoup(page.content, "html.parser")

listTags= soup.find_all("div", class_="tags-box")

for tag_box in listTags:
    tags= tag_box.find_all("span", class_="tag-item")
    for tag in tags:
        tag_text= tag.get_text()
        urlWithTags= f"{URLBASE}/tag/{tag_text}/page/{numberPage}"
        # print(f"{urlWithTags}\n")

        pageTag= requests.get(urlWithTags)
        soupTag= BeautifulSoup(pageTag.content, "html.parser")
        listQuotes= soup.find_all("div", class_="quote")
        for q in listQuotes:
            text= q.find("span", class_="text").get_text()
            author= q.find("small", class_="author").get_text()
            print(f"{text}-{author}\n")
