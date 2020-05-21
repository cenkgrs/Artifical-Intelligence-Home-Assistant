import sqlite3


def insert_command(text, command, command_type):
    print(command_type)
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO commands (text, command, type) VALUES (?, ?, ?) ",
                           (text, command, command_type))
            con.commit()

            write_command(text, command, command_type)

            return True

        except sqlite3.OperationalError:
            return False


def write_command(text, command, command_type):
    print(text, command)
    with open('./texts/commands.txt', 'a') as commands:
        commands.write(text + " - " + command + " - " + str(command_type) + "\n")

        return True


def get_command_to_txt():
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        print("got here")
        db = cursor.execute("SELECT text, command FROM commands")

        data = db.fetchall()

        for x in data:
            if x[1] == "todo":
                write_command(x[0], "to do")
                continue

            write_command(x[0], x[1])

        return True



