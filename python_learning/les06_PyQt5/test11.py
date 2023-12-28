import sys
from tkinter import N
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(371, 565)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 328, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QLCDNumber(self.layoutWidget)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn8 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn8.setMinimumSize(QtCore.QSize(80, 80))
        self.btn8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.buttonGroup_digits = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_digits.setObjectName("buttonGroup_digits")
        self.buttonGroup_digits.addButton(self.btn8)
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn2.setMinimumSize(QtCore.QSize(80, 80))
        self.btn2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.buttonGroup_digits.addButton(self.btn2)
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_plus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_plus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.buttonGroup_binary = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_binary.setObjectName("buttonGroup_binary")
        self.buttonGroup_binary.addButton(self.btn_plus)
        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_eq.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_eq.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_eq.setFont(font)
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout.addWidget(self.btn_eq, 3, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn0.setMinimumSize(QtCore.QSize(80, 80))
        self.btn0.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.buttonGroup_digits.addButton(self.btn0)
        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_div.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_div.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.buttonGroup_binary.addButton(self.btn_div)
        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.buttonGroup_digits.addButton(self.btn1)
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn9.setMinimumSize(QtCore.QSize(80, 80))
        self.btn9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.buttonGroup_digits.addButton(self.btn9)
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_dot.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_dot.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 3, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn3.setMinimumSize(QtCore.QSize(80, 80))
        self.btn3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.buttonGroup_digits.addButton(self.btn3)
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn4.setMinimumSize(QtCore.QSize(80, 80))
        self.btn4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.buttonGroup_digits.addButton(self.btn4)
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn5.setMinimumSize(QtCore.QSize(80, 80))
        self.btn5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.buttonGroup_digits.addButton(self.btn5)
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn7.setMinimumSize(QtCore.QSize(80, 80))
        self.btn7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.buttonGroup_digits.addButton(self.btn7)
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.layoutWidget)
        self.btn6.setMinimumSize(QtCore.QSize(80, 80))
        self.btn6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.buttonGroup_digits.addButton(self.btn6)
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_minus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_minus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.buttonGroup_binary.addButton(self.btn_minus)
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_mult.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_mult.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.buttonGroup_binary.addButton(self.btn_mult)
        self.gridLayout.addWidget(self.btn_mult, 2, 3, 1, 1)
        self.btn_pow = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_pow.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_pow.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.buttonGroup_binary.addButton(self.btn_pow)
        self.gridLayout.addWidget(self.btn_pow, 4, 0, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_sqrt.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 4, 1, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_fact.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_fact.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_fact.setFont(font)
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout.addWidget(self.btn_fact, 4, 2, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_clear.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(254, 166, 43);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn_plus.setText(_translate("Form", "+"))
        self.btn_eq.setText(_translate("Form", "="))
        self.btn0.setText(_translate("Form", "0"))
        self.btn_div.setText(_translate("Form", "/"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn_dot.setText(_translate("Form", "."))
        self.btn3.setText(_translate("Form", "3"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn_minus.setText(_translate("Form", "-"))
        self.btn_mult.setText(_translate("Form", "*"))
        self.btn_pow.setText(_translate("Form", "^"))
        self.btn_sqrt.setText(_translate("Form", "√"))
        self.btn_fact.setText(_translate("Form", "!"))
        self.btn_clear.setText(_translate("Form", "С"))


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cash_number = '0'
        self.op = None
        self.op_div = False
        self.res = '0'
        self.table.display(self.res)

        for el in (self.btn0, self.btn1, self.btn2, self.btn3,
                   self.btn4, self.btn5, self.btn6, self.btn7,
                   self.btn8, self.btn9, self.btn_dot):
            el.clicked.connect(self.number)

        for el in (self.btn_plus, self.btn_minus, self.btn_mult,
                   self.btn_div, self.btn_pow):
            el.clicked.connect(self.operation)

        for el in (self.btn_clear, self.btn_sqrt, self.btn_fact):
            el.clicked.connect(self.one_arg_op)

        self.btn_eq.clicked.connect(self.eq_op)

    def one_arg_op(self):
        imp = self.sender().text()
        if imp == 'С':
            self.res = '0'
        if imp == '!':
            n = int(float(self.res))
            factorial = 1
            for i in range(2, n+1):
                factorial *= i
            self.res = str(factorial)
        if imp == '√':
            self.res = str(int(self.res) ** 0.5)
        self.table.display(self.res)

    def ce(self):
        self.res = '0'
        self.table.display(self.res)

    def number(self):
        inp = self.sender().text()
        print(inp)
        if self.op != None or self.res == 'Error':
            self.res = '0'
        if inp == '0' and self.res != '0':
            self.res += '0'
        elif inp != '0':
            if '.' not in self.res and inp == '.':
                self.res += inp
            elif inp != '.':
                if self.res != '0':
                    self.res += inp
                else:
                    self.res = inp
        self.table.display(self.res)

    def operation(self):
        inp = self.sender().text()
        self.cash_number = self.res
        self.res = '0'
        if inp == '+':
            self.op = lambda: (
                float(self.cash_number) + float(self.res))
        elif inp == '-':
            self.op = lambda: (
                float(self.cash_number) - float(self.res))
        elif inp == '*':
            self.op = lambda: (
                float(self.cash_number) * float(self.res))
        elif inp == '^':
            self.op = lambda: (
                float(self.cash_number) ** float(self.res))
        elif inp == '/':
            self.op_div = True
            self.op = lambda: (
                float(self.cash_number) / float(self.res))

    def eq_op(self):
        if self.op and not (self.op_div and float(self.res) == 0.0):
            res = str(self.op())
            if len(res) >= 2 and res[-2:] == '.0':
                res = res[:-2]
        elif self.op == None:
            res = self.res
        else:
            res = 'Error'
        self.table.display(res)
        self.res = res
        self.op = None
        self.op_div = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
