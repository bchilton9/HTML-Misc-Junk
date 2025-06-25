#!/usr/bin/perl

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

sub cal_displaySidebarCal {

        my ($dataFile) = "$cm_dataDir/$cm_eventsFileName";

        my @dateArray = localtime(time);
        my ($month)   = $dateArray[4]+1;
        my ($year)    = $dateArray[5]+1900;
        my ($day)     = $dateArray[3];

        my ($objDB) = new vsDB(
                file => $dataFile,
                delimiter => $cm_delimiter,
        );

        if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($dataFile);die;};

        print qq~
        <tr><td>
          <table cellspacing='0' cellpadding='10'>
            <tr valign='top'>
              <td align='center'>
                <font size='2' face='arial,helvetica'>
                <p><font face='arial,helvetica' size='2'><b><a style="$cmsb_headFontStyle" href='$cm_scriptUrl?vsSD=0&vsMonth=$month&vsYear=$year'>$months[$month-1] $year</a></b></font>
                <table style='$cmsb_borderStyle' border='$cmsb_borderWidth' cellspacing='0'>
        ~;


        # figure out which day to highlight on the calendar
        my ($highlightDate) = $year . "." . $month . "." . $day;

        &PrintMonth1($month,$year,$objDB,$highlightDate);

        print qq~
                        </table>
                </font>
              </td>
            </tr>
          </table>
        </td></tr>
        ~;

        1;
}

sub PrintMonth1 {
    my $month   = shift || 1;
    my $year    = shift || 2001;
    my $objMyDb = shift || return 0;
        # highlightDate is passed in below...

    my ($firstDay,$numDays,$numWeeks) = &GetMonthInfo1($month,$year);

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

    # print the days of the week
    print "<tr>\n";
    foreach $temp (@daysAbbrev) {
                print "<td style='$cmsb_dayHeadCellStyle'><font style='$cmsb_dayHeadFontStyle' face='arial,helvetica' size='2'><b>$temp</b></font></td>";
    }
    print "</tr>\n";

    for (my $cellCount = 1;$cellCount <= $numWeeks; $cellCount++) {
                print "<tr valign='top'>\n";
                foreach $temp (@daysAbbrev) {
                    if (($dayCount > $firstDay-1) && ($weekDayCount < $numDays)) {
                                $weekDayCount++;

                                $thisDate = $year . "." . $month . "." . $weekDayCount;

                                if ($thisDate eq $highlightDate) {
                                    print "<td align='center' width='$cmsb_cellSize' height='$cmsb_cellSize' style='$cmsb_selCellStyle'><font face='arial,helvetica' size='2'>";
                                    $style = $cmsb_selFontStyle;
                                } else {
                                    print "<td align='center' width='$cmsb_cellSize' height='$cmsb_cellSize' style='$cmsb_stdCellStyle'><font face='arial,helvetica' size='2'>";
                                    $style = $cmsb_stdFontColor;
                                }

                            $objMyDb->RemoveFilter;
                            $objMyDb->Filter("DATE","eq",$thisDate);
                            #if ($settings[7] ne $root) {
                                    if ($username eq $anonuser) {
                                            $objMyDb->Filter("APPROVED","eq","1");
                                            $objMyDb->Filter("OWNER","eq",$cal_msg{'008'});
                                    } else {
                                            $objMyDb->Filter("APPROVED","eq","1");
                                            $objMyDb->Filter("OWNER","eq",$cal_msg{'008'});
                                            $objMyDb->Filter("OWNER","eq",$username,1);
                                            $objMyDb->Filter("DATE","eq",$thisDate);
                                    }
                            #}
                                if ($objMyDb->EOF) {
                                    print "<a style='$style' href='$cm_scriptUrl?vsSD=0&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'>$weekDayCount</a><br>";
                                } else {
                                    print "<b><a style='$style' href='$cm_scriptUrl?vsSD=0&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'>$weekDayCount</a></b><br>";
                                }

                                print "</font></td>\n";
                    } else {
                                print "<td style='$cmsb_emptyCellStyle'><font face='arial,helvetica' size='1'>&nbsp;</font></td>\n";
                    }

                    $dayCount++;
                }
                print "</tr>\n";
    }
}

sub GetMonthInfo1 {

    my $month = shift || 1;
    my $year  = shift || 2002;

    my($firstDow,$numDays);

    require Time::Local;

    # convert user input into approp format for processing
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

1;