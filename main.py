#CRUD api database:postgres use psycogp for now (will use orm (this is learning phase rn))
 
from fastapi import FastAPI , status , HTTPException ,Depends
from pydantic import BaseModel
import psycopg
from psycopg.rows import dict_row
from time import sleep
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import os
import models
from database import engine,get_db
from sqlalchemy import select

models.Base.metadata.create_all(bind=engine)

app=FastAPI()
load_dotenv()


while True:
    try:

        conn=psycopg.connect(
            user=os.getenv("user"),
            password=os.getenv("password"),
            dbname=os.getenv("dbname"),
            host=os.getenv("host"),
            row_factory=dict_row
        )
        cursor=conn.cursor()
        print("sucessfull connection establised")
        break
    except Exception as e:
        print("something wrong")
        sleep(2)

class Check_format(BaseModel):
    title:str
    content:str | None = None
    id:int | None = None
    published:bool = True


@app.get("/sqlalchemy")
def test_posts(db:Session=Depends(get_db)):
    statement=select(models.Post)
    posts = db.scalars(statement).all()
    return{"data":posts}


#C#Creating posts    

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(posts:Check_format):
    cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(posts.title,posts.content,posts.published))
    created_post=cursor.fetchone()
    conn.commit()
    return{"data":created_post}

#R#retreiving one individual post

@app.get("/posts/{id}")
def get_post_by_id(id:int): 
   cursor.execute(""" SELECT * FROM posts WHERE id = %s ;""",[id])
   get_post=cursor.fetchone()
   if get_post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id with {id} does not exist")
   return get_post

#R#getting all posts #get req

@app.get("/posts")
def get_all_posts():
    cursor.execute("""SELECT * FROM posts;""")
    get_posts=cursor.fetchall()
    return{"data":get_posts}

#D#delete the post

@app.delete("/posts/{id}")
def for_deleting_posts(id:int):
   cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(id,))
   deleted_post=cursor.fetchone()
   conn.commit()
   if deleted_post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
   
   return{"deleted post sucessfully":deleted_post}

#U#update the post

@app.put("/posts/{id}")
def for_updating_posts(id:int,post:Check_format):
    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s  WHERE id = %s  RETURNING *""",(post.title,post.content,post.published,id))
    updated_post=cursor.fetchone()
    conn.commit()

    if updated_post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
    return {"message": "Updated successfully", "updated_post": updated_post}


    