#!/usr/bin/perl

require 'cookie.lib';

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

if ($INPUT{'a'} eq "view") { &view; }
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
else { &error; }

##################################################################################

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

open (DATA, "data/members.alt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($Ausr, $Aclass, $Arace, $Auser, $Alvl) = split(/::/, $line);

if ($Auser eq "$Cookies{'user'}") {
$alt = "$alt<TR><TD>$Ausr</TD><TD>$Alvl</TD><TD>$Aclass</TD><TD>$Arace</TD><TD>";
$alt = "$alt<FORM><INPUT TYPE=hidden NAME=usr VALUE=$Ausr><INPUT TYPE=hidden NAME=alvl VALUE=$Alvl>";
$alt = "$alt<INPUT TYPE=hidden NAME=aclass VALUE=$Aclass><INPUT TYPE=hidden NAME=arace VALUE=$Arace>";
$alt = "$alt<INPUT TYPE=hidden NAME=user VALUE=$Auser><INPUT NAME=a TYPE=submit VALUE=EditAlt></FORM></TD>";
$alt = "$alt<TD><FORM><INPUT TYPE=hidden NAME=usr VALUE=$Ausr><INPUT TYPE=hidden NAME=alvl VALUE=$Alvl>";
$alt = "$alt<INPUT TYPE=hidden NAME=aclass VALUE=$Aclass><INPUT TYPE=hidden NAME=arace VALUE=$Arace>";
$alt = "$alt<INPUT TYPE=hidden NAME=user VALUE=$Auser><INPUT NAME=a TYPE=submit VALUE=DeleteAlt></FORM></TD></TR>\n";
}

}

$file = "profile_form.tmp";
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

$altclass = "<SELECT NAME=class>";

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

$altrace = "<SELECT NAME=race>";

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
($Ausr, $Aclass, $Arace, $Auser) = split(/::/, $line);
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
print DATA "junk\n";

close DATA;

$file = "update_email.tmp";
&output;

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