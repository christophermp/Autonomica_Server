
import socket

TCP_IP = '10.0.0.111'
TCP_PORT = 9600
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(b'::c1p=5000\r\n')
s.close()