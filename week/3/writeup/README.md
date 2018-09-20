Writeup 3 - OSINT II, OpSec and RE
======

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 3 Writeup

### Part 1 (100 pts)
*Mr. Krueger, there are three ways in which you can make your web server more secure: closing ports that are not needed, using stronger passwords, and looking into an IDS for your web server.
Your web server has multiple ports open (1337, 22, etc). The more ports that are left open on your server, the more you increase your attack surface, making it easier for a hacker to gain unauthorized access. Obviously you need port 80 to stay open, but I would recommend closing any ports on your server unless they are absolutely necessary to keep open. You could also filter your ports to only specific IP addresses so that only a select amount of machines can actually access those services.
You also need to have a stronger password for your workplace login. Your password was guessed by a brute-force attack in about 25 minutes. I would recommend using a password manager like LastPass. It can generate very complex passwords for you, and then store that password so you do not need to remember it. This would make it a lot more difficult for a brute force attack to guess your password.
My final suggestion would be for you to look into getting an Incident Detection System (IDS) integrated on your web server. An IDS would be able to detect suspicious activity on your web server, for example a brute force attack, and take measures to stop the attack before any real damage is done. Rapid7 and Symantec both have quality IDS's that you should check out.*
