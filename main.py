#C#creating a post   #post req
#R#retreiving one individual post
#R#getting all posts #get req
#U#update the post
#D#delete the post

import os
from dotenv import load_dotenv
from fastapi import FastAPI , status , HTTPException
from pydantic import BaseModel
import random
import psycopg
from psycopg.rows import dict_row
from time import sleep


app=FastAPI()
load_dotenv()

#in memory database -.-

database = [
    {"title": "My First Post", "content": "Hello world", "id": 1},
    {"title": "Learning FastAPI", "content": "It is going great!", "id": 2}
]


while True:

    try:
        conn = psycopg.connect(
            host=os.getenv("host"),
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            row_factory=dict_row      
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as e:
        print(f"Database connection failed: {e}")
        sleep(2)


class Check_format(BaseModel):
    title:str
    content:str | None = None
    id:int | None = None
    published:bool = True


def generate_id():
    for i in database:
        if i['id']== None:
            gen_num=random.randrange(1,1000000)
            i['id'] = gen_num
            
def find_post(id): 
    for i in database:
        if i["id"]== id:
            return i
       


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(posts:Check_format):
    cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s, %s ,%s) RETURNING * """,(posts.title,posts.content,posts.published))
    new_post=cursor.fetchone()
    conn.commit()
    return{"post added sucessfully":new_post}
    
#R#retreiving one individual post

@app.get("/posts/{id}")
def get_post_by_id(id:int):
   var=find_post(id)
   if var is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id with {id} does not exist")
   print(var) #not imp but i just wanted to see output hehe
   return var

#R#getting all posts #get req

@app.get("/posts")
def get_all_posts():
    cursor.execute(""" SELECT * FROM posts""")
    posts=cursor.fetchall()
    print(posts)
    return {"posts":posts}

def find_index(id):
    for i,j in enumerate(database):#i is index and j is dict
        if j["id"]==id:
            return i #returns index of the id 

#D#delete the post

@app.delete("/posts/{id}")
def for_deleting_posts(id:int):
   index=find_index(id)
   if index is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
   deleted_data=database.pop(index)
   return{"deleted post sucessfully":deleted_data}

#U#update the post

@app.put("/posts/{id}")
def for_updating_posts(id:int,userr_data:Check_format):
    index=find_index(id)
    if index is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
    user_data_dictt=userr_data.model_dump()
    print(user_data_dictt)
    user_data_dictt["id"]=id
    database[index]=user_data_dictt
    print(user_data_dictt)
    return {"message": "Updated successfully", "data": user_data_dictt}
    