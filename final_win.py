# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout)
from instr import *
from time import *





class FinalWin(QWidget):
    def __init__(self, start_time):
        super().__init__()
        self.start_time = start_time
        self.finish_time = time()
        self.set_appear()
        self.results()
        self.initUI()
        self.show()
        

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def results(self):
       self.total = round(self.finish_time - self.start_time, 2)

        
    def initUI(self):
        self.end1 = QLabel(txt_prog1)
        self.end2 = QLabel(txt_prog2)
        self.end3 = QLabel(txt_prog3)
        self.end4 = QLabel(str(self.total))
        self.v_line = QVBoxLayout()
        self.h_line = QHBoxLayout()

        self.v_line.addWidget(self.end1, alignment =
        Qt.AlignCenter)
        self.v_line.addWidget(self.end2, alignment =
        Qt.AlignCenter)
        self.h_line.addWidget(self.end3, alignment =
        Qt.AlignCenter)
        self.h_line.addWidget(self.end4, alignment =
        Qt.AlignCenter)
    
        self.v_line.addLayout(self.h_line)
        self.setLayout(self.v_line)
        



