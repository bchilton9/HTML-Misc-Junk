#!/usr/bin/perl
###############################################################################
###############################################################################
# ugconvert.cgi for User Gallery                                              #
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
require "../../config.pl"; # WebAPP config
require "./usergallery.cfg"; # User Gallery config
require "$usergalleryadmindir/ugsetup.dat";
######

# do not modify anything below this line unless you know what you are doing!

eval {
	require "$sourcedir/subs.pl";

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

# User Gallery v1.0 by Floyd #

if ($info{'action'} eq "start") {start();}
else {doorway();}
exit;
 
######################
sub doorway {
######################

		print_top();
		print qq~<table border="0" cellpadding="3" cellspacing="0" width="100%">
		<form onSubmit="submitonce(this)" action="$usergalleryurl/ugconvert.cgi?action=start" method="post">
		<tr>
		<td>Confirm Gallery Image Folder<br><input type="text" name="oldgallery" size="80" value="$imagesdir/gallery"></td>
		</tr>
		<tr>
		<td>Confirm UserGallery Image Folder<br><input type="text" name="newgallery" size="80" value="$usergalleryimagesdir"></td>
		</tr>
		<tr>
		<td>&nbsp;</td>
		</tr>
		<tr>
		<td><input class='button' type="submit" value="Start"></td>
		</tr>
		</form>
		</table>~;
		print_bottom();
		exit;
}

##################
sub start {
##################



opendir(IMD, $input{'oldgallery'}) || die("Cannot open directory $input{'oldgallery'}"); 
@thefiles= readdir(IMD); 
closedir(IMD);

@thefiles = reverse(sort { $a <=> $b } @thefiles);

foreach $line (@thefiles) {
$line =~ s/[\n\r]//g;
($dummy, $ext) = split(/\./, $line);
			if ($line ne "." && $line ne ".." && $line ne "thumbnails" && $ext eq "") {
			makealbum($line);
			@thepics = ();
			opendir(PICD, "$input{'oldgallery'}/$line") || die("Cannot open directory $input{'oldgallery'}/$line"); 
			@thepics = readdir(PICD); 
			closedir(PICD);
			@thepics = reverse(sort { $a <=> $b } @thepics);

			 				 foreach $pline (@thepics) {
							 $pline =~ s/[\n\r]//g;
							 ($dummy, $ext, $ext2) = split(/\./, $pline);
							 if ($ext eq "gif" or $ext eq "jpg" or $ext eq "jpeg" or $ext eq "GIF" or $ext eq "JPG" or $ext eq "JPEG" && $ext2 ne "txt" && $ext2 ne "cnt") {$imdir = "$input{'oldgallery'}/$line"; dopictures($imdir, $newalbumnumber, $pline);}
							 }
			} 
}

print "Location: $usergalleryurl/index.cgi\n\n";
exit;

} 

######################
sub makealbum {
######################

my ($desc) = @_;

		opendir (DIR, "$usergallerydb");
		@files = readdir(DIR);
		closedir (DIR);
		@files = grep(/cat/,@files);
		@files = reverse(sort { $a <=> $b } @files);
		$newalbumnumber = @files[0];
		$newalbumnumber =~ s/.cat//;
		$newalbumnumber++;

	$accesstype = "0";
	
	open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat"); 
	lock(FILE); 
	@cats = <FILE>; 
	unlock(FILE); 
	close(FILE); 
 
	open(FILE, ">$usergallerydb/cats.dat") || error("$err{'016'} $usergallerydb/cats.dat"); 
	lock(FILE); 
	print FILE "$newalbumnumber|$desc|$username|$date|$accesstype\n"; 
	print FILE @cats; 
	unlock(FILE); 
	close(FILE);
	
	open(FILE, ">$usergallerydb/$newalbumnumber.cat"); 
	lock(FILE); 
	print FILE ""; 
	unlock(FILE); 
	close(FILE);
	
	return $newalbumnumber; 
	
}

####################
sub dopictures {
####################
my ($dirtoget, $albumtogo, $filename) = @_;

$caption = "$filename";

	open(FILE, "$dirtoget/$caption.txt");
	lock(FILE);
	@cap = <FILE>;
	unlock(FILE);
	close(FILE);
	
	$newcaption = @cap[0];
	
	if ($newcaption eq "") {$caption = "$filename";
	} else {$caption = "$newcaption";}
	
	if (length($caption) > 20) {
						$tmpcaption = substr($caption, 0, 20);
						$tmpcaption =~ s/(.*)\s.*/$1/;
						$caption = "$tmpcaption...";
				}
				else {
				$caption = $caption;
				}	

	open(FILE, "$usergallerydb/$albumtogo.cat") || error("$err{'001'} $usergallerydb/$albumtogo.cat");
	lock(FILE);
	@pics = <FILE>;
	unlock(FILE);
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
	
	$newfilename = $filename;
	($dummy, $ext) = split(/\./, $newfilename);
	$newfilename = "$newpostnum.$ext";
	
	open(FILE, ">$usergallerydb/$albumtogo.cat") || error("$err{'001'} $usergallerydb/$albumtogo.cat");
	lock(FILE);
	print FILE "$num|admin|$caption|$newfilename|$date\n"; 
	print FILE @pics;
	unlock(FILE);
	close(FILE);
	
			 $dirtogo = "$usergalleryimagesdir";
			 $imgtoget = "$filename";
			 
			copy("$dirtoget/$imgtoget", "$dirtogo/$newfilename");
			
}

1;