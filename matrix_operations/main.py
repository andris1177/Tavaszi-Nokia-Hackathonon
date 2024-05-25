from re import compile, match

class MatrixOperations:
    def __init__(self):
        self.fileLocation = './input.txt'
        self.matrixes = {}
        self.matrix = []
        self.matrixId = None
        self.regexPatternRaw = r'^[A-Z]$'
        self.regexPattern = compile(self.regexPatternRaw)
        self.matriciesOrSolution = 0

    def readFile(self):
        with open(self.fileLocation, 'r') as f:
            for line in f:
                line = line.replace(" ", "").strip()

                if line == "matrices" or self.matriciesOrSolution == 1:
                    self.matriciesOrSolution = 1


                    if not line:
                        continue

                    if self.regexPattern.match(line):
                        if self.matrixId is not None:
                            self.matrixes[self.matrixId] = self.matrix

                        self.matrixId = line
                        self.matrix = []

                    else:
                        self.matrix.append(list(line))

                    if self.matrixId is not None:
                        self.matrixes[self.matrixId] = self.matrix

                else:
                    return 

    def run(self):
        self.readFile()
        print(self.matrixes)

        

solution = MatrixOperations()
solution.run()