from playwright.sync_api import sync_playwright
import os
import  time 
from dotenv import load_dotenv 
from playwright.sync_api import sync_playwright

load_dotenv()

with sync_playwright() as p: 
    browser = p.chromium.launch(headless=True)  # headless=False para ver el navegador
    page = browser.new_page()
    page.goto("https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")  # URL de la página
    email = str(os.getenv("EMAIL"))
    pss = str(os.getenv("PSSMAIL"))



    page.fill("#username", email)
    page.fill("#password", pss)

        # Click en el botón de login
    page.click('button[type="submit"]')


    page.goto("https://www.linkedin.com/search/results/people/?keywords=%22Analista%20de%20datos%20%22&origin=SWITCH_SEARCH_VERTICAL&sid=LsN")

    lista= page.locator("ul")

    for i in range(lista.count()):
        i= page.locator("li p")
        print (f"{i}")

    # browser.close()



