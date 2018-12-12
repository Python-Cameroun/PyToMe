"""
Will contain some default utils function like one which will
just serialize scraped data into a .json file. It should be used as callback in the 
run() method of the scraper engine
"""
import json


def json_callback_writer(stuff):
    file_json = open('scrapper.json', 'w')
    file_json.write(json.dumps(stuff, indent=4))
    file_json.close()
    return True
