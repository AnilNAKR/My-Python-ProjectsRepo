# from sqlalchemy import String, Integer, Float, Column
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(250), unique=True, nullable=False)
#     author = Column(String(250), nullable=False)
#     rating = Column(Float, nullable=False)
#
#     def __repr__(self):
#         return f"<Book {self.title}>"
