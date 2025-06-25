#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# add.cgi for admin/blocks/right                                              #
# v0.9.9 - Requin                                                             #
#                                                                             #
# Copyright (C) 2002 by Carter (carter@mcarterbrown.com)                      #
#                                                                             #
# This program is free software; you can redistribute it and/or               #
# modify it under the terms of the GNU General Public License                 #
# as published by the Free Software Foundation; either version 2              #
# of the License, or (at your option) any later version.                      #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program; if not, write to the Free Software                 #
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA. #
#                                                                             #
#                                                                             #
# File: Last modified: 09/12/02 by Floyd                                      #
###############################################################################
###############################################################################

$| = 1;

use CGI::Carp qw(fatalsToBrowser);

$scriptname = "WebAPP";
$scriptver = "0.9.8";

eval {
	require "../../../config.pl";
	require "$sourcedir/subs.pl";

	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};
if ($@) {
	print "Content-type: text/html\n\n";
	print qq~<h1>Software Error:</h1>
Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
<pre>$@</pre>
<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
~;
	exit;
}

getlanguage();
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

############################
# Get data from GET & POST #
############################
&parse_form;

##################################
# Print out the page for editing #
##################################
$navbar = "$btn{'014'} $nav{'063'} $btn{'014'} $nav{'123'}";
print_top();

check_access(editrblk); if ($access_granted ne "1") { error("$err{'011'}"); }


print "
<font face='Arial'>
<i>$msg{'348'}</i>
<form onSubmit='submitonce(this)' action='edit.cgi' method='GET'>
<input type='hidden' name='action' value='add'>
<input type='hidden' name='database' value='$input{'database'}'>
<table border='1'>
<tr><td><font size='2'>$msg{'349'}</font></td><td><input type='text' name='nblock'> $msg{'573'}</td></tr>
<tr><td><font size='2'>$msg{'350'}</font></td><td><input type='text' name='ntitle'> $msg{'574'}</td></tr>
<tr><td><font size='2'>$msg{'351'}</font></td><td><input type='text' name='nstat'> $msg{'552'}</td></tr>
<tr><td><font size='2'>Members Only</font></td><td><input type='text' name='nonly'> $msg{'575'}</td></tr>
<tr><td><font size='2'>$msg{'352'}</font></td><td><textarea name='nbcont' rows='20' cols='40'></textarea></td></tr>
</table>
<input type='Submit' value='$btn{'032'}'>
</form>
</font>
</font>
";

print_bottom();



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