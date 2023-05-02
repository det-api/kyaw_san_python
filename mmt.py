import serial
import time

count = True
filename = "output.txt"
# Define the RS422 communication settings
port = 'COM10'  # Replace with the actual port name
baudrate = 9600
bytesize = serial.EIGHTBITS
parity = serial.PARITY_EVEN
stopbits = serial.STOPBITS_ONE

my_CQrequest1 = bytearray(b'\x01\x30\x31\x02\x43\x51\x03\x12')
my_ENQrequest1 = bytearray(b'\x05\x30\x31')
# Create a serial object
#ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=0.5)
ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=0.1)

# Read all data from the serial port
data1 = b''

while True:

    if count:
        ser.write(my_ENQrequest1)
        while True:
            # Read data from the serial port
            data = ser.read()
            data1 += data

            #time.sleep(0.01)
            if not data:
                #print("brak")
                # No more data available, break out of the loop
                break

        # Process the received data
        print(data1)
        data2 = data1
        data1 = b''

        data6 = "\x06"

        if data2 == data6.encode('utf-8'):
            count = True
            print("06")
            
        else :
            count = False
            print("no")
            