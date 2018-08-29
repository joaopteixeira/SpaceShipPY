from CoreGame import Settings
from CoreGame.Menus.FrameNivel import Ui_Frame



class NivelGui(Ui_Frame):
    def __init__(self,frame):
        Ui_Frame.__init__(self)

        self.setupUi(frame)
        self.frame = frame
        self.frame.setStyleSheet("background-repeat:no-repeat;background-position: center;background-color:#f2f2f2;")

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

    def getframe(self):
        return self.frame