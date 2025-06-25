#!/usr/bin/perl

######################
# By Keny Misspeller #
# Of Druzzil Ro      #
# for SoS            #
######################

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

use DBI;
use LWP::Simple;

$page = "http://eqplayers.station.sony.com/guild_profile.vm?guildId=459561501316";

$begincut = "Last Played </a></td>";
$endcut = "<td width=\"2\" background=\"/images/main_page_layout/inner_content_right.gif";

$hostname="localhost";
$ms="onestcpb_seekers";
$username ="onestcpb_Daveo";
$password ="s0ulr3aver";


if ($INPUT{'page'} eq "NULL") { &show_page; }
elsif ($INPUT{'roster'} eq "NULL") { &roster; }
elsif ($INPUT{'newshistory'} eq "NULL") { &news_history; }
else { &main; }

sub news_history {
$mypage = "";

## OPEN Table
open (DATA, "./templates/Table.html");
@data = <DATA>;
close DATA;
$mytable = "@data";


## news
my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp ="SELECT * FROM `main_news` ORDER BY `date` DESC";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) {

        $mytableB = $mytable;
        $mytableB =~ s/!!TABLEHEADER!!/$row[1]/gi;
        $mytableB =~ s/!!TABLECONTENT!!/$row[2]/gi;
        $mytableB =~ s/!!DATE!!/$row[3]/gi;

       $mypage = "$mypage $mytableB";
 }


$sth->finish;
$dbh->disconnect;

## Open Main Templet
open (DATA, "./templates/Main_layout.html");
@data = <DATA>;
close DATA;
$HTML = "@data";

$HTML =~ s/!!CONTENT!!/$mypage/gi;

print "Content-type: text/html\n\n";
print "$HTML";
}

sub main {
$mypage = "";

## OPEN Table
open (DATA, "./templates/Table.html");
@data = <DATA>;
close DATA;
$mytable = "@data";


## news
my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp ="SELECT * FROM `main_news` ORDER BY `date` DESC LIMIT 0, 3";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) {

        $mytableB = $mytable;
        $mytableB =~ s/!!TABLEHEADER!!/$row[1]/gi;
        $mytableB =~ s/!!TABLECONTENT!!/$row[2]/gi;
        $mytableB =~ s/!!DATE!!/$row[3]/gi;

       $mynews = "$mynews $mytableB";
 }


$sth->finish;
$dbh->disconnect;


## left boxes
my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp ="SELECT * FROM `main_leftboxs`";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) {

        $mytableB = $mytable;
        $mytableB =~ s/!!TABLEHEADER!!/$row[1]/gi;
        $mytableB =~ s/!!TABLECONTENT!!/$row[2]/gi;
        $mytableB =~ s/!!DATE!!//gi;

       $leftboxes = "$leftboxes $mytableB";
 }


$sth->finish;
$dbh->disconnect;


## right boxes
my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp ="SELECT * FROM `main_rightboxs`";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) {

        $mytableB = $mytable;
        $mytableB =~ s/!!TABLEHEADER!!/$row[1]/gi;
        $mytableB =~ s/!!TABLECONTENT!!/$row[2]/gi;
        $mytableB =~ s/!!DATE!!//gi;

       $rightboxes = " $rightboxes $mytableB";
 }


$sth->finish;
$dbh->disconnect;


## Load Stats
        &get_stats;
        $mystats = $mytable;
        $mystats =~ s/!!TABLEHEADER!!/Guild Stats/gi;
        $mystats =~ s/!!TABLECONTENT!!/$stats/gi;
        $mystats =~ s/!!DATE!!//gi;


## Open Body Templet
open (DATA, "./templates/Home_body.html");
@data = <DATA>;
close DATA;
$mypage = "@data";

$mypage =~ s/!!NEWS!!/$mynews/gi;
$mypage =~ s/!!LEFTBOXS!!/$leftboxes/gi;
$mypage =~ s/!!RIGHTBOXES!!/$rightboxes/gi;
$mypage =~ s/!!STATS!!/$mystats/gi;

## Open Main Templet
open (DATA, "./templates/Main_layout.html");
@data = <DATA>;
close DATA;
$HTML = "@data";

$HTML =~ s/!!CONTENT!!/$mypage/gi;

print "Content-type: text/html\n\n";
print "$HTML";

}

sub roster {
$mypage = "";
$_ = get($page);

$mypage = qq~ <CENTER><TABLE cellspacing="0" cellpadding="2" border="0" align="center" class="forumline" width="700">
         <tr>
           <td class="catLeft" height="28" nowrap="nowrap"><CENTER><span class="cattitle">Rank</span></td>
           <td class="catLeft" nowrap="nowrap"><CENTER><span class="cattitle">Character</span></td>
           <td class="catLeft" nowrap="nowrap"><CENTER><span class="cattitle">Level</span></td>
           <td class="catLeft" nowrap="nowrap"><CENTER><span class="cattitle">Class</span></td>
           <td class="catLeft"><CENTER><span class="cattitle">Last Played</span></td>
~;

 s/^.*$begincut//s;

 s/$endcut.*$//s;

$_ =~ s/class="innerContentData"/class="row1"> <CENTER><span class="forumlink"/gi;
$_ =~ s/a href="character_profile.vm\?characterId\=/b /gi;
$_ =~ s/\/a/\/b/gi;
$_ =~ s/  bgcolor\=\#babed1//gi;
$_ =~ s/  bgcolor\=\#CACEDA//gi;

$mypage = "$mypage $_";

$mypage = qq~$mypage
   </TABLE>
   </CENTER>
~;


open (DATA, "./templates/Main_layout.html");
@data = <DATA>;
close DATA;
$HTML = "@data";

$HTML =~ s/!!CONTENT!!/$mypage/gi;

print "Content-type: text/html\n\n";
print "$HTML";

}

sub show_page {

$mypage = "";

my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp ="SELECT * FROM `main_pages` WHERE name='$INPUT{'p'}'";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) {
       $mypage = " $mypage $row[2] ";
 }

$sth->finish;
$dbh->disconnect;

open (DATA, "./templates/Main_layout.html");
@data = <DATA>;
close DATA;
$HTML = "@data";

$HTML =~ s/!!CONTENT!!/$mypage/gi;

print "Content-type: text/html\n\n";
print "$HTML";
}

sub get_stats {

$stats = "<CENTER><TABLE BORDER=0>";

$mystats = get($page);

$mystats =~ s/\s+//g;

$mystats =~ /<tdclass="innerContentField">Members<\/td><td><divalign="right"class="innerContentData">(.*?)<\/div><\/td>/i;
$stats = "$stats\n<TR><TD>Members:</TD><TD><B>$1</B></TD></TR>";

$mystats =~ /<tdclass="innerContentField">Avg.Level<\/td><td><divalign="right"class="innerContentData">(.*?)<\/div><\/td>/i;
$stats = "$stats\n<TR><TD>Avg. Level:</TD><TD><B>$1</B></TD></TR>";

$mystats =~ /<tdwidth="25%"class="innerContentField">Melee<\/td><tdclass="innerContentData"><divalign="right">(.*?)<\/div>/i;
$stats = "$stats\n<TR><TD>Melee:</TD><TD><B>$1</B></TD></TR>";

$mystats =~ /<tdclass="innerContentField">Casters<\/td><tdwidth="25%"class="innerContentData"><divalign="right">(.*?)<\/div>/i;
$stats = "$stats\n<TR><TD>Casters:</TD><TD><B>$1</B></TD></TR>";

$mystats =~ /<tdclass="innerContentField">Hybrids<\/td><tdclass="innerContentData"><divalign="right">(.*?)<\/div>/i;
$stats = "$stats\n<TR><TD>Hybrids:</TD><TD><B>$1</B></TD></TR>";

$mystats =~ /<tdclass="innerContentField">Priests<\/td><tdclass="innerContentData"><divalign="right">(.*?)<\/div>/i;
$stats = "$stats\n<TR><TD>Priests:</TD><TD><B>$1</B></TD></TR>";

$mystats =~ /<tdclass="innerContentField">GuildTributePoints<\/td><td><divalign="right"class="innerContentData">(.*?)<\/div><\/td>/i;
$stats = "$stats\n<TR><TD>Tribute Points:</TD><TD><B>$1</B></TD></TR>";


$stats = "$stats\n</TABLE>";

}

exit;