#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# view.cgi for admin/language                                                 #
# v0.9.9 - Requin                                                             #
# Added by Floyd                                                              #
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

if ( $action eq "addlang" ) { addlang(); }
elsif ( $action eq "addlang2" ) { addlang2(); }
elsif ( $action eq "editlang" ) { editlang(); }
elsif ( $action eq "editlang2" ) { editlang2(); }
elsif ( $action eq "deletelang" ) { deletelang(); }
else { viewlang(); }

##############
sub viewlang {
##############

	open (ORGDB,"<$scriptdir/lang/languages.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	$navbar = "$btn{'014'} $mnu{'043'} $btn{'014'} $msg{'190'}";
	print_top();

	if ($username ne "admin") { error("$err{'011'}"); }

	print qq~<font face='Arial' size='2'><i>$msg{'190'}</i></font>
<table width='100%' border='1'>
<tr>
<td bgcolor='#F2C973'><font size='2'>$msg{'208'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'185'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'186'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'187'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'188'}</font></td>
</tr>
~;

	foreach $rec (@ODB){
		chomp($rec);
		($language,$file,$status,$langgfx)=split(/\|/,$rec);
		print qq~<tr>
<td><font size="2"><a href="$pageurl/admin/language.cgi?action=editlang&amp;language=$language&amp;file=$file&amp;status=$status&amp;langgfx=$langgfx">$nav{'096'}</a> - <a
 href="$pageurl/admin/language.cgi?action=deletelang&amp;language=$language&amp;file=$file&amp;status=$status&amp;langgfx=$langgfx">$nav{'097'}</a></font></td>
<td><font size="2">$language</font></td>
<td><font size="2">$file</font></td>
<td><font size="2">$status</font></td>
<td><font size="2">$langgfx</font></td>
</tr>
~;
	}

	print qq~</table>
<p><a href="$pageurl/admin/language.cgi?action=addlang">$nav{'095'}</a></p>
<br>
<br>
$msg{'191'}~;

	print_bottom();
	exit;
}

##############
sub editlang {
##############

	$navbar = "$btn{'014'} $mnu{'043'} $btn{'014'} $msg{'189'}";
	print_top();

	if ($username ne "admin") { error("$err{'011'}"); }

	print qq~<font face='Arial'><b><i>$msg{'189'}</i></b></font>
<form action='$pageurl/admin/language.cgi?action=editlang2' method='post'>
<input type='hidden' name='language' value='$info{'language'}'>
<input type='hidden' name='file' value='$info{'file'}'>
<input type='hidden' name='status' value='$info{'status'}'>
<input type='hidden' name='langgfx' value='$info{'langgfx'}'>
<table border='1'>
<tr>
<td><font size='2'>$msg{'185'}</font></td>
<td><input type='text' name='nlanguage' value="$info{'language'}"></td>
</tr>
<tr>
<td><font size='2'>$msg{'186'}</font></td>
<td><input type='text' name='nfile' value="$info{'file'}"></td>
</tr>
<tr>
<td><font size='2'>$msg{'187'}</font></td>
<td><input type='text' name='nstatus' value="$info{'status'}"></td>
</tr>
<tr>
<td><font size='2'>$msg{'188'}</font></td>
<td><input type='text' name='nlanggfx' value="$info{'langgfx'}"></td>
</tr>
</table>
<input type='submit' value='$btn{'020'}'></form>~;

	print_bottom();
	exit;
}

###############
sub editlang2 {
###############

	if ($username ne "admin") { error("$err{'011'}"); } 

	open (ORGDB,"<$scriptdir/lang/languages.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	open (DATABASE,">$scriptdir/lang/languages.dat");
	hold (DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($language,$file,$status,$langgfx)=split(/\|/,$rec);
		if ($language eq $input{'language'} && $file eq $input{'file'} && $status eq $input{'status'} && $langgfx eq $input{'langgfx'}){
			print DATABASE "$input{'nlanguage'}|$input{'nfile'}|$input{'nstatus'}|$input{'nlanggfx'}\n";
		} else {
			print DATABASE "$language|$file|$status|$langgfx\n";
		}
	}
	release (DATABASE);	
	close (DATABASE);

	print "Location: $pageurl/admin/language.cgi\n\n";
}

#############
sub addlang {
#############

	if ($username ne "admin") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $mnu{'043'} $btn{'014'} $msg{'184'}";
	print_top();

	print qq~<font face='Arial' size='2'><b><i>$msg{'184'}</i></b></font>
<form action='$pageurl/admin/language.cgi?action=addlang2' method='post'>
<table border='1'>
<tr>
<td><font size='2'>$msg{'185'}</font></td>
<td><input type='text' name='nlanguage'></td>
</tr>
<tr>
<td><font size='2'>$msg{'186'}</font></td>
<td><input type='text' name='nfile'></td>
</tr>
<tr>
<td><font size='2'>$msg{'187'}</font></td>
<td><input type='text' name='nstatus'></td>
</tr>
<tr>
<td><font size='2'>$msg{'188'}</font></td>
<td><input type='text' name='nlanggfx'></td>
</tr>
</table><input type='submit' value='$btn{'019'}'></form>~;

	print_bottom();
	exit;
}

##############
sub addlang2 {
##############

	if ($username ne "admin") { error("$err{'011'}"); } 
	open (DATABASE1,">>$scriptdir/lang/languages.dat");
	hold (DATABASE1);
	print DATABASE1 "$input{'nlanguage'}|$input{'nfile'}|$input{'nstatus'}|$input{'nlanggfx'}\n";
	release (DATABASE1);
	close (DATABASE1);
	print "Location: $pageurl/admin/language.cgi\n\n";
}

################
sub deletelang {
################

	if ($username ne "admin") { error("$err{'011'}"); }

	open (ORGDB,"<$scriptdir/lang/languages.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	open (DATABASE,">$scriptdir/lang/languages.dat");
	hold (DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($language,$file,$status,$langgfx)=split(/\|/,$rec);
		if ($language eq $info{'language'} && $file eq $info{'file'} && $status eq $info{'status'} && $langgfx eq $info{'langgfx'}){
			print DATABASE "";
		} else {
			print DATABASE "$language|$file|$status|$langgfx\n";
		}
	}
	release (DATABASE);
	close (DATABASE);

	print "Location: $pageurl/admin/language.cgi\n\n";
}

1;
