# created by Kieran Jerry Jonathon
from TIGr import AbstractSourceReader
from ParserJonathanV2 import Parser

class AbstractInterface(AbstractSourceReader):

    def go(self):
        global interface
        config = open('config.txt', "r+")
        c = config.read().splitlines()
        if c[2] == 'FrontEndKieran':
            from FrontEndKieran import TkinterInterface
            interface = TkinterInterface(self)
        elif c[2] == 'FrontEndJerry':
            from FrontEndJerry import GuiInterface
            interface = GuiInterface(self)

        config.close()
        interface.start()


if __name__ == '__main__':
    config = open('config.txt', "r+")
    c = config.read().splitlines()
    if c[0] == 'DrawerKieran':
        from DrawerKieran import Drawer
    elif c[0] == 'DrawerTurtleJack':
        from DrawerTurtleJack import Drawer
    config.close()

    main = MainTIGr(Parser(Drawer()))
    main.go()
