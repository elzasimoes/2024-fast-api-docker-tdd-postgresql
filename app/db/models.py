from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Category(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "categories"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    slug = Column("slug", String, nullable=False)
