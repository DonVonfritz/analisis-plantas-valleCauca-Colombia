# Tarea 3 BIG DATA_ UNAD_ERICK FAJARDO

# Analisis-Plantas-ValleCauca-Colombia
#“Proyecto de análisis de datos en Spark para plantas en peligro en el Valle del Cauca Colombia"
 
# Cargar datos desde Portal de Gobierno Datos Abiertos Gob

 #CÓDIGO   PYTHON

# procesamiento_streaming.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

def procesamiento_streaming(spark, ruta_stream):
    """
    Realiza procesamiento en streaming en Spark.
    
    Args:
        spark (SparkSession): La sesión de Spark.
        ruta_stream (str): Ruta del stream a leer.
    
    Returns:
        None
    """
    try:
        # Crea un DataFrame de streaming
        df_stream = spark.readStream.csv(ruta_stream, header=True, inferSchema=True)
        
        # Ejemplo de transformación en streaming: contar filas
        df_resultado = df_stream.groupBy("columna").count()  # Reemplaza 'columna' con el nombre real
        
        # Escribir el resultado a la consola
        query = df_resultado.writeStream.outputMode("complete").format("console").start()
        
        query.awaitTermination()
    except Exception as e:
        print(f"Error en el procesamiento en streaming: {e}")

if __name__ == "__main__":
    spark = SparkSession.builder.appName('ProcesamientoStreaming').getOrCreate()
    ruta_stream = '/path/to/stream'  # Reemplaza con la ruta correcta para el stream
    procesamiento_streaming(spark, ruta_stream)


