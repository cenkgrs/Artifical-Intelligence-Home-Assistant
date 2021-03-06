from motors import right, left, backward, forward, stop, start_motors
#from web import start_interface
import multiprocessing
import RPi.GPIO as GPIO
import time
import pyttsx3
import random

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

servo = 16

# Set the GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(servo,GPIO.OUT)

GPIO.setup(7, GPIO.OUT) # Left light
GPIO.setup(8, GPIO.OUT)  # Right light
GPIO.setup(11, GPIO.OUT)  # Forward light

GPIO.output(7, True)
GPIO.output(8, True)
GPIO.output(11, True)

'''en = 25  # Engine 1
en2 = 22  # Engine 2
p = GPIO.PWM(en, 1000)
p2 = GPIO.PWM(en2, 1000)
'''

# Set servo duty cylcle
p3 = GPIO.PWM(servo,50) 

# Starting servos
p3.start(0)
p3.ChangeDutyCycle(0)

# Set database connection
conn = sqlite3.connect('/home/pi/Oracle/Oracle')
cursor = conn.cursor()

direction_indices = ["forward", "left", "right"]
direction_angles = [10, 12.5, 7.5]

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


    if distance > 30:
        print ("Mesafe:",distance - 0.5,"cm")
        #speak("My front is open")
        print("Open")
        return 1, distance
    else:
        #speak("There is an obstacle")
        print("Closed")
        return 0, distance
    
      
def pick_best_direction(options):
    
    best_direction = False
    best_direction_distance = 0

    p3.ChangeDutyCycle(0)

    for option in options:
        index = direction_indices.index(option)
        angle = direction_angles[index]

        p3.ChangeDutyCycle(angle)
        result, distance = calculate()

        if result == 1 and distance > best_direction_distance:
            best_direction_distance = distance
            best_direction = option

    p3.ChangeDutyCycle(10)
    
    if not best_direction:
        return False, 0
    
    print(best_direction)
    return best_direction, best_direction_distance


def pick_route(type, last_act, distance):
    print('picking route')
    remaining_choices = []
    if type == 0:  # Means it can't go forward and last action was forward
        choices = ["forward", "left", "right"]
        print('choices is ', choices)   
        decide = random.choice(choices)
        print('decide is ', decide)
        choices.remove(decide)  # Remove decided direction so it cant become a loop          

        result, distance = servos_on(decide)  # Check if the decided direction is empty (1, 0)

        # If decided direction is not empty choose any other valid direction

        while not result:
            print('choices is ', choices)
            # If choices list is empty -> meaning there is no open road so turn back
            if not choices:
                print("there is no choice left going back")
                backward(0.4)
                return

            # If there is still rotation to decide pick one and examine

            #decide = random.choice((remaining_choices.append(choices).remove(decide)))
            decide = random.choice(choices)
            choices.remove(decide)  # Remove decided direction so it cant become a loop

            result, distance = servos_on(decide)
            
        # Record last two actions
        cursor.execute("INSERT INTO Actions (action) VALUES ('forward')")  # This one because of last action was forward
        cursor.execute("INSERT INTO Actions (action, result) VALUES (?, ?) ", (decide, distance))

    # Getting best route to go
    elif type == 1:  # Means it cant go forward because last time forward was not empty and last action was backward
        choices = ["left", "right"]
        print('did go back last act was ', last_act[0][0])        
        # Remove last action (except backward) from array so it cant become a loop
        if last_act[0][0] == 'left' or last_act[0][0] == 'right':
            
            choices.remove(last_act[0][0]) # It may have gone left and face an object

        decide, distance = pick_best_direction(choices)  # Check if the decided direction is empty

        # If there is no empty direction -> go back
        if not decide:
            print("no best direction going back")
            backward(0.4)
            return

        cursor.execute("INSERT INTO Actions (action, result) VALUES (?, ?) ", (decide, distance))

    conn.commit()
    time.sleep(2)

    # Run the function that came from decision
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(decide)
    
    print('method is:' , method)
    if decide == "forward":
        method(0.6)
    else:
        method()
        

time.sleep(2)

# scheduler = BlockingScheduler()
# scheduler.add_job(check_alarm, 'interval', hours=0.5)
# scheduler.start()

st = Status()


def servos_on(direction):
    print('direction is ', direction)
    p3.ChangeDutyCycle(0)
    
    if direction == 'left':
        print('looking for left')
        p3.ChangeDutyCycle(12.5)

    elif direction == 'right':
        print('looking for right')
        p3.ChangeDutyCycle(7.5)

    else:
        p3.ChangeDutyCycle(10)
    
    result, distance = calculate()
        
    p3.ChangeDutyCycle(10)
    time.sleep(0.2)
    p3.ChangeDutyCycle(0)

    if result == 1:
        return True, distance
    
    return False, distance


def rotate_servo(direction):
    p3.ChangeDutyCycle(7 / 5)

    try:
        if direction == "left":
            print('looking for left')
            p3.ChangeDutyCycle(7.5)
        elif direction == "right":
            print('looking for right')
            p3.ChangeDutyCycle(12.5)
        else:
            p3.ChangeDutyCycle(10)

        p3.ChangeDutyCycle(10)
        time.sleep(0.5)
        p3.ChangeDutyCycle(0)

    except KeyboardInterrupt:
        GPIO.cleanup()

    print("came here")
    result, distance = calculate()

    if result == 1:
        print('direction is open')
        time.sleep(2)

        return True
    print('direction close')
    time.sleep(2)
    return False

def motor_on():
    start_motors()
    print("motors on")
    
    count = 0
    while(count < 10):
        st.status = False

        db = cursor.execute('SELECT action FROM Actions ORDER BY id DESC')
        last_act = db.fetchmany()

        # Result means the success of last action (if it hit the wall or not 0, 1)
        # distance means result of last action (15 cm)
        result, distance = calculate()
        if result == 1:  # If front is open go forward
            forward(0.6)
            
            stop()
            time.sleep(3)
            
            st.status = True

            pick_route(0, last_act, distance)
            stop()
            time.sleep(2)
        else: # If front is close go back and decide where to go
            backward(0.4)
            stop()
            time.sleep(3)
            
            pick_route(1, last_act, distance)
            stop()
            time.sleep(2)
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


#p1 = multiprocessing.Process(target=motor_on())
#p1.start()

#p2 = multiprocessing.Process(target=start_interface())
#p2.start()


# Code for manually controlling Oracle with numpads - i will add dualshock control

pick_route(0, 'forward', 50)
# motor_on()

def manual_controls():
    
    condition = True

    while condition:
        response = _getch()
        print(response)

        if response == '8':
            forward(0.5)
        elif response == '5':
            backward(1)
        elif response == '6':
            right()
        elif response == '4':
            left()
        elif response == 'q':
            stop()
            condition = False
        else:
            print('did not get that')
    print('finished')


