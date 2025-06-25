#!/usr/bin/perl
#########################################################
# Random Quote Copyright 2004 Chilton's Script Archive. #
# This script comes freewhere there is no support.      #
# For more scripts go to www.chiltons.us                #
#						        #
# To use this script copy the following lines into      #
# your page:					        #
# <!--#exec cgi="/path/to/quote.cgi"-->  or             #
# <!--#include virtual="/path/to/quote.cgi" -->         #
# Some servers do not suport both call's                #
# SSI is required				        #
#########################################################
# To install fill in the variables                      #
# Then upload to your server in ASCII and chmod to 755  #
# Put the SSI code where you want the quote to be       #
#########################################################

$quotefile = "quote.txt";
 # Location of the Quotes file.

$center = "1";
 #Is Quote centerd (1=yes, 2=no)

$fntstyle = "Arial";
 # Quotes Font Style.

$fntsize = "-1";
 # Quote Font Size.

$fntbold = "1";
 # Makes the quote bold (1=bold, 0=plain)

###########################
## No need to edit below ##
###########################

open (GETDATA, "$quotefile");
@Data = <GETDATA>;
close GETDATA;

srand(time ^ $$);
$number = rand(@Data);
$quote = @Data[$number];

print "Content-type: text/html\n\n";

if ($center =~ /1/i) {print "<center>";}
print "<font size=\"$fntsize\" face=\"$fntstyle\">";
if ($fntbold =~ /1/i) {print "<strong>";}
print "\"$quote\"";
if ($fntbold =~ /1/i) {print "</strong>";}
print "</font><br>\n";
if ($center =~ /1/i) {print "</center>";}

exit (0);