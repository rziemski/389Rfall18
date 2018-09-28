Writeup 3 - Pentesting I
======

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 4 Writeup

### Part 1 (45 pts)
*After using 'nc cornerstoneairlines.co 45', a banner came up that said "Cornerstone Airlines" along with a prompt to type in an IP address. I typed in the IP address for cornerstone airlines, and it brought back the output of the Unix ‘ping’ command on the address that I gave. I realized the program that is running on port 45 probably just uses 'ping' followed by whatever I typed in. I did the nc command again, except this time, I typed in the same IP address as before but then put '&& ls /' right after it. The output was what I expected, the output of the ping command on the IP address followed by the contents of the directory on the web server. I then guessed that the flag was most likely located in the /home directory, so I used nc again to access port 45, I typed in '142.93.118.186 && ls /home/' and the flag.txt was displayed. At this point I noticed I probably did not need to type in the full IP address, but instead just a semi colon. His program most likely sends whatever I type into the prompt straight into the ping command. I repeated the same process but instead wrote ‘; cat /home/flag.txt’ after the prompt, and obtained this output: “Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}.“* 
*One thing Fred could do to prevent this vulnerability would be to use regular expressions in his script to make sure the user only types in a valid IP address and nothing else. The regular expression would look like /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/. This would prevent command injections because the user could no longer type in any code after the IP, or just skip the IP all together and input ‘;’ and a command after the semi colon.*


### Part 2 (55 pts)
*This part was a lot more challenging for me. I understood conceptually what to do, but Python I/O was something I had never experience before and it took me a while to figure it out. My stub.py has a main function and two other functions, one to simulate a shell and one to "pull" information. In the end the script mostly works, however there were two problems I could not figure out. For one, I could not figure out how to cd into a directory on the victim's machine and stay there, because after every command I would lose connection to the web server. In the screenshot provided to help us out with our shell, they cd into the home directory and then call ls and it just displays the flag.txt file. I could not figure out how to do this. My script only handles, cd and ls, and will update the directory you are in before the carrot (>). My second issue was I could not figure out how to download the flag from the victim's computer onto my computer. Instead my pull function just uses cat and displays the contents of whatever file you give it on the terminal. The script should handle the other actions requested in part 2.*
