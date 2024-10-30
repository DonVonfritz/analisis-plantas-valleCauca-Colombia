# Tarea 3 BIG DATA_ UNAD_ERICK FAJARDO

# Analisis-Plantas-ValleCauca-Colombia
#“Proyecto de análisis de datos en Spark para plantas en peligro en el Valle del Cauca Colombia"
 
# Cargar datos desde Portal de Gobierno Datos Abiertos Gob

 #CÓDIGO   PYTHON

# cargar_hadoop.py

from pyspark.sql import SparkSession

def cargar_datos_hadoop(spark, ruta_datos):
    """
    Carga datos en Hadoop usando Spark.
    
    Args:
        spark (SparkSession): La sesión de Spark.
        ruta_datos (str): Ruta del archivo en Hadoop.
    
    Returns:
        DataFrame: DataFrame de Spark con los datos cargados.
    """
    try:
        df_hadoop = spark.read.csv(ruta_datos, header=True, inferSchema=True)
        print("Datos cargados en Hadoop exitosamente.")
        return df_hadoop
    except Exception as e:
        print(f"Error al cargar los datos en Hadoop: {e}")
        return None

if __name__ == "__main__":
    spark = SparkSession.builder.appName('CargarHadoop').getOrCreate()
    ruta_datos_hadoop = 'hdfs://localhost:9000/path/to/dataset.csv'  # Reemplaza con la ruta correcta
    df_hadoop = cargar_datos_hadoop(spark, ruta_datos_hadoop)
    df_hadoop.show()  # Muestra el contenido del DataFrame




