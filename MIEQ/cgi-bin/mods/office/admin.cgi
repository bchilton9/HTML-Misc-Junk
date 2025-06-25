#!/usr/bin/perl 
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

###############################################################################
###############################################################################
# Office Mod v0.9.6 for WebAPP - Automated Perl Portal                        #
# Copyright (C) 2002 by Brad (webmaster@indie-central.ca)					  #
# Based on selections of code by Carter (carter@mcarterbrown.com)             #
#-----------------------------------------------------------------------------#
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
# File: Last modified: 14 July 2002											  #
###############################################################################
###############################################################################

# Office Mod created by Brad (webmaster@indie-central.ca)
# calendar.cgi, contacts.cgi and tasks.cgi based on code by Jason M. Hinkle (GNU)
# index.cgi and journal.cgi based on code from WebAPP v0.9.6 by Carter

# if you modify any of this code, I would appreciate it if you can let me 
# know, so I can see how it's being used and improved -- Brad


### the following must be correct or else this script won't work ###
require "../../config.pl"; # main prog config
######

# do not modify anything below this line unless you know what you are doing!

$officeURL = "$scripturl/mods/office";
$imgURL = "$imagesurl/office";
$officeDIR = "$scriptdir/mods/office";
$dbdir = "$officeDIR/db";
$office_cfg = "$dbdir/office.cfg";

push(@INC,$scriptdir);
use vsLock;
use vsDB;
use CGI;

$scriptname = "WebOFFICE for WebAPP";
$scriptver = "0.9.6";

eval {
	require "$sourcedir/subs.pl"; # main prog subs
	require "$dbdir/office.pl"; # some office subs
	require "$officeDIR/config.dat"; # dat file for mod manager

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
	<p>If this problem persits, please contact the webmaster and inform them about the date and time that you recieved this error.</p>
~;
	exit;
}

getlanguage();
ban();
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if ($lang_support eq "1") { mod_langsupp(); } 

if ($username ne "admin") { error("$office_error{'001'}"); }

if ($action eq "admin_cfg") { admin_cfg(); }
elsif ($action eq "regenerate") { regenerate(); }
else {

# grab the office colours

my ($objConfig) = new vsDB(
	file => $office_cfg,
	delimiter => "\t",
);

$objConfig->Open;
my ($headerColor) = $objConfig->FieldValue("HeaderColor");
my ($dataDarkColor) = $objConfig->FieldValue("DataDarkColor");
my ($dataLightColor) = $objConfig->FieldValue("DataLightColor");
my ($dataDayColor) = $objConfig->FieldValue("DataDayColor");
my ($dataHighlightColor) = $objConfig->FieldValue("DataHighlightColor");
$objConfig->Close;
undef($objConfig);

$navbar = "$office_gen{'023'} $office_gen{'012'}";
print_top();

print qq~
<table cellspacing="0" cellpadding="2" border="0" width="100%">
<tr>
    <td colspan="2">~;
	top_navbar_admin($headerColor);
	print qq~
	</td>
</tr>
<tr>
    <td colspan="2" align="center" valign="top">~;
	Admin_msg($dataDarkColor,$dataLightColor);
	print qq~
	</td>
</tr>
<tr>
    <td colspan="2" align="center" valign="top"><P>~;
	Options($dataDarkColor,$dataLightColor);
	print qq~
	</td>
</tr>
<tr>
    <td colspan="2" align="center" valign="top">~;
	User_stuff($dataDarkColor,$dataLightColor);
	print qq~
	</td>
</tr>
<tr>
    <td colspan="2">~;
	bottom_nav();
	print qq~
	</td>
</tr>
</table>
~;

print_bottom();

} # end if


##############
sub User_stuff {
##############

my $dataDarkColor = shift;
my $dataLightColor = shift;

# <form method="post" action="$officeURL/admin.cgi?action=regenerate">

print qq~
<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
<tr>
<td bgcolor="$dataDarkColor" align="left"><b>$office_gen{'002'} $office_gen{'035'}</b></td>
</tr>
<tr><td bgcolor="$dataDarkColor">
	<table width="100%" cellpadding="2" cellspacing="1">
	<tr>
	<td bgcolor="$dataLightColor">
	<!-- who's using WebOFFICE? -->
		<table cellspacing="1" cellpadding="2" border="0" width="100%">
		<tr>
	    <td><b>$office_gen{'034'}</b></td>
		</tr><tr><td valign="middle">~;
		
		open(FILE, "$dbdir/office.users"); 
			file_lock(FILE); 
			chomp(@users = <FILE>); 
			unfile_lock(FILE); 
		close(FILE); 
 
	 	for ($a = 0; $a < @users; $a++) {
			($user) = split(/\n/, $users[$a]);
			print "<input type=\"checkbox\" name=\"\" value=\"$users[$a]\">$users[$a] ";
		}
		
		print qq~
		</td></tr>
		<tr><td></td>
		</tr></table>
	</td></tr></table>
</td></tr></table>
~;
# </form><INPUT TYPE="SUBMIT" VALUE="Regenerate" class="button">


}

##############
sub Admin_msg {
##############

my $dataDarkColor = shift;
my $dataLightColor = shift;

$admin_notes = "$dbdir/office.msg";

# grab the display config
open(CFG, "$office_cfg"); 
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

for ($b = 1; $b < @config; $b++) {
	($dummy[b], $dummy[b], $dummy[b], $dummy[b], $dummy[b], $dummy[b], $showit[b]) = split(/\t/, $config[$b]);
}

if ($showit[b] eq "on") {

if (-e("$admin_notes")) {
	print qq~
	<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
	<tr>
	<td bgcolor="$dataDarkColor" align="left">
	<IMG alt="$office_gen{'011'}" src="$imgURL/notes_small.gif" border="0" align="absmiddle">&nbsp;<b>$office_gen{'011'}</b></td>
	</tr>
	<tr><td bgcolor="$dataDarkColor">
	<table width="100%" cellpadding="2" cellspacing="1">
	<tr>
	<td bgcolor="$dataLightColor" class="newstextsmall">~;
	open(NOTES, "<$admin_notes"); 
		file_lock(NOTES);
		while(<NOTES>) {
			$line = $_;
		  	chop($line);
			print "$line\n";
		   }
		unfile_lock(NOTES);
	close(NOTES);
	print qq~</td>
	</tr>
	</table></td>
	</tr>
	</table>
	~;
}

}

}

##############
sub Options {
##############

# each user has a few viewing options available to them

my $dataDarkColor = shift;
my $dataLightColor = shift;

if ($username eq "admin") {

open(CFG, "$dbdir/office.cfg"); 
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

#if ($config[0] eq "on") { $detailed_contacts_checked = "checked"; }
#else { $detailed_contacts_checked = "unchecked"; }

print qq~
<form method="post" action="$officeURL/admin.cgi?action=admin_cfg">
<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
<tr>
<td bgcolor="$dataDarkColor" align="left"><b>$office_gen{'002'} $office_gen{'030'}</b></td>
</tr>
<tr><td bgcolor="$dataDarkColor">
	<table width="100%" cellpadding="2" cellspacing="1">
	<tr>
	<td bgcolor="$dataLightColor">
	<!-- general options -->
		<table cellspacing="1" cellpadding="2" border="0" width="100%">
		<tr>
	    <td colspan="4"><b>$office_gen{'022'} $office_gen{'019'}</b></td>
		</tr>~;
		for ($a = 0; $a < (@config-1); $a++) {
			($HeaderColor[$a], $DataDarkColor[$a], $DataLightColor[$a], $DataHighlightColor[$a], $dummy, $dummy) = split(/\t/, $config[$a]);
			print qq~
			<tr>
				<td align="left">$office_gen{'015'}<input type="hidden" name="HeaderColorText" value="$HeaderColor[$a]"></td>
			    <td align="left">$office_gen{'016'}<input type="hidden" name="DataDarkColorText" value="$DataDarkColor[$a]"></td>
			    <td align="left">$office_gen{'017'}<input type="hidden" name="DataLightColorText" value="$DataLightColor[$a]"></td>
			    <td align="left">$office_gen{'018'}<input type="hidden" name="DataHighlightColorText" value="$DataHighlightColor[$a]"></td>
			</tr>~;
		}
		for ($b = 1; $b < @config; $b++) {
			($HeaderColor[$b], $DataDarkColor[$b], $DataLightColor[$b], $DataHighlightColor[$b], $dummy, $dummy) = split(/\t/, $config[$b]);
			print qq~
			<tr>
			    <td align="left" bgcolor="$HeaderColor[$b]"><input type="text" size="10" name="HeaderColor" value="$HeaderColor[$b]"></td>
			    <td align="left" bgcolor="$DataDarkColor[$b]"><input type="text" size="10" name="DataDarkColor" value="$DataDarkColor[$b]"></td>
			    <td align="left" bgcolor="$DataLightColor[$b]"><input type="text" size="10" name="DataLightColor" value="$DataLightColor[$b]"></td>
			    <td align="left" bgcolor="$DataHighlightColor[$b]"><input type="text" size="10" name="DataHighlightColor" value="$DataHighlightColor[$b]"></td>
			</tr>~;
		}
		print qq~
		<tr>
	    <td colspan="4"><P><b>$office_cal{'001'} $office_gen{'019'}</b></td>
		</tr>~;
		for ($a = 0; $a < (@config-1); $a++) {
			($dummy, $dummy, $dummy, $dummy, $CalendarRequests[$a], $CalendarCC[$a], $dummy) = split(/\t/, $config[$a]);
			print qq~
			<tr>
				<td align="left" colspan="2">$office_cal{'043'}<input type="hidden" name="CalendarRequests" value="$CalendarRequests[$a]"></td>
			    <td align="left" colspan="2">$office_cal{'044'}<input type="hidden" name="CalendarCC" value="$CalendarCC[$a]"></td>
			</tr>~;
		}
		for ($b = 1; $b < @config; $b++) {
			($dummy, $dummy, $dummy, $dummy, $CalendarRequests[$b], $CalendarCC[$b], $dummy) = split(/\t/, $config[$b]);
			if ($CalendarCC[$b] eq "on") { $cc_admin_checked = "checked"; }
			else { $cc_admin_checked = "unchecked"; }
			print qq~
			<tr>
			    <td align="left" colspan="2"><input type="text" size="15" name="CalendarAssingned" value="$CalendarRequests[$b]"></td>
			    <td align="left" colspan="2"><input type="checkbox" name="CalendarCCyn" $cc_admin_checked></td>
			</tr>~;
		}
		print qq~
		<tr>
	    <td colspan="4"><P><b>$office_gen{'011'}</b></td>
		</tr>~;
		for ($a = 0; $a < (@config-1); $a++) {
			($dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $showthemsg[$a]) = split(/\t/, $config[$a]);
			print qq~
			<tr>
				<td align="left" colspan="4">$office_gen{'033'}<input type="hidden" name="showadminmsg" value="$showthemsg[$a]"></td>
			</tr>~;
		}
		for ($b = 1; $b < @config; $b++) {
			($dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $showthemsg[$b]) = split(/\t/, $config[$b]);
			if ($showthemsg[$b] eq "on") { $showadminmsg_checked = "checked"; }
			else { $showadminmsg_checked = "unchecked"; }
			print qq~
			<tr>
			    <td align="left" colspan="4"><input type="checkbox" name="showadminmsgyn" $showadminmsg_checked></td>
			</tr>~;
		}
		print qq~
		<tr><td colspan="4">
		<TEXTAREA NAME="notepad" COLS="50" ROWS="10" MAXLENGTH="250" wrap="virtual">~;
		if (-e("$admin_notes")) {
			open(NOTES, "<$admin_notes"); 
				file_lock(NOTES);
				while(<NOTES>) {
					$line = $_;
				  	chop($line);
					print "$line\n";
			    }
				unfile_lock(NOTES);
			close(NOTES);
		}	
		print qq~</TEXTAREA></td></tr>
		<tr><td colspan="4"><INPUT TYPE="SUBMIT" VALUE="$office_gen{'029'} $office_gen{'030'}" class="button"></td>
		</tr></table>
	</td></tr></table>
</td></tr></table>
</form>
~;

} # end admin check


} # end sub





################# 
sub admin_cfg { 
################# 

$admin_notes = "$dbdir/office.msg";

if ($username eq $admin) { error("$office_error{'001'}"); }

if (-e("$memberdir/$input{'CalendarAssingned'}.dat") || ($input{'CalendarAssingned'} eq "")) {

	unlink("$office_cfg");

	open(CFG, ">$office_cfg") || die("$office_error{'002'} $office_cfg"); 
		file_lock(CFG); 
		print CFG "HeaderColor\t";
		print CFG "DataDarkColor\t";
		print CFG "DataLightColor\t";
		print CFG "DataHighlightColor\t";
		print CFG "CalendarRequests\t";
		print CFG "CalendarCC\t";
		print CFG "showadminmsg\n";
		print CFG "$input{'HeaderColor'}\t";
		print CFG "$input{'DataDarkColor'}\t";
		print CFG "$input{'DataLightColor'}\t";
		print CFG "$input{'DataHighlightColor'}\t";
		print CFG "$input{'CalendarAssingned'}\t";
		print CFG "$input{'CalendarCCyn'}\t";
		print CFG "$input{'showadminmsgyn'}\n";
		unfile_lock(CFG); 
		chmod(CFG,0644);	
	close(CFG); 
}
else {
		error("$office_cal{'045'}");
}

if ($input{'notepad'} ne "") {
	$note = htmltotext($input{'notepad'});
	open(NOTES, ">$admin_notes") || error("$office_error{'002'} $admin_notes"); 
		file_lock(NOTES);
		print NOTES "$note";
		unfile_lock(NOTES);
	close(NOTES);
}
else {
	if (-e("$admin_notes")) {
		unlink("$admin_notes");
	}
}

print "Location: $officeURL/admin.cgi\n\n"; 
exit; 

}

1; # return true