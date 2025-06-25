#!/usr/bin/perl

use DBI;
$| = 1;
use CGI::Carp qw(fatalsToBrowser);
$scriptname = "Page";
$scriptver = "0.9.9";

BEGIN {

	require "../../config.pl";
	require "$lang";
	require "$sourcedir/subs.pl";


	push(@INC,$cm_scriptDir);
}

eval {
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};

if ($@) {
	print "Content-type: text/html\n\n";
	print qq~<h1>Software Error:</h1>
		Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
		<pre>$@</pre>
		<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
		~;
	exit;
}

&parse_form;


logips();
loadcookie();
loaduser();
logvisitors();


########################################

if ($input{'do'} eq "view") { &view; }

else {

$navbar = "&nbsp;$btn{'014'}&nbsp; $input{'go'}";

print_top();


print qq~
<CENTER>
  <TABLE border="0" cellspacing="0" cellpadding="0" class="forumtitlebackcolor" WIDTH=50%>
    <TR>
      <TD class="boardtitle">Name</TD>
      <TD class="boardtitle">Quanty</TD>
    </TR>
~;

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp ="
SELECT  *
FROM guildbank 
order by name
";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

print qq~
    <TR>
      <TD class="forumwindow2"><A HREF=http://www.eqguilded.com/freefire/cgi-bin/mods/bank/bank.cgi?do=view&show=$row[0] onclick="NewWindow(this.href,'name','420','220','yes');return false;">$row[2]</A></TD>
      <TD class="forumwindow2">$row[1]</TD>
~;
	  
 } 

}
$sth->finish; 
$dbh->disconnect;

print qq~
  </TABLE>
</CENTER>
~;

print_bottom();

}

########################################

sub view {

$show = "$input{'show'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from bank WHERE num='$show'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$num = "$row[0]";

$myrow[1] = "$row[1]";
$myrow[2] = "$row[2]";
$myrow[3] = "$row[3]";
$myrow[4] = "$row[4]";
$myrow[5] = "$row[5]";
$myrow[6] = "$row[6]";
$myrow[7] = "$row[7]";
$myrow[8] = "$row[8]";
$myrow[9] = "$row[9]";
$myrow[10] = "$row[10]";
$myrow[11] = "$row[11]";
$myrow[12] = "$row[12]";
$myrow[13] = "$row[13]";
$myrow[14] = "$row[14]";
$myrow[15] = "$row[15]";
$myrow[16] = "$row[16]";
$myrow[17] = "$row[17]";
$myrow[18] = "$row[18]";
$myrow[19] = "$row[19]";
$myrow[20] = "$row[20]";
$myrow[21] = "$row[21]";
$myrow[22] = "$row[22]";
$myrow[23] = "$row[23]";
$myrow[24] = "$row[24]";
$myrow[25] = "$row[25]";
$myrow[26] = "$row[26]";
$myrow[27] = "$row[27]";
$myrow[28] = "$row[28]";
$myrow[29] = "$row[29]";
$myrow[30] = "$row[30]";
$myrow[31] = "$row[31]";
$myrow[32] = "$row[32]";
$myrow[33] = "$row[33]";
$myrow[34] = "$row[34]";
$myrow[35] = "$row[35]";
$myrow[36] = "$row[36]";
$myrow[37] = "$row[37]";
$myrow[38] = "$row[38]";
$myrow[39] = "$row[39]";
$myrow[40] = "$row[40]";
$myrow[41] = "$row[41]";
$myrow[42] = "$row[42]";
$myrow[43] = "$row[43]";
$myrow[44] = "$row[44]";
$myrow[45] = "$row[45]";
$myrow[46] = "$row[46]";
$myrow[47] = "$row[47]";
$myrow[48] = "$row[48]";
$myrow[49] = "$row[49]";
$myrow[50] = "$row[50]";
$myrow[51] = "$row[51]";
$myrow[52] = "$row[52]";
$myrow[53] = "$row[53]";
$myrow[54] = "$row[54]";
$myrow[55] = "$row[55]";
$myrow[56] = "$row[56]";
$myrow[57] = "$row[57]";
$myrow[58] = "$row[58]";
$myrow[59] = "$row[59]";
$myrow[60] = "$row[60]";
$myrow[61] = "$row[61]";
$myrow[62] = "$row[62]";
$myrow[63] = "$row[63]";
$myrow[64] = "$row[64]";
$myrow[65] = "$row[65]";
$myrow[66] = "$row[66]";
$myrow[67] = "$row[67]";
$myrow[68] = "$row[68]";
 } 

}
$sth->finish; 
$dbh->disconnect; 


print "Content-type: text/html\n\n";

$color = "CCCCDD";

print qq~

<HTML>
<HEAD>
  <TITLE>$myrow[1]</TITLE>
</HEAD>
<BODY BGCOLOR="Gray" TEXT="#000000">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2" WIDTH="100%">
  <TR>
    <TD BGCOLOR="#CCCCDD"><B>$myrow[1]</B></TD>
  </TR>
  <TR>
    <TD BGCOLOR="#88BBEE"><small><B>
~;

if ($myrow[2] eq "1") { 
print "LORE ITEM   "; 
$color = "88BBEE";
}
if ($myrow[3] eq "1") { 
print "MAGIC ITEM   "; 
$color = "88BBEE";
}
if ($myrow[4] eq "1") { 
print "NO DROP"; 
$color = "88BBEE";
}

print "</B></TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

print qq~
<TR><TD BGCOLOR="$color"><small><B>Type:</B> $myrow[5] <B>Slot:</B> $myrow[6]</TD></TR>
~;

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

if ($myrow[7] ne "0") {
print "<TR><TD BGCOLOR=$color><small><B>DMG:</B> $myrow[7] <B>DLY:</B> $myrow[8] ";

if ($myrow[9] ne "0") {
print "<B>DMG Bonus:</B> $myrow[9]";
}

print "</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

}

print "<TR><TD BGCOLOR=$color><small><B>AC:</B> $myrow[10]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

if ($myrow[11] ne "") {

print "<TR><TD BGCOLOR=$color><small><B>Effect:</B> $myrow[11]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

}

if ($myrow[12] ne "") {

print "<TR><TD BGCOLOR=$color><small><B>Bane:</B> $myrow[12]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

}

if ($myrow[13] ne "") {

print "<TR><TD BGCOLOR=$color><small><B>Skill Mod:</B> $myrow[13]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

}

if ($myrow[14] ne "") {

print "<TR><TD BGCOLOR=$color><small><B>Focus:</B> $myrow[14]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

}


print "<TR><TD BGCOLOR=$color><small>";

if ($myrow[15] ne "0") { print "<B>DEX:</B> $myrow[15] "; }
if ($myrow[16] ne "0") { print "<B>STA:</B> $myrow[16] "; }
if ($myrow[17] ne "0") { print "<B>STR:</B> $myrow[17] "; }
if ($myrow[18] ne "0") { print "<B>CHA:</B> $myrow[18] "; }
if ($myrow[19] ne "0") { print "<B>AGI:</B> $myrow[19] "; }
if ($myrow[20] ne "0") { print "<B>INT:</B> $myrow[20] "; }
if ($myrow[21] ne "0") { print "<B>WIS:</B> $myrow[21] "; }

if ($myrow[22] ne "0") { print "<B>HP:</B> $myrow[22] "; }
if ($myrow[23] ne "0") { print "<B>MANA:</B> $myrow[23] "; }

if ($myrow[68] ne "0") { print "<B>ENDUR:</B> $myrow[68] "; }

if ($myrow[24] ne "0") { print "<B>SV FIRE:</B> $myrow[24] "; }
if ($myrow[25] ne "0") { print "<B>SV DISEASE:</B> $myrow[25] "; }
if ($myrow[26] ne "0") { print "<B>SV COLD:</B> $myrow[26] "; }
if ($myrow[27] ne "0") { print "<B>SV MAGIC:</B> $myrow[27] "; }
if ($myrow[28] ne "0") { print "<B>SV POISON:</B> $myrow[28] "; }

print "</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }


print "<TR><TD BGCOLOR=$color><small><B>WT:</B> $myrow[29] <B>SIZE:</B> $myrow[30]</TD></TR>";


if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

if ($myrow[31] ne "0") { 
print "<TR><TD BGCOLOR=$color><small><B>Required Level:</B> $myrow[31]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }
 }

if ($myrow[32] ne "0") { 
print "<TR><TD BGCOLOR=$color><small><B>Recamended Level:</B> $myrow[32]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }
 }

if ($myrow[33] ne "") { 
print "<TR><TD BGCOLOR=$color><small><B>Deity:</B> $myrow[33]</TD></TR>";

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }
 }


if ($myrow[49] eq "1") { 
print "<TR><TD BGCOLOR=$color><small><B>CLASS:</B> ALL</TD></TR>";
 }
else {
print "<TR><TD BGCOLOR=$color><small><B>CLASS:</B> ";
if ($myrow[50] eq "1") { print "BRD "; }
if ($myrow[51] eq "1") { print "BST "; }
if ($myrow[52] eq "1") { print "BER "; }
if ($myrow[53] eq "1") { print "CLR "; }
if ($myrow[54] eq "1") { print "DRU "; }
if ($myrow[55] eq "1") { print "ENC "; }
if ($myrow[56] eq "1") { print "MAG "; }
if ($myrow[57] eq "1") { print "MNK "; }
if ($myrow[58] eq "1") { print "NEC "; }
if ($myrow[59] eq "1") { print "PAL "; }
if ($myrow[60] eq "1") { print "RNG "; }
if ($myrow[61] eq "1") { print "ROG "; }
if ($myrow[62] eq "1") { print "SHD "; }
if ($myrow[63] eq "1") { print "SHM "; }
if ($myrow[64] eq "1") { print "WAR "; }
if ($myrow[65] eq "1") { print "WIZ"; }
print"</TD></TR>";
}

if ($color eq "CCCCDD") { $color = "88BBEE"; }
else { $color = "CCCCDD"; }

if ($myrow[34] eq "1") { 
print "<TR><TD BGCOLOR=$color><small><B>RACE:</B> ALL</TD></TR>";
 }
else {
print "<TR><TD BGCOLOR=$color><small><B>RACE:</B> ";
if ($myrow[35] eq "1") { print "BAR "; }
if ($myrow[36] eq "1") { print "DEF "; }
if ($myrow[37] eq "1") { print "DWF "; }
if ($myrow[38] eq "1") { print "ERU "; }
if ($myrow[39] eq "1") { print "FRG "; }
if ($myrow[40] eq "1") { print "GNM "; }
if ($myrow[67] eq "1") { print "HFL "; }
if ($myrow[41] eq "1") { print "HEF "; }
if ($myrow[42] eq "1") { print "HIE "; }
if ($myrow[43] eq "1") { print "HUM "; }
if ($myrow[44] eq "1") { print "IKS "; }
if ($myrow[45] eq "1") { print "OGR "; }
if ($myrow[46] eq "1") { print "TRL "; }
if ($myrow[47] eq "1") { print "ELF "; }
if ($myrow[48] eq "1") { print "VAH"; }
print"</TD></TR>";
}

print qq~
</TABLE>
~;

if ($myrow[66] eq "0") {
print "Item stats not verafied!";
}

print qq~
</BODY></HTML>

~;

}

########################################

sub parse_form {

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
   @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $input{$name} = $value;
   }
}

1;