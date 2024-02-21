from database.models import Session, Category, SubCategory, TrackableObject, Entry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



def get_categories():
    session = Session()
    categories = session.query(Category).all()
    session.close()
    return [(category.id, category.name) for category in categories]

def get_sub_categories(category_id):
    session = Session()
    sub_categories = session.query(SubCategory).filter_by(category_id=category_id).all()
    session.close()
    return [(sub_category.id, sub_category.name) for sub_category in sub_categories]

def get_trackable_objects(sub_category_id):
    session = Session()
    trackable_objects = session.query(TrackableObject).filter_by(sub_category_id=sub_category_id).all()
    session.close()
    return [(trackable_object.id, trackable_object.name, trackable_object.data_type) for trackable_object in trackable_objects]

def add_category(name):
    session = Session()
    new_category = Category(name=name)
    session.add(new_category)
    try:
        session.commit()
        print(f"Added category: {name}")
    except Exception as e:
        print(f"Error adding category {name}: {e}")
        session.rollback()
        raise e
    finally:
        session.close()

def add_sub_category(name, category_id):
    session = Session()
    new_sub_category = SubCategory(name=name, category_id=category_id)
    session.add(new_sub_category)
    try:
        session.commit()
        print(f"Added sub-category: {name}")
    except Exception as e:
        print(f"Error adding sub-category {name}: {e}")
        session.rollback()
        raise e
    finally:
        session.close()


def add_trackable_object(name, sub_category_id, data_type):
    session = Session()
    new_object = TrackableObject(name=name, sub_category_id=sub_category_id, data_type=data_type)
    session.add(new_object)
    try:
        session.commit()
        print(f"Added trackable ojbect: {name}")
    except Exception as e:
        print(f"Error adding trackable object {name}: {e}")
        session.rollback()
        raise e
    finally:
        session.close()


def add_entry(datetime, category_id, sub_category_id, trackable_object_id, value):
    session = Session()
    # Fetch the name of the trackable object for printing
    trackable_object = session.query(TrackableObject).filter_by(id=trackable_object_id).first()
    trackable_object_name = trackable_object.name if trackable_object else "Unknown"

    new_entry = Entry(datetime=datetime, category_id=category_id, sub_category_id=sub_category_id, trackable_object_id=trackable_object_id, value=value)
    session.add(new_entry)
    try:
        session.commit()
        print(f"Entry added successfully for {trackable_object_name}.")
    except Exception as e:
        print(f"Failed to add entry for {trackable_object_name}: {e}")
        session.rollback()
    finally:
        session.close()
