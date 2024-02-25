Phising url detector, done with a ML that makes decision based on lexical features and is trained via Random Forest.

Lexical features:

1) IP Address is contained in the URL
2) Abnormal URL (weird hostname)
3) Number of dots in URL
4) Number of WWW in URL
5) Number of @'s in URL
6) Number of directories in URL's file path
7) Number of embeds in URL's file path
8) If the URL is a short link
9) Number of HTTPS in the URL
10) Number of HTTP in the URL
11) Number of % in the URL
12) Number of ? in the URL
13) Number of hyphens in the URL
14) Number of equal signs in the URL
15) URL length
16) Hostname length
17) Contains pre-determined suspicious words
18) First directory's in the file path length
19) Top-Level Domain length
20) Number of digits in URL
21) Number of letters in URL
22) How often the website is accessed