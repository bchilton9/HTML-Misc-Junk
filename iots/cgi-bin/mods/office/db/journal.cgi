#!/usr/bin/perl 
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

# ----------------------------------------------------------------------------
# Based on instantmessage.pl in WebAPP 0.9.6
#
# LEGAL DISCLAIMER:
# This software is provided as-is.  Use it at your own risk.  The
# author takes no responsibility for any damages or losses directly
# or indirectly caused by this software.
# ----------------------------------------------------------------------------

# written by Brad (webmaster@indie-central.ca)

### the following must be correct or else this script won't work ###
require "../../config.pl"; # main WebAPP config

# do not modify anything below this line unless you know what you are doing!

$officeURL = "$scripturl/mods/office";
$imgURL = "$imagesurl/office";
$officeDIR = "$scriptdir/mods/office";
$dbdir = "$officeDIR/db";
$office_cfg = "$dbdir/office.cfg";
$this_cgi = "$officeURL/journal.cgi";

push(@INC,$scriptdir);
use vsLock;
use vsDB;
use CGI;

$scriptname = "Journal";
$scriptver = "0.9.6";

eval {
	require "$sourcedir/subs.pl"; # main WebAPP subs
	require "$dbdir/office.pl"; # some office subs
	require "$officeDIR/config.dat"; # dat file for mod manager

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
	<p>If this problem persits, please contact the webmaster and inform them about the date and time that you recieved this error.</p>
~;
	exit;
}

# WebAPP stuff #
getlanguage();
ban();
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if ($lang_support eq "1") { mod_langsupp(); } 

if ($username eq $anonuser) { error("$office_error{'001'}"); }

# Member-specific definitions for this module #
$user_dir = "$dbdir/$username";
$journal_dir = "$user_dir/journal";

$index_template = "$dbdir/index.html";

# do a quick check to see if the member has used their office before
# if not, then create the necessary subdirectory and config/db files
# use redundant checking for each file, just in case a particular file was deleted

# step one: user directory for db files
unless (-e("$user_dir")) {
	mkdir("$user_dir",0777);
	chmod(0777,"$user_dir");
}


unless (-e("$journal_dir")) { 
	mkdir("$journal_dir",0777);
	chmod(0777,"$journal_dir");
}

# step two: index file to hide db from browser
#unless (-e("$user_dir/index.html")) { 	
#	open (FILE, "<$index_template") || error("$office_error{'002'} $index_template"); 
#		file_lock(FILE);
#		@ind = <FILE>;
#		unfile_lock(FILE);
#	close (FILE);

#	open(FILE, ">$user_dir/index.html") || error("$office_error{'003'} $user_dir/index.html"); 
#		file_lock(FILE);
#		print FILE @ind;
#		unfile_lock(FILE);
#	close(FILE);
#}

# step three: check to see if this user appears in the office user list

$listed = 0;
open (USERS,"$dbdir/office.users");
	file_lock(USERS);
	while(<USERS>) {
		chop;
		@allnames = split(/\n/);
		if (grep (/\b^$username\b/i, @allnames) ne "0" ) { 
			$listed = 1;
		}
	}
	unfile_lock(USERS);
close(USERS);
				
if ($listed == 0) {
	open(FILE, "$dbdir/office.users"); 
		file_lock(FILE); 
		@users = <FILE>; 
		unfile_lock(FILE); 
	close(FILE); 
	
	open(FILE, ">$dbdir/office.users"); 
		file_lock(FILE); 
		foreach $curuser(@users) { print FILE "$curuser"; } 
		print FILE "$username\n"; 
		unfile_lock(FILE); 
	close(FILE); 
}



# done db file check


# Colour defintions

my ($objConfig) = new vsDB(
	file => $office_cfg,
	delimiter => "\t",
);

if (!$objConfig->Open) {print $objConfig->LastError; exit 1;};
my ($headerColor) = $objConfig->FieldValue("HeaderColor");
my ($dataDarkColor) = $objConfig->FieldValue("DataDarkColor");
my ($dataLightColor) = $objConfig->FieldValue("DataLightColor");
my ($dataHighlightColor) = $objConfig->FieldValue("DataHighlightColor");
$objConfig->Close;
undef($objConfig);

my ($scriptName) = $ENV{'SCRIPT_NAME'} || "journal.cgi";
my ($objCGI) = new CGI;

if ($action eq "edit") { edit(); }
elsif ($action eq "add2") { add2(); }
elsif ($action eq "modify2") { modify2(); }
elsif ($action eq "email_entry2") { email_entry2(); }
elsif ($action eq "remove") { remove(); }
elsif ($action eq "print") { print_entry(); }
else { 

# print out the journal index

$navbar = "$office_gen{'023'} $username\'s Journal";
print_top();

top_navbar_journal($headerColor);

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
close(FILE);

$jmsgid = $info{"id"};
$todo = $info{"op"};

print qq~

<table cellspacing="0" cellpadding="2" border="0" width="100%">
<tr>
<td valign="top" align="center">
~;
if ($todo eq "email") { }
else {
print qq~
<div align="right"><a href="#toc"><font size="1"><b>$office_journal{'009'}</b></font></a></div><BR>
~; 
}

# now we start the main guts of the table - the entry

# what are we doing? viewing, modifying, or adding a new entry?

if ($jmsgid ne "") {
	if ($todo eq "modify") { modify(); }
	elsif ($todo eq "email") { email_entry(); }
	else { view(); }
}
else { add(); }

print qq~</td>
</tr>
<tr>
<td valign="top" align="center">
<table width="100%" border="0" cellspacing="0" cellpadding="2">
<tr>
<td bgcolor="$dataDarkColor" align="center"><font size="1"><b>$office_journal{'009'}</b></font></td>
</tr>
~;

if (@entries == 0) {
	print qq~
	<tr>
		<td colspan="3" bgcolor="$dataLightColor"><font size="1">$office_journal{'006'}</font></td>
	</tr>~;
}

print qq~
<tr><td bgcolor="$dataDarkColor">
<a name="toc"><table width="100%" cellpadding="0" cellspacing="1"></a>
~;
	
$second = "$dataLightColor";

sort {$b[5] <=> $a[5]} @entries;

for ($a = 0; $a < @entries; $a++) {
	if ($second eq "$dataLightColor") { 
		$second="$dataLightColor"; 
	}
	else { 
		$second="$dataLightColor"; 
	}
	
	($jsub[$a], $jldate[$a], $jsdate[$a], $jmessageid[$a], $jfilenum[$a]) = split(/\|/, $entries[$a]);	
	
	$curid = "$jmessageid[$a]";
	$curfile = "$jfilenum[$a]";
	$curfile =~ s/\n//g;
	
	open(ENTRY, "$journal_dir/$curfile.txt") || error("$office_error{'002'} $journal_dir/$curfile.txt"); 
		file_lock(ENTRY);
		chomp($text = <ENTRY>);
		unfile_lock(ENTRY);
	close(ENTRY);
	($message, $moddate) = split(/\|/, $text);
	$tempmessage = substr($message,0,75);
	$tempmessage .= "...";
	
	$message = $tempmessage;
	if ($enable_ubbc) { doubbc(); }
	$tempmessage = $message;
					
	if ($jmessageid[$a] < 100) { 
		$jmessageid[$a] = $a; 
	}
	
	$title = "$jsub[$a]";
	
	if ($enable_ubbc) { doubbc(); }
	if ($enable_smile) { dosmilies(); }
			
	if (length($title) > 12) { 
		$title = substr($title,0,12); 
		$title .= "...";
	}
			
	if ($title eq "") {
		$title="$office_journal{'017'}"; 
	}
		
	if ($jmsgid == $curid) {
		$second = "$dataHighlightColor";
	}
	
	print qq~
	<tr>
	<td bgcolor="$second" width="10%"><font size="1">&nbsp;$jsdate[$a]</font></td>
	<td bgcolor="$second" width="20%"><font size="1"><a href="$this_cgi?action=view&amp;id=$jmessageid[$a]">&nbsp;$title</a></font></td>
	<td bgcolor="$second" width="70%"><font size="1">&nbsp;$tempmessage</font></td>
	</tr>
	~;	
}

print qq~
</table></td></tr>
<tr><td align="center" bgcolor="$dataDarkColor"><font size="1"><i><a href="$this_cgi">$office_journal{'002'}</a></i></font></td></tr>
</table>

~; # so ends the toc table

print qq~
</td></tr>
</table>
<BR>~;

bottom_nav();

print_bottom();

undef($objDB);
undef($objLock);
undef($objCGI);

} # end sub


#############
sub view {
#############		

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = (<FILE>);
	unfile_lock(FILE);
close(FILE);

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	foreach $entry (@entries) {
		chomp $entry;
		($subject, $ldate, $sdate, $msgid, $filenum) = split(/\|/, $entry);
		if ($jmsgid == $msgid) {
			open(ENTRY, "$journal_dir/$filenum.txt");
				file_lock(ENTRY);
				chomp($text = <ENTRY>);
				unfile_lock(ENTRY);
			close(ENTRY);
			($message, $moddate) = split(/\|/, $text);
			$thissubject = $subject;
			$thisdate = $ldate;
			$thisid = $msgid;
		}
	}
	unfile_lock(FILE);
close(FILE);

# all the language fields and icons for UBBC and Smilies are
# grabbed from the main WebAPP cfg
if ($enable_ubbc) { doubbc(); }
if ($enable_smile) { dosmilies(); }

print qq~

<table width="100%" bgcolor="$headerColor" border="0" cellspacing="0" cellpadding="3">
<tr>
    <td bgcolor="$dataDarkColor">&nbsp;<font size="2"><b>$thissubject</b></font></td>
    <td align="right" bgcolor="$dataDarkColor"><font size="1">$thisdate</font></td>
</tr>
<tr>
    <td colspan="2" bgcolor="$dataLightColor" class="newstextsmall"><BR>$message<BR><BR></td>
</tr>
<tr>
    <td bgcolor="$dataDarkColor">~;
	# has this file been modified?
	if ($moddate eq "") { 
		print qq~&nbsp;~; 
	}
	else {
		print qq~<font size="1">&nbsp;$office_journal{'010'} $moddate</font>~;
	}
	print qq~
	</td>
    <td bgcolor="$dataDarkColor" align="right">
		<a href="$this_cgi?action=print&amp;id=$thisid"><img src="$imgURL/print.gif" border="0" alt="$office_gen{'020'}" align="absmiddle"></a>&nbsp;
		<a href="$this_cgi?action=view&amp;id=$thisid&amp;op=modify"><img src="$imgURL/modify.gif" alt="$office_journal{'011'}" border="0" align="absmiddle"></a>&nbsp;
		<a href="$this_cgi?action=remove&amp;id=$thisid"><img src="$imgURL/delete.gif" alt="$office_journal{'012'}" border="0" align="absmiddle"></a></td>
</tr>
</table>
<br>
~;
# <a href="$this_cgi?action=view&amp;id=$thisid&amp;op=email"><img src="$imgURL/email.gif" border="0" alt="$office_journal{'003'}" align="absmiddle"></a>&nbsp;

} # end view message sub


#############
sub modify {
#############		

open(FILE, "<$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = (<FILE>);
	foreach $entry (@entries) {
		chomp $entry;
		($modsubj, $modldate, $modsdate, $modid, $modfile) = split(/\|/, $entry);
		if ($jmsgid == $modid) {
			open(FILE2, "$journal_dir/$modfile.txt");
				file_lock(FILE2);
				chomp($origmessage = <FILE2>);
				unfile_lock(FILE2);
			close(FILE2);
			($message, $moddate) = split(/\|/, $origmessage);
			$thismessage = htmltotext($message);
			$thissubject = $modsubj;
			$thisid = $modid;
			$thisfile = $modfile;
		}
	}
	unfile_lock(FILE);
close(FILE);

print qq~
<form action="$this_cgi?action=modify2" method="post" name="creator">
<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
	<td>
	<input name="journalid" value="$thisid" type="hidden">
	<input name="filename" value="$thisfile" type="hidden">
	<center>
	<table border="0" cellspacing="1" align="center">
	<tr>
		<td valign="top"><b>$office_journal{'013'}</b><BR>
		<input type="text" name="title" size="40" maxlength="50" value="$thissubject"></td>
	</tr>
	<tr>
		<td valign="top"><b>$office_journal{'014'}</b><BR>
		<script language="javascript" type="text/javascript">
<!--
function addCode(anystr) { 
document.creator.entry.value+=anystr;
} 
function showColor(color) { 
document.creator.entry.value+="[color="+color+"][/color]";
}
// -->
</script>
		<textarea name="entry" rows="20" cols="55" wrap="virtual">$thismessage</textarea></td>
	</tr>
	<tr>
		<td valign="middle">
		<input type="submit" value="$office_journal{'015'}" class="button">&nbsp;
		<input type="reset" value="$office_gen{'009'}" class="button"></td>
	</tr>
	</table>
	~;
		if ($enable_ubbc eq "1") { 
			print "<P>";
			ubbcblock();
		}
		if ($enable_smile) { 
			print "<P>";
			smilieblock(); 
		}
		print qq~
	</center>
	</td>
</tr>
</table>
</form>
~;

} # end modify message sub

##############
sub modify2 {
##############

$to_modify = $input{'journalid'};
$to_file = $input{'filename'};
$mod_title = htmlescape($input{'title'});
$mod_entry = htmlescape($input{'entry'});
	
if ($username eq "$anonuser") { error("$err{'011'}"); }

open(FILE, "<$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
close(FILE);

# first modify the index
open(FILE, ">$journal_dir/$username.idx") || error("$office_error{'005'} $journal_dir/$username.idx"); 
	file_lock(FILE);
	for ($a = 0; $a < @entries; $a++) {
		($origsubj, $origldate, $origsdate, $origid, $origfile) = split(/\|/, $entries[$a]);
		if ($origid < 100 ) {
			if($a ne $to_modify) { print FILE "$entries[$a]"; }
		}
		else {
			if(!($origid =~ /$to_modify/)) { 
				print FILE "$entries[$a]"; 
			}
			else {
				# no need to put a new line in after writing... 
				# I think it carries it over from the orig entry in the db
				print FILE "$mod_title|$origldate|$origsdate|$origid|$origfile";
				$mod_file = $origfile;
				$return_id = $origid;
			}
		}
	}
	unfile_lock(FILE);
close(FILE);

# then modify the entry -- but first back it up!
# maybe you'll actually be able to restore a backup in the next version ;-)

open (FILE, "<$journal_dir/$to_file.txt") || error("$office_error{'002'} $journal_dir/$to_file.txt"); 
	file_lock(FILE);
	@guts = <FILE>;
	unfile_lock(FILE);
close (FILE);

open(FILE, ">$journal_dir/$to_file.bak") || error("$office_error{'003'} $journal_dir/$to_file.bak"); 
	file_lock(FILE);
	print FILE @guts;
	unfile_lock(FILE);
close(FILE);

open(FILE, ">$journal_dir/$to_file.txt");
	file_lock(FILE);
	print FILE "$mod_entry|$date"; 
	unfile_lock(FILE);
close(FILE);

print "Location: $this_cgi\?action=view\&id=$return_id\n\n";

}

##############
sub remove {
##############
	
if ($username eq "$anonuser") { error("$err{'011'}"); }

open(FILE, "<$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
close(FILE);

# first remove the entry
open(FILE, ">$journal_dir/$username.idx");
	file_lock(FILE);
	for ($a = 0; $a < @entries; $a++) {
		($subj, $ldate, $sdate, $theid, $thefile) = split(/\|/, $entries[$a]);
		if ($theid < 100 ) {
			if($a ne $jmsgid) { print FILE "$entries[$a]"; }
		}
		else {
			if(!($theid =~ /$info{'id'}/)) { 
				print FILE "$entries[$a]"; 
			}
			else {
				$to_del = $thefile;
				$to_del =~ s/\n//g;
			}
		}
	}
	unfile_lock(FILE);
close(FILE);

# then delete the file
unlink("$journal_dir/$to_del.txt") || error("$office_error{'005'} $journal_dir/$thefile.txt"); 
# and delete the backup if it exists
if (-e("$journal_dir/$to_del.bak")) { unlink("$journal_dir/$to_del.bak") }

print "Location: $this_cgi\n\n";

}

############
sub add {
############

$mid = time; 
getdate();

open(FILE, "<$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
close(FILE);
	
$short = "$mon_num.$mday.$year";

print qq~
<center>
<form action="$this_cgi?action=add2" method="post" name="creator">
<table width="100%" border="0" cellspacing="0" cellpadding="1" align="center">
<tr>
	<td>
	<input name="journalid" value="$mid" type="hidden">
	<input name="ldate" value="$date" type="hidden">
	<input name="sdate" value="$short" type="hidden">
	<center>
	<table border="0" cellspacing="1" cellpadding="3" align="center">
	<tr>
		<td><b>$office_journal{'013'}</b><BR>
		<input type="text" name="title" size="40" maxlength="50"></td>
	</tr>
	<tr>
		<td valign="top"><b>$office_journal{'014'}</b><BR>
		<script language="javascript" type="text/javascript">
<!--
function addCode(anystr) { 
document.creator.entry.value+=anystr;
} 
function showColor(color) { 
document.creator.entry.value+="[color="+color+"][/color]";
}
// -->
</script>
		<textarea name="entry" rows="20" cols="55" wrap="virtual"></textarea></td>
	</tr>
	<tr>
		<td valign="middle">
		<input type="submit" value="$office_journal{'016'}" class="button">&nbsp;
		<input type="reset" value="$office_gen{'009'}" class="button"></td>
	</tr>
	</table>~;
		if ($enable_ubbc eq "1") { 
			print "<P>";
			ubbcblock();
		}
		if ($enable_smile) { 
			print "<P>";
			smilieblock(); 
		}
print qq~
	</center>
	</td>
</tr>
</table>
</form>
</center>
~;

}

#############
sub add2 {
#############

error("$err{'014'}") unless($input{'title'});
error("$err{'015'}") unless($input{'entry'});

$messageid = $input{'journalid'};
$title = htmlescape($input{'title'});
$entry = htmlescape($input{'entry'});
$ldate = $input{'ldate'};
$sdate = $input{'sdate'};

# first update the user's journal index file

open (FILE, "<$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
close (FILE);

opendir (DIR, "$journal_dir");
	@files = readdir(DIR);
closedir (DIR);
@files = grep(/txt/,@files);
@files = reverse(sort { $a <=> $b } @files);
$postnum = @files[0];
$postnum =~ s/.txt//;
$postnum++;

open (FILE, ">$journal_dir/$username.idx");
	file_lock(FILE);
	print FILE "$title|$ldate|$sdate|$messageid|$postnum\n";
	foreach $entry (@entries) { print FILE "$entry"; }
	unfile_lock(FILE);
close(FILE);

open (FILE, ">>$journal_dir/$postnum.txt");
	file_lock(FILE);
	print FILE "$entry";
	unfile_lock(FILE);
close(FILE);

print "Location: $this_cgi\?action=view\&id=$messageid\n\n";
exit;

}

####################
sub smilieblock {
####################

print qq~
<center>
<table border="0" cellspacing="0" cellpadding="2" align="center">
<tr>
<td bgcolor="$dataDarkColor" align="left" valign="middle">
&nbsp;<b>$msg{'533'}</b></td>
</tr>
<tr><td bgcolor="$dataDarkColor">
<table width="100%" cellpadding="2" cellspacing="1">
<tr>
<td bgcolor="$dataLightColor" align="left" valign="middle">
<a href="javascript:addCode('[bones]')"><img src="$imagesurl/forum/buttons/bones.gif" border="0" alt="$msg{'498'}" align="absmiddle"></a>
<a href="javascript:addCode('[confused]')"><img src="$imagesurl/forum/buttons/confused.gif" border="0" alt="$msg{'499'}" align="absmiddle"></a>
<a href="javascript:addCode('[cool]')"><img src="$imagesurl/forum/buttons/cool.gif" border="0" alt="$msg{'500'}" align="absmiddle"></a>
<a href="javascript:addCode('[cry]')"><img src="$imagesurl/forum/buttons/cry.gif" border="0" alt="$msg{'501'}" align="absmiddle"></a>
<a href="javascript:addCode('[eek]')"><img src="$imagesurl/forum/buttons/eek.gif" border="0" alt="$msg{'502'}" align="absmiddle"></a>
<a href="javascript:addCode('[evil]')"><img src="$imagesurl/forum/buttons/evil.gif" border="0" alt="$msg{'503'}" align="absmiddle"></a>
<a href="javascript:addCode('[frown]')"><img src="$imagesurl/forum/buttons/frown.gif" border="0" alt="$msg{'504'}" align="absmiddle"></a>
<a href="javascript:addCode('[grin]')"><img src="$imagesurl/forum/buttons/grin.gif" border="0" alt="$msg{'505'}" align="absmiddle"></a>
<a href="javascript:addCode('[bounce]')"><img src="$imagesurl/forum/buttons/bounce.gif" border="0" alt="$msg{'506'}" align="absmiddle"></a>
<a href="javascript:addCode('[lol]')"><img src="$imagesurl/forum/buttons/lol.gif" border="0" alt="$msg{'507'}" align="absmiddle"></a>
<a href="javascript:addCode('[mad]')"><img src="$imagesurl/forum/buttons/mad.gif" border="0" alt="$msg{'508'}" align="absmiddle"></a>
<a href="javascript:addCode('[nonsense]')"><img src="$imagesurl/forum/buttons/nonsense.gif" border="0" alt="$msg{'509'}" align="absmiddle"></a>
<a href="javascript:addCode('[oops]')"><img src="$imagesurl/forum/buttons/oops.gif" border="0" alt="$msg{'510'}" align="absmiddle"></a>
<a href="javascript:addCode('[rolleyes]')"><img src="$imagesurl/forum/buttons/rolleyes.gif" border="0" alt="$msg{'511'}" align="absmiddle"></a>
<a href="javascript:addCode('[smile]')"><img src="$imagesurl/forum/buttons/smile.gif" border="0" alt="$msg{'512'}" align="absmiddle"></a>
<a href="javascript:addCode('[tongue]')"><img src="$imagesurl/forum/buttons/tongue.gif" border="0" alt="$msg{'513'}" align="absmiddle"></a>
<a href="javascript:addCode('[wink]')"><img src="$imagesurl/forum/buttons/wink.gif" border="0" alt="$msg{'514'}" align="absmiddle"></a>
<a href="javascript:addCode('[ninja]')"><img src="$imagesurl/forum/buttons/ninja.gif" border="0" alt="$msg{'515'}" align="absmiddle"></a>
</td>
</tr>
</table></td>
</tr>
</table>
</center>
~;

}


####################
sub ubbcblock {
####################

print qq~
<center>
<table border="0" cellspacing="0" cellpadding="2" align="center">
<tr>
<td bgcolor="$dataDarkColor" align="left" valign="middle">
&nbsp;<b>$msg{'156'}</b></td>
</tr>
<tr><td bgcolor="$dataDarkColor">
<table width="100%" cellpadding="2" cellspacing="1">
<tr>
<td bgcolor="$dataLightColor" align="left" valign="middle">
<a href="javascript:addCode('[b][/b]')"><img src="$imagesurl/forum/buttons/bold.gif" align="absmiddle" width="23" height="22" alt="$msg{'117'}" border="0"></a>
<a href="javascript:addCode('[i][/i]')"><img src="$imagesurl/forum/buttons/italicize.gif" align="absmiddle" width="23" height="22" alt="$msg{'118'}" border="0"></a>
<a href="javascript:addCode('[u][/u]')"><img src="$imagesurl/forum/buttons/underline.gif" align="absmiddle" width="23" height="22" alt="$msg{'119'}" border="0"></a>
<a href="javascript:addCode('[sub][/sub]')"><img src="$imagesurl/forum/buttons/sub.gif" align="absmiddle" width="23" height="22" alt="$msg{'544'}" border="0"></a>
<a href="javascript:addCode('[sup][/sup]')"><img src="$imagesurl/forum/buttons/sup.gif" align="absmiddle" width="23" height="22" alt="$msg{'545'}" border="0"></a>
<a href="javascript:addCode('[strike][/strike]')"><img src="$imagesurl/forum/buttons/strike.gif" align="absmiddle" width="23" height="22" alt="$msg{'546'}" border="0"></a>
<a href="javascript:addCode('[left][/left]')"><img src="$imagesurl/forum/buttons/left.gif" align="absmiddle" width="23" height="22" alt="$msg{'548'}" border="0"></a>
<a href="javascript:addCode('[center][/center]')"><img src="$imagesurl/forum/buttons/center.gif" align="absmiddle" width="23" height="22" alt="$msg{'120'}" border="0"></a>
<a href="javascript:addCode('[right][/right]')"><img src="$imagesurl/forum/buttons/right.gif" align="absmiddle" width="23" height="22" alt="$msg{'549'}" border="0"></a>
<a href="javascript:addCode('[pre][/pre]')"><img src="$imagesurl/forum/buttons/pre.gif" align="absmiddle" width="23" height="22" alt="$msg{'547'}" border="0"></a>
<a href="javascript:addCode('[url][/url]')"><img src="$imagesurl/forum/buttons/url.gif" align="absmiddle" width="23" height="22" alt="$msg{'121'}" border="0"></a>
<a href="javascript:addCode('[img][/img]')"><img src="$imagesurl/forum/buttons/img.gif" align="absmiddle" width="23" height="22" alt="$msg{'171'}" border="0"></a>
<a href="javascript:addCode('[email][/email]')"><img src="$imagesurl/forum/buttons/email2.gif" align="absmiddle" width="23" height="22" alt="$msg{'122'}" border="0"></a>
<a href="javascript:addCode('[code][/code]')"><img src="$imagesurl/forum/buttons/code.gif" align="absmiddle" width="23" height="22" alt="$msg{'123'}" border="0"></a>
<a href="javascript:addCode('[quote][/quote]')"><img src="$imagesurl/forum/buttons/quote2.gif" align="absmiddle" width="23" height="22" alt="$msg{'124'}" border="0"></a>
<a href="javascript:addCode('[list][*][*][*][/list]')"><img src="$imagesurl/forum/buttons/list.gif" align="absmiddle" width="23" height="22" alt="$msg{'125'}" border="0"></a>&nbsp;
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
</td>
</tr>
</table></td>
</tr>
</table>
</center>
~;

}

################
sub print_entry {
################

print "Content-type: text/html\n\n";
print qq~
<html>
<head>
<title>$username\'s $office_journal{'001'}</title>
<link rel="stylesheet" href="$themesurl/standard/style.css" type="text/css"> 
</head>
<body>
<br>~;

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = (<FILE>);
	unfile_lock(FILE);
close(FILE);

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	foreach $entry (@entries) {
		chomp $entry;
		($subject, $ldate, $sdate, $msgid, $filenum) = split(/\|/, $entry);
		if ($msgid == $info{'id'}) {
			open(ENTRY, "$journal_dir/$filenum.txt");
				file_lock(ENTRY);
				chomp($text = <ENTRY>);
				unfile_lock(ENTRY);
			close(ENTRY);
			($message, $moddate) = split(/\|/, $text);
			$thissubject = $subject;
			$thisdate = $ldate;
			$thisid = $msgid;
			if ($enable_ubbc) { doubbc(); }
			if ($enable_smile) { dosmilies(); }
		}
	}
	unfile_lock(FILE);
close(FILE);
	
print qq~
<table border="0" cellpadding="3" cellspacing="3" width="100%">
<tr>
<td class="texttitle" valign="middle">
<IMG alt="$office_journal{'001'}" src="$imgURL/journal_big.gif" border="0" align="absmiddle">&nbsp;$thissubject</td>
</tr>
<tr>
<td class="textsmall">$office_journal{'001'}: $thisdate~;

if ($moddate eq "") { }
else {
	print qq~<BR>$office_journal{'010'} $moddate~;
}
print qq~
</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top">$message</td>
</tr>
</table>
<br>
<hr>
<br><center>
<small><a href="$this_cgi">$scriptname</a> v.$scriptver<br><br></small></center></body>
</html>
~;
exit;
}


################
sub email_entry {
################
if ($username eq "$anonuser") { error("$err{'011'}"); }

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	@entries = (<FILE>);
	unfile_lock(FILE);
close(FILE);

open(FILE, "$journal_dir/$username.idx");
	file_lock(FILE);
	foreach $entry (@entries) {
		chomp $entry;
		($subject, $ldate, $sdate, $msgid, $filenum) = split(/\|/, $entry);
		if ($msgid == $info{'id'}) {
			open(ENTRY, "$journal_dir/$filenum.txt");
				file_lock(ENTRY);
				chomp($text = <ENTRY>);
				unfile_lock(ENTRY);
			close(ENTRY);
			($message, $moddate) = split(/\|/, $text);
			$thissubject = $subject;
			$thisdate = $ldate;
			$thisid = $msgid;
		}
	}
	unfile_lock(FILE);
close(FILE);
	
$navbar = "$office_gen{'023'} $office_journal{'002'} $office_gen{'023'} $thissubject";
print_top();

print qq~<br>
<form action="$this_cgi?action=email_entry2&amp;id=$info{'id'}" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td colspan="2" class="formstextnormal" align="center">$office_journal{'003'}</td>
</tr>
<tr>
<td colspan="2">&nbsp;</td>
</tr>
<tr>
<td class="formstextnormal">$office_gen{'025'}</td>
<td><input type="text" name="name" value="$realname" size="40"></td>
</tr>
<tr>
<td class="formstextnormal">$office_gen{'026'}</td>
<td><input type="hidden" name="from" value="$realemail">$realemail</td>
</tr>
 <tr>
<td class="formstextnormal">$office_gen{'027'}</td>
<td><input type="text" name="sendto" size="40"></td>
</tr>
<tr>
<td>
<input type="submit" class="button" value="$office_journal{'005'}">&nbsp;
<input type="reset" class="button" value="$office_gen{'009'}">
<input type="hidden" name="subject" value="$thissubject"></td>
</tr>
</table>
</form>
~;
print_bottom();
exit;

}

#################
sub email_entry2 {
#################

if ($username eq "$anonuser")  { error("$err{'011'}"); }

error("$err{'005'}") unless ($input{'sendto'});
error("$err{'014'}") unless ($input{'from'});

open(ENTRY, "$journal_dir/$info{'id'}.txt");
	file_lock(ENTRY);
	chomp($text = <ENTRY>);
	unfile_lock(ENTRY);
close(ENTRY);

($message, $moddate) = split(/\|/, $text);

$foot = "\n\n$office_gen{'028'} $input{'name'}";
$title = ": $input{'subject'}";

	$mailmessage = convert_newsletter($message).$foot;
	$mailsubject = $title;
	$mailto = $input{'sendto'};
	$mailfrom = $input{'from'};

sendemail($mailto, $mailsubject, $mailmessage, $mailfrom);

print "Location: $this_cgi?action=view&id=$info{'id'}\n\n";

exit;
}


1; # return true


