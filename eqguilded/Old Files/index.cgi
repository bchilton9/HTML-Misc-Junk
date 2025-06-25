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
    if ($value eq "") { $value = "NULL"; }
    $INPUT{$name} = $value;
}

##################################################################################

# $guild{'#'}
# 1 Account Number
# 2 Guild Name
# 3 Guild Password
# 4 Guild Email
# 5 Gold Expires
# 6 Account Type
# 7 Account created
# 8 Account Creator
# 9 Server
# 10 counter image number

# $user{'#'}
# 1 First Name
# 2 SurName
# 3 Password
# 4 email
# 5 Guild
# 6 Class
# 7 Race
# 8 Level
# 9 access
# 10 rank
# 11 type
# 12 Points
# 13 Master if acct.

##################################################################################

$siteurl = "http://www.eqguilded.com";

##################################################################################

print "Content-type: text/html\n\n";

##################################################################################

if ($INPUT{'guild'} ne "") { 
    if ($INPUT{'do'} eq "edit") { &editwindow }
    elsif ($INPUT{'do'} eq "stats") { &showstats }
    elsif ($INPUT{'do'} eq "news") { &editnews }
    elsif ($INPUT{'do'} eq "updatenews") { &updatenews }
    elsif ($INPUT{'do'} eq "emailmem") { &emailmem }
    elsif ($INPUT{'do'} eq "sendemail") { &sendemail }
    elsif ($INPUT{'do'} eq "editpage") { &editpage }
    elsif ($INPUT{'do'} eq "editpagenum") { &editpagenum }
    elsif ($INPUT{'do'} eq "savepagenum") { &savepagenum }
    elsif ($INPUT{'do'} eq "page") { &page }
    elsif ($INPUT{'do'} eq "addpage") { &addpage }
    elsif ($INPUT{'do'} eq "editcontent") { &editcontent }
    elsif ($INPUT{'do'} eq "savecontent") { &savecontent }
    elsif ($INPUT{'do'} eq "editlink") { &editlink }
    elsif ($INPUT{'do'} eq "addlink") { &addlink }
    elsif ($INPUT{'do'} eq "deletelink") { &deletelink }
    elsif ($INPUT{'do'} eq "editmem") { &editmem }
    elsif ($INPUT{'do'} eq "deletemem") { &deletemem }
    elsif ($INPUT{'do'} eq "editmember") { &editmember }
    elsif ($INPUT{'do'} eq "savemember") { &savemember }
    elsif ($INPUT{'do'} eq "+") { &addpts }
    elsif ($INPUT{'do'} eq "-") { &takepts }
    elsif ($INPUT{'do'} eq "roster") { &roster }
    elsif ($INPUT{'do'} eq "editrank") { &editrank }
    elsif ($INPUT{'do'} eq "saverank") { &saverank }
    elsif ($INPUT{'do'} eq "deleterank") { &deleterank }
    elsif ($INPUT{'do'} eq "editphoto") { &editphoto }
    elsif ($INPUT{'do'} eq "gvalt") { &gvalt }
    elsif ($INPUT{'do'} eq "photos") { &photos }
    elsif ($INPUT{'do'} eq "valt") { &valt }
    elsif ($INPUT{'do'} eq "showguildb") { &showguildb }
    elsif ($INPUT{'do'} eq "editcss") { &editcss }
    elsif ($INPUT{'do'} eq "savecss") { &savecss }
    elsif ($INPUT{'do'} eq "uploadfile") { &uploadfile }
    elsif ($INPUT{'do'} eq "newalbum") { &newalbum; }
    elsif ($INPUT{'do'} eq "photopage") { &photopage; }
    elsif ($INPUT{'do'} eq "raids") { &raids; }
    elsif ($INPUT{'do'} eq "saveaddraids") { &saveaddraids; }
    elsif ($INPUT{'do'} eq "savedeleteraids") { &savedeleteraids; }
    elsif ($INPUT{'do'} eq "editraids") { &edieraids; }
    elsif ($INPUT{'do'} eq "editraidhead") { &editraidhead; }
    elsif ($INPUT{'do'} eq "saveraidhead") { &saveraidhead; }
    elsif ($INPUT{'do'} eq "Delete Item") { &deleteitem; }
    elsif ($INPUT{'do'} eq "Edit Item") { &edititem; }
    elsif ($INPUT{'do'} eq "saveedititem") { &saveedititem; }
    elsif ($INPUT{'do'} eq "additemtwo") { &additemtwo; }
    elsif ($INPUT{'do'} eq "additemthree") { &additemthree; }
    elsif ($INPUT{'do'} eq "additemfour") { &additemfour; }
    elsif ($INPUT{'do'} eq "setcounter") { &setcounter; }
    elsif ($INPUT{'do'} eq "savecounter") { &savecounter; }
    elsif ($INPUT{'do'} eq "chat") { &loadchatwin; }
    elsif ($INPUT{'do'} eq "savelinkline") { &savelinkline; }
    elsif ($INPUT{'do'} eq "changelinkline") { &changelinkline; }
    elsif ($INPUT{'do'} eq "aprove") { &aprove; }
    elsif ($INPUT{'do'} eq "decline") { &decline; }
elsif ($INPUT{'do'} eq "x") { &showguildx; }
    else { &showguild; }
}
elsif ($INPUT{'signup'} eq "NULL") { &signupform }
elsif ($INPUT{'signup'} eq "one") { &signupone }
elsif ($INPUT{'signup'} eq "emailvarafied") { &emailvarafied }
elsif ($INPUT{'signup'} eq "two") { &signuptwo }
elsif ($INPUT{'signup'} eq "three") { &signupthree }
elsif ($INPUT{'signup'} eq "four") { &signupfour }
elsif ($INPUT{'signup'} eq "five") { &signupfive }
elsif ($INPUT{'editsetting'} eq "NULL") { &editsetting }
elsif ($INPUT{'do'} eq "editinfo") { &editinfo }
elsif ($INPUT{'do'} eq "editprocss") { &editprocss }
elsif ($INPUT{'do'} eq "saveprocss") { &saveprocss }
elsif ($INPUT{'do'} eq "saveinfo") { &saveinfo }
elsif ($INPUT{'do'} eq "setguild") { &setguild }
elsif ($INPUT{'do'} eq "setguildtwo") { &setguildtwo }
elsif ($INPUT{'do'} eq "setguildthree") { &setguildthree }
elsif ($INPUT{'do'} eq "removeguild") { &removeguild }
elsif ($INPUT{'do'} eq "removeguildtwo") { &removeguildtwo }
elsif ($INPUT{'do'} eq "makeguild") { &makeguild }
elsif ($INPUT{'do'} eq "makeguildtwo") { &makeguildtwo }
elsif ($INPUT{'do'} eq "makeguildthree") { &makeguildthree }
elsif ($INPUT{'do'} eq "deleteguild") { &deleteguild }
elsif ($INPUT{'main'} eq "NULL") { &maintwo }
elsif ($INPUT{'do'} eq "view") { &viewmember }
elsif ($INPUT{'do'} eq "sendmsg") { &sendmsg }
elsif ($INPUT{'do'} eq "sendmsgtwo") { &sendmsgtwo }
elsif ($INPUT{'do'} eq "messages") { &messages }
elsif ($INPUT{'do'} eq "viewmessage") { &viewmessage }
elsif ($INPUT{'do'} eq "deletemessage") { &deletemessage }
elsif ($INPUT{'do'} eq "resettopfive") { &resettopfive }
elsif ($INPUT{'do'} eq "viewitem") { &viewitem; }
elsif ($INPUT{'do'} eq "mainx") { &mainx; }
else { &main; }


##################################################################################

sub main {
print <<"HTML";
<CENTER>
<B>EQ GUILDED will be down for the next few days for software upgrade's
HTML
}

sub mainx {

print <<"HTML";
<HTML>
<HEAD>
<Meta name="Author" content="Byron Chilton">
<Meta name="Publisher" content="Byron Chilton">
<Meta name="Copyright" content="COPYRIGHT 2003 ALL RIGHTS RESERVED EQGUILDED.COM ">
<Meta name="Revisit-After" content="5 days">
<Meta HTTP-EQUIV="Expires" content="none">
<Meta name="Keywords" content="everquest, eq, rpg, game, mmorpg, online, database, verant, sony, map, maps, item, items, quest, quests, landmark, landmarks, bestiary, zone, loc, location, screenshot, screenshots, 3dfx, tnt, dungeons, towns, norrath, guild, guilds">
<Meta name="Description" content="An Everquest website for seting up websites got your guild. Includeing a full roster, profiles, points, photo albums, vaults, and much more!">
<Meta name="Pagetopic" content="Internet">
<Meta name="Audience" content=" All">
<Meta name="Robots" content="all">
<Meta name="Content-Language" content="English"> 
<TITLE>EQ Guilded.com</TITLE>
</HEAD>


<script language="javascript">
document.write('<FRAMESET ROWS=100%>');
document.write('<FRAME NAME=main SRC=$siteurl/?main>');
document.write('</FRAMESET>');
</script>
<noscript> 
<BODY>
<CENTER><B>You must have JavaScript Enabeled on your system to view the website EQ Guilded.com!!
</BODY>
</noscript> 
</HTML>

HTML
}

##################################################################################

sub maintwo {
&getuser;

print <<"HTML";
<HTML>
<HEAD>
<Meta name="Author" content="Byron Chilton">
<Meta name="Publisher" content="Byron Chilton">
<Meta name="Copyright" content="COPYRIGHT 2003 ALL RIGHTS RESERVED EQGUILDED.COM ">
<Meta name="Revisit-After" content="5 days">
<Meta HTTP-EQUIV="Expires" content="none">
<Meta name="Keywords" content="everquest, eq, rpg, game, mmorpg, online, database, verant, sony, map, maps, item, items, quest, quests, landmark, landmarks, bestiary, zone, loc, location, screenshot, screenshots, 3dfx, tnt, dungeons, towns, norrath, guild, guilds">
<Meta name="Description" content="An Everquest website for seting up websites got your guild. Includeing a full roster, profiles, points, photo albums, vaults, and much more!">
<Meta name="Pagetopic" content="Internet">
<Meta name="Audience" content=" All">
<Meta name="Robots" content="all">
<Meta name="Content-Language" content="English"> 
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded.com</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%">
  <TR>
    <TD width="40%"><IMG SRC="images/logo.jpeg"></TD>
    <TD WIDTH="60%" VALIGN="Top"><P align="right">
HTML

if ($user eq "") {
print <<"HTML";
<B>You are not loged in</B><BR>
HTML
}
else {
$i = 0;
open (DATA, "user/$user.msg");
@data = <DATA>;
close DATA;
foreach $lineee (@data) {
$i = $i + 1;
}
print <<"HTML";
      <B>Loged in as $user{'1'} $user{'2'}</B><BR>
      <A HREF="$siteurl/?do=messages"onclick="NewWindow(this.href,'name','410','300','yes');return false;"><B><FONT COLOR=#000000>Message Center
      (0)</font></B></A>
HTML
}




print <<"HTML";
</TD>
    <TD width="1%" ><IMG SRC="images/leftcorn.jpg" WIDTH="18" HEIGHT="23"></TD>
  </TR>
</TABLE>
<TABLE border="0" width="100%" cellspacing="0" cellpadding="0" background="images/topline.jpg">
  <TR>
    <TD width="100%">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
      <FONT color="#FFFFFF" face="Arial" size="2"><B>www.EQGuilded.com</B></FONT></TD>
  </TR>
</TABLE>
<TABLE border="0" width="100%" bgcolor="#000000" cellspacing="0" cellpadding="0">
  <TR>
    <TD width="100%"><IMG BORDER="0" WIDTH="420" HEIGHT="53" SRC="images/mainphoto.jpeg"></TD>
  </TR>
</TABLE>
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%">
  <TR>
    <TD width="1%" valign="top"><BR>
      <P>
      <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR>
	  <TD><IMG SRC="images/sidetopleft.jpg"></TD>
	</TR>
	<TR>
	  <TD BGCOLOR=#000000><P ALIGN=Center>
	    <FONT COLOR="#ffffff"><SMALL><SMALL><SMALL>(By
	    Members)</SMALL></SMALL></SMALL><BR>
</FONT>
<Center>
HTML

open (DATA, "tenmem.dat");
@data = <DATA>;
close DATA;
print "@data";

print <<"HTML";
</TD>
	</TR>
	<TR>
	  <TD><IMG SRC="images/sidebottomleft.jpg"></TD>
	</TR>
      </TABLE>
      <P>
      <BR>
      <P>
      <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR>
	  <TD><IMG SRC="images/sidetopleft.jpg"></TD>
	</TR>
	<TR>
	  <TD BGCOLOR=#000000><P ALIGN=Center>
	    <FONT COLOR="#ffffff"><SMALL><SMALL><SMALL>(By
	    Visits)</SMALL></SMALL></SMALL><BR>
</FONT>
<Center>
HTML

open (DATA, "tenvit.dat");
@data = <DATA>;
close DATA;
print "@data";

print <<"HTML";
</TD>
	</TR>
	<TR>
	  <TD><IMG SRC="images/sidebottomleft.jpg"></TD>
	</TR>
      </TABLE>
    </TD>
    <TD><IMG SRC="images/leftcorn.jpg" WIDTH="18" HEIGHT="23"></TD>
    <TD width="97%" valign="top"><P style="margin-left: 30">
<P>
<BR>
HTML

open (DATA, "news.dat");
@data = <DATA>;
close DATA;
print "@data";

print <<"HTML";
</TD>
    <TD width="1%" valign="top"><P align="right">
      <IMG border="0" width="18" height="23" SRC="images/rightcorn.jpg"></TD>
    <TD width="1%" valign="top"><P align="right">
      <IMG border="0" width="130" height="37" SRC="images/side.jpg"><BR>
HTML
if ($user eq "") {
print <<"HTML";
      <A HREF="$siteurl/log.cgi" onclick="NewWindow(this.href,'name','300','150','no');return false;"><IMG SRC="images/login.jpg" BORDER="0"></A><BR>
      <A HREF="$siteurl/?signup"onclick="NewWindow(this.href,'name','400','300','yes');return false;"><IMG SRC="images/signup.jpg" BORDER="0"></A><BR>
HTML
}
else {
print <<"HTML";
      <A HREF="$siteurl/log.cgi?logout" onclick="NewWindow(this.href,'name','10','10','yes');return false;"><IMG SRC="images/logout.jpg" BORDER="0"></A><BR>
      <A HREF="$siteurl/?editsetting&guildname=$user{'5'}" onclick="NewWindow(this.href,'name','410','300','yes');return false;"><IMG SRC="images/edit.jpg" BORDER="0"></A><BR>
HTML
}
print <<"HTML";
<IMG SRC="images/guildlist.jpg" BORDER="0"><BR>

<A HREF="$siteurl/help.html" onclick="NewWindow(this.href,'name','600','400','yes');return false;"><IMG SRC="images/help.jpg" BORDER="0"></A><BR>
      <IMG border="0" width="130" height="24" SRC="images/sidebottom.jpg"></TD>
  </TR>
</TABLE>
<TABLE border="0" width="100%" cellspacing="0" cellpadding="0" background="images/topline.jpg">
  <TR>
    <TD width="100%"><FONT size="2">&nbsp;</FONT></TD>
  </TR>
</TABLE>
<CENTER>
      <FONT face="Arial" size="1">&copy; COPYRIGHT 2003 ALL RIGHTS RESERVED
      EQGUILDED.COM</FONT>
</BODY></HTML>
HTML

&gettime;

}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub viewmember {
&getuser;

$i = 0;
open (DATA, "user/$INPUT{'name'}.dat");
@data = <DATA>;
close DATA;
foreach $lineee (@data) {
$i = $i + 1;
$usera{$i} = "$lineee";
}

# 1 First Name
# 2 SurName
# 3 Password
# 4 email
# 5 Guild
# 6 Class
# 7 Race
# 8 Level
# 9 access (guild only)
# 10 rank (guild only)
# 11 type (guild only)
# 12 Points (guild only)
# 13 Master if acct. (guild only)

print <<"HTML";
<HTML>
<HEAD>
<STYLE>
HTML

open (DATA, "user/$INPUT{'name'}.css");
@data = <DATA>;
close DATA;
$output = "@data";
$output =~ s/!X!/;/gi;
print "$output";

print <<"HTML";
</STYLE>
<title>$usera{'1'} $usera{'2'}'s Profile</title>
</HEAD>
<BODY id=body  BACKGROUND="">
<div id=wraper>

<DIV ID=name>$usera{'1'} $usera{'2'}</DIV>
<DIV ID=lvlclassrace>$usera{'8'} $usera{'7'} $usera{'6'}</DIV>
HTML

if ($user{'1'} ne "") {
print "<DIV id=sendmsg><A HREF=$siteurl/?do=sendmsg&to=$INPUT{'name'} id=link>Send Message</A></DIV>";
}

print <<"HTML";
<DIV id=other1></DIV>
<DIV id=other2></DIV>
<DIV id=other3></DIV>
<DIV id=other4></DIV>
<DIV id=other5></DIV>
<DIV id=other6></DIV>
</div>
</BODY>
</Html>
HTML
}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub sendmsg {
print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><B>To:</TD>
	<TD>
<INPUT TYPE=text NAME=to VALUE="$INPUT{'to'}" onChange="javascript:this.value=this.value.toLowerCase();"> <A HREF="http://www.eqguilded.com/help.cgi?num=1" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A>
</TD>
      </TR>
      <TR>
	<TD><B>Subject:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="subject"> <A HREF="http://www.eqguilded.com/help.cgi?num=2" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><B>Message:</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><TEXTAREA NAME="message" COLS="30" rows=8></TEXTAREA> <A HREF="http://www.eqguilded.com/help.cgi?num=3" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=sendmsgtwo>
	  <INPUT TYPE=submit VALUE="Send"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub sendmsgtwo {
&getuser;
&gettime;

if ($INPUT{'subject'} eq "NULL") { $INPUT{'subject'} = ""; }

if ($INPUT{'to'} eq "NULL") { 
$tag = "You must enter somone to send the message to";
&sendmsg;
 }
elsif ($INPUT{'message'} eq "NULL") { 
$tag = "You must enter a message";
&sendmsg;
 }
else {

$good = "f";

open (DATA, "acounts.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $mail) = split(/::/, $line);

if ($name eq "$INPUT{'to'}") {
$good = "t";
} #end if
} #end foreach

if ($good eq "t") {

open (FILE, "msg.cnt");
flock (FILE, 2);
$cnt = <FILE>;
chop ($abcdefg);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$cnt++;

open(DATA, ">msg.cnt");
print DATA "$cnt\n";
print DATA "junk\n";
close DATA;


$INPUT{'message'} =~ s/\n/<BR>/gi;


open(DATA, ">msg/$cnt.msg");
print DATA "<CENTER><TABLE BORDER=0 CELLPADDING=2 ALIGN=Center WIDTH=75%>";
print DATA "<TR><TD><B>From:</B></TD><TD>$user{'1'}</TD></TR>";
print DATA "<TR><TD><B>Subject:</B></TD><TD>$INPUT{'subject'}</TD></TR>";
print DATA "<TR><TD COLSPAN=2><B>Message:</B></TD></TR>";
print DATA "<TR><TD COLSPAN=2>$INPUT{'message'}</TD></TR>";
print DATA "<TR><TD><B>Sent:</B></TD><TD>$datetime</TD></TR>";
print DATA "</TABLE></CENTER>";
print DATA "<P><CENTER>";
print DATA "<A HREF=$siteurl/?do=deletemessage&num=$cnt><IMG SRC=images/delete.jpg BORDER=0></A>";
print DATA "<A HREF=$siteurl/?do=sendmsg&to=$user{'1'}><IMG SRC=images/reply.jpg BORDER=0></A>";
print DATA "<A HREF=$siteurl/?do=messages><IMG SRC=images/msg.jpg BORDER=0></A>";
close DATA;


open (DATA, "user/$INPUT{'to'}.msg");
@data = <DATA>;
close DATA;
open(DATA, ">user/$INPUT{'to'}.msg");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$user";
print DATA "::$INPUT{'subject'}::$cnt";
print DATA "::junk\n";
close DATA;


$tag = "Your Message has been sent!<BR>";
&messages;
}
else {
$tag = "Invaled Member name in the To: field";
&sendmsg;
}

}

}

##################################################################################

sub messages {
&getuser;

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>$tag</B>
<P>
<TABLE BORDER="0" CELLPADDING="2" WIDTH="90%" BGCOLOR="#265833">
  <TR>
    <TD BGCOLOR="#008040"><P ALIGN=Center>
      <FONT COLOR="#ffffff"><B>From:</B></FONT></TD>
    <TD BGCOLOR="#008040"><P ALIGN=Center>
      <FONT COLOR="#ffffff"><B>Subject</B></FONT></TD>
    <TD BGCOLOR="#008040"><P ALIGN=Center>
      <FONT COLOR="#ffffff"><B>View</B></FONT></TD>
    <TD BGCOLOR="#008040"><P ALIGN=Center>
      <FONT COLOR="#ffffff"><B>Delete</B></FONT></TD>
  </TR>

HTML

open (DATA, "user/$user.msg");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($from, $sub, $num, $junk) = split(/::/, $line);

print "<TR><TD><FONT COLOR=#ffffff>$from</FONT></TD>";
print "<TD><FONT COLOR=#ffffff>$sub</FONT></TD>";
print "<TD><CENTER><A HREF=$siteurl/?do=viewmessage&num=$num><FONT COLOR=#ffffff>View</FONT></A></TD>";
print "<TD><CENTER><A HREF=$siteurl/?do=deletemessage&num=$num><FONT COLOR=#ffffff>Delete</FONT></A></TD></TR>";

}

print <<"HTML";
</TABLE>
<P>
<A HREF=$siteurl/?do=sendmsg id=windowlinks><IMG SRC="images/sendmsg.jpg" BORDER="0"></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub viewmessage {
open (DATA, "msg/$INPUT{'num'}.msg");
@data = <DATA>;
close DATA;

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>

@data

    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub deletemessage {
&getuser;

open (DATA, "user/$user.msg");
@data = <DATA>;
close DATA;
open (DATA, ">user/$user.msg");
foreach $line (@data) {
($from, $sub, $num, $junk) = split(/::/, $line);
if ($num eq "$INPUT{'num'}") {
print DATA "";
}
else {
print DATA "$line";
}
}
close DATA;

unlink("msg/$INPUT{'num'}.msg");


$tag = "Message Deleted";

&messages;
}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub editsetting {

if ($INPUT{'guildname'} eq "NULL") { $INPUT{'guildname'} = ""; }
$INPUT{'guild'} = "$INPUT{'guildname'}";

&getuser;

print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<A HREF=$siteurl/?do=editinfo id=windowlinks><B><FONT COLOR=#000000>Edit User Info</FONT></B></A> <A HREF="http://www.eqguilded.com/help.cgi?num=4" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A><BR>
<A HREF=$siteurl/?do=editprocss&name=$user id=windowlinks><B><FONT COLOR=#000000>Edit Profile Style Sheet</FONT></B></A><BR>
HTML


if ($user{'13'} eq "Master") {
print <<"HTML";
<A HREF=$siteurl/?do=deleteguild id=windowlinks><B><FONT COLOR=#000000>Delete $user{'5'}</FONT></B></A> <A HREF="http://www.eqguilded.com/help.cgi?num=5" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A><BR>
HTML
}
else {
if ($user{'5'} eq "\n") {
print <<"HTML";
<A HREF=$siteurl/?do=setguild id=windowlinks><B><FONT COLOR=#000000>Set Guild</FONT></B></A> <A HREF="http://www.eqguilded.com/help.cgi?num=6" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A><BR>
<A HREF=$siteurl/?do=makeguild id=windowlinks><B><FONT COLOR=#000000>Create Guild</FONT></B></A> <A HREF="http://www.eqguilded.com/help.cgi?num=7" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A><BR>
HTML
}
else {
print <<"HTML";
<A HREF=$siteurl/?do=removeguild id=windowlinks><B><FONT COLOR=#000000>Remove me from $user{'5'}</FONT></B></A> <A HREF="http://www.eqguilded.com/help.cgi?num=8" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A><BR>
HTML
}
}

print <<"HTML";
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub editprocss {

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceChars(entry) {
out = ";"; // replace this
add = "!x!"; // with this
temp = "" + entry; // temporary holder

while (temp.indexOf(out)>-1) {
pos= temp.indexOf(out);
temp = "" + (temp.substring(0, pos) + add + 
temp.substring((pos + out.length), temp.length));
}
document.subform.css.value = temp;
}
//  End -->
</script>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>


<FORM ACTION="index.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  <B>StyleScript</TD>
      </TR>
      <TR>
<TD><TEXTAREA NAME="css" COLS="30" rows=10>
HTML

open (DATA, "user/$INPUT{'name'}.css");
@data = <DATA>;
close DATA;
$output = "@data";
$output =~ s/!X!/;/gi;
print "$output";

print <<"HTML";
</TEXTAREA>
<P>
</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=saveprocss>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Save" onClick="replaceChars(document.subform.css.value);"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>

    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
&getdata;
}

##################################################################################

sub saveprocss {
&getdata;

open(DATA, ">user/$INPUT{'name'}.css");
print DATA "$INPUT{'css'}";
close DATA;

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

var page = "$siteurl/?main";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

//onload=winclose()
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload=winclose()>
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Style Sheet Updated!<BR>
<a href="#" onClick="window.close();"><B><FONT COLOR=#000000>Close</FONT></B></a>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub deleteguild {
&getuser;


if ($INPUT{'com'} eq "YES") {


open (DATA, "guilds.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $server, $junk) = split(/::/, $line);
if ($user{'5'} eq "$name\n") {
$guild = "$name";
}
}

unlink("data/$guild.dat");
unlink("style/$guild.css");
unlink("data/$guild.foot");
unlink("data/$guild.link");
unlink("data/$guild.news");
unlink("data/$guild.off");
unlink("data/$guild.photo");
unlink("data/$guild.rank");
unlink("data/$guild.valt");

open (DATA, "guilds.dat");
@data = <DATA>;
close DATA;
open(DATA, ">guilds.dat");
foreach $line (@data) {
($name, $server, $junk) = split(/::/, $line);
if ($guild eq "$name") {
print DATA "";
}
else {
print DATA "$line";
}
}
close DATA;



open (DATA, "data/$guild.mem");
@data = <DATA>;
close DATA;
open(DATA, ">data/$guild.mem");
foreach $line (@data) {
($name, $accs, $rank, $typ, $pts) = split(/::/, $line);

$i = 0;
open (DATAA, "user/$name.dat");
@dataa = <DATAA>;
close DATAA;
foreach $lineee (@dataa) {
$i = $i + 1;
$useraaaa{$i} = "$lineee";
}
open(DATAAAA, ">user/$name.dat");
print DATAAAA "$useraaaa{'1'}";
print DATAAAA "$useraaaa{'2'}";
print DATAAAA "$useraaaa{'3'}";
print DATAAAA "$useraaaa{'4'}";
print DATAAAA "\n";
print DATAAAA "$useraaaa{'6'}";
print DATAAAA "$useraaaa{'7'}";
print DATAAAA "$useraaaa{'8'}";
print DATAAAA "junk\n";
close DATAAAA;

}
close DATA;

open (DATA, "data/$guild.wate");
@data = <DATA>;
close DATA;
open(DATA, ">data/$guild.wate");
foreach $line (@data) {
($name, $junk) = split(/::/, $line);

$i = 0;
open (DATAA, "user/$name.dat");
@dataa = <DATAA>;
close DATAA;
foreach $lineee (@dataa) {
$i = $i + 1;
$useraaaa{$i} = "$lineee";
}
open(DATAAAA, ">user/$name.dat");
print DATAAAA "$useraaaa{'1'}";
print DATAAAA "$useraaaa{'2'}";
print DATAAAA "$useraaaa{'3'}";
print DATAAAA "$useraaaa{'4'}";
print DATAAAA "\n";
print DATAAAA "$useraaaa{'6'}";
print DATAAAA "$useraaaa{'7'}";
print DATAAAA "$useraaaa{'8'}";
print DATAAAA "junk\n";
close DATAAAA;

}
close DATA;

open (DATA, "data/$guild.page");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $num, $junk) = split(/::/, $line);
unlink("pages/$num.page");
}


unlink("data/$guild.page");
unlink("data/$guild.mem");
unlink("data/$guild.wate");

#################################################
print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

var page = "$siteurl/?main";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

//onload=winclose()
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload=winclose()>
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Guild Deleted<BR>
<a href="#" onClick="window.close();"><B><FONT COLOR=#000000>Close</FONT></B></a>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}
else {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Are you sure you want to delete<BR>
your guild and all of its files?<BR>
<A HREF=$siteurl/?do=deleteguild&com=YES><B><FONT COLOR=#000000>YES</FONT></B></A> <A HREF=null onclick=javascript:top.window.close();><B><FONT COLOR=#000000>NO</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub makeguild {
&getuser;

print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
<script language="JavaScript" src="validation.js"></script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function init() {
define('sname', 'string', 'Short Name');
}
//  End -->
</script>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function ignoreSpaces(string) {
var temp = "";
string = '' + string;
splitstring = string.split(" ");
for(i = 0; i < splitstring.length; i++)
temp += splitstring[i];
return temp;
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" OnLoad="init()">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<FORM ACTION="index.cgi" METHOD="POST">
<CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><B>Guild Short Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="sname" VALUE="" onChange="javascript:this.value=this.value.toLowerCase();" onBlur="this.value=ignoreSpaces(this.value);"> <A HREF="http://www.eqguilded.com/help.cgi?num=9" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=makeguildtwo>
	  <INPUT TYPE=submit VALUE="Next &gt;" onClick="validate();return returnVal;"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub makeguildtwo {

$INPUT{'sname'} =~ s/ /_/gi;
$sname = "$INPUT{'sname'}";

open (DATA, "guilds.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $server, $junk) = split(/::/, $line);
if ($name eq "$INPUT{'sname'}") {
print <<"HTML";
<HTML>
<HEAD>
<script language="JavaScript" src="validation.js"></script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function init() {
define('sname', 'string', 'Short Name');
}
//  End -->
</script>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function ignoreSpaces(string) {
var temp = "";
string = '' + string;
splitstring = string.split(" ");
for(i = 0; i < splitstring.length; i++)
temp += splitstring[i];
return temp;
}
//  End -->
</script>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" OnLoad="init()">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Short guild name taken!
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><B>Guild Short Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="sname" onChange="javascript:this.value=this.value.toLowerCase();" onBlur="this.value=ignoreSpaces(this.value);"> <A HREF="http://www.eqguilded.com/help.cgi?num=9" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=do VALUE=makeguildtwo>
	  <INPUT TYPE=submit VALUE="Next &gt;" onClick="validate();return returnVal;"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
exit;
}
}

if ($INPUT{'gname'} eq "NULL") {
$INPUT{'gname'} = "";
}
if ($INPUT{'email'} eq "NULL") {
$INPUT{'email'} = "";
}

print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
<script language="JavaScript" src="validation.js"></script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function init() {
define('gname', 'string', 'Guild Name');
define('email', 'email', 'E-Mail');
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" OnLoad="init()">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>

<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><B>Guild Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="gname" VALUE=$INPUT{'gname'}> <A HREF="http://www.eqguilded.com/help.cgi?num=10" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <!-- TR>
	<TD><P ALIGN=Left>
	  <B>Guild Password:</TD>
	<TD>
	  <INPUT TYPE="password" NAME="pass1" onChange="javascript:this.value=this.value.toLowerCase();"> <A HREF="http://www.eqguilded.com/help.cgi?num=11" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <TR>
	<TD><B>Re-Type:</TD>
	<TD>
	  <INPUT TYPE="password" NAME="pass2" onChange="javascript:this.value=this.value.toLowerCase();"></TD>
      </TR -->
      <TR>
	<TD><B>Guild E-Mail:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="email" VALUE=$INPUT{'email'}> <A HREF="http://www.eqguilded.com/help.cgi?num=12" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <TR>
	<TD><B>Server:</TD>
	<TD>
	    <SELECT NAME="server">
  <OPTION>Antonius Bayle
  <OPTION>Ayonae Ro
  <OPTION>Bertoxxulous
  <OPTION>Brell Serilis
  <OPTION>Bristlebane
  <OPTION>Cazic-Thule
  <OPTION>Drinal
  <OPTION>Druzzil Ro
  <OPTION>E'ci
  <OPTION>Erollisi Marr
  <OPTION>Fennin Ro
  <OPTION>Firiona Vie
  <OPTION>Innoruuk
  <OPTION>Kael Drakkal
  <OPTION>Kane Bayle
  <OPTION>Karana
  <OPTION>Lanys T'Vyl
  <OPTION>Luclin
  <OPTION>Maelin Starpyre
  <OPTION>Mithaniel Marr
  <OPTION>Morell-Thule
  <OPTION>Povar
  <OPTION>Prexus
  <OPTION>Quellious
  <OPTION>Rallos Zek
  <OPTION>Rodcet Nife
  <OPTION>Saryrn
  <OPTION>Sebilis
  <OPTION>Solusek Ro
  <OPTION>Stormhammer
  <OPTION>Sullon Zek
  <OPTION>Tallon Zek
  <OPTION>Threw Marr
  <OPTION>Terris-Thule
  <OPTION>The Nameless
  <OPTION>The Rathe
  <OPTION>The seventh Hammer
  <OPTION>The Tribunal
  <OPTION>Tholuxe Paells
  <OPTION>Torvonnilous
  <OPTION>Tunare
  <OPTION>Vallon Zek
  <OPTION>Vazaelle
  <OPTION>Veeshan
  <OPTION>Venril Sathir
  <OPTION>Xegony
  <OPTION>Xev
</SELECT> <A HREF="http://www.eqguilded.com/help.cgi?num=13" onclick="NewWindow(this.href,'help','250','400','yes');return false;"><IMG SRC="images/help.gif" BORDER="0"></A></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=sname VALUE=$INPUT{'sname'}>
<INPUT TYPE=hidden NAME=do VALUE=makeguildthree>
	  <INPUT TYPE=submit VALUE="Next &gt;" onClick="validate();return returnVal;"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################

sub makeguildthree {

&gettime;

&getuser;

open (FILE, "guilds.cnt");
flock (FILE, 2);
$cnt = <FILE>;
chop ($abcdefg);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$cnt++;

open(DATA, ">guilds.cnt");
print DATA "$cnt\n";
print DATA "junk\n";
close DATA;

open(DATA, ">user/$user.dat");
print DATA "$user{'1'}";
print DATA "$user{'2'}";
print DATA "$user{'3'}";
print DATA "$user{'4'}";
print DATA "$INPUT{'sname'}\n";
print DATA "$user{'6'}";
print DATA "$user{'7'}";
print DATA "$user{'8'}";
print DATA "junk\n";
close DATA;

open(DATA, ">data/$INPUT{'sname'}.dat");
print DATA "$cnt\n";
print DATA "$INPUT{'gname'}\n";
print DATA "$INPUT{'pass1'}\n";
print DATA "$INPUT{'email'}\n";
print DATA "1/1/2222\n";
print DATA "gold\n";
print DATA "$date\n";
print DATA "$user\n";
print DATA "$INPUT{'server'}\n";
print DATA "1\n";
print DATA "junk\n";
close DATA;

open (DATA, "defalt.css");
@data = <DATA>;
close DATA;
open(DATA, ">style/$INPUT{'sname'}.css");
print DATA "@data\n";
close DATA;
open (DATA, "defalt.cont");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'sname'}.foot");
print DATA "@data\n";
close DATA;

open(DATA, ">data/$INPUT{'sname'}.link");
print DATA "Home::$siteurl/?guild=$INPUT{'sname'}::1\n";
print DATA "Roster::$siteurl/?guild=$INPUT{'sname'}&do=roster::1\n";
print DATA "Photo Album::$siteurl/?guild=$INPUT{'sname'}&do=photos::1\n";
print DATA "Vault::$siteurl/?guild=$INPUT{'sname'}&do=valt::1\n";
print DATA "Raids::$siteurl/?guild=$INPUT{'sname'}&do=raids::1\n";
print DATA "Chat::$siteurl/?guild=$INPUT{'sname'}&do=chat::1\n";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.mem");
print DATA "$Cookies{'user'}::Master::Guild-Leader::Officer::0\n";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.news");
print DATA "Member News window\n";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.off");
print DATA "Officer News Window\n";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.page");
print DATA "";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.photo");
print DATA "";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.rank");
print DATA "Guild-Leader&1\n";
print DATA "Assistant-Guild-Leader&1\n";
print DATA "Officer's&3\n";
print DATA "Officer&1\n";
print DATA "Member's&3\n";
print DATA "Member&1\n";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.valt");
print DATA "";
close DATA;
open(DATA, ">data/$INPUT{'sname'}.wate");
print DATA "";
close DATA;

open (DATA, "guilds.dat");
@data = <DATA>;
close DATA;
open(DATA, ">guilds.dat");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'sname'}::$INPUT{'server'}::guild\n";
close DATA;

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

var page = "$siteurl/?main";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

//onload=winclose()
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload=winclose()>
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Your Guild has been Created<BR>
The URL to your guild's website is:<BR>
<A HREF=$siteurl/?guild=$INPUT{'sname'} TARGET=_new >$siteurl/?guild=$INPUT{'sname'}</A><BR>
<a href="#" onClick="window.close();"><B><FONT COLOR=#000000>Close</FONT></B></a>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################
##################################################################################
##################################################################################
##################################################################################

# stoped the help here

##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub removeguild {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Are you sure you want to be removed from your guild?<BR>
<A HREF=$siteurl/?do=removeguildtwo id=windowlinks><B><FONT COLOR=#000000>Yes</FONT></B></A> <A HREF=javascript:top.window.close(); id=windowlinks><B><FONT COLOR=#000000>No</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub removeguildtwo {
&getuser;

open(DATA, ">user/$user.dat");
print DATA "$user{'1'}";
print DATA "$user{'2'}";
print DATA "$user{'3'}";
print DATA "$user{'4'}";
print DATA "\n";
print DATA "$user{'6'}";
print DATA "$user{'7'}";
print DATA "$user{'8'}";
print DATA "junk\n";
close DATA;

($gname, $junk) = split(/\n/, $user{'5'});

open (DATA, "data/$gname.mem");
@data = <DATA>;
close DATA;

open(DATA, ">data/$gname.mem");
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
if ($name eq "$user") {
print DATA "";
}
else {
print DATA "$line";
}
}
close DATA;

open (DATA, "data/$gname.wate");
@data = <DATA>;
close DATA;

open(DATA, ">data/$gname.wate");
foreach $line (@data) {
($name, $junk) = split(/::/, $line);
if ($name eq "$user") {
print DATA "";
}
else {
print DATA "$line";
}
}
close DATA;

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

var page = "$siteurl/?main";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

top.window.close();

//onload=winclose()
}
//  End -->
</script>
</HEAD>
<BODY onload="winclose()">
</BODY>
</HTML>
HTML
}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub setguild {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Chose a server<BR>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>
	  <SELECT NAME="server">
  <OPTION>Antonius Bayle
  <OPTION>Ayonae Ro
  <OPTION>Bertoxxulous
  <OPTION>Brell Serilis
  <OPTION>Bristlebane
  <OPTION>Cazic-Thule
  <OPTION>Drinal
  <OPTION>Druzzil Ro
  <OPTION>E'ci
  <OPTION>Erollisi Marr
  <OPTION>Fennin Ro
  <OPTION>Firiona Vie
  <OPTION>Innoruuk
  <OPTION>Kael Drakkal
  <OPTION>Kane Bayle
  <OPTION>Karana
  <OPTION>Lanys T'Vyl
  <OPTION>Luclin
  <OPTION>Maelin Starpyre
  <OPTION>Mithaniel Marr
  <OPTION>Morell-Thule
  <OPTION>Povar
  <OPTION>Prexus
  <OPTION>Quellious
  <OPTION>Rallos Zek
  <OPTION>Rodcet Nife
  <OPTION>Saryrn
  <OPTION>Sebilis
  <OPTION>Solusek Ro
  <OPTION>Stormhammer
  <OPTION>Sullon Zek
  <OPTION>Tallon Zek
  <OPTION>Threw Marr
  <OPTION>Terris-Thule
  <OPTION>The Nameless
  <OPTION>The Rathe
  <OPTION>The seventh Hammer
  <OPTION>The Tribunal
  <OPTION>Tholuxe Paells
  <OPTION>Torvonnilous
  <OPTION>Tunare
  <OPTION>Vallon Zek
  <OPTION>Vazaelle
  <OPTION>Veeshan
  <OPTION>Venril Sathir
  <OPTION>Xegony
  <OPTION>Xev
</SELECT></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=setguildtwo>
	  <INPUT TYPE=submit VALUE="Next &gt;"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub setguildtwo {

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>
	  <SELECT NAME="setguild">
HTML

open (DATA, "guilds.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $server, $junk) = split(/::/, $line);
if ($server eq "$INPUT{'server'}") {

$i = 0;
open (DATAa, "data/$name.dat");
@dataa = <DATAa>;
close DATAa;
foreach $linea (@dataa) {
$i = $i + 1;
$guild{$i} = "$linea";
}

print "<OPTION>$guild{'2'} _$name\n";
}
}

print <<"HTML";
</SELECT></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=setguildthree>
	  <INPUT TYPE=submit VALUE="Next &gt;"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################

sub setguildthree {
&getuser;

($longname, $name) = split(/_/, $INPUT{'setguild'});


open(DATA, ">user/$user.dat");
print DATA "$user{'1'}";
print DATA "$user{'2'}";
print DATA "$user{'3'}";
print DATA "$user{'4'}";
print DATA "$name\n";
print DATA "$user{'6'}";
print DATA "$user{'7'}";
print DATA "$user{'8'}";
print DATA "junk\n";
close DATA;


open (DATA, "data/$name.wate");
@data = <DATA>;
close DATA;

open(DATA, ">data/$name.wate");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$user";
print DATA "::junk\n";
close DATA;

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

var page = "$siteurl/?main";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

top.window.close();

//onload=winclose()
}
//  End -->
</script>
</HEAD>
<BODY onload="winclose()">
</BODY>
</HTML>
HTML
}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub editinfo {
&getuser;

print <<"HTML";
<HTML>
<HEAD>
<script language="JavaScript" src="validation.js"></script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function init() {
define('name', 'string', 'Showname');
define('email', 'email', 'E-Mail');
}
//  End -->
</script>

  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" OnLoad="init()">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>$tag</B>
<P>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><B>LoginName:</TD>
	<TD>$user</TD>
      </TR>
      <TR>
	<TD><B>Showname:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="name" VALUE="$user{'1'}"></TD>
      </TR>
      <TR>
	<TD><B>Sur Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="sur" VALUE="$user{'2'}"></TD>
      </TR>
      <TR>
	<TD><B>Password:</TD>
	<TD>
	  <INPUT TYPE="password" NAME="pass1" onChange="javascript:this.value=this.value.toLowerCase();"></TD>
      </TR>
      <TR>
	<TD><B>Re-Type:</TD>
	<TD>
	  <INPUT TYPE="password" NAME="pass2" onChange="javascript:this.value=this.value.toLowerCase();"></TD>
      </TR>
      <TR>
	<TD><B>E-Mail:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="email" VALUE="$user{'4'}"></TD>
      </TR>
      <TR>
	<TD><B>Level:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="lvl" SIZE="3" MAXLENGTH="2" VALUE="$user{'8'}"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT type=hidden name=do value=saveinfo>
	  <INPUT TYPE=submit VALUE="Save" onClick="validate();return returnVal;"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################

sub saveinfo {
&getuser;

if ($INPUT{'lvl'} eq "NULL") {
$INPUT{'lvl'} = "";
}

if ($INPUT{'sur'} eq "NULL") {
$INPUT{'sur'} = "";
}

if ($INPUT{'pass1'} ne "NULL") {
  if ($INPUT{'pass1'} ne "$INPUT{'pass2'}") {
      $tag = "passwords did not match<BR>";
      &editinfo;
      exit;
  }
  elsif ($INPUT{'pass1'} eq "$INPUT{'pass2'}") {
     $pass = "$INPUT{'pass1'}\n";
  }
}

if ($pass eq "") {
$pass = "$user{'3'}";
}


open(DATA, ">user/$user.dat");
print DATA "$INPUT{'name'}\n";
print DATA "$INPUT{'sur'}\n";
print DATA "$pass";
print DATA "$INPUT{'email'}\n";
print DATA "$user{'5'}";
print DATA "$user{'6'}";
print DATA "$user{'7'}";
print DATA "$INPUT{'lvl'}\n";
print DATA "junk\n";
close DATA;

print <<"HTML";
<HTML>
<HEAD>
</HEAD>
<BODY onload="top.window.close();">
</BODY>
</HTML>
HTML

}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub signupform {
print <<"HTML";
<HTML>
<HEAD>

<script language="JavaScript" src="validation.js"></script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function init() {
define('user', 'string', 'Username');
define('email', 'email', 'E-Mail');
}
//  End -->
</script>

<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function ignoreSpaces(string) {
var temp = "";
string = '' + string;
splitstring = string.split(" ");
for(i = 0; i < splitstring.length; i++)
temp += splitstring[i];
return temp;
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" OnLoad="init()">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Right>
	  <B>User Name:</B></TD>
	<TD>
	  <INPUT TYPE="text" NAME="user" onChange="javascript:this.value=this.value.toLowerCase();" onBlur="this.value=ignoreSpaces(this.value);"></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>
	  <B>Valid E-Mail Address:</B></TD>
	<TD>
	  <INPUT TYPE="text" NAME="email"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="signup" VALUE="one">
	  <INPUT TYPE=submit VALUE="Next..." onClick="validate();return returnVal;"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub signupone {

$taken = "f";

open (DATA, "acounts.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $mail) = split(/::/, $line);

if ($name eq "$INPUT{'user'}") {
$taken = "t";
} #end if
} #end foreach

if ($taken eq "f") {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>An email has been sent to you.<BR>
Please check your email then click on the link to go to the next step.</B>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $INPUT{'email'}\n";
print MAIL "Reply-to: EQ Guilded <Webmaster\@eqguilded.com>\n";
print MAIL "From: EQ Guilded <Webmaster\@eqguilded.com>\n";
print MAIL "Subject: EQ Guilded Regastration E-Mail\n\n";
print MAIL "Welcome to EQ Guilded\n";
print MAIL "\n";
print MAIL "Please click on the link below to finish registering your acount.\n";
print MAIL "(You may have to copy and past the link in your brouser window)\n";
print MAIL "\n";
print MAIL "$siteurl/?signup=emailvarafied&user=$INPUT{'user'}&email=$INPUT{'email'}\n";
print MAIL "\n";
print MAIL "Thank you.\n";
print MAIL "EQ Guilded.\n";
print MAIL "Webmaster\@eqguilded.com\n";
print MAIL "www.EQGuilded.com\n";
}

else {
print <<"HTML";
<HTML>
<HEAD>
<script language="JavaScript" src="validation.js"></script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function init() {
define('user', 'string', 'Username');
}
//  End -->
</script>

<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function ignoreSpaces(string) {
var temp = "";
string = '' + string;
splitstring = string.split(" ");
for(i = 0; i < splitstring.length; i++)
temp += splitstring[i];
return temp;
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" OnLoad="init()">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>User Name Taken.<BR>
Please try another.</B>
<P>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Right>
	  <B>User Name:</B></TD>
	<TD>
	  <INPUT TYPE="text" NAME="user" onChange="javascript:this.value=this.value.toLowerCase();" onBlur="this.value=ignoreSpaces(this.value);"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="email" VALUE="$INPUT{'email'}">
	  <INPUT TYPE="hidden" NAME="signup" VALUE="one">
	  <INPUT TYPE=submit VALUE="Next..." onClick="validate();return returnVal;"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

}

##################################################################################

sub editoutemailvarafied {

print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}

//  End -->
</SCRIPT>
</HEAD>
<BODY onload="NewWindow('$siteurl/?signup=two&user=$INPUT{'user'}&email=$INPUT{'email'}','name','400','300','yes');top.window.close();">
</BODY>
</HTML>
HTML

}

##################################################################################

sub emailvarafied { #signuptwo {
open (DATA, "acounts.dat");
@data = <DATA>;
close DATA;
open(DATA, ">acounts.dat");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'user'}::$INPUT{'email'}\n";
close DATA;

print <<"HTML";
<HTML>
<HEAD>
<script language="JavaScript" src="validation.js"></script>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function init() {
define('name', 'string', 'Show Name');
define('pass', 'string', 'Password One', 6);
define('pass2', 'string', 'Password Two', 6);
}
//  End -->
</script>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function ignoreSpaces(string) {
var temp = "";
string = '' + string;
splitstring = string.split(" ");
for(i = 0; i < splitstring.length; i++)
temp += splitstring[i];
return temp;
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" OnLoad="init()">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST">
            	    <CENTER>
            	      <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
            		<TR>
            		  <TD><B>EQ Show Name:</TD>
            		  <TD>
            		    <INPUT TYPE="text" NAME="name"></TD>
            		</TR>
            		<TR>
            		  <TD><B>Password:</TD>
            		  <TD>
            		    <INPUT TYPE="password" NAME="pass"  onChange="javascript:this.value=this.value.toLowerCase();" onBlur="this.value=ignoreSpaces(this.value);"></TD>
            		</TR>
            		<TR>
            		  <TD><B>ReType Password:</TD>
            		  <TD>
            		    <INPUT TYPE="password" NAME="pass2"  onChange="javascript:this.value=this.value.toLowerCase();" onBlur="this.value=ignoreSpaces(this.value);"></TD>
            		</TR>
            		<TR>
            		<TR>
            		  <TD><B>Class:</TD>
            		  <TD>
            		    <SELECT NAME="class"> 
            		    <OPTION SELECTED>Bard 
            		    <OPTION>Cleric 
            		    <OPTION>Druid 
            		    <OPTION>Wizard 
            		    <OPTION>Enchanter 
            		    <OPTION>Magician 
            		    <OPTION>Monk 
            		    <OPTION>Necromancer 
            		    <OPTION>Paladin 
            		    <OPTION>Ranger 
            		    <OPTION>Roug 
            		    <OPTION>ShadowKnight 
            		    <OPTION>Shaman 
            		    <OPTION>Warrior
            		    <OPTION>Beastlord</SELECT></TD>
            		</TR>
            		<TR>
            		  <TD><B>Race:</TD>
            		  <TD>
            		    <SELECT NAME="race"> 
            		    <OPTION SELECTED>Barbarian 
            		    <OPTION>Dark_Elf 
            		    <OPTION>Dwarf 
            		    <OPTION>Erudite 
            		    <OPTION>Gnome 
            		    <OPTION>Half_Elf 
            		    <OPTION>Halfling 
            		    <OPTION>High_Elf 
            		    <OPTION>Human 
            		    <OPTION>Iskar 
            		    <OPTION>Orge 
            		    <OPTION>Troll 
            		    <OPTION>Wood_Elf
            		    <OPTION>Vah_Shir
            		    <OPTION>Frog</SELECT></TD>
            		</TR>
            		<TR>
            		  <TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE="hidden" NAME="email" value="$INPUT{'email'}">
<INPUT TYPE="hidden" NAME="user" value="$INPUT{'user'}">
            		    <INPUT TYPE=hidden value="three" name="signup">
            		    <INPUT TYPE=submit value="Next..." onClick="validate();return returnVal;"></TD>
            		</TR>
            	      </TABLE>
            	    </CENTER>
            	  </FORM>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub signupthree {
$con = "0";
$val = "0";

$name = $INPUT{'name'};
$pass = $INPUT{'pass'};
$pass2 = $INPUT{'pass2'};
$race = $INPUT{'race'};
$class = $INPUT{'class'};

if ($pass ne "$pass2") { 
print "Your Passwords did not match.<BR>";
$con = "1";
}
if ($con eq "1") {
&signuptwo;
}

if ($con eq "0") {

open (DATA, "user/$INPUT{'user'}.dat");
@data = <DATA>;
close DATA;
open(DATA, ">user/$INPUT{'user'}.dat");

print DATA "$INPUT{'name'}\n";
print DATA "\n";
print DATA "$INPUT{'pass'}\n";
print DATA "$INPUT{'email'}\n";
print DATA "\n";
print DATA "$INPUT{'class'}\n";
print DATA "$INPUT{'race'}\n";
print DATA "\n";
print DATA "junk\n";

close DATA;

open (DATA, "user/defalt.css");
@data = <DATA>;
close DATA;
open(DATA, ">user/$INPUT{'user'}.css");
print DATA "@data\n";
close DATA;


print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Thank you $INPUT{'name'}<BR>
You are now registered</B><BR>
You still need to setup your guild<BR>
To set the guild you need to log into the main page and click on the edit settings link.<BR>
In the edit settings you can setup your profile, create a guild, or set the guild that you are in!<BR>
<a href="http://www.eqguilded.com"><B><FONT COLOR=#000000>Go back to EQ Guilded</FONT></B></a>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML


}


}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub showguild {
print <<"HTML";
<CENTER>
<B>EQ GUILDED will be down for the next few days for software upgrade's
HTML
}

sub showguildx {
&getdata;
&gettime;
&checkgold;

print <<"HTML";

<TITLE>$guild{'2'}</TITLE>

<script language="javascript">

document.write('<FRAMESET ROWS=100%>');
document.write('<FRAME NAME=main SRC=$siteurl/?guild=$INPUT{'guild'}&do=showguildb>');
document.write('</FRAMESET>');

</script>
<noscript> 

<CENTER><B>You must have JavaScript Enabeled on your system to view the website for $guild{'2'}!!

</noscript> 
HTML

}

##################################################################################

sub showguildb {
&getuser;
&getdata;
&header;
&banner;


print <<"HTML";
<HTML>
<HEAD>
HTML
if ($guild{'6'} eq "Gold\n") {

open (DATA, "style/$INPUT{'guild'}.css");
@data = <DATA>;
close DATA;
$output = "@data";
$output =~ s/!X!/;/gi;
print "$output";
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}

print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body>
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD>$logbox</TD>
</TR>
</TABLE>

</DIV>
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML
&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
HTML

&footer;

print <<"HTML";
</DIV>
<P>
<div id="news">
<DIV id=newsname>$guild{'2'} News.</div>
<TEXTAREA id=newstext>
HTML
&showmemnews;
print <<"HTML";
</textarea>
</div>
<P>
<div id=counter><IMG SRC=http://www.eqguilded.com/counter.cgi?guild=$INPUT{'guild'}&i=$guild{'10'}></DIV>
<div id="admin">
HTML

if ($user{'9'} eq "Moderator") {
print "<HR id=adminhr>";
print "<TEXTAREA id=newstext>";
&showoffnews;
print "</TEXTAREA><P>";

&watelist;

print <<"HTML";
<P>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=edit&tag=yes   onclick="NewWindow(this.href,'name','650','550','yes');return false;" id=adminlink>Edit $guild{'2'} Website</A>
HTML
}

if ($user{'9'} eq "Administrator") {
print "<HR id=adminhr>";
print "<TEXTAREA id=newstext>";
&showoffnews;
print "</TEXTAREA><P>";

&watelist;

print <<"HTML";
<P>
<A HREF="$siteurl/?do=edit&tag=yes&guild=$INPUT{'guild'}"  onclick="NewWindow(this.href,'name','650','550','yes');return false;" id=adminlink>Edit $guild{'2'} Website</A>
HTML
}

print <<"HTML";
</td>
</TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</div>
<P>
HTML

&banner;

print <<"HTML";
</DIV>
</BODY></HTML>
HTML

}

##################################################################################

sub editwindow {

&getdata;
&getuser;

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
$tag
<HR>
<B>Edit Guild</B>
<P>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=emailmem><B><FONT COLOR=#000000>E-Mail Members</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editmem><B><FONT COLOR=#000000>Edit Members</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=news><B><FONT COLOR=#000000>Edit News</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=stats><B><FONT COLOR=#000000>View Guild Stats</FONT></B></A><BR>
HTML

if ($guild{'6'} ne "Silver\n") {
print <<"HTML";
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editphoto><B><FONT COLOR=#000000>Edit Photo Albums</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=gvalt><B><FONT COLOR=#000000>Guild Vault</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editraids><B><FONT COLOR=#000000>Edit Raids/Events</FONT></B></A><BR>
HTML
}
else {
print <<"HTML";
<SMALL>*</SMALL><B><FONT COLOR=#000000><U>Edit Photo Albums </U></FONT></B><BR>
<SMALL>*</SMALL><B><FONT COLOR=#000000><U>Guild Vault </U></FONT></B><BR>
<SMALL>*</SMALL><B><FONT COLOR=#000000><U>Edit Raids/Events </U></FONT></B><BR>
HTML
}


if ($user{'9'} eq "Administrator") {
print <<"HTML";
<hr>
<B>Edit Website</B>
<P>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editlink><B><FONT COLOR=#000000>Edit Link's</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editcontent><B><FONT COLOR=#000000>Edit Content</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=setcounter><B><FONT COLOR=#000000>Change Counter Image</FONT></B></A><BR>
HTML

if ($guild{'6'} ne "Silver\n") {
print <<"HTML";
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editcss><B><FONT COLOR=#000000>Edit StyleSheet</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editpage><B><FONT COLOR=#000000>Edit Page</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editrank><B><FONT COLOR=#000000>Edit Ranks</FONT></B></A><BR>
<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editraidhead><B><FONT COLOR=#000000>Edit Raid/Event Header</FONT></B></A><BR>
HTML
}
else {
print <<"HTML";
<SMALL>*</SMALL><B><FONT COLOR=#000000><U>Edit StyleSheet </U></FONT></B><BR>
<SMALL>*</SMALL><B><FONT COLOR=#000000><U>Edit Page </U></FONT></B><BR>
<SMALL>*</SMALL><B><FONT COLOR=#000000><U>Edit Ranks </U></FONT></B><BR>
<SMALL>*</SMALL><B><FONT COLOR=#000000><U>Edit Raid/Event Header </U></FONT></B><BR>
HTML
}
}


print <<"HTML";
<HR>
HTML

if ($guild{'6'} eq "Silver\n") {
print "<SMALL><B>* Gold Account Only</B></SMALL>";
}

print <<"HTML";
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub showstats {

&getdata;

$cnt = 0;
open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$cnt++;
}

($mon, $mday, $year, $junk) = split(/\//, $guild{'5'});

$tag = "<B>$guild{'2'} Stats</B><BR>";
$tag = "$tag<CENTER><TABLE BORDER=0 CELLSPACING=1 CELLPADDING=3 ALIGN=Center>";
$tag = "$tag<TR><TD><P ALIGN=Right>Acount Number:</TD><TD><B>$guild{'1'}</B></TD>";
$tag = "$tag</TR><TR><TD><P ALIGN=Right>Guild Name:</TD><TD><B>$guild{'2'}</B></TD>";
$tag = "$tag</TR><TR><TD><P ALIGN=Right>Guild Email:</TD><TD><B>$guild{'4'}</B></TD>";
$tag = "$tag</TR><TR><TD><P ALIGN=Right>Account Type:</TD><TD><B>$guild{'6'}</B></TD>";
if ($guild{'6'} eq "Gold\n") {
$tag = "$tag</TR><TR><TD><P ALIGN=Right>Gold Expires:</TD><TD><B>$mon/$mday/$year</B></TD>";
}
$tag = "$tag</TR><TR><TD><P ALIGN=Right>Account Creator:</TD><TD><B>$guild{'8'}</B></TD>";
$tag = "$tag</TR><TR><TD><P ALIGN=Right>Account Created:</TD><TD><B>$guild{'7'}</B></TD>";
$tag = "$tag</TR><TR><TD><P ALIGN=Right>Curent Members</TD><TD><B>$cnt</B></TD>";
$tag = "$tag</TR></TABLE></CENTER>";

&editwindow;

}

##################################################################################

sub editnews {

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceChars(entry) {
out = "!x!"; // replace this
add = "TEXTAREA"; // with this
temp = "" + entry; // temporary holder

while (temp.indexOf(out)>-1) {
pos= temp.indexOf(out);
temp = "" + (temp.substring(0, pos) + add + 
temp.substring((pos + out.length), temp.length));
}
document.subform.memnews.value = temp;
}
//  End -->
<!-- Begin
function replaceCharsb(entry) {
out = "!x!"; // replace this
add = "TEXTAREA"; // with this
temp = "" + entry; // temporary holder

while (temp.indexOf(out)>-1) {
pos= temp.indexOf(out);
temp = "" + (temp.substring(0, pos) + add + 
temp.substring((pos + out.length), temp.length));
}
document.subform.offnews.value = temp;
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload="replaceChars(document.subform.memnews.value);replaceCharsb(document.subform.offnews.value);">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  <B>Member News</TD>
      </TR>
      <TR>
	<TD><TEXTAREA NAME="memnews" COLS="30" rows=10>
HTML

open (DATA, "data/$INPUT{'guild'}.news");
@data = <DATA>;
close DATA;


$data = "@data";

$data =~ s/TEXTAREA/!x!/gi;

print "$data";


print <<"HTML";
</TEXTAREA></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
	  <B>Officer News</TD>
      </TR>
      <TR>
	<TD><TEXTAREA NAME="offnews" COLS="30" rows=10>
HTML

open (DATA, "data/$INPUT{'guild'}.off");
@data = <DATA>;
close DATA;

$data = "@data";

$data =~ s/TEXTAREA/!x!/gi;

print "$data";

print <<"HTML";
</TEXTAREA></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=updatenews>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
&getdata;
}

##################################################################################

sub updatenews {

open(DATA, ">data/$INPUT{'guild'}.news");
print DATA "$INPUT{'memnews'}";
close DATA;

open(DATA, ">data/$INPUT{'guild'}.off");
print DATA "$INPUT{'offnews'}";
close DATA;

$tag = "<B>News Updated</B>";

&editwindow;

}

##################################################################################

sub emailmem {
&getdata;

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><B>Subject:</B></TD>
	<TD>
	  <INPUT TYPE="text" NAME="subject" VALUE="$guild{'2'} Newsletter"></TD>
      </TR>
      <TR>
	<TD><B>To Type:</B></TD>
	<TD>
	  <SELECT NAME="to">
	  <OPTION SELECTED>All
	  <OPTION>Officer</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <B>Message:</B></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <TEXTAREA NAME="message" COLS="30" rows=10></TEXTAREA></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT type=hidden name=do value=sendemail>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Send"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
&getdata;
}

##################################################################################

sub sendemail {
&getdata;

open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;
foreach $line (@data) {
  ($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
  $i = 0;
  open (DATA, "user/$name.dat");
  @data = <DATA>;
  close DATA;
  foreach $linee (@data) {
    $i = $i + 1;
    $user{$i} = "$linee";
    $user{11} = "$typ";
}


if ($INPUT{'to'} eq "Officer") { 

if ($user{11} eq "Officer") { 
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $user{'4'}";
print MAIL "From: $guild{'4'}";
print MAIL "Subject: $INPUT{'subject'}\n";
print MAIL "$INPUT{'message'}\n";
}

}
elsif ($INPUT{'to'} eq "All") {
open (MAIL, "| /usr/sbin/sendmail -t -oi") || die "Can't open /usr/sbin/sendmail";
print MAIL "To: $user{'4'}";
print MAIL "From: $guild{'4'}";
print MAIL "Subject: $INPUT{'subject'}\n";
print MAIL "$INPUT{'message'}\n";
}


}

$tag = "<B>E-Mail's Sent</B>";

&editwindow;
}

##################################################################################

sub editpage {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<B>Click on a page name to edit the page</B><BR>
HTML

open (DATA, "data/$INPUT{'guild'}.page");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $page, $junk) = split(/::/, $line);
print "<A HREF=$siteurl/?guild=$INPUT{'guild'}&do=editpagenum&pagenum=$page>$name</A><BR>";
}

print <<"HTML";
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <B>Add New Page</B></TD>
      </TR>
      <TR>
	<TD>Page Name</TD>
	<TD>
	  <INPUT TYPE="text" NAME="pagename"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT type=hidden name=do value=addpage>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Add"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>

HTML
&getdata;
}

##################################################################################

sub editpagenum {

open (DATA, "pages/$INPUT{'pagenum'}.page");
@data = <DATA>;
close DATA;

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceChars(entry) {
out = "!x!"; // replace this
add = "TEXTAREA"; // with this
temp = "" + entry; // temporary holder

while (temp.indexOf(out)>-1) {
pos= temp.indexOf(out);
temp = "" + (temp.substring(0, pos) + add + 
temp.substring((pos + out.length), temp.length));
}
document.subform.html.value = temp;
}
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload="replaceChars(document.subform.html.value);">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  <B>Edit Page</B></TD>
      </TR>
      <TR>
	<TD><TEXTAREA NAME="html" COLS="30" rows=10>
HTML

$data = "@data";

$data =~ s/TEXTAREA/!x!/gi;

print "$data";

print <<"HTML";
</TEXTAREA></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=savepagenum>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
<INPUT type=hidden name=pagenum value=$INPUT{'pagenum'}>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

&getdata;
}

##################################################################################

sub savepagenum {
&getdata;

open(DATA, ">pages/$INPUT{'pagenum'}.page");
print DATA "$INPUT{'html'}";
close DATA;

$tag = "<B>Page Saved</B><BR>URL to page is<BR><A HREF=$siteurl/?guild=$INPUT{'guild'}&do=page&num=$INPUT{'pagenum'} target=_new>$siteurl/?guild=$INPUT{'guild'}&do=page&num=$INPUT{'pagenum'}</A>";

&editwindow;
}

##################################################################################

sub page {
&getuser;
&getdata;
&header;
&banner;
print <<"HTML";
<HTML>
<HEAD>
HTML
if ($guild{'6'} eq "Gold\n") {
open (DATA, "style/$INPUT{'guild'}.css");
@data = <DATA>;
close DATA;
$output = "@data";
$output =~ s/!X!/;/gi;
print "$output";
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}
print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body>
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD></TD>
</TR>
</TABLE>
</DIV>

<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML
&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
HTML

open (DATA, "pages/$INPUT{'num'}.page");
@data = <DATA>;
close DATA;

print "@data";

print <<"HTML";
<P>
HTML
&banner;
print <<"HTML";
</TD></TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</DIV>
</BODY></HTML>
HTML
}

##################################################################################

sub addpage {
&getdata;

open (FILE, "page.cnt");
flock (FILE, 2);
$cnt = <FILE>;
chop ($cnt);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$cnt++;

open(DATA, ">page.cnt");
print DATA "$cnt\n";
print DATA "junk\n";
close DATA;

open(DATA, ">pages/$cnt.page");
print DATA "Page Coming Soon!!";
close DATA;

open (DATA, "data/$INPUT{'guild'}.page");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.page");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'pagename'}::$cnt";
print DATA "::junk\n";
close DATA;

$tag = "<B>Page Created</B>";

&editwindow;

}

##################################################################################

sub editcontent {

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceChars(entry) {
out = "!x!"; // replace this
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
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload="replaceChars(document.subform.content.value);">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  <B>Content</TD>
      </TR>
      <TR>
	<TD><TEXTAREA NAME="content" COLS="30" rows=10>
HTML


open (DATA, "data/$INPUT{'guild'}.foot");
@data = <DATA>;
close DATA;



$data = "@data";

$data =~ s/TEXTAREA/!x!/gi;

print "$data";



print <<"HTML";
</TEXTAREA></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=savecontent>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
&getdata;
}

##################################################################################

sub savecontent {
&getdata;

open(DATA, ">data/$INPUT{'guild'}.foot");
print DATA "$INPUT{'content'}";
close DATA;

$tag = "<B>Content Updated</B>";

&editwindow;

}

##################################################################################

sub editcss {

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceChars(entry) {
out = ";"; // replace this
add = "!x!"; // with this
temp = "" + entry; // temporary holder

while (temp.indexOf(out)>-1) {
pos= temp.indexOf(out);
temp = "" + (temp.substring(0, pos) + add + 
temp.substring((pos + out.length), temp.length));
}
document.subform.css.value = temp;
}
//  End -->
</script>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>


<FORM ACTION="index.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  <B>StyleScript</TD>
      </TR>
      <TR>
<TD><TEXTAREA NAME="css" COLS="30" rows=10>
HTML

open (DATA, "style/$INPUT{'guild'}.css");
@data = <DATA>;
close DATA;
$output = "@data";
$output =~ s/!X!/;/gi;
print "$output";

print <<"HTML";
</TEXTAREA>
<P>
</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=savecss>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Save" onClick="replaceChars(document.subform.css.value);"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>

<P><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
&getdata;
}

##################################################################################

sub savecss {
&getdata;

open(DATA, ">style/$INPUT{'guild'}.css");
print DATA "$INPUT{'css'}";
close DATA;

$tag = "<B>StyleSheet Updated</B>";

&editwindow;

}

##################################################################################

sub editlink {
&getdata;
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<P>
<TABLE BORDER=0 CELLPADDING=2 ALIGN=Center>
<TR><TD><B>Link Name</B></TD><TD><B>Link Type</B></TD><TD><B>Delete Link</B></TD></TR>
HTML

open (DATA, "data/$INPUT{'guild'}.link");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $page, $typ) = split(/::/, $line);


if ($typ eq "1\n") {
print <<"HTML";
<TR><TD><A HREF=$page target=_new><B><FONT COLOR=#000000>$name</FONT></B></A></TD><TD>Same Window</TD><TD><A HREF="$siteurl/?guild=$INPUT{'guild'}&do=deletelink&delete=$name"><B><FONT COLOR=#000000><CENTER>Delete</FONT></B></A>
</TD></TR>
HTML
}
elsif ($typ eq "2\n") {
print <<"HTML";
<TR><TD><A HREF=$page target=_new><B><FONT COLOR=#000000>$name</FONT></B></A></TD><TD>New Window</TD><TD><A HREF="$siteurl/?guild=$INPUT{'guild'}&do=deletelink&delete=$name"><B><FONT COLOR=#000000><CENTER>Delete</FONT></B></A>
</TD></TR>
HTML
}
elsif ($typ eq "3\n") {
print <<"HTML";
<TR><TD><B>$name</B></TD><TD>LineFeed</TD><TD><A HREF="$siteurl/?guild=$INPUT{'guild'}&do=deletelink&delete=$name"><B><FONT COLOR=#000000><CENTER>Delete</FONT></B></A>
</TD></TR>
HTML
}


}
print <<"HTML";
</TABLE></CENTER>
<P>
<CENTER><A HREF=http://www.eqguilded.com/?guild=$INPUT{'guild'}&do=changelinkline><B><FONT COLOR=#000000>Change Link Order</FONT></B></A>
<P>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Link Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="name"></TD>
      </TR>
      <TR>
	<TD>Url:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="url"></TD>
      </TR>
      <TR>
	<TD>Type:</TD>
	<TD>
	  <SELECT NAME="type">
	  <OPTION SELECTED>1
	  <OPTION>2
	  <OPTION>3</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><CENTER>
<INPUT type=hidden name=do value=addlink>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Add"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML


}

##################################################################################

sub savelinkline {

$INPUT{'list'} =~ s/!HR!/\n/gi;
$INPUT{'list'} =~ s/!pct!/&/gi;
$INPUT{'list'} =~ s/!fs!/\//gi;
$INPUT{'list'} =~ s/!eql!/=/gi;
$INPUT{'list'} =~ s/!qm!/?/gi;

open(DATA, ">data/$INPUT{'guild'}.link");
print DATA "$INPUT{'list'}";
close DATA;

$tag = "<B>Link Order changed</b>";
&editwindow;

}

##################################################################################

sub changelinkline {

$cnt = 4;

print <<"HTML";

<HEAD>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function move(index,to) {
var list = document.form.list;
var total = list.options.length-1;
if (index == -1) return false;
if (to == +1 && index == total) return false;
if (to == -1 && index == 0) return false;
var items = new Array;
var values = new Array;
for (i = total; i >= 0; i--) {
items[i] = list.options[i].text;
values[i] = list.options[i].value;
}
for (i = total; i >= 0; i--) {
if (index == i) {
list.options[i + to] = new Option(items[i],values[i + to], 0, 1);
list.options[i] = new Option(items[i + to], values[i]);
i--;
}
else {
list.options[i] = new Option(items[i], values[i]);
   }
}
list.focus();
}
function submitForm() {
var list = document.form.list;
var theList = "";
for (i = 0; i <= list.options.length-1; i++) { 
theList += list.options[i].text + "!HR!";
}

out = "&"; // replace this
add = "!pct!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}
out = "="; // replace this
add = "!eql!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}
out = "/"; // replace this
add = "!fs!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}
out = "?"; // replace this
add = "!qm!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}

location.href = document.form.action + "?do=savelinkline&guild=$INPUT{'guild'}&list=" + theList;
}

//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>

<form method="GET" action="index.cgi" name="form">
<table>
<tr>
<td align="middle">
<select name="list" size="10" style="width:300">
HTML


$i = 0;
open (DATA, "data/$INPUT{'guild'}.link");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;

print "<option value=\"$i\">$line</option>";
}


print <<"HTML";
</select><br><br>

<input type="button" value="submit" onClick="submitForm()">
</td>
<td valign="top">
<input type="button" value="Up" 
onClick="move(this.form.list.selectedIndex,-1)"><br><br>
<input type="button" value="Down"
onClick="move(this.form.list.selectedIndex,+1)">
</td>
</tr>
</table>
</form>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub addlink {
&getdata;

open (DATA, "data/$INPUT{'guild'}.link");
@data = <DATA>;
close DATA;

if ($INPUT{'type'} eq "3") {
$INPUT{'url'} = "LineFeed";
}

open(DATA, ">data/$INPUT{'guild'}.link");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'name'}::$INPUT{'url'}::$INPUT{'type'}\n";
close DATA;


$tag = "<B>Link Added</b>";
&editwindow;
}

##################################################################################

sub deletelink {
&getdata;

open (DATA, "data/$INPUT{'guild'}.link");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.link");
foreach $line (@data) {
($name, $page, $typ) = split(/::/, $line);
if ($name eq "$INPUT{'delete'}") {
print DATA "";
}
else {
print DATA "$line";
}
}
close DATA;

$tag = "<B>Link Deleted</b>";
&editwindow;
}

##################################################################################

sub editmem {
&getdata;
&getuser;

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function setDataType(cValue)
  {
    // THIS FUNCTION CONVERTS DATES AND NUMBERS FOR PROPER ARRAY
    // SORTING WHEN IN THE SORT FUNCTION
    var isDate = new Date(cValue);
    if (isDate == "NaN")
      {
        if (isNaN(cValue))
          {
            // THE VALUE IS A STRING, MAKE ALL CHARACTERS IN
            // STRING UPPER CASE TO ASSURE PROPER A-Z SORT
            cValue = cValue.toUpperCase();
            return cValue;
          }
        else
          {
            // VALUE IS A NUMBER, TO PREVENT STRING SORTING OF A NUMBER
            // ADD AN ADDITIONAL DIGIT THAT IS THE + TO THE LENGTH OF
            // THE NUMBER WHEN IT IS A STRING
            var myNum;
            myNum = String.fromCharCode(48 + cValue.length) + cValue;
            return myNum;
          }
        }
  else
      {
        // VALUE TO SORT IS A DATE, REMOVE ALL OF THE PUNCTUATION AND
        // AND RETURN THE STRING NUMBER
        //BUG - STRING AND NOT NUMERICAL SORT .....
        // ( 1 - 10 - 11 - 2 - 3 - 4 - 41 - 5  etc.)
        var myDate = new String();
        myDate = isDate.getFullYear() + " " ;
        myDate = myDate + isDate.getMonth() + " ";
        myDate = myDate + isDate.getDate(); + " ";
        myDate = myDate + isDate.getHours(); + " ";
        myDate = myDate + isDate.getMinutes(); + " ";
        myDate = myDate + isDate.getSeconds();
        //myDate = String.fromCharCode(48 + myDate.length) + myDate;
        return myDate ;
      }
  }
function sortTable(col, tableToSort)
  {
    var iCurCell = col + tableToSort.cols;
    var totalRows = tableToSort.rows.length;
    var bSort = 0;
    var colArray = new Array();
    var oldIndex = new Array();
    var indexArray = new Array();
    var bArray = new Array();
    var newRow;
    var newCell;
    var i;
    var c;
    var j;
    // ** POPULATE THE ARRAY colArray WITH CONTENTS OF THE COLUMN SELECTED
    for (i=1; i < tableToSort.rows.length; i++)
      {
        colArray[i - 1] = setDataType(tableToSort.cells(iCurCell).innerText);
        iCurCell = iCurCell + tableToSort.cols;
      }
    // ** COPY ARRAY FOR COMPARISON AFTER SORT
    for (i=0; i < colArray.length; i++)
      {
        bArray[i] = colArray[i];
      }
    // ** SORT THE COLUMN ITEMS
    //alert ( colArray );
    colArray.sort();
    //alert ( colArray );
    for (i=0; i < colArray.length; i++)
      { // LOOP THROUGH THE NEW SORTED ARRAY
        indexArray[i] = (i+1);
        for(j=0; j < bArray.length; j++)
          { // LOOP THROUGH THE OLD ARRAY
            if (colArray[i] == bArray[j])
              {  // WHEN THE ITEM IN THE OLD AND NEW MATCH, PLACE THE
                // CURRENT ROW NUMBER IN THE PROPER POSITION IN THE
                // NEW ORDER ARRAY SO ROWS CAN BE MOVED ....
                // MAKE SURE CURRENT ROW NUMBER IS NOT ALREADY IN THE
                // NEW ORDER ARRAY
                for (c=0; c<i; c++)
                  {
                    if ( oldIndex[c] == (j+1) )
                    {
                      bSort = 1;
                    }
                      }
                      if (bSort == 0)
                        {
                          oldIndex[i] = (j+1);
                        }
                          bSort = 0;
                        }
          }
    }
  // ** SORTING COMPLETE, ADD NEW ROWS TO BASE OF TABLE ....
  for (i=0; i<oldIndex.length; i++)
    {
      newRow = tableToSort.insertRow();
      for (c=0; c<tableToSort.cols; c++)
        {
          newCell = newRow.insertCell();
          newCell.innerHTML = tableToSort.rows(oldIndex[i]).cells(c).innerHTML;
        }
      }
  //MOVE NEW ROWS TO TOP OF TABLE ....
  for (i=1; i<totalRows; i++)
    {
      tableToSort.moveRow((tableToSort.rows.length -1),1);
    }
  //DELETE THE OLD ROWS FROM THE BOTTOM OF THE TABLE ....
  for (i=1; i<totalRows; i++)
    {
      tableToSort.deleteRow();
    }
  }
// name="rsTable" id=rsTable cols=8javascript:sortTable(0, rsTable);
//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload="javascript:sortTable(0, rsTable);">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<P><BR>
<CENTER>
<SMALL>(clicking on the coloum headers will sort the list)</SMALL>
  <TABLE BORDER BORDERCOLOR=#000000 CELLPADDING="1" ALIGN="Center" name="rsTable" id=rsTable cols=8>
    <TR>
      <TD><CENTER><A HREF="javascript:sortTable(0, rsTable);"><FONT COLOR=#000000>Name</FONT></A></TD>
      <TD><CENTER><A HREF="javascript:sortTable(1, rsTable);"><FONT COLOR=#000000>Rank</FONT></A></TD>
      <TD><CENTER><A HREF="javascript:sortTable(2, rsTable);"><FONT COLOR=#000000>Type</FONT></A></TD>
      <TD><CENTER><A HREF="javascript:sortTable(3, rsTable);"><FONT COLOR=#000000>Access</FONT></A></TD>
      <TD><CENTER><A HREF="javascript:sortTable(4, rsTable);"><FONT COLOR=#000000>Pts</FONT></A></TD>
      <TD>+/- Pts</TD>
      <TD>Delete</TD>
      <TD>Edit</TD>
    </TR>
HTML

open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);


$i = 0;
open (DATAAA, "user/$name.dat");
@dataaa = <DATAAA>;
close DATAAA;
foreach $lineee (@dataaa) {
$i = $i + 1;
$usera{$i} = "$lineee";
}




print <<"HTML";
    <TR>
      <TD><A HREF=mailto:$usera{'4'}><FONT COLOR=#000000>$name</FONT></A></TD>
      <TD>$ran</TD>
      <TD>$typ</TD>
      <TD>$accs</TD>
      <TD>$pts</TD>
<TD>
<FORM ACTION="index.cgi" METHOD="POST">
<INPUT type=hidden name=name value=$name>
<INPUT type=hidden name=ran value=$ran>
<INPUT type=hidden name=typ value=$typ>
<INPUT type=hidden name=accs value=$accs>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
<INPUT TYPE="text" NAME="pts" SIZE="1">
<INPUT TYPE=submit name=do VALUE="+">
<INPUT TYPE=submit VALUE="-" name=do>
</FORM>
</TD>
HTML

if ($user{'9'} eq "Administrator") {
if ($accs eq "Master") {
print "<TD>&nbsp; Master &nbsp;</TD>";
}
else {
print <<"HTML";
      <TD>
&nbsp; <A HREF=$siteurl/?do=deletemem&guild=$INPUT{'guild'}&name=$name&rank=$ran&typ=$typ&accs=$accs&pts=$pts><FONT COLOR=black>Delete</FONT></A> &nbsp;
</TD>
HTML
}
print <<"HTML";
<TD>
&nbsp; <A HREF=$siteurl/?do=editmember&guild=$INPUT{'guild'}&name=$name&rank=$ran&typ=$typ&accs=$accs&pts=$pts><FONT COLOR=black>Edit</FONT></A> &nbsp;
</TD>
    </TR>
HTML
}

else {
print <<"HTML";
<TD><font size=1>Unauthorized</font></TD>
<TD><font size=1>Unauthorized</font></TD>
</TR>
HTML
}

}

print <<"HTML";
  </TABLE>
</CENTER>
<P>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################
sub deletemem {

open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.mem");
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
print DATA "";
}
else {
print DATA "$line";
}
}
close DATA;

&getdata;

$i = 0;
open (DATA, "user/$INPUT{'name'}.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$useraa{$i} = "$line";
}

open(DATA, ">user/$INPUT{'name'}.dat");
print DATA "$useraa{'1'}";
print DATA "$useraa{'2'}";
print DATA "$useraa{'3'}";
print DATA "$useraa{'4'}";
print DATA "\n";
print DATA "$useraa{'6'}";
print DATA "$useraa{'7'}";
print DATA "$useraa{'8'}";
print DATA "junk\n";
close DATA;

$tag = "<B>Member Deleted</b>";
&editwindow;
}
##################################################################################

sub editmember {
&getdata;

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><B>Name:</B></TD>
	<TD>$INPUT{'name'}<INPUT type=hidden name=name value=$INPUT{'name'}></TD>
      </TR>
      <TR>
	<TD><B>Access:</B></TD>
	<TD>
HTML
if ($INPUT{'accs'} eq "Master") {
print "Master<INPUT TYPE=hidden NAME=accs VALUE=Master>";
}
else {

if ($INPUT{'accs'} eq "Member") {
print <<"HTML";
	  <SELECT NAME="accs">
	  <OPTION SELECTED>Member
	  <OPTION>Moderator
	  <OPTION>Administrator</SELECT>
HTML
}
elsif ($INPUT{'accs'} eq "Moderator") {
print <<"HTML";
	  <SELECT NAME="accs">
	  <OPTION>Member
	  <OPTION SELECTED>Moderator
	  <OPTION>Administrator</SELECT>
HTML
}
elsif ($INPUT{'accs'} eq "Administrator") {
print <<"HTML";
	  <SELECT NAME="accs">
	  <OPTION>Member
	  <OPTION>Moderator
	  <OPTION SELECTED>Administrator</SELECT>
HTML
}
}
print <<"HTML";
</TD>
      </TR>
      <TR>
	<TD><B>Type:</B></TD>
	<TD>
HTML

if ($INPUT{'typ'} eq "Member") {
print <<"HTML";
	  <SELECT NAME="type">
	  <OPTION SELECTED>Member
	  <OPTION>Officer</SELECT></TD>
HTML
}
if ($INPUT{'typ'} eq "Officer") {
print <<"HTML";
	  <SELECT NAME="type">
	  <OPTION>Member
	  <OPTION SELECTED>Officer</SELECT></TD>
HTML
}

print <<"HTML";
      </TR>
      <TR>
	<TD><B>Rank:</B></TD>
	<TD>
HTML


print "<SELECT NAME=rank id=input>";
open (DATA, "data/$INPUT{'guild'}.rank");
@data = <DATA>;
close DATA;
foreach $line (@data) {
	chomp ($line);
	($ranks, $aaatype) = split(/&/, $line);
if ($aaatype eq "3") {
$ranks = "----- $ranks -----";
}
if ($aaatype eq "4") {
$ranks = "--- $ranks ---";
}
if ($ranks eq "$INPUT{'rank'}") {
print "<OPTION SELECTED>$ranks";
}
else {
print "<OPTION>$ranks";
}
}
print "</SELECT>";


print <<"HTML";
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT type=hidden name=pts value=$INPUT{'pts'}>
<INPUT type=hidden name=do value=savemember>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML


}

##################################################################################

sub savemember {
&getdata;

open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.mem");
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {

print DATA "$INPUT{'name'}::$INPUT{'accs'}::$INPUT{'rank'}::$INPUT{'type'}::$INPUT{'pts'}\n";
}
else {
print DATA "$line";
}
}
close DATA;

$tag = "<B>Member Updated</b>";
&editwindow;
}

##################################################################################

sub addpts {
&getdata;

open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.mem");
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
$pts = $pts + $INPUT{'pts'};
print DATA "$INPUT{'name'}::$INPUT{'accs'}::$INPUT{'ran'}::$INPUT{'typ'}::$pts\n";
}
else {
print DATA "$line";
}
}
close DATA;

$tag = "<B>Points Added</b>";
&editwindow;
}

##################################################################################

sub takepts {
&getdata;

open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.mem");
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
$pts = $pts - $INPUT{'pts'};
if ($pts < "0") { $pts = 0; }
print DATA "$INPUT{'name'}::$INPUT{'accs'}::$INPUT{'ran'}::$INPUT{'typ'}::$pts\n";
}
else {
print DATA "$line";
}
}
close DATA;

$tag = "<B>Points Subtracted</b>";
&editwindow;
}

##################################################################################

sub roster {
&getuser;
&getdata;
&header;
&banner;
print <<"HTML";
<HTML>
<HEAD>
HTML
if ($guild{'6'} eq "Gold\n") {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/$INPUT{'guild'}.css">
HTML
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}
print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body>
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD></TD>
</TR>
</TABLE>
</DIV>

<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML
&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
HTML

print <<"HTML";
<TABLE id=rostertable>
    <TR>
      <TD COLSPAN=3><div id=rostertext>Name</div></TD>
      <TD><div id=rostertext>Rank</div></TD>
      <TD><div id=rostertext>Lvl</div></TD>
      <TD><div id=rostertext>Race</div></TD>
      <TD><div id=rostertext>Class</div></TD>
    </TR>
HTML

open (DATA, "data/$INPUT{'guild'}.rank");
@dataaa = <DATA>;
close DATA;
foreach $line (@dataaa) {
	chomp ($line);
	($ranks, $types) = split(/&/, $line);

if ($types eq "3") {
print "<TR><TD COLSPAN=7><HR id=rosterhr><div id=rostertext>$ranks</DIV><HR id=rosterhr></TD></TR>";
}
else {

open (DATA, "data/$INPUT{'guild'}.mem");
@dataaaaaaaa = <DATA>;
close DATA;

foreach $linee (@dataaaaaaaa) {
($name, $accs, $rank, $typ, $pts) = split(/::/, $linee);

$i = 0;
open (DATA, "user/$name.dat");
@data = <DATA>;
close DATA;
foreach $lineee (@data) {
$i = $i + 1;
$usera{$i} = "$lineee";
}

if ($rank eq "$ranks") {

($cl, $myrank) = split(/_/, $rank);
if ($myrank eq "") {
$myrank = $rank;
}

if ($types eq "1") {
print <<"HTML";
<TR><TD COLSPAN=2><A HREF=$siteurl/?do=view&name=$name onclick="NewWindow(this.href,'name','600','400','yes');return false;" id=rostername>$usera{'1'} $usera{'2'}</A></TD>
<TD></TD><TD><div id=rostertext2>$myrank</DIV></TD><TD><div id=rostertext2>$usera{'8'}</DIV></TD><TD><div id=rostertext2>$usera{'7'}</DIV></TD><TD><div id=rostertext2>$usera{'6'}</DIV></TD></TR>
HTML
}
if ($types eq "2") {
print <<"HTML";
<TR><TD></TD>
<TD COLSPAN=2><A HREF=$siteurl/?do=view&name=$name onclick="NewWindow(this.href,'name','600','400','yes');return false;" id=rostername>$usera{'1'} $usera{'2'}</A></TD>
<TD><div id=rostertext2>$myrank</DIV></TD><TD><div id=rostertext2>$usera{'8'}</DIV></TD><TD><div id=rostertext2>$usera{'7'}</DIV></TD><TD><div id=rostertext2>$usera{'6'}</DIV></TD></TR>
HTML
}

}
}


}
}

print <<"HTML";
</TABLE></CENTER>
HTML

#open (DATA, "data/members.alt");
#@data = <DATA>;
#close DATA;

#foreach $line (@data) {
#chomp ($line);
#($Ausr, $Aclass, $Arace, $Auser, $alvl) = split(/::/, $line);

#$Ausr =~ s/_/ /gi;

#$altlist = "$altlist<TR>";
#$altlist = "$altlist<TD><div id=text2>$Ausr</div></TD>";
#$altlist = "$altlist<TD><div id=text3>$alvl</div></TD>";
#$altlist = "$altlist<TD><div id=text3>$Arace</div></TD>";
#$altlist = "$altlist<TD><div id=text3>$Aclass</div></TD>";
#$altlist = "$altlist<TD><div id=text3>$Auser</div></TD>";
#$altlist = "$altlist</TR>";


#}


print <<"HTML";
<P>
HTML
&banner;
print <<"HTML";
</TD></TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</DIV>
</BODY></HTML>
HTML
}

##################################################################################

sub editrank {

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
  <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Name</TD>
      <TD>Type</TD>
      <TD>Delete</TD>
    </TR>

HTML

open (DATA, "data/$INPUT{'guild'}.rank");
@data = <DATA>;
close DATA;

foreach $line (@data) {
($rname, $rtype) = split(/&/, $line);
print <<"HTML";
    <TR>
      <TD>$rname</TD>
      <TD>$rtype</TD>
      <FORM ACTION="index.cgi" METHOD="POST"><TD><INPUT type=hidden name=rank value="$rname"><INPUT type=hidden name=do value=deleterank><INPUT type=hidden name=guild value=$INPUT{'guild'}><INPUT TYPE=submit VALUE="Delete"></TD></FORM>
    </TR>
HTML
}



print <<"HTML";
  </TABLE>
</CENTER>
<P>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  Add Rank</TD>
      </TR>
      <TR>
	<TD>Rank Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="rname"></TD>
      </TR>
      <TR>
	<TD>Rank Type:</TD>
	<TD>
	  <SELECT NAME="rtype">
	  <OPTION SELECTED>1
	  <OPTION>2
	  <OPTION>3
	  <OPTION>4</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT type=hidden name=do value=saverank>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

&getdata;


}

##################################################################################

sub saverank {
&getdata;

open (DATA, "data/$INPUT{'guild'}.rank");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.rank");
foreach $line (@data) {
($name, $type) = split(/&/, $line);

print DATA "$line";
}
print DATA "$INPUT{'rname'}&$INPUT{'rtype'}\n";
close DATA;

$tag = "<B>Rank Saved</B>";
&editwindow;

}

##################################################################################

sub deleterank {
&getdata;

open (DATA, "data/$INPUT{'guild'}.rank");
@data = <DATA>;
close DATA;

open(DATA, ">data/$INPUT{'guild'}.rank");
foreach $line (@data) {
($name, $type) = split(/&/, $line);
if ($name eq "$INPUT{'rank'}") {

print DATA "";
}
else {
print DATA "$line";
}
}
close DATA;

$tag = "<B>Rank Deleted</B>";
&editwindow;
}

##################################################################################

sub editphoto {

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER><form ACTION=index.cgi METHOD=POST>
<DIV id=text2><B>Add to photo album:</B></DIV>
<SELECT NAME=page id=input>
HTML


open (DATA, "data/$INPUT{'guild'}.photo");
	@data = <DATA>;
close DATA;
foreach $line (@data) {
	chomp ($line);
	($page, $name) = split(/::/, $line);
print "<OPTION>$page";
}

print <<"HTML";
</SELECT><BR><DIV id=text2>Photo Address</DIV>
<input type=INPUT name=sourcefile id=input><BR>
<DIV id=text2>Description</div>
<input type=text name=desc id=input><BR>

<input type=hidden name=do value=uploadfile>
<input type=hidden name=guild value=$INPUT{'guild'}>
<input type=submit value=Save id=input>

</form><P><FORM ACTION=index.cgi METHOD=POST><DIV id=text2><B>Add new album</B></div>
<input type=hidden name=do value=newalbum>
<DIV id=text3>Short Name:</div>
<INPUT TYPE=text NAME=shtname id=input><BR>
<DIV id=text3>Long Name:</div>
<INPUT TYPE=text NAME=lngname id=input><BR>
<input type=hidden name=guild value=$INPUT{'guild'}>
<INPUT TYPE=submit value=Save id=input></FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################

sub newalbum {

open (DATA, "data/$INPUT{'guild'}.photo");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'guild'}.photo");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'shtname'}::$INPUT{'lngname'}\n";
close DATA;

$tag = "<CENTER><B>New Photo Album Added</B></CENTER>";
&editwindow;
}

##################################################################################

sub uploadfile {

$INPUT{'desc'} =~ s/ /%20/gi;

open (DATA, "data/$INPUT{'guild'}photo.$INPUT{'page'}.lst");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'guild'}photo.$INPUT{'page'}.lst");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'sourcefile'}::$INPUT{'desc'}\n";
close DATA;


$tag = "<CENTER><B>Picture Saved to Photo Album</B></CENTER>";
&editwindow;
}

##################################################################################

sub photopage {
&getuser;
&getdata;
&header;
&banner;
print <<"HTML";
<HTML>
<HEAD>
HTML
if ($guild{'6'} eq "Gold\n") {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/$INPUT{'guild'}.css">
HTML
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}
print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body>
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD></TD>
</TR>
</TABLE>
</DIV>

<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML
&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
<BR>
<P>
<TABLE id=table>
<TR>
HTML


open (DATA, "data/$INPUT{'guild'}photo.$INPUT{'page'}.lst");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($IMG, $DESC) = split(/::/, $line);
	$count = $count + 1;
	
	print "<TD><A HREF=?do=photoview&img=$IMG&desc=$DESC&guild=$INPUT{'guild'} TARGET=_img><IMG SRC=$IMG WIDTH=100 HEIGHT=100 BORDER=0></A></TD>";

	if ($count eq 6) {
		print "</TR><TR>";
		$count = 0;
	}
}
close DATA;




print <<"HTML";
</TR></TABLE>
<P>
HTML
&banner;
print <<"HTML";
</TD></TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</DIV>
</BODY></HTML>
HTML
}

##################################################################################

sub photos {
# view photo albums
&getuser;
&getdata;
&header;
&banner;
print <<"HTML";
<HTML>
<HEAD>
HTML
if ($guild{'6'} eq "Gold\n") {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/$INPUT{'guild'}.css">
HTML
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}
print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body>
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD></TD>
</TR>
</TABLE>
</DIV>

<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML
&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
<BR>
<P>
HTML




open (DATA, "data/$INPUT{'guild'}.photo");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($page, $name) = split(/::/, $line);
print "<A HREF=$siteurl/?do=photopage&page=$page&guild=$INPUT{'guild'} id=link>$name</A><P>";
}
close DATA;




print <<"HTML";
<P>
HTML
&banner;
print <<"HTML";
</TD></TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</DIV>
</BODY></HTML>
HTML
}


##################################################################################

sub raids {

&getuser;
&getdata;
&header;
&banner;
print <<"HTML";
<HTML>
<HEAD>
HTML
if ($guild{'6'} eq "Gold\n") {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/$INPUT{'guild'}.css">
HTML
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}
print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body>
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD></TD>
</TR>
</TABLE>
</DIV>

<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML

&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
<BR>
<P>
<CENTER>
HTML

open (DATA, "data/$INPUT{'guild'}.raidhead");
	@data = <DATA>;
close DATA;

print "@data";


print <<"HTML";
<P>
<HR width=50%>
<B>Upcoming Raids and Events</B>
<HR width=50%>
  <TABLE BORDER=0 CELLSPACING="2" CELLPADDING="2" ALIGN="Center" WIDTH="50%">
HTML




open (DATA, "data/$INPUT{'guild'}.raids");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($name, $date, $time, $info) = split(/::/, $line);
print "<TR><TD><B>$name</B></TD><TD>$date ($time)</TD></TR><TR><TD COLSPAN=2>$info</TD></TR>";

}
close DATA;



print <<"HTML";
  </TABLE>
</CENTER>
<P>
HTML
&banner;
print <<"HTML";
</TD></TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</DIV>
</BODY></HTML>
HTML
}

##################################################################################

sub editraidhead {

print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function replaceChars(entry) {
out = "!x!"; // replace this
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
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload="replaceChars(document.subform.content.value);">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  <B>Raid/Event Header</TD>
      </TR>
      <TR>
	<TD><TEXTAREA NAME="content" COLS="30" rows=10>
HTML


open (DATA, "data/$INPUT{'guild'}.raidhead");
	@data = <DATA>;
close DATA;

$data = "@data";

$data =~ s/TEXTAREA/!x!/gi;

print "$data";


print <<"HTML";
</TEXTAREA>
</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT type=hidden name=do value=saveraidhead>
<INPUT type=hidden name=guild value=$INPUT{'guild'}>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
&getdata;
}

##################################################################################

sub saveraidhead {
&getdata;

open(DATA, ">data/$INPUT{'guild'}.raidhead");
print DATA "$INPUT{'content'}";
close DATA;

$tag = "<B>Raid Header Updated</B>";

&editwindow;

}

##################################################################################

sub edieraids {


print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
  <TABLE BORDER=0 CELLSPACING="2" CELLPADDING="2" ALIGN="Center" WIDTH="50%">
HTML


open (DATA, "data/$INPUT{'guild'}.raids");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($name, $date, $time, $info) = split(/::/, $line);
print <<"HTML";
<FORM ACTION="index.cgi" METHOD="POST">
<TR><TD><B>$name</B></TD><TD>$date ($time)</TD><TD>
<INPUT TYPE=submit VALUE="Delete">
</TD></TR><TR><TD COLSPAN=3>$info</TD></TR>
  <INPUT TYPE="hidden" NAME="name" VALUE="$name">
  <INPUT TYPE="hidden" NAME="do" VALUE="savedeleteraids">
  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
  </FORM>
HTML
}
close DATA;


print <<"HTML";
</TABLE>
<P>
<HR width=50%>
<P>
<B>Add a Raid/Event</B>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="name"></TD>
      </TR>
      <TR>
	<TD>Date:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="date"></TD>
      </TR>
      <TR>
	<TD>Time:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="time"></TD>
      </TR>
      <TR>
	<TD>Info:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="info"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
	  <INPUT TYPE="hidden" NAME="do" VALUE="saveaddraids">
	  <INPUT TYPE=submit value=Save> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<P>

<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML


}

##################################################################################

sub saveaddraids {

open (DATA, "data/$INPUT{'guild'}.raids");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'guild'}.raids");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'name'}::$INPUT{'date'}::$INPUT{'time'}::$INPUT{'info'}::\n";
close DATA;


$tag = "<B>Raid Added</B>";
&editwindow;
}

##################################################################################

sub savedeleteraids {

open (DATA, "data/$INPUT{'guild'}.raids");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'guild'}.raids");
foreach $line (@data) {
	chomp ($line);
	($name, $date, $time, $info) = split(/::/, $line);
     if ($name eq "$INPUT{'name'}") {
	print DATA "";
     }
     else {

          print DATA "$line";
     }
}
close DATA;


$tag = "<B>Raid Deleted</B>";
&editwindow;

}

##################################################################################

sub gvalt {
print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function setDataType(cValue)
  {
    // THIS FUNCTION CONVERTS DATES AND NUMBERS FOR PROPER ARRAY
    // SORTING WHEN IN THE SORT FUNCTION
    var isDate = new Date(cValue);
    if (isDate == "NaN")
      {
        if (isNaN(cValue))
          {
            // THE VALUE IS A STRING, MAKE ALL CHARACTERS IN
            // STRING UPPER CASE TO ASSURE PROPER A-Z SORT
            cValue = cValue.toUpperCase();
            return cValue;
          }
        else
          {
            // VALUE IS A NUMBER, TO PREVENT STRING SORTING OF A NUMBER
            // ADD AN ADDITIONAL DIGIT THAT IS THE + TO THE LENGTH OF
            // THE NUMBER WHEN IT IS A STRING
            var myNum;
            myNum = String.fromCharCode(48 + cValue.length) + cValue;
            return myNum;
          }
        }
  else
      {
        // VALUE TO SORT IS A DATE, REMOVE ALL OF THE PUNCTUATION AND
        // AND RETURN THE STRING NUMBER
        //BUG - STRING AND NOT NUMERICAL SORT .....
        // ( 1 - 10 - 11 - 2 - 3 - 4 - 41 - 5  etc.)
        var myDate = new String();
        myDate = isDate.getFullYear() + " " ;
        myDate = myDate + isDate.getMonth() + " ";
        myDate = myDate + isDate.getDate(); + " ";
        myDate = myDate + isDate.getHours(); + " ";
        myDate = myDate + isDate.getMinutes(); + " ";
        myDate = myDate + isDate.getSeconds();
        //myDate = String.fromCharCode(48 + myDate.length) + myDate;
        return myDate ;
      }
  }
function sortTable(col, tableToSort)
  {
    var iCurCell = col + tableToSort.cols;
    var totalRows = tableToSort.rows.length;
    var bSort = 0;
    var colArray = new Array();
    var oldIndex = new Array();
    var indexArray = new Array();
    var bArray = new Array();
    var newRow;
    var newCell;
    var i;
    var c;
    var j;
    // ** POPULATE THE ARRAY colArray WITH CONTENTS OF THE COLUMN SELECTED
    for (i=1; i < tableToSort.rows.length; i++)
      {
        colArray[i - 1] = setDataType(tableToSort.cells(iCurCell).innerText);
        iCurCell = iCurCell + tableToSort.cols;
      }
    // ** COPY ARRAY FOR COMPARISON AFTER SORT
    for (i=0; i < colArray.length; i++)
      {
        bArray[i] = colArray[i];
      }
    // ** SORT THE COLUMN ITEMS
    //alert ( colArray );
    colArray.sort();
    //alert ( colArray );
    for (i=0; i < colArray.length; i++)
      { // LOOP THROUGH THE NEW SORTED ARRAY
        indexArray[i] = (i+1);
        for(j=0; j < bArray.length; j++)
          { // LOOP THROUGH THE OLD ARRAY
            if (colArray[i] == bArray[j])
              {  // WHEN THE ITEM IN THE OLD AND NEW MATCH, PLACE THE
                // CURRENT ROW NUMBER IN THE PROPER POSITION IN THE
                // NEW ORDER ARRAY SO ROWS CAN BE MOVED ....
                // MAKE SURE CURRENT ROW NUMBER IS NOT ALREADY IN THE
                // NEW ORDER ARRAY
                for (c=0; c<i; c++)
                  {
                    if ( oldIndex[c] == (j+1) )
                    {
                      bSort = 1;
                    }
                      }
                      if (bSort == 0)
                        {
                          oldIndex[i] = (j+1);
                        }
                          bSort = 0;
                        }
          }
    }
  // ** SORTING COMPLETE, ADD NEW ROWS TO BASE OF TABLE ....
  for (i=0; i<oldIndex.length; i++)
    {
      newRow = tableToSort.insertRow();
      for (c=0; c<tableToSort.cols; c++)
        {
          newCell = newRow.insertCell();
          newCell.innerHTML = tableToSort.rows(oldIndex[i]).cells(c).innerHTML;
        }
      }
  //MOVE NEW ROWS TO TOP OF TABLE ....
  for (i=1; i<totalRows; i++)
    {
      tableToSort.moveRow((tableToSort.rows.length -1),1);
    }
  //DELETE THE OLD ROWS FROM THE BOTTOM OF THE TABLE ....
  for (i=1; i<totalRows; i++)
    {
      tableToSort.deleteRow();
    }
  }
//  End -->
</script>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF" onload="javascript:sortTable(0, rsTable);">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<SMALL>(clicking on the coloum headers will sort the list)</SMALL>
  <TABLE BORDER=0 CELLSPACING="2" CELLPADDING="2" ALIGN="Center" WIDTH="75%" name="rsTable" id=rsTable cols=5>
<TR>
<TD><A HREF="javascript:sortTable(0, rsTable);"><FONT COLOR=black><B>Name</B></FONT></A></TD>
<TD><A HREF="javascript:sortTable(1, rsTable);"><FONT COLOR=black><B>Price</B></FONT></A></TD>
<TD><A HREF="javascript:sortTable(2, rsTable);"><FONT COLOR=black><B>Qty</B></FONT></A></TD>
<TD>Delete</TD>
<TD>Edit</TD>
</TR>
HTML


open (DATA, "data/$INPUT{'guild'}.valt");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($name, $price, $qty, $slot) = split(/::/, $line);
print <<"HTML";
<TR>
<TD width=50%><A HREF="$siteurl/?do=viewitem&name=$name&slot=$slot" onclick="NewWindow(this.href,'item','400','200','yes');return false;"><FONT COLOR=black>$name</FONT></A></TD>
<TD>$price</TD>
<TD>$qty</TD>
<TD>
<FORM ACTION="index.cgi" METHOD="POST">
<INPUT TYPE=submit name=do VALUE="Delete Item">
  <INPUT TYPE="hidden" NAME="name" VALUE="$name">
  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
  </FORM>
</TD>
<TD>
<FORM ACTION="index.cgi" METHOD="POST">
<INPUT TYPE=submit name=do VALUE="Edit Item">
  <INPUT TYPE="hidden" NAME="name" VALUE="$name">
  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
  </FORM>
</TD>
</TR>
HTML
}
close DATA;


print <<"HTML";
</TABLE>
<P>
<B>Add item</B>
<P>
Chose a slot
<FORM ACTION="index.cgi" METHOD="POST">
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
<P>
  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
  <INPUT TYPE="hidden" NAME="do" VALUE="additemtwo">
  <INPUT TYPE=submit VALUE="Next &gt;">
</FORM>


<P>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub additemtwo {
print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
Chose a Item
<FORM ACTION="index.cgi" METHOD="POST">
  <SELECT NAME="name">
HTML

open (DATA, "items/$INPUT{'slot'}.lst");
@data = <DATA>;
close DATA;

foreach $line (@data) {
($image, $name, $slot, $magic, $skill, $delay, $dmg, $ac, $wt, $str, $sta, $agi, $dex, $wis, $int, $cha, $svp, $svm, $svd, $svf, $svc, $effect, $smod, $class, $race, $hp, $vear, $lore, $nodrop) = split(/::/, $line);


print "<OPTION>$name\n";

}

print <<"HTML";
</SELECT>
<P>
  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
  <INPUT TYPE="hidden" NAME="do" VALUE="additemthree">
  <INPUT TYPE="hidden" NAME="slot" VALUE="$INPUT{'slot'}">
  <INPUT TYPE=submit VALUE="Next &gt;">
</FORM>
<P>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub additemthree {

print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name:</TD>
	<TD>$INPUT{'name'}
	  <INPUT TYPE="hidden" NAME="name" VALUE="$INPUT{'name'}"></TD>
      </TR>
      <TR>
	<TD>Price:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="price" VALUE="Price Not Set"></TD>
      </TR>
      <TR>
	<TD>Qty:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="qty" VALUE="1"></TD>
      </TR>
      <TR>
	<TD>Slot:</TD>
	<TD>$INPUT{'slot'}
	  <INPUT TYPE="hidden" NAME="slot" VALUE="$INPUT{'slot'}">
<INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
<INPUT TYPE="hidden" NAME="do" VALUE="additemfour">
</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
<P>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub additemfour {

open (DATA, "data/$INPUT{'guild'}.valt");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'guild'}.valt");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'name'}::$INPUT{'price'}::$INPUT{'qty'}::$INPUT{'slot'}\n";
close DATA;



$tag = "<B>Item Added</B>";
&editwindow;
}

##################################################################################

sub viewitem {

open (DATA, "items/$INPUT{'slot'}.lst");
@data = <DATA>;
close DATA;

foreach $line (@data) {
	chomp ($line);
        ($image, $name, $slot, $magic, $skill, $delay, $dmg, $ac, $wt, $str, $sta, $agi, $dex, $wis, $int, $cha, $svp, $svm, $svd, $svf, $svc, $effect, $smod, $class, $race, $hp, $vear, $lore, $nodrop) = split(/::/, $line);

if ($name eq "$INPUT{'name'}") {
print <<"HTML";
<HEAD>
  <TITLE>$name</TITLE>
</HEAD>
<BODY BGCOLOR="#000000" TEXT="#ffffff" BACKGROUND="$siteurl/images/vitembg.jpg">
<CENTER>
  <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center" width=100%>
    <TR>
      <TD><IMG SRC="http://www.eqguilded.com/images/items/$image.gif"></TD>
      <TD WIDTH="100%" VALIGN="Bottom"><B>$name</B></TD>
    </TR>
    <TR>
      <TD COLSPAN=2>
HTML

if ($magic eq "magic") { $magic = "MAGIC ITEM"; }
if ($lore eq "lore") { $lore = "LORE ITEM"; }
if ($nodrop eq "nodrop") { $nodrop = "NO DROP"; }
print "$magic $lore $nodrop<BR>";
print "Slot: $slot<BR>";
if ($skill ne "" ) { print "Skill: $skill "; }
if ($delay ne "" ) { print "Atk Delay: $delay<BR>"; }
if ($dmg ne "" ) { print "DMG: $dmg<BR>"; }
if ($ac ne "" ) { print "AC: $ac<BR>"; }
if ($hp ne "" ) { print "HP: $hp "; }
if ($str ne "" ) { print "STR: $str "; }
if ($sta ne "" ) { print "STA: $sta "; }
if ($agi ne "" ) { print "AGI: $agi "; }
if ($dex ne "" ) { print "DEX: $dex "; }
if ($wis ne "" ) { print "WIS: $wis "; }
if ($int ne "" ) { print "INT: $int "; }
if ($cha ne "" ) { print "CHA: $cha "; }
if ($svp ne "" ) { print "SVP: $svp "; }
if ($svm ne "" ) { print "SVM: $svm "; }
if ($svd ne "" ) { print "SVD: $svd "; }
if ($svf ne "" ) { print "SVF: $svf "; }
if ($svc ne "" ) { print "SVC: $svc "; }
print "<BR>Wt: $wt<BR>";
print "Class: $class<BR>";
print "Race: $race <BR>";
print "<P>";
if ($smod ne "" ) { print "Mod: $smod<BR>"; }
if ($effect ne "" ) { print "Effect: $effect<BR>"; }
print "<P>";
if ($vear ne "true") { print "This item is not vearafied!<BR>Stats may not be correct."; }


print <<"HTML";
</TD>
    </TR>
  </TABLE>
</CENTER>
HTML
     }

}

}

##################################################################################

sub valt {
#view valt
&getuser;
&getdata;
&header;
&banner;
print <<"HTML";
<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function setDataType(cValue)
  {
    // THIS FUNCTION CONVERTS DATES AND NUMBERS FOR PROPER ARRAY
    // SORTING WHEN IN THE SORT FUNCTION
    var isDate = new Date(cValue);
    if (isDate == "NaN")
      {
        if (isNaN(cValue))
          {
            // THE VALUE IS A STRING, MAKE ALL CHARACTERS IN
            // STRING UPPER CASE TO ASSURE PROPER A-Z SORT
            cValue = cValue.toUpperCase();
            return cValue;
          }
        else
          {
            // VALUE IS A NUMBER, TO PREVENT STRING SORTING OF A NUMBER
            // ADD AN ADDITIONAL DIGIT THAT IS THE + TO THE LENGTH OF
            // THE NUMBER WHEN IT IS A STRING
            var myNum;
            myNum = String.fromCharCode(48 + cValue.length) + cValue;
            return myNum;
          }
        }
  else
      {
        // VALUE TO SORT IS A DATE, REMOVE ALL OF THE PUNCTUATION AND
        // AND RETURN THE STRING NUMBER
        //BUG - STRING AND NOT NUMERICAL SORT .....
        // ( 1 - 10 - 11 - 2 - 3 - 4 - 41 - 5  etc.)
        var myDate = new String();
        myDate = isDate.getFullYear() + " " ;
        myDate = myDate + isDate.getMonth() + " ";
        myDate = myDate + isDate.getDate(); + " ";
        myDate = myDate + isDate.getHours(); + " ";
        myDate = myDate + isDate.getMinutes(); + " ";
        myDate = myDate + isDate.getSeconds();
        //myDate = String.fromCharCode(48 + myDate.length) + myDate;
        return myDate ;
      }
  }
function sortTable(col, tableToSort)
  {
    var iCurCell = col + tableToSort.cols;
    var totalRows = tableToSort.rows.length;
    var bSort = 0;
    var colArray = new Array();
    var oldIndex = new Array();
    var indexArray = new Array();
    var bArray = new Array();
    var newRow;
    var newCell;
    var i;
    var c;
    var j;
    // ** POPULATE THE ARRAY colArray WITH CONTENTS OF THE COLUMN SELECTED
    for (i=1; i < tableToSort.rows.length; i++)
      {
        colArray[i - 1] = setDataType(tableToSort.cells(iCurCell).innerText);
        iCurCell = iCurCell + tableToSort.cols;
      }
    // ** COPY ARRAY FOR COMPARISON AFTER SORT
    for (i=0; i < colArray.length; i++)
      {
        bArray[i] = colArray[i];
      }
    // ** SORT THE COLUMN ITEMS
    //alert ( colArray );
    colArray.sort();
    //alert ( colArray );
    for (i=0; i < colArray.length; i++)
      { // LOOP THROUGH THE NEW SORTED ARRAY
        indexArray[i] = (i+1);
        for(j=0; j < bArray.length; j++)
          { // LOOP THROUGH THE OLD ARRAY
            if (colArray[i] == bArray[j])
              {  // WHEN THE ITEM IN THE OLD AND NEW MATCH, PLACE THE
                // CURRENT ROW NUMBER IN THE PROPER POSITION IN THE
                // NEW ORDER ARRAY SO ROWS CAN BE MOVED ....
                // MAKE SURE CURRENT ROW NUMBER IS NOT ALREADY IN THE
                // NEW ORDER ARRAY
                for (c=0; c<i; c++)
                  {
                    if ( oldIndex[c] == (j+1) )
                    {
                      bSort = 1;
                    }
                      }
                      if (bSort == 0)
                        {
                          oldIndex[i] = (j+1);
                        }
                          bSort = 0;
                        }
          }
    }
  // ** SORTING COMPLETE, ADD NEW ROWS TO BASE OF TABLE ....
  for (i=0; i<oldIndex.length; i++)
    {
      newRow = tableToSort.insertRow();
      for (c=0; c<tableToSort.cols; c++)
        {
          newCell = newRow.insertCell();
          newCell.innerHTML = tableToSort.rows(oldIndex[i]).cells(c).innerHTML;
        }
      }
  //MOVE NEW ROWS TO TOP OF TABLE ....
  for (i=1; i<totalRows; i++)
    {
      tableToSort.moveRow((tableToSort.rows.length -1),1);
    }
  //DELETE THE OLD ROWS FROM THE BOTTOM OF THE TABLE ....
  for (i=1; i<totalRows; i++)
    {
      tableToSort.deleteRow();
    }
  }
//  End -->
</script>
HTML
if ($guild{'6'} eq "Gold\n") {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/$INPUT{'guild'}.css">
HTML
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}
print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body onload="javascript:sortTable(0, rsTable);">
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD></TD>
</TR>
</TABLE>
</DIV>

<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML

&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
<BR>
<CENTER>
Item's in out Valt<BR>
<SMALL>(clicking on the coloum headers will sort the list)</SMALL>
  <TABLE BORDER=0 CELLSPACING="2" CELLPADDING="2" ALIGN="Center" WIDTH="75%" name="rsTable" id=rsTable cols=3>
<TR><TD><A HREF="javascript:sortTable(0, rsTable);"><B><FONT COLOR=black>Name</A></TD>
<TD><A HREF="javascript:sortTable(1, rsTable);"><B><FONT COLOR=black>Price</A></TD>
<TD><A HREF="javascript:sortTable(2, rsTable);"><B><FONT COLOR=black>Qty</A></TD>
</TR>
HTML

open (DATA, "data/$INPUT{'guild'}.valt");
	@data = <DATA>;

foreach $line (@data) {
	chomp ($line);
	($name, $price, $qty, $slot) = split(/::/, $line);
print <<"HTML";
<TR>
<TD width=50%><A HREF="$siteurl/?do=viewitem&name=$name&slot=$slot" onclick="NewWindow(this.href,'item','400','200','yes');return false;"><FONT COLOR=black>$name</FONT></A></TD>
<TD>$price</TD>
<TD>$qty</TD>
</TR>
HTML
}
close DATA;

print <<"HTML";
</TABLE>
<P>
HTML
&banner;
print <<"HTML";
</TD></TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</DIV>
</BODY></HTML>
HTML
}

##################################################################################

sub deleteitem {

open (DATA, "data/$INPUT{'guild'}.valt");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'guild'}.valt");
foreach $line (@data) {
	chomp ($line);
	($name, $price, $qty, $slot) = split(/::/, $line);
     if ($name eq "$INPUT{'name'}") {
	print DATA "";
     }
     else {

          print DATA "$line\n";
     }
}
close DATA;


$tag = "<B>Item Deleted</B>";
&editwindow;

}

##################################################################################

sub edititem {

print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>
HTML


open (DATA, "data/$INPUT{'guild'}.valt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
	chomp ($line);
	($name, $price, $qty, $slot) = split(/::/, $line);
     if ($name eq "$INPUT{'name'}") {
	
print <<"HTML";
<FORM ACTION="index.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name:</TD>
	<TD>$name
	  <INPUT TYPE="hidden" NAME="name" VALUE="$name"></TD>
      </TR>
      <TR>
	<TD>Price:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="price" VALUE="$price"></TD>
      </TR>
      <TR>
	<TD>Qty:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="qty" VALUE="$qty"></TD>
      </TR>
      <TR>
	<TD>Slot:</TD>
	<TD>$slot
	  <INPUT TYPE="hidden" NAME="slot" VALUE="$slot">
<INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
<INPUT TYPE="hidden" NAME="do" VALUE="saveedititem">
</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML

     }

}
print <<"HTML";
<P>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################

sub saveedititem {

open (DATA, "data/$INPUT{'guild'}.valt");
@data = <DATA>;
close DATA;
open(DATA, ">data/$INPUT{'guild'}.valt");
foreach $line (@data) {
	chomp ($line);
	($name, $price, $qty, $slot) = split(/::/, $line);
     if ($name eq "$INPUT{'name'}") {
	print DATA "$INPUT{'name'}::$INPUT{'price'}::$INPUT{'qty'}::$slot\n";
     }
     else {

          print DATA "$line\n";
     }
}
close DATA;


$tag = "<B>Item Saved</B>";
&editwindow;
}

##################################################################################

sub aprove {

open (DATA, "data/$INPUT{'guild'}.wate");
@data = <DATA>;
close DATA;
open (DATA, ">data/$INPUT{'guild'}.wate");
foreach $line (@data) {
($name, $junk) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
print DATA "";
}
else {
print DATA "$line";
}

}
close DATA;

open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;
open (DATA, ">data/$INPUT{'guild'}.mem");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'name'}::Member::Member::Member::0\n";
close DATA;

print <<"HTML";
<HTML>
<head>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

var page = "$siteurl/?guild=$INPUT{'guild'}";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

}
//  End -->
</script>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY onload=winclose() topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>


<B>$INPUT{'name'} has been aproved<BR>
<a href="#" onClick="window.close();"><B><FONT COLOR=#000000>Close</FONT></B></a>
</BODY></HTML>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub decline {
open (DATA, "data/$INPUT{'guild'}.wate");
@data = <DATA>;
close DATA;
open (DATA, ">data/$INPUT{'guild'}.wate");
foreach $line (@data) {
($name, $junk) = split(/::/, $line);
if ($name eq "$INPUT{'name'}") {
print DATA "";
}
else {
print DATA "$line";
}

}
close DATA;


$i = 0;
open (DATA, "user/$INPUT{'name'}.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$useraa{$i} = "$line";
}

open(DATA, ">user/$INPUT{'name'}.dat");
print DATA "$useraa{'1'}";
print DATA "$useraa{'2'}";
print DATA "$useraa{'3'}";
print DATA "$useraa{'4'}";
print DATA "\n";
print DATA "$useraa{'6'}";
print DATA "$useraa{'7'}";
print DATA "$useraa{'8'}";
print DATA "junk\n";
close DATA;

print <<"HTML";
<HTML>
<head>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

var page = "$siteurl/?guild=$INPUT{'guild'}";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

}
//  End -->
</script>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY onload=winclose() topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>


<B>$INPUT{'name'} has been Declined<BR>
<a href="#" onClick="window.close();"><B><FONT COLOR=#000000>Close</FONT></B></a>
</BODY></HTML>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################

sub setcounter {

print <<"HTML";
<HTML>
<HEAD>
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>

<FORM ACTION="index.cgi" METHOD="POST">

<TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
<TR><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="1" CHECKED></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/1/1.gif">
<IMG SRC="http://www.eqguilded.com/images/1/2.gif">
<IMG SRC="http://www.eqguilded.com/images/1/3.gif">
<IMG SRC="http://www.eqguilded.com/images/1/4.gif">
<IMG SRC="http://www.eqguilded.com/images/1/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="2"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/2/1.gif">
<IMG SRC="http://www.eqguilded.com/images/2/2.gif">
<IMG SRC="http://www.eqguilded.com/images/2/3.gif">
<IMG SRC="http://www.eqguilded.com/images/2/4.gif">
<IMG SRC="http://www.eqguilded.com/images/2/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="3"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/3/1.gif">
<IMG SRC="http://www.eqguilded.com/images/3/2.gif">
<IMG SRC="http://www.eqguilded.com/images/3/3.gif">
<IMG SRC="http://www.eqguilded.com/images/3/4.gif">
<IMG SRC="http://www.eqguilded.com/images/3/5.gif">
</TD></TR><TR><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="4"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/4/1.gif">
<IMG SRC="http://www.eqguilded.com/images/4/2.gif">
<IMG SRC="http://www.eqguilded.com/images/4/3.gif">
<IMG SRC="http://www.eqguilded.com/images/4/4.gif">
<IMG SRC="http://www.eqguilded.com/images/4/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="5"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/5/1.gif">
<IMG SRC="http://www.eqguilded.com/images/5/2.gif">
<IMG SRC="http://www.eqguilded.com/images/5/3.gif">
<IMG SRC="http://www.eqguilded.com/images/5/4.gif">
<IMG SRC="http://www.eqguilded.com/images/5/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="6"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/6/1.gif">
<IMG SRC="http://www.eqguilded.com/images/6/2.gif">
<IMG SRC="http://www.eqguilded.com/images/6/3.gif">
<IMG SRC="http://www.eqguilded.com/images/6/4.gif">
<IMG SRC="http://www.eqguilded.com/images/6/5.gif">
</TD></TR><TR><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="7"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/7/1.gif">
<IMG SRC="http://www.eqguilded.com/images/7/2.gif">
<IMG SRC="http://www.eqguilded.com/images/7/3.gif">
<IMG SRC="http://www.eqguilded.com/images/7/4.gif">
<IMG SRC="http://www.eqguilded.com/images/7/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="8"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/8/1.gif">
<IMG SRC="http://www.eqguilded.com/images/8/2.gif">
<IMG SRC="http://www.eqguilded.com/images/8/3.gif">
<IMG SRC="http://www.eqguilded.com/images/8/4.gif">
<IMG SRC="http://www.eqguilded.com/images/8/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="9"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/9/1.gif">
<IMG SRC="http://www.eqguilded.com/images/9/2.gif">
<IMG SRC="http://www.eqguilded.com/images/9/3.gif">
<IMG SRC="http://www.eqguilded.com/images/9/4.gif">
<IMG SRC="http://www.eqguilded.com/images/9/5.gif">
</TD></TR><TR><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="10"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/10/1.gif">
<IMG SRC="http://www.eqguilded.com/images/10/2.gif">
<IMG SRC="http://www.eqguilded.com/images/10/3.gif">
<IMG SRC="http://www.eqguilded.com/images/10/4.gif">
<IMG SRC="http://www.eqguilded.com/images/10/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="11"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/11/1.gif">
<IMG SRC="http://www.eqguilded.com/images/11/2.gif">
<IMG SRC="http://www.eqguilded.com/images/11/3.gif">
<IMG SRC="http://www.eqguilded.com/images/11/4.gif">
<IMG SRC="http://www.eqguilded.com/images/11/5.gif">
</TD><TD>
<INPUT TYPE="radio" NAME="digit" VALUE="12"></TD>
<TD>
<IMG SRC="http://www.eqguilded.com/images/12/1.gif">
<IMG SRC="http://www.eqguilded.com/images/12/2.gif">
<IMG SRC="http://www.eqguilded.com/images/12/3.gif">
<IMG SRC="http://www.eqguilded.com/images/12/4.gif">
<IMG SRC="http://www.eqguilded.com/images/12/5.gif">
</TD>
</TR></TABLE>


  <INPUT TYPE="hidden" NAME="do" VALUE="savecounter">
  <INPUT TYPE="hidden" NAME="guild" VALUE="$INPUT{'guild'}">
  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
  <INPUT TYPE=reset>
</FORM>
<P>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML

}

##################################################################################

sub savecounter {

&getuser;
&getdata;


open(DATA, ">data/$INPUT{'guild'}.dat");
print DATA "$guild{'1'}";
print DATA "$guild{'2'}";
print DATA "$guild{'3'}";
print DATA "$guild{'4'}";
print DATA "$guild{'5'}";
print DATA "$guild{'6'}";
print DATA "$guild{'7'}";
print DATA "$guild{'8'}";
print DATA "$guild{'9'}";
print DATA "$INPUT{'digit'}\n";
print DATA "junk\n";
close DATA;

$tag = "<B>Counter Image Saved</B>";
&editwindow;
}

##################################################################################

sub loadchatwin {

&getdata;

print <<"HTML";
<HTML>
<HEAD>
HTML
if ($guild{'6'} eq "Gold\n") {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/$INPUT{'guild'}.css">
HTML
}
else {
print <<"HTML";
<LINK REL="STYLESHEET" TYPE="text/css" HREF="style/defalt.css">
HTML
}
print <<"HTML";
  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>
  <TITLE>$guild{'2'}</TITLE>
</HEAD>
<BODY id=body onload="NewWindow('chat.cgi?guild=$INPUT{'guild'}','name','400','300','yes');">
<div id="wrapper">
<div id="heading">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD>
<DIV id="namea">$guild{'2'}</DIV>
<DIV id="nameb">$guild{'2'}</DIV>
</TD>
<TD></TD>
</TR>
</TABLE>
</DIV>

<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH=100%>
<TR>
<TD id="links">

HTML

&showlinks;

print <<"HTML";
</td></tr><TR><td id=main>
<DIV id=content>
<P>
<BR>
<CENTER>

Loading chat window...<BR>

<P>
HTML
&banner;
print <<"HTML";
</TD></TR>
<TR><TD id=foot>
</td></TR>
</TABLE>
</DIV>
</BODY></HTML>
HTML

}

##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub getdata {

$i = 0;
open (DATA, "data/$INPUT{'guild'}.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$guild{$i} = "$line";
}

}

##################################################################################

sub getuser {

&GetCookies('user');

$user = "$Cookies{'user'}";

$i = 0;
open (DATA, "user/$user.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$user{$i} = "$line";
}
open (DATA, "data/$INPUT{'guild'}.mem");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $accs, $ran, $typ, $pts) = split(/::/, $line);
if ($name eq "$user") {
$user{9} = "$accs";
$user{10} = "$ran";
$user{11} = "$typ";
$user{12} = "$pts";
if ($user{'9'} eq "Master") {
$user{'9'} = "Administrator";
$user{'13'} = "Master";
}
}
}

}

##################################################################################

sub showlinks {

open (DATA, "data/$INPUT{'guild'}.link");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $url, $typ) = split(/::/, $line);
if ($typ eq "1\n") {
print "<A HREF=$url id=link>$name</A> ";
}
elsif ($typ eq "2\n") {
print "<A HREF=$url id=link target=_new>$name</A> ";
}
elsif ($typ eq "3\n") {
print "<BR>";
}
}

}

##################################################################################

sub showmemnews {

open (DATA, "data/$INPUT{'guild'}.news");
@data = <DATA>;
close DATA;
print "@data";

}

##################################################################################

sub showoffnews {

open (DATA, "data/$INPUT{'guild'}.off");
@data = <DATA>;
close DATA;
print "@data";

}

##################################################################################

sub header {

if ($user eq "") {

$logbox = "$logbox <DIV id=menuboxborder>";
$logbox = "$logbox <div id=loged>You are not loged in</DIV>";
$logbox = "$logbox <A HREF=$siteurl/log.cgi?guild=$INPUT{'guild'} onclick=\"NewWindow(this.href,'name','300','150','no')\;return false\;\" id=menubox>Login</A> <A HREF=$siteurl/?signup onclick=\"NewWindow(this.href,'name','400','300','yes')\;return false\;\" id=menubox>SignUp</A>
</DIV>";

}
else {
$i = 0;
open (DATA, "user/$user.msg");
@data = <DATA>;
close DATA;
foreach $lineee (@data) {
$i = $i + 1;
}

$logbox = "$logbox <DIV id=menuboxborder>";
$logbox = "$logbox <div id=loged>You are loged in as $user{'1'} $user{'2'}</DIV>";
$logbox = "$logbox <A HREF=$siteurl/log.cgi?logout&guild=$INPUT{'guild'} onclick=\"NewWindow(this.href,'name','10','10','yes')\;return  false\;\" id=menubox>Logout</A> <A HREF=$siteurl/?editsetting&guildname=$user{'5'} onclick=\"NewWindow(this.href,'name','410','300','yes')\;return false\;\" id=menubox>Edit Setting</A> <A HREF=$siteurl/?do=messages onclick=\"NewWindow(this.href,'name','410','300','yes')\;return  false\;\" id=menubox>Message Center ($i)</A><BR><div id=raidpoints>You have $user{'12'} points avaliable.</DIV></DIV>";

}

}

##################################################################################

sub footer {

open (DATA, "data/$INPUT{'guild'}.foot");
@data = <DATA>;
close DATA;
print "@data";

}

##################################################################################

sub gettime {
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

if ($hour <= 9) {
	$hour = "0$hour";
}
$mon = $mon + 1;
$year = $year + 1900;
if ($min <= 9) {
	$min = "0$min";
}
if ($hour >= 13) {
	$hour = $hour - 12;
	$ampm = "PM";
}
else {
$ampm = "AM";
}


$date = "$mon/$mday/$year";
$datetime = "$mon/$mday/$year $hour:$min $ampm EST";

}

##################################################################################
##################################################################################

sub banner {

if ($guild{'6'} eq "Silver\n") {
print "Site Provided by <A HREF=$siteurl>EQ Guilded</A>";
}
}

##################################################################################
##################################################################################

sub checkgold {
if ($guild{'6'} eq "Gold\n") {
($emon, $emday, $eyear, $junk) = split(/\//, $guild{'5'});

if ($emday < $mday) {
if ($emon <= $mon) {
if ($eyear <= $year) {

open(DATA, ">data/$INPUT{'guild'}.dat");
print DATA "$guild{'1'}";
print DATA "$guild{'2'}";
print DATA "$guild{'3'}";
print DATA "$guild{'4'}";
print DATA "\n";
print DATA "Silver\n";
print DATA "$guild{'7'}";
print DATA "$guild{'8'}";
print DATA "$guild{'9'}";
print DATA "$guild{'10'}";
print DATA "junk\n";
close DATA;
}
}
}


}
}

##################################################################################

sub watelist {
print <<"HTML";
<CENTER><B>Member's Wateing to be aproved!<BR>
<TABLE BORDER="0" CELLPADDING="2" WIDTH="50%" BGCOLOR="#265833">
  <TR>
    <TD BGCOLOR="#008040"><CENTER><FONT COLOR=#ffffff><B>Name</B></FONT></TD>
    <TD BGCOLOR="#008040"><CENTER><FONT COLOR=#ffffff><B>Aprove</B></FONT></TD>
    <TD BGCOLOR="#008040"><CENTER><FONT COLOR=#ffffff><B>Decline</B></FONT></TD>
  </TR>
HTML

open (DATA, "data/$INPUT{'guild'}.wate");
@data = <DATA>;
close DATA;
foreach $line (@data) {
($name, $junk) = split(/::/, $line);
print <<"HTML";
  <TR>
    <TD><FONT COLOR=#ffffff>$name</FONT></TD>
    <TD><CENTER><A HREF=$siteurl/?guild=$INPUT{'guild'}&do=aprove&name=$name onclick="NewWindow(this.href,'name','200','100','yes');return false;"><FONT COLOR=#ffffff>Aprove</FONT></A></TD>
    <TD><CENTER><A HREF=$siteurl/?guild=$INPUT{'guild'}&do=decline&name=$name onclick="NewWindow(this.href,'name','200','100','yes');return false;"><FONT COLOR=#ffffff>Decline</FONT></A></TD>
  </TR>
HTML
}
print <<"HTML";
</TABLE>
HTML
}


##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################
##################################################################################

sub resettopfive {
###MEMBERS
$topone = 0;
$toptwo = 0;
$topthere = 0;
$topfour = 0;
$topfive = 0;

$topone{'2'} = "N/A";
$toptwo{'2'} = "N/A";
$topthere{'2'} = "N/A";
$topfour{'2'} = "N/A";
$topfive{'2'} = "N/A";

open (DATA, "guilds.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {

($name, $server, $junk) = split(/::/, $line);

$cnt = 0;
open (DATA, "data/$name.mem");
@dataaa = <DATA>;
close DATA;

foreach $line (@dataaa) {
$cnt++;
}



if ($cnt >= $topone) {

$topfive = $topfour;
$topnamfive = "$topnamfour";
$topfour = $topthere;
$topnamfour = "$topnamthere";
$topthere = $toptwo;
$topnamthere = "$topnamtwo";
$toptwo = $topone;
$topnamtwo = "$topnamone";

$topone = $cnt;
$topnamone = "$name";

}

elsif ($cnt >= $toptwo) {

$topfive = $topfour;
$topnamfive = "$topnamfour";
$topfour = $topthere;
$topnamfour = "$topnamthere";
$topthere = $toptwo;
$topnamthere = "$topnamtwo";

$toptwo = $cnt;
$topnamtwo = "$name";

}

elsif ($cnt >= $topthere) {

$topfive = $topfour;
$topnamfive = "$topnamfour";
$topfour = $topthere;
$topnamfour = "$topnamthere";

$topthere = $cnt;
$topnamthere = "$name";

}

elsif ($cnt >= $topfour) {

$topfive = $topfour;
$topnamfive = "$topnamfour";

$topfour = $cnt;
$topnamfour = "$name";

}

elsif ($cnt >= $topfive) {

$topfive = $cnt;
$topnamfive = "$name";

}

}


$i = 0;
open (DATA, "data/$topnamone.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topone{$i} = "$line";
}

if ($topnamtwo ne "") {
$i = 0;
open (DATA, "data/$topnamtwo.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$toptwo{$i} = "$line";
}
}
if ($topnamthere ne "") {
$i = 0;
open (DATA, "data/$topnamthere.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topthere{$i} = "$line";
}
}
if ($topnamfour ne "") {
$i = 0;
open (DATA, "data/$topnamfour.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topfour{$i} = "$line";
}
}
if ($topnamfive ne "") {
$i = 0;
open (DATA, "data/$topnamfive.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topfive{$i} = "$line";
}
}

open(DATA, ">tenmem.dat");
print DATA "<A HREF=$siteurl/?guild=$topnamone target=_top><FONT COLOR=#ffffff size=2><B>$topone{'2'} ";
print DATA "($topone)</B></FONT></A><BR>\n";
if ($topnamtwo ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamtwo target=_top><FONT COLOR=#ffffff size=2><B>$toptwo{'2'} ";
print DATA "($toptwo)</B></FONT></A><BR>\n";
}
if ($topnamthere ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamthere target=_top><FONT COLOR=#ffffff size=2><B>$topthere{'2'} ";
print DATA "($topthere)</B></FONT></A><BR>\n";
}
if ($topnamfour ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamfour target=_top><FONT COLOR=#ffffff size=2><B>$topfour{'2'} ";
print DATA "($topfour)</B></FONT></A><BR>\n";
}
if ($topnamfive ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamfive target=_top><FONT COLOR=#ffffff size=2><B>$topfive{'2'} ";
print DATA "($topfive)</B></FONT></A><BR>\n";
}
close DATA;


####VISITS

$topone = "0";
$toptwo = "0";
$topthere = "0";
$topfour = "0";
$topfive = "0";

$topone{'2'} = "";
$toptwo{'2'} = "";
$topthere{'2'} = "";
$topfour{'2'} = "";
$topfive{'2'} = "";

$topfive = "";
$topnamfive = "";
$topfour = "";
$topnamfour = "";
$topthere = "";
$topnamthere = "";
$toptwo = "";
$topnamtwo = "";
$topone = "";
$topnamone = "";


open (DATA, "counters.db");
@data = <DATA>;
close DATA;
foreach $line (@data) {

$name = "";
$cnt = 0;

($name, $cnt, $junk, $junkt) = split(/\|/, $line);

if ($cnt >= $topone) {

$topfive = $topfour;
$topnamfive = "$topnamfour";
$topfour = $topthere;
$topnamfour = "$topnamthere";
$topthere = $toptwo;
$topnamthere = "$topnamtwo";
$toptwo = $topone;
$topnamtwo = "$topnamone";

$topone = $cnt;
$topnamone = "$name";

}

elsif ($cnt >= $toptwo) {

$topfive = $topfour;
$topnamfive = "$topnamfour";
$topfour = $topthere;
$topnamfour = "$topnamthere";
$topthere = $toptwo;
$topnamthere = "$topnamtwo";

$toptwo = $cnt;
$topnamtwo = "$name";

}

elsif ($cnt >= $topthere) {

$topfive = $topfour;
$topnamfive = "$topnamfour";
$topfour = $topthere;
$topnamfour = "$topnamthere";

$topthere = $cnt;
$topnamthere = "$name";

}

elsif ($cnt >= $topfour) {

$topfive = $topfour;
$topnamfive = "$topnamfour";

$topfour = $cnt;
$topnamfour = "$name";

}

elsif ($cnt >= $topfive) {

$topfive = $cnt;
$topnamfive = "$name";

}

}


$i = 0;
open (DATA, "data/$topnamone.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topone{$i} = "$line";
}

if ($topnamtwo ne "") {
$i = 0;
open (DATA, "data/$topnamtwo.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$toptwo{$i} = "$line";
}
}
if ($topnamthere ne "") {
$i = 0;
open (DATA, "data/$topnamthere.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topthere{$i} = "$line";
}
}
if ($topnamfour ne "") {
$i = 0;
open (DATA, "data/$topnamfour.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topfour{$i} = "$line";
}
}
if ($topnamfive ne "") {
$i = 0;
open (DATA, "data/$topnamfive.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;
$topfive{$i} = "$line";
}
}

open(DATA, ">tenvit.dat");
print DATA "<A HREF=$siteurl/?guild=$topnamone target=_top><FONT COLOR=#ffffff size=2><B>$topone{'2'} ";
print DATA "($topone)</B></FONT></A><BR>\n";

if ($topnamtwo ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamtwo target=_top><FONT COLOR=#ffffff size=2><B>$toptwo{'2'} ";
print DATA "($toptwo)</B></FONT></A><BR>\n";
}
if ($topnamthere ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamthere target=_top><FONT COLOR=#ffffff size=2><B>$topthere{'2'} ";
print DATA "($topthere)</B></FONT></A><BR>\n";
}
if ($topnamfour ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamfour target=_top><FONT COLOR=#ffffff size=2><B>$topfour{'2'} ";
print DATA "($topfour)</B></FONT></A><BR>\n";
}
if ($topnamfive ne "") {
print DATA "<A HREF=$siteurl/?guild=$topnamfive target=_top><FONT COLOR=#ffffff size=2><B>$topfive{'2'} ";
print DATA "($topfive)</B></FONT></A><BR>\n";
}
close DATA;

print "Top 5 Reset";
}