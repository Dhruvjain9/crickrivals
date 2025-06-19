from saveDashboard import Ui_saveDashboard
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

class SaveDashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_saveDashboard()
        self.ui.setStyleSheet("""/* Background */
QWidget {
    background-color: #f4fbff;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
}

/* Combo Boxes (Captain/Vice-Captain) */
QComboBox {
    background-color: #ffffff;
    border: 2px solid #99ccff;
    border-radius: 6px;
    padding: 4px 8px;
    font-weight: bold;
    color: #003366;
}

QComboBox::drop-down {
    border-left: 1px solid #99ccff;
    background-color: #e6f2ff;
}

QComboBox::item:hover {
    background-color: #d0ecff;
}

/* Labels */
QLabel {
    color: #003366;
    font-weight: bold;
    font-size: 14px;
}

/* Input Fields (if any) */
QLineEdit {
    background-color: #ffffff;
    border: 2px solid #99ccff;
    border-radius: 6px;
    padding: 6px;
    color: #003366;
}

/* Save Buttons */
QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                      stop:0 #00c6ff, stop:1 #0072ff);
    color: white;
    font-weight: bold;
    padding: 8px 20px;
    border-radius: 8px;
    border: none;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                      stop:0 #33d6ff, stop:1 #3399ff);
}

QPushButton:pressed {
    background-color: #005c99;
}

/* Group Boxes or Frames */
QGroupBox {
    border: 2px solid #99ccff;
    border-radius: 10px;
    margin-top: 10px;
    padding: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px 0 5px;
    color: #004080;
    font-size: 15px;
}

/* Optional: Scroll Area or List Style */
QScrollArea {
    background-color: #ffffff;
    border: none;
}
""")
        self.ui.setupUi(self)
