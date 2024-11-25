from PyQt5.QtWidgets import (QWidget, QTextBrowser, QVBoxLayout)


class chating_ui(QWidget):


    def __init__(self):
        super().__init__()
        self.text_browser = QTextBrowser(self)
        
        # Method 1: Set fixed size using setGeometry
        self.text_browser.setGeometry(10, 10, 400, 300)  # x, y, width, height
        
        # Method 2: Use a layout manager
        layout = QVBoxLayout()
        layout.addWidget(self.text_browser)
        self.setLayout(layout)
        
        self.text_browser.setOpenExternalLinks(True)



