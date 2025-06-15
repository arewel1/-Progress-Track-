# напиши здесь код для второго экрана приложения
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QRadioButton, QButtonGroup)
from instr import *
from third_win import *

from time import *



class Experiment():
    def __init__(self, ex1, time1, ex2, time2, ex3, time3, ex4, time4, ex5, time5, ex6, time6):
        self.exc1 = ex1
        self.time1 = time1
        self.exc2 = ex2
        self.time2 = time2
        self.exc3 = ex3
        self.time3 = time3
        self.exc4 = ex4
        self.time4 = time4
        self.exc5 = ex5
        self.time5 = time5
        self.exc6 = ex6
        self.time6 = time6



class TestWin(QWidget):
    
    def __init__(self):
        super().__init__()
        self.start_time = time()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()


        self.ex1 = "Пусто"
        self.ex2 = "Пусто"
        self.ex3 = "Пусто"
        self.ex4 = "Пусто"
        self.ex5 = "Пусто"
        self.ex6 = "Пусто"
    
     
        
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move( win_x, win_y)
    
    def initUI(self):

        self.btn_next = QPushButton(txt_resume)
        self.hint1 = QLineEdit(txt_1nfo)
        self.hint2 = QLineEdit(txt_1nfo)
        self.hint3 = QLineEdit(txt_1nfo)
        self.hint4 = QLineEdit(txt_1nfo)
        self.hint5 = QLineEdit(txt_1nfo)
        self.hint6 = QLineEdit(txt_2nfo)
        self.errop = QLabel(" ")
        #этап 1
        self.btn_answer11 = QRadioButton(txt_1ex1)
        self.btn_answer12 = QRadioButton(txt_1ex2)
        self.btn_answer13 = QRadioButton(txt_1ex3)
        self.btn_answer14 = QRadioButton(txt_1ex4)
        self.btn_answer14.setChecked(True)
        self.button_group1 = QButtonGroup()
        self.button_group1.addButton(self.btn_answer11, id = 1)
        self.button_group1.addButton(self.btn_answer12, id = 2)
        self.button_group1.addButton(self.btn_answer13, id = 3)
        self.button_group1.addButton(self.btn_answer14, id = 4)
        self.button1 = QPushButton("Подтвердить")

        #этап 2
        self.btn_answer21 = QRadioButton(txt_2ex1)
        self.btn_answer22 = QRadioButton(txt_2ex2)
        self.btn_answer23 = QRadioButton(txt_2ex3)
        self.btn_answer24 = QRadioButton(txt_2ex4)
        self.btn_answer24.setChecked(True)
        self.button_group2 = QButtonGroup()
        self.button_group2.addButton(self.btn_answer21, id = 1)
        self.button_group2.addButton(self.btn_answer22, id = 2)
        self.button_group2.addButton(self.btn_answer23, id = 3)
        self.button_group2.addButton(self.btn_answer24, id = 4)
        self.button2 = QPushButton("Подтвердить")

        #этап 3
        self.btn_answer31 = QRadioButton(txt_3ex1)
        self.btn_answer32 = QRadioButton(txt_3ex2)
        self.btn_answer33 = QRadioButton(txt_3ex3)
        self.btn_answer34 = QRadioButton(txt_3ex4)
        self.btn_answer34.setChecked(True)
        self.button_group3 = QButtonGroup()
        self.button_group3.addButton(self.btn_answer31, id = 1)
        self.button_group3.addButton(self.btn_answer32, id = 2)
        self.button_group3.addButton(self.btn_answer33, id = 3)
        self.button_group3.addButton(self.btn_answer34, id = 4)
        self.button3 = QPushButton("Подтвердить")

        #этап 4
        self.btn_answer41 = QRadioButton(txt_4ex1)
        self.btn_answer42 = QRadioButton(txt_4ex2)
        self.btn_answer43 = QRadioButton(txt_4ex3)
        self.btn_answer44 = QRadioButton(txt_4ex4)
        self.btn_answer44.setChecked(True)
        self.button_group4 = QButtonGroup()
        self.button_group4.addButton(self.btn_answer41, id = 1)
        self.button_group4.addButton(self.btn_answer42, id = 2)
        self.button_group4.addButton(self.btn_answer43, id = 3)
        self.button_group4.addButton(self.btn_answer44, id = 4)
        self.button4 = QPushButton("Подтвердить")

        #этап 5
        self.btn_answer51 = QRadioButton(txt_5ex1)
        self.btn_answer52 = QRadioButton(txt_5ex2)
        self.btn_answer53 = QRadioButton(txt_5ex3)
        self.btn_answer54 = QRadioButton(txt_5ex4)
        self.btn_answer54.setChecked(True)
        self.button_group5 = QButtonGroup()
        self.button_group5.addButton(self.btn_answer51, id = 1)
        self.button_group5.addButton(self.btn_answer52, id = 2)
        self.button_group5.addButton(self.btn_answer53, id = 3)
        self.button_group5.addButton(self.btn_answer54, id = 4)
        self.button5 = QPushButton("Подтвердить")

        #этап 6
        self.btn_answer61 = QRadioButton(txt_6ex1)
        self.btn_answer62 = QRadioButton(txt_6ex2)
        self.btn_answer63 = QRadioButton(txt_6ex3)
        self.btn_answer64 = QRadioButton(txt_6ex4)
        self.btn_answer64.setChecked(True)
        self.button_group6 = QButtonGroup()
        self.button_group6.addButton(self.btn_answer61, id = 1)
        self.button_group6.addButton(self.btn_answer62, id = 2)
        self.button_group6.addButton(self.btn_answer63, id = 3)
        self.button_group6.addButton(self.btn_answer64, id = 4)
        self.button6 = QPushButton("Подтвердить")


        #Расположение

        v_linem = QVBoxLayout()
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()
        v_line3 = QVBoxLayout()
        v_line4 = QVBoxLayout()
        v_lineh1 = QHBoxLayout()
        v_lineh2 = QHBoxLayout()
        v_lineh3 = QHBoxLayout()
        v_lineh4 = QHBoxLayout()
        v_lineh5 = QHBoxLayout()
        v_lineh6 = QHBoxLayout()
        v_line1.addWidget(
            self.btn_answer11, alignment = Qt.AlignLeft
        )
        v_line2.addWidget(
            self.btn_answer12, alignment = Qt.AlignLeft
        )
        v_line1.addWidget(
            self.btn_answer13, alignment = Qt.AlignLeft
        )
        v_line2.addWidget(
            self.btn_answer14, alignment = Qt.AlignLeft
        )
        #этап 2
        v_line3.addWidget(
            self.btn_answer21, alignment = Qt.AlignRight
        )
        v_line4.addWidget(
            self.btn_answer22, alignment = Qt.AlignRight
        )
        v_line3.addWidget(
            self.btn_answer23, alignment = Qt.AlignRight
        )
        v_line4.addWidget(
            self.btn_answer24, alignment = Qt.AlignRight
        )

        


        v_lineh1.addLayout(v_line1)
        v_line2.addWidget(
            self.button1, alignment = Qt.AlignLeft
        )
        v_lineh1.addLayout(v_line2)

        v_lineh1.addLayout(v_line3)
        v_line4.addWidget(
            self.button2, alignment = Qt.AlignRight
        )
        v_lineh1.addLayout(v_line4)

        v_line1.addWidget(
            self.hint1, alignment = Qt.AlignLeft
        )
        v_line3.addWidget(
            self.hint2, alignment = Qt.AlignRight
        )

       
        #этап 3
        v_line1.addWidget(
            self.btn_answer31, alignment = Qt.AlignLeft
        )
        v_line2.addWidget(
            self.btn_answer32, alignment = Qt.AlignLeft
        )
        v_line1.addWidget(
            self.btn_answer33, alignment = Qt.AlignLeft
        )
        v_line2.addWidget(
            self.btn_answer34, alignment = Qt.AlignLeft
        )

        #этап 4
        v_line3.addWidget(
            self.btn_answer41, alignment = Qt.AlignRight
        )
        v_line4.addWidget(
            self.btn_answer42, alignment = Qt.AlignRight
        )
        v_line3.addWidget(
            self.btn_answer43, alignment = Qt.AlignRight
        )
        v_line4.addWidget(
            self.btn_answer44, alignment = Qt.AlignRight
        )

        v_line2.addWidget(
            self.button3, alignment = Qt.AlignLeft
        )
        v_line4.addWidget(
            self.button4, alignment = Qt.AlignRight
        )

        v_line1.addWidget(
            self.hint3, alignment = Qt.AlignLeft
        )
        v_line3.addWidget(
            self.hint4, alignment = Qt.AlignRight
        )

        #этап 5
        v_line1.addWidget(
            self.btn_answer51, alignment = Qt.AlignLeft
        )
        v_line2.addWidget(
            self.btn_answer52, alignment = Qt.AlignLeft
        )
        v_line1.addWidget(
            self.btn_answer53, alignment = Qt.AlignLeft
        )
        v_line2.addWidget(
            self.btn_answer54, alignment = Qt.AlignLeft
        )

        #этап 6
        v_line3.addWidget(
            self.btn_answer61, alignment = Qt.AlignRight
        )
        v_line4.addWidget(
            self.btn_answer62, alignment = Qt.AlignRight
        )
        v_line3.addWidget(
            self.btn_answer63, alignment = Qt.AlignRight
        )
        v_line4.addWidget(
            self.btn_answer64, alignment = Qt.AlignRight
        )

        v_line2.addWidget(
            self.button5, alignment = Qt.AlignLeft
        )
        v_line4.addWidget(
            self.button6, alignment = Qt.AlignRight
        )

        v_line1.addWidget(
            self.hint5, alignment = Qt.AlignLeft
        )
        v_line3.addWidget(
            self.hint6, alignment = Qt.AlignRight
        )

        v_linem.addLayout(v_lineh1)
        v_linem.addLayout(v_lineh2)
        v_linem.addLayout(v_lineh3)
        v_linem.addLayout(v_lineh4)
        v_linem.addLayout(v_lineh5)
        v_linem.addLayout(v_lineh6)

        v_linem.addWidget(
            self.btn_next, alignment = Qt.AlignCenter
        )
        v_linem.addWidget(
            self.errop, alignment = Qt.AlignCenter
        )
        self.setLayout(v_linem)


    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.button1.clicked.connect(self.secret_text1)
        self.button2.clicked.connect(self.secret_text2)
        self.button3.clicked.connect(self.secret_text3)
        self.button4.clicked.connect(self.secret_text4)
        self.button5.clicked.connect(self.secret_text5)
        self.button6.clicked.connect(self.secret_text6)
    
    def secret_text1(self):
        self.ex1 = (self.button_group1.button(self.button_group1.checkedId()).text())
    def secret_text2(self):
        self.ex2 = (self.button_group1.button(self.button_group1.checkedId()).text())
    def secret_text3(self):
        self.ex3 = (self.button_group1.button(self.button_group1.checkedId()).text())
    def secret_text4(self):
        self.ex4 = (self.button_group1.button(self.button_group1.checkedId()).text())
    def secret_text5(self):
        self.ex5 = (self.button_group1.button(self.button_group1.checkedId()).text())
    def secret_text6(self):
        self.ex6 = (self.button_group1.button(self.button_group1.checkedId()).text())

    def next_click(self):
        try:
            a1 = self.hint1.text().split(",")
            h, m, s = map(int,a1)
            a2 = self.hint2.text().split(",")
            h, m, s = map(int,a2)
            a3 = self.hint3.text().split(",")
            h, m, s = map(int,a3)
            a4 = self.hint4.text().split(",")
            h, m, s = map(int,a4)
            a5 = self.hint5.text().split(",")
            h, m, s = map(int,a5)
            a6 = self.hint6.text().split(",")
            h, m, s = map(int,a6)
            self.hide()
            self.exp = Experiment(self.ex1, self.hint1.text(), self.ex2, self.hint2.text(), self.ex3, self.hint3.text(), self.ex4, self.hint4.text(), self.ex5, self.hint5.text(), self.ex6, self.hint6.text())
            self.tw = ThirdWin(self.exp, self.start_time)
        except Exception as er:

            self.errop.setText("Ошибка ввода времени либо колличества")
            
 
        

    

#app = QApplication([])
#mw = TestWin()
#app.exec_()



