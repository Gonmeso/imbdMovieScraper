import requests
import re
import csv
import argparse
import sys
from datetime import datetime
from bs4 import BeautifulSoup
from math import ceil
from time import sleep

class imdbScraper():

    url = 'https://www.imdb.com/search/title?title_type=feature&release_date={},{}&start={}&ref_=adv_prv'
    
    def __init__(self):
        self.startDate = None
        self.endDate = None
        self.total = 0
        self.iteraciones = 0
        self.movieList = [['title', 'duration', 'certificate', \
                        'genre', 'rating', 'directors', 'stars']]


    def setDates(self, args):
        try:
            startDate = datetime.strptime(args.startDate, "%Y-%m-%d").strftime("%Y-%m-%d")
            endDate = datetime.strptime(args.endDate,"%Y-%m-%d").strftime("%Y-%m-%d")
            self.startDate = startDate
            self.endDate = endDate
            print('Fechas actualizadas')

        except Exception as e:
            print(e)
            sys.exit(1)

    def __updateTotalMovies(self):
        response = requests.get(self.url.format(self.startDate, self.endDate,'1'))
        soup = BeautifulSoup(response.text,"html.parser")
        total_div = soup.findAll('div', {"class" : "desc"} ) 
        total_span = total_div[0].findAll('span')[0]
        total = int(total_span.find(text=True).split(" ")[2].replace(",",""))
        self.total = total
        print("Número total de películas: {}".format(total))
    
    def __updateIterations(self):
        self.iteraciones = ceil(self.total / 50)

    def __getTittle(self, movie):
        try:
            title = movie.h3.a.find(text=True)
        except:
            title = 'NA'
        return title    


    def __getDuration(self, movie):
        try:
            duration = movie.find(class_="runtime").find(text = True)
        except:
            duration = 'NA'
        return duration
    
    def __getCertificate(self, movie): 
        try:
            certificate = movie.find(class_="certificate").find(text = True)
        except:
            certificate = 'NA'
        return certificate
    
    def __getGenre(self, movie):
        try:
            genre = movie.find(class_="genre").find(text = True).replace('\n','').strip()
        except:
            genre = 'NA'
        return genre

    def __getRating(self, movie):
        try:
            rating = movie.find(class_="ratings-bar").strong.find(text=True)
        except:
            rating = 'NA'
        return rating

    def __getDirectors(self, movie):

        raw_directors = movie.find_all('p',class_="")[1].find_all('a', {'href': re.compile(r'_dr_')})
        film_directors = []
        for director in raw_directors:
            film_directors.append(director.find(text=True))
        film_directors = ', '.join(film_directors)

        if film_directors == '':
            film_directors = 'NA'

        return film_directors
    
    def __getStars(self, movie):

        film_stars = []
        raw_stars = movie.find_all('p',class_="")[1].find_all('a', {'href': re.compile(r'_st_')})
        for star in raw_stars:
            film_stars.append(star.find(text=True))
        film_stars = ', '.join(film_stars)

        if film_stars == '':
            film_stars = 'NA'

        return film_stars

    def __scrapMoviesInfo(self, htmlPage):

        for movie in htmlPage:
            film_title = self.__getTittle(movie)
            film_duration = self.__getDuration(movie)
            film_certificate =self.__getCertificate(movie)
            film_genre = self.__getGenre(movie)
            film_rating = self.__getRating(movie)
            film_directors = self.__getDirectors(movie)
            film_stars = self.__getStars(movie)

            self.movieList.append([film_title, film_duration, film_certificate, \
                    film_genre, film_rating, film_directors, film_stars])
    
    def __scrapAllMovies(self):

        for i in range(self.iteraciones):
            sleep(1)
            
            start = (i*50)+1
            response = requests.get(self.url.format(self.startDate, self.endDate,start))
            soup = BeautifulSoup(response.text,"html.parser")

            movies_div = soup.findAll('div', {"class" : "lister-item-content"} )

            self.__scrapMoviesInfo(movies_div)
            print("Ronda {}: se han encontrado en total {} películas". format((i+1),
                                                                        len(self.movieList)-1))
        print("Web scraping finalizado con éxito!")
    
    def writeMoviesToCsv(self, output):
        with open(output, 'w', newline='') as f:
            wr = csv.writer(f, delimiter=';')
            for scraped_movie in self.movieList:
                wr.writerow(scraped_movie)
        print("Fichero {} creado!".format(output))

    def startMovieScraping(self):

        if self.startDate is not None or self.endDate is not None:
            self.__updateTotalMovies()
            self.__updateIterations()
            self.__scrapAllMovies()
        else:
            #logging
            sys.exit(1)
