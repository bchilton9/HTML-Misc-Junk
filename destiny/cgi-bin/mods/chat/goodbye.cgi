#!/usr/bin/perl

	require "./chat.pl";	

print "Content-type: text/html\n\n"; 
print qq~<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> 
<html><head>
<title>Good bye!</title>
<link rel="stylesheet" href="$themesurl/$usertheme/style.css" type="text/css"> 
</head>
<body class=menubackcolor onload="top.window.close();">
<CENTER>
Chat Closed<BR>
Please Wate...


<!--
<br>
<br>
You have left the chat room, click <INPUT TYPE="BUTTON" VALUE="Let me back in" ONCLICK="history.go(-1)"> to go back.
<P>Otherwise 
               <input type=button value=\"Click here\" onClick=\"top.window.close();\"> to close this window.
<hr>
-->

</body>
</html>
~;     