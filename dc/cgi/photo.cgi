#!/usr/local/bin/perl 

require 'cgi-lib2.pl';

&ReadParse;

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

##################################################################################

if ($in{'a'} eq "uploadfile") { &uploadfile }
elsif ($in{'a'} eq "pform") { &pform; }
elsif ($in{'a'} eq "newalbum") { &newalbum; }

##################################################################################

sub uploadfile {

   if (!$in{'sourcefile'}) {
$cont = "$cont<html><body><center><font size=+1 color=\"FF0000\">ERROR: Upload file not specified or empty.</font></center>";
$cont = "$cont<p>You did not provide a file to be uploaded or it is empty.  Please try again.</p>\n";
$file = "photo.tmp";
&output;


   	exit;
   }
   if ($ENV{'CONTENT_LENGTH'} > 300000) {
$cont = "$cont<html><body><center><font size=+1 color=\"FF0000\">ERROR: Upload file too large.</font></center>";
$cont = "$cont<p>Size of your upload file exceeds max file size. Please try again.</p>\n";
$file = "photo.tmp";
&output;


   	exit;
   }
   
   if (opendir(DIR,"$upload_dir") != 1) {
         `chmod 0777 $upload_dir`;
   }

open (FILE, "photo.cnt");
flock (FILE, 2);
$abcdefg = <FILE>;
chop ($abcdefg);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
$abcdefg++;
open(DATA, ">photo.cnt");
print DATA "$abcdefg\n";
print DATA "junk\n";
close DATA;

   $upload_dir = "$upload_dir/";
   open(REAL,">$upload_dir$abcdefg$in{'destn_filename'}");
   print REAL $in{'sourcefile'};
   close(REAL);
      `chmod 0777 $upload_dir$abcdefg$in{'destn_filename'}`;
$cont = "$cont<p><center><font size=+1 color=\"FF0000\"><b>File Upload Completed</b></font></center>";

open (FILE,"tmps/photo.tmp");
$file = "photo.tmp";
&output;

$in{'desc'} =~ s/ /%20/gi;

open (DATA, "$in{'page'}.lst");
@data = <DATA>;
close DATA;
open(DATA, ">$in{'page'}.lst");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$abcdefg$in{'destn_filename'}::$in{'desc'}\n";
close DATA;

   exit;
}

##################################################################################

sub pform {
$pag = "$pag<SELECT NAME=page>";

open (DATA, "photo.lst");
	@data = <DATA>;
close DATA;
foreach $line (@data) {
	chomp ($line);
	($page, $name) = split(/::/, $line);
$pag = "$pag<OPTION>$page";
}
$pag = "$pag</SELECT>";

$file = "photo_form.tmp";
&output;
}

##################################################################################

sub newalbum {

open (DATA, "photo.lst");
@data = <DATA>;
close DATA;
open(DATA, ">photo.lst");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$in{'shtname'}::$in{'lngname'}\n";
close DATA;


$cont = "$cont<p><center><font size=+1 color=\"FF0000\"><b>New Album Added.</b></font></center>";

$file = "photo.tmp";
&output;
}


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