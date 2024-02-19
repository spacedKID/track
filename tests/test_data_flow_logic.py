import unittest
from src.data_flow_logic import get_categories, get_sub_categories, get_trackable_objects

class TestDataFlowLogic(unittest.TestCase):

    def test_get_categories(self):
        categories = get_categories()
        self.assertTrue(len(categories) > 0)  # Assuming you have at least one category in your DB

    def test_get_sub_categories(self):
        # Assuming you know the ID of a category with sub-categories
        category_id = 1
        sub_categories = get_sub_categories(category_id)
        self.assertTrue(len(sub_categories) > 0)

    def test_get_trackable_objects(self):
        # Assuming you know the ID of a sub-category with trackable objects
        sub_category_id = 1
        trackable_objects = get_trackable_objects(sub_category_id)
        self.assertTrue(len(trackable_objects) > 0)

if __name__ == '__main__':
    unittest.main()
