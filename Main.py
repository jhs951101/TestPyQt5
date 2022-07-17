import sys
import subprocess

try:
    from PyQt5.uic import loadUi
    from PyQt5 import uic, QtWidgets
    from PyQt5.QtWidgets import QDialog, QApplication

except:
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip']);

    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pyqt5']);
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'PyQt5-tools']);

    from PyQt5.uic import loadUi
    from PyQt5 import uic, QtWidgets
    from PyQt5.QtWidgets import QDialog, QApplication


class FirstController(QDialog):
    def __init__(self):
        super(FirstController, self).__init__();
        loadUi("View/firstView.ui", self);
        self.btnGoToSecond.clicked.connect(self.btn_clicked);
        
    def btn_clicked(self):
        secondView = SecondController();
        widget.addWidget(secondView);
        widget.setCurrentIndex(widget.currentIndex()+1);


class SecondController(QDialog):
    def __init__(self):
        super(SecondController, self).__init__();
        loadUi("View/secondView.ui", self);
        self.btnGoToFirst.clicked.connect(self.btn_clicked);

    def btn_clicked(self):
        widget.removeWidget(self);
        widget.setCurrentIndex(widget.currentIndex()-1);


if __name__ == "__main__":
    app = QApplication(sys.argv);
    widget = QtWidgets.QStackedWidget();

    firstView = FirstController();
    widget.addWidget(firstView);
    widget.setFixedWidth(400);
    widget.setFixedHeight(400);
    widget.show();

    try:
        sys.exit(app.exec_());
    except:
        print("");