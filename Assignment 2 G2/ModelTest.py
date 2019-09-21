import unittest


class ModelTest(unittest.TestCase):

    def test(self):
        from DrawerKieran import Drawer
        from ParserKC import Parser
        toDraw = open('Input.txt', "r+").read()
        s = Parser(Drawer()).parse(toDraw)
        self.assertEqual(s, 'pen down')


if __name__ == '__main__':
    unittest.main()
