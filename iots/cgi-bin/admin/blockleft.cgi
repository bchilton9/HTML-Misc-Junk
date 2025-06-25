#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# view.cgi for admin/blocks/left                                              #
# v0.9.9.2 - Requin                                                           #
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
<p>If this problem persists, please contact the webmaster and inform him about date and time you've received this error.</p>
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

if ( $action eq "addlblk" ) { addlblk(); }
elsif ( $action eq "addlblk2" ) { addlblk2(); }
elsif ( $action eq "editlblk" ) { editlblk(); }
elsif ( $action eq "editlblk2" ) { editlblk2(); }
elsif ( $action eq "deletelblk" ) { deletelblk(); }
else { viewlblk(); }

##############
sub viewlblk {
##############

	check_access("editlblk"); if ($access_granted ne "1") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $nav{'063'} $btn{'014'} $btn{'034'} $btn{'014'} $mnu{'021'}";
	print_top();

	print qq~<i>$btn{'034'}</i>
<table border="1">
<tr>
<td width="150" align="center" bgcolor='#F2C973'><b>$msg{'353'}</b></td>
<td align="center" bgcolor='#F2C973'><b>$help{'012'}</b></td>
</tr>
~;

	open (ORGDB,"<$datadir/blocks/blockleft.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	foreach $rec (@ODB){
		chomp($rec);
		($block,$title,$stat,$bcont)=split(/\|/,$rec);
		$cont = showhtml($bcont);
		$cont =~ s/&&/\n/g;
		$cont =~ s/&lt;/</ig;

		print qq~<tr>
<td><table width="150">~;

		print qq~<tr>
<td><table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable">
<tr>
<td>&nbsp;$title</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menubordercolor">
<tr>
<td width="100%"><table border="0" cellpadding="0" cellspacing="3"
 width="100%" class="menubackcolor">
~;

		print qq~<tr>
<td>$cont</td>
</tr>
~;

		print qq~</table></td>
</tr>
</table></td>
</tr>
~;

		print qq~</table></td>
<td align="center"><a
 href="$pageurl/admin/blockleft.cgi?action=editlblk&amp;block=$block&amp;title=$title&amp;stat=$stat">$nav{'096'}</a> - <a
 href="$pageurl/admin/blockleft.cgi?action=deletelblk&amp;block=$block&amp;title=$title&amp;stat=$stat">$nav{'097'}</a></td>
</tr>
~;
	}

	print qq~<tr>
<td align="center" colspan="2"><a
 href="$pageurl/admin/blockleft.cgi?action=addlblk">&nbsp;$nav{'121'}</a></td>
</tr>
</table>
<br>
~;

	print_bottom();
	exit;
}

###############
sub editlblk {
###############

	check_access("editlblk"); if ($access_granted ne "1") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $nav{'063'} $btn{'014'} $nav{'120'}";
	print_top();

	open(FILE, "$datadir/blocks/blockleft.dat" || print "There was an error" );
	hold(FILE);
	chomp(@blocks = <FILE>);
	release(FILE);
	close(FILE);

	for ($a = 0; $a < @blocks; $a++) {
		($ablock, $atitle, $astat, $abcont, $only) = split(/\|/, $blocks[$a]);
		if ($ablock eq $info{'block'} and $atitle eq $info{'title'}) {
			$cont = htmltotext($abcont); # to put to a form for editing
			$cont =~ s/&amp;&amp;/\n/g; # inverse of regex to save line breaks inside tags

			print qq~<font face='Arial'><b><i>$btn{'033'}</i></b></font>
<form action='$pageurl/admin/blockleft.cgi?action=editlblk2' method='post'>
<input type='hidden' name='block' value='$info{'block'}'>
<input type='hidden' name='title' value='$info{'title'}'>
<table border='1'>
<tr>
<td><font size='2'>$msg{'349'}</font></td>
<td><input type='text' name='nblock' value="$info{'block'}"> $msg{'573'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'350'}</font></td>
<td><input type='text' name='ntitle' value="$info{'title'}"> $msg{'574'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'351'}</font></td>
<td><input type='text' name='nstat' value="$info{'stat'}"> $msg{'552'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'587'}</font></td>
<td><input type='text' name='nonly' value="$only"> $msg{'575'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'352'}</font></td>
<td><textarea name='nbcont' rows='20' cols='40' wrap='off'>$cont</textarea></td>
</tr>
</table>
<input type='submit' value='$btn{'033'}'>
</form>
~;

		}
	}

	print_bottom();
	exit;
}

###############
sub editlblk2 {
###############

	check_access("editlblk"); if ($access_granted ne "1") { error("$err{'011'}"); }

	open (ORGDB,"<$datadir/blocks/blockleft.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	open (DATABASE,">$datadir/blocks/blockleft.dat");
	hold (DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($block,$title,$stat,$bcont,$only)=split(/\|/,$rec);
		if ($block eq $input{'block'}){
			$input{'nbcont'} =~ s/\n(?=[^<]+>)/&&/gs; # save line breaks inside tags
			$cont = htmlescape($input{'nbcont'});
			$cont =~ s/scrypt/script/g; #
			$cont =~ s/yframe/iframe/g; # allow for javascript and iframe in blocks

			print DATABASE "$input{'nblock'}|$input{'ntitle'}|$input{'nstat'}|$cont|$input{'nonly'}\n";
		} else {
			print DATABASE "$block|$title|$stat|$bcont|$only\n";
		}
	}

	release (DATABASE);
	close (DATABASE);

	print "Location: $pageurl/admin/blockleft.cgi\n\n";
}

#############
sub addlblk {
#############

	check_access("editlblk"); if ($access_granted ne "1") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $nav{'063'} $btn{'014'} $nav{'119'}";
	print_top();

	print qq~<font face='Arial'><b><i>$msg{'348'}</i></b></font>
<form action='$pageurl/admin/blockleft.cgi?action=addlblk2' method='post'>
<table border='1' width='100%'>
<tr>
<td><font size='2'>$msg{'349'}</font></td>
<td><input type='text' name='nblock'> $msg{'573'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'350'}</font></td>
<td><input type='text' name='ntitle'> $msg{'574'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'351'}</font></td>
<td><input type='text' name='nstat'> $msg{'552'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'587'}</font></td>
<td><input type='text' name='nonly'> $msg{'575'}</td>
</tr>
<tr>
<td><font size='2'>$msg{'352'}</font></td>
<td><textarea name='nbcont' rows='20' cols='40' wrap='off'></textarea></td>
</tr>
</table>
<input type='submit' value='$btn{'022'}'></form>
~;

	print_bottom();
	exit;
}

##############
sub addlblk2 {
##############

	check_access("editlblk"); if ($access_granted ne "1") { error("$err{'011'}"); }

	open (DATABASE1,">>$datadir/blocks/blockleft.dat");
	hold (DATABASE1);

	$input{'nbcont'} =~ s/\n(?=[^<]+>)/&&/gs; # save line breaks inside tags
	$cont = htmlescape($input{'nbcont'});
	$cont =~ s/scrypt/script/g; #
	$cont =~ s/yframe/iframe/g; # allow for javascript and iframe in blocks

	print DATABASE1 "$input{'nblock'}|$input{'ntitle'}|$input{'nstat'}|$cont|$input{'nonly'}";

	release (DATABASE1);
	close (DATABASE1);

	print "Location: $pageurl/admin/blockleft.cgi\n\n";
}

################
sub deletelblk {
################

	check_access("editlblk"); if ($access_granted ne "1") { error("$err{'011'}"); }

	open (ORGDB,"<$datadir/blocks/blockleft.dat");
	hold (ORGDB);
	@ODB=<ORGDB>;
	release (ORGDB);
	close (ORGDB);

	open (DATABASE,">$datadir/blocks/blockleft.dat");
	hold (DATABASE);
	@raw_data=<DATABASE>;

	foreach $rec (@ODB){
		chomp($rec);
		($block,$title,$stat,$bcont,$only)=split(/\|/,$rec);
		if ($block eq $info{'block'}){
 			print DATABASE @raw_data;
		} else {
			print DATABASE "$block|$title|$stat|$bcont|$only\n";
		}
	}

	release (DATABASE);
	close (DATABASE);

	print "Location: $pageurl/admin/blockleft.cgi\n\n";
}

1;
