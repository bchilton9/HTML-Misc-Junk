#!/usr/bin/perl

##############

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

if ($INPUT{'e'} eq "400") { $error = "400 Error: Bad Request"; }
elsif ($INPUT{'e'} eq "401") { $error = "401 Error: Authorization Required"; }
elsif ($INPUT{'e'} eq "403") { $error = "403 Error: Forbidden"; }
elsif ($INPUT{'e'} eq "404") { $error = "404 Error: File Not Found"; }
elsif ($INPUT{'e'} eq "405") { $error = "405 Error: Method Not Allowed"; }
elsif ($INPUT{'e'} eq "500") { $error = "500 Error: Internal Server Error"; }
elsif ($INPUT{'e'} eq "501") { $error = "501 Error: Method Not Implemented"; }
else { $error = "Unknown Error"; }

print "Content-type: text/html\n\n";

print qq~
<HTML>
<HEAD>
  <TITLE>Sanctuary - $error</TITLE>
</HEAD>
<BODY BGCOLOR="#000000" TEXT="#ffffff" LINK="#ffffff" VLINK="#ffffff">
<Center>
<B>$error</B><BR>
  <HR COLOR=blue>

<IMG SRC="http://www.sanctuaryeq2.com/images/duh.jpg">

  <HR COLOR=blue>
<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi"><B>Return to the Sanctuary Home Page!</B></A><BR>
<BR>
<!-- <B>This error has been loged and will be corrected as soon as possable.</B> -->
<B>Please report this error to Linkk!</B>
</CENTER>
</BODY></HTML>

~;

