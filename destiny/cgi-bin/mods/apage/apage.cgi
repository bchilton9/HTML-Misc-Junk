#!/usr/bin/perl -w
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

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

eval {
	require "../../config.pl";
	require "$sourcedir/subs.pl";
	require "config.dat";
	require "apage.dat";
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
&parse_form;
getdate();
logips();
loadcookie();
loaduser();
logvisitors();


###########################################################################
###########################################################################
############################ Here Starts APage ############################
###########################################################################
###########################################################################

if ($lang_support eq "1") { mod_langsupp(); }

# Start making your changes here! #

$act 	= $info{act};
$action	= $info{action};
$hfile	= $info{hfile};
$ofile	= $info{ofile};
$f  	= $info{f};
$catact = $info{catact};
$apdir  = $info{apdir};
 
if ( $hfile eq "" ) { $hfile = $f; }

if ( $apdir ne "" ) { 
	$apageimagedir = "$defaultImageDir/$apdir";
	$apageimageurl = "$defaultImageURL/$apdir";
	$apagehtmldir  = "$defaultHTMLDir/$apdir";
	$apagefullhtmldir = "$defaultFullHTMLDir/$apdir";
	$apageshortimagedir = "$relativeimagedir/$apdir";
	$apget = "&apdir=$apdir";
	$apcur = "$apdir/";
} else { 
	$apageshortimagedir = "$relativeimagedir";
	$apagehtmldir  = "$defaultHTMLDir";
	$apageimagedir = "$defaultImageDir";
	$apageimageurl = "$defaultImageURL";
	$apagefullhtmldir = "$defaultFullHTMLDir";
}

$navbar = "> APage > $apagehtmldir";


if ($act eq "view" ) 				{ view_the_files(); } 
elsif ($act eq "edit" && $hfile =~ /.txt$/ ) 	{ edit_txt_file(); } 
elsif ($act eq "edit" && $hfile =~ /.htm/ ) 	{ edit_htm_file(); } 
elsif ($act eq "save" && $hfile =~ /.txt$/ ) 	{ save_txt_file(); } 
elsif ($act eq "save" && $hfile =~ /.htm/ ) 	{ save_htm_file(); } 
elsif ($act eq "save" && $hfile =~ /.htm/ ) 	{ save_htm_file(); } 
elsif ($act eq "delete" && $hfile =~ /./ ) 	{ delete_the_file(); } 
elsif ($act eq "add" ) 				{ add_the_file(); } 
elsif ($act eq "rename" ) 			{ rename_the_file(); } 
elsif ($act eq "renamed" ) 			{ renamed_the_file(); } 
elsif ($act eq "newfile" ) 			{ new_the_file(); } 
elsif ($act eq "readme" ) 			{ read_the_readme(); } 
elsif ($act eq "pic" ) 				{ manage_the_pictures(); } 
elsif ($act eq "picdata" ) 			{ fix_the_txt_file(); } 
elsif ($act eq "deleteimage" ) 			{ delete_the_image(); }
elsif ($f =~ /.txt$/ ) 				{ view_txt_file(); } 
elsif ($f =~ /.htm/ ) 				{ view_htm_file(); }

elsif ($act eq "createdir" ) 			{ creat_a_dir(); } 
elsif ($act eq "removedir" ) 			{ view_the_files(); } 
elsif ($act eq "newdir" ) 			{ save_a_dir(); } 
elsif ($act eq "deletefolder" ) 		{ delete_the_folder(); } 

elsif ($action ne "" )                          { aset_the_settings(); }

else 						{ view_the_files(); }

####################
sub view_the_files {
####################
check_the_user();
print_top();

opendir(DIR,$apagefullhtmldir) || die ("$apage{'100'} $apagefullhtmldir: $!\n");
local(@files) = grep(!/^\./,readdir(DIR));
closedir DIR;
$mrcount = "0";
$mrpount = "0";
$crzcount = "0";

foreach $line (@files) {
	if ($line =~ /.txt$/ || $line =~ /.html$/ || $line =~ /.htm$/)
	{
		$apfiledate = (stat("$apagefullhtmldir/$line"))[8];
		$apfilesize = (stat("$apagefullhtmldir/$line"))[7];
		push(@listfiledates, "$apfiledate|$line");
		push(@listfilesizes, "$apfilesize|$line");
		push(@listfiles," |$line");
		
		$crzcount++;
	}
	elsif ($line !~ /\S+\.\S+/) 
	{ 
		if (-d "$apagefullhtmldir/$line") 
		{
			opendir(FOLDIR,"$apagefullhtmldir/$line") || die ("$apage{'100'} $apagefullhtmldir/$line: $!\n");
			local(@insidefiles) = grep(!/^\./,readdir(FOLDIR));
			closedir FOLDIR;
			$apfoldersize = @insidefiles;
			$apfolderdate = (stat("$apagefullhtmldir/$line"))[8];
			push(@listfoldersizes, "$apfoldersize|$line|$apfoldersize");
			push(@listfolderdates, "$apfolderdate|$line|$apfoldersize");
			push(@listffolders," |$line|$apfoldersize"); 
			$mrpount++; 
		}
	}
}

$a1 = "up.gif";
$a2 = "down.gif";
$b1 = "up.gif";
$b2 = "down.gif";
$c1 = "upgrey.gif";
$c2 = "down.gif";

@sortedarray = sort(@listfiles);
if    ($info{sortby} eq "date") { @sortedarray = sort(ascend @listfiledates); $a1 = "upgrey.gif"; $c1 = "up.gif";}
elsif ($info{sortby} eq "size") { @sortedarray = sort(ascend @listfilesizes); $b1 = "upgrey.gif"; $c1 = "up.gif";}
elsif ($info{sortby} eq "dedt") { @sortedarray = sort(decend @listfiledates); $a2 = "downgrey.gif"; $c1 = "up.gif";}
elsif ($info{sortby} eq "desz") { @sortedarray = sort(decend @listfilesizes); $b2 = "downgrey.gif"; $c1 = "up.gif";}
elsif ($info{sortby} eq "denm") { @sortedarray = reverse(@sortedarray); $c2 = "downgrey.gif"; $c1 = "up.gif";}

@sortedfoldarray = sort(@listffolders);
if    ($info{sortby} eq "date") { @sortedfoldarray = sort(ascend @listfolderdates); }
elsif ($info{sortby} eq "dedt") { @sortedfoldarray = sort(decend @listfolderdates); }
elsif ($info{sortby} eq "size") { @sortedfoldarray = sort(ascend @listfoldersizes); }
elsif ($info{sortby} eq "desz") { @sortedfoldarray = sort(decend @listfoldersizes); }
elsif ($info{sortby} eq "denm") { @sortedfoldarray = reverse(@sortedfoldarray); }




if ( $apagehtmldir ne $defaultHTMLDir ) {

	print qq~
	<table border="0" cellpadding="0" cellspacing="0" width="100%"  class="navbar" bgcolor="$color4"><tr>
	<td align="center">&nbsp;<a href="apage.cgi" class="nav">$apage{'101'}</a>&nbsp;</td> ~;
	if ($apagehtmldir =~ /\w+\/\w+\// ) {
		@aptparts = split(/\//,$apdir);
		pop(@aptparts);
		foreach $apsinglepart (@aptparts) { $apprevdir .= "$apsinglepart/"; }
		$apprevdir =~ s/\/$//g;
		print qq~<td align="center">&nbsp;<a href="apage.cgi?apdir=$apprevdir" class="nav">$apage{'102'}</a>&nbsp;</td>~;
	}
	
	print qq~</tr> </table><P>~;
}

#if ( $apagehtmldir eq $defaultHTMLDir ) {
#	print qq~ <map name="FPMap0">
#	<area href="$apageurl?action=$modlang.dat" shape="rect" coords="10, 1, 30, 15">
#	<area href="$apageurl?action=apage.dat" shape="rect" coords="49, 1, 69, 15"></map><img border="0" 
#	src="$apageicondir/configbar.gif" align="right" usemap="#FPMap0" ALT="$apage{'103'}"><BR> ~;
#}

print qq~ 
<CENTER><font color="$color7"><B>$apagemessage</B></font><font face="arial" size="2">&nbsp;
<table cellSpacing="0" cellPadding="0" width="100%" bgColor="#000000" border="0">
  <tbody>
    <tr>
      <td>
        <table cellSpacing="1" cellPadding="2" width="100%" border="0">
          <tbody>
            <tr>
              <td bgColor="$color2" align="center"><b><font color="$color1">$apage{'106'}</font></b></td>
              <td bgColor="$color2" align="center"><b><font color="$color1">$apage{'107'}</font></b><a href="apage.cgi?act=view&sortby=date$apget"><img border="0" src="$apageicondir/$a1" border="0" ALT="$apage{'104'}"></A><a href="apage.cgi?act=view&sortby=dedt$apget"><img border="0" src="$apageicondir/$a2" border="0" ALT="$apage{'105'}"></A></td>
              <td bgColor="$color2" align="center"><b><font color="$color1">$apage{'108'}</font></b><a href="apage.cgi?act=view&sortby=size$apget"><img border="0" src="$apageicondir/$b1" border="0" ALT="$apage{'104'}"></A><a href="apage.cgi?act=view&sortby=desz$apget"><img border="0" src="$apageicondir/$b2" border="0" ALT="$apage{'105'}"></A></td>
              <td bgColor="$color2" align="center"><b><font color="$color1">$apage{'109'}</font></b></td>
              <td bgColor="$color2" align="center"><b><font color="$color1">$apage{'110'}</font></b><a href="apage.cgi?act=view&sortby=name$apget"><img border="0" src="$apageicondir/$c1" border="0" ALT="$apage{'104'}"></A><a href="apage.cgi?act=view&sortby=denm$apget"><img border="0" src="$apageicondir/$c2" border="0" ALT="$apage{'105'}"></A></td>
            </tr>
          </font>

~;



foreach $line (@sortedfoldarray) {
	($dummy,$nline,$thisfoldersize) = split(/\|/, $line);
	$line = $nline;	
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = 
           localtime((stat("$apagefullhtmldir/$line"))[8] + 3600*$timeoffset); 
	$mon++; 
	$year = 1900 + $year;
	if ($min < 10) {$min = "0" .$min; }
	print qq~
          <tr>
            <font size="2">
              <td bgColor="$color3" align="center">
                <table border="0" width="100%" cellspacing="0" cellpadding="0">
                  <tr>
                    <td align="center"><a href="apage.cgi?apdir=$apcur$line"><img border="0" src="$apageicondir/inbo1.gif" border="0" ALT="$apage{'111'}"></A></td>
                    <td align="center"><a href="apage.cgi?act=deletefolder&delfold=$line$apget"><img border="0" src="$apageicondir/tshc1.gif" border="0" ALT="$apage{'112'}"></A></td>
                  </tr>
                </table>
              </td>
              <td bgColor="$color3">&nbsp;$hour:$min, $mday/$mon/$year</td>
              <td bgColor="$color3">&nbsp;$thisfoldersize $apage{'120'}</td>
              <td bgColor="$color3" align="center"><font face="arial" size="2"><img border="0" src="$apageicondir/open.gif" ALT="$apage{'113'}"></font></td>
              <td bgColor="$color3">&nbsp;$line</td>
            </font>
            </tr>
	~;
}



foreach $line (@sortedarray) {
	$mrcount++;
	($dummy,$nline) = split(/\|/, $line);
	$line = $nline;
	$oddcount = $mrcount % 2;
	if ($oddcount eq "0") { $alterncolor = "$color5"; } else { $alterncolor = "$color6"; }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = 
           localtime((stat("$apagefullhtmldir/$line"))[8] + 3600*$timeoffset); 
	$mon++; 
	$year = 1900 + $year;
	if ($min < 10) {$min = "0" .$min; }
	$filesize = (stat("$apagefullhtmldir/$line"))[7];
	$kbfilesize = int($filesize / 1024);
	
	print qq~
          <tr>
            <font size="2">
              <td bgColor="$alterncolor" align="center">
                <table border="0" width="100%" cellspacing="0" cellpadding="0">
                  <tr>
                    <td align="center"><a href="apage.cgi?f=$line$apget"><img border="0" src="$apageicondir/mag.gif" border="0" ALT="$apage{'114'}"></A></td>
                    <td align="center"><a href="apage.cgi?act=edit&hfile=$line$apget"><img border="0" src="$apageicondir/modify.gif" border="0" ALT="$apage{'115'}"></A></td>
                    <td align="center"><a href="apage.cgi?f=$line&pre=on$apget"><img border="0" src="$apageicondir/preview.gif" border="0" ALT="$apage{'116'}"></A></td>
                    <td align="center"><a href="apage.cgi?act=rename&hfile=$line$apget"><img border="0" src="$apageicondir/move.gif" border="0" ALT="$apage{'117'}"></A></td>
                    <td align="center"><a href="apage.cgi?act=delete&hfile=$line$apget"><img border="0" src="$apageicondir/delete.gif" border="0" ALT="$apage{'118'}"></A></td>
                  </tr>
                </table>
              </td>
              <td bgColor="$alterncolor">&nbsp;$hour:$min, $mday/$mon/$year</td>
              <td bgColor="$alterncolor">&nbsp;$kbfilesize kb</td>
              <td bgColor="$alterncolor" align="center"><font face="arial" size="2"><img border="0" src="$apageicondir/pmon.gif" ALT="$apage{'119'}"></font></td>
              <td bgColor="$alterncolor">&nbsp;$line</td>
            </font>
            </tr>
	~;

}

print qq~

          </tbody>
        </table>
      </font>
      </td>
    </tr>
  </tbody>
</table>
<br>
<b>$apage{'121'}: [$mrpount]&nbsp;&nbsp; |&nbsp;&nbsp; $apage{'122'}: [$mrcount]</b><br>&nbsp;<BR></CENTER>
~;


apage_menu_bar(1);
print_bottom();
exit;
}

####################
sub edit_htm_file {
####################
check_the_user();
print_top();

open(FILE, "$apagefullhtmldir/$hfile") || error("$apagefullhtmldir/$hfile");   
file_lock(FILE); 
@lines = <FILE>; 
unfile_lock(FILE); 
close(FILE); 

if ( $htmlarea eq "1" && $info{ha} eq "1") { $on = "yes"; }
if ( $htmlarea eq "1" && $info{ha} eq "")  { $on = "yes"; }
if ( $htmlarea eq "0" && $info{ha} eq "1") { $on = "yes"; }
if ( $htmlarea eq "0" && $info{ha} eq "0") { $on = "no"; }
if ( $htmlarea eq "0" && $info{ha} eq "")  { $on = "no"; }
if ( $htmlarea eq "1" && $info{ha} eq "0") { $on = "no"; }
if ( $htmlarea eq "2" )			   { $on = "never"; }

#if ( $on eq "yes" ) {
#$thismessage = "-- <a href=\"apage.cgi?act=edit&hfile=$hfile&ha=0&apdir=$apdir\">$apage{'129'}</a>";
#htmlAreaInsert(message);
#} elsif ( $on eq "no" ) { 
#	$thismessage = "-- <a href=\"apage.cgi?act=edit&hfile=$hfile&ha=1&apdir=$apdir\">$apage{'130'}</a>"; 
#}


print qq~<form onSubmit="submitonce(this)" action="apage.cgi" method="post"> 
<input type="hidden" name="apdir" value="$apdir">
<input type="hidden" name="act" value="save">
<input type="hidden" name="hfile" value="$hfile">
<table border="0" width="100%" cellpading="0" cellspacing="0"> <tr> <td> <B>$hfile</B> $thismessage<br> 
<textarea name="message" id="message" style="width:100%" rows="25">~;
foreach $wert (@lines) { 
	print "$wert"; 
	}
print qq~</textarea></td> </tr> 
<tr><td><input type="submit" value="$btn{'022'}">&nbsp;&nbsp;<input type="reset" value="$btn{'023'}"></td> </tr> 
</table> </form> 
~; 

apage_menu_bar(2);
print_bottom();
exit;
}

###################
sub edit_txt_file {
###################
check_the_user();
print_top();

open(FILE, "$apagefullhtmldir/$hfile") || error("$apagefullhtmldir/$hfile"); 
file_lock(FILE); 
chomp(@lines = <FILE>); 
unfile_lock(FILE); 
close(FILE); 

$subject = htmltotext($lines[0]); 
$message = htmltotext($lines[1]); 

print qq~<form onSubmit="submitonce(this)" action="apage.cgi" method="post" name="creator">
<input type="hidden" name="apdir" value="$apdir">
<input type="hidden" name="act" value="save">
<input type="hidden" name="hfile" value="$hfile">
<table border="0" cellspacing="1">
<tr><td colspan="2"><CENTER><B>$hfile</B><br></CENTER></td></tr>
<tr>
<td class="formstextnormal">$msg{'037'}</td>
<td><input type="text" name="subject" value="$subject" size="55" maxlength="250"></td>
</tr>
<tr>
<td valign="top" class="formstextnormal">$msg{'038'}</td>
<td><script language="javascript" type="text/javascript">
<!--
function addCode(anystr) { 
document.creator.message.value+=anystr;
} 
function showColor(color) { 
document.creator.message.value+="[color="+color+"][/color]";
}
// -->
</script>
<textarea name="message" rows="20" cols="50">$message</textarea></td>
</tr>
<tr>
<td class="formstextnormal" valign="top"><b>$msg{'156'}</b></td>
<td valign="top"><a href="javascript:addCode('[b][/b]')"><img src="$imagesurl/forum/buttons/bold.gif" align="bottom" width="23" height="22" alt="$msg{'117'}" border="0"></a>
<a href="javascript:addCode('[i][/i]')"><img src="$imagesurl/forum/buttons/italicize.gif" align="bottom" width="23" height="22" alt="$msg{'118'}" border="0"></a>
<a href="javascript:addCode('[u][/u]')"><img src="$imagesurl/forum/buttons/underline.gif" align="bottom" width="23" height="22" alt="$msg{'119'}" border="0"></a>
<a href="javascript:addCode('[sub][/sub]')"><img src="$imagesurl/forum/buttons/sub.gif" align="bottom" width="23" height="22" alt="$msg{'544'}" border="0"></a>
<a href="javascript:addCode('[sup][/sup]')"><img src="$imagesurl/forum/buttons/sup.gif" align="bottom" width="23" height="22" alt="$msg{'545'}" border="0"></a>
<a href="javascript:addCode('[strike][/strike]')"><img src="$imagesurl/forum/buttons/strike.gif" align="bottom" width="23" height="22" alt="$msg{'546'}" border="0"></a>
<a href="javascript:addCode('[left][/left]')"><img src="$imagesurl/forum/buttons/left.gif" align="bottom" width="23" height="22" alt="$msg{'548'}" border="0"></a>
<a href="javascript:addCode('[center][/center]')"><img src="$imagesurl/forum/buttons/center.gif" align="bottom" width="23" height="22" alt="$msg{'120'}" border="0"></a><br>
<a href="javascript:addCode('[right][/right]')"><img src="$imagesurl/forum/buttons/right.gif" align="bottom" width="23" height="22" alt="$msg{'549'}" border="0"></a>
<a href="javascript:addCode('[pre][/pre]')"><img src="$imagesurl/forum/buttons/pre.gif" align="bottom" width="23" height="22" alt="$msg{'547'}" border="0"></a>
<a href="javascript:addCode('[url][/url]')"><img src="$imagesurl/forum/buttons/url.gif" align="bottom" width="23" height="22" alt="$msg{'121'}" border="0"></a>
<a href="javascript:addCode('[img][/img]')"><img src="$imagesurl/forum/buttons/img.gif" align="bottom" width="23" height="22" alt="$msg{'171'}" border="0"></a>
<a href="javascript:addCode('[email][/email]')"><img src="$imagesurl/forum/buttons/email2.gif" align="bottom" width="23" height="22" alt="$msg{'122'}" border="0"></a>
<a href="javascript:addCode('[code][/code]')"><img src="$imagesurl/forum/buttons/code.gif" align="bottom" width="23" height="22" alt="$msg{'123'}" border="0"></a>
<a href="javascript:addCode('[quote][/quote]')"><img src="$imagesurl/forum/buttons/quote2.gif" align="bottom" width="23" height="22" alt="$msg{'124'}" border="0"></a>
<a href="javascript:addCode('[list][*][*][*][/list]')"><img src="$imagesurl/forum/buttons/list.gif" align="bottom" width="23" height="22" alt="$msg{'125'}" border="0"></a><br>
<select name="color" onChange="showColor(this.options[this.selectedIndex].value)">
<option value="Black" selected>$msg{'127'}</option>
<option value="Red">$msg{'128'}</option>
<option value="Yellow">$msg{'129'}</option>
<option value="Pink">$msg{'130'}</option>
<option value="Green">$msg{'131'}</option>
<option value="Orange">$msg{'132'}</option>
<option value="Purple">$msg{'133'}</option>
<option value="Blue">$msg{'134'}</option>
<option value="Beige">$msg{'135'}</option>
<option value="Brown">$msg{'136'}</option>
<option value="Teal">$msg{'137'}</option>
<option value="Navy">$msg{'138'}</option>
<option value="Maroon">$msg{'139'}</option>
<option value="LimeGreen">$msg{'140'}</option>
</select>
</td>~;

require "$sourcedir/forum_display.pl";  smilieblock();

print qq~<tr>
<td colspan="2"><CENTER><BR>
<input type="submit" class="button" value="$btn{'022'}">
&nbsp;&nbsp;<input type="reset" class="button" value="$btn{'009'}"></CENTER></td>
</tr>
</table>
</form>
~;

apage_menu_bar(2);
print_bottom();
exit;
}


#####################
sub fix_the_txt_file {
#####################
open(FILE, "$apagefullhtmldir/$hfile") || error("$apagefullhtmldir/$hfile"); 
file_lock(FILE); 
@lines = <FILE>; 
unfile_lock(FILE); 
close(FILE); 

open (FILE,">$apagefullhtmldir/$hfile");
file_lock(FILE); 
print FILE "\n"; 
foreach $dtp ( @lines ) { 
chomp($dtp);
$messg = htmlescape($dtp);
print FILE "$messg<BR>";
}
unfile_lock(FILE); 
close(FILE); 

manage_the_pictures();

}


#####################
sub save_txt_file {
#####################
check_the_user();
print_top();

chomp($info{subject});
chomp($info{message});

$subject = htmlescape($info{subject});
$message = htmlescape($info{message});

open (FILE,">$apagefullhtmldir/$hfile");
file_lock(FILE); 
print FILE "$subject\n"; 
print FILE "$message\n"; 
unfile_lock(FILE); 
close(FILE); 

print qq~<B>$hfile</B> $apage{'131'}<P>~;
apage_menu_bar(2);
print_bottom();
exit;
}


#####################
sub save_htm_file {
#####################
check_the_user();
print_top();


chomp($info{message});
$sectioncontent = $info{message};


open (FILE,">$apagefullhtmldir/$hfile");
file_lock(FILE); 
print FILE "$sectioncontent";
unfile_lock(FILE); 
close(FILE);

print qq~
<B>$hfile</B> $apage{'132'}<P>~;
apage_menu_bar(2);
print_bottom();
exit;
}


#####################
sub view_htm_file {
#####################
print_top();
open(FILE, "$apagefullhtmldir/$f") || error("$apagefullhtmldir/$f"); 
file_lock(FILE); 
@lines = <FILE>; 
unfile_lock(FILE); 
close(FILE); 

if ($info{pre} eq "on") {
$topmessage = "<CENTER><B>viewing $f</B> <BR> <HR></CENTER>";
}

print "$topmessage\n@lines\n";

if ($info{pre} eq "on") { apage_menu_bar(2); }
print_bottom();
exit;
}


#####################
sub read_the_readme {
#####################
check_the_user();
print_top();

open(FILE, "$modDir/readme.txt") || error("$modDir/readme.txt"); 
file_lock(FILE); 
chomp(@lines = <FILE>); 
unfile_lock(FILE); 
close(FILE); 

foreach $line (@lines) {
$message = htmltotext($line); 
doubbctopic();
print qq~$message<BR>~;
}

apage_menu_bar(1);
print_bottom();
exit;
}

#####################
sub view_txt_file {
#####################
print_top();

open(FILE, "$apagefullhtmldir/$f") || error("$apagefullhtmldir/$f"); 
file_lock(FILE); 
chomp(@lines = <FILE>); 
unfile_lock(FILE); 
close(FILE); 

if ($info{pre} eq "on") { $topmessage = "<CENTER><B>$apage{'133'} $f</B> <BR> <HR></CENTER>"; }

$message = htmltotext($lines[1]); 
$subject = showhtml("$lines[0]");

doubbctopic();
dosmilies();

print qq~ $topmessage<h3>$subject</h3> $message~;

if ($info{pre} eq "on") { apage_menu_bar(2); }

print_bottom();
exit;
}

#######################
sub delete_the_folder {
#######################
check_the_user();

if ($info{confirm} ne "yes") {
print_top();
print qq~
<P><BR>$apage{'134'}<BR>
$apage{'135'}<P>
$apage{'136'} $apagehtmldir/$info{delfold}? &nbsp;&nbsp;&nbsp;
<a href="apage.cgi?act=deletefolder&delfold=$info{delfold}&confirm=yes$apget"><B>$apage{'137'}</B></a> --- 
<a href="apage.cgi?act=view$apget"><B>$apage{'138'}</B></a>
~;
apage_menu_bar(1);
print_bottom();
exit;
} else {

$imgdelcount = "0";
opendir(DIR,"$apagefullhtmldir/$info{delfold}") || die ("$apage{'100'} $apagefullhtmldir/$info{delfold}: $!\n");
local(@files) = grep(!/^\./,readdir(DIR));
closedir DIR;
if (@files > 0) { error ("$apagefullhtmldir/$info{delfold} $apage{'139'}.<BR> $apage{'140'}.\n"); }

opendir(DIR,"$apageimagedir/$info{delfold}") || die ("$apage{'141'} $apageimagedir/$info{delfold}: $!\n");
local(@files) = grep(!/^\./,readdir(DIR));
closedir DIR;

foreach $imagefile (@files) { unlink("$apageimagedir/$info{delfold}/$imagefile"); $imgdelcount++; }

rmdir("$apagefullhtmldir/$info{delfold}");
rmdir("$apageimagedir/$info{delfold}");
$apagemessage = "$apagehtmldir/$info{delfold} $apage{'143'} $apageshortimagedir$info{delfold} $apage{'142'}.<BR>";
view_the_files();
}
}

#####################
sub delete_the_file {
#####################
check_the_user();
if ($info{confirm} ne "yes") {
print_top();
print qq~
<P><BR>$apage{'144'} $hfile? &nbsp;&nbsp;&nbsp;
<a href="apage.cgi?act=delete&hfile=$hfile&confirm=yes$apget"><B>$apage{'145'}</B></a> --- 
<a href="apage.cgi?act=view$apget"><B>$apage{'146'}</B></a>
~;
apage_menu_bar(1);
print_bottom();
exit;
} else {
unlink("$apagefullhtmldir/$hfile");
$apagemessage = "$hfile deleted<BR>";
view_the_files();
}
}


#####################
sub rename_the_file {
#####################
check_the_user();
print_top();

print qq~<form onSubmit="submitonce(this)" action="apage.cgi" method="post">
<input type="hidden" name="apdir" value="$apdir">
<input type="hidden" name="act" value="renamed">
<input type="hidden" name="ofile" value="$hfile">
<table border="0" width="100%" cellpading="0" cellspacing="0"> <tr> <td> 
<B>$apage{'147'}</B><br>
$apage{'148'}<BR>
$apage{'149'}<BR>
$apage{'150'}<BR>
$apage{'151'}<BR>
$apage{'152'}<BR>
<input type="text" size="40" name="hfile" value="$hfile">  
<input type="submit" value="$btn{'022'}">&nbsp;&nbsp;<input type="reset" value="$btn{'023'}"></td> </tr> 
</table> </form> 
~; 

apage_menu_bar(1);
print_bottom();
exit;
}

#####################
sub add_the_file {
#####################
check_the_user();
print_top();

print qq~<form onSubmit="submitonce(this)" action="apage.cgi" method="post"> 
<input type="hidden" name="apdir" value="$apdir">
<input type="hidden" name="act" value="newfile">
<input type="hidden" name="hfile" value="$hfile">
<table border="0" width="100%" cellpading="0" cellspacing="0"> <tr> <td> 
<B>$apage{'153'}</B><br>
$apage{'154'}<BR>
$apage{'155'} <BR>
$apage{'156'}<BR>
<input type="text" size="40" name="hfile" value="$hfile">  
<input type="submit" value="$btn{'022'}">&nbsp;&nbsp;<input type="reset" value="$btn{'023'}"></td> </tr> 
</table> </form> 
~; 

apage_menu_bar(1);
print_bottom();
exit;
}




#####################
sub creat_a_dir {
#####################
check_the_user();
print_top();

print qq~<form onSubmit="submitonce(this)" action="apage.cgi" method="post"> 
<input type="hidden" name="apdir" value="$apdir">
<input type="hidden" name="act" value="newdir">
<table border="0" width="100%" cellpading="0" cellspacing="0"> <tr> <td> 
<B>$apage{'157'}</B><br>
$apage{'158'} <BR>
$apage{'159'} <b>$apagehtmldir</b> $apage{'160'}<BR>
<input type="text" size="40" name="newfoldname" value="">  
<input type="submit" value="$btn{'022'}">&nbsp;&nbsp;<input type="reset" value="$btn{'023'}"></td> </tr> 
</table> </form> 
~; 

apage_menu_bar(1);
print_bottom();
exit;
}

#####################
sub save_a_dir {
#####################
check_the_user();

if ($info{newfoldname} =~ /\W/ ) { error("$apage{'161'}"); }

if (-d "$apagefullhtmldir/$info{newfoldname}") 
{
	error("$apage{'162'} <B>$apagefullhtmldir/$info{newfoldname}</B> $apage{'163'}.");
} 
elsif (-d "$apageimagedir/$info{newfoldname}")
{
	error("$apage{'162'} <B>$apageimagedir/$info{newfoldname}</B> $apage{'163'}.");
}

mkdir("$apagefullhtmldir/$info{newfoldname}", 0777);
chmod( 0777, "$apagefullhtmldir/$info{newfoldname}");
mkdir("$apageimagedir/$info{newfoldname}", 0777);
chmod( 0777, "$apageimagedir/$info{newfoldname}");
$apagemessage ="$apage{'164'} $apagehtmldir/$info{newfoldname} $apage{'143'} $apageshortimagedir/$info{newfoldname}.<P>";
view_the_files();

}




#####################
sub renamed_the_file {
#####################
check_the_user();
print_top();

if ($hfile !~ /.txt$/ && $hfile !~ /.htm$/ &&$hfile !~ /.html$/ ) { print qq~Bad file name<br>~; } 
elsif ($hfile eq ".txt" || $hfile eq ".htm" || $hfile eq ".html" || $hfile =~ / /) { print qq~Bad file name<br>~; } 
else {

open(FILE, "$apagefullhtmldir/$ofile") || error("$apagefullhtmldir/$ofile"); 
file_lock(FILE); 
@lines = <FILE>;
unfile_lock(FILE); 
close(FILE); 

unlink("$apagefullhtmldir/$ofile");

open(FILE, ">$apagefullhtmldir/$hfile") || error("$apagefullhtmldir/$hfile"); 
file_lock(FILE); 
print FILE @lines;
unfile_lock(FILE); 
close(FILE); 
print qq~$apage{'165'} <B>$ofile</B> to <B>$hfile</B>.<BR>~; 
}

apage_menu_bar(1);
print_bottom();
exit;
}


#####################
sub new_the_file {
#####################
check_the_user();
print_top();

if ($hfile !~ /.txt$/ && $hfile !~ /.htm$/ &&$hfile !~ /.html$/ ) { print qq~Bad file name<br>~; } 
elsif ($hfile eq ".txt" || $hfile eq ".htm" || $hfile eq ".html" || $hfile =~ / /) { print qq~Bad file name<br>~; } 
else {

open(FILE, ">$apagefullhtmldir/$hfile") || error("$apagefullhtmldir/$hfile"); 
file_lock(FILE); 
print FILE " ";
unfile_lock(FILE); 
close(FILE); 
print qq~
$apage{'166'} - $hfile.<BR>
$apage{'167'}<BR>
~; 
}

apage_menu_bar(2);
print_bottom();
exit;
}

#########################
sub manage_the_pictures {
#########################
check_the_user();
opendir(DIR,"$apageimagedir") || die ("$apage{'100'} $apageimagedir: $!\n");
local(@files) = grep(!/^\./,readdir(DIR));
closedir DIR;
$mrcount=0;

foreach $gl (@files) {
	if ($gl =~ /.gif$/ || $gl =~ /.jpg$/ || $gl =~ /.jpeg$/ || $gl =~ /.GIF$/ || $gl =~ /.JPG$/ || $gl =~ /.JPEG$/ || $gl =~ /.png$/ || $gl =~ /.PNG$/ ) {
push (@newlist,"$gl");
$mrcount++;
 }
}

print "Content-type: text/html\n\n";
print "<html><head><title>$apage{'168'}</title></head><body>\n";
print qq~
<script language="javascript" type="text/javascript">
<!--
function addCode(anystr) { 
document.creator.picurl.value="<IMG SRC=\'"+anystr+"\'>";
} 
// -->
</script>
<CENTER>~;
if ($info{message} ne "") { print "Your upload was a <b>$info{message}</b>."; }
if ($delmess ne "") { print "$delmess"; }

print qq~
<table cellspacing="0" cellpadding="2" style="border: 1 solid black">
<tr><th nowrap align="left" bgcolor="$color2" style="border-bottom: 1 solid black" height="20">
<font size="3" color="$color1"><b>$apage{'169'}:</b> $apdir</font></tr>
<tr><td align="center"><BR>
<font face="Arial" size="2">$apage{'169'}(.jpg , .gif , .htm, .txt)</font><BR>
<form onSubmit="submitonce(this)" action="apage-upload.cgi" method="post" enctype="multipart/form-data">
<input type="hidden" name="apdir" value="$apdir">
&nbsp;&nbsp;<input type="File" name="FILE1">&nbsp;&nbsp;
<br><input type="Submit" value="$apage{'170'}">
</form><hr></font></tr><tr><td align="center"> ~;
if ( $mrcount eq "0" ) { print "$apage{'171'} <BR>$apage{'172'}.<BR> <BR>"; }
else { print qq~
<form onSubmit="submitonce(this)" action="apage.cgi" name="creator" method="get">
<input type="hidden" name="apdir" value="$apdir">
<input type="hidden" name="act" value="deleteimage">
$mrcount Current Picture(s):<br>
<select name="myDestination">~;
foreach $ft (@newlist) { print "<option value=\"$apageimageurl/$ft\">$ft</option> \n "; }
print qq~</select><BR>
<input type="button" value="$apage{'173'}"
    onclick="ob=this.form.myDestination;window.open(ob.options[ob.selectedIndex].value,'hi','status=1,scrollbars=1,resizable=1,width=400,height=300')">
<input type="submit" value="$apage{'174'}" name="delete">
<input type="button" value="$apage{'175'}" name="getcode" 
    onclick="javascript:addCode(this.form.myDestination.options[this.form.myDestination.selectedIndex].value)">
<BR><input type="text" name="picurl" size="30"></form>~;}
print qq~</tr></table></CENTER><BR>
$dtp
~;
print "</body></html>\n";
exit;
}

######################
sub delete_the_image {
######################
check_the_user();
@picparts = split(/\//, $info{myDestination});
$pic = pop(@picparts);
$picname = $pic;
unlink("$apageimagedir/$pic");
$delmess = "$apage{'176'} <B>$picname</B> $apage{'177'}.<BR>";
manage_the_pictures();
}


#######################
sub aset_the_settings {
#######################
	if ($action eq "apage.dat") {
		check_the_user();
		print_top();
		$settings_file = "apage.dat";
		$return_url = "apage.cgi?act=view";
		require "aset.cgi";
		aset_set_settings();
		print_bottom();
		exit;
	}

	if ($action eq "$modlang.dat") {
		check_the_user();
#		print_top();
#		$settings_file = "language/$modlang.dat";          
#		$return_url = "apage.cgi";
		$locations = "aset.cgi?selected_return_url=apage.cgi&selected_settings_file=language/$modlang.dat";
		print "Location: $locations\n\n";
#		require "aset.cgi";
#		aset_set_settings();
#		print_bottom();
		exit;
	}
} #close aset_the_settings



#####################
sub apage_menu_bar {
#####################
$in = "@_";
print qq~
<script language="javascript" type="text/javascript">
<!--
function winopen() {
window.open("apage.cgi?act=pic$apget","","width=300,height=370,scrollbars")
}
// -->
</script>
<P><table border="0" cellpadding="0" cellspacing="0" width="100%"  class="navbar" bgcolor="$color4"> 
<tr>  
<td width="" align="center">&nbsp;<a href="apage.cgi?act=view$apget"  class="nav">$apage{'123'}</a>&nbsp;</td> ~;
if ($in eq "1" || $in eq "2") { print qq~ 
<td width="" align="center">&nbsp;<a href="apage.cgi?act=add$apget" class="nav">$apage{'124'}</a>&nbsp;</td> ~; }
if ($in eq "1") { print qq~ 
<td width="" align="center">&nbsp;<a href="apage.cgi?act=createdir$apget" class="nav">$apage{'125'}</a>&nbsp;</td> ~; }
if ($in eq "2") { print qq~ 
<td width="" align="center">&nbsp;<a href="apage.cgi?act=edit&hfile=$hfile$apget" class="nav">$apage{'126'}</a>&nbsp;</td>~; }
if ($in eq "2") { print qq~ 
<td width="" align="center">&nbsp;<a href="apage.cgi?f=$hfile&pre=on$apget" class="nav">$apage{'127'}</a>&nbsp;</td>~; }
if ($in ne "9") { print qq~ 
<td width="" align="center">&nbsp;<a href="javascript:winopen()" class="nav">$apage{'128'}</a>&nbsp;</td> ~; }
print qq~</tr> </table>~;
}



#####################
sub check_the_user {
#####################
$member = lc $username;
open(FILE, "$memberdir/$member.dat");
file_lock(FILE);
chomp(@members = <FILE>);
unfile_lock(FILE);
close(FILE);

if ($username ne "admin" && $members[7] ne "Administrator" && $extradmin !~ /(^|,)$username(,|$)/ ) { error("$err{'011'}"); }
}

#########################
sub ascend { $a <=> $b; }
sub decend { $b <=> $a; }
#########################

#####################
sub end_txt_script {
#####################
print_top();
print "$apage{'178'}";
print_bottom();
exit;
} #close end_txt_script


###########################################################################
###########################################################################
############################## End Of APage! ##############################
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
<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
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

