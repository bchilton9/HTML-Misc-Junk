###############################################################################
# CollapsedSubs: displaysticky
#############
sub displaysticky {
#############

        $viewnum = $info{'num'};
        if ($viewnum !~ /^[0-9]+$/) { error("$err{'006'}" ); }

#
if ($settings[14] ne "$root") {

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        @categories = <FILE>;
        unfile_lock(FILE);
        close(FILE);

foreach $curcat (@categories) {
                $curcat =~ s/[\n\r]//g;

                open(FILE, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
                file_lock(FILE);
                @catinfo = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                $catinfo[1] =~ s/[\n\r]//g;

                if ($settings[14] eq "Guild Leader") { $rank = 5; }
                if ($settings[14] eq "Officer") { $rank = 4; }
                if ($settings[14] eq "Member") { $rank = 3; }
                if ($settings[14] eq "Recruit") { $rank = 3; }
            if ($settings[14] eq "Friend") { $rank = 1; }

                if ($catinfo[1] eq "Guild Leader") { $catrank = 5; }
                if ($catinfo[1] eq "Officer") { $catrank = 4; }
                if ($catinfo[1] eq "Member") { $catrank = 3; }
                if ($catinfo[1] eq "Recruit") { $catrank = 2; }
            if ($catinfo[1] eq "Friend") { $catrank = 1; }


        if ($catinfo[1] ne "") {

                foreach $searchcat (@catinfo) {
                $searchcat =~ s/[\n\r]//g;

                if ($currentboard eq "$searchcat" && $rank < $catrank) {
                        print_top();  print "What are you doing?"; print_bottom(); exit; }

                } }

        }
}
#

        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        chomp(@membergroups = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$messagedir/$viewnum.txt") || error("$err{'001'} $messagedir/$viewnum.txt");
        file_lock(FILE);
        chomp(@messages = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        ($msub, $mname, $memail, $mdate, $musername, $micon, $mip, $mmessage) = split(/\|/, $messages[@messages-1]);
        $writedate = "$date";
        writelog("$viewnum");

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

        open(FILE, "$boardsdir/$currentboard.dat") || error("$err{'001'} $boardsdir/$currentboard.dat!");
        file_lock(FILE);
        chomp(@boardinfo=<FILE>);
        unfile_lock(FILE);
        close(FILE);

        $boardname = "$boardinfo[0]";

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

        open(FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        chomp(@tthreads = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $d = 0;
        while ($tthreads[$d] ne '') { $d++; }
        $count = $d;
        $i = 0;

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

        open(FILE, ">$boardsdir/$currentboard.sticky") || error("$err{'016'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        while ($i < $count) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $tthreads[$i]);
                if ( $viewnum eq $mnum ) {

                        $stickyviews++;

                        print FILE "$mnum|$msub|$mname|$musername|$memail|$mdate|$mreplies|$stickyviews|$mlpname|$micon|$mstate\n";
                }
                elsif ( $viewnum ne $mnum ) { print FILE "$mnum|$msub|$mname|$musername|$memail|$mdate|$mreplies|$stickyviews|$mlpname|$micon|$mstate\n"; }

                $i++;
        }
        unfile_lock(FILE);
        close(FILE);

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing?"; print_bottom(); exit; }

        open(FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        chomp(@threads = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        for ($x = 0; $x < @threads; $x++) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$x]);
                if ($viewnum eq $mnum) {
                        if ($mstate == 0) { $type = "stickythread"; $typealt = "$msg{'493'}"; }
                        if ($mreplies >= 15 || $stickyviews >= 75) { $type = "stickyhotthread"; $typealt = "$msg{'495'}"; }
                        if ($mreplies >= 25 || $stickyviews >= 100) { $type = "stickyveryhotthread"; $typealt = "$msg{'496'}"; }
                        if ($mstate == 1) { $type = "stickylocked"; $typealt = "$msg{'497'}"; }
                        $x = @threads;
                }
        }

        ($msub[0], $mname[0], $memail[0], $mdate[0], $musername[0], $micon[0], $mip[0], $mmessage[0]) = split(/\|/, $messages[0]);
        $title = "$msub[0]";

                $msub[0] = censor_it($msub[0]);

        if ($enable_notification && $username ne $anonuser) {
                $notification = qq~&nbsp;<a href="$forum&amp;op=notify&amp;thread=$viewnum"><img src="$imagesurl/$langgfx/notify.gif" alt="$msg{'105'}" border="0"></a> ~;
        }

        jumpto();

        if ($info{'start'} ne "") { $start = "$info{'start'}"; }
        else { $start = 0; }

        $navbar = "$btn{'014'} $nav{'003'} $btn{'014'} $boardname";
        print_top();
        print qq~<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td valign="bottom" class="forumtext"><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;
<a href="$cgi?action=forum&amp;board=" class="forumnav">$nav{'003'}</a>
<br>
<img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$forum" class="forumnav">$boardname</a>
<br>
<img src="$imagesurl/forum/tline2.gif" width="24" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;$msub[0]</td>
<td align="right" valign="bottom"><a href="$forum&amp;op=printpage&amp;num=$viewnum" target="_blank"><img src="$imagesurl/forum/print.gif" alt="$msg{'106'}" border=0></a><br>
<a href="$forum&amp;op=poststicky&amp;num=$viewnum&amp;title=post+reply&amp;start=$start" class="forumnav"><img src="$imagesurl/$langgfx/reply.gif" alt="$msg{'107'}" border="0"></a>$notification</td>
</tr>
</table>
<table width="100%" class="forumtitlebackcolor" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td class="forumwindow3">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td><img src="$imagesurl/forum/$type.gif" alt="$typealt"></td>
<td class="forumtext">&nbsp;<b>$msg{'049'}</b></td>
</tr>
</table>
</td>
<td class="forumwindow3"><b>$msg{'064'} $msub[0]</b></td>
</tr>
~;
        $second = "forumwindow3";
        for ($a = $start; $a < @messages; $a++) {

                if ($second eq "forumwindow2") { $second="forumwindow3"; }
                else { $second="forumwindow2"; }
                $numshown++;
                ($msub[$a], $mname[$a], $memail[$a], $mdate[$a], $musername[$a], $micon[$a], $mip[$a], $mmessage[$a]) = split(/\|/, $messages[$a]);

                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }
                $mmessage[$a] =~ s/\n//g;
                $message = "$mmessage[$a]";
                $name = "$mname[$a]";
                $messagedate = "$mdate[$a]";
                display_date($messagedate); $messagedate = $user_display_date;

                if ($access[33] eq "on") { $ip = "$mip[$a]"; }
                else { $ip = "$msg{'108'}"; }

                $removed = 0;
                if (!(-e("$memberdir/$musername[$a].dat"))) { $removed = 1; }
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $sendm = "";
                $memberinfo = "";
                $memberpic = "";
                $memset[9] = "";

                if ($musername[$a] ne "$anonuser" && $removed == 0) {
                if ($username ne "$anonuser") { $sendm = qq~&nbsp;&nbsp;<a href="$cgi?action=imsend&amp;to=$musername[$a]"><img src="$imagesurl/forum/message.gif" alt="$msg{'109'} $mname[$a]" border="0"></a>~; }

                        open(FILE, "$memberdir/$musername[$a].dat");
                        file_lock(FILE);
                        chomp(@memset = <FILE>);
                        unfile_lock(FILE);
                        close(FILE);

                        if ($memset[4] eq "") { $memset[4] = "$pageurl/index.cgi"; }
                        if ($memset[4] eq "http://") { $memset[4] = "$pageurl/index.cgi"; }

                        $ranking = $memset[6]+$memset[11]+$memset[12];

                        $postinfo = qq~$msg{'021'} $memset[6]~;

                        if ($username ne "$anonuser") {
                                $viewd = qq~&nbsp;&nbsp;<a href="$cgi?action=viewprofile&amp;username=$musername[$a]"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $mname[$a]" border="0"></a>~;
                        }
                        $memberinfo = "$membergroups[2]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        if ($ranking > 25) {
                                #$memberinfo = "$membergroups[3]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 50) {
                                #$memberinfo = "$membergroups[4]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 75) {
                                #$memberinfo = "$membergroups[5]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 100) {
                                #$memberinfo = "$membergroups[6]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 250) {
                                #$memberinfo = "$membergroups[7]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                        }
                        #if ($ranking > 500) {
                        #        #$memberinfo = "$membergroups[8]";
                        #        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                        #}
                        #if ($boardmoderator eq "$musername[$a]") { $memberinfo = "$membergroups[1]"; }
                        #if ($memset[7] ne "") { $memberinfo = "$memset[7]"; }
                        #if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }

#if ($memset[7] eq "Administrator") {
#$memberinfo = "Sanctuary $memset[14]<BR>Sanctuary $memset[7]";
#}
#elsif ($boardmoderator eq "$musername[$a]") {
#$memberinfo = "Sanctuary $memset[14]<BR>Sanctuary $memset[7]";
#}
#else {
$memberinfo = "$memset[14]";
#}

                        $signature = "$memset[5]";
                        $signature =~ s/\&\&/<br>/g;
                        if ($signature ne "") {
                                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;

                        }
                        if (!($memset[8] =~ /\D/) && $memset[8] ne "") { $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~; }
                }
                else { $memberinfo = "$anonuser"; }

                $message = "$message\n$signature";
                $memberpic ="";

                if ($musername[$a] ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                }

                if ($enable_ubbc) { doubbc(); }
                if ($enable_smile) { dosmilies(); }

                $url = "";
                if ($memset[3] ne "" && $musername[$a] ne "$anonuser") { $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $mname[$a]" border="0"></a>&nbsp;&nbsp;~; }

                $message = censor_it($message);
                $subject = censor_it($subject);

                if ($access[33] ne "on") { $ip = "$msg{'108'}"; }

                symbol_alt($micon[$a]);

$sname = showhtml($name);
#$spostinfo = showhtml($postinfo);

                print qq~<tr>
<td class="$second" width="140" valign="top"><b>$sname</b><br>
$memberinfo<br>
$memberpic<br><BR>
$star<br>
$postinfo<BR><BR>
</td>
<td class="$second" valign="top">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
<td><img src="$imagesurl/forum/$micon[$a].gif" alt="$symbolalt"></td>
<td width="100%">&nbsp;<b>$subject</b></td>
<td align="right" nowrap>&nbsp;<b>$msg{'110'}</b> $messagedate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message<br>
</td>
</tr>
<tr class="$second">
<td><img src="$imagesurl/forum/ip.gif" alt="$msg{'111'}" align="top"> $ip</td>
<td>
<table border="0" cellspacing="0" cellpadding="0" width="100%" maxwidth="80">
<tr>
<td>$url~; if ($hidemail eq "1" && $musername[$a] ne "$anonuser") {
print qq~<a href="$cgi?action=anonemail&sendto=$musername[$a]" class="forumnav">~; }
else { print qq~<a href="mailto:$memail[$a]">~; } print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $mname[$a]" border="0"></a>$viewd$sendm$icq</td>
<td align="right"><a href="$forum&amp;op=poststicky&amp;num=$viewnum&amp;quote=$a&amp;title=post+reply&amp;start=$start"><img src="$imagesurl/forum/quote.gif" alt="$msg{'056'}" border="0"></a>~; if ($username ne $anonuser) {print qq~&nbsp;&nbsp;<a href="$forum&amp;op=modifysticky&amp;message=$a&amp;thread=$viewnum"><img src="$imagesurl/forum/modify.gif" alt="$msg{'112'}" border="0"></a>&nbsp;&nbsp;<a href="$forum&amp;op=modifysticky2&amp;thread=$viewnum&amp;id=$a&amp;d=1"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a>~;} print qq~</td>
</tr>
</table>
</td>
</tr>
~;
                if ($numshown >= $maxmessagedisplay) { $a = @messages; }
        }

        print qq~</table>
</td>
</tr>
</table>
<table border="0" width="100%" cellspacing="1" cellpadding="2">
<tr>
<td valign="bottom" class="forumtext"><img src="$imagesurl/forum/tline2.gif" width="24" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;$msub[0]
<br>
<img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$forum" class="forumnav">$boardname</a>
<br>
<img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;
<a href="$cgi?action=forum&amp;board=" class="forumnav">$nav{'003'}</a>
</td>
<td align="left" valign="top">
~;
      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

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

if($username eq "$boardmoderator" || $access[32] eq "on") { $adminfunction = qq~<a href="$forum&amp;op=movestickythread&amp;thread=$viewnum"><img src="$imagesurl/forum/move.gif" alt="$msg{'113'}" border="0"></a>&nbsp;~; }
if($username eq "$boardmoderator" || $access[31] eq "on") { $adminfunction = qq~$adminfunction<a href="$forum&amp;op=removestickythread&amp;thread=$viewnum"><img src="$imagesurl/forum/remove.gif" alt="$msg{'114'}" border="0"></a>&nbsp;~; }
if($username eq "$boardmoderator" || $access[30] eq "on") { $adminfunction = qq~$adminfunction<a href="$forum&amp;op=lockstickythread&amp;thread=$viewnum"><img src="$imagesurl/forum/lock.gif" alt="$msg{'115'}" border="0"></a>~; }

        print qq~$adminfunction</td>

<td align="right" valign="top"><a href="$forum&amp;op=poststicky&amp;num=$viewnum&amp;title=post+reply&amp;start=$start"><img src="$imagesurl/$langgfx/reply.gif" alt="$msg{'107'}" border="0"></a>$notification</td>
</tr>
<tr>
<tr>
<td valign="top" class="forumtext"><b>$msg{'039'}</b>
~;

        $nummessages = @messages;
        $c = 0;
        while (($c*$maxmessagedisplay) < $nummessages) {
                $viewc = $c+1;
                $strt = ($c*$maxmessagedisplay);
                if ($start == $strt) { print "[$viewc] "; }
                else { print qq~<a href="$forum$curboard&amp;op=displaysticky&amp;num=$viewnum&amp;start=$strt">$viewc</a> ~; }
                $c++;
        }

print qq~</td>~;
#<td colspan="2" align="right" valign="top" class="forumtext"><form onSubmit="submitonce(this)" onSubmit="submitonce(this)" action="$cgi" method="get">
#$msg{'104'} <select name="board">$selecthtml</select> <input type="submit" class="button" value="$btn{'014'}">
#<input type="hidden" name="action" value="forum"></form></td>
print qq~</tr>
</table>
~;

        print_bottom();
        exit;
}

#############
sub display {
#############
        $viewnum = $info{'num'};
        if ($viewnum !~ /^[0-9]+$/) { error("$err{'006'}" ); }

#
if ($settings[14] ne "$root") {

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        @categories = <FILE>;
        unfile_lock(FILE);
        close(FILE);

foreach $curcat (@categories) {
                $curcat =~ s/[\n\r]//g;

                open(FILE, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
                file_lock(FILE);
                @catinfo = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                $catinfo[1] =~ s/[\n\r]//g;


                if ($settings[14] eq "Guild Leader") { $rank = 5; }
                if ($settings[14] eq "Officer") { $rank = 4; }
                if ($settings[14] eq "Member") { $rank = 3; }
                if ($settings[14] eq "Recruit") { $rank = 3; }
            if ($settings[14] eq "Friend") { $rank = 1; }

                if ($catinfo[1] eq "Guild Leader") { $catrank = 5; }
                if ($catinfo[1] eq "Officer") { $catrank = 4; }
                if ($catinfo[1] eq "Member") { $catrank = 3; }
                if ($catinfo[1] eq "Recruit") { $catrank = 2; }
            if ($catinfo[1] eq "Friend") { $catrank = 1; }

        if ($catinfo[1] ne "") {

                foreach $searchcat (@catinfo) {
                $searchcat =~ s/[\n\r]//g;

                if ($currentboard eq "$searchcat" && $rank < $catrank) {
                        print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

                } }

        }
}

#

        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        chomp(@membergroups = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$messagedir/$viewnum.txt") || error("$err{'001'} $messagedir/$viewnum.txt");
        file_lock(FILE);
        chomp(@messages = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        ($msub, $mname, $memail, $mdate, $musername, $micon, $mip, $mmessage) = split(/\|/, $messages[@messages-1]);
        $writedate = "$date";
        writelog("$viewnum");

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        open(FILE, "$boardsdir/$currentboard.dat") || error("$err{'001'} $boardsdir/$currentboard.dat!");
        file_lock(FILE);
        chomp(@boardinfo=<FILE>);
        unfile_lock(FILE);
        close(FILE);

        $boardname = "$boardinfo[0]";

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        open(FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        chomp(@tthreads = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $d = 0;
        while ($tthreads[$d] ne '') { $d++; }
        $count = $d;
        $i = 0;

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        open(FILE, ">$boardsdir/$currentboard.txt") || error("$err{'016'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        while ($i < $count) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $tthreads[$i]);
                if ($viewnum eq $mnum) {
                        $mviews++;
                        print FILE "$mnum|$msub|$mname|$musername|$memail|$mdate|$mreplies|$mviews|$mlpname|$micon|$mstate\n";
                }
                else { print FILE "$mnum|$msub|$mname|$musername|$memail|$mdate|$mreplies|$mviews|$mlpname|$micon|$mstate\n"; }

                $i++;
        }
        unfile_lock(FILE);
        close(FILE);

      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        open(FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        chomp(@threads = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        for ($x = 0; $x < @threads; $x++) {



                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$x]);
                if ($viewnum eq $mnum) {
                        if ($mstate == 0) { $type = "thread"; $typealt = "$msg{'490'}"; }
                        if ($mreplies >= 15 || $mviews >= 75) { $type = "hotthread"; $typealt = "$msg{'491'}"; }
                        if ($mreplies >= 25 || $mviews >= 100) { $type = "veryhotthread"; $typealt = "$msg{'492'}"; }
                        if ($mstate == 1) { $type = "locked"; $typealt = "$msg{'494'}"; }
                        $x = @threads;
                }
        }

        ($msub[0], $mname[0], $memail[0], $mdate[0], $musername[0], $micon[0], $mip[0], $mmessage[0]) = split(/\|/, $messages[0]);
        $title = "$msub[0]";

                $msub[0] = censor_it($msub[0]);

        if ($enable_notification && $username ne $anonuser) {
                $notification = qq~&nbsp;<a href="$forum&amp;op=notify&amp;thread=$viewnum"><img src="$imagesurl/$langgfx/notify.gif" alt="$msg{'105'}" border="0"></a> ~;
        }

        jumpto();

        if ($info{'start'} ne "") { $start = "$info{'start'}"; }
        else { $start = 0; }

        $navbar = "$btn{'014'} $nav{'003'} $btn{'014'} $boardname";
        print_top();
        print qq~<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td valign="bottom" class="forumtext"><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;
<a href="$cgi?action=forum&amp;board=">$nav{'003'}</a>
<br>
<img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$forum" class="forumnav">$boardname</a>
<br>
<img src="$imagesurl/forum/tline2.gif" width="24" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;$msub[0]</td>
<td align="right" valign="bottom"><a href="$forum&amp;op=printpage&amp;num=$viewnum" target="_blank"><img src="$imagesurl/forum/print.gif" alt="$msg{'106'}" border=0></a><br>
<a href="$forum&amp;op=post&amp;num=$viewnum&amp;title=post+reply&amp;start=$start"><img src="$imagesurl/$langgfx/reply.gif" alt="$msg{'107'}" border="0"></a>$notification</td>
</tr>
</table>
<table width="100%" class="forumtitlebackcolor" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td class="boardtitle">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td><img src="$imagesurl/forum/$type.gif" alt="$typealt"></td>
<td>&nbsp;<b>$msg{'049'}</b></td>
</tr>
</table>
</td>
<td class="boardtitle"><b>$msg{'064'} $msub[0]</b></td>
</tr>
~;
        $second = "forumwindow3";
        for ($a = $start; $a < @messages; $a++) {

                if ($second eq "forumwindow2") { $second="forumwindow3"; }
                else { $second="forumwindow2"; }
                $numshown++;
                ($msub[$a], $mname[$a], $memail[$a], $mdate[$a], $musername[$a], $micon[$a], $mip[$a], $mmessage[$a]) = split(/\|/, $messages[$a]);

                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }
                $mmessage[$a] =~ s/\n//g;
                $message = "$mmessage[$a]";
                $name = "$mname[$a]";
                $messagedate = "$mdate[$a]";
                display_date($messagedate); $messagedate = $user_display_date;

                if ($access[33] eq "on") { $ip = "$mip[$a]"; }
                else { $ip = "$msg{'108'}"; }

                $removed = 0;
                if (!(-e("$memberdir/$musername[$a].dat"))) { $removed = 1; }
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $sendm = "";
                $memberinfo = "";
                $memberpic = "";
                $memset[9] = "";

                if ($musername[$a] ne "$anonuser" && $removed == 0) {
                        if ($username ne "$anonuser") { $sendm = qq~&nbsp;&nbsp;<a href="$cgi?action=imsend&amp;to=$musername[$a]"><img src="$imagesurl/forum/message.gif" alt="$msg{'109'} $mname[$a]" border="0"></a>~; }

                        open(FILE, "$memberdir/$musername[$a].dat");
                        file_lock(FILE);
                        chomp(@memset = <FILE>);
                        unfile_lock(FILE);
                        close(FILE);

                        if ($memset[4] eq "") { $memset[4] = "$pageurl/index.cgi"; }
                        if ($memset[4] eq "http://") { $memset[4] = "$pageurl/index.cgi"; }

                        $ranking = $memset[6]+$memset[11]+$memset[12];

                        $postinfo = qq~$msg{'021'} $memset[6]~;

                        if ($username ne "$anonuser") {
                                $viewd = qq~&nbsp;&nbsp;<a href="$cgi?action=viewprofile&amp;username=$musername[$a]"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $mname[$a]" border="0"></a>~;
                        }
                        $memberinfo = "$membergroups[2]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        if ($ranking > 25) {
                                #$memberinfo = "$membergroups[3]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 50) {
                                #$memberinfo = "$membergroups[4]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 75) {
                                #$memberinfo = "$membergroups[5]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 100) {
                                #$memberinfo = "$membergroups[6]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/starG.gif" alt="" border="0">~;
                        }
                        if ($ranking > 250) {
                                #$memberinfo = "$membergroups[7]";
                                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                        }
                        #if ($ranking > 500) {
                        #        #$memberinfo = "$membergroups[8]";
                        #        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                        #}
                        #$boardmoderator eq "$musername[$a]" $memberinfo = "$membergroups[1]"; }
                        #if ($memset[7] ne "") { $memberinfo = "$memset[7]"; }
                        #if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }

#if ($memset[7] eq "Administrator") {
#$memberinfo = "Sanctuary $memset[14]<BR>Sanctuary $memset[7]";
#}
#elsif ($boardmoderator eq "$musername[$a]") {
#$memberinfo = "Sanctuary $memset[14]<BR>Sanctuary $memset[7]";
#}
#else {
$memberinfo = "$memset[14]";
#}

                        $signature = "$memset[5]";
                        $signature =~ s/\&\&/<br>/g;
                        if ($signature ne "") {
                                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;

                        }
                        if (!($memset[8] =~ /\D/) && $memset[8] ne "") { $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~; }
                }
                else { $memberinfo = "$anonuser"; }

                $message = "$message\n$signature";
                $memberpic ="";

                if ($musername[$a] ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                }

                if ($enable_ubbc) { doubbc(); }
                if ($enable_smile) { dosmilies(); }

                $url = "";
                if ($memset[3] ne "\n" && $musername[$a] ne "$anonuser") { $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $mname[$a]" border="0"></a>&nbsp;&nbsp;~; }

                $message = censor_it($message);
                $subject = censor_it($subject);

                if ($access[33] ne "on") { $ip = "$msg{'108'}"; }

                symbol_alt($micon[$a]);

$sname = showhtml($name);
#$spostinfo = showhtml($postinfo);

                print qq~<tr>
<td class="$second" width="140" valign="top"><b>$sname</b><br>
$memberinfo<br>
$memberpic<br><BR>
$star<br>
$postinfo<br><BR>
</td>
<td class="$second" valign="top">
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
<td><img src="$imagesurl/forum/$micon[$a].gif" alt="$symbolalt"></td>
<td width="100%">&nbsp;<b>$subject</b></td>
<td align="right" nowrap>&nbsp;<b>$msg{'110'}</b> $messagedate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message<br>
</td>
</tr>
<tr class="$second">
<td><img src="$imagesurl/forum/ip.gif" alt="$msg{'111'}" align="top"> $ip</td>
<td>
<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
<td>$url~; if ($hidemail eq "1" && $musername[$a] ne "$anonuser") { print qq~<a href="$cgi?action=anonemail&sendto=$musername[$a]">~; } else { print qq~<a href="mailto:$memail[$a]">~; } print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $mname[$a]" border="0"></a>$viewd$sendm$icq</td>
<td align="right"><a href="$forum&amp;op=post&amp;num=$viewnum&amp;quote=$a&amp;title=post+reply&amp;start=$start"><img src="$imagesurl/forum/quote.gif" alt="$msg{'056'}" border="0"></a>~; if ($username ne $anonuser) {print qq~&nbsp;&nbsp;<a href="$forum&amp;op=modify&amp;message=$a&amp;thread=$viewnum"><img src="$imagesurl/forum/modify.gif" alt="$msg{'112'}" border="0"></a>&nbsp;&nbsp;<a href="$forum&amp;op=modify2&amp;thread=$viewnum&amp;id=$a&amp;d=1"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a>~;} print qq~</td>
</tr>
</table>
</td>
</tr>
~;
                if ($numshown >= $maxmessagedisplay) { $a = @messages; }
        }

        print qq~</table>
</td>
</tr>
</table>
<table border="0" width="100%" cellspacing="1" cellpadding="2">
<tr>
<td valign="bottom" class="forumtext"><img src="$imagesurl/forum/tline2.gif" width="24" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;$msub[0]
<br>
<img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$forum" class="forumnav" class="forumnav">$boardname</a>
<br>
<img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;
<a href="$cgi?action=forum&amp;board=" class="forumnav">$nav{'003'}</a></td>
<td align="left" valign="top">
~;
      if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
                        if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

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

if($username eq "$boardmoderator" || $access[32] eq "on") { $adminfunction = qq~<a href="$forum&amp;op=movethread&amp;thread=$viewnum"><img src="$imagesurl/forum/move.gif" alt="$msg{'113'}" border="0"></a>&nbsp;~; }
if($username eq "$boardmoderator" || $access[31] eq "on") { $adminfunction = qq~$adminfunction<a href="$forum&op=removethread&amp;thread=$viewnum"><img src="$imagesurl/forum/remove.gif" alt="$msg{'114'}" border="0"></a>&nbsp;~; }
if($username eq "$boardmoderator" || $access[30] eq "on") { $adminfunction = qq~$adminfunction<a href="$forum&amp;op=lockthread&amp;thread=$viewnum"><img src="$imagesurl/forum/lock.gif" alt="$msg{'115'}" border="0"></a>~; }

        print qq~$adminfunction
        </td>
<td align="right" valign="top"><a href="$forum&amp;op=post&amp;num=$viewnum&amp;title=post+reply&amp;start=$start"><img src="$imagesurl/$langgfx/reply.gif" alt="$msg{'107'}" border="0"></a>$notification</td>
</tr>
<tr><td class="forumtext" valign="top"><b>$msg{'039'}</b>
~;

        $nummessages = @messages;
        $c = 0;
        while (($c*$maxmessagedisplay) < $nummessages) {
                $viewc = $c+1;
                $strt = ($c*$maxmessagedisplay);
                if ($start == $strt) { print "[$viewc] "; }
                else { print qq~<a href="$forum$curboard&amp;op=display&amp;num=$viewnum&amp;start=$strt">$viewc</a> ~; }
                $c++;
        }
print qq~</td>~;
#<td align="right" colspan="2" class="forumtext"><form onSubmit="submitonce(this)" action="$cgi" method="get">
#$msg{'104'} <select name="board">$selecthtml</select> <input type="submit" class="button" value="$btn{'014'}">
#<input type="hidden" name="action" value="forum"></form></td>
print qq~</tr>
</table>
~;
        print_bottom();
        exit;
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
      if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

print "Content-type: text/html\n\n";
print qq~
<html>
<head>
<title>
$pagename
</title>
</head>
<body>~;

        if ($info{'num'} ne "") {
                open(FILE, "$messagedir/$info{'num'}.txt") || error("$err{'001'} $messagedir/$info{'num'}.txt");
                file_lock(FILE);
                chomp(@messages = <FILE>);
                unfile_lock(FILE);
                close(FILE);
        }

                foreach $line (@messages) { $numshown++; }

                for ($a = 0; $a < 1; $a++) {
                        @item = split (/\|/, $messages[$a]);

                        $message = $item[7];
                        if ($enable_ubbc) { doubbctopic(); }
                        if ($enable_smile) { dosmilies(); }
                        display_date($item[3]); $item[3] = "$msg{'054'} $user_display_date";
                        if ($item[1] eq "") { $item[1] = "$msg{'183'}"; }
                }

                        print qq~
                        <table border="0" cellpadding="3" cellspacing="3" width="100%">
                        <tr>
                        <td><font face="arial" size="4" color="#003399"><img src="$imagesurl/forum/$item[5].gif" alt="">&nbsp;<b>$item[0]</b></font></td>
                        </tr>
                        <tr>
                        <td><font face="arial" size="-3" color="#000000">$item[3] $msg{'042'} <b>$item[1]</b>
                        </td>
                        </tr>
                        <tr>
                        <td valign="top"><font face="arial" size="-1" color="#000000">$message</font></td>
                        </tr>~;

        if ($numshown > 1) {print qq~
                                 <tr>
                                 <td><hr align="left" width="200"><font face="arial" size="3" color="#003399"><b>$msg{'585'}</b></font></td>
                                 </tr>
                                 <tr>
                                 <td>&nbsp;</td>
                                 </tr>~;

                for ($a = 1; $a < $numshown; $a++) {
                        @item = split (/\|/, $messages[$a]);

                        $message = $item[7];
                        if ($enable_ubbc) { doubbctopic(); }
                        if ($enable_smile) { dosmilies(); }
                        display_date($item[3]); $item[3] = "$msg{'054'} $user_display_date";
                        if ($item[1] eq "") { $item[1] = "$msg{'183'}"; }

                        if ($item[5] ne "") { print qq~
                        <tr>
                        <td><font face="arial" size="2" color="#003399"><img src="$imagesurl/forum/$item[5].gif" alt="">&nbsp;<b>$item[0]</b></font></td>
                        </tr>
                        <tr>
                        <td><font face="arial" size="-3" color="#000000">$item[3] $msg{'042'} <b>$item[1]</b>
                        </td>
                        </tr>
                        <tr>
                        <td valign="top"><font face="arial" size="-1" color="#000000">$message</font></td>
                        </tr>~;
                        if ($a < ($numshown-1)) { print qq~
                        <tr>
                        <td><hr align="left" width="200"></td>
                        </tr>~;
                        }
                        }
                }
        }

                        print qq~
                        <tr>
                        <td><hr><center><small>$msg{'534'} <b>$pagename</b><br>$msg{'159'}<br></small></center></td>
                        </tr>
                        </table>
                        </body>
                        </html>~;


exit;
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

        ($tdate, $dummy) = split(/ - /, $date);
        ($tmonth, $tday, $tyear) = split(/\//, $tdate);
        $todaysdate = ($tyear*365)+($tmonth*30)+$tday; # todays date
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
                 $datedifference = $todaysdate-$number2;
                 if ($datedifference <= $max_log_days_old) {
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

if (-e "$scriptdir/user-lib/forum_display.pl") {require "$scriptdir/user-lib/forum_display.pl"}

1; # return true