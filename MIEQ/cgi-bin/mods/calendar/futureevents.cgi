#!/usr/bin/perl
# ----------------------------------------------------------------------------
# WebApp Calendar Mod - calendar.pl
#
# Mod created by Ted Loomos (tloomos@pbs-inc.net)
#
# Based on the verysimple organizer suite
# Copyright (c) 2001 Jason M. Hinkle. All rights reserved. This script is
# free software; you may redistribute it and/or modify it under the same
# terms as Perl itself.
# For more information see: http://www.verysimple.com/scripts/
#
# LEGAL DISCLAIMER:
# This software is provided as-is.  Use it at your own risk.  The
# author takes no responsibility for any damages or losses directly
# or indirectly caused by this software.
#
# Version History
# 0.0.1 - 06/09/02 - Initial script created
# 0.0.2 - 06/24/02 - Cleaned up code and fixed minor bugs
# 0.0.3 - 07/13/02 - Modified sidebar.cgi so it can be used on the left side
#
# To Do:
# ----------------------------------------------------------------------------
$| = 1;
use CGI::Carp qw(fatalsToBrowser);
$scriptname = "WebAPP";
$scriptver = "0.9.9";

BEGIN {
##--------------------------------------------------------------
## If you are not using standard folder locations, the following
## line may need to be changed to match your installation
##--------------------------------------------------------------
        require "$scriptdir/mods/calendar/data/calendar.cfg";
##--------------------------------------------------------------
## Nothing below this point should require modification
##--------------------------------------------------------------
        if (-e "$cm_langDir/$userlang") {require "$cm_langDir/$userlang"} else {require "$cm_langDir/$cm_langFileName"}

        push(@INC,$cm_scriptDir);
}

use vsDB;

####################################
# Calendar Mod
####################################

sub cal_displayfutureevents {

#
        my ($dataFile) = "$cm_dataDir/$cm_eventsFileName";

        my @dateArray = localtime(time);
        my ($month)   = $dateArray[4]+1;
        my ($year)    = $dateArray[5]+1900;
        my ($day)     = $dateArray[3];

        my ($objDB) = new vsDB(
                file => $dataFile,
                delimiter => $cm_delimiter,
        );

        if (!$objDB->Open) {print $objDB->LastError;$objLock->release($dataFile);die;};

        # figure out which day to highlight on the calendar
        my ($highlightDate) = $year . "." . $month . "." . $day;

# show the event details for today and 200 days forward or 10 events
   my $workday = time();
        my @dateArray = localtime($workday);
        my ($month)   = $dateArray[4]+1;
        my ($year)    = $dateArray[5]+1900;
        my ($day)     = $dateArray[3];
        $rjteventcnt = 0;
    &PrintDay($year,$month,$day,$objDB);

   for ($i = 1; $i < 200; $i++) {
   $workday = $workday + ( 24 * 60 * 60 );
        my @dateArray = localtime($workday);
        my ($month)   = $dateArray[4]+1;
        my ($year)    = $dateArray[5]+1900;
        my ($day)     = $dateArray[3];
    &PrintDay($year,$month,$day,$objDB);
        if ($rjteventcnt > 10) { $i = 200; }
    }
   my $workday = time();
        my @dateArray = localtime($workday);
        my ($month)   = $dateArray[4]+1;
        my ($year)    = $dateArray[5]+1900;
        my ($day)     = $dateArray[3];

        print  "<br><a href='$cm_scriptUrl?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$day'>More Events</a>";


        1;
}

# _____________________________________________________________________________
sub PrintDay {
    my $year = shift || return 0 ;
    my $month = shift || return 0 ;
    my $day = shift || return 0 ;
    my $objMyDb = shift || return 0;


    my $thisDate = "$year.$month.$day";

    # add a filter to get the event details for the day
    $objMyDb->RemoveFilter;
    $objMyDb->Filter("DATE","eq",$thisDate);
    #if ($settings[7] ne $root) {
            if ($username eq $anonuser) {
                    $objMyDb->Filter("APPROVED","eq","1");
                    $objMyDb->Filter("OWNER","eq","$cal_msg{'008'}");
            } else {
                    $objMyDb->Filter("APPROVED","eq","1");
                    $objMyDb->Filter("OWNER","eq","$cal_msg{'008'}");
                    $objMyDb->Filter("OWNER","eq","$username",1);
                    $objMyDb->Filter("DATE","eq",$thisDate);
            }
    #}


    # print "<font size='2' face='arial,helvetica'><b>$cal_msg{'003'} $months[$month-1] $day, $year </b></font><br>\n";

    # print "<b>$cal_msg{'004'}</b>";
    # print "<b>$cal_msg{'005'}</b>";

    # check for no events found and display message if appropriate
    if ($objMyDb->EOF) {
        #        print "\n";
    }

    # display each event record in table
    while (!$objMyDb->EOF) {
                print "<br>";
                print  $months[$month-1]. " " . $day . " ". $objMyDb->FieldValue("TIME") . "<br>";
                print  "<a href='$cm_scriptUrl?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$day&vsID=" . $objMyDb->FieldValue("ID") . "'>" . $objMyDb->FieldValue("EVENT") . "&nbsp;</a>";
                $rjteventcnt = $rjteventcnt + 1;
                $objMyDb->MoveNext;
    }


}


    require Time::Local;


1;