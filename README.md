# Garden Python

Garden Python is a set of scripts connected to the [GardenPi Project](https://github.com/mycobee/garden_pi_be.git).  The scripts are implemented as cron jobs to send sensor data to the Rails API, take photos, and pick up jobs from the database for execution. 

## Getting Started

`git clone https://github.com/mycobee/garden_python`

### Installing

Once the repository is cloned to your raspberry pi, you will need to implement the jobs with cron

Open your crontab for editing
```
crontab -e
```

And edit it with intended script data

```
* * * * * python3 ~/garden_py/lib/data_runner.py

0 * * * * python3 ~/garden_py/lib/picture_taker.py

* * * * * python3 ~/garden_py/lib/job_runner.py
* * * * * sleep 10; python3 ~/garden_py/lib/job_runner.py
* * * * * sleep 20; python3 ~/garden_py/lib/job_runner.py
* * * * * sleep 30; python3 ~/garden_py/lib/job_runner.py
* * * * * sleep 40; python3 ~/garden_py/lib/job_runner.py
* * * * * sleep 50; python3 ~/garden_py/lib/job_runner.py
```

## Built With

* Python3
