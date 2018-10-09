Writeup 5 - Binaries I
======

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 5 Writeup

*At first I was not too happy to see assembly code again, especially since it was a different type of assembly that I learned in my previous computer science class. It took me some getting used to the syntax and the main registers for x86. I had to refer to the slides a lot. How I coded in assembly previously would try as simply as possible to translate the given C code into assembly line by line. This is how I tackled the memset function. 
After looking at the slides I was able to figure out that the 3 parameters were stored in rdi, rsi, and rdx, respectively. I then moved those values into the registers I wanted, and set my counter register (rcx) to 0 to begin my for loop. The for loop was pretty simple to write. I just moved every value in the src to the destination and then incremented both of the pointers until my counter concluded the loop. 
Strcpy was more difficult for me. I looked on Piazza and saw people posting about the stosb opcode. After some digging I found out that it was used to copy strings from one place to another, so I figured I would use it. A small explanation of what registers to use for stos was posted on Piazza and I used that to guide me. However, I was not able to complete this function. When I run the test, every character prints out perfectly except for the 'W' in "World" and I do not understand why. I think it may have something to do with the space bar in front of it. I tried to look up a solution online but could not find one.*

