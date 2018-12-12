from scraper.mixins import PyToMeBaseScrapperMixin, NO_DESCRIPTION
import shortuuid as shuuid
import time


class GitHubJobScrapper(PyToMeBaseScrapperMixin):

    def __init__(self, base_url= None, *args, **kwargs):
        super().__init__(base_url)
        
    def get_datablocks(self, page_content):
        """
        Retrive all the block from the targeted page which represents job info,
        result should be on the form of 
        [
            'html content here',
            'html content here',
            ......
        ] # to be parsed one by one with get_block_content() 

        arg: page_content : the content of the page fetched by using requests. This has been done by the framework itself
        """
        self.job_block = page_content.find_all('div', class_='job') #  in the case of pythonjobs.github.io
        # each job's block is contain with job class

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
        filled_block = []
        for job in self.job_block:
            #  extract each of them here
            filled_block.append({
                'job_title': job.find('h1').find('a').text,
                'job_description':job.p.text,
                'job_date':job.find_all('span')[1].text,
                'job_location':job.find_all('span')[0].text,
                'job_details_link':"{}{}".format(self.base_url.replace(self.base_url[-1],''), job.find('h1').find('a')['href']),
                'job_compagny':job.find_all('span')[3].text,
                'job_site':self.base_url, 
                'job_hash': shuuid.uuid(name='{}{}'.format(self.base_url, job.find('h1').find('a')['href'])),
                'fetched_timestamp': time.time()
            })
        self.job_data_set = filled_block


class PythonJobScrapper(PyToMeBaseScrapperMixin):

    def __init__(self, base_url = None, *args, **kwargs):
        super().__init__('https://www.python.org/jobs/')
    
    def get_datablocks(self, page_content):
        self.job_block = page_content.find_all('ol')[0].find_all('li')
        #print(self.job_block[0].find_all('li'))

    def get_block_content(self):
        filled_job = []
        for job in self.job_block:

            filled_job.append({
                'job_title': job.find('span').find('a').text,
                'job_description': NO_DESCRIPTION,
                'job_date': job.find('span', class_='listing-posted').find('time').text,
                'job_location':job.find('span', class_='listing-location').a.text,
                'job_details_link':"{}{}".format('https://www.python.org', job.find('h2').a['href']),
                'job_compagny':job.find('span', class_='listing-company-name').text.split(' ')[-17],
                'job_site':self.base_url, 
                'job_hash': shuuid.uuid(name='{}{}'.format('https://www.python.org', job.find('h2').a['href'])),
                'fetched_timestamp': time.time()
            })
        self.job_data_set = filled_job