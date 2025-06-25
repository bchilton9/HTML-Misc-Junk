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

if ($username eq $anonuser) { error("$office_error{'001'}"); }

# point to all the source files
$user_dir = "$dbdir/$username";
$index_template = "$dbdir/index.html"; # redirector if someone tries to view db files

# do a quick check to see if the member has used their office before
# if not, then create the necessary subdirectory and config/db files
# use redundant checking for each file, just in case a particular file was deleted

# step one: user directory for db files
unless (-e("$user_dir")) {
	mkdir("$user_dir",0777);
	chmod(0777,"$user_dir");
}

# step two: index file to hide db from browser
unless (-e("$user_dir/index.html")) { 	
	open (FILE, "<$index_template") || error("$office_error{'002'} $index_template"); 
		file_lock(FILE);
		@ind = <FILE>;
		unfile_lock(FILE);
	close (FILE);

	open(FILE, ">$user_dir/index.html") || error("$office_error{'003'} $user_dir/index.html"); 
		file_lock(FILE);
		print FILE @ind;
		unfile_lock(FILE);
	close(FILE);
}

# step three: check to see if this user appears in the office user list

$listed = 0;
open (USERS,"$dbdir/office.users");
	file_lock(USERS);
	while(<USERS>) {
		chop;
		@allnames = split(/\n/);
		if (grep (/\b^$username\b/i, @allnames) ne "0" ) { 
			$listed = 1;
		}
	}
	unfile_lock(USERS);
close(USERS);
				
if ($listed == 0) {
	open(FILE, "$dbdir/office.users"); 
		file_lock(FILE); 
		@users = <FILE>; 
		unfile_lock(FILE); 
	close(FILE); 
	
	open(FILE, ">$dbdir/office.users"); 
		file_lock(FILE); 
		foreach $curuser(@users) { print FILE "$curuser"; } 
		print FILE "$username\n"; 
		unfile_lock(FILE); 
	close(FILE); 
}



# done db file check

if ($action eq "write_cfg") { write_cfg(); }
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

$navbar = "$office_gen{'023'} $username\'s Journal";
print_top();

# print out the main table - holds everything
# if nothing else, this mod is a test to see how many tables it takes to 
# break a browser display! ;-)

print qq~
Journal Actavated!
<P>
<A HREF=http://www.eqguilded.com/freefire/cgi-bin/mods/office/journal.cgi>Click here to start!</A>
~;

print_bottom();

} # end if

##############
sub Calendar {
##############

my $dataDarkColor = shift;
my $dataLightColor = shift;
my $dataHighlightColor = shift;

$this_cgi = "calendar.cgi";
$calendar_table = "$user_dir/$username.calendar";
$calendar_template = "$dbdir/calendar.tab";

unless (-e("$calendar_table")) { 
	open (FILE, "<$calendar_template") || error("$office_error{'002'} $calendar_template"); 
		file_lock(FILE);
		@tab = <FILE>;
		unfile_lock(FILE);
	close (FILE);

	open(FILE, ">$calendar_table") || error("$office_error{'003'} $calendar_table"); 
		file_lock(FILE);
		foreach $line (@tab) { print FILE "$line"; }
		unfile_lock(FILE);
	close(FILE);
}

my ($objCGI) = new CGI;
my @dateArray = localtime(time);
my ($month) = $objCGI->param('vsMonth') || $dateArray[4]+1;
my ($year) = $objCGI->param('vsYear') || $dateArray[5]+1900;
my ($day) = $objCGI->param('vsDay') || $dateArray[3];
my ($showDefault) = 0;
my ($showDayDetails) = 1;
#my ($noShowDayDetails) = 1;

my ($objDB) = new vsDB(
	file => $calendar_table,
	delimiter => "\t",
);

# lock the datafile 
my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
$objLock->lock($calendar_table) || die("$office_error{'004'} $calendar_table"); 

if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($calendar_table);die;};

&PrintMonth($month,$year,$objDB,$highlightDate,$dataDarkColor,$dataLightColor,$dataHighlightColor);

# unlock the datafile
$objLock->unlock($calendar_table);

undef($objDB);
undef($objLock);
undef($objCGI);

}

############################
sub PrintMonth {
############################

my $month = shift || 1;
my $year = shift || 2001;
my $objMyDb = shift || return 0;

# highlightDate is passed in below...
    
my ($firstDay,$numDays,$numWeeks) = &GetMonthInfo($month,$year);

my @days = ($office_cal{'022'},$office_cal{'023'},$office_cal{'024'},$office_cal{'025'},$office_cal{'026'},$office_cal{'027'},$office_cal{'028'});

my @months = ($office_cal{'008'},$office_cal{'009'},$office_cal{'010'},$office_cal{'011'},$office_cal{'012'},$office_cal{'013'},$office_cal{'014'},$office_cal{'015'},$office_cal{'016'},$office_cal{'017'},$office_cal{'018'},$office_cal{'019'});

my $temp;
my $dayCount = 0;
my $weekDayCount = 0;
my $thisDate;
    
my @dateArray = localtime(time);
$dateArray[5]+=1900;
$dateArray[4]+=1;
my $today = $dateArray[5] . "." . $dateArray[4] . "." . $dateArray[3];

my $highlightDate = shift || $today;

# pass along the remaining variables
my $dataDarkColor = shift;
my $dataLightColor = shift;
my $dataHighlightColor = shift;

print "<BR>\n";
print "<center><font size=\"+2\"><b>$months[$month-1] $year</b></font></center><P>\n";

print "<center><table border='1' cellspacing='0' cellpadding='2' width='329' align='center'>\n";
$cellheight = "47";
$cellwidth = "47";
	
# print the days of the week 
print "<tr>\n";
foreach $temp (@days) {
	print "<td bgcolor='$dataDarkColor'><b>$temp</b></td>";
}
print "</tr>\n";

for (my $cellCount = 1;$cellCount <= $numWeeks; $cellCount++) {
	print "<tr valign='top'>\n";
	foreach $temp (@days) {
	    if (($dayCount > $firstDay-1) && ($weekDayCount < $numDays)) {
		$weekDayCount++;

		$thisDate = $year . "." . $month . "." . $weekDayCount;

		if ($thisDate eq $highlightDate) {
		    print "<td width='$cellwidth' height='$cellheight' bgcolor='$dataHighlightColor'>";
		} else {
		    print "<td width='$cellwidth' height='$cellheight' bgcolor='white'>";
		}
		
		if ($thisDate eq $today) {
		    $tick = "*";
		} else {
		    $tick = "";
		}		    

		$objMyDb->RemoveFilter;	
		$objMyDb->Filter("DATE","eq",$thisDate);

		if ($objMyDb->EOF) {
		    print "<a href='$this_cgi?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'>$weekDayCount</a> $tick<br>";
		} else {
		    print "<a href='$this_cgi?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'><u>$weekDayCount</u></a> $tick<br>";
		}			

#		if ($showDayDetails) {
		    print "<font size='1'>";
		    while (!$objMyDb->EOF) {
			$chopit = substr($objMyDb->FieldValue("EVENT"),0,8); # bm mod
			print "<a href='$this_cgi?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount&vsID=" . $objMyDb->FieldValue("ID") . "'>" . $chopit . "</a><br>";
			$objMyDb->MoveNext;
		    }
		    print "</font>";
#		}
		
		print "</td>\n";
	    } else {
		print "<td bgcolor='$dataLightColor'>&nbsp;</td>\n";
	    }
	    
	    $dayCount++;
	}    
	print "</tr>\n";
    }    
    print "</table></center><BR><BR>\n";
}

############################
sub GetMonthInfo {
############################

    my $month = shift || 1;
    my $year = shift || 2001;

    my($firstDow,$numDays);

    require Time::Local;

    # convert user input into approp format for proc4essing
    --$month;
    $year -= 1900;

    # figure out following month & year    
    my $nmonth = $month + 1;
    my $nyear  = $year;
    if ($nmonth > 11) {
	$nmonth = 0;
	$nyear++;
    }

    # ready to grab first day of the month (0 based array)
    $firstDow  = (localtime(Time::Local::timelocal(0,0,0,1,$month,$year)))[6];
    # numDays is one day prior to 1st of month after
    $numDays = (localtime(Time::Local::timelocal(0,0,0,1,$nmonth,$nyear) - 60*60*24))[3];

    # figure out the number of weeks the month spans across
    my $numWeeks = ($numDays + $firstDow) / 7;
    $numWeeks = int($numWeeks) + 1 unless ($numWeeks == int($numWeeks));

    return ($firstDow,$numDays, $numWeeks);
}

##############
sub Journal {
##############

$this_cgi = "journal.cgi";
$journal_dir = "$user_dir/journal";

# check to see if the directory exists
unless (-e("$journal_dir")) {
	mkdir("$journal_dir",0777);
	chmod(0777,"$journal_dir");
}

# grab the journal index
open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
close(FILE);

# grab the display config
open(CFG, "$user_dir/$username.cfg"); 
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

if (@entries == 0) {
	print qq~<font size="1">$office_journal{'006'}</font>~;
}

else {
	sort {$b[5] <=> $a[5]} @entries;
	
	if ($config[3] eq "") {
		$loop = 5;
	}
	else {
		$loop = $config[3];
	}
	
	if (!($loop <= @entries)) { $loop = @entries; }
	
	print "<table width=\"100%\" cellpadding=\"1\" cellspacing=\"0\">\n";
	
	for ($a = 0; $a < $loop; $a++) {
		($jsub[$a], $jldate[$a], $jsdate[$a], $jmessageid[$a], $jfilenum[$a]) = split(/\|/, $entries[$a]);	
	
		if ($jmessageid[$a] < 100) { 
			$jmessageid[$a] = $a; 
		}
	
		$title = "$jsub[$a]";
	
		if (length($title) > 30) { 
			$title = substr($title,0,26); 
			$title .= "...";
		}
			
		if ($title eq "") {
			$title="No Title"; 
		}
		
		print qq~
		<tr>
		<td><font size="1">$jsdate[$a]:&nbsp;<font size="1"><a href="$this_cgi?action=view&amp;id=$jmessageid[$a]">$title</a></font></td>
		</tr>~;	
	}
	
	print "</table>\n";

}

} # end sub

##############
sub Tasks {
##############

$this_cgi = "tasks.cgi";
$tasks_table = "$user_dir/$username.tasks";
$tasks_template = "$dbdir/tasks.tab";

unless (-e("$tasks_table")) { 
	open (FILE, "<$tasks_template") || error("$office_error{'002'} $tasks_template"); 
		file_lock(FILE);
		@tab = <FILE>;
		unfile_lock(FILE);
	close (FILE);

	open(FILE, ">$tasks_table") || error("$office_error{'003'} $tasks_table"); 
		file_lock(FILE);
		foreach $line (@tab) { print FILE "$line"; }
		unfile_lock(FILE);
	close(FILE);
}

my ($objDB) = new vsDB(
	file => $tasks_table,
	delimiter => "\t",
);

#my ($objMyDB) = shift;
my ($fieldName, $fieldValue);
my ($count) = 0;

# these shouldn't be changed, there's not a lot of space to show more than two fields
my (@showFields) = ("Description","DueDate");

# lock the datafile 
my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
$objLock->lock($tasks_table) || die("$office_error{'004'} $tasks_table"); 

if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($tasks_table);die;};

$objDB->Sort($sortField) if ($sortField ne "");	
$objDB->Filter("Complete","ne","Yes") unless ($showCompleted);

# start printing out the tasks
print qq~
<table width="100%" cellpadding="2" cellspacing="0" border="0">
~;

# the following code prints out the column descriptions
# you can remove the # if you want to display them

# print "<tr>"; 
#foreach $fieldName (@showFields) {
	# check for fields, display name based on lang file
#	if ($fieldName eq "Complete") { $showfield = "$office_task{'006'}"; }
#	elsif ($fieldName eq "Description") { $showfield = "$office_task{'007'}"; }
#	elsif ($fieldName eq "DueDate") { $showfield = "$office_task{'008'}"; }
#	elsif ($fieldName eq "AssignedTo") { $showfield = "$office_task{'009'}"; }
#	elsif ($fieldName eq "Notes") { $showfield = "$office_task{'010'}"; }
#	else { $showfield = "" };
#	print "<td><font size=\"1\">$showfield:</font></td>"; 
#}
# print "</tr>";

$empty = "1";
while (!$objDB->EOF) {
	print "<tr><td valign=\"middle\"><img src=\"$imgURL/task.gif\" border=\"0\" align=\"absmiddle\"></td>";
	foreach $fieldName (@showFields) {
		$fieldValue = $objDB->FieldValue($fieldName);
		$fieldValue = "&nbsp;" if ($fieldValue eq "");
		if (length($fieldValue) > 20) { 
			$fieldValue = substr($fieldValue,0,20); 
			$fieldValue .= "...";
		}
		print "<td valign=\"middle\"><font size=\"1\"><a href='" . $this_cgi . "?vsCOM=EDIT&vsID=" . $objDB->FieldValue("ID") . "'>$fieldValue</a></font></td>";
		$empty = "0";
	}
	print "</tr><tr>";
	$objDB->MoveNext;
	$count++;
}	

if ($empty == "1") { 
	print "<tr><td><font size=\"1\">$office_task{'011'}</font></td></tr>";
}

print "</table>";

$objLock->unlock($tasks_table);


undef($objDB);
undef($objLock);
undef($objCGI);


}

##############
sub Contacts {
##############

$this_cgi = "contacts.cgi";
$contacts_table = "$user_dir/$username.contacts";
$contacts_template = "$dbdir/contacts.tab";

unless (-e("$contacts_table")) { 
	open (FILE, "<$contacts_template") || error("$office_error{'002'} $contacts_template"); 
		file_lock(FILE);
		@tab = <FILE>;
		unfile_lock(FILE);
	close (FILE);

	open(FILE, ">$contacts_table") || error("$office_error{'003'} $contacts_table"); 
		file_lock(FILE);
		foreach $line (@tab) { print FILE "$line"; }
		unfile_lock(FILE);
	close(FILE);
}

if (-e("$user_dir/contacts.show")) {

	open(FILE, "$user_dir/contacts.show");
		file_lock(FILE);
		@entries = <FILE>;
		unfile_lock(FILE);
	close(FILE);

	sort {$b[5] <=> $a[5]} @entries;
	
	print qq~
	<table width="100%" cellpadding="1" cellspacing="0">
	~;

	for ($a = 0; $a < @entries; $a++) {
		($id[$a], $firstn[$a], $lastn[$a], $addy[$a], $phone[$a]) = split(/\|/, $entries[$a]);	
		if ($addy[$a] eq "") {
			$initials = substr("$firstn[$a]",0,1);
			$whattodo = "$initials. $lastn[$a]";
		}
		else {
			$initials = substr("$firstn[$a]",0,1);
			$whattodo = "<a href=\"mailto:$addy[$a]\">$initials. $lastn[$a]</a>";
		}
		print qq~
		<tr>
			<td>
			<a href="$this_cgi?vsAP=$activePage&vsSORT=$sortField&vsCOM=EDIT&vsID=$id[$a]">
			<img src="$imgURL/contact.gif" alt="$office_con{'029'}" border="0"></a></td>
			<td><font size="1">$whattodo</font></td>
			<td><font size="1">$phone[$a]</font></td>
		</tr>
		~;
	}

	print qq~</table>~;
}

else { # no contacts have been selected
	print "$office_con{'034'}";
}


}


##############
sub Recent_Journal {
##############

my $dataDarkColor = shift;
my $dataLightColor = shift;
$this_cgi = "journal.cgi";

# grab the display config
open(CFG, "$user_dir/$username.cfg"); 
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

if ($config[2] eq "on") {

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
close(FILE);

	# fix 3 Nov 2002
	if (@entries == 0) {
		print qq~
		<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
		<tr>
		<td bgcolor="$dataDarkColor" align="left">
		<IMG alt="$office_journal{'001'}" src="$imgURL/journal_small.gif" border="0" align="absmiddle">
		&nbsp;</td>
		<td bgcolor="$dataDarkColor" align="right">&nbsp;</td>
		</tr>
		<tr><td bgcolor="$dataDarkColor" colspan="2">
		<table width="100%" cellpadding="2" cellspacing="1">
		<tr>
		<td bgcolor="$dataLightColor" class="newstextsmall">
		<font size="1">$office_journal{'006'}</font>
		</td>
		</tr>
		</table>
		</td>
		</tr>
		<tr>
		<td bgcolor="$dataDarkColor" align="right" colspan="2">&nbsp;</td>
		</tr>
		</table>
		~;
	}

	else {
	# end fix

	for ($a = 0; $a < 1; $a++) {
		($jsub[$a], $jldate[$a], $jsdate[$a], $jmessageid[$a], $jfilenum[$a]) = split(/\|/, $entries[$a]);	
	
		$curid = "$jmessageid[$a]";
		$curfile = "$jfilenum[$a]";
		$curfile =~ s/\n//g;
		
		open(ENTRY, "$journal_dir/$curfile.txt") || error("$office_error{'002'} $journal_dir/$curfile.txt"); 
			file_lock(ENTRY);
			chomp($text = <ENTRY>);
			unfile_lock(ENTRY);
		close(ENTRY);
		($message, $moddate) = split(/\|/, $text);
		$tempmessage = substr($message,0,1500);
		$tempmessage .= "...";
		
		$message = $tempmessage;
		if ($enable_ubbc) { doubbc(); }
		if ($enable_smile) { dosmilies(); }
		$tempmessage = $message;
		
		$title = "$jsub[$a]";
		
		if (length($title) > 50) { 
			$title = substr($title,0,47); 
			$title .= "...";
		}
				
		if ($title eq "") {
			$title="$office_journal{'017'}"; 
		}
		
		print qq~
		<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
		<tr>
		<td bgcolor="$dataDarkColor" align="left">
		<IMG alt="$office_journal{'001'}" src="$imgURL/journal_small.gif" border="0" align="absmiddle">
		<a href="$officeURL/journal.cgi?action=view&id=$curid">&nbsp;<b>$title</b></a></td>
		<td bgcolor="$dataDarkColor" align="right">$jsdate[$a]&nbsp;</td>
		</tr>
		<tr><td bgcolor="$dataDarkColor" colspan="2">
		<table width="100%" cellpadding="2" cellspacing="1">
		<tr>
		<td bgcolor="$dataLightColor" class="newstextsmall">~;
		if (@entries == 0) {
			print "<font size=\"1\">$office_journal{'006'}</font>";
		}
		else {
			print "$tempmessage";
		} # end entry check
		print qq~
		</td>
		</tr>
		</table>
		</td>
		</tr>
		<tr>
		<td bgcolor="$dataDarkColor" align="right" colspan="2">
		<a href="$this_cgi?action=print&amp;id=$curid"><img src="$imgURL/print.gif" border="0" alt="$office_gen{'020'}" align="absmiddle"></a>&nbsp;
		<a href="$this_cgi?action=view&amp;id=$curid&amp;op=modify"><img src="$imgURL/modify.gif" alt="$office_journal{'011'}" border="0" align="absmiddle"></a>&nbsp;
		<a href="$this_cgi?action=remove&amp;id=$curid"><img src="$imgURL/delete.gif" alt="$office_journal{'012'}" border="0" align="absmiddle"></a>
		</td>
		</tr>
		</table>
		~;
	
	#	<a href="$this_cgi?action=view&amp;id=$curid&amp;op=email"><img src="$imgURL/email.gif" border="0" alt="$office_journal{'003'}" align="absmiddle"></a>&nbsp;
	
	} # end for

	} # end if
} # end if
} # end sub

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

open(CFG, "$user_dir/$username.cfg"); 
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

if ($config[0] eq "on") { $detailed_contacts_checked = "checked"; }
else { $detailed_contacts_checked = "unchecked"; }

if ($config[2] eq "on") { $recent_entry_checked = "checked"; }
else { $recent_entry_checked = "unchecked"; }

print qq~
<form method="post" action="$officeURL/index.cgi?action=write_cfg">
<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
<tr>
<td bgcolor="$dataDarkColor" align="left"><b>$office_gen{'031'} $office_gen{'019'}</b></td>
</tr>
<tr><td bgcolor="$dataDarkColor">
	<table width="100%" cellpadding="2" cellspacing="1">
	<tr>
	<td bgcolor="$dataLightColor">
	<!-- sections divided up in this table -->
		<table cellspacing="0" cellpadding="6" border="0">
		<tr>
		<td valign="top" align="left">
			<table cellpadding="2" cellspacing="0">
			<tr><td colspan="2"><font size="2"><B>$office_con{'001'}</b></font></td></tr>
			<tr>
				<td valign="middle" align="center"><input type="checkbox" name="detailed_contacts" $detailed_contacts_checked></td>
				<td valign="middle" align="left"><font size="1">$office_con{'035'}</font></td></tr>
			<tr>
				<td valign="middle" align="center"><input type="text" name="display_contacts" value="$config[1]" size="2" maxlength="2"></td>
				<td valign="middle" align="left"><font size="1">$office_con{'036'}</font></td></tr>
			</table>
		</td>
		
		<td valign="top" align="left">
			<table cellpadding="2" cellspacing="0">
			<tr><td colspan="2"><font size="2"><B>$office_journal{'001'}</b></font></td></tr>
			<tr>
				<td valign="middle" align="center"><input type="checkbox" name="recent_entry" $recent_entry_checked></td>
				<td valign="middle" align="left"><font size="1">$office_journal{'007'}</font></td></tr>
			<tr>
				<td valign="middle" align="center"><input type="text" name="entry_index" value="$config[3]" size="2" maxlength="2"></td>
				<td valign="middle" align="left"><font size="1">$office_journal{'008'}</font></td></tr>
			</table>
		</td>
		
		<td valign="top" align="left">
			<table cellpadding="2" cellspacing="0">
			<tr><td colspan="2"><font size="2"><B>$office_task{'001'}</b></font></td></tr>
			<tr>
				<td valign="middle" align="center"><input type="text" name="task_index" value="$config[4]" size="2" maxlength="2"></td>
				<td valign="middle" align="left"><font size="1">$office_task{'012'}</font></td></tr>
			<tr>
				<td valign="middle" align="center">&nbsp;</td>
				<td valign="middle" align="left"><font size="1">&nbsp;</font></td></tr>
			</table>
		</td>
		</tr>
		<tr><td colspan="2"><INPUT TYPE="SUBMIT" VALUE="$office_gen{'029'} $office_gen{'030'}" class="button"></td>
		</tr></table>
	</td></tr></table>
</td></tr></table>
</form>
~;

} # end sub


################# 
sub write_cfg { 
################# 

open(CFG, ">$user_dir/$username.cfg"); 
	file_lock(CFG); 
	print CFG "$input{'detailed_contacts'}\n";
	print CFG "$input{'display_contacts'}\n";
	print CFG "$input{'recent_entry'}\n";
	print CFG "$input{'entry_index'}\n";
	print CFG "$input{'task_index'}\n";
	unfile_lock(CFG); 
close(CFG); 

print "Location: $officeURL/index.cgi\n\n"; 
exit; 

}


1; # return true