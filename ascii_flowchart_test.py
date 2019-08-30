import unittest

from ascii_flowchart import ItemRectangle, Item


class ItemRectangleTest(unittest.TestCase):
    def test_zero_arguments(self):
        shape = ItemRectangle()
        self.assertEqual(shape.x, 10)
        self.assertEqual(shape.y, 5)

    def test_max_x(self):
        shape = ItemRectangle(x=Item.max_x*2)
        self.assertEqual(shape.x, Item.max_x)

    def test_max_y(self):
        shape = ItemRectangle(y=Item.max_y*2)
        self.assertEqual(shape.y, Item.max_y)

    def test_max_padding_x(self):
        shape = ItemRectangle(padding_x=Item.max_padding_x*2)
        self.assertEqual(shape.padding_x, Item.max_padding_x)

    def test_max_padding_y(self):
        shape = ItemRectangle(padding_y=Item.max_padding_y*2)
        self.assertEqual(shape.padding_y, Item.max_padding_y)

    def test_tab_character_sanitize(self):
        shape = ItemRectangle(text='a\t\t\b')
        self.assertEqual('\t' in ''.join(shape.text), False)

    def test_only_first_character_for_x(self):
        shape = ItemRectangle(character_x='-_=')
        self.assertEqual(shape.character_x, '-')

    def test_only_first_character_for_y(self):
        shape = ItemRectangle(character_y='-_=')
        self.assertEqual(shape.character_y, '-')

    def test_only_first_character_for_fill(self):
        shape = ItemRectangle(character_fill='-_=')
        self.assertEqual(shape.character_fill, '-')

    def test_only_first_character_for_joint(self):
        shape = ItemRectangle(character_joint='-_=')
        self.assertEqual(shape.character_joint, '-')

    def test_wrap_the_text_regardless_passed_x(self):
        text='0123456789'
        shape = ItemRectangle(text=text, x=2)
        self.assertGreater(shape.x, len(text))

    def test_wrap_the_text_regardless_passed_y(self):
        text='1\n2\n3\n4\n5\n6\n7'
        shape = ItemRectangle(text=text, y=2)
        self.assertGreater(shape.y, len(text.split('n')))


if __name__ == '__main__':
    unittest.main()
