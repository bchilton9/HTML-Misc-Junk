#!/usr/bin/perl


  read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
  if (length($buffer) < 5) {
    $buffer = $ENV{QUERY_STRING};
  }
 
  @pairs = split(/&/, $buffer);
  foreach $pair (@pairs) {
    ($name, $value) = split(/=/, $pair);

    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $value =~ s/[\;\|\\ ]/ /ig;
    $INPUT{$name} = $value;
}


print "Content-type: text/html\n\n";
print <<"HTML";
<HTML>
<HEAD>
  <!-- Created with AOLpress/2.0 -->
  <TITLE>Ravens Of Dispair</TITLE>
</HEAD>
<BODY BGCOLOR="#000000" TEXT="#ffffff" LINK="#ffffff" VLINK="#ffffff">
<TABLE BORDER=2 CELLSPACING="1" WIDTH=100% BORDERCOLOR=blue>
  <TR>
    <TD><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR VALIGN="Top">
	  <TD ROWSPAN=2><IMG SRC="http://www.erenetwork.com/ravens/header.gif" WIDTH="451"
		HEIGHT="135"></TD>
	  <TD WIDTH=70% BGCOLOR="#ffffff"><FORM ACTION="admin.cgi" METHOD=POST>
	      <P ALIGN=Right>
	      <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
		<TR>
		  <TD><FONT COLOR="#000000"><B>Name.</B></FONT></TD>
		  <TD>
		    <INPUT TYPE="text" NAME="name" SIZE="10"></TD>
		</TR>
		<TR>
		  <TD><FONT COLOR="#000000"><B>Pass.</B></FONT></TD>
		  <TD>
		    <INPUT TYPE="password" NAME="password" SIZE="10"></TD>
		</TR>
		<TR>
		  <TD><FONT COLOR="#000000"><B>Members</B> </FONT>
		    <INPUT TYPE=hidden NAME=a value=login></TD>
		  <TD><P ALIGN=Right>
		    <INPUT TYPE=submit VALUE=LogOn></TD>
		</TR>
	      </TABLE>
	    </FORM>
	  </TD>
	  <TD BGCOLOR="#ffffff"><IMG SRC="http://www.erenetwork.com/ravens/spacer.gif"
		WIDTH="19" HEIGHT="93"></TD>
	</TR>
	<TR>
	  <TD BGCOLOR="#0008AD"><P ALIGN=Right>
	    <A HREF="http://www.erenetwork.com/ravens/cgi/admin.cgi">Login</A> | <A HREF="http://www.erenetwork.com/ravens">Sign Up</A> |
	    <A HREF="mailto:webmaster@erenetwork.com">E-Mail</A></TD>
	  <TD BGCOLOR="#0008AD"><IMG SRC="http://www.erenetwork.com/ravens/spacer2.gif"
		WIDTH="19" HEIGHT="41"></TD>
	</TR>
	<TR>
	  <TD COLSPAN=3><TABLE BORDER BORDERCOLOR=#0008ad CELLPADDING="2" WIDTH=100%>
	      <TR>
		<TD WIDTH=15%><IMG SRC="http://www.erenetwork.com/ravens/dragons of Elfwood.gif"
		      WIDTH="161" HEIGHT="450"></TD>
		<TD VALIGN="Top"><P ALIGN=Center>
		  <!-- start main content -->
HTML
print "<CENTER><BIG><B>Leaders</B></BIG><BR><CENTER><TABLE BORDER BORDERCOLOR=0000ff CELLPADDING=2 ALIGN=Center WIDTH=450><TR>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Name</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Race</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Class</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Rank</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=0000ff>b</FONT></TD>\n";
print "</TR>\n";
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "Head-Leader") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "1st-Leader") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "2nd-Leader") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "3rd-Leader") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "4th-Leader") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "5th-Leader") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
print "</TABLE></CENTER>";
print "<CENTER><BIG><B>Leaders</B></BIG><BR><CENTER><TABLE BORDER BORDERCOLOR=0000ff CELLPADDING=2 ALIGN=Center WIDTH=450><TR>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Name</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Race</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Class</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Rank</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=0000ff>R</FONT></TD>\n";
print "</TR>\n";
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "Oscar") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
print "</TABLE></CENTER>";
print "<CENTER><BIG><B>Leaders</B></BIG><BR><CENTER><TABLE BORDER BORDERCOLOR=0000ff CELLPADDING=2 ALIGN=Center WIDTH=450><TR>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Name</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Race</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Class</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Rank</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=0000ff>R</FONT></TD>\n";
print "</TR>\n";
#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($rank eq "Raven") {
print "<TR>\n";
print "<TD><B>$usr</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr TARGET=\_new>Message</A></TD>\n";
print "</TR>\n";
}
}
####################################
print "</TABLE></CENTER>";