from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QPainter, Qt, QTextCursor, QKeyEvent, QFont, QPen
from PySide6.QtWidgets import QWidget



#https://stackoverflow.com/questions/2443358/how-to-add-lines-numbers-to-qtextedit

class NumberBar(QWidget):
    def __init__(self, parent=None):
        super(NumberBar, self).__init__(parent)
        self.editor = parent
        self.editor.document().blockCountChanged.connect(self.update_width)
        self.editor.verticalScrollBar().valueChanged.connect(self.update_on_scroll)
        self.editor.keyReleaseEvent = self.update_on_scroll
        self.update_width('1')


    def update_on_scroll(self, scroll):
        if type(scroll) == QKeyEvent:
            self.update()
            scroll.accept()
            return
        if self.isVisible():
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update()

    def update_width(self, string):
        width = self.fontMetrics().boundingRect(str(string)).width() + 8
        if self.width() != width:
            self.setFixedWidth(width)


    def paintEvent(self, event):

        if self.isVisible():
            cur = self.editor.textCursor()
            cur.movePosition(QTextCursor.Start)
            block = cur.block()

            height = self.fontMetrics().height()
            number = block.blockNumber()
            font = QFont("Times", 10, QFont.Bold)
            pen = QPen(QColor(50, 50, 50), 1, Qt.SolidLine)
            painter = QPainter(self)
            painter.setPen(pen)
            painter.fillRect(event.rect(), QColor(255, 255, 255))


            current_block = self.editor.textCursor().blockNumber() + 1

            condition = True

            while block.isValid() and condition:
                r2 = self.editor.document().documentLayout().blockBoundingRect(block).translated(
                    self.editor.viewport().geometry().x(),
                    self.editor.viewport().geometry().y() -
                    (self.editor.verticalScrollBar().sliderPosition())
                    ).toRect()
                number += 1

                rect = QRect(0,  r2.top() + 2, self.width() - 5, height)

                if number == current_block:
                    font.setBold(True)
                else:
                    font.setBold(False)

                painter.setFont(font)
                painter.drawText(rect, Qt.AlignRight, '%i' % number)

                if r2.top() > event.rect().bottom():
                    condition = False

                block = block.next()
            painter.end()