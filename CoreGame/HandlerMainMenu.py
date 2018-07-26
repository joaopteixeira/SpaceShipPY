import sys
from importlib import reload

from PyQt5 import QtWidgets, QtCore

from CoreGame.Menus.MainMenu import Ui_Dialog
from CoreGame import Settings


class MyFirstGuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        self.i = 0
        self.frame.setStyleSheet("background-image:url("+Settings.navlist[self.i]+");background-repeat:no-repeat;background-position: center;")

        self.bt_rigth.clicked.connect(self.choose)
        self.bt_left.clicked.connect(self.choose)
        self.bt_play.clicked.connect(self.play)

        self.bt_unlock.clicked.connect(self.unlock)

    def play(self):
        print(Settings.NAVIMG)
        for u in Settings.NAVUNLOCKED:
            if u == self.i:
                from CoreGame import game
                reload(game)


    def unlock(self):
        if int(self.label_3.text()) >= 300:
            Settings.NAVUNLOCKED.append(self.i)
            self.bt_unlock.setVisible(False)
            self.label_3.setText(str(int(self.label_3.text())-300))






    def choose(self):




        print(len(Settings.navlist))
        if self.i < len(Settings.navlist)-1:
            self.i+=1
        else:
            self.i=0
        self.frame.setStyleSheet("background-image:url(" + Settings.navlist[
            self.i] + ");background-repeat:no-repeat;background-position: center;")
        self.bt_unlock.setVisible(True)
        for u in Settings.NAVUNLOCKED:
            if u == self.i:
                self.bt_unlock.setVisible(False)

        Settings.NAVIMG = str(Settings.navlist[self.i])
        print(Settings.NAVIMG)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())