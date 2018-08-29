from PyQt5.uic.properties import QtCore, QtWidgets

from CoreGame import Settings
from CoreGame.Menus.FrameStore import Ui_Frame

class StoreGui(Ui_Frame):
    def __init__(self,frame):
        Ui_Frame.__init__(self)

        self.setupUi(frame)
        self.frame = frame
        self.frame.setStyleSheet("background-image:url(" + Settings.navlist[Settings.NAVSELECTED] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")

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
        self.i = 0
        self.bt_unlock.setStyleSheet("QPushButton{background-image:url('lock.png');color:transparent;background-color:transparent;padding-top:120px;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")

        self.bt_right.setStyleSheet(self.styleright)
        self.bt_left.setStyleSheet(self.styleleft)
        self.lb_velocity.setStyleSheet("QPushButton{background-image:url('velocity.png');padding-left:30px;color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: left;margin: 1px;border-style: outset;}")
        self.lb_disparo.setStyleSheet("QPushButton{background-image:url('shoot.png');padding-left:30px;color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: left;margin: 1px;border-style: outset;}")
        self.lb_preco.setStyleSheet("QPushButton{background-image:url('price.png');padding-left:30px;color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: left;margin: 1px;border-style: outset;}")

        self.bt_unlock.clicked.connect(self.unlock)
        self.bt_right.clicked.connect(self.choose)
        self.bt_left.clicked.connect(self.choose)

    def getframe(self):
        return self.frame

    def unlock(self):
        print("asd")
        if int(Settings.COINS) >= 300:
            Settings.NAVUNLOCKED.append(Settings.NAVSELECTED)
            self.bt_unlock.setVisible(False)
            #self.label_8.setVisible(False)
            Settings.COINS -= 300

    def choose(self):
        if Settings.NAVSELECTED < len(Settings.navlist)-1:
            Settings.NAVSELECTED+=1
        else:
            Settings.NAVSELECTED=0
        self.frame.setStyleSheet("background-image:url(" + Settings.navlist[
            Settings.NAVSELECTED] + ") stretch stretch;background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")

        self.bt_unlock.setVisible(True)
        #self.label_8.setVisible(True)
        for u in Settings.NAVUNLOCKED:
            if u == Settings.NAVSELECTED:
                self.bt_unlock.setVisible(False)
                #self.label_8.setVisible(False)

        Settings.NAVIMG = str(Settings.navlist[Settings.NAVSELECTED])