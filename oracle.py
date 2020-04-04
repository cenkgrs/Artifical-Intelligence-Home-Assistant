from alarm import alarm, check_alarm
from currency import get_currency
from youtube import get_video

import RPi.GPIO as GPIO
import time
import pyttsx3
import random
# from apscheduler.schedulers.blocking import BlockingScheduler

import sqlite3
import termios
import sys, tty
import warnings
warnings.filterwarnings("ignore")


GPIO.setwarnings(False)
language = 'en'

in1 = 24
in2 = 23
en = 25
temp1 = 1
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
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

GPIO.output(7, True)
GPIO.output(8, True)
GPIO.output(11, True)

p = GPIO.PWM(en, 1000)
p2 = GPIO.PWM(en2, 1000)

# Starting the motors
p.start(25)
p2.start(22)

# Set motors rpm
p.ChangeDutyCycle(25)
p2.ChangeDutyCycle(25)

# Set database connection
conn = sqlite3.connect('/home/pi/Oracle/Oracle')
cursor = conn.cursor()


# Function for getting input without enter
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

# Lights open function
def lights_o():
    GPIO.output(7, True)
    GPIO.output(8, True)
    GPIO.output(11, True)


# Runs when Oracle speaks
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
    #Sends a signal and wait for it to return and calculate the distance by difference

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
        print("Open")
        return 1, distance
    else:
        #speak("There is an obstacle")
        print("Closed")
        return 0, distance

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

    print("Going forward")
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
    
    print("Going back")
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
    
    print("Going right")
    
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
    print("Going left")
    

    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(11, False)
    
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(en,GPIO.HIGH)
    GPIO.output(en2,GPIO.LOW)

def pick_route(type, last_act):
    if type == 0: # Means it can't go forward and last action was forward
        choices = ["left", "right"]
        decide = random.choice(choices)
        # Record last two actions
        cursor.execute("INSERT INTO Actions (action) VALUES ('forward')")
        cursor.execute("INSERT INTO Actions (action, result) VALUES (?, ?) ", (decide, distance))
    elif type == 1: # Means it can go all the three ways and last action was backward
        choices = ["forward", "left", "right"]
        choices.remove(last_act[0][0]) # Remove last action (except backward) from array so it cant become a loop
        decide = random.choice(choices)

        cursor.execute("INSERT INTO Actions (action, result) VALUES (?, ?) ", (decide, distance))

    conn.commit()
    print(decide)

    # Run the function that came from decision
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(decide)
    
    if decide == "forward":
        method(1)
    else :
        method()


# Set all motors to stop first
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

time.sleep(2)

#speak("Welcome home sir")

# scheduler = BlockingScheduler()
# scheduler.add_job(check_alarm, 'interval', hours=0.5)
# scheduler.start()

st = status()

count = 0
while(count < 50):
    db = cursor.execute('SELECT action FROM Actions ORDER BY id DESC')
    last_act = db.fetchmany()

    # Result means the success of last action (if it hit the wall or not 0, 1)
    # distance means result of last action (15 cm)
    result, distance = calculate()
    if result == 1: # If front is open go forward
        forward(0.6)

        stop()
        pick_route(1, last_act)
    else: # If front is close go back and decide where to go
        backward(0.4)
        stop()
        pick_route(0, last_act)

        stop()

    # Update the last action result and success
    cursor.execute("UPDATE Actions SET result = ?, success = ? WHERE id = (SELECT MAX(id) FROM Actions) "
                   , (distance, result))
    conn.commit()
    count = count + 1

# If st.status is False then
# This piece of code checks if Oracle is already stopped or not
if st.status == False:
    stop()
    speak("I am too tired sir")
    speak("Good Bye !")

elif st.status == True:
    speak("I am too tired sir")
    speak("Good Bye !")

    # Code for manually controlling Oracle with numpads - i will add dualshock control
    '''
    response = _getch()
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