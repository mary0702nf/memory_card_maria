from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
app = QApplication([])
from random import choice, shuffle
from time import sleep
from memo___card_layout import *
from memo___app import *


class Question():
    def __init__(self, question, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        self.attempts = 0
        self.correct = 0

    def got_rightans(self):
        self.attempts = self.attempts + 1
        self.correct = self.correct + 1

    def got_wrongans(self):
        self.attempts =+ 1


q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

lst_quest = [q1, q2, q3, q4]
lst_rbtns = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

lst_inpt_objects = [inpt_quest, inpt_right_ans, inpt_wrong_ans1, inpt_wrong_ans2, inpt_wrong_ans3]

def switch_screen():
    if btn_next.text() == "Відповісти":
        RadioGroupBox.hide()
        chek_result()
        AnsGroupBox.show()
        btn_next.setText("Наступне питання")
    else:
        new_question()
        RadioGroupBox.show()
        AnsGroupBox.hide()
        btn_next.setText("Відповісти")


def new_question():
    global cur_q
    cur_q = choice(lst_quest)
    lb_Correct.setText(cur_q.right_ans)
    lb_Question.setText(cur_q.question)
    shuffle(lst_rbtns)
    RadioGroup.setExclusive(False)
    lst_rbtns[0].setText(cur_q.right_ans)
    lst_rbtns[1].setText(cur_q.wrong_ans1)
    lst_rbtns[2].setText(cur_q.wrong_ans2)
    lst_rbtns[3].setText(cur_q.wrong_ans3)


def chek_result():
        for rbtn in lst_rbtns:
            if rbtn.isChecked():
                if rbtn.text() == lb_Correct.text():
                    lb_Result.setText("Правильно!")
                    cur_q.got_rightans()
                    rbtn.setChecked(False)
                else:
                    lb_Result.setText("Не правильно")
                    cur_q.got_wrongans()
                    rbtn.setChecked(False)


def rest():
    window_card.hide()
    sleep(sp_rest.value())
    window_card.show()


def menu():
    if cur_q.attempts !=0:
        result = (cur_q.correct/cur_q.attempts) * 100
    else:
        result = 0
    text = f'Разів відповіли: {cur_q.attempts}\n'\
            f'Вірних відповідей: {cur_q.correct}\n'\
            f'Успіх: {round(result, 2)}%'

    lb_statistik.setText(text)
    window_card.hide()
    window_menu.show()


def go_back():
    window_card.show()
    window_menu.hide()


def accept():
    new_q = Question(inpt_quest.text(), inpt_right_ans.text(), inpt_wrong_ans1.text(), inpt_wrong_ans2.text(), inpt_wrong_ans3.text())
    lst_quest.append(new_q)
    for object in lst_inpt_objects:
        object.clear()


def clear_inpt():
    for object in lst_inpt_objects:
        object.clear()

def delete():
    lst_quest.remove(cur_q)
    new_question()


right_an = lst_rbtns[0]
wrong_ans1, wrong_ans2, wrong_ans3 = lst_rbtns[1], lst_rbtns[2], lst_rbtns[3]


new_question()


btn_next.clicked.connect(switch_screen)
btn_rest.clicked.connect(rest)

btn_menu.clicked.connect(menu)

btn_goBakc.clicked.connect(go_back)
btn_accept.clicked.connect(accept)
btn_clear.clicked.connect(clear_inpt)
btn_delete.clicked.connect(delete)

app.exec_()
