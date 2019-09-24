# Created by Kieran Jerry Jonathon
from TIGr import AbstractInterface
from ParserJonathanV2 import Parser


class MainTIGr(AbstractInterface):

    def __init__(self, parser):
        super().__init__(parser)

    def create_interface(self):
        c = self.open_config()
        if c[2] == 'FrontEndKieran':
            from FrontEndKieran import TkinterInterface
            self.interface = TkinterInterface(self)
        elif c[2] == 'FrontEndJerry':
            from FrontEndJerry import GuiInterface
            self.interface = GuiInterface(self)
        self.interface.start()

    def open_config(self):
        self.config = open('config.txt', "r+")
        return self.config.read().splitlines()

    def go(self):
        self.create_interface()


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
