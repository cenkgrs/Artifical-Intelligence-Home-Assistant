import sqlite3
import logging
from sleep_habits import predict

logger = logging.Logger('catch_all')


def insert_bedtime(bedtime, waketime, date, rate):

    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO sleep_records (bedtime, waketime, date, rate) VALUES (?, ?, ?, ?) ",
                           (bedtime, waketime, date, rate))
            con.commit()

            return True

        except Exception as e:
            logger.error('Failed to upload to ftp: ' + str(e))
            return False


def update_bedtime(waketime):
    with sqlite3.connect("Oracle") as con:
        cursor = con.cursor()
        try:
            cursor.execute("UPDATE sleep_records SET waketime = (?) WHERE id = (SELECT MAX(id) FROM sleep_records) "
                           , (waketime,))

            last_data = cursor.execute("SELECT * FROM sleep_records WHERE id = (SELECT MAX(id) FROM sleep_records)")
            last_data = last_data.fetchone()

            print(last_data)
            bedtime = last_data[1]
            wake = last_data[2]
            rate = last_data[3]

            calculate_sleep_time(bedtime, wake)

            predict(bedtime, wake, rate, )

            return True

        except Exception as e:
            logger.error('Failed to upload to ftp: ' + str(e))
            return False


def calculate_sleep_time(start, end):
    print(start)
    print(end)

update_bedtime("06")
#insert_bedtime("00", "07", "20.05.2020", 80)