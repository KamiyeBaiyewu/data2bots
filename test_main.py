from os import EX_CANTCREAT
import unittest


class TestMyFunctions(unittest.TestCase):
    def test_read_file_data(self):
        import json
        f = open('data/data_1.json')
        # this gives json object as a dictionary
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
