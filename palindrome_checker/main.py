from re import sub

class PalindrómaTest:
    def __init__(self):
        self.fileLocation = "./input.txt"
        self.data = []
        self.regexPattern = r'[^a-z0-9]'
        self.run()

    def readFile(self):
        with open(self.fileLocation, "r") as f:
            self.rawData = f.read()
        
        self.data = self.rawData.lower().strip().split("\n")

        for i in range(len(self.data)):
            self.data[i] = sub(self.regexPattern, "", self.data[i])

        f.close()

    def testData(self, word):
        self.wordRewersed = word[::-1]
        if word == self.wordRewersed:
            return f"YES, {self.uniqueCaracters(word)}"
        else:
            return "NO, -1"
        
    def uniqueCaracters(self, word):
        return len(set(word))

    def mainLoop(self):
        for i in self.data:
            print(self.testData(i))

    def run(self):
        self.readFile()
        self.mainLoop()
 

solution = PalindrómaTest()