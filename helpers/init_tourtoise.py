from tortoise import Tortoise
import os


async def init_tortoise():
    await Tortoise.init(
        db_url=os.getenv("DATABASE_URL"),
        modules={
            "models": [
                "models.advertiser",
                "models.affiliate",
                "models.compaign",
                "models.contact",
                "models.lead",
                "models.lead_data",
                "models.offer",
                "models.setting",
                "models.verticle",
                "models.data_update_log",
            ]
        },
    )
    await Tortoise.generate_schemas()
