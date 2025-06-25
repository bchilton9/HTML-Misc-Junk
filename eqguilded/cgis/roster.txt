#!/usr/bin/perl

require '../../cookie.lib';
require 'config.pl';
use DBI;

&get_html;
&get_guild;
&main;

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
    $INPUT{$name} = $value;
}

##################################################################################

sub main {

print "Content-type: text/html\n\n";

my $dbhc = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $rankdb";

if($sthc=$dbhc->prepare($temp)) 
{ 
 $sthc->execute;  #Execute the query 

 while((@rowc=$sthc->fetchrow_array)!=NULL) { 
          $rowc_hit=1;



my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $userdb WHERE aproved='true' and rank='$rowc[0]'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;


my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from user WHERE id='$row[0]'";

if($sthb=$dbhb->prepare($temp)) 
{ 
 $sthb->execute;  #Execute the query 

 while((@rowb=$sthb->fetchrow_array)!=NULL) { 
          $rowb_hit=1;

$roster_line = "";
$roster_line = "$HTML{'roster_line_html'}";

$roster_line =~ s/!!name!!/$rowb[1]/gi;
$roster_line =~ s/!!sur!!/$rowb[2]/gi;
$roster_line =~ s/!!level!!/$rowb[8]/gi;
$roster_line =~ s/!!rank!!/$row[2]/gi;
$roster_line =~ s/!!class!!/$rowb[6]/gi;
$roster_line =~ s/!!race!!/$rowb[7]/gi;
$roster = "$roster $roster_line";

 } 

}
$sthb->finish; 
$dbhb->disconnect; 

 } 

}
$sth->finish; 
$dbh->disconnect; 

}
}
$sthc->finish; 
$dbhc->disconnect; 

$content = "$HTML{'roster_head_html'} $roster $HTML{'roster_foot_html'}";

$HTML{'off_page_html'} =~ s/!!content!!/$content/gi;
$HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
$HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
$HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
print "$HTML{'off_page_html'}";



}

##################################################################################

sub get_html {


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $htmldb";

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

##################################################################################

sub get_guild {

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($guild eq "$row[0]") {
$guildname = "$row[1]";
$goldexp = "$row[4]";
$server = "$row[8]";
$counterimg = "$row[9]";
}


 } 

}
$sth->finish; 
$dbh->disconnect; 

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

$mon = $mon + 1;
$year = $year + 1900;

($eyear, $emon, $emday) = split(/-/, $goldexp);

if ($eyear eq $year) {

if ($emon < $mon) { $stats = "Silver"; }

elsif ($emon eq $mon) {
    if ($emday < $mday) { $stats = "Silver"; }
    else { $stats = "Gold"; }
} # END MONTH

elsif ($mon < $emon) { $stats = "Gold"; }

} # END YEAR

elsif ($eyear > $year) { $stats = "Gold"; }
else { $stats = "Silver"; }


if ($stats eq "Gold") {

$headbanner = "";
$footbanner = "";

}

else {

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from html";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$MAINHTML{$row[0]} = $row[1];

 } 

}
$sth->finish; 
$dbh->disconnect; 

$headbanner = "$MAINHTML{'header_banner_html'}";
$footbanner = "$MAINHTML{'footer_banner_html'}";
}


}