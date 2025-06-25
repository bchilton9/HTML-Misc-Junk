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
# WebAPP Database Multiple is modified to this purpose by DavidF from 	      #
# original code by carter and floyd of webapp 9.8.			      #
#  						      			      #
# For more information see: http://www.web-app.org/                	      #
#                                                                             #
# File: Last modified: 04/15/03                                               #
###############################################################################
###############################################################################

$scriptname = "WebAPP";
$scriptver = "0.9.5";

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
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

$wadbmDIR = "$mods_dir/wadbm";
$wadbmURL = "$mods_url/wadbm";
$wadbmdataDIR = "$wadbmDIR/data";
$wadbmadminDIR = "$wadbmDIR/admin";

####################################
# WebAPP DataBase Multiple Mod index.cgi
####################################

if ($lang_support eq "1") { mod_langsupp(); }

$navbar = " $btn{'014'} $tutorial{'001'}"; 
print_top();

if ($action eq "admin") {
	if ($op eq "") { require "$wadbmDIR/index.pl"; displaydbs(); }
	elsif ($op eq "managecats") { require "$wadbmadminDIR/admin.cgi"; managecats(); }
	elsif ($op eq "reordercats") { require "$wadbmadminDIR/admin.cgi"; reordercats(); }
}	
	else { displaydbs(); } 
exit; #all done

################ 
sub displaydbs { 
################ 
	#check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); } 
 
	open(FILE, "$wadbmdataDIR/cats.txt") || error("$err{'001'} $wadbmdataDIR/cats.txt"); 
	file_lock(FILE); 
	chomp(@categories = <FILE>); 
	unfile_lock(FILE); 
	close(FILE); 
 
	foreach $curcat (@categories) {
		$curcat =~ s/[\n\r]//g; 
	}
	
	$navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $mnu{'014'}"; 
 
	print_top();
	print qq~<table border="0" width="80%" cellpadding="3" cellspacing="0" align="center">~; 
	foreach $curcat (@categories) {
		open(FILE, "$wadbmdataDIR/$curcat.cat") || error("$err{'001'} $wadbmdataDIR/$curcat.cat"); 
		file_lock(FILE); 
		chomp(@catinfo = <FILE>); 
		unfile_lock(FILE); 
		close(FILE);
	
	foreach $catinfo (@catinfo) {
		$catinfo =~ s/[\n\r]//g; 
	}
		print qq~<tr><td colspan="2" valign="top" class="fullnewstitle"><a href="$wadbmURL/wadbm.cgi?vsFILE=$curcat">@catinfo[0]</a></td><td>@catinfo[1]</td></tr>~;
	} 
	print qq~</table> 
~; 
	print_bottom(); 
	exit; 
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

