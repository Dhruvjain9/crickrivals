# CrickRivals Fantasy Cricket App

### Overview
CrickRivals is a simple and basic fantasy cricket application that allows users to sign up, log in, and create their own fantasy cricket team. The app focuses on a straightforward user experience, enabling users to select players from real cricket teams to build their playing XI.

### Features
1. User Authentication

- Users can sign up to create an account.

- Users can log in with their credentials to access the app.

2. Team Creation

- Users can select players to form their fantasy cricket team.

- The interface allows easy addition and removal of players.

3. Basic UI

- Simple and clean interface focused on ease of use.

- Minimal design without complicated options or extra features.

### Technology Stack
- Frontend: PyQt (or specify your actual UI framework)

- Backend: Python

- Database: MySQL for storing user data and team selections

### Installation and Setup
1. Clone the repository:
   
       git clone https://github.com/yourusername/crickrivals.git
       cd crickrivals

2. Install dependencies:

       pip install -r requirements.txt

- Set up the MySQL database and configure connection details in the app.

3. Run the application:

        python main.py
4. Usage:

- Sign up for a new account or log in if you already have one.

- Create your fantasy cricket team by selecting players.

- Save your team and manage it through the app.

Project Structure

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

Contact
For any questions or support, contact:
Email: dhruv5130@outlook.com
