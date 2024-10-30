# Tarea 3 BIG DATA_ UNAD_ERICK FAJARDO

# Analisis-Plantas-ValleCauca-Colombia
#“Proyecto de análisis de datos en Spark para plantas en peligro en el Valle del Cauca Colombia"
 
# Cargar datos desde Portal de Gobierno Datos Abiertos Gob

 #CÓDIGO   PYTHON

# procesamiento_batch.py

from pyspark.sql import SparkSession

def procesamiento_batch(spark, df):
    """
    Realiza procesamiento batch en un DataFrame de Spark.
    
    Args:
        spark (SparkSession): La sesión de Spark.
        df (DataFrame): DataFrame de Spark a procesar.
    
    Returns:
        DataFrame: DataFrame procesado.
    """
    try:
        # Ejemplo de transformación: filtrar datos
        df_filtrado = df.filter(df['columna'] > 100)  # Reemplaza 'columna' con el nombre real
        print("Procesamiento batch realizado exitosamente.")
        return df_filtrado
    except Exception as e:
        print(f"Error en el procesamiento batch: {e}")
        return None

if __name__ == "__main__":
    spark = SparkSession.builder.appName('ProcesamientoBatch').getOrCreate()
    # Cargar un DataFrame (puedes usar el código anterior para cargarlo)
    df = spark.read.csv('hdfs://localhost:9000/path/to/dataset.csv', header=True, inferSchema=True)
    df_procesado = procesamiento_batch(spark, df)
    df_procesado.show()  # Muestra el resultado del procesamiento
