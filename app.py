# imports
#  flask used to server and integrate with frontend
from flask import flask, render_template, request, Response, url_for, redirect
# used to send long operations in parallel thread so that code does'nt stop
import threading
# flask_cors. cross_origin used to deploy so that api can be hit from anywhere in the world
from flask_cors import cross_origin
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# initializing flask app
app = flask(__name__)

# selenium 