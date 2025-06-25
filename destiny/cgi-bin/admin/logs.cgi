#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# view.cgi for admin/logs                                                     #
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


viewlog();

#############
sub viewlog {
#############

	$navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $nav{'053'}";
	print_top();

	if ($username ne "admin") { error("$err{'011'}"); }

	open (ORGDB1,"<$datadir/recommend.log");
	hold (ORGDB1);
	@ODB1=<ORGDB1>;
	release (ORGDB1);
	close (ORGDB1);

	print qq~<font face='Arial' size='2'><i>$msg{'365'}</i></font>
<table width='100%' border='1'>
<tr>
<td bgcolor='#F2C973'><font size='2'>$msg{'214'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'360'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'361'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'362'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'363'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'364'}</font></td>
</tr>
~;

	foreach $rec1 (@ODB1){
		chomp($rec1);
		($dater,$refererr,$senderr,$senderemailr,$recipr,$recipemailr)=split(/\|/,$rec1);
		print qq~<tr>
<td><font size="2">$dater</font></td>
<td><font size="2">$refererr</font></td>
<td><font size="2">$senderr</font></td>
<td><font size="2">$senderemailr</font></td>
<td><font size="2">$recipr</font></td>
<td><font size="2">$recipemailr</font></td>
</tr>
~;
	}

	print qq~</table>~;

	print_bottom();
	exit;
}

1;
