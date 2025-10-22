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

# #seleccionana una columna especifica 
# titleProductos= dataProducts["price"]
# print(titleProductos)


#Seleccioona varias columnas
# titlePriceProducts= dataProducts[["title", "price", "product_type"]]
# print(titlePriceProducts)

#Retorna el dataType de las columnas seleccionadas
#  dataProducts[["title", "price"]].shape


#Filtrar entre columnas

# Cuenta cuántos productos tienen price <= 35
# products = dataProducts[dataProducts["price"] <= 35]
# print(products.head())


# #fILTRAR CON MAS de una condicion 
# productPrice= dataProducts[(dataProducts["price"] == 28.00) & (dataProducts["product_type"] == "Womens Sleeveless Tops")]
# print(productPrice.head())

#datos de pasajeros por los que se conoce la edad

# product_no_na= dataProducts[dataProducts["inventory_quantity"].notna()]
# # print(product_no_na.head())
# print(product_no_na.shape)  # Muestra el número de filas y columnas



#Seleccion de productos que tengan un precio masyot a 28.00
# productsPrice= dataProducts.loc[dataProducts["price"] > 28.00, "title"]

# print(productsPrice)

# #Seleccion especifica de filas y columnas
# products= dataProducts.iloc[9:25, 2:5]
# print(products)

https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#how-do-i-filter-specific-rows-from-a-dataframe

Ultima pagina en la que me quede