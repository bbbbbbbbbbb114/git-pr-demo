import unittest

from greet import greet


class GreetingTests(unittest.TestCase):
    def test_names(self):
        cases = [
            ("Alice", "Hello, Alice!"),
            ("  Alice  ", "Hello, Alice!"),
            ("   ", "Hello, Guest!"),
            ("", "Hello, Guest!"),
        ]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(greet(name), expected)


if __name__ == "__main__":
    unittest.main()
