from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Configure o Selenium para usar o Chrome WebDriver
driver = webdriver.Chrome()

# Acesse a URL usando Selenium
url = "https://openai.com/blog"
driver.get(url)

# Aguarde alguns segundos para garantir que o conteúdo seja carregado
time.sleep(3)

# Obtenha o HTML da página
page_source = driver.page_source

# Parse o HTML com BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Encontre todos os títulos
header_titles = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
for header in header_titles:
    print(header.text.strip())

# Feche o navegador
driver.quit()
