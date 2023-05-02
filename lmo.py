import serial
import time

# Define the RS422 communication settings
port = 'COM10'  # Replace with the actual port name
baudrate = 9600
bytesize = serial.EIGHTBITS
parity = serial.PARITY_EVEN
stopbits = serial.STOPBITS_ONE

my_CQrequest1 = bytearray(b'\x01\x30\x31\x02\x43\x51\x03\x12')
# Create a serial object
#ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=0.5)
ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=0.1)

# Read all data from the serial port
data1 = b''

while True:
    ser.write(my_CQrequest1)
    while True:
        # Read data from the serial port
        data = ser.read()
        data1 += data

        #time.sleep(0.01)
        if not data:
            print("brak")
            # No more data available, break out of the loop
            break

        # Process the received data
    print(data1)
    data1 = b''