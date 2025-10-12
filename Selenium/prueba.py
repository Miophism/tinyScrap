from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Espera explícita a que el input de email sea visible y habilitado
email_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.NAME, "no_type"))
)

# Limpiar el input y escribir
email_input.clear()
email_input.send_keys("admin@localhost.dev")

# Si quisieras hacer clic en algún checkbox:
check_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.NAME, "checkbox_input"))
)
check_input.click()

# Mantener navegador abierto
input("Presiona Enter para cerrar...")

driver.quit()
