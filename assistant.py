from alarm import alarm, check_alarm
from currency import get_currency
from youtube import get_video
from search import search

import os
import pyttsx3
import speech_recognition as sr
import random

# Speak Lists

r = sr.Recognizer()  # Recognizer object
source = sr.Microphone()  # Microphone object

welcoming_q = ["hello", "hi", "hey", "hello Oracle", "hi Oracle", "hey Oracle", "Oracle are you there", "are you there Oracle"]
welcoming_q = welcoming_q + ["hello oracle", "hi oracle", "hey oracle", "oracle are you there", "are you there oracle"]
welcoming_a = ["at your service sir","hi sir", "hello sir", "hey there sir"]

thanks_q = ["thank you Oracle", "thanks Oracle", "well done Oracle", "thank you"]
thanks_a = ["you're welcome sir"]

goodness_q = ["how are you", "are you okay", "how are you oracle"]
goodness_a = ["i am okay sir, what about you", "i am very good, thank you"]

who_q = ["who are you", "who are you ma'm", "tell me your name"]
who_a = ["i am oracle", "my name is oracle", "i am an artifical intelligence"]

search_q = ["I want to search", "i want to search", "i want to search something", "I want to search something", "I want to search something", "search", "want to search"]
search_a = ["ok sir,what do you wanna search", "what do you wanna search sir", "what is it you wanna search sir"]

video_q = ["open YouTube", "open the YouTube", "let's watch something", "i want to watch something", "let's watch video", "open some video oracle"]
video_a = ["what do you want to watch sir", "watch what sir", "what is it you wanna search sir", "what do you wanna watch sir", "sure, what do you want to watch"]

complete_a = ["You got it sir", "Will do sir", "Right away sir"]

quit_q = ["shut down oracle", "shutdown oracle",  "shut down", "power off", "close oracle", "power off oracle"]
quit_q = quit_q + ["shut down Oracle", "shutdown Oracle", "close Oracle", "power off Oracle"]
quit_a = ["okay sir see you tomorrow", "bye sir", "see you sir"]

alarm_q = ["i wanna set an alarm", "set an alarm", "setup an alarm", "i want you to set an alarm"]
alarm_a = ["okay sir lets set an alarm"]

currency_q = ["currency", "give me the value of turkish lira", "what is the value of turkish lira", "value of turkish lira"]
currency_a = ["just a second boss", "i am looking it down", "just give me a moment"]


# Checking the what user said what it represents
def check_command(audio):
    global source
    if audio.lower() in welcoming_q:
        speak(random.choice(welcoming_a))
    elif audio in thanks_q:  # Raise if say thanks
        speak(random.choice(thanks_a))
    elif audio in who_q: # Raise when identity ask
        speak(random.choice(who_a))
    elif audio in goodness_q:
        speak(random.choice(goodness_a))
    elif audio.lower() in quit_q:  # Raise when i want to close the program
        speak(random.choice(quit_a))
        raise SystemExit(0)
    elif audio.lower() in search_q:  # Raise when i want to search something
        speak(random.choice(search_a))

        search()


    elif audio in video_q:
        speak(random.choice(video_a))

        get_video()

    elif audio in alarm_q:
        speak(random.choice(alarm_a))
        alarm(sr.Microphone())

    elif audio in currency_q:
        speak(random.choice(currency_a))
        get_currency()


# Call when you gonna tell something
def listen():
    with sr.Microphone() as source:

        try:
            os.system('play -nq -t alsa synth {} sine {}'.format(0.15,
                                                                 500))  # 1 = duration, 440 = frequency -> this sounds a beep
            audio = r.listen(source)
            check_command(r.recognize_google(audio))
            print(r.recognize_google(audio))

        except sr.UnknownValueError:
            speak("Did not get that sir")
            print("Google Speech Recognition could not understand audio")
            listen()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Runs when Oracle speaks
def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say(text)
        engine.runAndWait()

speak("Welcome sir")
while True:
    listen()