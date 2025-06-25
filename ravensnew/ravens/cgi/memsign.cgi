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
open (DATA, "head.txt");
@data = <DATA>;
close DATA;
foreach $line (@data) {
print "$line";
}
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

if ($con eq "0") {
if ($pass eq $pass2) {
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name2, $passa, $email2, $race2, $class2, $rank, $aprov) = split(/::/, $line);
if ($name eq $name2) {
$val = "1";
}
}

if ($val eq "1") {
print "<CENTER><B>EQ name allready registered</B></CENTER>";
print "<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
}
else {


open (DATA, "data.dat");
@data = <DATA>;
close DATA;
open(DATA, ">data.dat");
print DATA "$INPUT{'name'}::$INPUT{'pass'}::$INPUT{'email'}::$INPUT{'race'}::$INPUT{'class'}::Raven::a\n";
foreach $line (@data) {
print DATA "$line";
}
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

}

}
else {
print "<CENTER><B>Your passwords dident mach</B></CENTER>";
print "<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
}

}



