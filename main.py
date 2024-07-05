from fastapi import FastAPI
from routes.route import todo_router

app = FastAPI()

app.include_router(todo_router)
