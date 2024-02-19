from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, SubCategory, TrackableObject, Entry
import datetime

# Replace 'sqlite:///my_tracking_app.db' with your actual database URI
engine = create_engine('sqlite:///track.db')
Session = sessionmaker(bind=engine)
session = Session()

def insert_test_data():
    # Clear existing data (optional)
    session.query(Entry).delete()
    session.query(TrackableObject).delete()
    session.query(SubCategory).delete()
    session.query(Category).delete()
    session.commit()

    # Insert Categories
    category1 = Category(name="Health")
    category2 = Category(name="Productivity")
    session.add_all([category1, category2])
    session.commit()

    # Insert Sub-Categories
    sub_category1 = SubCategory(name="Diet", category=category1)
    sub_category2 = SubCategory(name="Exercise", category=category1)
    sub_category3 = SubCategory(name="Work", category=category2)
    session.add_all([sub_category1, sub_category2, sub_category3])
    session.commit()

    # Insert Trackable Objects
    trackable_object1 = TrackableObject(name="Calories", sub_category=sub_category1, data_type="integer")
    trackable_object2 = TrackableObject(name="Miles Run", sub_category=sub_category2, data_type="float")
    trackable_object3 = TrackableObject(name="Hours Worked", sub_category=sub_category3, data_type="float")
    session.add_all([trackable_object1, trackable_object2, trackable_object3])
    session.commit()

def query_test_data():
    # Query Categories
    categories = session.query(Category).all()
    print("Categories:")
    for category in categories:
        print(f"- {category.name}")

    # Query Sub-Categories
    sub_categories = session.query(SubCategory).all()
    print("\nSub-Categories:")
    for sub_category in sub_categories:
        print(f"- {sub_category.name} (Category: {sub_category.category.name})")

    # Query Trackable Objects
    trackable_objects = session.query(TrackableObject).all()
    print("\nTrackable Objects:")
    for trackable_object in trackable_objects:
        print(f"- {trackable_object.name} (Sub-Category: {trackable_object.sub_category.name}, Data Type: {trackable_object.data_type})")

if __name__ == "__main__":
    insert_test_data()
    query_test_data()
