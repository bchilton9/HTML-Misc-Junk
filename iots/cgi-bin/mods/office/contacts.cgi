#!/usr/bin/perl
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

# ----------------------------------------------------------------------------
# Based on contacts.pl - part of the verysimple organizer suite
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
require "../../config.pl"; # main WebAPP config

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

$scriptname = "WebOFFICE for WebAPP - Contacts";
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
# getcgi(); # removed since it messes up this module; it isn't necessary to use this here
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if ($lang_support eq "1") { mod_langsupp(); } 

if ($username eq $anonuser) { error("$office_error{'001'}"); }

# Member-specific definitions for this module #
$user_dir = "$dbdir/$username";
$index_template = "$dbdir/index.html"; # redirector if someone tries to view db files
$data_table = "$user_dir/$username.contacts";
$data_template = "$dbdir/contacts.tab";

# if the date table doesn't exist, create a blank one

unless (-e("$user_dir")) {
	mkdir("$user_dir",0777);
	chmod(0777,"$user_dir");
}

unless (-e("$data_table")) { 
	open (FILE, "<$data_template") || error("$office_error{'002'} $data_template"); 
		lock(FILE);
		chomp (@tab = <FILE>);
		unlock(FILE);
	close (FILE);

	open(FILE, ">$data_table") || error("$office_error{'003'} $data_table"); 
		lock(FILE);
		foreach $line (@tab) { print FILE "$line"; }
		unlock(FILE);
	close(FILE);
}

if ($username eq $anonuser) { error("$office_error{'001'}"); }

my ($objConfig) = new vsDB(
	file => $office_cfg,
	delimiter => "\t",
);

if (!$objConfig->Open) {print $objConfig->LastError; exit 1;};
my ($headerColor) = $objConfig->FieldValue("HeaderColor");
my ($dataDarkColor) = $objConfig->FieldValue("DataDarkColor");
my ($dataLightColor) = $objConfig->FieldValue("DataLightColor");
$objConfig->Close;
undef($objConfig);

# grab the display config
open(CFG, "$user_dir/$username.cfg"); 
	lock(CFG); 
	chomp(@config = <CFG>); 
	unlock(CFG); 
close(CFG); 

$showDetails = "0";

if ($config[0] eq "on") {
	$showDetails = "1";
}

$pageSize = $config[1];
if (($pageSize eq "") || ($pageSize eq "0")) { $pageSize = "100"; }

my ($scriptName) = $ENV{'SCRIPT_NAME'} || "contacts.cgi";
my ($objCGI) = new CGI;
my ($command) = $objCGI->param('vsCOM') || "";
my ($idNum) = $objCGI->param('vsID') || "";
my ($activePage) = $objCGI->param('vsAP') || "1";
my ($sortField) = $objCGI->param('vsSORT') || "LastName";
my ($showAll) = $objCGI->param('vsALL') || 0;
my ($filterField) = $objCGI->param('vsFilterField') || "";
my ($filterValue) = $objCGI->param('vsFilterValue') || "";
# office stuff
my ($display_it) = $objCGI->param('show_on_index') || "";
my ($detail_mode) = $objCGI->param('show_details') || "";

$navbar = "$office_gen{'023'} <a href=\"$officeURL/index.cgi\">$username\'s $office_gen{'002'}</a> $office_gen{'023'} $office_con{'001'}";
print_top();

top_navbar_contacts($headerColor);

print qq~<form action="$scriptName" method="post">~;

my ($objDB) = new vsDB(
	file => $data_table,
	delimiter => "\t",
);

# lock the datafile 
my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
$objLock->lock($data_table) || die("$office_error{'004'} $data_table"); 

if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($data_table);die;};

# so what's next?

if ($command eq "EDIT") {
	$objDB->Filter("ID","eq",$idNum);
	PrintCurrentRecord($objDB);
} elsif ($command eq "UPDATE") {
	$objDB->Filter("ID","eq",$idNum);
	$db_id = $idNum;
	UpdateCurrentRecord($objDB,$objCGI,$db_id);
	$objDB->RemoveFilter;
	$objDB->MoveFirst;
	PrintAllRecords($objDB);
} elsif ($command eq "DELETE") {
	$objDB->Filter("ID","eq",$idNum);
	$objDB->Delete;
	if (!$objDB->Commit) {print "<p><b>" . $objDB->LastError . "</b><p>";};
	$objDB->RemoveFilter;
	$objDB->MoveFirst;
	PrintAllRecords($objDB);
} elsif ($command eq "ADD") {
	PrintBlankRecord($objDB);
} elsif ($command eq "INSERT") {
	$objDB->AddNew;
	my ($newId) = $objDB->Max("ID") || 0;
	$newId = int($newId) + 1;
	$objDB->FieldValue("ID",$newId);
	$db_id = $newId;
	UpdateCurrentRecord($objDB,$objCGI,$db_id);
	$objDB->MoveFirst;
	PrintAllRecords($objDB);
} else {
	PrintAllRecords($objDB);
}

# unlock the datafile
$objLock->unlock($data_table);

bottom_nav();

print_bottom();

undef($objDB);
undef($objLock);
undef($objCGI);


############################
sub PrintAllRecords {
############################

my ($objMyDB) = shift;
my ($fieldName,$fieldValue);
my ($count) = 0;

my ($visiblePageSize) = $pageSize;	
if ($showAll) {$visiblePageSize = 999};

$objMyDB->Sort($sortField);
	
if ($filterField && $filterValue) {
    $objMyDB->Filter($filterField,"like",$filterValue);
}
	
$objMyDB->PageSize($visiblePageSize);
$objMyDB->ActivePage($activePage);
$activePage = $objMyDB->ActivePage; # (in case we specified one out of range) 
	
my ($pageCount) = $objMyDB->PageCount;
	
print qq~
<form action="$scriptName" method="GET">
<table cellspacing="0" cellpadding="2" border="0" width="100%">
<tr>
<td bgcolor="$dataDarkColor" align="left" valign="middle">
~;

if ($showAll) {
	print qq~
	<input type="button" class="button" onclick='window.location="$scriptName?vsALL=0";' value="$pageSize $office_con{'026'}">
	~;
} else {
	print qq~
	<input type="button" class="button" onclick='window.location="$scriptName?vsALL=1";' value="$office_con{'025'} $office_con{'027'}">
	~;
}

print qq~
&nbsp;<input type="button" class="button" onclick='window.location="$scriptName?vsSORT=$sortField&vsAP=$activePage&vsCOM=ADD";' value="$office_con{'028'}"></td>
<td bgcolor="$dataDarkColor" align="right" valign="middle">
<select name="vsFilterField">
<option value="LastName"~;
print " selected" if ($filterField eq "LastName");
print ">$office_con{'003'}</option>\n";
print "<option value='Company'";
print " selected" if ($filterField eq "Company");
print ">$office_con{'005'}</option>\n";
print "<option value='FirstName'";
print " selected" if ($filterField eq "FirstName");
print ">$office_con{'002'}</option>\n";
print qq~
</select>&nbsp;
<b>&nbsp;\~=&nbsp;</b>
<input type="text" size="10" name="vsFilterValue" value="$filterValue">&nbsp;
<input type="submit" class="button" value="$office_gen{'008'}">&nbsp;
~;

if ($filterField && $filterValue) {
    print qq~<input type="submit" class="button" value="$office_gen{'009'}" onclick="this.form.vsFilterValue.value = ''; return true;">~;
}

print qq~
</td></tr></table>
</form>
<p>
~;

@myfields = ("FirstName","LastName","Title","Company","WorkAddress1","WorkAddress2","WorkCity","WorkState","WorkZip","HomeAddress1","HomeAddress2","HomeCity","HomeState","HomeZip","WorkPhone","HomePhone","MobilePhone","Fax","Pager","PrimaryEmail","SecondaryEmail","WebSiteURL","Country","ID","Notes");
@myfewerfields = ("FirstName","LastName","Company","WorkPhone","PrimaryEmail");
@mysortfields = ("FirstName","LastName","Company");

if ($showAll) {
	$display = "$office_con{'037'} $office_con{'027'} $office_gen{'013'}";
} else {
	$display = "$office_con{'037'} $pageSize $office_con{'026'}";
}

print "<center>$office_con{'030'} ";

print "<select name='ap' onchange=\"document.location='" . $scriptName . PassThrough("vsAP") . "' + this.options[this.selectedIndex].value;return true;\">\n";
print "<option value='1'>&nbsp;1&nbsp;</option>";
for (my $x = 1; $x < $pageCount; $x++) {
	print "<option value='" . ($x + 1) . "'";
	print " selected" if ($activePage == ($x + 1));
	print ">&nbsp;" . ($x + 1) . "&nbsp;</option>";
}
print "\n</select>\n";

print " $office_con{'031'} $pageCount";
print " (" . $objMyDB->RecordCount . " $office_gen{'013'}). $display.";
print "<p></center>\n";

if($showDetails == "0") { # don't show detailed cards
	
	print qq~
	<table cellspacing="0" cellpadding="3" border="0" width="100%">
	<tr valign="top" bgcolor="$dataDarkColor">
	<td>&nbsp;</td>
	~;

foreach $fieldName (@myfewerfields) {
	# check for fields, display name based on lang file
	if ($fieldName eq "FirstName") { $showfield = "$office_con{'002'}"; }
	elsif ($fieldName eq "LastName") { $showfield = "$office_con{'003'}"; }
	elsif ($fieldName eq "Company") { $showfield = "$office_con{'005'}"; }
	elsif ($fieldName eq "PrimaryEmail") { $showfield = "$office_con{'021'}"; }
	elsif ($fieldName eq "WorkPhone") { $showfield = "$office_con{'016'}"; }
	elsif ($fieldName eq "HomePhone") { $showfield = "$office_con{'017'}"; }
	elsif ($fieldName eq "WebSiteURL") { $showfield = "$office_con{'023'}"; }
	else { $showfield = ""; }
	print "<td class=\"newstextsmall\"><b><a href='$scriptName?vsALL=$showAll&vsSORT=$fieldName&vsFilterField=$filterField&vsFilterValue=$filterValue'>" . $showfield . "</a></b></td>\n";
}

	print "</tr>\n";

	while (!$objMyDB->EOF && $count < $visiblePageSize) {
		print "<tr valign='top' bgcolor='$dataLightColor'>\n";
		print "<td><a href='" . $scriptName . "?vsAP=$activePage&vsSORT=$sortField&vsCOM=EDIT&vsID=" . $objMyDB->FieldValue("ID") . "'>";
		print qq~<img src="$imgURL/contact.gif" alt="$office_con{'029'}" border="0"></a></td>\n~;
		foreach $fieldName (@myfewerfields) {
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue = "&nbsp;" if ($fieldValue eq "");
			if ($fieldName eq "PrimaryEmail" && $fieldValue ne "&nbsp;") {
				print "<td><font size='1'><a href='mailto:" . $fieldValue . "'>" . $objMyDB->FieldValue($fieldName) . "</a></font></td>\n";
			} else {
				print "<td><font size='1'>" . $fieldValue . "</font></td>\n";
			}
		}
		print "</tr>\n";
		$objMyDB->MoveNext;
		$count++;
	}	
	print "</table>\n";

}
else { # show details

print "<center><font size=\"1\">$office_con{'038'} ";

# the sorter
foreach $fieldName (@mysortfields) {
	if ($fieldName eq "FirstName") { $showfield = "$office_con{'002'}"; }
	elsif ($fieldName eq "LastName") { $showfield = "$office_con{'003'}"; }
	elsif ($fieldName eq "Title") { $showfield = "$office_con{'004'}"; }
	elsif ($fieldName eq "Company") { $showfield = "$office_con{'005'}"; }
	#elsif ($fieldName eq "WorkAddress1") { $showfield = "$office_con{'006'}"; }
	#elsif ($fieldName eq "WorkAddress2") { $showfield = "$office_con{'007'}"; }
	#elsif ($fieldName eq "WorkCity") { $showfield = "$office_con{'008'}"; }
	#elsif ($fieldName eq "WorkState") { $showfield = "$office_con{'009'}"; }
	#elsif ($fieldName eq "WorkZip") { $showfield = "$office_con{'010'}"; }
	#elsif ($fieldName eq "HomeAddress1") { $showfield = "$office_con{'011'}"; }
	#elsif ($fieldName eq "HomeAddress2") { $showfield = "$office_con{'012'}"; }
	#elsif ($fieldName eq "HomeCity") { $showfield = "$office_con{'013'}"; }
	#elsif ($fieldName eq "HomeState") { $showfield = "$office_con{'014'}"; }
	#elsif ($fieldName eq "HomeZip") { $showfield = "$office_con{'015'}"; }
	#elsif ($fieldName eq "WorkPhone") { $showfield = "$office_con{'016'}"; }
	#elsif ($fieldName eq "HomePhone") { $showfield = "$office_con{'017'}"; }
	#elsif ($fieldName eq "MobilePhone") { $showfield = "$office_con{'018'}"; }
	#elsif ($fieldName eq "Fax") { $showfield = "$office_con{'019'}"; }
	#elsif ($fieldName eq "Pager") { $showfield = "$office_con{'020'}"; }
	#elsif ($fieldName eq "PrimaryEmail") { $showfield = "$office_con{'021'}"; }
	#elsif ($fieldName eq "SecondaryEmail") { $showfield = "$office_con{'022'}"; }
	#elsif ($fieldName eq "WebSiteURL") { $showfield = "$office_con{'023'}"; }
	elsif ($fieldName eq "Country") { $showfield = "$office_con{'032'}"; }
	else { $showfield = "" };
	print "<a href='$scriptName?vsALL=$showAll&vsSORT=$fieldName&vsFilterField=$filterField&vsFilterValue=$filterValue'>" . $showfield . "</a> | ";
}

print "</font></center><P>";

while (!$objMyDB->EOF && $count < $visiblePageSize) {
	foreach $fieldName (@myfields) {
		$fieldValue = $objMyDB->FieldValue($fieldName);
		$fieldValue = "&nbsp;" if ($fieldValue eq "");
		
		# push fields into variables for layout
		if ($fieldName eq "FirstName") { $FirstName = $fieldValue; }
		elsif ($fieldName eq "LastName") { $LastName = $fieldValue; }
		elsif ($fieldName eq "Title") { $Title = $fieldValue; }
		elsif ($fieldName eq "Company") { $Company = $fieldValue; }
		elsif ($fieldName eq "WorkAddress1") { $WorkAddress1 = $fieldValue; }
		elsif ($fieldName eq "WorkAddress2") { $WorkAddress2 = $fieldValue; }
		elsif ($fieldName eq "WorkCity") { $WorkCity = $fieldValue; }
		elsif ($fieldName eq "WorkState") { $WorkState = $fieldValue; }
		elsif ($fieldName eq "WorkZip") { $WorkZip = $fieldValue; }
		elsif ($fieldName eq "HomeAddress1") { $HomeAddress1 = $fieldValue; }
		elsif ($fieldName eq "HomeAddress2") { $HomeAddress2 = $fieldValue; }
		elsif ($fieldName eq "HomeCity") { $HomeCity = $fieldValue; }
		elsif ($fieldName eq "HomeState") { $HomeState = $fieldValue; }
		elsif ($fieldName eq "HomeZip") { $HomeZip = $fieldValue; }
		elsif ($fieldName eq "WorkPhone") { $WorkPhone = $fieldValue; $WorkPhoneshowfield = "$office_con{'016'}"; }
		elsif ($fieldName eq "HomePhone") { $HomePhone = $fieldValue; $HomePhoneshowfield = "$office_con{'017'}"; }
		elsif ($fieldName eq "MobilePhone") { $MobilePhone = $fieldValue; $MobilePhoneshowfield = "$office_con{'018'}"; }
		elsif ($fieldName eq "Fax") { $Fax = $fieldValue; $Faxshowfield = "$office_con{'019'}"; }
		elsif ($fieldName eq "Pager") { $Pager = $fieldValue; $Pagershowfield = "$office_con{'020'}"; }
		elsif ($fieldName eq "PrimaryEmail") { $PrimaryEmail = $fieldValue; $PrimaryEmailshowfield = "$office_con{'021'}"; }
		elsif ($fieldName eq "SecondaryEmail") { $SecondaryEmail = $fieldValue; $SecondaryEmailshowfield = "$office_con{'022'}"; }
		elsif ($fieldName eq "WebSiteURL") { $WebSiteURL = $fieldValue; }
		elsif ($fieldName eq "Country") { $Country = $fieldValue; }
		elsif ($fieldName eq "ID") { $ID = $fieldValue; }
		elsif ($fieldName eq "Notes") { $Notes = $fieldValue; }
		else { };
	} 
		print qq~
		<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center">
		<tr>
			<td bgcolor="$dataDarkColor" align="left" valign="middle">&nbsp;<b>$LastName, $FirstName</b></td>
			<td bgcolor="$dataDarkColor" align="right" valign="middle">
				<a href="$this_cgi?vsAP=$activePage&vsSORT=$sortField&vsCOM=EDIT&vsID=$ID">
				<img src="$imgURL/contact.gif" alt="$office_con{'029'}" border="0"></a>&nbsp;</td>
		</tr>
		<tr>
			<td bgcolor="$dataDarkColor" colspan="2">
			<table width="100%" cellpadding="2" cellspacing="1">
			<tr>
				<td bgcolor="$dataLightColor" align="left" valign="top">
				<table cellspacing="0" cellpadding="4" border="0" width="100%">
				<tr><td colspan="4"><b>$Company</b></td></tr>
				<tr>
				    <td valign="top" width="20%">
					<font size="1">
					$WorkAddress1<BR>
					$WorkAddress2<BR>
					$WorkCity&nbsp;$WorkState<BR>
					$WorkZip<BR>$Country
					</font>
					</td>
				    <td valign="top" width="20%">
					<font size="1">$HomeAddress1<BR>
					$HomeAddress2<BR>
					$HomeCity&nbsp;$HomeState<BR>
					$HomeZip<BR>$Country
					</font>
					</td>
				    <td valign="top" width="30%">
					<font size="1">
					<a href="mailto:$PrimaryEmail">$PrimaryEmail</a><BR>
					<a href="mailto:$SecondaryEmail">$SecondaryEmail</a><BR>
					<a href="$WebSiteURL" target="_blank">$WebSiteURL</a></font>
					</td>
				    <td valign="top" width="30%">
					<font size="1">
					$WorkPhoneshowfield: $WorkPhone<BR>
					$HomePhoneshowfield: $HomePhone<BR>
					$MobilePhoneshowfield: $MobilePhone<BR>
					$Faxshowfield: $Fax<BR>
					$Pagershowfield: $Pager</font>
					</td>
				</tr>
				<tr>
				    <td colspan="4"><font size="1">$Notes</font></td>
				</tr>
				</table></td>
			</tr>
			</table></td>
		</tr>
		</table><P>
	~;

	$objMyDB->MoveNext;
	$count++;
}	

} # end show details check

print "<p><center>\n";

print "$office_con{'030'} ";

print "<select name='ap' onchange=\"document.location='" . $scriptName . PassThrough("vsAP") . "' + this.options[this.selectedIndex].value;return true;\">\n";
print "<option value='1'>&nbsp;1&nbsp;</option>";
for (my $x = 1; $x < $pageCount; $x++) {
	print "<option value='" . ($x + 1) . "'";
	print " selected" if ($activePage == ($x + 1));
	print ">&nbsp;" . ($x + 1) . "&nbsp;</option>";
}
print "\n</select>\n";

print " $office_con{'031'} $pageCount";
print " (" . $objMyDB->RecordCount . " $office_gen{'013'}). $display.";
print "<p></center>\n";

}


############################
sub PrintCurrentRecord {
############################

my ($objMyDB) = shift;
my ($fieldName, $fieldValue);

print "<table cellspacing='2' cellpadding='2' border='0' align='center'>\n";

foreach $fieldName ($objMyDB->FieldNames) {
	$fieldValue = $objMyDB->FieldValue($fieldName);
	$fieldValue =~ s/\"/&quot;/g;		
	if ($fieldName eq "ID") {
	    print "<input type='hidden' name='vsID' value='$fieldValue'>\n";
		$thisID = $fieldValue;
	} elsif ($fieldName eq "Notes") {
		print qq~
		<tr valign="top" bgcolor="$dataLightColor">
		<td valign="middle"><b>$office_con{'024'}</b></td>
		<td><textarea cols="38" rows="3" name="$fieldName">$fieldValue</textarea></td>
		</tr>~;
	} else {
		# have to decipher which field is being displayed, in order to allow for multi-languages
		# not as nice as the original code, but what can ya do?
		if ($fieldName eq "FirstName") { $showfield = "$office_con{'002'}"; }
		elsif ($fieldName eq "LastName") { $showfield = "$office_con{'003'}"; }
		elsif ($fieldName eq "Title") { $showfield = "$office_con{'004'}"; }
		elsif ($fieldName eq "Company") { $showfield = "$office_con{'005'}"; }
		elsif ($fieldName eq "WorkAddress1") { $showfield = "$office_con{'006'}"; }
		elsif ($fieldName eq "WorkAddress2") { $showfield = "$office_con{'007'}"; }
		elsif ($fieldName eq "WorkCity") { $showfield = "$office_con{'008'}"; }
		elsif ($fieldName eq "WorkState") { $showfield = "$office_con{'009'}"; }
		elsif ($fieldName eq "WorkZip") { $showfield = "$office_con{'010'}"; }
		elsif ($fieldName eq "HomeAddress1") { $showfield = "$office_con{'011'}"; }
		elsif ($fieldName eq "HomeAddress2") { $showfield = "$office_con{'012'}"; }
		elsif ($fieldName eq "HomeCity") { $showfield = "$office_con{'013'}"; }
		elsif ($fieldName eq "HomeState") { $showfield = "$office_con{'014'}"; }
		elsif ($fieldName eq "HomeZip") { $showfield = "$office_con{'015'}"; }
		elsif ($fieldName eq "WorkPhone") { $showfield = "$office_con{'016'}"; }
		elsif ($fieldName eq "HomePhone") { $showfield = "$office_con{'017'}"; }
		elsif ($fieldName eq "MobilePhone") { $showfield = "$office_con{'018'}"; }
		elsif ($fieldName eq "Fax") { $showfield = "$office_con{'019'}"; }
		elsif ($fieldName eq "Pager") { $showfield = "$office_con{'020'}"; }
		elsif ($fieldName eq "PrimaryEmail") { $showfield = "$office_con{'021'}"; }
		elsif ($fieldName eq "SecondaryEmail") { $showfield = "$office_con{'022'}"; }
		elsif ($fieldName eq "WebSiteURL") { $showfield = "$office_con{'023'}"; }
		elsif ($fieldName eq "Country") { $showfield = "$office_con{'032'}"; }
		else { $showfield = "" };
		print qq~
		<tr bgcolor="$dataLightColor">
		<td valign="middle"><b>$showfield</b></td>
		<td><input size="40" name="$fieldName" value="$fieldValue"></td>
		</tr>
		~;
	}
}

# check to see if this contact is flagged to show on the index page
if (-e("$user_dir/contacts.show")) {
	open(FILE, "$user_dir/contacts.show");
		lock(FILE);
		@entries = <FILE>;
		unlock(FILE);
	close(FILE);
	for ($a = 0; $a < @entries; $a++) {
		chomp($entries);
		($id, $firstn, $lastn, $addy, $phone) = split(/\|/, $entries[$a]);	
		if ($thisID == $id) {
			$show_on_index_checked = "checked"; 
		}
	}
}

# print the switch
print qq~
<tr bgcolor="$dataLightColor">
	<td align="right"><input type="checkbox" name="show_on_index" $show_on_index_checked></td>
	<td valign="middle"><b>$office_con{'033'}</b></td>
</tr>
~;

print qq~
</table><p>
<input type="hidden" name="vsALL" value="$showAll">
<input type="hidden" name="vsAP" value="$activePage">
<input type="hidden" name="vsSORT" value="$sortField">
~;

# office stuff
print qq~
<input type="hidden" name="the_lastname" value="$lastname">
<input type="hidden" name="the_firstname" value="$firstname">
<input type="hidden" name="the_email" value="$email">
~;

if ($objMyDB->FieldValue("ID")) {
	print qq~
	<input type="hidden" name="vsCOM" value="UPDATE">
	<input type="submit" value="$office_gen{'003'}" class="button">~;
	print "<input style=\"COLOR: FF0000;\" type='reset' class='button' value=\"$office_gen{'004'}\" onclick=\"if (confirm('$office_gen{'007'}')) {self.location='$scriptName?vsSORT=$sortField&vsAP=$activePage&vsALL=$showAll&vsCOM=DELETE&vsID=" . $objMyDB->FieldValue("ID") . "';return false;} else {return false;};\">\n";
} else {
	print qq~
	<input type="hidden" name="vsCOM" value="INSERT">
	<input type="submit" value="$office_gen{'006'}" class="button">
	~;
}

print qq~
<input type="reset" value="$office_gen{'005'}" class="button" onclick="window.history.go(-1);return false;"><p>
~;

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
my ($db_id) = shift;

my ($fieldName,$fieldValue);
foreach $fieldName ($objMyDB->FieldNames) {
	$fieldValue = $objMyCGI->param($fieldName);
	$objMyDB->FieldValue($fieldName,$fieldValue);
	if ($fieldName eq "FirstName") {
		$db_firstname = $fieldValue;
	}
	elsif ($fieldName eq "LastName") {
		$db_lastname = $fieldValue;
	}
	elsif ($fieldName eq "PrimaryEmail") {
		$db_email = $fieldValue;
	}
	elsif ($fieldName eq "WorkPhone") {
		$db_wphone = $fieldValue;
	}
	else {}
}

if ($display_it eq "on") {
	open (FILE, "<$user_dir/contacts.show");
		lock(FILE);
		@showus = <FILE>;
		unlock(FILE);
	close (FILE);
	
	open (FILE, ">$user_dir/contacts.show");
		lock(FILE);
		$islisted = 0;
		# fix 2 Nov 2002
		for ($a = 0; $a < @showus; $a++) {
			($sid, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $showus[$a]);
			if ($db_id =~ /$sid/) {
				$islisted = 1;
			}
		}
		# end fix
		print FILE "$db_id|$db_firstname|$db_lastname|$db_email|$db_wphone\n" unless $islisted == 1;
		foreach $contact (@showus) { print FILE "$contact"; }
		unlock(FILE);
	close(FILE);
}
else { # make sure it doesn't appear in the list
	open (FILE, "<$user_dir/contacts.show");
		lock(FILE);
		@showus = <FILE>;
		unlock(FILE);
	close (FILE);
	
	open (FILE, ">$user_dir/contacts.show");
		lock(FILE);
		for ($a = 0; $a < @showus; $a++) {
			($sid, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $showus[$a]);
			if(!($db_id =~ /$sid/)) { 
					print FILE "$showus[$a]"; 
			}
			else { 
			}
		}
		unlock(FILE);
	close(FILE);
}

if (!$objMyDB->Commit) {print "<p><b>" . $objMyDB->LastError . "</b><p>";};

}


############################
sub PassThrough {
############################

my ($fieldName) = shift || return '';
my ($fieldValue) = shift || "";
my (@params) = $objCGI->param;
my ($appendChar) = "?";
my ($param);
my ($queryString);
my ($val);
foreach $param (@params) {
	unless ($fieldName eq $param) {
		$val = $objCGI->param($param) || "";
		$val =~s/([^a-zA-Z0-9_\-.])/uc sprintf("%%%02x",ord($1))/eg;
		$queryString .= $appendChar . $param . "=" . $val;
		$appendChar = "&";
	}
}		
$queryString .= $appendChar . $fieldName . "=" . $fieldValue;
return $queryString;	

}


1; # return true

