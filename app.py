#!/usr/bin/env python3

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

import json
import requests

class MyJobs:
    vault_json = '/srv/vault/playfield/default.current.json'
    vault = {}

    def __init__(self):
        with open(self.vault_json, 'r') as f:
            self.vault = json.load(f)

    def ActiveFitnessJob(self):
        api_secret = self.vault['ACTIVE_FITNESS_API_SECRET']
        api_seed = self.vault['ACTIVE_FITNESS_API_SEED']
        api_currentcount_url = self.vault['ACTIVE_FITNESS_API_CURRENTCOUNT_URL']

        res = requests.get(
            api_current_count_url,
            headers={'x-api-seed': api_seed, 'x-api-secret': api_secret}
        )

        with open('/tmp/active_fitness_currentcount.txt', 'a') as f:
            f.write(res.text)
            f.write('\n')

jobs = MyJobs()

scheduler = BackgroundScheduler()
scheduler.add_job(jobs.ActiveFitnessJob, 'interval', minutes=1)
scheduler.start()

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello, world!</p>'
