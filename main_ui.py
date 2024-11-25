from PyQt5.QtWidgets import (QMainWindow, QApplication, QGridLayout, QPushButton, QWidget, QCalendarWidget)
import chating_ui as cu
import memo_ui as mu

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__ui__()

    def __ui__(self):
        self.setWindowTitle("학습 관리 도구")
        self.setGeometry(100, 100, 800, 600)
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QGridLayout(self.main_widget)
        
        # Memo section
        self.memo_ui = mu.memo_ui()
        self.main_layout.addWidget(self.memo_ui, 0, 0)
        
        # Calendar section
        self.calendar = QCalendarWidget(self)
        self.main_layout.addWidget(self.calendar, 1, 0)
        
        # Chat section
        self.chating_ui = cu.chating_ui()
        self.main_layout.addWidget(self.chating_ui, 0, 1, 2, 1)











