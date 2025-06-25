#!/usr/bin/perl

##################################################
## Guestbook 1.0 copyright Byron Chilton        ##
## For more scripts go to http://www.d0tt.com   ##
##                                              ##
##             ###############                  ##
##                                              ##
##  To install this script read the readme.txt  ##
##################################################

$bookname="D0TT.coms";
###The name for your guestbook

$header="header.txt";
###Header file for your guestbook

$footer="footer.txt";
###Footer file for your guestbook

$impath="http://www.d0tt.com";
###Path to the images (pic1.gif,pic2.gif,pic3.gif) no traling /

$adminpass="admin";
###Admins password

$mailprog="/usr/lib/sendmail";
###Your servers sendmail program 

$websend="no";
###Send mail to webmaster when book is signed (yes or no)

$usersend="no";
###Send mail to signer when book is signed (yes or no)

$mail="webmaster\@D0TT.com";
###Webmasters email (make shure thear is a \ before the @ (exp. \@)

$subject="Thank you for signing my guestbook";
###Email to signers subject

$emailcon="thankmail.txt";
###Contents of the email to the signer

####################
### STOP EDITING ###
####################

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
  if($ENV{QUERY_STRING} eq "sign") { &sign }
  else { &book }
  }
if($ENV{'REQUEST_METHOD'} eq "POST") {
  if($INPUT{'submit'} eq "Sign Guestbook") { &signcomf }
  if($INPUT{'submit'} eq "Delete one") { &deletecom }
  if($INPUT{'submit'} eq "Delete All") { &deleteallcom }
  if($INPUT{'submit'} eq "Delete") { &delete }
  if($INPUT{'submit'} eq "Yes") { &deleteall }
if($INPUT{'submit'} eq "Main") { &admin }
if($INPUT{'pass'} eq "$adminpass") { &admin }

}

##SIGN BOOK
sub sign {
print "Content-type: text/html\n\n";
&header;
print "<h3>Sign $bookname Guestbook</H3>\n";
print "<P><FORM ACTION=guestbook.cgi METHOD=POST>\n";
print "<TABLE BORDER=0 CELLPADDING=2>\n";
print "<TR><TD>Your name:</TD><TD>\n";
print "<INPUT TYPE=text NAME=name SIZE=15></TD>\n";
print "</TR><TR><TD>Your E-Mail:</TD><TD>\n";
print "<INPUT TYPE=text NAME=email SIZE=15></TD>\n";
print "</TR><TR><TD>Your Site</TD><TD>\n";
print "http://<INPUT TYPE=text NAME=url SIZE=15></TD>\n";
print "</TR><TR><TD>Comments:</TD>\n";
print "<TD><TEXTAREA NAME=comments COLS=18></TEXTAREA></TD>\n";
print "</TR><TR><TD>How did you find us:</TD><TD>\n";
print "<INPUT TYPE=text NAME=how SIZE=15></TD>\n";
print "</TR><TR><TD>Pic:</TD>\n";
print "<TD><TABLE BORDER CELLPADDING=2><TR><TD>\n";
print "<INPUT TYPE=radio NAME=pic VALUE=pic1.gif></TD>\n";
print "<TD><INPUT TYPE=radio NAME=pic VALUE=pic2.gif></TD>\n";
print "<TD><INPUT TYPE=radio NAME=pic VALUE=pic3.gif></TD>\n";
print "</TR><TR><TD><IMG SRC=$impath/pic1.gif></TD><TD><IMG SRC=$impath/pic2.gif></TD><TD><IMG SRC=$impath/pic3.gif></TD></TR>\n";
print "</TABLE></TD></TR><TR>\n";
print "<TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Sign Guestbook\"></TD>\n";
print "</TR></TABLE></FORM>\n";
&foot;
&logo;
close ();
}

sub signcomf {
open (DATA, "guestbook.data");
@data = <DATA>;
close DATA;

open(FILE, ">guestbook.data");
print FILE "$INPUT{'name'}:$INPUT{'email'}:$INPUT{'url'}:$INPUT{'comments'}:$INPUT{'how'}:$INPUT{'pic'}\n";
foreach $line (@data){
print FILE "$line";
}

close (FILE);

print "Content-type: text/html\n\n";
&header;
print "<P><h3>Thank you for signing my guestbook!</H3>\n";
print "<B>Hear is what you enterd:</B><BR>\n";
print "<B>Name:</B> $INPUT{'name'}<BR>\n";
print "<B>E-Mail:</B> $INPUT{'email'}<BR>\n";
print "<B>URL:</B> $INPUT{'url'}<BR>\n";
print "<B>Comments:</B> $INPUT{'comments'}<BR>\n";
print "<B>How find:</B> $INPUT{'how'}<BR>\n";
print "<B>Pic:</B> <IMG SRC=$impath/$INPUT{'pic'}><BR><P>\n";
print "<A HREF=guestbook.cgi><B>Back to the book</B></A>\n";
&foot;
&logo;

if($usersend eq "yes") {
open (DATA, "$emailcon");
@DATA=<DATA>;
close (DATA);
$econtent = "@DATA";

open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
print MAIL "To: $INPUT{'email'}\n";
print MAIL "Reply-to: $mail\n";
print MAIL "From: $mail\n";
print MAIL "Subject: $subject\n";
print MAIL "$econtent\n";
close (MAIL);
}

if($websend eq "yes") {
open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
print MAIL "To: $mail\n";
print MAIL "Reply-to: $mail\n";
print MAIL "From: $mail\n";
print MAIL "Subject: Your Guestbook has been signed\n";
print MAIL "This is what theay added\n";
print MAIL "Name: $INPUT{'name'}\n";
print MAIL "E-Mail: $INPUT{'email'}\n";
print MAIL "URL: $INPUT{'url'}\n";
print MAIL "Comments: $INPUT{'comments'}\n";
print MAIL "How find: $INPUT{'how'}\n";
print MAIL "Pic: $INPUT{'pic'}\n";
close (MAIL);
}
}

sub book {
print "Content-type: text/html\n\n";
&header;
print "<B><A HREF=guestbook.cgi?sign>Please sign my guestbook</a></B><BR><P>";

open (DATA, "guestbook.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $email, $url, $comments, $how, $pic) = split(/:/, $line);
print "<TABLE BORDER CELLSPACING=0 CELLPADDING=0 WIDTH=30%>\n";
print "<TR><TD><TABLE BORDER=0 CELLSPACING=0 CELLPADDING=2 WIDTH=100%><TR><TD BGCOLOR=808080 WIDTH=10%>\n";
if($email) {
print "<A HREF=mailto:$email>";
}
print "<B>$name</B>";
if($email) {
print "</A>\n";
}
print "</TD><TD BGCOLOR=808080 Width=20% ALIGN=right><IMG SRC=$impath/$pic></TD>\n";
print "</TR><TR><TD BGCOLOR=808080>Comments:</TD>\n";
print "<TD BGCOLOR=c0c0c0>$comments</TD></TR>\n";
if($url) {
print "<TR><TD BGCOLOR=808080>Webpage:</TD>\n";
print "<TD BGCOLOR=c0c0c0><A HREF=http://$url>$url</A></TD></TR>\n";
}
if($how) {
print "<TR><TD BGCOLOR=808080>How found us:</TD>\n";
print "<TD BGCOLOR=c0c0c0>$how</TD></TR>\n";
}
print "</TABLE></TD></TR></TABLE><P>\n";
}
&foot;
&logo;
close ();
}

sub adminlogin {
print "Content-type: text/html\n\n";
&head;
print "<FORM ACTION=guestbook.cgi METHOD=POST>";
print "Password: <INPUT TYPE=password NAME=pass><BR>";
print "<INPUT TYPE=submit VALUE=Login></FORM>";
close ();
}

sub admin {
print "Content-type: text/html\n\n";
&head;
print "<FORM ACTION=guestbook.cgi METHOD=POST>";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Delete one\"><INPUT TYPE=submit NAME=submit VALUE=\"Delete All\"></FORM>";
&logo;
close ();
}

sub logo {
print "<HR COLOR=blue><CENTER><B>Ran with Guestbook 1.0</B><BR>";
print "Free from <A HREF=http://www.d0tt.com>www.d0tt.com</A>";
}


sub header {
open (HEAD, "$header");
@DATA=<HEAD>;
close (HEAD);
foreach $line (@DATA){
print "$line";
}
}
sub foot {
open (FOOT, "$footer");
@DATA2=<FOOT>;
close (FOOT);
foreach $line (@DATA2){
print "$line";
}
}

sub deletecom {
print "Content-type: text/html\n\n";
&head;
print "<FORM ACTION=guestbook.cgi METHOD=POST>\n";
print "<TABLE BORDER CELLPADDING=2>\n";
print "<TR><TD>Delete:</TD><TD>Name:</TD><TD>Email:</TD><TD>Comments</TD></TR>\n";

$i=0;
open (DATA, "guestbook.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i++;
chomp ($line);
($name, $email, $url, $comments, $how, $pic) = split(/:/, $line);

print "<TR><TD><INPUT TYPE=radio NAME=line VALUE=$i>\n";
print "</TD><TD>$name</TD><TD>$email</TD><TD>$comments</TD></TR>\n";
}
print "<TR><TD COLSPAN=4><P ALIGN=Center>$i people have signed</TD></TR>\n";
print "<TR><TD COLSPAN=4><P ALIGN=Center>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Delete\"></TD>\n";
print "</TR></TABLE></FORM>\n";
&reload;
}

sub delete {
$a=0;
open (DATA, "guestbook.data");
@data = <DATA>;
close DATA;

open(FILE, ">guestbook.data");
	foreach $line (@data) {
	$a++;
	if ($a eq "$INPUT{'line'}") {
		print FILE "";
		}
	else {
		print FILE "$line";
		}
	}
close (FILE);

print "Content-type: text/html\n\n";
&head;
print "Deleted!";
&reload;
}

sub head {
print "<CENTER><h3>GuestBook 1.0</H3><hr color=blue>";
}

sub deleteallcom {
print "Content-type: text/html\n\n";
&head;
print "<h2><font color=red>WARNING!!</font></H2><BR>";
print "This will delete all your guestbook data!!<BR>Are you shure you want to do this?<BR>";
print "<FORM ACTION=guestbook.cgi METHOD=POST>";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Yes\"></FORM>";
&reload;
}

sub deleteall {
open(FILE, ">guestbook.data");
print FILE "";
close (FILE);
print "Content-type: text/html\n\n";
&head;
print "All data has been deleted";
&reload;
}

sub reload {
print "<BR><FORM ACTION=guestbook.cgi METHOD=POST>";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Main\"></FORM>";
}