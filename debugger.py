import RPi.GPIO as GPIO
import time

direction_indices = ["forward", "left", "right"]
direction_angles = [10, 12.5, 7.5]

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


def calculate():
    # Sends a signal and wait for it to return and calculate the distance by difference

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.2)

    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    if distance > 30:
        print("Mesafe:", distance - 0.5, "cm")
        # speak("My front is open")
        print("Open")
        return 1, distance
    else:
        # speak("There is an obstacle")
        print("Closed")
        return 0, distance


def pick_best_direction(options):

    best_direction_distance = 0

    p3.ChangeDutyCycle(0)

    for option in options:
        index = direction_indices.index(option)
        angle = direction_angles[index]

        p3.ChangeDutyCycle(angle)
        result, distance = calculate()

        if not result and distance > best_direction_distance:
            best_direction_distance = distance
            best_direction = option

    p3.ChangeDutyCycle(10)

    if not best_direction:
        return False, 0

    return best_direction, best_direction_distance


pick_best_direction(["left", "right"])
