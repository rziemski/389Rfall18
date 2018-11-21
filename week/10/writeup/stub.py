#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import time

#####################################
### STEP 1: Calculate forged hash ###
#####################################

host = "142.93.118.186"
port = 1234

#connecting to notary
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)
print(data)

#choosing option 1
s.send('1\n')
data = s.recv(1024)
print(data)

#sending 'Hello World!' as message
s.send('Hello World!\n')
data = s.recv(1024)
print(data)
data = data.split(':')


message = 'Hello World!'    # original message here
legit = data[2].strip()      # a legit hash of secret + message goes here, obtained from signing a message

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'Something malicious'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
msg_len_in_bytes = len(message)
msg_len_in_bits = msg_len_in_bytes * 8
pad_len_in_bytes = ((448 - msg_len_in_bits) / 8) - 1 #subtract one bc of \x80 in beginning
secret_len = 10   # this is a guess, should be between 6 and 15

padding = '\x80'
count = pad_len_in_bytes - secret_len
while count != 0:
	padding = padding + '\x00'
	count = count - 1

padding = padding + '\\' + hex(msg_len_in_bits + (secret_len * 8))[1::] # size of message + secret in bits
count = 7
while count != 0:
	padding = padding + '\x00'
	count = count - 1 

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
payload = message + padding + malicious

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!

#send second option
s.send('2\n')
data = s.recv(1024)
print(data)

#send fake hash
s.send(fake_hash + '\n')
data = s.recv(1024)
print(data)

#send payload
s.send(payload + '\n')
time.sleep(1)
data = s.recv(1024)
print(data)
print(repr(payload))

s.close()



