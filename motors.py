import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# from oracle import lights_o

# Set the GPIO pins
GPIO.setmode(GPIO.BCM)

in1 = 24  # Motor 1
in2 = 23  # Motor 2
in3 = 27  # Motor 3
in4 = 10  # Motor 4

en = 25  # Engine 1
en2 = 22  # Engine 2


GPIO.setup(in1, GPIO.OUT)  # Left side motors
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)  # Right side motors
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)


p = GPIO.PWM(en, 1000)
p2 = GPIO.PWM(en2, 1000)

# Set motors rpm
p.ChangeDutyCycle(25)
p2.ChangeDutyCycle(25)


def start_motors():
    # Starting the motors
    print("starting motors")
    p.start(25)
    p2.start(22)

    # Set all motors to stop first
    stop()


def stop():
    time.sleep(0.5)

#     lights_o("stop")

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


def forward(sec):
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)

    print("Going forward")
#     lights_o("forward")

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(en, GPIO.HIGH)
    GPIO.output(en2, GPIO.HIGH)

    time.sleep(sec)


def backward(sec):
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)

    print("Going back")
#     lights_o("backward")

    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(en, GPIO.HIGH)
    GPIO.output(en2, GPIO.HIGH)

    time.sleep(sec)


def right():
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)

    print("Going right")

#     lights_o("right")

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(en, GPIO.LOW)
    GPIO.output(en2, GPIO.HIGH)


def left():
    p.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    print("Going left")

#     lights_o("left")

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(en, GPIO.HIGH)
    GPIO.output(en2, GPIO.LOW)