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
    $INPUT{$name} = $value;
}

##################################################################################

open (FILE, "config.pl");
flock (FILE, 2);
$guildname = <FILE>;
chop ($guildname);
$email = <FILE>;
chop ($email);
$cgipath = <FILE>;
chop ($cgipath);
$imgpath = <FILE>;
chop ($imgpath);
$upload_dir = <FILE>;
chop ($upload_dir);
$sitepath = <FILE>;
chop ($sitepath);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$egga = "false";
$eggb = "false";
$eggc = "false";
$eggd = "false";
$egge = "false";
$eggf = "false";
$eggg = "false";
$eggh = "false";
$eggi = "false";
$eggj = "false";

&GetCookies('user');
&GetCookies('pass');

print "Content-type: text/html\n\n";

open (DATA, "headB.txt");
@data = <DATA>;
close DATA;

print "@data";

if ($INPUT{'a'} eq "egg") { &egg }
elsif ($INPUT{'a'} eq "stats") { &stats; }
elsif ($INPUT{'a'} eq "statsall") { &statsall; }
elsif ($INPUT{'a'} eq "giveprize") { &giveprize; }

##################################################################################

sub egg {
$done = "no";

print <<"HTML";
<IMG SRC=turkey.gif><BR>
a Wild Turkey has been slan by $Cookies{'user'}.
HTML

open (DATA, "egg.dat");
@data = <DATA>;
close DATA;
open(DATA, ">egg.dat");
foreach $line (@data) {
chomp ($line);
($usr) = split(/::/, $line);
if ($usr eq "$Cookies{'user'}") {
$done = "yes";
}
print DATA "$line\n";
}
if ($done eq "no") {
print DATA "$Cookies{'user'}\n";

open(DATAA, ">egg/$Cookies{'user'}");
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "false\n";
print DATAA "junk\n";
close DATAA;
}
close DATA;


open (FILE, "egg/$Cookies{'user'}");
flock (FILE, 2);
$egga = <FILE>;
chop ($egga);
$eggb = <FILE>;
chop ($eggb);
$eggc = <FILE>;
chop ($eggc);
$eggd = <FILE>;
chop ($eggd);
$egge = <FILE>;
chop ($egge);
$eggf = <FILE>;
chop ($eggf);
$eggg = <FILE>;
chop ($eggg);
$eggh = <FILE>;
chop ($eggh);
$eggi = <FILE>;
chop ($eggi);
$eggj = <FILE>;
chop ($eggj);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

if ($INPUT{'page'} eq "main") { $egga = "true"; }
if ($INPUT{'page'} eq "char") { $eggb = "true"; }
if ($INPUT{'page'} eq "rost") { $eggc = "true"; }
if ($INPUT{'page'} eq "phot") { $eggd = "true"; }
if ($INPUT{'page'} eq "borda") { $egge = "true"; }
if ($INPUT{'page'} eq "bordb") { $eggf = "true"; }
if ($INPUT{'page'} eq "stat") { $eggg = "true"; }
if ($INPUT{'page'} eq "dbego") { $eggh = "true"; }
if ($INPUT{'page'} eq "sett") { $eggi = "true"; }
if ($INPUT{'page'} eq "prof") { $eggj = "true"; }

open(DATAA, ">egg/$Cookies{'user'}");
print DATAA "$egga\n";
print DATAA "$eggb\n";
print DATAA "$eggc\n";
print DATAA "$eggd\n";
print DATAA "$egge\n";
print DATAA "$eggf\n";
print DATAA "$eggg\n";
print DATAA "$eggh\n";
print DATAA "$eggi\n";
print DATAA "$eggj\n";
print DATAA "junk\n";
close DATAA;

} #end sub egg

##################################################################################

sub stats {

$cnt = 0;

open (FILE, "egg/$Cookies{'user'}");
flock (FILE, 2);
$egga = <FILE>;
chop ($egga);
$eggb = <FILE>;
chop ($eggb);
$eggc = <FILE>;
chop ($eggc);
$eggd = <FILE>;
chop ($eggd);
$egge = <FILE>;
chop ($egge);
$eggf = <FILE>;
chop ($eggf);
$eggg = <FILE>;
chop ($eggg);
$eggh = <FILE>;
chop ($eggh);
$eggi = <FILE>;
chop ($eggi);
$eggj = <FILE>;
chop ($eggj);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

if ($egga eq "true") { $cnt = $cnt + 1; }
if ($eggb eq "true") { $cnt = $cnt + 1; }
if ($eggc eq "true") { $cnt = $cnt + 1; }
if ($eggd eq "true") { $cnt = $cnt + 1; }
if ($egge eq "true") { $cnt = $cnt + 1; }
if ($eggf eq "true") { $cnt = $cnt + 1; }
if ($eggg eq "true") { $cnt = $cnt + 1; }
if ($eggh eq "true") { $cnt = $cnt + 1; }
if ($eggi eq "true") { $cnt = $cnt + 1; }
if ($eggj eq "true") { $cnt = $cnt + 1; }


print <<"HTML";
Your stats on Turkey hunt
<P>
You have slan $cnt of 10 turkeys!

HTML
}

##################################################################################

sub statsall {

open (DATA, "egg.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {

$cnt = 0;

open (FILE, "egg/$line");
flock (FILE, 2);
$egga = <FILE>;
chop ($egga);
$eggb = <FILE>;
chop ($eggb);
$eggc = <FILE>;
chop ($eggc);
$eggd = <FILE>;
chop ($eggd);
$egge = <FILE>;
chop ($egge);
$eggf = <FILE>;
chop ($eggf);
$eggg = <FILE>;
chop ($eggg);
$eggh = <FILE>;
chop ($eggh);
$eggi = <FILE>;
chop ($eggi);
$eggj = <FILE>;
chop ($eggj);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

if ($egga eq "true") { $cnt = $cnt + 1; }
if ($eggb eq "true") { $cnt = $cnt + 1; }
if ($eggc eq "true") { $cnt = $cnt + 1; }
if ($eggd eq "true") { $cnt = $cnt + 1; }
if ($egge eq "true") { $cnt = $cnt + 1; }
if ($eggf eq "true") { $cnt = $cnt + 1; }
if ($eggg eq "true") { $cnt = $cnt + 1; }
if ($eggh eq "true") { $cnt = $cnt + 1; }
if ($eggi eq "true") { $cnt = $cnt + 1; }
if ($eggj eq "true") { $cnt = $cnt + 1; }

print "$line has slan $cnt Turkeys.<BR>"
}

print <<"HTML";
<P>
<B>Prizes have been given too</B>
<P>
HTML
open (DATA, "eggprize.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
print "$line<BR>";
}
print <<"HTML";
<P>
<B>Give a prize</B>
<P>
<FORM>
  <TABLE CELLPADDING="2">
    <TR>
      <TD>There Name:</TD>
      <TD>
	<INPUT TYPE="text" NAME="name"></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<INPUT name=a value=giveprize TYPE=submit></TD>
    </TR>
  </TABLE>
</FORM>
HTML
}


##################################################################################

sub giveprize {
print <<"HTML";
$INPUT{'name'} has been added to the prize list
HTML

open (DATA, "eggprize.dat");
@data = <DATA>;
close DATA;
open(DATA, ">eggprize.dat");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'name'}\n";
close DATA;

}


##################################################################################

open (DATA, "footB.txt");
@data = <DATA>;
close DATA;

print "@data";