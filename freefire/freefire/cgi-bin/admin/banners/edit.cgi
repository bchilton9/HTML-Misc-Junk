#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# edit.cgi for admin/banners                                                  #
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
# File: Last modified: 10/30/02                                               #
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

if ($username ne "admin") { error("$err{'011'}"); } 

#######################################
# Define the variables for the script #
#######################################
$database="$datadir/banners/data.txt";
$databaseview="$scripturl/admin/banners/view.cgi";

############################
# Get data from GET & POST #
############################
&parse_form;

#################################################
# Get the origional database data & buffer data #
#################################################
open (ORGDB,"<$database");
file_lock(ORGDB);
@ODB=<ORGDB>;
unfile_lock(ORGDB);
close (ORGDB);

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################
open (DATABASE,">$database");
file_lock(DATABASE);
@DB=<DATABASE>;
	foreach $rec (@ODB){
		chomp($rec);
		($banurl,$iban,$iw,$ih,$alt,$hits)=split(/\|/,$rec);

	$input{'banurl'} =~ s/EQSIGN/\=/g;
	$input{'banurl'} =~ s/QMSIGN/\?/g;
	$input{'banurl'} =~ s/DQUOTE/\"/g;
	$input{'banurl'} =~ s/SQUOTE/\'/g;
	$input{'banurl'} =~ s/AMPSIGN/\&/g;

		if ($banurl eq $input{'banurl'} && $iban eq $input{'iban'}){
		print DATABASE "$input{'nbanurl'}|$input{'niban'}|$input{'niw'}|$input{'nih'}|$input{'nalt'}|$input{'nhit'}\n";
		}else{
		print DATABASE "$banurl|$iban|$iw|$ih|$alt|$hits\n";
		}
	}
unfile_lock(DATABASE);
close (DATABASE);

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################
if ($input{'action'} eq 'add'){
check_access(editbanner); if ($access_granted ne "1") { error("$err{'011'}"); } 
open (DATABASE1,">>$database");
file_lock(DATABASE);
print DATABASE1 "$input{'nbanurl'}|$input{'niban'}|$input{'niw'}|$input{'nih'}|$input{'nalt'}|0\n";
unfile_lock(DATABASE);
close (DATABASE1);
}

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################
if ($input{'action'} eq "delete"){
check_access(editbanner); if ($access_granted ne "1") { error("$err{'011'}"); } 
open (DATABASE,">$database");
file_lock(DATABASE);
@DB=<DATABASE>;
	foreach $rec (@ODB){
		chomp($rec);
		($banurl,$iban,$iw,$ih,$alt,$hits)=split(/\|/,$rec);

	$info{'banurl'} =~ s/EQSIGN/\=/g;
	$info{'banurl'} =~ s/QMSIGN/\?/g;
	$info{'banurl'} =~ s/DQUOTE/\"/g;
	$info{'banurl'} =~ s/SQUOTE/\'/g;
	$info{'banurl'} =~ s/AMPSIGN/\&/g;

		if ($banurl eq $info{'banurl'} && $iban eq $info{'iban'}){
		print DATABASE "";
		}else{
		print DATABASE "$banurl|$iban|$iw|$ih|$alt|$hits\n";
		}
	}
unfile_lock(DATABASE);
close (DATABASE);
}
########################################
# Print a small message to the browser #
########################################
print "Location: $databaseview\n\n";

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

