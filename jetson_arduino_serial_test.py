from serial import Serial
import time
arduino = Serial(port = '/dev/cu.usbmodem14201', baudrate=9600, timeout=.1)
arduino.flush()
done = 0
while(done==0):
    arduino.write(b'1')
    time.sleep(2)
    data = arduino.readline()
    if data==b'\x01': 
        done = 1
    print(data)

done = 0
arduino.flush()
while(done==0):
    arduino.write(b'0')
    time.sleep(2)
    data = arduino.readline()
    if data==b'\x00': 
        done = 1
    print(data)