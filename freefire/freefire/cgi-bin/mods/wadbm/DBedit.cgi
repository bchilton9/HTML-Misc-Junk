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
# WebAPP DataBase Multiple DBedit.cgi
####################################

if ($lang_support eq "1") { mod_langsupp(); }

$navbar = " $btn{'014'} $dbadmin{'001'}"; 
print_top();
#check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); }#uncomment for admin assistant access#
if ($username ne "admin") { error("$err{'011'}"); }#comment for admin assistant access#
print "<font face='arial' size='2'>
	<table bgcolor='#DDDDDD' border='0' width='100%'><tr><td><b>VerySimple Data Editor</b> <i>modified for WebAPP DB</i></td></tr></table>
	<p>
";


eval 'use vsDB';
eval 'use CGI';

my ($objCGI) = new CGI;
my ($command) = $objCGI->param('vsCOM') || "";
my ($rowNum) = $objCGI->param('vsRN') || "";
my ($fileName) = $objCGI->param('vsFILE') || "";
my ($delimiter) = $objCGI->param('vsDEL') || "";
my ($pageSize) = 10;
my ($activePage) = $objCGI->param('vsAP') || 1;
##added DJF##
my ($newFieldName) = $objCGI->param('vsNewFieldName') || "";
##end add##
my ($scriptName) = $ENV{'SCRIPT_NAME'} || "DBedit.cgi";
my ($filePath) = $ENV{"WADB"} . "/data/" . $fileName;

print "<form onSubmit='submitonce(this)' action='" . $scriptName . "' method='post'>\n";


# default to tab character 
$delimiter = "\t" unless ($delimiter);
my ($objDB) = new vsDB(
	file => $filePath,
	delimiter => $delimiter,
);

if ($fileName) {

	$objDB->Open;

	#$objDB->Sort("ID");
	#$objDB->Commit;

	if ($command eq "EDIT") {
		$objDB->AbsolutePosition($rowNum);
		PrintCurrentRecord($objDB);
	} elsif ($command eq "UPDATE") {
		$objDB->AbsolutePosition($rowNum);
		UpdateCurrentRecord($objDB,$objCGI);
		$objDB->MoveFirst;
		PrintAllRecords($objDB);
	} elsif ($command eq "DELETE") {
		$objDB->AbsolutePosition($rowNum);
		$objDB->Delete;
		$objDB->Commit;
		$objDB->MoveFirst;
		PrintAllRecords($objDB);
	} elsif ($command eq "ADD") {
		PrintBlankRecord($objDB);
	} elsif ($command eq "INSERT") {
		$objDB->AddNew;
		UpdateCurrentRecord($objDB,$objCGI);
		$objDB->MoveFirst;
		PrintAllRecords($objDB);
##added command DJF##
	} elsif ($command eq "NEWFIELDADD") {
	$objDB->AddNewField($newFieldName,$newFieldName);
	UpdateCurrentRecord($objDB,$objCGI);
	#$objDB->MoveFirst;
	PrintAllRecords($objDB);
	}
##end add##
	else {
		PrintAllRecords($objDB);
	}

}

print "<p>\n";
print "<table><tr><td>";
print "<table border='1' cellspacing='1' cellpadding='2'><tr><td><font face='arial,helvetica' size='2'>";
print "<b>File Path:</b> \n";
print $ENV{"WADB"} . "/<input type='text' name='vsFILE' size='30' value='" . $fileName . "'><br>\n";
print "<b>Delimiter:</b> \n";
print "<input type='text' name='vsDEL' size='1' value='" . $delimiter . "'> (default = tab character)<br>\n";
print "<input type='submit' value='Select Data File'>\n";
print "</font></td></tr></table>";
print "</td>";
print "<td>";
print "<table><tr><td>$wadb{'002'}</td></tr></table>";
print "</td></tr></table><br>";
print "<table><tr><td>";
##added form DJF##
	print "<form onSubmit='submitonce(this)' action='" . $scriptName . "' method='post'>\n";
	print "<input type='hidden' name='vsFILE' value='$fileName'>\n";
	print "<input type='hidden' name='vsCOM' value='NEWFIELDADD'>\n";
	print "<input type='text' name='vsNewFieldName' value='$newFieldName'>\n";
	print "<input type='submit' value='Add New Field'>\n";
	print "</form></td><td valign='top'>$wadb{'003'}</td></tr></table>";
##end add##
print "
	</font><p>
	</font>
	";
undef($objDB);
print_bottom();
exit;

#_____________________________________________________________________________
sub PrintAllRecords {
	check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); }
	my ($objMyDB) = shift;
	my ($fieldName);
	my ($count) = 0;

	my (@fieldNames) = ['Code','Category','Description'];

	$objMyDB->ActivePage($activePage);
	
	$activePage = $objMyDB->ActivePage;
	my ($pageCount) = $objMyDB->PageCount;
	
	print "<table cellspacing='2' cellpadding='2' border='0'>\n";
	print "<tr valign='top' bgcolor='#CCCCCC'>\n";
	print "<td>&nbsp;</td>\n";
	foreach $fieldName ($objMyDB->FieldNames) {
		print "<td><b><font face='arial' size='2'>" . $fieldName . "</font></b></td>\n";
	}
	print "</tr>\n";
	while (!$objMyDB->EOF && $count < $pageSize) {
		print "<tr valign='top' bgcolor='#EEEEEE'>\n";
		print "<td><font face='arial' size='1'><a href='" . $scriptName . "?vsFILE=$fileName&vsAP=$activePage&vsDEL=$delimiter&vsCOM=EDIT&vsRN=" . $objMyDB->AbsolutePosition . "'>Edit</a> | <a href='" . $scriptName . "?vsFILE=$fileName&vsDEL=$delimiter&vsAP=$activePage&vsCOM=DELETE&vsRN=" . $objMyDB->AbsolutePosition . "' onclick=\"return confirm('Permenantly delete this record?');\">Delete</a></font></td>\n";
		foreach $fieldName ($objMyDB->FieldNames) {
			print "<td><font face='arial' size='2'>" . $objMyDB->FieldValue($fieldName) . "</font></td>\n";
		}
		print "</tr>\n";
		$objMyDB->MoveNext;
		$count++;
	}	
	print "</table>\n";
	print "<p>\n";

	print "Result Page " . $activePage . " of " . $pageCount;
	if ($activePage > 1) {
		print " <a href='?vsFILE=$fileName&vsDEL=$delimiter&vsAP=" . ($activePage - 1) . "'>Previous</a>";
	}
	if ($activePage < $pageCount) {
		print " <a href='?vsFILE=$fileName&vsDEL=$delimiter&vsAP=" . ($activePage + 1) . "'>Next</a>";
	}
	print " (" . $objMyDB->RecordCount . " Records)\n";
	print "<p>\n";
	print "<b><font face='arial' size='2'><a href='" . $scriptName . "?vsFILE=$fileName&vsDEL=$delimiter&vsAP=$activePage&vsCOM=ADD'>Add New Record</a></font></b>$dbadmin{'009'}\n";
}

#_____________________________________________________________________________
sub PrintCurrentRecord {
	my ($objMyDB) = shift;
	my ($fieldName, $fieldValue);
	print "<table cellspacing='2' cellpadding='2' border='0'>\n";
	foreach $fieldName ($objMyDB->FieldNames) {
		print "<tr valign='top' bgcolor='#DDDDDD'>\n";
		print "<td><font face='arial' size='2'>" . $fieldName . "</font></td>\n";
		print "<td><input size=\"50\" name=\"" . $fieldName . "\" value=\"";

		$fieldValue = $objMyDB->FieldValue($fieldName);
		$fieldValue =~ s/\"/&quot;/g;		

		print $fieldValue . "\"></td>\n";
		print "</tr>\n";
	}
	print "</table>\n";
	print "<p>\n";
	print "<input type='hidden' name='vsRN' value='" . $objMyDB->AbsolutePosition . "'>\n";
	print "<input type='hidden' name='vsCOM' value='UPDATE'>\n";
	print "<input type='hidden' name='vsAP' value='$activePage'>\n";
	print "<input type='submit' value='Update'>\n";
	print "<input type='reset' value='Cancel' onclick=\"window.history.go(-1);return false;\">\n";
}

#_____________________________________________________________________________
sub PrintBlankRecord {
	my ($objMyDB) = shift;
	my ($fieldName);
	print "<table cellspacing='2' cellpadding='2' border='0'>\n";
	foreach $fieldName ($objMyDB->FieldNames) {
		print "<tr valign='top' bgcolor='#DDDDDD'>\n";
		print "<td><font face='arial' size='2'>" . $fieldName . "</font></td>\n";
		print "<td><input size='50' name='" . $fieldName . "' value=''></td>\n";
		print "</tr>\n";
	}
	print "</table>\n";
	print "<p>\n";
	print "<input type='hidden' name='vsCOM' value='INSERT'>\n";
	print "<input type='hidden' name='vsAP' value='$activePage'>\n";
	print "<input type='submit' value='Update'>\n";
	print "<input type='reset' value='Cancel' onclick=\"window.history.go(-1);return false;\">\n";
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
	$objMyDB->Commit;
} 

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

1;

