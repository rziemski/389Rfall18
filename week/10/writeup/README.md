Writeup 10 - Crypto II
=====

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 10 Writeup

### Part 1 (70 Pts)
*Original Hash: ac06bd7b0c41e7b6544fd014751666d9*
*Crafted Hash: 38086ea35ddd93077800e5e4e54a23e3*
*Payload: 'Hello World!\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\\xb0\x00\x00\x00\x00\x00\x00\x00Something malicious'
Flag: CMSC389R-{i_still_put_the_M_between_the_DV}*

### Part 2 (30 Pts)
*To generate a key:* `gpg --gen-key`
*Then you type in a name, email, and a password*
*To import a public key:* `gpg --import pubkey.asc`
*To encrypt a message and dump it to a file:* `gpg -e -u "Your Name" -r "Their Name" msg.txt`

