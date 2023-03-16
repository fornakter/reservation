import sqlite3

connect = sqlite3.connect("reservation.db")
cursor = connect.cursor()

data = [
    ("Asia", "Placek", "2021-12--25"),
    ("Tata", "Pierdoła", "2022-10-20")
    ]

# Add tables
# cursor.execute("CREATE TABLE reservation(name text, subname text, day date)")
cursor.executemany("INSERT INTO reservation (name, subname, day) VALUES (?,?,?)", data)

for row in cursor.execute("select * from reservation"):
    print(row)

# Save data
connect.commit()
connect.close()
