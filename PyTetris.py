from time import sleep
from os import system
class PyTetris:
    def __init__(self):
        self.a = [[str(j) for j in range(10)] for i in range(10)]
        self.tetObj = "#"
        self.coordinate = 0
        self.axis = 4

    def showTetris(self):
        system("clear")
        for i in self.a: print("".join(i))
        self.moveTetris(self.coordinate,self.axis)
        self.coordinate+=1
        self.showTetris()

    def moveTetris(self,val,ax):
        try:
            self.a[val][ax] = self.tetObj
            self.a[val-1][ax] = str(val-val+ax)
        except IndexError:
            self.a[val-1][ax] = self.tetObj
            self.coordinate = 0
        sleep(1)

startTetris = PyTetris()
startTetris.showTetris()