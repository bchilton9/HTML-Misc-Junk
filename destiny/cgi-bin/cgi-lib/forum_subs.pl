###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# forum_subs.pl 						                              #
# v0.9.9 - Requin       									#
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
# File: Last modified: 09/18/02                                               #
###############################################################################
###############################################################################

################
sub poststicky {
################
				open(FILE, "$boardsdir/$currentboard.dat");
				file_lock(FILE);
				chomp(@boardinfo = <FILE>);
				unfile_lock(FILE);
				close(FILE);
				$boardinfo[2] =~ s/[\n\r]//g;

				$boardinfo[2] =~ /^\|(.*?)\|$/;

				$moderators = $boardinfo[2];
				$moderators =~ s/\|(\S?)/,$1/g;

				foreach $curuser (split(/ /, $moderators)) {

						if ($username eq "$curuser") { $boardmoderator = $username; }
		
					}

	if ($settings[14] ne "$root" && $username ne "$boardmoderator") { error("$err{'011'}"); }
      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
			if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
			
				open(FILE, "$boardsdir/$currentboard.dat");
				file_lock(FILE);
				chomp(@boardinfo = <FILE>);
				unfile_lock(FILE);
				close(FILE);
				$boardinfo[2] =~ s/[\n\r]//g;

				open(FILE, "$memberdir/$boardinfo[2].dat");
				file_lock(FILE);
				chomp(@modprop = <FILE>);
				unfile_lock(FILE);
				close(FILE);

				$boardmoderator = $modprop[1];
	if ($username eq $anonuser && $enable_guestposting == 0) { error("$err{'011'}"); }

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
			if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
			
	open(FILE, "$boardsdir/$currentboard.sticky") || error("$err{'01'} $boardsdir/$currentboard.sticky");
	file_lock(FILE);
	chomp(@threads = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	for ($x = 0; $x < @threads; $x++) {
($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$x]);
		if ($info{'num'} eq $mnum && $mstate == 1) {
			error("$err{'024'}");
			$x = @threads;
		}
	}
	
	if ($enable_notification && $username ne $anonuser) {
	 $notification = qq~<tr>
<td><b>$msg{'105'}</b></td>
<td><input type="checkbox" name="notify" value="x"></td>
</tr>
~;
	}

	if ($realname ne "") { $name_field = qq~$realname<input type="hidden" name="name" value="$realname">~; }
	else { $name_field = qq~<input type="text" name="name" size="50" value="$form_name">~; }

	if ($realemail ne "") { $email_field = qq~$realemail<input type="hidden" name="email" value="$realemail">~; }
	else { $email_field = qq~<input type="text" name="email" size="50" value="$form_name">~; }

	if ($info{'num'} ne "") {
		open(FILE, "$messagedir/$info{'num'}.txt") || error("$err{'001'} $messagedir/$info{'num'}.txt");
		file_lock(FILE);
		chomp(@messages = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		($msubject, $mname, $memail, $mdate, $musername, $micon, $mip, $mmessage) = split(/\|/, $messages[0]);
		$msubject =~ s/Re: //g;
		$form_subject = "Re: $msubject";

		if ($info{'quote'} ne "") {
			($msubject, $mname, $memail, $mdate, $musername, $micon, $mip, $mmessage) = split(/\|/, $messages[$info{'quote'}]);
			$form_message = "$mmessage";
			$form_message =~ s/\[quote\](\S+?)\[\/quote\]//isg;
			$form_message =~ s/\[(\S+?)\]//isg;
			$form_message = "\n\n\[quote\]$form_message\[/quote\]";
			$form_message = htmltotext($form_message);
			$msubject =~ s/Re: //g;
			$form_subject = "Re: $msubject";
		}
	}

	$navbar = "$btn{'014'} $nav{'036'} ";
	print_top();
	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
	<tr>
<td><form action="$forum&amp;op=poststicky2&amp;start=$info{'start'}" method="post" name="creator">
<input type="hidden" name="followto" value="$info{'num'}">
<table border="0">
<tr>
<td class="formstextnormal">$msg{'013'}</td>
<td>$name_field</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'007'}</td>
<td>$email_field</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'037'}</td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'116'}</td>
<td><script language="javascript" type="text/javascript">
<!--
function showImage() {
document.images.icons.src="$imagesurl/forum/"+document.creator.icon.options[document.creator.icon.selectedIndex].value+".gif";
}
// -->
</script>
<select name="icon" onChange="showImage()">
<option value="xx">$msg{'143'}</option>
<option value="thumbup">$msg{'144'}</option>
<option value="thumbdown">$msg{'145'}</option>
<option value="exclamation">$msg{'146'}</option>
<option value="question">$msg{'147'}</option>
<option value="lamp">$msg{'148'}</option>
</select>
<img src="$imagesurl/forum/xx.gif" name="icons" width="15" height="15" border="0" hspace="15" alt=""></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'038'}</td>
<td>
<script language="javascript" type="text/javascript">
<!--
function addCode(anystr) { 
document.creator.message.value+=anystr;
} 
function showColor(color) { 
document.creator.message.value+="[color="+color+"][/color]";
}
// -->
</script>
<textarea name="message" rows="10" cols="40">$form_message</textarea></td>
</tr>~;
if ($enable_ubbc eq "1") {print qq~
<tr>
<td><b>$msg{'156'}</b></td>
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
</td>
</tr>~;}
smiliebfile_lock(); 
print qq~
$notification
<tr>
<td align="center" colspan="2"><input type="submit" class="button" name="moda" value="$btn{'044'}">&nbsp;<input type="submit" class="button" value="$btn{'008'}">
<input type="reset" class="button" value="$btn{'009'}"></td>
</tr>
</form>
</td>
</tr>~;
show_legend();
print qq~
</table>
~;
	if (@messages) { 
		print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
		<tr>
<td><b>$msg{'141'}</b></td>
</tr>
<tr>
<td colspan="3">
<table width="100%" class="forumtitlebackcolor" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
~;
		foreach $line (@messages) {
			($trash, $tempname, $trash, $tempdate, $trash, $trash, $trash, $temppost) = split(/\|/, $line);
			$message = "$temppost";	
			if ($enable_ubbc) { doubbc(); }
			if ($enable_smile) { dosmilies(); }
			print qq~<tr>
<td class="forumwindow3">$msg{'047'} $tempname ($tempdate)</td>
</tr>
<tr>
<td class="forumwindow2">$message</td>
</tr>
~;
		}
		print qq~</table>
</td>
</tr>
</table>
~;
 	}
	else { print "<!--no summary-->"; }

	print_bottom();
	exit;
}

#################
sub poststicky2 {
#################
				open(FILE, "$boardsdir/$currentboard.dat");
				file_lock(FILE);
				chomp(@boardinfo = <FILE>);
				unfile_lock(FILE);
				close(FILE);
				$boardinfo[2] =~ s/[\n\r]//g;

				$boardinfo[2] =~ /^\|(.*?)\|$/;

				$moderators = $boardinfo[2];
				$moderators =~ s/\|(\S?)/,$1/g;

				foreach $curuser (split(/ /, $moderators)) {

						if ($username eq "$curuser") { $boardmoderator = $username; }
		
					}

	if ($settings[14] ne "$root" && $username ne "$boardmoderator") { error("$err{'011'}"); }

if ($input{'moda'} eq "$btn{'011'}")  { print "Location: $cgi\?action=forum\&board=$currentboard\n\n"; }
elsif ($input{'moda'} eq "$btn{'044'}") {

# Put the preview code here....
#######################################################################################

$navbar = "$btn{'014'} $nav{'159'}";
print_top();

	error("$err{'013'}") unless($input{'name'});
	error("$err{'005'}") unless($input{'email'});
	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});

if ($username ne "$anonuser") {

open(FILE, "$memberdir/$username.dat"); 
		file_lock(FILE); 
		@settings = <FILE>; 
		unfile_lock(FILE); 
		close(FILE); 
 
		for( $i = 0; $i < @settings; $i++ ) { 
			$settings[$i] =~ s~[\n\r]~~g; 
		} 
}

$nsubject = htmltotext($input{'subject'});
$nmessage = htmltotext($input{'message'});

	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
	<tr>
<td><form action="$forum&amp;op=poststicky2&amp;start=$info{'start'}" method="post" name="creator">
<input type="hidden" name="num" value="$info{'num'}">
<input type="hidden" name="followto" value="$input{'followto'}">
<input type="hidden" name="name" value="$input{'name'}">
<input type="hidden" name="email" value="$input{'email'}">
<input type="hidden" name="subject" value="$nsubject">
<input type="hidden" name="message" value="$nmessage">
<input type="hidden" name="icon" value="$input{'icon'}">
</td></tr>
</table>
~;


	$name = htmlescape($input{'name'});
	$email = htmlescape($input{'email'});
	$subject = htmlescape($input{'subject'});
	$message = htmlescape($input{'message'});
	$icon = "$input{'icon'}";
	$sig = htmlescape($settings[5]);

			if ($enable_ubbc) { doubbc(); }
			if ($enable_smile) { dosmilies(); }

print qq~
<table width="100%" class="forumtitlebackcolor" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td class="forumwindow3">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td><img src="$imagesurl/forum/stickythread.gif" alt="$msg{'493'}"></td>
<td class="forumtext">&nbsp;<b>$msg{'049'}</b></td>
</tr>
</table>
</td>
<td class="forumwindow3"><b>$msg{'064'} $subject</b></td>
</tr>~;

if ($username ne "$anonuser") {
print qq~
<tr>
<td class="forumwindow2" width="140" valign="top"><b>$name</b><br>
<img src="$settings[9]" width="60" height="100" border="0" alt=""></a><br>
$settings[14]<br>
<br>
Forumposts: $settings[6]<br><br>$msg{'022'} $settings[11]<br><br>$msg{'023'} $settings[12]<br><br><br>
</td>
<td class="forumwindow2" valign="top">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
<td><img src="$imagesurl/forum/$icon.gif" alt="$msg{'517'}"></td>
<td width="100%">&nbsp;<b>$subject</b></td>
<td align="right" nowrap>&nbsp;<b>$msg{'110'}</b> $date</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
 <br> <br> <br>
----------------- <br>
$sig
<br>
</td>
</tr>
<tr class="forumwindow2">
<td><img src="$imagesurl/forum/ip.gif" alt="$msg{'111'}" align="top">$ENV{'REMOTE_ADDR'}</td>
<td>
<table border="0" cellspacing="0" cellpadding="0" width="100%" maxwidth="80">
<tr>
<td><a href="$settings[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=anonemail&sendto=$username" class="forumnav"><img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=viewprofile&amp;username=$username"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=imsend&amp;to=$username"><img src="$imagesurl/forum/message.gif" alt="$msg{'109'} $name" border="0"></a>&nbsp;&nbsp;<a href="http://www.icq.com/$settings[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$settings[8]&amp;img=5" alt="$msg{'052'} $settings[8]" border="0"></a></td>
<td align="right"><td>
</tr>
</table>
</td>
</tr>
<tr class="forumwindow2">
<td align="center" colspan="2">
<INPUT type="button" class="button" value="$btn{'030'}" onClick="history.back()"><!-- edit -->
<input type="submit" class="button" value="$btn{'043'}"><!-- Post Message -->
<input type="submit" class="button" name="moda" value="$btn{'011'}"><!-- Delete --></td>
</tr>
</form>
</table>
~;
}

print_bottom();

exit;
}
#########################################################################################

else {

	error("$err{'013'}") unless($input{'name'});
	error("$err{'005'}") unless($input{'email'});
	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});

	$name = htmlescape($input{'name'});
	$email = htmlescape($input{'email'});
	$subject = htmlescape($input{'subject'});
	$message = htmlescape($input{'message'});
	$icon = "$input{'icon'}";

	if ($username ne "$anonuser") { 
		$name = "$settings[1]";
		$email = "$settings[2]";
	}
	else {
		open(FILE, "$memberdir/memberlist.dat");
		file_lock(FILE);
		chomp(@memberlist = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		if (exists $memberlist{$name}) { error("$err{'007'}"); }
		for ($a = 0; $a < @memberlist; $a++) {
			open(FILE, "$memberdir/$memberlist[$a].dat");
			file_lock(FILE);
			chomp(@check_settings = <FILE>);
			unfile_lock(FILE);
			close(FILE);

			if ($check_settings[1] eq $name) { error("$err{'007'}"); }
		}
	}
	if (length($subject) > 50) { $subject = substr($subject,0,50); }

	if ($input{'followto'} eq "") {
		opendir (DIR, "$messagedir");
		@files = readdir(DIR);
		closedir (DIR);
		@files = grep(/txt/,@files);
		@files = reverse(sort { $a <=> $b } @files);
		$postnum = @files[0];
		$postnum =~ s/.txt//;
		$postnum++;
	}
	
      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	
	open (FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
	file_lock(FILE);
	@messages = <FILE>;
	unfile_lock(FILE);
	close (FILE);

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	open (FILE, ">$boardsdir/$currentboard.sticky") || error("$err{'016'} $boardsdir/$currentboard.sticky");
	file_lock(FILE);
	$followto = $input{'followto'};
	if ($followto eq "") {
		print FILE "$postnum|$subject|$name|$username|$email|$date|0|0|$name|$icon\|0\n";
		print FILE @messages;
	}
	else {
		for ($a = 0; $a < @messages; $a++) {
			($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $messages[$a]);
			$mstate =~ s/[\n\r]//g;
			$mreplies++;
			if ($mnum == $followto) { print FILE "$mnum|$msub|$mname|$musername|$memail|$date|$mreplies|$stickyviews|$name|$micon|$mstate\n"; }
		}
		for ($a = 0; $a < @messages; $a++) {
			($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $messages[$a]);
			$mstate =~ s/[\n\r]//g;
			if ($mnum == $followto) { }
			else { print FILE "$messages[$a]"; }
		}
	}
	unfile_lock(FILE);
	close(FILE);

	if (-e("$messagedir/$followto.txt")) { 
		open(FILE, ">>$messagedir/$followto.txt") || error("$err{'001'} $messagedir/$followto.txt"); 
	}
	else { 
		open(FILE, ">$messagedir/$postnum.txt") || error("$err{'016'} $messagedir/$postnum.txt"); 
	}
	file_lock(FILE);
	print FILE "$subject|$name|$email|$date|$username|$icon|$ENV{REMOTE_ADDR}|$message\n";
	unfile_lock(FILE);
	close (FILE);
	
	if (-e("$messagedir/$followto.txt")) { $thread = "$followto"; }
	else { $thread = "$postnum"; }

	if (-e("$messagedir/$thread.mail")) { notify_users(); }
	$writedate = "$date";
	writelog("$currentboard");

	if ($username ne "$anonuser") {
		$settings[6]++;

		open(FILE, ">$memberdir/$username.dat") || error("$err{'016'} $memberdir/$username.dat");
		file_lock(FILE);
		for ($i = 0; $i < @settings; $i++) {
				print FILE "$settings[$i]\n";
		}
		unfile_lock(FILE);
		close(FILE);
	}


	if ($input{'notify'}) {
		print "Location: $cgi\?action=forum\&board=$currentboard\&op=notify2\&thread=$thread\n\n";
	}
	else { print "Location: $cgi\?action=forum\&board=$currentboard\&op=displaysticky\&num=$thread\&start=$info{'start'}\n\n"; }
	exit;

}



}


##########
sub post {
##########
	if ($username eq $anonuser && $enable_guestposting == 0) { error("$err{'011'}"); }

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
			if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
			
	open(FILE, "$boardsdir/$currentboard.txt") || error("$err{'01'} $boardsdir/$currentboard.txt");
	file_lock(FILE);
	chomp(@threads = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	for ($x = 0; $x < @threads; $x++) {
($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$x]);
		if ($info{'num'} eq $mnum && $mstate == 1) {
			error("$err{'024'}");
			$x = @threads;
		}
	}
	
	if ($enable_notification && $username ne $anonuser) {
	 $notification = qq~<tr>
<td><b>$msg{'105'}</b></td>
<td><input type="checkbox" name="notify" value="x"></td>
</tr>
~;
	}

	if ($realname ne "") { $name_field = qq~$realname<input type="hidden" name="name" maxlength="20" value="$realname">~; }
	else { $name_field = qq~<input type="text" name="name" size="50" maxlength="20" value="$form_name">~; }

	if ($realemail ne "") { $email_field = qq~$realemail<input type="hidden" name="email" maxlength="35" value="$realemail">~; }
	else { $email_field = qq~<input type="text" name="email" size="50" maxlength="35" value="$form_name">~; }

	if ($info{'num'} ne "") {
		open(FILE, "$messagedir/$info{'num'}.txt") || error("$err{'001'} $messagedir/$info{'num'}.txt");
		file_lock(FILE);
		chomp(@messages = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		($msubject, $mname, $memail, $mdate, $musername, $micon, $mip, $mmessage) = split(/\|/, $messages[0]);
		$msubject =~ s/Re: //g;
		$form_subject = "Re: $msubject";

		if ($info{'quote'} ne "") {
			($msubject, $mname, $memail, $mdate, $musername, $micon, $mip, $mmessage) = split(/\|/, $messages[$info{'quote'}]);
			$form_message = "$mmessage";
			$form_message =~ s/\[quote\](\S+?)\[\/quote\]//isg;
			$form_message =~ s/\[(\S+?)\]//isg;
			$form_message = "\n\n\[quote\]$form_message\[/quote\]";
			$form_message = htmltotext($form_message);
			$msubject =~ s/Re: //g;
			$form_subject = "Re: $msubject";
		}
	}

	$navbar = "$btn{'014'} $nav{'036'} ";
	print_top();
	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
<td><form action="$forum&amp;op=post2&amp;start=$info{'start'}" method="post" name="creator">
<input type="hidden" name="followto" value="$info{'num'}">
<table border="0">
<tr>
<td><b>$msg{'013'}</b></td>
<td>$name_field</td>
</tr>
<tr>
<td><b>$msg{'007'}</b></td>
<td>$email_field</td>
</tr>
<tr>
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td><b>$msg{'116'}</b></td>
<td><script language="javascript" type="text/javascript">
<!--
function showImage() {
document.images.icons.src="$imagesurl/forum/"+document.creator.icon.options[document.creator.icon.selectedIndex].value+".gif";
}
// -->
</script>
<select name="icon" onChange="showImage()">
<option value="xx">$msg{'143'}</option>
<option value="thumbup">$msg{'144'}</option>
<option value="thumbdown">$msg{'145'}</option>
<option value="exclamation">$msg{'146'}</option>
<option value="question">$msg{'147'}</option>
<option value="lamp">$msg{'148'}</option>
</select>
<img src="$imagesurl/forum/xx.gif" name="icons" width="15" height="15" border="0" hspace="15" alt=""></td>
</tr>
<tr>
<td valign=top><b>$msg{'038'}</b></td>
<td>
<script language="javascript" type="text/javascript">
<!--
function addCode(anystr) { 
document.creator.message.value+=anystr;
} 
function showColor(color) { 
document.creator.message.value+="[color="+color+"][/color]";
}
// -->
</script>
<textarea name="message" rows="10" cols="40">$form_message</textarea></td>
</tr>~;
if ($enable_ubbc eq "1") {print qq~
<tr>
<td><b>$msg{'156'}</b></td>
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
</td>
</tr>~;}
smiliebfile_lock(); 
print qq~
$notification
<tr>
<td align="center" colspan="2"><input type="submit" class="button" name="moda" value="$btn{'044'}">&nbsp;<input type="submit" class="button" value="$btn{'008'}">
<input type="reset" class="button" value="$btn{'009'}"></td>
</tr>
</form>
</td>
</tr>~;
show_legend();
print qq~
</table>
~;
	if (@messages) { 
		print qq~<br>
<b>$msg{'141'}</b><br>
<table width="100%" class="boardtitle" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
~;
		foreach $line (@messages) {
			($trash, $tempname, $trash, $tempdate, $trash, $trash, $trash, $temppost) = split(/\|/, $line);
			$message = "$temppost";	
			if ($enable_ubbc) { doubbc(); }
			if ($enable_smile) { dosmilies(); }
			print qq~<tr>
<td class="forumwindow3">$msg{'047'} $tempname ($tempdate)</td>
</tr>
<tr>
<td class="forumwindow2">$message</td>
</tr>
~;
		}
		print qq~</table>
</td>
</tr>
</table>
~;
 	}
	else { print "<!--no summary-->"; }

	print_bottom();
	exit;
}

###########
sub post2 {
###########
	if ($username eq "$anonuser" && $enable_guestposting == 0) { error("$err{'011'}"); }

if ($input{'moda'} eq "$btn{'011'}")  { print "Location: $cgi\?action=forum\&board=$currentboard\n\n"; }
elsif ($input{'moda'} eq "$btn{'044'}") {

# Put the preview code here....
#######################################################################################

$navbar = "$btn{'014'} $nav{'159'}";
print_top();

	error("$err{'013'}") unless($input{'name'});
	error("$err{'005'}") unless($input{'email'});
	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});

if ($username ne "$anonuser") {

open(FILE, "$memberdir/$username.dat"); 
		file_lock(FILE); 
		@settings = <FILE>; 
		unfile_lock(FILE); 
		close(FILE); 
 
		for( $i = 0; $i < @settings; $i++ ) { 
			$settings[$i] =~ s~[\n\r]~~g; 
		} 
}


$nsubject = htmltotext($input{'subject'});
$nmessage = htmltotext($input{'message'});

	print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
	<tr>
<td><form action="$forum&amp;op=post2&amp;start=$info{'start'}" method="post" name="creator">
<input type="hidden" name="num" value="$info{'num'}">
<input type="hidden" name="followto" value="$input{'followto'}">
<input type="hidden" name="name" value="$input{'name'}">
<input type="hidden" name="email" value="$input{'email'}">
<input type="hidden" name="subject" value="$nsubject">
<input type="hidden" name="message" value="$nmessage">
<input type="hidden" name="icon" value="$input{'icon'}">
</td></tr>
</table>
~;


	$name = htmlescape($input{'name'});
	$email = htmlescape($input{'email'});
	$subject = htmlescape($input{'subject'});
	$message = htmlescape($input{'message'});
	$icon = "$input{'icon'}";
	$sig = htmlescape($settings[5]);

			if ($enable_ubbc) { doubbc(); }
			if ($enable_smile) { dosmilies(); }

print qq~
<table width="100%" class="forumtitlebackcolor" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td class="forumwindow3">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td><img src="$imagesurl/forum/thread.gif" alt="$msg{'490'}"></td>
<td class="forumtext">&nbsp;<b>$msg{'049'}</b></td>
</tr>
</table>
</td>
<td class="forumwindow3"><b>$msg{'064'} $subject</b></td>
</tr>~;

if ($username ne "$anonuser") {
print qq~
<tr>
<td class="forumwindow2" width="140" valign="top"><b>$name</b><br>
<img src="$settings[9]" width="60" height="100" border="0" alt=""></a><br>
$settings[14]<br>
<br>
Forumposts: $settings[6]<br><br>$msg{'022'} $settings[11]<br><br>$msg{'023'} $settings[12]<br><br><br>
</td>
<td class="forumwindow2" valign="top">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
<td><img src="$imagesurl/forum/$icon.gif" alt="$msg{'517'}"></td>
<td width="100%">&nbsp;<b>$subject</b></td>
<td align="right" nowrap>&nbsp;<b>$msg{'110'}</b> $date</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
 <br> <br> <br>
----------------- <br>
$sig
<br>
</td>
</tr>
<tr class="forumwindow2">
<td><img src="$imagesurl/forum/ip.gif" alt="$msg{'111'}" align="top">$ENV{'REMOTE_ADDR'}</td>
<td>
<table border="0" cellspacing="0" cellpadding="0" width="100%" maxwidth="80">
<tr>
<td><a href="$settings[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=anonemail&sendto=$username" class="forumnav"><img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=viewprofile&amp;username=$username"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=imsend&amp;to=$username"><img src="$imagesurl/forum/message.gif" alt="$msg{'109'} $name" border="0"></a>&nbsp;&nbsp;<a href="http://www.icq.com/$settings[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$settings[8]&amp;img=5" alt="$msg{'052'} $settings[8]" border="0"></a></td>
<td align="right"><td>
</tr>
</table>
</td>
</tr>
<tr class="forumwindow2">
<td align="center" colspan="2">
<INPUT type="button" class="button" value="$btn{'030'}" onClick="history.back()"><!-- edit -->
<input type="submit" class="button" value="$btn{'043'}"><!-- Post Message -->
<input type="submit" class="button" name="moda" value="$btn{'011'}"><!-- Delete --></td>
</tr>
</form>
</table>
~;
}

if ($username eq "$anonuser") {

print qq~
<tr>
<td class="forumwindow2" width="140" valign="top"><b>$name</b><br>
<br>
<br><br><br>
</td>
<td class="forumwindow2" valign="top">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
<td><img src="$imagesurl/forum/$icon.gif" alt="$msg{'517'}"></td>
<td width="100%">&nbsp;<b>$subject</b></td>
<td align="right" nowrap>&nbsp;<b>$msg{'110'}</b> $date</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
<br> <br> <br>
</td>
</tr>
<tr class="forumwindow2">
<td><img src="$imagesurl/forum/ip.gif" alt="$msg{'111'}" align="top">$ENV{'REMOTE_ADDR'}</td>
<td>
<table border="0" cellspacing="0" cellpadding="0" width="100%" maxwidth="80">
<tr>
<td></td>
<td align="right"><td>
</tr>
</table>
</td>
</tr>
<tr class="forumwindow2">
<td align="center" colspan="2">
<INPUT type="button" class="button" value="$btn{'030'}" onClick="history.back()">
<input type="submit" class="button" value="$btn{'043'}">
<input type="submit" class="button" name="moda" value="$btn{'011'}"></td>
</tr>
</form>
</table>
~;

}

print_bottom();

exit;
}
#########################################################################################

else {


	if ($username ne $anonuser) {
	error("$err{'003'}") unless($input{'name'});
	error("$err{'005'}") unless($input{'email'});
	}

	error("$err{'014'}") unless($input{'subject'});
	error("$err{'015'}") unless($input{'message'});

	if ($username eq $anonuser && $enable_guestposting == 1) {
	error("$err{'003'}") unless($input{'email'});
	error("$err{'005'}") unless($input{'name'});
	}
	

	$name = htmlescape($input{'name'});
	$email = htmlescape($input{'email'});
	$subject = htmlescape($input{'subject'});
	$message = htmlescape($input{'message'});
	$icon = "$input{'icon'}";

	if ($username ne "$anonuser") { 
		$name = "$settings[1]";
		$email = "$settings[2]";
	}
	else {
		open(FILE, "$memberdir/memberlist.dat");
		file_lock(FILE);
		chomp(@memberlist = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		if (exists $memberlist{$name}) { error("$err{'007'}"); }
		for ($a = 0; $a < @memberlist; $a++) {
			open(FILE, "$memberdir/$memberlist[$a].dat");
			file_lock(FILE);
			chomp(@check_settings = <FILE>);
			unfile_lock(FILE);
			close(FILE);

			if ($check_settings[1] eq $name) { error("$err{'007'}"); }
		}
	}
	if (length($subject) > 50) { $subject = substr($subject,0,50); }

	if ($input{'followto'} eq "") {
		opendir (DIR, "$messagedir");
		@files = readdir(DIR);
		closedir (DIR);
		@files = grep(/txt/,@files);
		@files = reverse(sort { $a <=> $b } @files);
		$postnum = @files[0];
		$postnum =~ s/.txt//;
		$postnum++;
	}
	
      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	
	open (FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
	file_lock(FILE);
	@messages = <FILE>;
	unfile_lock(FILE);
	close (FILE);

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	open (FILE, ">$boardsdir/$currentboard.txt") || error("$err{'016'} $boardsdir/$currentboard.txt");
	file_lock(FILE);
	$followto = $input{'followto'};
	if ($followto eq "") {
		print FILE "$postnum|$subject|$name|$username|$email|$date|0|0|$name|$icon\|0\n";
		print FILE @messages;
	}
	else {
		for ($a = 0; $a < @messages; $a++) {
			($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $messages[$a]);
			$mstate =~ s/[\n\r]//g;
			$mreplies++;
			if ($mnum == $followto) { print FILE "$mnum|$msub|$mname|$musername|$memail|$date|$mreplies|$mviews|$name|$micon|$mstate\n"; }
		}
		for ($a = 0; $a < @messages; $a++) {
			($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $messages[$a]);
			$mstate =~ s/[\n\r]//g;
			if ($mnum == $followto) { }
			else { print FILE "$messages[$a]"; }
		}
	}
	unfile_lock(FILE);
	close(FILE);

	if (-e("$messagedir/$followto.txt")) { 
		open(FILE, ">>$messagedir/$followto.txt") || error("$err{'001'} $messagedir/$followto.txt"); 
	}
	else { 
		open(FILE, ">$messagedir/$postnum.txt") || error("$err{'016'} $messagedir/$postnum.txt"); 
	}
	file_lock(FILE);
	print FILE "$subject|$name|$email|$date|$username|$icon|$ENV{REMOTE_ADDR}|$message\n";
	unfile_lock(FILE);
	close (FILE);
	
	if (-e("$messagedir/$followto.txt")) { $thread = "$followto"; }
	else { $thread = "$postnum"; }

	if (-e("$messagedir/$thread.mail")) { notify_users(); }
	$writedate = "$date";
	writelog("$currentboard");

	if ($username ne "$anonuser") {
		$settings[6]++;

		open(FILE, ">$memberdir/$username.dat") || error("$err{'016'} $memberdir/$username.dat");
		file_lock(FILE);
		for ($i = 0; $i < @settings; $i++) {
				print FILE "$settings[$i]\n";
		}
		unfile_lock(FILE);
		close(FILE);
	}


	if ($input{'notify'}) {
		print "Location: $cgi\?action=forum\&board=$currentboard\&op=notify2\&thread=$thread\n\n";
	}
	else { print "Location: $cgi\?action=forum\&board=$currentboard\&op=display\&num=$thread\&start=$info{'start'}\n\n"; }
	exit;
}

}


############ 
sub jumpto { 
############ 
     open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt"); 
     file_lock(FILE); 
     @jumptofiles = <FILE>; 
     unfile_lock(FILE); 
     close(FILE); 


     foreach $jumpfile (@jumptofiles) { 
           $jumpfile =~ s/[\n\r]//g; 

           open(FILE, "$boardsdir/$jumpfile.cat") || error("$err{'001'} $boardsdir/$jumpfile.cat"); 
           file_lock(FILE); 
           @jumpinfo = <FILE>; 
           unfile_lock(FILE); 
           close(FILE); 

           $jumpinfo[1] =~ s/[\n\r]//g; 
           if ($jumpinfo[1] ne "") { 
                 if ($settings[14] ne "$root" && $settings[14] ne "$jumpinfo[1]") {      next; } 
           } 

           $jumptoboard = "$jumpinfo[0]"; 
           foreach $jumptoboard (@jumpinfo) { 
                 if ($jumptoboard ne "$jumpinfo[0]" && $jumptoboard ne "$jumpinfo[1]") { 
                       $jumptoboard =~ s/[\n\r]//g; 

                       open(FILE, "$boardsdir/$jumptoboard.dat") || error("$err{'001'} $boardsdir/$jumptoboard.dat"); 
                       file_lock(FILE); 
                       chomp(@jumpoptions = <FILE>); 
                       unfile_lock(FILE); 
                       close(FILE); 
                       $selecthtml .= qq~<option value="$jumptoboard">@jumpoptions[0]</option>~; 
           } 
     } 
} 
} 

##############
sub printpage {
###############
	if ($info{'num'} ne "") {
		open(FILE, "$messagedir/$info{'num'}.txt") || error("$err{'001'} $messagedir/$info{'num'}.txt");
		file_lock(FILE);
		chomp(@messages = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		($title, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $messages[0]);

		print "Content-type: text/html\n\n";
		print qq~<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="Generator" content="$scriptname $scriptver">
<title>$title</title>
<link rel="stylesheet" href="$themesurl/standard/style.css" type="text/css">
</head>
<table border="0" cellpadding="1" cellspacing="0" width="100%">

~;
		foreach $line (@messages) {
			($subject, $name, $dummy, $date, $dummy, $dummy, $dummy, $message) = split(/\|/, $line);
			if ($enable_ubbc) { doubbc(); }
			if ($enable_smile) { dosmilies(); }
			print qq~
<tr>
<td class="texttitle">$subject</td>
</tr>
<tr>
<td><b>$msg{'047'} $name ($date)</b><td>
</tr>
<tr>
<td>$message</td>
</tr>
<tr>
<td><hr></td>
</tr>
~;
		}
		print qq~</table><br>
<center>
<small>$msg{'534'} <a href="$cgi">$pagename</a><br><br>
</small></center></body>

</html>
~;
	}
}

####################
sub smilieblock {
####################
if ($enable_smile eq "1") {
print qq~
<tr>
<td class="formstextnormal">$msg{'533'}</td>
<td valign="middle">
<a href="javascript:addCode('[bones]')"><img src="$imagesurl/forum/buttons/bones.gif" border="0" alt="$msg{'498'}"></a>
<a href="javascript:addCode('[confused]')"><img src="$imagesurl/forum/buttons/confused.gif" border="0" alt="$msg{'499'}">
<a href="javascript:addCode('[cool]')"><img src="$imagesurl/forum/buttons/cool.gif" border="0" alt="$msg{'500'}"></a>
<a href="javascript:addCode('[cry]')"><img src="$imagesurl/forum/buttons/cry.gif" border="0" alt="$msg{'501'}"></a>
<a href="javascript:addCode('[eek]')"><img src="$imagesurl/forum/buttons/eek.gif" border="0" alt="$msg{'502'}"></a>
<a href="javascript:addCode('[evil]')"><img src="$imagesurl/forum/buttons/evil.gif" border="0" alt="$msg{'503'}"></a>
<a href="javascript:addCode('[frown]')"><img src="$imagesurl/forum/buttons/frown.gif" border="0" alt="$msg{'504'}"></a>
<a href="javascript:addCode('[grin]')"><img src="$imagesurl/forum/buttons/grin.gif" border="0" alt="$msg{'505'}"></a>
<a href="javascript:addCode('[bounce]')"><img src="$imagesurl/forum/buttons/bounce.gif" border="0" alt="$msg{'506'}"></a>
<br>
<a href="javascript:addCode('[lol]')"><img src="$imagesurl/forum/buttons/lol.gif" border="0" alt="$msg{'507'}"></a>
<a href="javascript:addCode('[mad]')"><img src="$imagesurl/forum/buttons/mad.gif" border="0" alt="$msg{'508'}"></a>
<a href="javascript:addCode('[nonsense]')"><img src="$imagesurl/forum/buttons/nonsense.gif" border="0" alt="$msg{'509'}"></a>
<a href="javascript:addCode('[oops]')"><img src="$imagesurl/forum/buttons/oops.gif" border="0" alt="$msg{'510'}"></a>
<a href="javascript:addCode('[rolleyes]')"><img src="$imagesurl/forum/buttons/rolleyes.gif" border="0" alt="$msg{'511'}"></a>
<a href="javascript:addCode('[smile]')"><img src="$imagesurl/forum/buttons/smile.gif" border="0" alt="$msg{'512'}"></a>
<a href="javascript:addCode('[tongue]')"><img src="$imagesurl/forum/buttons/tongue.gif" border="0" alt="$msg{'513'}"></a>
<a href="javascript:addCode('[wink]')"><img src="$imagesurl/forum/buttons/wink.gif" border="0" alt="$msg{'514'}"></a>
<a href="javascript:addCode('[ninja]')"><img src="$imagesurl/forum/buttons/ninja.gif" border="0" alt="$msg{'515'}"></a>
</td>
</tr>
~;
}
}

####################
sub show_legend {
####################
		if ($username ne "$anonuser") {

		open(FILE, "$memberdir/$username.pref") || error("$err{'010'}");
		file_lock(FILE);
		chomp(@preferences = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		if ($preferences[7] == 1 || $preferences[7] eq "" ) {legend();}
		
		} else {legend();}

}

####################
sub legend {
####################

print qq~
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td><td valign="top">
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable"$background>
<tr>
<td>&nbsp;$msg{'516'}</td>
</tr>
</table>
<table border="0" cellpadding="1" cellspacing="0" width="100%" class="menubordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="3" cellspacing="0" width="100%" class="menubackcolor">
<tr>
<td valign="top" width="100%">
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><center><b><u>$msg{'116'}</u></b></center></td>
</tr>
<tr>
<td>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td>
&nbsp;<img src="$imagesurl/forum/xx.gif" border="0" alt="$msg{'517'}">&nbsp;&nbsp;$msg{'517'}.<br>
&nbsp;<img src="$imagesurl/forum/thumbup.gif" border="0" alt="$msg{'518'}">&nbsp;&nbsp;$msg{'518'}.<br>
&nbsp;<img src="$imagesurl/forum/thumbdown.gif" border="0" alt="$msg{'519'}">&nbsp;&nbsp;$msg{'519'}.<br>
</td>
<td>
&nbsp;<img src="$imagesurl/forum/exclamation.gif" border="0" alt="$msg{'520'}">&nbsp;&nbsp;$msg{'520'}<br>
&nbsp;<img src="$imagesurl/forum/question.gif" border="0" alt="$msg{'521'}">&nbsp;&nbsp;$msg{'521'}.<br>
&nbsp;<img src="$imagesurl/forum/lamp.gif" border="0" alt="$msg{'522'}">&nbsp;&nbsp;$msg{'522'}.
</td>
</tr>
</table>
</td>
</tr>~;
if ($enable_ubbc eq "1") {print qq~
<tr>
<td><center><b><u>$msg{'156'}</u></b></center></td>
</tr>
<tr>
<td>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td>
&nbsp;<img src="$imagesurl/forum/buttons/bold.gif" border="0" alt="$msg{'117'}">&nbsp;&nbsp;$msg{'523'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/italicize.gif" border="0" alt="$msg{'118'}">&nbsp;&nbsp;$msg{'524'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/underline.gif" border="0" alt="$msg{'119'}">&nbsp;&nbsp;$msg{'525'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/sub.gif" alt="$msg{'544'}" border="0"></a>&nbsp;&nbsp;$msg{'544'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/sup.gif" alt="$msg{'545'}" border="0"></a>&nbsp;&nbsp;$msg{'545'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/strike.gif" alt="$msg{'546'}" border="0"></a>&nbsp;&nbsp;$msg{'546'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/pre.gif" alt="$msg{'547'}" border="0"></a>&nbsp;&nbsp;$msg{'547'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/url.gif" border="0" alt="$msg{'121'}">&nbsp;&nbsp;$msg{'527'}.<br>
</td>
<td>
&nbsp;<img src="$imagesurl/forum/buttons/left.gif" alt="$msg{'548'}" border="0"></a>&nbsp;&nbsp;$msg{'548'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/center.gif" border="0" alt="$msg{'120'}">&nbsp;&nbsp;$msg{'526'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/right.gif" alt="$msg{'549'}" border="0"></a>&nbsp;&nbsp;$msg{'549'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/img.gif" border="0" alt="$msg{'171'}">&nbsp;&nbsp;$msg{'528'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/email2.gif" border="0" alt="$msg{'122'}">&nbsp;&nbsp;$msg{'529'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/code.gif" border="0" alt="$msg{'123'}">&nbsp;&nbsp;$msg{'530'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/quote2.gif" border="0" alt="$msg{'124'}">&nbsp;&nbsp;$msg{'531'}.<br>
&nbsp;<img src="$imagesurl/forum/buttons/list.gif" border="0" alt="$msg{'125'}">&nbsp;&nbsp;$msg{'532'}.
</td>
</tr>
</table>
</td>
</tr>~; }
print qq~
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
~;

}

####################
sub checkfornew {
####################

	$new ="";

	($dates1, $dummy) = split(/ /, $date1);
	($month, $day, $year) = split(/\//, $dates1);
	$number1 = ($year*365)+($month*30)+$day; # Log Date
	($dates2, $dummy) = split(/ /, $date2);
	($month, $day, $year) = split(/\//, $dates2);
	$number2 = ($year*365)+($month*30)+$day; # Post date
	($dummy, $times1) = split(/ - /, $date1);
	($hour, $min, $sec) = split(/:/, $times1);
	$number3 = ($hour*60)+$min; # Log Time
	($dummy, $times2) = split(/ - /, $date2);
	($hour, $min, $sec) = split(/:/, $times2);
	$number4 = ($hour*60)+$min; # Post Time
	
	if ($number1 eq $number2) {
		 if ($number3 lt $number4) {
		 $new = qq~<img src="$imagesurl/forum/new.gif" alt="">~; }
	}
	
	if ($number1 lt $number2) {
		 $datedifference = $number2-$number1;
		 if ($datedifference le $max_log_days_old) {
		 $new = qq~<img src="$imagesurl/forum/new.gif" alt="">~;
		 }
	}
		 	
}

#####################
sub symbol_alt {
#####################

	local ($field) = @_;

if ($field eq "xx") {$symbolalt = "$msg{'517'}";}
if ($field eq "thumbup") {$symbolalt = "$msg{'518'}";}
if ($field eq "thumbdown") {$symbolalt = "$msg{'519'}";}
if ($field eq "exclamation") {$symbolalt = "$msg{'520'}";}
if ($field eq "question") {$symbolalt = "$msg{'521'}";}
if ($field eq "lamp") {$symbolalt = "$msg{'522'}";}

}

##################
sub notify_users {
##################
	open(FILE, "$messagedir/$thread.mail");
	@mails = <FILE>;
	close(FILE);

	foreach $curmail (@mails) {
		$curmail =~ s/[\n\r]//g;
		$notifysubject = "$msg{'142'} $subject";
		$notifymessage = qq~$inf{'016'} $pageurl/$forum$curboard&op=display&num=$thread~;
		sendemail($curmail, $notifysubject, $notifymessage);
	}
}

if (-e "$scriptdir/user-lib/forum_subs.pl") {require "$scriptdir/user-lib/forum_subs.pl"} 

1; # return true

