import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_ad = '127.0.0.1'
port = int(input('Please enter the port : '))
s.connect((ip_ad, port))
while True:
    str=input("Enter a message :")
    s.send(str.encode())
    if str == 'exit': break
data=s.recv(1024)
s.close()
print(data.decode())