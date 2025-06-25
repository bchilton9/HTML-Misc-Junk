#!/usr/bin/perl

require 'cookie.lib';
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
    $INPUT{$name} = $value;
}

##################################################################################

if ($INPUT{'do'} eq "delete_guild") { &delete_guild; }
else { &main; }

##################################################################################

sub main {

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_delete_site_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub delete_guild {

&get_user;

$guild = "$user{'guild'}";


&build_guild_files;

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_delete_finish_html'}/gi;
print "$HTML{'off_page_html'}";


}

##################################################################################

sub build_guild_files {

$albumdb = "$guild album";
$albumdb =~ s/ /_/gi;

$htmldb = "$guild html";
$htmldb =~ s/ /_/gi;

$newsdb = "$guild news";
$newsdb =~ s/ /_/gi;

$pagesdb = "$guild pages";
$pagesdb =~ s/ /_/gi;

$photodb = "$guild photo";
$photodb =~ s/ /_/gi;

$ranksdb = "$guild ranks";
$ranksdb =~ s/ /_/gi;

$userdb = "$guild user";
$userdb =~ s/ /_/gi;

$postsdb = "$guild posts";
$postsdb =~ s/ /_/gi;

$formsdb = "$guild forums";
$formsdb =~ s/ /_/gi;

## GET SERVER

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($guild eq "$row[0]") {
$server = "$row[8]";
}


 } 

}
$sth->finish; 
$dbh->disconnect;


####################
## REMOVE MEMBERS ##
####################

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from `$userdb`";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1; 


my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 
$temp="UPDATE `user` SET `guild` = '' WHERE `id` = '$row[0]'";
$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;



 } 

}
$sth->finish; 
$dbh->disconnect; 



my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

###################
## DELETE TABLES ##
###################

## PHOTO ALBUM TABLE
$temp = "DROP TABLE `$albumdb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## PHOTO DATABASE TABLE
$temp = "DROP TABLE `$photodb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## HTML TABLE
$temp = "DROP TABLE `$htmldb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## NEWS TABLE
$temp = "DROP TABLE `$newsdb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## PAGES TABLE
$temp = "DROP TABLE `$pagesdb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## RANKS TABLE
$temp = "DROP TABLE `$ranksdb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## USER TABLE
$temp = "DROP TABLE `$userdb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## FORUMS TABLE
$temp = "DROP TABLE `$formsdb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## POSTS TABLE
$temp = "DROP TABLE `$postsdb`";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

######################
## DONE WITH TABLES ##
######################

$dbh->disconnect;

## SET GUILD IN USERFILES

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="UPDATE `user` SET `guild` = '' WHERE `id` = '$user' LIMIT 1"; 
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

## DELETE CGIS

unlink ("./$server/$guild/index.cgi");
unlink ("./$server/$guild/page.cgi");
unlink ("./$server/$guild/roster.cgi");
unlink ("./$server/$guild/forum.cgi");
unlink ("./$server/$guild/config.pl");

## DELETE FOLDER

rmdir("/home/eqguild/public_html/$server/$guild");

## REMOVE INFO TO GUILD DB

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="DELETE FROM `guild` WHERE `shortname` = '$guild' LIMIT 1";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

##########
## DONE ##
##########

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
