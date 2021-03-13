import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QFile, QObject
from playsound import playsound

playsound('StudioRhodesCsharp4R.wav')

class MainWindow(QObject):

    def __init__(self, ui_file, parent=None):

        super(MainWindow, self).__init__(parent)

        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        ui_file.close()

        self.window.show()

    def addEventListeners(self):

        A_button = self.window.FindChild(QPushButton, 'A_push')
        A_button.held.connect(self.AKeyHeld)

    def AKeyHeld(self, obj):
        AKey = self.window.findChild(QPushButton, 'A_push')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('mini_piano.ui')
    sys.exit(app.exec_()) 