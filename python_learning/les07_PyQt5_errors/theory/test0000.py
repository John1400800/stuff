import sys

from test_ui import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication


class PayForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # self.setupUi(test_ui)
        self.payButton.clicked.connect(self.get_data)

    def get_data(self):
        card_num = self.cardData.text()
        print(card_num)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PayForm()
    form.show()
    sys.exit(app.exec())
