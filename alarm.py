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
    conn = sqlite3.connect('/home/cenk/Masaüstü/Oracle/Oracle')
    cursor = conn.cursor()

    speak("Hour is sir ?")

    with sr.Microphone() as source:
        os.system('play -nq -t alsa synth {} sine {}'.format(0.15, 500))  # 1 = duration, 440 = frequency -> this sounds a beep
        audio = r.listen(source)
        try:
            hour = r.recognize_google(audio)

            speak("And minute is ?")
            os.system('play -nq -t alsa synth {} sine {}'.format(0.15, 500))  # 1 = duration, 440 = frequency -> this sounds a beep
            audio = r.listen(source)
            minute = r.recognize_google(audio)

            speak(f"You asked me to set an alarm for {int(hour)} {int(minute)} sir")
            cursor.execute("INSERT INTO Alarms (hour, minute) VALUES (?, ?)", (hour, minute))
            conn.commit()

        except ValueError or sr.UnknownValueError or speech_recognition.UnknownValueError or sr.UnknownValueError():
            speak("There was an error sir, i am gonna ask you to repeat it")
            alarm()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            alarm()

    conn.close()
def check_alarm():
    cn = sqlite3.connect('/home/cenk/Masaüstü/Oracle/Oracle')
    cs = cn.cursor()
    check_hour = datetime.datetime.now().hour
    check_min = datetime.datetime.now().minute

    try:
        db = cs.execute(f'SELECT * FROM Alarms ORDER BY hour ASC')
        last = db.fetchmany()
        print(last)


        if check_hour == last[0][1] and check_min == last[0][2]:
            mixer.init()
            mixer.music.load('/home/cenk/Masaüstü/Oracle/ringtone/alarm.mp3')
            mixer.music.play()
            speak("You did set an alarm for this hour sir")

            cs.execute(f"DELETE FROM Alarms WHERE hour = ? and minute = ?", (check_hour, check_min))
            cn.commit()

    except IndexError:
        return False

    cn.close()



