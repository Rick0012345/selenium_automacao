from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from exread import *  

def login():
    global navegador
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service = servico, options = chrome_options)
    navegador.get('https://www.instagram.com/')
    sleep(4)
    #FAZER LOGIN NO INSTAGRAM (INSERIR  SEU ID E SENHA) NOS CAMPOS ONDE CONTEM XXXXXXX
    navegador.find_element('xpath','//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("XXXXXX")
    navegador.find_element('xpath','//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("XXXXXXX.")
    navegador.find_element('xpath','//*[@id="loginForm"]/div/div[3]').click()
    #############################################################################################
    sleep(7)
    navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div').click()
    sleep(8)
    navegador.find_element(By.CSS_SELECTOR,'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1').click()


login()

def verificar():
    for index, row in df.iterrows():
        sleep(3)
        navegador.find_element(By.CLASS_NAME,'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1').click()
        sleep(3)
        navegador.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys(f'{df.loc[c,"Seguidores"]}')
        if df.loc[c,'Seguidores'] >= 100:
            df.loc[c, 'verificador'] = "ok"
        c=c+1

verificar()