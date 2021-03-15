import sys

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton
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
        self.window.findChild(QPushButton, 'ASharp_push').released.connect(self.ASharpKeyHeld)
        self.window.findChild(QPushButton, 'B_push').released.connect(self.BKeyHeld)
        self.window.findChild(QPushButton, 'C_push').released.connect(self.CKeyHeld)
        self.window.findChild(QPushButton, 'CSharp_push').released.connect(self.CSharpKeyHeld)
        self.window.findChild(QPushButton, 'D_push').released.connect(self.DKeyHeld)
        self.window.findChild(QPushButton, 'DSharp_push').released.connect(self.DSharpKeyHeld)
        self.window.findChild(QPushButton, 'E_push').released.connect(self.EKeyHeld)
        self.window.findChild(QPushButton, 'F_push').released.connect(self.FKeyHeld)
        self.window.findChild(QPushButton, 'FSharp_push').released.connect(self.FSharpKeyHeld)
        self.window.findChild(QPushButton, 'G_push').released.connect(self.GKeyHeld)
        self.window.findChild(QPushButton, 'GSharp_push').released.connect(self.GSharpKeyHeld)

        self.window.findChild(QPushButton, 'A2_push').released.connect(self.A2KeyHeld)
        self.window.findChild(QPushButton, 'ASharp2_push').released.connect(self.ASharp2KeyHeld)
        self.window.findChild(QPushButton, 'B2_push').released.connect(self.B2KeyHeld)
        self.window.findChild(QPushButton, 'C2_push').released.connect(self.C2KeyHeld)
        self.window.findChild(QPushButton, 'CSharp2_push').released.connect(self.CSharp2KeyHeld)
        self.window.findChild(QPushButton, 'D2_push').released.connect(self.D2KeyHeld)
        self.window.findChild(QPushButton, 'DSharp2_push').released.connect(self.DSharp2KeyHeld)
        self.window.findChild(QPushButton, 'E2_push').released.connect(self.E2KeyHeld)
        self.window.findChild(QPushButton, 'F2_push').released.connect(self.F2KeyHeld)
        self.window.findChild(QPushButton, 'FSharp2_push').released.connect(self.FSharp2KeyHeld)
        self.window.findChild(QPushButton, 'G2_push').released.connect(self.G2KeyHeld)
        self.window.findChild(QPushButton, 'GSharp2_push').released.connect(self.GSharp2KeyHeld)

        self.window.findChild(QPushButton, 'A3_push').released.connect(self.A3KeyHeld)


    def AKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass7_2_e.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def ASharpKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass6_1_f.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def BKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass5_1_g.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def CKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass5_3_a.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def CSharpKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass4_1_a .wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def DKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass3_1_d.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def DSharpKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass3_2_d .wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def EKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass3_3_e.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def FKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass2_5_a.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def FSharpKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass1_1_a .wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def GKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass1_2_b.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def GSharpKeyHeld(self):

        KeyfileName = 'sounds_folder\\bass1_3_c.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def A2KeyHeld(self):

        KeyfileName = 'sounds_folder\\bass1_4_c .wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def ASharp2KeyHeld(self):

        KeyfileName = 'sounds_folder\\bass1_5_d.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def B2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 0.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def C2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 1.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def CSharp2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 2.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def D2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 3.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def DSharp2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 4.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def E2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 5.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def F2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 6.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def FSharp2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 7.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def G2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 8.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def GSharp2KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny noise 9.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

    def A3KeyHeld(self):

        KeyfileName = 'sounds_folder\\tiny looped noise e.wav'
        self.window.findChild(QLineEdit, 'fileNameDisplay').setText(KeyfileName)
        playsound(KeyfileName)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MainWindow('mini_piano2.ui')
    sys.exit(app.exec_()) 