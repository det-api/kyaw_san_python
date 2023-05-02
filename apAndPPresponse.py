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

#PUMP Permission Approved
my_APsend1 = bytearray(b'\x01\x30\x31\x02\x41\x50\x03\x11') 
my_APsend2 = bytearray(b'\x01\x30\x32\x02\x41\x50\x03\x12')
my_APsend3 = bytearray(b'\x01\x30\x33\x02\x41\x50\x03\x13')
my_APsend4 = bytearray(b'\x01\x30\x34\x02\x41\x50\x03\x14')

my_ack = bytearray(b'\x06')

# Create a serial object
#ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=0.5)
ser = serial.Serial(port, baudrate, bytesize, parity, stopbits, timeout=0.1)

# Read all data from the serial port
data1 = b''


def AQ_function(binary_data , pump):
    # Convert binary data to string
    string_data = binary_data.decode('ascii')
    # Split string into parts using "AQ" as the delimiter
    par = string_data.partition("AQ")
    if par[1] == 'AQ' :
     result_array = [par[0], "AQ", par[2]]
     global gg
     gg = result_array[0][1:3]
     print(gg)
     print(type(gg))
     # sent Permission for PUMPS 1 to 4
    
    #ser.write(my_ack)
     if gg == '01':
        ser.write(my_APsend1)
        print("AP sent")
        count = True

def PP_function(binary_data , pump):
    # Convert binary data to string
    string_data = binary_data.decode('ascii')
    #if string_data != "\x06":
    par = string_data.partition("PP")
    parOne = string_data.partition("LK")

    if par[1] == "PP":
        result_array = [par[0], "PP", par[2]]

        # print(result_array[1])

        if result_array[1] == 'PP' :
            # Extract desired substrings from the third element of the result array
            sub_one = result_array[2][:7][:-3] + "." + result_array[2][4:7][-3:]
            sub_two = result_array[2][7:14]
            print("when pump {} is under fueling at {}kyats and volume is {}".format(pump, sub_two ,sub_one ))
    elif parOne[1] == "LK" : 
         result_array = [par[0], "LK", par[2]]

        # print(result_array[1])

         if result_array[1] == 'LK' :
            print(" You have done ")


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
            #count = False
            print("no")
            AQ_function(data2,1)
            PP_function(data2,1)
            