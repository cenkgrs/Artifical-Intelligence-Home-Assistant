import RPi.GPIO as GPIO          
import time
import os
import pyttsx3
import speech_recognition as sr
import random
from picamera import PiCamera
from time import sleep

import termios
import sys, tty
import warnings
warnings.filterwarnings("ignore")

GPIO.setwarnings(False)
language = 'en'

in1 = 24
in2 = 23
en = 25
temp1=1
en2 = 22
in3 = 27
in4 = 10

TRIG = 14
ECHO = 15

# Set the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

GPIO.output(7, True)
GPIO.output(8, True)
GPIO.output(11, True)

p=GPIO.PWM(en,1000)
p2=GPIO.PWM(en2,1000)

#Starting the motors
p.start(25)
p2.start(22)

#Set motors rpm
p.ChangeDutyCycle(25)
p2.ChangeDutyCycle(25)

#Function for getting input without enter
def _getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
    return _getch()

#Lights open function
def lights_o():
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(11, True)

#Call when you gonna tell something
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        try:
            speak("Say something")
            audio = r.listen(source)
            text = r.recognize_google(audio, language = 'en-IN', show_all = True )
            speak("You said '" + r.recognize_google(audio) + "'")
        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

#Runs when ORacle speaks
def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say(text)
        engine.runAndWait()

class status:
    def __init__(self):
        self.state = True

#Calculates the distance between any object
def calculate():

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)


    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.2)

    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    

    if distance > 20:
        print ("Mesafe:",distance - 0.5,"cm")
        #speak("My front is open")
        speak("Open")
        return 1
    else:
        #print ("Engel var")
        #speak("There is an obstacle")
        speak("Closed")
        return 0

def stop():
    time.sleep(0.5)
    
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(11, True)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
    lights_o()
    
    st.status = True
        
def forward(sec):
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)

    #speak("Going forward")
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(11, True)

    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(en,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    
    time.sleep(sec)
    
    st.status = False
    
def backward(sec):
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    
    speak("Going back")
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(11, False)
    
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(en,GPIO.HIGH)
    GPIO.output(en2,GPIO.HIGH)
    
    time.sleep(sec)
    
def right():
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    
    speak("Going right")
    
    GPIO.output(7, False)
    GPIO.output(8, True)
    GPIO.output(11, False)
    
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(en,GPIO.LOW)
    GPIO.output(en2,GPIO.HIGH)

def left():
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    speak("Going left")
    

    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(11, False)
    
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(en,GPIO.HIGH)
    GPIO.output(en2,GPIO.LOW)

# Set all motors to stop first
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
speak("Welcome home sir")

st = status()

count = 0
while(1):
    #listen()
        
    result = calculate()
    if result == 1: # If front is open go forward
        forward(1)
        stop()
    else: # If front is close go back and decide where to go
        backward(1)
        stop()

        decide = random.randrange(0,2)
        print(decide)
        if decide == 0:
            left()
        elif decide == 1:
            right()

        stop()
    
    #If st.status is False then 
    if count > 1 and st.status == False:
        stop()
        speak("I am too tired sir")
        speak("Good Bye !")
        
        break
    elif count > 60 and st.status == True:
        speak("I am too tired sir")
        speak("Good Bye !")
        
        break
    
    count = count + 1
    
    '''response = _getch()
    print(response)
    #response = int(input("Where to 8 5 6 4"))
    
    if response == '8':
        forward()
    elif response == '5':
        backward()
    elif response == '6':
        right()
    elif response == '4':
        left()
    else:
        stop()
        '''