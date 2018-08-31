from PyQt5.uic.properties import QtCore

from CoreGame import Settings
from CoreGame.Menus.FrameNivel import Ui_Frame




class NivelGui(Ui_Frame):
    def __init__(self,frame,menu):
        Ui_Frame.__init__(self)

        self.setupUi(frame)
        self.frame = frame
        self.menu = menu
        check = False
        if self.menu == 0:
            for u in Settings.LEVELUNLOCKED:
                if u == Settings.currentlevel:
                    check = True


            if check:
                self.style = "QFrame{background-image:url(" + Settings.bosslist[
                    Settings.currentlevel] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;}}"
                self.label.setVisible(False)
                self.bt_unlock.setVisible(False)
            else:
                self.style = "QFrame{background-image:url(" + Settings.bosslistLOCK[
                    Settings.currentlevel] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;}}"
                self.label.setVisible(True)
                self.bt_unlock.setVisible(True)


            self.bt_right_2.setVisible(True)
            self.bt_right.setVisible(True)
            self.bt_left.setVisible(True)
            self.bt_right_2.setText("Nivel 1")
            self.bt_right_2.setStyleSheet(
                "QPushButton{background-image:url('level.png');margin: 1px;border-style: outset;background-repeat:no-repeat;background-position: center;background-color:transparent;color:#2b5259;}")

            self.label.setStyleSheet(
                "QPushButton{background-repeat:no-repeat;background-position: center;color:#2b5259;background-color:transparent;border-style: outset;margin: 1px;font-size:80px;}")

        elif self.menu == 1:
            self.style = "QFrame{background-color:#f2f2f2;}}"
            self.bt_right_2.setVisible(False)
            self.bt_right.setVisible(False)
            self.bt_left.setVisible(False)
            self.label.setText("   Modo Livre")
            self.label.setVisible(True)
            self.bt_unlock.setVisible(False)

            self.label.setStyleSheet(
                "QPushButton{background-image:url('modearcadebig.png');background-repeat:no-repeat;background-position: left;color:#2b5259;background-color:transparent;border-style: outset;margin: 1px;font-size:80px;}")

        self.frame.setStyleSheet(self.style)


        self.styleleft = """

            QPushButton{
                background-image:url('left.png');
                margin: 1px;
                border-style: outset;
                background-repeat:no-repeat;
                background-position: center;

                padding-top:120px;
                background-color:transparent;
            color:transparent;
            }
            QPushButton:hover{
                background-color:white;
                color:#2b5259;

            }

            """
        self.styleright = """

            QPushButton{
                background-image:url('right.png');
                margin: 1px;
                border-style: outset;
                background-repeat:no-repeat;
                background-position: center;
                padding-top:120px;
                background-color:transparent;
            color:transparent;
            }
            QPushButton:hover{
                background-color:white;
                color:#2b5259;

            }

            """

        self.bt_unlock.setStyleSheet("QPushButton{background-image:url('lock.png');color:transparent;background-color:transparent;background-repeat:no-repeat;padding-top:120px;background-position: center;margin: 1px;border-style: outset;}")
        self.bt_right.setStyleSheet(self.styleright)
        self.bt_left.setStyleSheet(self.styleleft)




        self.bt_right.clicked.connect(self.chooseright)
        self.bt_left.clicked.connect(self.chooseleft)


    def getframe(self):
        return self.frame

    def chooseright(self):
        check = False
        if Settings.currentlevel < len(Settings.bosslist)-1:
            Settings.currentlevel+=1
            self.bt_right_2.setText("Nivel "+str(Settings.currentlevel+1))
        self.bt_unlock.setVisible(True)
        self.label.setVisible(True)
        for u in Settings.LEVELUNLOCKED:
            if u == Settings.currentlevel:
                self.bt_unlock.setVisible(False)
                self.label.setVisible(False)
                check = True

        if check:
            self.frame.setStyleSheet("background-image:url(" + Settings.bosslist[
            Settings.currentlevel] + ") stretch stretch;background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")
        else:
            self.frame.setStyleSheet("background-image:url(" + Settings.bosslistLOCK[
                Settings.currentlevel] + ") stretch stretch;background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")

    def chooseleft(self):
        check = False
        if Settings.currentlevel > 0:
            Settings.currentlevel -= 1
            self.bt_right_2.setText("Nivel " + str(Settings.currentlevel + 1))
        self.bt_unlock.setVisible(True)
        self.label.setVisible(True)
        for u in Settings.LEVELUNLOCKED:
            if u == Settings.currentlevel:
                self.bt_unlock.setVisible(False)
                self.label.setVisible(False)
                check = True

        if check:
            self.frame.setStyleSheet("background-image:url(" + Settings.bosslist[
            Settings.currentlevel] + ") stretch stretch;background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")
        else:
            self.frame.setStyleSheet("background-image:url(" + Settings.bosslistLOCK[
                Settings.currentlevel] + ") stretch stretch;background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")


            #Settings.NAVIMG = str(Settings.backimg[Settings.currentlevel])