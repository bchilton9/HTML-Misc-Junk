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
if ($INPUT{'name'} eq "") { &error; }
else {

if ($INPUT{'a'} eq "list") { &list; }
elsif ($INPUT{'a'} eq "Read") { &read }
elsif ($INPUT{'a'} eq "Delete") { &delete }
elsif ($INPUT{'a'} eq "Reply") { &send }
elsif ($INPUT{'a'} eq "Send Message") { &sendmessage }
else { &error; }
}

sub list {
$count = "0";
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Defenders Message System</TITLE>
</HEAD>
<BODY BACKGROUND="http://www.erenetwork.com/defender/parchment.gif">
<P ALIGN=Center>
HTML

open (DATA, "dat/$INPUT{'name'}.msg");
@data = <DATA>;
foreach $line (@data) {
chomp ($line);
($sender, $num) = split(/::/, $line);
print <<"HTML";
<FORM METHOD="POST">
<CENTER><TABLE BORDER BORDERCOLOR=red WIDTH=40% CELLPADDING="2" ALIGN="Center">
<TR><TD><P ALIGN=Center>
<FONT COLOR="#000000">From:</FONT></TD>
<TD COLSPAN=2>$sender
<INPUT TYPE=hidden VALUE="$sender" NAME="sender">
<INPUT TYPE=hidden VALUE="$num" NAME="msgnum">
<INPUT TYPE=hidden VALUE="$INPUT{'name'}" NAME=name>
</TD></TR><TR><TD><P ALIGN=Center>
<INPUT TYPE=submit VALUE="Read" NAME=a></TD>
<TD><P ALIGN=Center>
<INPUT TYPE=submit VALUE="Reply" NAME=a></TD>
<TD><P ALIGN=Center>
<INPUT TYPE=submit VALUE="Delete" NAME=a></TD>
</TR></TABLE></CENTER></FORM><P>
HTML
$count = "1";
}
close DATA;


if ($count eq "0") {
print <<"HTML";
<P><CENTER>
<B>No Messages</B>
HTML
}
print <<"HTML";
</BODY></HTML>
HTML
}



sub read {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Defenders Message System</TITLE>
</HEAD>
<BODY BACKGROUND="http://www.erenetwork.com/defender/parchment.gif">
<P ALIGN=Center>
<A HREF=msg.cgi?a=list&name=$INPUT{'name'}>Main Page</A>
HTML
open (DATA, "msges/$INPUT{'msgnum'}");
@data = <DATA>;
close DATA;
print "@data";

print <<"HTML";
</BODY></HTML>
HTML
}



sub delete {
open(DATA, "dat/$INPUT{'name'}.msg");
@data = <DATA>;
close DATA;
open(DATA, ">dat/$INPUT{'name'}.msg");
foreach $line (@data) {
chomp ($line);
($sender, $num) = split(/::/, $line);
if ($num eq "$INPUT{'msgnum'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}
close DATA;
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Defenders Message System</TITLE>
</HEAD>
<BODY BACKGROUND="http://www.erenetwork.com/defender/parchment.gif">
<P ALIGN=Center>
<A HREF=msg.cgi?a=list&name=$INPUT{'name'}>Main Page</A>
<P><CENTER><B>
Message Deleted
</BODY></HTML>
HTML

}



sub send{
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Defenders Message System</TITLE>
</HEAD>
<BODY BACKGROUND="http://www.erenetwork.com/defender/parchment.gif">
<P ALIGN=Center>
<A HREF=msg.cgi?a=list&name=$INPUT{'name'}>Main Page</A>
<P><CENTER><B>
<FORM METHOD="POST">
  <CENTER>
    <TABLE BORDER BORDERCOLOR=red WIDTH=40% CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  <FONT COLOR="#000000">From:</FONT></TD>
	<TD>$INPUT{'name'}
<INPUT TYPE=hidden VALUE="$INPUT{'name'}" NAME=name>
</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
	  To:</TD>
	<TD>$INPUT{'sender'}
<INPUT TYPE=hidden VALUE="$INPUT{'sender'}" NAME=sender>
</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><TEXTAREA NAME="message" ROWS="10" COLS="50"></TEXTAREA></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Send Message" NAME=a></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
</BODY></HTML>
HTML
}

sub sendmessage {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Defenders Message System</TITLE>
</HEAD>
<BODY BACKGROUND="http://www.erenetwork.com/defender/parchment.gif">
<P ALIGN=Center>
<A HREF=msg.cgi?a=list&name=$INPUT{'name'}>Main Page</A>
<P><CENTER><B>
Message has been sent to $INPUT{'sender'}
</BODY></HTML>
HTML

open (FILE, "count.txt");
flock (FILE, 2);
$abcdefg = <FILE>;
chop ($abcdefg);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$abcdefg++;

open(DATA, ">count.txt");
print DATA "$abcdefg\n";
print DATA "junk\n";
close DATA;

open(DATA, ">dat/$INPUT{'sender'}.msg");
foreach $line (@data) {
print DATA "$line\n";
}
print DATA "$INPUT{'name'}::$abcdefg\n";
close DATA;


open(DATA, ">msges/$abcdefg");
print DATA "<FORM METHOD=POST><CENTER>\n";
print DATA "<TABLE BORDER BORDERCOLOR=red WIDTH=40% CELLPADDING=2 ALIGN=Center>\n";
print DATA "<TR><TD><P ALIGN=Center>\n";
print DATA "<FONT COLOR=000000>From:</FONT></TD><TD>\n";
print DATA "<INPUT TYPE=hidden VALUE=$abcdefg NAME=msgnum>\n";
print DATA "$INPUT{'name'}<INPUT TYPE=hidden VALUE=$INPUT{'name'} NAME=sender>\n";
print DATA "<INPUT TYPE=hidden VALUE=$INPUT{'sender'} NAME=name>\n";
print DATA "</TD></TR><TR><TD COLSPAN=2>$INPUT{'message'}\n";
print DATA "</TD></TR><TR><TD><P ALIGN=Center>\n";
print DATA "<INPUT TYPE=submit VALUE=Reply NAME=a></TD>\n";
print DATA "<TD><P ALIGN=Center>\n";
print DATA "<INPUT TYPE=submit VALUE=Delete NAME=a></TD></TR>\n";
print DATA "</TABLE></CENTER></FORM>\n";
close DATA;
}


sub error{
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Defenders Message System</TITLE>
</HEAD>
<BODY BACKGROUND="http://www.erenetwork.com/defender/parchment.gif">
<P ALIGN=Center>
<P><CENTER><B>
Please enter your charater name
<FORM>
<INPUT TYPE=text NAME=name>
<INPUT TYPE=submit VALUE=Reply NAME=a>
</BODY></HTML>
HTML
}


