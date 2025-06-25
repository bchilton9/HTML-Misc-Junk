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

##################################################################################

$siteurl = "http://66.129.123.149/~eqguild";

##################################################################################

if ($INPUT{'login'} eq "NULL") { 

$user = "$INPUT{'user'}";

$i = 0;
open (DATA, "user/$user.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chop ($line);
$i = $i + 1;
$user{$i} = "$line";
}

   if ($user{'1'} eq "") { 
      print "Content-type: text/html\n\n";
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded Login</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" height=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER><B>Username error!!</B><BR>
<a href="#" onClick="history.go(-1)"><B><FONT COLOR=#000000>&lt; Back</FONT></B></a>
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
   else { 
      if ($INPUT{'password'} eq "$user{'3'}") { 
         &SetCookies('user',"$user");
         &SetCookies('pass',"$INPUT{'password'}");
         print "Content-type: text/html\n\n";
         print "\n";


print <<"HTML";
<HTML>
<head>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {

HTML

if ($INPUT{'guild'} eq "") {
print <<"HTML";
var page = "$siteurl/?main";
HTML
}
else {
print <<"HTML";
var page = "$siteurl/?guild=$INPUT{'guild'}";
HTML
}

print <<"HTML";

windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

window.close();

}
//  End -->
</script>
</HEAD>
<BODY onload=winclose()>

</BODY></HTML>
HTML
         exit;
      }
      else {
         print "Content-type: text/html\n\n";
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded Login</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" height=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER><B>Password error!!</B><BR>
<a href="#" onClick="history.go(-1)"><B><FONT COLOR=#000000>&lt; Back</FONT></B></a>
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
}

##################################################################################

elsif ($INPUT{'logout'} eq "NULL") { 
   &SetCookies('user',"");
   &SetCookies('pass',"");
   print "Content-type: text/html\n\n";
   print "\n";

print <<"HTML";
<HTML>
<head>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function winclose() {
HTML

if ($INPUT{'guild'} eq "") {
print <<"HTML";
var page = "$siteurl/?main";
HTML
}
else {
print <<"HTML";
var page = "$siteurl/?guild=$INPUT{'guild'}";
HTML
}

print <<"HTML";
windowprops = "height=500,width=500,location=no,"
+ "scrollbars=no,menubars=no,toolbars=no,resizable=yes";

window.open(page, "main", windowprops);

window.close();

}
//  End -->
</script>
</HEAD>
<BODY onload=winclose()>

</BODY></HTML>
HTML

   exit;
}


##################################################################################

else {
print "Content-type: text/html\n\n";
print <<"HTML";
<HTML>
<HEAD>
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
  <TITLE>EQ Guilded Login</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%">
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
      <FORM>
	<CENTER>
	  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
	    <TR>
	      <TD><B>Username:</B></TD>
	      <TD>
		<INPUT TYPE="text" NAME="user" onBlur="this.value=ignoreSpaces(this.value);"  onChange="javascript:this.value=this.value.toLowerCase();"></TD>
	    </TR>
	    <TR>
	      <TD><B>Password:</B></TD>
	      <TD>
		<INPUT TYPE="password" NAME="password" onBlur="this.value=ignoreSpaces(this.value);"  onChange="javascript:this.value=this.value.toLowerCase();"></TD>
	    </TR>
	    <TR>
	      <TD COLSPAN=2><P ALIGN=Center>
		<INPUT type=hidden name=login value=NULL> 
		<INPUT TYPE=submit value=Submit> &nbsp; 
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