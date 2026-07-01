#CRUD api database:postgres use psycogp for now (will use orm (this is learning phase rn))
from typing import List
from fastapi import FastAPI , status , HTTPException ,Depends
# from pydantic import BaseModel
import psycopg
from psycopg.rows import dict_row
from time import sleep
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import os
import models , schemas
from database import engine,get_db
from sqlalchemy import select,delete,update

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

#C#Creating posts    

@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db)):
    new_post=models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    

#R#retreiving one individual post

@app.get("/posts/{id}",response_model=schemas.Post)
def get_post_by_id(id:int,db: Session = Depends(get_db)): 
   statement=select(models.Post).where(models.Post.id==id)
   post = db.scalars(statement).first()
   if post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id with {id} does not exist")
   return post

#R#getting all posts #get req

@app.get("/posts",response_model=List[schemas.Post])
def test_posts(db:Session=Depends(get_db)):
    statement=select(models.Post)
    posts = db.scalars(statement).all()
    return posts

#D#delete the post

@app.delete("/posts/{id}")
def for_deleting_posts(id:int,db:Session=Depends(get_db)):
   statement=delete(models.Post).where(models.Post.id==id).returning(models.Post)
   deleted_post = db.scalars(statement).first()

   if deleted_post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
   
   db.commit()
   return deleted_post #idk why but its not returning back the deleted_post


#U#update the post

@app.put("/posts/{id}",response_model=schemas.Post)
def for_updating_posts(id:int,post:schemas.PostCreate,db:Session=Depends(get_db)):
    statement=update(models.Post).where(models.Post.id==id).values(**post.model_dump()).returning(models.Post)
    updated_post = db.scalars(statement).first()
    if updated_post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
    db.commit()
    return updated_post



     