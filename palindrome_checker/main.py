from re import sub

class PalindrómaTest:
    def __init__(self):
        self.fileLocation = "./input.txt"
        self.lines = []
        self.regexPattern = r'[^a-z0-9]'

    def readFile(self):
        with open(self.fileLocation, "r") as f:
            self.rawData = f.read()
        
        self.lines = self.rawData.lower().strip().split("\n")

        for i in range(len(self.lines)):
            self.lines[i] = sub(self.regexPattern, "", self.lines[i])

    def getPaleindromaInfo(self, word):
        self.wordRewersed = word[::-1]
        if word == self.wordRewersed:
            return f"YES, {self.uniqueCaracters(word)}"
        else:
            return "NO, -1"
        
    def uniqueCaracters(self, word):
        return len(set(word))

    def analizeRows(self):
        for word in self.lines:
            print(self.getPaleindromaInfo(word))

    def run(self):
        self.readFile()
        self.analizeRows()
 
solution = PalindrómaTest()
solution.run()