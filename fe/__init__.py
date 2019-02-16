# -*- coding: utf-8 -*-
import os

from flask import Flask

# Create flask app

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Create dummy secrey key so we can use flash
app.config['SECRET_KEY'] = os.urandom(24)

from fe import views
