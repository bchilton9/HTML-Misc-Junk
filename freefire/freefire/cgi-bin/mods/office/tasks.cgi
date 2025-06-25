#!/usr/bin/perl
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

# ----------------------------------------------------------------------------
# Based on tasks.cgi
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
$tab_template = "$dbdir/tasks.tab"; # standard storage file for all tasks
$index_template = "$dbdir/index.html"; # redirector if someone tries to view db files

push(@INC,$scriptdir);
use vsLock;
use vsDB;
use CGI;

$scriptname = "WebOFFICE for WebAPP - Tasks";
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
# getcgi(); # removed since it messes up the office modules; it isn't necessary to use this here
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if ($lang_support eq "1") { mod_langsupp(); } 

if ($username eq $anonuser) { error("$office_error{'001'}"); }

# Member-specific definitions for this module #
$user_dir = "$dbdir/$username";
$data_table = "$user_dir/$username.tasks";
$data_template = "$dbdir/tasks.tab";

# if the date table doesn't exist, create a blank one

unless (-e("$user_dir")) {
	mkdir("$user_dir",0777);
	chmod(0777,"$user_dir");
}

unless (-e("$data_table")) { 
	open (FILE, "<$data_template") || error("$office_error{'002'} $data_template"); 
		file_lock(FILE);
		chomp (@tab = <FILE>);
		unfile_lock(FILE);
	close (FILE);

	open(FILE, ">$data_table") || error("$office_error{'003'} $data_table"); 
		file_lock(FILE);
		foreach $line (@tab) { print FILE "$line"; }
		unfile_lock(FILE);
	close(FILE);
}

# Task defintions / modified from original code

my ($objConfig) = new vsDB(
	file => $office_cfg,
	delimiter => "\t",
);

$objConfig->Open;
my ($headerColor) = $objConfig->FieldValue("HeaderColor");
my ($dataDarkColor) = $objConfig->FieldValue("DataDarkColor");
my ($dataLightColor) = $objConfig->FieldValue("DataLightColor");
$objConfig->Close;
undef($objConfig);

my ($scriptName) = $ENV{'SCRIPT_NAME'} || "tasks.cgi";
my ($objCGI) = new CGI;
my ($command) = $objCGI->param('vsCOM') || "";
my ($showCompleted) = $objCGI->param('vsSC') || 0;
my ($idNum) = $objCGI->param('vsID') || "";
my ($activePage) = $objCGI->param('vsAP') || "1";
my ($sortField) = $objCGI->param('vsSORT') || "";

# grab the display config
open(CFG, "$user_dir/$username.cfg"); 
	file_lock(CFG); 
	chomp(@config = <CFG>); 
	unfile_lock(CFG); 
close(CFG); 

$pageSize = $config[4];
if (($pageSize eq "") || ($pageSize eq "0")) { $pageSize = "100"; }

$navbar = "$office_gen{'023'} <a href=\"$officeURL/index.cgi\">$username\'s Office</a> $office_gen{'023'} $office_task{'001'}";
print_top();

top_navbar_tasks($headerColor);

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
	UpdateCurrentRecord($objDB,$objCGI);
	$objDB->RemoveFilter;
	$objDB->MoveFirst;
	PrintAllRecords($objDB);
} elsif ($command eq "DELETE") {
	$objDB->Filter("ID","eq",$idNum);
	$objDB->Delete;
	$objDB->Commit;
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
	UpdateCurrentRecord($objDB,$objCGI);
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
my ($fieldName, $fieldValue);
my ($count) = 0;

$objMyDB->Sort($sortField) if ($sortField ne "");	
$objMyDB->Filter("Complete","ne","Yes") unless ($showCompleted);

$objMyDB->PageSize($pageSize);
$objMyDB->ActivePage($activePage);
	
my ($pageCount) = $objMyDB->PageCount;
	
print "<table cellspacing='2' cellpadding='2' border='0' width='100%'><tr><td bgcolor='$dataDarkColor' valign='middle'>\n";
print "<input type='submit' value=\"$office_task{'002'}\" class='button' onclick=\"self.location='$scriptName" . PassThrough("vsCOM","ADD") . "';return false\">\n";

if ($showCompleted) {
	print " <input type='submit' class='button' value=\"$office_task{'003'}\" onclick=\"self.location='$scriptName?vsSORT=$sortField';return false\">\n";
} else {
	print " <input type='submit' class='button' value=\"$office_task{'004'}\" onclick=\"self.location='$scriptName?vsSORT=$sortField&vsSC=1';return false\">\n";
}
print "</td></tr></table>\n";

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


print "<p><table cellspacing='2' cellpadding='2' border='0' width='100%'>\n";
print "<tr bgcolor='$dataLightColor'>\n";
print "<td>&nbsp;</td>\n";

# don't change these :)
@showFields = ("Complete", "Description", "AssignedTo", "DueDate");

foreach $fieldName (@showFields) {
	# check for fields, display name based on lang file
	if ($fieldName eq "Complete") { $showfield = "$office_task{'006'}"; }
	elsif ($fieldName eq "Description") { $showfield = "$office_task{'007'}"; }
	elsif ($fieldName eq "DueDate") { $showfield = "$office_task{'008'}"; }
	elsif ($fieldName eq "AssignedTo") { $showfield = "$office_task{'009'}"; }
	elsif ($fieldName eq "Notes") { $showfield = "$office_task{'010'}"; }
	else { $showfield = "" };
	print "<td class=\"newstextsmall\"><b><a href='$scriptName?vsSORT=$fieldName&vsSC=$showCompleted'>" . $showfield . "</a></b></td>\n";
}

	print "</tr>\n";

	while (!$objMyDB->EOF && $count < $pageSize) {
		print "<tr valign='top' bgcolor='$dataLightColor'>\n";
		print "<td><a href='" . $scriptName . "?vsSORT=$sortField&vsAP=$activePage&vsCOM=EDIT&vsID=" . $objMyDB->FieldValue("ID") . "'>";
		print qq~<img src="$imgURL/task.gif" alt="$office_task{'005'}" border="0"></a></td>\n~;
		foreach $fieldName (@showFields) {
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue = "&nbsp;" if ($fieldValue eq "");
			print "<td valign='middle'><font size='1'>$fieldValue</font></td>\n";
		}
		print "</tr>\n";
		$objMyDB->MoveNext;
		$count++;
	}	
	print "</table>\n";

print "<p>\n";

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

}


############################
sub PrintCurrentRecord {
############################

my ($objMyDB) = shift;
my ($fieldName, $fieldValue);

print "<table cellspacing='2' cellpadding='2' border='0'>\n";

foreach $fieldName ($objMyDB->FieldNames) {
	if ($fieldName eq "ID") {
	    print "<input type='hidden' name='vsID' value='" . $objMyDB->FieldValue("ID") . "'>\n";
	} else {
		# have to decipher which field is being displayed, in order to allow for multi-languages
		# not as nice as the original code, but what can ya do?
		if ($fieldName eq "Complete") { $showfield = "$office_task{'006'}"; }
		elsif ($fieldName eq "Description") { $showfield = "$office_task{'007'}"; }
		elsif ($fieldName eq "DueDate") { $showfield = "$office_task{'008'}"; }
		elsif ($fieldName eq "AssignedTo") { $showfield = "$office_task{'009'}"; }
		elsif ($fieldName eq "Notes") { $showfield = "$office_task{'010'}"; }
		else { $showfield = "" };
		
	    print "<tr valign='top' bgcolor='$dataLightColor'>\n";
	    print "<td>" . $showfield . "</td>\n";
		if ($fieldName eq "Complete") {
			my ($yes) = "";
			my ($no) = "";
			$yes = "checked" if ($objMyDB->FieldValue("Complete") eq "Yes");
			$no = "checked" if ($objMyDB->FieldValue("Complete") eq "No");
			print "<td>";
			print "<input type=\"radio\" name=\"Complete\" value=\"Yes\" $yes>Yes\n";
			print "<input type=\"radio\" name=\"Complete\" value=\"No\" $no>No\n";
			print "</td>";
		} elsif ($fieldName eq "Notes") {
			print "<td><textarea name='Notes' cols='38' rows='3'>";
			$fieldValue = $objMyDB->FieldValue("Notes");
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "</textarea></td>\n";
		} else {
			print "<td><input size=\"50\" name=\"" . $fieldName . "\" value=\"";
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue =~ s/\"/&quot;/g;		
			print $fieldValue . "\"></td>\n";
	    }
	    print "</tr>\n";
	}
}
print "</table>\n";
print "<p>\n";

print "<input type='hidden' name='vsSC' value='$showCompleted'>\n";
print "<input type='hidden' name='vsAP' value='$activePage'>\n";
print "<input type='hidden' name='vsSORT' value='$sortField'>\n";

print "<input type='hidden' name='vsCOM' value='UPDATE'>\n";
print "<input type='submit' value=\"$office_gen{'003'}\" class=\"button\">\n";
print "<input style=\"COLOR: FF0000;\" type='reset' value=\"$office_gen{'004'}\" class=\"button\" onclick=\"if (confirm('$office_gen{'007'}')) {self.location='$scriptName?vsSORT=$sortField&vsAP=$activePage&vsSC=$showCompleted&vsCOM=DELETE&vsID=" . $objMyDB->FieldValue("ID") . "';return false;} else {return false;};\">\n";

print "<input type='reset' value=\"$office_gen{'005'}\" class=\"button\" onclick=\"window.history.go(-1);return false;\">\n";
print "<p>\n";

}


############################
sub PrintBlankRecord {
############################

my ($objMyDB) = shift;
my ($fieldName);
print "<table cellspacing='2' cellpadding='2' border='0'>\n";
foreach $fieldName ($objMyDB->FieldNames) {
	if ($fieldName ne "ID") {
		# have to decipher which field is being displayed, in order to allow for multi-languages
		# not as nice as the original code, but what can ya do?
		if ($fieldName eq "Complete") { $showfield = "$office_task{'006'}"; }
		elsif ($fieldName eq "Description") { $showfield = "$office_task{'007'}"; }
		elsif ($fieldName eq "DueDate") { $showfield = "$office_task{'008'}"; }
		elsif ($fieldName eq "AssignedTo") { $showfield = "$office_task{'009'}"; }
		elsif ($fieldName eq "Notes") { $showfield = "$office_task{'010'}"; }
		else { $showfield = "" };
		
		print "<tr valign='top' bgcolor='$dataLightColor'>\n";
		print "<td>$showfield</td>\n";
		if ($fieldName eq "Complete") {
			print "<td>";
			print "<input type=\"radio\" name=\"Complete\" value=\"Yes\">Yes\n";
			print "<input type=\"radio\" name=\"Complete\" value=\"No\" checked>No\n";
			print "</td>";
		} elsif ($fieldName eq "Notes") {
			print "<td><textarea name='Notes' cols='38' rows='3'></textarea></td>\n";
		} else {
			print "<td><input size=\"50\" name=\"" . $fieldName . "\" value=\"\"></td>\n";
	    }
		print "</tr>\n";
	}
}
print "</table>\n";
print "<p>\n";
print "<input type='hidden' name='vsSC' value='$showCompleted'>\n";
print "<input type='hidden' name='vsAP' value='$activePage'>\n";
print "<input type='hidden' name='vsSORT' value='$sortField'>\n";

print "<input type='hidden' name='vsCOM' value='INSERT'>\n";
print "<input type='submit' value=\"$office_gen{'006'}\" class=\"button\">\n";

print "<input type='reset' value=\"$office_gen{'005'}\" class=\"button\" onclick=\"window.history.go(-1);return false;\">\n";
print "<p>\n";

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
