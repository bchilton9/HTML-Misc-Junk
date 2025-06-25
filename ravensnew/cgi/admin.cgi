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

if ($INPUT{'a'} eq "login") { &login; }
elsif ($INPUT{'a'} eq "Aprove") { &aprove }
elsif ($INPUT{'a'} eq "Delete") { &delete }
elsif ($INPUT{'a'} eq "email") { &email }
elsif ($INPUT{'a'} eq "SendEmail") { &semail }
elsif ($INPUT{'a'} eq "list") { &list }
elsif ($INPUT{'a'} eq "Edit") { &edit }
elsif ($INPUT{'a'} eq "update") { &update }
elsif ($INPUT{'a'} eq "news") { &news }
elsif ($INPUT{'a'} eq "Update News") { &upnews }
else { &form; }

sub form {
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
	  <TD WIDTH=70% BGCOLOR="#ffffff"><FORM METHOD=POST>
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
	    <A HREF="http://www.erenetwork.com/ravens/cgi/admin.cgi">Login</A> | <A HREF="../index.html">Sign Up</A> |
	    <A HREF="mailto:webmaster@erenetwork.com">E-Mail</A> |
	    <A HREF="http://www.ravensofdispair.com/cgi/memlist.cgi">Member List</A></TD>
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
<BR><P>
<FORM METHOD=POST><CENTER>
<TABLE BORDER CELLPADDING=2 ALIGN=Center BORDERCOLOR=blue>
<TR>
<TD>Name</TD><TD>
<INPUT TYPE=text NAME=name></TD>
</TR><TR><TD>Password</TD><TD>
<INPUT TYPE=text NAME=password></TD>
</TR><TR><TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=a value=login>
<INPUT TYPE=submit></TD></TR>
</TABLE></CENTER></FORM>

<!-- end main content --></TD>
	      </TR>
	    </TABLE>
	  </TD>
	</TR>
      </TABLE>
    </TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

sub login {
open (FILE, "data/$INPUT{'name'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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

if ($name eq "") { print "<CENTER><B>Username error!!"; }

else { 
if ($INPUT{'password'} eq "$cryptpass") { &start }
else { print "<CENTER><B><B>Password error!!"; }
}


}



sub start{
open (FILE, "data/$INPUT{'name'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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


print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Ravens Of Dispair</TITLE>
</HEAD>
<BODY BGCOLOR="#000000" TEXT="#ffffff" LINK="#ffffff" VLINK="#ffffff">
<TABLE BORDER=2 CELLSPACING="1" WIDTH=100% BORDERCOLOR=blue>
  <TR>
    <TD><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR VALIGN="Top">
	  <TD ROWSPAN=2><IMG SRC="http://www.erenetwork.com/ravens/header.gif" WIDTH="451"
		HEIGHT="135"></TD>
	  <TD WIDTH=70% BGCOLOR="#ffffff">
	      <P ALIGN=Right>
<FONT COLOR=#000000><B>Hello
HTML
print " $INPUT{'name'}<BR></FONT>";

$count = "0";
open (DATA, "msg/dat/$INPUT{'name'}.msg");
@data = <DATA>;
foreach $line (@data) {
$count++;
}
close DATA;
if ($count eq "0") {
print "<FONT COLOR=000000><B><SMALL>You Have No Messages</SMALL></B></FONT>\n";
}
else {
print "<A HREF=http://www.erenetwork.com/ravens/cgi/msg/msg.cgi?a=list&name=$INPUT{'name'} TARGET=_new>\n";
print "<FONT COLOR=000000><B><SMALL>You have $count Messages</SMALL></B></FONT></A>\n";
}

print <<"HTML";
	  </TD>
	  <TD BGCOLOR="#ffffff"><IMG SRC="http://www.erenetwork.com/ravens/spacer.gif"
		WIDTH="19" HEIGHT="93"></TD>
	</TR>
	<TR>
	  <TD BGCOLOR="#0008AD"><P ALIGN=Right><A HREF=admin.cgi?a=login&name=$INPUT{'name'}&password=$INPUT{'password'}>Main Page</A> |
	    <A HREF="http://www.erenetwork.com/ravens/cgi/memlist.cgi?name=$INPUT{'name'}">Member List</A></TD>
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
<BR><P><CENTER>
<IMG SRC=turn.gif><BR>
HTML
##################TOURNAMENT START
$turnnum = "0";
open (DATA, "turn.txt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($name2) = split(/::/, $line);
if ($INPUT{'name'} eq "$name2") {
$turnnum = "1";
}
}

if ($turnnum eq "1") {
print <<"HTML";
<B>You are Signed up for the turnament!!</B><BR>
HTML
}
else {
print <<"HTML";
<B>You are not signed up for the turnament!!</B><BR>
<A HREF=http://www.erenetwork.com/ravens/cgi/turn.cgi?name=$INPUT{'name'}&password=$INPUT{'password'}>Click Here to sign up</A><BR>
HTML
}



print <<"HTML";
<A HREF="http://www.erenetwork.com/ravens/cgi/tinfo.cgi" target="_new">Info on the tournament</A><BR>
<P>
<TEXTAREA NAME="News" ROWS="15" COLS="60">
HTML
#####################TOURNAMENT END

open (DATA, "news.dat");
@data = <DATA>;
close DATA;

print "@data";


print <<"HTML";
</TEXTAREA>
HTML


############### ADMIN
if ($acc eq "b") { &admin }
if ($acc eq "c") { &admin }


sub admin {
print <<"HTML";
<BR>
<P>
<CENTER>
To Be aproved!
  <TABLE BORDER CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Name</TD>
      <TD>EMail</TD>
      <TD>Race</TD>
      <TD>Class</TD>
      <TD>Rank</TD>
      <TD>Aprove</TD>
      <TD>Delete</TD>
      <TD>Edit</TD>
    </TR>
HTML

open (DATA, "wateing.list");
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


print <<"HTML";
<BODY>
HTML

print "<FORM METHOD=POST><INPUT TYPE=hidden VALUE=$INPUT{'name'} NAME=name>
<INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password><TR><TD>$usr
<INPUT TYPE=hidden VALUE=$usr NAME=usr></TD>\n";
print "<TD>$email</TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>Raven</TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Aprove NAME=a></TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Delete NAME=a></TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Edit NAME=a></TD></TR></FORM>\n";


}
print "</TABLE></CENTER>\n";
print <<"HTML";
<CENTER>
<P>
<BR>
<A HREF="admin.cgi?a=email&name=$INPUT{'name'}&password=$INPUT{'password'}">E-Mail Members</A>
<P>
<A HREF="admin.cgi?a=list&name=$INPUT{'name'}&password=$INPUT{'password'}">List All Members</A>
<P>
<A HREF="admin.cgi?a=news&name=$INPUT{'name'}&password=$INPUT{'password'}">Update News</A>
HTML

}
}




sub aprove {
print "<CENTER>Adding user to members listing...<BR>";
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
open(DATA, ">data/members.data");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'usr'}\n";
close DATA;

print "Sending user Welcome Email...<BR>";
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $INPUT{'email'}\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Aproved\n\n";
print MAIL "You have been aproved!\n";
print MAIL "Your name will now apear\n";
print MAIL "on the Ravens members list\n";
print MAIL "And you will now have acses to the ravens Members page!\n";
print MAIL "www.ravensofdispair.com\n";

print "Deleteing user from wateing list...<BR>";
open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
open(DATA, ">wateing.list");
foreach $line (@data) {
chomp ($line);
($usr, $pass, $email, $race, $class, $rank) = split(/::/, $line);
if ($usr eq "$INPUT{'usr'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}
print "Finished addeding $INPUT{'usr'}";
}





sub delete {

print "<CENTER>Deleteing user from wateing list..<BR>";
open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
open(DATA, ">wateing.list");
foreach $line (@data) {
chomp ($line);
($usr, $pass, $email, $race, $class, $rank) = split(/::/, $line);
if ($usr eq "$INPUT{'usr'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}


print "Deleteing user from member list...<BR>";
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
open(DATA, ">data/members.data");
foreach $line (@data) {
chomp ($line);
($usr) = split(/::/, $line);
if ($usr eq "$INPUT{'usr'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}


print "Eraceing users data file..<BR>";
open (DATA, "data/$INPUT{'usr'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'usr'}");

print DATA "";


close DATA;

print "<CENTER>User $INPUT{'usr'} has beed deleted!";
}



sub list {
print <<"HTML";
<BODY>
<CENTER>
Raven Members
  <TABLE BORDER CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Name</TD>
      <TD>EMail</TD>
      <TD>Race</TD>
      <TD>Class</TD>
      <TD>Rank</TD>
      <TD>Delete</TD>
      <TD>Edit</TD>
    </TR>
HTML

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

print "<FORM METHOD=POST><INPUT TYPE=hidden VALUE=$INPUT{'name'} NAME=name><INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password>\n";
print "<TR><TD>$usr<INPUT TYPE=hidden VALUE=$usr NAME=usr></TD>\n";
print "<TD>$email<INPUT TYPE=hidden VALUE=$email NAME=email></TD>\n";
print "<TD>$race<INPUT TYPE=hidden VALUE=$race NAME=race></TD>\n";
print "<TD>$class<INPUT TYPE=hidden VALUE=$class NAME=class></TD>\n";
print "<TD>$rank<INPUT TYPE=hidden VALUE=$rank NAME=rank>\n";
print "<INPUT TYPE=hidden VALUE=$acc NAME=acc></TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Delete NAME=a></TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Edit NAME=a></TD></TR></FORM>\n";

}
print "</TABLE></CENTER>\n";
}


sub edit {
print <<"HTML";
<FORM METHOD="POST">
<INPUT TYPE=hidden VALUE=$INPUT{'name'} NAME=name>
<INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password>
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name</TD>
	<TD>
	  <INPUT TYPE="text" NAME="usr" VALUE="$INPUT{'usr'}"></TD>
      </TR>
      <TR>
	<TD>E-Mail</TD>
	<TD>
	  <INPUT TYPE="text" NAME="email" VALUE="$INPUT{'email'}"></TD>
      </TR>
      <TR>
	<TD>Race</TD>
	<TD>
	  <INPUT TYPE="text" NAME="race" VALUE="$INPUT{'race'}">
</TD>
      </TR>
      <TR>
	<TD>Class</TD>
	<TD>
	  <INPUT TYPE="text" NAME="class" VALUE="$INPUT{'class'}"></TD>
      </TR>
HTML

open (FILE, "data/$INPUT{'name'}");
flock (FILE, 2);
$Ausr = <FILE>;
chop ($Ausr);
$Acryptpass = <FILE>;
chop ($Acryptpass);
$Aemail = <FILE>;
chop ($Aemail);
$Arace = <FILE>;
chop ($Arace);
$Aclass = <FILE>;
chop ($Aclass);
$Arank = <FILE>;
chop ($Arank);
$Aacc = <FILE>;
chop ($Aacc);
$Ajunk = <FILE>;
chop ($Ajunk);
flock (FILE, 8);
close(FILE);

if ($Aacc eq "c") {
print <<"HTML";
      <TR>
	<TD>Rank</TD>
	<TD>
	  <SELECT NAME="rank">
	  <OPTION>Head-Leader
	  <OPTION>1st-Leader
	  <OPTION>2nd-Leader
	  <OPTION>3rd-Leader
	  <OPTION>4th-Leader
	  <OPTION>5th-Leader
	  <OPTION SELECTED>Raven
	  <OPTION>Oscar</SELECT></TD>
      </TR>
      <TR>
	<TD>Accesses</TD>
	<TD>
	  <SELECT NAME="acc">
	  <OPTION SELECTED>a
	  <OPTION>b
          <OPTION>c</SELECT></TD>
      </TR>
HTML
}
else {
print <<"HTML";
<INPUT TYPE=hidden VALUE=$INPUT{'rank'} NAME=rank>
<INPUT TYPE=hidden VALUE=$INPUT{'acc'} NAME=acc>
HTML
}


print <<"HTML";
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit NAME=a Value=update></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}








sub update {

open (FILE, "data/$INPUT{'usr'}");
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


open (DATA, "data/$INPUT{'usr'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'usr'}");

print DATA "$INPUT{'usr'}\n";
print DATA "$pass\n";
print DATA "$INPUT{'email'}\n";
print DATA "$INPUT{'race'}\n";
print DATA "$INPUT{'class'}\n";
print DATA "$INPUT{'rank'}\n";
print DATA "$INPUT{'acc'}\n";
print DATA "junk\n";

close DATA;

print "<CENTER>User $INPUT{'usr'} has been Updated";
}


sub email {
print <<"HTML";
<FORM METHOD="POST">
<INPUT TYPE=hidden VALUE=$INPUT{'name'} NAME=name>
<INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password>
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  Message</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <TEXTAREA NAME="message" ROWS="15" COLS="60"></TEXTAREA></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
  <SELECT NAME=to>
  <OPTION SELECTED>All
  <OPTION>Offaser</SELECT><BR>
	  <INPUT TYPE=submit VALUE="SendEmail" NAME=a></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}

sub semail {
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


if ($INPUT{'to'} eq "Offaser") { 

if ($rank eq "Head-Leader") { 
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "Oscar") { 
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "1st-Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "2nd-Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "3rd-Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "4th-Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "5th-Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}

}
elsif ($INPUT{'to'} eq "All") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens NewsLetter\n\n";
print MAIL "Hello $usr!\n";
print MAIL "$INPUT{'message'}\n";
}


}
print "<CENTER>E-Mails have been sent";
}

sub news {
print <<"HTML";
<FORM METHOD="POST">
<INPUT TYPE=hidden VALUE=$INPUT{'name'} NAME=name>
<INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password>
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  News</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <TEXTAREA NAME="news" ROWS="15" COLS="60">
HTML

open (DATA, "news.dat");
@data = <DATA>;
close DATA;

print "@data";


print <<"HTML";
</TEXTAREA></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Update News" NAME=a></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}

sub upnews {
open (DATA, "news.dat");
@data = <DATA>;
close DATA;
open(DATA, ">news.dat");

print DATA "$INPUT{'news'}";

print <<"HTML";
<CENTER><B>News has been Updated</B><BR>
HTML
}

print "<P><CENTER><A HREF=admin.cgi?a=login&name=$INPUT{'name'}&password=$INPUT{'password'}>Main Page</A>";