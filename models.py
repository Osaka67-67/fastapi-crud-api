#model represents table in our database

from datetime import datetime
from sqlalchemy import String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column 
from database import Base

class Post(Base):
    __tablename__="posts"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String)
    content:Mapped[str]=mapped_column(String)
    published: Mapped[bool] = mapped_column(server_default="TRUE", default=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=func.now(), server_default=func.now())   