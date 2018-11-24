# <>Python-Hire-Jobs
#
# Author: [Sanix-darker](https://github.com/sanix-darker)
#
# Ressources / WebSites used to fetch data:
# https://github.com/pyjobs/annonces~
# https://djangogigs.com/gigs/remote/~
# https://angel.co/europe/python/jobs~
# https://remoteml.com/tags/Python/~
# https://nodesk.co/remote-jobs/python/~
# https://www.codementor.io/freelance-jobs/python~
# https://www.indeed.com.ph/Remote-Python-jobs~
# https://remote4me.com/remote-python-jobs~
# https://www.irishjobs.ie/Remote-Python-Jobs~
# https://www.reed.co.uk/jobs/python-developer-remote/36144618~
# https://www.simplyhired.com/search?q=remote+python+developer&l=austin%2C+tx&job=ViO7geREaxO513t_xvNXtyVy2t9_kmX9_BjPGMevSnLgkOwH73PMww~
# https://remotees.com/remote-python-jobs~
# https://www.indeed.co.uk/Python-jobs-in-Remote~
# https://jobs.trovit.co.uk/remote-python-jobs~
# https://www.glassdoor.co.uk/Job/uk-remote-python-jobs-SRCH_IL.0,2_IN2_KO3,16.htm~
# https://www.cybercoders.com/jobs/remote-python-developer-jobs/~
# https://www.pearsonfrank.com/32655/uk-remote-python-developer~
# https://www.flexjobs.com/jobs/python~
# https://twitter.com/remotepython?lang=en~
# https://www.reddit.com/r/remotepython/~
# https://www.remotelyawesomejobs.com/remote-python-jobs/~
# https://europeremotely.com/remote-jobs/Python~
# https://www.glassdoor.com/Job/remote-python-jobs-SRCH_IL.0,6_IS11047_KO7,13.htm~
# https://www.glassdoor.com/Job/remote-python-jobs-SRCH_KO0,13.htm~
# https://www.linkedin.com/jobs/python-remote-jobs~
# https://stackoverflow.com/jobs/remote-developer-jobs-using-python~
# https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python~
# https://www.workingnomads.co/remote-python-jobs~
# https://www.python.org/jobs/location/telecommute/~
# https://jobs.github.com/positions?description=python~
# https://pythonjobs.github.io/~
# https://www.python.org/jobs/~
# https://www.indeed.com/q-Remote-Python-Developer-jobs.html~
# https://www.indeed.com/q-Remote-Python-jobs.html~
# https://www.indeed.com/q-Python-jobs.html~
# https://www.indeed.com/q-Python-Developer-jobs.html~
# https://remoteok.io/remote-python-jobs~
# https://www.linkedin.com/jobs/python-jobs~
# https://www.linkedin.com/jobs/python-developer-jobs~
# https://www.remotepython.com/~
# https://www.pythonjobs.com/~
# https://www.glassdoor.com/Job/python-developer-jobs-SRCH_KO0,16.htm~
# https://www.naukri.com/python-developer-jobs~
# https://www.upwork.com/o/jobs/browse/skill/python/~
# https://www.seek.co.nz/python-jobs~
# https://www.nijobs.com/Python-Jobs-in-Belfast~
# https://www.irishjobs.ie/Python-Developer-Jobs-in-Dublin~
# https://stackoverflow.com/jobs/developer-jobs-using-python~
# https://www.technojobs.co.uk/python-jobs~
# https://www.pythonjobshq.com/~

import requests
import BeautifulSoup
import schedule
import time

# Globlas variables
WEBSITE_DATABASE = "website.pytome"

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