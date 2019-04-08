import serial
import time

BAUD_RATE = 115200
PORT = "/dev/tty.14-DevB"
ACCEL_PORT = "/dev/cu.usbmodem14601"

TIMEOUT = 0.5

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

def flush():
    for _ in range(20):
        accelerometer.reset_input_buffer()
        time.sleep(5/20)

# Setup serial port with path to port
bt = serial.Serial(PORT, 115200, timeout=5)
accelerometer = serial.Serial(ACCEL_PORT, 115200, timeout=5)
bt.flushInput()
accelerometer.flushInput()
x_axis_holder = 0
y_axis_holder = 0

accelerometer.readline()
while True:
    coords = accelerometer.readline()
    print(coords.decode("utf-8"))
    try:
        result = [int(coord.strip()) for coord in coords.decode("utf-8").split(",")]
    except:
        continue
    if len(result) == 2 or len(result) == 3:
        x_axis = result[0]
        y_axis = result[1]
    else:
        continue

    if abs(x_axis_holder - x_axis) < 20 and abs(y_axis_holder - y_axis) < 20:
        continue
    if y_axis  >= 15:
        forward()
        print(str(x_axis_holder) + ',' + str(y_axis_holder))
        print("forward " + str(y_axis - y_axis_holder))
        x_axis_holder = x_axis
        y_axis_holder = y_axis
        print(result)
    elif y_axis < -15:
        print(str(x_axis_holder) + ',' + str(y_axis_holder))
        print("backward " + str(y_axis - y_axis_holder))
        backwards()
        x_axis_holder = x_axis
        y_axis_holder = y_axis
        print(result)
    if (x_axis >= 15):
        print(str(x_axis_holder) + ',' + str(y_axis_holder))
        print("right " + str(x_axis_holder - x_axis))
        right()
        x_axis_holder = x_axis
        y_axis_holder = y_axis
        print(result)
        #flush()
    elif (x_axis < -15):
        print(str(x_axis_holder) + ',' + str(y_axis_holder))
        print("left " + str(x_axis_holder - x_axis))
        left()
        x_axis_holder = x_axis
        y_axis_holder = y_axis
        print(result)
