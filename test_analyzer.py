import unittest
import os

def analyze_text():
    pass

class TextAnalysisTests(unittest.TestCase):
    """Test for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for then next methods to use"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w', 'utf-8') as f:
            f.write('Now we are engaged in a great civil war.\n'
            'testing whether that nation,\n'
            'or any nation so conceived and so dedicated,\n'
            'can long endure.')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.filename)
        finally:
            pass
    
    def test_function_runa(self):
        """Basic smoke test: does the function run."""
        analyze_text()

if __name__ == '__main__':
    unittest.main()