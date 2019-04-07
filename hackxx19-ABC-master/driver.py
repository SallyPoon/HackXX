import serial
import time
import math

BAUD_RATE = 115200
PORT = "/dev/tty.14-DevB"
ACCEL_PORT = "/dev/cu.usbmodem14601"

TIMEOUT = 0.5

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
#bt = serial.Serial(PORT, 115200, timeout=5)
accelerometer = serial.Serial(ACCEL_PORT, 115200, timeout=5)
#bt.flushInput()
accelerometer.flushInput()

while True:
    reader = accelerometer.readline();
    print(reader)
    coords = reader.decode("utf-8")
    coords = coords.strip()
    result = [coords.strip() for coords in coords.split(",")]
    #print(result)
    try:
        results = [int(x) for x in result]
    except:
        continue;
    print(results)
    x_axis = results[0]
    y_axis = results[1]
    z_axis = results[2]
    # if z_axis >= 17:
    #     PAUSE = not PAUSE
    #     time.sleep(TIMEOUT);
    # if PAUSE:
    #     if y_axis >= 17 and z_axis <= 17:
    #         forward()
    #         print("forward " + str(y_axis))
    #     if y_axis <= -17 and z_axis >= -17:
    #         backwards()
    #         print("backward " + str(y_axis))
    #     if x_axis >= 17:
    #         right()
    #         print("right " + str(x_axis))
    #     if x_axis <= -17:
    #         left()
    #         print("left " + str(x_axis))
