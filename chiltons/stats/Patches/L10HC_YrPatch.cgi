#!/usr/bin/perl -i

# v3.15 8/26/03

use CGI ':standard';

print header;

require "L10HC_LIB.pl";
	
$acct ='.';
$filePermissions = "755";



	unless (-e "$acct/L10HC_Archive/Doms/Y$curYr2") {mkdir "$acct/L10HC_Archive/Doms/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Refs/Y$curYr2") {mkdir "$acct/L10HC_Archive/Refs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEs/Y$curYr2") {mkdir "$acct/L10HC_Archive/SEs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/KWs/Y$curYr2") {mkdir "$acct/L10HC_Archive/KWs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEKWs/Y$curYr2") {mkdir "$acct/L10HC_Archive/SEKWs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/rTypes/Y$curYr2") {mkdir "$acct/L10HC_Archive/rTypes/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/sRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/sRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/pgRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/pgRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/paRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/paRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Hits/Y$curYr2") {mkdir "$acct/L10HC_Archive/Hits/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Paths/Y$curYr2") {mkdir "$acct/L10HC_Archive/Paths/Y$curYr2", $filePermissions;}
	
print "Patch completed";