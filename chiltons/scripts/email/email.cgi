#!/usr/bin/perl
                                    
#################################################
# Email script coppyright Byron Chilton         #
# For more scripts go to http://www.d0tt.com    #
#                                               #
# To install the script                         #
# Set up the Variables                          #
# Upload the email.cgi to your cgi-bin in ASCII #
# chmode it to 755                              #
# upload email.html                             #
#################################################

$email="someone\@something.com"; 
## Your Email addres

$mailprog="/usr/lib/sendmail"; 
## Your servers sendmail prog

$subject="Thank you";
## Email subject

$site="D0TT.com";
## Your sites name

$siteurl="http://www.D0TT.com/email.shtml";
## Your sites URL

##These fields are optional

$useloc="0";
## Use the Location field (0=no,1=yes) If yes make a field named "loc"

$useurl="0";
## Use the URL field (0=no,1=yes) If yes make a field named "url"

#####These fields can have aneything in them!!

$useou1="0";
## Use the other1 field (0=no,1=yes) If yes make a field named "other1"
$out1="Other1";
## The name of other1

$useou2="0";
## Use the other2 field (0=no,1=yes) If yes make a field named "other2"
$out2="Other2";
## The name of other2

$useou3="0";
## Use the other3 field (0=no,1=yes) If yes make a field named "other 3"
$out3="Other3";
## The name of other3


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


$name="$FORM{'name'}";
$mailto="$FORM{'mailto'}";
$comments="$FORM{'comment'}";

print "Content-type: text/html\n\n"; 
print "Your info has been sent!<BR>\n\n";
print "To return to $site<BR>\n\n";
print "<A HREF=$siteurl>Click Here</A>\n\n";
print "<P><P>\n\n";
print "<A HREF=http://www.d0tt.com>Send mail by Byron</A><BR>\n\n";


## SEND TO USER
open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
print MAIL "To: $mailto\n";
print MAIL "Reply-to: $email\n";
print MAIL "From: $email\n";
print MAIL "Subject: $subject\n";
print MAIL "Thank you for sending me feedback I will reply as soon as I can!\n\n";
print MAIL "You sent me:\n\n";
print MAIL "Name: $name\n";
print MAIL "E-Mail: $mailto\n";
print MAIL "Comments: $comments\n";
if ($useloc eq "1") {
$loc="$FORM{'loc'}";
print MAIL "Location: $loc\n";
}
if ($useurl eq "1") {
$usrurl="$FORM{'url'}";
print MAIL "URL: $usrurl\n";
}

if ($useou1 eq "1") {
$usrou1="$FORM{'other1'}";
print MAIL "$out1: $usrou1\n";
}

if ($useou2 eq "1") {
$usrou2="$FORM{'other2'}";
print MAIL "$out2: $usrou2\n";
}

if ($useou3 eq "1") {
$usrou3="$FORM{'other3'}";
print MAIL "$out3: $usrou3\n";
}
print MAIL " To go back to my homepage go to $siteurl\n\n";
print MAIL "\n\n";
print MAIL "Send mail made by Byron. http://www.d0tt.com";

## SEND TO WEBMASTER
open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
print MAIL "To: $email\n";
print MAIL "Reply-to: $mailto\n";
print MAIL "From: $mailto\n";
print MAIL "Subject: Someone has sent you email from your webpage\n";
print MAIL "Someone has sent you email from your webpage\n\n";
print MAIL "$name has sent you a message:\n\n";
print MAIL "E-Mail: $mailto\n";
print MAIL "Comments: $comments\n";
if ($useloc eq "1") {
$loc="$FORM{'loc'}";
print MAIL "Location: $loc\n";
}
if ($useurl eq "1") {
$usrurl="$FORM{'url'}";
print MAIL "URL: $usrurl\n";
}
if ($useou1 eq "1") {
$usrou1="$FORM{'other1'}";
print MAIL "$out1: $usrou1\n";
}
if ($useou2 eq "1") {
$usrou2="$FORM{'other2'}";
print MAIL "$out2: $usrou2\n";
}
if ($useou3 eq "1") {
$usrou3="$FORM{'other3'}";
print MAIL "$out3: $usrou3\n";
}
print MAIL "\n\n";
print MAIL "Send mail made by Byron. http://www.d0tt.com";