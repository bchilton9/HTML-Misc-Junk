#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# edit.cgi for admin/blocks/left                                              #
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
# File: Last modified: 09/12/02 by Carter                                     #
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


#######################################
# Define the variables for the script #
#######################################
$database="$datadir/blocks/blockleft.dat";
$databaseview="$scripturl/admin/blocks/left/view.cgi";

############################
# Get data from GET & POST #
############################
&parse_form;

#################################################
# Get the origional database data & buffer data #
#################################################

check_access(editlblk); if ($access_granted ne "1") { error("$err{'011'}"); } 

open (ORGDB,"<$database");
@ODB=<ORGDB>;
close (ORGDB);

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################
open (DATABASE,">$database");
@DB=<DATABASE>;
	foreach $rec (@ODB){
		chomp($rec);
		($block,$title,$stat,$bcont,$only)=split(/\|/,$rec);
		if ($block eq $input{'block'}){
		$cont = htmlescape($input{'nbcont'});
		print DATABASE "$input{'nblock'}|$input{'ntitle'}|$input{'nstat'}|$cont|$input{'nonly'}\n";
		}else{
		print DATABASE "$block|$title|$stat|$bcont|$only\n";
		}
	}
close (DATABASE);

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################
if ($input{'action'} eq 'add'){
check_access(editlblk); if ($access_granted ne "1") { error("$err{'011'}"); } 
open (DATABASE1,">>$database");
$cont = htmlescape($input{'nbcont'});
print DATABASE1 "$input{'nblock'}|$input{'ntitle'}|$input{'nstat'}|$cont|$input{'nonly'}";
close (DATABASE1);
}

#################################################################
# Open the database to write data, changing the neccesary lines #
#################################################################
if ($input{'action'} eq 'delete'){
check_access(editlblk); if ($access_granted ne "1") { error("$err{'011'}"); } 
open (DATABASE,">$database");
@DB=<DATABASE>;
@raw_data=<DATABASE>;

	foreach $rec (@ODB){
		chomp($rec);
		($block,$title,$stat,$bcont,$only)=split(/\|/,$rec);
		if ($block eq $input{'block'}){
 		print DATABASE @raw_data;
		}
		else{
		print DATABASE "$block|$title|$stat|$bcont|$only\n";
		}
	}
		close (DATABASE);
}

################
sub htmlescape {
################
	my $text = shift;

	$text =~ s/&/&amp;/g;
	$text =~ s/"/&quot;/g;
	$text =~ s/  / \&nbsp;/g;
	$text =~ s/</&lt;/g;
	$text =~ s/>/&gt;/g;
	$text =~ s/\t/ \&nbsp; \&nbsp; \&nbsp;/g;
	$text =~ s/\cM//g;
	$text =~ s/\n/<br>/g;
	$text =~ s/\|/<pipe>/g;
	

	return $text;
}

################
sub htmltotext {
################
	my $html = shift;

	$html =~ s~<br>~\n~gi;
	$html =~ s~<\/*(blockquote|ul|li|p)[^<>]*>~\n\n~gi;
	$html =~ s~<a href=\"*([^\s<>\"]+)\"*[^>]*>([\s\S]+?)<\/a>~$2 (link: $1)~gi;
	$html =~ s~<[^>]+>~~g;
	$html =~ s~\"~&quot;~g;
	$html =~ s/ \&nbsp;/  /g;
	$html =~ s~<pipe>~\|~g;

	return $html;
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


1;
