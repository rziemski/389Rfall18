OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Thursday, September 13 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `kruegster1990`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `kruegster1990` and answer the following questions:

1. What is `kruegster1990`'s real name? *Fred Krueger*

2. List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.
*- Was born in 1990 and lives in Silver Spring, MD (retrieved from his Twitter account, which I found from Googling his username)
-His email address is kruegster1990@tutanota.com (found on cornerstoneairlines.co)
-His website is cornerstoneairlines.co (found on his Twitter account)
-Has Twitter, Stwity, Instagram, Reddit, and I think a wikiHow account
  -these were all found through either checkusername or namevine.com after searching his username*

3. What is the IP address of the webserver hosting his company's site? How did you discover this?
*IP Address: 142.93.118.186
 -Found this from typing the domain name into dnsdumpster.com*

4. List any hidden files or directories you found on this website. Did you find any flags?
*-The website contains a robots.txt file, which is how I discovered the secret directory on Fred's website
-In the soucre code of the secret page there was the flag CMSC389R-{fly_th3_sk1es_w1th_u5}
-In the source code of the home page was CMSC389R-{h1dden_fl4g_in_s0urce}
-I used Dirbuster to brute force the website to guess directory names, and I found three more hidden directories: /icons, /icons/small, and /server-status
	-all three directories were forbidden for me to access*

5. Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?
*IP address associated with the Admin directory on the website: 142.93.117.193
 -I found this from navigated to the admin directory and looking at the URL*

6. If you found any associated server(s), where are they located? How did you discover this?
*-dnsdumpster.com says the main IP address (142.93.118.186) is located in Toronto,Canada, however Shodan.com says it is in New York
-the IP for the Admin page is located in New York according to shodan.io, but zoomeye.org says that IP is located in Toronto like the main page*

7. Which operating system is running on the associated server(s)? How did you discover this?
*-142.93.118.186 is a Ubuntu System
	-found on censys.io
-142.93.117.193 is also Ubuntu
	-found on censys.io*

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
*-->CMSC389R-{dns-txt-rec0rd-ftw}
	-located in the text file on the DNS records*

### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to the Cornerstone Airlines administrator server via an open port that you should have found in Part 1. 

Once you have gained access to the Cornerstone Airlines administrator portal with the correct login credentials, you will have access to a system shell. 

Use your knowledge of Linux and OSINT techniques to locate a specific flight record, read it, and submit the flag inside.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.
*After an nmap scan on the Admin page of the cornerstoneairlines.co website, I saw some odd ports were open, like port 1337. After nc'ing to that port, I got a prompt that said "username". As for the bruteforce script, I went online to read how the python socket module worked, and read about the various methods I could use. I tried to make the script as simple as possible. It will only stop if it does not get a "Fail" response from the prompt, and returns the correct password, which was "pokemon".
From there I went to home/flight_records, and saw a list of flight records. I remembered from his instagram account he posted a flight ticket, so I used that airplane number on the ticket, and used the cat linux command to get the flag. CMSC389R-{c0rn3rstone-air-27670}*

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, [Push it](https://github.com/UMD-CS-STICs/389Rfall18/blob/master/HW_Submit_Instructions.md) up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
