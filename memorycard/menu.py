from PyQt5.QtWidgets import QWidget,QLineEdit, QFromLayout,QlistView,QPushButton,QVBoxLayout,QVBoxLayout,QHBoxLayout,QHBoxLayout

line_ans = QLineEdit("")
line_corect = QLineEdit("")
line_false1 = QLineEdit("")
line_false2 = QLineEdit("")
line_false3 = QLineEdit("")

form = QFromLayout()
for.addRow("Введіть запитання",line_ans)
for.addRow("Введіть правивильну відповідь",line_corect)
for.addRow("Введіть неправильний варіант",line_false1 )
for.addRow("Введіть неправильний варіант",line_false2 )
for.addRow("Введіть неправильний варіант",line_false3 )



list_q = QlistView()

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
line2.addWidget(btn_back)

line3 = QHBoxLayout()
line3.addLayout(line1)
line3.addLayout(line2)

line4 = QHBoxLayout()
line4.addWidget(btn_back, stretch=2)

main_menu_line = QHBoxLayout()
main_menu_line.addLayout(line3)
main_menu_line.addLayout(line4)



line3 = QHBoxLayout()
line4 = QHBoxLayout()
main_menu_line = QHBoxLayout()


