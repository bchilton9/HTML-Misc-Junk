#!/usr/bin/perl

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

print "Content-type: text/html\n\n";


if ($INPUT{'name'} eq "") {
print <<"HTML";
<CENTER>There has been an error<BR>
Please go to <A HREF=http://www.ravensofdispair.com>The Main Page</A> and log in
HTML
}

else {
open (DATA, "turn.txt");
@data = <DATA>;
close DATA;
open(DATA, ">turn.txt");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'name'}\n";
close DATA;
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>Ravens Of Dispair</TITLE>
</HEAD>
<BODY BGCOLOR="#000000" TEXT="#ffffff" LINK="#ffffff" VLINK="#ffffff">
<TABLE BORDER=2 CELLSPACING="1" WIDTH=100% BORDERCOLOR=blue>
  <TR>
    <TD><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR VALIGN="Top">
	  <TD ROWSPAN=2><IMG SRC="http://www.ravensofdispair.com/header.gif" WIDTH="451"
		HEIGHT="135"></TD>
	  <TD WIDTH=70% BGCOLOR="#ffffff">
	      <P ALIGN=Right>
<FONT COLOR=#000000><B>Hello
 keny<BR></FONT>
	  </TD>
	  <TD BGCOLOR="#ffffff"><IMG SRC="http://www.ravensofdispair.com/spacer.gif"
		WIDTH="19" HEIGHT="93"></TD>
	</TR>
	<TR>
	  <TD BGCOLOR="#0008AD"><P ALIGN=Right><A HREF=admin.cgi?a=login&name=keny&password=0519aa>Main Page</A> |
	    <A HREF="http://www.erenetwork.com/ravens/cgi/memlist.cgi?name=keny">Member List</A></TD>
	  <TD BGCOLOR="#0008AD"><IMG SRC="http://www.ravensofdispair.com/spacer2.gif"
		WIDTH="19" HEIGHT="41"></TD>
	</TR>
	<TR>
	  <TD COLSPAN=3><TABLE BORDER BORDERCOLOR=#0008ad CELLPADDING="2" WIDTH=100%>
	      <TR>
		<TD WIDTH=15%><IMG SRC="http://www.ravensofdispair.com/dragons of Elfwood.gif"
		      WIDTH="161" HEIGHT="450"></TD>
		<TD VALIGN="Top"><P ALIGN=Center>
		  <!-- start main content -->
<CENTER>You are now signed up for the turnament<BR>
<A HREF=admin.cgi?a=login&name=$INPUT{'name'}&password=$INPUT{'password'}>Main Page</A>
HTML
}