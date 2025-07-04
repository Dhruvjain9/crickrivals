# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'saveDashboard.ui'
# Created by: PyQt5 UI code generator 5.15.6
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_saveDashboard(object):
    def __init__(self, team_name, team1, team2, players_list, team1_code, team2_code, username):
        self.team1_code = team1_code
        self.team2_code = team2_code
        self.team_name = team_name
        self.team1 = team1
        self.team2 = team2
        self.players_list = players_list
        self.captain = None
        self.vice_captain = None
        self.selected_player_item = None
        self.username = username  # Store username for DB operations

    def setupUi(self, saveDashboard):
        saveDashboard.setObjectName("saveDashboard")
        saveDashboard.resize(1741, 936)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        saveDashboard.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(saveDashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 1701, 851))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(350, 400))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.itemClicked.connect(self.store_selected_item)  # Just store clicked player
        self.listWidget.setItemAlignment(QtCore.Qt.AlignRight)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/save--v1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(500, 200))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(f"images/{self.team1_code}.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(300, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(300, 35))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(500, 200))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(f"images/{self.team2_code}.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)
        saveDashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(saveDashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1741, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        saveDashboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(saveDashboard)
        self.statusbar.setObjectName("statusbar")
        saveDashboard.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(saveDashboard)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/new-team.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Team.setIcon(icon1)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionManage_Team = QtWidgets.QAction(saveDashboard)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/manage-team.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManage_Team.setIcon(icon2)
        self.actionManage_Team.setObjectName("actionManage_Team")
        self.actionInstructions = QtWidgets.QAction(saveDashboard)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/instructions.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInstructions.setIcon(icon3)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionManual = QtWidgets.QAction(saveDashboard)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManual.setIcon(icon4)
        self.actionManual.setObjectName("actionManual")
        self.actionSave_Team = QtWidgets.QAction(saveDashboard)
        self.actionSave_Team.setIcon(icon)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.menuFile.addAction(self.actionNew_Team)
        self.menuFile.addAction(self.actionManage_Team)
        self.menuFile.addAction(self.actionSave_Team)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.populate_players()
        # Connect buttons to their respective functions
        self.listWidget.setSortingEnabled(True)
        self.pushButton_4.clicked.connect(self.save_team)
        self.pushButton.clicked.connect(self.set_captain)
        self.pushButton_2.clicked.connect(self.set_vice_captain)
          # Populate the list with players

        self.retranslateUi(saveDashboard)
        QtCore.QMetaObject.connectSlotsByName(saveDashboard)

    def retranslateUi(self, saveDashboard):
        _translate = QtCore.QCoreApplication.translate
        saveDashboard.setWindowTitle(_translate("saveDashboard", "Save Team"))
        self.label_11.setText(_translate("saveDashboard", "Vice Captain (VC) :"))
        self.label_4.setText(_translate("saveDashboard", "Playing XI"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("saveDashboard", "VS"))
        self.label_2.setText(_translate("saveDashboard", "Team Name: "))
        self.pushButton_4.setText(_translate("saveDashboard", "Save Team"))
        self.pushButton_4.setShortcut(_translate("saveDashboard", "Ctrl+S"))
        self.label_3.setText(_translate("saveDashboard", f"{self.team_name}"))
        self.label_10.setText(_translate("saveDashboard", "<Player Name>"))
        self.label_8.setText(_translate("saveDashboard", "Captain (C) :"))
        self.label_12.setText(_translate("saveDashboard", "<Player Name>"))
        self.label_7.setText(_translate("saveDashboard", f"{self.team2}"))
        self.label.setText(_translate("saveDashboard", f"{self.team1}"))
        self.pushButton.setText(_translate("saveDashboard", "Captain (C)"))
        self.pushButton_2.setText(_translate("saveDashboard", "Vice Captain (VC)"))
        self.menuFile.setTitle(_translate("saveDashboard", "File"))
        self.menuHelp.setTitle(_translate("saveDashboard", "Help"))
        self.actionNew_Team.setText(_translate("saveDashboard", "New Team"))
        self.actionManage_Team.setText(_translate("saveDashboard", "Manage Team"))
        self.actionInstructions.setText(_translate("saveDashboard", "Instructions"))
        self.actionManual.setText(_translate("saveDashboard", "Manual"))
        self.actionSave_Team.setText(_translate("saveDashboard", "Save Team"))
    
    def store_selected_item(self, item):
        self.selected_player_item = item  # Store the selected QListWidgetItem

    def populate_players(self):
        print("Populating players...")  # Debug print
        self.listWidget.clear()
        self.selected_player_item = None  # Reset selection

        for player_str in self.players_list:
            print("Adding:", player_str)  # Debug each player
            item = QtWidgets.QListWidgetItem(player_str)
            self.listWidget.addItem(item)

    def save_team(self):
        if not hasattr(self, 'captain') or not hasattr(self, 'vice_captain'):
            QtWidgets.QMessageBox.warning(self, "Incomplete Selection", "Please select both Captain and Vice Captain.")
            return

        if not self.captain or not self.vice_captain:
            QtWidgets.QMessageBox.warning(self, "Incomplete Selection", "Please select both Captain and Vice Captain.")
            return

        # Implement your actual saving logic here
        QtWidgets.QMessageBox.information(self, "Success", "Team saved successfully!")

    def set_captain(self):
        if not hasattr(self, 'selected_player_item') or not self.selected_player_item:
            QtWidgets.QMessageBox.warning(self, "No Selection", "Please select a player to make Captain.")
            return
        
        selected = self.selected_player_item.text()
        
        if hasattr(self, 'vice_captain') and selected == self.vice_captain:
            QtWidgets.QMessageBox.warning(self, "Invalid", "Player already selected as Vice Captain.")
            return

        self.captain = selected
        self.label_10.setText(f"{self.captain}")

    def set_vice_captain(self):
        if not hasattr(self, 'selected_player_item') or not self.selected_player_item:
            QtWidgets.QMessageBox.warning(self, "No Selection", "Please select a player to make Vice Captain.")
            return

        selected = self.selected_player_item.text()

        if hasattr(self, 'captain') and selected == self.captain:
            QtWidgets.QMessageBox.warning(self, "Invalid", "Player already selected as Captain.")
            return

        self.vice_captain = selected
        self.label_12.setText(f"{self.vice_captain}")


    def save_team(self):
        if not hasattr(self, 'captain') or not hasattr(self, 'vice_captain'):
            QtWidgets.QMessageBox.warning(None, "Incomplete Selection", "Please select both Captain and Vice Captain.")
            return

        if not self.captain or not self.vice_captain:
            QtWidgets.QMessageBox.warning(None, "Incomplete Selection", "Please select both Captain and Vice Captain.")
            return

        try:
            username = self.username  # Using this as table name
            team_name = self.team_name  # Also storing it in the table

            # Extract all player codes from list
            players = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
            player_codes = [p.split(" - ")[0] if " - " in p else p for p in players]

            # Clean captain & vice-captain codes
            captain_code = self.captain.split(" - ")[0] if " - " in self.captain else self.captain
            vice_captain_code = self.vice_captain.split(" - ")[0] if " - " in self.vice_captain else self.vice_captain

            # Connect DB
            conn = sqlite3.connect("team_data.db")
            cursor = conn.cursor()

            # Create user table with team_name column now included
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS "{username}" (
                    sno INTEGER PRIMARY KEY AUTOINCREMENT,
                    team_name TEXT,
                    team1 TEXT,
                    team2 TEXT,
                    players TEXT,
                    vice_captain TEXT,
                    captain TEXT
                )
            ''')

            # Insert row
            cursor.execute(f'''
                INSERT INTO "{username}" (team_name, team1, team2, players, vice_captain, captain)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (team_name, self.team1_code, self.team2_code, ",".join(player_codes), vice_captain_code, captain_code))

            conn.commit()
            conn.close()

            QtWidgets.QMessageBox.information(None, "Success", "Team saved successfully!")

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to save team:\n{str(e)}")

