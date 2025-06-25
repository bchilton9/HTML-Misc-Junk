#!/usr/bin/perl
#####################################################
# Send a site coppyright Byron Chilton              #
# For more scripts go to http://www.d0tt.com        #
#                                                   #
# To install this script set up the variables below #
# Upload the sendasite.cgi to you cgi-bin in ASCII  #
# chmode it to 755                                  #
# upload sendasite.html                             #
#####################################################

$subject="This page is really cool";
## The subject of the emails

$siteurl="http://www.domain.com";
## your sites url

$site="site name";
## Your sites name

$mailprog="/usr/lib/sendmail";
## your servers sendmail program

$logging="yes";
$pass="admin";


##########################
## DO NOT EDIT ANY MORE ##
##########################

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
    push(@values,$value); push(@names,$name);   
    $FORM{$name} = $value;
  }

if($ENV{QUERY_STRING} eq "admin") { &login }
elsif($FORM{'password'} eq "$pass") { &admin }
elsif($FORM{'Clear'} eq "Clear") { &clear }
else { &send }

sub send {
$sendto="$FORM{'to'}";
$sendfrom="$FORM{'from'}";
$sendname="$FORM{'name'}";
$comments="$FORM{'comment'}";

print "Content-type: text/html\n\n"; 
print "Thank you for sending my site!<BR>\n\n";
print "To return to $site<BR>\n\n";
print "<A HREF=$siteurl>Click Here</A>\n\n";
print "<P><P>\n\n";
print "<A HREF=http://www.d0tt.com>Send a site by Byron</A><BR>\n\n";

if($logging eq "yes") {
open (DATA, "send.data");
@data = <DATA>;
close DATA;

$data = "@data";

open(FILE, ">404.data");
print FILE "$sendto:$sendfrom:$sendname:$comments\n";
foreach $line (@data){
print FILE "$line";
}
close (FILE);
}

## SEND TO
open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
print MAIL "To: $sendto\n";
print MAIL "Reply-to: $sendfrom\n";
print MAIL "From: $sendfrom\n";
print MAIL "Subject: $subject\n";
print MAIL "$sendname sent you this really cool page called $site.\n\n";
print MAIL "You can go see it at:\n";
print MAIL "$siteurl\n\n";
print MAIL "Theay have also included:\n";
print MAIL "$comments\n\n";
print MAIL "\n\n";
print MAIL "Send a site by Byron. http://www.d0tt.com";
close (MAIL);
}

sub login {
print "Content-type: text/html\n\n"; 
print "<CENTER><FORM ACTION=sendasite.cgi METHOD=POST>";
print "<INPUT TYPE=password NAME=password><BR>";
print "<INPUT TYPE=submit VALUE=Login></FORM>";
}

sub admin {
print "Content-type: text/html\n\n"; 
print "<CENTER>";
open (DATA, "send.data");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($sendto, $sendfrom, $sendname, $comments) = split(/:/, $line);
print "$sendfrom sent your site to $sendto $sendname $comments<BR>";
}
print "<FORM ACTION=sendasite.cgi METHOD=POST>";
print "<INPUT TYPE=submit NAME=Clear VALUE=Clear></FORM>";
&foot;
}

sub clear {
print "Content-type: text/html\n\n"; 
print "<CENTER>";
open(FILE, ">404.data");
print FILE "";
close (FILE);
print "<B>Cleared</B>";
&foot;
}

sub foot {
print "<HR COLOR=BLUE>Send a Site by <A HREF=http://www.d0tt.com>Byron Chilton</A>";
}