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
close(FILE);

###########################################
## Update Latest Registered Domains List ##
###########################################
open (FILE, "recent.htm");
flock (FILE, 2);
$recenthtml1 = <FILE>;
$recenthtml2 = <FILE>;
$recenthtml3 = <FILE>;
$recenthtml4 = <FILE>;
$recent1= <FILE>;
$recent2= <FILE>;
$recent3= <FILE>;
$recent4= <FILE>;
$recent5= <FILE>;
$recent6= <FILE>;
$recent7= <FILE>;
$recent8= <FILE>;
$recent9= <FILE>;
$recent10= <FILE>;
$recent11= <FILE>;
$recent12= <FILE>;
$recent13= <FILE>;
$recent14= <FILE>;
$recent15= <FILE>;
$recent16= <FILE>;
$recent17= <FILE>;
$recent18= <FILE>;
$recent19= <FILE>;
$recent20= <FILE>;
$recent21= <FILE>;
$recent22= <FILE>;
$recent23= <FILE>;
$recent24= <FILE>;
$recent25= <FILE>;
$recent26= <FILE>;
$recent27= <FILE>;
$recent28= <FILE>;
$recent29= <FILE>;
flock (FILE, 8);
close (FILE);

######################
## GET TODAY'S DATE ##
######################

@days   = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
@months = ('January','February','March','April','May','June','July',
                 'August','September','October','November','December');
    
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];
$time = sprintf("%02d:%02d:%02d",$hour,$min,$sec);

$date = "$days[$wday], $months[$mon] $mday";


########################################################
## RE-CREATE THE RECENT.HTM FILE WITH NEW INFORMATION ##
########################################################

open(FILE,">recent.htm");
flock (FILE, 2);
print FILE "$recenthtml1";
print FILE "$recenthtml2";
print FILE "$recenthtml3";
print FILE "$recenthtml4";
print FILE "$date &nbsp;&nbsp;&nbsp;<A HREF=http://$sitename>$sitename</a><BR>\n";
print FILE "$recent1";
print FILE "$recent2";
print FILE "$recent3";
print FILE "$recent4";
print FILE "$recent5";
print FILE "$recent6";
print FILE "$recent7";
print FILE "$recent8";
print FILE "$recent9";
print FILE "$recent10";
print FILE "$recent11";
print FILE "$recent12";
print FILE "$recent13";
print FILE "$recent14";
print FILE "$recent15";
print FILE "$recent16";
print FILE "$recent17";
print FILE "$recent18";
print FILE "$recent19";
print FILE "$recent20";
print FILE "$recent21";
print FILE "$recent22";
print FILE "$recent23";
print FILE "$recent24";
print FILE "$recent25";
print FILE "$recent26";
print FILE "$recent27";
print FILE "$recent28";
print FILE "$recent29";
flock (FILE, 8);
close(FILE);

###################################
## TELL THE USER WE ARE FINISHED ##
###################################

print "Content-type: text/html\n\n";
print <<"END";

<CENTER><BR><BR>Name: <BIG><A HREF="http://$sitename" target="_top">$sitename</a></BIG> is ready.
END

