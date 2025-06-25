#!/usr/bin/perl
#################################################################
#################################################################

$directory = "/usr/home/byron/public_html/cgi-bin/v3";
$records = "/usr/home/byron/public_html/v3/data";
$masterpassword = "0519a";



#####################
# Get the form data #
#####################

read(STDIN, $values, $ENV{'CONTENT_LENGTH'});

# Split up the name-value pairs
@pairs = split(/&/, $values);

foreach $set (@pairs) {
   ($name, $itemvalue) = split(/=/, $set);

# Remove plus signs and any encoding present
   $itemvalue =~ tr/+/ /;
   $itemvalue =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
   $itemvalue =~ s/&lt;!--(.|\n)*--&gt;//g;

   $FORM{$name} = $itemvalue; 
}                                     
	
##########################
# Set incoming Variables #
##########################

$hostname = $FORM{'whois'};
#$formname = $FORM{'formname'};
$formpass = $FORM{'formpass'};

##################################
## MAKE SURE EVERYTHING IS ZERO ##
##################################

$change="";
$masteruser="";
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
$htmlswitch="";
$mysitename="";
$bodycode="";
$fontcode="";
$bannerswitch="";

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
$htmlswitch = <FILE>;
chop ($htmlswitch);
$mysitename = <FILE>;
chop ($mysitename);
$bodycode = <FILE>;
chop ($bodycode);
$fontcode = <FILE>;
chop ($fontcode);
flock (FILE, 8);
close(FILE);

###############################
## GET INFORMATION FROM FILE ##
###############################

open (FILE, "$records/$hostname.$domain");
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


######################
## CHECK FOR ERRORS ##
######################

if ($formpass eq $password) {
	$change = "yes";
}

if ($formpass eq $masterpassword) {
	$change = "yes";
	$masteruser = "yes";
}

if ($sitename eq "") {
	$change = "no";
}


#################################
## OPEN THE LOCATION AS LISTED ##
#################################
open (HEAD, "../ssi/v3header.txt");
@DATA=<HEAD>;
close (HEAD);
$head="@DATA";
open (FOOT, "../ssi/footer.txt");
@DATA2=<FOOT>;
close (FOOT);
$foot="@DATA2";

if ($change eq 'yes') {
print "Content-type: text/html\n\n";
print <<"END";
<META HTTP-EQIV="Expires" CONTENT="Tue, 12 Jan 1971 06:23:00 GMT">
$bodycode
$fontcode
$head
<big>$mysitename Virtual Subdomain Modification:</big>

<PRE>
     	Active Name: $sitename
<FORM method=post action="edit.cgi">
Actual Web Location: <INPUT TYPE=TEXT SIZE=60 NAME="location"
value="$location">
          Full Name: <INPUT TYPE=TEXT SIZE=30 NAME="username" value="$username">
           Password: <INPUT TYPE=TEXT SIZE=15 NAME="password" value="$password">
      Email Address: <INPUT TYPE=TEXT SIZE=30 NAME="email" value="$email">
      Website Title: <INPUT TYPE=TEXT SIZE=50 NAME="title" value="$title">
Website Description: <INPUT TYPE=TEXT SIZE=60 NAME="description" value="$description">
   METAtag Keywords: <INPUT TYPE=TEXT SIZE=60 NAME="keywords" value="$keywords">
        URL Hideing: <INPUT TYPE=TEXT SIZE=3 NAME="urlhide" value="$urlhideing">
END

if ($masteruser eq "no") {
print <<"END";
<INPUT TYPE=HIDDEN VALUE="$htmlcode" NAME="htmlcode">
<INPUT TYPE=HIDDEN VALUE="$userbanner" NAME="bannerswitch">
END
}
if ($masteruser eq "yes") {
print <<"END";
    Extra HTML Code: <INPUT TYPE=TEXT SIZE=60 NAME="htmlcode"
value="$htmlcode">
         Show popup: <INPUT TYPE=text SIZE=3 NAME="bannerswitch" value="$userbanner">
END
}
print <<"END";
<INPUT TYPE=HIDDEN VALUE="$sitename" NAME="sitename">

<CENTER><INPUT TYPE=submit VALUE="Update: $hostname.$domain"></CENTER>

<CENTER>Exit to <A HREF="http://www.$domain">http//www.$domain</a></CENTER>
</PRE>
</FORM>
$foot
END

}
if ($change eq 'no') {

print "Content-type: text/html\n\n";
print <<"END";
$bodycode
$fontcode
$head
<big>$mysitename Virtual Domain:</big>
<BR><BR>

Sorry,  Your username, password or subdomain was entered incorrectly!
<br><br>
Click <A href="http://www.d0tt.com/domain.shtml">here</a> to try again.
$foot
END

}
