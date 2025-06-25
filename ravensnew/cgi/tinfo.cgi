#!/usr/bin/perl

print "Content-type: text/html\n\n";

print <<"HTML";
<HTML>
<HEAD>
  <!-- Created with AOLpress/2.0 -->
  <TITLE>Naked Man Tournament</TITLE>
</HEAD>
<BODY BGCOLOR="#ffffff">
<P ALIGN=Center>
<IMG SRC="turn.gif">
<Center>
<A HREF="#rules">Rules</A><BR>
<A HREF="#sup">Members signed up</A><BR>
<A HREF="#prize">Prizes</A>


<P><BR><P><BR><P><BR><P><BR>
<A NAME="rules"><B>Ravens Of Dispair: Naked Man Tournament: Rules</B></A>
<CENTER>
  <TABLE BORDER CELLSPACING="1" ALIGN="Center" WIDTH="500">
    <TR>
      <TD>1:</TD>
      <TD>Player must be humen, lvl 1, with only the starting equipment (tunics,
	swords, spells, ect..).</TD>
    </TR>
    <TR>
      <TD>2:</TD>
      <TD>No buffs!! If you start with a buff spell you may use it. Buffs from
	outher players are not alowed. Merchent bot spells eaven lvl one spells are
	not allowed.</TD>
    </TR>
    <TR>
      <TD>3:</TD>
      <TD>Fights will be to the death in the freeport arena. Help from non fighting
	players will disqualafi the fighter that is helped and the helping party
	if in the turnament.</TD>
    </TR>
    <TR>
      <TD>4:</TD>
      <TD>One fight at a time. Fights will be organized, started, stoped, and winner
	will be deturmend by Keny or anouther ranking offaser.</TD>
    </TR>
    <TR>
      <TD>5:</TD>
      <TD>Prizes will be givein for 1st 2nd and 3rd place. 1st place winer will
	be giveing 1st choice in prizes, then 2nd place winer and so on.</TD>
    </TR>
    <TR>
      <TD>6:</TD>
      <TD>Names must resembel your main charators name in some way. ie kenytwo,
	battlebojax, fryfighter. This will make shure one player dosent win and anouther
	player gets the prize.</TD>
    </TR>
    <TR>
      <TD>7:</TD>
      <TD>Fighting chars must be in freeport. Your main char dosent have to be
	in freeport. Wolfkeeper will deliver the prizes to your main char anywhere
	in the world.</TD>
    </TR>
    <TR>
      <TD>8:</TD>
      <TD>Fighting chars can me any class and/or denaty. Theay must me humen and
	theay must be naked. Starting stats (ie str, sta, agi, ext...) are up to
	the fighter and how theay want to spend there points</TD>
    </TR>
    <TR>
      <TD>9:</TD>
      <TD>Fighters must be registered members of Ravens of Dispair both in game
	and on the website. Your alts for the turnament dont have to be signed up
	just your main charator.</TD>
    </TR>
    <TR>
      <TD>10:</TD>
      <TD>Fighters must pre sign up at the website if theay wish to atend this
	event. There is a button on the main members page to do this.</TD>
    </TR>
    <TR>
      <TD>11:</TD>
      <TD>Time and date of the turnament will be deturmend at a later time. There
	will be a voteing on what day to hold the tournament.</TD>
    </TR>
    <TR>
      <TD>12:</TD>
      <TD>Rules may be changed at any time with out notice!</TD>
    </TR>
  </TABLE>
</CENTER>
<P><BR>
<P><BR>
<P><BR>
<P><BR>
<CENTER>
<A NAME="sup"><B>Members Signed up for the turnament</B></A>
  <TABLE BORDER CELLPADDING="1" ALIGN="Center" WIDTH=200>
HTML
open (DATA, "turn.txt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
print "<TR><TD><CENTER>$line</TD></TR>";

}


print <<"HTML";
  </TABLE>
</CENTER>
<P><BR>
<P><BR>
<P><BR>
<P><BR>
<CENTER>
<A NAME="prize"><B>Prizes</B></A><BR>
No info on prizes yet
</BODY></HTML>

HTML
