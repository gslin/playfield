#!/usr/bin/env python3

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

def ActiveFitnessJob():
    pass

scheduler = BackgroundScheduler()
scheduler.add_job(ActiveFitnessJob, 'interval', minutes=1)
scheduler.start()

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello, world!</p>'
