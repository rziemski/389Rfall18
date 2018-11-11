#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashes = open("../hashes", 'r')


# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

print("Bruteforcing hashes...")
h = hashes.readlines()
w = wordlist.readlines()

for sha512 in h:
	sha512 = sha512.strip()
	for password in w:
		password = password.strip()
		for salt in salts:
			salt_and_pass = salt + password
			hashed_pass = hashlib.sha512(bytes(salt_and_pass)).hexdigest()
			if hashed_pass == sha512:
				print("Password: %s, Salt: %s" % (password, salt))
			hashed_pass = ""
			salt_and_pass = ""
print("Complete")