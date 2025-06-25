#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# downloadadmin.cgi for admin/downloads                                       #
# v0.9.9 - Requin                                                             #
#                                                                             #
# Freely Distributed: webapp@attbi.com                                        #
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

if ($action eq "adddlcat") { adddlcat(); }
elsif ($action eq "adddlcat2") { adddlcat2(); }
elsif ($action eq "editdlcat") { editdlcat(); }
elsif ($action eq "editdlcat2") { editdlcat2(); }
elsif ($action eq "deletedlcat") { deletedlcat(); }
elsif ($action eq "deletedlcat2") { deletedlcat2(); }
else { viewlist(); }

###############
sub viewlist {
###############
check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$downloadsdir/downloadcats.dat");
hold(DATABASE);
@downloadsdatabase=<DATABASE>;
release(DATABASE);
close (DATABASE);

$navbar = "$btn{'014'} $mnu{'006'} $btn{'014'} $nav{'127'}";
print_top();

print qq~<font face='Arial' size='2'>
<i>$nav{'127'}</i><br>
<table width='100%' border='1'>
<tr>
<td bgcolor='#F2C973'><font size='2'>$msg{'354'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'358'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'573'}</font></td>
<td bgcolor='#F2C973'><font size='2'>$msg{'357'}</font></td>
</tr>
~;

foreach $dldrec (@downloadsdatabase){
	chomp($dldrec);
	($download,$file,$desc)=split(/\|/,$dldrec);
	print qq~<tr>
<td><font size="2"><a href="$pageurl/admin/downloadadmin.cgi?action=editdlcat&amp;file=$file">$nav{'096'}</a> - <a href="$pageurl/admin/downloadadmin.cgi?action=deletedlcat&amp;file=$file">$nav{'097'}</a></font></td>
<td><font size="2">$download</font></td>
<td><font size="2">$file</font></td>
<td><font size="2">$desc</font></td>
</tr>
~;
}

print qq~</table>
<p><a href="$pageurl/admin/downloadadmin.cgi?action=adddlcat">$nav{'125'}</a></p>
</font>~;

print_bottom();
exit;
}

#################
sub adddlcat {
#################
check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }

$navbar = "$btn{'014'} $mnu{'006'} $btn{'014'} $nav{'125'}";
print_top();

print qq~<font face='Arial'>
<i>$nav{'125'}</i><br>
<form action='$pageurl/admin/downloadadmin.cgi?action=adddlcat2' method='post'>
<table border='1'>
<tr>
<td><font size='2'>$msg{'358'} ($msg{'574'})</font></td>
<td><input type='text' name='ncatname'></td>
</tr>
<tr>
<td><font size='2'>$msg{'573'}</font></td>
<td><input type='text' name='ncatfile'></td>
</tr>
<tr>
<td><font size='2'>$msg{'357'}</font></td>
<td><input type='text' name='ncatdesc'></td>
</tr>
</table>
<input type='submit' value='$btn{'035'}'>
</form>
</font>~;

print_bottom();
exit;
}

#################
sub adddlcat2 {
#################
check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
if ($input{'ncatfile'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<+|\%)/) { error("$err{'006'}") }
if ($input{'ncatname'} eq "") {error("$err{'034'}");}
if ($input{'ncatfile'} eq "") {error("$err{'035'}");}
if ($input{'ncatdesc'} eq "") {error("$err{'036'}");}

$ncatfile = $input{'ncatfile'};
$ncatfile =~ s/^\s+//;
$ncatfile =~ s/\s+$//;
$ncatfile =~ tr/ /_/;
$ncatfile = lc($ncatfile);

open (DATABASE,"$downloadsdir/downloadcats.dat");
hold(DATABASE);
chomp(@checkdownloadsdatabase=<DATABASE>);
release(DATABASE);
close (DATABASE);

				foreach $finddldrec (@checkdownloadsdatabase){
				@dlcatitem = split(/\|/, $finddldrec);
				if ($ncatfile eq $dlcatitem[1]) { error("$err{'037'}"); }
				}

open (DATABASE,"$downloadsdir/downloadcats.dat");
hold(DATABASE);
@downloadsdatabase=<DATABASE>;
release(DATABASE);
close (DATABASE);

				open (DOWNLOADS,"$downloadsdir/downloadcats.dat");
				hold(DOWNLOADS);
				chomp(@checkdownloadsdatabase = <DOWNLOADS>);
				release(DOWNLOADS);
				close (DOWNLOADS);
				
				foreach $checkdldrec (@checkdownloadsdatabase){
				@dlcatitem = split(/\|/, $checkdldrec);
				if ($input{'ncatfile'} eq $dlcatitem[1]) { error("$err{'037'}");}
				}

open (NEWDATABASE,">$downloadsdir/downloadcats.dat");
hold(NEWDATABASE);
print NEWDATABASE "$input{'ncatname'}|$ncatfile|$input{'ncatdesc'}\n"; 
print NEWDATABASE @downloadsdatabase;
release(NEWDATABASE);
close (NEWDATABASE);

print "Location: $pageurl/admin/downloadadmin.cgi\n\n"; 
exit;

}

#################
sub editdlcat {
#################
check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$downloadsdir/downloadcats.dat");
hold(DATABASE);
chomp(@downloadsdatabase=<DATABASE>);
release(DATABASE);
close (DATABASE);

				foreach $finddldrec (@downloadsdatabase){
				@dlcatitem = split(/\|/, $finddldrec);
				if ($info{'file'} eq $dlcatitem[1]) { $ecatname = $dlcatitem[0] ; $ecatfile = $dlcatitem[1] ; $ecatdesc = $dlcatitem[2]; }
				}

$navbar = "$btn{'014'} $mnu{'006'} $btn{'014'} $nav{'126'} $btn{'014'} $ecatname";
print_top();

print qq~<font face='Arial'>
<i>$nav{'126'}</i><br>
<form action="$pageurl/admin/downloadadmin.cgi?action=editdlcat2" method="post">
<table border='1'>
<tr>
<td><font size='2'>$msg{'358'}</font></td>
<td><input type='text' name='ncatname' value="$ecatname"></td>
</tr>
<tr>
<td><font size='2'>$msg{'573'}</font></td>
<td><input type='hidden' name='ncatfile' value="$ecatfile">$ecatfile</td>
</tr>
<tr>
<td><font size='2'>$msg{'357'}</font></td>
<td><input type='text' name='ncatdesc' value="$ecatdesc"></td>
</tr>
</table>
<input type='submit' value='$btn{'036'}'>
</form>
</font>~;

print_bottom();
exit;
}

#################
sub editdlcat2 {
#################
check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
if ($input{'ncatname'} eq "") {error("$err{'034'}");}
if ($input{'ncatfile'} eq "") {error("$err{'035'}");}
if ($input{'ncatdesc'} eq "") {error("$err{'036'}");}

open (DATABASE,"$downloadsdir/downloadcats.dat");
hold(DATABASE);
@downloadsdatabase=<DATABASE>;
release(DATABASE);
close (DATABASE);

open (EDITDATABASE,">$downloadsdir/downloadcats.dat");
hold(EDITDATABASE);
		for ($a = 0; $a < @downloadsdatabase; $a++) {
			($ocatname, $ocatfile, $ocatdesc) = split(/\|/,$downloadsdatabase[$a]);
			if ($ocatfile eq $input{'ncatfile'}) { print EDITDATABASE "$input{'ncatname'}|$input{'ncatfile'}|$input{'ncatdesc'}\n"; }
			else { print EDITDATABASE "$downloadsdatabase[$a]"; }
		}
release(EDITDATABASE);
close (EDITDATABASE);

print "Location: $pageurl/admin/downloadadmin.cgi\n\n"; 
exit;
}

#################
sub deletedlcat {
#################
check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$downloadsdir/downloadcats.dat");
hold(DATABASE);
chomp(@downloadsdatabase=<DATABASE>);
release(DATABASE);
close (DATABASE);

				foreach $finddldrec (@downloadsdatabase){
				@dlcatitem = split(/\|/, $finddldrec);
				if ($info{'file'} eq $dlcatitem[1]) { $dcatname = $dlcatitem[0]; $dcatfile = $dlcatitem[1]; }
				}

	$navbar = "$btn{'014'} $btn{'011'} $dcatname";
	print_top();
	
	print qq~<b>$btn{'011'} $dcatname?</b><br>
	<a href="$pageurl/admin/downloadadmin.cgi?action=deletedlcat2&amp;file=$dcatfile">$nav{'047'}</a> - <a href="$pageurl/admin/downloadadmin.cgi">$nav{'048'}</a>~;
	
	print_bottom();
	exit;
}

#################
sub deletedlcat2 {
#################
check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$downloadsdir/downloadcats.dat");
hold(DATABASE);
@downloadsdatabase=<DATABASE>;
release(DATABASE);
close (DATABASE);

open (DELETEDATABASE,">$downloadsdir/downloadcats.dat");
hold(DELETEDATABASE);
		for ($a = 0; $a < @downloadsdatabase; $a++) {
			($ocatname, $ocatfile, $ocatdesc) = split(/\|/,$downloadsdatabase[$a]);
			if ($ocatfile eq $info{'file'}) { print DELETEDATABASE ""; }
			else { print DELETEDATABASE "$downloadsdatabase[$a]"; }
		}
release(DELETEDATABASE);
close (DELETEDATABASE);

unlink("$downloadsdir/$info{'file'}.dat"); 
unlink("$downloadsdir/$info{'file'}.cnt");

print "Location: $pageurl/admin/downloadadmin.cgi\n\n"; 
exit;
}

1;
