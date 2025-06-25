#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
# Mod Manager                                              				#
# v0.9.9 - Requin                                                             #
#-----------------------------------------------------------------------------#
# modmanager.cgi	                	                                          #
#                                                                             #
# Copyright (C) 2002 by WebAPP ( webapp@attbi.com )                           #
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
#                                                                             #
# Last modified: 01/07/03                                                     #
###############################################################################
###############################################################################

$| = 1;
use CGI::Carp qw(fatalsToBrowser);

$mm_build = "4";

eval {
	require "../config.pl";
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

####################################
# Mod Manager By Floyd
####################################

mmmod_langsupp();

mm_config();

if ($modlangfail eq "") {$modlangfail = "0";}

if ($access[35] ne "on") { error("$err{'011'}"); }

# Check to see if there was a function specified #
if ($action eq "create") { create_config(); }
if ($action eq "generate") { generate_config(); }
if ($action eq "editcf") { edit_config(); }
if ($action eq "edit_cffile") { regenerate_config(); }
else {

$navbar = " $btn{'014'} $modmanager{'001'} $mm_verbuild"; 
print_top();

print qq~<br><b><u>$modmanager{'002'}</u></b><p>~;

@pairs = split('&',$ENV{'QUERY_STRING'});
	foreach $pair (@pairs) {
		local($key, $value) = split('=', $pair);
       $value =~ tr/+/ /;
       $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	 $value =~ s/://g;
	 $GET{$key} = $value;
	}
	
	if ($ENV{'QUERY_STRING'} eq "") {
		opendir(DIR, "$moddir/");
			@dirlist = readdir(DIR);
		closedir(DIR);
		@sdir = sort @dirlist;
		
      FILE: foreach (@sdir) {
			next FILE if($_ eq '.');
			next FILE if($_ eq '..');
			next FILE if($_ eq 'modmanager.cgi');
			next FILE if($_ eq 'index.html');
			next FILE if($_ eq 'index.htm');
			next FILE if($_ eq '.htaccess');
			next FILE if($_ eq 'language');
			next FILE if($_ eq 'config.dat');
			next FILE if($_ eq 'mods.pl');
			
			$modfolder = $_;			
			
			eval {
			require "$moddir/$modfolder/config.dat";
			
			if ($IIS != 2) {
			if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
			}
			if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
			if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
			}
			};
			if ($@) { print qq~<font size="3"><b>$modfolder</b></font><br><font size="3" color="#FF0000"><b>$modmanager{'003'}</b></font>&nbsp;<font size="2" color="#FF0000"><b>$modmanager{'004'}</b></font><br>
			<font size="2">&nbsp;[<a href="$modurl/modmanager.cgi?action=create&mod=$modfolder">$modmanager{'005'}</a>]&nbsp;</font><p>~;
			} else { print qq~<font size="3"><b>$mod_name</b></font>&nbsp;<font size="2"><i>v$mod_vers</i></font><br>
			<font size="2">$mod_desc</font><br>~;
			if ($config_vers ne "$mm_vers") { print qq~<font size="3" color="#FF0000"><b>$modmanager{'003'}</b></font>&nbsp;$modmanager{'034'}$mm_verbuild. $modmanager{'035'}<br>~; }
			if ($mod_admin eq "1") { print qq~<font size="2">&nbsp;[<a href="$pageurl/mods/$_/admin/$admin_name">$mod_name&nbsp;$modmanager{'007'}</a>]&nbsp;</font>~; }
			print qq~<font size="2">&nbsp;[<a href="$modurl/modmanager.cgi?action=editcf&mod=$modfolder">$modmanager{'008'}</a>]&nbsp;</font>~;
			print qq~<p>~;
			$mod_admin = "0";
			$mod_lang = "0";
			$config_vers = "";
			}		
	}

print qq~
<p><hr align="left" width="100"><p>

				<font size="3"><b>$mmod_name</b></font>&nbsp;<font size="2"><i>$mm_verbuild</i></font><br>
				<font size="2">$mmod_desc</font>~;
				
				if ($modlangfail eq "1") {print qq~<p><font size="3" color="#FF0000"><b>$modmanager{'000'}</b></font>~;}

print qq~<p>~;

print_bottom();
exit;

}
}

################################
sub mm_config {
################################

($getdef_lang,$dummy)=split(/\./,$language);

$mm_vers = "$scriptver.$mm_build";
$mm_verbuild = "v$scriptver Build:$mm_build";
$mmod_name = "Mod Manager";
$mmod_vers = "$scriptver";
$mmod_desc = "Mod Manager.";
$mmlang_support = "1";
$mmdef_lang = "$getdef_lang.dat";
$moddir = "$scriptdir/mods";
$modurl = "$scripturl/mods";

}

################################
sub create_config {
###############################

$navbar = "$btn{'014'} $modmanager{'001'} $btn{'014'} $modmanager{'005'}"; 
print_top();

print qq~
<br>$modmanager{'024'}<p>
<form method="post" action="$modurl/modmanager.cgi?action=generate">
<table border="0" cellspacing="1">
<input type="hidden" name="mod_folder" value="$info{'mod'}">
<input type="hidden" name="config_vers" value="$mm_vers">
<input type="hidden" name="mod_lang" value="$def_lang">
<tr>
<td><b>$modmanager{'011'}</b></td>
<td><input type="text" name="mod_name" size="25" value="$info{'mod'}"></td>
</tr>
<tr>
<td><b>$modmanager{'012'}</b></td>
<td><input type="text" name="mod_vers" size="25"></td>
</tr>		
<tr>
<td><b>$modmanager{'013'}</b></td>
<td><select name="mod_admin"><option selected>0</option>
														 <option>1</option>
														 </select>&nbsp;$modmanager{'014'}</td>
</tr>
<tr>
<td><b>$modmanager{'033'}</b></td>
<td><input type="text" name="admin_name" size="25" value="admin.cgi"></td>
</tr>
<tr>
<td><b>$modmanager{'015'}</b></td>
<td><select name="lang_support"><option selected>0</option>
														 <option>1</option>
														 </select>&nbsp;$modmanager{'016'}</td>
</tr>
<tr>
<td><b>$modmanager{'017'}</b></td>
<td><textarea name="mod_desc" wrap=virtual rows=5 cols=35>$info{'mod'} $modmanager{'018'}</TEXTAREA></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$modmanager{'005'}"></td>
</tr>
</form>~;

				if ($modlangfail eq "1") {print qq~<tr><td colspan="2">&nbsp;</td></tr><tr><td colspan="2"><font size="3" color="#FF0000"><b>$modmanager{'000'}</b></font></td></tr>~;}

print qq~</table><p>~;

print_bottom();
exit;

}

##################################
sub generate_config {
##################################

	$mod_folder  = $input{'mod_folder'};
	$config_vers  = $input{'config_vers'};
	$mod_lang  = $input{'mod_lang'};
	$mod_name  = $input{'mod_name'};
	$mod_vers  = $input{'mod_vers'};
	$mod_admin  = $input{'mod_admin'};
	$admin_name  = $input{'admin_name'};
	$lang_support  = $input{'lang_support'};
	$mod_desc  = $input{'mod_desc'};
	
	if ($mod_name eq "") { error ("$modmanager{'028'}"); }
	if ($mod_vers eq "") { error ("$modmanager{'029'}"); }
	if ($mod_desc eq "") { error ("$modmanager{'030'}"); }
	if ($admin_name eq "" && $mod_admin eq "1") { error ("$modmanager{'031'}"); }
		
	open(FILE, ">$moddir/$mod_folder/config.dat");
	file_lock(FILE);
	
print FILE qq~\$config_vers = "$config_vers";
\$mod_name = "$mod_name";
\$mod_vers = "$mod_vers";
\$mod_desc = "$mod_desc";
\$mod_admin = "$mod_admin";
\$admin_name = "$admin_name";
\$lang_support = "$lang_support";
\$mod_lang = "$mmdef_lang";
1;
~;
	
	unfile_lock(FILE);
	close(FILE);	

print "Location: $modurl/modmanager.cgi\n\n";
	
}

################################
sub edit_config {
###############################

$navbar = "$btn{'014'} $modmanager{'001'} $btn{'014'} $modmanager{'008'}"; 
print_top();

require "$scriptdir/mods/$info{'mod'}/config.dat";

print qq~
<br>$modmanager{'024'}<p>
<form method="post" action="$modurl/modmanager.cgi?action=edit_cffile">
<table border="0" cellspacing="1">
<input type="hidden" name="mod_folder" value="$info{'mod'}">
<input type="hidden" name="config_vers" value="$mm_vers">
<tr>
<td><b>$modmanager{'011'}</b></td>
<td><input type="text" name="mod_name" size="25" value="$mod_name"></td>
</tr>
<tr>
<td><b>$modmanager{'012'}</b></td>
<td><input type="text" name="mod_vers" size="25" value="$mod_vers"></td>
</tr>		
<tr>
<td><b>$modmanager{'013'}</b></td>
<td><select name="mod_admin">~;
															if ( $mod_admin eq "0") {print qq~<option selected value="0">0</option>~; 
															} else { print qq~<option value="0">0</option>~; }
														 	if ( $mod_admin eq "1") {print qq~<option selected value="1">1</option>~;
														 	} else { print qq~<option value="1">1</option>~; }
print qq~</select>&nbsp;$modmanager{'014'}</td>
</tr>
<tr>
<td><b>$modmanager{'033'}</b></td>
<td><input type="text" name="admin_name" size="25" value="$admin_name"></td>
</tr>
<tr>
<td><b>$modmanager{'015'}</b></td>
<td><select name="lang_support">~;
															if ( $lang_support eq "0") {print qq~<option selected value="0">0</option>~; 
															} else { print qq~<option value="0">0</option>~; }
														 	if ( $lang_support eq "1") {print qq~<option selected value="1">1</option>~;
														 	} else { print qq~<option value="1">1</option>~; }
print qq~</select>&nbsp;$modmanager{'016'}</td>
</tr>
<tr>
<td><b>$modmanager{'017'}</b></td>
<td><textarea name="mod_desc" wrap=virtual rows=5 cols=35>$mod_desc</TEXTAREA></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$modmanager{'008'}"></td>
</tr>
</form>~;

				if ($modlangfail eq "1") {print qq~<tr><td colspan="2">&nbsp;</td></tr><tr><td colspan="2"><font size="3" color="#FF0000"><b>$modmanager{'000'}</b></font></td></tr>~;}

print qq~</table><p>~;

print_bottom();
exit;

}

##################################
sub regenerate_config {
##################################

	$mod_folder  = $input{'mod_folder'};
	$config_vers  = $input{'config_vers'};
	$mod_lang  = $input{'mod_lang'};
	$mod_name  = $input{'mod_name'};
	$mod_vers  = $input{'mod_vers'};
	$mod_admin  = $input{'mod_admin'};
	$admin_name  = $input{'admin_name'};
	$lang_support  = $input{'lang_support'};
	$mod_desc  = $input{'mod_desc'};
	
	if ($mod_name eq "") { error ("$modmanager{'028'}"); }
	if ($mod_vers eq "") { error ("$modmanager{'029'}"); }
	if ($mod_desc eq "") { error ("$modmanager{'030'}"); }
	if ($admin_name eq "" && $mod_admin eq "1") { error ("$modmanager{'031'}"); }
	
	open(FILE, ">$moddir/$mod_folder/config.dat") || error("$err{'001'} $moddir/$mod_folder/config.dat");
	file_lock(FILE);
	
print FILE qq~\$config_vers = "$config_vers";
\$mod_name = "$mod_name";
\$mod_vers = "$mod_vers";
\$mod_desc = "$mod_desc";
\$mod_admin = "$mod_admin";
\$admin_name = "$admin_name";
\$lang_support = "$lang_support";
\$mod_lang = "$mmdef_lang";
1;
~;
	
	unfile_lock(FILE);
	close(FILE);
	
print "Location: $modurl/modmanager.cgi\n\n";
	
}

###########################
sub mmmod_langsupp {
###########################

if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat");
		file_lock(FILE); #file_file_lock(FILE);
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
 		($modlang,$dummy)=split(/\./,$userlang);

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

if ($@) { mmmod_langsuppfail(); }

}

###########################
sub mmmod_langsuppfail {
###########################

eval {
	require "language/$mmdef_lang";
	
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};

if ($@) { mmmod_langsuppcritical(); }

}

########################
sub mmmod_langsuppcritical {
########################

# PLEASE - DO NOT EDIT OR TRANSLATE THIS SECTION! - THANKS!

$modmanager{'000'} = "MOD MANAGER LANGUAGE FAILED - NOW USING BUILT-IN LANGUAGE FILE!";

$modmanager{'001'} = "Mod Manager";
$modmanager{'002'} = "A list of currently installed Mods is below.";
$modmanager{'003'} = "Warning!";
$modmanager{'004'} = "Config File not found.";
$modmanager{'005'} = "Create Config File";
$modmanager{'007'} = "Admin";
$modmanager{'008'} = "Edit Config File";
$modmanager{'011'} = "Mod Name:";
$modmanager{'012'} = "Mod Version:";
$modmanager{'013'} = "Admin Script:";
$modmanager{'014'} = "Please select 0 if there is no Admin Script or 1 if there is.";
$modmanager{'015'} = "Language Support:";
$modmanager{'016'} = "Please select 0 if there is no Language Support or 1 if there is.";
$modmanager{'017'} = "Mod Description:";
$modmanager{'018'} = "Mod for WebAPP.";
$modmanager{'024'} = "<b>NOTE:</b> Please ensure that both the <i>Admin Script</i> and <i>Language Support</i> variables are set correctly. Failure to do so will cause script errors.";
$modmanager{'028'} = "No Mod Name";
$modmanager{'029'} = "No Mod Version Number";
$modmanager{'030'} = "No Mod Description";
$modmanager{'031'} = "No Mod Admin Script Name";
$modmanager{'032'} = "No Default Language File";
$modmanager{'033'} = "Main Admin Script Name";
$modmanager{'034'} = "Config File is <b>NOT</b> to ";
$modmanager{'035'} = "Please Edit!";

}

1;
