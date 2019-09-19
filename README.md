<img src="assets/img/logo.jpg">

# <>PyToMe

## Introduction
   We know how it's sometimes realy complicated for a developper in Cameroon to get hire by a companie for a full time job, or just get Hire for a single project, i created this project to resolve that problem (For Python developpers....), it's a really simple app, fetching and notify suscribers, PyToMe fetch jobs around multiple websites(Only PYTHON's one) and notify every developper that subscribe to it.

## How it's works

PyToMe have a list of website where it will fetch data(jobs/projects) and will notify developers with a frequency that will be configure.

## How to use it in production:

- First Suscribe to [PyToMe](https://github.com/pytome)
- Enjoy receiving offers;-)

## How to install it locally as a developper

You just need to hit theese commands: 
```shell
git clone https://github.com/Python-Cameroun/pytome
cd to/the/project/

# For Windows users, in the CLI hit this:
pm.bat

# For Windows users, in the CLI hit this:
sh ./pm.sh

#The script will do the rest for you!
```

## Dependencies

Theese are few dependencies used in this project :

- requests
- BeautifulSoup
- schedule
- Flask
- For launch the local server on index.html, this code use http-server (allready install in node_modules/ directory)

## TODO

- [OK] The Python Job with frequency
- [OK]  Base engine for web scrappers 
- [OK] Default webscrapper available ( githubjob and python.org job's scrapper )
- [ - ] Add Flask support
- [ - ] The Mailing system to notify all developpers subscribed on this app.
- [OK] The Web page where to suscribe to PyToMe.
- [OK] Saving Mails.
- [ - ] The Python Config (For personnalize notifications)
    - [ - ] The Type (Remote Jobs, full time, etc...).
    - [ - ] The country / city.
    - [ - ] The number of notifications.
    - [ - ] The delay from notifications.

## Rendering
<img src="assets/img/rendu.png" />

## Author
[Sanix-darker](https://github.com/sanix-darker)

## Contributors
[Adonis Simo (root)](https://github.com/simo97)

## Organization
[Python Cameroon](https://github.com/python-cameroun)

## License
Be free to Update/Use, fork this source code!
