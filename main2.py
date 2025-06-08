from saveDashboard import Ui_saveDashboard
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

class SaveDashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_saveDashboard()
        self.ui.setupUi(self)