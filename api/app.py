# <>Python-Hire-Jobs
#
# Author: [Sanix-darker](https://github.com/sanix-darker)
#
# Ressources / WebSites used to fetch data:
# See WEBSITE_DATABASE 

import requests
import BeautifulSoup
import schedule
import time

# Globlas variables
WEBSITE_DATABASE = "./data/website.ptm"

def Presentation():
    print "-------------------------------------------------------"
    print "--------------------- PYTHOME v0.1 --------------------"
    print "-------------------------------------------------------"
    print "====================================By S@n1x-d4rk3r===="

# This method take as parameter:
# -the url, 
# -the example of schema to fetch and 
# -the total of result to be get
def fetch_fromIT(url, schema, total):
    soup = BeautifulSoup('\n'.join(requests.get(url).text.splitlines()[1:total]), 'html.parser')
    return [i.get('href') for i in soup.find_all(schema)]

def getWebSite_and_schema_and_save_data():
    result = ""
    # Getting list of links and schemas 
    # and remove whitespace characters like `\n` at the end of each line
    lines = [line.rstrip('\n') for line in open(WEBSITE_DATABASE)]
    # Loop in lines, fetch and get result
    for x in lines:
        result += fetch_fromIT(x.plit('~')[0], x.plit('~')[1], 15)
    return result;

# The method JOB
def PYTOME_job():
    print "Starting the Job............."    
    getWebSite_and_schema_and_save_data()

# Other Schedules Options
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# Let say, automation every day at 00:01
#schedule.every().day.at("00:01").do(PYTOME_job)


Presentation()
PYTOME_job()
# while True:
#     schedule.run_pending()
#     time.sleep(1)