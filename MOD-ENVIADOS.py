from tkinter import BROWSE
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    # Abre uma nova guia
    pagina = navegador.new_page()

    # Acessa a pagina
    pagina.goto("https:site.com.br/")
    # Seleciona o campo do email
    pagina.locator('xpath=//*[@id="user"]').click()
    # Insere o email
    pagina.fill('xpath=//*[@id="user"]', "email")
    # Seleciona o campo de senha
    pagina.locator('xpath=//*[@id="pass"]').click()
    # Insere a senha
    pagina.fill('xpath=//*[@id="pass"]', "senha")
    # Clica em entrar
    pagina.locator('xpath=//*[@id="login_submit"]').click() 
    time.sleep(5)
    # Clica em enviados
    pagina.locator('xpath=//*[@id="rcmliSU5CT1guU2VudA"]/a').click() 
    time.sleep(2)
    # Clica na seta
    pagina.locator('xpath=//*[@id="rcmbtn138"]').click() 
    time.sleep(1)

    # Processo de mover emails

    #Clica no email
    pagina.click("td[class='subject']")
    # Seleciona todos emails
    pagina.locator("tr[class='message selected focused']").press('Control+A') 
    time.sleep(2)
    # Clica em opções
    pagina.locator('xpath=//*[@id="messagemenulink"]').click() 
    time.sleep(1)
    # Seleciona mover
    pagina.locator('xpath=//*[@id="rcmbtn128"]/span').click() 
    time.sleep(0.5)
    # Escolhe pasta
    pagina.locator('xpath=//*[@id="folder-selector"]/ul/li[7]/a/span').click() 
    time.sleep(5)

# ====================================================================================== #
