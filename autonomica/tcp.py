
import socket

TCP_IP = '10.0.0.111'
TCP_IP2 = '172.23.192.1'
TCP_PORT = 9600
TCP_PORT2 = 5000



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(b'::c1p=5000\r\n')
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP2, TCP_PORT2))
s.send(b'Lamp_on\r\n')
s.close()