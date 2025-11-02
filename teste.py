from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from time import sleep
import re


grupoDeContatos = [
    "teste 20/20 SELENIUM tel2 - P1",
    "teste 20/20 SELENIUM tel5 - P1"
]

horas = [
    "21:00",
    "22:30",
]

urlLogin = "https://app.zapresponder.com.br/auth/sign-in"
email = ""
senha = ""
urlAddGrupoDeContatos = "https://app.zapresponder.com.br/dashboard/contact-groups/new"
urlAddCampanha = "https://app.zapresponder.com.br/dashboard/campaigns/new"

temp_CLT1 = 'lembrete_clt'
temp_CLT2 = 'aviso_clt'

google = webdriver.Chrome()

try:
    google.get(urlLogin)
    wait = WebDriverWait(google, 10)
    sleep(5)
    botoes = google.find_elements(By.CLASS_NAME, "chakra-input")
    clickLogin = google.find_element(By.XPATH, "//*[contains(text(), 'Entrar')]")

    botoes[0].send_keys(email)
    botoes[1].send_keys(senha)
    clickLogin.click()
    sleep(2)

    google.get(urlAddGrupoDeContatos)

    for i in range(len(grupoDeContatos)):
        try:
            if i >= 1:
                google.get(urlAddGrupoDeContatos)
            btnText = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "chakra-input")))
            btnText.clear()
            btnText.send_keys(grupoDeContatos[i])

            btnAdd = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Salvar grupo')]")))
            btnAdd.click()
            google.get(urlAddGrupoDeContatos)
            print(f"Grupo '{grupoDeContatos[i]}' criado!")
            

        except StaleElementReferenceException:
            print("Elemento ficou 'stale', recarregando a página e tentando novamente...")


    google.get(urlAddCampanha)

    for i, grupo in enumerate(grupoDeContatos):
        try:
            if i >= 1:
                google.get(urlAddCampanha)

    
            tel_match = re.search(r'(?<=tel)\d+', grupo)
            tel = tel_match.group() if tel_match else ""

            if int(tel) <= 1:
                 tel = ""

            btname = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Disparo em massa']")))
            btname.send_keys(grupo)


            btnDepar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "chakra-react-select__input")))
            btnDepar.click()
            

        
            
            btnTel = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//*[contains(text(), 'Atendimentos {tel}')]")))
            btnTel[0].click()
            print(tel)


            btnGrup = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "chakra-react-select__input")))
            btnGrup[3].send_keys(grupo)
            

            btnGrupin = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//*[contains(text(), '{grupo}')]")))
            btnGrupin[1].click()

            btnProx = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Próximo')]")))
            btnProx.click()
            


            btnTemp = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Criar novo')]")))
            btnTemp.click()
            

            btnChoose = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Template')]")))
            btnChoose.click()
            

            btnInputTemp = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "chakra-react-select__dropdown-indicator")))
            btnInputTemp.click()
            

            selectTemp = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//div[contains(text(), '{temp_CLT1}') or contains(text(), '{temp_CLT2}')]")))
            selectTemp[0].click()

            qlEditor = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ql-editor")))
            if len(qlEditor) >= 2:
                qlEditor[0].send_keys("margem de crédito")
                qlEditor[1].send_keys("crédito")
            else:
                qlEditor[0].send_keys("margem de crédito")

            saveTemp = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="save"]')))
            saveTemp.click()

            ProxEtapa = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Próxima etapa')]")))
            ProxEtapa.click()
            


            agenda = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "chakra-switch__track")))
            agenda[3].click()

            data = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "chakra-input")))
            data.send_keys(Keys.SPACE)
            data.send_keys(Keys.ENTER)
            for t in range(3):
                data.send_keys(Keys.ARROW_RIGHT)

            data.send_keys(horas[i])
            data.send_keys(Keys.ENTER)
            sleep(2)
            
   
            verificar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "chakra-checkbox__control")))
            verificar.click()

            agendarCamp = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Agendar campanha']")))
            agendarCamp.click()
            sleep(2)
            google.get(urlAddCampanha)

        except StaleElementReferenceException:
            print("Elemento ficou 'stale', recarregando a página e tentando novamente...")

finally:
            print("Acabou")
            google.quit()