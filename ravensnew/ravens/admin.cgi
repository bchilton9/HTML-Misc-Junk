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
<FORM METHOD=POST><CENTER>
<TABLE BORDER CELLPADDING=2 ALIGN=Center>
<TR><TD>Admin Password</TD><TD>
<INPUT TYPE=text NAME=password></TD>
</TR><TR><TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=a value=login>
<INPUT TYPE=submit></TD></TR>
</TABLE></CENTER></FORM>
HTML
}

sub login {
if ($INPUT{'password'} eq "0519a") {
print <<"HTML";
<CENTER>
To Be aproved!
  <TABLE BORDER CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Name</TD>
      <TD>Password</TD>
      <TD>EMail</TD>
      <TD>Race</TD>
      <TD>Class</TD>
      <TD>Rank</TD>
      <TD>Aprove</TD>
      <TD>Delete</TD>
      <TD>Edit</TD>
    </TR>
HTML

open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "a") {
print <<"HTML";
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
function killEntry(entry) { if (window.confirm("Are you sure you want to Delete this Member?")) 
{ window.location.href = "http://www.erenetwork.com/ravens/cgi/admin.cgi?a=Delete&password=$INPUT{'password'}&name=" + entry + "" } }
  </Script>
</HEAD>
<BODY>
HTML

print "<FORM METHOD=POST><INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password><TR><TD>$name<INPUT TYPE=hidden VALUE=$name NAME=name></TD>\n";
print "<TD>$pass<INPUT TYPE=hidden VALUE=$pass NAME=pass></TD>\n";
print "<TD>$email<INPUT TYPE=hidden VALUE=$email NAME=email></TD>\n";
print "<TD>$race<INPUT TYPE=hidden VALUE=$race NAME=race></TD>\n";
print "<TD>$class<INPUT TYPE=hidden VALUE=$class NAME=class></TD>\n";
print "<TD><SELECT NAME=rank>\n";
print "<OPTION>Head Leader\n";
print "<OPTION>1st Leader\n";
print "<OPTION>2nd Leader\n";
print "<OPTION>3rd Leader\n";
print "<OPTION>4th Leader\n";
print "<OPTION>5th Leader\n";
print "<OPTION SELECTED>Raven\n";
print "<OPTION>Oscar</SELECT></TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Aprove NAME=a></TD>\n";
print "<TD><INPUT TYPE=button VALUE=Delete onClick=javascript:killEntry('$name')></TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Edit NAME=a></TD></TR></FORM>\n";


}
}
print "</TABLE></CENTER>\n";
print <<"HTML";
<CENTER>
<P>
<BR>
<A HREF="admin.cgi?a=email&password=$INPUT{'password'}">E-Mail Members</A>
<P>
<A HREF="admin.cgi?a=list&password=$INPUT{'password'}">List All Members</A>
<P>
<A HREF="admin.cgi?a=news&password=$INPUT{'password'}">Update News</A>
HTML

}
else {
print "<CENTER><B>Invalid Password!";
}
}

sub aprove {
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
open(DATA, ">data.dat");
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
print DATA "$INPUT{'name'}::$INPUT{'pass'}::$INPUT{'email'}::$INPUT{'race'}::$INPUT{'class'}::$INPUT{'rank'}::V\n";
}
else {
print DATA "$line\n";
}
}
close DATA;

$password = crypt($INPUT{'pass'}, "YL");
open (wdata, ">>../members/.htpasswd") or &error("Unable to write to the data file");
print wdata "$INPUT{'name'}:";
print wdata "$password\n";
close(wdata); 

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

print "<CENTER>User $INPUT{'name'} has beed aproved!";
}

sub delete {
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
open(DATA, ">data.dat");
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}
close DATA;


open (DATA, "../members/.htpasswd");
@data = <DATA>;
close DATA;
open(DATA, ">../members/.htpasswd");
foreach $line (@data) {
chomp ($line);
($name, $pass) = split(/:/, $line);
if ($name eq "$INPUT{'name'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}
close DATA; 


print "<CENTER>User $INPUT{'name'} has beed deleted!";
}

sub list {
print <<"HTML";
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
function killEntry(entry) { if (window.confirm("Are you sure you want to Delete this Member?")) 
{ window.location.href = "http://www.erenetwork.com/ravens/cgi/admin.cgi?a=Delete&password=$INPUT{'password'}&name=" + entry + "" } }
  </Script>
</HEAD>
<BODY>
<CENTER>
Raven Members
  <TABLE BORDER CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Name</TD>
      <TD>Password</TD>
      <TD>EMail</TD>
      <TD>Race</TD>
      <TD>Class</TD>
      <TD>Rank</TD>
      <TD>Aprov</TD>
      <TD>Delete</TD>
      <TD>Edit</TD>
    </TR>
HTML

open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);

print "<FORM METHOD=POST><INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password><TR><TD>$name<INPUT TYPE=hidden VALUE=$name NAME=name></TD>\n";
print "<TD>$pass<INPUT TYPE=hidden VALUE=$pass NAME=pass></TD>\n";
print "<TD>$email<INPUT TYPE=hidden VALUE=$email NAME=email></TD>\n";
print "<TD>$race<INPUT TYPE=hidden VALUE=$race NAME=race></TD>\n";
print "<TD>$class<INPUT TYPE=hidden VALUE=$class NAME=class></TD>\n";
print "<TD>$rank<INPUT TYPE=hidden VALUE=$rank NAME=rank></TD>\n";

print "<TD>$aprov<INPUT TYPE=hidden VALUE=$aprov NAME=aprov></TD>\n";

print "<TD><INPUT TYPE=button VALUE=Delete onClick=javascript:killEntry('$name')></TD>\n";
print "<TD><INPUT TYPE=submit VALUE=Edit NAME=a></TD></TR></FORM>\n";

}
print "</TABLE></CENTER>\n";
}


sub edit {
print <<"HTML";
<FORM METHOD="POST">
<INPUT TYPE=hidden VALUE=$INPUT{'password'} NAME=password>
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name</TD>
	<TD>
	  <INPUT TYPE="text" NAME="name" VALUE="$INPUT{'name'}"></TD>
      </TR>
      <TR>
	<TD>Password</TD>
	<TD>
	  <INPUT TYPE="text" NAME="pass" VALUE="$INPUT{'pass'}"></TD>
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
      <TR>
	<TD>Rank</TD>
	<TD>
	  <SELECT NAME="rank">
	  <OPTION>Head Leader
	  <OPTION>1st Leader
	  <OPTION>2nd Leader
	  <OPTION>3rd Leader
	  <OPTION>4th Leader
	  <OPTION>5th Leader
	  <OPTION SELECTED>Raven
	  <OPTION>Oscar</SELECT></TD>
      </TR>
      <TR>
	<TD>Aproved</TD>
	<TD>
	  <SELECT NAME="aprov">
	  <OPTION SELECTED>V
	  <OPTION>A</SELECT></TD>
      </TR>
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
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
open(DATA, ">data.dat");
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
print DATA "$INPUT{'name'}::$INPUT{'pass'}::$INPUT{'email'}::$INPUT{'race'}::$INPUT{'class'}::$INPUT{'rank'}::$INPUT{'aprov'}\n";
}
else {
print DATA "$line\n";
}
}
close DATA;

$passw = crypt($INPUT{'pass'}, "YL");
open (DATA, "../members/.htpasswd");
@data = <DATA>;
close DATA;
open(DATA, ">../members/.htpasswd");
foreach $line (@data) {
chomp ($line);
($namea, $passa) = split(/:/, $line);
if ($namea eq "$INPUT{'name'}") {
print DATA "$INPUT{'name'}:";
print DATA "$passw\n";
}
else {
print DATA "$line\n";
}
}
close DATA; 
print "<CENTER><B>$INPUT{'name'} Updated";
}


sub email {
print <<"HTML";
<FORM METHOD="POST">
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
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($INPUT{'to'} eq "Offaser") { 

if ($rank eq "Oscar") { 
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $name!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "1st Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $name!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "2nd Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $name!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "3rd Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $name!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "4th Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $name!\n";
print MAIL "$INPUT{'message'}\n";
}
elsif ($rank eq "5th Leader") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens Oscar Message\n\n";
print MAIL "Hello $name!\n";
print MAIL "$INPUT{'message'}\n";
}

}
elsif ($INPUT{'to'} eq "All") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: Webmaster\@ravensofdispair.com\n";
print MAIL "From: Webmaster\@ravensofdispair.com\n";
print MAIL "Subject: Ravens NewsLetter\n\n";
print MAIL "Hello $name!\n";
print MAIL "$INPUT{'message'}\n";
}


}
print "<CENTER>E-Mails Sent";
}

sub news {
print <<"HTML";
<FORM METHOD="POST">
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

open (DATA, "../members/data.html");
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
open (DATA, "../members/data.html");
@data = <DATA>;
close DATA;
open(DATA, ">../members/data.html");

print DATA "$INPUT{'news'}";

print <<"HTML";
<CENTER><B>News Updated</B><BR>
HTML
}

print "<P><CENTER><A HREF=admin.cgi?a=login&password=$INPUT{'password'}>Main Page</A>";