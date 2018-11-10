# Práctica 1 - Tipología y ciclo de vida de los datos


## 1. Título del dataset.

2018 IMBD Movies (Imdb_2018_raw.csv)

## 2. Subtítulo del dataset.

Dataset con información sobre las películas registradas en IMDB durante el 2018

## 3. Imagen. Agregad una imagen que identifique vuestro dataset visualmente

Esta imagen muestra las portadas de películas actuales

![alt text](https://designwithred.com/wp-content/uploads/2018/03/30-Stunning-Movie-Poster-Design-Inspiration-2018-850x425.jpg "Logo Title Text 1")

## 4. Contexto. ¿Cuál es la materia del conjunto de datos?

El conjunto de datos se encuentra relacionado con los medios audiovisuales registrados en la conocida página web, concretamente nos permite obtener información general de las películas en un determinado periodo de tiempo, en este caso el año 2018. Por otro lado, también nos permite obtener los recursos humanos principales de la película.
Contiene 8871 observaciones y 7 variables distintas.

## 5. Contenido. ¿Qué campos incluye? ¿Cuál es el periodo de tiempo de los datos y cómo se ha recogido?

Se muestran los siguientes campos:

* title: título de la película en cuestión
* duration: duración de la película
* certificate: certificado del público recomendado
* genre: género o géneros de la película
* rating: puntuación de la película en IMDB
* directors: director o directores de la película
* stars: reparto de la películas

El periodo de tiempo utilizado es del año 2018 desde el uno de enero hasta finales de diciembre, pero en la llamada al script se pueden seleccionar las fechas deseadas. 
El tiempo se ha seleccionado como parámetro de entrada por lo que puede recoger el periodo de tiempo que se le indique. 

## 6. Agradecimientos. ¿Quién es  propietario del conjunto de datos?

En este caso los datos se tratan de hechos, salvo la puntuación que es información propietaria de IMDB, sin embargo este dataset va a ser de uso personal y no se pretende la republicación de ningún tipo de dato propietario.

Análisis anteriores:

* IMDB 5000 Movie Dataset: https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset
* IMDB data from 2006 to 2016: https://www.kaggle.com/PromptCloudHQ/imdb-data

Recursos:

* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
* Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* Guía de ejemplo: https://github.com/rafoelhonrado/foodPriceScraper

Propietario:
```
 {
  "domain_name": [
    "IMDB.COM",
    "imdb.com"
  ],
  "registrar": "MarkMonitor, Inc.",
  "whois_server": "whois.markmonitor.com",
  "referral_url": null,
  "updated_date": [
    "2016-05-05 23:11:07",
    "2016-05-05 16:11:07"
  ],
  "creation_date": [
    "1996-01-05 05:00:00",
    "1996-01-04 21:00:00"
  ],
  "expiration_date": [
    "2020-01-04 05:00:00",
    "2020-01-03 00:00:00"
  ],
  "name_servers": [
    "NS1.P31.DYNECT.NET",
    "NS2.P31.DYNECT.NET",
    "NS3.P31.DYNECT.NET",
    "NS4.P31.DYNECT.NET",
    "PDNS1.ULTRADNS.NET",
    "PDNS2.ULTRADNS.NET",
    "PDNS3.ULTRADNS.ORG",
    "PDNS4.ULTRADNS.ORG",
    "PDNS5.ULTRADNS.INFO",
    "PDNS6.ULTRADNS.CO.UK",
    "ns1.p31.dynect.net",
    "pdns3.ultradns.org",
    "ns4.p31.dynect.net",
    "ns2.p31.dynect.net",
    "pdns4.ultradns.org",
    "pdns5.ultradns.info",
    "pdns6.ultradns.co.uk",
    "pdns2.ultradns.net",
    "pdns1.ultradns.net",
    "ns3.p31.dynect.net"
  ],
  "status": [
    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
    "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
    "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
    "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
    "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
    "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
    "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
  ],
  "emails": [
    "abusecomplaints@markmonitor.com",
    "whoisrelay@markmonitor.com"
  ],
  "dnssec": "unsigned",
  "name": null,
  "org": "IMDb.com, Inc.",
  "address": null,
  "city": null,
  "state": "WA",
  "zipcode": null,
  "country": "US"
}

```

## 7. Inspiración. ¿Por qué es interesante este conjunto de datos?  ¿Qué preguntas le gustaría responder la comunidad?

Mi inspiración principal proviene de mi gusto por las películas y todos los medios audiovisuales en general (series, películas, música, etc.) y como puedo aplicar una nueva técnica para obtener datos de interés. 
Por otro lado, al visitar frecuentemente kaggle y visitar los datasets disponibles en algún momento me crucé con datasets relacionados con IMDB, pero generados por otras personas. Por ello he elegido este portal, para tratar de entender como se han realizado estos datasets originalmente y como podría aplicarlo para uso personal, además de adquirir nuevos conocimientos durante la práctica.

Con este dataset se podrían observar distintas cosas, como por ejemplo:

* Directores/actores con más películas en un periodo determinado
* Rating promedio general/por género
* Cantidad de películas por género
* Genero con mayores valoraciones en un periodo
* Duración promedio general/por género/director
* Por otro lado, también se podría utilizar para aumentar los datos disponibles y cruzarlo con distintos  portales o incluir información de los directores/actores.

## 8. Licencia. 

Se va a utilizar la licencia “Released Under CC0: Public Domain License” para renunciar a los derechos del conjunto de datos y hacer que sean de dominio público. 
Esta licencia permite compartir el conjunto con el resto del mundo sin necesidad de mención, se ha elegido está para que otras personas puedan disponer del mismo y realizar las operaciones y estudios que consideren.

## 9. Código

El código se encuentra en la carpeta src del repositorio: https://github.com/Gonmeso/imbdMovieScraper

## 10. Dataset

El dataset se encuentra en la carpeta src del repositorio: https://github.com/Gonmeso/imbdMovieScraper
