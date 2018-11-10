# IMDB Movie Scraper

## Descripción

Se tarta de una práctica para la asignatura Tipología y ciclo de vida de los datos del Máster de Data Science en la UOC.

El cometido es relizar un web scrapper que permita obtener la información general de las películas publicadas en el portal de IMDB según unas fechas de entrada.

## Miembros del equipo

**Gonzalo Mellizo-Soto**.

## Ficheros

* **src/new_main.py**: main del programa. Se realiza la llamada sobre este script introduciendo las fechas y el nombre de salida como atributos: 

  `python new_main.py --startDate 2018-01-01 --endDate 2018-12-30 --name test_dataset.csv`
* **src/movieScraper.py**: clase `imdbScraper()` y la definición de sus método públicos y privados para realizar web scraping sobre IMDB.
* **src/requirements.txt**: ficheros de requerimientos para la ejecución del scaper, se utiliza con el comando:

  `pip install -r requirements.txt`
* **src/imbd_2018_raw.csv**: fichero que contiene el dataset
* **doc/Practica1_Tipologia.html**: fichero html con la entrega de la práctica
* **doc/Practica1_Tipologia.odt**: fichero odt con la entrega de la práctica
* **doc/Readme.md**: markdown con la entrega de la práctica para la visualización directa en github

## Recursos

* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
* Beautiful Soup Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* Guía de ejemplo: https://github.com/rafoelhonrado/foodPriceScraper
