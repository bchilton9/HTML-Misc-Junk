#!/usr/bin/perl

require '../../cookie.lib';
require 'config.pl';
use DBI;

&get_html;
&get_guild;

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

if ($INPUT{'show'} eq "news_history") { &news_history; }
else { &main; }

##################################################################################

sub main {

&get_user;

&get_news;

print "Content-type: text/html\n\n";

if ($user ne "") {

$msg_cnt = 0;


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * 
FROM messages
HAVING `to` = '$user'";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
        $row_hit=1;
$msg_cnt++;
 } 

}
$sth->finish; 
$dbh->disconnect; 

$HTML{'log_box_html_in'} =~ s/!!name!!/$user{'name'}/gi;
$HTML{'log_box_html_in'} =~ s/!!sur!!/$user{'sur'}/gi;
$HTML{'log_box_html_in'} =~ s/!!messages!!/$msg_cnt/gi;
$HTML{'log_box_html_in'} =~ s/!!points!!/$user{'points'}/gi;
$HTML{'main_page_html'} =~ s/!!logbox!!/$HTML{'log_box_html_in'}/gi;
}
else {
$HTML{'main_page_html'} =~ s/!!logbox!!/$HTML{'log_box_html_out'}/gi;
}

$counter = "<IMG SRC=\"http://www.eqguilded.com/counter.cgi?i=$counterimg&guild=$guild\">";

$HTML{'main_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
$HTML{'main_page_html'} =~ s/!!news!!/$news/gi;
$HTML{'main_page_html'} =~ s/!!guildname!!/$guildname/gi;
$HTML{'main_page_html'} =~ s/!!counter!!/$counter/gi;

$HTML{'main_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
$HTML{'main_page_html'} =~ s/!!footbanner!!/$footbanner/gi;

print "$HTML{'main_page_html'}";

}

##################################################################################

sub get_user {

&GetCookies('user');

$user = "$Cookies{'user'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from user WHERE id='$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$user{'id'} = "$user";
$user{'name'} = "$row[1]";
$user{'sur'} = "$row[2]";
$user{'pass'} = "$row[3]";
$user{'email'} = "$row[4]";
$user{'guild'} = "$row[5]";
$user{'class'} = "$row[6]";
$user{'race'} = "$row[7]";
$user{'level'} = "$row[8]";
$user{'datecreated'} = "$row[9]";
$user{'dateactave'} = "$row[10]";
 } 

}
$sth->finish; 
$dbh->disconnect; 


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $userdb WHERE name='$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$user{'access'} = "$row[1]";
$user{'rank'} = "$row[2]";
$user{'type'} = "$row[3]";
$user{'points'} = "$row[4]";

 } 

}
$sth->finish; 
$dbh->disconnect;

}

##################################################################################

sub get_news {

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT  * 
FROM  `$newsdb` 
ORDER BY `date` DESC
LIMIT 0, 5";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$news_box = "";
$news_box = "$HTML{'news_box_html'}";

$news_box =~ s/!!date!!/$row[0]/gi;
$news_box =~ s/!!news!!/$row[1]/gi;
$news = "$news $news_box";


 } 

}
$sth->finish; 
$dbh->disconnect; 


}

##################################################################################

sub news_history {

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT  * 
FROM  `$newsdb` 
ORDER BY `date` DESC";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$news_box = "";
$news_box = "$HTML{'news_box_html'}";

$news_box =~ s/!!date!!/$row[0]/gi;
$news_box =~ s/!!news!!/$row[1]/gi;
$news = "$news $news_box";


 } 

}
$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
$HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
$HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
$HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
$HTML{'off_page_html'} =~ s/!!content!!/$news/gi;
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

##################################################################################
