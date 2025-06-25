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

$con = "0";
$val = "0";

$name = $INPUT{'name'};
$pass = $INPUT{'pass'};
$pass2 = $INPUT{'pass2'};
$email = $INPUT{'email'};
$race = $INPUT{'race'};
$class = $INPUT{'class'};

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
	    <A HREF="http://www.erenetwork.com/ravens/cgi/admin.cgi">Login</A> | <A HREF="http://www.erenetwork.com/ravens/cgi/memsign.cgi">Sign Up</A> |
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

#open (DATA, "head.txt");
#@data = <DATA>;
#close DATA;
#foreach $line (@data) {
#print "$line";
#}
if ($name eq "") { 
print "<CENTER><B>You must enter a EQ Name</B></CENTER>";
$con = "1";
}
if ($pass eq "") { 
print "<CENTER><B>You must enter a Password</B></CENTER>";
$con = "1";
}
if ($pass2 eq "") { 
print "<CENTER><B>You Must Re-Type your Password to conferm</B></CENTER>";
$con = "1";
}
if ($email eq "") { 
print "<CENTER><B>You must enter a E-Mail</B></CENTER>";
$con = "1";
}
if ($race eq "") { 
print "<CENTER><B>You must enter a Race</B></CENTER>";
$con = "1";
}
if ($class eq "") { 
print "<CENTER><B>You must enter a class</B></CENTER>";
$con = "1";
}
if ($con eq "1") {
print "<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
}


if ($pass eq $pass2) {

if ($con eq "0") {
if ($pass eq $pass2) {
open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name2) = split(/::/, $line);
if ($name eq $name2) {
$val = "1";
}
}
}
}


if ($con eq "0") {
if ($pass eq $pass2) {
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name2) = split(/::/, $line);
if ($name eq $name2) {
$val = "1";
}
}
} #ifpass
} #ifcon



if ($val eq "1") {
print "<CENTER><B>EQ name allready registered</B></CENTER>";
print "<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
} #ifval

else {


open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
open(DATA, ">wateing.list");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$name\n";
close DATA;

open (DATA, "data/$INPUT{'name'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'name'}");

print DATA "$INPUT{'name'}\n";
print DATA "$INPUT{'pass'}\n";
print DATA "$INPUT{'email'}\n";
print DATA "$INPUT{'race'}\n";
print DATA "$INPUT{'class'}\n";
print DATA "Raven\n";
print DATA "a\n";
print DATA "junk\n";

close DATA;

print "<CENTER><B>Thank you $INPUT{'name'}<BR>";
print "You are now registered<BR>";

open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $INPUT{'email'}\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Registered\n\n";
print MAIL "Welcome To Ravens of Dispair $INPUT{'name'}\n";
print MAIL "You are now in the Ravens Database\n";
print MAIL "You will be added to the members listing\n";
print MAIL "as soon as your membership has been verafied!\n";
print MAIL "If you dont recive an email stateing that you are verafied\n";
print MAIL "Please contact Keny (our Leader) on EverQuest or by E-Mail\n";
print MAIL "at webmaster\@ravensofdispair.com\n\n";
print MAIL "Thank you for becomeing a Raven\n";
print MAIL "The Ravens of Dispair Head Crew!!\n\n\n";
print MAIL "Members Info\:\n";
print MAIL "Eq Name $INPUT{'name'}\n";
print MAIL "Password $INPUT{'pass'}\n";
print MAIL "E-Mail $INPUT{'email'}\n";
print MAIL "Class $INPUT{'class'}\n";
print MAIL "Race $INPUT{'race'}\n";

} # else

}
else {
print "<CENTER><B>Your passwords dident mach</B></CENTER>";
print "<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
} #else



