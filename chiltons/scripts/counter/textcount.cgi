#!/usr/bin/perl

##########################################################
# Text COunter Copyright 2004 Chilton's Script Archive.  #
# This script comes freewhere there is no support.       #
# For more scripts go to www.chilton.us                  #
#						         #
# To use this script copy the following lines into       #
# your page:					         #
# <!--#exec cgi="/path/to/textcount.cgi"-->  or          #
# <!--#include virtual="/path/to/textcount.cgi" -->      #
# Some servers do not suport both call's                 #
# SSI is required				         #
##########################################################
# To install                                             #
# Then upload to your server in ASCII and chmod to 755   #
# Put the SSI code where you want the Text Counter to be #
##########################################################

###########################
## No need to edit below ##
###########################

open (DATA, "textcont.dat");
@data = <DATA>;
close DATA;

$con="@data";

$con++;

open(FILE, ">textcont.dat");
print FILE "$con";
close (FILE);

print "Content-type: text/html\n\n";
print "$con";