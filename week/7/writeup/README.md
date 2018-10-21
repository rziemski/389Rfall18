Writeup 7 - Forensics I
======

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG image file

2. Bucharest, Romania

3. 2018:08:22 11:33:24

4. Iphone 8 Camera

5. 539.5 m Above Sea Level

6. CMSC389R-{look_I_f0und_a_str1ng}, CMSC389R-{abr@cadabra}

### Part 2 (55 pts)

*I first checked what kind of file the binary was. I ran the 'file' command on it and it says it was an ELF executable file. I ran the executable and it printed out, "Where is your flag?". I decided to use gdb to step through the program and disassemble the main function of the binary. I noticed at first that the main function was moving a bunch of values right next to each other, so I figured it was spelling out a file name or something of that nature. I converted the hex it was putting on the stack to decimal and then looked up the ASCII values for each decimal. I noticed it spelled out "/tmp/.stego". I figured it was writing to this file on my local machine so I entered my tmp file and the .stego hidden file was there. I deleted it and ran the binary file again to make sure it was the binary file that was generating it. I ran 'file' on it and it said it was just data, which stumped me for a while. I received a tip from one of the instructors to check out the magic bytes of the file and compare that to a JPG magic byte. After a hexdump I noticed the magic bytes of .stego was the same as the JPG magic byte but moved to the right slightly. I modified the magic bytes in the .stego file and ran 'file' on it again and it read that it was a JPG file. I was not sure where to go from here because I tried running strings on the file and grep "CMSC" on a hexdump of .stego but was not getting any flags. I went back to the file being .stego. I thought it just had to have a message hidden using steganography. It asked for a password, so I tried "password", "dinosaur" (the picture was of a dinosaur), and others and nothing worked. Then I realized the picture was of a stegosaurus and so I tried "stegosaurus" and that was the password that revealed the flag: CMSC389R-{dropping_files_is_fun}*
