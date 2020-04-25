import smtplib
import config
import random
import speech_recognition as sr
import os
import re
import answers
import pyttsx3
from sphinx import *

# Runs when Oracle speaks
def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say(text)
        engine.runAndWait()

r = sr.Recognizer()
r.energy_threshold = 4000
source = sr.Microphone()


def listen():
    command = ""
    with sr.Microphone(sample_rate=12000) as source:
        os.system('play -nq -t alsa synth {} sine {}'.format(0.15, 500))  # 1 = duration, 440 = frequency -> this sounds a beep

        audio = r.record(source, duration=4)
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + ' \n')
    except sr.UnknownValueError:
        #speak("Did not get that sir")
        print("Google Speech Recognition could not understand audio")
        listen()
    except sr.RequestError as e:
        print("Sorry, the service is down; {0}".format(e))
        listen()
    return command

def send_mail(subject, msg, to_email):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, to_email, message)
        server.quit()

        return True
    except:
        return False


def get_mail_info():
    subject = listen()
    speak("And the message is ?")
    msg = listen()
    speak('''Can you select a contact from the list below sir ?
            1 is cenkgrs@gmail.com
            2 is joonjazzar15@gmail.com
            3 is cenk@digitaltrade.com.tr''')

    case = listen()

    to_email = config.mail_contact.get(case, "Invalid number")

    speak(random.choice(answers.complete_a))

    status = send_mail(subject, msg, to_email)

    if status:
        speak("Email sended successfully boss")
    else:
        speak("Email failed to sent")


