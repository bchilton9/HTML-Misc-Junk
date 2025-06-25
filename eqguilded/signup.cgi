#!/usr/bin/perl

use DBI;
&get_html;

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

if ($INPUT{'signup_b'} eq "NULL") { &signup_b; }
else { &signup_form; }

##################################################################################

sub signup_b {

$user{'id'} = "";

if ($INPUT{'sur'} eq "NULL") {
$INPUT{'sur'} = "";
}
if ($INPUT{'level'} eq "NULL") {
$INPUT{'level'} = "";
}

$user = "$INPUT{'user'}";
$name = "$INPUT{'name'}";
$sur = "$INPUT{'sur'}";
$pass = "$INPUT{'pass'}";
$email = "$INPUT{'email'}";
$race = "$INPUT{'race'}";
$class = "$INPUT{'class'}";
$level = "$INPUT{'level'}";
 
my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from user WHERE id='$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$user{'id'} = "$user";
 } 

}
$sth->finish; 
$dbh->disconnect; 


if ($user{'id'} ne "") {
print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/Username Taken/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}
else {
my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="INSERT INTO `user` ( `id` , `name` , `sur` , `password` , `email` , `guild` , `class` , `race` , `level` , `created` , `lastactive` ) 
VALUES (
'$user', '$name', '$sur', '$pass', '$email', '', '$class', '$race', '$level', NOW(), NOW())";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/You are now Signed up!<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}

}

##################################################################################

sub signup_form {

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'sign_up_form_html'}/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub get_html {


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from html";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$HTML{$row[0]} = $row[1];


 } 

}
$sth->finish; 
$dbh->disconnect; 


}