#!/usr/bin/perl

require 'cookie.lib';
#require 'output.pl';
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

open (FILE, "config.pl");
flock (FILE, 2);
$guildname = <FILE>;
chop ($guildname);
$guildemail = <FILE>;
chop ($guildemail);
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

if ($INPUT{'a'} eq "login") { 
#sub login {
open (FILE, "data/$INPUT{'name'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

if ($usr eq "") { 
print "Content-type: text/html\n\n";

$cont = "Username error!!";

$file = "view_page.tmp";
&output;

exit;
 }

else { 
if ($INPUT{'password'} eq "$cryptpass") { 


    &SetCookies('user',"$usr");
    &SetCookies('pass',"$INPUT{'password'}");
print "Content-type: text/html\n\n";
    print "\n";


$cont = "You are now logged in<BR><A HREF=$cgipath/index.cgi?a=start id=link>Click here to enter</A>";

$file = "view_page.tmp";
&output;

exit;

 }
else {
print "Content-type: text/html\n\n";

$cont = "Password error!!";

$file = "view_page.tmp";
&output;

exit;
 }


}
 }
##################################################################################
elsif ($INPUT{'a'} eq "logout") { 


    &SetCookies('user',"");
    &SetCookies('pass',"");
print "Content-type: text/html\n\n";
    print "\n";

$cont = "You are now logged out.";

$file = "view_page.tmp";
&output;

exit;
 }
else {


print "Content-type: text/html\n\n";


##################################################################################

if (&GetCookies('user')) {

    &GetCookies('pass');
    print "\n";

}



if ($INPUT{'a'} eq "start") { &start }
elsif ($INPUT{'a'} eq "Approve") { &aprove }
elsif ($INPUT{'a'} eq "Delete") { &delete }
elsif ($INPUT{'a'} eq "email") { &email }
elsif ($INPUT{'a'} eq "SendEmail") { &semail }
elsif ($INPUT{'a'} eq "list") { &list }
elsif ($INPUT{'a'} eq "Edit") { &edit }
elsif ($INPUT{'a'} eq "update") { &update }
elsif ($INPUT{'a'} eq "news") { &news }
elsif ($INPUT{'a'} eq "Update News") { &upnews }
elsif ($INPUT{'a'} eq "page") { &page }
elsif ($INPUT{'a'} eq "editpage") { &editpage }
elsif ($INPUT{'a'} eq "editpageB") { &editpageB }
elsif ($INPUT{'a'} eq "Update Page") { &uppage }
elsif ($INPUT{'a'} eq "sett") { &sett }
elsif ($INPUT{'a'} eq "upsett") { &upsett }
elsif ($INPUT{'a'} eq "+") { &pts }
elsif ($INPUT{'a'} eq "-") { &takepts }
elsif ($INPUT{'a'} eq "photoview") { &photoview; }
elsif ($INPUT{'a'} eq "photopage") { &photopage; }
elsif ($INPUT{'a'} eq "photolist") { &photolist; }
elsif ($INPUT{'a'} eq "roster") { &roster; }
elsif ($INPUT{'a'} eq "sendmessage") { &sendmessage; }
elsif ($INPUT{'a'} eq "stats") { &stats; }
elsif ($INPUT{'a'} eq "Sign Up") { &signup; }
elsif ($INPUT{'a'} eq "Sugest Raid") { &sugraid; }
elsif ($INPUT{'a'} eq "viewraid") { &viewraid; }
elsif ($INPUT{'a'} eq "deleteraid") { &deleteraid; }
elsif ($INPUT{'a'} eq "uploadfile") { &uploadfile }
elsif ($INPUT{'a'} eq "pform") { &pform; }
elsif ($INPUT{'a'} eq "newalbum") { &newalbum; }
elsif ($INPUT{'a'} eq "view") { &view; }
elsif ($INPUT{'a'} eq "prof") { &form }
elsif ($INPUT{'a'} eq "addalt") { &addalt }
elsif ($INPUT{'a'} eq "addaltb") { &addaltb }
elsif ($INPUT{'a'} eq "EditAlt") { &editalt }
elsif ($INPUT{'a'} eq "editaltb") { &editaltb }
elsif ($INPUT{'a'} eq "DeleteAlt") { &deletealt }
elsif ($INPUT{'a'} eq "wizard") { &wizard }
elsif ($INPUT{'a'} eq "upwiz") { &upwiz }
elsif ($INPUT{'a'} eq "pass") { &pass }
elsif ($INPUT{'a'} eq "info") { &info }
elsif ($INPUT{'a'} eq "uppass") { &uppass }
elsif ($INPUT{'a'} eq "upinfo") { &upinfo }
elsif ($INPUT{'a'} eq "Change_CSS") { &ccss }
else { &form; }

}

##################################################################################

sub form {

if (&GetCookies('user')) {
&GetCookies('user');

	if ($Cookies{'user'} eq "") {
		&formb;
	}
	else {
    		&start;
	}
}
else {
	&formb;
}

}



##################################################################################

sub formb {
#### START VISIT
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$hour = $hour + 1;
if ($hour <= 9) {
	$hour = "0$hour";
}
$mon = $mon + 1;
$year = $year + 1900;
if ($min <= 9) {
	$min = "0$min";
	$mymin = $min + 60;
	$hour = $hour - 1;
}
else {
	$mymin = $min;
}
$mymin = $mymin - 10;
if ($mymin <= 9) {
	$mymin = "0$mymin";
}
if ($mday <= 9) {
	$mday = "0$mday";
}
$time = "$mon$mday$year$hour$mymin";
open (DATAAA, "visit.dat");
@data = <DATAAA>;
close DATAAA;
foreach $line (@data) {
chomp ($line);
($name, $tim) = split(/::/, $line);
if ($time <= $tim) {


$visit = "$visit $name,";


}
}
####ENDVISIT

$file = "main_loged_out.tmp";
&output;

}


##################################################################################

sub start{


&GetCookies('user');
&GetCookies('pass');


open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

open (FILE, "profile/$Cookies{'user'}");
flock (FILE, 2);
$aaasir = <FILE>;
chop ($aaasir);
$aaalvl = <FILE>;
chop ($aaalvl);
$aaaimg = <FILE>;
chop ($aaaimg);
$aaarel = <FILE>;
chop ($aaarel);
$aaasay = <FILE>;
chop ($aaasay);
$aaaac = <FILE>;
chop ($aaaac);
$aaaatk = <FILE>;
chop ($aaaatk);
$aaastr = <FILE>;
chop ($aaastr);
$aaasta = <FILE>;
chop ($aaasta);
$aaaagi = <FILE>;
chop ($aaaagi);
$aaadex = <FILE>;
chop ($aaadex);
$aaawis = <FILE>;
chop ($aaawis);
$aaaint = <FILE>;
chop ($aaaint);
$aaacha = <FILE>;
chop ($aaacha);
$junk = <FILE>;
chop ($junk);
flock (FILE, 14);
close(FILE);

if ($junk eq "") {
print <<"HTML";
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
var agree=confirm("You have not setup your profile yet would you like to do so now?");
if (agree)
window.location = "$cgipath/profile.cgi?a=wizard";
else
document.write("");
// End -->
</SCRIPT>
HTML
}

#### START VISIT
$don = "no";
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$hour = $hour + 1;
if ($hour <= 9) {
	$hour = "0$hour";
}
$mon = $mon + 1;
$year = $year + 1900;
if ($min <= 9) {
	$min = "0$min";
}
if ($mday <= 9) {
	$mday = "0$mday";
}
open (DATA, "visit.dat");
@data = <DATA>;
close DATA;
open(DATAA, ">visit.dat");
foreach $line (@data) {
	chomp ($line);
	($name, $tim) = split(/::/, $line);
	if ($name eq $Cookies{'user'}) {
		print DATAA "$Cookies{'user'}::$mon$mday$year$hour$min\n";
		$don = "yes";
	} #end if name
	else {
		print DATAA "$line\n";
	} #end else name
} #end foreach
if ($don eq "no") {
	print DATAA "$Cookies{'user'}::$mon$mday$year$hour$min\n";
} #end if done
close DATAA;
if ($min <= 9) {
	$mymin = $min + 60;
	$hour = $hour - 1;
}
else {
	$mymin = $min;
}
$mymin = $mymin - 10;
if ($mymin <= 9) {
	$mymin = "0$mymin";
}
$time = "$mon$mday$year$hour$mymin";
$visit = "";
open (DATAAA, "visit.dat");
@data = <DATAAA>;
close DATAAA;
foreach $line (@data) {
chomp ($line);
($name, $tim) = split(/::/, $line);
if ($time <= $tim) {

$visit = "$visit <A HREF=msg/msg.cgi?a=Reply&sender=$name id=visitlist>$name</A>,";

}
}
####ENDVISIT



####STARTADMIN
if ($acc eq "Moderator") { &admin }
if ($acc eq "Administrator") { &admin }


sub admin {

####START WATEING
open (DATA, "wateing.list");
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
$Aacc = <FILE>;
chop ($Aacc);
$rank = <FILE>;
chop ($rank);
$raid = <FILE>;
chop ($raid);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$wate = "$wate<FORM><TR><TD>$usr<INPUT TYPE=hidden VALUE=$usr NAME=usr></TD>";
$wate = "$wate<TD>$email</TD><TD>$race</TD><TD>$class</TD><TD>Member</TD>";
$wate = "$wate<TD><INPUT TYPE=submit VALUE=Approve NAME=a id=input></TD>";
$wate = "$wate<TD><INPUT TYPE=submit VALUE=Delete NAME=a id=input></TD></TR></FORM>";
}

if ($acc eq "Administrator") {
open (FILE,"tmps/admin_full.tmp");
while (<FILE>) { $full.=$_; }
$full =~ s/!!listwateing!!/$wate/gi;
close (FILE);
}

####STARTOFFICERNEWS
open (DATA, "officernews.dat");
@data = <DATA>;
close DATA;
$offnews = "@data";
####ENDOFFICERNEWS

open (FILE,"tmps/admin.tmp");
while (<FILE>) { $file_content_admin.=$_; }
$file_content_admin =~ s/!!listwateing!!/$wate/gi;
$file_content_admin =~ s/!!fulladmin!!/$full/gi;
$file_content_admin =~ s/!!officernews!!/$offnews/gi;
close (FILE);
}
####ENDADMIN


$file = "main_loged_in.tmp";
&output;

}

##################################################################################

sub aprove {

open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
open(DATA, ">data/members.data");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'usr'}\n";
close DATA;

open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
open(DATA, ">wateing.list");
foreach $line (@data) {
chomp ($line);
($usr) = split(/::/, $line);
if ($usr eq "$INPUT{'usr'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}


$file = "add_user.tmp";
&output;

}

##################################################################################

sub delete {
open (DATA, "wateing.list");
@data = <DATA>;
close DATA;
open(DATA, ">wateing.list");
foreach $line (@data) {
chomp ($line);
($usr) = split(/::/, $line);
if ($usr eq "$INPUT{'usr'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}

open (DATA, "data/members.data");
@data = <DATA>;
close DATA;
open(DATA, ">data/members.data");
foreach $line (@data) {
chomp ($line);
($usr) = split(/::/, $line);
if ($usr eq "$INPUT{'usr'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}


unlink("data/$INPUT{'usr'}");


$file = "delete_user.tmp";
&output;

}

##################################################################################

sub list {
####STARTMEMBERS
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
$mem = "$mem<FORM METHOD=POST>";
$mem = "$mem<TR><TD><div id=text2><A HREF=mailto:$email id=text2>$usr</A></div><INPUT TYPE=hidden VALUE=$usr NAME=usr></TD>";
$mem = "$mem<TD><div id=text3>$rank</div><INPUT TYPE=hidden VALUE=$rank NAME=rank></TD>";
$mem = "$mem<TD><div id=text3>$type</div><INPUT TYPE=hidden VALUE=$type NAME=type></TD>";
$mem = "$mem<TD><div id=text3>$acc</div><INPUT TYPE=hidden VALUE=$acc NAME=acc></TD>";
$mem = "$mem<TD><div id=text3>$raid</div><INPUT TYPE=hidden VALUE=$raid NAME=raid>";
$mem = "$mem<INPUT TYPE=hidden VALUE=$email NAME=email><INPUT TYPE=hidden VALUE=$race NAME=race>";
$mem = "$mem<INPUT TYPE=hidden VALUE=$class NAME=class></TD>";
$mem = "$mem<TD><INPUT TYPE=test size=3 NAME=pts id=input><INPUT TYPE=submit VALUE=+ NAME=a id=input><INPUT TYPE=submit VALUE=- NAME=a id=input></TD>";
$mem = "$mem<TD><INPUT TYPE=submit VALUE=Delete NAME=a id=input></TD>";
$mem = "$mem<TD><INPUT TYPE=submit VALUE=Edit NAME=a id=input></TD></TR></FORM>";
}
####ENDMEMBERS

$file = "list_mem.tmp";
&output;

}

##################################################################################

sub edit {
&GetCookies('user');
&GetCookies('pass');
####STARTRACE
$race = "<SELECT NAME=race id=input>";
if ($INPUT{'race'} eq "Barbarian") {
$race = "$race<OPTION SELECTED>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Dark_Elf") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION SELECTED>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Dwarf") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION SELECTED>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Erudite") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION SELECTED>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Gnome") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION SELECTED>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Half_Elf") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION SELECTED>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Halfling") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION SELECTED>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "High_Elf") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION SELECTED>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Human") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION SELECTED>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Iskar") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION SELECTED>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Orge") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION SELECTED>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Troll") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION SELECTED>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Wood_Elf") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION SELECTED>Wood_Elf";
$race = "$race<OPTION>Vah_Shir";
}
elsif ($INPUT{'race'} eq "Vah_Shir") {
$race = "$race<OPTION>Barbarian";
$race = "$race<OPTION>Dark_Elf";
$race = "$race<OPTION>Dwarf";
$race = "$race<OPTION>Erudite";
$race = "$race<OPTION>Gnome";
$race = "$race<OPTION>Half_Elf";
$race = "$race<OPTION>Halfling";
$race = "$race<OPTION>High_Elf";
$race = "$race<OPTION>Human";
$race = "$race<OPTION>Iskar";
$race = "$race<OPTION>Orge";
$race = "$race<OPTION>Troll";
$race = "$race<OPTION>Wood_Elf";
$race = "$race<OPTION SELECTED>Vah_Shir";
}
$race = "$race</SELECT>";
####ENDRACE
####STARTCLAS
$class = "<SELECT NAME=class id=input>";
if ($INPUT{'class'} eq "Bard") {
$class = "$class<OPTION SELECTED>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Cleric") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION SELECTED>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Druid") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION SELECTED>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Wizard") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION SELECTED>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Enchanter") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION SELECTED>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Magician") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION SELECTED>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Monk") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION SELECTED>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Necromancer") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION SELECTED>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Paladin") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION SELECTED>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Ranger") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION SELECTED>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Roug") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION SELECTED>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "ShadowKnight") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION SELECTED>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Shaman") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION SELECTED>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Warrior") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION SELECTED>Warrior";
$class = "$class<OPTION>Beastlord";
}
elsif ($INPUT{'class'} eq "Beastlord") {
$class = "$class<OPTION>Bard";
$class = "$class<OPTION>Cleric";
$class = "$class<OPTION>Druid";
$class = "$class<OPTION>Wizard";
$class = "$class<OPTION>Enchanter";
$class = "$class<OPTION>Magician";
$class = "$class<OPTION>Monk";
$class = "$class<OPTION>Necromancer";
$class = "$class<OPTION>Paladin";
$class = "$class<OPTION>Ranger";
$class = "$class<OPTION>Roug";
$class = "$class<OPTION>ShadowKnight";
$class = "$class<OPTION>Shaman";
$class = "$class<OPTION>Warrior";
$class = "$class<OPTION SELECTED>Beastlord";
}
$class = "$class</SELECT>";
####ENDCLASS
####STARTRANK
open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$Ausr = <FILE>;
chop ($Ausr);
$Acryptpass = <FILE>;
chop ($Acryptpass);
$Aemail = <FILE>;
chop ($Aemail);
$Arace = <FILE>;
chop ($Arace);
$Aclass = <FILE>;
chop ($Aclass);
$Atype = <FILE>;
chop ($Atype);
$Aacc = <FILE>;
chop ($Aacc);
$arank = <FILE>;
chop ($arank);
$araid = <FILE>;
chop ($araid);
$Astyle = <FILE>;
chop ($Astyle);
$Ajunk = <FILE>;
chop ($Ajunk);
flock (FILE, 8);
close(FILE);

if ($Aacc eq "Administrator") {
$type = "<SELECT NAME=type id=input>";

if ($INPUT{'type'} eq "Member") {
$type = "$type<OPTION SELECTED>Member";
$type = "$type<OPTION>Officer";
}
if ($INPUT{'type'} eq "Officer") {
$type = "$type<OPTION>Member";
$type = "$type<OPTION SELECTED>Officer";
}
$type = "$type</SELECT>";





$rank = "<SELECT NAME=rank id=input>";
open (DATA, "ranks.lst");
@data = <DATA>;
close DATA;
foreach $line (@data) {
	chomp ($line);
	($ranks, $aaatype) = split(/::/, $line);

if ($aaatype eq "3") {
$ranks = "----- $ranks -----";
}
if ($aaatype eq "4") {
$ranks = "--- $ranks ---";
}

if ($ranks eq "$INPUT{'rank'}") {
$rank = "$rank<OPTION SELECTED>$ranks";
}

else {
$rank = "$rank<OPTION>$ranks";
}


}


$rank = "$rank</SELECT><INPUT TYPE=hidden VALUE=$INPUT{'raid'} NAME=raid>";





$acc = "<SELECT NAME=acc id=input>";
if ($INPUT{'acc'} eq "Administrator") {
$acc = "$acc<OPTION>Member";
$acc = "$acc<OPTION>Moderator";
$acc = "$acc<OPTION SELECTED>Administrator";
}
elsif ($INPUT{'acc'} eq "Moderator") {
$acc = "$acc<OPTION>Member";
$acc = "$acc<OPTION SELECTED>Moderator";
$acc = "$acc<OPTION>Administrator";
}
elsif ($INPUT{'acc'} eq "Member") {
$acc = "$acc<OPTION SELECTED>Member";
$acc = "$acc<OPTION>Moderator";
$acc = "$acc<OPTION>Administrator";
}
$acc = "$acc</SELECT>";
}
else {
$rank = "<DIV id=text3>$INPUT{'rank'}</div><INPUT TYPE=hidden VALUE=$INPUT{'rank'} NAME=rank><INPUT TYPE=hidden VALUE=$INPUT{'raid'} NAME=raid>";
$type = "<DIV id=text3>$INPUT{'type'}</div><INPUT TYPE=hidden VALUE=$INPUT{'type'} NAME=type>";
$acc = "<DIV id=text3>$INPUT{'acc'}</div><INPUT TYPE=hidden VALUE=$INPUT{'acc'} NAME=acc>";
}
####ENDRANK


$file = "edit_mem.tmp";
&output;
}

##################################################################################

sub update {
open (FILE, "data/$INPUT{'usr'}");
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

open (DATA, "data/$INPUT{'usr'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'usr'}");
print DATA "$INPUT{'usr'}\n";
print DATA "$pass\n";
print DATA "$INPUT{'email'}\n";
print DATA "$INPUT{'race'}\n";
print DATA "$INPUT{'class'}\n";
print DATA "$INPUT{'type'}\n";
print DATA "$INPUT{'acc'}\n";
print DATA "$INPUT{'rank'}\n";
print DATA "$INPUT{'raid'}\n";
print DATA "$style\n";
print DATA "junk\n";
close DATA;

$file = "edit_save.tmp";
&output;
}

##################################################################################

sub pts {
open (FILE, "data/$INPUT{'usr'}");
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$pts = $INPUT{'pts'} + $raid;

open (DATA, "data/$INPUT{'usr'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'usr'}");
print DATA "$INPUT{'usr'}\n";
print DATA "$pass\n";
print DATA "$INPUT{'email'}\n";
print DATA "$INPUT{'race'}\n";
print DATA "$INPUT{'class'}\n";
print DATA "$INPUT{'type'}\n";
print DATA "$INPUT{'acc'}\n";
print DATA "$INPUT{'rank'}\n";
print DATA "$pts\n";
print DATA "$style\n";
print DATA "junk\n";
close DATA;

$file = "edit_save.tmp";
&output;
}
##################################################################################

sub takepts {
open (FILE, "data/$INPUT{'usr'}");
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$pts = $raid - $INPUT{'pts'};
if ($pts <= 0) {
$pts = 0;
}

open (DATA, "data/$INPUT{'usr'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'usr'}");
print DATA "$INPUT{'usr'}\n";
print DATA "$pass\n";
print DATA "$INPUT{'email'}\n";
print DATA "$INPUT{'race'}\n";
print DATA "$INPUT{'class'}\n";
print DATA "$INPUT{'type'}\n";
print DATA "$INPUT{'acc'}\n";
print DATA "$INPUT{'rank'}\n";
print DATA "$pts\n";
print DATA "$style\n";
print DATA "junk\n";
close DATA;

$file = "edit_save.tmp";
&output;
}

##################################################################################

sub email {
$file = "email_mem.tmp";
&output;
}

##################################################################################

sub semail {
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);


if ($INPUT{'to'} eq "Officer") { 

if ($type eq "Officer") { 
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: $guildemail\n";
print MAIL "From: $guildemail\n";
print MAIL "Subject: @guildname Officer Message\n\n";
print MAIL "Hello $usr\n";
print MAIL "$INPUT{'message'}\n";
}

}
elsif ($INPUT{'to'} eq "All") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $email\n";
print MAIL "Reply-to: $guildemail\n";
print MAIL "From: $guildemail\n";
print MAIL "Subject: $guildname NewsLetter\n\n";
print MAIL "Hello $usr\n";
print MAIL "$INPUT{'message'}\n";
}


}

$file = "email_sent.tmp";
&output;
}

##################################################################################

sub news {
$file = "edit_news.tmp";
&output;
}

##################################################################################

sub upnews {
open (DATA, "news.dat");
@data = <DATA>;
close DATA;
open(DATA, ">news.dat");
print DATA "$INPUT{'news'}";
close DATA;

open (DATA, "officernews.dat");
@data = <DATA>;
close DATA;
open(DATA, ">officernews.dat");
print DATA "$INPUT{'offnews'}";
close DATA;

$file = "update_news.tmp";
&output;

}

##################################################################################

sub page {


open (DATA, "$INPUT{'page'}.dat");
@data = <DATA>;
close DATA;

$cont = "@data";

$file = "view_page.tmp";
&output;
}

##################################################################################

sub editpage {
open (DATA, "pages.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$page = "$page<A HREF=index.cgi?a=editpageB&page=$line id=link>Edit $line</A><BR>";
}

$file = "edit_page_list.tmp";
&output;
}

##################################################################################

sub editpageB {
if ($INPUT{'new'} eq "true") { 
open (DATA, "pages.dat");
@data = <DATA>;
close DATA;
open(DATA, ">pages.dat");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'page'}\n";
close DATA;
 }

open (DATA, "$INPUT{'page'}.dat");
@data = <DATA>;
close DATA;

$cont = "@data";

$file = "edit_page_form.tmp";
&output;
}

##################################################################################

sub uppage {

open (DATA, "$INPUT{'page'}.dat");
@data = <DATA>;
close DATA;
open(DATA, ">$INPUT{'page'}.dat");

print DATA "$INPUT{'content'}";

$url = "$cgipath/index.cgi?a=page&page=$INPUT{'page'}";

$file = "edit_page_save.tmp";
&output;

}

##################################################################################

sub sett {
$file = "edit_setting.tmp";
&output;
}

##################################################################################

sub upsett {
open (DATA, "config.pl");
@data = <DATA>;
close DATA;
open(DATA, ">config.pl");

print DATA "$INPUT{'gname'}\n";
print DATA "$INPUT{'guildmail'}\n";
print DATA "$cgipath\n";
print DATA "$imgpath\n";
print DATA "$upload_dir\n";
print DATA "$sitepath\n";
print DATA "junk\n";

close DATA;

$file = "update_setting.tmp";
&output;
}

##################################################################################

sub photoview {

$file = "photo_view.tmp";
&output;

}

##################################################################################

sub photolist {
open (DATA, "photo.lst");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($page, $name) = split(/::/, $line);
$plist = "$plist<A HREF=?a=photopage&page=$page id=link>$name</A><P>";
}


$file = "photo_list.tmp";
&output;
}

#########################################################################

sub photopage {
open (DATA, "$INPUT{'page'}.lst");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($IMG, $DESC) = split(/::/, $line);
	$count = $count + 1;
	
	$list = "$list<TD><A HREF=?a=photoview&img=$IMG&desc=$DESC TARGET=_img><IMG SRC=$imgpath/$IMG WIDTH=100 HEIGHT=100 BORDER=0></A></TD>";

	if ($count eq 6) {
		$list = "$list</TR><TR>";
		$count = 0;
	}
}
close DATA;

$file = "photo_album.tmp";
&output;


if ($INPUT{'page'} eq "firstday") {
print <<"HTML";
<CENTER><A HREF="egg.cgi?a=egg&page=phot">
<IMG SRC="smturkey.gif" WIDTH="50" HEIGHT="50" BORDER="0"></A>
HTML
}

}

#########################################################################

sub roster {
open (DATA, "ranks.lst");
@dataaa = <DATA>;
close DATA;
foreach $line (@dataaa) {
	chomp ($line);
	($ranks, $types) = split(/::/, $line);

if ($types eq "3") {
$lead = "$lead<TR><TD COLSPAN=7><div id=text1><HR>$ranks<HR></DIV></TD></TR>";
}
else {

open (DATA, "data/members.data");
@data = <DATA>;
close DATA;

foreach $linee (@data) {
chomp ($linee);
open (FILE, "data/$linee");
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
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

if ($rank eq "$ranks") {
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

($cl, $myrank) = split(/_/, $rank);
if ($myrank eq "") {
$myrank = $rank;
}


if ($types eq "1") {
$lead = "$lead<TR><TD COLSPAN=2><A HREF=$cgipath/profile.cgi?a=view&user=$usr id=text2>$usr $sir</A></TD>";
$lead = "$lead<TD></TD><TD><div id=text3>$myrank</DIV></TD><TD><div id=text3>$lvl</DIV></TD><TD><div id=text3>$race</DIV></TD><TD><div id=text3>$class</DIV></TD></TR>";
}
if ($types eq "2") {
$lead = "$lead<TR><TD></TD>";
$lead = "$lead<TD COLSPAN=2><A HREF=$cgipath/profile.cgi?a=view&user=$usr id=text2>$usr $sir</A></TD>";
$lead = "$lead<TD><div id=text3>$myrank</DIV></TD><TD><div id=text3>$lvl</DIV></TD><TD><div id=text3>$race</DIV></TD><TD><div id=text3>$class</DIV></TD></TR>";
}

}
}


}
}


open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($Ausr, $Aclass, $Arace, $Auser, $alvl) = split(/::/, $line);

$Ausr =~ s/_/ /gi;

$altlist = "$altlist<TR>";
$altlist = "$altlist<TD><div id=text2>$Ausr</div></TD>";
$altlist = "$altlist<TD><div id=text3>$alvl</div></TD>";
$altlist = "$altlist<TD><div id=text3>$Arace</div></TD>";
$altlist = "$altlist<TD><div id=text3>$Aclass</div></TD>";
$altlist = "$altlist<TD><div id=text3>$Auser</div></TD>";
$altlist = "$altlist</TR>";


}

$file = "member_list.tmp";
&output;
}

#########################################################################

sub sendmessage {
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
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$type = <FILE>;
chop ($type);
$raid = <FILE>;
chop ($raid);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
$messlist = "$messlist<TR>\n";
$messlist = "$messlist<TD><B>$usr</B></TD>\n";
$messlist = "$messlist<TD><A HREF=msg/msg.cgi?a=Reply&name=$INPUT{'name'}&sender=$usr id=text3>Send</A></TD>\n";
$messlist = "$messlist</TR>\n";
}

$file = "send_message.tmp";
&output;
}

#########################################################################

sub stats {

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

$Bard = 0;
$Cle = 0;
$Dru = 0;
$Wiz = 0;
$Enc = 0;
$Mag = 0;
$Mon = 0;
$Nec = 0;
$Pal = 0;
$Ran = 0;
$Rou = 0;
$Sk = 0;
$Sha = 0;
$War = 0;
$Bea = 0;
$Bar = 0;
$Dar = 0;
$Dwa = 0;
$Eru = 0;
$Gno = 0;
$Hlf = 0;
$Hal = 0;
$Hig = 0;
$Hum = 0;
$Isk = 0;
$Org = 0;
$Tro = 0;
$Woo = 0;
$Vah = 0;

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
$rank = <FILE>;
chop ($rank);
$acc = <FILE>;
chop ($acc);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

open (FILE, "profile/$line");
flock (FILE, 2);
$aaasir = <FILE>;
chop ($aaasir);
$lvl = <FILE>;
chop ($lvl);
$aaaimg = <FILE>;
chop ($aaaimg);
$aaarel = <FILE>;
chop ($aaarel);
$aaasay = <FILE>;
chop ($aaasay);
$aaaac = <FILE>;
chop ($aaaac);
$aaaatk = <FILE>;
chop ($aaaatk);
$aaastr = <FILE>;
chop ($aaastr);
$aaasta = <FILE>;
chop ($aaasta);
$aaaagi = <FILE>;
chop ($aaaagi);
$aaadex = <FILE>;
chop ($aaadex);
$aaawis = <FILE>;
chop ($aaawis);
$aaaint = <FILE>;
chop ($aaaint);
$aaacha = <FILE>;
chop ($aaacha);
flock (FILE, 14);
close(FILE);

$LVL{$lvl} = $LVL{$lvl} + 1;

if ($class eq "Bard") {
$Bard = $Bard + 1;
}
if ($class eq "Cleric") {
$Cle = $Cle + 1;
}
if ($class eq "Druid") {
$Dru = $Dru + 1;
}
if ($class eq "Wizard") {
$Wiz = $Wiz + 1;
}
if ($class eq "Enchanter") {
$Enc = $Enc + 1;
}
if ($class eq "Magician") {
$Mag = $Mag + 1;
}
if ($class eq "Monk") {
$Mon = $Mon + 1;
}
if ($class eq "Necromancer") {
$Nec = $Nec + 1;
}
if ($class eq "Paladin") {
$Pal = $Pal + 1;
}
if ($class eq "Ranger") {
$Ran = $Ran + 1;
}
if ($class eq "Roug") {
$Rou = $Rou + 1;
}
if ($class eq "ShadowKnight") {
$Sk = $Sk + 1;
}
if ($class eq "Shaman") {
$Sha = $Sha + 1;
}
if ($class eq "Warrior") {
$War = $War + 1;
}
if ($class eq "Beastlord") {
$Bea = $Bea + 1;
}
if ($race eq "Barbarian") {
$Bar = $Bar + 1;
}
if ($race eq "Dark_Elf") {
$Dar = $Dar + 1;
}
if ($race eq "Dwarf") {
$Dwa = $Dwa + 1;
}
if ($race eq "Erudite") {
$Eru = $Eru + 1;
}
if ($race eq "Gnome") {
$Gno = $Gno + 1;
}
if ($race eq "Half_Elf") {
$Hlf = $Hlf + 1;
}
if ($race eq "Halfling") {
$Hal = $Hal + 1;
}
if ($race eq "High_Elf") {
$Hig = $Hig + 1;
}
if ($race eq "Human") {
$Hum = $Hum + 1;
}
if ($race eq "Iskar") {
$Isk = $Isk + 1;
}
if ($race eq "Orge") {
$Org = $Org + 1;
}
if ($race eq "Troll") {
$Tro = $Tro + 1;
}
if ($race eq "Wood_Elf") {
$Woo = $Woo + 1;
}
if ($race eq "Vah_Shir") {
$Vah = $Vah + 1;
}

}


open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($Ausr, $class, $race, $Auser, $lvl) = split(/::/, $line);

$LVL{$lvl} = $LVL{$lvl} + 1;

if ($class eq "Bard") {
$Bard = $Bard + 1;
}
if ($class eq "Cleric") {
$Cle = $Cle + 1;
}
if ($class eq "Druid") {
$Dru = $Dru + 1;
}
if ($class eq "Wizard") {
$Wiz = $Wiz + 1;
}
if ($class eq "Enchanter") {
$Enc = $Enc + 1;
}
if ($class eq "Magician") {
$Mag = $Mag + 1;
}
if ($class eq "Monk") {
$Mon = $Mon + 1;
}
if ($class eq "Necromancer") {
$Nec = $Nec + 1;
}
if ($class eq "Paladin") {
$Pal = $Pal + 1;
}
if ($class eq "Ranger") {
$Ran = $Ran + 1;
}
if ($class eq "Roug") {
$Rou = $Rou + 1;
}
if ($class eq "ShadowKnight") {
$Sk = $Sk + 1;
}
if ($class eq "Shaman") {
$Sha = $Sha + 1;
}
if ($class eq "Warrior") {
$War = $War + 1;
}
if ($class eq "Beastlord") {
$Bea = $Bea + 1;
}
if ($race eq "Barbarian") {
$Bar = $Bar + 1;
}
if ($race eq "Dark_Elf") {
$Dar = $Dar + 1;
}
if ($race eq "Dwarf") {
$Dwa = $Dwa + 1;
}
if ($race eq "Erudite") {
$Eru = $Eru + 1;
}
if ($race eq "Gnome") {
$Gno = $Gno + 1;
}
if ($race eq "Half_Elf") {
$Hlf = $Hlf + 1;
}
if ($race eq "Halfling") {
$Hal = $Hal + 1;
}
if ($race eq "High_Elf") {
$Hig = $Hig + 1;
}
if ($race eq "Human") {
$Hum = $Hum + 1;
}
if ($race eq "Iskar") {
$Isk = $Isk + 1;
}
if ($race eq "Orge") {
$Org = $Org + 1;
}
if ($race eq "Troll") {
$Tro = $Tro + 1;
}
if ($race eq "Wood_Elf") {
$Woo = $Woo + 1;
}
if ($race eq "Vah_Shir") {
$Vah = $Vah + 1;
}

}

$LVL{110} = $LVL{'1'} + $LVL{'2'} + $LVL{'3'} + $LVL{'4'} + $LVL{'5'} + $LVL{'6'} + $LVL{'7'} + $LVL{'8'} + $LVL{'9'} + $LVL{'10'};
$LVL{1120} = $LVL{'11'} + $LVL{'12'} + $LVL{'13'} + $LVL{'14'} + $LVL{'15'} + $LVL{'16'} + $LVL{'17'} + $LVL{'18'} + $LVL{'19'} + $LVL{'20'};
$LVL{2130} = $LVL{'21'} + $LVL{'22'} + $LVL{'23'} + $LVL{'24'} + $LVL{'25'} + $LVL{'26'} + $LVL{'27'} + $LVL{'28'} + $LVL{'29'} + $LVL{'30'};
$LVL{3140} = $LVL{'31'} + $LVL{'32'} + $LVL{'33'} + $LVL{'34'} + $LVL{'35'} + $LVL{'36'} + $LVL{'37'} + $LVL{'38'} + $LVL{'39'} + $LVL{'40'};
$LVL{4150} = $LVL{'41'} + $LVL{'42'} + $LVL{'43'} + $LVL{'44'} + $LVL{'45'} + $LVL{'46'} + $LVL{'47'} + $LVL{'48'} + $LVL{'49'} + $LVL{'50'};
$LVL{5160} = $LVL{'51'} + $LVL{'52'} + $LVL{'53'} + $LVL{'54'} + $LVL{'55'} + $LVL{'56'} + $LVL{'57'} + $LVL{'58'} + $LVL{'59'} + $LVL{'60'};
$LVL{6165} = $LVL{'61'} + $LVL{'62'} + $LVL{'63'} + $LVL{'64'} + $LVL{'65'};


##### Bard #####
$Bardper = $Bard / $members;
$Bardper = sprintf("%3.2f",($Bard/($members || 1))*100);
$Bardwidth = int($Bardper * 1);
$clas = "$clas<TR><TD>Bard</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Bardwidth> $Bardper% ($Bard)</TD></TR>";
##### Cleric #####
$Cleper = $Cle / $members;
$Cleper = sprintf("%3.2f",($Cle/($members || 1))*100);
$Clewidth = int($Cleper * 1);
$clas = "$clas<TR><TD>Cleric</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Clewidth> $Cleper% ($Cle)</TD></TR>";
##### Druid #####
$Druper = $Dru / $members;
$Druper = sprintf("%3.2f",($Dru/($members || 1))*100);
$Druwidth = int($Druper * 1);
$clas = "$clas<TR><TD>Druid</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Druwidth> $Druper% ($Dru)</TD></TR>";
##### Wizard #####
$Wizper = $Wiz / $members;
$Wizper = sprintf("%3.2f",($Wiz/($members || 1))*100);
$Wizwidth = int($Wizper * 1);
$clas = "$clas<TR><TD>Wizard</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Wizwidth> $Wizper% ($Wiz)</TD></TR>";
##### Enchanter #####
$Encper = $Enc / $members;
$Encper = sprintf("%3.2f",($Enc/($members || 1))*100);
$Encwidth = int($Encper * 1);
$clas = "$clas<TR><TD>Enchanter</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Encwidth> $Encper% ($Enc)</TD></TR>";
##### MAGICAN #####
$Magper = $Mag / $members;
$Magper = sprintf("%3.2f",($Mag/($members || 1))*100);
$Magwidth = int($Magper * 1);
$clas = "$clas<TR><TD>Magican</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Magwidth> $Magper% ($Mag)</TD></TR>";
##### Monk #####
$Monper = $Mon / $members;
$Monper = sprintf("%3.2f",($Mon/($members || 1))*100);
$Monwidth = int($Monper * 1);
$clas = "$clas<TR><TD>Monk</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Monwidth> $Monper% ($Mon)</TD></TR>";
##### Necromancer #####
$Necper = $Nec / $members;
$Necper = sprintf("%3.2f",($Nec/($members || 1))*100);
$Necwidth = int($Necper * 1);
$clas = "$clas<TR><TD>Necromancer</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Necwidth> $Necper% ($Nec)</TD></TR>";
##### Paladin #####
$Palper = $Pal / $members;
$Palper = sprintf("%3.2f",($Pal/($members || 1))*100);
$Palwidth = int($per * 1);
$clas = "$clas<TR><TD>Paladin</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Palwidth> $Palper% ($Pal)</TD></TR>";
##### Ranger #####
$Ranper = $Ran / $members;
$Ranper = sprintf("%3.2f",($Ran/($members || 1))*100);
$Ranwidth = int($Ranper * 1);
$clas = "$clas<TR><TD>Ranger</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Ranwidth> $Ranper% ($Ran)</TD></TR>";
##### Roug #####
$Rouper = $Rou / $members;
$Rouper = sprintf("%3.2f",($Rou/($members || 1))*100);
$Rouwidth = int($Rouper * 1);
$clas = "$clas<TR><TD>Roug</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Rouwidth> $Rouper% ($Rou)</TD></TR>";
##### ShadowKnight #####
$Skper = $Sk / $members;
$Skper = sprintf("%3.2f",($Sk/($members || 1))*100);
$Skwidth = int($per * 1);
$clas = "$clas<TR><TD>ShadowKnight</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Skwidth> $Skper% ($Sk)</TD></TR>";
##### Shaman #####
$Shaper = $Sha / $members;
$Shaper = sprintf("%3.2f",($Sha/($members || 1))*100);
$Shawidth = int($Shaper * 1);
$clas = "$clas<TR><TD>Shaman</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Shawidth> $Shaper% ($Sha)</TD></TR>";
##### Warrior #####
$Warper = $Warmag / $members;
$Warper = sprintf("%3.2f",($War/($members || 1))*100);
$Warwidth = int($Warper * 1);
$clas = "$clas<TR><TD>Warrior</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Warwidth> $Warper% ($War)</TD></TR>";
##### Beastlord #####
$Beaper = $Bea / $members;
$Beaper = sprintf("%3.2f",($Bea/($members || 1))*100);
$Beawidth = int($Beaper * 1);
$clas = "$clas<TR><TD>Beastlord</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Beawidth> $Beaper% ($Bea)</TD></TR>";



##### Barbarian #####
$Barper = $Bar / $members;
$Barper = sprintf("%3.2f",($Bar/($members || 1))*100);
$Barwidth = int($Barper * 1);
$rac = "$rac<TR><TD>Barbarian</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Barwidth> $Barper% ($Bar)</TD></TR>";
##### Dark_Elf #####
$Darper = $Dar / $members;
$Darper = sprintf("%3.2f",($Dar/($members || 1))*100);
$Darwidth = int($Darper * 1);
$rac = "$rac<TR><TD>Dark_Elf</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Darwidth> $Darper% ($Dar)</TD></TR>";
##### Dwarf #####
$Dwaper = $Dwa / $members;
$Dwaper = sprintf("%3.2f",($Dwa/($members || 1))*100);
$Dwawidth = int($Dwaper * 1);
$rac = "$rac<TR><TD>Dwarf</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Dwawidth> $Dwaper% ($Dwa)</TD></TR>";
##### Erudite #####
$Eruper = $Eru / $members;
$Eruper = sprintf("%3.2f",($Eru/($members || 1))*100);
$Eruwidth = int($Eruper * 1);
$rac = "$rac<TR><TD>Erudite</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Eruwidth> $Eruper% ($Eru)</TD></TR>";
##### Gnome #####
$Gnoper = $Gno / $members;
$Gnoper = sprintf("%3.2f",($Gno/($members || 1))*100);
$Gnowidth = int($Gnoper * 1);
$rac = "$rac<TR><TD>Gnome</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Gnowidth> $Gnoper% ($Gno)</TD></TR>";
##### Half_Elf #####
$Hlfper = $Hlf / $members;
$Hlfper = sprintf("%3.2f",($Hlf/($members || 1))*100);
$Hlfwidth = int($Hlfper * 1);
$rac = "$rac<TR><TD>Half_Elf</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Hlfwidth> $Hlfper% ($Hlf)</TD></TR>";
##### Halfling #####
$Halper = $Hal / $members;
$Halper = sprintf("%3.2f",($Hal/($members || 1))*100);
$Halwidth = int($Halper * 1);
$rac = "$rac<TR><TD>Halfling</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Halwidth> $Halper% ($Hal)</TD></TR>";
##### High_Elf #####
$Higper = $Hig / $members;
$Higper = sprintf("%3.2f",($Hig/($members || 1))*100);
$Higwidth = int($Higper * 1);
$rac = "$rac<TR><TD>High_Elf</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Higwidth> $Higper% ($Hig)</TD></TR>";
##### Human #####
$Humper = $Hum / $members;
$Humper = sprintf("%3.2f",($Hum/($members || 1))*100);
$Humwidth = int($Humper * 1);
$rac = "$rac<TR><TD>Human</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Humwidth> $Humper% ($Hum)</TD></TR>";
##### Iskar #####
$Iskper = $Isk / $members;
$Iskper = sprintf("%3.2f",($Isk/($members || 1))*100);
$Iskwidth = int($Iskper * 1);
$rac = "$rac<TR><TD>Iskar</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Iskwidth> $Iskper% ($Isk)</TD></TR>";
##### Orge #####
$Orgper = $Org / $members;
$Orgper = sprintf("%3.2f",($Org/($members || 1))*100);
$Orgwidth = int($Orgper * 1);
$rac = "$rac<TR><TD>Orge</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Orgwidth> $Orgper% ($Org)</TD></TR>";
##### Troll #####
$Troper = $Tro / $members;
$Troper = sprintf("%3.2f",($Tro/($members || 1))*100);
$Trowidth = int($Troper * 1);
$rac = "$rac<TR><TD>Troll</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Trowidth> $Troper% ($Tro)</TD></TR>";
##### Wood_Elf #####
$Wooper = $Woo / $members;
$Wooper = sprintf("%3.2f",($Woo/($members || 1))*100);
$Woowidth = int($Wooper * 1);
$rac = "$rac<TR><TD>Wood_Elf</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Woowidth> $Wooper% ($Woo)</TD></TR>";
##### Vah_Shir #####
$Vahper = $Vah / $members;
$Vahper = sprintf("%3.2f",($Vah/($members || 1))*100);
$Vahwidth = int($Vahper * 1);
$rac = "$rac<TR><TD>Vah_Shir</TD><TD><img align=absmiddle src=stats.gif height=10 width=$Vahwidth> $Vahper% ($Vah)</TD></TR>";


##### 1-10 #####
$per = $LVL{'110'} / $members;
$per = sprintf("%3.2f",($LVL{'110'}/($members || 1))*100);
$width = int($per * 1);
$lv = "$lv<TR><TD>lvl 1-10</TD><TD><img align=absmiddle src=stats.gif height=10 width=$width> $per% ($LVL{'110'})</TD></TR>";

##### 11-20 #####
$per = $LVL{'1120'} / $members;
$per = sprintf("%3.2f",($LVL{'1120'}/($members || 1))*100);
$width = int($per * 1);
$lv = "$lv<TR><TD>lvl 11-20</TD><TD><img align=absmiddle src=stats.gif height=10 width=$width> $per% ($LVL{'1120'})</TD></TR>";

##### 2130 #####
$per = $LVL{'2130'} / $members;
$per = sprintf("%3.2f",($LVL{'2130'}/($members || 1))*100);
$width = int($per * 1);
$lv = "$lv<TR><TD>lvl 21-30</TD><TD><img align=absmiddle src=stats.gif height=10 width=$width> $per% ($LVL{'2130'})</TD></TR>";

##### 3140 #####
$per = $LVL{'3140'} / $members;
$per = sprintf("%3.2f",($LVL{'3140'}/($members || 1))*100);
$width = int($per * 1);
$lv = "$lv<TR><TD>lvl 31-40</TD><TD><img align=absmiddle src=stats.gif height=10 width=$width> $per% ($LVL{'3140'})</TD></TR>";

##### 4150 #####
$per = $LVL{'4150'} / $members;
$per = sprintf("%3.2f",($LVL{'4150'}/($members || 1))*100);
$width = int($per * 1);
$lv = "$lv<TR><TD>lvl 41-50</TD><TD><img align=absmiddle src=stats.gif height=10 width=$width> $per% ($LVL{'4150'})</TD></TR>";

##### 5160 #####
$per = $LVL{'5160'} / $members;
$per = sprintf("%3.2f",($LVL{'5160'}/($members || 1))*100);
$width = int($per * 1);
$lv = "$lv<TR><TD>lvl 51-60</TD><TD><img align=absmiddle src=stats.gif height=10 width=$width> $per% ($LVL{'5160'})</TD></TR>";

##### 6165 #####
$per = $LVL{'6165'} / $members;
$per = sprintf("%3.2f",($LVL{'6165'}/($members || 1))*100);
$width = int($per * 1);
$lv = "$lv<TR><TD>lvl 61-65</TD><TD><img align=absmiddle src=stats.gif height=10 width=$width> $per% ($LVL{'6165'})</TD></TR>";


$file = "stats.tmp";
&output;
}

#########################################################################

sub sugraid {
$zlvl = $INPUT{'zb'} - $INPUT{'za'};
$zlvl = $zlvl / 2;
$zlvl = $zlvl + $INPUT{'za'};
$items = $zlvl * $INPUT{'zamt'};

open (DATA, "raid.lst");
@data = <DATA>;
close DATA;
open(DATA, ">raid.lst");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$Cookies{'user'}::$INPUT{'zname'}::$INPUT{'za'}::$INPUT{'zb'}::$INPUT{'zamt'}::$INPUT{'zitems'}\n";
close DATA;


$cont = "Your Raid/Event has been submited for review.<BR><TABLE BORDER=0 class=table><TR><TD>";
$cont = "$cont<TR><TD>Zone:</TD><TD>$INPUT{'zname'}</TD></TR>";
$cont = "$cont<TR><TD>Aprox level:</TD><TD>$zlvl</TD></TR>";
$cont = "$cont<TR><TD>Items needed:</TD><TD>$INPUT{'zamt'}</TD></TR>";
$cont = "$cont<TR><TD COLSPAN=2>$INPUT{'zitems'}</TD></TR>";
$cont = "$cont<TR><TD COLSPAN=2>You need $items raid points.</TD></TR></TABLE>";
$cont = "$cont If you do not have enuff points your raid will still be consitered by the DC councl.";

$file = "view_page.tmp";
&output;
}

#########################################################################

sub deleteraid {
open (DATA, "raid.lst");
@data = <DATA>;
close DATA;
open(DATA, ">raid.lst");
foreach $line (@data) {
chomp ($line);
($usr, $zone, $za, $zb, $zamt, $zitems) = split(/::/, $line);
if ($usr eq "$INPUT{'usr'}") {
if ($zone eq "$INPUT{'zone'}") {
if ($zitems eq "$INPUT{'zitems'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}
else {
print DATA "$line\n";
}
}
else {
print DATA "$line\n";
}
}
$cont = "Raid Deleted";

$file = "view_page.tmp";
&output;
}
#########################################################################
sub viewraid {
$cont = "$cont<TABLE BORDER=0 class=table>";
$cont = "$cont<TR><TD>Users name</TD><TD>Zone Name</TD><TD>Zone Level</TD><TD>Amount of items</TD><TD>Items Needed</TD><TD>Delete</TD></TR>";
open (DATA, "raid.lst");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($usr, $zone, $za, $zb, $zamt, $zitems) = split(/::/, $line);

$zlvl = $zb - $za;
$zlvl = $zlvl / 2;
$zlvl = $zlvl + $za;

$cont = "$cont<TR><FORM><TD>$usr<INPUT TYPE=hidden name=usr value=$usr></TD><TD>$zone<INPUT TYPE=hidden name=zone value=$zone></TD><TD>$zlvl</TD><TD>$zamt</TD><TD>$zitems<INPUT TYPE=hidden name=zitems value=\"$zitems\"></TD><TD><INPUT TYPE=SUBMIT NAME=a VALUE=deleteraid></TD></FORM></TR>";
}
$cont = "$cont</TABLE>";

$file = "view_page.tmp";
&output;
}
#########################################################################
sub signup {
$con = "0";
$val = "0";

$name = $INPUT{'name'};
$pass = $INPUT{'pass'};
$pass2 = $INPUT{'pass2'};
$race = $INPUT{'race'};
$class = $INPUT{'class'};

if ($name eq "") { 
$cont = "$cont You must enter a EQ Name";
$con = "1";
}
if ($pass eq "") { 
$cont = "$cont You must enter a Password";
$con = "1";
}
if ($pass2 eq "") { 
$cont = "$cont You Must Re-Type your Password to conferm";
$con = "1";
}
if ($INPUT{'email'} eq "") { 
$cont = "$cont You must enter a E-Mail";
$con = "1";
}
if ($race eq "") { 
$cont = "$cont You must enter a Race";
$con = "1";
}
if ($class eq "") { 
$cont = "$cont You must enter a class";
$con = "1";
}
if ($con eq "1") {
$cont = "$cont Please Hit your brosers back butten!";
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
$cont = " EQ name allready registered<br> ";
$cont = "$con Please Hit your brosers back butten!";
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

$cont = "Thank you $INPUT{'name'}<BR>";
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
$cont = "Your passwords dident mach<br>";
$cont = "$cont Please Hit your brosers back butten!";
} #else

$file = "save_sign.tmp";
&output;
}

#########################################################################

sub newalbum {

open (DATA, "photo.lst");
@data = <DATA>;
close DATA;
open(DATA, ">photo.lst");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'shtname'}::$INPUT{'lngname'}\n";
close DATA;


$cont = "$cont New Album Added.";

$file = "photo.tmp";
&output;
}

#########################################################################

sub pform {
$pag = "$pag<SELECT NAME=page id=input>";

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

#########################################################################

sub uploadfile {

$cont = "$cont Photo Added";

open (FILE,"tmps/photo.tmp");
$file = "photo.tmp";
&output;

$INPUT{'desc'} =~ s/ /%20/gi;

open (DATA, "$INPUT{'page'}.lst");
@data = <DATA>;
close DATA;
open(DATA, ">$INPUT{'page'}.lst");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$abcdefg$INPUT{'destn_filename'}::$INPUT{'desc'}\n";
close DATA;

}

#########################################################################

sub view {
print "Content-type: text/html\n\n";


open (FILE, "data/$INPUT{'user'}");
flock (FILE, 2);
$aaausr = <FILE>;
chop ($aaausr);
$aaacryptpass = <FILE>;
chop ($aaacryptpass);
$aaaemail = <FILE>;
chop ($aaaemail);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$aaatype = <FILE>;
chop ($aaatype);
$aaaacc = <FILE>;
chop ($aaaacc);
$aaarank = <FILE>;
chop ($aaarank);
$pts = <FILE>;
chop ($pts);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

open (FILE, "profile/$INPUT{'user'}");
flock (FILE, 2);
$sir = <FILE>;
chop ($sir);
$lvl = <FILE>;
chop ($lvl);
$img = <FILE>;
chop ($img);
$rel = <FILE>;
chop ($rel);
$say = <FILE>;
chop ($say);
$ac = <FILE>;
chop ($ac);
$atk = <FILE>;
chop ($atk);
$str = <FILE>;
chop ($str);
$sta = <FILE>;
chop ($sta);
$agi = <FILE>;
chop ($agi);
$dex = <FILE>;
chop ($dex);
$wis = <FILE>;
chop ($wis);
$int = <FILE>;
chop ($int);
$cha = <FILE>;
chop ($cha);
flock (FILE, 14);
close(FILE);

$file = "view_profile.tmp";
&output;

}


##################################################################################

sub form {
print "Content-type: text/html\n\n";
&GetCookies('user');

open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$aaausr = <FILE>;
chop ($aaausr);
$aaacryptpass = <FILE>;
chop ($aaacryptpass);
$aaaemail = <FILE>;
chop ($aaaemail);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$aaatype = <FILE>;
chop ($aaatype);
$aaaacc = <FILE>;
chop ($aaaacc);
$aaarank = <FILE>;
chop ($aaarank);
$pts = <FILE>;
chop ($pts);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);



$css = "<SELECT NAME=css id=input>";
open (DATA, "css.lst");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);

if ($line eq "$style") {
$css = "$css<OPTION SELECTED>$line";
}

else {
$css = "$css<OPTION>$line";
}

}
$css = "$css</SELECT>";




open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($Ausr, $Aclass, $Arace, $Auser, $Alvl) = split(/::/, $line);

if ($Auser eq "$Cookies{'user'}") {
$alt = "$alt<TR><TD><div id=profileedittext>$Ausr</div></TD><TD><div id=profileedittext>$Alvl</div></TD><TD><div id=profileedittext>$Aclass</div></TD><TD><div id=profileedittext>$Arace</div></TD><TD>";
$alt = "$alt<FORM><INPUT TYPE=hidden NAME=usr VALUE=$Ausr><INPUT TYPE=hidden NAME=alvl VALUE=$Alvl>";
$alt = "$alt<INPUT TYPE=hidden NAME=aclass VALUE=$Aclass><INPUT TYPE=hidden NAME=arace VALUE=$Arace>";
$alt = "$alt<INPUT TYPE=hidden NAME=user VALUE=$Auser><INPUT NAME=a TYPE=submit VALUE=EditAlt id=input></FORM></TD>";
$alt = "$alt<TD><FORM><INPUT TYPE=hidden NAME=usr VALUE=$Ausr><INPUT TYPE=hidden NAME=alvl VALUE=$Alvl>";
$alt = "$alt<INPUT TYPE=hidden NAME=aclass VALUE=$Aclass><INPUT TYPE=hidden NAME=arace VALUE=$Arace>";
$alt = "$alt<INPUT TYPE=hidden NAME=user VALUE=$Auser><INPUT NAME=a TYPE=submit VALUE=DeleteAlt id=input></FORM></TD></TR>\n";
}

}

$file = "profile_form.tmp";
&output;
}

##################################################################################

sub ccss {
print "Content-type: text/html\n\n";
&GetCookies('user');


open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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
$pts = <FILE>;
chop ($pts);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);


open (DATA, "data/$Cookies{'user'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$Cookies{'user'}");

print DATA "$usr\n";
print DATA "$cryptpass\n";
print DATA "$email\n";
print DATA "$race\n";
print DATA "$class\n";
print DATA "$type\n";
print DATA "$acc\n";
print DATA "$rank\n";
print DATA "$pts\n";
print DATA "$INPUT{'css'}\n";
print DATA "junk\n";

close DATA;


$file = "change_css.tmp";
&output;
}

##################################################################################

sub wizard {
print "Content-type: text/html\n\n";
&GetCookies('user');

open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$aaausr = <FILE>;
chop ($aaausr);
$aaacryptpass = <FILE>;
chop ($aaacryptpass);
$aaaemail = <FILE>;
chop ($aaaemail);
$race = <FILE>;
chop ($race);
$class = <FILE>;
chop ($class);
$aaatype = <FILE>;
chop ($aaatype);
$aaaacc = <FILE>;
chop ($aaaacc);
$aaarank = <FILE>;
chop ($aaarank);
$pts = <FILE>;
chop ($pts);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

open (FILE, "profile/$Cookies{'user'}");
flock (FILE, 2);
$sir = <FILE>;
chop ($sir);
$lvl = <FILE>;
chop ($lvl);
$img = <FILE>;
chop ($img);
$rel = <FILE>;
chop ($rel);
$say = <FILE>;
chop ($say);
$ac = <FILE>;
chop ($ac);
$atk = <FILE>;
chop ($atk);
$str = <FILE>;
chop ($str);
$sta = <FILE>;
chop ($sta);
$agi = <FILE>;
chop ($agi);
$dex = <FILE>;
chop ($dex);
$wis = <FILE>;
chop ($wis);
$int = <FILE>;
chop ($int);
$cha = <FILE>;
chop ($cha);
flock (FILE, 14);
close(FILE);

$file = "profile_edit.tmp";
&output;
}

##################################################################################

sub upwiz {
print "Content-type: text/html\n\n";
&GetCookies('user');

open (DATA, "profile/$Cookies{'user'}");
@data = <DATA>;
close DATA;
open(DATA, ">profile/$Cookies{'user'}");
print DATA "$INPUT{'sir'}\n";
print DATA "$INPUT{'lvl'}\n";
print DATA "$INPUT{'img'}\n";
print DATA "$INPUT{'rel'}\n";
print DATA "$INPUT{'say'}\n";
print DATA "$INPUT{'ac'}\n";
print DATA "$INPUT{'atk'}\n";
print DATA "$INPUT{'str'}\n";
print DATA "$INPUT{'sta'}\n";
print DATA "$INPUT{'agi'}\n";
print DATA "$INPUT{'dex'}\n";
print DATA "$INPUT{'wis'}\n";
print DATA "$INPUT{'int'}\n";
print DATA "$INPUT{'cha'}\n";
print DATA "junk\n";
close DATA;


$file = "profile_save.tmp";
&output;
}

##################################################################################

sub addalt {
print "Content-type: text/html\n\n";

$file = "add_alt.tmp";
&output;
}

##################################################################################

sub addaltb {
print "Content-type: text/html\n\n";

&GetCookies('user');
$INPUT{'usr'} =~ s/ /_/gi;

open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;
open(DATA, ">data/members.alt");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'usr'}::$INPUT{'class'}::$INPUT{'race'}::$Cookies{'user'}::$INPUT{'lvl'}\n";
close DATA;

$file = "save_alt.tmp";
&output;
}

##################################################################################

sub editalt {
print "Content-type: text/html\n\n";

$altclass = "<SELECT NAME=class id=input>";

if ($INPUT{'aclass'} eq "Bard") { 
$altclass = "$altclass<OPTION SELECTED>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Cleric") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION SELECTED>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Druid") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION SELECTED>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Wizard") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION SELECTED>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Enchanter") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION SELECTED>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Magician") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION SELECTED>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Monk") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION SELECTED>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Necromancer") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION SELECTED>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Paladin") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION SELECTED>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Ranger") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION SELECTED>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Roug") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION SELECTED>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "ShadowKnight") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION SELECTED>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Shaman") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION SELECTED>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Warrior") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION SELECTED>Warrior";
$altclass = "$altclass<OPTION>Beastlord";
}
elsif ($INPUT{'aclass'} eq "Beastlord") {
$altclass = "$altclass<OPTION>Bard";
$altclass = "$altclass<OPTION>Cleric";
$altclass = "$altclass<OPTION>Druid";
$altclass = "$altclass<OPTION>Wizard";
$altclass = "$altclass<OPTION>Enchanter";
$altclass = "$altclass<OPTION>Magician";
$altclass = "$altclass<OPTION>Monk";
$altclass = "$altclass<OPTION>Necromancer";
$altclass = "$altclass<OPTION>Paladin";
$altclass = "$altclass<OPTION>Ranger";
$altclass = "$altclass<OPTION>Roug";
$altclass = "$altclass<OPTION>ShadowKnight";
$altclass = "$altclass<OPTION>Shaman";
$altclass = "$altclass<OPTION>Warrior";
$altclass = "$altclass<OPTION SELECTED>Beastlord";
}
$altclass = "$altclass</SELECT>";

$altrace = "<SELECT NAME=race id=input>";

if ($INPUT{'arace'} eq "Barbarian") {
$altrace = "$altrace<OPTION SELECTED>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Dark_Elf") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION SELECTED>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Dwarf") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION SELECTED>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Erudite") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION SELECTED>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Gnome") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION SELECTED>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Half_Elf") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION SELECTED>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Halfling") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION SELECTED>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "High_Elf") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION SELECTED>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Human") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION SELECTED>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Iskar") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION SELECTED>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Orge") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION SELECTED>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Troll") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION SELECTED>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Wood_Elf") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION SELECTED>Wood_Elf";
$altrace = "$altrace<OPTION>Vah_Shir";
}
elsif ($INPUT{'arace'} eq "Vah_Shir") {
$altrace = "$altrace<OPTION>Barbarian";
$altrace = "$altrace<OPTION>Dark_Elf";
$altrace = "$altrace<OPTION>Dwarf";
$altrace = "$altrace<OPTION>Erudite";
$altrace = "$altrace<OPTION>Gnome";
$altrace = "$altrace<OPTION>Half_Elf";
$altrace = "$altrace<OPTION>Halfling";
$altrace = "$altrace<OPTION>High_Elf";
$altrace = "$altrace<OPTION>Human";
$altrace = "$altrace<OPTION>Iskar";
$altrace = "$altrace<OPTION>Orge";
$altrace = "$altrace<OPTION>Troll";
$altrace = "$altrace<OPTION>Wood_Elf";
$altrace = "$altrace<OPTION SELECTED>Vah_Shir";
}

$altrace = "$altrace</SELECT>"; 


$file = "edit_alt.tmp";
&output;

}

##################################################################################

sub editaltb {

open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;

open(DATA, ">data/members.alt");
foreach $line (@data) {
chomp ($line);
($Ausr, $Aclass, $Arace, $Auser, $alvl) = split(/::/, $line);
if ($Ausr eq "$INPUT{'ausr'}") {
print DATA "$INPUT{'usr'}::$INPUT{'class'}::$INPUT{'race'}::$INPUT{'user'}::$INPUT{'lvl'}\n";
}
else {
print DATA "$line\n";
}
}

print "Content-type: text/html\n\n";

$file = "update_alt.tmp";
&output;

}

##################################################################################

sub deletealt {

open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;
open(DATA, ">data/members.alt");
foreach $line (@data) {
chomp ($line);
($Ausr, $Aclass, $Arace, $Auser, $alvl) = split(/::/, $line);
if ($Ausr eq "$INPUT{'usr'}") {
print DATA "";
}
else {
print DATA "$line\n";
}
}

print "Content-type: text/html\n\n";

$file = "delete_alt.tmp";
&output;
}

##################################################################################

sub pass {
print "Content-type: text/html\n\n";

$file = "change_pass.tmp";
&output;
}

##################################################################################

sub uppass {
&GetCookies('user');
open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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
$pts = <FILE>;
chop ($pts);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

print "Content-type: text/html\n\n";

if ($INPUT{'newpass'} eq "") {

$cont = "<CENTER>New Password invalid!";
}
else {

if ($INPUT{'oldpass'} eq "$cryptpass") {
if ($INPUT{'newpass'} eq "$INPUT{'newpassb'}") {

open (DATA, "data/$Cookies{'user'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$Cookies{'user'}");

print DATA "$usr\n";
print DATA "$INPUT{'newpass'}\n";
print DATA "$email\n";
print DATA "$race\n";
print DATA "$class\n";
print DATA "$type\n";
print DATA "$acc\n";
print DATA "$rank\n";
print DATA "$pts\n";
print DATA "$style\n";
print DATA "junk\n";

close DATA;
$cont = "<CENTER>Password Changed!";
}
else {
$cont = "<CENTER>New Passwords did not match!";
}
}
else {
$cont = "<CENTER>Old Password invalid!";
}
}


$file = "save_pass.tmp";
&output;

}

##################################################################################

sub info {
&GetCookies('user');
open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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
$pts = <FILE>;
chop ($pts);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
print "Content-type: text/html\n\n";

$file = "change_email.tmp";
&output;

}

##################################################################################

sub upinfo {
&GetCookies('user');
open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$usr = <FILE>;
chop ($usr);
$cryptpass = <FILE>;
chop ($cryptpass);
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
$pts = <FILE>;
chop ($pts);
$style = <FILE>;
chop ($style);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

print "Content-type: text/html\n\n";

open (DATA, "data/$Cookies{'user'}");
@data = <DATA>;
close DATA;
open(DATA, ">data/$Cookies{'user'}");

print DATA "$usr\n";
print DATA "$cryptpass\n";
print DATA "$INPUT{'email'}\n";
print DATA "$race\n";
print DATA "$class\n";
print DATA "$type\n";
print DATA "$acc\n";
print DATA "$rank\n";
print DATA "$pts\n";
print DATA "$style\n";
print DATA "junk\n";

close DATA;

$file = "update_email.tmp";
&output;

}

##################################################################################

sub output {


open (FILE, "data/$Cookies{'user'}");
flock (FILE, 2);
$ousr = <FILE>;
chop ($oname);
$opass = <FILE>;
chop ($opass);
$oemail = <FILE>;
chop ($oemail);
$orace = <FILE>;
chop ($orace);
$oclass = <FILE>;
chop ($oclass);
$otype = <FILE>;
chop ($otype);
$oacc = <FILE>;
chop ($oacc);
$orank = <FILE>;
chop ($orank);
$oraid = <FILE>;
chop ($oraid);
$style = <FILE>;
chop ($style);
$ojunk = <FILE>;
chop ($ojunk);
flock (FILE, 8);
close(FILE);
####STARTRANKS
open (DATA, "ranks.lst");
@data = <DATA>;
close DATA;
$ranks = "@data";
####ENDRANKS
####STARTHEADER
open (DATA, "tmps/header.tmp");
@data = <DATA>;
close DATA;
$header = "@data";
####ENDHEADER
####STARTNEWS
open (DATA, "news.dat");
@data = <DATA>;
close DATA;
$news = "@data";
####ENDNEWS
####STARTLINKS
open (DATA, "links.dat");
@data = <DATA>;
close DATA;
$links = "@data";
####ENDLINKS
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
$message = "<div id=message>You Have No Messages</div>";
}
else {
$message = "<A HREF=$cgipath/msg/msg.cgi?a=list id=message>You have $count Messages</A>";
}
####ENDMESSAGE
if ($style eq "") {
$style = "Defalt";
}
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
$file_content =~ s/!!edittype!!/$type/gi;
$file_content =~ s/!!raidpoints!!/$oraid/gi;
$file_content =~ s/!!header!!/$header/gi;
$file_content =~ s/!!sndmesslist!!/$messlist/gi;
$file_content =~ s/!!stylesheet!!/$style/gi;
$file_content =~ s/!!links!!/$links/gi;
close (FILE);

print "$file_content";

}