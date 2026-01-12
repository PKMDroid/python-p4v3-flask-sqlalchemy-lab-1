import pytest
from app import app, db
from models import Earthquake


@pytest.fixture(autouse=True)
def setup_database():
    """Set up test database before each test and tear down after."""
    with app.app_context():
      
        db.create_all()
        
      
        db.session.query(Earthquake).delete()
        
       
        earthquakes = [
            Earthquake(id=1, magnitude=9.5, location="Chile", year=1960),
            Earthquake(id=2, magnitude=9.2, location="Alaska", year=1964),
        ]
        
        db.session.bulk_save_objects(earthquakes)
        db.session.commit()
        
        yield  
        
    
        db.session.remove()
        db.drop_all()