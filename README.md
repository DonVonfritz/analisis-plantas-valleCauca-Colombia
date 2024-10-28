# Analisis-Plantas-ValleCauca-Colombia
“Proyecto de análisis de datos en Spark para plantas en peligro en el Valle del Cauca Colombia"

Título del proyecto
Introducción
Descripción del Conjunto de Datos
Estructura del proyecto
Instalación y configuración
Instrucciones de Ejecución
Análisis y resultados
Enlace al Conjunto de Datos

Desarrollo de Contenidos

     Análisis de Plantas del Valle del Cauca en Riesgo de Amenaza

Introducción
          La pérdida de biodiversidad es un problema ambiental crítico. En el Valle del Cauca, Colombia, varias especies de plantas están en peligro debido a factores como la deforestación y el cambio climático. Mi proyecto busca analizar las categorías de amenaza de estas especies para apoyar la toma de decisiones informadas sobre conservación.
          Este proyecto aborda la pérdida de biodiversidad en el Valle del Cauca, Colombia,  enfocándose en especies de plantas que se encuentran en diversas categorías de  amenaza, desde "Vulnerable" hasta "En Peligro Crítico". El análisis tiene como objetivo apoyar la toma de decisiones en conservación al ofrecer datos precisos y en tiempo real sobre la situación de estas especies. La pérdida de estas plantas impacta negativamente en los ecosistemas locales, y un detallado de su estado permite  orientar análisis de acciones de preservación y políticas ambientales.
Descripción del Conjunto de Datos
Utilizamos un conjunto de datos públicos sobre las plantas del Valle del Cauca clasificadas en categorías de amenaza. El conjunto incluye información detallada como el nombre científico de cada planta, su categoría de amenaza y la localidad específica dentro del Valle del Cauca donde fue identificada.
Enlace al conjunto de datos originales : PLANTAS DEL DEPARTAMENTO DEL VALLE DEL CAUCA CON CATEGORÍA DE AMENAZA

Estructura del proyecto
/data: Carpeta para el almacenamiento del conjunto de datos en formato CSV.
/batch_processing: Scripts de procesamiento por lotes para el análisis exploratorio de datos.
/streaming_processing: Scripts para procesamiento en tiempo real usando Spark 
Streaming y Kafka.
/config: Archivos de configuración para Kafka y Spark.
/resultados: Carpeta de almacenamiento para guardar resultados de análisis y visualizaciones.

Instalación y configuración
Dependencias
Asegúrese de instalar las siguientes dependencias:
•	Python 3.7+
•	PySpark :pip install pyspark
•	Kafka-Python :pip install kafka-python
•	Java 8+ (requerido para Spark)
•	Apache Kafka y el guardián del zoológico
•	Apache Hadoop (opcional, si deseas almacenamiento distribuido)

Instrucciones de configuración
1. Configurar Kafka: Descarga e instala Kafka y Zookeeper. Una vez instalado, inicia Zookeeper y Kafka Server.
 código
# Inicia Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties
# Inicia Kafka Server
bin/kafka-server-start.sh config/server.properties
2. Configurar Spark: Configura Spark en modo local para pruebas, o en modo clúster si  trabajas con grandes volúmenes de datos.
3. Crear Tema en Kafka: Crea un tema en Kafka llamado plantas_topicpara la transmisión de datos.
 código
bin/kafka-topics.sh --create --topic plantas_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Ejecución
Procesamiento por lotes
Para ejecutar el análisis por lotes, asegúrese de tener el conjunto de datos descargado en la carpeta /data. Luego, ejecuta el siguiente script:
 código
spark-submit batch_processing/analyze_plants_batch.py

Procesamiento en Tiempo Real (Streaming)
Inicia la simulación de datos en tiempo real enviándolos al tema de Kafka. Luego, ejecuta el script de Spark Streaming para procesar estos datos:
Simulación de datos: Usa un generador de datos para enviar datos simulados al tema de Kafka.
Pyton
 código 
python
data_stream_generator.py

Script de Streaming: Ejecute el script de Spark Streaming para procesar los datos entrantes.

código
spark-submit streaming_processing/analyze_plants_streaming.py

Análisis y resultados
El análisis por lotes y en tiempo real nos ha permitido observar cómo las especies  en diversas categorías de amenaza se distribuyen en el Valle del Cauca. Los  resultados incluyen:

Distribución por categoría de amenaza: La mayoría de las especies están clasificadas  como "Vulnerables", con concentraciones significativas en ciertas áreas.
Monitoreo en tiempo real: El sistema identifica y registra cualquier cambio en la categoría de amenaza de especies, lo cual ayuda a tomar decisiones rápidas en conservación.
Visualizaciones: Puedes encontrar las visualizaciones en la carpeta /results o generar las propias exportando los datos procesados a herramientas de visualización como Power BI o Tableau.

Enlace al Conjunto de Datos
Si necesitas descargar el archivo original, accede al siguiente enlace: PLANTAS DEL DEPARTAMENTO DEL VALLE DEL CAUCA CON CATEGORÍA DE AMENAZA.  
https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/PLANTAS-DEL-DEPARTAMENTO-DEL-VALLE-DEL-CAUCA-CON-C/di5n-jaf8/data_preview 



