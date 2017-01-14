import unittest

from create_box import create_box, hollow_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)

    # Add your own test using third_box_expected
    def test_big_box(self):
        self.assertEqual(create_box(3,24,'x'), third_box_expected)

first_hollow = """
****
*  *
****
""".lstrip()

second_hollow = """
@
""".lstrip()

third_hollow = """
xxxxxxxxxx
x        x
xxxxxxxxxx
""".lstrip()

class TestCreateBox1(unittest.TestCase):
    def test_box1(self):
        self.assertEqual(hollow_box(3, 4, '*'), first_hollow)

    def test_small_box1(self):
        self.assertEqual(hollow_box(1, 1, '@'), second_hollow)

    # Add your own test using third_box_expected
    def test_big_box1(self):
        self.assertEqual(hollow_box(3,10,'x'), third_hollow)
