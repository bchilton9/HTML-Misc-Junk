#!/usr/bin/perl
if ( $0 =~ /aset\.cgi$/ ) { ##- Outside sub-routine call part-1 -##
use CGI qw(:standard);

###################################################################################
###################################################################################
######/                          APage Mod v0.4.0b                         \#######
#####/                   for WebAPP - Automated Perl Portal                  \#####
####|-------------------------------------------------------------------------|####
####| Written by Weston Lemos (wes@onetruth.com)                              |####
####|-------------------------------------------------------------------------|####
####| Description:                                                            |####
####|                  APage Mod is a basic page creator,                     |####
####|               editor and viewer for use within WebAPP.                  |####
####|-------------------------------------------------------------------------|####
####|-------------------------------------------------------------------------|####
####| This program is free software; you can redistribute it and/or           |####
####| modify it under the terms of the GNU General Public License             |####
####| as published by the Free Software Foundation; either version 2          |####
####| of the License, or (at your option) any later version.                  |####
####|                                                                         |####
####| This program is distributed in the hope that it will be useful,         |####
####| but WITHOUT ANY WARRANTY; without even the implied warranty of          |####
####| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           |####
####| GNU General Public License for more details.                            |####
####|                                                                         |####
####| You should have received a copy of the GNU General Public License       |####
####| along with this program; if not, write to the Free Software             |####
####| Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307,  |####
####| USA                                                                     |####
#####\                                                                       /#####
######\  File: Last modified: 04/30/03  by Weston                           /######
###################################################################################
###################################################################################


#######################################################
### Change these if you plan use this with one      ###
### primary settings file and with one main script. ###
### You can leave the settings_file blank if you    ###
### are using it as a stand alone settings manager. ###
#######################################################
$settings_file = ""; 
$return_url = "apage.cgi";

###################################################
### Set the stand_alone variable to allow this  ###
### script to be used as a stand alone settings ###
### editor where the admin can from his browser ###
### select what settings files he/she wants to  ###
### edit.  Be careful. Insert "yes" for stand   ###
### alone, "no" for not. If you are             ###
### distributing this as part of another mod    ###
### make sure this is set to "no".              ###
###################################################
$stand_alone = "yes";

####################################################
#### Make sure the path to the config is right. ####
####################################################
require "../../config.pl";

###################################################################################
###################################################################################
######/                    ASet v0.2 - Modified for AMail                  \#######
#####/                   for WebAPP - Automated Perl Portal                  \#####
####|-------------------------------------------------------------------------|####
####| Written by Weston Lemos (wes@onetruth.com)                              |####
####|-------------------------------------------------------------------------|####
####| Description:                                                            |####
####|  ASet is a setting file manager intended to facilitate the              |####
####|  managing of small settings files.                                      |####
####|                                                                         |####
####| Usage:                                                                  |####
####|  ASet was originally created as a development aid for those             |####
####|  wishing to make WebAPP based scripts with "easy-to-manage"             |####
####|  settings files.  Besides being able to help other scripts ASet         |####
####|  can be installed as a stand alone settings file manager.               |####
####|  Although ASet will work with many different settings files, it is      |####
####|  recommended on either simple settings files or on settings files       |####
####|  that were created with specific ASet formatting.                       |####
####|                                                                         |####
####| Mod / Script Developers:                                                |####
####|  Just take this code and include it with your mod and have it           |####
####|  point to the settings file that you wish.  Set the "return_url"        |####
####|  to point to the name of your main script.  Make sure to set the        |####
####|  stand_alone variable to "no". If you do use this script, please        |####
####|  place your Mod/Script description above this one.   Advanced           |####
####|  Developers: If you wish you can go ahead and modify this code to       |####
####|  make it more seamless with their own script.  For the most             |####
####|  updated version of this program, make sure to check out ModAPP at      |####
####|  http://www.web-app.org/modapp/cgi-bin/index.cgi .                      |####
####|                                                                         |####
####| File types supported:                                                   |####
####|  It will support most all simple settings files.  The default           |####
####|  accepted extensions are .dat, .cfg, and .lng.                          |####
####|                                                                         |####
####| Known Bugs:                                                             |####
####|  Tab spaced settings files often will have alignment issues. (FIXED)    |####
####|  ASet does not support multilined variables.                            |####
####|  Variables with semicolons in their values do not currently work.(FIXED)|####
####|  It seems to be quite processor intensive currently. (FIXED)            |####
####|  Error with Double Quotes. (FIXED) Converts all to &quot;               |####
####|  &quot; isn't good for array's. -- Use (') single quotes. (WORKS)       |####
####|  Let me know if you find more.                                          |####
####|-------------------------------------------------------------------------|####
####|-------------------------------------------------------------------------|####
####| This program is free software; you can redistribute it and/or           |####
####| modify it under the terms of the GNU General Public License             |####
####| as published by the Free Software Foundation; either version 2          |####
####| of the License, or (at your option) any later version.                  |####
####|                                                                         |####
####| This program is distributed in the hope that it will be useful,         |####
####| but WITHOUT ANY WARRANTY; without even the implied warranty of          |####
####| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           |####
####| GNU General Public License for more details.                            |####
####|                                                                         |####
####| You should have received a copy of the GNU General Public License       |####
####| along with this program; if not, write to the Free Software             |####
####| Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307,  |####
####| USA                                                                     |####
#####\                                                                       /#####
######\  File: Last modified: April 13, 2003  by Weston                     /######
###################################################################################
###################################################################################


require "$sourcedir/subs.pl";

eval {
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
<pre>$@</pre><p>If this problem persits, please contact the webmaster and 
inform him about date and time you've recieved this error.</p>~;
	exit;
}

getlanguage();
ban();
getdate();
&parse_form;
logips();
loadcookie();
loaduser();
logvisitors();

} ##- End of outside sub-routine call part-1 -##

################################
# Language and color settings: #
################################
$asetcolor2 = "#a0a8b8";

$aset{'101'} = "Main Settings:";
$aset{'102'} = "Select";
$aset{'103'} = "Settings File Name";
$aset{'104'} = "May have Relative or Full path.";
$aset{'105'} = "Note: If the all information above looks right, it should most likely save right.";
$aset{'106'} = "Settings Successfully Saved!";
$aset{'107'} = "Test Output";
$aset{'108'} = "Click Here to Return"; 
$aset{'109'} = " > ASet Settings Manager";
$aset{'110'} = "The file you selected is not a valid settings file.";
$aset{'111'} = "Chick <a href=$return_url><b>HERE</b></a> to go back.";
$aset{'112'} = "File not found!"; 

@valid_settings_extensions =  ('dat', 'lng', 'cfg', 'DAT', 'LNG', 'CFG'); 


if ( $0 =~ /aset\.cgi$/ ) { ##- Outside sub-routine call part-2 -##

################################
$navbar = "$aset{'109'}";
################################
###################################################
# Lets see if you are valid enough to get in here #
###################################################
if ($username ne "admin" ) { error("$err{'011'}"); }          #### This line IS NOT called if you use this file as a subroutine ####
###################################################

if ( $stand_alone eq "yes" && $info{selected_settings_file} eq "") { print_stand_alone(); }
if ( $info{selected_settings_file} ne "" ) { $settings_file = $info{selected_settings_file}; }
aset_set_settings();
} ##- End of outside sub-routine call part-2 -##


#######################
sub print_stand_alone {
#######################
print_top();
	
print qq~
<CENTER><table border="0" cellpadding="6" cellspacing="0" style="border:1 solid black" width="550">
<tr><th nowrap align="left" bgcolor="$asetcolor2" style="border-bottom:1 solid black">
$aset{'101'}</th></tr>
<tr><td valign="top" >
    <form onSubmit="submitonce(this)" method="POST" action="aset.cgi">
    <input type=hidden  name="asetaction" value="asetmainsettings">
		<tr><td>
		<b>$aset{'103'}</b> - $aset{'104'}<br>
                <input type="text" name="selected_settings_file" style="width: 540px" size="65" value="$settings_file">
                </tr></td>

<TR><TD><p><CENTER><input type="submit" value="$aset{'102'}" name="B1"></p></CENTER>
</form> &nbsp;</tr></td></td></tr></table></CENTER>
~;
print_bottom();
exit;
} 



########################
sub aset_save_settings {
########################

open(FILE, "$settings_file") || error("$aset{'112'} $settings_file <BR>$aset{'111'}"); 
file_lock(FILE);
chomp(@sfile = <FILE>);
unfile_lock(FILE); 
close(FILE); 

$MScount = "0";
foreach $dline (@sfile) {
	$dline =~ s/\s+$//g;

	if ( $dline =~ /(^\s*)(\$|\@)(\S+)(\s*)=(\s*)(\"|\'|\()(.*)(\"\;|\'\;|\)\;)(\s*)(\#*)(.*)$/ ) {

		$sp1m 		= "$1";
		$MSvartype 	= "$2";
		$MSvar 		= "$3";
		$sp2m 		= "$4";
		$sp3m 		= "$5";
		$first_char 	= "$6";
		$MSvalue 	= "$7";
		$last_char 	= "$8";
		$sp4m 		= "$9";
		$pcom		= "$10";
		$MScomment 	= "$11";
		
		
		
		if ( $MSvar =~ /(\S+)\{(\'?|\"?)(\w+)(\'?|\"?)\}/ ) { $MSvarK = "$1-$3"; }
		else { $MSvarK = "$MSvar"; }
		
		$info{$MSvarK} =~ s/"/&quot;/g;
		
		$coolio = "$sp1m$MSvartype$MSvar$sp2m=$sp3m$first_char$info{$MSvarK}$last_char$sp4m$pcom$MScomment";
		push(@newpfile,"$coolio");
	} else { push(@newpfile,$dline); } 
	$MScount++;
}

if ( $info{sampleout} eq "sample" ) {
	if ( $0 =~ /aset\.cgi$/ ) {print "Content-type: text/plain\n\n";}
	print "<pre>\n";		
	foreach $text (@newpfile) { 
		$text =~ s/</&lt;/g;
		$text =~ s/>/&gt;/g;
		$text =~ s/&quot;/&amp;quot;/g;	
		print "$text\n"; 
	}	
	print qq~</pre><CENTER><HR WIDTH=50%>$aset{'105'}<form><input type=button value="$msg{'603'}" 
		 onClick="javascript:window.close();"></form></CENTER><P> ~;
	if ( $0 !~ /aset\.cgi$/ ) {print_bottom();}
	exit;
}

open(RILE, ">$settings_file") || error("$aset{'112'} $settings_file<BR> $aset{'111'}"); 
file_lock(RILE);
foreach $nline (@newpfile) { print RILE "$nline\n"; }
unfile_lock(RILE); 
close(RILE); 

if ( $info{selected_settings_file} ne "" ) { $settings_file = $info{selected_settings_file}; }
if ( $info{selected_return_url} ne "" ) { $return_url = $info{selected_return_url}; }

$savemessage = "<h2>$aset{'106'}</h2>";
aset_set_settings();
} #close Save The Settings



#######################
sub aset_set_settings {
#######################

if ( $0 !~ /aset\.cgi$/ ) {
	@funnyguys = split(/\//, $0);
	$thecurrentscript = pop(@funnyguys);
} else { $thecurrentscript = "aset.cgi"; }


if ( $info{asetaction} eq "asetsave" ) {
	$info{asetaction} = "";
	aset_save_settings(); 
}

if ( $0 =~ /aset\.cgi$/ ) { print_top(); }

$proceed_type = "0";
foreach $setextn (@valid_settings_extensions) {
	if($settings_file =~ /\.$setextn$/) {
		$proceed_type = 1;
		last;
	}
}
if ($proceed_type eq "0") { error("$aset{'110'}<BR>$settings_file<BR>$aset{'111'}"); }

open(FILE, "$settings_file") || error("$aset{'112'} $settings_file<BR> $aset{'111'}"); 
file_lock(FILE);
chomp(@sfile = <FILE>);
unfile_lock(FILE); 
close(FILE); 


if ($return_url ne "" ) {
$return_button = "<input type=\"button\" value=\"$aset{'108'}\" onclick=\"self.location='$return_url'\">";	
}

if ($didasetsetbefore ne "yepitdid" ) {

print qq~

<script language=javascript>
<!--
function OnButton1()
{
	document.aset.sampleout.value = "sample";
	document.aset.target = "_blank";	// Opens in a new window
	document.aset.submit();			// Submit the page
	return true;
}
function OnButton2()
{
	document.aset.sampleout.value = "";
	document.aset.target = "_top";		// Opens in the same window
	document.aset.submit();			// Submit the page
	return true;
}
-->
</script>

<CENTER>$savemessage<table border="0" cellpadding="6" cellspacing="0" style="border:1 solid black" width="550">
<tr><th nowrap align="left" bgcolor="$asetcolor2" style="border-bottom:1 solid black">
$aset{'101'}</th></tr>
<tr><td valign="top" >
    <form onSubmit="submitonce(this)" method="POST" name="aset"action="$thecurrentscript">
    <input type="hidden" name="asetaction" value="asetsave">
    <input type="hidden" name="sampleout" value="">
    <input type="hidden" name="selected_settings_file" value="$settings_file">
    <input type="hidden" name="selected_return_url" value="$return_url">
    <input type="hidden" name="action" value="$settings_file">
    <input type="hidden" name="act" value="$settings_file">

~;

$MScount = "0";
foreach $dline (@sfile) {
	$dline =~ s/\s+$//g;
	$MScommentbig = "";
	$MScommentlittle = "";

	
	if ( $dline =~ /^\#\@\#\@\s+/ ) {
		$DAnotes = $dline;
		$DAnotes =~ s/^\#\@\#\@\s+//;
		$MSillycount = $MScount + 1;
		if ( @sfile[$MSillycount] =~ /^\#\@\#\@\s+/ ) {
			$DADnotes .= " $DAnotes";	
		} else {
			$DADnotes .= " $DAnotes";
			print qq~<tr><td>$DADnotes</tr></td>~;
			$DADnotes = "";
		}
		
	} elsif ( $dline =~ /^\#\#\#\#\# (.*) \#\#\#\#\#$/ ) { 
		$MSboxtitile = "$dline";
		$MSboxtitile =~ s/\#\#\#\#\#//g;
		print qq~
		<tr><td>
		<table border="0" cellpadding="2" cellspacing="0" style="border:1 solid black" width="100%">
		<tr><th nowrap align="left" bgcolor="$asetcolor2" style="border-bottom:1 solid black">
		$MSboxtitile</th></tr>
		~;
		 
	} elsif ( $dline =~ /^\#\%+\#$/ ) {
		print qq~</table></tr></td>~;		
	

	} elsif ( $dline =~ /(^\s*)(\$|\@)(\S+)(\s*)=(\s*)(\"|\'|\()(.*)(\"\;|\'\;|\)\;)(\s*)(\#*)(.*)$/ ) {

		$sp1m 		= "$1";
		$MSvartype 	= "$2";
		$MSvar 		= "$3";
		$sp2m 		= "$4";
		$sp3m 		= "$5";
		$first_char 	= "$6";
		$MSvalue 	= "$7";
		$last_char 	= "$8";
		$sp4m 		= "$9";
		$pcom		= "$10";
		$MScomment 	= "$11";
		
		if ( $MSvar =~ /(\S+)\{(\'?|\"?)(\w+)(\'?|\"?)\}/ ) { $MSvarK = "$1-$3"; }
		else { $MSvarK = "$MSvar"; }
		
		if ( $MScomment =~ /^\-/ ) { $MScommentlittle = $MScomment; }
		elsif ( $pcom =~ /\#/ ) { $MScommentbig = "$MScomment<BR>"; }

		print qq~ 
		<tr><td>$MScommentbig
		<b>$MSvar</b> $MScommentlittle<br>
                <input type="text" name="$MSvarK" style="width: 540px" size="65" value="$MSvalue">
                </tr></td>
                ~;
	}
	$MScount++;
}

print qq~
<TR><TD><p><CENTER>
<INPUT type="button" value="$btn{'022'}" name=button2 onclick="return OnButton2();">&nbsp; 
<input type="reset" value="$btn{'023'}" name="B2">&nbsp;
<INPUT type="button" value="$aset{'107'}" name=button1 onclick="return OnButton1();">
</p>$return_button</CENTER>
</form> &nbsp;</tr></td></td></tr></table></CENTER>
~;

if ( $0 =~ /aset\.cgi$/ ) { print_bottom(); exit; }

} 

$didasetsetbefore = "yepitdid";

}



###########################################################################
###########################################################################
############################## End Of ASet! ##############################
###########################################################################
###########################################################################

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
<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this 
error.</p>
~;
	exit;
}

}

########################################
# Code to get the data from GET & POST #
########################################
sub parse_form {

	read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	if (length($buffer) < 5) {
		$buffer = $ENV{QUERY_STRING};
	}
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);

		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		if ($name =~ /^multiple-/) {
			$name =~ s/multiple-//;
			push (@{$info{$name}}, $value);
		} else {
			$info{$name} = $value;
		}
	}
}

1;





