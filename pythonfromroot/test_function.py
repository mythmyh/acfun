from ontime2 import start_quotes
from apscheduler.schedulers.blocking import BlockingScheduler
schedule = BlockingScheduler()
schedule.add_job(start_quotes, 'cron', month='1-12', day='*', hour='0-23', minute='59')
schedule.start()
