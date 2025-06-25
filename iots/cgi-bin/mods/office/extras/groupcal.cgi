#!/usr/bin/perl
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

# ----------------------------------------------------------------------------
# Based on calendar.pl - part of the verysimple organizer suite
# Copyright (c) 2001 Jason M. Hinkle. All rights reserved. This script is
# free software; you may redistribute it and/or modify it under the same
# terms as Perl itself.
# For more information see: http://www.verysimple.com/scripts/
#
# LEGAL DISCLAIMER:
# This software is provided as-is.  Use it at your own risk.  The
# author takes no responsibility for any damages or losses directly
# or indirectly caused by this software.
# ----------------------------------------------------------------------------

# WebAPP integration by Brad (webmaster@indie-central.ca)

### the following must be correct or else this script won't work ###
require "../../config.pl"; # main prog config
######

# do not modify anything below this line unless you know what you are doing!

$officeURL = "$scripturl/mods/office";
$imgURL = "$imagesurl/office";
$officeDIR = "$scriptdir/mods/office";
$dbdir = "$officeDIR/db";
$office_cfg = "$dbdir/office.cfg";
$index_template = "$dbdir/index.html"; # redirector if someone tries to view db files
$data_table = "$dbdir/group.calendar";
$data_template = "$dbdir/calendar.tab";

push(@INC,$scriptdir);
use vsLock;
use vsDB;
use CGI;

$scriptname = "WebOFFICE for WebAPP - Group Calendar";
$scriptver = "0.9.6";

eval {
	require "$sourcedir/subs.pl"; # main WebAPP subs
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

# WebAPP stuff #
getlanguage();
ban();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if ($lang_support eq "1") { mod_langsupp(); } 

# grab the display config
open(CFG, "$office_cfg") || error("$office_error{'001'} $office_cfg");
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

for ($b = 1; $b < @config; $b++) {
	($dummy[b], $dummy[b], $dummy[b], $dummy[b], $editor[b], $cc[b], $dummy[b]) = split(/\t/, $config[$b]);
}

$cc_yn = $cc[b];

$the_editor = $editor[b];

if ($the_editor eq "") {
	$the_editor = "admin";
}

unless (($username eq "admin") || ($username eq $the_editor)) {
	getcgi(); 
	if ($action eq "sendIM") {
		sendIM();
	}
}

# if the date table doesn't exist, create a blank one

unless (-e("$data_table")) { 
	open (FILE, "<$data_template") || error("$office_error{'002'} $data_template"); 
		file_lock(FILE);
		chomp(@tab = <FILE>);
		unfile_lock(FILE);
	close (FILE);
	
	open(FILE, ">$data_table") || error("$office_error{'003'} $data_table"); 
		file_lock(FILE);
		foreach $line (@tab) { print FILE "$line"; }
		print FILE "\n";
		unfile_lock(FILE);
	close(FILE);
}

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

my ($scriptName) = $ENV{'SCRIPT_NAME'} || "groupcal.cgi";
my ($objCGI) = new CGI;
my @dateArray = localtime(time);
my ($month) = $objCGI->param('vsMonth') || $dateArray[4]+1;
my ($year) = $objCGI->param('vsYear') || $dateArray[5]+1900;
my ($day) = $objCGI->param('vsDay') || $dateArray[3];
my ($command) = $objCGI->param('vsCOM') || "";
my ($id) = $objCGI->param('vsID') || "";
my ($showDefault) = 0;

my ($showDayDetails) = $objCGI->param('vsSD') || 0;
my ($noShowDayDetails) = 1;

$noShowDayDetails = 0 if ($showDayDetails);


$navbar = "$office_gen{'023'} $pagename $office_cal{'032'}";
print_top();
# print "<h2>Debugging Info:</h2>";
# print "config: @config<P>";
# print "editor: $the_editor<P>";
print qq~
<table cellspacing="0" cellpadding="0" border="0" width="100%">
	<tr>
	    <td align="left" valign="middle">
		<font size="+2"><IMG alt="$office_gen{'001'} $office_cal{'001'}" src="$imgURL/calendar_big.gif" border="0" align="absmiddle">&nbsp;$office_gen{'001'} $office_cal{'001'}</font>
		</td>
		<td align="right" valign="middle">
			<table align="right" cellspacing="0" cellpadding="2" border="0">
				<tr>
				<td align="center" bgcolor="$headerColor" valign="middle">~;
				if ($username ne $anonuser) {
					print qq~<a href="$officeURL/index.cgi"><IMG alt="$office_cal{'033'}" src="$imgURL/office_big.gif" border=0></A>~;
				}
				else {
				print qq~<IMG alt="$office_cal{'034'}" src="$imgURL/office_big.gif" border=0>~;
				}
				print qq~
				</tr>
				<tr>
				<td align="center" bgcolor="$dataDarkColor"><font size="1">~;
				if ($username ne $anonuser) {
					print qq~&nbsp;<a href="$officeURL/index.cgi">$office_cal{'033'}&nbsp;</A>~;
				}
				else {
				print qq~&nbsp;~;
				}
				print qq~</font></td>
				</tr>
			</table>
		</td>
	</tr>
</table>
~;

my ($objDB) = new vsDB(
	file => $data_table,
	delimiter => "\t",
);

# lock the datafile 
my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
$objLock->lock($data_table) || die("$office_error{'004'} $data_table"); 

if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($data_table);die;};

# so what's next?

if ($command eq "UPDATE") {
	$objDB->Filter("ID","eq",$id);
	UpdateCurrentRecord($objDB,$objCGI);
	$objDB->RemoveFilter;
	$objDB->MoveFirst;
} elsif ($command eq "DELETE") {
	$objDB->Filter("ID","eq",$id);
	$objDB->Delete;
	$objDB->Commit;
	$objDB->RemoveFilter;
	$objDB->MoveFirst;
} elsif ($command eq "INSERT") {
	$objDB->AddNew;
	my ($newId) = $objDB->Max("ID") || 0;
	$newId = int($newId) + 1;
	$objDB->FieldValue("ID",$newId);
	UpdateCurrentRecord($objDB,$objCGI);
	$objDB->MoveFirst;
}

# unlock the datafile
$objLock->unlock($data_table);

# print remaining content
&PrintDefault;

print_bottom();

undef($objDB);
undef($objLock);
undef($objCGI);


############################
sub PrintDefault {
############################

# there are now two displays available
# depending on if you are viewing the calendar details or not :)

print qq~
<table cellspacing="0" cellpadding="5" border="0" width="100%">
~;

# figure out which day to highlight on the calendar
my ($highlightDate) = $year . "." . $month . "." . $day;
	
# figure out following & previous month & year
my ($nmonth) = $month;
my ($nyear)  = $year;
NextMonth(\$nmonth,\$nyear);
my ($pmonth) = $month;
my ($pyear)  = $year;
PreviousMonth(\$pmonth,\$pyear);
	
if (!$showDayDetails) { # print two calendars side-by-side
	print "<tr><td valign='top' align='center' width='50%'>";
	# calendar for current month
	&PrintMonth($month,$year,$objDB,$highlightDate);

	print "</td><td valign='top' align='center' width='50%'>";
	# calendar for next month
	&PrintMonth($nmonth,$nyear,$objDB,$highlightDate);

	print "</tr><tr><td valign='top' width='50%'>";
	# show the event details for the day
	&PrintDay($year,$month,$day,$objDB);
	
	# display the  navigation
	print "<form><table width='100%' border='0' cellspacing='0' cellpadding='2'><tr><td align='center' valign='middle'>\n";
	print "<b>\n";
	print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=" . ($year - 1) . "'><img src='$imgURL/2arrowl.gif' alt='$month/" . ($year - 1) . "' border='0'></a>\n";
	print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$pmonth&vsYear=$pyear'><img src='$imgURL/1arrowl.gif' alt='$pmonth/$pyear' border='0'></a> \n";
	print "<select name='month' onchange=\"document.location='$scriptName?vsSD=$showDayDetails&' + this.options[this.selectedIndex].value;return true;\">\n";
	print "<option value='vsMonth=$pmonth&vsYear=$pyear'>$pmonth / $pyear</option>\n";
	print "<option value='vsMonth=$month&vsYear=$year' selected>$month / $year</option>\n";

	my ($nM) = $month;
	my ($nY) = $year;
	for (my $count = 1;$count < 12;$count++) {
		NextMonth(\$nM,\$nY);
		print "<option value='vsMonth=$nM&vsYear=$nY'>$nM / $nY</option>\n";	
	}	

	print "</select>\n";
	print " <a href='$scriptName?vsSD=$showDayDetails&vsMonth=$nmonth&vsYear=$nyear'><img src='$imgURL/1arrowr.gif' alt='$nmonth/$nyear' border='0'></a>\n";
	print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=" . ($year + 1) . "'><img src='$imgURL/2arrowr.gif' alt='$month/" . ($year + 1) . "' border='0'></a>\n";
	print "</b>\n";
	print "</form></td></tr></table>";
	# end nav display

	print qq~</td><td valign='top' width='50%'>~;

	print "<p>";
   
	if ($command eq "EDIT") {
		$objDB->Filter("ID","eq",$id);
		PrintCurrentRecord($objDB);
	} else {
		PrintBlankRecord($objDB);
	}    

	print "</td>\n";
	print "</tr></table>\n";
}

else { # reformat the page for a larger calendar
	print "<tr><td valign='top' align=\"center\">";
	# current calendar
	&PrintMonth($month,$year,$objDB,$highlightDate);
	
	print "</td></tr><tr><td valign='top'>";
	
	# display the navigation
	print "<form><table width='100%' border='0' cellspacing='0' cellpadding='2'><tr><td align='center' valign='middle'>\n";
	print "<b>\n";
	print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=" . ($year - 1) . "'><img src='$imgURL/2arrowl.gif' alt='$month/" . ($year - 1) . "' border='0'></a>\n";
	print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$pmonth&vsYear=$pyear'><img src='$imgURL/1arrowl.gif' alt='$pmonth/$pyear' border='0'></a> \n";
	print "<select name='month' onchange=\"document.location='$scriptName?vsSD=$showDayDetails&' + this.options[this.selectedIndex].value;return true;\">\n";
	print "<option value='vsMonth=$pmonth&vsYear=$pyear'>$pmonth / $pyear</option>\n";
	print "<option value='vsMonth=$month&vsYear=$year' selected>$month / $year</option>\n";

	my ($nM) = $month;
	my ($nY) = $year;
	for (my $count = 1;$count < 12;$count++) {
		NextMonth(\$nM,\$nY);
		print "<option value='vsMonth=$nM&vsYear=$nY'>$nM / $nY</option>\n";	
	}	

	print "</select>\n";
	print " <a href='$scriptName?vsSD=$showDayDetails&vsMonth=$nmonth&vsYear=$nyear'><img src='$imgURL/1arrowr.gif' alt='$nmonth/$nyear' border='0'></a>\n";
	print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=" . ($year + 1) . "'><img src='$imgURL/2arrowr.gif' alt='$month/" . ($year + 1) . "' border='0'></a>\n";
	print "</b>\n";
	print "</form></td></tr></table>";
	# end nav display
	
	print "</td></tr><tr><td valign='top'>";

	# show the event details for the day
	&PrintDay($year,$month,$day,$objDB);
	
	print "</td></tr><tr><td valign='top'>";
   
	if ($command eq "EDIT") {
		$objDB->Filter("ID","eq",$id);
		PrintCurrentRecord($objDB);
	} else {
		PrintBlankRecord($objDB);
	}    

	print "</td>\n";
	print "</tr></table>\n";

}

} # end sub

############################
sub PrintDay {
############################

my $year = shift || return 0 ;
my $month = shift || return 0 ;
my $day = shift || return 0 ;
my $objMyDb = shift || return 0;

my $thisDate = "$year.$month.$day";

my @months = ($office_cal{'008'},$office_cal{'009'},$office_cal{'010'},$office_cal{'011'},$office_cal{'012'},$office_cal{'013'},$office_cal{'014'},$office_cal{'015'},$office_cal{'016'},$office_cal{'017'},$office_cal{'018'},$office_cal{'019'});

$objMyDb->RemoveFilter;	
$objMyDb->Filter("DATE","eq",$thisDate);

print qq~
<table width="100%" border="0" cellspacing="0" cellpadding="2">
<tr>
	<td bgcolor="$dataDarkColor">
	<IMG alt="$office_cal{'001'}" src="$imgURL/calendar_small.gif" border="0" align="absmiddle">&nbsp;<b>$office_cal{'020'} $months[$month-1] $day, $year</b></td>
</tr>
<tr>
	<td bgcolor="$dataDarkColor">
	<table width="100%" cellpadding="2" cellspacing="1" border="0">
	~;

# the following prints out the headings for the daily event data
# remove the # in order to display them

#print qq~
#<tr>
#<td width="20">&nbsp;</td>
#<td width="75"><b>$office_cal{'004'}</b></td>
#<td width="250"><b>$office_cal{'005'}</b></td>
#</tr>
#~;

if ($objMyDb->EOF) {
	print "<tr><td colspan='3' bgcolor='$dataLightColor'><i>$office_cal{'021'}</i></td></tr>\n";
}

while (!$objMyDb->EOF) {
	print "<tr><td align='center' valign='middle' width='20' bgcolor='$dataLightColor'><a href='$scriptName?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$day&vsID=" . $objMyDb->FieldValue("ID") . "'><img src='$imgURL/calendar.gif' alt=\"$office_cal{'031'}" . $objMyDb->FieldValue("EVENT") . "\"' border='0'></a></td>";
	print "<td valign='middle' bgcolor='$dataLightColor'><font size=\"1\">" . $objMyDb->FieldValue("TIME") . "</font></td>";
	$event = substr($objMyDb->FieldValue("EVENT"),0,25);
	$event .= "...";
	print "<td valign='middle' bgcolor='$dataLightColor'><font size=\"1\">$event</font></td>\n";
	if ($showDayDetails) {
		if ($enable_ubbc) { 
			$message = $objMyDb->FieldValue("DETAILS");
			doubbc();
			$details = substr($message,0,65);
			$details .= "...";
		}
		else {
			$details = substr($objMyDb->FieldValue("DETAILS"),0,65);
			$details .= "...";
		}
		print "<td valign='middle' bgcolor='$dataLightColor'><font size=\"1\">$details</font></td>\n";
	}
	print "</tr>";
	$objMyDb->MoveNext;
}

print "</table></td></tr></table>\n";

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

print "<p>\n";
print "<b>$months[$month-1] $year</b>\n";

if ($showDayDetails) {
	print " <font size='1'>[ <a href='$scriptName?vsSD=0&vsMonth=$month&vsYear=$year'>$office_cal{'029'}</a> ]</font>\n"
} else {
	print " <font size='1'>[ <a href='$scriptName?vsSD=1&vsMonth=$month&vsYear=$year'>$office_cal{'030'}</a> ]</font>\n"
}		
	
if ($showDayDetails) { # large calendar - hack for size
    print "<table border='1' cellspacing='0' cellpadding='2' width='455'>\n";
	$cellwidth = "65";
}
else { # small calendar - hack for size
    print "<table border='1' cellspacing='0' cellpadding='2' width='252'>\n";
	$cellwidth = "36";
}
	
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
		    print "<td width='$cellwidth' height='$cellwidth' bgcolor='$dataHighlightColor'>";
		} else {
		    print "<td width='$cellwidth' height='$cellwidth'>";
		}
		
		if ($thisDate eq $today) {
		    $tick = "*";
		} else {
		    $tick = "";
		}		    

		$objMyDb->RemoveFilter;	
		$objMyDb->Filter("DATE","eq",$thisDate);

		if ($objMyDb->EOF) {
		    print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'>$weekDayCount</a> $tick<br>";
		} else {
		    print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'><u>$weekDayCount</u></a> $tick<br>";
		}			

		if ($showDayDetails) {
		    print "<font size='1'>";
		    while (!$objMyDb->EOF) {
			$chopit = substr($objMyDb->FieldValue("EVENT"),0,9); # bm mod
			print "<a href='$scriptName?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount&vsID=" . $objMyDb->FieldValue("ID") . "'>" . $chopit . "...</a><br>";
			$objMyDb->MoveNext;
		    }
		    print "</font>";
		}
		
		print "</td>\n";
	    } else {
		print "<td bgcolor='$dataLightColor'>&nbsp;</td>\n";
	    }
	    
	    $dayCount++;
	}    
	print "</tr>\n";
    }    
    print "</table>\n";
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


############################
sub PrintCurrentRecord {
############################

my ($objMyDB) = shift;
my ($fieldName, $fieldValue);

open(CFG, "$office_cfg") || error("$office_error{'001'} $office_cfg");
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

for ($b = 1; $b < @config; $b++) {
	($dummy[b], $dummy[b], $dummy[b], $dummy[b], $editor[b], $cc[b], $dummy[b]) = split(/\t/, $config[$b]);
}

$cc_yn = $cc[b];

$the_editor = $editor[b];

if ($the_editor eq "") {
	$the_editor = "admin";
}

# next - decide what form action to use.  If the user is admin, they'll want the data modification buttons
# if the user is a member, we want the action to send an IM instead.

if (($username eq "admin") || ($username eq $the_editor)) {
	print "<form action='$scriptName' method='post'>\n";
} 
else {
	print "<form action='$scriptName?action=sendIM' method='post'>\n";
}

print qq~
<table width="100%" border="0" cellspacing="0" cellpadding="2">
<tr>
	<td bgcolor="$dataDarkColor">
	<IMG alt="$office_cal{'007'}" src="$imgURL/notes_small.gif" border="0" align="absmiddle">&nbsp;<b>$office_cal{'007'}</b></td>
</tr>
<tr>
	<td bgcolor="$dataDarkColor">
	<table width="100%" cellpadding="2" cellspacing="1" border="0">
~;

# modified the following in order to support multiple languages
# not as nice as original code

if ($showDayDetails) {
	$cols = "50";
	$rows = "5";
	$size = "25";
}
else {
	$cols = "16";
	$rows = "10";
	$size = "20";
}

# next, we print out one of three versions of the	Event Details:
# anonymous user: add the details within the HTML (no input/text boxes)
# regular member: add the details as above, but also print out the add form
# editor and/or admin: print out form, but push details into it.

if ($username eq "$anonuser") { 
	foreach $fieldName ($objMyDB->FieldNames) {
		if ($fieldName eq "ID") {
			print "<input type='hidden' name='vsID' value='" . $objMyDB->FieldValue("ID") . "'>\n";
		}
		elsif ($fieldName eq "DATE") {
			if ($objMyDB->FieldValue("ID")) {
				print "<input type='hidden' name='DATE' value='" . $objMyDB->FieldValue("DATE") . "'>\n";
			}
		} 
		elsif ($fieldName eq "TIME") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"middle\">$office_cal{'004'}</td>\n";
			print "<td valign=\"middle\">";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</td>\n";
			print "</tr>\n";
		} 
		elsif ($fieldName eq "EVENT") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"middle\">$office_cal{'005'}</td>\n";
			print "<td valign=\"middle\">";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</td>\n";
			print "</tr>\n";		
		} 
		elsif ($fieldName eq "DETAILS") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"top\">$office_cal{'006'}</td>\n";
			print "<td valign=\"top\">";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$message = $fieldValue;
			if ($enable_ubbc) { doubbc(); }
			$fieldValue = $message;
#			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</td>\n";
			print "</tr>\n";
		} 
		else {
		}
	}
	print "</table></td></tr></table><BR>\n"
}

elsif (($username eq "admin") || ($username eq $the_editor)) { 
	foreach $fieldName ($objMyDB->FieldNames) {
		if ($fieldName eq "ID") {
			print "<input type='hidden' name='vsID' value='" . $objMyDB->FieldValue("ID") . "'>\n";
		}
		elsif ($fieldName eq "DATE") {
			if ($objMyDB->FieldValue("ID")) {
				print "<input type='hidden' name='DATE' value='" . $objMyDB->FieldValue("DATE") . "'>\n";
			}
		} 
		elsif ($fieldName eq "DETAILS") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"top\">$office_cal{'006'}</td>\n";
			print "<td valign=\"top\"><textarea name='DETAILS' cols='$cols' rows='$rows'>";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</textarea></td>\n";
			print "</tr>\n";
		}
		elsif ($fieldName eq "TIME") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"middle\">$office_cal{'004'}</td>\n";
			print "<td valign=\"middle\"><input size=\"$size\" name=\"TIME\" value=\"";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "\"></td>\n";
			print "</tr>\n";
		}
		elsif ($fieldName eq "EVENT") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"middle\">$office_cal{'005'}</td>\n";
			print "<td valign=\"middle\"><input size=\"$size\" name=\"EVENT\" value=\"";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "\"></td>\n";
			print "</tr>\n";
		}
		else {
		}
	}
	print "</table></td></tr></table><BR>\n"
}

else { # all other members see this 
	foreach $fieldName ($objMyDB->FieldNames) {
		if ($fieldName eq "ID") {
			print "<input type='hidden' name='vsID' value='" . $objMyDB->FieldValue("ID") . "'>\n";
		}
		elsif ($fieldName eq "DATE") {
			if ($objMyDB->FieldValue("ID")) {
				print "<input type='hidden' name='DATE' value='" . $objMyDB->FieldValue("DATE") . "'>\n";
			}
		} 
		elsif ($fieldName eq "DETAILS") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"top\">$office_cal{'006'}</td>\n";
			print "<td valign=\"top\">";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$message = $fieldValue;
			if ($enable_ubbc) { doubbc(); }
			$fieldValue = $message;
#			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</td>\n";
			print "</tr>\n";
		} 
		elsif ($fieldName eq "TIME") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"middle\">$office_cal{'004'}</td>\n";
			print "<td valign=\"middle\">";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</td>\n";
			print "</tr>\n";
		} 
		elsif ($fieldName eq "EVENT") {
			print "<tr bgcolor='$dataLightColor'>\n";
			print "<td valign=\"middle\">$office_cal{'005'}</td>\n";
			print "<td valign=\"middle\">";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</td>\n";
			print "</tr>\n";		
		} 
		else {
		}
	}
	print "</table></td></tr></table><BR>\n"	
}

print qq~

~;

print qq~
<input type="hidden" name="vsSD" value="$showDayDetails">
<input type="hidden" name="vsDay" value="$day">
<input type="hidden" name="vsMonth" value="$month">
<input type="hidden" name="vsYear" value="$year">
~;

if (($username eq "admin") || ($username eq "$the_editor")) {
	if ($objMyDB->FieldValue("ID")) {
		print qq~
		<input type="hidden" name="vsCOM" value="UPDATE">
		<input type="submit" value="$office_gen{'003'}" class="button">~;
		print "<input style=\"COLOR: FF0000;\" type='submit' class='button' value=\"$office_gen{'004'}\" onclick=\"if (confirm('$office_gen{'007'}')) {self.location='$scriptName?vsSD=$showDayDetails&vsCOM=DELETE&vsMonth=$month&vsYear=$year&vsDay=$day&vsID=" . $objMyDB->FieldValue("ID") . "';return false;} else {return false;};\">\n";
	} 
	else {
		print qq~
		<input type="hidden" name="DATE" value="$year.$month.$day">
		<input type="hidden" name="vsCOM" value="INSERT">
		<input type="submit" class="button" value="$office_gen{'006'}">
		~;
	}
} 
else {
	if ($username ne "$anonuser") {
	
	# now print out the add form for the members
	print qq~
	<table width="100%" border="0" cellspacing="0" cellpadding="2">
	<tr>
		<td bgcolor="$dataDarkColor">
		<IMG alt="Add an Event" src="$imgURL/notes_small.gif" border="0" align="absmiddle">&nbsp;<b>Add an Event</b></td>
	</tr>
	<tr>
		<td bgcolor="$dataDarkColor">
		<table width="100%" cellpadding="2" cellspacing="1" border="0">
		<tr bgcolor='$dataLightColor'><td colspan="2">$office_cal{'035'}</td></tr>
	~;
	# clean this up later:
	print "<input type='hidden' name='DATE' value='" . $objMyDB->FieldValue("DATE") . "'>\n";
	print "<input type='hidden' name='vsID' value='" . $objMyDB->FieldValue("ID") . "'>\n";
	print "<tr bgcolor='$dataLightColor'>\n";
	print "<td valign=\"middle\">$office_cal{'004'}</td>\n";
	print "<td valign=\"middle\"><input size=\"$size\" name=\"TIME\">\n";
	print "</tr>\n";
	print "<tr bgcolor='$dataLightColor'>\n";
	print "<td valign=\"middle\">$office_cal{'005'}</td>\n";
	print "<td valign=\"middle\"><input size=\"$size\" name=\"EVENT\">\n";
	print "<tr bgcolor='$dataLightColor'>\n";
	print "<td valign=\"top\">$office_cal{'006'}</td>\n";
	print "<td valign=\"top\"><textarea name='DETAILS' cols='$cols' rows='$rows'>";
	print "</textarea></td>\n";
	print "</tr>\n";
	#
	print qq~
	<tr bgcolor='$dataLightColor'><td colspan="2">
	<input type="submit" value="$office_gen{'014'}" class="button">
	<input type='hidden' name='MEMBERNAME' value='$username'>
	<input type='hidden' name='YEAR' value='$year'>
	<input type='hidden' name='MONTH' value='$month'>
	<input type='hidden' name='DAY' value='$day'>
	<input type='hidden' name='vsCOM' value='sendIM'>
	</td></tr>
	</table></td></tr></table><BR>
	~;
	}
}
if (($username eq "admin") || ($username eq "$the_editor")) {
	print qq~<input type="reset" value="$office_gen{'005'}" class="button" onclick="window.history.go(-1);return false;">~;
}
print "</form>\n";


}	


############################
sub PrintBlankRecord {
############################

my ($objMyDB) = shift;
$objMyDB->AddNew;
PrintCurrentRecord($objMyDB); # this won't be committed, so no big deal
return 1;

}


############################
sub UpdateCurrentRecord {
############################

my ($objMyDB) = shift;
my ($objMyCGI) = shift;
my ($fieldName,$fieldValue);
foreach $fieldName ($objMyDB->FieldNames) {
	$fieldValue = $objMyCGI->param($fieldName);
	$objMyDB->FieldValue($fieldName,$fieldValue);
}
$objMyDB->Commit;

}



############################
sub NextMonth {
############################

my ($nMonth) = shift || return 0;
my ($nYear) = shift || return 0;
$$nMonth++;
if ($$nMonth > 12) {
	$$nMonth = 1;
	$$nYear++;
}

}

############################
sub PreviousMonth {
############################

my ($nMonth) = shift || return 0;
my ($nYear) = shift || return 0;
$$nMonth--;
if ($$nMonth < 1) {
	$$nMonth = 12;
	$$nYear--;
}

}


##############
sub sendIM { 
##############

# grab the display config
open(CFG, "$office_cfg"); 
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

for ($b = 1; $b < @config; $b++) {
	($dummy[b], $dummy[b], $dummy[b], $dummy[b], $editor[b], $cc[b], $dummy[b]) = split(/\t/, $config[$b]);
}

$the_editor = $editor[b];
if ($the_editor eq "") {
	$the_editor = "admin";
}

$event_year = $input{'YEAR'};
$event_month = $input{'MONTH'};
$event_day = $input{'DAY'};
$event_date = "$event_month.$event_day.$event_year";
$event_time = htmlescape($input{'TIME'});
$event_event = htmlescape($input{'EVENT'});
$event_details = htmlescape($input{'DETAILS'});
$event_member = $input{'MEMBERNAME'};
$return_day =  $input{'vsDay'};
$return_month =  $input{'vsMonth'};
$return_year =  $input{'vsYear'};

$msgid = time;
$imsubj = "$office_cal{'036'} $event_date";
$formatmsg = "<b>$office_cal{'037'}</b><P>$realname $office_cal{'038'}<P><b>$office_cal{'003'}:</b> $event_date<BR><b>$office_cal{'004'}:</b> $event_time<BR><b>$office_cal{'005'}:</b> $event_event<BR><b>$office_cal{'006'}:</b> $event_details<BR><b>$office_cal{'039'}:</b> $date<P>";
$formatmsg .= "<BR><BR><B><a href=\"$officeURL/groupcal.cgi?vsSD=$showDayDetails&vsMonth=$event_month&vsYear=$event_year&vsDay=$event_day\" target=\"_blank\">$office_cal{'046'}</a></b> $office_cal{'047'}";

# send the request to the calendar editor
open (AFILE, "$memberdir/$the_editor.msg") || error("$office_error{'001'} $memberdir/$the_editor.msg");
	file_lock(AFILE);
	@imessages = <AFILE>;
	unfile_lock(AFILE);
close (AFILE);

open (AFILE, ">$memberdir/$the_editor.msg") || error("$office_error{'002'} $memberdir/$the_editor.msg");
	file_lock(AFILE);
	print AFILE "$realname|$imsubj|$date|$formatmsg|$msgid\n";
	foreach $curm (@imessages) { print AFILE "$curm"; }
	unfile_lock(AFILE);
close(AFILE);

# if the admin wishes to be Cc'd, send them a copy
if ($cc[b] eq "on") {
	$formatmsg .= "<BR>$the_editor $office_cal{'048'}";

	open (CFILE, "$memberdir/admin.msg") || error("$office_error{'001'} $memberdir/admin.msg");
		file_lock(CFILE);
		@imessages = <CFILE>;
		unfile_lock(CFILE);
	close (CFILE);

	open (CFILE, ">$memberdir/admin.msg") || error("$office_error{'002'} $memberdir/admin.msg");
		file_lock(CFILE);
		print CFILE "$realname|$imsubj|$date|$formatmsg|$msgid\n";
		foreach $curm (@imessages) { print CFILE "$curm"; }
		unfile_lock(CFILE);
	close(CFILE);
}

# notify the user who submitted the info
$mformatmsg = "<b>$office_cal{'037'}</b><P>$office_cal{'040'} $date. $office_cal{'041'}:<P><b>$office_cal{'003'}:</b> $event_date<BR><b>$office_cal{'004'}:</b> $event_time<BR><b>$office_cal{'005'}:</b> $event_event<BR><b>$office_cal{'006'}:</b> $event_details<BR><BR>$office_cal{'042'}";

open (MFILE, "$memberdir/$event_member.msg") || error("$office_error{'002'} $memberdir/$event_member.msg");
#open (MFILE, "$memberdir/$event_member.msg");
	file_lock(MFILE);
	@imessages = <MFILE>;
	unfile_lock(AFILE);
close (MFILE);

open (MFILE, ">$memberdir/$event_member.msg") || error("$$office_error{'002'} $memberdir/$event_member.msg");
	file_lock(MFILE);
	print MFILE "$the_editor|$imsubj|$date|$mformatmsg|$msgid\n";
	foreach $curm (@imessages) { print MFILE "$curm"; }
	unfile_lock(MFILE);
close(MFILE);


print "Location: $officeURL/groupcal.cgi?vsSD=1&vsMonth=$return_month&vsYear=$return_year&vsDay=$return_day\n\n"; 
exit; 

}



1; # return true