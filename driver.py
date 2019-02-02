import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from detect_blinks import main
from threading import Thread, Event

class StoppableThread(Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = Event()

    def run(self):
        main()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
 
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Blink Of an Eye'
        self.left = 100
        self.top = 100
        self.width = 480
        self.height = 270
        self.threadCheck = False
        self.th = StoppableThread()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        startButton = QPushButton('Start', self)
        stopButton = QPushButton('Stop', self)
        csvButton = QPushButton('Generate Report in CSV', self)
        excelButton = QPushButton('Generate Report in Excel', self)
        startButton.setToolTip('Start Eye Blink Tracking')
        stopButton.setToolTip('Stop the Service')
        csvButton.setToolTip('Generate Report as a CSV file')
        csvButton.adjustSize()
        excelButton.setToolTip('Generate Report as an Excel file')
        excelButton.adjustSize()
        startButton.move(100, 70)
        stopButton.move(100, 150)
        csvButton.move(270, 70)
        excelButton.move(270, 150)

        self.statusBar().showMessage('Ready...')
        startButton.clicked.connect(self.start_service)
        stopButton.clicked.connect(self.stop_service)
        self.show()

    @pyqtSlot()
    def start_service(self):
        self.statusBar().showMessage('Starting service...')
        try:
            self.th.start()
        except:
            raise Exception()
        self.threadCheck = True
        if self.threadCheck == True:
            self.statusBar().showMessage('Running...')
        

    @pyqtSlot()
    def stop_service(self):
        self.statusBar().showMessage('Stopping service...')
        try:
            if self.th.isAlive():
                self.th.stop()
        except:
            raise Exception()
        self.threadCheck = False
        self.statusBar().showMessage('Stopped')

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())