# TAREA 3
import pandas as pd

archivo_csv = r"/Users/evelyncarrascoalcaide/Desktop/Mini proyecto SEM3/proyecto_ventas_V3/ventas_productos.csv"
#Subimos el archivo CSV guardado en el área local
df = pd.read_csv(archivo_csv, sep=";")

#Para ver las primeras 5 filas
print(df.head())
