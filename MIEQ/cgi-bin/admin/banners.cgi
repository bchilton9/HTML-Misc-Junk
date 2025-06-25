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

if ( $action eq "addbanner" ) { addbanner(); }
elsif ( $action eq "addbanner2" ) { addbanner2(); }
elsif ( $action eq "editbanner" ) { editbanner(); }
elsif ( $action eq "editbanner2" ) { editbanner2(); }
elsif ( $action eq "deletebanner" ) { deletebanner(); }
else { viewbanner(); }

################
sub viewbanner {
################

	check_access("editbanner"); if ($access_granted ne "1") { error("$err{'011'}"); }

	open (ORGDB,"<$datadir/banners/data.txt");
	hold(ORGDB);
	@ODB=<ORGDB>;
	release(ORGDB);
	close (ORGDB);

	$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $banner{'015'}";
	print_top();

	print qq~<table width='100%' cellspacing="1" cellpadding="3" border='1'>
<tr>
<td colspan="3" align="left" class="forumwindow3"><a
 href="$pageurl/admin/banners.cgi?action=addbanner">$banner{'002'}</a></td>
</tr>
<tr>
<td align="center" class="forumwindow1"><b>$banner{'012'}</b></td>
<td align="center" class="forumwindow1"><b>$banner{'018'}</b></td>
<td align="center" class="forumwindow1"><b>$banner{'017'}</b></td>
</tr>
~;

	foreach $rec (@ODB){
		chomp($rec);
		($banurl,$iban,$iw,$ih,$alt,$hits)=split(/\|/,$rec);
		if ($hits eq "") {$hits = 0;}
		$siw = ($iw/2); $sih = ($ih/2);

	$clickurl = $banurl; # clickable banners here
	$banurl =~ s/\=/EQSIGN/g;
	$banurl =~ s/\?/QMSIGN/g;
	$banurl =~ s/\"/DQUOTE/g;
	$banurl =~ s/\'/SQUOTE/g;
	$banurl =~ s/\&/AMPSIGN/g;

		print qq~<tr>
<td align="center" width="15%" class="forumwindow1"><a
 href="$pageurl/admin/banners.cgi?action=editbanner&amp;banurl=$banurl&amp;iban=$iban&amp;iw=$iw&amp;ih=$ih&amp;alt=$alt&amp;hit=$hits">$banner{'013'}</a> - <a
 href="$pageurl/admin/banners.cgi?action=deletebanner&amp;banurl=$banurl&amp;iban=$iban&amp;iw=$iw&ih=$ih&amp;alt=$alt&amp;hit=$hits">$banner{'014'}</a></td>
<td align="center" width="70%" class="forumwindow1"><a
 href="$clickurl" target="_blank" class="bannerlink"><img
 src="$iban" width="$siw" height="$sih" alt="$alt" border="0"></a></td>
<td align="center" width="15%" class="forumwindow1">$hits</td>
</tr>
~;
	}

	print qq~<tr>
<td colspan="3" align="left" class="forumwindow3"><a
 href="$pageurl/admin/banners.cgi?action=addbanner">$banner{'002'}</a></td>
</tr>
</table>
<br>
~;

	print_bottom();
	exit;
}

############### 
sub addbanner {
###############

	check_access("editbanner"); if ($access_granted ne "1") { error("$err{'011'}"); }
 
	$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $banner{'002'}"; 
	print_top(); 
 
	print qq~<font face='Arial'><b><i>$banner{'002'}</i></b></font> 
<form action="$pageurl/admin/banners.cgi?action=addbanner2" method="post"> 
<table border='1'> 
<tr>
<td><font size='2'>$banner{'003'}</font></td>
<td><input type="text" name="nbanurl"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'004'}</font></td>
<td><input type="text" name="niban"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'005'}</font></td>
<td><input type="text" name="niw"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'006'}</font></td>
<td><input type="text" name="nih"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'007'}</font></td>
<td><input type="text" name="nalt"></td>
</tr> 
</table>
<input type='submit' value='$banner{'002'}'></form>~; 
 
	print_bottom();
	exit; 
} 

################
sub addbanner2 {
################

	check_access("editbanner"); if ($access_granted ne "1") { error("$err{'011'}"); } 

	open (DATABASE1,">>$datadir/banners/data.txt");
	hold(DATABASE1);
	print DATABASE1 "$input{'nbanurl'}|$input{'niban'}|$input{'niw'}|$input{'nih'}|$input{'nalt'}|0\n";
	release(DATABASE1);
	close (DATABASE1);

	print "Location: $pageurl/admin/banners.cgi\n\n"; 
	exit;
}

################
sub editbanner {
################

	check_access("editbanner"); if ($access_granted ne "1") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $banner{'010'}"; 
	print_top(); 
 
	print qq~<font face='Arial'><b><i>$banner{'010'}</i></b></font> 
<form action="$pageurl/admin/banners.cgi?action=editbanner2" method="post">
<input type='hidden' name="banurl" value="$info{'banurl'}"> 
<input type='hidden' name="iban" value="$info{'iban'}"> 
<table border='1'> ~;

# 5 substitution lines were here...
	$info{'banurl'} =~ s/EQSIGN/\=/g;
	$info{'banurl'} =~ s/QMSIGN/\?/g;
	$info{'banurl'} =~ s/DQUOTE/\"/g;
	$info{'banurl'} =~ s/SQUOTE/\'/g;
	$info{'banurl'} =~ s/AMPSIGN/\&/g;

print qq~<tr>
<td><font size='2'>$banner{'003'}</font></td>
<td><input type='text' name='nbanurl' value="$info{'banurl'}"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'004'}</font></td>
<td><input type="text" name="niban" value="$info{'iban'}"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'005'}</font></td>
<td><input type='text' name='niw' value="$info{'iw'}"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'006'}</font></td>
<td><input type='text' name='nih' value="$info{'ih'}"></td>
</tr> 
<tr>
<td><font size='2'>$banner{'007'}</font></td>
<td><input type='text' name='nalt' value="$info{'alt'}"></td>
</tr>
<tr>
<td><font size='2'>$banner{'017'}</font></td>
<td><input type='hidden' name='nhit' value="$info{'hit'}">$info{'hit'}</td>
</tr> 
</table>
<input type='submit' value='$banner{'010'}'></form>~; 
 
	print_bottom();
	exit; 
}

#################
sub editbanner2 {
#################

	open (ORGDB,"<$datadir/banners/data.txt");
	hold(ORGDB);
	@ODB=<ORGDB>;
	release(ORGDB);
	close (ORGDB);

	open(DATABASE,">$datadir/banners/data.txt");
	hold(DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($banurl,$iban,$iw,$ih,$alt,$hits)=split(/\|/,$rec);

# 5 substitution lines were here...
		$input{'banurl'} =~ s/EQSIGN/\=/g;
		$input{'banurl'} =~ s/QMSIGN/\?/g;
		$input{'banurl'} =~ s/DQUOTE/\"/g;
		$input{'banurl'} =~ s/SQUOTE/\'/g;
		$input{'banurl'} =~ s/AMPSIGN/\&/g;

		if ($banurl eq $input{'banurl'} && $iban eq $input{'iban'}){
			print DATABASE "$input{'nbanurl'}|$input{'niban'}|$input{'niw'}|$input{'nih'}|$input{'nalt'}|$input{'nhit'}\n";
		}	else	{
			print DATABASE "$banurl|$iban|$iw|$ih|$alt|$hits\n";
		}
	}
	release(DATABASE);
	close (DATABASE);

	print "Location: $pageurl/admin/banners.cgi\n\n"; 
	exit;
}

##################
sub deletebanner {
##################

	check_access("editbanner"); if ($access_granted ne "1") { error("$err{'011'}"); }

	open (ORGDB,"<$datadir/banners/data.txt");
	hold(ORGDB);
	@ODB=<ORGDB>;
	release(ORGDB);
	close (ORGDB);

	open (DATABASE,">$datadir/banners/data.txt");
	hold(DATABASE);
	foreach $rec (@ODB){
		chomp($rec);
		($banurl,$iban,$iw,$ih,$alt,$hits)=split(/\|/,$rec);

# 5 substitution lines were here... (were input, changed to info)
		$info{'banurl'} =~ s/EQSIGN/\=/g;
		$info{'banurl'} =~ s/QMSIGN/\?/g;
		$info{'banurl'} =~ s/DQUOTE/\"/g;
		$info{'banurl'} =~ s/SQUOTE/\'/g;
		$info{'banurl'} =~ s/AMPSIGN/\&/g;

		if ($banurl eq $info{'banurl'} && $iban eq $info{'iban'}){
			print DATABASE "";
		} else {
			print DATABASE "$banurl|$iban|$iw|$ih|$alt|$hits\n";
		}
	}
	release(DATABASE);
	close (DATABASE);
#	}
	print "Location: $pageurl/admin/banners.cgi\n\n"; 
	exit;
}

1;
