# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(346, 530, 75, 51))
        self.btn_right.setStyleSheet("color: rgb(255, 57, 229);")
        self.btn_right.setObjectName("btn_right")
        self.btn_flip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_flip.setGeometry(QtCore.QRect(436, 530, 75, 51))
        self.btn_flip.setStyleSheet("color: rgb(255, 0, 4);")
        self.btn_flip.setObjectName("btn_flip")
        self.btn_sharp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sharp.setGeometry(QtCore.QRect(526, 530, 75, 51))
        self.btn_sharp.setStyleSheet("color: rgb(8, 0, 255);")
        self.btn_sharp.setObjectName("btn_sharp")
        self.btn_bw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bw.setGeometry(QtCore.QRect(616, 530, 121, 51))
        self.btn_bw.setStyleSheet("color: rgb(255, 177, 19);")
        self.btn_bw.setObjectName("btn_bw")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(230, 530, 101, 51))
        self.btn_left.setStyleSheet("color: rgb(170, 85, 127);")
        self.btn_left.setObjectName("btn_left")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 70, 491, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_dir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dir.setGeometry(QtCore.QRect(35, 9, 171, 51))
        self.btn_dir.setStyleSheet("color: rgb(255, 0, 0);")
        self.btn_dir.setObjectName("btn_dir")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 181, 501))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 70, 369, 371))
        self.label.setStyleSheet("color: rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(740, 530, 91, 51))
        self.btn_save.setStyleSheet("color: rgb(255, 0, 127);")
        self.btn_save.setObjectName("btn_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_right.setText(_translate("MainWindow", "Вправо"))
        self.btn_flip.setText(_translate("MainWindow", "джерело"))
        self.btn_sharp.setText(_translate("MainWindow", "Різкість "))
        self.btn_bw.setText(_translate("MainWindow", "Ч/Б"))
        self.btn_left.setText(_translate("MainWindow", "Вліво"))
        self.btn_dir.setText(_translate("MainWindow", "Папка"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn_save.setText(_translate("MainWindow", "Зберегти"))

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
