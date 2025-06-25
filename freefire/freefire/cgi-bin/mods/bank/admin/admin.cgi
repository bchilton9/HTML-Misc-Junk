#!/usr/bin/perl

use DBI;


BEGIN {
	##--------------------------------------------------------------
	## If you are not using standard folder locations, the following
	## line may need to be changed to match your installation
	##--------------------------------------------------------------

	require "../../../config.pl";
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


if ($input{'do'} eq "additem") { &additem; }
elsif ($input{'do'} eq "additemtwo") { &additemtwo; }
elsif ($input{'do'} eq "addedit") { &addedit; }
elsif ($input{'do'} eq "addeditb") { &addeditb; }
elsif ($input{'do'} eq "addeditc") { &addeditc; }
elsif ($input{'do'} eq "addone") { &addone; }
elsif ($input{'do'} eq "subone") { &subone; }
elsif ($input{'do'} eq "delete") { &delete; }


#elsif ($input{'do'} eq "") { &; }

else { &PrintDefault; }

print_bottom();

# _____________________________________________________________________________

sub addone {

$qty = "$input{'qty'}";
$qty = $qty + 1;
$item = "$input{'item'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp = "UPDATE `guildbank` SET `qty` = '$qty' WHERE `item` = '$item' LIMIT 1";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

print "Item Updated!";
}

# _____________________________________________________________________________

sub subone {

$qty = "$input{'qty'}";
$qty = $qty - 1;
$item = "$input{'item'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp = "UPDATE `guildbank` SET `qty` = '$qty' WHERE `item` = '$item' LIMIT 1";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

print "Item Updated!";
}

# _____________________________________________________________________________

sub delete {

$item = "$input{'item'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp = "DELETE FROM `guildbank` WHERE `item` = '$item' LIMIT 1";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

print "Item Deleted!";
}

# _____________________________________________________________________________
sub PrintDefault {

print qq~
<A HREF="?do=additem">Add Item to
Database</A><BR>
<A HREF="?do=addedit">Add/Edit Items in Bank</A>
~;

}

# _____________________________________________________________________________

sub addedit {

print qq~
<P ALIGN=Center>
To Add an item enter the full or part of the name in the box below!
<FORM onSubmit="submitonce(this)">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Item:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="search"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="do" VALUE="addeditb">
	  <INPUT TYPE=submit VALUE="Search"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>

<CENTER>
  <TABLE border="0" cellspacing="0" cellpadding="0" class="forumtitlebackcolor" WIDTH=75%>
    <TR>
      <TD class="boardtitle">Name</TD>
      <TD class="boardtitle">Quanty</TD>
      <TD class="boardtitle">Add One</TD>
      <TD class="boardtitle">Subtract One</TD>
      <TD class="boardtitle">Delete</TD>
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
      <TD class="forumwindow2"><A HREF=?do=addone&item=$row[0]&qty=$row[1]>Add One</A></TD>
~;

if ($row[1] eq "1") {
print "<TD class=forumwindow2>Subtract One</TD>";
}
else {
print "<TD class=forumwindow2><A HREF=?do=subone&item=$row[0]&qty=$row[1]>Subtract One</A></TD>";
}

print qq~
      <TD class="forumwindow2"><A HREF=?do=delete&item=$row[0]>Delete</A></TD>
    </TR>
~;
	  
 } 

}
$sth->finish; 
$dbh->disconnect;

print qq~
  </TABLE>
</CENTER>
~;

}

# _____________________________________________________________________________

sub addeditb {

$search = "$input{'search'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp ="
SELECT  *
FROM bank 
WHERE name LIKE '%$search%' 
order by name
";

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
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Items Found:</TD>
	<TD>
<SELECT NAME="item">
$tag
</SELECT></TD>
      </TR>
      <TR>
	<TD>Quanty:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="qty" VALUE="1" SIZE="3" MAXLENGTH="1"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="do" VALUE="addeditc">
	  <INPUT TYPE=submit VALUE="Add Item"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;

}

# _____________________________________________________________________________

sub addeditc {

$item = "$input{'item'}";
$qty = "$input{'qty'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp ="
SELECT  *
FROM bank 
WHERE num = '$item' 
order by name
";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$name = "$row[1]";
	  
 } 

}
$sth->finish; 
$dbh->disconnect;


my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp ="
SELECT  *
FROM guildbank 
WHERE item LIKE '$item' 

";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$noitem = "$row[0]";	  
 } 

}
$sth->finish; 
$dbh->disconnect;


if ($noitem ne "") {

print qq~
Item Already in Guild Bank! Please use the Edit Items!
~;

}
else {

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp = "INSERT INTO `guildbank` ( `item` , `qty` , `name` )";
$temp = "$temp VALUES ( '$item', '$qty', '$name'  ) ";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

print qq~
Item Added to the Guilds Bank!
~;
}

}

# _____________________________________________________________________________

sub additem {

print qq~
<form onSubmit="submitonce(this)">
  <CENTER>
This will only add the item into the database you will still have to add the item into the guild bank!<BR>
<B>IF THE ITEM DOSE NOT HAVE THE STAT LEAVE IT BLANK!</B><BR>
<B>ONCE YOU SUBMIT THIS FORM YOU CAN NOT EDIT THE ITEM LATER! MAKE SURE EVERYTHING IS CORRECT!</B>
<P>
    <TABLE BORDER CELLSPACING="1" CELLPADDING="2" ALIGN="Center">
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
	  <INPUT TYPE=hidden NAME="do" VALUE="additemtwo">
	  <INPUT TYPE=submit VALUE="Add Item"> &nbsp; &nbsp;
	  <INPUT TYPE=reset VALUE="Reset Form"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>

~;

}


# _____________________________________________________________________________
sub additemtwo {

if ($input{'name'} eq "") {

print qq~
Please Enter an Item Name!
~;

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
$hef = "$input{'hef'}";
$endur = "$input{'endur'}";


my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_freefire:localhost","eqguilded","sword") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$temp = "INSERT INTO `bank` ( `name` , `lore`, `magic` , `nodrop` , `type` , `slot` , `dmg` , `dly` , `dmgbonus` , `ac` , `effect` , `bane` , `skill` , `focus` , `dex` , `sta` , `str` , `cha` , `agi` , `int` , `wis` , `hp` , `mana` , `svfire` , `svdisease` , `svcold` , `svmagic` , `svpoision` , `weight` , `size` , `reqlvl` , `reclvl` , `deity` , `raceall` , `bar` , `def` , `dwf` , `eru` , `frg` , `gnm` , `hfl` , `hie` , `hum` , `iks` , `ogr` , `trl` , `elf` , `vah` , `classall` , `brd` , `bst` , `ber` , `clr` , `dru` , `enc` , `mag` , `mnk` , `nec` , `pal` , `rng` , `rog` , `shd` , `shm` , `war` , `wiz` , `hef', `ENDUR` )";

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


}
}


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