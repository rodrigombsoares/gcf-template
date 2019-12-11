"""
python -m cloud_function_name.tests.integration_tests
"""
from ..main import main_function
from dotenv import load_dotenv
import unittest

load_dotenv()

assert main_function('hi') == 'hiahia'