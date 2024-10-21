from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from helpers.lifespan import lifespan
from controllers import (
    data_controller
)


app = FastAPI(lifespan=lifespan)

app.include_router(data_controller.router, prefix="/api")