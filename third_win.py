from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QRadioButton, QButtonGroup)
from instr import *
from final_win import *


class ThirdWin(QWidget):
    def __init__(self, exp, start_time):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.start_time = start_time
    
    def timer_test(self):
        global time
        a = self.exp.time6.split(",")
        h, m, s = map(int,a)
        time = QTime(h, m, s)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_sits1(self):
        global time
        a = self.exp.time1.split(",")
        h, m, s = map(int,a)
        time = QTime(h, m, s)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer_sits2(self):
        global time
        a = self.exp.time2.split(",")
        h, m, s = map(int,a)
        time = QTime(h, m, s)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer_sits3(self):
        global time
        a = self.exp.time3.split(",")
        h, m, s = map(int,a)
        time = QTime(h, m, s)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer_sits4(self):
        global time
        a = self.exp.time4.split(",")
        h, m, s = map(int,a)
        time = QTime(h, m, s)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer_sits5(self):
        global time
        a = self.exp.time5.split(",")
        h, m, s = map(int,a)
        time = QTime(h, m, s)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer_sits6(self):
        global time
        a = self.exp.time6.split(",")
        h, m, s = map(int,a)
        time = QTime(h, m, s)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move( win_x, win_y)

    def initUI(self):
        self.btn_next = QPushButton(txt_resume)
        self.text_timer = QLabel("")
        #этап 1
        self.exp1 = QLabel(self.exp.exc1)
        self.test1 = QPushButton(txt_timers)
        #этап 2
        self.exp2 = QLabel(self.exp.exc2)
        self.test2 = QPushButton(txt_timers)
        #этап 3
        self.exp3 = QLabel(self.exp.exc3)
        self.test3 = QPushButton(txt_timers)
        #этап 4
        self.exp4 = QLabel(self.exp.exc4)
        self.test4 = QPushButton(txt_timers)
        #этап 5
        self.exp5 = QLabel(self.exp.exc5)
        self.test5 = QPushButton(txt_timers)
        #этап 6
        self.exp6 = QLabel(self.exp.exc6)
        self.test6 = QPushButton(txt_timers)

        v_line1 = QHBoxLayout()
        v_line2 = QHBoxLayout()
        v_line3 = QHBoxLayout()
        v_line4 = QHBoxLayout()
        v_linem = QVBoxLayout()
        
        v_line1.addWidget(
            self.exp1, alignment = Qt.AlignLeft
        )
        v_line1.addWidget(
            self.exp2, alignment = Qt.AlignCenter
        )
        v_line1.addWidget(
            self.exp3, alignment = Qt.AlignRight
        )
        v_line2.addWidget(
            self.test1, alignment = Qt.AlignLeft
        )
        v_line2.addWidget(
            self.test2, alignment = Qt.AlignCenter
        )
        v_line2.addWidget(
            self.test3, alignment = Qt.AlignRight
        )


        v_line3.addWidget(
            self.exp4, alignment = Qt.AlignLeft
        )
        v_line3.addWidget(
            self.exp5, alignment = Qt.AlignCenter
        )
        v_line3.addWidget(
            self.exp6, alignment = Qt.AlignRight
        )
        v_line4.addWidget(
            self.test4, alignment = Qt.AlignLeft
        )
        v_line4.addWidget(
            self.test5, alignment = Qt.AlignCenter
        )
        v_line4.addWidget(
            self.test6, alignment = Qt.AlignRight
        )





        v_linem.addLayout(v_line1)
        v_linem.addLayout(v_line2)
        v_linem.addWidget(
            self.text_timer, alignment = Qt.AlignCenter
        )
        v_linem.addLayout(v_line3)
        v_linem.addLayout(v_line4)
        v_linem.addWidget(
            self.btn_next, alignment = Qt.AlignCenter
        )
      

        

        self.setLayout(v_linem)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.test1.clicked.connect(self.timer_sits1)
        self.test2.clicked.connect(self.timer_sits2)
        self.test3.clicked.connect(self.timer_sits3)
        self.test4.clicked.connect(self.timer_sits4)
        self.test5.clicked.connect(self.timer_sits5)
        self.test6.clicked.connect(self.timer_test)

    def next_click(self):
        self.hide()
        self.tw = FinalWin(self.start_time)