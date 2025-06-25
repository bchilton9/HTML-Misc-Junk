#!/usr/bin/perl

use DBI;


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

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

$mon = $mon + 1;
$year = $year + 1900;

$tag = qq~
<A HREF=index.cgi>Edit Main</A><BR>
Todays Date: $year-$mon-$mday<BR>
<CENTER>
~;

##################################################################################

if ($INPUT{'do'} eq "guild_edit_html") { &guild_edit_html; }
elsif ($INPUT{'do'} eq "guild_edit_html_b") { &guild_edit_html_b; }
elsif ($INPUT{'do'} eq "guild_edit_html_c") { &guild_edit_html_c; }
elsif ($INPUT{'do'} eq "list_guilds") { &list_guilds; }
elsif ($INPUT{'do'} eq "edit_guild") { &edit_guild; }
elsif ($INPUT{'do'} eq "edit_guild_b") { &edit_guild_b; }

#elsif ($INPUT{'do'} eq "delete_guild") { &delete_guild; }

else { &main; }

##################################################################################

sub main {

print "Content-type: text/html\n\n";
print "<CENTER>";


print "<A HREF=?do=guild_edit_html>Edit Html</A><BR>";
print "<A HREF=?do=list_guilds>List Guilds</A><BR>";
print "<A HREF=http://www.eqguilded.com/links/admin/admin.cgi>Edit Links</A><BR>";
print "<A HREF=http://www.eqguilded.com/banner/showsell.pl?PASSWORD=0519aa&SCREEN=LOGIN&COMMAND=login>Edit Banners</A><BR>";
print "<A HREF=http://www.eqguilded.com/faq/faqman.cgi?action=list&page=index.html&pass=0519aa&submit=Log+On>Edit FAQ</A>";


}

##################################################################################

sub list_guilds {

$order = "$INPUT{'order'}";

if ($order eq "") {
$order = "shortname";
}

$tag = qq~ $tag
<CENTER>
  <TABLE BORDER CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD><A HREF=http://www.eqguilded.com/admin/index.cgi?do=list_guilds&order=shortname>Shortname</A></TD>
      <TD><A HREF=http://www.eqguilded.com/admin/index.cgi?do=list_guilds&order=longname>Longname</A></TD>
      <TD><A HREF=http://www.eqguilded.com/admin/index.cgi?do=list_guilds&order=email>E-Mail</A></TD>
      <TD><A HREF=http://www.eqguilded.com/admin/index.cgi?do=list_guilds&order=goldexp>Gold Exp</A></TD>
      <TD><A HREF=http://www.eqguilded.com/admin/index.cgi?do=list_guilds&order=createdon>Created on</A></TD>
      <TD><A HREF=http://www.eqguilded.com/admin/index.cgi?do=list_guilds&order=createdby>Created By</A></TD>
      <TD><A HREF=http://www.eqguilded.com/admin/index.cgi?do=list_guilds&order=server>Server</A></TD>
      <TD></TD>
      <TD></TD>
    </TR>
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild order by `$order`";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;


if ($row[8] ne "") {
$tag = qq~ $tag
    <TR>
      <TD><A HREF=http://www.eqguilded.com/$row[0]>$row[0]</A></TD>
      <TD>$row[1]</TD>
      <TD><A HREF=mailto:$row[3]>$row[3]</A></TD>
      <TD>$row[4]</TD>
      <TD>$row[6]</TD>
      <TD>$row[7]</TD>
      <TD>$row[8]</TD>
      <TD><A HREF=?do=edit_guild&guild=$row[0]>EDIT GUILD</A></TD>
      <TD><A HREF=?do=delete_guild&guild=$row[0]>DELETE GUILD</A></TD>
    </TR>
~;
}

 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag
  </TABLE>
</CENTER>
~;

print "Content-type: text/html\n\n";
print "$tag";

}

##################################################################################

sub edit_guild {

$guild = "$INPUT{'guild'}";


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild WHERE `shortname` = '$guild'";

$sth=$dbh->prepare($temp);
$sth->execute;  #Execute the query 

@row=$sth->fetchrow_array;
$row_hit=1;

$sth->finish; 
$dbh->disconnect; 


$tag = qq~ $tag
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Short Name:</TD>
	<TD>$row[0]
	  <INPUT TYPE="hidden" NAME="shortname" VALUE="$row[0]"></TD>
      </TR>
      <TR>
	<TD>Long Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="longname" VALUE="$row[1]"></TD>
      </TR>
      <TR>
	<TD>Password:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="password" VALUE="$row[2]"></TD>
      </TR>
      <TR>
	<TD>E-Mail:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="email" VALUE="$row[3]"></TD>
      </TR>
      <TR>
	<TD>Gold Exp:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="goldexp" VALUE="$row[4]"></TD>
      </TR>
      <TR>
	<TD>Created On:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="createdon" VALUE="$row[6]"></TD>
      </TR>
      <TR>
	<TD>Created By:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="createdby" VALUE="$row[7]"></TD>
      </TR>
      <TR>
	<TD>Server:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="server" VALUE="$row[8]"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=edit_guild_b>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;

print "Content-type: text/html\n\n";
print "$tag";

}

##################################################################################

sub edit_guild_b {

$shortname = "$INPUT{'shortname'}";
$longname = "$INPUT{'longname'}";
$password = "$INPUT{'password'}";
$email = "$INPUT{'email'}";
$goldexp = "$INPUT{'goldexp'}";
$createdon = "$INPUT{'createdon'}";
$createdby = "$INPUT{'createdby'}";
$server = "$INPUT{'server'}";


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n";

$temp = "UPDATE `guild` SET `longname` = '$longname', `password` = '$password', `email` = '$email', `goldexp` = '$goldexp', `createdon` = '$createdon', `createdby` = '$createdby', `server` = '$server' WHERE `shortname` = '$shortname' LIMIT 1";

$sth=$dbh->prepare($temp);
$sth->execute;  #Execute the query 
$sth->finish; 
$dbh->disconnect; 


$tag = qq~ $tag
Guild Saved
~;

print "Content-type: text/html\n\n";
print "$tag";

}

##################################################################################

sub guild_edit_html {


$tag = qq~ $tag
<CENTER>Please chose a templet to edit!<BR>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Templet:</TD>
	<TD>
	  <SELECT NAME="templet">
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from html order by `name`";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;


$tag = "$tag <OPTION>$row[0]\n";
 } 

}
$sth->finish; 
$dbh->disconnect; 




$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_html_b">
	  <INPUT TYPE=submit VALUE="Edit HTML"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>

~;

print "Content-type: text/html\n\n";
print "$tag";

}
##################################################################################

sub guild_edit_html_b {


$templet = "$INPUT{'templet'}";

$tag = qq~ $tag
<HTML><HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function displayHTML(form) {
var inf = form.content.value;
win = window.open(", ", 'popup', 'toolbar = no, status = no');
win.document.write("" + inf + "");
}
//  End -->
</script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceChars(entry) {
out = ";"; // replace this
add = "IXIXIXIXI"; // with this
temp = "" + entry; // temporary holder

while (temp.indexOf(out)>-1) {
pos= temp.indexOf(out);
temp = "" + (temp.substring(0, pos) + add + 
temp.substring((pos + out.length), temp.length));
}
document.subform.content.value = temp;

}
//  End -->
</script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceCharsB(entry) {
out = "TATATAT"; // replace this
add = "TEXTAREA"; // with this
temp = "" + entry; // temporary holder

while (temp.indexOf(out)>-1) {
pos= temp.indexOf(out);
temp = "" + (temp.substring(0, pos) + add + 
temp.substring((pos + out.length), temp.length));
}
document.subform.content.value = temp;

}
//  End -->
</script>

</HEAD>
<BODY onload="replaceCharsB(document.subform.content.value);">
<FORM ACTION="index.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class=cat>
      <TR>
	<TD><P ALIGN=Center>
	  Editing Templet "$templet"</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
	  <TEXTAREA NAME="content" ROWS="30" COLS="60">
~;


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from html";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] eq "$templet") {
$row[1] =~ s/TEXTAREA/TATATAT/gi;

$tag = "$tag $row[1]\n";
}

 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag
</TEXTAREA>
</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_html_c">
<INPUT TYPE=hidden NAME="templet" VALUE="$templet">
<input type="button" value="Preview" onclick="displayHTML(this.form)"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=submit VALUE="Save Templet" onClick="replaceChars(document.subform.content.value);"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=reset VALUE="Start Over"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
</BODY></HTML>
~;

print "Content-type: text/html\n\n";
print "$tag";

}

##################################################################################

sub guild_edit_html_c {

$templet = "$INPUT{'templet'}";
$content = "$INPUT{'content'}";

$content =~ s/'/\\'/gi;
$content =~ s/IXIXIXIXI/\\;/gi;

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="UPDATE `html` 
SET `content` = '$content' 
WHERE `name` = '$templet'"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag
Templet Saved!
<P>
<A HREF=?do=guild_edit_html class=menu>Edit Another Templet</A><BR>
<A HREF=? class=menu>Return to admin</A><BR>
~;

print "Content-type: text/html\n\n";
print "$tag";

}

##################################################################################
