import numpy as np

class MatrixOperation:
    def __init__(self):
        self.fileLocation = "./input.txt"
        self.matrixes = {}
        self.operations = []

    def readFile(self):
        isInOperation = False
        matrix = None

        with open(self.fileLocation, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line == "operations":
                isInOperation = True
                matrix = None
                continue

            if not isInOperation:
                if len(line) > 0 and line[0] in "ABCDEFGHIJ" and len(line) == 1:
                    matrix = line[0]
                    self.matrixes[matrix] = []

                elif matrix:
                    self.matrixes[matrix].append(list(map(int, line.split())))

            else:
                self.operations.append(line)

    def convertListToNpArray(self):
        for i in self.matrixes:
            self.matrixes[i] = np.array(self.matrixes[i])

    def calculate(self):
        # clacluating the values
        for operation in self.operations:
            operationForNumpy = operation.replace("*", "@")
            result = eval(operationForNumpy, {}, self.matrixes)
            resultList = result.tolist()
            print("".join(operation))
            for j in range(len(resultList)):
                print(" ".join(map(str, result[j])))
            

    def run(self):
        self.readFile()
        self.convertListToNpArray()
        self.calculate()

solution = MatrixOperation()
solution.run()