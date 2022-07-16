import sys;
from PyQt5.QtWidgets import QApplication, QWidget;

# pip install pyqt5
# pip install PyQt5-tools

class Main(QWidget):
    def __init__(self):
        super().__init__();
        self.initUI();
    
    def initUI(self):
        self.show();

app = QApplication(sys.argv);
w = Main();
sys.exit(app.exec_());