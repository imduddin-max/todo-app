import unittest
from utils import add_numbers, validate_email


class TestAddNumbers(unittest.TestCase):
    """Unit tests for the add_numbers function."""

    def test_add_positive_integers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -4), -5)

    def test_add_floats(self):
        self.assertAlmostEqual(add_numbers(1.5, 2.3), 3.8)

    def test_add_non_numeric_raises_type_error(self):
        with self.assertRaises(TypeError):
            add_numbers("a", 1)


class TestValidateEmail(unittest.TestCase):
    """Unit tests for the validate_email function."""

    def test_valid_email(self):
        self.assertTrue(validate_email("user@example.com"))

    def test_missing_at_sign(self):
        self.assertFalse(validate_email("userexample.com"))

    def test_missing_domain(self):
        self.assertFalse(validate_email("user@"))

    def test_non_string_returns_false(self):
        self.assertFalse(validate_email(12345))


if __name__ == "__main__":
    unittest.main()
