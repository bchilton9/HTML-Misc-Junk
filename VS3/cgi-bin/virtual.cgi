#!/usr/bin/perl

use DBI;

$directory = "/home/virtual/site246/fst/var/www/cgi-bin";

$hostname = $ENV{'HTTP_HOST'};
$hostname =~ tr/A-Z/a-z/;


open(FILE,"$directory/virtual.data");
flock (FILE, 2);
$domain= <FILE>;
chop ($domain);
$errorpage = <FILE>;
chop ($errorpage);
$bannerswitch = <FILE>;
chop ($bannerswitch);
$cloak = <FILE>;
chop ($cloak);
$htmlcode = <FILE>;
chop ($htmlcode);
$sitename = <FILE>;
chop ($sitename);
$mbackground = <FILE>;
chop ($mbackground);
$mfont = <FILE>;
chop ($mfont);
$bannercount = <FILE>;
chop ($bannercount);
$bannerlocation = <FILE>;
chop ($bannerlocation);
$endoffile = <FILE>;
flock (FILE, 8);
close(FILE);


my $dbh = DBI->connect("DBI:mysql:eqguilded_com_-_vs3:localhost","eqguilded","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM `domains` WHERE `name` = '$hostname' LIMIT 1";

if($sth=$dbh->prepare($temp)) { 
 $sth->execute;

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$sitename = "$row[0]";
$owner = "$row[1]";
$type = "$row[2]";
$status = "$row[3]";
$location = "$row[4]";
$title = "$row[5]";
$description = "$row[6]";
$keywords = "$row[7]";

 } 

}
$sth->finish; 
$dbh->disconnect; 


if ($status eq "gold") {
if ($type ne "0") {
if ($type ne "1") {
$type = "1";
}
}

if ($type eq "4") { $type = "0"; }
if ($type eq "5") { $type = "1"; }
}


if ($sitename eq '') {
	$location=$errorpage;
}

print "Content-Type: text/html\n\n";

print qq~
<HTML>
<HEAD>
<meta NAME="description" CONTENT="$description">
<meta NAME="keywords" CONTENT="$keywords">
<TITLE>$title</TITLE>
~;


### BANNER FRAME ###
if ($type eq "0") {


if ($status eq "silver") {
print qq~
<SCRIPT LANAGUAGE="JavaScript">
<!--
banner = window.open("$bannerlocation/0.htm","banner",
"resizable=yes,width=520,height=80");
//-->
</SCRIPT>
~;
}

print qq~
<frameset frameborder=0 framespacing=0 border=0 rows="100%,*" noresize>
<frame name="frame" src="$location" noresize>
</frameset>
<NOFRAMES>
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$location">
</HEAD>
<BODY BGCOLOR="#8080ff">
<CENTER>
<A HREF="http://eqguilded.com">EQGuilded.com Subdomain System</A><BR>
<A HREF="$location">Enter $sitename</A>
</NOFRAMES>
~;

}


### BANNER NO FRAME ###
if ($type eq "1") {

#### BANNER
if ($status eq "silver") {
print qq~
<SCRIPT LANAGUAGE="JavaScript">
<!--
banner = window.open("$bannerlocation/0.htm","banner",
"resizable=yes,width=520,height=80");
//-->
</SCRIPT>
~;
}

print qq~
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$location">
</HEAD>
<BODY BGCOLOR="#8080ff">
<CENTER>
<A HREF="http://eqguilded.com">EQGuilded.com Subdomain System</A><BR>
<A HREF="$location">Enter $sitename</A>
~;

}


### NO BANNER FRAME ###
if ($type eq "2") {
print qq~
<FRAMESET ROWS="60,*" BORDER="0">
<FRAME SRC="$bannerlocation/1.htm" NAME="banner" SCROLLING="No" NORESIZE>
<FRAME SRC="$location" NAME="frame">
</FRAMESET>
<NOFRAMES>
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$location">
</HEAD>
<BODY BGCOLOR="#8080ff">
<CENTER>
<A HREF="http://eqguilded.com">EQGuilded.com Subdomain System</A><BR>
<A HREF="$location">Enter $sitename</A>
</NOFRAMES>
~;
}


### DELAY PAGE ###
if ($type eq "3") {

print qq~
<META HTTP-EQUIV="Refresh" CONTENT="5;URL=$location">
</HEAD>
<BODY BGCOLOR="#8080ff">
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" HEIGHT="100%">
    <TR>
      <TD><TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" BGCOLOR="#cfcfcf">
	  <TR>
	    <TD><P ALIGN=Center>
	      <B><BIG>EQGuilded.com Subdomain System.<BR>
	      You will be redirected in 5 seconds.</BIG></B>
	      <CENTER>
		Please Visit our Sponsor in the mean time.
		<P>
		<A HREF="http://eqguilded.com" TARGET="_new"><IMG SRC="http://eqguilded.com/banners/banner1.jpg"
		    border=0""></A>
		<P>
		Or Visit EQGuilded.com and get your own subdomain.EQGuilded.com.
		<P>
		<A HREF="http://eqguilded.com" TARGET="_new"><IMG SRC="http://eqguilded.com/banners/banner1.jpg"
		    border=0""></A>
		<P>
		Opening the links will not affect the site you are trying to visit.<BR>
		Sponser's site will be opened in a new window.
	      </CENTER>
	    </TD>
	  </TR>
	</TABLE>
      </TD>
    </TR>
  </TABLE>
</CENTER>
~;

}

print qq~
</BODY>
</HTML>
~;