from io import StringIO
import sys
import unittest

from assessment import printName, multiplication_pattern, number_pyramid, triangle

class TestMyFunctions(unittest.TestCase):

    def test_printName(self):
        file_name = "test_name.txt"
        with open(file_name, "w") as file:
            file.write("John Doe")
        
        result = printName(file_name)
        
        self.assertEqual(result, "John Doe")

    def test_multiplication_pattern(self):

        text_capture = StringIO()
        sys.stdout = text_capture
        multiplication_pattern(5)
        self.assertEqual("1  \n2  4  \n3  6  9  \n4  8  12  16  \n5  10  15  20  25  \n",text_capture.getvalue())


    def test_number_pyramid(self):

        expected_output = "1 \n2 3 \n4 5 6 \n7 8 9 10 \n"
        text_capture = StringIO()
        sys.stdout = text_capture
        number_pyramid(5)
        self.assertEqual("1 \n\n2 3 \n\n4 5 6 \n\n7 8 9 10 \n\n11 12 13 14 15 \n\n",text_capture.getvalue())


    def test_triangle(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        triangle(5)
        self.assertEqual("    *\n   **\n  ***\n ****\n*****\n",text_capture.getvalue())
        

if __name__ == '__main__':
    unittest.main()
