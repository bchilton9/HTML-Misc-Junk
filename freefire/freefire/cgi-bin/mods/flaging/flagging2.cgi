#!/usr/bin/perl

$| = 1;
use DBI;
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
		<p>If this problem persits, please contact the webmaster, inform him about date, time you've recieved this error.</p>
		~;
	exit;
}

&parse_form;


logips();
loadcookie();
loaduser();
logvisitors();


########################################

$navbar = "&nbsp;$btn{'014'}&nbsp; $input{'go'}";

print_top();

if ($input{'do'} eq "editflagging") { &editflagform; }
elsif ($input{'do'} eq "editflaggingb") { &saveflag; }
elsif ($input{'do'} eq "viewflag") { &viewflag; }
else { print "No Input Please go to the main page!"; }

print "@data";

print_bottom();

########################################

sub editflagform {

my $dbh = DBI->connect("DBI:mysql:freefire_us_-_flagging:localhost","freefire","dragon42") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from flagging WHERE name='$username'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$id = "$row[0]";

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

 } 

}
$sth->finish; 
$dbh->disconnect; 


if ($id eq "") {

my $dbh = DBI->connect("DBI:mysql:freefire_us_-_freefire:localhost","freefire","dragon42") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp = "INSERT INTO `flagging` ( `name` , `anypoj` , `allpoj` , `xana` , `behe` , `grimror` , `grummus` , `hedge` , `terris` , `askr` , `gernic` , `aerin` , `bertoxx` , `saryrn` , `wembly` , `hohtrial` , `mithanial` , `tallon` , `vallon` , `rallos` , `karana` , `jiva` , `xuzl` , `arlyxir` , `rizlona` , `dresolik` , `solusek` , `xegony` , `fennin` , `coirnav` , `rathe` ) VALUES ('$username', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0')";

$sth=$dbh->prepare($temp);

$sth->execute;
$sth->finish; 
$dbh->disconnect;

}


print qq~
<P>
<P>
<FORM>
  <CENTER>
    <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 1</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Any PoJ Trial</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="anypoj" VALUE="on"
~;
if ($myrow[1] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">All PoJ Trials</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="allpoj" VALUE="on"
~;
if ($myrow[2] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoI Xanamech</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="xana" VALUE="on"
~;
if ($myrow[3] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoI Behemoth</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="behe" VALUE="on"
~;
if ($myrow[4] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoD Grimror Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="grimror" VALUE="on"
~;
if ($myrow[5] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoD Grummus</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="grummus" VALUE="on"
~;
if ($myrow[6] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoN Hedge Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="hedge" VALUE="on"
~;
if ($myrow[7] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoNb Terris Thule</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="terris" VALUE="on"
~;
if ($myrow[8] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 2</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoS Askr Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="askr" VALUE="on"
~;
if ($myrow[9] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">PoV Grenic Quest</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="gernic" VALUE="on"
~;
if ($myrow[10] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoV Aerin'Dar</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="aerin" VALUE="on"
~;
if ($myrow[11] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed CoD Bertoxxulous</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="bertoxx" VALUE="on"
~;
if ($myrow[12] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoTorment Saryrn</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="saryrn" VALUE="on"
~;
if ($myrow[13] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">PoS Wembly Quest</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="wembly" VALUE="on"
~;
if ($myrow[14] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 3</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">HoH Trials</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="hohtrial" VALUE="on"
~;
if ($myrow[15] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed HoHb Mithanial Marr</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="mithanial" VALUE="on"
~;
if ($myrow[16] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoTactics Tallon Zek</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="tallon" VALUE="on"
~;
if ($myrow[17] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoTactics Vallon Zek</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="vallon" VALUE="on"
~;
if ($myrow[18] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoTactics Rallos Zek Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="rallos" VALUE="on"
~;
if ($myrow[19] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">BoT Rescue Karana Quest</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="karana" VALUE="on"
~;
if ($myrow[20] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed SolRoTower Jiva</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="jiva" VALUE="on"
~;
if ($myrow[21] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed SolRoTower Xuzl</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="xuzl" VALUE="on"
~;
if ($myrow[22] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed SolRoTower Arlyxir</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="arlyxir" VALUE="on"
~;
if ($myrow[23] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed SolRoTower Rizlona</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="rizlona" VALUE="on"
~;
if ($myrow[24] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed SolRoTower Protector of Dresolik</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="dresolik" VALUE="on"
~;
if ($myrow[25] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed SolRoTower Solusek Ro</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="solusek" VALUE="on"
~;
if ($myrow[26] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 4</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoAir Xegony</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="xegony" VALUE="on"
~;
if ($myrow[27] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoFire Fennin Ro</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="fennin" VALUE="on"
~;
if ($myrow[28] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoWater Coirnav</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="coirnav" VALUE="on"
~;
if ($myrow[29] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoEarthb The Rathe</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="rathe" VALUE="on"
~;
if ($myrow[30] eq "1") { print " CHECKED"; }
print qq~
></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="do" VALUE="editflaggingb">
	  <INPUT TYPE=submit VALUE="Save Flag's"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;

}

########################################

sub saveflag {

my $dbh = DBI->connect("DBI:mysql:freefire_us_-_flagging:localhost","freefire","dragon42") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp = "UPDATE `flagging` SET";

if ($input{'anypoj'} eq "on") { $temp = "$temp `anypoj` = '1',"; }
else { $temp = "$temp `anypoj` = '0',"; }

if ($input{'allpoj'} eq "on") { $temp = "$temp `allpoj` = '1',"; }
else { $temp = "$temp `allpoj` = '0',"; }

if ($input{'xana'} eq "on") { $temp = "$temp `xana` = '1',"; }
else { $temp = "$temp `xana` = '0',"; }

if ($input{'behe'} eq "on") { $temp = "$temp `behe` = '1',"; }
else { $temp = "$temp `behe` = '0',"; }

if ($input{'grimror'} eq "on") { $temp = "$temp `grimror` = '1',"; }
else { $temp = "$temp `grimror` = '0',"; }

if ($input{'grummus'} eq "on") { $temp = "$temp `grummus` = '1',"; }
else { $temp = "$temp `grummus` = '0',"; }

if ($input{'hedge'} eq "on") { $temp = "$temp `hedge` = '1',"; }
else { $temp = "$temp `hedge` = '0',"; }

if ($input{'terris'} eq "on") { $temp = "$temp `terris` = '1',"; }
else { $temp = "$temp `terris` = '0',"; }

if ($input{'askr'} eq "on") { $temp = "$temp `askr` = '1',"; }
else { $temp = "$temp `askr` = '0',"; }

if ($input{'gernic'} eq "on") { $temp = "$temp `gernic` = '1',"; }
else { $temp = "$temp `gernic` = '0',"; }

if ($input{'aerin'} eq "on") { $temp = "$temp `aerin` = '1',"; }
else { $temp = "$temp `aerin` = '0',"; }

if ($input{'bertoxx'} eq "on") { $temp = "$temp `bertoxx` = '1',"; }
else { $temp = "$temp `bertoxx` = '0',"; }

if ($input{'saryrn'} eq "on") { $temp = "$temp `saryrn` = '1',"; }
else { $temp = "$temp `saryrn` = '0',"; }

if ($input{'wembly'} eq "on") { $temp = "$temp `wembly` = '1',"; }
else { $temp = "$temp `wembly` = '0',"; }

if ($input{'hohtrial'} eq "on") { $temp = "$temp `hohtrial` = '1',"; }
else { $temp = "$temp `hohtrial` = '0',"; }

if ($input{'mithanial'} eq "on") { $temp = "$temp `mithanial` = '1',"; }
else { $temp = "$temp `mithanial` = '0',"; }

if ($input{'tallon'} eq "on") { $temp = "$temp `tallon` = '1',"; }
else { $temp = "$temp `tallon` = '0',"; }

if ($input{'vallon'} eq "on") { $temp = "$temp `vallon` = '1',"; }
else { $temp = "$temp `vallon` = '0',"; }

if ($input{'rallos'} eq "on") { $temp = "$temp `rallos` = '1',"; }
else { $temp = "$temp `rallos` = '0',"; }

if ($input{'karana'} eq "on") { $temp = "$temp `karana` = '1',"; }
else { $temp = "$temp `karana` = '0',"; }

if ($input{'jiva'} eq "on") { $temp = "$temp `jiva` = '1',"; }
else { $temp = "$temp `jiva` = '0',"; }

if ($input{'xuzl'} eq "on") { $temp = "$temp `xuzl` = '1',"; }
else { $temp = "$temp `xuzl` = '0',"; }

if ($input{'arlyxir'} eq "on") { $temp = "$temp `arlyxir` = '1',"; }
else { $temp = "$temp `arlyxir` = '0',"; }

if ($input{'rizlona'} eq "on") { $temp = "$temp `rizlona` = '1',"; }
else { $temp = "$temp `rizlona` = '0',"; }

if ($input{'dresolik'} eq "on") { $temp = "$temp `dresolik` = '1',"; }
else { $temp = "$temp `dresolik` = '0',"; }

if ($input{'solusek'} eq "on") { $temp = "$temp `solusek` = '1',"; }
else { $temp = "$temp `solusek` = '0',"; }

if ($input{'xegony'} eq "on") { $temp = "$temp `xegony` = '1',"; }
else { $temp = "$temp `xegony` = '0',"; }

if ($input{'fennin'} eq "on") { $temp = "$temp `fennin` = '1',"; }
else { $temp = "$temp `fennin` = '0',"; }

if ($input{'coirnav'} eq "on") { $temp = "$temp `coirnav` = '1',"; }
else { $temp = "$temp `coirnav` = '0',"; }

if ($input{'rathe'} eq "on") { $temp = "$temp `rathe` = '1'"; }
else { $temp = "$temp `rathe` = '0'"; }

$temp = "$temp WHERE `name` = '$username' LIMIT 1"; 

$sth=$dbh->prepare($temp);

$sth->execute;
$sth->finish; 
$dbh->disconnect;

print "<P>Flagging Progress saved.";

}

########################################

sub viewflag {

my $dbh = DBI->connect("DBI:mysql:freefire_us_-_flagging:localhost","freefire","dragon42") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from flagging WHERE name='$input{'show'}'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$id = "$row[0]";

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

 } 

}
$sth->finish; 
$dbh->disconnect; 


print qq~
<FORM>
  <CENTER>
    <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 1</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Any PoJ Trial</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="anypoj" VALUE="on"
~;
if ($myrow[1] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">All PoJ Trials</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="allpoj" VALUE="on"
~;
if ($myrow[2] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoI Xanamech</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="xana" VALUE="on"
~;
if ($myrow[3] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoI Behemoth</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="behe" VALUE="on"
~;
if ($myrow[4] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoD Grimror Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="grimror" VALUE="on"
~;
if ($myrow[5] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoD Grummus</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="grummus" VALUE="on"
~;
if ($myrow[6] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoN Hedge Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="hedge" VALUE="on"
~;
if ($myrow[7] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoNb Terris Thule</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="terris" VALUE="on"
~;
if ($myrow[8] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 2</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoS Askr Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="askr" VALUE="on"
~;
if ($myrow[9] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">PoV Grenic Quest</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="gernic" VALUE="on"
~;
if ($myrow[10] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoV Aerin'Dar</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="aerin" VALUE="on"
~;
if ($myrow[11] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed CoD Bertoxxulous</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="bertoxx" VALUE="on"
~;
if ($myrow[12] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoTorment Saryrn</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="saryrn" VALUE="on"
~;
if ($myrow[13] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">PoS Wembly Quest</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="wembly" VALUE="on"
~;
if ($myrow[14] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 3</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">HoH Trials</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="hohtrial" VALUE="on"
~;
if ($myrow[15] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed HoHb Mithanial Marr</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="mithanial" VALUE="on"
~;
if ($myrow[16] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoTactics Tallon Zek</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="tallon" VALUE="on"
~;
if ($myrow[17] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoTactics Vallon Zek</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="vallon" VALUE="on"
~;
if ($myrow[18] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">PoTactics Rallos Zek Quest</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="rallos" VALUE="on"
~;
if ($myrow[19] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">BoT Rescue Karana Quest</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="karana" VALUE="on"
~;
if ($myrow[20] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed SolRoTower Jiva</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="jiva" VALUE="on"
~;
if ($myrow[21] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed SolRoTower Xuzl</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="xuzl" VALUE="on"
~;
if ($myrow[22] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed SolRoTower Arlyxir</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="arlyxir" VALUE="on"
~;
if ($myrow[23] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed SolRoTower Rizlona</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="rizlona" VALUE="on"
~;
if ($myrow[24] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed SolRoTower Protector of Dresolik</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="dresolik" VALUE="on"
~;
if ($myrow[25] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed SolRoTower Solusek Ro</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="solusek" VALUE="on"
~;
if ($myrow[26] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD COLSPAN=2 class="boardtitle"><P ALIGN=Center>
	  <B>Tier 4</B></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoAir Xegony</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="xegony" VALUE="on"
~;
if ($myrow[27] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoFire Fennin Ro</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="fennin" VALUE="on"
~;
if ($myrow[28] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow2">Killed PoWater Coirnav</TD>
	<TD class="forumwindow2">
	  <INPUT TYPE="checkbox" NAME="coirnav" VALUE="on"
~;
if ($myrow[29] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
      <TR>
	<TD class="forumwindow3">Killed PoEarthb The Rathe</TD>
	<TD class="forumwindow3">
	  <INPUT TYPE="checkbox" NAME="rathe" VALUE="on"
~;
if ($myrow[30] eq "1") { print " CHECKED"; }
print qq~
 disabled></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
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