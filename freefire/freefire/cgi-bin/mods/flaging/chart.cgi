#!/usr/bin/perl


use DBI;

&parse_form;

#ALIGN=LEFT VALIGN=TOP

print "Content-type: text/html\n\n";

$color1 = "CCCCDD";
$color2 = "DDCCCC";

print qq~
<HTML>
<HEAD>

<style type="text/css">
.verticaltext{
font: bold 13px Arial;
width: 25px;
writing-mode: tb-rl;
}

.text{
font: bold 13px Arial;
}

</style>

<TITLE>Freefire - Flagging Chart</TITLE>
</HEAD>

<BODY BGCOLOR=gray>

<TABLE BORDER="1" BORDERCOLOR=black CELLSPACING="0" CELLPADDING="2">
  <TR ALIGN=center VALIGN=center>
    <TD></TD>
    <TD BGCOLOR=$color2 class="verticaltext">Any PoJ Trial</TD>
    <TD BGCOLOR=$color1 class="verticaltext">All PoJ Trials</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed PoI Xanamech</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed PoI Behemoth</TD>
    <TD BGCOLOR=$color2 class="verticaltext">PoD Grimror Quest</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed PoD Grummus</TD>
    <TD BGCOLOR=$color2 class="verticaltext">PoN Hedge Quest</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed PoNb Terris Thule</TD>

    <TD BGCOLOR=$color2 class="verticaltext">PoS Askr Quest</TD>
    <TD BGCOLOR=$color1 class="verticaltext">PoV Grenic Quest</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed PoV Aerin'Dar</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed CoD Bertoxxulous</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed PoTorment Saryrn</TD>
    <TD BGCOLOR=$color1 class="verticaltext">PoS Wembly Quest</TD>

    <TD BGCOLOR=$color2 class="verticaltext">HoH Trials</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed HoHb Mithanial Marr</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed PoTactics Tallon Zek</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed PoTactics Vallon Zek</TD>
    <TD BGCOLOR=$color2 class="verticaltext">PoTactics Rallos Zek Quest</TD>
    <TD BGCOLOR=$color1 class="verticaltext">BoT Rescue Karana Quest</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed SolRoTower Jiva</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed SolRoTower Xuzl</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed SolRoTower Arlyxir</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed SolRoTower Rizlona</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed SolRoTower Protector of Dresolik</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed SolRoTower Solusek Ro</TD>

    <TD BGCOLOR=$color2 class="verticaltext">Killed PoAir Xegony</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed PoFire Fennin Ro</TD>
    <TD BGCOLOR=$color2 class="verticaltext">Killed PoWater Coirnav</TD>
    <TD BGCOLOR=$color1 class="verticaltext">Killed PoEarthb The Rathe</TD>

  </TR>

~;


my $dbh = DBI->connect("DBI:mysql:freefire_us_-_flagging:localhost","freefire","dragon42") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

if ($input{'show'} eq "") {

$temp ="select * from flagging ORDER BY name";

}
else {

$temp ="select * from flagging WHERE name='$input{'show'}'";

}

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] ne "admin") { 
if ($row[0] ne "admin2") { 
print qq~
  <TR>
    <TD BGCOLOR=$color1 class=text>$row[0]</TD>
~;

if ($row[1] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[2] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[3] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[4] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[5] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[6] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[7] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[8] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[9] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[10] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[11] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[12] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[13] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[14] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[15] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[16] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[17] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[18] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[19] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[20] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[21] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[22] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[23] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[24] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[25] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[26] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[27] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[28] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[29] eq "1") { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color2><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }
if ($row[30] eq "1") { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/x.gif BORDER=0></TD>"; }
else { print "<TD BGCOLOR=$color1><IMG SRC=http://www.freefire.us/images/flagging/o.gif BORDER=0></TD>"; }


print qq~
  </TR>
~;
}
}
 } 

}
$sth->finish; 
$dbh->disconnect; 



print qq~

</TABLE>
</BODY>
</HTML>

~;



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