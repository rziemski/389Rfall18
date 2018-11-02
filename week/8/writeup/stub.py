#!/usr/bin/env python2

import sys
import struct
import re
import time
import binascii

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
offset = 0
magic, version = struct.unpack("<LL", data[offset: offset + 8])
offset += 8
timestamp = struct.unpack("<L", data[offset: offset + 4])[0]
offset += 4
author = struct.unpack("<Q", data[offset: offset + 8])[0]
offset += 8
sectioncount = struct.unpack("<L", data[offset: offset + 4])[0]
offset += 4
# Header ends here

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

try:
	readtime = time.ctime(timestamp)
except NameError:
	bork("Bad timestamp! Not a valid UNIX timestamp")

try:
	readauth = binascii.unhexlify('%x' % author)
except TypeError:
	bork("Bad author! Not ascii code!")

if sectioncount <= 0:
	bork("Bad section count! Count less than or equal to 0")


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s, READABLE TIME: %s" % (int(timestamp), readtime))
print("AUTHOR: %s" % readauth)
print("SECTION COUNT: %d" % int(sectioncount))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
count = sectioncount
while count > 0:
	stype, slen = struct.unpack("<LL", data[offset: offset + 8])
	offset += 8
	text = ""
	doubles = ""

	print("SECTION %d" % count)

	if slen == 0:
		count -= 1
		continue

	# Check what type of section it is
	if stype == 0x1: # SECTION_PNG
		print("TYPE: SECTION_PNG")
		text = struct.unpack("<%dc" % slen, data[offset: offset + slen])
		offset += slen
		png_header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
		png_trailer = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'
		bytearr1 = bytearray(png_header)
		bytearr2 = bytearray(text)
		bytearr3 = bytearray(png_trailer);
		png_file = open("pic.png", "wb")
		png_file.write(bytearr1)
		png_file.write(bytearr2)
		png_file.write(bytearr3)
	elif stype == 0x2: # SECTION_DWORDS
		print("TYPE: SECTION_DWORDS")
		numwords = slen / 8
		while numwords != 0:
			word = struct.unpack("<q", data[offset: offset + 8])[0]
			offset += 8
			text += ", " + str(word)
			numwords -= 1
		print("[" + text + "]") 
	elif stype == 0x3: # SECTION_UTF8
		print("TYPE: SECTION_UTF8")
		text = struct.unpack("<%ds" % slen, data[offset: offset + slen])[0]
		offset += slen
		print(text.decode('utf-8'))
	elif stype == 0x4: # SECTION_DOUBLES
		print("TYPE: SECTION_DOUBLES")
		double = struct.unpack("<d", data[offset: offset + 8])
		offset += 8
		doubles += str(double) + ", "
		print("[" + doubles + "]")
	elif stype == 0x5: # SECTION_WORDS
		print("TYPE: SECTION_WORDS")
		numwords = slen / 4
		while numwords != 0:
			word = struct.unpack("<L", data[offset: offset + 4])[0]
			offset += 4
			text += ", " + str(word)
			numwords -= 1
		print("[" + text + "]")
	elif stype == 0x6: # SECTION_COORD
		print("TYPE: SECTION_COORD")
		lng, lat = struct.unpack("<dd", data[offset: offset + 16])
		offset += 16
		print("(LATITUDE: %d, LONGITUDE: %d)" % (lat, lng))
	elif stype == 0x7: # SECTION_REFERENCE
		print("TYPE: SECTION_REFERENCE")
		text = struct.unpack("<L", data[offset: offset + 4])[0]
		offset += 4
		print(text)
	elif stype == 0x9: # SECTION_ASCII
		print("TYPE: SECTION_ASCII")
		text = struct.unpack("<%ds" % slen, data[offset: offset + slen])[0]
		offset += slen
		print(text)
		newf = open("ascii.txt", "w")
		newf.write(text)

	count -= 1	

