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
        self.window.findChild(QPushButton, 'ASharp_push').clicked.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'B_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'C_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'CSharp_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'D_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'DSharp_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'E_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'F_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'FSharp_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'G_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'GSharp_push').pressed.connect(self.AKeyHeld)

        self.window.findChild(QPushButton, 'A2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'ASharp2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'B2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'C2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'CSharp2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'D2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'DSharp2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'E2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'F2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'FSharp2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'G2_push').pressed.connect(self.AKeyHeld)
        self.window.findChild(QPushButton, 'GSharp2_push').pressed.connect(self.AKeyHeld)

        self.window.findChild(QPushButton, 'A3_push').pressed.connect(self.AKeyHeld)

    def AKeyHeld(self):

        playsound('LilCSharp copy.wav')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MainWindow('mini_piano2.ui')
    sys.exit(app.exec_()) 