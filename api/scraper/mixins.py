"""
The base mixin used to implement the different scraper

TODO : Write a complete and working doc
TODO : Write tests
TODO : Let the code follow PEP 8 Coding style
"""

import requests
import shortuuid as shuuid
from bs4 import BeautifulSoup
import time

NO_DESCRIPTION = 'No description provided by the site'


class PyToMeBaseScrapperMixin:
    """
    default url : https://pythonjobs.github.io/
    """

    base_url = ''
    job_block = []
    job_data_set = []

    def __init__(self, base_url, *args, **kwargs):
        if base_url == None:
            self.base_url = 'https://pythonjobs.github.io/' 
        else:
            self.base_url = base_url
        self.job_block = []

    def get_datablocks(self,page_content):
        """
        Retrive all the block from the targeted page which represents job info,
        result should be on the form of 
        [
            'html content here',
            'html content here',
            ......
        ] # to be parsed one by one with get_block_content() 
        """
        raise NotImplementedError('This method has not being implemented, the current class should be use only by inheritance')

    def get_block_content(self):
        """
        Retrive the content of one block of data, data should be shaped as follow
        {
            'job_title':'',
            'job_description:'',
            'job_date':'',
            'job_location':'',
            'job_details_link':'',
            'job_compagny':'',
            'job_site':'', # where the job has been scrapped
            'job_hash':'' # built by using shortuuuid() lib by combining job_title+job_compagny+job_date str
        }
        """
        raise NotImplementedError('This method has not being implemented, the current class should be use only by inheritance')
    
    def _log_result(self):
        #print(self.job_block)
        pass

    def launch(self):
        self.__init__()

        if self.job_block == []:
            page_response = requests.get(self.base_url)
            page_content = BeautifulSoup(page_response.content, 'html.parser')
            self.get_datablocks(page_content)
        self.get_block_content()
        return self.get_job_dataset()

    def get_job_dataset(self):
        """
        Just return the current dataset of job fetched or not yet fetched
        """
        return self.job_data_set