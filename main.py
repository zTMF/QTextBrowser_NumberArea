import sys

from PyQt5 import Qt
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QApplication, QTextBrowser, QWidget, QHBoxLayout, QFrame
from ToGIT.number_bar import NumberBar


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #Create Layout
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(0, 0, 0, 0)

        #Editor QTextBrowser
        self.editor = QTextBrowser()
        self.editor.setReadOnly(False)
        self.editor.setFrameShape(QFrame.Shape.NoFrame)

        #Number Area
        self.number_area = NumberBar(self.editor)

        horizontal_layout.addWidget(self.number_area)
        horizontal_layout.addWidget(self.editor)

        self.setLayout(horizontal_layout)





        self.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())