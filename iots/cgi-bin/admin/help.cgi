#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# view.cgi for admin/help                                                     #
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
# File: Last modified: 2005                                                   #
###############################################################################
###############################################################################

$| = 1;

use CGI::Carp qw(fatalsToBrowser);

$scriptname = "WebAPP";

eval {
	require "../config.pl";
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

if ($action eq "addhlp") { addhlp(); }
elsif ($action eq "addhlp2") { addhlp2(); }
elsif ($action eq "edithlp") { edithlp(); }
elsif ($action eq "edithlp2") { edithlp2(); }
elsif ($action eq "deletehlp") { deletehlp(); }
else { viewhelp(); }

##############
sub viewhelp {
##############

	check_access("editfaq"); if ($access_granted ne "1") { error("$err{'011'}"); }

	open (ORGDB,"<$datadir/help/data.txt");
	hold(ORGDB);
	@ODB=<ORGDB>;
	release(ORGDB);
	close (ORGDB);

	$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $help{'015'}";
	print_top();

	print qq~<font face='Arial' size='2'><b><i>$help{'011'}</i></b></font>
<table width='100%' border='1'>
<tr>
<td bgcolor='#F2C973'><font size='2'>$help{'012'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$help{'003'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$help{'004'}</font></td>
</tr>
~;

	foreach $rec (@ODB){
		chomp($rec);
		($helpq,$helpa)=split(/\|/,$rec);
		print qq~<tr>
<td><font size="2"><a href="$pageurl/admin/help.cgi?action=edithlp&amp;question=$helpq">$help{'013'}</a> - <a
 href="$pageurl/admin/help.cgi?action=deletehlp&amp;question=$helpq">$help{'014'}</a></font></td>
<td><font size="2">$helpq</font></td>
<td><font size="2">$helpa</font></td>
</tr>
~;
	}

	print qq~</table>
<p><a href="$pageurl/admin/help.cgi?action=addhlp">$help{'002'}</a></p>
~;

	print_bottom();
	exit;

}

############
sub addhlp {
############

	check_access("editfaq"); if ($access_granted ne "1") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $help{'002'}";
	print_top();

	print qq~<font face='Arial'><b><i>$help{'002'}</i></b></font>
<form action='$pageurl/admin/help.cgi?action=addhlp2' method='post'>
<table border='1'>
<tr>
<td><font size='2'>$help{'003'}</font></td>
<td><input type='text' name='nhelpq'></td>
</tr>
<tr>
<td><font size='2'>$help{'004'}</font></td>
<td><textarea name="nhelpa" cols="40" rows="10"></textarea></td>
</tr>
</table>
<input type='submit' value='$help{'002'}'>
</form>~;

	print_bottom();
	exit;

}

#############
sub addhlp2 {
#############

	check_access("editfaq"); if ($access_granted ne "1") { error("$err{'011'}"); }

	if ($input{'nhelpq'} eq "") {error("$err{'034'}");}
	if ($input{'nhelpa'} eq "") {error("$err{'035'}");}

	$input{'nhelpa'} =~ s~[\n]~<BR>~g; 
	$input{'nhelpa'} =~ s~[\r]~~g; 
	open (DATABASE1,">>$datadir/help/data.txt");
	hold(DATABASE1);
	print DATABASE1 "$input{'nhelpq'}|$input{'nhelpa'}\n";
	release(DATABASE1);
	close (DATABASE1);

	print "Location: $pageurl/admin/help.cgi\n\n"; 
	exit;

}

#############
sub edithlp {
#############

	check_access("editfaq"); if ($access_granted ne "1") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $help{'010'}";
	print_top();

	open(FILE, "<$datadir/help/data.txt");
	hold(FILE);
	chomp(@datas = <FILE>);
	release(FILE);
	close(FILE);

	foreach $rec (@datas){
		chomp($rec);
		($helpq,$helpa)=split(/\|/,$rec);

		if ($info{'question'} eq "$helpq") {
			$helpa =~ s~<BR>~\n~g;
			print qq~<font face='Arial'><b><i>$help{'010'}</i></b></font>
<form action='$pageurl/admin/help.cgi?action=edithlp2' method='post'>
<input type='hidden' name='helpq' value='$helpq'>
<table border='1'>
<tr>
<td><font size='2'>$help{'003'}</font></td>
<td><textarea name="nhelpq" cols="40" rows="2">$helpq</textarea></td>
</tr>
<tr>
<td><font size='2'>$help{'004'}</font></td>
<td><textarea name="nhelpa" cols="40" rows="10">$helpa</textarea></td>
</tr>
</table>
<input type='Submit' value='$help{'010'}'>
</form>
~;

		}

		else {}

	}

	print_bottom();
	exit;

}

##############
sub edithlp2 {
##############

	open (ORGDB,"<$datadir/help/data.txt");
	hold(ORGDB);
	@ODB=<ORGDB>;
	release(ORGDB);
	close (ORGDB);

	open (DATABASE,">$datadir/help/data.txt");
	hold(DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($helpq,$helpa)=split(/\|/,$rec);

		if ($helpq eq $input{'helpq'}){
			$input{'nhelpa'} =~ s~[\n]~<BR>~g; 
			$input{'nhelpa'} =~ s~[\r]~~g;
			print DATABASE "$input{'nhelpq'}|$input{'nhelpa'}\n";
		} else {
			print DATABASE "$helpq|$helpa\n";
		}
	}
	release(DATABASE);	
	close (DATABASE);

	print "Location: $pageurl/admin/help.cgi\n\n"; 
	exit;

}

###############
sub deletehlp {
###############

	check_access("editfaq"); if ($access_granted ne "1") { error("$err{'011'}"); }

	open (ORGDB,"<$datadir/help/data.txt");
	hold(ORGDB);
	@ODB=<ORGDB>;
	release(ORGDB);
	close (ORGDB);
 
	open (DATABASE,">$datadir/help/data.txt");
	hold(DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($helpq,$helpa)=split(/\|/,$rec);

		if ($helpq eq $info{'question'}){
			print DATABASE "";
		} else {
			print DATABASE "$helpq|$helpa\n";
		}
	}
	release(DATABASE);	
	close (DATABASE);

	print "Location: $pageurl/admin/help.cgi\n\n"; 
	exit;

}

1;
