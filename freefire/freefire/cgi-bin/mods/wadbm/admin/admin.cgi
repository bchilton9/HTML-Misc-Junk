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
	require "../../../config.pl";
	require "$sourcedir/subs.pl";
	require "../config.dat";
	
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
$wadbmadmin = "mods/wadbm/admin/admin.cgi";

####################################
# WebAPP DataBase Multiple admin.cgi
####################################

if ($lang_support eq "1") { mod_langsupp(); }

$navbar = " $btn{'014'} $dbadmin{'001'}"; 
print_top();

if ($action eq "admin") {
	if ($op eq "") { require "$wadbmadminDIR/admin.cgi"; topdisplay(); }
	elsif ($op eq "managecats") { require "$wadbmadminDIR/admin.cgi"; managecats(); }
	elsif ($op eq "reordercats") { require "$wadbmadminDIR/admin.cgi"; reordercats(); }
	elsif ($op eq "removecat") { require "$wadbmadminDIR/admin.cgi"; removecat(); }
	elsif ($op eq "createcat") { require "$wadbmadminDIR/admin.cgi"; createcat(); }
}	
	else { topdisplay(); } 
exit; #all done

################ 
sub topdisplay { 
################ 
	#check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); } 
 	if ($username ne "admin") { error("$err{'011'}"); }

	open(FILE, "$wadbmdataDIR/cats.txt") || error("$err{'001'} $wadbmdataDIR/cats.txt"); 
	file_lock(FILE); 
	chomp(@categories = <FILE>); 
	unfile_lock(FILE); 
	close(FILE);

	$navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $mnu{'014'}"; 
 
	print_top(); 
	print qq~<br><table border="0" width="100%" cellpading="0" cellspacing="0"> 
<tr> 
<td valign="top">
<a href="$pageurl/$wadbmadmin?action=admin&amp;op=managecats">Create New/Delete a Database or change order of existing Databases.</a>
</td> 
</tr>
<tr>
<td valign="top">
<a href="$wadbmURL/DBedit.cgi">Configure/Edit a New/Existing Database.</a>
</td>
</tr> 
</table> 
~; 
	print_bottom(); 
	exit; 
} 
################ 
sub managecats { 
################ 
	#check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); } 
 	if ($username ne "admin") { error("$err{'011'}"); }

	open(FILE, "$wadbmdataDIR/cats.txt") || error("$err{'001'} $wadbmdataDIR/cats.txt"); 
	file_lock(FILE); 
	chomp(@categories = <FILE>); 
	unfile_lock(FILE); 
	close(FILE); 
 
	$catsdropdown = ""; 
	$catlist = ""; 
	foreach $curcat (@categories) { 
		$catsdropdown = "$catsdropdown<option>$curcat</option>"; 
		$catlist = "$catlist\n$curcat"; 
	} 
 
	$navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $mnu{'014'}"; 
 
	print_top(); 
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0"> 
<tr> 
<td valign="top"> 
<form onSubmit="submitonce(this)" action="$pageurl/$wadbmadmin?action=admin&amp;op=reordercats" method="post"> 
<b>$dbadmin{'002'}</b><br> 
<textarea name="cats" cols="40" rows="4">$catlist</textarea><br> 
<input type="submit" value="$btn{'024'}"> 
</form></td> 
<td valign="top"><form onSubmit="submitonce(this)" action="$pageurl/$wadbmadmin?action=admin&amp;op=removecat" method="post"> 
<b>$dbadmin{'003'}</b><br> 
<select name="cat"> 
$catsdropdown 
</select> 
<input type=submit value="$btn{'011'}"> 
</form></td></tr> 
<tr><td valign="top"><form onSubmit="submitonce(this)" action="$pageurl/$wadbmadmin?action=admin&amp;op=createcat" method="post"> 
<b>$dbadmin{'004'}</b><br> 
$dbadmin{'005'}<br> 
<input type="text" size="15" name="catid"><br> 
$dbadmin{'006'}<br> 
<input type="text" size="40" name="catname"><br> 
$dbadmin{'007'}<br> 
<input type="text" size="40" name="dbdescription"><br> 
$dbadmin{'008'}<br>
<input type="submit" value="$btn{'025'}">
</form>
</td> 
</tr>
</table> 
~; 
	print_bottom(); 
	exit; 
} 
 
#################
sub reordercats {
#################
	#check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); }
	if ($username ne "admin") { error("$err{'011'}"); }

	$input{'cats'} =~ s/\r//g;
	open(FILE, ">$wadbmdataDIR/cats.txt") || error("$err{'016'} $wadbmdataDIR/cats.txt");
	file_lock(FILE);
	print FILE "$input{'cats'}";
	unfile_lock(FILE);
	close(FILE);
	managecats();
	exit;
}
 
############### 
sub removecat { 
############### 
	#check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); } 
 	if ($username ne "admin") { error("$err{'011'}"); }

	open(FILE, "$wadbmdataDIR/cats.txt") || error("$err{'001'} $wadbmdataDIR/cats.txt"); 
	file_lock(FILE); 
	chomp(@categories = <FILE>); 
	unfile_lock(FILE); 
	close(FILE); 
 
	$newcatlist = ""; 
	foreach $curcat (@categories) { 
		if ($curcat ne "$input{'cat'}") { $newcatlist = "$newcatlist$curcat\n"; } 
	} 
 
	open(FILE, ">$wadbmdataDIR/cats.txt") || error("$err{'016'} $wadbmdataDIR/cats.txt"); 
	file_lock(FILE); 
	print FILE "$newcatlist"; 
	unfile_lock(FILE); 
	close(FILE); 
 
	$curcat = "$input{'cat'}"; 
	 
	open(FILE, "$wadbmdataDIR/$curcat.cat") || error("$err{'001'} $wadbmdataDIR/$curcat.cat"); 
	file_lock(CAT); 
	chomp(@catinfo = <CAT>); 
	unfile_lock(CAT); 
	close(CAT); 
 
	$curcatname = "$catinfo[0]"; 
 
	unlink("$wadbmdataDIR/$curcat.cat");
	unlink("$wadbmdataDIR/$curcat.cfg"); 
	unlink("$wadbmdataDIR/$curcat.dat"); 
	managecats(); 
	exit; 
} 
 
############### 
sub createcat { 
############### 
	#check_access(editcats); if ($access_granted ne "1") { error("$err{'011'}"); } 
 	if ($username ne "admin") { error("$err{'011'}"); }

	$catid = "$input{'catid'}";
	
	$defaultCFG = "Title	BodyTag	HeaderColor	DataDarkColor	DataLightColor	DetailIcon	PageSize	ShowFields	Delimiter	UseFileLocking
ChangeMe	<body bgcolor='#FFFFFF' link='#000000' vlink='#000000'>	#BBBBBB	#BBBBBB	#EEEEEE	../../../images/wadbm/contact.gif	15	field3,field4,field6,field8		0";

	$defaultDAT = "ID	Complete
1	No"; 
 
	open(FILE, "$wadbmdataDIR/cats.txt") || error("$err{'001'} $wadbmdataDIR/cats.txt"); 
	file_lock(FILE); 
	chomp(@categories = <FILE>); 
	unfile_lock(FILE); 
	close(FILE); 
 
	open(FILE, ">$wadbmdataDIR/cats.txt") || error("$err{'016'} $wadbmdataDIR/cats.txt"); 
	file_lock(FILE); 
	foreach $curcat (@categories) { 
		print FILE "$curcat\n"; 
	} 
	print FILE "$catid"; 
	unfile_lock(FILE); 
	close(FILE); 
 
	open(FILE, ">$wadbmdataDIR/$catid.cat"); 
	print FILE "$input{'catname'}\n"; 
	print FILE "$input{'dbdescription'}\n"; 
	close(FILE);

	open(FILE, ">$wadbmdataDIR/$catid.dat"); 
	print FILE "$defaultDAT"; 
	close(FILE);

	open(FILE, ">$wadbmdataDIR/$catid.cfg"); 
	print FILE "$defaultCFG"; 
	close(FILE); 
	managecats(); 
	exit; 
} 

exit;

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
	require "../language/$modlang.dat";
	
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
	require "../language/$mod_lang";
	
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

