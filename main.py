from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import sqlite3
import hashlib
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer
from crickrivals_ui import Ui_CrickRivals  # Login UI
from crickrivals_2 import Ui_MainWindow    # Dashboard UI


def hash_password(password):
    """Hash the password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()



class DashboardWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""
/* Main Window */
QMainWindow {
    background-color: #e6f0ff;
}

/* Menu Bar */
QMenuBar {
    background-color: #f2f9ff;
    color: #003366;
    font: bold 14px "Segoe UI";
}

QMenuBar::item:selected {
    background-color: #b3d9ff;
}

/* Black Marquee Banner */
QLabel#label_banner {
    background-color: black;
    color: white;
    font: bold 18px "Arial";
    padding: 10px;
    border-radius: 10px;
    qproperty-alignment: AlignCenter;
}

/* Team Section Backgrounds */
QFrame {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #d6eaff, stop:1 #f2fbff);
    border: 1px solid #cce0ff;
    border-radius: 10px;
    padding: 10px;
}

/* VS Label */
QLabel#vsLabel {
    font: bold 18px "Calibri";
    color: #004080;
    qproperty-alignment: AlignCenter;
}

/* Team Logos */
QLabel[objectName^="teamLogo"] {
    border: 2px solid #99ccff;
    border-radius: 10px;
    padding: 5px;
    background-color: white;
}

/* Match Button */
QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00c6ff, stop:1 #0072ff);
    border: none;
    border-radius: 8px;
    color: white;
    font: bold 14px "Segoe UI";
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4dd2ff, stop:1 #3399ff);
}

QPushButton:pressed {
    background-color: #005c99;
}
""")

        self.setWindowTitle("CrickRivals - Dashboard")
        self.setWindowIcon(QtGui.QIcon("images/logo.png"))  # Optional: Add your app icon here


class LoginWindow(QtWidgets.QMainWindow, Ui_CrickRivals):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""
QMainWindow {
    background-color: #eaf6ff;
    font-family: 'Segoe UI', sans-serif;
    font-size: 14px;
}

/* Labels */
QLabel {
    color: #003366;
    font-weight: bold;
}

/* Input Fields */
QLineEdit {
    border: 2px solid #a0cfff;
    border-radius: 10px;
    padding: 8px 12px;
    background-color: #ffffff;
    color: #000000;
}

QLineEdit:focus {
    border: 2px solid #3399ff;
    background-color: #f0fbff;
}

/* Buttons */
QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00b7ff, stop:1 #0072ff);
    border: none;
    border-radius: 10px;
    color: white;
    font: bold 14px 'Segoe UI';
    padding: 10px 20px;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4dcfff, stop:1 #3399ff);
}

QPushButton:pressed {
    background-color: #005c99;
}
""")

        self.setWindowTitle("CrickRivals - Login")
        self.setWindowIcon(QtGui.QIcon("images/logo.png"))  # Optional

        self.db_path = "app_database.db"
        self.pushButton_6.clicked.connect(self.handle_login)
        self.pushButton_5.clicked.connect(self.handle_signup)

        self.dashboard = None

    def handle_login(self):
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text()

        if not username or not password:
            QMessageBox.warning(self, "Input Error", "Please enter both username and password.")
            return

        if self.check_user_credentials(username, password):
            QMessageBox.information(self, "Login Success", f"Welcome back, {username} 👋")
            self.open_dashboard()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def check_user_credentials(self, username, password):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, hash_password(password))
            )
            user = cursor.fetchone()
            conn.close()
            return user is not None
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Something went wrong:\n{str(e)}")
            return False

    def handle_signup(self):
        QMessageBox.information(self, "Coming Soon", "Sign up will be added in a future update!")

    def open_dashboard(self):
        self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # Optional: cleaner style
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
