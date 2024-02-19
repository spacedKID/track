from models import Session, Category, SubCategory, TrackableObject

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
