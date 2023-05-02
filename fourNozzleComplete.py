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


#enquiry requst for each PUMP
my_ENQrequest1 = bytearray(b'\x05\x30\x31')
my_ENQrequest2 = bytearray(b'\x05\x30\x32')
my_ENQrequest3 = bytearray(b'\x05\x30\x33')
my_ENQrequest4 = bytearray(b'\x05\x30\x34')


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


dataone = b''
datatwo = b''
datathree = b''
datafour = b''

def AQ_function(binary_data , pump):
    # Convert binary data to string
    string_data = binary_data.decode('ascii')
    # Split string into parts using "AQ" as the delimiter
    par = string_data.partition("AQ")
    if par[1] == 'AQ' :
     result_array = [par[0], "AQ", par[2]]
     global gg
     gg = result_array[0][1:3]
     # sent Permission for PUMPS 1 to 4
    
     #ser.write(my_ack)
     if gg == '01':
        ser.write(my_APsend1)
    
     elif gg == '02':
        ser.write(my_APsend2)

     elif gg == '03':
        ser.write(my_APsend3)

     elif gg == '04':
        ser.write(my_APsend4)
    

     

def PP_function(binary_data , pump):
    # Convert binary data to string
    string_data = binary_data.decode('ascii')
    #if string_data != "\x06":
    par = string_data.partition("PP")
    parOne = string_data.partition("LK")

    if par[1] == "PP":
        result_array = [par[0], "PP", par[2]]

        if result_array[1] == 'PP' :
            # Extract desired substrings from the third element of the result array
            sub_one = result_array[2][:7][:-3] + "." + result_array[2][4:7][-3:]
            sub_two = result_array[2][7:14]
            print("when pump {} is under fueling at {}kyats and volume is {}".format(pump, sub_two ,sub_one ))
    elif parOne[1] == "LK" : 
         result_array = [par[0], "LK", par[2]]

         if result_array[1] == 'LK':
            if pump == 1 :
                print("Pump 1 is Done")
            elif pump == 2 :
                print("Pump 2 is Done")
            elif pump == 3 :
                print("Pump 3 is Done")
            elif pump == 1 :
                print("Pump 4 is Done")


def ENQrequest1():
    ser.write(my_ENQrequest1)
    while True:
        # Read data from the serial port
        data1temp = ser.read()
        global dataone
        dataone += data1temp

        #time.sleep(0.01)
        if not data1temp:
            #print("brak")
            # No more data available, break out of the loop
            break

        # Process the received data
    print(dataone)
    data1 = dataone
    dataone = b''

    data6 = "\x06"

    if data1 == data6.encode('utf-8'):
        count = True
        print("06")
            
    else :
        #count = False
        print("no")
        AQ_function(data1,1)
        PP_function(data1,1)


def ENQrequest2():
        ser.write(my_ENQrequest2)
        while True:
            # Read data from the serial port
            data2temp = ser.read()
            global datatwo
            datatwo += data2temp

            #time.sleep(0.01)
            if not data2temp:
                #print("brak")
                # No more data available, break out of the loop
                break

        # Process the received data
        print(datatwo)
        data2 = datatwo
        datatwo = b''

        data6 = "\x06"

        if data2 == data6.encode('utf-8'):
            count = True
            print("06")
            
        else :
            #count = False
            print("no")
            AQ_function(data2,2)
            PP_function(data2,2)



def ENQrequest3():
        ser.write(my_ENQrequest3)
        while True:
            # Read data from the serial port
            data3temp = ser.read()
            global datathree
            datathree += data3temp

            #time.sleep(0.01)
            if not data3temp:
                #print("brak")
                # No more data available, break out of the loop
                break

        # Process the received data
        print(datathree)
        data3 = datathree
        datathree = b''

        data6 = "\x06"

        if data3 == data6.encode('utf-8'):
            count = True
            print("06")
            
        else :
            #count = False
            print("no")
            AQ_function(data3,3)
            PP_function(data3,3)


def ENQrequest4():
        ser.write(my_ENQrequest4)
        while True:
            # Read data from the serial port
            data4temp = ser.read()
            global datafour
            datafour += data4temp

            #time.sleep(0.01)
            if not data4temp:
                #print("brak")
                # No more data available, break out of the loop
                break

        # Process the received data
        print(datafour)
        data4 = datafour
        datafour = b''

        data6 = "\x06"

        if data4 == data6.encode('utf-8'):
            count = True
            print("06")
            
        else :
            #count = False
            print("no")
            AQ_function(data4,4)
            PP_function(data4,4)



while True:

    if count:
        ENQrequest1()
        ENQrequest2()
        ENQrequest3()
        ENQrequest4()
        
            