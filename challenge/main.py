from fastapi import FastAPI
from . import models
from .database import engine
from .routers import challenge, user, health


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(health.router)
app.include_router(challenge.router)
app.include_router(user.router)
