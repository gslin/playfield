#!/usr/bin/env python3

from . import vault
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

import requests

class MyJobs:
    def ActiveFitnessJob(self):
        v = vault.Vault().getVault()

        api_secret = v['ACTIVE_FITNESS_API_SECRET']
        api_seed = v['ACTIVE_FITNESS_API_SEED']
        api_currentcount_url = v['ACTIVE_FITNESS_API_CURRENTCOUNT_URL']

        res = requests.get(
            api_currentcount_url,
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
