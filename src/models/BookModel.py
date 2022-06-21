# src/models/BookrModel.py
import datetime
from . import db

class BookModel(db.Model):
  """
  Book Model
  """

  # table name
  __tablename__ = 'books'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  author = db.Column(db.String(128), unique=True, nullable=False)
  pages = db.Column(db.String(128), nullable=True)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data.get('name')
    self.author = data.get('author')
    self.pages = data.get('pages')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_books():
    return BookModel.query.all()

  @staticmethod
  def get_one_book(id):
    return BookModel.query.get(id)

  
  def __repr(self):
    return '<id {}>'.format(self.id)
