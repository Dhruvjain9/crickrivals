import sqlite3

def reset_real_time_match_table():
    conn = sqlite3.connect("app_database.db")  # ✅ Use your DB file name/path
    cursor = conn.cursor()

    # 🔨 Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS real_time_match (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team1 TEXT NOT NULL,
            team2 TEXT NOT NULL
        )
    """)

    # 🚮 Delete all old data
    cursor.execute("DELETE FROM real_time_match")

    # ♻️ Insert new fresh data
    new_matches = [
        ("Punjab Kings (PBKS)", "Royal Challengers Bengaluru (RCB)"),
        ("Chennai Super Kings (CSK)", "Mumbai Indians (MI)")
    ]
    cursor.executemany("INSERT INTO real_time_match (team1, team2) VALUES (?, ?)", new_matches)

    conn.commit()
    conn.close()
    print("✅ Table reset with fresh match data.")

# 🟢 Run it once
reset_real_time_match_table()
