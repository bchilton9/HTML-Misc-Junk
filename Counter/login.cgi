#!/usr/bin/perl

require 'cookie.lib';
use DBI;


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
if ($value eq "") { $value = "NULL"; }
    $INPUT{$name} = $value;
}

##################################################################################

if ($INPUT{'login'} eq "NULL") { &login; }
elsif ($INPUT{'logout'} eq "NULL") { &logout; }

##################################################################################

sub login {

$user = "$INPUT{'username'}";
$pass = "$INPUT{'password'}";

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 


$temp ="SELECT * FROM `user` WHERE  `username` = '$user'";

if($sth=$dbh->prepare($temp)) 
{ 
    $sth->execute;  #Execute the query 

    while((@row=$sth->fetchrow_array)!=NULL) { 
       $row_hit=1;
 
       if ($row[1] ne "$user") {
          print "Content-type: text/html\n\n";
          print "User not found";
          exit;
       }
       elsif ($row[3] ne "$pass") {
          print "Content-type: text/html\n\n";
          print "Invalid Password";
          exit;
       }
       else {

             &SetCookiesSave('user',"$user");
             &SetCookiesSave('pass',"$pass");
  
          print "Content-type: text/html\n\n";
print qq~
<HTML>
<HEAD>
<META HTTP-EQUIV="Refresh" CONTENT="5;URL=index.cgi?do=cp">
<TITLE>Please wate.</TITLE>
</HEAD>
<BODY>
Please wate or click <A HREF="index.cgi?do=cp">here</A>.
</BODY>
</HTML>
~;
          exit;

       }

    }      
}

$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";
print "Login Failure";
exit;

}

##################################################################################

sub logout {

   &SetCookies('user',"");
   &SetCookies('pass',"");

print "Content-type: text/html\n\n";
print qq~
<HTML>
<HEAD>
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=index.cgi">
<TITLE>Please wate.</TITLE>
</HEAD>
<BODY>
Please wate or click <A HREF="index.cgi">here</A>.
</BODY>
</HTML>
~;


}

##################################################################################
