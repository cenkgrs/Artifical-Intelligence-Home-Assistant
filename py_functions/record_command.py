import sqlite3


def insert_command(text, command):
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO commands (text, command) VALUES (?, ?) ", (text, command))
            con.commit()

            write_command(text, command)

            return True

        except sqlite3.OperationalError:
            return False


def write_command(text, command):
    print(text, command)
    with open('./texts/commands.txt', 'a') as commands:
        commands.write(text + " - " + command + "\n")

        return True
