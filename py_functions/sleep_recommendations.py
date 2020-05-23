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

            last_data = cursor.execute("SELECT * FROM sleep_records WHERE id = (SELECT MAX(id) FROM sleep_records)")
            last_data = last_data.fetchone()

            if last_data[2] is not None:
                print(last_data[2])
                return True, "updated"

            bedtime = last_data[1]
            rate = last_data[4]
            sleep_time = calculate_sleep_time(bedtime, waketime)

            status = predict(bedtime, waketime, rate, sleep_time)

            cursor.execute("UPDATE sleep_records SET waketime = (?), sleep_time = (?), status = (?) "
                           "WHERE id = (SELECT MAX(id) FROM sleep_records) "
                           , (waketime, sleep_time, status))

            return True, status

        except Exception as e:
            logger.error('Error: ' + str(e))
            return False


def calculate_sleep_time(start, end):
    start = int(start)
    end = int(end)

    end = end + 24  # If is end hour like 4, 8 it will become 32, 40
    start = start + 24 if start < 10 else start  # If start hour is not like 20 22, it will add 24 for

    sleep_time = end - start  # This is like 1 + 24 = 25 and 6 + 24 = 30 -> 30 - 24 = 6 hours sleep time

    return sleep_time
