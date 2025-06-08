#!/usr/bin/env python3

from . import db
from . import vault
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from sqlalchemy import text

import requests
import time

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

        cnt = res.json()[0]['total']
        now = int(time.time())

        engine = db.DB().getEngine()
        with engine.connect() as c:
            c.execute(text('SET AUTOCOMMIT = ON'))
            c.execute(
                text('INSERT INTO activefitness_count (cnt, created_at) VALUES (:cnt, :created_at);'),
                {'cnt': cnt, 'created_at': now}
            )

jobs = MyJobs()

scheduler = BackgroundScheduler()
scheduler.add_job(jobs.ActiveFitnessJob, 'interval', minutes=1)
scheduler.start()

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello, world!</p>'

@app.route('/activefitness.json')
def activefitness():
    engine = db.DB().getEngine()
    with engine.connect() as c:
        rs = c.execute(text('SELECT COUNT(*) FROM activefitness_count ORDER BY created_at DESC;'))
        return { 'cnt': rs.fetchone()[0] }
