import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: #333; color: #fff; font-size: 18px;")
        self.setup()
        
        
    def setup(self):
        
        self.btns=[
            ('H',0,0),('^',0,1),('Delete',0,2),('Clear',0,3),
            ('7',1,0),('8',1,1),('9',1,2),('*',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('/',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('.',4,0),('0',4,1),('+',4,2),('=',4,3),
        ]
        
        self.History = QTextBrowser()
        self.historylay = QVBoxLayout()
        self.historylay.addWidget(self.History) 
        
        self.layout = QGridLayout()
        min = QWidget()
        man = QWidget()
        min.setLayout(self.layout)
        man.setLayout(self.historylay)

        
        
        for x,y,z in self.btns:
            btn = QPushButton(x)
            btn.clicked.connect(self.btnop)
            btn.setFixedHeight(70)
            self.layout.addWidget(btn,y,z)
            if x == 'H':
                btn.setCheckable(True)
                
                

        self.scrn = QLabel()
        self.scrn.setFixedHeight(100)
        self.scrn.setFont(QFont('Arial', 90))
        self.scrn.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setWindowIcon(QIcon('calculator.png'))
        
        self.hisgrid = QStackedLayout()
        self.hisgrid.addWidget(man)
        self.hisgrid.addWidget(min)
        self.hisgrid.setCurrentIndex(1)
                
        mainlayout = QVBoxLayout()      
        mainlayout.addWidget(self.scrn)
        mainlayout.addLayout(self.hisgrid)
        
        mai = QWidget()
        mai.setLayout(mainlayout)
        
        self.setFixedSize(300, 500)
        self.setWindowTitle('Calculator') 
        self.setCentralWidget(mai)
        
        
        
    def btnop(self, checked):
        btn = self.sender()
        
        
            
        if btn.text() == '=':
            if '^' in self.scrn.text():
                j = self.scrn.text()
                self.scrn.setText(str(eval(self.scrn.text().replace('^','**'))))
                m = self.scrn.text()
                self.History.append('%s = %s' %(j,m))
            else:
                try:
                    j = self.scrn.text()
                    self.scrn.setText(str(eval(self.scrn.text())))
                    m = self.scrn.text()
                    self.History.append('%s = <br>%s</br>' %(j,m))
                except Exception as e:
                    self.scrn.setText('Math Error')
        elif btn.text() == 'Delete':
            try:
                self.scrn.setText(self.scrn.text().replace(self.scrn.text()[-1], ''))
            except:
                self.scrn.setText('')
        elif btn.text() == 'Clear':
            self.scrn.setText('')
        elif btn.text() == 'H':
            if btn.isChecked():
                self.historylay.addWidget(btn)
                self.hisgrid.setCurrentIndex(0)
            else:
                self.layout.addWidget(btn,0,0)
                self.hisgrid.setCurrentIndex(1)
        else:
            self.scrn.setText(self.scrn.text() + btn.text())
            

        
app = QApplication(sys.argv)
mainw = main()
mainw.show()
app.exec()

