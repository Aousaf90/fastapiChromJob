import asyncio
from fastapi import FastAPI
from helpers.init_tourtoise import init_tortoise
from helpers.schedule import scheduler, schedule_daily, schedule_yearly
from helpers.fetch_data import fetch_all, fetch_yearly_data, fetch_weekly_data


async def lifespan(app):
    await init_tortoise()

    schedule_daily(fetch_weekly_data)
    schedule_yearly(fetch_yearly_data)

    loop = asyncio.get_event_loop()
    loop.create_task(start_scheduler())
    yield
    await stop_scheduler()


async def start_scheduler():
    scheduler.start()


async def stop_scheduler():
    scheduler.shutdown()


# from helpers.init_tourtoise import init_tortoise
# import asyncio
# from helpers.schedule import scheduler, schedule_daily, schedule_yearly
# from helpers.fetch_data import fetch_all, fetch_yearly_data


# async def lifespan(app):
#     await init_tortoise()
#     schedule_daily(fetch_all)
#     schedule_yearly(fetch_yearly_data)
#     loop = asyncio.get_event_loop()
#     loop.run_in_executor(None, scheduler.start)
#     yield
#     print("Process Ended")
