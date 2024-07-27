from multiprocessing.connection import answer_challenge
from tkinter import Radiobutton
from memorycard_ import *

win_card = QWidget()
win_card.resize(600,500)
win_card.setWindowTitle("Memory Card")
win_card.move(0,0)
btn_sleep = QPushButton("Відпочити")
box_min = QSpinBox()
box_min.setValue(5)
lb_min = QLabel("Хвилин")
lb_ans = QLabel("Запитання")
btn_menu = QPushButton("Меню")
btn_ans = QPushButton("Відповісти")
bts_ans1 = QRadioButton("1")
bts_ans2 = QRadioButton("2")
bts_ans3 = QRadioButton("3")
bts_ans4 = QRadioButton("4")
AnswersGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup.appButton(btn_ans1)
RadioGroup.appButton(btn_ans2)
RadioGroup.appButton(btn_ans3)
RadioGroup.appButton(btn_ans4)

line1 = QVBoxLayout()
line2 = QVBoxLayout()
line1.addWidget(btn_menu)
line1.addWidget(btn_sleep)
line1.addWidget(box_min)

line_btn_ans1 = QBoxLayout()
line_btn_ans2 = QBoxLayout()

line_btn_ans1.addWidget(btn_ans1)
line_btn_ans1.addWidget(btn_ans2)
line_btn_ans2.addWidget(btn_ans3)
line_btn_ans2.addWidget(btn_ans4)
mainline_btn_ans = QHBoxLayout()
mainline_btn_ans.addLayout(line_btn_ans1)
mainline_btn_ans.addLayout(line_btn_ans2)
mainline_btn_set.Layout(mainline_btn_ans)

main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addWidget(lb_ans)
main_line.addWidget(AnswersGroupBox)
main_line.addWidget(btn_ans)
win_card.setLayout(main_line)




win_card.show()
App.exec_()