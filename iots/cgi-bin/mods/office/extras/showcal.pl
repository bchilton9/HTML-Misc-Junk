#!/usr/bin/perl

# this is a replacement for:

###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# showcal.pl 						  		      #
#                                                                             #
# Copyright (C) 2002 by Carter (carter@mcarterbrown.com)                      #
#                                                                             #
###############################################################################
###############################################################################

# showcal.pl - WebOFFICE v0.9.6
# Based on the print month sub of verysimple's calendar


############################
sub displayCal {
############################

push(@INC,$scriptdir);
use vsLock;
use vsDB;
use CGI;

$officeURL = "$scripturl/mods/office";
$officeDIR = "$scriptdir/mods/office";
$dbdir = "$officeDIR/db";
$office_cfg = "$dbdir/office.cfg";
$data_table = "$dbdir/group.calendar";
$data_template = "$dbdir/calendar.tab";

require "$sourcedir/subs.pl"; # main prog subs
require "$dbdir/office.pl"; # some office subs
require "$officeDIR/config.dat"; # dat file for mod manager

getlanguage();
if ($lang_support eq "1") { mod_langsupp(); }

# if the date table doesn't exist, create a blank one

unless (-e("$data_table")) { 
	open (FILE, "<$data_template") || error("$office_error{'002'} $data_template"); 
		file_lock(FILE);
		@tab = <FILE>;
		unfile_lock(FILE);
	close (FILE);

	open(FILE, ">$data_table") || error("$office_error{'003'} $data_table"); 
		file_lock(FILE);
		foreach $line (@tab) { print FILE "$line"; }
		print FILE "\n";
		unfile_lock(FILE);
		close(FILE);
}
	
$scriptName = "$officeURL/groupcal.cgi";
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
my ($cellSize) = 25;
$cellSize = 60 if ($showDayDetails);
$noShowDayDetails = 0 if ($showDayDetails);

my ($objDB) = new vsDB(
	file => $data_table,
	delimiter => "\t",
);


# lock the datafile 
my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
$objLock->lock($data_table) || die("$office_error{'004'} $data_table"); 

if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($data_table);die;};

&PrintMonth($month,$year,$objDB,$highlightDate);

# unlock the datafile
$objLock->unlock($data_table);

}

1;


############################
sub PrintMonth {
############################

# start printing the calendar

# Calendar defintions. 

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
my $style;

my @dateArray = localtime(time);
$dateArray[5]+=1900;
$dateArray[4]+=1;
my $today = $dateArray[5] . "." . $dateArray[4] . "." . $dateArray[3];

my $highlightDate = shift || $today;

print "<p><tr><td align='center'>\n";
print "<a href='$scriptName?vsSD=1&vsMonth=$month&vsYear=$year'><b>$months[$month-1] $year</b></a>\n";
print "<table border='1' cellspacing='0' cellpadding='2' width='98%'>\n";


# print the days of the week 
print "<tr>\n";
foreach $temp (@days) {
	print "<td bgcolor=\"$dataDarkColor\"><b>$temp</b></td>\n";
}
print "</tr>\n";

for (my $cellCount = 1;$cellCount <= $numWeeks; $cellCount++) {
	print "<tr valign='top'>\n";
	foreach $temp (@days) {
	if (($dayCount > $firstDay-1) && ($weekDayCount < $numDays)) {
		$weekDayCount++;

		$thisDate = $year . "." . $month . "." . $weekDayCount;
		
		if ($thisDate eq $highlightDate) {
		    print "<td width='14%' height='$cellSize' bgcolor='$dataHighlightColor'>";
		} else {
		    print "<td width='14%' height='$cellSize'>";
		}
		
		$objMyDb->RemoveFilter;	
		$objMyDb->Filter("DATE","eq",$thisDate);

		if ($objMyDb->EOF) {
		print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'>$weekDayCount</a><br>\n";
		} else {
		print "<a href='$scriptName?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'><u>$weekDayCount</a></u><br>\n";
		}			

		if ($showDayDetails) {
		print "\n";
		while (!$objMyDb->EOF) {
			print "<a href='$scriptName?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount&vsID=" . $objMyDb->FieldValue("ID") . "'>" . $objMyDb->FieldValue("EVENT") . "</a><br>\n";
			$objMyDb->MoveNext;
		}
		print "\n";
		}
		

		print "</td>\n";
	} else {
		print "<td bgcolor=\"$dataLightColor\">&nbsp;</td>\n";
	}
	
	$dayCount++;
	}
	print "</tr>\n";
}
print "</table></td></tr>\n";

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