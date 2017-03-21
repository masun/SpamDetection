# Proyecto Final de Minería de Datos
## Spam Detection on Twitter

Requerimientos: 
   * python2
   * [scikit-learn](http://scikit-learn.org/stable/)
   * [numpy](http://www.numpy.org/)
   * [matplotlib](http://matplotlib.org/)
   * [python-weka-wrapper](https://github.com/fracpete/python-weka-wrapper)
   * [django](https://www.djangoproject.com/)

Otras herramientas usadas:
   * [weka](http://www.cs.waikato.ac.nz/ml/weka/)
   * [birdwatcher](https://github.com/michenriksen/birdwatcher)
   * [Cloud9](https://c9.io/?redirect=0)

Fuentes:
  * Teóricas:
    * [Fake and Spam Messages: Detecting Misinformation During Natural Disasters on Social Media](http://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=5497&context=etd)
    * [Spam Detection for Twitter](http://webcache.googleusercontent.com/search?q=cache:deRMaAsShcEJ:project-archive.inf.ed.ac.uk/ug4/20150692/ug4_proj.pdf+&cd=7&hl=en&ct=clnk&gl=ve)
    * [Spam Detection on Twitter Using Traditional Classifiers](http://wbox0.cse.lehigh.edu/~chuah/publications/atc11_spam_camera.pdf)
  * Prácticas:
    * [Palabras comunes del idioma castellano](https://github.com/6/stopwords-json/blob/master/dist/es.json)
    * [Herramienta para la extracción de tópicos modificada](https://de.dariah.eu/tatom/topic_model_python.html)
    * [Ejemplos del uso de Weka con Python](http://pythonhosted.org/python-weka-wrapper/examples.html)
    * [Más ejemplos del uso de Weka con Python](https://github.com/fracpete/python-weka-wrapper-examples)

Instrucciones
--------------

Para correr la aplicación en Cloud9, se usa la siguiente orden en el directorio *Interfaz*:

`python manage.py runserver 0.0.0.0:8080`

luego se va a la siguiente dirección con el navegador: 

`http://[nombre del workspace]-[nombre del usuario].c9users.io:8080/tweets/?`

donde [nombre del workspace] es el nombre del workspace usado en Cloud9 y [nombre del usuario] es el nombre del usuario en
Cloud9 quien creó dicho workspace.

Una vez entrado el cliente a la dirección mostrada arriba, se puede ingresar la cuenta de Twitter de algún portal
de noticias en el buscador. Por ejemplo: @CNNEE.

Cuando termine de cargar los últimos tuits de este usuario, va a mostrarlos en una tabla. Un tuit es rojo cuando es 
considerado *Spam* por el modelo usado. Es verde si es considerado sano.

Integrantes:
   * Leslie Rodrigues    10-10613
   * Edward Fernández    10-11121
   * Joel Rivas          11-10866
   * Georvic Tur         12-11402



