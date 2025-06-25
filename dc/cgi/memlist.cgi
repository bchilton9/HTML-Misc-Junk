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

print "Content-type: text/html\n\n";


open (DATA, "ranks.lst");
@dataaa = <DATA>;
close DATA;
foreach $linee (@dataaa) {
chomp ($linee);

#####################################
open (DATA, "data/members.data");
@data = <DATA>;
close DATA;

foreach $line (@data) {
open (FILE, "data/$line");
flock (FILE, 2);
$usr = <FILE>;
chop ($name);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$type = <FILE>;
chop ($type);
$acc = <FILE>;
chop ($acc);
$rank = <FILE>;
chop ($rank);
$raid = <FILE>;
chop ($raid);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

if ($rank eq "$linee") {
open (FILE, "profile/$'usr");
flock (FILE, 2);
$sir = <FILE>;
chop ($sir);
$lvl = <FILE>;
chop ($aalvl);
$aaimg = <FILE>;
chop ($aaimg);
$aarel = <FILE>;
chop ($aarel);
$aasay = <FILE>;
chop ($aasay);
$aaac = <FILE>;
chop ($aaac);
$aaatk = <FILE>;
chop ($aaatk);
$aastr = <FILE>;
chop ($aastr);
$aasta = <FILE>;
chop ($aasta);
$aaagi = <FILE>;
chop ($aaagi);
$aadex = <FILE>;
chop ($aadex);
$aawis = <FILE>;
chop ($aawis);
$aaint = <FILE>;
chop ($aaint);
$aacha = <FILE>;
chop ($aacha);
flock (FILE, 14);
close(FILE);
$lead = "$lead<TR>";
$lead = "$lead<TD><B><A HREF=$cgipath/profile.cgi?a=view&user=$usr>$usr $sir</A></B></TD>";
$lead = "$lead<TD>$lvl</TD>";
$lead = "$lead<TD>$race</TD>";
$lead = "$lead<TD>$class</TD>";
$lead = "$lead<TD>$rank</TD>";
print "</TR>";
}
}
####################################
}


#####################################

open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($Ausr, $Aclass, $Arace, $Auser, $alvl) = split(/::/, $line);

$altlist = "$altlist<TR>";
$altlist = "$altlist<TD><B>$Ausr</B></TD>";
$altlist = "$altlist<TD>$alvl</TD>";
$altlist = "$altlist<TD>$Arace</TD>";
$altlist = "$altlist<TD>$Aclass</TD>";
$altlist = "$altlist<TD>$Auser</TD>";
$altlist = "$altlist</TR>";


}

####################################

$file = "member_list.tmp";
&output;


print "<P><A HREF=http://www.erenetwork.com/dc/egg.cgi?a=egg&page=rost>";
print "<IMG SRC=http://www.erenetwork.com/dc/smturkey.gif WIDTH=50 HEIGHT=50 BORDER=0></A>";


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
