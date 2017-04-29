Umbrella
==========
#### Descripción

Umbrella es una aplicacion de busqueda de archivos por medio de palabras claves ingresadas en la barra de busqueda,
para ello se implemento un algoritmo de busqueda para la analitica de texto.

#### Requisitos 
* Python 3.6
* Mrjob
* Flask 
* MongoDB

#### Correr el wordcount.py
-Se descarga el dataset
$wget -w 2 -m -H "http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=es"

-Se descomprime
$find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done; 

-Se copian solo los txt en una carpeta
$find . -type f -print0 | xargs -0 mv -t <Nuevo directorio>
Ejemplo:
$find . -type f -print0 | xargs -0 mv -t /home/cmunozf/dataset

-Se crean las carpetas necesarias en donde se guardaran los archivos hdfs
$hdfs dfs -mkdir /user/st0263/username/data_in
$hdfs dfs -mkdir /user/st0263/username/data_out

Luego se pasa el dataset a hdfs 
$hdfs dfs -copyFromLocal <directorio a copiar>/*.txt <directorio final>
Ejemplo:
$hdfs dfs -copyFromLocal /home/cmunozf/dataset/*.txt hdfs:/user/cmunozf/data_in/

-Se ejecuta el wordCount en el dataset que esta en hdfs
$python <direccion fichero> hdfs:/<direccion donde estan los datos>/*.txt -r hadoop --output-dir hdfs:/<directorio salida de lso datos>
Ejemplo:
$python topicosTelematica-algoritmo/invertedIndex.py hdfs:/user/cmunozf/data_in/*.txt -r hadoop --output-dir hdfs:/user/cmunozf/data_out/out6
