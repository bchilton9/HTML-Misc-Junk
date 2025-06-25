#!/usr/bin/perl

###############################################

require 'cookie.lib';
use DBI;

###############################################

$home = "http://www.eqguilded.com/cgi-bin/main.cgi";

###############################################

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

#####################
### IF ELSIF ELSE ###
#####################

if ($INPUT{'do'} eq "login") { &login; }
elsif ($INPUT{'do'} eq "logout") { &logout; }
elsif ($INPUT{'do'} eq "edit") { &edit; }
elsif ($INPUT{'do'} eq "editb") { &editb; }
elsif ($INPUT{'do'} eq "delete") { &delete; }
elsif ($INPUT{'do'} eq "whois") { &whois; }
elsif ($INPUT{'do'} eq "create") { &create; }
elsif ($INPUT{'do'} eq "settings") { &settings; }
elsif ($INPUT{'do'} eq "settingsb") { &settingsb; }
elsif ($INPUT{'do'} eq "signup") { &signup; }
elsif ($INPUT{'do'} eq "signupb") { &signupb; }
elsif ($INPUT{'do'} eq "actavate") { &actavate; }
elsif ($INPUT{'do'} eq "domains") { &domains; }
else { &main; }

#################
### MAIN SUBS ###
#################

###############################################
sub login {
###############################################

$done = "0";
$user = "$INPUT{'user'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_vs3:localhost","eqguilded","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 


$temp ="SELECT * FROM `users` WHERE `username` = '$user' limit 1";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

      if ($INPUT{'pass'} eq "$row[2]") {

 if ($INPUT{'rember'} eq "on") {
         &SetCookiesSave('user',"$user");
         &SetCookiesSave('pass',"$INPUT{'pass'}");
}
else {
         &SetCookies('user',"$user");
         &SetCookies('pass',"$INPUT{'pass'}");
}

$done = "1";

print "Content-type: text/html\n\n";
print qq~
<HTML>
<HEAD>
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$home">
<TITLE>EQGuilded.com - Please wate.</TITLE>
</HEAD>
<BODY>
Please wate or click <A HREF="$home">here</A>.
</BODY>
</HTML>
~;


      }
else {
$done = "1";
&header;
print qq~
Invalid Password<BR>
Please try agine.<BR>
~;
&loginform;
&footer;

}

 } 

}

if ($done eq "0") { 

&header;
print qq~
Loggin Failed<BR>
Please try agine.<BR>
~;
&loginform;
&footer;

} 



$sth->finish; 
$dbh->disconnect; 


}

###############################################
sub logout {
###############################################

   &SetCookies('user',"");
   &SetCookies('pass',"");

print "Content-type: text/html\n\n";
print qq~
<HTML>
<HEAD>
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$home">
<TITLE>EQGuilded.com - Please wate.</TITLE>
</HEAD>
<BODY>
Please wate or click <A HREF="$home">here</A>.
</BODY>
</HTML>
~;

}

###############################################
#sub edit {
###############################################
#}

###############################################
#sub editb {
###############################################
#}

###############################################
#sub delete {
###############################################
#}

###############################################
sub whois {
###############################################

$whois = "$INPUT{'whois'}.$INPUT{'domain'}";

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_vs3:localhost","eqguilded","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM `domains` WHERE name = '$whois'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$taken = "$row[0]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

if ($taken ne "") {
&header;

print qq~
$whois is not Available<BR>
<P>
<B>Try a diffrent Subdomain!</B>
<P>
Please enter subdomain to search: (<FONT
COLOR="red"><U>subdomain</U></FONT>
.eqguilded.com)<BR>
<FORM>
http://<INPUT TYPE="TEXT" SIZE="20" NAME="whois">.eqguilded.com<BR>
<INPUT TYPE="HIDDEN" NAME="do" value="whois">
<INPUT TYPE="HIDDEN" NAME="domain" value="eqguilded.com">
<INPUT TYPE="submit" NAME="submit" VALUE="Register/Check Name">
</FORM>
~;

&footer;
}

else {
&header;

print qq~
$whois is Available<BR>
<FORM>
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Subdomain:</TD>
	<TD>$whois<INPUT TYPE="hidden" name="whois" value="$whois"></TD>
      </TR>
      <TR>
	<TD>Forward to:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="forward" VALUE="http://"></TD>
      </TR>
      <TR>
	<TD>Type:</TD>
	<TD>
	  <SELECT NAME="type">

	  <OPTION VALUE="0">Banner/Cloked
	  <OPTION VALUE="1">Banner/Uncloked
	  <OPTION VALUE="2">Banner/Frame
	  <OPTION VALUE="3">Banner/Delay-Page

</SELECT>
</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Register"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;

&footer;
}

}

###############################################
#sub create {
###############################################
#}

###############################################
#sub settings {
###############################################
#}

###############################################
#sub settingsb {
###############################################
#}

###############################################
sub main {
###############################################

&GetCookies('user');

$user = "$Cookies{'user'}";

&header;

print qq~
OPEN AND PRINT MAIN CONTENT
~;

&footer;

}

###############################################
#sub signup {
###############################################
#}

###############################################
#sub signupb {
###############################################
#}

###############################################
#sub actavate {
###############################################
#}

###############################################
sub domains {
###############################################

$num = 0;

&GetCookies('user');

$user = "$Cookies{'user'}";

&header;

print qq~
Subdomain List:<BR>
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" WIDTH="100%" ALIGN="Center">
    <TR>
      <TD BGCOLOR="#0000ff"><FONT COLOR="#FFFFFF">Subdomain:</FONT></TD>
      <TD BGCOLOR="#0000ff"><FONT COLOR="#FFFFFF">Forward:</FONT></TD>
      <TD BGCOLOR="#0000ff"><FONT COLOR="#FFFFFF">Type:</FONT></TD>
      <TD BGCOLOR="#0000ff" WIDTH="10%"></TD>
      <TD BGCOLOR="#0000ff" WIDTH="10%"></TD>
      <TD BGCOLOR="#0000ff" WIDTH="10%"></TD>
    </TR>
~;

my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_vs3:localhost","eqguilded","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM `domains` WHERE owner = '$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;


if ($row[2] eq "1") { $type = "Banner/Uncloked"; }
elsif ($row[2] eq "2") { $type = "Banner/Frame"; }
elsif ($row[2] eq "3") { $type = "Banner/Delay-Page"; }
elsif ($row[2] eq "4") { $type = "Cloked"; }
elsif ($row[2] eq "5") { $type = "Uncloked"; }
else { $type = "Banner/Cloked"; }

$ num = $num + 1;

print qq~
    <TR>
      <TD BGCOLOR="#cfcfcf"><A HREF="http://$row[0]" TARGET="_new">$row[0]</A></TD>
      <TD BGCOLOR="#cfcfcf"><A HREF="$row[4]" TARGET="_new">$row[4]</A></TD>
      <TD BGCOLOR="#cfcfcf">$type</TD>
      <TD BGCOLOR="#cfcfcf"><CENTER><A HREF="?do=edit&domain=$row[0]">Edit</A></TD>
      <TD BGCOLOR="#cfcfcf"><CENTER><A HREF="?do=delete&domain=$row[0]">Delete</A></TD>
      <TD BGCOLOR="#cfcfcf"><CENTER>PayPal</TD>
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

if ($num eq 0) {
print qq~
<I>You have no Subdomains.</I><BR>
~;
}

print qq~
<P>
<B>Register a Subdomain!</B>
<P>
Please enter subdomain to search: (<FONT
COLOR="red"><U>subdomain</U></FONT>
.eqguilded.com)<BR>
<FORM>
http://<INPUT TYPE="TEXT" SIZE="20" NAME="whois">.eqguilded.com<BR>
<INPUT TYPE="HIDDEN" NAME="do" value="whois">
<INPUT TYPE="HIDDEN" NAME="domain" value="eqguilded.com">
<INPUT TYPE="submit" NAME="submit" VALUE="Register/Check Name">
</FORM>
~;

&footer;

}

################
### SUB SUBS ###
################

###############################################
sub header {
###############################################

&GetCookies('user');

$user = "$Cookies{'user'}";

print "Content-type: text/html\n\n";

print qq~
<HTML>
<HEAD>
  <TITLE>EQGuilded.com</TITLE>
</HEAD>
<BODY BGCOLOR="#8080ff">
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="600" BGCOLOR="#FFFFFF" HEIGHT="100%">
    <TR>
      <TD BACKGROUND="http://www.eqguilded.com/line.jpg"><CENTER>
	  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
	    <TR>
	      <TD VALIGN="Top"><A HREF="?"><IMG SRC="http://www.eqguilded.com/eqglogo.gif" WIDTH="318" HEIGHT="62" BORDER="0"></A></TD>
	      <TD VALIGN="Top">
~;

if ($user ne "") { &logedin; }
else { &loginform; }

print qq~
           </TD>
	    </TR>
	  </TABLE>
	</CENTER>
      </TD>
    </TR>
    <TR>
      <TD HEIGHT="100%"><CENTER>
	  <TABLE BORDER="0" CELLSPACING="2" CELLPADDING="2" ALIGN="Center" WIDTH="100%"  HEIGHT="100%">
	    <TR>
	      <TD VALIGN="Top">
~;

}

###############################################
sub footer {
###############################################

print qq~
             </TD>
	    </TR>
	  </TABLE>
	</CENTER>
      </TD>
    </TR>
  </TABLE>
</CENTER>
</BODY></HTML>
~;

}

###############################################
sub loginform {
###############################################

print qq~
<FORM>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
    <TR>
      <TD><SMALL><I>User:</I></SMALL></TD>
      <TD><SMALL><I>Pass:</I></SMALL></TD>
      <TD></TD>
    </TR>
    <TR>
      <TD>
	<INPUT TYPE="text" NAME="user" SIZE="7"></TD>
      <TD>
	<INPUT TYPE="password" NAME="pass" SIZE="7"></TD>
      <TD><INPUT TYPE="hidden" NAME="do" VALUE="login"><INPUT TYPE=submit VALUE="Log in"></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><INPUT TYPE="checkbox" NAME="rember" VALUE="on" CHECKED><SMALL><I>Rember me!</I></SMALL></TD>
      <TD><A HREF="?do=signup"><SMALL><I>Sign Up</I></SMALL></A></TD>
    </TR>
  </TABLE>
</FORM>
~;

}

###############################################
sub logedin {
###############################################

print qq~
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="2">
  <TR>
    <TD COLSPAN=3><BR><SMALL><B>Loged in as $user!</SMALL></B></TD>
  </TR>
 <TR>
    <TD><P ALIGN=Center>
      <A HREF="?do=options"><SMALL>Options</SMALL></A></TD>
    <TD><P ALIGN=Center>
      <A HREF="?do=domains"><SMALL>Domains</SMALL></A></TD>
    <TD><P ALIGN=Center>
      <A HREF="?do=logout"><SMALL>Log out</SMALL></A></TD>
  </TR>
  <TR>
    <TD COLSPAN=3><BR></TD>
  </TR>
</TABLE>
~;

}