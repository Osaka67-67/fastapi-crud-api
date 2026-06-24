#retreiving one individual post
#getting all posts #get req
#creating a post   #post req

from fastapi import FastAPI , HTTPException ,status,Response
from pydantic import BaseModel 
#from typing import Optional         now we use | pipe in latest python ver
from random import randrange

app = FastAPI()

database=[{"name":"Prerit","age":18,"id":1},{"fav_anime":"Maid_Sama","id":2}]

@app.get("/")
def home_page():
    return{"message":"this is home page"}

@app.get("/posts")
def get_posts():
    return{"data":database}

class Format(BaseModel):
    title: str
    content: str
    #tags: Optional[str] = None old way now we use | pipe latest ver python hehe
    tags: str | None = None
    

#post req
'''
this func takes usr data and converts json format data into dict and then store it in list db
for default value you can use '=True or =False  '

'''
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def post_posts(usr_added_data:Format):
    usr_added_data_dict=usr_added_data.model_dump()
    usr_added_data_dict["id"]=randrange(0,10000)
    database.append(usr_added_data_dict)
    print(database)
    return{"message":usr_added_data_dict}

#func to find post by id
def find_id(id):
    for i in database:
        if i["id"]==id:
            return i
        
@app.get("/posts/{id}")#path param
def get_post_by_id(id:int):# id:int caz if we dont then id will be passed as string and error 
    post_by_id=find_id(id)
    if not post_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found!")

    return{"message":post_by_id}

def find_index_post(id):
    for i , p in enumerate(database):
        if p["id"]==id:
            return i



@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exit")
    database.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

@app.put("/posts/{id}")

def update_post(id:int,post:Format):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exit")
    dict_post=post.model_dump()
    dict_post["id"]=id
    database[index]=dict_post
    print(dict_post)
    return{"message":dict_post}

