#!/usr/bin/perl

	require "./chat.pl";	

print "Content-type: text/html\n\n"; 
print qq~

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> 
<html><head><title>$pagetitle</title>
<!-- <META HTTP-EQUIV=Refresh Content="5;URL=$baseurl/chat.list.html"> //-->

<link rel="stylesheet" href="$themesurl/$usertheme/style.css" type="text/css"> 
</head>
<body class="menutable">
<table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%" class="menubackcolor">
<tr>
<td align=center class=cat>
<h1>Chat Room</h1>
<br>
<h3>Rules of the Chat Room</h3></center>
No smoking, drinking, or loud music in the Chat Room.  Now, I mean it
you guys!<P>
<hr>
</td>
</tr>
</table>
</body></html>
~;     