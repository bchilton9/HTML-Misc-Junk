#!/usr/bin/perl
#################################################################
#                                                             	#
# Virtual Subdomains V3.2	By Jeff Ledger			#	
# Program Section: REGISTER	jledger@cyberstreet.com		#
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
# CHANGE THIS TO THE LOCATION OF YOUR RECORDS			#
#################################################################


$records = "/usr/home/byron/public_html/v3/data";
$mailprog = "/usr/lib/sendmail";

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

$sitename = $FORM{'sitename'};
$location = $FORM{'location'};
$username = $FORM{'username'};
$password = $FORM{'password'};
$email = $FORM{'email'};
$title = $FORM{'title'};
$description = $FORM{'description'};
$keywords = $FORM{'keywords'};
$htmlcode = $FORM{'htmlcode'};
$bannerswitch = $FORM{'bannerswitch'};
$urlhideing = $FORM{'urlhide'};

####################################
## Fix Explorer Hidden Fields Bug ##
####################################

if ($sitename =~ /\n/) {
	chop ($sitename)
}

if ($htmlcode =~ /\n/) {
	chop ($htmlcode)
}

if ($bannerswitch =~ /\n/) {
	chop ($bannerswitch)
}
if ($urlhideing =~ /\n/) {
	chop ($urlhideing)
}

#####################################
## Create the new subdomain record ##
#####################################

open(FILE, ">$records/$sitename");
print FILE "$sitename\n";
print FILE "$location\n";
print FILE "$username\n";
print FILE "$password\n";
print FILE "$email\n";
print FILE "$title\n";
print FILE "$description\n";
print FILE "$keywords\n";
print FILE "$htmlcode\n";
print FILE "$bannerswitch\n";
print FILE "$urlhideing\n";
close(FILE);


###################################
## TELL THE USER WE ARE FINISHED ##
###################################
open (HEAD, "../ssi/v3header.txt");
@DATA=<HEAD>;
close (HEAD);
$head="@DATA";
open (FOOT, "../ssi/footer.txt");
@DATA2=<FOOT>;
close (FOOT);
$foot="@DATA2";

print "Content-type: text/html\n\n";
print <<"END";
$head
<CENTER><BR><BR>Name: <BIG><A HREF="http://$sitename" target="_top">$sitename</a></BIG> has been updated.<BR>
Return to <A HREF=http://www.d0tt.com>D0TT.com</A>
$foot
END

##send mail
