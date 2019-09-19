# <>Python-Hire-Jobs
#
# Author: [Sanix-darker](https://github.com/sanix-darker)
#
# Ressources / WebSites used to fetch data:
# See WEBSITE_DATABASE 
# on pending:
# https://angel.co/europe/python/jobs~a
# https://remoteml.com/tags/Python/~a
# https://nodesk.co/remote-jobs/python/~a
# https://www.codementor.io/freelance-jobs/python~a
# https://www.indeed.com.ph/Remote-Python-jobs~a
# https://remote4me.com/remote-python-jobs~a
# https://www.irishjobs.ie/Remote-Python-Jobs~a
# https://www.reed.co.uk/jobs/python-developer-remote/36144618~a
# https://www.simplyhired.com/search?q=remote+python+developer&l=austin%2C+tx&job=ViO7geREaxO513t_xvNXtyVy2t9_kmX9_BjPGMevSnLgkOwH73PMww~a
# https://remotees.com/remote-python-jobs~a
# https://www.indeed.co.uk/Python-jobs-in-Remote~a
# https://jobs.trovit.co.uk/remote-python-jobs~a
# https://www.glassdoor.co.uk/Job/uk-remote-python-jobs-SRCH_IL.0,2_IN2_KO3,16.htm~a
# https://www.cybercoders.com/jobs/remote-python-developer-jobs/~a
# https://www.pearsonfrank.com/32655/uk-remote-python-developer~a
# https://www.flexjobs.com/jobs/python~a
# https://twitter.com/remotepython?lang=en~a
# https://www.reddit.com/r/remotepython/~a
# https://www.remotelyawesomejobs.com/remote-python-jobs/~a
# https://europeremotely.com/remote-jobs/Python~a
# https://www.glassdoor.com/Job/remote-python-jobs-SRCH_IL.0,6_IS11047_KO7,13.htm~a
# https://www.glassdoor.com/Job/remote-python-jobs-SRCH_KO0,13.htm~a
# https://www.linkedin.com/jobs/python-remote-jobs~a
# https://stackoverflow.com/jobs/remote-developer-jobs-using-python~a
# https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python~a
# https://www.workingnomads.co/remote-python-jobs~a
# https://www.python.org/jobs/location/telecommute/~a
# https://jobs.github.com/positions?description=python~a
# https://pythonjobs.github.io/~a
# https://www.python.org/jobs/~a
# https://www.indeed.com/q-Remote-Python-Developer-jobs.html~a
# https://www.indeed.com/q-Remote-Python-jobs.html~a
# https://www.indeed.com/q-Python-jobs.html~a
# https://www.indeed.com/q-Python-Developer-jobs.html~a
# https://remoteok.io/remote-python-jobs~a
# https://www.linkedin.com/jobs/python-jobs~a
# https://www.linkedin.com/jobs/python-developer-jobs~a
# https://www.remotepython.com/~a
# https://www.pythonjobs.com/~a
# https://www.glassdoor.com/Job/python-developer-jobs-SRCH_KO0,16.htm~a
# https://www.naukri.com/python-developer-jobs~a
# https://www.upwork.com/o/jobs/browse/skill/python/~a
# https://www.seek.co.nz/python-jobs~a
# https://www.nijobs.com/Python-Jobs-in-Belfast~a
# https://www.irishjobs.ie/Python-Developer-Jobs-in-Dublin~a
# https://stackoverflow.com/jobs/developer-jobs-using-python~a
# https://www.technojobs.co.uk/python-jobs~a
# https://www.pythonjobshq.com/~a
import os
import requests
from bs4 import BeautifulSoup
import schedule
import time

# Globlas variables
WEBSITE_DATABASE = "./data/website.ptm"

def Presentation():
    print "====PYTHON CAMEROUN===================================="
    print "--------------------- PYTHOME v0.1 --------------------"
    print "====================================By S@n1x-d4rk3r===="

# This method take as parameter:
# -the url, 
# -the example of schema to fetch and 
# -the total of result to be get
def fetch_fromIT(url, schema, total):
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    result = ""
    for link in soup.find_all(schema.split(',')[0]):
        try:
            result += link.get(schema.split(',')[1])
            print(link.get(schema.split(',')[1]))
        except:
            print "Error on coercing to Unicode: need string or buffer, NoneType found"
    return result

def getWebSite_and_schema_and_save_data():
    result = []
    # Getting list of links and schemas 
    # and remove whitespace characters like `\n` at the end of each line
    lines = [line.rstrip('\n') for line in open(WEBSITE_DATABASE)]
    # Loop in lines, fetch and get result
    for x in lines:
        print "Fetching on "+x.split('~')[0]
        result += fetch_fromIT(x.split('~')[0], x.split('~')[1], 15)
    return result;

# The method JOB
def PYTOME_job():
    print "Starting the Job............."    
    print getWebSite_and_schema_and_save_data()

# Other Schedules Options
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# Let say, automation every day at 00:01
schedule.every().day.at("00:01").do(PYTOME_job)

Presentation()

while True:
    schedule.run_pending()
    time.sleep(1)