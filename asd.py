import random
import sqlite3

def act():
    return 0, 15

conn = sqlite3.connect('/home/cenk/Masaüstü/Oracle/Oracle')
cursor = conn.cursor()
result, distance = act()

choices = ["left", "right"]
decide = random.choice(choices)
cursor.execute("INSERT INTO Actions (action) VALUES ('forward')")

db = cursor.execute('SELECT action FROM Actions ORDER BY id DESC')
last_act = db.fetchmany()
print(last_act)