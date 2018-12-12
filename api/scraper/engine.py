from scraper.mixins import PyToMeBaseScrapperMixin


class ScraperEngine:

    _data = []
    _scrapers = []
    """
    Plugin system to load and unload scrapers
    """
    def __init__(self, plugins: list=list(), *args, **kwargs):
        self._data = []
        self._scrapers = []
        for scraper in plugins:
            if isinstance(scraper, PyToMeBaseScrapperMixin): #  only consider class based on PyToMeBaseScrapperMixin
                self._scrapers.append(scraper)

    def run(self, cb):
        scrapers = self._scrapers
        scrp_data = []
        for scraper in scrapers:
            scrp_data += scraper.launch() #  run and add result to the same var here
        self._data = scrp_data
        cb(self._data) #  the callback here