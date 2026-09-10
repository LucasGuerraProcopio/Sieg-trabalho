from time import * 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#entrar no site do login
driver= webdriver.Chrome()
driver.get("https://talkabit-z3eg.onrender.com/app/login")

campo_login_id = driver.find_element(By.ID,"teamToken")
campo_login_id.send_keys("MATRIX-KXGM6")

campo_login_id = driver.find_element(By.ID,"password")
campo_login_id.send_keys("talkabit")

botao = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
botao.click()

try: 
    linhas = driver.find_elements(By.CSS_SELECTOR, "#resultados table tbody tr")
except:
    try:
        linhas = driver.find_elements(By.CSS_SELECTOR, "#resultados table tbody li")
    except:
        try:
            linhas = driver.find_elements(By.CSS_SELECTOR, "#resultados table tbody tl")
        except:
            print('Erro 404')

for linha in linhas:

    dados = linha.find_elements(By.TAG_NAME, "td")

    status = linha.find_element(By.CSS_SELECTOR, ".badge").text

    if status == 'Autorizada':
        link = linha.find_element(By.CSS_SELECTOR, "a")
        link.click()
        infos = driver.find_elements(By.CSS_SELECTOR, "#card table tbody tr")

        chave = infos[1]
        chave = chave.find_element(By.CSS_SELECTOR, "td[data-chave]")

        valor = infos[5]
        valor = valor.find_element(By.CSS_SELECTOR, "td")