Writeup 9 - Crypto I
=====

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 9 Writeup

### Part 1 (60 Pts)
*Part one for me was the more challenging part of the two. I knew what I had to do conceptually, but my inexperience with python was the reason this part took me so long. For the longest time my program would only crack the first hash, and it would not crack the others. This stumped me, so I decided to go to the office hours to ask for suggestions. It turns out my for loop that would go through once, and then stop. I needed to add* `h = hashes.readlines()` and `w = wordlist.readlines()` *This fixed my issue. My output was as follows:*
**Bruteforcing hashes...
Password: neptune, Salt: k
Password: pizza, Salt: p
Password: loveyou, Salt: u
Password: jordan, Salt: m
Complete**

### Part 2 (40 Pts)
*This part came a lot quicker to me. At first, I thought I only had to answer one question, and I would get the flag. However I noticed every time I would connect to the server it would change up the hash and the hash type. I did some splitting of the string output to get the hash type and the hash, then used a bunch of if statements to determine the correct hash type. I ran the program again, and this is when I realized I would have to make some type of loop, because it asks multiple questions. I added a while loop, and this worked until the end when I would get an error when I was splitting up the output, because when you win the game, the output is different. I could see what the ending output is on the terminal though, so I added an if statement that would check if I won the game, and the program would exit normally. The flag I found at the end was* **CMSC389R-{H4sh-5l!ngInG-h@sH3r}**