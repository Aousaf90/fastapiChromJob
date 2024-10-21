from tortoise import run_async
from helpers.init_tourtoise import init_tortoise
from helpers.fetch_data import fetch_all


async def main():
    await init_tortoise()
    await fetch_all()


run_async(main())