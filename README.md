# networks
Exercises in UDP/TCP servers and packet analysis using Wireshark.  
Both include server side code and client side code and pcap files with the packets analyzed.
<h3>Exercise 1</h3>
First exercise consists of testing requests and answers on an echo test server and the correlating packets that are being sent.
Also includes a server acting as a DNS query responder, replies with IP addresses to common URLs.
<h3>Exercise 2</h3>
Second exercise builds on it and shows the difference between a UDP based server to a TCP based server and their differences in terms of packets and inner workings.  
Also simulates HTTP requests and handling, providing requested pages if found (using regex to compare to available pages) and handling exceptions otherwise
