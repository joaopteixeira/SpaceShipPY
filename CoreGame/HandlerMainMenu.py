import sys
from importlib import reload

from PyQt5 import QtWidgets, QtCore

from CoreGame.Menus.MainMenu import Ui_Dialog
from CoreGame import Settings
from CoreGame.Menus.HandlerStore import StoreGui
from CoreGame.Menus.Controller.HandlerMenuNivel import NivelGui
from CoreGame.Menus.service.ServNav import ServNav




class MyFirstGuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setupUi(dialog)
        self.uiframe = NivelGui(QtWidgets.QFrame(self.widget),0)
        self.frame = self.uiframe.getframe()
        self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
        self.menu = 0


        self.style = """

                QPushButton{
                    background-image:url('store.png');
                    background-repeat:no-repeat;
                    margin: 1px;
                    border-style: outset;
                    text-align:bottom;
                     padding-bottom:7px;
                    background-position: center;
                    background-color:white;
                    color:white;
                }
                QPushButton:hover{
                    background-color:#f2f2f2;
                    color:#2b5259;
                    
                }
                

                """
        self.stylels = """

                QLabel{
                    background-image:url('lastscore.png');
                    background-repeat:no-repeat;
                    background-position: center;
                    background-color:white;
                color:white;
                }
                QLabel:hover{
                    background-color:#f2f2f2;
                    color:black;
                }

                """
        self.stylebs = """

                QLabel{
                    background-image:url('bigscore.png');
                    background-repeat:no-repeat;
                    background-position: center;
                    background-color:white;
                color:white;
                }
                QLabel:hover{
                    background-color:#f2f2f2;
                    color:black;

                }

                """
        self.styleexit = """

                QPushButton{
                    background-image:url('exit.png');
                    background-repeat:no-repeat;
                    margin: 1px;
                    border-style: outset;
                    text-align:bottom;
                    background-position: center;
                    background-color:white;
                color:white;
                }
                QPushButton:hover{
                    background-color:#f2f2f2;
                    color:#2b5259;

                }

                """

        self.stylefreecoins = """

            QPushButton{
                background-image:url('movie.png');
                background-repeat:no-repeat;
                margin: 1px;
                border-style: outset;
                text-align:bottom;
                padding-bottom:7px;
                background-position: center;
                background-color:white;
                color:white;
            }
            QPushButton:hover{
                background-color:#f2f2f2;
                color:#2b5259;

            }


            """

        #self.widget.setStyleSheet(self.style);
        # 0d111c
        self.frame.setVisible(True)
        self.label_3.setText(str(Settings.COINS))
        self.i = 0



        self.barra.setStyleSheet("QWidget{background-color:white;}")

        if self.menu == 0:
            self.bt_nav.setText("Niveis")
            self.bt_powerup.setText("Modo Livre")

            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('modelevel.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('modearcade.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")

        elif self.menu == 1:
            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('navicon.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('powerupicon.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")


        self.bt_play.setStyleSheet("QPushButton{background-image:url('play.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
        self.bt_back.setStyleSheet("QPushButton{background-image:url('anterior.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
        self.label_3.setStyleSheet("QLabel{background-image:url('coins.png');background-repeat:no-repeat;margin: 1px; border-style: outset;text-align:bottom;padding-top:40px;background-position: center;background-color:white;color:#2b5259;}")


        #self.bt_right_2.setStyleSheet(self.styleright)
        #self.bt_left_2.setStyleSheet(self.styleleft)
        self.widget.setStyleSheet("background-color:#f2f2f2")
        self.ls_icon.setStyleSheet(self.stylels)
        self.bs_icon.setStyleSheet(self.stylebs)
        self.ls_freecoins.setStyleSheet(self.stylefreecoins)
        #self.label_9.setStyleSheet("")
        self.bt_store.setStyleSheet(self.style)
        self.label.setStyleSheet("background-image:url('logo.png');background-repeat:no-repeat;background-position: left;background-color:white;color:#2b5259;")
        self.lb_exit.setStyleSheet(self.styleexit)
        #self.label_4.setStyleSheet("QLabel{background-image:url('storebig.png');color:#2b5259;background-color:transparent;background-position: left;background-repeat:no-repeat;margin: 1px;border-style: outset;}")

        self.bt_play.clicked.connect(self.play)

        #self.bt_unlock.clicked.connect(self.unlock)
        self.bt_store.clicked.connect(self.store)
        self.bt_powerup.clicked.connect(self.handlebtpw)
        self.bt_nav.clicked.connect(self.handlebtnav)
        self.bt_back.clicked.connect(self.handlerbtanterior)


    def handlebtnav(self):
        if self.menu == 1:
            Settings.NAVSELECTED = 0
            self.uiframe = StoreGui(QtWidgets.QFrame(self.widget), 0)
            self.frame = self.uiframe.getframe()
            self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
            self.label_3.setText(str(Settings.COINS))
            self.frame.show()
        elif self.menu == 0:
            self.uiframe = NivelGui(QtWidgets.QFrame(self.widget), 0)
            self.frame = self.uiframe.getframe()
            self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
            self.label_3.setText(str(Settings.COINS))
            self.frame.show()

    def handlebtpw(self):
        if self.menu == 1:
            for i in Settings.NAVUNLOCKED:
                if i == Settings.NAVSELECTED:
                    self.uiframe = StoreGui(QtWidgets.QFrame(self.widget), 1)
                    self.frame = self.uiframe.getframe()
                    self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
                    self.label_3.setText(str(Settings.COINS))
                    self.frame.show()


        elif self.menu == 0:
            self.uiframe = NivelGui(QtWidgets.QFrame(self.widget), 1)
            self.frame = self.uiframe.getframe()
            self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
            self.label_3.setText(str(Settings.COINS))
            self.frame.show()


    def store(self):
        self.uiframe = StoreGui(QtWidgets.QFrame(self.widget),0)
        self.frame = self.uiframe.getframe()
        self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
        self.label_3.setText(str(Settings.COINS))
        self.frame.show()
        self.style = """QPushButton{background-image:url('store.png');background-repeat:no-repeat;margin: 1px;border-style: outset;text-align:bottom;background-position: center;background-color:#f2f2f2;color:#2b5259;
            }
            
            """
        self.bt_store.setStyleSheet(self.style)
        self.menu = 1
        self.mudarmenu()

    def play(self):
        print(Settings.NAVIMG)
        for u in Settings.NAVUNLOCKED:
            if u == Settings.NAVSELECTED:
                from CoreGame import game
                reload(game)

    def mudarmenu(self):
        if self.menu == 0:
            self.bt_nav.setText("Niveis")
            self.bt_powerup.setText("Modo Livre")

            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('modelevel.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('modearcade.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")

        elif self.menu == 1:
            self.bt_nav.setText("Navs")
            self.bt_powerup.setText("PowerUps")
            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('navicon.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('powerupicon.png');color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")


    def reloadstyle(self):
        self.style = """QPushButton{background-image:url('store.png'); background-repeat:no-repeat;margin: 1px;
                border-style: outset;
                text-align:bottom;
                background-position: center;
                background-color:white;
                color:white;
            }
            QPushButton:hover{
                background-color:#f2f2f2;
                color:#2b5259;

            }


            """
        self.bt_store.setStyleSheet(self.style)

    def handlerbtanterior(self):
        self.reloadstyle()
        self.uiframe = NivelGui(QtWidgets.QFrame(self.widget),0)
        self.frame = self.uiframe.getframe()
        self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
        self.label_3.setText(str(Settings.COINS))
        self.frame.show()
        self.menu = 0
        self.mudarmenu()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())