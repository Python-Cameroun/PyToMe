"""
An example on how to use this code.

** How it work **
1 - import available scrapers
2 - import Scraping engine
3 - import default callback method, json_callback_writer() 
4 - create an instance of the scraping engine with the 2 default available scraper
5 - run it by calling it run() method and pass to it the utils's method which will be use as callback

normally you will have a scrapper.json file in the current folder with result of scraping
"""
from scraper.scraper import GitHubJobScrapper, PythonJobScrapper
from scraper.engine import ScraperEngine
from scraper.utils import json_callback_writer

app = ScraperEngine([GitHubJobScrapper(), PythonJobScrapper()])
app.run(json_callback_writer)