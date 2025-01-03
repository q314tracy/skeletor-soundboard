import sys
import playsound
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

#button spacing parameters
button_number = 5
button_spacing_x = 10
button_spacing_y = 10
button_width = 150
button_height = 50

#strings for buttons
bunglers_list = ["Bunglers", r'\sounds\bunglers.mp3']
laugh_list = ["Laugh", r'\sounds\laugh.mp3']
cabbage_list = ["Cabbage", r'\sounds\cabbage.mp3']
moron_list = ["Moron", r'\sounds\moron.mp3']
scientist_list = ["Scientist", r'\sounds\scientist.mp3']

class window(QMainWindow):
    #init
    def __init__(self):
        super().__init__()
        #main window
        self.setWindowTitle("Window")
        self.setGeometry(
            500, 
            500, 
            1000,
            500)
        #buttons
        self.button0 = self.create_button(0, 0, bunglers_list[0], bunglers_list[1])
        self.button1 = self.create_button(1, 0, cabbage_list[0], cabbage_list[1])
        self.button2 = self.create_button(2, 0, laugh_list[0], laugh_list[1])
        self.button3 = self.create_button(3, 0, moron_list[0], moron_list[1])
        self.button4 = self.create_button(4, 0, scientist_list[0], scientist_list[1])

    #function for button creation
    def create_button(self, x:int, y:int, name:str, file_dir:str):
        button = QPushButton(f"{name}", self)
        button.setGeometry(
            int(x * button_width + button_spacing_x),
            int(y * button_height + button_spacing_y),
            int(button_width),
            int(button_height))
        button.clicked.connect(lambda: self.play_sound(file_dir))

    #function for playing sounds
    def play_sound(self, file_dir):
        playsound.playsound(os.getcwd() + file_dir)

#gather args from sys for input to window and start window
window_app = QApplication(sys.argv)
window_main = window()
window_main.show()
sys.exit(window_app.exec())
