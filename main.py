import sys
# import os
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import QFile, QObject

from playsound import playsound

# from pydub import AudioSegment
# from pydub.playback import play

# cwd = os.getcwd()

# wavepath = cwd+'\\StudioRhodesCsharp4R.wav'

# sound = AudioSegment.from_file(wavepath, format="wav")

# play(sound)
# print(sound.frame_rate)

# octaves = -0.5

# new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

# adjusted_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

# play(adjusted_sound)

class MainWindow(QObject):

    def __init__(self, ui_file, parent=None):

        super(MainWindow, self).__init__(parent)

        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        ui_file.close()

        # self.addEventListeners()

        self.window.show()

    def addEventListeners(self):

        self.window.findChild(QPushButton, 'A_push').clicked.connect(playsound('StudioRhodesCsharp4R.wav'))

    def AKeyHeld(self):
        self.playsound('StudioRhodesCsharp4R.wav')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('mini_piano2.ui')
    sys.exit(app.exec_()) 