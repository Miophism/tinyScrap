import os
from dotenv import load_dotenv 
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
# options.add_argument("--headless")  # o probá sin esto si no querés modo invisible
print("Inicializando Chrome...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
print("Chrome iniciado correctamente ✅")


def scrolling():
    # Localiza el contenedor principal de las invitaciones
    scrollable_div = driver.find_element(By.CSS_SELECTOR, "div.scaffold-finite-scroll__content")

    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)

    while True:
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable_div)
        time.sleep(2)  # da tiempo a que cargue el nuevo bloque
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        if new_height == last_height:
            break
        last_height = new_height

try:
    load_dotenv()
    # 1️⃣ Ir a la página del formulario
    url = "https://www.linkedin.com/uas/login?fromSignIn=true&session_redirect=%2Fflagship-web%2Fmynetwork%2Finvitation-manager%2Fsent%2F"  # ejemplo educativo
    driver.get(url)

    email= str (os.getenv("EMAIL"))
    pss= str(os.getenv("PSSMAIL"))

    # (Simulamos un formulario real, para tu proyecto reemplazá los selectores)
    time.sleep(10)  # dejar que cargue JS

    # 2️⃣ Escribir en los campos
    username = driver.find_element(By.ID, "username")  # id del campo
    username.clear()
    username.send_keys(email)

    password= driver.find_element(By.ID , "password")
    password.clear()
    password.send_keys(pss)
    # 3️⃣ Enviar formulario (Enter o clic)
    password.send_keys(Keys.RETURN)

    # 4️⃣ Esperar la respuesta de la página
    time.sleep(2)

    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
    time.sleep(10)    
    scrolling()  # 👈 ahora sí cargará todo el contenido
    time.sleep(5)
    html = driver.page_source
    

    # 6️⃣ Analizar con BeautifulSoup (por ejemplo, leer el texto resultante)
    soup = BeautifulSoup(html, "html.parser")    
    
    
    users = soup.find_all("div", class_="affedcf8 dff55e42 b83627a1 _243b3958 _8d73c5ce c894219c _4abd70fa _6c32936c e9a74028 d130d62c _95a301cd _5cab6891")
    print("👥 Invitaciones enviadas:\n")
    for i, user in enumerate(users, start=1):
        userName= user.find("p", class_="_05455670 b9d7a024 def86ac1 faa18d37 _82181d3d d5661784 faca1a7a bbb43258 _1439b421 _1c964261").get_text()
        invState= user.find("button").get_text()
        if invState == "Retirar":
            print("-------------- \n") 
            print(f"{i}. {userName}. \n Estado de solicitud de red: Pendiente" )
            print("-------------- \n") 
finally:
    driver.quit()
