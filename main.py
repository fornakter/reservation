import sqlite3
import sys
import subprocess


class ResSys:
    def __init__(self):
        print('''
        1. Make a reservation
        2. Cancel a reservation
        3. Print schedule
        4. Save schedule to a file
        5. Readme
        6. Exit
        ''')
        chose = input('I chose: ')
        match chose:
            case '1':
                self.make_reserv()
            case '2':
                self.cancel_reserv()
            case '3':
                self.print()
            case '4':
                self.Save()
            case '5':
                self.read_me()
            case '6':
                print("Bye!")
                sys.exit()
            case _:
                print('I dont know what is this')
                ResSys()

    def make_reserv(self):
        data = []
        connect = sqlite3.connect("reservation.db")
        cursor = connect.cursor()
        data[0] = input("Podaj imie: ")
        data = ["Asia", "Placek", "2021-12-25"]
        try:
            # Add tables
            cursor.execute("CREATE TABLE reservation(name text, surname text, day date)")
        except:
            pass

        cursor.execute("INSERT INTO reservation (name, surname, day) VALUES (?,?,?)", data)

        for row in cursor.execute("select * from reservation"):
            print(row)

        # Save data
        connect.commit()
        connect.close()

    def cancel_reserv(self):
        print('Dokonaj rezerwacji')

    def print(self):
        print('Dokonaj rezerwacji')

    def Save(self):
        print('Dokonaj rezerwacji')

    def read_me(self):
        try:
            subprocess.Popen(["notepad", "README.md"])
        except:
            subprocess.Popen(["xed", "README.md"])
        ResSys()


if __name__ == '__main__':
    ResSys()
