from apscheduler.schedulers.blocking import BlockingScheduler
import os


def run():
    os.chdir('/home/mayinghao/bilibili/bilibili/spiders/')
    os.system('python cmd_line_house.py')


schedule = BlockingScheduler()
schedule.add_job(run, 'interval', seconds=1800)
schedule.start()
