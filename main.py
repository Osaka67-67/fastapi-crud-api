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

class Check_format(BaseModel):
    title:str
    content:str | None = None
    id:int | None = None
    published:bool = True





#C#Creating posts    

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Check_format,db: Session = Depends(get_db)):
    new_post=models.Post(
        title=post.title,
        content=post.content,
        published=post.published,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}
    

#R#retreiving one individual post

@app.get("/posts/{id}")
def get_post_by_id(id:int,db: Session = Depends(get_db)): 
   statement=select(models.Post).where(models.Post.id==id)
   post = db.scalars(statement).first()
   if post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id with {id} does not exist")
   return {"data":post} 

#R#getting all posts #get req

@app.get("/posts")
def test_posts(db:Session=Depends(get_db)):
    statement=select(models.Post)
    posts = db.scalars(statement).all()
    return{"data":posts}

#D#delete the post

@app.delete("/posts/{id}")
def for_deleting_posts(id:int,db:Session=Depends(get_db)):
   statement=delete(models.Post).where(models.Post.id==id).returning(models.Post)
   deleted_post = db.scalars(statement).first()

   if deleted_post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
   
   db.commit()
   return{"deleted post":deleted_post} #idk why but its not returning back the deleted_post


#U#update the post

@app.put("/posts/{id}")
def for_updating_posts(id:int,post:Check_format,db:Session=Depends(get_db)):
    statement=update(models.Post).where(models.Post.id==id).values(title=post.title,content=post.content,published=post.published).returning(models.Post)
    
    updated_post = db.scalars(statement).first()
    
    if updated_post is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
    db.commit()
    return {"message": "Updated successfully", "updated_post": updated_post}



    