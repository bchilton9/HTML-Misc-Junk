#!/usr/bin/perl
###############################################################################
###############################################################################
# admin.cgi for User Gallery                                                  #
# Copyright (C) 2002 by Floyd (webmaster@diminishedresponsibility.co.uk)      #
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
#                                                                             #
# v1.0 - First Release. 21st October 2002                                     #
# v1.1 - Bug Fixes and Security Update. 23rd October 2002                     #
# v1.2 - Upload Script Improvements. (NB: NOT RELEASED)                       #
# v1.3 - Picture Views now Counted. (NB: NOT RELEASED)                        #
# v1.4 - Bug Fixes and Further Uploader Improvements. (NB: NOT RELEASED)      #
# v1.5 - New and Hot Pictures Noted. Final Code Tweeks. 12th December 2002    #
#                                                                             #
# NOTE: THIS WILL BE THE LAST UPDATE OF USER GALLERY AS A STAND ALONE MOD.    #
# FURTHER DEVELOPMENT WILL BE VIA THE G.O.M.E.S SYSTEM.                       #
#                                                                             #
# Last Modified: 12/11/02                                                     #
###############################################################################

$| = 1;

use CGI::Carp qw(fatalsToBrowser);
use File::Copy;

### the following must be correct or else this script won't work ###
require "../../../config.pl"; # WebAPP config
require "../usergallery.cfg"; # User Gallery config
require "./ugsetup.dat"; # User Gallery settings
######

# do not modify anything below this line unless you know what you are doing!

eval {
	require "$sourcedir/subs.pl";
	require "$usergallerydir/language/english.dat";
	require "$usergallerydir/ugplugin.pl";

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
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

# Compatability Checks #
if ($shownewalbum eq "") {$shownewalbum = "0";}
if ($shownewpicture eq "") {$shownewpicture = "0";}
if ($showhotpicture eq "") {$showhotpicture = "0";}
if ($approvalaccess eq "") {$approvalaccess = "0";}
########################

# User Gallery Mod by Floyd #

ugadminplugin1(); exit;

################ 
sub doorway { 
################ 

if ($settings[7] ne "$root") { error("$err{'011'}"); } 

$navbar = "$btn{'014'} $ugadmin{'001'}";
print_top(); 

print qq~ 
<a href="$usergalleryadminurl/admin.cgi?op=verifypictures">$ugadmin{'002'}</a>~; if ($username eq "admin") {print qq~&nbsp;-&nbsp;<a href="$usergalleryadminurl/admin.cgi?op=viewfailed">$ugadmin{'032'}</a>&nbsp;-&nbsp;<a href="$usergalleryadminurl/admin.cgi?op=setup">$ugadmin{'003'}</a>~;}

print qq~<br><br>
<a href="$usergalleryurl/index.cgi">$ugadmin{'004'}</a>
<br> 
~;
print_bottom(); 
exit; 
} 


################ 
sub verifypictures { 
################
if ($settings[7] ne "$root") { error("$err{'011'}"); }
 
	if ($approvalaccess eq "0") {
		 if ($username ne "admin") { error("$err{'011'}"); }
	}
	
	open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat"); 
	file_lock(FILE); 
	@categories = <FILE>; 
	unfile_lock(FILE); 
	close(FILE); 
 
		open (FILE, "<$usergallerydb/newugs.dat") || error("$soserror{'001'} $usergallerydb/newugs.dat");
			file_lock(FILE);
			@newugs = <FILE>;
			unfile_lock(FILE);
		close (FILE);

	($num, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $newugs[0]); 
	$num++; 
		
		if ($postnum eq 0) {$postnum = 1;} 
 
	for ($a = 0; $a < @newugs; $a++) { 
		($num[$a], $album[$a], $sendername[$a], $picturename[$a], $filename[$a], $adddate[$a]) = split(/\|/, $newugs[$a]); 
	} 
 
	$navbar = "$btn{'014'} $ugadmin{'001'} $btn{'014'} $ugadmin{'002'}";
	print_top(); 
 
	if (@newugs == 0) { print qq~$ugadmin{'005'}<br><br><a href="$usergalleryadminurl/admin.cgi">$ugadmin{'006'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi">$ugadmin{'004'}</a><br>~; } 
	else { 
		print qq~
		<table border="0" cellpadding="5" cellspacing="0" width="100%"> 
		<tr> 
			<td align="center"><b>$ugadmin{'007'}</b></td>
		</tr> 
		</table> 
~; 
		if ($info{'start'} eq "") { $start = 0; } 
		else { $start = "$info{'start'}"; }
		
		$numshown = 0; 
		for ($b = 0; $b < @newugs; $b++) { 
			$numshown++; 
 			
			print qq~
			<form onSubmit="submitonce(this)" action="$usergalleryadminurl/admin.cgi?op=verifypictures2&amp;num=$num[$b]" method="post">
			<table border="0" cellpadding="5" cellspacing="0" width="100%" align="center"> 
			<tr> 
				<td align="center">$ugadmin{'008'}<br>$sendername[$b]</td> 
			</tr>
			<tr> 
				<td align="center">$ugadmin{'009'}<br><input type="text" name="description" size="20" maxlength="20" value="$picturename[$b]"></td> 
			</tr>~;
			
		foreach $acurcat (@categories) {
			$acurcat =~ s/[\n\r]//g;
			@acitem = split(/\|/, $acurcat);
			if($acitem[0] eq "$album[$b]") {
				$boardlist="$boardlist<option selected value=\"$acitem[0]\">$acitem[1]</option>";
			} else {
				$boardlist="$boardlist<option value=\"$acitem[0]\">$acitem[1]</option>";
			}
		}
			
			print qq~<tr>
					<td align="center">Album<br><select name="album">$boardlist</select></td>
				</tr>
		<tr> 
			<td align="center">$ugadmin{'010'}<br><a href="$usergalleryimagesurl/pending/$filename[$b]" target="_blank"><img src="$usergalleryimagesurl/pending/$filename[$b]" width="120" height="200" border="0"></a></td> 
		</tr>
			<tr>
				<td align="center">&nbsp;
					<input type="hidden" value="$num[$b]" name="num">
					<input type="hidden" name="sendername" value="$sendername[$b]">
					<input type="hidden" name="filename" value="$filename[$b]">
					<input type="hidden" name="adddate" value="$adddate[$b]">
					<input class='button' type="submit" name="moda" value="$ugadmin{'011'}">
					<input class='button' type="submit" name="moda" value="$ugadmin{'012'}">
				</td> 
			</tr>
			</table>
			</form>
~; 
			if ($numshown >= 20) { $b = @newugs; } 
		} 

	} 
	print_bottom(); 
	exit; 
}
 
################# 
sub verifypictures2 { 
################# 

if ($settings[7] ne "$root") { error("$err{'011'}"); } 

	if ($approvalaccess eq "0") {
		 if ($username ne "admin") { error("$err{'011'}"); }
	}

if ($input{'description'} eq "") {$input{'description'} = "$ugadmin{'013'}";} 

open(DATA, "<$usergallerydb/newugs.dat"); 
	file_lock(DATA); 
	@data = <DATA>; 
	unfile_lock(DATA); 
close(DATA); 
		
if ($input{'moda'} eq "$ugadmin{'011'}") { 

	$imgtoget = "";
	
	open(FILE, "$usergallerydb/$input{'album'}.cat") || error("$err{'001'} $usergallerydb/$input{'album'}.cat");
	file_lock(FILE);
	@pics = <FILE>;
	unfile_lock(FILE);
	close(FILE);
	
	@picsgetnum = reverse(sort { $a <=> $b } @pics);
	$num = @picsgetnum[0];
	$num =~ s/\.//;
	$num++;;
	
		opendir (DIR, "$usergalleryimagesdir");
		@files = readdir(DIR);
		closedir (DIR);
		@files = reverse(sort { $a <=> $b } @files);
		$newpostnum = @files[0];
		$newpostnum =~ s/\.//;
		$newpostnum++;
	
	$newfilename = $input{'filename'};
	($dummy, $ext) = split(/\./, $newfilename);
	$newfilename = "$newpostnum.$ext";
	
	open(FILE, ">$usergallerydb/$input{'album'}.cat") || error("$err{'001'} $usergallerydb/$input{'album'}.cat");
	file_lock(FILE);
	print FILE "$num|$input{'sendername'}|$input{'description'}|$newfilename|$date|0\n"; 
	print FILE @pics;
	unfile_lock(FILE);
	close(FILE);
	
			 $dirtoget = "$usergalleryimagesdir";
			 $dirtoget = "$usergalleryimagesdir/pending";
			 $dirtogo = "$usergalleryimagesdir";
			 $imgtoget = "$input{'filename'}";
			
			copy("$dirtoget/$imgtoget", "$dirtogo/$newfilename");
			unlink("$dirtoget/$imgtoget");			 

	open (FILE, "$usergallerydb/newugs.dat");
		file_lock(FILE);
		@threads = <FILE>;
		unfile_lock(FILE);
	close (FILE);

	open (FILE, ">$usergallerydb/newugs.dat");
		file_lock(FILE);
		for ($a = 0; $a < @threads; $a++) {
			($nnum, $nalbumtogo, $nsendername, $ndescription, $nfilename, $ndate) = split(/\|/,$threads[$a]);
			if ($nnum eq $info{'num'}) { print FILE ""; }
			else { print FILE "$threads[$a]"; }
		}
		unfile_lock(FILE);
	close(FILE);
	
}

else { # not approved
	open (FILE, "$usergallerydb/newugs.dat");
		file_lock(FILE);
		@threads = <FILE>;
		unfile_lock(FILE);
	close (FILE);

	open (FILE, ">$usergallerydb/newugs.dat");
		file_lock(FILE);
		for ($a = 0; $a < @threads; $a++) {
			($num, $albumtogo, $sendername, $description, $filename, $dddate) = split(/\|/,$threads[$a]);
			if ($num eq $info{'num'}) { print FILE ""; }
			else { print FILE "$threads[$a]"; }
		}
		unfile_lock(FILE);
	close(FILE);
	
			$dirtoget = "$usergalleryimagesdir/pending";
			$imgtoget = "$input{'filename'}";
			
			unlink("$dirtoget/$imgtoget");
	
}
print "Location: $usergalleryadminurl/admin.cgi?op=verifypictures\n\n"; 
exit;
}

#####################
sub setup {
#####################

if ($username ne "admin") { error("$err{'011'}"); }

$navbar = "$btn{'014'} $ugadmin{'001'} $btn{'014'} $ugadmin{'003'}";
print_top();
print qq~
<form onSubmit="submitonce(this)" method="post" action="$usergalleryadminurl/admin.cgi?op=setup2">
<table border="0" cellspacing="1">
<tr>
<td><b>$ugadmin{'014'}</b><br>
<select name="nallowaction">~;
if ( $allowaction eq "0") {print qq~<option selected value="0">$ugadmin{'016'}</option>~;} else { print qq~<option value="0">$ugadmin{'016'}</option>~; }
if ( $allowaction eq "1") {print qq~<option selected value="1">$ugadmin{'017'}</option>~;} else { print qq~<option value="1">$ugadmin{'017'}</option>~; }
if ( $allowaction eq "2") {print qq~<option selected value="2">$ugadmin{'018'}</option>~;} else { print qq~<option value="2">$ugadmin{'018'}</option>~; }
if ( $allowaction eq "3") {print qq~<option selected value="3">$ugadmin{'019'}</option>~;} else { print qq~<option value="3">$ugadmin{'019'}</option>~; }
if ( $allowaction eq "4") {print qq~<option selected value="4">$ugadmin{'020'}</option>~;} else { print qq~<option value="4">$ugadmin{'020'}</option>~; }
if ( $allowaction eq "5") {print qq~<option selected value="5">$ugadmin{'021'}</option>~;} else { print qq~<option value="5">$ugadmin{'021'}</option>~; }
if ( $allowaction eq "6") {print qq~<option selected value="6">$ugadmin{'022'}</option>~;} else { print qq~<option value="6">$ugadmin{'022'}</option>~; }
if ( $allowaction eq "7") {print qq~<option selected value="7">$ugadmin{'023'}</option>~;} else { print qq~<option value="7">$ugadmin{'023'}</option>~; }
print qq~</select></td>
</tr>
<tr>
<td><b>$ugadmin{'038'}</b><br>
<select name="napprovalaccess">~;
if ( $approvalaccess eq "0") {print qq~<option selected value="0">$ugadmin{'039'}</option>~;} else { print qq~<option value="0">$ugadmin{'039'}</option>~; }
if ( $approvalaccess eq "1") {print qq~<option selected value="1">$ugadmin{'040'}</option>~;} else { print qq~<option value="1">$ugadmin{'040'}</option>~; }
print qq~</select></td>
</tr>
<tr>
<td><b>$ugadmin{'015'}</b><br>
<select name="nmaxperpage">~;
if ( $maxperpage eq "8") {print qq~<option selected value="8">8</option>~;} else { print qq~<option value="8">8</option>~; }
if ( $maxperpage eq "12") {print qq~<option selected value="12">12</option>~;} else { print qq~<option value="12">12</option>~; }
if ( $maxperpage eq "16") {print qq~<option selected value="16">16</option>~;} else { print qq~<option value="16">16</option>~; }
if ( $maxperpage eq "20") {print qq~<option selected value="20">20</option>~;} else { print qq~<option value="20">20</option>~; }
if ( $maxperpage eq "24") {print qq~<option selected value="24">24</option>~;} else { print qq~<option value="24">24</option>~; }
print qq~</select></td>
</tr>
<tr>
<td><b>$ugadmin{'025'}</b><br>
<select name="nshownewalbum">~;
if ( $shownewalbum eq "0") {print qq~<option selected value="0">$ugadmin{'028'}</option>~;} else { print qq~<option value="0">$ugadmin{'028'}</option>~; }
if ( $shownewalbum eq "1") {print qq~<option selected value="1">1 $ugadmin{'029'}</option>~;} else { print qq~<option value="1">1 $ugadmin{'029'}</option>~; }
if ( $shownewalbum eq "3") {print qq~<option selected value="3">3 $ugadmin{'030'}</option>~;} else { print qq~<option value="3">3 $ugadmin{'030'}</option>~; }
if ( $shownewalbum eq "5") {print qq~<option selected value="5">5 $ugadmin{'030'}</option>~;} else { print qq~<option value="5">5 $ugadmin{'030'}</option>~; }
if ( $shownewalbum eq "7") {print qq~<option selected value="7">7 $ugadmin{'030'}</option>~;} else { print qq~<option value="7">7 $ugadmin{'030'}</option>~; }
print qq~</select></td>
</tr>
<tr>
<td><b>$ugadmin{'026'}</b><br>
<select name="nshownewpicture">~;
if ( $shownewpicture eq "0") {print qq~<option selected value="0">$ugadmin{'028'}</option>~;} else { print qq~<option value="0">$ugadmin{'028'}</option>~; }
if ( $shownewpicture eq "1") {print qq~<option selected value="1">1 $ugadmin{'029'}</option>~;} else { print qq~<option value="1">1 $ugadmin{'029'}</option>~; }
if ( $shownewpicture eq "3") {print qq~<option selected value="3">3 $ugadmin{'030'}</option>~;} else { print qq~<option value="3">3 $ugadmin{'030'}</option>~; }
if ( $shownewpicture eq "5") {print qq~<option selected value="5">5 $ugadmin{'030'}</option>~;} else { print qq~<option value="5">5 $ugadmin{'030'}</option>~; }
if ( $shownewpicture eq "7") {print qq~<option selected value="7">7 $ugadmin{'030'}</option>~;} else { print qq~<option value="7">7 $ugadmin{'030'}</option>~; }
print qq~</select></td>
</tr>
<tr>
<td><b>$ugadmin{'027'}</b><br>
<select name="nshowhotpicture">~;
if ( $showhotpicture eq "0") {print qq~<option selected value="0">$ugadmin{'028'}</option>~;} else { print qq~<option value="0">$ugadmin{'028'}</option>~; }
if ( $showhotpicture eq "25") {print qq~<option selected value="25">25 $ugadmin{'031'}</option>~;} else { print qq~<option value="25">25 $ugadmin{'031'}</option>~; }
if ( $showhotpicture eq "50") {print qq~<option selected value="50">50 $ugadmin{'031'}</option>~;} else { print qq~<option value="50">50 $ugadmin{'031'}</option>~; }
if ( $showhotpicture eq "75") {print qq~<option selected value="75">75 $ugadmin{'031'}</option>~;} else { print qq~<option value="75">75 $ugadmin{'031'}</option>~; }
if ( $showhotpicture eq "100") {print qq~<option selected value="100">100 $ugadmin{'031'}</option>~;} else { print qq~<option value="100">100 $ugadmin{'031'}</option>~; }
print qq~</select></td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td><input class='button' type="submit" value="$ugadmin{'024'}"></td>
</tr>
</form>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td><a href="$usergalleryadminurl/admin.cgi">$ugadmin{'006'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi">$ugadmin{'004'}</a></td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
~;

print_bottom();
exit;
}

#####################
sub setup2 {
#####################

if ($username ne "admin") { error("$err{'011'}"); }

open(FILE, ">$usergalleryadmindir/ugsetup.dat");
file_lock(FILE);
	
print FILE qq~\$allowaction = "$input{'nallowaction'}";
\$maxperpage = "$input{'nmaxperpage'}";
\$shownewalbum = "$input{'nshownewalbum'}";
\$shownewpicture = "$input{'nshownewpicture'}";
\$showhotpicture = "$input{'nshowhotpicture'}";
\$approvalaccess = "$input{'napprovalaccess'}";
1;
~;
	
	unfile_lock(FILE);
	close(FILE);
	
print "Location: $usergalleryadminurl/admin.cgi?op=setup\n\n";
exit;
}

####################
sub view_failed {
####################

if ($username ne "admin") { error("$err{'011'}"); }

		open (FILE, "<$usergallerydb/failedugs.dat") || error("$error{'001'} $usergallerydb/failedugs.dat"); 
			file_lock(FILE);
			@failugs = <FILE>;
			unfile_lock(FILE);
		close (FILE);
		
$navbar = "$btn{'014'} $ugadmin{'001'} $btn{'014'} $ugadmin{'032'}";
print_top();
print qq~<table>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td><a href="$usergalleryadminurl/admin.cgi">$ugadmin{'006'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi">$ugadmin{'004'}</a></td>
</tr>
</table>
<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2">
<tr>
		<td class="imtitle" width="20%"><b>Album Number:</b></td>
		<td class="imtitle" width="60%"><b>User:</b></td>
		<td class="imtitle" width="20%"><b>Date:</b></td>
</tr>~;

	if (@failugs == 0) {
		print qq~<tr>
<td colspan="3" class="imwindow1">$ugadmin{'034'}</td>
</tr>~;
}

$second = "imwindow2";
for ($a = 0; $a < @failugs; $a++) {
		if ($second eq "imwindow1") { $second="imwindow2"; }
		else { $second="imwindow1"; }
		
		($dummy, $failedalbum[$a], $faileduser[$a], $faileddate[$a]) = split(/\|/, $failugs[$a]);
		display_date($faileddate[$a]); $faileddate[$a] = $user_display_date;
		
		print qq~<tr>
		<td class="$second" width="20%">$failedalbum[$a]</td>
		<td class="$second" width="60%"><a href="$scripturl/$cgi?action=imsend&to=$faileduser[$a]" class="$imnav">$faileduser[$a]</a></td>
		<td class="$second" width="20%">$faileddate[$a]</td>
		</tr>~;
		
}

print qq~<tr><td class="imtitle" align="center" colspan="3" width="100%"><a href="$usergalleryadminurl/admin.cgi?op=resetfailed">$ugadmin{'033'}</a></td></tr>
</table>
<table>
<tr>
<td><a href="$usergalleryadminurl/admin.cgi">$ugadmin{'006'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi">$ugadmin{'004'}</a></td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>~;

print_bottom();
exit;
}

####################
sub reset_failed {
####################

if ($username ne "admin") { error("$err{'011'}"); }

	open(FILE, ">$usergallerydb/failedugs.dat") || error("$error{'001'} $usergallerydb/failedugs.dat"); 
		file_lock(FILE); 
		print FILE ""; 
		unfile_lock(FILE); 
	close(FILE);

print "Location: $usergalleryadminurl/admin.cgi?op=viewfailed\n\n";
	
}

1; # return true 