###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# instantmessage.pl                              			            #
# Date Formatting, Timezones & Error Messages by: Floyd for v0.9.8            #
# Delete all IM's:  Carter                                                    # 
#                                                                             #  
# Copyright (C) 2002 by WebAPP (webapp@attbi.com)                             #
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
# File: Last modified: 03/27/02                                               #
###############################################################################
###############################################################################

#############
sub imindex {
#############
	if ($username eq "$anonuser") { error("noguests"); }
	open(FILE, "$memberdir/$username.msg");
	file_lock(FILE);
	@imessages = <FILE>;
	unfile_lock(FILE);
	close(FILE);
	open(FILE, "$memberdir/membergroups.dat");
	file_lock(FILE);
	@membergroups = <FILE>;
	unfile_lock(FILE);
	close(FILE);
	
	open(CENSOR, "$boardsdir/censor.txt");
	file_lock(CENSOR);
	@censored = <CENSOR>;
	unfile_lock(CENSOR);
	close(CENSOR);
	open(FILE, "$memberdir/$username.dat") || error("$err{'010'}"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE); 
	
	$umessageid = $info{"messageid"};
	$navbar = "$btn{'014'} $nav{'028'}";	
	print_top();
	print qq~<table width="100%" border="0" cellspacing="1" cellpadding="3">
<tr>
<td>
~;
if ($umessageid ne "") {
	imview();
} 
print qq~<table cellpadding="3" cellspacing="3" width="100%" border="0"><tr>
	<td align="left"><a href="$cgi?action=imsend">$nav{'029'}</a></td>
	<td colspan="2" align="center">&nbsp;</td>
	<td align="right"><a href="$cgi?action=imremove&amp;id=all">$msg{'576'}</a></td>
	</tr></table>
	<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td class="imtitle" width="10%"><b>$msg{'182'}</b></td>
<td class="imtitle" width="20%"><b>$msg{'214'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>
</tr>
~;
	if (@imessages == 0) {
		print qq~<tr>
<td colspan="4" class="imwindow1">$msg{'050'}</td>
</tr>~;
}
	$second = "imwindow2";
	sort {$b[5] <=> $a[5]} @immessages;
	for ($a = 0; $a < @imessages; $a++) {
		if ($second eq "imwindow1") { $second="imwindow2"; }
		else { $second="imwindow1"; }
		
		($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);
                
                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
		$subject = "$msub[$a]";
		if ($subject eq "") { $subject="---"; }
		
		$mmessage[$a] =~ s/\n//g;
		$mmessage[$a] =~ s/\r//g;
		$message="$mmessage[$a]";
		$name = "$mname[$a]";
		$mail = "$memset[2]";
		$date = "$mdate[$a]";
		$ip = "$mip[$a]";
		$postinfo = "";
		$signature = "";
		$viewd = "";
		$icq = "";
		$star = "";
		$newim = "";
		$imnav = "oldimlink";
if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
	$newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
	$second = "imselected";
}
display_date($mdate[$a]); $mdate[$a] = $user_display_date;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second" width="10%"><a href="$cgi?action=imsend&to=$musername[$a]" class="$imnav">$musername[$a]</a></td>~;
}
print qq~<td class="$second" width="20%" nowrap>$mdate[$a]</td>
<td class="$second" width="60%"><a href="$cgi?action=im&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$newim$msub[$a]</td>~;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imremove&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
} else {print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imsend&to=$musername[$a]&num=$messageid[$a]"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>&nbsp;&nbsp;<a href="$cgi?action=imremove&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
}
print qq~</tr>~;	
}
print qq~</table><table cellpadding="3" cellspacing="3" width="100%" border="0"><tr>
	<td align="left"><a href="$cgi?action=imsend">$nav{'029'}</a></td>
	<td colspan="2" align="center">&nbsp;</td>
	<td align="right"><a href="$cgi?action=imremove&amp;id=all">$msg{'576'}</a></td>
	</tr></table><br>~;
if ($username eq "admin") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
</tr>
</table>~;
}
if ($username ne "admin" && $settings[7] eq "$root") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1">
<a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a>

</td>
</tr>
</table>~;
}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}

print qq~<br>~;
print_bottom();
}

#############
sub imview {
#############	
  if ($username eq "$anonuser") { error("noguests"); }
	if ($info{'from'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	
	$from = $info{"from"};
	open(FILE, "$memberdir/$from.dat");
	file_lock(FILE);
	@memset = <FILE>;
	unfile_lock(FILE);
	close(FILE);
		open(FILE, ">$memberdir/$username.msg");
		file_lock(FILE);
		foreach $msg (@imessages) {
		chomp $msg;
		($t, $t, $t, $t, $messageid1, $t) = split(/\|/, $msg);
		if ($umessageid == $messageid1) {
			($musername, $msub, $mdate, $mmessage, $messageid, $mviewed) = split(/\|/, $msg);
			$subject = $msub; $message = $mmessage;
			print FILE "$msg|1\n";
		}
		else {
			print FILE "$msg\n" ;
		}
	}
	unfile_lock(FILE);
	close(FILE);
	
	
		$ranking = $memset[6]+$memset[11]+$memset[12];
		
		$postinfo = qq~$msg{'021'} $memset[6]<br>
$msg{'022'} $memset[11]<br>
$msg{'023'} $memset[12]<br>
~;
		$viewd = qq~&nbsp;&nbsp;<a href="$cgi\?action=viewprofile&username=$musername"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $musername[$a]" border="0"></a>~;
		$memberinfo = "$membergroups[2]";
		$star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
		if ($ranking > 25) {
			$memberinfo = "$membergroups[3]";
			$star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
		}
		if ($ranking > 50) {
			$memberinfo = "$membergroups[4]";
			$star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
		}
		if ($ranking > 75) {
			$memberinfo = "$membergroups[5]";
			$star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
		}
		if ($ranking > 100) {
			$memberinfo = "$membergroups[6]";
			$star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
		}
		if ($ranking > 250) {
			$memberinfo = "$membergroups[7]";
			$star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
		}
		if ($ranking > 500) {
			$memberinfo = "$membergroups[8]";
			$star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
		}
		if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
		if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
		if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }
		$signature = "$memset[5]";
		$signature =~ s/\&\&/<br>/g;
		$signature = qq~<br><br><br>
-----------------<br>
$signature
~;
		$memset[8] =~ s/\n//g;
		$memset[8] =~ s/\r//g;
		if ($memset[8] ne "") {
	                if (!($memset[8] =~ /\D/)) { 
				$icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
			}
		}
		$message = "$message\n$signature";
		if ($enable_ubbc) { doubbc(); }
		if ($enable_smile) { dosmilies(); }
		$url = "";
		if ($memset[3] ne "\n" && $musername ne "$anonuser") {
			$url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
		}
		foreach $censor (@censored) {
			$censor =~ s/\n//g;
			($word, $censored) = split(/\=/, $censor);
			$message =~ s/$word/$censored/g;
			$subject =~ s/$word/$censored/g;
		}
		display_date($mdate); $mdate = $user_display_date;
		print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor="$windowbg"><b>$msg{'049'}</b></td>
<td bgcolor="$windowbg"><b>$msg{'037'}</b></td>
</tr>
<tr>
<td bgcolor="#ffffff" width="140" valign="top" rowspan="2"><b>$memset[1]</b><br>
$memberinfo<br>
$star<br><br>
$postinfo<br>
</td>
<td bgcolor="#ffffff" valign="top">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td width="100%">&nbsp;<b>$subject</b></td>
<td align="right" nowrap><b>$msg{'054'}</b> $mdate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
</td>
</tr>
<tr>
<td bgcolor="#ffffff">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td>~;
if ($musername ne "$anonuser") {print qq~$url~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~<a href="$cgi?action=anonemail&sendto=$memset[1]">~;
}
else {
print qq~<a href="mailto:$mail">~;
}
print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $musername" border="0"></a>$viewd$icq~;
}
print qq~</td><td align="right">~;
if ($musername ne "$anonuser") {print qq~
<a href="$cgi?action=imsend&num=$messageid&quote=1&to=$musername"><img src="$imagesurl/forum/quote.gif" alt="$msg{'056'}" border="0"></a>&nbsp;&nbsp;<a href="$cgi?action=imsend&to=$musername&num=$messageid"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>&nbsp;&nbsp;~;
}
print qq~<a href="$cgi?action=imremove&id=$messageid"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<br><br>
~;
}
##############
sub imremove {
##############
	if ($username eq "$anonuser") { error("noguests"); }

if ($info{'id'} eq "all") { 
	open(FILE, ">$memberdir/$username.msg");
	file_lock(FILE);
	print FILE "";
	unfile_lock(FILE);
	close(FILE);
	
}
else {
	open(FILE, "$memberdir/$username.msg");
	file_lock(FILE);
	@imessages = <FILE>;
	unfile_lock(FILE);
	close(FILE);
	open(FILE, ">$memberdir/$username.msg");
	file_lock(FILE);
	for ($a = 0; $a < @imessages; $a++) {
		($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
		if ($messageid < 100 ) {
			if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
		}
		else {
			if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
		}
	}
	unfile_lock(FILE);
	close(FILE);
}
	print "Location: $pageurl/$cgi\?action=im\n\n";
}
############
sub impost {
############
        $mid = time; 
	if ($username eq "$anonuser") { error("noguests"); }
	open(FILE, "$memberdir/$username.msg");
	file_lock(FILE);
	@imessages = <FILE>;
	unfile_lock(FILE);
	close(FILE);
	
	 if ($info{'subject'} ne "") { 
           $form_subject = $info{'subject'}; 
     } 
     if ($info{'msg'} ne "") { 
           $form_message = $info{'msg'}; 
     } 
	if ($info{'num'} ne "") {
		foreach $line (@imessages) {
			($mfrom, $msubject, $mdate, $mmessage, $messageid) = split(/\|/, $line);
			if ($info{'num'} eq $messageid) {
				$msubject =~ s/Re: //g;
				$form_subject = "Re: $msubject";
				$msg = $mmessage;
			}
		}
		if ($info{'quote'} == 1) {
			$form_message =~ s/\[quote\](\S+?)\[\/quote\]//isg;
			$form_message =~ s/\[(\S+?)\]//isg;
			$mmessage = htmltotext($msg);
			$form_message = "\n\n\[quote\]$mmessage\[/quote\]";
		}
	}
	$navbar = "$btn{'014'} $nav{'029'}";
	print_top();
	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
<td><form onSubmit="submitonce(this)" onSubmit="submitonce(this)" action="$cgi?action=imsend2" method="post">
<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="1">
<tr>
<td><b>$msg{'059'}</b></td>
~;
	if ($info{'to'} ne "") {
		print qq~<td><input type="text" name="to" value="$info{'to'}" size="20" maxlength="50"></td>~;
	}
	else {
		print qq~<td><select name="to">
~;
		open(MEM, "$memberdir/memberlist.dat");
		file_lock(MEM);
		@members = <MEM>;
		unfile_lock(MEM);
		close(MEM);
		@members = (sort { lc($a) cmp lc($b) } @members);
		for ($i = 0; $i < @members; $i++) {
			$members[$i] =~ s/\n//g;
			if ($members[$i] ne $username) {print qq~<option value="$members[$i]">$members[$i]</option>\n~;}
		}
	print qq~</select></td>
~;
	}
	print qq~</tr>
<tr>
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td valign="top"><b>$msg{'038'}</b></td>
<td><textarea name="message" rows="10" cols="40">$form_message</textarea></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
	print_bottom();
	exit;
}
#############
sub impost2 {
#############
	if ($username eq "$anonuser") { error("noguests"); }
	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});
	$messageid = $input{'messageid'};
	$subject = htmlescape($input{'subject'});
	$message = htmlescape($input{'message'});
	if (-e("$memberdir/$input{'to'}.dat")) { } else { error("$err{'010'}"); }
	open (FILE, "$memberdir/$input{'to'}.msg");
	file_lock(FILE);
	@imessages = <FILE>;
	unfile_lock(FILE);
	close (FILE);
	open (FILE, ">$memberdir/$input{'to'}.msg");
	file_lock(FILE);
	print FILE "$username|$subject|$date|$message|$messageid\n";
	foreach $curm (@imessages) { print FILE "$curm"; }
	unfile_lock(FILE);
	close(FILE);
	print "Location: $pageurl/$cgi\?action=im\n\n";
	exit;
}
############
sub siteim {
############
	if ($settings[7] ne "Administrator") { error("$err{'011'}"); }
	open(FILE, "$memberdir/$username.dat"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE);
     $mid = time; 

	$navbar = "$btn{'014'} $nav{'029'}";
	print_top();
	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
<td><form onSubmit="submitonce(this)" action="$cgi?action=siteim2" method="post">
<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="1">
<tr>
<td><b>$msg{'059'}</b></td>
<td>$msg{'563'}</td>
</tr>
<tr>
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td valign="top"><b>$msg{'038'}</b></td>
<td><textarea name="message" rows="10" cols="40"></textarea></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
	print_bottom();
	exit;
}
#############
sub siteim2 {
#############
	if ($settings[7] ne "Administrator") { error("$err{'011'}"); }
	open(FILE, "$memberdir/$username.dat"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE);

	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});
	$imsubj = htmlescape($input{'subject'});
	$formatmsg = htmlescape($input{'message'});

	open (FILE, "$memberdir/memberlist.dat");
	file_lock(FILE);
	@sendingto = <FILE>;
	unfile_lock(FILE);
	close (FILE);
	foreach $sitemember (@sendingto) {
		$sitemember =~ s/[\n\r]//g;
							
				sendim($sitemember, $imsubj, $formatmsg, $username);

		}
	print "Location: $pageurl/$cgi\?action=im\n\n";
	exit;
}
#############
sub adminim {
#############
				open (FILE, "$memberdir/$username.dat");
				file_lock(FILE);
				@settings = <FILE>;
				unfile_lock(FILE);
				close(FILE);
				for( $i = 0; $i < @settings; $i++ ) {
				$settings[$i] =~ s~[\n\r]~~g;
				}
	if ($username ne "admin" && $settings[7] ne "$root") { error("$err{'011'}"); }
	open(FILE, "$memberdir/$username.dat"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE);
     $mid = time; 

	$navbar = "$btn{'014'} $nav{'029'}";
	print_top();
	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
<td><form onSubmit="submitonce(this)" action="$cgi?action=adminim2" method="post">
<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="1">
<tr>
<td><b>$msg{'059'}</b></td>
<td>$msg{'595'}</td>
</tr>
<tr>
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td valign="top"><b>$msg{'038'}</b></td>
<td><textarea name="message" rows="10" cols="40"></textarea></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
	print_bottom();
	exit;
}
##############
sub adminim2 {
##############
				open (FILE, "$memberdir/$username.dat");
				file_lock(FILE);
				@settings = <FILE>;
				unfile_lock(FILE);
				close(FILE);
				for( $i = 0; $i < @settings; $i++ ) {
				$settings[$i] =~ s~[\n\r]~~g;
				}
	if ($username ne "admin" && $settings[7] ne "$root") { error("$err{'011'}"); }
	open(FILE, "$memberdir/$username.dat"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE);

	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});
	$imsubj = htmlescape($input{'subject'});
	$formatmsg = htmlescape($input{'message'});

	open (FILE, "$memberdir/memberlist.dat");
	file_lock(FILE);
	@sendingto = <FILE>;
	unfile_lock(FILE);
	close (FILE);
	foreach $sitemember (@sendingto) {
		$sitemember =~ s/[\n\r]//g;
				
				open (FILE, "$memberdir/$sitemember.dat");
				file_lock(FILE);
				@settings = <FILE>;
				unfile_lock(FILE);
				close(FILE);
				for( $i = 0; $i < @settings; $i++ ) {
				$settings[$i] =~ s~[\n\r]~~g;
				}
				if ($settings[7] eq "$root") {			
				sendim($sitemember, $imsubj, $formatmsg, $username);
				}
		}
	print "Location: $pageurl/$cgi\?action=im\n\n";
	exit;
}
###########
sub modim {
###########
				open (FILE, "$memberdir/$username.dat");
				file_lock(FILE);
				@settings = <FILE>;
				unfile_lock(FILE);
				close(FILE);
				for( $i = 0; $i < @settings; $i++ ) {
				$settings[$i] =~ s~[\n\r]~~g;
				}
	if ($username ne "admin" && $settings[7] ne "$root" && $settings[7] ne "$boardmoderator") { error("$err{'011'}"); }
	open(FILE, "$memberdir/$username.dat"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE);
     $mid = time; 

	$navbar = "$btn{'014'} IM to all Moderators";
	print_top();
	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
<td><form onSubmit="submitonce(this)" action="$cgi?action=modim2" method="post">
<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="1">
<tr>
<td><b>$msg{'059'}</b></td>
<td>$msg{'594'}</td>
</tr>
<tr>
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td valign="top"><b>$msg{'038'}</b></td>
<td><textarea name="message" rows="10" cols="40"></textarea></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
	print_bottom();
	exit;
}
############
sub modim2 {
############
				open (FILE, "$memberdir/$username.dat");
				file_lock(FILE);
				@settings = <FILE>;
				unfile_lock(FILE);
				close(FILE);
				for( $i = 0; $i < @settings; $i++ ) {
				$settings[$i] =~ s~[\n\r]~~g;
				}
	if ($username ne "admin" && $settings[7] ne "$root" && $settings[7] ne "$boardmoderator") { error("$err{'011'}"); }
	open(FILE, "$memberdir/$username.dat"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE);

	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});
	$imsubj = htmlescape($input{'subject'});
	$formatmsg = htmlescape($input{'message'});

	open (FILE, "$memberdir/memberlist.dat");
	file_lock(FILE);
	@sendingto = <FILE>;
	unfile_lock(FILE);
	close (FILE);
	foreach $sitemember (@sendingto) {
		$sitemember =~ s/[\n\r]//g;
							
				open (FILE, "$memberdir/$sitemember.dat");
				file_lock(FILE);
				@settings = <FILE>;
				unfile_lock(FILE);
				close(FILE);
				for( $i = 0; $i < @settings; $i++ ) {
				$settings[$i] =~ s~[\n\r]~~g;
				}
				if ($settings[7] eq "Administrator") {			
				sendim($sitemember, $imsubj, $formatmsg, $username);
				}
				if ($settings[7] eq "Officer") {			
				sendim($sitemember, $imsubj, $formatmsg, $username);
				}

		}
	print "Location: $pageurl/$cgi\?action=im\n\n";
	exit;
}

if (-e "$scriptdir/user-lib/instantmessage.pl") {require "$scriptdir/user-lib/instantmessage.pl"} 
1; # return true

