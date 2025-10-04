import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/page/1/"
page = requests.get(URL)





soup = BeautifulSoup(page.content, "html.parser")

listArticles= soup.find_all("div", class_="quote")


for q in listArticles:
    text= q.find("span", class_="text").get_text()
    author= q.find("small", class_="author" ).get_text()
    tags= q.find("div", class_="tags").get_text()
    print(f"{text}, {author}, {tags}\n")


#primer contacto con beutiful 