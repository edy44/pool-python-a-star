import sys
from map import Map
from astar import Astar

if __name__ == '__main__':
    
    size = len(sys.argv)
    if size == 2:
        try:
            _file = open(sys.argv[1], "r")
            content = _file.read()
            _file.close()
            map = Map(content)
        except:
            print("The file is unknown")
        if map.getStepNumber() >= 2:
                Astar(map)
        else:
            print("The map must have 2 steps at least")
    else:
        print("The path of the file is required")
