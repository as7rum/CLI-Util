import unittest
from unittest import mock
from file_service import FileService

class FileServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.file_service = FileService()

    def test_get_list_of_names(self):
        # Mock the get_list_of_items_from_yaml_file method
        with mock.patch.object(FileService, '_FileService__get_list_of_items_from_yaml_file') as mock_method:
            mock_method.return_value = [{'name': 'Task 1'}, {'name': 'Task 2'}, {'name': 'Task 3'}]
            result = self.file_service.get_list_of_names('test.yaml')
            expected_result = ['Task 1', 'Task 2', 'Task 3']
            self.assertEqual(result, expected_result)



if __name__ == 'main':
    unittest.main()