import serial  # import serial module
ser = serial.Serial('/dev/tty/ACM0', 9600)  # connect to port and put baudrate
while(ser.read()):
    ser.read()  # read input
