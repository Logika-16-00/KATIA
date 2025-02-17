from cProfile import label
from multiprocessing.connection import answer_challenge
import select
from tabnanny import check
from PyQt5.QtWidgets import QWidget,QMessageBox
from card import *
from app import *
from menu import *
from data import *
from random import *
radio_list = [btn_ans1, btn_ans2, btn_ans3, btn_ans4]
frm_card = 0 
form_list =[]
# Тестові данні
def testlist():

    frm = Question('Максимальна висота атмосфери', '11000м', '1100м', '5000м', '25000м')
    form_list.append(frm)
    frm = Question('Дім', 'house', 'horse', 'hurry', 'hour')
    form_list.append(frm)
    frm = Question('Найпопулярніша гра в світі', 'Minecraft', 'GTA V', 'Roblox', 'Cs:Go')
    form_list.append(frm)
from app import App

win_card = QWidget()
win_menu = QWidget()
def set_card():
    win_card.resize(600,500)
    win_card.setWindowTitle("Memory Card")
    win_card.move(0,0)
    win_card.setLayout(main_line)
def set_menu():
    win_menu.resize(800,600)
    win_menu.setWindowTitle("Memory Card")
    win_menu.move(0,0)
    win_menu.setLayout(main_menu_line)

def back_to_menu():
    win_card.hide()
    win_menu.show()

def back_to_test():
    win_menu.hide()
    win_card.show()
btn_back.clicked.connect(back_to_test)


btn_menu.clicked.connect(back_to_menu) 

def show_q():
    list_q.clear()
    for q in form_list:
        list_q.addItem(q.name)
testlist()
show_q()

def clear():
    line_ans.clear()
    line_corect.clear()
    line_false1.clear()
    line_false2.clear()
    line_false3.clear()
btn_clear.clicked.connect(clear)

def add():
    q_text = line_ans.text()
    q_correct = line_corect.text()
    q_false1 = line_false1.text()
    q_false2 = line_false2.text()
    q_false3 = line_false3.text()

    if q_text and q_correct and q_false1 and q_false2 and q_false3:
        new_q = Question(q_text, q_correct, q_false1, q_false2, q_false3)
        form_list.append(new_q)
        clear()
        list_q.addItem(new_q.name)

    else:
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Помилка")
        msg_box.setText("Заповніть всі поля")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.exec_()


btn_add.clicked.connect(add)

def show_q():
    q = choice(form_list)
    lb_ans.setText(q.name)
    answers = [q.correct,q.wrong1,q.wrong2,q.wrong3]
    shuffle(answers)

    btn_ans1.setText(answers[0])
    btn_ans2.setText(answers[1])
    btn_ans3.setText(answers[2])
    btn_ans4.setText(answers[3])
    return q 
def show_res():
    if btn_ans.text() == "Відповісти":
        AnswersGroupBox.hide()
        ResGroupBox.show()
        # if selected_button:
        #     if q.checked(selected_button.text):
        #         lb_res.setText("Правильно")
        #         lb_corect.setText(q.correct)
        #     else:
        #         lb_res.setText("Неправильно")
        #         lb_corect.setText(q.correct)

        # btn_ans.setText("Наступне питання")
        # selected_button = RadioGroup,checkButton()
        
    else:
        show_res()
        show_q()
def show_res():
    AnswersGroupBox.show()
    ResGroupBox.hide()
    btn_ans.setText("Відповісти")
    RadioGroup.setExclusive(0)
    btn_ans1.setChecked(False)
    btn_ans2.setChecked(False)
    btn_ans3.setChecked(False)
    btn_ans4.setChecked(False)
    RadioGroup.setExclusive(1)
btn_ans.clicked.connect(show_res)
set_card()
set_menu()

win_menu.show()
App.exec_()