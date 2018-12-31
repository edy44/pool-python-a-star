from collections import OrderedDict
from time import sleep
import os

class Map:

    def __init__(self, content):
        self.step = {}
        self.collect = {}
        self.content = content
        self.map = self.init_map(content)


    def init_map(self, content):
        map = {}
        line = None
        column = 1
        position = 0
        collect = 0
        for char in content:
            if char == "\n":
                size = column - 1
                if line == None:
                    line = 0
                else:
                    line += 1
                column = 0
                map[line] = {}
            else:
                if line is not None:
                    if column != 1 and column != size:
                        if char == " ":
                            map[line][column-2] = ""
                        else:
                            map[line][column-2] = char
                            if char != "#":
                                if char == "o":
                                    self.collect[collect] = [line, column-2]
                                    collect += 1
                                else:
                                    self.step[int(char)] = [line, column-2]
            column += 1
        line = len(map) - 1
        map.pop(line)
        map.pop(line-1)
        self.step = OrderedDict(sorted(self.step.items(), key=lambda t: t[0]))
        self.line = len(map)
        self.column = len(map[0])
        return map


    def getLine(self):
        return self.line

    
    def getColumn(self):
        return self.column


    def getContent(self):
        return self.content


    def getStep(self):
        step = {}
        for key, position in self.step.items():
            step[key] = position
        return step


    def getCollect(self):
        collect = {}
        for key, position in self.collect.items():
            collect[key] = position
        return collect


    def getStepNumber(self):
        return len(self.step) 


    def getCollectNumber(self):
        return len(self.collect)


    def getPosition(self, position):
        return self.step[position]


    def getCollectPosition(self, position):
        return self.collect[position]


    def add_value(self, line, column, value):
        self.map[line][column] = value
    

    def get_value(self, line, column):
        return self.map[line][column]


    def update(self, path, key = 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        for path_position in path:
            line = path_position[0]
            column = path_position[1]
            self.add_value(line, column, ".")
            for number, position in self.step.items():
                line = position[0]
                column = position[1]
                self.add_value(line, column, str(number))
            for number, position in self.collect.items():
                if path_position == position:
                    line = position[0]
                    column = position[1]
                    self.add_value(line, column, "x")
            self.print_content(path, key)
            self.print_map()
            sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        self.print_content(path, key)
        self.print_map()


    def print_map(self):
        self.print_tags()
        for line, column in self.map.items():
            result = "#"
            for key, value in column.items():
                if value == "":
                    result += " "
                else:
                    result += str(value)
            result += "#" 
            print(result)
        self.print_tags()
    

    def print_tags(self):
        column = self.column + 1
        result = ""
        while column >= 0:
            result += "#"
            column -= 1
        print(result)


    def print_content(self, path, key):
        content = "Path from " + str(key-1) + " to " + str(key)
        if len(self.collect) != 0: 
            content += " with " + str(len(self.collect)) + " stops"
        content += " in " + str(len(path)-1) + " steps"
        print(content)    

