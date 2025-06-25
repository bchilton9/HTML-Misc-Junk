#!/usr/bin/perl
#################################################################
#                                                             	#
# Virtual Subdomains V3.2	By Jeff Ledger			#	
# Program Section: WHOIS	jledger@cyberstreet.com		#
# 								#
#################################################################
# COPYRIGHT NOTICE:	<*> THIS PROGRAM IS SHARWARE <*>	#
# Copyright 1999 Jeffrey D. Ledger All Rights Reserved		#
#								#
# Virtual Subdomains may be used and modified free of charge	#
# by anyone so long as this copyright notice and the comments	#
# above remain intact.  By using this code you agree to		#
# indemnify Jeffrey D Ledger from any liability that might	#
# arise from it's use.						#
#								#
# You are encouraged to register this software at the 		#
# Ledgerlabs.cc website located at: www.ledgerlabs.cc		#
# A small registration fee of $5.00 will help us offset the	#
# costs of late night coffee and the Ledgerlabs website.	#
#								#
# Selling the code for this program without prior written	#
# consent is expressly forbidden.  In other words, please ask	#
# first before you try and make money off of my program.	#
# 								#
#################################################################
# CHANGE THIS TO THE LOCATION OF YOUR SCRIPT & RECORDS		#
#################################################################

$directory = "/home/virtual/site246/fst/var/www/cgi-bin";
$records = "/home/virtual/site246/fst/var/www/cgi-bin/records";


# IMPORTANT!	READ THE DOCUMENTATION COMPLETELY FIRST!	#
#################################################################
# 	NO CHANGES NEED TO BE MADE BEYOND THIS POINT!		#
#################################################################


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
$hostname =~ tr/A-Z/a-z/;

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

$request = "no";

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
flock (FILE, 8);
close(FILE);


######################
## CHECK FOR ERRORS ##
######################

if ($sitename eq '') {
	$request = "yes";
}

if ($hostname eq '') {
	$request = "no";
}

###############################################
## CHECK REQUESTED NAME AGAINST RESERVE LIST ##
###############################################
open (DAT, "virtual.reserved");
@database = <DAT>;
close (DAT);

foreach $line (@database){
	chop $line;
	if ($hostname eq $line){
	$request = "no";
	$title = "RESERVED";
	$location = " ";
	$username = "WEBMASTER";
	$email = " ";
	next;
	}
}


#################################
## OPEN THE LOCATION AS LISTED ##
#################################

if ($request eq 'yes') {
print "Content-type: text/html\n\n";
print <<"END";
<META HTTP-EQUIV="Expires" CONTENT="Tue, 12 Jan 1971 06:23:00 GMT">
$bodycode
$fontcode

<big>$mysitename Virtual Subdomains Setup:</big>

<PRE>
     Requested Name: $hostname.$domain
<FORM method=post action="register.cgi">
Actual Web Location: <INPUT TYPE=TEXT SIZE=60 NAME="location"
value="http://">
     Your Full Name: <INPUT TYPE=TEXT SIZE=30 NAME="username">
  Choose a Password: <INPUT TYPE=TEXT SIZE=15 NAME="password">
 Your Email Address: <INPUT TYPE=TEXT SIZE=30 NAME="email">
      Website Title: <INPUT TYPE=TEXT SIZE=50 NAME="title">
Website Description: <INPUT TYPE=TEXT SIZE=60 NAME="description">
   METAtag Keywords: <INPUT TYPE=TEXT SIZE=60 NAME="keywords">
<INPUT TYPE=HIDDEN VALUE="$htmlswitch" NAME="htmlcode">
<INPUT TYPE=HIDDEN VALUE="$bannerswitch" NAME="bannerswitch">
<INPUT TYPE=HIDDEN VALUE="$hostname.$domain" NAME="sitename">

<CENTER><INPUT TYPE=submit VALUE="Register: $hostname.$domain"></CENTER>

<CENTER>Exit to <A HREF="http://www.$domain">http//www.$domain</a></CENTER>
</PRE>
</FORM>
END

}
if ($username eq 'Webmaster') {
	$location = "Not Listed";
}

if ($request eq 'no') {
print "Content-type: text/html\n\n";
print <<"END";
$bodycode
$fontcode

<big>$mysitename Virtual Domain:</big>
<BR><BR>

Sorry, Requested name is already taken..
<br><br>
<PRE>
       Domain: $hostname.$domain
Website Title: $title
True Location: $location
Registered by: $username
Email Address: $email

<PRE><br>
Click <A href="whois.htm">here</a> to check another name.
END

}
