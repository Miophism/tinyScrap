## menu con los tags de la pagina para retornar todas las frases de cierto tag
import requests 
from bs4 import BeautifulSoup

URLBASE = "https://quotes.toscrape.com"
page = requests.get(URLBASE)

# cantPag= input("¿De cuantas paginas queres la informacion?")
# cant= int(cantPag)

# print(f"{cant}")


soup= BeautifulSoup(page.content, "html.parser")

listTags= soup.find_all("div", class_="tags-box")

contador= 0
tags_objs = []  

for tag_box in listTags:
    tags= tag_box.find_all("span", class_="tag-item")
    for tag in tags:
        tag_text= tag.get_text().strip()
        contador+=1
        tags_objs.append({  
        "Tag disponible": tag_text,
        "N°": contador
        })
        print(f'{contador} {tag_text}')



condicion = int(input("Ingrese el número del tag mediante su id: "))
encontrado= None
for tag in tags_objs:
    if tag["N°"] == condicion :
        encontrado= tag
        break


if encontrado:
    print(f" Tag seleccionado: {encontrado['Tag disponible']}")
else:
    print(" No está disponible el tag")