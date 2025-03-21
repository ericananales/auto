# test_main.py

import unittest
from main import concatenate_words  # Importing the concatenate_words function

class TestMain(unittest.TestCase):
    
    # Test case for the concatenate_words function
    def test_concatenate_words(self):
        self.assertEqual(concatenate_words('Hello', 'World'), 'Hello World')  # Check if 'Hello' + 'World' = 'Hello World'
        self.assertEqual(concatenate_words('Good', 'Morning'), 'Good Morning')  # Check if 'Good' + 'Morning' = 'Good Morning'
        self.assertEqual(concatenate_words('Python', 'Rocks'), 'Python Rocks')  # Check if 'Python' + 'Rocks' = 'Python Rocks'

if __name__ == '__main__':
    unittest.main()  # This runs all the test cases when the script is executed
