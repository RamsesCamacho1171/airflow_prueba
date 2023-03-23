from webSbraping.ExtractWebScraping import ExtractWebScrapping
from webSbraping.TransformWebScraping import TransformWebScraping

prueba = ExtractWebScrapping("https://sie.energia.gob.mx/bdiController.do?action=cuadro&cvecua=IE11C01")
data = prueba.getDataWeb()
print(data[1])
