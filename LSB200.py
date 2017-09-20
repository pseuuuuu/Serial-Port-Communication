import time
import serial

ser = serial.Serial(
    port='COM3',
    baudrate=38400,
    stopbits=1,
    bytesize=8,
    timeout=1,
    rtscts=True,
    writeTimeout=1
)

ser.flushInput()
ser.flushOutput()

print ('Serial Port is connected: ' + str(ser.isOpen()))

'''
ser.write("VER".encode('ascii')+b'\r\n')
time.sleep(2) 
# print (ser.inWaiting())
out=ser.read(64)
print ('Receiving...'+out)
ser.close()

'''

print ('Enter your commands below.')

while 1 :
    out=''
    ser.flushInput()
    ser.flushOutput()
    # python 2.7
    #cmd= raw_input(">> ")

    # python 3.4
    cmd = input(">> ")
    
    ser.write(cmd.encode('ascii')+b'\r\n')
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(24).decode()
    if out != '':
        print (">>" + out)
    else:
        print ("Nothing Received")

    if cmd== 'EXIT':
        ser.close()
        print ('Serial Closed')
        break
