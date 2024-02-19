from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, SubCategory, TrackableObject, Entry
import datetime
import random

# !! includes lines deleting existing data -- run at your own risk !!

# creates two categories, three sub_categories, and three trackable_objects
# populates N rows in entries table for each of three trackable objects
# prints those table entries for visual inspection

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

def insert_entries():
    # Fetch TrackableObjects by name
    calories_obj = session.query(TrackableObject).filter_by(name="Calories").first()
    miles_run_obj = session.query(TrackableObject).filter_by(name="Miles Run").first()
    hours_worked_obj = session.query(TrackableObject).filter_by(name="Hours Worked").first()

    # Generate 5 entries for each TrackableObject with random data
    for _ in range(5):
        entry_calories = Entry(
            category_id=calories_obj.sub_category.category_id,
            sub_category_id=calories_obj.sub_category_id,
            trackable_object_id=calories_obj.id,
            value=str(random.randint(1000, 3000))  # Calories
        )
        entry_miles_run = Entry(
            category_id=miles_run_obj.sub_category.category_id,
            sub_category_id=miles_run_obj.sub_category_id,
            trackable_object_id=miles_run_obj.id,
            value=str(random.uniform(1.0, 10.0))  # Miles Run
        )
        entry_hours_worked = Entry(
            category_id=hours_worked_obj.sub_category.category_id,
            sub_category_id=hours_worked_obj.sub_category_id,
            trackable_object_id=hours_worked_obj.id,
            value=str(random.uniform(0.5, 12.0))  # Hours Worked
        )
        session.add_all([entry_calories, entry_miles_run, entry_hours_worked])

    session.commit()

def query_entries():
    # Query and print Entries with full details
    entries = session.query(Entry).all()
    print("\nEntries:")
    for entry in entries:
        # Fetch the trackable object, sub-category, and category for each entry
        trackable_object = session.query(TrackableObject).filter_by(id=entry.trackable_object_id).first()
        sub_category = session.query(SubCategory).filter_by(id=trackable_object.sub_category_id).first()
        category = session.query(Category).filter_by(id=sub_category.category_id).first()

        # Print full path details
        print(f"{entry.datetime} | {category.name} > {sub_category.name} > "
              f"{trackable_object.name} = {entry.value}")

if __name__ == "__main__":
    insert_test_data()  # Ensure test data is present
    insert_entries()  # Insert entries with random data
    query_test_data()  # Query and print Categories, Sub-Categories, and Trackable Objects
    query_entries()  # Query and print Entries
