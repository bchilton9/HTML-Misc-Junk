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

        require "./data/calendar.cfg";
        require "../../config.pl";
        require "$lang";
        require "$sourcedir/subs.pl";

        ##--------------------------------------------------------------
        ## Nothing below this point should require modification
        ##--------------------------------------------------------------

        push(@INC,$cm_scriptDir);
}

eval {
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

&parse_form;

getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if (-e "$cm_langDir/$userlang") {require "$cm_langDir/$userlang"} else {require "$cm_langDir/$cm_langFileName"}

use vsLock;
use vsDB;

# Set file paths
my ($dataFile)      = "$cm_dataDir/$cm_eventsFileName";

# Default to view today unless a date is passed in
my @dateArray = localtime(time);
my ($month) = $input{'vsMonth'} || $dateArray[4]+1;
my ($year) = $input{'vsYear'} || $dateArray[5]+1900;
my ($day) = $input{'vsDay'} || $dateArray[3];
my ($command) = $input{'vsCOM'} || "";
my ($id) = $input{'vsID'} || "";

# Set options based on whether details are showing (large/small calendar view)
my ($showDayDetails) = $input{'vsSD'} || 0;
if ($showDayDetails) {
        $calCellSize    = $cml_cellSize;
        $calBorderStyle = $cml_borderStyle;
} else {
        $calCellSize    = $cms_cellSize;
        $calBorderStyle        = $cms_borderStyle;
}

# Initialize the datafile
my ($objDB) = new vsDB(
        file => $dataFile,
        delimiter => $delimiter,
);

# lock the datafile
my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
if ($cm_useFileLocking) {
   $objLock->lock($dataFile) || die "Couldn't Lock Datafile";
}
if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($dataFile);die;};

## --------- Main Logic --------------
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
if ($cm_useFileLocking) {
        $objLock->unlock($dataFile);
}


# ----------- print everything to the browser ---
$navbar = "&nbsp;$btn{'014'}&nbsp; $cm_title";
print_top();

&PrintDefault;

print_bottom();

# release objs
undef($objDB);
undef($objLock);
undef($objCGI);


# _____________________________________________________________________________
sub PrintDefault {
    print "<table cellspacing='0' cellpadding=10' border='0'><tr valign='top'>\n";
    print "<td>\n";
    print "<font size='2' face='arial,helvetica'>\n";

        # figure out which day to highlight on the calendar
        my ($highlightDate) = $year . "." . $month . "." . $day;

        # figure out following & previous month & year
        my ($nmonth) = $month;
        my ($nyear)  = $year;
        NextMonth(\$nmonth,\$nyear);
        my ($pmonth) = $month;
        my ($pyear)  = $year;
        PreviousMonth(\$pmonth,\$pyear);

        # display the calendar(s)
        &PrintMonth($month,$year,$objDB,$highlightDate);
    if (!$showDayDetails) {
            &PrintMonth($nmonth,$nyear,$objDB,$highlightDate);
    }

    print "</font>\n";
    print "</td><td>\n";
    print "<font size='2' face='arial,helvetica'>\n";

        # show the event details for the day
    &PrintDay($year,$month,$day,$objDB);

    print "<p>\n";
        if ($command eq "EDIT") {
                $objDB->Filter("ID","eq",$id);
                PrintCurrentRecord($objDB);
        } else {
                PrintBlankRecord($objDB);
        }

        # display the navigation
    print "<form><table width='100%' bgcolor='' border='1' cellspacing='0' cellpadding='2'><tr><td align='center'>\n";
    print "<font size='2' face='arial,helvetica'><b>\n";
    print "<a href='$cm_scriptUrl?vsSD=$showDayDetails&vsMonth=$month&vsYear=" . ($year - 1) . "'>&lt;&lt;</a>\n";
    print "&nbsp;<a href='$cm_scriptUrl?vsSD=$showDayDetails&vsMonth=$pmonth&vsYear=$pyear'>&lt;</a>\n";
        print "<select name='month' onchange=\"document.location='$cm_scriptUrl?vsSD=$showDayDetails&' + this.options[this.selectedIndex].value;return true;\">\n";
        print "<option value='vsMonth=$pmonth&vsYear=$pyear'>$pmonth / $pyear</option>\n";
        print "<option value='vsMonth=$month&vsYear=$year' selected>$month / $year</option>\n";
        my ($nM) = $month;
        my ($nY) = $year;
        for (my $count = 1;$count < 12;$count++) {
                NextMonth(\$nM,\$nY);
                print "<option value='vsMonth=$nM&vsYear=$nY'>$nM / $nY</option>\n";
        }
        print "</select>\n";
    print " <a href='$cm_scriptUrl?vsSD=$showDayDetails&vsMonth=$nmonth&vsYear=$nyear'>&gt;</a>\n";
    print "&nbsp;<a href='$cm_scriptUrl?vsSD=$showDayDetails&vsMonth=$month&vsYear=" . ($year + 1) . "'>&gt;&gt;</a>\n";
        print "</b></font>\n";
        print "</td></tr></table></form>";

    print "</font>\n";
    print "</td>\n";
    print "</tr></table>\n";
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

    print "<table border='1' cellspacing='0' cellpadding='2' width='350' bgcolor=''>\n";
    print "<font size='2' face='arial,helvetica'><b>$cal_msg{'003'} $months[$month-1] $day, $year </b></font><br>\n";
    print "<tr><td width='25'>&nbsp;</td>\n";
    print "<td width='75'><font size='2' face='arial,helvetica'><b>$cal_msg{'004'}</b></font></td>\n";
    print "<td width='250'><font size='2' face='arial,helvetica'><b>$cal_msg{'005'}</b></font></td></tr>\n";

    # check for no events found and display message if appropriate
    if ($objMyDb->EOF) {
                print "<tr><td colspan='3'><font size='2' face='arial,helvetica'>$cal_msg{'006'}</font></td></tr>\n";
    }

    # display each event record in table
    while (!$objMyDb->EOF) {
                print "<tr><td><a href='$cm_scriptUrl?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$day&vsID=" . $objMyDb->FieldValue("ID") . "'><img src='$cm_detailIconUrl' border='0'></a></td>";
                print "<td><font size='2' face='arial,helvetica'>" . $objMyDb->FieldValue("TIME") . "&nbsp;</font></td>";
                print "<td><font size='2' face='arial,helvetica'>" . $objMyDb->FieldValue("EVENT") . "&nbsp;</font></td></tr>\n";
                $objMyDb->MoveNext;
    }

    print "</table>\n";
}

# _____________________________________________________________________________
sub PrintMonth {

    my $month = shift || 1;
    my $year = shift || 2001;
    my $objMyDb = shift || return 0;
        # highlightDate is passed in below...

    my ($firstDay,$numDays,$numWeeks) = &GetMonthInfo($month,$year);

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

        # print calendar heading
    print "<p>\n";
    print "<font face='arial,helvetica' size='2' style='$cm_headFontStyle'><b>$months[$month-1] $year</b></font>\n";
        if ($showDayDetails) {
                print " <font size='1'>[<a href='$cm_scriptUrl?vsSD=0&vsMonth=$month&vsYear=$year'>$cal_msg{'002'}</a>]</font>\n"
        } else {
                print " <font size='1'>[<a href='$cm_scriptUrl?vsSD=1&vsMonth=$month&vsYear=$year'>$cal_msg{'001'}</a>]</font>\n"
        }
    print "<table style='$calBorderStyle' border='$calBorderWidth' cellspacing='0'>\n";


    # print the days of the week
    print "<tr>\n";
    foreach $temp (@daysAbbrev) {
                print "<td style='$cm_dayHeadCellStyle'><font face='arial,helvetica' size='2' style='$cm_dayHeadFontStyle'><b>$temp</b></font></td>";
    }
    print "</tr>\n";

    # print the detail section of the calendar
    for (my $cellCount = 1;$cellCount <= $numWeeks; $cellCount++) {
                print "<tr valign='top'>\n";
                foreach $temp (@daysAbbrev) {
                    if (($dayCount > $firstDay-1) && ($weekDayCount < $numDays)) {
                                $weekDayCount++;

                                $thisDate = $year . "." . $month . "." . $weekDayCount;

                                # format cell appropriately based on whether we're processing the highlighted date
                                if ($thisDate eq $highlightDate) {
                                    print "<td width='$calCellSize' height='$calCellSize' style='$cm_selCellStyle'><font face='arial,helvetica' size='2'>";
                                } else {
                                    print "<td width='$calCellSize' height='$calCellSize' style='$cm_stdCellStyle'><font face='arial,helvetica' size='2'>";
                                }

                                # get the style to apply to text for this day
                                if ($thisDate eq $today) {
                                    $style = $cm_todayFontStyle;
                            } elsif ($thisDate eq $highlightDate) {
                                    $style = $cm_selFontStyle;
                                } else {
                                    $style = $cm_stdFontStyle;
                                }

                                # determine if there are any events for this day visible to the current user
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

                            # if events exist that are visible to this user, format font appropriately
                                if ($objMyDb->EOF) {
                                    print "<a style='$style' href='$cm_scriptUrl?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'>$weekDayCount</a><br>";
                                } else {
                                    print "<b><a style='$style' href='$cm_scriptUrl?vsSD=$showDayDetails&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount'>$weekDayCount</a></b><br>";
                                }

                                # show the events for the day if in "Show Details" mode
                                if ($showDayDetails) {
                                    print "<font size='1'>";
                                    while (!$objMyDb->EOF) {
                                                print "<a style='$style' href='$cm_scriptUrl?vsSD=$showDayDetails&vsCOM=EDIT&vsMonth=$month&vsYear=$year&vsDay=$weekDayCount&vsID=" . $objMyDb->FieldValue("ID") . "'>" .$objMyDb->FieldValue("EVENT") . "</a><br>";
                                                $objMyDb->MoveNext;
                                    }
                                    print "</font>";
                                }

                                print "</font></td>\n";
                    } else {
                            # empty cell
                                print "<td style='$cm_emptyCellStyle'><font face='arial,helvetica' size='1'>&nbsp;</font></td>\n";
                    }

                    $dayCount++;
                }
                print "</tr>\n";
    }
    print "</table>\n";
}


# _____________________________________________________________________________
sub GetMonthInfo {

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


#_____________________________________________________________________________
sub PrintCurrentRecord {
        my ($objMyDB) = shift;
        my ($fieldName, $fieldValue);
    my ($recType)   = "New";
    my ($userType)  = "Guest";
    my ($recAccess) = "Read Only";

        if ($objMyDB->FieldValue("ID")) {
                $recType = "Existing";
        }

        if ($username ne $anonuser) {
                if ($access[20] eq "on") { #$settings[7] eq $root) {
                        $userType = "Admin";
                } else {
                        $userType = "Member";
                }
        }

        if ($objMyDB->FieldValue("SOURCE") eq $username || $userType eq "Admin" || $recType eq "New") {
                $recAccess = "Read Write";
        }

if ($username eq $anonuser) {
$recAccess = "Read Only";
}

        if ($recAccess eq "Read Write") {
                print "<form onSubmit='submitonce(this)'  action='$cm_scriptUrl' method='post'>\n";
        }
        print "<p>\n";
        print "<b>$cal_msg{'007'}</b><br>\n";
        print "<table cellspacing='2' cellpadding='2' border='0'>\n";

        foreach $fieldName ($objMyDB->FieldNames) {
                $cleanFieldName = $fieldName;
                $cleanFieldName =~ s/\r//g;

                if ($recAccess eq "Read Only") {
                        if ($cleanFieldName eq "TIME" ||
                            $cleanFieldName eq "EVENT" ||
                            $cleanFieldName eq "DETAILS") {

                                # show record in read-only format (no form)
                            print "<tr valign='top'>\n";
                            print "<td><font face='arial' size='2'>" . $cal_db{$cleanFieldName} . "</font></td>\n";
                            $fieldValue = $objMyDB->FieldValue($fieldName);
                            $fieldValue =~ s/\"/&quot;/g;
                            print "<td>" . $fieldValue . "</td>\n";
                            print "</tr>\n";
                    } elsif ($cleanFieldName eq "WEBSITE") {
                            print "<tr valign='top'>\n";
                            print "<td><font face='arial' size='2'>" . $cal_db{$cleanFieldName} . "</font></td>\n";
                            $fieldValue = $objMyDB->FieldValue($fieldName);
                            $fieldValue =~ s/\"/&quot;/g;
                            print "<td><a href=" . $fieldValue . " target='_blank'>" . $fieldValue . "</a></td>\n";
                            print "</tr>\n";
                    }
            } elsif ($cleanFieldName eq "ID") {
                    print "<input type='hidden' name='vsID' value='" . $objMyDB->FieldValue("ID") . "'>\n";
                } elsif ($cleanFieldName eq "SOURCE") {
                        if ($recType eq "Existing") {
                                # retain original creator of event for existing events
                            print "<input type='hidden' name='SOURCE' value='" . $objMyDB->FieldValue($fieldName) . "'>\n";
                        } else {
                                # save current user as creator of event for new events
                            print "<input type='hidden' name='SOURCE' value='" . $username . "'>\n";
                        }
                } elsif ($cleanFieldName eq "DATE") {
                        if ($recType eq "Existing") {
                                print "<input type='hidden' name='DATE' value='" . $objMyDB->FieldValue("DATE") . "'>\n";
                        }
                } elsif ($cleanFieldName eq "APPROVED") {
                        if ($recType eq "Existing") {
                            if ($userType eq "Admin") {
                                    # allow admins to change approval on existing events
                                    print "<TD>$cal_db{$cleanFieldName}</TD>\n";
                                    print "<TD><select size='1' name='$cleanFieldName'>\n";
                                    if ($objMyDB->FieldValue("APPROVED") == 1) {
                                            print "<option value='1' selected>$cal_opt{'001'}</option>\n";
                                            print "<option value='0'>$cal_opt{'002'}</option>\n";
                                    } else {
                                            print "<option value='1'>$cal_opt{'001'}</option>\n";
                                            print "<option value='0' selected>$cal_opt{'002'}</option>\n";
                                    }
                                    print "</select>\n";
                            } else {
                                    print "<input type='hidden' name='APPROVED' value='" . $objMyDB->FieldValue("APPROVED") . "'>\n";
                            }
                    } else {
                            # auto-approve events entered by the admin
                            if ($userType eq "Admin") {
                                    print "<input type='hidden' name='APPROVED' value='1'>\n";
                            } else {
                                    print "<input type='hidden' name='APPROVED' value='0'>\n";
                            }
                    }
                } elsif ($cleanFieldName eq "OWNER") {
                        if ($userType eq "Guest") {
                                # make all guest events public
                                print "<input type='hidden' name='OWNER' value=\"$cal_msg{'008'}\">\n";
                        } else {
                                # allow the user to select whether the event is public or private
                                print "<tr valign='top'>\n";
                            print "<td><font face='arial' size='2'>" . $cal_db{$cleanFieldName} . "</font></td>\n";
                            $fieldValue = $objMyDB->FieldValue($fieldName);
                                 if ($recType eq "Existing") {
                                         # display owner of existing events - do not allow modification
                                     print "<td>$fieldValue</td>\n";
                                    print "<input type='hidden' name='OWNER' value='" . $objMyDB->FieldValue($fieldName) . "'>\n";
                                } else {
                                        # allow new events to be public or private
                                    if ($userType eq "Admin") {
                                    print "<td><input type='radio' value=\"$cal_msg{'008'}\" name='OWNER' CHECKED>$cal_msg{'008'}";
                                    print "    <input type='radio' value='$username' name='OWNER'>$cal_msg{'018'} $realname</TD>\n";
                                    } else {
                                    print "<TD><input type='radio' value='$username' name='OWNER' CHECKED>$cal_msg{'018'} $realname</TD>\n";
                                    }
                                 }
                                print "</tr>\n";
                        }
                } elsif ($cleanFieldName eq "DETAILS") {
                    print "<tr valign='top'>\n";
                    print "<td><font face='arial' size='2'>" . $cal_db{$cleanFieldName} . "</font></td>\n";
                    print "<td><textarea name='DETAILS' cols='30' rows='3'>";
                    $fieldValue = $objMyDB->FieldValue($fieldName);
                    $fieldValue =~ s/\"/&quot;/g;
                    print $fieldValue . "</textarea></td>\n";
                    print "</tr>\n";
                } else {
                    print "<tr valign='top'>\n";
                    print "<td><font face='arial' size='2'>" . $cal_db{$cleanFieldName} . "</font></td>\n";
                    print "<td><input size=\"40\" name=\"" . $fieldName . "\" value=\"";
                    $fieldValue = $objMyDB->FieldValue($fieldName);
                    $fieldValue =~ s/\"/&quot;/g;
                    print $fieldValue . "\"></td>\n";
                    print "</tr>\n";
                }
        }
         print "</table>\n";
         print "<p>\n";
        if ($recAccess eq "Read Write") {
                print "<input type='hidden' name='vsSD' value='$showDayDetails'>\n";
                print "<input type='hidden' name='vsDay' value='$day'>\n";
                print "<input type='hidden' name='vsMonth' value='$month'>\n";
                print "<input type='hidden' name='vsYear' value='$year'>\n";
                if ($recType  eq "Existing") {
                        print "<input type='hidden' name='vsCOM' value='UPDATE'>\n";
                        print "<input class='button' type='submit' value=\"$cal_btn{'003'}\">\n";
                        print "<input class='button' type='submit' value=\"$cal_btn{'004'}\" onclick=\"if (confirm('".$cal_msg{'009'}."')) {self.location='$cm_scriptUrl?vsSD=$showDayDetails&vsCOM=DELETE&vsMonth=$month&vsYear=$year&vsDay=$day&vsID=" . $objMyDB->FieldValue("ID") . "';return false;} else {return false;};\">\n";
                        print "<input class='button' type='reset' value=\"$cal_btn{'001'}\" onclick=\"window.history.go(-1);return false;\">\n";
                } else {
                        print "<input type='hidden' name='DATE' value='$year.$month.$day'>\n";
                        print "<input type='hidden' name='vsCOM' value='INSERT'>\n";
                        print "<input class='button' type='submit' value=\"$cal_btn{'002'}\">\n";
                        print "<input class='button' type='reset' value=\"$cal_btn{'001'}\" onclick=\"window.history.go(-1);return false;\">\n";
                }
                print "</form>\n";

         }

}

#_____________________________________________________________________________
sub PrintBlankRecord {
        my ($objMyDB) = shift;
        $objMyDB->AddNew;
        PrintCurrentRecord($objMyDB); # this won't be committed, so no big deal
        return 1;
}

#_____________________________________________________________________________
sub UpdateCurrentRecord {
        my ($objMyDB) = shift;
        my ($input) = shift;
        my ($fieldName,$fieldValue);
        foreach $fieldName ($objMyDB->FieldNames) {

                $fieldValue = $input{$fieldName};

                if ($fieldName eq 'APPROVED') {
                        #If this is an approved public event, keep it approved
                        if ($input{'OWNER'} ne $cal_msg{'008'} || $cm_requireAdminApproval == 0) {
                                $fieldValue = '1';
                        } else {
                                $fieldValue = $input{$fieldName};
                        }

                        #Notify admin of new unapproved public event
                        #if ($command eq "INSERT" && $fieldValue eq '0' && $cm_emailAdminNewEventNotice == 1) {
                        #        $subject = "New Event: ".$input{"EVENT"};
                        #        $message  = "A new event has arrived - please review it.\n\n";
                        #        $message .= "Event:                        ".$input{"EVENT"}."\n";
                        #        $message .= "Date:                        ".$input{"DATE"}."\n";
                        #        $message .= "Time:                        ".$input{"TIME"}."\n";
                        #        $message .= "Website:                ".$input{"WEBSITE"}."\n";
                        #        $message .= "Created by:        ".$input{"SOURCE"}."\n";
                        #        $message .= "Details:                ".$input{"DETAILS"}."\n";
                        #        $from = "$webmaster_email (DevDesk Event Manager)";
                        #
                        #        sendemail($cm_eventAdminEmailAddress, $subject, $message, $from);
                        #}
                }

                if ($fieldName eq 'WEBSITE') {
                        #website address must start with http:// - apend it if it isn't there.
                    if ($fieldValue !~ m/^http:\/\//i) {
                            $fieldValue = "http://" . $fieldValue;
                    }
            }

                $objMyDB->FieldValue($fieldName,$fieldValue);
        }
        $objMyDB->Commit;
}

#_____________________________________________________________________________
sub NextMonth {
        #        NextMonth(\$month,\$year);
        #  using slashed passed var by reference and values are modified by the sub
        my ($nMonth) = shift || return 0;
        my ($nYear) = shift || return 0;
        $$nMonth++;
        if ($$nMonth > 12) {
                $$nMonth = 1;
                $$nYear++;
        }
}

#_____________________________________________________________________________
sub PreviousMonth {
        # PreviousMonth(\$month,\$year);
        #  using slashed passed var by reference and values are modified by the sub
        my ($nMonth) = shift || return 0;
        my ($nYear) = shift || return 0;
        $$nMonth--;
        if ($$nMonth < 1) {
                $$nMonth = 12;
                $$nYear--;
        }
}

########################################
# Code to get the data from GET & POST #
########################################
sub parse_form {

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
   @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $input{$name} = $value;
   }
}

1;