#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# view.cgi for admin/blocks/right                                             #
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
# File: Last modified: 05/08/02 by Floyd                                      #
###############################################################################
###############################################################################
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

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

#######################################
# Define the variables for the script #
#######################################
$database="$datadir/blocks/blockright.dat";

##################################################
# Check to see if there was a database specified #
##################################################
if ($input{'database'} eq ''){
$db=$database;
}else{
$db=$input{'database'};
}

#################################################
# Get the origional database data & buffer data #
#################################################
open (ORGDB,"<$database");
@ODB=<ORGDB>;
close (ORGDB);

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################
$navbar = "$btn{'014'} $nav{'063'} $btn{'014'} $btn{'034'} $btn{'014'} $mnu{'022'}";
print_top();
check_access(editrblk); if ($access_granted ne "1") { error("$err{'011'}"); }


print qq~<b>$btn{'034'}</b>
<HR>
<table width='150' border='1'>
<tr><td width='150'><div align='center'><b>$msg{'353'}</b></div></td></tr>~;

foreach $rec (@ODB){
	chomp($rec);
	($block,$title,$stat,$bcont)=split(/\|/,$rec);
	$cont = showhtml($bcont);
print qq~
<tr><td width='150'><bgcolor = "$boxbgcolor">~;
			boxheader("$title");
			print qq~<tr><td>$cont</td></tr>~;
			boxfooter();
			print qq~<td><div align='center'><a href="edit_record.cgi?block=$block\&title=$title\&stat=$stat\&bcont=$bcont">$nav{'096'}</a> - <a href="edit.cgi?action=delete\&block=$block\&title=$title\&stat=$stat\&bcont=$bcont">$nav{'097'}</a></div></td>\n~;
}
print qq~
<tr><td colspan='2'><center><a href="add.cgi\?database=$db">&nbsp;$nav{'121'}</a></center></td></tr>
</table>
<br>
~;

print_bottom();
exit;

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
