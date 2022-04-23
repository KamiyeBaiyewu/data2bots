from os import EX_CANTCREAT
import unittest


#This block of code captures the "message" attribute from the existing json file and checks that other files follow the same schema
class TestMyFunctions(unittest.TestCase):
    def test_read_file_data(self):
        import json
        f = open('data/data_1.json')
        # This line converts json objects to a dictionary
        dict = json.load(f)

        req = {
            "required": "false"
        }
        app = {**dict["message"], **req}

        with open('sample.json', 'w') as json_file:
            json.dump(app, json_file)

        expected_output = sample.json

        actual_output = read_file_data(filename, 'example/path')

        self.assertEqual(actual_output, expected_output)

       # path = "test"
        #filename = testcase.json
