DESCRIPCIÓN DE LOS DATASETS

dumpCaraotaDigitalCNNELaPatilla.csv
    Datos obtenidos por Birdwatcher sin ser procesados.

dumpCaraotaDigitalCNNELaPatillaRANDOM.csv
    Datos obtenidos por Birdwatcher desordenados de manera aleatoria. No todos
    se usan en los conjuntos de entrenamiento y validación. Sin embargo, todos
    se usan para generar los tópicos

featureVectorsDumpCaraotaDigitalCNNELaPatillaENTRENAMIENTO.csv
    Vectores de features clasificados manualmente de la primera parte del
    archivo de tuits desordenados

featureVectorsDumpCaraotaDigitalCNNELaPatilla_VALIDACION.csv
    Vectores de features clasificados manualmente de la parte siguiente
    a los anteriores en el archivo de tuits desordenados

topicsWithTopWords.csv
    Tópicos generados por extractor_de_topics.py con sus palabras más importantes

idTuitsWithTopTopics.csv
    Tabla relacional entre los identificadores de todos los tuits y su repespectivo
    tópico más importante

idTuitsWithTopTopicsEntrenamiento.csv
    Tabla relacional entre los identificadores de los tuits de entrenamiento y 
    su repespectivo tópico más importante

datos_separados/
    Carpeta que contiene una partición de los tuits de entrenamiento de acuerdo
    a su tópico más importante. Cada número del nombre del archivo corresponde
    al tópico como se muestra en topicsWithTopWords.csv y 
    idTuitsWithTopTopicsEntrenamiento.csv

originales/
    Este directorio contiene los datasets originales sin preprocesar y sin los
    atributos

con_atributos_adicionales/
    Aquí se encuentran los datasets con los atributos adicionales que no 
    dependen estrictamente del texto o se calculan de manera distina con
    los tópicos


Comentarios:

    DATASETS ETIQUETADOS AUTOMÁTICAMENTE:
        Los datasets que tengan en su nombre las palabras 'filtro' 'cluster' fueron
        etiquetados de manera automática con Weka
        