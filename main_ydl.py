import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from tabs import youdwnl_tabs


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yuhook")
        self.setWindowIcon(QIcon("./images/cappuccino.png"))
        self.setGeometry(200, 200, 580, 400)

        self.table_widget = youdwnl_tabs(self)
        self.setCentralWidget(self.table_widget)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


'''
stylesheet = """
    MainWindow {
        background-image: url("./images/istockphoto-1172479732-170667a.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()

    app.exec()
