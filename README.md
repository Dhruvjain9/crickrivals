# 🏏CrickRivals Fantasy Cricket🏏

## Overview
CrickRivals is a simple and basic fantasy cricket application that allows users to sign up, log in, and create their own fantasy cricket team. The app focuses on a straightforward user experience, enabling users to select players from real cricket teams to build their playing XI.

## 🚀 Features
1. 👤 User Authentication

- Users can sign up to create an account.

- Users can log in with their credentials to access the app.

2. 🏏 Team Creation

- Users can select players to form their fantasy cricket team.

- The interface allows easy addition and removal of players.

3. 🪟 Basic UI

- Simple and clean interface focused on ease of use.

- Minimal design without complicated options or extra features.

4. 🗃️ Database Integration
- Uses MySQL to store:

   - User credentials

   - Selected fantasy teams

- Connected using **mysql-connector-python**.
## 🎨 Qt Designer – UI Design Tool

If you installed pyqt5-tools, the Qt Designer executable is usually located here:

      C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>\Lib\site-packages\pyqt5_tools\Qt\bin\designer.exe

>⚠️ Replace <YourUsername> and <version> with your actual username and Python version (like Python311).

### Steps to use Qt Designer:
1. Navigate to the path above.
2. Run designer.exe.
3. Design your UI using drag-and-drop.
4. Save the file as <filename>.ui.

## 🔁 Converting .ui to .py using pyuic5
Once your .ui file is ready, you need to convert it into Python code to use it in your project.

      pyuic5 -x path/to/your_file.ui -o your_output.py

Example:

      pyuic5 -x dashboard.ui -o dashboard_ui.py
      
This will generate a Python file (dashboard_ui.py) containing the entire GUI code from the .ui file, which you can then import and use like:

      from dashboard_ui import Ui_MainWindow

## 🧑‍💻 Technology Stack
- Frontend: PyQt (or specify your actual UI framework)

- Backend: Python

- Database: MySQL for storing user data and team selections

## ⚙️ Installation and Setup
1. 🧾 Clone the repository:
   
       git clone https://github.com/yourusername/crickrivals.git
       cd crickrivals

2. 📦 Install dependencies:

       pip install -r requirements.txt

- Set up the MySQL database and configure connection details in the app.

3. 🐍  Run the application:

        python main.py
4. 🛠️ Usage:

- Sign up for a new account or log in if you already have one.

- Create your fantasy cricket team by selecting players.

- Save your team and manage it through the app.

## 📁 Project Structure

    /crickrivals
    │
    ├── /images            # UI resources like images and icons
    ├── /database           # SQL schema and scripts
    ├── /src                # Source code files
    │   ├── main.py         # Main app entry point
    │   ├── crickrivals_ui.py         # Authentication logic
    │   ├── dashboard_ui.py # Team selection management
    ├── requirements.txt    # Python dependencies
    └── README.md           # Project documentation


For any questions or support, contact:

Email: dhruv5130@outlook.com
