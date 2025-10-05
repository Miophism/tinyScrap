import requests
from bs4 import BeautifulSoup
import json


URL = "https://quotes.toscrape.com/page/1/"
page = requests.get(URL)

nomber_archivo = "frases.json"

soup = BeautifulSoup(page.content, "html.parser")

listArticles= soup.find_all("div", class_="quote")
nombre_archivo = "datos.json"

datos_json=[]

for q in listArticles:
    text= q.find("span", class_="text").get_text()
    author= q.find("small", class_="author" ).get_text()
    tags= q.find("div", class_="tags").get_text()
    frases_python={
    "Frase":text,
    "Autor":author,
    "Tags":tags
    }
    datos_json.append(frases_python)


with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
    json.dump(datos_json, archivo_json, indent=4,ensure_ascii=False)