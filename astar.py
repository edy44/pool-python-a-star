from map import Map
from node import Node

class Astar:

    positions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def __init__(self, map):
        self.map = map
        self.find_path()     


    def find_path(self):
        step_number = self.map.getStepNumber()
        if step_number == 2:
            collect_number = self.map.getCollectNumber()
            if collect_number == 0:
                self.one_path()
            else:
                self.one_path_with_collects()
        else:
            self.one_path_with_steps()


    def one_path(self):
        start = self.map.getPosition(0)
        end = self.map.getPosition(1)
        path = self.algo(start, end)
        if len(path) != 0:
            self.map.update(path)
        else:
            return self.print_error() 


    def one_path_with_collects(self):
        start = self.map.getPosition(0)
        collect = self.map.getCollect()
        delete = ""
        number = 0
        while len(collect) != 0:
            min_path = []
            for key, position in collect.items():         
                end = self.map.getCollectPosition(key)
                path = self.algo(start, end)
                if len(path) == 0:
                    return self.print_error()
                if min_path == [] or len(min_path) >= len(path):
                    min_path = path
                    delete = key
            self.map.update(min_path)
            number += len(min_path)
            collect.pop(delete)
            start = end
        end = self.map.getPosition(1)
        path = self.algo(start, end)
        if len(path) == 0:
            return self.print_error() 
        number += len(path)
        self.map.update(path)


    def one_path_with_steps(self):
        start = self.map.getPosition(0)
        steps = self.map.getStep()
        steps.pop(0)
        for key, position in steps.items():        
            end = self.map.getPosition(key)
            path = self.algo(start, end)
            if len(path) == 0:
                return self.print_error()
            map = Map(self.map.getContent())
            map.update(path, key)
            start = end


    def algo(self, start, end):
        start_node = Node(start, None)
        end_node = Node(end, None)
        open_list = []
        close_list = []
        open_list.append(start_node)

        while len(open_list) > 0:

            current_node = open_list[0]
            current_index = 0

            for index, node in enumerate(open_list):
                if node.f < current_node.f:
                    current_node = node
                    current_index = index
            
            open_list.pop(current_index)
            close_list.append(current_node)

            if current_node.position == end_node.position:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] 

            children = []
            for new_position in Astar.positions:
                line = current_node.position[0] + new_position[0]
                column = current_node.position[1] + new_position[1] 
                node_position = [line, column]
                if line < 0 or line > self.map.getLine()-1 or column < 0 or column > self.map.getColumn()-1:
                    continue
                if self.map.get_value(line, column) == "#":
                    continue
                new_node = Node(node_position, current_node)
                children.append(new_node)

            for child in children:
                add_close = True
                for close_child in close_list:
                    if child.position == close_child.position:
                        add_close = False
                add_open = True
                for open_node in open_list:
                    if child.position == open_node.position and child.g > open_node.g:
                        add_open = False
                if add_open and add_close:
                    child.g = current_node.g + 1
                    child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                    child.f = child.g + child.h
                    open_list.append(child)

        return []


    def print_error(self):
        print("No way to find a Path !")  
