from PyQt5.QtWidgets import (QWidget, QTextEdit, QVBoxLayout)
import yaml

class memo_ui(QWidget):

    def __init__(self):
        super().__init__()

        try :
            with open('save_ocr_p.yml', 'r') as f:
                self.data = yaml.safe_load(f)
                self.memo = self.data['memo']


        except:
            with open('save_ocr_p.yml', 'w') as f:
                yaml.dump({'memo': ""}, f)
                self.memo = ""

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Write your memo here...")
        self.text_edit.setText(self.memo)
        self.text_edit.textChanged.connect(self.text_change)
        
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def text_change(self):
        print("Text changed")
        text = self.text_edit.toPlainText()
        with open('save_ocr_p.yml', 'w') as f:
            yaml.dump({'memo': text}, f)