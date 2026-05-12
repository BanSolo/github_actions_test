import unittest
from main import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_no_arguments_returns_empty_string(self):
        self.assertEqual(concatenate_strings(), "")

    def test_single_argument_returns_same_string(self):
        self.assertEqual(concatenate_strings("hello"), "hello")

    def test_multiple_arguments(self):
        cases = [
            (("a", "b", "c"), "abc"),
            (("first", "", "last"), "firstlast"),
            (("",), ""),
            ((" ", "space"), " space"),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                self.assertEqual(concatenate_strings(*args), expected)

    def test_unicode_and_special_characters(self):
        self.assertEqual(concatenate_strings("пр", "ивет", "😊"), "привет😊")

    def test_many_arguments_concatenation_performance_like(self):
        parts = ["x"] * 1000
        self.assertEqual(concatenate_strings(*parts), "x" * 1000)

    def test_non_string_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            concatenate_strings("a", 1)

if __name__ == "__main__":
    unittest.main()