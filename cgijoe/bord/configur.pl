#!/usr/local/bin/perl
#################################################################
#             Message Board V4.5.1 (Freeware)
#
# This program is distributed as freeware. We are not            	
# responsible for any damages that the program causes	
# to your system. It may be used and modified free of 
# charge, as long as the copyright notice
# in the program that give me credit remain intact.
# If you find any bugs in this program. It would be thankful
# if you can report it to us at cgifactory@cgi-factory.com.  
# However, that email address above is only for bugs reporting. 
# We will not  respond to the messages that are sent to that 
# address. If you have any trouble installing this program. 
# Please feel free to post a message on our CGI Support Forum.
# Selling this script is absolutely forbidden and illegal.
##################################################################
#
#               COPYRIGHT NOTICE:
#
#         Copyright 1999-2001 CGI-Factory.com TM 
#		  A subsidiary of SiliconSoup.com LLC
#
#
#      Web site: http://www.cgi-factory.com
#      E-Mail: cgifactory@cgi-factory.com
#      Released Date: Junuary 13, 2001
#	
#   Message Board V4.5.1 is protected by the copyright 
#   laws and international copyright treaties, as well as other 
#   intellectual property laws and treaties.
###################################################################
#Type in the full system path here if you are using a windows server
$fullpath="./";
####
push(@INC, $fullpath);
#don't change these two vairables unless you know what you are doing
$main_admin="message-admin.pl";
$configur_admin="configur.pl";
##############################
#you may need to change the following variables to full system path if you are using windows servers. 
$mcfg="mcfg.pl";
$mgcfg="mgcfg.pl";
$vcfg="vcfg.pl";
$smtp_mail="smtp_mail.lib";
$version="V 4.51";
#filename for superuser.db
$superuser="superuser.db";
print "Content-type: text/html\n\n";
#import variables. However, use eval to avoid 500 error message 
#when something goes wrong

eval {
require "$mcfg";
require "$vcfg";
require "$mgcfg";
};
if ($@) {
&error("Unable to load $mcfg, $vcfg and $mgcfg. Please check out the readme file. $@");
}
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$request{$name} = $value;
}
#

if ($request{'action'} eq "main_page") {
&main_page;
exit;
}
if ($request{'action'} eq "save") {
&save;
exit;
}

print <<EOF;
<HTML>
<HEAD>
<TITLE>Message Board Freeware $version</TITLE>
</HEAD>
<BODY bgcolor="#ffffff">
<center>
<font face="Arial"><font size="+2">
  Message Board Freeware $version Configurations
</font>
<br>
<br>
Please enter your Super user admin name and password to Login:
<form action="$configur_admin" method="post">
<b>Super User Admin Name:</b> <input type="text" name="admin">&nbsp;&nbsp;
<b>Password:</b> <input type="password" name="password">
<input type="hidden" name="action" value="main_page">
<input type="submit" value="ok">
</form>
</center>
</body>
</html>
EOF
exit;

# main page
sub main_page {
&vpassword;
#open the board data file
open (content, "<$bdata/board1.bd") or @content="";
if ($flock eq "y") {
flock content, 2; 
}
@content=<content>;
close (content);
chomp(@content[3]);
#
print <<EOF;
<html>
<head>
  <title>Message Board Freeware $version Configurations</title>
</head>
<body bgcolor="#ffffff">
<table border="0" bgcolor="#000000" cellspacing="1" cellpadding="0">
  <form action="$configur_admin" method="POST">
  <tr bgcolor="#7CA3DE">
    <td>
	  <font size="3" face="arial" color="#ffffff">
        <b>Message Board Freeware $version Configurations</b>
      </font>
    </td>
  </tr>
  <tr bgcolor="#999999">
    <td>
	  <font size="2" face="arial" color="#f0f0f0">
		<b>Settings that are shared by both view.pl and message.pl</b>
	  </font>
	</td>
  </tr>
  
<!-- Beign WWW Paths ---------------------------------------------------------->
  
  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#f0f0f0">
		<b>WWW Paths: preceeded by http:// and ended with item listed</b>
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    (i.e. cookie.js: http://www.yourdomain.com/cgi-bin/amb4_5/cookie.js)
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">
	    <tr bgcolor="#ffffff">
		  <td width="100%">
			<b>&nbsp;Website Domain Name</b>
		  </td>
		  <td>
		    <input type="Text" name="domain" value="$domain" size="60">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
  		    <b>&nbsp;message.pl</b>
		  </td>
		  <td>
		    <input type="Text" name="cgi" value="$cgi" size="60">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
			<b>&nbsp;view.pl</b>
		  </td>
		  <td>
		    <input type="Text" name="cgi2" value="$cgi2" size="60">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
			<b>&nbsp;Default Icon Image</b>
		  </td>
		  <td>
		    <input type="Text" name="default_icon" value="$default_icon" size="60">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
			<b>&nbsp;Email Icon Image</b>
		  </td>
		  <td>
		    <input type="Text" name="email_icon" value="$email_icon" size="60">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
			<b>&nbsp;Cookie.js</b>
		  </td>
		  <td>
		    <input type="Text" name="cookie_js" value="$cookie_js" size="60">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>
  
<!-- End WWW Paths ------------------------------------------------------------>
<!-- Begin Full System Paths -------------------------------------------------->  
  
  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Full system paths to directories for data files: no back slash at the end</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    It is suggested that you create the directories below in a location that your visitors do not have access to
	    If your visitors can read the contents inside your cgi-bin, try to create the directories under wwwroot.
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;Message Boards</b>
		  </td>
		  <td>
		    <input type="Text" name="bdata" value="$bdata" size="60">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;Logged IP Records and Flood Control Info</b>
		  </td>
		  <td>
		    <input type="Text" name="misc" value="$misc" size="60">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Full System Paths ---------------------------------------------------->
<!-- Begin Mail Settings ------------------------------------------------------>

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Email Settings</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp;
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;Sending mail options: 0: sendmail 1: SMTP</b>
		  </td>
		  <td>
		    <input type="Text" name="mail_option" value="$mail_option" size="30" maxlength="1">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>
			  &nbsp;The full system path to the mail program<br>
			  &nbsp;(sendmail) or the smtp server(SMTP)<br>
			  &nbsp;(add <font color="red">-t</font> or remove <font color="red">-t</font> for sendmail path if it causes any error)
			</b>
		  </td>
		  <td>
		    <input type="Text" name="mailprog" value="$mailprog" size="30">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;Your email address: NO back slash in front of the symbol @</b>
		  </td>
		  <td>
		    <input type="Text" name="yourmail" value="$yourmail" size="30">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Mail Settings -------------------------------------------------------->
<!-- Begin Date --------------------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Date Formatting</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    Date Format options [ 1: Long Format, 2: dd/mm/year, 3: mm/dd/year ] 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;Time Format (1-3)</b>
		  </td>
		  <td>
		    <input type="Text" name="date_format" value="$date_format" size="3" maxlength="1">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;Time Difference (hours or -hours)</b>
		  </td>
		  <td>
		    <input type="Text" name="time_differ" value="$time_differ" size="3" maxlength="3">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Date ----------------------------------------------------------------->
<!-- Begin General Formatting ------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>General Formatting</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp; 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;Text color for the page spliting links, post box, and reply box</b>
		  </td>
		  <td>
		    <input type="Text" name="other_color" value="$other_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;Font face for the entire message board</b>
		  </td>
		  <td>
		    <input type="Text" name="font_face" value="$font_face" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;Font size for the entire message board system</b>
		  </td>
		  <td>
		    <input type="Text" name="font_size" value="$font_size" size="10">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End General Formatting --------------------------------------------------->
<!-- Begin Options Yes/No ----------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Options (Yes/No)</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    Lower-case Only: Enter y for yes and n for no
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;Allow visitors to store their username and password in cookies</b> 
		  </td>
		  <td>
		    <input type="Text" name="username_cookie" value="$username_cookie" size="1">
		  </td>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;Reply Email notification for the visitors</b> 
		  </td>
		  <td>
		    <input type="Text" name="replymail" value="$replymail" size="1">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;File locking. Don't set it to "n" unless your system really have trouble using flock. Turn it off at your own risk.</b> 
		  </td>
		  <td>
		    <input type="Text" name="flock" value="$flock" size="1">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>
			  &nbsp;Send an alert mail to yourself when someone trys to gain access to the admin script with an incorrect login.<br>
			  &nbsp;This feature will only work with sendmail. However, login errors will still be logged in errorlog.txt
	        </b>
		  </td>
		  <td>
		    <input type="Text" name="alert" value="$alert" size="1">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Options Yes/No ------------------------------------------------------->
<!-- Begin Misc --------------------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Misc</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp; 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;File extension for created messages. (i.e. shtml , htm, or html)</b>
		  </td>
		  <td>
		    <input type="Text" name="file_ending" value="$file_ending" size="30">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;Title for unregistered members</b>
		  </td>
		  <td>
		    <input type="Text" name="member_title" value="$member_title" size="30">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Misc ----------------------------------------------------------------->
  <tr bgcolor="#999999">
    <td>
	  <font size="2" face="arial" color="#f0f0f0">
		<b>Settings that are used view.pl</b>
	  </font>
	</td>
  </tr>
  
 
<!-- Beign WWW Paths (view.pl)---------------------------------------------------------->
  
  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#f0f0f0">
		<b>WWW Paths: preceeded by http:// and ended with item listed</b>
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    (i.e. cookie.js: http://www.yourdomain.com/cgi-bin/amb4_5/cookie.js)
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">
	    <tr bgcolor="#ffffff">
		  <td width="100%">
			<b>&nbsp;The WWW Path to the new topic icon image</b>
		  </td>
		  <td>
		    <input type="Text" name="new_icon" value="$new_icon" size="60">
		  </td>
		</tr>

	  </table>
	</td>
  </tr>
  
<!-- End WWW Paths (view.pl)------------------------------------------------------------> 
<!-- Begin General Formatting (view.pl)------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>General Formatting</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp; 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The color of entire board border</b>
		  </td>
		  <td>
		    <input type="Text" name="table_background_color" value="$table_background_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The color of lines between subject cells</b>
		  </td>
		  <td>
		    <input type="Text" name="inner_table_background_color" value="$inner_table_background_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;The color of the board title bar</b>
		  </td>
		  <td>
		    <input type="Text" name="title_bar_color" value="$title_bar_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The color of the board title bar text</b>
		  </td>
		  <td>
		    <input type="Text" name="title_bar_text_color" value="$title_bar_text_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The color of the column title bar</b>
		  </td>
		  <td>
		    <input type="Text" name="column_title_color" value="$column_title_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The color of the column title bar text</b>
		  </td>
		  <td>
		    <input type="Text" name="column_title_text_color" value="$column_title_text_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The first color choice for each field</b>
		  </td>
		  <td>
		    <input type="Text" name="color1" value="$color1" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The second color choice for each field</b>
		  </td>
		  <td>
		    <input type="Text" name="color2" value="$color2" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The color of the text in each field </b>
		  </td>
		  <td>
		    <input type="Text" name="font_color" value="$font_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The width of the messages index table </b>
		  </td>
		  <td>
		    <input type="Text" name="table_width" value="$table_width" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The width of the "from" field</b>
		  </td>
		  <td>
		    <input type="Text" name="from_width" value="$from_width" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The width of the "last post" field</b>
		  </td>
		  <td>
		    <input type="Text" name="post_width" value="$post_width" size="10">
		  </td>
		</tr>
		
	  </table>
	</td>
  </tr>

<!-- End General Formatting (view.pl)--------------------------------------------------->
<!-- Begin Options Yes/No (view.pl)----------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Options (Yes/No)</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    Lower-case Only: Enter y for yes and n for no
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;Use cookie to track new messages since a visitor's last visit?</b>
		  </td>
		  <td>
		    <input type="Text" name="use_cookie" value="$use_cookie" size="1">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Options Yes/No (view.pl) ------------------------------------------------------->
<!-- Begin Misc (view.pl)--------------------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Misc</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp; 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;Time period for the cookie on the visitor's computer to be reset</b>
		  </td>
		  <td>
		    <input type="Text" name="reset_cookie" value="$reset_cookie" size="30">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The default time period for displaying messages. (Minimum: <b>1</b>. Maximum: 90. all = display all messages)</b>
		  </td>
		  <td>
		    <input type="Text" name="time_period" value="$time_period" size="30">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;Max number of messages per page to be listed by view.pl </b>
		  </td>
		  <td>
		    <input type="Text" name="max" value="$max" size="30">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Misc (view.pl)----------------------------------------------------------------->

  <tr bgcolor="#999999">
    <td>
	  <font size="2" face="arial" color="#f0f0f0">
		<b>Settings that are used message.pl</b>
	  </font>
	</td>
  </tr>
  
<!-- Begin General Formatting (message.pl)------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>General Formatting</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp; 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The color of entire board border</b>
		  </td>
		  <td>
		    <input type="Text" name="mtable_background_color" value="$mtable_background_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The color of lines between subject cells</b>
		  </td>
		  <td>
		    <input type="Text" name="minner_table_background_color" value="$minner_table_background_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;The color of the board title bar</b>
		  </td>
		  <td>
		    <input type="Text" name="mtitle_bar_color" value="$mtitle_bar_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The color of the board title bar text</b>
		  </td>
		  <td>
		    <input type="Text" name="mtitle_bar_text_color" value="$mtitle_bar_text_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The first color choice for each field</b>
		  </td>
		  <td>
		    <input type="Text" name="mcolor1" value="$mcolor1" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The second color choice for each field</b>
		  </td>
		  <td>
		    <input type="Text" name="mcolor2" value="$mcolor2" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The color of the text in each field </b>
		  </td>
		  <td>
		    <input type="Text" name="mfont_color" value="$mfont_color" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The color of the column title bar for posted messages</b>
		  </td>
		  <td>
		    <input type="Text" name="mbar" value="$mbar" size="10">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;The color of the column text in the title bar for posted messages</b>
		  </td>
		  <td>
		    <input type="Text" name="mbar_text" value="$mbar_text" size="10">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td width="100%">
		    <b>&nbsp;The width of messages </b>
		  </td>
		  <td>
		    <input type="Text" name="message_width" value="$message_width" size="10">
		  </td>
		</tr>
		
	  </table>
	</td>
  </tr>

<!-- End General Formatting (message.pl)--------------------------------------------------->
<!-- Begin Options Yes/No (message.pl)----------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Options (Yes/No)</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    Lower-case Only: Enter y for yes and n for no
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	

		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;Allow html tags when a visitor posts a message?</b> 
		  </td>
		  <td>
		    <input type="Text" name="html" value="$html" size="1">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;Name field required?</b>
		  </td>
		  <td>
		    <input type="Text" name="require_name" value="$require_name" size="1">
		  </td>
		</tr>
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;Subject field required?</b> 
		  </td>
		  <td>
		    <input type="Text" name="require_subject" value="$require_subject" size="1">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td>
		    <b>&nbsp;Email field required?</b>
		  </td>
		  <td>
		    <input type="Text" name="require_email" value="$require_email" size="1">
		  </td>
		</tr>
		</table>
	</td>
  </tr>

<!-- End Options Yes/No (message.pl) ------------------------------------------------------->
<!-- Begin Misc (message.pl)--------------------------------------------------------------->

  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Misc</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp; 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
		<tr bgcolor="#ffffff">
		  <td>
		    <b>&nbsp;The name of your web site</b>
		  </td>
		  <td>
		    <input type="Text" name="sitetitle" value="$sitetitle" size="30">
		  </td>
		</tr>
		<tr bgcolor="#f0f0ff">
		  <td width="100%">
		    <b>&nbsp;Max number of reply messages allowed on each post (0=no limit)</b>
		  </td>
		  <td>
		    <input type="Text" name="max_reply" value="$max_reply" size="30">
		  </td>
		</tr>
	  </table>
	</td>
  </tr>

<!-- End Misc (message.pl)----------------------------------------------------------------->

 
<!-- begin board configuration----------------------------------------------------------------->
  <tr bgcolor="#000090">
    <td>
	  <font size="2" face="arial" color="#ffffff">
		<b>Board Configuration</b> 
	  </font>
	</td>
  </tr>
  <tr bgcolor="#f0f0ff">
    <td>
	  <font size="1" face="arial" color="#000000">
	    &nbsp; 
	  </font>
	</td>
  </tr>
  <tr>
    <td>
	  <table border="0" bgcolor="#cccccc" cellspacing="1" cellpadding="1" width="100%">	
	  		 <form action="$configur_admin" method="post">
	 		 <tr bgcolor="#ffffff"><td>Name or title of the Message Board</td><td><input type="text" name="forum_name" value="@content[2]"></td></tr>
			 <tr bgcolor="#f0f0ff"><td>Full System path the the message directory</td><td><input type="text" name="full" value="@content[0]"></td></tr>
			 <tr bgcolor="#ffffff"><td>WWW path the the message directory</td><td><input type="text" name="www" value="@content[1]"></td></tr>
			 <tr bgcolor="#f0f0ff"><td>Public Board? (This variable is used in Advanced Message Board V4.5x)</td><td><input type=\"text\" name=\"vis\" value=\"@content[3]\" size="1">1=Yes (public board).2=No(private board)</td></tr>
     		 <tr bgcolor="#ffffff"><td>Board mode (1=opened: accepts new messages; 2=closed: does not accept any new message): </td><td><input type=\"text\" name=\"mode\" value=\"@content[4]\" size="1"></td></tr>
	  	 		  <input type="hidden" name="admin" value="$request{'admin'}">
			      <input type="hidden" name="password" value="$request{'password'}">
	 		      <input type="hidden" name="paction" value="main_one">
			      <input type="hidden" name="nick" value="$request{'board'}">
	 			  <input type="hidden" name="action" value="modify_con">  
	  		 </table>
 
      </td>
</tr>
<!-- end board configuration----------------------------------------------------------------->

  <tr bgcolor="#7CA3DE">
    <td>
	<table border="0">
	  <tr>
	    <td>
			<input type="hidden" name="admin" value="$request{'admin'}"><input type="hidden" name="password" value="$request{'password'}">
				  <input type="hidden" name="action" value="save"><input type="submit" value="Modify">
        
		</td>
		</form>
		<td>
		&nbsp;
     		</td>
	  </tr>
	  </table>
	</td>
  </tr>
</table>
</td>
</tr>
</table>
</body>
</html>

EOF
exit;
}
####### save change

sub save {
&vpassword;	
$request{'yourmail'}=~ s/@/\\@/g;
open (main, ">$fullpath/$mcfg") or &error("Unable to write to $mcfg. Please make sure you have chmoded it to \"755\"(chmod it to \"777\" if it still doesn't work)");
if ($flock==1) {
flock main, 2; 
} 
print main "\$domain=\"$request{'domain'}\"\;\n";
print main "\$bdata=\"$request{'bdata'}\"\;\n";
print main "\$mdata=\"$request{'mdata'}\"\;\n";
print main "\$misc=\"$request{'misc'}\"\;\n";
print main "\$member_title=\"$request{'member_title'}\"\;\n";
print main "\$cgi=\"$request{'cgi'}\"\;\n";
print main "\$cgi2=\"$request{'cgi2'}\"\;\n";
print main "\$search=\"$request{'search'}\"\;\n";
print main "\$register_cgi=\"$request{'register_cgi'}\"\;\n";
print main "\$account_cgi=\"$request{'account_cgi'}\"\;\n";
print main "\$directory_cgi=\"$request{'directory_cgi'}\"\;\n";
print main "\$lookup_cgi=\"$request{'lookup_cgi'}\"\;\n";
print main "\$ip_cgi=\"$request{'ip_cgi'}\"\;\n";
print main "\$subadmin_cgi=\"$request{'subadmin_cgi'}\"\;\n";
print main "\$user_lookup=\"$request{'user_lookup'}\"\;\n";
print main "\$record_user_post=\"$request{'record_user_post'}\"\;\n";
print main "\$file_ending=\"$request{'file_ending'}\"\;\n";
print main "\$default_icon=\"$request{'default_icon'}\"\;\n";
print main "\$email_icon=\"$request{'email_icon'}\"\;\n";
print main "\$profile_icon=\"$request{'profile_icon'}\"\;\n";
print main "\$date_format=\"$request{'date_format'}\"\;\n";
print main "\$time_differ=\"$request{'time_differ'}\"\;\n";
print main "\$btitle=\"$request{'btitle'}\"\;\n";
print main "\$other_color=\"$request{'other_color'}\"\;\n";
print main "\$font_face=\"$request{'font_face'}\"\;\n";
print main "\$font_size=\"$request{'font_size'}\"\;\n";
print main "\$flock=\"$request{'flock'}\"\;\n";
print main "\$alert=\"$request{'alert'}\"\;\n";
print main "\$yourmail=\"$request{'yourmail'}\"\;\n";
print main "\$mail_option=\"$request{'mail_option'}\"\;\n";
print main "\$mailprog=\"$request{'mailprog'}\"\;\n";
print main "\$replymail=\"$request{'replymail'}\"\;\n";
print main "\$opticon=\"$request{'opticon'}\"\;\n";
print main "\$username_cookie=\"$request{'username_cookie'}\"\;\n";
print main "\$cookie_js=\"$request{'cookie_js'}\"\;\n";
print main "1\;\n";

close(main);

open (view, ">$fullpath/$vcfg") or &error("Unable to write to $vcfg. Please make sure you have chmoded it to \"755\"(chmod it to \"777\" if it still doesn't work)");
if ($flock==1) {
flock view, 2; 
} 
print view "\$use_cookie=\"$request{'use_cookie'}\"\;\n";
print view "\$new_icon=\"$request{'new_icon'}\"\;\n";
print view "\$reset_cookie=\"$request{'reset_cookie'}\"\;\n";
print view "\$sort_it=\"$request{'sort_it'}\"\;\n";
print view "\$time_period=\"$request{'time_period'}\"\;\n";
print view "\$max=\"$request{'max'}\"\;\n";
print view "\$time_select=\"$request{'time_select'}\"\;\n";
print view "\$custom_day=\"$request{'custom_day'}\"\;\n";
print view "\$a_search=\"$request{'a_search'}\"\;\n";
print view "\$table_background_color=\"$request{'table_background_color'}\"\;\n";
print view "\$inner_table_background_color=\"$request{'inner_table_background_color'}\"\;\n";
print view "\$title_bar_color=\"$request{'title_bar_color'}\"\;\n";
print view "\$title_bar_text_color=\"$request{'title_bar_text_color'}\"\;\n";
print view "\$column_title_color=\"$request{'column_title_color'}\"\;\n";
print view "\$column_title_text_color=\"$request{'column_title_text_color'}\"\;\n";
print view "\$color1=\"$request{'color1'}\"\;\n";
print view "\$color2=\"$request{'color2'}\"\;\n";
print view "\$font_color=\"$request{'font_color'}\"\;\n";
print view "\$table_width=\"$request{'table_width'}\"\;\n";
print view "\$from_width=\"$request{'from_width'}\"\;\n";
print view "\$post_width=\"$request{'post_width'}\"\;\n";
print view "1\;\n";
close(view);

open (message, ">$fullpath/$mgcfg") or &error("Unable to write to $mgcfg. Please make sure you have chmoded it to \"755\"(chmod it to \"777\" if it still doesn't work)");
if ($flock==1) {
flock message, 2; 
} 
print message "\$flood_control=\"$request{'flood_control'}\"\;\n";
print message "\$flood_control2=\"$request{'flood_control2'}\"\;\n";
print message "\$flood_time=\"$request{'flood_time'}\"\;\n";
print message "\$sitetitle=\"$request{'sitetitle'}\"\;\n";
print message "\$max_reply=\"$request{'max_reply'}\"\;\n";
print message "\$html=\"$request{'html'}\"\;\n";
print message "\$require_name=\"$request{'require_name'}\"\;\n";
print message "\$require_subject=\"$request{'require_subject'}\"\;\n";
print message "\$require_email=\"$request{'require_email'}\"\;\n";
print message "\$filter=\"$request{'filter'}\"\;\n";
print message "\$mcolor1=\"$request{'mcolor1'}\"\;\n";
print message "\$mcolor2=\"$request{'mcolor2'}\"\;\n";
print message "\$mfont_color=\"$request{'mfont_color'}\"\;\n";
print message "\$mbar=\"$request{'mbar'}\"\;\n";
print message "\$mbar_text=\"$request{'mbar_text'}\"\;\n";
print message "\$message_width=\"$request{'message_width'}\"\;\n";
print message "\$mtitle_bar_color=\"$request{'mtitle_bar_color'}\"\;\n";
print message "\$mtitle_bar_text_color=\"$request{'mtitle_bar_text_color'}\"\;\n";
print message "\$mtable_background_color=\"$request{'mtable_background_color'}\"\;\n";
print message "\$minner_table_background_color=\"$request{'minner_table_background_color'}\"\;\n";
print message "1\;\n";
close(message);

open (board, ">$request{'bdata'}/board1.bd") or &error("Unable to write to board1.bd in the data directory.");
print board "$request{'full'}\n";
print board "$request{'www'}\n";
print board "$request{'forum_name'}\n";
print board "$request{'vis'}\n";
print board "$request{'mode'}\n";
close (board);
	
print "The new configuration has been saved. If anything doesn't work out, you can run $configur_admin again to change the setting again. However, if $configur_admin fails to loads itself, you will just have to reupload mcfg.pl, mgcfg.pl, and vcfg.pl.\n";
print "<br><br><font size=\"-1\"><b>Warning: Please close your browser if you want to log off.</b><br>";
print "Copyright 1999-2001 CGI-Factory.com of SiliconSoup.com LLC</font>";
exit;
}	
###### password

sub vpassword{
if (!$ENV{'REMOTE_HOST'}) {
$IP=$ENV{'REMOTE_ADDR'};
}
else {
$IP=$ENV{'REMOTE_HOST'};
}
open (pass, "<$fullpath/$superuser") or &error("Unable to open the admin data.");
if ($flock==1) {
flock pass, 2; 
}
$pass=<pass>;
close(pass);

$compare=$request{'admin'};
$compare=~ tr/A-Z/a-z/;
$compare=~ s/\s//;
chomp($pass);
@check=split(/\|/, $pass);
if ($compare eq "@check[0]" and $compare == "@check[0]") {
$ok=1;
$request{'password'}=~ tr/A-Z/a-z/;
$password=crypt("$request{'password'}", YL);
unless ($password eq "@check[1]") {
&wrong;
}
}
unless ($ok==1) {
&wrong;	
}
}	

sub wrong {
$timenow=localtime();
print "<h2>Incorrect login</h2>";
print "The password you entered is incorrect.<br>";
print "The following information has been sent to the webmaster of the web site for security reasons.<br>";
print "<ul>Your IP Address: $IP</ul>";
print "<ul>Admin Name you tried: $request{'admin'}</ul>";
print "<ul>Password your entered: $request{'password'}</ul>";
print "<ul>Time: $timenow</ul>";

open (errorlog, ">>$fullpath/errorlog.txt") or &error("unable to write to errorlog.txt"); #log the incorrect login
if ($flock eq "y") {
flock errorlog, 2; 
}
print errorlog "IP: $IP| admin: $request{'admin'}| pass: $request{'password'}| time: $timenow\n";
close (errorlog);

if ($alert eq "y") {
open (MAIL, "|$mailprog") or &error("Unable to open the mail program");
print MAIL "To: $yourmail\n";
print MAIL "From: $yourmail\n";
print MAIL "Subject: bad password\n";
print MAIL "someone entered the wrong password for entering the admin script.\n";
print MAIL "Here is information:\n\n";
print MAIL "IP Address: $IP\n";
print MAIL "Admin Name: $request{'admin'}\n";
print MAIL "Password: $request{'password'}\n";
print MAIL "$timenow\n";
close(MAIL);
}
exit;	
}	

#####error
sub error {
print "<h2>An error has occured</h2> The error is $_[0]<br>\n";	
print "$!\n<br><br>";
print "If the error message is \"No such file or directory,\" please make sure the system path your are using is correct.<br>\n";
print "Also, you need to make sure you have uploaded the file or created the directory as it explains in the read me file.<br><br>\n";	
print "If the error message is \"permission denied,\" please make sure you have chmoded the file as it explains in the read me file.<br>\n";	
exit;	
}
 
	
	
	

