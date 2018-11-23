# <>Python-Hire-Jobs
# BIGS THANKs TO -> poteto and jessicard on GITHUB;
# because, i used their "README.md" to fetch data for this project!
#
# Author: Sanix-darker

import re
import requests

def get_companies():
    """Get all companies that don't do whiteboard hiring"""
    req = requests.get('https://raw.githubusercontent.com/poteto/hiring-without-whiteboards/master/README.md')
    return [
        re.search(r'^- \[(.*)\]', _).group(1)
        for _ in req.text.split('\n')
        if re.search(r'^- \[(.*)\]', _)
    ]

def get_companies_for_remote_job():
    """Get all companies that have remote job opportunities"""
    req = requests.get('https://raw.githubusercontent.com/jessicard/remote-jobs/master/README.md')
    regex_search = r'(\[(.*)\]|^(.*) \|.*\|)'
    return [
        re.search(regex_search, _).group(2)
        if re.search(regex_search, _).group(2)
        else re.search(regex_search, _).group(3)
        for _ in req.text.split('\n')
        if re.search(regex_search, _)
    ]