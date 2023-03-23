import random
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
import unittest
import json

class Prueba(unittest.TestCase):

    def setUp(self):
        opt = Options()
        opt.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
        s=Service(ChromeDriverManager().install())
        self.driver=webdriver.Chrome(service=s,chrome_options=opt)

    #se tiene que llamar test
    def test_buscar(self):
        driver=self.driver
        driver.get("https://sie.energia.gob.mx/bdiController.do?action=cuadro&cvecua=DIPS_SE_C29_ESP")
        elemento=driver.find_element(By.ID,"opciones")
        elemento.click()
        sleep(1)
        selector=driver.find_element(By.ID,"anoini")
        valorIni=selector.find_element(By.XPATH,'.//option[@value="2018"]')
        valorIni.click()
        selector=driver.find_element(By.ID,"anofin")
        valorFin=selector.find_element(By.XPATH,'.//option[@value="2031"]')
        valorFin.click()
        sleep(1)
        boton=driver.find_element(By.XPATH,'//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable"][5]//button[text()="Aceptar"]')
        boton.click()
        sleep(4) 
        tabla=driver.find_element(By.XPATH,'//table[@id="cuadroTable"]')
        filas=tabla.find_elements(By.XPATH,'.//tr[not(@class)]')
        nombres=['descripcion','f2018','f2019','f2020','f2021','f2022','f2023','f2024','f2025','f2026','f2027','f2028','f2029','f2030','f2031']
        registro=[]
        c=0
        for fila in filas:
           nueva_fila={}
           if(c>1 and c<13):
               columnas=fila.find_elements(By.XPATH,'.//td')
               index=0
               for colu in columnas:
                    if(colu.text!=None and colu.text!=''):
                        nueva_fila[nombres[index]]=colu.text
                        index+=1
               registro.append(nueva_fila)
           c+=1
        sleep(1)
        print(registro)
        registro=json.dumps(registro, indent = 0)
        text_file = open("python_data.json", "w")
        text_file.write(registro)
        text_file.close()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

