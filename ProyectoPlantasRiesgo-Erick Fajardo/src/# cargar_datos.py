# Tarea 3 BIG DATA_ UNAD_ERICK FAJARDO

# Analisis-Plantas-ValleCauca-Colombia
#“Proyecto de análisis de datos en Spark para plantas en peligro en el Valle del Cauca Colombia"
 
# Cargar datos desde Portal de Gobierno Datos Abiertos Gob

 #CÓDIGO   PYTHON

# cargar_datos.py

import pandas as pd

def cargar_datos(url):
    """
    Carga datos desde un URL.
    
    Args:
        url (str): URL del archivo CSV a cargar.
    
    Returns:
        DataFrame: DataFrame de pandas con los datos cargados.
    """
    try:
        datos = pd.read_csv(url)
        print("Datos cargados exitosamente.")
        return datos
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

if __name__ == "__main__":
    url_datos = 'https://datos.gov.co/api/3/action/datastore_search?resource_id=xxx'  # Reemplaza con la URL correcta
    df_datos = cargar_datos(url_datos)
    print(df_datos.head())  # Muestra las primeras filas del DataFrame
