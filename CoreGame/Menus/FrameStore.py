# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\framestore.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1131, 651)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bt_left = QtWidgets.QPushButton(Frame)
        self.bt_left.setGeometry(QtCore.QRect(0, 0, 141, 651))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.bt_left.setFont(font)
        self.bt_left.setStyleSheet("")
        self.bt_left.setIconSize(QtCore.QSize(26, 16))
        self.bt_left.setDefault(False)
        self.bt_left.setFlat(True)
        self.bt_left.setObjectName("bt_left")
        self.bt_right = QtWidgets.QPushButton(Frame)
        self.bt_right.setGeometry(QtCore.QRect(986, 0, 141, 651))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.bt_right.setFont(font)
        self.bt_right.setStyleSheet("")
        self.bt_right.setIconSize(QtCore.QSize(26, 16))
        self.bt_right.setDefault(False)
        self.bt_right.setFlat(True)
        self.bt_right.setObjectName("bt_right")
        self.bt_unlock = QtWidgets.QPushButton(Frame)
        self.bt_unlock.setGeometry(QtCore.QRect(142, 0, 141, 651))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.bt_unlock.setFont(font)
        self.bt_unlock.setFlat(True)
        self.bt_unlock.setObjectName("bt_unlock")
        self.lb_disparo = QtWidgets.QPushButton(Frame)
        self.lb_disparo.setGeometry(QtCore.QRect(840, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.lb_disparo.setFont(font)
        self.lb_disparo.setStyleSheet("")
        self.lb_disparo.setIconSize(QtCore.QSize(26, 16))
        self.lb_disparo.setDefault(False)
        self.lb_disparo.setFlat(True)
        self.lb_disparo.setObjectName("lb_disparo")
        self.lb_velocity = QtWidgets.QPushButton(Frame)
        self.lb_velocity.setGeometry(QtCore.QRect(840, 60, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.lb_velocity.setFont(font)
        self.lb_velocity.setStyleSheet("")
        self.lb_velocity.setIconSize(QtCore.QSize(26, 16))
        self.lb_velocity.setDefault(False)
        self.lb_velocity.setFlat(True)
        self.lb_velocity.setObjectName("lb_velocity")
        self.lb_preco = QtWidgets.QPushButton(Frame)
        self.lb_preco.setGeometry(QtCore.QRect(840, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(12)
        self.lb_preco.setFont(font)
        self.lb_preco.setStyleSheet("")
        self.lb_preco.setIconSize(QtCore.QSize(26, 16))
        self.lb_preco.setDefault(False)
        self.lb_preco.setFlat(True)
        self.lb_preco.setObjectName("lb_preco")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.bt_left.setText(_translate("Frame", "Anterior"))
        self.bt_right.setText(_translate("Frame", "Seguinte"))
        self.bt_unlock.setText(_translate("Frame", "Desbloquear"))
        self.lb_disparo.setText(_translate("Frame", "400"))
        self.lb_velocity.setText(_translate("Frame", "400"))
        self.lb_preco.setText(_translate("Frame", "400"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

