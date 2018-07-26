# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1125, 804)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1161, 811))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(620, 270, 411, 221))
        self.frame.setStyleSheet("background-image:url(..RD2.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_unlock = QtWidgets.QPushButton(self.frame)
        self.bt_unlock.setGeometry(QtCore.QRect(0, 90, 411, 41))
        self.bt_unlock.setObjectName("bt_unlock")
        self.bt_left = QtWidgets.QPushButton(self.widget)
        self.bt_left.setGeometry(QtCore.QRect(550, 270, 75, 221))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.bt_left.setFont(font)
        self.bt_left.setStyleSheet("background-color:transparent;")
        self.bt_left.setObjectName("bt_left")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(720, 10, 47, 41))
        self.label_3.setObjectName("label_3")
        self.bt_play = QtWidgets.QPushButton(self.widget)
        self.bt_play.setGeometry(QtCore.QRect(620, 530, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt_play.setFont(font)
        self.bt_play.setStyleSheet("background-color:white;")
        self.bt_play.setObjectName("bt_play")
        self.bt_rigth = QtWidgets.QPushButton(self.widget)
        self.bt_rigth.setGeometry(QtCore.QRect(1030, 270, 75, 221))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.bt_rigth.setFont(font)
        self.bt_rigth.setStyleSheet("background-color:transparent;")
        self.bt_rigth.setObjectName("bt_rigth")
        self.bt_play_2 = QtWidgets.QPushButton(self.widget)
        self.bt_play_2.setGeometry(QtCore.QRect(620, 200, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.bt_play_2.setFont(font)
        self.bt_play_2.setStyleSheet("background-color:white;")
        self.bt_play_2.setObjectName("bt_play_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(650, 10, 91, 41))
        self.label_2.setObjectName("label_2")
        self.barra = QtWidgets.QWidget(self.widget)
        self.barra.setGeometry(QtCore.QRect(80, 0, 281, 811))
        self.barra.setStyleSheet("background-color:#101723;")
        self.barra.setObjectName("barra")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.bt_unlock.setText(_translate("Dialog", "Unlocked"))
        self.bt_left.setText(_translate("Dialog", "<"))
        self.label_3.setText(_translate("Dialog", "1000"))
        self.bt_play.setText(_translate("Dialog", "Play"))
        self.bt_rigth.setText(_translate("Dialog", ">"))
        self.bt_play_2.setText(_translate("Dialog", "Back"))
        self.label_2.setText(_translate("Dialog", "Coins"))

        self.widget.setStyleSheet("background-image:url(back.jpg)")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

