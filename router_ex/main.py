from fastapi import FastAPI
import routers.example_router as re


app = FastAPI()

app.include_router(re.router)



