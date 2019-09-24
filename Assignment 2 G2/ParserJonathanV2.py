# Created by Kieran Jerry Jonathon
from TIGr import AbstractParser
import re


class Parser(AbstractParser):
    def __init__(self, drawer):
        super().__init__(drawer)
        self.commandlist = {
            "P": "self.drawer.select_pen(self.data)",
            "D": "self.drawer.pen_down()",
            "N": "self.drawer.draw_line(0, self.data)",
            "E": "self.drawer.draw_line(90, self.data)",
            "S": "self.drawer.draw_line(180, self.data)",
            "W": "self.drawer.draw_line(270, self.data)",
            "X": "self.drawer.go_along(self.data)",
            "Y": "self.drawer.go_down(self.data)",
            "U": "self.drawer.pen_up()"
        }

    def parse(self, raw_source):
        self.source = raw_source.splitlines()
        for line in self.source:
            # Find all word by line
            inputs = re.findall("\w+", line)
            # Find all numbers by line
            self.data = re.findall("\d+", line)
            # Make all words uppercase
            self.command = inputs[0].upper()
            # Number has to be greater than 0
            if len(self.data) > 0:
                # Make it a whole number
                self.data = int(float(self.data[0]))
            # If command from input in the look table
            try:
                # Basically import the command and in the process it add the data.
                parsed_command = self.commandlist[self.command[0]]
                exec(parsed_command)
            except ValueError as e:
                print(f'{e}: Value outside boundary')
            except KeyError as e:
                print(f'{e}: Not a command')
