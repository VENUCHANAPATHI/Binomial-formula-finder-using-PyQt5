from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget,QDial,QGroupBox,QVBoxLayout,QHBoxLayout,QGridLayout,QLabel,QApplication,QPushButton,QLineEdit
import math
import sys

class Window(QWidget): #Defining class Window and deriving from QWidget class
    def __init__(self):
        super().__init__()
        #Initialising titles,geometry,icon
        self.title = "PyQt5 binomial finder"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 100
        self.icon = 'binom.png'
        self.initWindow()

    def initWindow(self):
        #Creating window
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.layout_creation()
        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)
        self.setLayout(vbox)

        self.show()

    def layout_creation(self):
        self.grpbox = QGroupBox("Choose your option from below")
        gridlayout = QGridLayout()

        self.label = QLabel("Power value of (a+b) ")

        gridlayout.addWidget(self.label,0,0)

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(6)
        #self.dial.setValue(30)
        self.dial.valueChanged.connect(self.slider_changed)
        gridlayout.addWidget(self.dial,1,0)

        self.label2 = QLabel("Value selected is")
        gridlayout.addWidget(self.label2, 0, 1)

        btn2 = QPushButton(self, text="QUIT")
        btn2.setIcon(QtGui.QIcon("close.png"))
        btn2.clicked.connect(self.close)
        gridlayout.addWidget(btn2, 2, 1)

        self.label1 = QLabel("Answer will be here")
        gridlayout.addWidget(self.label1, 2, 0)

        self.label3 = QLabel("Answer will be here")
        gridlayout.addWidget(self.label3, 1, 1)

        #self.label3.setText(str(self.dial.value()))

        self.grpbox.setLayout(gridlayout)
    def slider_changed(self):
        self.label3.setText(str(self.dial.value()))
        try:
            n = int(self.dial.value())
            if (n == 0):
                self.label1.setText("1")
            elif (n == 1):
                self.label1.setText("a+b")
            elif (n == 2):
                self.label1.setText("a^2+2ab+b^2")
            else:
                def func(x, y):
                    return (math.factorial(x) / (math.factorial(x - y) * math.factorial(y)))

                coefficents = [str(int(func(i, j))) for i, j in zip([n for i in range(n + 1)], range(n + 1)[::-1])]
                a = ["a^{}".format(i) for i in range(n + 1)[::-1]]
                b = ["b^{}".format(i) for i in range(n + 1)]
                final = [i + j for i, j in zip(a, b)]
                last = [i + j for i, j in zip(coefficents, final)]
                final_output = [
                    i.replace("a^0", '') if ('a^0' in i) else i.replace("b^0", '') if ('b^0' in i) else i.replace("a^1",'a') if ('a^1' in i) else i.replace("b^1", 'b') if ('b^1' in i) else i.replace(i, i) for i in last]
                final_output[0] = "a^{}".format(abs(int(n)))
                final_output[-1] = "b^{}".format(abs(int(n)))
                # return "+".join(last)
                # formula.set("+".join(last))
                self.label1.setText("+".join(final_output))
        except ValueError:
            self.label1.setText( "Please input a number")

    def close(self):
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
