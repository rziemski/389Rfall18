Writeup 11 - Web II
=====

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 11 Writeup

### Part 1 (40 Pts)
*It took me way too long to realize that 'S' 'Q' and 'L' were bolded on the assignment README. Once I read that I realized I had to conduct an SQL injection. I figured out that when you click the items listed on the site, a lookup takes place. Using what I learned about SQL injection, I knew I could inject an SQL command in the url following* `id`*. I kept getting an Internal Server Error when I would type in my injection. I had to go to office hours to figure out that the server blocks the* `OR` *SQL command, so I had to figure out how to get around that. I found out that lowercase 'or' is also acceptable syntax in SQL, so I used that instead. My only other problem was making sure my HTML encoding was correct. At first I tried just putting in the command without the html encoding and I would get an internal server error. I had to figure out that %27 was for an apostraphe and %20 was for a space. My final sql injection looked like* `/item?id=3%27%20or%201=1%20--%20` *and it returned the flag* `CMSC38R-{y0U-are_the_5ql_n1nja}`

### Part 2 (60 Pts)
*In the description of the first level, the site says the user input is directly included into the page. After reading that, I could guess that if I surrounded* `alert("hello")` *with script tags, that it would execute.*

*The second part was slightly more challenging. I could not use a script tag this time, but with some previous knowledge of HTML, I tried using an image tag,* `<img src="blah" onerror="alert("hello")"/>` *and that got me through level 2.*

*Level 3 was not too bad for me. It was actually similar to level two in that you needed to use onerror. I noticed when you click each image on the site, the number at the end of the url changes. I did some more inspecting using the code provided, I noticed the chooseTab function constructs an HTML image tag. I realized if I could put the injection in the url of the page, it would execute my code. The URL I put in was* `https://xss-game.appspot.com/level3/frame#3' onerror='alert("hello")'` *and that got me through level 3.*

*Level 4 took me a long time to figure out, and I used the hints for this one because I was struggling to figure out what to do. I put in the (') like the hint said and received the error code. Part of the output looked like this:* `startTimer(''');`*. I figured what I would need to do is somehow escape the function call and inject the alert function after it. I tried doing* `https://xss-game.appspot.com/level4/frame?timer=');` *But it was not escaping correctly. I remembered from the first part of this project that sometimes it would mess up if the url was not html encoding. I looked up the encoding for a semi-colon and found out it was %3B. The final url turned out to be:* `https://xss-game.appspot.com/level4/frame?timer=');alert(1);('`*.*

*Level 5 was not as bad as level 4. After looking through the code, after you type in your email and click "Next >>", it redirects you to the value that "next" is set to. I also noticed that the code does nothing to the email you put input. So I tried setting next in the url to* `alert("hello")` *but that would not work. I did some digging online and found that I had to insert* `javascript:` *in front of it to get it to execute the javascript alert function. I typed in* `https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert("hello")` *into the url, then typed in a bogus email, and that got me through level 5.*

*I understood what I had to do for level 6, however I was unsure how to host my own javascript code. I know that I had to type another url after the '#' in the original url. I tried out the hints and the last hint helped with hosting the code. I tried* `https://xss-game.appspot.com/level6/frame#https://google.com/jsapi?callback=foo`*, but that did not work because there is a regex blocking https from being in the injected url. After looking at the code I realized the regex is NOT case sensitive. So I just switched https to htTps and then it worked. I was not positive what the google site did, but after some tests, I realized it just executes whatever the value of callback is, so I just switched it to alert("hey), and for some reason that did not work either. I tried many different variations until I tried just typing in 'alert' and that worked. The final url was:* `https://xss-game.appspot.com/level6/frame#//www.google.com/jsapi?callback=alert`*.*  