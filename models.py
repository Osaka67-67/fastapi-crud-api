#model represents table in our database

from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column 
from database import Base

class Post(Base):
    __tablename__="posts"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(nullable=False)
    content:Mapped[str]=mapped_column(nullable=False)
    published: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())       