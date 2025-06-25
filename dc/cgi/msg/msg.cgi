#!/usr/bin/perl

require '../cookie.lib';

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

print "Content-type: text/html\n\n";
&GetCookies('user');

##################################################################################

if ($Cookies{'user'} eq "") { &error; }
else {

if ($INPUT{'a'} eq "list") { &list; }
elsif ($INPUT{'a'} eq "Read") { &read }
elsif ($INPUT{'a'} eq "Delete") { &delete }
elsif ($INPUT{'a'} eq "Reply") { &send }
elsif ($INPUT{'a'} eq "Send Message") { &sendmessage }
}

##################################################################################

sub list {
$count = "0";

open (DATA, "dat/$Cookies{'user'}.msg");
@data = <DATA>;
foreach $line (@data) {
chomp ($line);
($sender, $sub, $num) = split(/::/, $line);


open (FILE,"../tmps/message_list_msg.tmp");
while (<FILE>) { $file_content_a.=$_; }
$file_content_a =~ s/!!msgfrom!!/$sender/gi;
$file_content_a =~ s/!!msgnum!!/$num/gi;
$file_content_a =~ s/!!subject!!/$sub/gi;
close (FILE);


$count = "1";
}
close DATA;

if ($count eq "0") {
$file_content_a = "<B>No Messages</B>";
}

$file = "message_list.tmp";
&output;

}

##################################################################################

sub read {


open (DATA, "msges/$INPUT{'msgnum'}");
@data = <DATA>;
close DATA;


$mymsg = "@data";


$file = "message_list_view.tmp";
&output;

}

##################################################################################

sub delete {
open(DATA, "dat/$Cookies{'user'}.msg");
@data = <DATA>;
close DATA;
open(DATA, ">dat/$Cookies{'user'}.msg");
foreach $line (@data) {
chomp ($line);
($sender, $sub, $num) = split(/::/, $line);
if ($num eq "$INPUT{'msgnum'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}
close DATA;

unlink("msges/$INPUT{'msgnum'}");

$file = "message_list_delete.tmp";
&output;
}

##################################################################################

sub send{
$file = "message_send.tmp";
&output;
}

##################################################################################

sub sendmessage {

$file = "message_sent.tmp";
&output;

open (FILE, "count.txt");
flock (FILE, 2);
$abcdefg = <FILE>;
chop ($abcdefg);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$abcdefg++;

open(DATA, ">count.txt");
print DATA "$abcdefg\n";
print DATA "junk\n";
close DATA;


open (DATA, "dat/$INPUT{'sender'}.msg");
@data = <DATA>;
close DATA;

open(DATA, ">dat/$INPUT{'sender'}.msg");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$Cookies{'user'}::$INPUT{'sub'}::$abcdefg\n";
close DATA;

open (FILE,"../tmps/message.tmp");
while (<FILE>) { $file_content_a.=$_; }
$file_content_a =~ s/!!msgnum!!/$abcdefg/gi;
$file_content_a =~ s/!!from!!/$Cookies{'user'}/gi;
$file_content_a =~ s/!!name!!/$INPUT{'sender'}/gi;
$file_content_a =~ s/!!subject!!/$INPUT{'sub'}/gi;
$file_content_a =~ s/!!message!!/$INPUT{'message'}/gi;
close (FILE);

open(DATA, ">msges/$abcdefg");
print DATA "$file_content_a";
close DATA;
}

##################################################################################

sub output {

####STARTNEWS
open (DATA, "news.dat");
@data = <DATA>;
close DATA;
$news = "@data";
####ENDNEWS
####STARTOFFICERNEWS
open (DATA, "officernews.dat");
@data = <DATA>;
close DATA;
$offnews = "@data";
####ENDOFFICERNEWS
####STARTMESSAGE
$count = "0";
open (DATA, "msg/dat/$Cookies{'user'}.msg");
@data = <DATA>;
foreach $line (@data) {
$count++;
}
close DATA;
if ($count eq "0") {
$message = "<SMALL>You Have No Messages</SMALL>";
}
else {
$message = "<A HREF=$cgipath/msg/msg.cgi?a=list><SMALL>You have $count Messages</SMALL></A>";
}
####ENDMESSAGE
##################################################################################
$memb = "0";
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$memb = $memb + 1;
}
$altnum = "0";
open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$altnum = $altnum + 1;
}
$members = $memb + $altnum;
##################################################################################
####STARTHEADER
open (DATA, "../tmps/header.tmp");
@data = <DATA>;
close DATA;
$header = "@data";
####ENDHEADER

$imgpath = "$imgpath/$INPUT{'img'}";

open (FILE,"../tmps/$file");
while (<FILE>) { $file_content.=$_; }
$file_content =~ s/!!header!!/$header/gi;
$file_content =~ s/!!news!!/$news/gi;
$file_content =~ s/!!officernews!!/$offnews/gi;
$file_content =~ s/!!visitlist!!/$visit/gi;
$file_content =~ s/!!cookieuser!!/$Cookies{'user'}/gi;
$file_content =~ s/!!guildname!!/$guildname/gi;
$file_content =~ s/!!guildemail!!/$guildemail/gi;
$file_content =~ s/!!viewname!!/$INPUT{'user'}/gi;
$file_content =~ s/!!viewsir!!/$sir/gi;
$file_content =~ s/!!viewlvl!!/$lvl/gi;
$file_content =~ s/!!viewclass!!/$class/gi;
$file_content =~ s/!!viewrace!!/$race/gi;
$file_content =~ s/!!viewsay!!/$say/gi;
$file_content =~ s/!!viewimage!!/$img/gi;
$file_content =~ s/!!viewac!!/$ac/gi;
$file_content =~ s/!!viewatk!!/$atk/gi;
$file_content =~ s/!!viewstr!!/$str/gi;
$file_content =~ s/!!viewsta!!/$sta/gi;
$file_content =~ s/!!viewagi!!/$agi/gi;
$file_content =~ s/!!viewdex!!/$dex/gi;
$file_content =~ s/!!viewwis!!/$wis/gi;
$file_content =~ s/!!viewint!!/$int/gi;
$file_content =~ s/!!viewcha!!/$cha/gi;
$file_content =~ s/!!useremail!!/$email/gi;
$file_content =~ s/!!memnum!!/$memb/gi;
$file_content =~ s/!!altnum!!/$altnum/gi;
$file_content =~ s/!!allnum!!/$members/gi;
$file_content =~ s/!!message!!/$message/gi;
$file_content =~ s/!!sndmesslist!!/$messlist/gi;
$file_content =~ s/!!msglist!!/$file_content_a/gi;
$file_content =~ s/!!msgview!!/$mymsg/gi;
$file_content =~ s/!!sendto!!/$INPUT{'sender'}/gi;
close (FILE);

print "$file_content";

}