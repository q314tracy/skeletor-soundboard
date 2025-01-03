import sys
import playsound
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QFont

#button spacing parameters
button_number = 5
button_spacing_x = 10
button_spacing_y = 10
button_width = 300
button_height = 100

#window sizing parameters
window_size = [2, 4] #table of buttons
window_width = (window_size[0] * button_width) + ((window_size[0] + 1) * button_spacing_x)
window_height = (window_size[1] * button_height) + ((window_size[1] + 1) * button_spacing_y)

#font options
font = QFont()
font.bold()
font.setPointSize(20)

#string lists for buttons
#directory strings must be raw due to backslashes
bunglers = ["BUNGLERS", r'\sounds\bunglers.mp3']
laugh = ["LAUGH", r'\sounds\laugh.mp3']
cabbage = ["CABBAGE", r'\sounds\cabbage.mp3']
moron = ["MORON", r'\sounds\moron.mp3']
scientist = ["SCIENTIST", r'\sounds\scientist.mp3']
suitcase = ["SUITCASE", r'\sounds\suitcase.mp3']
wimplash = ["WIMPLASH", r'\sounds\wimplash.mp3']

#window class
class window(QMainWindow):
    #init
    def __init__(self):
        super().__init__()
        #main window
        self.setWindowTitle("Skeletor is my OTP")
        self.setGeometry(
            500,
            500, 
            window_width,
            window_height)
        #buttons
        self.button0 = self.create_button(0, 0, bunglers[0], bunglers[1])
        self.button1 = self.create_button(1, 0, cabbage[0], cabbage[1])
        self.button2 = self.create_button(0, 1, laugh[0], laugh[1])
        self.button3 = self.create_button(1, 1, moron[0], moron[1])
        self.button4 = self.create_button(0, 2, scientist[0], scientist[1])
        self.button5 = self.create_button(1, 2, suitcase[0], suitcase[1])
        self.button6 = self.create_button(0, 3, wimplash[0], wimplash[1])

    #function for button creation
    def create_button(self, x:int, y:int, name:str, file_dir:str):
        button = QPushButton(f"{name}", self)
        button.setGeometry(
            int((x * button_width + button_spacing_x * x) + button_spacing_x),
            int((y * button_height + button_spacing_y * y) + button_spacing_y),
            int(button_width),
            int(button_height))
        button.setFont(font)
        button.clicked.connect(lambda: self.play_sound(file_dir))

    #function for playing sounds
    def play_sound(self, file_dir):
        playsound.playsound(os.getcwd() + file_dir)

#gather args from sys for input to window and start window
window_app = QApplication(sys.argv)
window_main = window()
window_main.show()
sys.exit(window_app.exec())
