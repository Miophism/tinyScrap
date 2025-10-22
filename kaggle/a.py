import pandas as pd
dataProducts =  pd.read_csv("gymshark_products.csv")


# print (dataProducts)
#Trae  las primeras y las últimas 5 filas 
# print (dataProducts.head(10))

#Quiero ver las primeras 8 filas de un pandas DataFrame
# print (dataProducts.tail(8))

#Para evr los tipos de columnas 
# print(dataProducts.dtypes)

#Conversion de cvs a excel
# dataProducts.to_excel("titanic.xlsx", sheet_name="passengers", index=False)


#resumen tcnico del archivo
# dataProducts.info()

#Instalcion de depenencia 
# pip install openpyxl


# Seleccion especifica de un datarfame 
# print(type(dataProducts["tags"]))
# pandas.core.series.Series

#seleccion de varias columns 
# dataBasic= dataProducts[["title","product_type"]]
# print(dataBasic.head())

#ver el tipo de datos de varias olumnas

# print(type(dataProducts[["title", "product_type"]]))

dataProducts[["tile", "product_type"]].shape