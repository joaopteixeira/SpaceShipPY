from PyQt5.uic.properties import QtCore, QtWidgets

from CoreGame import Settings
from CoreGame.Menus.FrameStore import Ui_Frame
from CoreGame.Menus.service.ServNav import ServNav
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QByteArray,Qt

class StoreGui(Ui_Frame):
    def __init__(self,frame,menu):
        Ui_Frame.__init__(self)

        self.setupUi(frame)
        self.frame = frame
        self.menu = menu
        if self.menu == 0:
            self.frame.setStyleSheet("background-image:url(" + Settings.navlist[Settings.NAVSELECTED] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")
            self.nav_pw.setVisible(False)
        elif self.menu == 1:
            self.nav_pw.setVisible(True)
            self.nav_pw.setStyleSheet(
                "QPushButton{background-image:url(" + Settings.navlistMINI[Settings.NAVSELECTED] + ");color:#2b5259;padding-top:60px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")

            self.frame.setStyleSheet("background-image:url(" + Settings.poweruplist[
                Settings.POWERUPSELECTED] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")

        self.navs = ServNav()
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
        self.lb_velocity.setStyleSheet("QPushButton{background-image:url('velocity.png');padding-left:30px;color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: right;margin: 1px;border-style: outset;}")
        self.lb_disparo.setStyleSheet("QPushButton{background-image:url('shoot.png');padding-left:30px;color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: right;margin: 1px;border-style: outset;}")
        self.lb_preco.setStyleSheet("QPushButton{background-image:url('price.png');padding-left:30px;color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: right;margin: 1px;border-style: outset;}")
        self.lb_vida.setStyleSheet("QPushButton{background-image:url('life.png');padding-left:30px;color:#2b5259;background-repeat:no-repeat;background-color:transparent;background-position: right;margin: 1px;border-style: outset;}")

        self.lb_preco.setText(str(self.navs.getnavs()[0].getpreco()))
        self.lb_velocity.setText(str(self.navs.getnavs()[0].getvelocidade()))
        self.lb_disparo.setText(str(self.navs.getnavs()[0].getdisparo()))
        self.lb_vida.setText(str(self.navs.getnavs()[0].getvida()))

        self.bt_unlock.clicked.connect(self.unlock)
        self.bt_right.clicked.connect(self.chooseright)
        self.bt_left.clicked.connect(self.chooseleft)


        #GIF
        #self.movie = QMovie("123.gif", QByteArray(), self.frame)
        #self.movie.setCacheMode(QMovie.CacheAll)
        #self.movie.setSpeed(100)
        #self.label.setAlignment(Qt.AlignCenter)
        #self.label.setMovie(self.movie)

#        self.movie.start()





    def getframe(self):
        return self.frame

    def unlock(self):
        print("asd")
        if self.menu == 0:
            if int(Settings.COINS) >= self.navs.getnavs()[Settings.NAVSELECTED].getpreco():
                Settings.NAVUNLOCKED.append(Settings.NAVSELECTED)
                self.bt_unlock.setVisible(False)
                #self.label_8.setVisible(False)
                Settings.COINS -= self.navs.getnavs()[Settings.NAVSELECTED].getpreco()
        elif self.menu == 1:
            if int(Settings.COINS) >= 100:
                Settings.POWERUPUNLOCKED.append(Settings.POWERUPSELECTED)
                self.bt_unlock.setVisible(False)
                Settings.COINS -= 100
                self.navs.getnavs()[Settings.NAVSELECTED].set


    def chooseleft(self):
        if self.menu == 0:
            if Settings.NAVSELECTED > 0:
                Settings.NAVSELECTED-=1
                self.lb_preco.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getpreco()))
                self.lb_velocity.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getvelocidade()))
                self.lb_disparo.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getdisparo()))
                self.lb_vida.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getvida()))

            self.bt_unlock.setVisible(True)
            #self.label_8.setVisible(True)
            for u in Settings.NAVUNLOCKED:
                if u == Settings.NAVSELECTED:
                    self.bt_unlock.setVisible(False)
                    #self.label_8.setVisible(False)

            Settings.NAVIMG = str(Settings.navlist[Settings.NAVSELECTED])
            self.frame.setStyleSheet("background-image:url(" + Settings.navlist[
                Settings.NAVSELECTED] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")

        elif self.menu == 1:
            if Settings.POWERUPSELECTED > 0:
                Settings.POWERUPSELECTED-=1
                self.bt_unlock.setVisible(True)
            for u in Settings.POWERUPUNLOCKED:
                if u == Settings.POWERUPSELECTED:
                    self.bt_unlock.setVisible(False)

            self.frame.setStyleSheet("background-image:url(" + Settings.poweruplist[
                Settings.POWERUPSELECTED] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")

    def chooseright(self):
        if self.menu == 0:
            if Settings.NAVSELECTED < len(Settings.navlist)-1:
                print("entrei")
                Settings.NAVSELECTED += 1
                self.lb_preco.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getpreco()))
                self.lb_velocity.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getvelocidade()))
                self.lb_disparo.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getdisparo()))
                self.lb_vida.setText(str(self.navs.getnavs()[Settings.NAVSELECTED].getvida()))

            self.bt_unlock.setVisible(True)
            # self.label_8.setVisible(True)
            for u in Settings.NAVUNLOCKED:
                if u == Settings.NAVSELECTED:
                    self.bt_unlock.setVisible(False)
                    # self.label_8.setVisible(False)

            Settings.NAVIMG = str(Settings.navlist[Settings.NAVSELECTED])
            self.frame.setStyleSheet("background-image:url(" + Settings.navlist[
                Settings.NAVSELECTED] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")


        elif self.menu == 1:
            if Settings.POWERUPSELECTED < len(Settings.poweruplist)-1:
                Settings.POWERUPSELECTED += 1
                self.bt_unlock.setVisible(True)
            for u in Settings.POWERUPUNLOCKED:
                if u == Settings.POWERUPSELECTED:
                    self.bt_unlock.setVisible(False)

            self.frame.setStyleSheet("background-image:url(" + Settings.poweruplist[
                Settings.POWERUPSELECTED] + ");background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")
