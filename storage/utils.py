# storage/utils.py

from sqlalchemy.orm import sessionmaker
from storage.databases import Categories, engine

# Set up the database session
Session = sessionmaker(bind=engine)
session = Session()

def get_all_categories():
    """Fetch all categories from the database."""
    return session.query(Categories).all()

def add_category(name):
    """Add a new category to the database."""
    new_category = Categories(name=name)
    session.add(new_category)
    session.commit()