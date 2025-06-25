#!/usr/bin/perl

print "Content-type: text/html\n\n";
open (DATA, "head.txt");
@data = <DATA>;
close DATA;
foreach $line (@data) {
print "$line";
}


print "<BIG><B>Leaders</B></BIG><BR><CENTER><TABLE BORDER BORDERCOLOR=0000ff CELLPADDING=2 ALIGN=Center WIDTH=400><TR>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Name</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Race</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Class</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Rank</FONT></TD></TR>\n";



open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "Head Leader") {
print "<TR>\n";
print "<TD><B>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "</TR>\n";
}
}
}
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "1st Leader") {
print "<TR>\n";
print "<TD><B>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "</TR>\n";
}
}
}
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "2nd Leader") {
print "<TR>\n";
print "<TD><B>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "</TR>\n";
}
}
}
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "3rd Leader") {
print "<TR>\n";
print "<TD><B>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "</TR>\n";
}
}
}
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "4th Leader") {
print "<TR>\n";
print "<TD><B>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "</TR>\n";
}
}
}
open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "5th Leader") {
print "<TR>\n";
print "<TD><B>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "<TD>$rank</TD>\n";
print "</TR>\n";
}
}
}

print "</TABLE></CENTER><P><BR><CENTER><BIG><B>Oscar</B></BIG><BR>";
print "<CENTER><TABLE BORDER BORDERCOLOR=0000ff CELLPADDING=2 ALIGN=Center WIDTH=400><TR>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Name</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Race</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Class</FONT></TD>\n";

open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "Oscar") {
print "<TR>\n";
print "<TD><b>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "</TR>\n";
}
}
}


print "</TABLE></CENTER><P><BR><BIG><B>Ravens</B></BIG><BR>";
print "<CENTER><TABLE BORDER BORDERCOLOR=0000ff CELLPADDING=2 ALIGN=Center WIDTH=400><TR>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Name</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Race</FONT></TD>\n";
print "<TD BGCOLOR=0000ff><FONT COLOR=ffffff>Class</FONT></TD>\n";

open (DATA, "data.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($name, $pass, $email, $race, $class, $rank, $aprov) = split(/::/, $line);
if ($aprov eq "V") {
if ($rank eq "Raven") {
print "<TR>\n";
print "<TD><B>$name</B></TD>\n";
print "<TD>$race</TD>\n";
print "<TD>$class</TD>\n";
print "</TR>\n";
}
}
}


print "</TABLE></CENTER>";