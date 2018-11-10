from movieScraper import imdbScraper
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--startDate", help="Enter start date of interval with the following format '%Y-%m-%d'")
parser.add_argument("--endDate", help="Enter end date of interval with the following format '%Y-%m-%d'")
parser.add_argument("--name", help="Enter the name of the output file")
args = parser.parse_args()

ms = imdbScraper()

ms.setDates(args)
ms.startMovieScraping()
ms.writeMoviesToCsv(args.name)