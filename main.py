import sys
from Game import Game
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen 
from PyQt5.QtGui import QIcon , QFont
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtGui

game = Game()
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Rock - Paper - Scissors'
        self.left = 10
        self.top = 10
        self.width = 1024 
        self.height = 768
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width,self.height) 

        self.mainLabel = QLabel("Choose your move",self)
        self.mainLabel.setFont(QtGui.QFont("Times",24,QtGui.QFont.Bold))
        self.mainLabel.setGeometry(400,50,400,400)


        rockButton = QPushButton("Rock",self)
        rockButton.move(500,500)
        rockButton.clicked.connect(self.rockButtonOnClick)
        
        scissorsButton = QPushButton("Scissors",self)
        scissorsButton.move(400,500)
        scissorsButton.clicked.connect(self.scissorsButtonOnClick)

        paperButton = QPushButton("Paper",self)
        paperButton.move(600,500)
        paperButton.clicked.connect(self.paperButtonOnClick)

        self.show()

    @pyqtSlot()
    def rockButtonOnClick(self):
        computerMove = game.retrieveComputerMove()
        if computerMove == "Rock":
            self.mainLabel.setText("Tie")
        if computerMove == "Scissors":
            self.mainLabel.setText("You win")
        if computerMove == "Paper":
            self.mainLabel.setText("You lose")
    def scissorsButtonOnClick(self):
        computerMove = game.retrieveComputerMove()
        self.mainLabel.setText("Clicked Scissors")
    
    def paperButtonOnClick(self):
        computerMove = game.retrieveComputerMove()
        self.mainLabel.setText("Clicked Paper")
       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())