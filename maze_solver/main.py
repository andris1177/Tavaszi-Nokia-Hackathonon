from re import compile
from queue import Queue

class MazeSolver:
    def __init__(self):
       self.fileLocation = "./input.txt"
       self.mazes = {}
       self.mazeId = None
       self.regexPatternRaw = r'^[A-Z]$'
       self.regexPattern = compile(self.regexPatternRaw)
       self.movement = [(1,0), (0,1), (-1,0), (0,-1)]

    def readFile(self):
        # seperating mazes into a dictionarie
        with open(self.fileLocation, 'r') as f:
            maze = []
            for line in f:
                line = line.replace(" ", "").strip()

                if not line:
                    continue

                if self.regexPattern.match(line):
                    if self.mazeId is not None:
                        self.mazes[self.mazeId] = self.maze

                    self.mazeId = line
                    self.maze = []

                else:
                    self.maze.append(list(line))

            if self.mazeId is not None:
                self.mazes[self.mazeId] = self.maze

    def convertCordinateToDirection(self, cordinates):
        # converting the cordinates into directions

        directions = "S "

        for cordinate in range(1, len(cordinates)):

            differenceX = cordinates[cordinate][0] - cordinates[cordinate-1][0]
            differenceY = cordinates[cordinate][1] - cordinates[cordinate-1][1]

            if differenceX == 1 and differenceY == 0:
                directions += "D "

            if differenceX == -1 and differenceY == 0:
                directions += "U "

            if differenceX == 0 and differenceY == 1:
                directions += "R "

            if differenceX == 0 and differenceY == -1:
                directions += "L "

        directions + "G"

        return directions

    def findMazeEntryAndExit(self, maze):
        # finding the entry of the maze and the goal
        self.startPos = None
        self.endPos = None
        
        for line in range(len(maze)):
            for char in range(len(maze[line])):
                if maze[line][char] == "S":
                    self.startPos = (line, char)

                elif maze[line][char] == "G":
                    self.endPos = (line, char)
                    
    def findPath(self, maze):
        # Breadth-first search
        queue = Queue()
        queue.put([self.startPos])

        while not queue.empty():
            path = queue.get()
            x, y = path[-1]

            if (x, y) == self.endPos:
                return path

            for dx, dy in self.movement:
                nextX, nextY = x + dx, y + dy

                if maze[nextX][nextY] != "#" and (nextX, nextY) not in path:
                    new_path = list(path)
                    new_path.append((nextX, nextY))
                    queue.put(new_path)

    def run(self):
        self.readFile()
        for mazeId in self.mazes.keys():
            self.findMazeEntryAndExit(self.mazes[mazeId])
            print(mazeId)
            print(self.convertCordinateToDirection(self.findPath(self.mazes[mazeId])))
            print("\n")

solution = MazeSolver()
solution.run()
