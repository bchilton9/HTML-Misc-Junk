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

        require "../data/calendar.cfg";
        require "../../../config.pl";
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

################
# Set file paths
################
my ($cm_eventFile)  = "$cm_dataDir/$cm_eventsFileName";
my ($command)       = $input{'cmCOMMAND'};
my ($action)        = $input{'cmACTION'};

$navbar = "&nbsp;$btn{'014'}&nbsp; $cm_title $cal_msg{'017'}";
print_top();
if ($username ne "admin") { error("$err{'011'}"); }
DisplayNavigation();

# Initialize the datafile
my ($objDB) = new vsDB(
        file => $cm_eventFile,
        delimiter => $delimiter,
);

# lock the datafile
#my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
#if ($cm_useFileLocking) {
#   $objLock->lock($cm_eventFile) || die "Couldn't Lock Datafile";
#}
if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($cm_eventFile);die;};

if ($command eq "SETTINGS") {
        if ($action eq "UPDATE") {SaveSettings();}
        ShowSettings();
} elsif ($command eq "APPROVE") {
        if ($action eq "UPDATE") {ApproveEvents();}
        ShowUnapprovedEvents();
} elsif ($command eq "EVENT_MANAGER") {
        if ($action eq "UPDATE") {UpdateEvents();}
        ShowEventManager();
}

print_bottom();

# unlock the datafile
#if ($cm_useFileLocking) {
#        $objLock->unlock($dataFile);
#}

# release objs
undef($objDB);
undef($objLock);

exit;

sub DisplayNavigation() {
        print qq~
        [<a href="$cm_adminScriptUrl?cmCOMMAND=SETTINGS">$cal_msg{'011'}</a>]&nbsp;
        [<a href="$cm_adminScriptUrl?cmCOMMAND=APPROVE">$cal_msg{'012'}</a>]&nbsp;
        [<a href="$cm_adminScriptUrl?cmCOMMAND=EVENT_MANAGER">$cal_msg{'013'}</a>]<BR><BR>
        ~;
}

sub        ShowSettings() {
        print qq~
        <font size='3' face='arial,helvetica'><B>$cal_msg{'011'}</B></font>
        <form onSubmit="submitonce(this)" action="$cm_adminScriptUrl" method="post">
        <input type="hidden" name="cmCOMMAND" value="SETTINGS">
        <input type="hidden" name="cmACTION" value="UPDATE">
        <table border="0" width="100%" cellpading="0" cellspacing="0">
    <tr><td>$cal_set{'001'}</td><td><input type="text" name="cm_title" value="$cm_title" size="40"></td></tr>
    <tr><td>$cal_set{'002'}</td><td><select size="1" name="cm_requireAdminApproval">
    ~;

    if ($cm_requireAdminApproval == 1) {
            print "<option value='1' selected>Yes</option><option value='0'>No</option></select></td></tr>\n";
    } else {
            print "<option value='1'>Yes</option><option value='0' selected>No</option></select></td></tr>\n";
    }

    print "<tr><td>$cal_set{'003'}</td><td><select size='1' name='cm_emailAdminNewEventNotice'>";
        if ($cm_emailAdminNewEventNotice == 1) {
            print "<option value='1' selected>Yes</option><option value='0'>No</option></select></td></tr>\n";
    } else {
            print "<option value='1'>Yes</option><option value='0' selected>No</option></select></td></tr>\n";
    }

    print qq~
    <tr><td>$cal_set{'004'}</td><td><input type="text" name="cm_eventAdminEmailAddress" value="$cm_eventAdminEmailAddress" size="30"></td></tr>
    <tr><td colspan="2" style="padding-top: 8"><hr><b>$cal_set{'005'}</b></td></tr>
    <tr><td>$cal_set{'006'}</td><td><input type="text" name="cm_scriptDir" value="$cm_scriptDir" size="60"></td></tr>
    <tr><td>$cal_set{'010'}</td><td><input type="text" name="cm_dataDir" value="$cm_dataDir" size="60"></td></tr>
    <tr><td>$cal_set{'007'}</td><td><input type="text" name="cm_langDir" value="$cm_langDir" size="60"></td></tr>
    <tr><td>$cal_set{'008'}</td><td><input type="text" name="cm_scriptUrl" value="$cm_scriptUrl" size="60"></td></tr>
    <tr><td>$cal_set{'009'}</td><td><input type="text" name="cm_adminScriptUrl" value="$cm_adminScriptUrl" size="60"></td></tr>
    <tr><td>$cal_set{'012'}</td><td><input type="text" name="cm_eventsFileName" value="$cm_eventsFileName" size="30"></td></tr>
        <tr><td>$cal_set{'013'}</td><td><input type="text" name="cm_langFileName" value="$cm_langFileName" size="30"></td></tr>
        <tr><td>$cal_set{'014'}</td><td><input type="text" name="cm_detailIconUrl" value="$cm_detailIconUrl" size="30"></td></tr>

        <tr><td colspan="2" style="padding-top: 8"><hr><b>$cal_set{'015'}</b></td></tr>
    <tr><td>$cal_set{'016'}</td><td><input type="text" name="cm_delimiter" value="$cm_delimiter" size="3"></td></tr>
    <tr><td>$cal_set{'017'}</td><td><select size="1" name="cm_useFileLocking">
    ~;
    if ($cm_useFileLocking == 1) {
            print "<option value='1' selected>Yes</option><option value='0'>No</option></select></td></tr>\n";
    } else {
            print "<option value='1'>Yes</option><option value='0' selected>No</option></select></td></tr>\n";
    }

    print qq~
    <tr><td colspan="2" style="padding-top: 8"><hr><b>$cal_set{'018'}&nbsp;</b>$cal_set{'019'}</td></tr>
    <tr><td>$cal_set{'020'}</td><td><input type="text" name="cmsb_cellSize" value="$cmsb_cellSize" size="3"></td></tr>
    <tr><td>$cal_set{'021'}</td><td><input type="text" name="cmsb_borderWidth" value="$cmsb_borderWidth" size="3"></td></tr>
    <tr><td>$cal_set{'022'}</td><td><input type="text" name="cmsb_borderStyle" value="$cmsb_borderStyle" size="60"></td></tr>
    <tr><td>$cal_set{'023'}</td><td><input type="text" name="cmsb_headFontStyle" value="$cmsb_headFontStyle" size="60"></td></tr>
    <tr><td>$cal_set{'024'}</td><td><input type="text" name="cmsb_dayHeadFontStyle" value="$cmsb_dayHeadFontStyle " size="60"></td></tr>
    <tr><td>$cal_set{'025'}</td><td><input type="text" name="cmsb_dayHeadCellStyle" value="$cmsb_dayHeadCellStyle" size="60"></td></tr>
    <tr><td>$cal_set{'026'}</td><td><input type="text" name="cmsb_selFontStyle" value="$cmsb_selFontStyle" size="60"></td></tr>
    <tr><td>$cal_set{'027'}</td><td><input type="text" name="cmsb_selCellStyle" value="$cmsb_selCellStyle " size="60"></td></tr>
    <tr><td>$cal_set{'028'}</td><td><input type="text" name="cmsb_stdFontStyle" value="$cmsb_stdFontStyle" size="60"></td></tr>
    <tr><td>$cal_set{'029'}</td><td><input type="text" name="cmsb_stdCellStyle" value="$cmsb_stdCellStyle" size="60"></td></tr>
    <tr><td>$cal_set{'030'}</td><td><input type="text" name="cmsb_emptyCellStyle" value="$cmsb_emptyCellStyle" size="60"></td></tr>

    <tr><td colspan="2" style="padding-top: 8"><hr><b>$cal_set{'031'}&nbsp; </b>$cal_set{'019'}</td></tr>
    <tr><td>$cal_set{'032'}</td><td><input type="text" name="cml_cellSize" value="$cml_cellSize" size="3"></td></tr>
    <tr><td>$cal_set{'033'}</td><td><input type="text" name="cml_borderWidth" value="$cml_borderWidth" size="3"></td></tr>
    <tr><td>$cal_set{'034'}</td><td><input type="text" name="cml_borderStyle" value="$cml_borderStyle" size="60"></td></tr>
        <tr><td>$cal_set{'035'}</td><td><input type="text" name="cms_cellSize" value="$cms_cellSize" size="3"></td></tr>
        <tr><td>$cal_set{'036'}</td><td><input type="text" name="cms_borderWidth" value="$cms_borderWidth" size="3"></td></tr>
        <tr><td>$cal_set{'037'}</td><td><input type="text" name="cms_borderStyle" value="$cms_borderStyle" size="60"></td></tr>
        <tr><td>$cal_set{'038'}</td><td><input type="text" name="cm_headFontStyle" value="$cm_headFontStyle" size="60"></td></tr>
        <tr><td>$cal_set{'039'}</td><td><input type="text" name="cm_dayHeadFontStyle" value="$cm_dayHeadFontStyle" size="60"></td></tr>
    <tr><td>$cal_set{'040'}</td><td><input type="text" name="cm_dayHeadCellStyle" value="$cm_dayHeadCellStyle" size="60"></td></tr>
        <tr><td>$cal_set{'041'}</td><td><input type="text" name="cm_selFontStyle" value="$cm_selFontStyle" size="60"></td></tr>
        <tr><td>$cal_set{'042'}</td><td><input type="text" name="cm_selCellStyle" value="$cm_selCellStyle" size="60"></td></tr>
        <tr><td>$cal_set{'043'}</td><td><input type="text" name="cm_stdFontStyle" value="$cm_stdFontStyle" size="60"></td></tr>
        <tr><td>$cal_set{'044'}</td><td><input type="text" name="cm_stdCellStyle" value="$cm_stdCellStyle" size="60"></td></tr>
    <tr><td>$cal_set{'045'}</td><td><input type="text" name="cm_todayFontStyle" value="$cm_todayFontStyle" size="60"></td></tr>
        <tr><td>$cal_set{'046'}</td><td><input type="text" name="cm_emptyCellStyle" value="$cm_emptyCellStyle" size="60"></td></tr>
        <BR>
        <tr><td colspan=2 align=center><input type="submit" value="$cal_btn{'003'}"> <input type="reset" value="$cal_btn{'001'}"></td></tr>
        </table>
        </form>

        ~;
}

sub        SaveSettings() {

        $input{'cm_eventAdminEmailAddress'} =~ s/\@/\\@/;

        open(FILE, ">$cm_dataDir/calendar.cfg") || error("$err{'016'} $cm_dataDir/calendar.cfg");
        file_lock(FILE);

        print FILE

        qq~

        #---------------------------------
        # General Settings
        #---------------------------------
        \$cm_title                    = "$input{'cm_title'}";
        \$cm_requireAdminApproval     =  $input{'cm_requireAdminApproval'};
        \$cm_emailAdminNewEventNotice =  $input{'cm_emailAdminNewEventNotice'};
        \$cm_eventAdminEmailAddress   = "$input{'cm_eventAdminEmailAddress'}";

        #---------------------------------
        # Paths & Files
        #---------------------------------
        \$cm_scriptDir           = "$input{'cm_scriptDir'}";
        \$cm_dataDir             = "$input{'cm_dataDir'}";
        \$cm_langDir             = "$input{'cm_langDir'}";
        \$cm_scriptUrl           = "$input{'cm_scriptUrl'}";
        \$cm_adminScriptUrl      = "$input{'cm_adminScriptUrl'}";
        \$cm_eventsFileName      = "$input{'cm_eventsFileName'}";
        \$cm_langFileName        = "$input{'cm_langFileName'}";
        \$cm_detailIconUrl       = "$input{'cm_detailIconUrl'}";

        #---------------------------------
        # Database Settings
        #---------------------------------
        \$cm_delimiter           = "$input{'cm_delimiter'}";
        \$cm_useFileLocking      =  $input{'cm_useFileLocking'};

        #---------------------------------
        # Style Elements
        #---------------------------------
        # Sidebar Calendar
        #---------------------------------
        \$cmsb_cellSize          = "$input{'cmsb_cellSize'}";
        \$cmsb_borderWidth       = "$input{'cmsb_borderWidth'}";
        \$cmsb_borderStyle       = "$input{'cmsb_borderStyle'}";
        \$cmsb_headFontStyle     = "$input{'cmsb_headFontStyle'}";
        \$cmsb_dayHeadFontStyle  = "$input{'cmsb_dayHeadFontStyle'}";
        \$cmsb_dayHeadCellStyle  = "$input{'cmsb_dayHeadCellStyle'}";
        \$cmsb_selFontStyle      = "$input{'cmsb_selFontStyle'}";
        \$cmsb_selCellStyle      = "$input{'cmsb_selCellStyle'}";
        \$cmsb_stdFontStyle      = "$input{'cmsb_stdFontStyle'}";
        \$cmsb_stdCellStyle      = "$input{'cmsb_stdCellStyle'}";
        \$cmsb_emptyCellStyle    = "$input{'cmsb_emptyCellStyle'}";

        #---------------------------------
        # Large Calendar (show detail)
        #---------------------------------
        \$cml_cellSize           = "$input{'cml_cellSize'}";
        \$cml_borderWidth        = "$input{'cml_borderWidth'}";
        \$cml_borderStyle        = "$input{'cml_borderStyle'}";

        #---------------------------------
        # Small Calendar (hide detail)
        #---------------------------------
        \$cms_cellSize           = "$input{'cms_cellSize'}";
        \$cms_borderWidth        = "$input{'cms_borderWidth'}";
        \$cms_borderStyle        = "$input{'cms_borderStyle'}";

        #---------------------------------
        # Large & Small Calendars
        #---------------------------------
        \$cm_headFontStyle       = "$input{'cm_headFontStyle'}";
        \$cm_dayHeadFontStyle    = "$input{'cm_dayHeadFontStyle'}";
        \$cm_dayHeadCellStyle    = "$input{'cm_dayHeadCellStyle'}";
        \$cm_selFontStyle        = "$input{'cm_selFontStyle'}";
        \$cm_selCellStyle        = "$input{'cm_selCellStyle'}";
        \$cm_stdFontStyle        = "$input{'cm_stdFontStyle'}";
        \$cm_stdCellStyle        = "$input{'cm_stdCellStyle'}";
        \$cm_todayFontStyle      = "$input{'cm_todayFontStyle'}";
        \$cm_emptyCellStyle      = "$input{'cm_emptyCellStyle'}";

        1; #return true
        ~;

        unfile_lock(FILE);
        close(FILE);


        $cm_title                    = "$input{'cm_title'}";
        $cm_requireAdminApproval     =  $input{'cm_requireAdminApproval'};
        $cm_emailAdminNewEventNotice =  $input{'cm_emailAdminNewEventNotice'};
        $cm_eventAdminEmailAddress   = "$input{'cm_eventAdminEmailAddress'}";

        $cm_scriptDir           = "$input{'cm_scriptDir'}";
        $cm_dataDir             = "$input{'cm_dataDir'}";
        $cm_langDir             = "$input{'cm_langDir'}";
        $cm_scriptUrl           = "$input{'cm_scriptUrl'}";
        $cm_adminScriptUrl      = "$input{'cm_adminScriptUrl'}";
        $cm_eventsFileName      = "$input{'cm_eventsFileName'}";
        $cm_langFileName        = "$input{'cm_langFileName'}";
        $cm_detailIconUrl       = "$input{'cm_detailIconUrl'}";

        $cm_delimiter           = "$input{'cm_delimiter'}";
        $cm_useFileLocking      =  $input{'cm_useFileLocking'};

        $cmsb_cellSize          = "$input{'cmsb_cellSize'}";
        $cmsb_borderWidth       = "$input{'cmsb_borderWidth'}";
        $cmsb_borderStyle       = "$input{'cmsb_borderStyle'}";
        $cmsb_headFontStyle     = "$input{'cmsb_headFontStyle'}";
        $cmsb_dayHeadFontStyle  = "$input{'cmsb_dayHeadFontStyle'}";
        $cmsb_dayHeadCellStyle  = "$input{'cmsb_dayHeadCellStyle'}";
        $cmsb_selFontStyle      = "$input{'cmsb_selFontStyle'}";
        $cmsb_selCellStyle      = "$input{'cmsb_selCellStyle'}";
        $cmsb_stdFontStyle      = "$input{'cmsb_stdFontStyle'}";
        $cmsb_stdCellStyle      = "$input{'cmsb_stdCellStyle'}";
        $cmsb_emptyCellStyle    = "$input{'cmsb_emptyCellStyle'}";

        $cml_cellSize           = "$input{'cml_cellSize'}";
        $cml_borderWidth        = "$input{'cml_borderWidth'}";
        $cml_borderStyle        = "$input{'cml_borderStyle'}";

        $cms_cellSize           = "$input{'cms_cellSize'}";
        $cms_borderWidth        = "$input{'cms_borderWidth'}";
        $cms_borderStyle        = "$input{'cms_borderStyle'}";

        $cm_headFontStyle       = "$input{'cm_headFontStyle'}";
        $cm_dayHeadFontStyle    = "$input{'cm_dayHeadFontStyle'}";
        $cm_dayHeadCellStyle    = "$input{'cm_dayHeadCellStyle'}";
        $cm_selFontStyle        = "$input{'cm_selFontStyle'}";
        $cm_selCellStyle        = "$input{'cm_selCellStyle'}";
        $cm_stdFontStyle        = "$input{'cm_stdFontStyle'}";
        $cm_stdCellStyle        = "$input{'cm_stdCellStyle'}";
        $cm_todayFontStyle      = "$input{'cm_todayFontStyle'}";
        $cm_emptyCellStyle      = "$input{'cm_emptyCellStyle'}";

}

sub        ShowUnapprovedEvents {

        $objDB->RemoveFilter;
        $objDB->Filter("APPROVED","eq","0");

        print "<font size='3' face='arial,helvetica'><B>$cal_msg{'012'}</B></font><BR>\n";

    # check for no events found and display message if appropriate
    if ($objDB->EOF) {
                print "<font size='2' face='arial,helvetica'>$cal_msg{'015'}</font>\n";
    } else {
                print qq~
                <form onSubmit="submitonce(this)" action="$cm_adminScriptUrl" method="post">
                <input type="hidden" name="cmCOMMAND" value="APPROVE">
                <input type="hidden" name="cmACTION" value="UPDATE">
                <BR><table border=1 cellspacing=0>
                <tr><td><font size='2' face='arial,helvetica'>$cal_opt{'003'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_opt{'004'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'DATE'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'TIME'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'EVENT'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'OWNER'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'SOURCE'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'WEBSITE'}</font></td></tr>
                ~;

            $recNum = 1;

            # display each event record in table
            while (!$objDB->EOF) {
                    print "<tr><td align='center'><input type='checkbox' name='cmAPPROVE-" . $recNum . "' value='" . $objDB->FieldValue("ID") . "'></td>\n";
                    print "<td align='center'><input type='checkbox' name='cmDELETE-" . $recNum . "' value='" . $objDB->FieldValue("ID") . "'></td>\n";
                        print "<td><font size='2' face='arial,helvetica'>".$objDB->FieldValue("DATE")."&nbsp;</font></td>\n";
                        print "<td><font size='2' face='arial,helvetica'>".$objDB->FieldValue("TIME")."&nbsp;</font></td>\n";
                        print "<td><font size='2' face='arial,helvetica'>".$objDB->FieldValue("EVENT")."&nbsp;</font></td>\n";
                        print "<td><font size='2' face='arial,helvetica'>".$objDB->FieldValue("OWNER")."&nbsp;</font></td>\n";
                        print "<td><font size='2' face='arial,helvetica'>".$objDB->FieldValue("SOURCE")."&nbsp;</font></td>\n";
                        print "<td><a href='".$objDB->FieldValue("WEBSITE")."'>".$objDB->FieldValue("WEBSITE")."</a></td></tr>\n";

                        $recNum++;
                        $objDB->MoveNext;
            }

                print "<tr><td colspan=8 align=center><input type='submit' value='".$cal_btn{'006'}."'></td></tr>";
                print "</table></form>";
        }

}

sub        ApproveEvents {

        while (($key, $value) = each(%input)) {
                $objDB->RemoveFilter;
                $objDB->Filter("ID","eq",$value);
                if (substr($key,0,9) eq "cmDELETE-") {
                        $objDB->Delete;
                } elsif (substr($key,0,10) eq "cmAPPROVE-") {
                        $objDB->FieldValue("APPROVED","1");
                }
                $objDB->Commit;
        }
}

sub        ShowEventManager() {

        my @dateArray = localtime(time);
        my ($month) = $input{'cmMonth'} || $dateArray[4]+1;
        my ($year)  = $input{'cmYear'} || $dateArray[5]+1900;

        $objDB->RemoveFilter;
        $objDB->Filter("DATE","like","$year.$month");

        print "<font size='3' face='arial,helvetica'><B>$cal_msg{'013'}</B></font><BR>\n";

        print qq~
        <BR><form onSubmit="submitonce(this)" action="$cm_adminScriptUrl" method="post">
        <input type="hidden" name="cmCOMMAND" value="EVENT_MANAGER">
        <table border=0 cellspacing=3 cellpadding=3>
        <tr>
        <td><font size='2' face='arial,helvetica'>$cal_msg{'014'} </font></td>
        <td><font size='2' face='arial,helvetica'><select size="1" name="cmMonth">
        ~;

        for ($mo = 1;$mo <= 12; $mo++) {
                if ($mo eq $month) {
                        print "<option value='$mo' selected>".@months[$mo - 1]."</option>\n";
                } else {
                        print "<option value='$mo'>".@months[$mo - 1]."</option>\n";
                }
        }
          print "</select><select size='1' name='cmYear'>";

    for ($yr = $dateArray[5]+1900-2;$yr <= $dateArray[5]+1900+2; $yr++) {
            if ($yr eq $year) {
                        print "<option selected>$yr</option>\n";
                } else {
                        print "<option>$yr</option>\n";
                }
        }

        print qq~
        </select></font></td>
        <td><input type='submit' value='$cal_btn{'007'}'></td></form></tr></table></form>
        <br><hr><br>
        ~;

    # check for no events found and display message if appropriate
    if ($objDB->EOF) {
                print "<font size='2' face='arial,helvetica'>$cal_msg{'016'} $month/$year.</font>\n";
    } else {
            print qq~
                <form onSubmit="submitonce(this)" action="$cm_adminScriptUrl" method="post">
                <input type="hidden" name="cmCOMMAND" value="EVENT_MANAGER">
                <input type="hidden" name="cmACTION" value="UPDATE">
                <input type="hidden" name="cmMonth" value="$month">
                <input type="hidden" name="cmYear" value="$year">
                <table border=0 cellspacing=0 cellpadding=2>
                <tr><td><font size='2' face='arial,helvetica'>$cal_db{'DATE'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'TIME'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'EVENT'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'OWNER'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'WEBSITE'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_db{'DETAILS'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_opt{'005'}</font></td>
                <td><font size='2' face='arial,helvetica'>$cal_opt{'004'}</font></td></tr>
                ~;

            $recNum = 1;

            # display each event record in table
            while (!$objDB->EOF) {
                    print "<tr><input type='hidden' name='ID-" . $recNum . "' value='".$objDB->FieldValue("ID")."'>\n";
                        print "<td><input type='text' size='10' name='DATE-" . $recNum . "' value='".$objDB->FieldValue("DATE")."'></td>\n";
                        print "<td><input type='text' size='10' name='TIME-" . $recNum . "' value='".$objDB->FieldValue("TIME")."'></td>\n";
                        print "<td><input type='text' size='40' name='EVENT-" . $recNum . "' value='".$objDB->FieldValue("EVENT")."'></td>\n";
                        print "<td><input type='text' size='40' name='OWNER-" . $recNum . "' value='".$objDB->FieldValue("OWNER")."'></td>\n";
                        print "<td><input type='text' size='40' name='WEBSITE-" . $recNum . "' value='".$objDB->FieldValue("WEBSITE")."'></td>\n";
                        print "<td><textarea cols='30' rows='1' name='DETAILS-" . $recNum . "' value='".$objDB->FieldValue("DETAILS")."'></TEXTAREA></td>\n";
                        print "<td><input type='checkbox' name='APPROVED-" . $recNum . "' value='1'";
                        if ($objDB->FieldValue("APPROVED") eq "1") {
                                print " CHECKED ";
                        }
                        print "></td>\n";
                        print "<td><input type='checkbox' name='DELETE-" . $recNum . "' value='" . $objDB->FieldValue("ID") . "'></td></tr>\n";

                        $recNum++;
                        $objDB->MoveNext;
            }

                print "<input type='hidden' name='cmCOUNT' value='".--$recNum."'>\n";
                print "<tr><td colspan=8 align=center><input type='submit' value='".$cal_btn{'003'}."'> <input type='reset' value='".$cal_btn{'005'}."'></td></tr>\n";
                print "</table></form>\n";
        }

}

sub        UpdateEvents() {


        for ($rec = 1; $rec <= $input{'cmCOUNT'}; $rec++) {
                $id = $input{'ID-'.$rec};
                $objDB->RemoveFilter;
                $objDB->Filter("ID","eq",$id);
                if (exists($input{'DELETE-'.$rec})) {
                        $objDB->Delete;
                } else {
                        $objDB->FieldValue("DATE","$input{'DATE-'.$rec}");
                        $objDB->FieldValue("TIME","$input{'TIME-'.$rec}");
                        $objDB->FieldValue("EVENT","$input{'EVENT-'.$rec}");
                        $objDB->FieldValue("OWNER","$input{'OWNER-'.$rec}");
                        $objDB->FieldValue("DETAILS","$input{'DETAILS-'.$rec}");
                        $objDB->FieldValue("WEBSITE","$input{'WEBSITE-'.$rec}");
                        if (exists($input{'APPROVED-'.$rec})) {
                                $objDB->FieldValue("APPROVED","1");
                        } else {
                                $objDB->FieldValue("APPROVED","0");
                        }
                }
                $objDB->Commit;
        }
        $objDB->RemoveFilter;

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