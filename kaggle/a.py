import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = ""

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "ahrnishpdahal/gymshark-products-dataset",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())


#para ver la estructura de los datos
import pandas as pd

df = pd.read_csv("gymshark_products.csv")
print(df.head())  # primeras filas
print(df.columns)  # nombres de columnas



# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv("gymshark_products.csv")

# # Tipos de productos
# plt.figure(figsize=(8,5))
# df['product_type'].value_counts().plot(kind='bar', color='skyblue')
# plt.title("Cantidad de productos por tipo")
# plt.xlabel("Tipo de producto")
# plt.ylabel("Cantidad")
# plt.show()

# # Distribución de precios
# plt.figure(figsize=(7,5))
# sns.histplot(df['price'], bins=20, kde=True)
# plt.title("Distribución de precios")
# plt.show()



# avg_price = df.groupby('product_type')['price'].mean().sort_values(ascending=False)

# plt.figure(figsize=(8,5))
# avg_price.plot(kind='bar', color='coral')
# plt.title("Precio promedio por tipo de producto")
# plt.ylabel("Precio promedio ($)")
# plt.xlabel("Tipo de producto")
# plt.show()


# top_10 = df[['title', 'price']].sort_values(by='price', ascending=False).head(10)
# plt.figure(figsize=(10,5))
# sns.barplot(x='price', y='title', data=top_10, palette='viridis')
# plt.title("Top 10 productos más caros")
# plt.xlabel("Precio ($)")
# plt.ylabel("Producto")
# plt.show()

