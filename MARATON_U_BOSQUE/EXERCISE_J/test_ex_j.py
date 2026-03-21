import unittest
from unittest.mock import patch
from io import StringIO
from exercise_j import main

class TestMain(unittest.TestCase):

    @patch('sys.stdin', StringIO("1\n21\n"))
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        main()
        output = mock_stdout.getvalue()

        expected = "CASE 1: ODD"
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()