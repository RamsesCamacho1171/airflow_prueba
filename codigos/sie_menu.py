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
        driver.get("https://sie.energia.gob.mx/bdiController.do?action=temas")
        sleep(1)
        electricidad=driver.find_element(By.XPATH,'//div[@id="content"]//li[@id="CUADROS"]') 
        elec=electricidad.find_element(By.XPATH,'.//li[@id="LUZ"]/a')
        elec.click()
        sleep(1)
        generacion=electricidad.find_element(By.XPATH,'.//li[@id="IIIA1"]/a')
        generacion.click()
        sleep(1)
        ge_tec=electricidad.find_element(By.XPATH,'.//li[@id="IIIA1C05"]/a')
        ge_tec.click()
        self.extraer_tabla(nombre="ge_bru_tec",ini=-1,fin=17)
        driver.back()
        driver.back()
        electricidad=driver.find_element(By.XPATH,'//div[@id="content"]//li[@id="CUADROS"]') 
        cap_in=electricidad.find_element(By.XPATH,'.//li[@id="IIIA1C04"]/a')
        cap_in.click()
        sleep(1)
        self.extraer_tabla(nombre="cap_in_tec",ini=0, fin=18)
        sleep(2)
       

    def extraer_tabla(self,nombre,ini,fin):
        driver=self.driver
        elemento=driver.find_element(By.ID,"opciones")
        elemento.click()
        sleep(1)
        sel_fe=driver.find_element(By.ID,"periodicidad")
        sel_fe=sel_fe.find_element(By.XPATH,'.//option[@value="12"]')
        sel_fe.click()
        selector=driver.find_element(By.ID,"anoini")
        valorIni=selector.find_element(By.XPATH,'.//option[@value="2002"]')
        valorIni.click()
        selector=driver.find_element(By.ID,"anofin")
        valorFin=selector.find_element(By.XPATH,'.//option[@value="2022"]')
        valorFin.click()
        sleep(1)
        boton=driver.find_element(By.XPATH,'//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable"][5]//button[text()="Aceptar"]')
        boton.click()
        sleep(4) 
        tabla=driver.find_element(By.XPATH,'//table[@id="cuadroTable"]')
        filas=tabla.find_elements(By.XPATH,'.//tr[not(@class)]')
        registro=[]
        c=0
        for fila in filas:
           nueva_fila={}
           if(c>ini and c<fin):
               columnas=fila.find_elements(By.XPATH,'.//td')
               index=-1
               num=2
               for colu in columnas:
                    if(colu.text!=None and colu.text!=''):
                        n="0"+str(num) if num < 9 else num    
                        if(index==-1):
                            nueva_fila["descripcion"]=colu.text
                        else:
                            nueva_fila["f_20"+str(n)]=colu.text
                            num=num+1 
                    index+=1
               #print(nueva_fila)      
               registro.append(nueva_fila)
           c+=1
          
        sleep(1)
        # print(registro)
        registro=json.dumps(registro, indent = 0,ensure_ascii=False)
        text_file = open(str(nombre)+".json", "w")
        text_file.write(registro)
        text_file.close()
    

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

