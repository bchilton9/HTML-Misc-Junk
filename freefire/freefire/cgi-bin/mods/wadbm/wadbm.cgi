#!/usr/bin/perl -w
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
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
#  									      #
# WebAPP Database Multiple is modified to this purpose by DavidF from original#
# code by Jason M. Hinkle. 						      #
# For more information see: http://www.verysimple.com/scripts/                #
#                                                                             #
# File: Last modified: 04/15/03                                               #
###############################################################################
###############################################################################

require "../../config.pl"; # main WebAPP config

$scriptname = "WebAPP";
$scriptver = "0.9.5";
$wadbmbuild = "Beta 0.6";

eval {
	require "../../config.pl";
	require "$sourcedir/subs.pl";
	require "config.dat";
	
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

getlanguage();
ban();
#getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

# do not modify anything below this line unless you know what you are doing!

$wadbDIR = "$mods_dir/wadbm";
$ENV{"WADB"} = "$wadbDIR";
push(@INC,$scriptdir);

####################################
# A Wonderful Mod by Me!
####################################

if ($lang_support eq "1") { mod_langsupp(); }

# Start making your changes here! #

use vsLock;
use vsDB;
use CGI;


my ($objCGI) = new CGI;
my ($command) = $objCGI->param('vsCOM') || "";
my ($idNum) = $objCGI->param('vsID') || "";
my ($fileName) = $objCGI->param('vsFILE') || "";
my ($scriptName) = $ENV{'SCRIPT_NAME'} || "wadbm.cgi";
my ($filePath) = $ENV{"WADB"} . "/data/" . $fileName . ".dat";
my ($showCompleted) = $objCGI->param('vsSC') || 0;
my ($activePage) = $objCGI->param('vsAP') || "1";
my ($sortField) = $objCGI->param('vsSORT') || "Date";
my ($showAll) = $objCGI->param('vsALL') || 0;
my ($filterField) = $objCGI->param('vsFilterField') || "";
my ($filterValue) = $objCGI->param('vsFilterValue') || "";
my ($newFieldName) = $objCGI->param('vsNewFieldName') || "";


$configFile = "$wadbDIR/data/$fileName.cfg";

# --- get the configuration settings 
my ($objConfig) = new vsDB(
	file => $configFile,
	delimiter => "\t",
);
if (!$objConfig->Open) {print $objConfig->LastError; exit 1;};
my ($title) = $objConfig->FieldValue("Title");
my ($bodyTag) = $objConfig->FieldValue("BodyTag");
my ($headerColor) = $objConfig->FieldValue("HeaderColor");
my ($dataDarkColor) = $objConfig->FieldValue("DataDarkColor");
my ($dataLightColor) = $objConfig->FieldValue("DataLightColor");
my ($detailIcon) = $objConfig->FieldValue("DetailIcon");
my (@showFields) = split(",",$objConfig->FieldValue("ShowFields"));
my ($delimiter) = $objConfig->FieldValue("Delimiter") || "\t";
my ($pageSize) = $objConfig->FieldValue("PageSize") || "10";
my ($useFileLocking) = $objConfig->FieldValue("UseFileLocking") || 1;

$objConfig->Close;
undef($objConfig);
# -- end config

$navbar = " $btn{'014'} $webappdb{'001'} $title"; 
print_top();

print "<table bgcolor='$headerColor' border='0' width='100%'><tr><td><b>$title</b></td></tr></table><p>";
print "<form onSubmit='submitonce(this)' action='" . $scriptName . "' method='post'>\n";

my ($objDB) = new vsDB(
	file => $filePath,
	delimiter => $delimiter,
);

# lock the datafile	
my ($objLock) = new vsLock(-warn => 1, -max => 5, delay => 1);
if ($useFileLocking) {
    $objLock->lock($filePath) || die "Couldn't Lock config $filePath Datafile";
}

if (!$objDB->Open) {print $objDB->LastError;$objLock->unlock($filePath);exit 1;};

# --------- Main Logic --------------

if ($fileName) {
if ($command eq "EDIT") {
	$objDB->Filter("ID","eq",$idNum);
	PrintCurrentRecord($objDB);
} elsif ($command eq "UPDATE") {
	$objDB->Filter("ID","eq",$idNum);
	#$objDB->CR ("<BR>");
	UpdateCurrentRecord($objDB,$objCGI);
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
	UpdateCurrentRecord($objDB,$objCGI);
	$objDB->MoveFirst;
	PrintAllRecords($objDB);
} elsif ($command eq "NEWFIELDADD") {
	$objDB->AddNewField($newFieldName,$newFieldName);
	UpdateCurrentRecord($objDB,$objCGI);
	#$objDB->MoveFirst;
	PrintAllRecords($objDB);
} else {
	PrintAllRecords($objDB);
}
}

if ($useFileLocking) {
    $objLock->unlock($filePath);
}

print "</form>";

print_bottom();

undef($objDB);
undef($objLock);
undef($objCGI);

#_____________________________________________________________________________
sub PrintAllRecords {
	my ($objMyDB) = shift;
	my ($fieldName,$fieldValue);
	my ($count) = 0;

	my ($visiblePageSize) = $pageSize;	
	if ($showAll) {$visiblePageSize = 999};

	$objMyDB->Sort($sortField);
	$objMyDB->Filter("Complete","ne","Yes") unless ($showCompleted);
	
	if ($filterField && $filterValue) {
	    $objMyDB->Filter($filterField,"like",$filterValue);
	}
	$objMyDB->AddNewField($newFieldName);
	$objMyDB->PageSize($visiblePageSize);
	$objMyDB->ActivePage($activePage);
	$activePage = $objMyDB->ActivePage; # (in case we specified one out of range) 
	
	my ($pageCount) = $objMyDB->PageCount;
	
	
	#print "<form onSubmit="submitonce(this)" action='$scriptName' method='GET'>\n";
	print "<table cellspacing='2' cellpadding='2' border='0'><tr valign='middle'><td bgcolor='$dataDarkColor'>\n";
	if ($showAll) {
		print "<input type='button' onclick=\"window.location='$scriptName?vsFILE=$fileName&vsALL=0';\" value='Show $pageSize Per Page'>";
	} else {
		print "<input type='button' onclick=\"window.location='$scriptName?vsFILE=$fileName&vsALL=1';\" value='Show All'>";
	}
	#if ($showCompleted) {
	#	print " <input type='submit' value='Hide Completed' onclick=\"self.location='$scriptName?vsFILE=$fileName&vsSORT=$sortField';return false\">\n";
	#} else {
	#	print " <input type='submit' value='Show Completed' onclick=\"self.location='$scriptName?vsFILE=$fileName&vsSORT=$sortField&vsSC=1';return false\">\n";
	#}
	check_access(editcats); if ($access_granted eq "1") {
		print " <input type='button' onclick=\"window.location='$scriptName?vsFILE=$fileName&vsSORT=$sortField&vsAP=$activePage&vsCOM=ADD';\" value='New Record'>\n";
	} else {
		print "&nbsp;\n";
		print "&nbsp;\n";
	}
	print "</td><td>\n";
	print "</td><td bgcolor='$dataDarkColor'>\n";
	print "<input type='hidden' name='vsFILE' value='$fileName'>\n";
	print "<select name='vsFilterField'>\n";
	foreach $fieldName (@showFields) {
		print "<option value=$fieldName";
		print " selected" if ($filterField eq "$fieldName");
		print ">$fieldName</option>\n";
	}
	print "</select>&nbsp;";
	print "<font face='Arial,Helvetica' size='2'><b>&nbsp;~=&nbsp;</b></font>\n";
	print "<input type='text' size='10' name='vsFilterValue' value='$filterValue'>&nbsp;";
	print "<input type='submit' value='Search'>&nbsp;";
	if ($filterField && $filterValue) {
	    print "<input type='submit' value='Clear' onclick=\"this.form.vsFilterValue.value = ''; return true;\">";
	}
	print "</td></tr></table>\n";
	print "</form>\n";

	print "<p>\n";
	print "<table bgcolor='#000000' cellspacing='1' cellpadding='2' width='100%' border='0'>\n";
	print "<tr valign='top' bgcolor='#CCCCCC'>\n";
	print "<td>&nbsp;</td>\n";
	foreach $fieldName (@showFields) {
		print "<td><b><font face='arial' size='2'><a href='$scriptName?vsFILE=$fileName&vsALL=$showAll&vsSORT=$fieldName&vsFilterField=$filterField&vsFilterValue=$filterValue' title='Sort by $fieldName'>" . $fieldName . "</a></font></b></td>\n";
	}
	print "</tr>\n";
$windowbg2 = "#E9F9FF";
$windowbg3 = "#FFFFFF";
$second = "$windowbg2";
	while (!$objMyDB->EOF && $count < $visiblePageSize) {
		print "<tr valign='top' bgcolor='$second'>\n";
	if ($second eq "$windowbg2") { $second="$windowbg3"; }
		else { $second="$windowbg2"; }
		print "<td><font face='arial' size='1'><a href='" . $scriptName . "?vsFILE=$fileName&vsAP=$activePage&vsSORT=$sortField&vsCOM=EDIT&vsID=" . $objMyDB->FieldValue("ID") . "'><img src='$detailIcon' alt='Details' border='0'></a></font></td>\n";
		foreach $fieldName (@showFields) {
			$fieldValue = $objMyDB->FieldValue($fieldName);
			$fieldValue = "&nbsp;" if ($fieldValue eq "");
			if ($fieldName eq "Contact" && $fieldValue ne "&nbsp;") {
				print "<td><font face='arial' size='2'><a href='mailto:" . $fieldValue . "'>" . $objMyDB->FieldValue($fieldName) . "</a></font></td>\n";
			} else {
				print "<td><font face='arial' size='2'>" . $fieldValue . "</font></td>\n";
			}
		}
		print "</tr>\n";
		$objMyDB->MoveNext;
		$count++;
	}	
	print "</table>\n";
	print "<p>\n";

	print "Result Page ";

	print "<select name='ap' onchange=\"document.location='" . $scriptName . PassThrough("vsAP") . "' + this.options[this.selectedIndex].value;return true;\">\n";
	print "<option value='1'>1</option>";
	for (my $x = 1; $x < $pageCount; $x++) {
		print "<option value='" . ($x + 1) . "'";
		print " selected" if ($activePage == ($x + 1));
		print ">" . ($x + 1) . "</option>";
	}
	print "\n</select>\n";
	
	print " of $pageCount";
	print " (" . $objMyDB->RecordCount . " Records)";
	print "<p>\n";

}

#_____________________________________________________________________________
sub PrintCurrentRecord {
	my ($objMyDB) = shift;
	my ($fieldName, $fieldValue);
	check_access(editcats); if ($access_granted eq "1") {
	print "<table cellspacing='2' cellpadding='2' border='0'>\n";
	foreach $fieldName ($objMyDB->FieldNames) {
		$fieldValue = $objMyDB->FieldValue($fieldName);
		$fieldValue =~ s/\"/&quot;/g;		
		if ($fieldName eq "ID") {
		    print "<input type='hidden' name='vsID' value='$fieldValue'>\n";
		} else {
		    print "<tr valign='top' bgcolor='$dataLightColor'>\n";
		    print "<td><font face='arial' size='2'>$fieldName</font></td>\n";
		    print "<td><textarea cols=\"50\" rows='3' name=\"$fieldName\">$fieldValue</textarea></td>\n";
		    print "</tr>\n";
		} 
	}
	print "</table>\n";
	print "<p>\n";
	print "<input type='hidden' name='vsALL' value='$showAll'>\n";
	print "<input type='hidden' name='vsAP' value='$activePage'>\n";
	print "<input type='hidden' name='vsSORT' value='$sortField'>\n";
	print "<input type='hidden' name='vsFILE' value='$fileName'>\n";

	
		if ($objMyDB->FieldValue("ID")) {
			print "<input type='hidden' name='vsCOM' value='UPDATE'>\n";
			print "<input type='submit' value='Update'>\n";
			print "<input style=\"COLOR: maroon;\" type='reset' value='Delete'  onclick=\"if (confirm('Permanently delete this record?')) {self.location='$scriptName?vsFILE=$fileName&vsSORT=$sortField&vsAP=$activePage&vsALL=$showAll&vsCOM=DELETE&vsID=" . $objMyDB->FieldValue("ID") . "';return false;} else {return false;};\">\n";
		} else {
			print "<input type='hidden' name='vsCOM' value='INSERT'>\n";
			print "<input type='submit' value='Add'>\n";
		}

	print "<input type='reset' value='Cancel' onclick=\"window.history.go(-1);return false;\">\n";
	print "<p></form>\n";
	if ($username eq admin) {
	print "<form onSubmit='submitonce(this)' action='" . $scriptName . "' method='post'>\n";
	print "<input type='hidden' name='vsFILE' value='$fileName'>\n";
	print "<input type='hidden' name='vsCOM' value='NEWFIELDADD'>\n";
	print "<input type='text' name='vsNewFieldName' value='$newFieldName'>\n";
	print "<input type='submit' value='Add New Field'>\n";
	}
	} else { 
	print "<table cellspacing='2' cellpadding='5' border='0'>\n";
	foreach $fieldName ($objMyDB->FieldNames) {
		$fieldValue = $objMyDB->FieldValue($fieldName);
		$fieldValue =~ s/\"/&quot;/g;		
		if ($fieldName eq "ID") {
		    print "<input type='hidden' name='vsID' value='$fieldValue'>\n";
		} else {
		    print "<tr valign='top'>\n";
		    print "<td class='cat'><font face='arial' size='3'>$fieldName:</font></td>\n";
		    print "<td class='cat'><font face='arial' size='2'>$fieldValue</td>\n";
		    print "</tr>\n";
		} 
	}
	print "</table>\n"; 
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
    my ($objMyCGI) = shift;
    my ($fieldName,$fieldValue);
    foreach $fieldName ($objMyDB->FieldNames) {
	$fieldValue = $objMyCGI->param($fieldName);
	$objMyDB->FieldValue($fieldName,$fieldValue);
    }
    if (!$objMyDB->Commit) {print "<p><b>" . $objMyDB->LastError . "</b><p>";};
}

#_____________________________________________________________________________
sub PassThrough {
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

# Finish making your changes here! #

###########################
sub mod_langsupp {
###########################

$modlangfail = "0";

if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat");
		file_lock(FILE);
		@settings = <FILE>;
		unfile_lock(FILE);
		close(FILE);

		for( $i = 0; $i < @settings; $i++ ) {
			$settings[$i] =~ s~[\n\r]~~g;
		}
		
		if ($settings[0] ne $password && $action ne "logout") { error("$err{'002'}"); }
		else {
			$realname = $settings[1];
			$realemail = $settings[2];
			$userlang = $settings[15];
		}
		
}

		if ($userlang eq "") { $userlang = $language; }
						
			 if ($modlangfail ne "1") {
			 @modlanguage = $userlang;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
			 } else {
			 @modlanguage = $language;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
		}

eval {
	require "language/$modlang.dat";
	
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};

if ($@) {$modlangfail = "1"; mod_langsuppfail();}

}

########################
sub mod_langsuppfail {
########################

eval {
	require "language/$mod_lang";
	
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

}
}

1;

