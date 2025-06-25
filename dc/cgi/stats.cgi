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

print "Content-type: text/html\n\n";

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
##################################################################################

$LVL{110} = $LVL{'1'} + $LVL{'2'} + $LVL{'3'} + $LVL{'4'} + $LVL{'5'} + $LVL{'6'} + $LVL{'7'} + $LVL{'8'} + $LVL{'9'} + $LVL{'10'};
$LVL{1120} = $LVL{'11'} + $LVL{'12'} + $LVL{'13'} + $LVL{'14'} + $LVL{'15'} + $LVL{'16'} + $LVL{'17'} + $LVL{'18'} + $LVL{'19'} + $LVL{'20'};
$LVL{2130} = $LVL{'21'} + $LVL{'22'} + $LVL{'23'} + $LVL{'24'} + $LVL{'25'} + $LVL{'26'} + $LVL{'27'} + $LVL{'28'} + $LVL{'29'} + $LVL{'30'};
$LVL{3140} = $LVL{'31'} + $LVL{'32'} + $LVL{'33'} + $LVL{'34'} + $LVL{'35'} + $LVL{'36'} + $LVL{'37'} + $LVL{'38'} + $LVL{'39'} + $LVL{'40'};
$LVL{4150} = $LVL{'41'} + $LVL{'42'} + $LVL{'43'} + $LVL{'44'} + $LVL{'45'} + $LVL{'46'} + $LVL{'47'} + $LVL{'48'} + $LVL{'49'} + $LVL{'50'};
$LVL{5160} = $LVL{'51'} + $LVL{'52'} + $LVL{'53'} + $LVL{'54'} + $LVL{'55'} + $LVL{'56'} + $LVL{'57'} + $LVL{'58'} + $LVL{'59'} + $LVL{'60'};
$LVL{6165} = $LVL{'61'} + $LVL{'62'} + $LVL{'63'} + $LVL{'64'} + $LVL{'65'};

##################################################################################


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