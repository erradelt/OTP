import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

import otp_encrypter_ui
import otp_decrypter_ui

class MasterWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UIsetting()
              
    def UIsetting(self):
        self.setGeometry (200,200,700,700)
        self.setWindowTitle('OneTimePad')
        self.table_widget = GuiTabs(self)
        self.setCentralWidget(self.table_widget)      
        self.show()

class Encrypter(QWidget):
    def __init__(self):
        super().__init__()
        self.encrypterwindow()
    
    def encrypterwindow(self):
        self.encrypter = otp_encrypter_ui.MyMainWindow()
        layout = QVBoxLayout(self)
        layout.addWidget(self.encrypter)
        self.setLayout(layout)

class Decrypter(QWidget):
    def __init__(self):
        super().__init__()
        self.decrypterwindow()
    
    def decrypterwindow(self):
        self.decrypter = otp_decrypter_ui.MyMainWindow()
        layout = QVBoxLayout(self)
        layout.addWidget(self.decrypter)
        self.setLayout(layout)

class GuiTabs(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)      
        self.tabbar = QTabWidget()

        self.encrypter_tab = Encrypter()
        self.decrypter_tab = Decrypter()

        self.tabbar.addTab(self.encrypter_tab, 'encrypter')
        self.tabbar.addTab(self.decrypter_tab, 'decrypter')

        self.layout.addWidget(self.tabbar)
        self.setLayout(self.layout)
    
def main():
    app = QApplication(sys.argv)
    ex = MasterWin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
