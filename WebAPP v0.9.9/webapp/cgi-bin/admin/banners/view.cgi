#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# view.cgi for admin/banners                                                  #
# v0.9.9 - Requin                                                             #
# Javascript banner rotation removed by Carter v0.9.4                         #
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
# File: Last modified: 10/30/02 by Floyd                                      #
###############################################################################
###############################################################################

$| = 1;

use CGI::Carp qw(fatalsToBrowser);

$scriptname = "WebAPP";
$scriptver = "0.9.9";

eval {
	require "../../config.pl";
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
$database="$datadir/banners/data.txt";

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
lock(ORGDB);
@ODB=<ORGDB>;
unlock(ORGDB);
close (ORGDB);

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################

check_access(editbanner); if ($access_granted ne "1") { error("$err{'011'}"); }

$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $banner{'015'}";
print_top();

print qq~<table width='100%' cellspacing="1" cellpadding="3" border='1'>
<tr><td colspan="3" align="left" class="forumwindow3"><a href="add.cgi\?database=$db">$banner{'002'}</a></td></tr>
<tr><td align="center" class="forumwindow1"><b>$banner{'012'}</b></td><td align="center" class="forumwindow1"><b>$banner{'018'}</b></td><td align="center" class="forumwindow1"><b>$banner{'017'}</b></td></tr>
~;
foreach $rec (@ODB){
	chomp($rec);
	($banurl,$iban,$iw,$ih,$alt,$hits)=split(/\|/,$rec);
	if ($hits eq "") {$hits = 0;}
	$siw = ($iw/2); $sih = ($ih/2);

	$banurl =~ s/\=/EQSIGN/g;
	$banurl =~ s/\?/QMSIGN/g;
	$banurl =~ s/\"/DQUOTE/g;
	$banurl =~ s/\'/SQUOTE/g;
	$banurl =~ s/\&/AMPSIGN/g;

print qq~
<tr><td align="center" width="15%" class="forumwindow1"><a href="edit_record.cgi?banurl=$banurl\&iban=$iban\&iw=$iw\&ih=$ih\&alt=$alt\&hit=$hits">$banner{'013'}</a> - <a href="edit.cgi?action=delete\&banurl=$banurl\&iban=$iban\&iw=$iw\&ih=$ih\&alt=$alt\&hit=$hits">$banner{'014'}</a></td><td align="center" width="70%" class="forumwindow1"><a href="$banurl" target="_blank" class="bannerlink"><img src="$iban" width="$siw" height="$sih" alt="$alt" border="0"></a></td><td align="center" width="15%" class="forumwindow1">$hits</td></tr>\n
~;
}
print qq~<tr><td colspan="3" align="left" class="forumwindow3"><a href="add.cgi\?database=$db">$banner{'002'}</a></td></tr>
</table><br>~;

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

