from extract_data_webLinks import ExtractDataWebLinks
#from ExtractDataLinks import DownloadDataLink


pagina = ExtractDataWebLinks("https://datos.gob.mx/busca/dataset/informacion-estadistica-de-invenciones-signos-distintivos-y-proteccion-a-la-propiedad-intelectu")
print("Los links extraidos son:")
links = pagina.iniciarExtracciónLinks()
print(links[0])  
#dataDownload = DownloadDataLink(links[0])
#dataDownload.startExtraction()
