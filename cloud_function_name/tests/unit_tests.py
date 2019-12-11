"""
Call tests as:
    python -m cloud_function_name.tests.unit_tests
"""
from ..main import main_function, sec_function
from unittest.mock import patch
from dotenv import load_dotenv
import unittest
import os


class CloudTest(unittest.TestCase):
    
    def setUp(self):
        """
        You can setup any thing in here to run before each test
        """
        load_dotenv()
        print('Hi from setUp')

    @patch('cloud_function_name.main.sec_function', return_value='potato')
    def test_main_function(self, mocked_sec_function):
        """
        This is an example on how to mock a function
        basically we substitute the return value of main.sec_function
        to potato
        """
        # main_function will call sec_function and return its value
        main_fun_return = main_function('req')
        # our expected return is the mocked return value we called
        self.assertEqual(main_fun_return, 'potato')
        # but we need to test if we called sec_fun passing the right param
        # so let's do it!
        mocked_sec_function.assert_called_once_with('reqa')

    def test_sec_function(self):
        """
        Now we need to test if sec_function is doing 
        what it is supposed to do!
        """
        sec_fun_return = sec_function('hello')
        self.assertEqual(sec_fun_return, 'hellohello')


if __name__ == '__main__':
    unittest.main()