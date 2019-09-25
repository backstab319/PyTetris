class PyTetris:
    def __init__(self):
        self.a = [["" for j in range(10)] for i in range(10)]
    def showTetris(self):
        for i in self.a: print("".join(i))
startTetris = PyTetris()
startTetris.showTetris()