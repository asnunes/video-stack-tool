from PyQt5 import QtWidgets
from ui.video_stack import VideoStack
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VideoStack()
    window.show()
    sys.exit(app.exec())