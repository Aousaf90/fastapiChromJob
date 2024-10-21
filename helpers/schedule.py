import asyncio
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from typing import Callable

app = FastAPI()

scheduler = AsyncIOScheduler()


def schedule_daily(callback: Callable[[], None]):
    """
    Schedule the given callback function to be executed every 1 minute.
    """
    print('Minutely scheduler')
    trigger = CronTrigger(hour="*/2")
    scheduler.add_job(callback, trigger, id="minutely_trigger")


def schedule_yearly(callback: Callable[[], None]):
    """
    Schedule the given callback function to be executed once a year.
    """
    yearly_trigger = CronTrigger(day_of_week="sun", hour=0, minute=00, second=0)
    scheduler.add_job(callback, yearly_trigger, id="yearly_trigger")







# _______________________________
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
# from typing import Callable
# from apscheduler.schedulers.asyncio import AsyncIOScheduler


# scheduler = BackgroundScheduler()
# async_scheduler = AsyncIOScheduler()

# def schedule_daily(callback: Callable[[], None]):
#     """
#     Schedule the given callback function to be executed once a day.
#     """
#     trigger = CronTrigger(hour=2, minute=0, second=0)
#     scheduler.add_job(callback, trigger, id='daily_trigger')


# def schedule_yearly(callback: Callable[[], None]):
#     """
#     Schedule the given callback function to be executed once a year.
#     """
#     yearlly_trigger = CronTrigger(day_of_week='mon', hour=7, minute=10, second=00)
#     async_scheduler.add_job(callback, yearlly_trigger, id='yearly_trigger')
#     print("Yearly job scheduled.")
