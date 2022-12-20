from fastapi import FastAPI
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import register_tortoise
from typing import List

from models import Todo

app = FastAPI()

# we can also create our own pydantic model using
#   tortoise, using this, we dont need our custom BaseModel any more
todo_pydantic = pydantic_model_creator(Todo, name = "Todo")
todo_pydanticIn = pydantic_model_creator(Todo, name = "TodoIn", exclude_readonly = True)

# Create, Read, Update, Delete

store_todo = []

@app.get('/')
async def home():
    return {"Hello": "World"}

@app.get('/todo/')
async def get_all_todos():
    return await todo_pydantic.from_queryset(Todo.all())

@app.post('/todo/')
async def create_todo(city: todo_pydanticIn):
    todo_obj = await Todo.create(**city.dict(exclude_unset=True))
    return await todo_pydantic.from_tortoise_orm(todo_obj)

@app.get('/todo/{todo_id}')
async def get_todo(todo_id: int):
    return await todo_pydantic.from_queryset_single(Todo.get(id=todo_id))

@app.delete('/todo/{todo_id}')
async def delete_city(todo_id: int):
    await Todo.filter(id=todo_id).delete()
    return {}

# @app.post('/todo/')
# async def create_todo(todo: todo_pydanticIn):
#     store_todo.append(todo)
#     return todo

# @app.post('/todo/', status_code=201)
# async def create_todo(todo: todo_pydantic):
#     return {
#         "name": todo.name,
#         "age": todo.age
#     }




# @app.get('/todo/',status_code=200)
# async def get_todos():
#     store_todo = await todo_pydantic.from_queryset(Todo.all())
#     return store_todo


# @app.post('/todo/')
# async def create_todo(todo: todo_pydantic):
#     store_todo.append(todo)
#     return todo

# @app.get('/todo/', response_model=List[todo_pydantic])
# async def get_all_todos():
#     return store_todo

# @app.get('/todo/{id}')
# async def get_todo(id: int):

#     try:
        
#         return store_todo
    
#     except:
        
#         raise HTTPException(status_code=404, detail="Todo Not Found")
    

# @app.put('/todo/{id}')
# async def update_todo(id: int, todo: todo_pydantic):

#     try:

#         store_todo[id] = todo
#         return store_todo[id]
    
#     except:
        
#         raise HTTPException(status_code=404, detail="Todo Not Found")


# @app.delete('/todo/{id}')
# async def delete_todo(id: int):

#     try:

#         obj = store_todo[id]
#         store_todo.pop(id)
#         return obj
    
#     except:
        
#         raise HTTPException(status_code=404, detail="Todo Not Found")

# todos = []

# @app.get('/')
# async def index():
#     return {"message": "Hello"}

# @app.post('/todo', status_code=201)
# async def create_todo(todo: CreateTodo):
#     return {
#         "name": todo.name,
#         "age": todo.age
#     }

# @app.get('/todo', response_model=List[CreateTodo])
# async def get_all_todos():
#     return todos


# @app.get('/todo',status_code=200)
# async def get_todos():
#     todos = await todo_pydantic.from_queryset(Todo.all())
#     return todos

# @app.get('/todo/{todo_id}',status_code=200)
# async def get_todo(todo_id:int):
#     todo = await todo_pydantic.from_queryset_single(Todo.get(id = todo_id))
#     return {'data' : todo}

# @app.delete('/todo/{todo_id}')
# async def delete_todo(todo_id: int):
#     await Todo.filter(id = todo_id).delete()
#     return {}


    # print(todo.json())
    # # exclude_unset will deal with null collumns if the user does not pass it in
    # todo_obj = await Todo.create(**todo.dict(exclude_unset = True))
    # response = await todo_pydantic.from_tortoise_orm(todo_obj)
    # return {'status' : 'ok', 'data' : response}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas = True,
    add_exception_handlers = True
)
