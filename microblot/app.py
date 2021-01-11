from fastapi import FastAPI

from microblot.routers import main, slack


app = FastAPI()


app.include_router(main.router)
app.include_router(slack.router)
