from re import compile, match 

class MazeSolver:
    def __init__(self):
       self.fileLocation = "./input.txt"
       self.mazes = {}
       self.maze = []
       self.mazeId = None
       self.regexPatternRaw = r'^[A-Z]$'
       self.regexPattern = compile(self.regexPatternRaw)

       self.empty = "."
       self.block = "#"
       self.goal = "G"

    def readFile(self):
        with open(self.fileLocation, 'r') as f:
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

    def run(self):
        self.readFile()
        print(self.mazes["A"])

solution = MazeSolver()
solution.run()