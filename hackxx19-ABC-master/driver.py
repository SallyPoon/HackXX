import serial
import time
import math

BAUD_RATE = 115200
PORT = "/dev/tty.14-DevB"
ACCEL_PORT = "/dev/cu.usbmodem14601"

TIMEOUT = 2

PAUSE = False

ANGLE = 90

# Bytes!
FORWARD = b"w"
BACKWARD = b"s"
LEFT = b"a"
RIGHT = b"d"
SERVO_LEFT = b"q"
SERVO_RIGHT = b"e"

def forward():
    bt.write(FORWARD)
    time.sleep(TIMEOUT)

def backwards():
    bt.write(BACKWARD)
    time.sleep(TIMEOUT)

def left():
    bt.write(LEFT)
    time.sleep(TIMEOUT)

def right():
    bt.write(RIGHT)
    time.sleep(TIMEOUT)

def servo_left():
    bt.write(SERVO_LEFT)
    time.sleep(TIMEOUT)

def servo_right():
    bt.write(SERVO_RIGHT)
    time.sleep(TIMEOUT)

def pause():
    PAUSE = !PAUSE
    time.sleep(TIMEOUT);


# Setup serial port with path to port
bt = serial.Serial(PORT, 115200, timeout=5)
accelerometer = serial.Serial(ACCEL_PORT, 115200, timeout=5)
bt.flushInput()
accelerometer.flushInput()

while True:
    reader = accelerometer.readline();
    coords = reader.decode("utf-8")
    coords = coords.strip()
    result = [coords.strip() for coords in coords.split(",")]
    print(result)
    try:
        results = [int(x) for x in result]
    except:
        continue;
    x_axis = results[0]
    y_axis = results[1]
    z_axis = results[2]
    if z_axis >= 17:
        pause()
    if PAUSE:
        if z_axis/y_axis * ANGLE >= 390:
            forward()
            print("forward " + str(y_axis))
        if z_axis/y_axis * ANGLE<= 310:
            backwards()
            print("backward " + str(y_axis))
        if z_axis/x_axis * ANGLE >= 380:
            right()
            print("right " + str(x_axis))
        if z_axis/x_axis * ANGLE <= 320:
            left()
            print("left " + str(y_axis))
