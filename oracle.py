from alarm import alarm, check_alarm
from currency import get_currency
from youtube import get_video
from motors import right, left, backward, forward, stop
from web import start_interface
import multiprocessing
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

temp1 = 1

#  Distance sensor
TRIG = 14
ECHO = 15

servo = 36

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

# Set the GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(servo,GPIO.OUT)

GPIO.setup(7, GPIO.OUT) # Left light
GPIO.setup(8, GPIO.OUT)  # Right light
GPIO.setup(11, GPIO.OUT)  # Forward light

GPIO.output(7, True)
GPIO.output(8, True)
GPIO.output(11, True)

en = 25  # Engine 1
en2 = 22  # Engine 2
p = GPIO.PWM(en, 1000)
p2 = GPIO.PWM(en2, 1000)


# Starting servos
p3 = GPIO.PWM(servo,50) 

# Set servo duty cylcle
p3.start(2.5)

# Set database connection
conn = sqlite3.connect('/home/pi/Oracle/Oracle')
cursor = conn.cursor()

class Status:
    def __init__(self):
        self.state = True

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
def lights_o(type):
    if type == "stop":
        GPIO.output(7, True)
        GPIO.output(8, True)
        GPIO.output(11, True)
    elif type == "right":
        GPIO.output(7, False)
        GPIO.output(8, True)
        GPIO.output(11, False)
    elif type == "left":
        GPIO.output(7, True)
        GPIO.output(8, False)
        GPIO.output(11, False)
    elif type == "forward":
        GPIO.output(7, False)
        GPIO.output(8, False)
        GPIO.output(11, True)
    else:
        GPIO.output(7, False)
        GPIO.output(8, False)
        GPIO.output(11, False)

# Runs when Oracle speaks
def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english+f3')
        engine.say(text)
        engine.runAndWait()


# Calculates the distance between any object
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


def pick_route(type, last_act, distance):
    remaining_choices = []
    if type == 0: # Means it can't go forward and last action was forward
        choices = ["left", "right"]
        decide = random.choice(choices)
        result = rotate_servo(decide) # Check if the decided direction is empty

        if not result: # If decided direction is not empty choose any other valid direction
            decide = random.choice((remaining_choices.append(choices)).remove(decide))

        # Record last two actions
        cursor.execute("INSERT INTO Actions (action) VALUES ('forward')")
        cursor.execute("INSERT INTO Actions (action, result) VALUES (?, ?) ", (decide, distance))

    elif type == 1:  # Means it can go all the three ways and last action was backward
        choices = ["forward", "left", "right"]
        choices.remove(last_act[0][0])  # Remove last action (except backward) from array so it cant become a loop
        decide = random.choice(choices)

        result = rotate_servo(decide)  # Check if the decided direction is empty

        if not result:  # If decided direction is not empty choose any other valid direction
            decide = random.choice((remaining_choices.append(choices)).remove(decide))

        cursor.execute("INSERT INTO Actions (action, result) VALUES (?, ?) ", (decide, distance))

    conn.commit()
    print(decide)

    # Run the function that came from decision
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(decide)
    
    if decide == "forward":
        method(1)
    else:
        method()




time.sleep(2)

#speak("Welcome home sir")

# scheduler = BlockingScheduler()
# scheduler.add_job(check_alarm, 'interval', hours=0.5)
# scheduler.start()

st = Status()


def rotate_servo(direction):
    try:
        if direction == "left":
            p.ChangeDutyCycle(3)
        elif direction == "right":
            p.ChangeDutyCycle(9)
        else:
            p.ChangeDutyCycle(6)
    except KeyboardInterrupt:
        GPIO.cleanup()

    result, distance = calculate()

    if result == 1:
        return True
    return False

def motor_on():
    # Starting the motors
    p.start(25)
    p2.start(22)

    # Set all motors to stop first
    stop()

    count = 0
    while(count < 50):
        st.status = False

        db = cursor.execute('SELECT action FROM Actions ORDER BY id DESC')
        last_act = db.fetchmany()

        # Result means the success of last action (if it hit the wall or not 0, 1)
        # distance means result of last action (15 cm)
        result, distance = calculate()
        if result == 1: # If front is open go forward
            forward(0.6)

            stop()
            st.status = True

            pick_route(1, last_act, distance)
        else: # If front is close go back and decide where to go
            backward(0.4)
            stop()
            pick_route(0, last_act, distance)

            stop()
            st.status = True

        # Update the last action result and success
        cursor.execute("UPDATE Actions SET result = ?, success = ? WHERE id = (SELECT MAX(id) FROM Actions) "
                       , (distance, result))
        conn.commit()
        count = count + 1
    else:
        # If st.status is False then
        # This piece of code checks if Oracle is already stopped or not
        if not st.state:
            stop()
            speak("I am too tired sir")
            speak("Good Bye !")

        elif st.state:
            speak("I am too tired sir")
            speak("Good Bye !")


p1 = multiprocessing.Process(target=motor_on())
# p1.start()

p2 = multiprocessing.Process(target=start_interface())
# p2.start()

# servos_on()



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

