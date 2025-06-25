#!/usr/bin/perl

use DBI;


BEGIN {
	##--------------------------------------------------------------
	## If you are not using standard folder locations, the following
	## line may need to be changed to match your installation
	##--------------------------------------------------------------

	require "../../config.pl";
	require "$sourcedir/subs.pl";

	##--------------------------------------------------------------
	## Nothing below this point should require modification
	##--------------------------------------------------------------
}


&parse_form;


logips();
loadcookie();
loaduser();
logvisitors();



# ----------- print everything to the browser ---

$navbar = "&nbsp;$btn{'014'}&nbsp; $cm_title";

print_top();


if ($input{'do'} eq "delete") { &delete; }
elsif ($input{'do'} eq "edit") { &edit; }
elsif ($input{'do'} eq "search") { &search; }
elsif ($input{'do'} eq "add") { &add; }
elsif ($input{'do'} eq "new") { &new; }
elsif ($input{'do'} eq "save") { &save; }
else { &PrintDefault; }

print_bottom();


# _____________________________________________________________________________
sub PrintDefault {

$slot[1] = "Primary";
$slot[2] = "Secondary";
$slot[3] = "Range";
$slot[4] = "Ammo";
$slot[5] = "Right_Ear";
$slot[6] = "Left_Ear";
$slot[7] = "Neck";
$slot[8] = "Face";
$slot[9] = "Head";
$slot[10] = "Shoulders";
$slot[11] = "Right_Finger";
$slot[12] = "Left_Finger";
$slot[13] = "Right_Wrist";
$slot[14] = "Left_Wrist";
$slot[15] = "Arms";
$slot[16] = "Chest";
$slot[17] = "Back";
$slot[18] = "Feet";
$slot[19] = "Legs";
$slot[20] = "Waist";
$slot[21] = "Hands";
$slot[22] = "Charm";

print qq~

<TABLE BORDER=0 CELLPADDING="2">
  <TR>
    <TD class="formstexttitle">Edit Inventory</TD>
  </TR>
  <TR>
    <TD>

<TABLE cellpadding="2" cellspacing="2" width="350" border="0">

~;

$i = 0;

open (DATA, "$memberdir/$username.inv");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp($line);

$i = $i + 1;

if ($line ne "Empty") {

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from bank WHERE num='$line'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

while((@row=$sth->fetchrow_array)!=NULL) { 
$row_hit=1;
$mynum = "$row[0]";
$myname = "$row[1]";
} 

}
$sth->finish; 
$dbh->disconnect; 

print qq~
<TR>
<TD class="forumwindow3"><P ALIGN=Right>$slot[$i]:</TD>
<TD WIDTH="60%" class="forumwindow1">

<A HREF=http://www.eqguilded.com/freefire/cgi-bin/mods/bank/bank.cgi?do=view&show=$mynum 
onclick="NewWindow(this.href,'name','420','220','yes');return false;">
$myname
</A>

</TD>
<TD class="forumwindow1" WIDTH="200"><CENTER>
<A HREF=inventory.cgi?do=edit&slot=$slot[$i]>
<img src="http://www.eqguilded.com/freefire/images/forum/modify.gif" border="0"></A>
<A HREF=inventory.cgi?do=delete&slot=$slot[$i]>
<img src="http://www.eqguilded.com/freefire/images/forum/remove.gif" border="0"></A>
</TD>
</TR>
~;
}

else {

print qq~
<TR><TD class="forumwindow3"><P ALIGN=Right>$slot[$i]:</TD>
<TD WIDTH="60%" class="forumwindow1">Empty</TD>

<TD class="forumwindow1" WIDTH="200"><CENTER>
<A HREF=inventory.cgi?do=edit&slot=$slot[$i]>
<img src="http://www.eqguilded.com/freefire/images/forum/modify.gif" border="0"></A>
<A HREF=inventory.cgi?do=delete&slot=$slot[$i]>
<img src="http://www.eqguilded.com/freefire/images/forum/remove.gif" border="0"></A>
</TD></TR>
~;

}

}

print qq~
</TABLE>
</TD>
  </TR>
</TABLE>

~;

}

# _____________________________________________________________________________


sub delete {

open (DATA, "$memberdir/$username.inv");
chomp(@slot = <DATA>);
close DATA;


if($input{'slot'} eq "Primary") { $slot[0] = "Empty"; }
if($input{'slot'} eq "Secondary") { $slot[1] = "Empty"; }
if($input{'slot'} eq "Range") { $slot[2] = "Empty"; }
if($input{'slot'} eq "Ammo") { $slot[3] = "Empty"; }
if($input{'slot'} eq "Right_Ear") { $slot[4] = "Empty"; }
if($input{'slot'} eq "Left_Ear") { $slot[5] = "Empty"; }
if($input{'slot'} eq "Neck") { $slot[6] = "Empty"; }
if($input{'slot'} eq "Face") { $slot[7] = "Empty"; }
if($input{'slot'} eq "Head") { $slot[8] = "Empty"; }
if($input{'slot'} eq "Shoulders") { $slot[9] = "Empty"; }
if($input{'slot'} eq "Right_Finger") { $slot[10] = "Empty"; }
if($input{'slot'} eq "Left_Finger") { $slot[11] = "Empty"; }
if($input{'slot'} eq "Right_Wrist") { $slot[12] = "Empty"; }
if($input{'slot'} eq "Left_Wrist") { $slot[13] = "Empty"; }
if($input{'slot'} eq "Arms") { $slot[14] = "Empty"; }
if($input{'slot'} eq "Chest") { $slot[15] = "Empty"; }
if($input{'slot'} eq "Back") { $slot[16] = "Empty"; }
if($input{'slot'} eq "Feet") { $slot[17] = "Empty"; }
if($input{'slot'} eq "Legs") { $slot[18] = "Empty"; }
if($input{'slot'} eq "Waist") { $slot[19] = "Empty"; }
if($input{'slot'} eq "Hands") { $slot[20] = "Empty"; }
if($input{'slot'} eq "Charm") { $slot[21] = "Empty"; }


	open(FILE, ">$memberdir/$username.inv");
	file_lock(FILE);
	print FILE "$slot[0]\n";
	print FILE "$slot[1]\n";
	print FILE "$slot[2]\n";
	print FILE "$slot[3]\n";
	print FILE "$slot[4]\n";
	print FILE "$slot[5]\n";
	print FILE "$slot[6]\n";
	print FILE "$slot[7]\n";
	print FILE "$slot[8]\n";
	print FILE "$slot[9]\n";
	print FILE "$slot[10]\n";
	print FILE "$slot[11]\n";
	print FILE "$slot[12]\n";
	print FILE "$slot[13]\n";
	print FILE "$slot[14]\n";
	print FILE "$slot[15]\n";
	print FILE "$slot[16]\n";
	print FILE "$slot[17]\n";
	print FILE "$slot[18]\n";
	print FILE "$slot[19]\n";
	print FILE "$slot[20]\n";
	print FILE "$slot[21]\n";
	unfile_lock(FILE);
	close(FILE);


&PrintDefault;

}

# _____________________________________________________________________________


sub edit {

print qq~

<FORM>
  <TABLE BORDER="0" CELLPADDING="2">
    <TR>
      <TD><P ALIGN=right>
	<B>Slot:</B></TD>
      <TD>$input{'slot'}
	<INPUT TYPE="hidden" NAME="slot" VALUE="$input{'slot'}"></TD>
    </TR>
    <TR>
      <TD><B>Name:</B></TD>
      <TD>
	<INPUT TYPE="text" NAME="search"></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<INPUT TYPE="hidden" NAME="do" VALUE="search">
	<INPUT TYPE=submit VALUE="Search"></TD>
    </TR>
  </TABLE>
</FORM>

~;

}

# _____________________________________________________________________________

sub search {

if ($input{'slot'} eq "Left_Ear") { $lookslot = "Ear"; }
elsif ($input{'slot'} eq "Right_Ear") { $lookslot = "Ear"; }
elsif ($input{'slot'} eq "Left_Finger") { $lookslot = "Finger"; }
elsif ($input{'slot'} eq "Right_Finger") { $lookslot = "Finger"; }
elsif ($input{'slot'} eq "Right_Wrist") { $lookslot = "Wrist"; }
elsif ($input{'slot'} eq "Left_Wrist") { $lookslot = "Wrist"; }
else { $lookslot = "$input{'slot'}"; }



if ($settings[20] eq "Magican") { $class = "mag"; }
elsif ($settings[20] eq "Bard") { $class = "brd"; }
elsif ($settings[20] eq "Beastlord") { $class = "bst"; }
elsif ($settings[20] eq "Cleric") { $class = "clr"; }
elsif ($settings[20] eq "Druid") { $class = "dru"; }
elsif ($settings[20] eq "Enchanter") { $class = "enc"; }
elsif ($settings[20] eq "Monk") { $class = "mnk"; }
elsif ($settings[20] eq "Necromancer") { $class = "nec"; }
elsif ($settings[20] eq "Paladin") { $class = "pal"; }
elsif ($settings[20] eq "Ranger") { $class = "rng"; }
elsif ($settings[20] eq "Rogue") { $class = "rog"; }
elsif ($settings[20] eq "Shadow Knight") { $class = "shd"; }
elsif ($settings[20] eq "Shaman") { $class = "shm"; }
elsif ($settings[20] eq "Warrior") { $class = "war"; }
elsif ($settings[20] eq "Wizard") { $class = "wiz"; }
elsif ($settings[20] eq "Berzerker") { $class = "ber"; }

if ($settings[21] eq "Gnome") { $race = "gnm"; }
elsif ($settings[21] eq "Barbarian") { $race = "bar"; }
elsif ($settings[21] eq "Dark Elf") { $race = "def"; }
elsif ($settings[21] eq "Dwarf") { $race = "swf"; }
elsif ($settings[21] eq "Erudite") { $race = "eru"; }
elsif ($settings[21] eq "Froglok") { $race = "frg"; }
elsif ($settings[21] eq "Half Elf") { $race = "hef"; }
elsif ($settings[21] eq "Halfling") { $race = "hfl"; }
elsif ($settings[21] eq "High Elf") { $race = "hie"; }
elsif ($settings[21] eq "Human") { $race = "hum"; }
elsif ($settings[21] eq "Iksar") { $race = "iks"; }
elsif ($settings[21] eq "Ogre") { $race = "ogr"; }
elsif ($settings[21] eq "Troll") { $race = "trl"; }
elsif ($settings[21] eq "Vah Shir") { $race = "vah"; }
elsif ($settings[21] eq "Wood Elf") { $race = "elf"; }


$search = "$input{'search'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp ="SELECT  * FROM bank 
WHERE name LIKE '%$search%' AND 
slot = '$lookslot' AND 
(classall = '1' or $class = '1') AND 
(raceall = '1' or $race = '1')
order by name";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$tag = "$tag <OPTION VALUE=$row[0]>$row[1]\n";
	  
 } 

}
$sth->finish; 
$dbh->disconnect;


print qq~
<FORM onSubmit="submitonce(this)">
    <TABLE BORDER="0" CELLPADDING="2">

      <TR>
	<TD>Slot:</TD>
	<TD>$input{'slot'}
	<INPUT TYPE="hidden" NAME="slot" VALUE="$input{'slot'}"></TD>
      </TR>

      <TR>
	<TD>Items Found:</TD>
	<TD>
<SELECT NAME="item">
$tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="do" VALUE="add">
	  <INPUT TYPE=submit VALUE="Add Item"></TD>
      </TR>

<TR><TD COLSPAN=2><P ALIGN=Center>
<A HREF="inventory.cgi?do=new">Item not listed? Add it here!</A>
</TD></TR>
    </TABLE>
</FORM>


~;


}

# _____________________________________________________________________________

sub add {

if($input{'item'} eq "") {

print "No item selected!";

&PrintDefault;

}
else {

open (DATA, "$memberdir/$username.inv");
chomp(@slot = <DATA>);
close DATA;


if($input{'slot'} eq "Primary") { $slot[0] = "$input{'item'}"; }
if($input{'slot'} eq "Secondary") { $slot[1] = "$input{'item'}"; }
if($input{'slot'} eq "Range") { $slot[2] = "$input{'item'}"; }
if($input{'slot'} eq "Ammo") { $slot[3] = "$input{'item'}"; }
if($input{'slot'} eq "Right_Ear") { $slot[4] = "$input{'item'}"; }
if($input{'slot'} eq "Left_Ear") { $slot[5] = "$input{'item'}"; }
if($input{'slot'} eq "Neck") { $slot[6] = "$input{'item'}"; }
if($input{'slot'} eq "Face") { $slot[7] = "$input{'item'}"; }
if($input{'slot'} eq "Head") { $slot[8] = "$input{'item'}"; }
if($input{'slot'} eq "Shoulders") { $slot[9] = "$input{'item'}"; }
if($input{'slot'} eq "Right_Finger") { $slot[10] = "$input{'item'}"; }
if($input{'slot'} eq "Left_Finger") { $slot[11] = "$input{'item'}"; }
if($input{'slot'} eq "Right_Wrist") { $slot[12] = "$input{'item'}"; }
if($input{'slot'} eq "Left_Wrist") { $slot[13] = "$input{'item'}"; }
if($input{'slot'} eq "Arms") { $slot[14] = "$input{'item'}"; }
if($input{'slot'} eq "Chest") { $slot[15] = "$input{'item'}"; }
if($input{'slot'} eq "Back") { $slot[16] = "$input{'item'}"; }
if($input{'slot'} eq "Feet") { $slot[17] = "$input{'item'}"; }
if($input{'slot'} eq "Legs") { $slot[18] = "$input{'item'}"; }
if($input{'slot'} eq "Waist") { $slot[19] = "$input{'item'}"; }
if($input{'slot'} eq "Hands") { $slot[20] = "$input{'item'}"; }
if($input{'slot'} eq "Charm") { $slot[21] = "$input{'item'}"; }


	open(FILE, ">$memberdir/$username.inv");
	file_lock(FILE);
	print FILE "$slot[0]\n";
	print FILE "$slot[1]\n";
	print FILE "$slot[2]\n";
	print FILE "$slot[3]\n";
	print FILE "$slot[4]\n";
	print FILE "$slot[5]\n";
	print FILE "$slot[6]\n";
	print FILE "$slot[7]\n";
	print FILE "$slot[8]\n";
	print FILE "$slot[9]\n";
	print FILE "$slot[10]\n";
	print FILE "$slot[11]\n";
	print FILE "$slot[12]\n";
	print FILE "$slot[13]\n";
	print FILE "$slot[14]\n";
	print FILE "$slot[15]\n";
	print FILE "$slot[16]\n";
	print FILE "$slot[17]\n";
	print FILE "$slot[18]\n";
	print FILE "$slot[19]\n";
	print FILE "$slot[20]\n";
	print FILE "$slot[21]\n";
	unfile_lock(FILE);
	close(FILE);


&PrintDefault;

}
}

# _____________________________________________________________________________

sub new {


print qq~
<form onSubmit="submitonce(this)">
<CENTER>
This will only add the item into the database you will still have to add the item into your inventory!<BR>
<B>IF THE ITEM DOSE NOT HAVE THE STAT LEAVE IT BLANK!</B><BR>
<B>ONCE YOU SUBMIT THIS FORM YOU CAN NOT EDIT THE ITEM LATER! MAKE SURE EVERYTHING IS CORRECT!</B><BR>
<P>
    <TABLE BORDER CELLSPACING="1" CELLPADDING="2" BORDERCOLOR=blue>
      <TR>
	<TD><P ALIGN=Right>
	  Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="name"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
	    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	      <TR>
		<TD>Lore:</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="lore" VALUE="1"></TD>
		<TD>Magic:</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="magic" VALUE="1"></TD>
		<TD>No Drop:</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="nodrop" VALUE="1"></TD>
	      </TR>
	    </TABLE>
	  </CENTER>
	</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Type:</TD>
	<TD>
	  <SELECT NAME="type"> 
	  <OPTION>Armor 
	  <OPTION>Spell 
	  <OPTION>1hs 
	  <OPTION>2hs 
	  <OPTION>1hb 
	  <OPTION>2hb 
	  <OPTION>Pierceing 
	  <OPTION>2hp 
	  <OPTION>H2H 
	  <OPTION>Archery 
	  <OPTION>Throwing 
	  <OPTION>Other </SELECT></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Slot:</TD>
	<TD>
	  <SELECT NAME="slot"> 
	  <OPTION value="Arms">Arms 
	  <OPTION value="Back">Back 
	  <OPTION value="Charm">Charm 
	  <OPTION value="Chest">Chest 
	  <OPTION value="Ear">Ear 
	  <OPTION value="Face">Face 
	  <OPTION value="Finger">Finger 
	  <OPTION value="Feet">Feet 
	  <OPTION value="Hands">Hands 
	  <OPTION value="Head">Head 
	  <OPTION value="Legs">Legs 
	  <OPTION value="Neck">Neck 
	  <OPTION value="Shoulders">Shoulders 
	  <OPTION value="Waist">Waist 
	  <OPTION value="Wrist">Wrist 
	  <OPTION value="Primary">Primary 
	  <OPTION value="Secondary">Secondary 
	  <OPTION value="Range">Range 
	  <OPTION value="Ammo">Ammo 
	  <OPTION value="Inventory">Inventory </SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
	    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	      <TR>
		<TD>DMG:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="dmg" SIZE="3"></TD>
		<TD>DLY:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="dly" SIZE="3"></TD>
		<TD>DMG Bonus:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="dmgbonus" SIZE="3"></TD>
	      </TR>
	    </TABLE>
	  </CENTER>
	</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  AC:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="ac" SIZE="3"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Effect:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="Effect"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Bane:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="bane"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Skill Mod:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="skillmod"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Focus:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="focus"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
	    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	      <TR>
		<TD>DEX:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="dex" SIZE="3"></TD>
		<TD>STA:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="sta" SIZE="3"></TD>
		<TD>STR:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="str" SIZE="3"></TD>
		<TD>CHA:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="cha" SIZE="3"></TD>
	      </TR>
	      <TR>
		<TD>AGI:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="agi" SIZE="3"></TD>
		<TD>INT:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="int" SIZE="3"></TD>
		<TD>WIS:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="wis" SIZE="3"></TD>
		<TD></TD>
		<TD></TD>
	      </TR>
	    </TABLE>
	  </CENTER>
	</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
	    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	      <TR>
		<TD>HP:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="hp" SIZE="3"></TD>
		<TD>MANA:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="mana" SIZE="3"></TD>
		<TD>ENDUR:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="endur" SIZE="3"></TD>
	      </TR>
	    </TABLE>
	  </CENTER>
	</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
	    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	      <TR>
		<TD>SV FIRE:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="svfire" SIZE="3"></TD>
		<TD>SV DISEASE:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="svdisease" SIZE="3"></TD>
		<TD>SV COLD:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="svcold" SIZE="3"></TD>
	      </TR>
	      <TR>
		<TD>SV MAGIC:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="svmagic" SIZE="3"></TD>
		<TD>SV POISON:</TD>
		<TD>
		  <INPUT TYPE="text" NAME="svpoison" SIZE="3"></TD>
		<TD></TD>
		<TD></TD>
	      </TR>
	    </TABLE>
	  </CENTER>
	</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Weight:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="weight" SIZE="3"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Size:</TD>
	<TD>
	  <SELECT NAME="size"> 
	  <OPTION SELECTED>Small 
	  <OPTION>Medium 
	  <OPTION>Large 
	  <OPTION>Giant</SELECT></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Required Level:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="reqlevel" SIZE="3" MAXLENGTH="2"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Recamended Level:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="reclevel" SIZE="3" MAXLENGTH="2"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  Deity:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="deity"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
	    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	      <TR>
		<TD>ALL</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="raceall" VALUE="1"></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
	      </TR>
	      <TR>
		<TD>BAR</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="bar" VALUE="1"></TD>
		<TD>DEF</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="def" VALUE="1"></TD>
		<TD>DWF</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="dwf" VALUE="1"></TD>
		<TD>ERU</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="eru" VALUE="1"></TD>
		<TD>FRG</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="frg" VALUE="1"></TD>
	      </TR>
	      <TR>
		<TD>GNM</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="gnm" VALUE="1"></TD>
		<TD>HFL</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="hfl" VALUE="1"></TD>
		<TD>HEF</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="hef" VALUE="1"></TD>
		<TD>HIE</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="hie" VALUE="1"></TD>
		<TD>HUM</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="hum" VALUE="1"></TD>
	      </TR>
	      <TR>
		<TD>IKS</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="isk" VALUE="1"></TD>
		<TD>OGR</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="ogr" VALUE="1"></TD>
		<TD>TRL</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="trl" VALUE="1"></TD>
		<TD>ELF</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="elf" VALUE="1"></TD>
		<TD>VAH</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="vah" VALUE="1"></TD>
	      </TR>
	    </TABLE>
	  </CENTER>
	</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
	    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	      <TR>
		<TD>ALL</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="classall" VALUE="1"></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
	      </TR>
	      <TR>
		<TD>BRD</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="brd" VALUE="1"></TD>
		<TD>BST</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="bst" VALUE="1"></TD>
		<TD>BER</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="ber" VALUE="1"></TD>
		<TD>CLR</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="clr" VALUE="1"></TD>
		<TD>DRU</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="dru" VALUE="1"></TD>
	      </TR>
	      <TR>
		<TD>ENC</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="enc" VALUE="1"></TD>
		<TD>MAG</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="mag" VALUE="1"></TD>
		<TD>MNK</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="mnk" VALUE="1"></TD>
		<TD>NEC</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="nec" VALUE="1"></TD>
		<TD>PAL</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="pal" VALUE="1"></TD>
	      </TR>
	      <TR>
		<TD>RNG</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="rng" VALUE="1"></TD>
		<TD>ROG</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="rog" VALUE="1"></TD>
		<TD>SHD</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="shd" VALUE="1"></TD>
		<TD>SHM</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="shm" VALUE="1"></TD>
		<TD>WAR</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="war" VALUE="1"></TD>
	      </TR>
	      <TR>
		<TD>WIZ</TD>
		<TD>
		  <INPUT TYPE="checkbox" NAME="wiz" VALUE="1"></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
		<TD></TD>
	      </TR>
	    </TABLE>
	  </CENTER>
	</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=hidden NAME="do" VALUE="save">
	  <INPUT TYPE=submit VALUE="Add Item"> &nbsp; &nbsp;
	  <INPUT TYPE=reset VALUE="Reset Form"></TD>
      </TR>
    </TABLE>
</CENTER>
</FORM>

~;

}

# _____________________________________________________________________________

sub save {

if ($input{'name'} eq "") {

print qq~
Please Enter an Item Name!
~;

&new;

}
else {

$name = "$input{'name'}";
$lore = "$input{'lore'}";
$magic = "$input{'magic'}"; 
$nodrop = "$input{'nodrop'}"; 
$type = "$input{'type'}"; 
$slot = "$input{'slot'}"; 
$dmg = "$input{'dmg'}"; 
$dly = "$input{'dly'}"; 
$dmgbonus = "$input{'dmgbonus'}"; 
$ac = "$input{'ac'}"; 
$effect = "$input{'effect'}"; 
$bane = "$input{'bane'}"; 
$skillmod = "$input{'skillmod'}"; 
$focus = "$input{'focus'}"; 
$dex = "$input{'dex'}"; 
$sta = "$input{'sta'}"; 
$str = "$input{'str'}"; 
$cha = "$input{'cha'}"; 
$agi = "$input{'agi'}"; 
$int = "$input{'int'}"; 
$wis = "$input{'wis'}"; 
$hp = "$input{'hp'}"; 
$mana = "$input{'mana'}"; 
$svfire = "$input{'svfire'}"; 
$svdisease = "$input{'svdisease'}"; 
$svcold = "$input{'svcold'}"; 
$svmagic = "$input{'svmagic'}"; 
$svpoison = "$input{'svpoison'}"; 
$weight = "$input{'weight'}"; 
$size = "$input{'size'}"; 
$reqlevel = "$input{'reqlevel'}"; 
$reclevel = "$input{'reclevel'}"; 
$deity = "$input{'deity'}"; 
$raceall = "$input{'raceall'}"; 
$bar = "$input{'bar'}"; 
$def = "$input{'def'}"; 
$dwf = "$input{'dwf'}"; 
$eru = "$input{'eru'}"; 
$frg = "$input{'frg'}"; 
$gnm = "$input{'gnm'}"; 
$hfl = "$input{'hfl'}"; 
$hef = "$input{'hef'}"; 
$hie = "$input{'hie'}"; 
$hum = "$input{'hum'}"; 
$isk = "$input{'isk'}"; 
$ogr = "$input{'ogr'}"; 
$trl = "$input{'trl'}"; 
$elf = "$input{'elf'}"; 
$vah = "$input{'vah'}"; 
$classall = "$input{'classall'}"; 
$brd = "$input{'brd'}"; 
$bst = "$input{'bst'}"; 
$ber = "$input{'ber'}"; 
$clr = "$input{'clr'}"; 
$dru = "$input{'dru'}"; 
$enc = "$input{'enc'}"; 
$mag = "$input{'mag'}"; 
$mnk = "$input{'mnk'}"; 
$nec = "$input{'nec'}"; 
$pal = "$input{'pal'}"; 
$rng = "$input{'rng'}"; 
$rog = "$input{'rog'}"; 
$shd = "$input{'shd'}"; 
$shm = "$input{'shm'}"; 
$war = "$input{'war'}"; 
$wiz = "$input{'wiz'}";
$endur = "$input{'endur'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp = "INSERT INTO `bank` ( `name` , `lore`, `magic` , `nodrop` , `type` , `slot` , `dmg` , `dly` , `dmgbonus` , `ac` , `effect` , `bane` , `skill` , `focus` , `dex` , `sta` , `str` , `cha` , `agi` , `int` , `wis` , `hp` , `mana` , `svfire` , `svdisease` , `svcold` , `svmagic` , `svpoision` , `weight` , `size` , `reqlvl` , `reclvl` , `deity` , `raceall` , `bar` , `def` , `dwf` , `eru` , `frg` , `gnm` , `hfl` , `hie` , `hum` , `iks` , `ogr` , `trl` , `elf` , `vah` , `classall` , `brd` , `bst` , `ber` , `clr` , `dru` , `enc` , `mag` , `mnk` , `nec` , `pal` , `rng` , `rog` , `shd` , `shm` , `war` , `wiz` , `hef` , `ENDUR` )";

$temp = "$temp VALUES ( 
'$name', 
'$lore', 
'$magic', 
'$nodrop', 
'$type', 
'$slot', 
'$dmg', 
'$dly', 
'$dmgbonus', 
'$ac', 
'$effect', 
'$bane', 
'$skillmod', 
'$focus', 
'$dex', 
'$sta', 
'$str', 
'$cha', 
'$agi', 
'$int', 
'$wis', 
'$hp', 
'$mana', 
'$svfire', 
'$svdisease', 
'$svcold', 
'$svmagic', 
'$svpoison', 
'$weight', 
'$size', 
'$reqlevel', 
'$reclevel', 
'$deity', 
'$raceall', 
'$bar', 
'$def', 
'$dwf', 
'$eru', 
'$frg', 
'$gnm', 
'$hfl', 
'$hie', 
'$hum', 
'$isk', 
'$ogr', 
'$trl', 
'$elf', 
'$vah', 
'$classall', 
'$brd', 
'$bst', 
'$ber', 
'$clr', 
'$dru', 
'$enc', 
'$mag', 
'$mnk', 
'$nec', 
'$pal', 
'$rng', 
'$rog', 
'$shd', 
'$shm', 
'$war', 
'$wiz', 
'$hef',
'$endur'
 ) ";


$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;


print qq~
Item added to database!
~;

&PrintDefault;

}

}

# _____________________________________________________________________________


########################################
# Code to get the data from GET & POST #
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