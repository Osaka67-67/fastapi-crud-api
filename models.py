#model represents table in our database

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
class Post(Base):
    __tablename__="posts"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String)
    content:Mapped[str]=mapped_column(String)
    published:Mapped[bool]=mapped_column(server_default="True",default=True)