#!/usr/bin/perl

$memberurl="http://www.d0tt.com";
$data="/usr/home/byron/public_html/cgi-bin/scripts/members/data";
$pay="no";
$price="4";
$month="no";
$cc="no";
$check="no";
$mailprog="/usr/lib/sendmail";
$domain="d0tt.com";
$cgiurl="http://www.d0tt.com/cgi-bin/scripts/members/members.cgi";

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

if($ENV{'REQUEST_METHOD'} eq "GET") {  
  if($ENV{QUERY_STRING} eq "add") { &addform }
else { &login }
 }
if($ENV{'REQUEST_METHOD'} eq "POST") {
  if($INPUT{'submit'} eq "Join") { &newmem }
  if($INPUT{'submit'} eq "Login") { &members }
}

sub login {
print "Content-type: text/html\n\n";
print "<FORM ACTION=members.cgi METHOD=POST>\n";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD>User name:</TD><TD>\n";
print "<INPUT TYPE=text NAME=user SIZE=15></TD>\n";
print "</TR><TR><TD>Password:</TD><TD>\n";
print "<INPUT TYPE=password NAME=password SIZE=15></TD>\n";
print "</TR><TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=Login></TD>\n";
print "</TR><TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<A HREF=members.cgi?add>Not a member yet</A></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
}

sub members {
print "Content-type: text/html\n\n";
if($INPUT{'user'} eq "") { print "Please enter a username"; }

open (FILE, "$data/$INPUT{'user'}");
flock (FILE, 2);
$user = <FILE>;
chop ($user);
$pass = <FILE>;
chop ($pass);
$name = <FILE>;
chop ($name);
$email = <FILE>;
chop ($email);
$age = <FILE>;
chop ($age);
$state = <FILE>;
chop ($state);
$ccnum = <FILE>;
chop ($ccnum);
$ccname = <FILE>;
chop ($ccname);
$ccexp = <FILE>;
chop ($ccexp);
flock (FILE, 8);
close(FILE);
if($pass eq "") {
$pass="bad";
}
if($INPUT{'password'} eq "$pass") {
print "<FRAMESET ROWS=\"100%,*\"><FRAME SRC=$memberurl></FRAMESET>\n";
print "<NOFRAMES><B>Members page requires frames</B></NOFRAMES>\n";
}
else {
$pass="bad";
}
if($pass eq "bad") {
print "bad password";
}
}

sub addform {
print "Content-type: text/html\n\n";
print "<FORM ACTION=members.cgi METHOD=POST>\n";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
## start get data
print "<TR><TD>Username:</TD><TD><INPUT TYPE=text NAME=user></TD></TR>\n";
print "<TR><TD>Real Name:</TD><TD><INPUT TYPE=text NAME=name></TD></TR>\n";
print "<TR><TD>E-Mail:</TD><TD><INPUT TYPE=text NAME=email></TD></TR>\n";
print "<TR><TD>Age:</TD><TD><INPUT TYPE=text NAME=age SIZE=3 MAXLENGTH=2></TD></TR>\n";
print "<TR><TD>State:</TD><TD><INPUT TYPE=text NAME=state SIZE=3 MAXLENGTH=2></TD></TR>\n";
##start price
if($pay eq "yes") {
  print "<TR><TD COLSPAN=2><P ALIGN=Center>There is a charge of $price for membership.</TD></TR>\n";
  ##start cc
  if($cc eq "yes") {
    print "<TR><TD>Credit Card #:</TD>\n";
    print "<TD><INPUT TYPE=text NAME=ccnum></TD></TR>\n";
    print "<TR><TD>Credit card name:</TD>\n";
    print "<TD><INPUT TYPE=text NAME=ccname></TD></TR>\n";
    print "<TR><TD>Credit card expire:</TD>\n";
    print "<TD><INPUT TYPE=text NAME=ccexp SIZE=10></TD></TR>\n";
    }
  ##start check
  if($check eq "yes") {
    print "<TR><TD COLSPAN=2>Check info</TD></TR>\n";
    }
}
print "<TR><TD COLSPAN=2><P ALIGN=Center><INPUT TYPE=submit NAME=submit VALUE=Join></TD></TR></TABLE></CENTER></FORM>\n";
}

sub newmem {
print "Content-type: text/html\n\n";
### CHECK INPUT
if($INPUT{'user'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
if($INPUT{'name'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
if($INPUT{'email'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
if($INPUT{'age'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
if($INPUT{'state'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
#  if($pay eq "yes") {
#    if($cc eq "yes") {
#      if($INPUT{'ccnum'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
#      if($INPUT{'ccname'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
#      if($INPUT{'ccexp'} eq "") { print "Data missing. Hit back and fill in all the felds.<BR>\n"; }
#    }
#  }
else {
###############RANDOM PASS NEEDED
open (FILE, "$data/$INPUT{'user'}");
flock (FILE, 2);
$user = <FILE>;
chop ($user);
$pass = <FILE>;
chop ($pass);
$name = <FILE>;
chop ($name);
$email = <FILE>;
chop ($email);
$age = <FILE>;
chop ($age);
$state = <FILE>;
chop ($state);
$ccnum = <FILE>;
chop ($ccnum);
$ccname = <FILE>;
chop ($ccname);
$ccexp = <FILE>;
chop ($ccexp);
flock (FILE, 8);
close(FILE);

if($user eq "") {

open(FILE, ">$data/$INPUT{'user'}");
print FILE "$INPUT{'user'}\n";
print FILE "$pass\n";
print FILE "$INPUT{'name'}\n";
print FILE "$INPUT{'email'}\n";
print FILE "$INPUT{'age'}\n";
print FILE "$INPUT{'state'}\n";
print FILE "$INPUT{'ccnum'}\n";
print FILE "$INPUT{'ccname'}\n";
print FILE "$INPUT{'ccexp'}\n";
close(FILE);

print "You will recive an email with your password within the hour";

open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
print MAIL "To: $INPUT{'email'}\n";
print MAIL "Reply-to: webmaster\@$domain\n";
print MAIL "From: webmaster\@$domain\n";
print MAIL "Subject: membership password\n";
			print MAIL "\n";
			print MAIL "Welcome $INPUT{'name'}\n";
			print MAIL "Your password is $pass\n";
			print MAIL "Go to:\n";
			print MAIL "$cgiurl\n";
			print MAIL "to login\n";
			print MAIL "\n";
			print MAIL "Thank you\n";
}
else {
print "Username taken";
}
}
}