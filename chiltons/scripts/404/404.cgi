#!/usr/bin/perl

$site = "D0TT.com";
$mail = "crashtest\@d0tt.com";
$url = "http://www.d0tt.com";
$pass = "admin";

##############

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
  else { &s404 }
  }
elsif($ENV{'REQUEST_METHOD'} eq "POST") {
  if($INPUT{'password'} eq "$pass") { &admin }
if($INPUT{'submit'} eq "Delete All") { &delete }
}

##Delete 404s
sub delete {
print "Content-type: text/html\n\n";
print "<CENTER><H3>404 logger: All 404s deleted</H3><HR COLOR=blue>";
print "<P><P>404 logger by <A href=http://www.d0tt.com>Byron</A>";

open(FILE, ">404.data");
print FILE "end:end:end";
close (FILE);
}

##Admin
sub admin {
print "Content-type: text/html\n\n";
print "<CENTER><H3>404 logger: Admin</H3><HR COLOR=blue>";

open (DATA, "404.data");
@data = <DATA>;
close DATA;

foreach $line (@data){
chomp ($line);
($page, $ip, $date) = split(/:/, $line);
if ($page eq "end") {
print "No 404s";
}
else {
print "<B>\"$page\"</B><BR>Wasen't found on \"$date\" by ip# \"$ip\"<BR>";
}
}
print "<FORM ACTION=404.cgi METHOD=POST>";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Delete All\">";
print "<P><P><HR COLOR=blue>404 logger by <A href=http://www.d0tt.com>Byron</A>";
}

##Admin login
sub adminlogin {
print "Content-type: text/html\n\n";
print "<CENTER><H3>404 logger: login</H3><HR COLOR=blue>";
print "<FORM ACTION=404.cgi METHOD=POST>";
print "Password: <INPUT TYPE=password NAME=password><BR>";
print "<INPUT TYPE=submit VALUE=Login>";
print "<P><P><HR COLOR=blue>404 logger by <A href=http://www.d0tt.com>Byron</A>";
}

##404
sub s404 {
print "Content-type: text/html\n\n";
print "<CENTER><H2>404 error: Not found</H2><HR COLOR=blue>";
print "<B>The file you are looking for was not found at $site</B><BR>";
print "Go to <a href=$url>$site</A> and try to find what your looking for.<BR>";
print "If you got this error off of my site please <a href=mailto:$mail>E-Mail</A> me.";
print "<P><P><HR COLOR=blue>404 logger by <A href=http://www.d0tt.com>Byron</A>";

open (DATA, "404.data");
@data = <DATA>;
close DATA;

$data = "@data";

if ($data eq "end:end:end") {
open(FILE, ">404.data");
print FILE "$ENV{'HTTP_REFERER'}:$ENV{'REMOTE_ADDR'}:date\n";
close (FILE);
}

else {
open(FILE, ">404.data");
print FILE "$ENV{HTTP_REFERER}:$ENV{'REMOTE_ADDR'}:date\n";
foreach $line (@data){
print FILE "$line";
}
close (FILE);
}
}