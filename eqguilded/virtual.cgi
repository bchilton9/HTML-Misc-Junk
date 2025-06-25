#!/usr/bin/perl

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


$hostname = $ENV{'REDIRECT_URL'};



my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp ="select * from guild";

$sth=$dbh->prepare($temp);
$sth->execute;

while(@row = $sth->fetchrow_array) { 

$row[0] = "/$row[0]";

if ($row[0] eq "$hostname") {
$server = "$row[8]";
}

} 

$sth->finish; 
$dbh->disconnect; 

if ($server eq "") {
print "Content-Type: text/html\n\n";

print qq~
Page not found
~;
}

else {
$location = "http://www.eqguilded.com/$server$hostname";

print "Content-Type: text/html\n\n";

print qq~
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$location">
<BODY BGCOLOR="#ffffff"><CENTER>
<A HREF=$location>$location</A></CENTER>
~;

}