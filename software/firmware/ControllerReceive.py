import os
import serial
import time
import socket
from serial.tools import list_ports

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
socket.bind((UDP_IP, UDP_PORT))

serbaud = 9600
sertimeout = 3

RoverDrivePortString = "ID: MainDrive"
RoverDrivePort = ""

def list_serialPorts():
  for port in list_ports.comports():
    yield port[0]
    
def get_controlPort(checkString):
  for port in list(list_serialPorts()):
    try:
      ser = serial.Serial(port, serbaud, timeout=sertimeout)
      multilinecheck = []
      for i in range(0,2):
	multilinecheck.append(ser.readline())
	time.sleep(2)
      if any(checkString in string for string in multilinecheck):
	  print "Port Found: " + port
	  ser.close()
	  return port
    except serial.SerialException:
      pass

def SendPacket(SerPort, left, right, estop, chksum):  
      SerPort.write(chr(255))
      SerPort.write(estop)
      SerPort.write(left)
      SerPort.write(right)
      SerPort.write(chksum)
      SerPort.write(chr(255))
      
if __name__ == '__main__':
  RoverDrivePort = get_controlPort(RoverDrivePortString)
  DrvSer = serial.Serial(RoverDrivePort, serbaud, timeout=sertimeout)
  time.sleep(2)
  DrvSer.write(chr(68))
  time.sleep(2)
 
  while(1):
    os.system('clear')
    data, addr = socket.recvfrom(1024)
    if data:
      estop = data[1]
      left = data[2]
      right = data[3]
      chksum = data[4]
      print "Left Value: " + str(int(ord(left)))
      print "Right Value: " + str(int(ord(right)))
      print "E-Stop: " + str(int(ord(estop)))
      SendPacket(DrvSer, left, right, estop, chksum)
      time.sleep(.005)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 