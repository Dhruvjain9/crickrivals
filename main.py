from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import sqlite3
import hashlib
from crickrivals_ui import Ui_CrickRivals  # Login UI
from crickrivals_2 import Ui_MainWindow    # Dashboard UI


def hash_password(password):
    """Hash the password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()



class DashboardWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, username):
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.setStyleSheet("""
/* 🌟 Main Window */
QMainWindow {
    background-color: #f8fbff;
    font-family: "Segoe UI", sans-serif;
    font-size: 14px;
}

/* 🔝 Menu Bar */
QMenuBar {
    background-color: #ffffff;
    color: #1a1a1a;
    padding: 6px;
    font-weight: bold;
    border-bottom: 1px solid #d0e3ff;
}

QMenuBar::item:selected {
    background-color: #cce6ff;
    color: #004080;
}

/* 🏁 Marquee / Banner */
QLabel#label_banner {
    background-color: #004080;
    color: #ffffff;
    font-size: 20px;
    font-weight: bold;
    padding: 12px;
    border-radius: 12px;
    qproperty-alignment: AlignCenter;
}

/* 🧊 Card-style Frames */
QFrame {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #ebf5ff, stop:1 #ffffff);
    border: 1px solid #cfdff7;
    border-radius: 12px;
    padding: 10px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
}

/* ⚔️ VS Label */
QLabel#vsLabel {
    font: bold 20px "Segoe UI";
    color: #003366;
    qproperty-alignment: AlignCenter;
}

/* 🏏 Team Logos */
QLabel[objectName^="teamLogo"] {
    background-color: #ffffff;
    border: 2px solid #aad4ff;
    border-radius: 12px;
    padding: 6px;
    margin: 4px;
}

/* 🎯 Push Buttons */
QPushButton {
    background-color: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #42a5f5, stop:1 #1e88e5
    );
    color: #ffffff;
    font-weight: bold;
    font-size: 14px;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
}

QPushButton:hover {
    background-color: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #64b5f6, stop:1 #2196f3
    );
}

QPushButton:pressed {
    background-color: #1565c0;
}

/* ✅ Combo Boxes */
QComboBox {
    background-color: #ffffff;
    border: 1px solid #b3d9ff;
    padding: 5px 10px;
    border-radius: 8px;
    font-weight: bold;
    color: #003366;
}

QComboBox:hover {
    background-color: #e0f2ff; /* Light blue on hover */
    border: 1px solid #66bfff;
}
/* 📝 Labels (Default) */
QLabel {
    color: #333333;
    font-size: 14px;
}
QLabel#label_title {
    font: bold 24px "Segoe UI";
    color: #003366;
    qproperty-alignment: AlignCenter;
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
        self.lineEdit_2.returnPressed.connect(self.handle_login)
        self.lineEdit.returnPressed.connect(self.handle_login)
        self.pushButton_6.clicked.connect(self.handle_login)
        self.pushButton_5.clicked.connect(self.handle_signup)

        self.dashboard = None
        self.username = None
        self.password = None
    def handle_login(self):
        self.username = self.lineEdit.text().strip()
        self.password = self.lineEdit_2.text()

        if not self.username or not self.password:
            QMessageBox.warning(self, "Input Error", "Please enter both username and password.")
            return

        if self.check_user_credentials(self.username, self.password):
            QMessageBox.information(self, "Login Success", f"Welcome back, {self.username} 👋")
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
        self.dashboard = DashboardWindow(self.username)
        self.dashboard.show()
        self.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # Optional: cleaner style
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
