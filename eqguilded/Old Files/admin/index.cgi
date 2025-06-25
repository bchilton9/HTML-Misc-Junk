#!/usr/bin/perl

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

$siteurl = "http://www.eqguilded.com";

##################################################################################

use DBI;

print "Content-type: text/html\n\n";

##################################################################################

if ($INPUT{'do'} eq "editnews") { &editnews; }
elsif ($INPUT{'do'} eq "savenews") { &savenews; }
elsif ($INPUT{'do'} eq "addhelpitem") { &addhelpitem; }
elsif ($INPUT{'do'} eq "savehelpitem") { &savehelpitem; }
elsif ($INPUT{'do'} eq "edithelppage") { &edithelppage; }
elsif ($INPUT{'do'} eq "savehelppage") { &savehelppage; }
elsif ($INPUT{'do'} eq "edititemsone") { &edititemsone; }
elsif ($INPUT{'do'} eq "edititemstwo") { &edititemstwo; }
elsif ($INPUT{'do'} eq "additem") { &additem; }
elsif ($INPUT{'do'} eq "additemtwo") { &additemtwo; }
elsif ($INPUT{'do'} eq "editmem") { &editmem; }
elsif ($INPUT{'do'} eq "delete_user") { &delete_user; }
else { &list; }

##################################################################################

sub list {

print <<"HTML";
<CENTER>
$tag<BR>
<HR width=50%>
<A HREF=?do=editmem>Edit Member</A><BR>
Edit Guild<BR>
<A HREF=?do=editnews>Edit Main Page</A><BR>
<A HREF=?do=additem>Add Items</A><BR>
<A HREF=?do=edititemsone>Edit Items</A><BR>
<A HREF=?do=addhelpitem>Add Help Items</A><BR>
Edit Help Items<BR>
<A HREF=?do=edithelppage>Edit Help Page</A><BR>
<HR width=50%>
HTML

}

##################################################################################

sub editmem {
print <<"HTML";
<CENTER>
<TABLE BORDER=0 CELLPADDING="5">
  <TR>
    <TD colspan="2" align="center"></TD>
    <TD><B>Id</TD>
    <TD><B>Name</TD>
    <TD><B>Sur</TD>
    <TD><B>Password</TD>
    <TD><B>E-Mail</TD>
    <TD><B>Guild</TD>
    <TD><B>Class</TD>
    <TD><B>Race</TD>
    <TD><B>Level</TD>
</TR>
HTML

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp ="select * from user ORDER BY name";


$sth=$dbh->prepare($temp);
$sth->execute;


while(@row = $sth->fetchrow_array) { 

print <<"HTML";
  <TR>
    <TD valign="middle" bgcolor="#DDDDDD">Edit</TD>
    <TD valign="middle" bgcolor="#DDDDDD"><A HREF=?do=delete_user&name=$row[0]><FONT COLOR=#000000>Delete</FONT></A></TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[0]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[1]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[2]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[3]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[4]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[5]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[6]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[7]</TD>
    <TD valign="top" bgcolor="#DDDDDD">$row[8]</TD>
</TR>
<TR>

<TR>

<TD colspan="5" align="center"></TD>
    <TD><SMALL>Date Created:</SMALL></TD>
    <TD valign="top"><SMALL>$row[9]</SMALL></TD>
    <TD colspan="2"><SMALL><P ALIGN=right>Date Last Accessed:</SMALL></TD>
    <TD colspan="2" valign="top"><SMALL>$row[10]</SMALL></TD>
  </TR>
<TR>
<TD colspan="11">
</TD>
</TR>
HTML
 
} 

$sth->finish; 
$dbh->disconnect; 

print <<"HTML";
</TABLE>
HTML
}

##################################################################################

sub delete_user {

$tag = "<B>User Deleted</B>";

&list;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$name = "$INPUT{'name'}";

$temp = "DELETE FROM user WHERE name = '$name'"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

}

##################################################################################
#Edit Guild
##################################################################################
#Edit Help item
##################################################################################
#Delete Item
##################################################################################
#Edit stats on item
##################################################################################

sub additem {

print <<"HTML";
<CENTER>
<FORM>
  <CENTER>
    <TABLE id=table WIDTH="500">
      <TR>
	<TD COLSPAN=6>

 <TABLE BORDER CELLPADDING="2">
    <TR>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="1" CHECKED></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/1.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="2"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/2.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="3"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/3.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="4"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/4.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="5"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/5.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="6"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/6.gif"></TD>

    </TR>
    <TR>

      <TD><INPUT TYPE="radio" NAME="image" VALUE="7"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/7.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="8"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/8.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="9"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/9.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="10"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/10.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="11"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/11.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="12"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/12.gif"></TD>

</TR>
<TR>

      <TD><INPUT TYPE="radio" NAME="image" VALUE="13"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/13.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="14"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/14.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="15"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/15.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="16"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/16.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="17"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/17.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="18"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/18.gif"></TD>

</TR>
<TR>

      <TD><INPUT TYPE="radio" NAME="image" VALUE="19"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/19.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="20"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/20.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="21"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/21.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="22"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/22.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="23"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/23.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="24"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/24.gif"></TD>

</TR>
<TR>

      <TD><INPUT TYPE="radio" NAME="image" VALUE="25"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/25.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="26"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/26.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="27"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/27.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="28"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/28.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="29"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/29.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="30"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/30.gif"></TD>
</TR>
<TR>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="31"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/31.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="32"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/32.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="33"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/33.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="34"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/34.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="35"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/35.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="36"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/36.gif"></TD>

    </TR>
<TR>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="37"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/37.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="38"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/38.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="39"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/39.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="40"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/40.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="41"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/41.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="42"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/42.gif"></TD>

    </TR>
<TR>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="43"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/43.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="44"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/44.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="45"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/45.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="46"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/46.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="47"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/47.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="48"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/48.gif"></TD>

    </TR>
<TR>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="49"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/49.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="50"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/50.gif"></TD>
      <TD><INPUT TYPE="radio" NAME="image" VALUE="51"></TD>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/51.gif"></TD>
      <TD></TD>
      <TD></TD>
      <TD></TD>
      <TD></TD>
      <TD></TD>
      <TD></TD>
    </TR>
  </TABLE>
</TD>
      </TR>
      <TR>
	<TD COLSPAN=6>
	  <INPUT TYPE="text" NAME="name" VALUE="Item Name"></TD>
      </TR>
      <TR>
	<TD COLSPAN=6>
	  <INPUT TYPE="checkbox" NAME="magic" VALUE="magic">Magic Item<BR>
<INPUT TYPE="checkbox" NAME="lore" VALUE="lore">Lore Item<BR>
<INPUT TYPE="checkbox" NAME="nodrop" VALUE="nodrop">No Drop Item

</TD>
      </TR>
      <TR>
	<TD>Slot:</TD>
	<TD COLSPAN=3>
  <SELECT NAME="slot">
  <OPTION value=ammo>Ammo
  <OPTION value=arms>Arms
  <OPTION value=back>Back
  <OPTION value=charm>Charm
  <OPTION value=chest>Chest
  <OPTION value=ears>Ears
  <OPTION value=face>Face
  <OPTION value=feet>Feet
  <OPTION value=fingers>Fingers
  <OPTION value=hand>Hands
  <OPTION value=head>Head
  <OPTION value=inven>Inventory
  <OPTION value=legs>Legs
  <OPTION value=neck>Neck
  <OPTION value=prim>Primary
  <OPTION value=primsec>Primary/Secondary
  <OPTION value=primsecrng>Primary/Secondary/Range
  <OPTION value=primsecrngammo>Primary/Secondary/Range/Ammo
  <OPTION value=rang>Range
  <OPTION value=sec>Secondary
  <OPTION value=shoulder>Shoulders
  <OPTION value=waist>Waist
  <OPTION value=wrists>Wrists
</SELECT>
</TD>
	<TD></TD>
	<TD></TD>
      </TR>
      <TR>
	<TD>Skill:</TD>
	<TD COLSPAN=3>
	  <INPUT TYPE="text" NAME="skill"></TD>
	<TD>Delay:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="delay" SIZE="3"></TD>
      </TR>
      <TR>
	<TD>Dmg:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="dmg" SIZE="3"></TD>
	<TD>AC:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="ac" SIZE="3"></TD>
	<TD>WT:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="wt" SIZE="3"></TD>
      </TR>
      <TR>
	<TD>STR:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="str" SIZE="3"></TD>
	<TD>STA:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="sta" SIZE="3"></TD>
	<TD>AGI:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="agi" SIZE="3"></TD>
      </TR>
      <TR>
	<TD>DEX:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="dex" SIZE="3"></TD>
	<TD>WIS:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="wis" SIZE="3"></TD>
	<TD>INT:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="int" SIZE="3"></TD>
      </TR>
      <TR>
	<TD>CHA:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="cha" SIZE="3"></TD>
	<TD>SVP:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="svp" SIZE="3"></TD>
	<TD>SVM:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="svm" SIZE="3"></TD>
      </TR>
      <TR>
	<TD>SVD:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="svd" SIZE="3"></TD>
	<TD>SVF:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="svf" SIZE="3"></TD>
	<TD>SVC:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="svc" SIZE="3"></TD>
      </TR>
      <TR>
	<TD>HP:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="hp" SIZE="3"></TD>
	<TD>SVF:</TD>

      <TR>
	<TD>Effect:</TD>
	<TD COLSPAN=5>
	  <INPUT TYPE="text" NAME="effect"></TD>
      </TR>
      <TR>
	<TD>Skill Mod:</TD>
	<TD COLSPAN=5>
	  <INPUT TYPE="text" NAME="smod"></TD>
      </TR>
      <TR>
	<TD>Class:</TD>
	<TD COLSPAN=5>
	  <INPUT TYPE="text" NAME="class"></TD>
      </TR>
      <TR>
	<TD>Race:</TD>
	<TD COLSPAN=5>
	  <INPUT TYPE="text" NAME="race"></TD>
      </TR>
      <TR>
	<TD COLSPAN=6><P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=additemtwo>
	  <INPUT TYPE=submit VALUE="Add_Item"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}

##################################################################################

sub additemtwo {

open (DATA, "../items/$INPUT{'slot'}.lst");
@data = <DATA>;
close DATA;
open(DATA, ">../items/$INPUT{'slot'}.lst");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'image'}::$INPUT{'name'}::$INPUT{'slot'}::$INPUT{'magic'}::$INPUT{'skill'}::$INPUT{'delay'}::$INPUT{'dmg'}::$INPUT{'ac'}::$INPUT{'wt'}::$INPUT{'str'}::$INPUT{'sta'}::$INPUT{'agi'}::$INPUT{'dex'}::$INPUT{'wis'}::$INPUT{'int'}::$INPUT{'cha'}::$INPUT{'svp'}::$INPUT{'svm'}::$INPUT{'svd'}::$INPUT{'svf'}::$INPUT{'svc'}::$INPUT{'effect'}::$INPUT{'smod'}::$INPUT{'class'}::$INPUT{'race'}::$INPUT{'hp'}::true::$INPUT{'lore'}::$INPUT{'nodrop'}\n";
close DATA;

$tag = "<B>Item Added</B>";

&list;
}

##################################################################################

sub edititemsone {

print <<"HTML";
<CENTER>
<B>Chose a slot</B>
<P>
<BR>

<A HREF=?do=edititemstwo&slot=ammo>Ammo</A><BR>
<A HREF=?do=edititemstwo&slot=arms>Arms</A><BR>
<A HREF=?do=edititemstwo&slot=back>Back</A><BR>
<A HREF=?do=edititemstwo&slot=charm>Charm</A><BR>
<A HREF=?do=edititemstwo&slot=chest>Chest</A><BR>
<A HREF=?do=edititemstwo&slot=ears>Ears</A><BR>
<A HREF=?do=edititemstwo&slot=face>Face</A><BR>
<A HREF=?do=edititemstwo&slot=feet>Feet</A><BR>
<A HREF=?do=edititemstwo&slot=fingers>Fingers</A><BR>
<A HREF=?do=edititemstwo&slot=hand>Hands</a><BR>
<A HREF=?do=edititemstwo&slot=head>Head</A><BR>
<A HREF=?do=edititemstwo&slot=inven>Inventory</A><BR>
<A HREF=?do=edititemstwo&slot=legs>Legs</A><BR>
<A HREF=?do=edititemstwo&slot=neck>Neck</A><BR>
<A HREF=?do=edititemstwo&slot=prim>Primary</A><BR>
<A HREF=?do=edititemstwo&slot=primsec>Primary/Secondary</A><BR>
<A HREF=?do=edititemstwo&slot=primsecrng>Primary/Secondary/Range</A><BR>
<A HREF=?do=edititemstwo&slot=primsecrngammo>Primary/Secondary/Range/Ammo</A><BR>
<A HREF=?do=edititemstwo&slot=rang>Range</A><BR>
<A HREF=?do=edititemstwo&slot=sec>Secondary</A><BR>
<A HREF=?do=edititemstwo&slot=shoulder>Shoulders</A><BR>
<A HREF=?do=edititemstwo&slot=waist>Waist</A><BR>
<A HREF=?do=edititemstwo&slot=wrists>Wrists</A><BR>



<CENTER><P>
<A HREF=?>Main</A>
HTML
}

##################################################################################

sub edititemstwo {
open (DATA, "../items/$INPUT{'slot'}.lst");
@data = <DATA>;
close DATA;

foreach $line (@data) {
($image, $name, $slot, $magic, $skill, $delay, $dmg, $ac, $wt, $str, $sta, $agi, $dex, $wis, $int, $cha, $svp, $svm, $svd, $svf, $svc, $effect, $smod, $class, $race, $hp, $vear, $lore, $nodrop) = split(/::/, $line);

print <<"HTML";
<CENTER>
  <TABLE BORDER CELLPADDING="2" ALIGN="Center" WIDTH="320">
    <TR>
      <TD VALIGN="top"><SMALL><IMG SRC=http://www.eqguilded.com/images/items/$image.gif></SMALL></TD>
      <TD COLSPAN=4><SMALL>$name</SMALL></TD>
    </TR>
    <TR>
      <TD><SMALL>$magic $lore $nodrop</SMALL></TD>
      <TD><SMALL>Slot: $slot</SMALL></TD>
      <TD><SMALL>AC: $ac</SMALL></TD>
      <TD><SMALL>WT: $wt</SMALL></TD>
      <TD><SMALL>HP: $hp</SMALL></TD>
    </TR>
    <TR>
      <TD><SMALL>Dmg: $dmg</SMALL></TD>
      <TD><SMALL>STR: $str</SMALL></TD>
      <TD><SMALL>STA: $sta</SMALL></TD>
      <TD><SMALL>AGI: $agi</SMALL></TD>
      <TD><SMALL>DEX: $dex</SMALL></TD>
    </TR>
    <TR>
      <TD><SMALL>WIS: $wis</SMALL></TD>
      <TD><SMALL>INT: $int</SMALL></TD>
      <TD><SMALL>CHA: $cha</SMALL></TD>
      <TD><SMALL>SVP: $svp</SMALL></TD>
      <TD><SMALL>SVM: $svm</SMALL></TD>
    </TR>
    <TR>
      <TD><SMALL>SVD: $svd</SMALL></TD>
      <TD><SMALL>SVF: $svf</SMALL></TD>
      <TD><SMALL>SVC: $svc</SMALL></TD>
      <TD></TD>
      <TD></TD>
    </TR>
    <TR>
      <TD COLSPAN=5><SMALL>Effect: $effect</SMALL></TD>
    </TR>
    <TR>
      <TD COLSPAN=5><SMALL>Skill Mod: $smod</SMALL></TD>
    </TR>
    <TR>
      <TD COLSPAN=5><SMALL>Class: $class</SMALL></TD>
    </TR>
    <TR>
      <TD COLSPAN=5><SMALL>Race: $race</SMALL></TD>
    </TR>
    <TR>
      <TD COLSPAN=5><SMALL>Vearafied: $vear</SMALL></TD>
    </TR>
    <TR>
      <TD COLSPAN=5>EDIT BUTTON DELETE BUTTON</TD>
    </TR>
  </TABLE>
</CENTER>
<CENTER><P>
<A HREF=?>Main</A>
HTML
}
}

##################################################################################

sub editnews {

print <<"HTML";
<FORM ACTION="index.cgi" METHOD="POST">
  <P ALIGN=Center>
  <TEXTAREA NAME="news" ROWS="20" COLS="60">
HTML

open (DATA, "../news.dat");
@data = <DATA>;
close DATA;

print "@data";

print <<"HTML";
</TEXTAREA>
  <P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=savenews>
  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
  <INPUT TYPE=reset>
</FORM>
<CENTER><P>
<A HREF=?>Main</A>
HTML

}

##################################################################################

sub savenews {

open(DATA, ">../news.dat");
print DATA "$INPUT{'news'}";
close DATA;

$tag = "<B>Main Page Updated</B>";

&list;

}

##################################################################################

sub addhelpitem {


open (FILE, "help.cnt");
flock (FILE, 2);
$abcdefg = <FILE>;
chop ($abcdefg);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);


$abcdefg++;


open(DATA, ">help.cnt");
print DATA "$abcdefg\n";
print DATA "junk\n";
close DATA;


print <<"HTML";
<FORM ACTION="index.cgi" METHOD="POST">
  <P ALIGN=Center>
  <TEXTAREA NAME="hlp" ROWS="30" COLS="50">SUBJECT
&lt;HR&gt;
INFO
&lt;BR&gt;
&lt;P&gt;
&lt;B&gt;NOTE:&lt;/B&gt; NOTE
</TEXTAREA>
  <P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=savehelpitem>
<INPUT TYPE=hidden NAME=num VALUE=$abcdefg>
  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
  <INPUT TYPE=reset>
</FORM>
<CENTER><P>
<A HREF=?>Main</A>
HTML

}

##################################################################################

sub savehelpitem {

open(DATA, ">../help/$INPUT{'num'}.hlp");
print DATA "$INPUT{'hlp'}";
close DATA;

$tag = "<B>Help Item Updated/Added</B><BR>";

$tag = "$tag URL to help item is http://www.eqguilded.com/help.cgi?num=$INPUT{'num'}";

&list;

}

##################################################################################

sub edithelppage {

print <<"HTML";
<FORM ACTION="index.cgi" METHOD="POST">
  <P ALIGN=Center>
  <TEXTAREA NAME="hlp" ROWS="20" COLS="60">
HTML

open (DATA, "../help.html");
@data = <DATA>;
close DATA;

print "@data";

print <<"HTML";
</TEXTAREA>
  <P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=savehelppage>
  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
  <INPUT TYPE=reset>
</FORM>
<CENTER><P>
<A HREF=?>Main</A>
HTML

}

##################################################################################

sub savehelppage {

open(DATA, ">../help.html");
print DATA "$INPUT{'hlp'}";
close DATA;

$tag = "<B>Help Page Updated</B><BR>";
&list;
}

##################################################################################