Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *Ryan Ziemski*
Section: *0201*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Ryan Ziemski*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. UMD CyberSec website

2. c0uchpot4doz, laz0rrh4x

3. 206.189.113.189 (New York), 104.248.224.85 (Wilmington), resprectively

4. port 2749

5. They said "we're all set for tomorrow at 1500"

6. They sent a file with the address: https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing
	- file is called update.fpff
	- one of them said they could read the file with the parser that was given out last week

7. They are going to see each other tomorrow

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. Wed Oct 24 20:40:07 2018

2. Author: x4hr0zal

3. Says their are 9 sections, there are really 8 sections I think because when "Section 1" prints out, its just a bunch of random characters. 

4. ------- HEADER -------
MAGIC: 0xdeadbeef
VERSION: 1
TIMESTAMP: 1540428007, READABLE TIME: Wed Oct 24 20:40:07 2018
AUTHOR: x4hr0zal
SECTION COUNT: 9
-------  BODY  -------
SECTION 9
TYPE: SECTION_ASCII
Call this number to get your flag: (422) 537 - 7946
SECTION 8
TYPE: SECTION_WORDS
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
SECTION 7
TYPE: SECTION_COORD
(LATITUDE: -77, LONGITUDE: 38)
SECTION 6
TYPE: SECTION_REFERENCE
1
SECTION 5
TYPE: SECTION_ASCII
The imfamous security pr0s at CMSC389R will never find this!
SECTION 4
TYPE: SECTION_ASCII
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}
SECTION 3
TYPE: SECTION_COORD
(LATITUDE: -76, LONGITUDE: 38)
SECTION 2
TYPE: SECTION_PNG
SECTION 1
TYPE: SECTION_ASCII
AF(saSAdf1AD)Snz**asd1
5. Flags: CMSc389R-{PlaIN_dIfF_FLAG}, CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}
