import requests
from bs4 import BeautifulSoup

contPages= 1
URLBASE = "https://quotes.toscrape.com/page/"

while contPages <= 6:
    url_complete= f"{URLBASE}{contPages}"
    page = requests.get(url_complete)
    soup = BeautifulSoup(page.content, "html.parser")
    listArticles= soup.find_all("div", class_="quote")
    print(len(listArticles))

    for q in listArticles:
        text= q.find("span", class_="text").get_text()
        author= q.find("small", class_="author" ).get_text()
        tags= q.find("div", class_="tags").get_text()
        print(f"{text}, {author}, {tags}\n")
    contPages+=1




#retorno de articulos mediante un contador de paginas 