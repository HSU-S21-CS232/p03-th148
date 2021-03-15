import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QFile, QObject

from playsound import playsound

class MainWindow(QObject):

    def __init__(self, ui_file, parent=None):

        super(MainWindow, self).__init__(parent)

        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        ui_file.close()

        self.addEventListeners()

        self.window.show()

    def addEventListeners(self):

        self.window.findChild(QPushButton, 'A_push').released.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'ASharp_push').clicked.connect(self.ASharpKeyHeld)
        self.window.findChild(QPushButton, 'B_push').pressed.connect(self.BKeyHeld)
        self.window.findChild(QPushButton, 'C_push').pressed.connect(self.CKeyHeld)
        self.window.findChild(QPushButton, 'CSharp_push').pressed.connect(self.CSharpKeyHeld)
        self.window.findChild(QPushButton, 'D_push').pressed.connect(self.DKeyHeld)
        self.window.findChild(QPushButton, 'DSharp_push').pressed.connect(self.DSharpKeyHeld)
        self.window.findChild(QPushButton, 'E_push').pressed.connect(self.EKeyHeld)
        self.window.findChild(QPushButton, 'F_push').pressed.connect(self.FKeyHeld)
        self.window.findChild(QPushButton, 'FSharp_push').pressed.connect(self.FSharpKeyHeld)
        self.window.findChild(QPushButton, 'G_push').pressed.connect(self.GKeyHeld)
        self.window.findChild(QPushButton, 'GSharp_push').pressed.connect(self.GSharpKeyHeld)

        self.window.findChild(QPushButton, 'A2_push').pressed.connect(self.A2KeyHeld)
        self.window.findChild(QPushButton, 'ASharp2_push').pressed.connect(self.ASharp2KeyHeld)
        self.window.findChild(QPushButton, 'B2_push').pressed.connect(self.B2KeyHeld)
        self.window.findChild(QPushButton, 'C2_push').pressed.connect(self.C2KeyHeld)
        self.window.findChild(QPushButton, 'CSharp2_push').pressed.connect(self.CSharp2KeyHeld)
        self.window.findChild(QPushButton, 'D2_push').pressed.connect(self.D2KeyHeld)
        self.window.findChild(QPushButton, 'DSharp2_push').pressed.connect(self.DSharp2KeyHeld)
        self.window.findChild(QPushButton, 'E2_push').pressed.connect(self.E2KeyHeld)
        self.window.findChild(QPushButton, 'F2_push').pressed.connect(self.F2KeyHeld)
        self.window.findChild(QPushButton, 'FSharp2_push').pressed.connect(self.FSharp2KeyHeld)
        self.window.findChild(QPushButton, 'G2_push').pressed.connect(self.G2KeyHeld)
        self.window.findChild(QPushButton, 'GSharp2_push').pressed.connect(self.GSharp2KeyHeld)

        self.window.findChild(QPushButton, 'A3_push').pressed.connect(self.A3KeyHeld)

    def AKeyHeld(self):

        playsound('sounds_folder\\bass1_1_a .wav')

    def ASharpKeyHeld(self):

        playsound('sounds_folder\\bass1_2_b.wav')

    def BKeyHeld(self):

        playsound('sounds_folder\\bass1_3_c.wav')

    def CKeyHeld(self):

        playsound('sounds_folder\\bass1_4_c .wav')

    def CSharpKeyHeld(self):

        playsound('sounds_folder\\bass1_5_d.wav')

    def DKeyHeld(self):

        playsound('sounds_folder\\bass2_5_a.wav')

    def DSharpKeyHeld(self):

        playsound('sounds_folder\\bass3_1_d.wav')

    def EKeyHeld(self):

        playsound('sounds_folder\\bass3_2_d .wav')

    def FKeyHeld(self):

        playsound('sounds_folder\\bass3_3_e.wav')

    def FSharpKeyHeld(self):

        playsound('sounds_folder\\bass4_1_a .wav')

    def GKeyHeld(self):

        playsound('sounds_folder\\bass5_1_g.wav')

    def GSharpKeyHeld(self):

        playsound('sounds_folder\\bass5_3_a.wav')

    def A2KeyHeld(self):

        playsound('sounds_folder\\bass6_1_f.wav')

    def ASharp2KeyHeld(self):

        playsound('sounds_folder\\bass7_2_e.wav')

    def B2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 0.wav')

    def C2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 1.wav')

    def CSharp2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 2.wav')

    def D2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 3.wav')

    def DSharp2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 4.wav')

    def E2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 5.wav')

    def F2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 6.wav')

    def FSharp2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 7.wav')

    def G2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 8.wav')

    def GSharp2KeyHeld(self):

        playsound('sounds_folder\\tiny noise 9.wav')

    def A3KeyHeld(self):

        playsound('sounds_folder\\tiny noise 0.wav')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MainWindow('mini_piano2.ui')
    sys.exit(app.exec_()) 