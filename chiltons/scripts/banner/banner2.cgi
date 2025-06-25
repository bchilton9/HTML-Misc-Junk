#!/usr/bin/perl
#######################################################
# Banner rotater copyright 1999 Byron Chilton         #
# For more scripts go to http://www.d0tt.com          #
#                    ########                         #
# View the readme to install                          #
#######################################################

$adminpass = "admin";
## Admin password
$datafile = "/usr/home/byron/public_html/cgi-bin/scripts/banner";
## File of all your data and cgi
 
################
# Stop Editing #
################
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

if($ENV{'REQUEST_METHOD'} eq "GET") {  
  if($ENV{QUERY_STRING} eq "admin") { &adminlogin }
  else { &banner }
  }
elsif($ENV{'REQUEST_METHOD'} eq "POST") {
if($INPUT{'submit'} eq "Start") { &admin }
if($INPUT{'submit'} eq "Reload main admin") { &admin }
if($INPUT{'submit'} eq "Add Banner") { &add }
if($INPUT{'submit'} eq "Delete Banner") { &condelete }
if($INPUT{'submit'} eq "Delete All") { &deleteall }
if($INPUT{'submit'} eq "Delete") { &delete }
if($INPUT{'submit'} eq "View Stats") { &stats }
if($INPUT{'submit'} eq "Setup") { &setup }
if($INPUT{'submit'} eq "Update") { &update }
if($INPUT{'submit'} eq "Add") { &added }
}

sub banner {

open(FILE,"setup.txt");
flock (FILE, 2);
$border= <FILE>;
chop ($border);
$width = <FILE>;
chop ($width);
$height = <FILE>;
chop ($height);
$showdesc = <FILE>;
chop ($showdwsc);
$target = <FILE>;
chop ($target);
$center = <FILE>;
chop ($center);
flock (FILE, 8);
close(FILE);

open (GETDATA, "banner.txt");
@Data = <GETDATA>;
close GETDATA;

srand(time ^ $$);
$number = rand(@Data);
$line = @Data[$number];

chomp ($line);
($id, $hits, $url, $banurl, $bandesc) = split(/:/, $line);


if ($center =~ /yes/i) {print "<center>";}
print "<a href=\"http\://$url\" target=\"$target\">";
print "<IMG src=\"http\://$banurl\" border=\"$border\" width=\"$width\" height=\"$height\"><BR>";
if ($showdesc =~ /yes/i) {print "$bandesc";}
print "</A><BR>\n";
if ($center =~ /yes/i) {print "</center>";}
}

sub adminlogin {
&head;
print "<CENTER><FORM ACTION=banner2.cgi METHOD=POST>";
print "Password: <INPUT TYPE=password NAME=password><BR>";
print "<INPUT TYPE=submit NAME=submit VALUE=Start></FORM></CENTER>";
&footer;
}

sub admin {
if($INPUT{'password'} eq "$adminpass") {
&head;
print "<CENTER><FORM ACTION=banner2.cgi METHOD=POST>";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Add Banner\">";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Delete Banner\">";
#print "<INPUT TYPE=submit NAME=submit VALUE=\"View Stats\">";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Setup\"></FORM></CENTER>";
&footer;
}
else {
&head;
print "<CENTER><B>Bad password</B><BR>";
print "<a href=banner2.cgi?admin>Try agine</A>";
}
}

sub add {
&head;
print "<FORM ACTION=banner2.cgi METHOD=POST>";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>";
print "<TR><TD>Site id:</TD><TD>";
print "<INPUT TYPE=text NAME=id SIZE=15></TD>";
print "<TR><TD>Site URL:</TD><TD>";
print "http://<INPUT TYPE=text NAME=siteurl SIZE=15></TD>";
print "</TR><TR><TD>Banner URL:</TD><TD>";
print "http://<INPUT TYPE=text NAME=banurl SIZE=15></TD>";
print "</TR><TR><TD>Desc:</TD><TD>";
print "<INPUT TYPE=text NAME=desc SIZE=15></TD>";
print "</TR><TR><TD COLSPAN=2><P ALIGN=Center>";
print "<INPUT TYPE=submit NAME=submit VALUE=Add></TD>";
print "</TR></TABLE></CENTER></FORM><BR>";
&butten;
&footer;
}

sub added {
&head;
#open (DATA, "banner.txt");
#@bdata = <DATA>;
#close DATA;
#open (FILE, ">$datafile/banner.txt");
#print FILE "$INPUT{'id'}:0:$INPUT{'siteurl'}:$INPUT{'banurl'}:$INPUT{'desc'}\n";
#foreach $line (@bdata){
#print FILE "$line";
#}
#close (FILE);

print "<B>Banner Added</B><P>";
print "<IMG SRC=http://$INPUT{'banurl'}><BR>";
print "http://$INPUT{'siteurl'}<BR>";
print "$INPUT{'desc'}<P>";
&butten;
&footer;
}

sub deleteall {
if($INPUT{'password'} eq "$adminpass") {
&head;
print "<CENTER>All banners deleted";
&butten;
&footer;

open(FILE, ">banner.txt");
print FILE "";
close (FILE);
}
else {
&head;
print "<CENTER><B>Bad password</B><BR>";
&footer;
}
}

sub delete {
#$a=0;
#open (DATA, "banner.txt");
#@data = <DATA>;
#close DATA;

#open(FILE, ">banner.txt");
#	foreach $line (@data) {
#	$a++;
#	if ($a eq "$INPUT{'line'}") {
#		print FILE "";
#		}
#	else {
#		print FILE "$line";
#		}
#	}
#close (FILE);

&head;
print "Deleted!";
&butten;
&footer;
}

sub condelete {
&head;
print "<FORM ACTION=banner2.cgi METHOD=POST>\n";
print "<TABLE BORDER CELLPADDING=2>\n";
print "<TR><TD>Delete:</TD><TD>URL:</TD><TD>Banner</TD></TR>\n";

$i=0;
open (DATA, "banner.txt");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i++;
chomp ($line);
($id, $hits, $url, $banurl, $bandesc) = split(/:/, $line);

print "<TR><TD><INPUT TYPE=radio NAME=line VALUE=$i>\n";
print "</TD><TD>http://$url</TD><TD><IMG SRC=http://$banurl></TD></TR>\n";
}
print "<TR><TD COLSPAN=4><P ALIGN=Center>$i Banners</TD></TR>\n";
print "<TR><TD COLSPAN=4><P ALIGN=Center>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Delete\"></TD>\n";
print "</TR></TABLE></FORM><BR>\n";

print "<CENTER><FORM ACTION=banner2.cgi METHOD=POST><B>\n";
print "<B>Delete all the banners!</B><BR>\n";
print "Password: <input type=password name=password><BR>\n";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Delete All\"></FORM>\n";
&butten;
&footer;
}

sub stats {

&head;
open (DATA, "banner.txt");
@bdata = <DATA>;
close DATA;
foreach $line (@bdata){
chomp ($line);
($id, $hits, $url, $banurl, $bandesc) = split(/:/, $line);
print "$id.  <IMG SRC=$banurl><BR>\n";
}
print "stats are comeing soon";
&butten;
&footer;
}

sub butten {
print "<CENTER><FORM ACTION=banner2.cgi METHOD=POST>";
print "<INPUT TYPE=hidden NAME=password VALUE=$adminpass>";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Reload main admin\"></FORM></CENTER>";
}

sub footer {

print "<HR color=blue><CENTER>Banner Rotater 2<BR>";
print "Copyright <A HREF=http://www.d0tt.com>Byron Chilton</A></CENTER>";
}

sub setup {

open(FILE,"setup.txt");
flock (FILE, 2);
$border= <FILE>;
chop ($border);
$width = <FILE>;
chop ($width);
$height = <FILE>;
chop ($height);
$showdesc = <FILE>;
chop ($showdwsc);
$target = <FILE>;
chop ($target);
$center = <FILE>;
chop ($center);
flock (FILE, 8);
close(FILE);

&head;
print "<FORM ACTION=banner2.cgi METHOD=POST>";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>";
print "<TR><TD>Image border:</TD><TD>";
print "<INPUT TYPE=text NAME=border VALUE=\"$border\" SIZE=15></TD>";
print "</TR><TR><TD>Image width:</TD><TD>";
print "<INPUT TYPE=text NAME=width VALUE=\"$width\" SIZE=15></TD>";
print "</TR><TR><TD>Image height:</TD><TD>";
print "<INPUT TYPE=text NAME=height VALUE=\"$height\" SIZE=15></TD>";
print "</TR><TR><TD>Show descriptshen:</TD><TD>";
print "<INPUT TYPE=text NAME=showdesc VALUE=\"$showdesc\" SIZE=15></TD>";
print "</TR><TR><TD>Target:</TD><TD>";
print "<INPUT TYPE=text NAME=target VALUE=\"$target\" SIZE=15></TD>";
print "</TR><TR><TD>Centerd:</TD><TD>";
print "<INPUT TYPE=text NAME=center VALUE=\"$center\" SIZE=15></TD>";
print "</TR><TR><TD COLSPAN=2><P ALIGN=Center>";
print "<INPUT TYPE=submit NAME=submit VALUE=\"Update\"></TD>";
print "</TR></TABLE></CENTER></FORM>";
&butten;
&footer;
}

sub update {
#open(FILE, ">$datafile/setup.txt");
#print FILE "$INPUT{'border'}\n";
#print FILE "$INPUT{'width'}\n";
#print FILE "$INPUT{'height'}\n";
#print FILE "$INPUT{'showdesc'}\n";
#print FILE "$INPUT{'target'}\n";
#print FILE "$INPUT{'center'}\n";
#print FILE "###\n";
#close (FILE);

&head;
print "<center><B>Setup updated</B></CENTER>";
&butten;
&footer;
}

sub head {

print "<center><H3>Banner rotater 2 admin</h3>";
print "<HR color=blue>";
}