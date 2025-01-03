import sys
import playsound
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #get the current directory
        current_dir = os.getcwd() + r'\sounds'

        #main window
        self.setWindowTitle("Skeletor Soundboard")
        self.setGeometry(500, 500, 1000, 500)

        #buttons
        self.wimp_scientist_button = QPushButton("Wimp Scientist", self)
        self.wimp_scientist_button.setGeometry(10, 10, 200, 50)
        self.wimp_scientist_button.clicked.connect(self.wimp_scientist)

        self.laugh_button = QPushButton("Diabolical Laugh", self)
        self.laugh_button.setGeometry(10, 60, 200, 50)
        self.laugh_button.clicked.connect(self.laugh)

        self.metal_moron_button = QPushButton("Metal Moron", self)
        self.metal_moron_button.setGeometry(10, 110, 200, 50)
        self.metal_moron_button.clicked.connect(self.metal_moron)

        self.wimplash_button = QPushButton("Wimplash", self)
        self.wimplash_button.setGeometry(10, 160, 200, 50)
        self.wimplash_button.clicked.connect(self.wimplash)

        self.bunglers_button = QPushButton("Bunglers", self)
        self.bunglers_button.setGeometry(10, 210, 200, 50)
        self.bunglers_button.clicked.connect(self.bunglers)

        self.cabbage_button = QPushButton("Cabbage", self)
        self.cabbage_button.setGeometry(10, 260, 200, 50)
        self.cabbage_button.clicked.connect(self.cabbage)
    
    #functions for playing sounds
    def wimp_scientist(self):
        playsound.playsound(os.getcwd() + r'\sounds\wimp_scientist.mp3')
    def laugh(self):
        playsound.playsound(os.getcwd() + r'\sounds\laugh.mp3')
    def metal_moron(self):
        playsound.playsound(os.getcwd() + r'\sounds\metalmoron.mp3')
    def wimplash(self):
        playsound.playsound(os.getcwd() + r'\sounds\wimplash.mp3')
    def bunglers(self):
        playsound.playsound(os.getcwd() + r'\sounds\bunglers.mp3')
    def cabbage(self):
        playsound.playsound(os.getcwd() + r'\sounds\cabbage.mp3')


app = QApplication(sys.argv)
main_window = mainwindow()
main_window.show()
sys.exit(app.exec_())