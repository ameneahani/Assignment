import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main_window.ui")



class Calculator:
    def __init__(self):
        self.a = 0
        self.operation = ""

    def get_num(self):
        try:
            self.a = float(main_window.txtbox.text())
        except ValueError:
            self.a = 0
        main_window.txtbox.setText("")

    def subtract(self):
        self.operation = "-"
        self.get_num()

    def add(self):
        self.operation = "+"
        self.get_num()

    def devide(self):
        self.operation = "/"
        self.get_num()

    def mul(self):
        self.operation = "*"
        self.get_num()

    def math_function(self, func):
        self.get_num()
        main_window.txtbox.setText(str(func(self.a)))

    def sin(self): self.math_function(math.sin)
    def cos(self): self.math_function(math.cos)
    def tan(self): self.math_function(math.tan)
    def sqrt(self): self.math_function(math.sqrt)
    def log(self): self.math_function(math.log)
    
    def negate(self):
        self.get_num()
        main_window.txtbox.setText(str(-1*self.a))

    def percent(self):
        self.get_num()
        main_window.txtbox.setText(str(self.a/100))

    def cot(self):
        self.get_num()
        if math.tan(self.a) != 0:
            main_window.txtbox.setText(str(1/math.tan(self.a)))
        else:
            main_window.txtbox.setText("None")

    def equal(self):
        try:
            b = float(main_window.txtbox.text())
        except ValueError:
            b = 0
        
        if self.operation == "-":
            c = self.a - b
        elif self.operation == "+":
            c = self.a + b
        elif self.operation == "/" and b != 0:
            c = self.a/b
        elif self.operation == "/" and b == 0:
            c = "None"
        elif self.operation == "*":
            c = self.a*b
        else:
            c = b
        main_window.txtbox.setText(str(c))

    def clear(self):
        main_window.txtbox.setText("0")

    def append_number(self, num):
        current = main_window.txtbox.text()
        if current == "0" and num != "." :
            current = ""
        try: # if current is alphabet or None
            float(current)
        except ValueError:
            current = ""
        main_window.txtbox.setText(current+num)

    def connect_btn(self):
        main_window.btn_sub.clicked.connect(self.subtract)
        main_window.btn_sum.clicked.connect(self.add)
        main_window.btn_equal.clicked.connect(self.equal)
        main_window.btn_devide.clicked.connect(self.devide)
        main_window.btn_mul.clicked.connect(self.mul)
        main_window.btn_sin.clicked.connect(self.sin)
        main_window.btn_cos.clicked.connect(self.cos)
        main_window.btn_tan.clicked.connect(self.tan)
        main_window.btn_cot.clicked.connect(self.cot)
        main_window.btn_sqrt.clicked.connect(self.sqrt)
        main_window.btn_log.clicked.connect(self.log)
        main_window.btn_percent.clicked.connect(self.percent)
        main_window.btn_negate.clicked.connect(self.negate)
        main_window.btn_clear.clicked.connect(self.clear)

        main_window.btn_0.clicked.connect(lambda: self.append_number("0"))
        main_window.btn_1.clicked.connect(lambda: self.append_number("1"))
        main_window.btn_2.clicked.connect(lambda: self.append_number("2"))
        main_window.btn_3.clicked.connect(lambda: self.append_number("3"))
        main_window.btn_4.clicked.connect(lambda: self.append_number("4"))
        main_window.btn_5.clicked.connect(lambda: self.append_number("5"))
        main_window.btn_6.clicked.connect(lambda: self.append_number("6"))
        main_window.btn_7.clicked.connect(lambda: self.append_number("7"))
        main_window.btn_8.clicked.connect(lambda: self.append_number("8"))
        main_window.btn_9.clicked.connect(lambda: self.append_number("9"))
        main_window.btn_dot.clicked.connect(lambda:self.append_number("."))


cal = Calculator()
cal.connect_btn()
main_window.txtbox.setText("0")
main_window.show()
app.exec()
