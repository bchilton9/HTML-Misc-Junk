#!/usr/bin/perl

$adminpass="admin";
$mailprog="/usr/lib/sendmail";
$email="webmaster\@d0tt.com";


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
  if($ENV{QUERY_STRING} eq "admin") { &adminlogin }
  if($ENV{QUERY_STRING} eq "remove") { &removeform }
  else { &addform }
  }
if($ENV{'REQUEST_METHOD'} eq "POST") {
  if($INPUT{'submit'} eq "Join List") { &addmember }
  if($INPUT{'submit'} eq "Login") { &admin }
  if($INPUT{'submit'} eq "Send Mails") { &sendmail }
}

sub addform {
print "Content-type: text/html\n\n";
print "<FORM ACTION=maillist.cgi METHOD=POST>\n";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD>E-Mail address:</TD>\n";
print "<TD><INPUT TYPE=text NAME=email></TD></TR>\n";
print "<TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Join List\"></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
&logo;
}

sub addmember {
open (DATA, "emails");
@data = <DATA>;
close DATA;

open(FILE, ">emails");
print FILE "$INPUT{'email'}\n";
foreach $line (@data){
print FILE "$line";
}

print "Content-type: text/html\n\n";
print "Thank you. You have been added";
&logo;
}

sub adminlogin {
print "Content-type: text/html\n\n";
print "<FORM ACTION=maillist.cgi METHOD=POST>\n";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD>E-Mail address:</TD>\n";
print "<TD><INPUT TYPE=text NAME=pass></TD></TR>\n";
print "<TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Login\"></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
&logo;
}

sub admin {
if($INPUT{'pass'} eq "$adminpass") {
print "Content-type: text/html\n\n";
print "<FORM ACTION=maillist.cgi METHOD=POST>\n";
print "<TABLE BORDER CELLPADDING=2><TR><TD>Subject:</TD><TD>\n";
print "<INPUT TYPE=text NAME=sub></TD></TR>\n";
print "<TR><TD>Content:</TD>\n";
print "<TD><TEXTAREA NAME=main ROWS=4 COLS=18></TEXTAREA></TD></TR>\n";
print "<TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Send Mails\"></TD>\n";
print "</TR></TABLE></FORM>\n";
&logo;
}

sub logo {
print "<HR COLOR=BLUE><CENTER>Mailing List by <A HREF=http://www.d0tt.com>Byron Chilton</A>";
}

sub sendmail {
open (DATA, "emails");
@data = <DATA>;
close DATA;

open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
#print MAIL "To:
#foreach $line (@data) {
#chomp ($line);
#($emails) = split(/:/, $line);
#$emails,\n";
print MAIL "Reply-to: $email\n";
print MAIL "From: $email\n";
print MAIL "Subject: $INPUT{'sub'}\n";
print MAIL "\n";
print MAIL "$INPUT{'main'}\n\n";
Print MAIL "Mailing list by www.d0tt.com";

print "Content-type: text/html\n\n";
print "Mails sent";
&logo;
}