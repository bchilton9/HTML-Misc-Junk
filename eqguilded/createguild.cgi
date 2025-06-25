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

if ($INPUT{'do'} eq "create_guild") { &create_guild; }
else { &main; }

##################################################################################

sub main {

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_create_form_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub create_guild {

&get_user;

$guild = "$INPUT{'guild'}";
$longname = "$INPUT{'longname'}";
$password = "$INPUT{'pass'}";
$email = "$INPUT{'email'}";
$server = "$INPUT{'server'}";


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp ="select * from guild WHERE shortname ='$guild'";

$sth=$dbh->prepare($temp);
$sth->execute;

while(@row = $sth->fetchrow_array) { 

$check = "$row[0]";

} 

$sth->finish; 
$dbh->disconnect; 


if ($check eq "") {

&build_guild_files;

$HTML{'guild_create_finish_html'} =~ s/!!URL!!/http:\/\/www.eqguilded.com\/$guild/gi;
$HTML{'guild_create_finish_html'} =~ s/!!URLB!!/http:\/\/www.eqguilded.com\/$server\/$guild/gi;

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_create_finish_html'}/gi;
print "$HTML{'off_page_html'}";

}
else {

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/Guild Short Name Taken<BR>Please try agine!<BR>$HTML{'guild_create_form_html'}/gi;
print "$HTML{'off_page_html'}";

}

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

open (DATA, "./cgis/temp/default/main_page_html.txt");
@data = <DATA>;
close DATA;
$main_page_html = "@data";

open (DATA, "./cgis/temp/default/log_box_html_in.txt");
@data = <DATA>;
close DATA;
$log_box_html_in = "@data";

open (DATA, "./cgis/temp/default/log_box_html_out.txt");
@data = <DATA>;
close DATA;
$log_box_html_out = "@data";

open (DATA, "./cgis/temp/default/news_box_html.txt");
@data = <DATA>;
close DATA;
$news_box_html = "@data";

open (DATA, "./cgis/temp/defalt/off_page_html.txt");
@data = <DATA>;
close DATA;
$off_page_html = "@data";

open (DATA, "./cgis/temp/default/roster_line_html.txt");
@data = <DATA>;
close DATA;
$roster_line_html = "@data";

open (DATA, "./cgis/temp/default/roster_head_html.txt");
@data = <DATA>;
close DATA;
$roster_head_html = "@data";

open (DATA, "./cgis/temp/default/roster_foot_html.txt");
@data = <DATA>;
close DATA;
$roster_foot_html = "@data";

open (DATA, "./cgis/temp/default/links_html.txt");
@data = <DATA>;
close DATA;
$links_html = "@data";

open (DATA, "./cgis/temp/default/forum_main_html.txt");
@data = <DATA>;
close DATA;
$forum_main_html = "@data";

open (DATA, "./cgis/temp/default/forum_post_html.txt");
@data = <DATA>;
close DATA;
$forum_post_html = "@data";

open (DATA, "./cgis/temp/default/forum_thread_html.txt");
@data = <DATA>;
close DATA;
$forum_thread_html = "@data";

open (DATA, "./cgis/temp/default/forum_topic_html.txt");
@data = <DATA>;
close DATA;
$forum_topic_html = "@data";

open (DATA, "./cgis/temp/default/forum_view_main_html.txt");
@data = <DATA>;
close DATA;
$forum_view_main_html = "@data";

open (DATA, "./cgis/temp/default/forum_view_thred_html.txt");
@data = <DATA>;
close DATA;
$forum_view_thred_html = "@data";


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

###################
## CREATE TABLES ##
###################

## PHOTO ALBUM TABLE
$temp = "CREATE TABLE `$albumdb` (`album` text NOT NULL) TYPE=MyISAM";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## PHOTO DATABASE TABLE
$temp = "CREATE TABLE `$photodb` (`album` text NOT NULL, `image` text NOT NULL, `discription` text NOT NULL) TYPE=MyISAM";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## HTML TABLE
$temp = "CREATE TABLE `$htmldb` (`name` varchar(25) NOT NULL default '', `content` text NOT NULL, `useheader` varchar(10) NOT NULL default '') TYPE=MyISAM";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## NEWS TABLE
$temp = "CREATE TABLE `$newsdb` (`date` date NOT NULL default '0000-00-00', `news` text NOT NULL) TYPE=MyISAM";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## PAGES TABLE
$temp = "CREATE TABLE `$pagesdb` (`name` varchar(25) NOT NULL default '', `content` text NOT NULL) TYPE=MyISAM";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## RANKS TABLE
$temp = "CREATE TABLE `$ranksdb` (`name` text NOT NULL) TYPE=MyISAM";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## USER TABLE
$temp = "CREATE TABLE `$userdb` (`name` varchar(25) NOT NULL default '', `access` varchar(25) NOT NULL default '', `rank` text NOT NULL, `type` text NOT NULL, `points` varchar(25) NOT NULL default '', `aproved` varchar(25) NOT NULL default '') TYPE=MyISAM";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## FORUMS TABLE
$temp = "CREATE TABLE `$formsdb` (`id` int(11) NOT NULL auto_increment, `forum` text, `description` text, PRIMARY KEY  (`id`)) TYPE=MyISAM AUTO_INCREMENT=3";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## POSTS TABLE
$temp = "CREATE TABLE `$postsdb` (`id` int(11) NOT NULL auto_increment, `name` text, `message` longtext, `subject` text, `ip` text, `thread` int(11) default NULL, `topic` text, `forum` text, `date` text, `sticky` varchar(10) NOT NULL default '', `locked` varchar(10) NOT NULL default '', PRIMARY KEY  (`id`)) TYPE=MyISAM AUTO_INCREMENT=24";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

##########################
## INSERT DEFALT VALUES ##
##########################

## HTML TABLE
$temp = "INSERT INTO `$htmldb` VALUES ('main_page_html', '$main_page_html', 'true')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('log_box_html_in', '$log_box_html_in', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('log_box_html_out', '$log_box_html_out', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('news_box_html', '$news_box_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('off_page_html', '$off_page_html', 'true')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('roster_line_html', '$roster_line_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('roster_head_html', '$roster_head_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('roster_foot_html', '$roster_foot_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('links_html', '$links_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_main_html', '$forum_main_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_post_html', '$forum_post_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_thread_html', '$forum_thread_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_topic_html', '$forum_topic_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_view_main_html', '$forum_view_main_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_view_thred_html', '$forum_view_thred_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## NEWS TABLE
$temp = "INSERT INTO `$newsdb` VALUES (NOW( ), 'Dynamic News Boxes! To update go into your Edit Settings and select Add/Delete News.')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## RANKS TABLE
$temp = "INSERT INTO `$ranksdb` VALUES ('Guild-Leader')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$ranksdb` VALUES ('Assistant-Guild-Leader')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$ranksdb` VALUES ('Officer')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$ranksdb` VALUES ('Member')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

## USER TABLE
$temp = "INSERT INTO `$userdb` VALUES ('$user', 'Master', 'Guild-Leader', 'Officer', '0', 'true')";
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
$temp="UPDATE `user` SET `guild` = '$guild' WHERE `id` = '$user' LIMIT 1"; 
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

## GET SERVER

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM server HAVING `server` = '$server'";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
        $row_hit=1;
$server = "$row[1]";
 } 

}

$sth->finish; 
$dbh->disconnect; 

## CREATE FOLDER

mkdir("/home/eqguild/public_html/$server/$guild", 0755);

## CREATE CGIS

open (DATA, "./cgis/index.txt");
@data = <DATA>;
close DATA;
open(DATA, ">./$server/$guild/index.cgi");
print DATA "@data";
close DATA;

open (DATA, "./cgis/page.txt");
@data = <DATA>;
close DATA;
open(DATA, ">./$server/$guild/page.cgi");
print DATA "@data";
close DATA;

open (DATA, "./cgis/roster.txt");
@data = <DATA>;
close DATA;
open(DATA, ">./$server/$guild/roster.cgi");
print DATA "@data";
close DATA;

open (DATA, "./cgis/forum.txt");
@data = <DATA>;
close DATA;
open(DATA, ">./$server/$guild/forum.cgi");
print DATA "@data";
close DATA;

open(DATA, ">./$server/$guild/config.pl");
print DATA "\$htmldb = \"$guild\_html\"\;\n";
print DATA "\$newsdb = \"$guild\_news\"\;\n";
print DATA "\$albumdb = \"$guild\_album\"\;\n";
print DATA "\$photodb = \"$guild\_photo\"\;\n";
print DATA "\$userdb = \"$guild\_user\"\;\n";
print DATA "\$pagesdb = \"$guild\_pages\"\;\n";
print DATA "\$rankdb = \"$guild\_ranks\"\;\n";
print DATA "\$linkdb = \"$guild\_links\"\;\n";
print DATA "\$postsdb = \"$guild\_posts\"\;\n";
print DATA "\$formsdb = \"$guild\_forums\"\;\n";
print DATA "\$guild = \"$guild\"\;\n";
close DATA;

## CMOD

chmod_file("./$server/$guild/index.cgi", "0755");
chmod_file("./$server/$guild/page.cgi", "0755");
chmod_file("./$server/$guild/roster.cgi", "0755");
chmod_file("./$server/$guild/forum.cgi", "0755");
chmod_file("./$server/$guild/config.pl", "0777");

## ADD INFO TO GUILD DB

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="INSERT INTO `guild` ( `shortname` , `longname` , `password` , `email` , `goldexp` , `stats` , `createdon` , `createdby` , `server` , `counterimage` ) VALUES ('$guild', '$longname', '$password', '$email', '0000-00-00' , '', NOW( ) , '$user', '$server', '1')"; 
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

##########
## DONE ##
##########

}

##################################################################################

sub chmod_file {
my ($destination, $permissions) = @_;
chmod(oct($permissions), $destination)
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
