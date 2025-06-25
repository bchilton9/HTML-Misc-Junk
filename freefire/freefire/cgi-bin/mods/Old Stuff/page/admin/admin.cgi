#!/usr/bin/perl
###############################################################################
# WebApp Calendar Mod - calendar.pl
#
# Mod created by Ted Loomos (tloomos@pbs-inc.net)
#
# Based on the verysimple organizer suite
# Copyright (c) 2001 Jason M. Hinkle. All rights reserved. This script is
# free software; you may redistribute it and/or modify it under the same
# terms as Perl itself.
# For more information see: http://www.verysimple.com/scripts/
#
# LEGAL DISCLAIMER:
# This software is provided as-is.  Use it at your own risk.  The
# author takes no responsibility for any damages or losses directly
# or indirectly caused by this software.
#
# Version History
# 0.0.1 - 06/09/02 - Initial script created
# 0.0.2 - 06/24/02 - Cleaned up code and fixed minor bugs
#
# To Do:
###############################################################################

BEGIN {
	##--------------------------------------------------------------
	## If you are not using standard folder locations, the following
	## line may need to be changed to match your installation
	##--------------------------------------------------------------

	require "../../../config.pl";
	require "$sourcedir/subs.pl";

	##--------------------------------------------------------------
	## Nothing below this point should require modification
	##--------------------------------------------------------------
}


&parse_form;


logips();
loadcookie();
loaduser();
logvisitors();



# ----------- print everything to the browser ---
$navbar = "&nbsp;$btn{'014'}&nbsp; $cm_title";
print_top();

&PrintDefault;

print_bottom();



# _____________________________________________________________________________
sub PrintDefault {

print qq~
no admin yet
~;

}



########################################
# Code to get the data from GET & POST #
########################################
sub parse_form {

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
   @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $input{$name} = $value;
   }
}

1;