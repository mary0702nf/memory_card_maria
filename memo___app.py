from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
window_menu = QWidget()
window_menu.setWindowTitle("Меню")
window_menu.resize(500, 400)

show_window = False


# КНОПКИ
btn_clear = QPushButton("Очистити")
btn_goBakc = QPushButton("Назад")
btn_accept = QPushButton("Прийняти")
btn_delete = QPushButton("Видалити")

# СТАТИСТИКА
title = QLabel("Статистика")

lb_statistik = QLabel()


# ТЕКСТ
Question = QLabel("Введіть запитання:")
lb_RightAns = QLabel("Введіть вірну відповідь:")
lb_WrongAns1 = QLabel("Введіть першу хибну відповідь:")
lb_WrongAns2 = QLabel("Введіть другу хибну відповідь:")
lb_WrongAns3 = QLabel("Введіть третю хибну відповідь:")



# ПОЛЯ ВВОДУ
inpt_quest = QLineEdit()
inpt_right_ans = QLineEdit()
inpt_wrong_ans1 = QLineEdit()
inpt_wrong_ans2 = QLineEdit()
inpt_wrong_ans3 = QLineEdit()


# МАКЕТИ
lt_Main = QVBoxLayout()

btn_layout = QVBoxLayout()
lt_Vertical2 = QVBoxLayout()
lt_Vertical3  = QVBoxLayout()
lt_Vertical4  = QVBoxLayout()


lt_Horizontal1 = QHBoxLayout()
lt_Horizontal2 = QHBoxLayout()


# ВЕРТИКАЛЬНІ

btn_layout.addWidget(btn_goBakc, alignment=Qt.AlignLeft)
btn_layout.addWidget(btn_accept, alignment=Qt.AlignLeft)
btn_layout.addWidget(btn_clear, alignment=Qt.AlignLeft)
btn_layout.addWidget(btn_delete, alignment=Qt.AlignLeft)

lt_Vertical2 .addWidget(title, alignment=Qt.AlignCenter)
lt_Vertical2.addWidget(lb_statistik, alignment=Qt.AlignCenter)

lt_Vertical3.addWidget(Question, alignment=Qt.AlignLeft)
lt_Vertical3.addWidget(lb_RightAns, alignment=Qt.AlignLeft)
lt_Vertical3.addWidget(lb_WrongAns1, alignment=Qt.AlignLeft)
lt_Vertical3.addWidget(lb_WrongAns2, alignment=Qt.AlignLeft)
lt_Vertical3.addWidget(lb_WrongAns3, alignment=Qt.AlignLeft)


lt_Vertical4.addWidget(inpt_quest, alignment=Qt.AlignLeft)
lt_Vertical4.addWidget(inpt_right_ans, alignment=Qt.AlignLeft)
lt_Vertical4.addWidget(inpt_wrong_ans1, alignment=Qt.AlignLeft)
lt_Vertical4.addWidget(inpt_wrong_ans2, alignment=Qt.AlignLeft)
lt_Vertical4.addWidget(inpt_wrong_ans3, alignment=Qt.AlignLeft)



# ГОРИЗОНТАЛЬНІ

lt_Horizontal1.addLayout(btn_layout)
lt_Horizontal1.addLayout(lt_Vertical2)


lt_Horizontal2.addLayout(lt_Vertical3)
lt_Horizontal2.addLayout(lt_Vertical4)

lt_Main.addLayout(lt_Horizontal1)
lt_Main.addLayout(lt_Horizontal2)


window_menu.setLayout(lt_Main)
if show_window:
    window_menu.show()
