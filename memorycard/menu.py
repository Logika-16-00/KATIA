from PyQt5.QtWidgets import QWidget,QLineEdit, QFormLayout,QListWidget,QPushButton,QVBoxLayout,QVBoxLayout,QHBoxLayout,QHBoxLayout

line_ans = QLineEdit("")
line_corect = QLineEdit("")
line_false1 = QLineEdit("")
line_false2 = QLineEdit("")
line_false3 = QLineEdit("")

form = QFormLayout()
form.addRow("Введіть запитання",line_ans)
form.addRow("Введіть правивильну відповідь",line_corect)
form.addRow("Введіть неправильний варіант",line_false1 )
form.addRow("Введіть неправильний варіант",line_false2 )
form.addRow("Введіть неправильний варіант",line_false3 )



list_q = QListWidget()

btn_add = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
btn_back = QPushButton("нАзад")

wdgt_edit = QWidget()
wdgt_edit.setLayout(form)

line1 = QVBoxLayout()
line1.addWidget(list_q)
line1.addWidget(btn_add)
line2 = QVBoxLayout()
line2.addWidget(wdgt_edit)
line2.addWidget(btn_clear)

line3 = QHBoxLayout()
line3.addLayout(line1)
line3.addLayout(line2)


main_menu_line = QVBoxLayout()
main_menu_line.addLayout(line3)

main_menu_line.addWidget(btn_back)

