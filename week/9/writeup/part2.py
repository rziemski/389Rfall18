#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import time

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data)
data = data.split('the')
data = data[2].split()
hash_type = data[0]
hash_literal = data[3]

while 'You win!' not in data:
	if hash_type == 'sha512':
		answer = hashlib.sha512(bytes(hash_literal)).hexdigest()
	elif hash_type == 'sha384':
		answer = hashlib.sha384(bytes(hash_literal)).hexdigest()
	elif hash_type == 'sha256':
		answer = hashlib.sha256(bytes(hash_literal)).hexdigest()
	elif hash_type == 'sha224':
		answer = hashlib.sha224(bytes(hash_literal)).hexdigest()
	elif hash_type == 'sha1':
		answer = hashlib.sha1(bytes(hash_literal)).hexdigest()
	elif hash_type == 'md5':
		answer = hashlib.md5(bytes(hash_literal)).hexdigest()

	s.send(answer + '\n')
	data = s.recv(1024)
	print(data)
	if 'You win!' in data:
		break
	data = data.split('the')
	data = data[1].split()
	hash_type = data[0]
	hash_literal = data[3]

# close the connection
s.close()
