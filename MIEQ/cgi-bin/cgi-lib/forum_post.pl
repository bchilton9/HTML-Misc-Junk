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

        #if ($settings[14] ne "$root" && $username ne "$boardmoderator") { error("$err{'011'}"); }
      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

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
        if ($username eq $anonuser && $enable_guestposting == 0) { error("noguests"); }

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

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
<td><form  action="$forum&amp;op=poststicky2&amp;start=$info{'start'}" method="post" name="creator">
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
function upload() {
window.open("$pageurl/$cgi?action=uploadpicture","","width=300,height=150,scrollbars")
}
// -->
</script>
<textarea name="message" rows="10" cols="40">$form_message</textarea></td>
</tr>
~;

if ($username eq "admin" || $forumimgupld eq "1" && $username ne "$anonuser") {
print qq~
<tr>
<td>&nbsp;</td>
<td class="formstextnormal" valign="top">
<a href="javascript:upload()">$msg{'598'}</a>
</td>
</tr>
~;
}

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
&smilieblock;
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

        #if ($settings[14] ne "$root" && $username ne "$boardmoderator") { error("$err{'011'}"); }

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

$nsubject = previewstrip($input{'subject'});
$nmessage = previewstrip($input{'message'});

        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
        <tr>
<td><form  action="$forum&amp;op=poststicky2&amp;start=$info{'start'}" method="post" name="creator">
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

                        $sig = "$settings[5]";
                        $sig =~ s/\&\&/<br>/g;
                        if ($sig ne "") {
                                $sig = qq~<br><br><br>
-----------------<br>
$sig
~;

                        }

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
<td class="forumwindow2" width="140" valign="top"><b>$name</b><br>~;

if ($settings[9] eq "") { $settings[9] = "_nopic.gif"; }

if ($settings[9] =~ /^\http:\/\// ) {
        if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
        else { $tmp_width = ""; }
        if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
        else { $tmp_height = ""; }
        $memberpic = qq~<img src="$settings[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
        }

        else {
         $memberpic = qq~<img src="$imagesurl/avatars/$settings[9]" border="0" alt=""></a>~;
 }

print qq~
$memberpic
<br>
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
$sig
<br>
</td>
</tr>
<tr class="forumwindow2">
<td><img src="$imagesurl/forum/ip.gif" alt="$msg{'111'}" align="top">$ENV{'REMOTE_ADDR'}</td>
<td>
<table border="0" cellspacing="0" cellpadding="0" width="100%" maxwidth="80">
<tr>
<td><a href="$settings[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=anonemail&sendto=$username" class="forumnav"><img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=viewprofile&amp;username=$username"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=imsend&amp;to=$username"><img src="$imagesurl/forum/message.gif" alt="$msg{'109'} $name" border="0"></a></td>
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

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

        open (FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        @messages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

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

        if ($input{'followto'} ne "") {
                open(FILE, ">>$messagedir/$followto.txt") || error("$err{'001'} $messagedir/$followto.txt");
        }
        else {
                open(FILE, ">$messagedir/$postnum.txt") || error("$err{'016'} $messagedir/$postnum.txt");
        }
        file_lock(FILE);
        print FILE "$subject|$name|$email|$date|$username|$icon|$ENV{REMOTE_ADDR}|$message\n";
        unfile_lock(FILE);
        close (FILE);

        if ($input{'followto'} ne "") { $thread = "$followto"; }
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
        if ($username eq $anonuser && $enable_guestposting == 0) { error("noguests"); }

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

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
<td><form  action="$forum&amp;op=post2&amp;start=$info{'start'}" method="post" name="creator">
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
function upload() {
window.open("$pageurl/$cgi?action=uploadpicture","","width=300,height=150,scrollbars")
}
// -->
</script>
<textarea name="message" rows="10" cols="40">$form_message</textarea></td>
</tr>
~;

if ($username eq "admin" || $forumimgupld eq "1" && $username ne "$anonuser") {
print qq~
<tr>
<td>&nbsp;</td>
<td class="formstextnormal" valign="top">
<a href="javascript:upload()">$msg{'598'}</a>
</td>
</tr>~;
}

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
&smilieblock;
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
        if ($username eq "$anonuser" && $enable_guestposting == 0) { error("noguests"); }

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


$nsubject = previewstrip($input{'subject'});
$nmessage = previewstrip($input{'message'});

        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
        <tr>
<td><form  action="$forum&amp;op=post2&amp;start=$info{'start'}" method="post" name="creator">
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

                        $sig = "$settings[5]";
                        $sig =~ s/\&\&/<br>/g;
                        if ($sig ne "") {
                                $sig = qq~<br><br><br>
-----------------<br>
$sig
~;
}

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
<td class="forumwindow2" width="140" valign="top"><b>$name</b><br>~;

if ($settings[9] eq "") { $settings[9] = "_nopic.gif"; }

if ($settings[9] =~ /^\http:\/\// ) {
        if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
        else { $tmp_width = ""; }
        if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
        else { $tmp_height = ""; }
        $memberpic = qq~<img src="$settings[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
        }

        else {
         $memberpic = qq~<img src="$imagesurl/avatars/$settings[9]" border="0" alt=""></a>~;
 }

print qq~
$memberpic
<br>
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
$sig
<br>
</td>
</tr>
<tr class="forumwindow2">
<td><img src="$imagesurl/forum/ip.gif" alt="$msg{'111'}" align="top">$ENV{'REMOTE_ADDR'}</td>
<td>
<table border="0" cellspacing="0" cellpadding="0" width="100%" maxwidth="80">
<tr>
<td><a href="$settings[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=anonemail&sendto=$username" class="forumnav"><img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=viewprofile&amp;username=$username"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $name" border="0"></a>&nbsp;&nbsp;<a href="index.cgi?action=imsend&amp;to=$username"><img src="$imagesurl/forum/message.gif" alt="$msg{'109'} $name" border="0"></a></td>
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
        error("$err{'005'}") unless($input{'email'});
        error("$err{'003'}") unless($input{'name'});
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

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

        open (FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        @messages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

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

        if ($input{'followto'} ne "") {
                open(FILE, ">>$messagedir/$followto.txt") || error("$err{'001'} $messagedir/$followto.txt");
        }
        else {
                open(FILE, ">$messagedir/$postnum.txt") || error("$err{'016'} $messagedir/$postnum.txt");
        }
        file_lock(FILE);
        print FILE "$subject|$name|$email|$date|$username|$icon|$ENV{REMOTE_ADDR}|$message\n";
        unfile_lock(FILE);
        close (FILE);

        if ($input{'followto'} ne "") { $thread = "$followto"; }
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



if (-e "$scriptdir/user-lib/forum_post.pl") {require "$scriptdir/user-lib/forum_post.pl"}

1; # return true