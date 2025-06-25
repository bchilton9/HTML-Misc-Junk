#!/usr/bin/perl

require 'cookie.lib';
#require 'html.pl';
use DBI;

&get_html;

## print <<"HTML";
## $content =~ s/!!var!!/$var/gi;
## print "Content-type: text/html\n\n";


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
$HTML{'main_page_html'} =~ s/!!logbox!!/$HTML{'log_box_html_in'}/gi;
}
else {
$HTML{'main_page_html'} =~ s/!!logbox!!/$HTML{'log_box_html_out'}/gi;
}

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM server ORDER BY server";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
        $row_hit=1;
$serverlist = "$serverlist <OPTION>$row[0]\n";
 } 

}
$sth->finish; 
$dbh->disconnect; 


$HTML{'main_page_html'} =~ s/!!serverlist!!/$serverlist/gi;
$HTML{'main_page_html'} =~ s/!!maincontent!!/$HTML{'main_content_html'}/gi;
$HTML{'main_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'main_page_html'} =~ s/!!rightblocks!!/$HTML{'right_blocks_html'}/gi;
$HTML{'main_page_html'} =~ s/!!news!!/$news/gi;

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

}

##################################################################################

sub get_news {

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT  * 
FROM  `news` 
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
$news_box =~ s/!!tag!!/$row[1]/gi;
$news = "$news $news_box";


 } 

}
$sth->finish; 
$dbh->disconnect; 


}

##################################################################################

sub news_history {

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT  * 
FROM  `news` 
ORDER BY `date` DESC";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$news_box = "";
$news_box = "$HTML{'news_box_html'}";

$news_box =~ s/!!date!!/$row[0]/gi;
$news_box =~ s/!!tag!!/$row[1]/gi;
$news = "$news $news_box";


 } 

}
$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/$news/gi;
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
