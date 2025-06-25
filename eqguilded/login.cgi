#!/usr/bin/perl

require 'cookie.lib';
#require 'html.pl';
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

#$off_page_html =~ s/!!tag!!/""/gi;
#print "$off_page_html";

##################################################################################

if ($INPUT{'login'} eq "NULL") { &login; }
elsif ($INPUT{'logout'} eq "NULL") { &logout; }

##################################################################################

sub login {

$user = "$INPUT{'user'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 


$temp ="select * from user WHERE id='$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

      if ($INPUT{'password'} eq "$row[3]") {

 if ($INPUT{'rember'} eq "true") {
         &SetCookiesSave('user',"$user");
         &SetCookiesSave('pass',"$INPUT{'password'}");
}
else {
         &SetCookies('user',"$user");
         &SetCookies('pass',"$INPUT{'password'}");
}


         print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/You are now logged in<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

      }
else {
         print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/Invalid Password<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

 } 

#if((!$sth->fetchrow_array) and ($row_hit==0)) { 
#print "Content-type: text/html\n\n";
#$HTML{'off_page_html'} =~ s/!!tag!!/User not found<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
#$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
#print "$HTML{'off_page_html'}";
# } 
} 
else { 
print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/Loggin Failed<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

} 



$sth->finish; 
$dbh->disconnect; 
}

##################################################################################

sub logout {

   &SetCookies('user',"");
   &SetCookies('pass',"");
         print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/You are now logged out<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
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