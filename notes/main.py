from PyQt5.QtWidgets import QApplication,QInputDialog
from PyQt5.QtWidgets import QMainWindow
from notes import Ui_MainWindow
import json


import json
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_make.clicked.connect(self.add_note)
        for note in notes.keys():
            self.ui.list_1.addItem(note)
        self.ui.list_1.itemDoubleClicked.connect(self.show_note)
        self.ui.btn_tag.clicked.connect(self.add_tag)
    def show_note(self):
        self.ui.list_1.clear()
        self.ui.list_2.clear()
        note_name = item.text()

        if note_name in notes:
            self.ui.list_2.addItem(notes[note_name]["теги"])
            self.ui.lineEdit.setText(notes[note_name]["текст"])

    def add_tag(self):
    
        if self.ui.list_1.currentItem():
            tag_name,ok =QInputDialog.getText(self,"Додати тег","Введіть тег")
            if tag_name and ok:
               
                note_name =self.ui.list_1.currentItem().text()
                if note_name in notes[note_name]["теги"]:
                    self.ui.list_2.addItem(tag_name)
                    notes[note_name]["теги"].append(tag_name)
            self.write_to_file()

    def delete_note(self):
        if self.ui.list_1.currentItem() and self.ui.list_2.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            tag_name = self.ui.list_2.currentItem().text()
            self.ui.list_1.takeItem(self.ui.list_1.currentRow())
            notes[note_name]["теги"].remove(tag_name)                                  
        self.write_to_file()

    def delete_tag(self):
        if self.ui.list_1.currentItem():
            note_name = self.ui.list_1.currentItem().text()
            del notes[note_name]
            self.ui.list_1.takeItem(self.ui.list_1.currentRow())
        self.write_to_file()



    def add_note(self):
        note_name,ok = QInputDialog.getText(self , "Додати замітку" , "Назва замітки")
        if ok and note_name != "":
            notes[note_name] = {"теги": [], "текст":""}
            self.ui.list_1.addItem(note_name)
        self.write_to_file()
    def write_to_file(self):
        with open("notes/notes.json","w",encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)


with open("notes/notes.json","r",encoding="utf-8") as file:
    notes = json.load(file)
print(notes)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()