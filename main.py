import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import mysql.connector
from crickrivals_ui import Ui_CrickRivals
from dashboard_ui import Ui_Dashboard

class DashboardWindow(QMainWindow):
    def __init__(self, username=None):
        super().__init__()
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)
        self.ui.set_main_window(self)  # 👈 Set self as main window
        self.ui.logged_in_username = username  # 👈 Set the logged-in username
        

class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CrickRivals()
        self.ui.setupUi(self)

        self.ui.pushButton_6.clicked.connect(self.handle_login)
        self.ui.pushButton_5.clicked.connect(self.handle_signup)  # optional

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if not username or not password:
            self.show_message("Please enter both username and password.")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="TIGER",  # change if needed
                database="ipl_fantasy"
            )
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                #self.show_message("✅ Login successful!", success=True)
                self.open_dashboard(username)
            else:
                self.show_message("❌ Invalid username or password.")

            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            self.show_message(f"Database error: {err}")

    def open_dashboard(self,username):
        self.dashboard = DashboardWindow(username)
        self.dashboard.show()
        self.close()  # close login window

    def handle_signup(self):
        self.show_message("Signup page coming soon 😉")

    def show_message(self, message, success=False):
        msg = QMessageBox()
        msg.setText(message)
        if success:
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setIcon(QMessageBox.Warning)
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
