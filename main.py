from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sqlite3
from crickrivals_ui import Ui_CrickRivals  # import your auto-generated UI class
from crickrivals_2 import Ui_MainWindow  # import your dashboard UI class


class DashboardWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # You can add dashboard-specific init code here

class LoginWindow(QtWidgets.QMainWindow, Ui_CrickRivals):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db_path = "app_database.db"
        self.pushButton_6.clicked.connect(self.handle_login)
        self.pushButton_5.clicked.connect(self.handle_signup)

        self.dashboard = None
    def handle_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if self.check_user_credentials(username, password):
            QtWidgets.QMessageBox.information(self, "Login Success", "Welcome back, " + username)
            self.open_dashboard()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def check_user_credentials(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None

    def handle_signup(self):
        QtWidgets.QMessageBox.information(self, "Sign Up", "Sign up not implemented yet")

    def open_dashboard(self):
        if self.dashboard is None:
            self.dashboard = DashboardWindow()
        self.dashboard.show()
        self.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
