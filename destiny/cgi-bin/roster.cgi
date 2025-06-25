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
if ($value eq "") { $value = "NULL"; }
    $INPUT{$name} = $value;
}

use LWP::Simple; 

$mymode = "$INPUT{'mode'}";

if ($INPUT{'mode'} eq "") {
$mymode = "rank";
}

$page = "http://eq2players.station.sony.com/en/guild_roster.vm?mode=$mymode&guildId=432113";

$begincut = "Join Date</td>";

$endcut = "<td width=\"12\"  background=\"/images/en/boxes/dark/tile_right.gif\">";



$_ = get($page); 

print "Content-type: text/html\n\n";


 s/^.*$begincut//s;

 s/$endcut.*$//s;

$_ =~ s/class="field_data_small"/TARGEt="_new"/gi;

print "<HTML><HEAD><link rel=stylesheet href=http://www.destinyeq2.com/themes/roster.css type=text/css></HEAD><BODY>";

print "<table width=100% border=0 class=menu><tr>";
print "<td><A HREF=roster.cgi?mode=rank>Rank</A></td>";
print "<td>&nbsp;&nbsp;</td>";
print "<td><A HREF=roster.cgi?mode=character_name>Name</A></td>";
print "<td>&nbsp;&nbsp;</td>";
print "<td><nobr><A HREF=roster.cgi?mode=character_class>Class</A> (<A HREF=roster.cgi?mode=character_level>Level</A>)</nobr></td>";
print "<td>&nbsp;</td>";
print "<td><nobr><A HREF=roster.cgi?mode=artisan_class>Artisan Class</A> (<A HREF=roster.cgi?mode=artisan_level>Level</A>)</nobr></td>";
print "<td>&nbsp;</td>";
print "<td><A HREF=roster.cgi?mode=quests>Quests</A></td>";
print "<td>&nbsp;</td>";
print "<td><A HREF=roster.cgi?mode=ratio>KVD Ratio</A></td>";
print "<td>&nbsp;</td>";
print "<td><A HREF=roster.cgi?mode=status>Status</A></td>";
print "<td>&nbsp;</td>";
print "<td><A HREF=roster.cgi?mode=join_date>Join Date</A></td></tr>";


print $_; 


print "</TABLE><BR><P> <CENTER><SMALL>Imported from <A HREF=http://www.eq2players.com target=_new><SMALL>EQ2Players.com</SMALL></A>! If anything is incorrect.... its there fault. =)</SMALL></BODY></HTML>";

exit;
