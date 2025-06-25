#!/usr/bin/perl

require 'cookie.lib';

##################################################################################

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

##################################################################################

# $guild{'#'}
# 1 Account Number
# 2 Guild Name
# 3 Guild Password
# 4 Guild Email
# 5 Gold Expires
# 6 Account Type
# 7 Account created
# 8 Account Creator
# 9 Server
# 10 counter image number

# $user{'#'}
# 1 First Name
# 2 SurName
# 3 Password
# 4 email
# 5 Guild
# 6 Class
# 7 Race
# 8 Level
# 9 access
# 10 rank
# 11 type
# 12 Points
# 13 Master if acct.

##################################################################################

print "Content-type: text/html\n\n";

##################################################################################

if ($INPUT{'do'} eq "name") { &name; }
elsif ($INPUT{'do'} eq "chat") { &chat; }
elsif ($INPUT{'do'} eq "text") { &text; }
elsif ($INPUT{'do'} eq "sendtext") { &sendtext; }
else { &showframe; }


##################################################################################

sub showframe {
&getdata;

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function frameNavig() {
frames['chat'].window.location="chat.cgi?do=chat&guild=$INPUT{'guild'}";
}

// End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<FRAMESET COLS="100%" BORDER=0>
  <FRAMESET ROWS="10%,75%,15%">
    <FRAME SRC="chat.cgi?do=name&guild=$INPUT{'guild'}" NAME="name" SCROLLING="No" NORESIZE>
    <FRAME SRC="chat.cgi?do=chat&guild=$INPUT{'guild'}" NAME="chat" NORESIZE>
    <FRAME SRC="chat.cgi?do=text&guild=$INPUT{'guild'}" NAME="text" SCROLLING="No" NORESIZE>
  </FRAMESET>
</FRAMESET>

<NOFRAMES>
<BODY>
<P>
</BODY></NOFRAMES></HTML>
HTML
}

##################################################################################

sub name {
&getdata;

print <<"HTML";
<HTML>
<HEAD>
</HEAD>
<BODY topmargin="3" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="green">

<CENTER><BIG><B><FONT COLOR=white>$guild{'2'} Chat Room</FONT></B></BIG></CENTER>
</BODY>
</HTML>
HTML

}

##################################################################################

sub chat {
open (DATA, "data/$INPUT{'guild'}.chat");
@data = <DATA>;
close DATA;

$data = "@data";


print <<"HTML";
<HTML>
<HEAD>
<META HTTP-EQUIV=refresh CONTENT=10 URL="chat.cgi?do=chat&guild=$INPUT{'guild'}">
<META HTTP-EQUIV="expires" CONTENT="0">
<META HTTP-EQUIV="pragma" CONTENT="no-cache">
</HEAD>
<BODY>
HTML

print "$data";

print <<"HTML";
<A NAME="end"></A>
<SCRIPT LANGUAGE="JavaScript">
<!--
if (document.all) {
 end.scrollIntoView(false);
}
//-->
</SCRIPT>
</BODY></HTML>
HTML
}

##################################################################################

sub text {

print <<"HTML";
<HTML>
<HEAD>
</HEAD>
<BODY topmargin="5" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="darkgreen" onload="parent.frameNavig()">
<CENTER>
<FORM ACTION="chat.cgi" METHOD="POST" NAME="msgform">
  <INPUT TYPE="text" NAME="mess" SIZE="40">
  <INPUT TYPE=submit VALUE="Send">
  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
  <INPUT TYPE="hidden" NAME="do" VALUE="sendtext">
</FORM>
<SCRIPT LANGUAGE="JavaScript">
<!--
    document.msgform.mess.focus();
//-->
</SCRIPT>
</BODY></HTML>
HTML

}

##################################################################################

sub sendtext {

&getuser;

$i = 0;

open (DATA, "data/$INPUT{'guild'}.chat");
@data = <DATA>;
close DATA;

foreach $line (@data) {
$i = $i + 1;
}

open(DATA, ">data/$INPUT{'guild'}.chat");
foreach $line (@data) {
if ($i >= 40) {
$i = $i - 1;
print DATA "";
}
else {
print DATA "$line";
}
}
print DATA "<B>$user{'1'}></B> $INPUT{'mess'}<BR>\n";
close DATA;

&text;

}

##################################################################################

sub getdata {

$i = 0;
open (DATA, "data/$INPUT{'guild'}.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$guild{$i} = "$line";
}

}

##################################################################################

sub getuser {

&GetCookies('user');

$user = "$Cookies{'user'}";

$i = 0;
open (DATA, "user/$user.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$user{$i} = "$line";
}
open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
if ($name eq "$user") {
$user{9} = "$accs";
$user{10} = "$ran";
$user{11} = "$typ";
$user{12} = "$pts";
if ($user{'9'} eq "Master") {
$user{'9'} = "Administrator";
$user{'13'} = "Master";
}
}
}

}

##################################################################################