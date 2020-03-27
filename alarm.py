import random

import speech_recognition
from pygame import mixer
import sqlite3
import speech_recognition as sr
import os
import pyttsx3
import pyaudio
import warnings
warnings.filterwarnings("ignore")
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

conn = sqlite3.connect('/home/cenk/Masaüstü/Oracle/Oracle')
cursor = conn.cursor()

print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
# Runs when Oracle speaks
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('voice', 'english-north')
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # Recognizer object

def alarm():


    speak("Hour is sir ?")

    with sr.Microphone() as source:
        os.system('play -nq -t alsa synth {} sine {}'.format(0.15, 500))  # 1 = duration, 440 = frequency -> this sounds a beep
        audio = r.listen(source)
        try:
            hour = int(r.recognize_google(audio))

            speak("And minute is ?")
            os.system('play -nq -t alsa synth {} sine {}'.format(0.15, 500))  # 1 = duration, 440 = frequency -> this sounds a beep
            audio = r.listen(source)
            minute = int(r.recognize_google(audio))

            print(hour, minute)
            speak(f"You asked me to set an alarm for {hour} {minute} sir")
            cursor.execute(f"INSERT INTO Alarms (hour,minute) VALUES (?, ?)", (hour, minute))
            conn.close()
        except ValueError or sr.UnknownValueError or speech_recognition.UnknownValueError or sr.UnknownValueError():
            speak("There was an error sir, i am gonna ask you to repeat it")
            alarm()


def check_alarm():
    cn = sqlite3.connect('/home/cenk/Masaüstü/Oracle/Oracle')
    cs = cn.cursor()
    check_hour = datetime.datetime.now().hour
    check_min = datetime.datetime.now().minute

    db = cs.execute(f'SELECT * FROM Alarms ORDER BY hour ASC')
    last = db.fetchmany()
    print(last)

    if check_hour == last[0][1] and check_min == last[0][2]:
        mixer.init()
        mixer.music.load('/home/cenk/Masaüstü/Oracle/ringtone/alarm.mp3')
        mixer.music.play()
        speak("You did set an alarm for this hour sir")

        cs.execute(f"DELETE FROM Alarms WHERE hour = ? and minute = ?", (check_hour, check_min))

    cn.close()
alarm()
scheduler = BlockingScheduler()
scheduler.add_job(check_alarm, 'interval', hours=0.001)
scheduler.start()

#check_alarm()

