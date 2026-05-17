import unittest

from main import concatenate_strings
from main import get_string_length
from main import reverse_string
from main import count_vowels
from main import count_consonants


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
        self.assertEqual(concatenate_strings("qwe", "asd", "😊"), "qweasd😊")

    def test_many_arguments_concatenation_performance_like(self):
        parts = ["x"] * 1000
        self.assertEqual(concatenate_strings(*parts), "x" * 1000)

    def test_non_string_argument_raises_type_error(self):
        with self.assertRaises(TypeError):
            concatenate_strings("a", 1)

    def test_get_string_length(self):
        self.assertEqual(get_string_length("hello"), 5)
        self.assertEqual(get_string_length(""), 0)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels(""), 0)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("hello"), 3)
        self.assertEqual(count_consonants(""), 0)


if __name__ == "__main__":
    unittest.main()
