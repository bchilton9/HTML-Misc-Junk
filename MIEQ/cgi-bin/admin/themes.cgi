#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# view.cgi for admin/themes                                                   #
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

if ( $action eq "addtheme" ) { addtheme(); }
elsif ( $action eq "addtheme2" ) { addtheme2(); }
elsif ( $action eq "editrecord" ) { editrecord(); }
elsif ( $action eq "editrecord2" ) { editrecord2(); }
elsif ( $action eq "deletetheme" ) { deletetheme(); }
else { viewthemes(); }

################
sub viewthemes {
################

	$navbar = "$btn{'014'} $mnu{'004'} $btn{'014'} $msg{'370'}";
	print_top();

	if ($username ne "admin") { error("$err{'011'}"); }

	print qq~<font face='Arial' size='2'><i>$msg{'370'}</i></font>
<table width='100%' border='1'>
<tr>
<td bgcolor='#F2C973'><font size='2'>$msg{'354'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'368'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'356'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'351'}</font></td>
</tr>
~;

	open (ORGDB,"<$themesdir/themes.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	foreach $rec (@ODB){
		chomp($rec);
		($themes,$dir,$status)=split(/\|/,$rec);
		print qq~<tr>
<td><font size="2"><a href="$pageurl/admin/themes.cgi?action=editrecord&amp;themes=$themes&amp;dir=$dir&amp;status=$status">$nav{'096'}</a> - <a href="$pageurl/admin/themes.cgi?action=deletetheme&amp;themes=$themes&amp;dir=$dir&amp;status=$status">$nav{'097'}</a></font></td><td><font size="2">$themes</font></td><td><font size="2">$dir</font></td><td><font size="2">$status</font></td></tr>~;
}
print qq~</table>
<p><a href="$pageurl/admin/themes.cgi?action=addtheme">$nav{'098'}</a></p>
<br>
<br>
$msg{'191'}~;

	print_bottom();
	exit;
}

################
sub editrecord {
################

	$navbar = "$btn{'014'} $mnu{'004'} $btn{'014'} $btn{'038'}";
	print_top();

	if ($username ne "admin") { error("$err{'011'}"); }

	print qq~<font face='Arial'><i>$msg{'369'}</i></font><br>
<form action='$pageurl/admin/themes.cgi?action=editrecord2' method='post'>
<input type='hidden' name='themes' value='$info{'themes'}'>
<input type='hidden' name='dir' value='$info{'dir'}'>
<input type='hidden' name='status' value='$info{'status'}'>
<table border='1'>
<tr>
<td><font size='2'>$msg{'368'}</font></td>
<td><input type='text' name='nthemes' value="$info{'themes'}"></td>
</tr>
<tr>
<td><font size='2'>$msg{'356'}</font></td>
<td><input type='text' name='ndir' value="$info{'dir'}"></td>
</tr>
<tr>
<td><font size='2'>$msg{'351'}</font></td>
<td><input type='text' name='nstatus' value="$info{'status'}"></td>
</tr>
</table>
<input type='Submit' value='$btn{'038'}'></form>~;

	print_bottom();
	exit;
}

#################
sub editrecord2 {
#################

	if ($username ne "admin") { error("$err{'011'}"); } 

	open (ORGDB,"<$themesdir/themes.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	open (DATABASE,">$themesdir/themes.dat");
	hold (DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($themes,$dir,$status)=split(/\|/,$rec);
		if ($themes eq $input{'themes'} && $dir eq $input{'dir'} && $status eq $input{'status'}){
			print DATABASE "$input{'nthemes'}|$input{'ndir'}|$input{'nstatus'}\n";
		} else {
			print DATABASE "$themes|$dir|$status\n";
		}
	}
	release (DATABASE);	
	close (DATABASE);

	print "Location: $pageurl/admin/themes.cgi\n\n";
}

##############
sub addtheme {
##############

	$navbar = "$btn{'014'} $mnu{'004'} $btn{'014'} $btn{'037'}";
	print_top();

	if ($username ne "admin") { error("$err{'011'}"); }

	print qq~<font face='Arial'><i>$msg{'367'}</i><font><br>
<form action='$pageurl/admin/themes.cgi?action=addtheme2' method='post'>
<table border='1'>
<tr>
<td><font size='2'>$msg{'368'}</font></td>
<td><input type='text' name='nthemes'></td>
<td>$msg{'550'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'356'}</font></td>
<td><input type='text' name='ndir'></td>
<td>$msg{'551'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'351'}</font></td>
<td><input type='text' name='nstatus'></td>
<td>$msg{'552'}</td>
</tr>
</table>
<input type='Submit' value='$btn{'037'}'></form>~;

	print_bottom();
	exit;
}

###############
sub addtheme2 {
###############

	if ($username ne "admin") { error("$err{'011'}"); } 

	open (DATABASE1,">>$themesdir/themes.dat");
	hold (DATABASE1);
	print DATABASE1 "$input{'nthemes'}|$input{'ndir'}|$input{'nstatus'}\n";
	release (DATABASE1);
	close (DATABASE1);
	print "Location: $pageurl/admin/themes.cgi\n\n";
}

#################
sub deletetheme {
#################

	if ($username ne "admin") { error("$err{'011'}"); }

	open (ORGDB,"<$themesdir/themes.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	open (DATABASE,">$themesdir/themes.dat");
	hold (DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($themes,$dir,$status)=split(/\|/,$rec);
		if ($themes eq $info{'themes'} && $dir eq $info{'dir'} && $status eq $info{'status'}){
			print DATABASE "";
		} else {
			print DATABASE "$themes|$dir|$status\n";
		}
	}

	release (DATABASE);	
	close (DATABASE);

	print "Location: $pageurl/admin/themes.cgi\n\n";
}

1;
