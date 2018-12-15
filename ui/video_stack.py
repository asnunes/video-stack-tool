from PyQt5 import QtWidgets, uic

class VideoStack(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(VideoStack, self).__init__()
        self.uic = uic.loadUi('ui/templates/video_stack.ui', self)
