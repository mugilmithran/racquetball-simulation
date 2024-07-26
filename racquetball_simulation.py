import random

class SimStats:
    def __init__(self):
        self.winsA = 0
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0
        
    def update(self, aGame):
        a, b = aGame.getScores()
        if a > b:
            self.winsA += 1
            if b == 0:
                self.shutsA += 1
        else:
            self.winsB += 1
            if a == 0:
                self.shutsB += 1
                
    def printReport(self):
        n = self.winsA + self.winsB
        print(f'Summary of {n} games:\n')
        print("     wins(%total) shutouts(%wins)")
        print("--------------------------------")
        self.printLine("A", self.winsA, self.shutsA, n)
        self.printLine("B", self.winsB, self.shutsB, n)
        
    def printLine(self, label, wins, shuts, n):
        if wins == 0:
            shutStr = "-----"
        else:
            shutStr = f"{shuts/wins:4.1%}"
        print(f"Player {label}: {wins:5} ({wins/n:5.1%}) {shuts:11} ({shutStr})")
        
class RBallGame:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA
        
    def play(self):
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()
                
    def isOver(self):
        a, b = self.getScores()
        return a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and a == 0)
    
    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA
            
    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()
    
class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        
    def winsServe(self):
        return random.random() <= self.prob
    
    def incScore(self):
        self.score += 1
        
    def getScore(self):
        return self.score

def getInputs():
    probA = float(input("Enter the probability for Player A:"))
    probB = float(input("Enter the probability for Player B:"))
    n = int(input("Enter the number games to simulate:"))
    return probA, probB, n

def main():
    print("This program simulates a series of racquet games between two players")
    probA, probB, n = getInputs()
    
    stats = SimStats()
    for _ in range(n):
        theGame = RBallGame(probA, probB)
        theGame.play()
        stats.update(theGame)
        
    stats.printReport()
    

if __name__ == "__main__":
    main()
    
                
        