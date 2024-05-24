class MatrixOperations:
    def __init__(self):
       self.fileLocation = './input.txt'
       self.data = [[]]
       self.readFile()
       self.teszt()

    def readFile(self):
        with open(self.fileLocation, "r") as f:
            for i in f:
                self.data.append(i.replace("\n", " ").strip().split())

    def teszt(self):
        for i in range(len(self.data)):
            print(self.data[i])

        

solution = MatrixOperations()