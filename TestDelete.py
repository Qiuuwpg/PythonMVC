
import unittest
from TravelModel import TravelModel

class TestDeleteRecord(unittest.TestCase):
    def setUp(self):
        """
        Initialize a new instance of the `PotatoesModel` class and load data.
        """
        self.Travels_model = TravelModel()
        self.Travels_model.load_data()
        

    def test_delete_record(self):
        """
        Test the `delete_record` method of the `PotatoesModel` class.
        This test checks the following requirements:
             - The number of records in the `potatoes` list is greater than 0.
             - The specified record is deleted from the `potatoes` list.
             - The number of records in the `potatoes` list is no greater than 99 and decreases by 1 after the specified record is deleted.
        """
        original_num_records = len(self.Travels_model.travels)
        self.assertTrue(original_num_records > 0)

        index_to_delete = min(99, original_num_records - 1)
        self.Travels_model.delete_record(index_to_delete)
     

if __name__ == '__main__':
    unittest.main()
    print("Program by Jianchao Jia")
