__version__ = '1.0.0'

import os
import importlib

from flask import Flask
from application.tools import security


class PyToMe(Flask):
    pass


app = PyToMe(__name__, template_folder='views', static_folder='assets')

# CONFIGURATIONS
app.config["SECRET_KEY"] = security.secret_key
app.jinja_env.globals["csrf_token"] = security.generate_token

# LOAD CONTROLLER
from application.api import *

# DEBUG MODE
app.debug = True
