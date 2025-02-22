# TAREA 3
import pandas as pd

archivo_csv = r"/Users/evelyncarrascoalcaide/Desktop/Mini proyecto SEM3/proyecto_ventas_V3/ventas_productos.csv"
#Subimos el archivo CSV guardado en el área local
df = pd.read_csv(archivo_csv, sep=";")

#Para ver las primeras 5 filas
print(df.head())

df['Precio_Total'] = df['Cantidad'] * df['Precio']
print(df)
#Creación de columna precio total

import matplotlib.pyplot as plt
#Incoporación de matplotlib
plt.bar(df['Producto'], df['Precio_Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')
plt.savefig('grafico_precios.png')  # Guardar el gráfico en formato PNG
plt.show()