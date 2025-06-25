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

print "Content-type: text/html\n\n";


if ($INPUT{'num'} eq "") {
$tag = "We're sorry, but this topic is currently unavailable!";
}

else {

open (DATA, "help/$INPUT{'num'}.hlp");
@data = <DATA>;
close DATA;
$data = "@data";


if ($data eq "") {

$tag = "We're sorry, but this topic is currently unavailable!";

}

else {

$tag = "$data";

}

}

print <<"HTML";
<HTML>
<HEAD>
  <TITLE>EQ Guilded Help</TITLE>
</HEAD>
<BODY BGCOLOR="#a5f8fe">
<CENTER><B><BIG>EQ Guilded Help</BIG></B></CENTER>
  <HR>
$tag
<HR>
<CENTER>
<a href="#" onClick="window.close();"><B><FONT COLOR=#000000>Close Window</FONT></B></a>
</BODY></HTML>
HTML
