#this file is the runner for the jobs endpoint request.
#currently the only exisiting type of is for triggering a relay

from relay_job import RelayJob
import requests
import json

#response comes back with some sort of hash similar {job: {type: water, duration: 60}}

#create class water_job.py

#initialize water_job.py with job.duration
r = requests.get('https://garden-pi-be.herokuapp.com/api/v1/gardens/1/jobs?seconds_ago=10')
data = json.loads(r.text)

print(data['data'])

if data['data']:
    currentJob = RelayJob(10)
    currentJob.triggerRelay()
