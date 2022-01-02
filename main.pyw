from cal_form import *
import sys

class Calculator(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        self.text = ""
        self.__flag = False
        #Numbers
        self.ui.one.clicked.connect(self.__one)
        self.ui.two.clicked.connect(self.__two)
        self.ui.three.clicked.connect(self.__three)
        self.ui.four.clicked.connect(self.__four)
        self.ui.five.clicked.connect(self.__five)
        self.ui.six.clicked.connect(self.__six)
        self.ui.seven.clicked.connect(self.__seven)
        self.ui.eight.clicked.connect(self.__eight)
        self.ui.nine.clicked.connect(self.__nine)
        self.ui.zero.clicked.connect(self.__zero)
        #Simbols
        self.ui.point.clicked.connect(self.__point)
        self.ui.plus.clicked.connect(self.__plus)
        self.ui.multiplication.clicked.connect(self.__multiply)
        self.ui.minus.clicked.connect(self.__minus)
        self.ui.division.clicked.connect(self.__division)
        self.ui.equals.clicked.connect(self.__equals)
        self.ui.par_op.clicked.connect(self.__par_op)
        self.ui.par_clo.clicked.connect(self.__par_clo)
        self.ui.delete_2.clicked.connect(self.__del)
        self.ui.clear.clicked.connect(self.__clear)
        
    def __messagebox(self,text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Warning")
        msg.setInformativeText(text)
        msg.setWindowTitle("Basic Calculator")
        msg.exec_()
        
    def __one(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "1"
        self.ui.input.setText(self.text)
    
    def __two(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "2"
        self.ui.input.setText(self.text)

    def __three(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "3"
        self.ui.input.setText(self.text)
        
    def __four(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "4"
        self.ui.input.setText(self.text)
        
    def __five(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "5"
        self.ui.input.setText(self.text)
        
    def __six(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "6"
        self.ui.input.setText(self.text)
        
    def __seven(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "7"
        self.ui.input.setText(self.text)
        
    def __eight(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "8"
        self.ui.input.setText(self.text)
    
    def __nine(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "9"
        self.ui.input.setText(self.text)

    def __zero(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "0"
        self.ui.input.setText(self.text)
 
    def __plus(self):
        self.__flag = False
        self.text = self.text + "+"
        self.ui.input.setText(self.text)

    def __minus(self):
        self.__flag = False
        self.text = self.text + "-"
        self.ui.input.setText(self.text) 

    def __multiply(self):
        self.__flag = False
        self.text = self.text + "*"
        self.ui.input.setText(self.text)   

    def __division(self):
        self.__flag = False
        self.text = self.text + "/"
        self.ui.input.setText(self.text)
        
    def __par_op(self):
        self.__flag = False
        self.text = self.text + "("
        self.ui.input.setText(self.text)
        
    def __par_clo(self):
        self.__flag = False
        self.text = self.text + ")"
        self.ui.input.setText(self.text)
    
    def __del(self):
        self.__flag = False
        self.text = self.text[:-1]
        self.ui.input.setText(self.text)
    
    def __clear(self):
       self.__flag = False
       self.text = ""
       self.ui.input.setText(self.text)        

    def __point(self):
        if self.__flag == True:
            self.text = ""
            self.__flag = False
        self.text = self.text + "."
        self.ui.input.setText(self.text)

    def __equals(self):
        try:
            self.text = str(eval(self.text))
            self.ui.input.setText(self.text)
            self.__flag = True
        except SyntaxError:
            if self.text == "":
                self.__messagebox("Need a value")
            else:
                self.__messagebox("Syntax error")
        except ZeroDivisionError:
            self.__messagebox("Cannot be divided by zero")
                                 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())