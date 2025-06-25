#!/usr/bin/perl
#################################################################
#################################################################

$directory = "/usr/home/byron/public_html/cgi-bin/v3";
$records = "/usr/home/byron/public_html/v3/data";

$hostname = $ENV{'HTTP_HOST'};
$hostname =~ tr/A-Z/a-z/;
$cloak = "hide";
$rema = "";
$remb - "";

###################################
## GET CONFIGURATION INFORMATION ##
###################################

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


##################################
## MAKE SURE EVERYTHING IS ZERO ##
##################################

$sitename="0";
$location="";
$username="";
$password="";
$email="";
$title="";
$description="";
$keywords="";
$htmlcode="";
$userbanner="";
$showbanner="yes";

###############################
## GET INFORMATION FROM FILE ##
###############################

open (FILE, "$records/$hostname");
flock (FILE, 2);
$sitename = <FILE>;
chop ($sitename);
$location = <FILE>;
chop ($location);
$username = <FILE>;
chop ($username);
$password = <FILE>;
chop ($password);
$email = <FILE>;
chop ($email);
$title = <FILE>;
chop ($title);
$description = <FILE>;
chop ($description);
$keywords = <FILE>;
chop ($keywords);
$htmlcode = <FILE>;
chop ($htmlcode);
$userbanner = <FILE>;
chop ($userbanner);
$urlhideing = <FILE>;
chop ($urlhideing);
flock (FILE, 8);
close(FILE);


###################################
## CHECK FOR ERRORS AND SETTINGS ##
###################################

if ($sitename eq '') {
	$location=$errorpage;
}


if ($cloak eq "nohide") {
	$rema = "<!--";
	$remb = "-->";

}
if ($userbanner eq "no") {
	$showbanner="no";
}

#################################
## OPEN THE LOCATION AS LISTED ##
#################################
print "Content-Type: text/html\n\n";

print <<"END";
<meta NAME="GENERATOR" CONTENT="Virtual Subdomains V3.2 - http://www.ledgerlabs.cc">
<meta NAME="description" CONTENT="$description">
<meta NAME="keywords" CONTENT="$keywords">
<TITLE>$title</TITLE>
$htmlcode
END

if ($showbanner eq "yes") {
srand();
$bannernumber = int(rand($bannercount));
print <<"END2";
<SCRIPT LANAGUAGE="JavaScript">
<!--
banner = window.open("$bannerlocation$bannernumber.shtml","banner",
"resizable=yes,width=520,height=80");
//-->
</SCRIPT>
END2
}

if ($urlhideing eq "yes") {
print <<"END";
<frameset frameborder=0 framespacing=0 border=0 rows="100%,*" noresize>
<frame name="frame" src="$location" noresize>
</frameset>
<NOFRAMES>
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$location">
<BODY BGCOLOR="#ffffff"><CENTER>
<A HREF=$location>$title</A></CENTER>
</NOFRAMES>
END
}

else {
print <<"END";
<META HTTP-EQUIV="Refresh" CONTENT="0;URL=$location">
<BODY BGCOLOR="#ffffff"><CENTER>
<A HREF=$location>$title</A></CENTER>
END
}