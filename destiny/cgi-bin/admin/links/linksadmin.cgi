#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# linksadmin.cgi for admin/links                                              #
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
#                                                                             #
# File: Last modified: 01/30/03 by Floyd                                      #
###############################################################################
###############################################################################

$| = 1;
use CGI::Carp qw(fatalsToBrowser);

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

if ($action eq "addlncat") { addlncat(); }
elsif ($action eq "addlncat2") { addlncat2(); }
elsif ($action eq "editlncat") { editlncat(); }
elsif ($action eq "editlncat2") { editlncat2(); }
elsif ($action eq "deletelncat") { deletelncat(); }
elsif ($action eq "deletelncat2") { deletelncat2(); }
else { viewlist(); }

###############
sub viewlist {
###############
check_access(editlink); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$linksdir/linkcats.dat");
file_lock(DATABASE);
@linksdatabase=<DATABASE>;
unfile_lock(DATABASE);
close (DATABASE);

$navbar = "$btn{'014'} $mnu{'007'} $btn{'014'} $nav{'130'}";
print_top();

print qq~<font face='Arial' size='2'>
<i>$msg{'366'}</i><br>
<table width='100%' border='1'>
<tr><td bgcolor='#F2C973'><font size='2'>$msg{'354'}</font></td><td bgcolor='#F2C973'><font size='2'>$msg{'359'}</font></td><td bgcolor='#F2C973'><font size='2'>$msg{'356'}</font></td><td bgcolor='#F2C973'><font size='2'>$msg{'357'}</font></td></tr>~;

foreach $lnkrec (@linksdatabase){
	chomp($lnkrec);
	($link,$file,$desc)=split(/\|/,$lnkrec);
	print qq~<tr><td><font size="2"><a href="$pageurl/admin/links/linksadmin.cgi?action=editlncat&amp;file=$file">$nav{'096'}</a> - <a href="$pageurl/admin/links/linksadmin.cgi?action=deletelncat&amp;file=$file">$nav{'097'}</a></font></td><td><font size="2">$link</font></td><td><font size="2">$file</font></td><td><font size="2">$desc</font></td></tr>~;
}

print qq~</table><p><a href="$pageurl/admin/links/linksadmin.cgi?action=addlncat">$nav{'128'}</a></p></font>~;

print_bottom();
exit;
}

#################
sub addlncat {
#################
check_access(editlink); if ($access_granted ne "1") { error("$err{'011'}"); }

$navbar = "$btn{'014'} $mnu{'007'} $btn{'014'} $nav{'128'}";
print_top();

print qq~<font face='Arial'>
<i>$nav{'128'}</i><br>
<form onSubmit="submitonce(this)" onSubmit="submitonce(this)" action='$pageurl/admin/links/linksadmin.cgi?action=addlncat2' method='post'>
<table border='1'>
<tr><td><font size='2'>$msg{'359'}</font></td><td><input type='text' name='ncatname'></td></tr>
<tr><td><font size='2'>$msg{'356'}</font></td><td><input type='text' name='ncatfile'></td></tr>
<tr><td><font size='2'>$msg{'357'}</font></td><td><input type='text' name='ncatdesc'></td></tr>
</table>
<input type='submit' value='$btn{'035'}'>
</form>
</font>
</font>~;

print_bottom();
exit;
}

#################
sub addlncat2 {
#################
check_access(editlink); if ($access_granted ne "1") { error("$err{'011'}"); }
if ($input{'ncatfile'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<+|\%)/) { error("$err{'006'}") }
if ($input{'ncatname'} eq "") {error("$err{'034'}");}
if ($input{'ncatfile'} eq "") {error("$err{'035'}");}
if ($input{'ncatdesc'} eq "") {error("$err{'036'}");}

$ncatfile = $input{'ncatfile'};
$ncatfile =~ s/^\s+//;
$ncatfile =~ s/\s+$//;
$ncatfile =~ tr/ /_/;
$ncatfile = lc($ncatfile);

open (DATABASE,"$linksdir/linkcats.dat");
file_lock(DATABASE);
chomp(@checklinkssdatabase=<DATABASE>);
unfile_lock(DATABASE);
close (DATABASE);

				foreach $findlnkrec (@checklinksdatabase){
				@lncatitem = split(/\|/, $findlnkrec);
				if ($ncatfile eq $lncatitem[1]) { error("$err{'037'}"); }
				}

open (DATABASE,"$linksdir/linkcats.dat");
file_lock(DATABASE);
@linksdatabase=<DATABASE>;
unfile_lock(DATABASE);
close (DATABASE);

				open (LINKS,"$linksdir/linkcats.dat");
				file_lock(LINKS);
				chomp(@checklinksdatabase = <LINKS>);
				unfile_lock(LINKS);
				close (LINKS);
				
				foreach $checklnkrec (@checklinksdatabase){
				@lncatitem = split(/\|/, $checklnkrec);
				if ($input{'ncatfile'} eq $lncatitem[1]) { error("$err{'037'}");}
				}

open (NEWDATABASE,">$linksdir/linkcats.dat");
file_lock(NEWDATABASE);
print NEWDATABASE "$input{'ncatname'}|$input{'ncatfile'}|$input{'ncatdesc'}\n"; 
print NEWDATABASE @linksdatabase;
unfile_lock(NEWDATABASE);
close (NEWDATABASE);

print "Location: $pageurl/admin/links/linksadmin.cgi\n\n"; 
exit;

}

#################
sub editlncat {
#################
check_access(editlink); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$linksdir/linkcats.dat");
file_lock(DATABASE);
chomp(@linksdatabase=<DATABASE>);
unfile_lock(DATABASE);
close (DATABASE);

				foreach $findlnkrec (@linksdatabase){
				@lncatitem = split(/\|/, $findlnkrec);
				if ($info{'file'} eq $lncatitem[1]) { $ecatname = $lncatitem[0] ; $ecatfile = $lncatitem[1] ; $ecatdesc = $lncatitem[2]; }
				}

$navbar = "$btn{'014'} $mnu{'007'} $btn{'014'} $nav{'129'} $btn{'014'} $ecatname";
print_top();

print qq~<font face='Arial'>
<i>$nav{'129'}</i><br>
<form onSubmit="submitonce(this)" action="$pageurl/admin/links/linksadmin.cgi?action=editlncat2" method="post">
<table border='1'>
<tr><td><font size='2'>$msg{'359'}</font></td><td><input type='text' name='ncatname' value="$ecatname"></td></tr>
<tr><td><font size='2'>$msg{'356'}</font></td><td><input type='hidden' name='ncatfile' value="$ecatfile">$ecatfile</td></tr>
<tr><td><font size='2'>$msg{'357'}</font></td><td><input type='text' name='ncatdesc' value="$ecatdesc"></td></tr>
</table>
<input type='submit' value='$btn{'036'}'>
</form>
</font>
</font>~;

print_bottom();
exit;
}

#################
sub editlncat2 {
#################
check_access(editlink); if ($access_granted ne "1") { error("$err{'011'}"); }
if ($input{'ncatname'} eq "") {error("$err{'034'}");}
if ($input{'ncatfile'} eq "") {error("$err{'035'}");}
if ($input{'ncatdesc'} eq "") {error("$err{'036'}");}

open (DATABASE,"$linksdir/linkcats.dat");
file_lock(DATABASE);
@linksdatabase=<DATABASE>;
unfile_lock(DATABASE);
close (DATABASE);

open (EDITDATABASE,">$linksdir/linkcats.dat");
file_lock(EDITDATABASE);
		for ($a = 0; $a < @linksdatabase; $a++) {
			($ocatname, $ocatfile, $ocatdesc) = split(/\|/,$linksdatabase[$a]);
			if ($ocatfile eq $input{'ncatfile'}) { print EDITDATABASE "$input{'ncatname'}|$input{'ncatfile'}|$input{'ncatdesc'}\n"; }
			else { print EDITDATABASE "$linksdatabase[$a]"; }
		}
unfile_lock(EDITDATABASE);
close (EDITDATABASE);

print "Location: $pageurl/admin/links/linksadmin.cgi\n\n"; 
exit;
}

#################
sub deletelncat {
#################
check_access(editlink); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$linksdir/linkcats.dat");
file_lock(DATABASE);
chomp(@linksdatabase=<DATABASE>);
unfile_lock(DATABASE);
close (DATABASE);

				foreach $findlnkrec (@linksdatabase){
				@lncatitem = split(/\|/, $findlnkrec);
				if ($info{'file'} eq $lncatitem[1]) { $dcatname = $lncatitem[0]; $dcatfile = $lncatitem[1]; }
				}

	$navbar = "$btn{'014'} $btn{'011'} $dcatname";
	print_top();
	
	print qq~<b>$btn{'011'} $dcatname?</b><br>
	<a href="$pageurl/admin/links/linksadmin.cgi?action=deletelncat2&amp;file=$dcatfile">$nav{'047'}</a> - <a href="$pageurl/admin/links/linksadmin.cgi">$nav{'048'}</a>~;
	
	print_bottom();
	exit;
}

#################
sub deletelncat2 {
#################
check_access(editlink); if ($access_granted ne "1") { error("$err{'011'}"); }

open (DATABASE,"$linksdir/linkcats.dat");
file_lock(DATABASE);
@linksdatabase=<DATABASE>;
unfile_lock(DATABASE);
close (DATABASE);

open (DELETEDATABASE,">$linksdir/linkcats.dat");
file_lock(DELETEDATABASE);
		for ($a = 0; $a < @linksdatabase; $a++) {
			($ocatname, $ocatfile, $ocatdesc) = split(/\|/,$linksdatabase[$a]);
			if ($ocatfile eq $info{'file'}) { print DELETEDATABASE ""; }
			else { print DELETEDATABASE "$linksdatabase[$a]"; }
		}
unfile_lock(DELETEDATABASE);
close (DELETEDATABASE);

unlink("$linksdir/$info{'file'}.dat"); 
unlink("$linksdir/$info{'file'}.cnt");

print "Location: $pageurl/admin/links/linksadmin.cgi\n\n"; 
exit;
}

1;
