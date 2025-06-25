#!/usr/bin/perl

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

$con = "0";
$val = "0";

##################################################################################

open (FILE, "config.pl");
flock (FILE, 2);
$guildname = <FILE>;
chop ($guildname);
$email = <FILE>;
chop ($email);
$cgipath = <FILE>;
chop ($cgipath);
$imgpath = <FILE>;
chop ($imgpath);
$upload_dir = <FILE>;
chop ($upload_dir);
$sitepath = <FILE>;
chop ($sitepath);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

##################################################################################

$name = $INPUT{'name'};
$pass = $INPUT{'pass'};
$pass2 = $INPUT{'pass2'};
$race = $INPUT{'race'};
$class = $INPUT{'class'};

##################################################################################

print "Content-type: text/html\n\n";

##################################################################################

if ($name eq "") { 
$cont = "$cont<CENTER><B>You must enter a EQ Name</B></CENTER>";
$con = "1";
}
if ($pass eq "") { 
$cont = "$cont<CENTER><B>You must enter a Password</B></CENTER>";
$con = "1";
}
if ($pass2 eq "") { 
$cont = "$cont<CENTER><B>You Must Re-Type your Password to conferm</B></CENTER>";
$con = "1";
}
if ($INPUT{'email'} eq "") { 
$cont = "$cont<CENTER><B>You must enter a E-Mail</B></CENTER>";
$con = "1";
}
if ($race eq "") { 
$cont = "$cont<CENTER><B>You must enter a Race</B></CENTER>";
$con = "1";
}
if ($class eq "") { 
$cont = "$cont<CENTER><B>You must enter a class</B></CENTER>";
$con = "1";
}
if ($con eq "1") {
$cont = "$cont<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
}


if ($pass eq $pass2) {

if ($con eq "0") {
if ($pass eq $pass2) {
open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name2) = split(/::/, $line);
if ($name eq $name2) {
$val = "1";
}
}
}
}


if ($con eq "0") {
if ($pass eq $pass2) {
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name2) = split(/::/, $line);
if ($name eq $name2) {
$val = "1";
}
}
} #ifpass
} #ifcon



if ($val eq "1") {
$cont = "<CENTER><B>EQ name allready registered</B></CENTER>";
$cont = "$con<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
} #ifval

else {
if ($con eq "0") {

open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
open(DATA, ">wateing.list");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$name\n";
close DATA;

open (DATA, "data/$INPUT{'name'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'name'}");

print DATA "$INPUT{'name'}\n";
print DATA "$INPUT{'pass'}\n";
print DATA "$INPUT{'email'}\n";
print DATA "$INPUT{'race'}\n";
print DATA "$INPUT{'class'}\n";
print DATA "Member\n";
print DATA "Member\n";
print DATA "Member\n";
print DATA "0\n";
print DATA "junk\n";

close DATA;

$cont = "<CENTER><B>Thank you $INPUT{'name'}<BR>";
$cont = "$cont You are now registered<BR>";

open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $INPUT{'email'}\n";
print MAIL "Reply-to: $email\n";
print MAIL "From: $email\n";
print MAIL "Subject: $guildname Registered\n\n";
print MAIL "Welcome To $guildname $INPUT{'name'}\n";
print MAIL "You are now in the $guildname Database\n";
print MAIL "You will be added to the members listing\n";
print MAIL "as soon as your membership has been verafied!\n";
print MAIL "Thank you for becomeing a $guildname\n";
print MAIL "The $guildname Head Crew!!\n\n\n";
print MAIL "Members Info\:\n";
print MAIL "Eq Name $INPUT{'name'}\n";
print MAIL "Password $INPUT{'pass'}\n";
print MAIL "E-Mail $INPUT{'email'}\n";
print MAIL "Class $INPUT{'class'}\n";
print MAIL "Race $INPUT{'race'}\n";

}
} # else

}
else {
$cont = "<CENTER><B>Your passwords dident mach</B></CENTER>";
$cont = "$cont<CENTER><B>Please Hit your brosers back butten!</B></CENTER>";
} #else

$file = "save_sign.tmp";
&output;

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
open (DATA, "tmps/header.tmp");
@data = <DATA>;
close DATA;
$header = "@data";
####ENDHEADER

$imgpath = "$imgpath/$INPUT{'img'}";

open (FILE,"tmps/$file");
while (<FILE>) { $file_content.=$_; }
$file_content =~ s/!!header!!/$header/gi;
$file_content =~ s/!!content!!/$cont/gi;
$file_content =~ s/!!news!!/$news/gi;
$file_content =~ s/!!officernews!!/$offnews/gi;
$file_content =~ s/!!visitlist!!/$visit/gi;
$file_content =~ s/!!cookieuser!!/$Cookies{'user'}/gi;
$file_content =~ s/!!message!!/$message/gi;
$file_content =~ s/!!admin!!/$file_content_admin/gi;
$file_content =~ s/!!listmembers!!/$mem/gi;
$file_content =~ s/!!editname!!/$INPUT{'usr'}/gi;
$file_content =~ s/!!editemail!!/$INPUT{'email'}/gi;
$file_content =~ s/!!editrace!!/$race/gi;
$file_content =~ s/!!editclass!!/$class/gi;
$file_content =~ s/!!editrank!!/$rank/gi;
$file_content =~ s/!!editaccess!!/$acc/gi;
$file_content =~ s/!!pagelist!!/$page/gi;
$file_content =~ s/!!pageurl!!/$url/gi;
$file_content =~ s/!!guildname!!/$guildname/gi;
$file_content =~ s/!!guildemail!!/$guildemail/gi;
$file_content =~ s/!!photolist!!/$plist/gi;
$file_content =~ s/!!photo!!/$list/gi;
$file_content =~ s/!!image!!/$imgpath/gi;
$file_content =~ s/!!description!!/$INPUT{'desc'}/gi;
$file_content =~ s/!!listleader!!/$lead/gi;
$file_content =~ s/!!listofficer!!/$off/gi;
$file_content =~ s/!!listmember!!/$mem/gi;
$file_content =~ s/!!listalts!!/$altlist/gi;
$file_content =~ s/!!albumlist!!/$pag/gi;
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
$file_content =~ s/!!alts!!/$alt/gi;
$file_content =~ s/!!altname!!/$INPUT{'usr'}/gi;
$file_content =~ s/!!altlvl!!/$INPUT{'alvl'}/gi;
$file_content =~ s/!!altclass!!/$altclass/gi;
$file_content =~ s/!!altrace!!/$altrace/gi;
$file_content =~ s/!!password!!/$passup/gi;
$file_content =~ s/!!useremail!!/$email/gi;
$file_content =~ s/!!memnum!!/$memb/gi;
$file_content =~ s/!!altnum!!/$altnum/gi;
$file_content =~ s/!!allnum!!/$members/gi;
$file_content =~ s/!!classtable!!/$clas/gi;
$file_content =~ s/!!racetable!!/$rac/gi;
$file_content =~ s/!!lvltable!!/$lv/gi;
$file_content =~ s/!!pagename!!/$INPUT{'page'}/gi;
close (FILE);

print "$file_content";

}