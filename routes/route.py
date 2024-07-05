from fastapi import APIRouter,status
from fastapi.responses import  JSONResponse
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

todo_router = APIRouter()


@todo_router.get('/',response_description='get a list of todos')
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

@todo_router.post('/')
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return JSONResponse(status_code=status.HTTP_201_CREATED,content={'message':'todo created'})
