#!/usr/bin/perl

	require "./chat.pl";	

#<link rel="stylesheet" href="$themesurl/$usertheme/style.css" type="text/css"> 

print "Content-type: text/html\n\n"; 
print qq~<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> 
     
<html> 
 
<head> 
<meta http-equiv="expires" content="0">  
<meta name="Generator" content="$scriptname $scriptver"> 
<title>$pagetitle</title> 

<frameset rows="0,110" border=0>

 <!-- <frameset cols="80%,*" border=0> //-->

<frame src="$chat_url/chat.rules.cgi" name="listen">

<!--  <frame src="$chat_url/chat.cgi?FA=ShowUsers" name="show"></frameset>//-->

<frame src="$chat_url/chat.cgi?FA=LoginScreen" name="talk" scrolling=no> 

  </frameset>
</head>
<body>
Sorry you need a frame enabled browser to chat.

</body></html>
~;