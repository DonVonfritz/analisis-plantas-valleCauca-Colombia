 # Tarea 3 BIG DATA_ UNAD_ERICK FAJARDO
 #CÓDIGO   PYTHON


#Código del Proyecto Plantas en Categoróia de Riesgo

# Importamos librerías necesarias
from pyspark.sql import SparkSession, functions as F

# Inicializa la sesión de Spark
spark = SparkSession.builder.appName('Tarea3').getOrCreate()

# Define la ruta del archivo .csv en tu sistema local
file_path = '/ruta/a/tu/di5n-jaf8.csv'  # Cambia esta ruta según donde esté tu archivo

# Lee el archivo .csv
df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(file_path)

# Imprimimos el esquema
df.printSchema()

# Muestra las primeras filas del DataFrame
df.show()

# Estadísticas básicas
df.summary().show()

# Pregunta 1: Filtrar plantas de una familia específica
print("Plantas de la familia 'Nombre de la familia'\n")
plantas_familia = df.filter(F.col('Familia') == 'Nombre de la familia').select('Nombre científico', 'Nombres comunes', 'Año')
plantas_familia.show()

# Pregunta 2: Contar cuántas especies hay por cada año
print("Número de especies por año\n")
especies_por_año = df.groupBy('Año').count().sort(F.col('Año'))
especies_por_año.show()

# Pregunta 3: Filtrar por amenaza a nivel nacional
print("Plantas amenazadas a nivel nacional\n")
plantas_amenazadas = df.filter(F.col('AMENAZA A NIVEL NACIONAL (Resolución 192 de 2014)') == 'Sí').select('Nombre científico', 'Nombres comunes', 'Familia')
plantas_amenazadas.show()

# Pregunta 4: Contar el número de plantas por familia
print("Número de plantas por familia\n")
plantas_por_familia = df.groupBy('Familia').count().sort(F.col('count').desc())
plantas_por_familia.show()

# Pregunta 5: Obtener las plantas más recientes registradas
print("Plantas más recientes registradas\n")
plantas_recientes = df.sort(F.col('Año').desc()).select('Nombre científico', 'Año')
plantas_recientes.show()


