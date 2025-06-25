###############################################################################

################
sub boardindex {
################
        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        @categories = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$memberdir/memberlist.dat") || error("$err{'001'} $memberdir/memberlist.dat");
        file_lock(FILE);
        @memberlist = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $totalm = 0;
        $totalt = 0;

        foreach $curcat (@categories) {
                $curcat =~ s/[\n\r]//g;

                open(FILE, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
                file_lock(FILE);
                @catinfo = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                if ($settings[14] eq "Guild Leader") { $rank = 5; }
                if ($settings[14] eq "Officer") { $rank = 4; }
                if ($settings[14] eq "Member") { $rank = 3; }
                if ($settings[14] eq "Recruit") { $rank = 3; }
            if ($settings[14] eq "Friend") { $rank = 1; }

                $catinfo[1] =~ s/[\n\r]//g;

                if ($catinfo[1] eq "Guild Leader") { $catrank = 5; }
                if ($catinfo[1] eq "Officer") { $catrank = 4; }
                if ($catinfo[1] eq "Member") { $catrank = 3; }
                if ($catinfo[1] eq "Recruit") { $catrank = 2; }
            if ($catinfo[1] eq "Friend") { $catrank = 1; }

                if ($catinfo[1] ne "") {
                        if ($settings[14] ne "$root" && $rank < $catrank) { next; } #$settings[14] ne "$catinfo[1]") { next; }
                }

                $curcatname = "$catinfo[0]";
                foreach $curboard (@catinfo) {
                        if ($curboard ne "$catinfo[0]" && $curboard ne "$catinfo[1]") {
                                $curboard =~ s/[\n\r]//g;

                                open(FILE, "$boardsdir/$curboard.txt") || error("$err{'001'} $boardsdir/$curboard.txt");
                                file_lock(FILE);
                                chomp(@messages = <FILE>);
                                unfile_lock(FILE);
                                close(FILE);

                                $tm = @messages;

                                ($dummy, $dummy, $dummy, $dummy, $dummy, $postdate, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $messages[0]);
                                $boardinfo[2] =~ s/[\n\r]//g;
                                $messagecount = 0;
                                for ($a = 0; $a < @messages; $a++) {
                                        ($dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $mreplies, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $messages[$a]);
                                        $messagecount++;
                                        $messagecount = $messagecount+$mreplies;
                                }
                                $totalm = $totalm+$messagecount;
                                $totalt = $totalt+$tm;
                        }
                }
        }

        $navbar = "$btn{'014'} $nav{'003'}";
        print_top();
        print qq~<table width="100%" border="0" cellspacing="1" cellpadding="2">
~;


        undef @allmembers;

        open(FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        chomp(@memberlist = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $thelatestmember = $memberlist[$#memberlist];

        open(FILE, "$memberdir/$thelatestmember.dat");
        file_lock(FILE);
        chomp(@lmsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $tlmname = @lmsettings[1];

        $count = @memberlist;

print qq~
<tr>
        <td align="left" class="webapptext">
        $msg{'029'} $count,&nbsp;&nbsp;$msg{'096'}: $totalt,&nbsp;&nbsp;$msg{'097'}: $totalm<br>
        $msg{'028'} ~; if ($username ne "$anonuser") { print qq~<a href="$cgi?action=viewprofile&amp;username=$thelatestmember">$tlmname</a><br><br>~; } if ($username eq "$anonuser") { print qq~$tlmname<br><br>~; } print qq~
        </td>
</tr>
~;

print qq~
<tr>
<td valign="bottom" class="forumtext"><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;
$nav{'003'}</td>
</tr>
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" class="forumtitlebackcolor">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td width="10" class="boardtitle">&nbsp;</td>
<td nowrap align="left" class="boardtitle">$msg{'095'}</td>
<td nowrap align="center" class="boardtitle">$msg{'096'}</td>
<td nowrap align="center" class="boardtitle">$msg{'097'}</td>
<td nowrap align="center" class="boardtitle">$msg{'098'}</td>
<!-- td nowrap align="left" class="boardtitle">$msg{'099'}</td -->
</tr>
~;

        foreach $curcat (@categories) {
                $curcat =~ s/[\n\r]//g;

                open(FILE, "$boardsdir/$curcat.cat");
                file_lock(FILE);
                chomp(@catinfo = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                if ($settings[14] eq "Guild Leader") { $rank = 5; }
                if ($settings[14] eq "Officer") { $rank = 4; }
                if ($settings[14] eq "Member") { $rank = 3; }
                if ($settings[14] eq "Recruit") { $rank = 3; }
            if ($settings[14] eq "Friend") { $rank = 1; }

                $catinfo[1] =~ s/[\n\r]//g;

                if ($catinfo[1] eq "Guild Leader") { $catrank = 5; }
                if ($catinfo[1] eq "Officer") { $catrank = 4; }
                if ($catinfo[1] eq "Member") { $catrank = 3; }
                if ($catinfo[1] eq "Recruit") { $catrank = 2; }
            if ($catinfo[1] eq "Friend") { $catrank = 1; }

                if ($catinfo[1] ne "") {
                        if ($settings[14] ne "$root" && $rank < $catrank) { next; } #$settings[14] ne "$catinfo[1]") { next; }
                }
                $curcatname = "$catinfo[0]";

                print qq~<tr>
<td width="10" valign="top" class="boardtitle">&nbsp;</td>
<td colspan="5" class="boardtitle">$curcatname</td>
</tr>
~;

                foreach $curboard (@catinfo) {
                        if ($curboard ne "$catinfo[0]" && $curboard ne "$catinfo[1]") {
                                $curboard =~ s/[\n\r]//g;

                                open(FILE, "$boardsdir/$curboard.dat");
                                file_lock(FILE);
                                chomp(@boardinfo = <FILE>);
                                unfile_lock(FILE);
                                close(FILE);

                                $curboardname = "$boardinfo[0]";
                                $descr = "$boardinfo[1]";

                                open(FILE, "$boardsdir/$curboard.txt");
                                file_lock(FILE);
                                chomp(@messages = <FILE>);
                                unfile_lock(FILE);
                                close(FILE);

                                ####### abywn: added to include stickies
                                open(FILE2, "<$boardsdir/$curboard.sticky");
                                file_lock(FILE2);
                                @messagessticky = <FILE2>;
                                unfile_lock(FILE2);
                                close(FILE2);
                                @messages = (@messages, @messagessticky);
                                ####### abywn: end of added code

                                $tm = @messages;
                                if (@messages == 0) { $tm = "0"; }

                                ($dummy, $dummy, $dummy, $dummy, $dummy, $postdate, $dummy, $dummy, $poster, $dummy, $dummy) = split(/\|/, $messages[0]);
                                $boardinfo[2] =~ s/[\n\r]//g;


                                $messagecount = 0;

                                for ($a = 0; $a < @messages; $a++) {
                                        ($dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $mreplies, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $messages[$a]);
                                        $messagecount++;
                                        $messagecount = $messagecount+$mreplies;
                                }

        ($tdate, $dummy) = split(/ - /, $date);
        ($tmonth, $tday, $tyear) = split(/\//, $tdate);
        $todaysdate = ($tyear*365)+($tmonth*30)+$tday; # todays date
        ($pdates, $dummy) = split(/ /, $postdate);
        ($pmonth, $pday, $pyear) = split(/\//, $pdates);
        $pnumber = ($pyear*365)+($pmonth*30)+$pday; # postdate
        $difference = $todaysdate - $pnumber;


                                if ($postdate eq "") { $postdate="???"; }
                                $dlp = readlog("$curboard");
                                $new = qq~<img src="$imagesurl/forum/off.gif" alt="">~;
                                if ($dlp ne "$postdate" && $postdate ne "???" && $username ne "$anonuser" && $difference <= "$max_log_days_old") { $new = qq~<img src="$imagesurl/forum/on.gif" alt="">~; }

                                if ($poster eq "") { $poster = "???"; }
                                else { $poster = "$poster"; }

                                display_date($postdate); $postdate = $user_display_date;

                                print qq~<tr>
<td valign="top" width=10 class="forumwindow2">$new</td>
<td valign="top" class="forumwindow2">
<a href="$cgi?action=forum&amp;board=$curboard" class="forumlink">$curboardname</a><br>
$descr</td>
<td valign="top" width="10%" align="center" class="forumwindow2">$tm</td>
<td valign="top" width="10%" align="center" class="forumwindow2">$messagecount</td>
<td valign="top" width="15%" align="center" class="forumwindow2" nowrap>$postdate<br>($poster)</td>
<!-- td valign="top" width="20%" align="left" class="forumwindow2">~;
################ additions

$howmany = 0;

                                $boardinfo[2] =~ /^\|(.*?)\|$/;

                                $moderators = $boardinfo[2];
                                $moderators =~ s/\|(\S?)/,$1/g;

                                foreach $curuser (split(/ /, $moderators)) {

                                        $howmany++;

                                        open(FILE, "$memberdir/$curuser.dat");
                                        file_lock(FILE);
                                        chomp(@modprop = <FILE>);
                                        unfile_lock(FILE);
                                        close(FILE);

                                        $boardmoderator = '';
                                        $boardmoderator = qq~<a href="$cgi?action=viewprofile&username=$curuser">$modprop[1]</a>~;

                                        if ($howmany > 1) { print ", "; }

                                        print "$boardmoderator";

                                        }
################
print qq~</td -->
</tr>
~;
                        }
                }
        }
        print qq~</table>
</td>
</tr>
</table>~;

($ndate, $ntime) = split(/ - /, $date);
($nhour, $nmin, $nsec) = split(/:/, $ntime);

getTimezones($timezone); $ntime = "$nhour:$nmin $displaytimezone";

print qq~

<table width="100%">
<tr>
<td align="left" class="forumtext">$msg{'564'} $ntime</td><td align="right" class="forumtext">~; if ($username ne "$anonuser") { print qq~<a href="$cgi?action=markasread" class="forumnav">$msg{'565'}</a>~; } print qq~</td>
</tr>
</table>
<table cellpadding="2" cellspacing="0" border="0" width="100%"  align="center">
<tr>
        <td align="center" class="forumtext">
        <img src="$imagesurl/forum/on.gif">&nbsp;$msg{'566'}&nbsp;&nbsp;<img src="$imagesurl/forum/off.gif">&nbsp;$msg{'567'}<br>
        </td>
</tr>
</table>
~;


        print_bottom();
        exit;
}

##################
sub messageindex {
##################

            if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

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

        $navbar = "$btn{'014'} $nav{'003'} $btn{'014'} $boardname";
        print_top();
        print qq~<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td class="forumtext"><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;
<a href="$cgi?action=forum&amp;board=" class="forumnav">$nav{'003'}</a>
<br>
<img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;$boardname</td>
<td align="right" valign="bottom">

<a href="$forum&amp;op=post&amp;title=start+new+thread"><img src="$imagesurl/$langgfx/new_thread.gif" alt="$msg{'100'}" border="0"></a>



<!-- My Code Additions -->

~;

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

if ($access[28] eq "on") { print qq~
&nbsp;&nbsp;

<a href="$forum&amp;op=poststicky&amp;title=start+new+sticky"><img src="$imagesurl/$langgfx/sticky.gif" alt="Create Sticky Thread" border="0"></a>

~;
}
print qq~
<!-- End my code additions -->

</td>

</tr>
</table>
<table width="100%" class="forumtitlebackcolor" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td class="boardtitle" width="16">&nbsp;</td>
<td class="boardtitle" width="15">&nbsp;</td>
<td class="boardtitle" width="40%"><b>$msg{'037'}</b></td>
<td class="boardtitle" width="20%"><b>$msg{'101'}</b></td>
<td class="boardtitle" width="10%" align="center"><b>$msg{'102'}</b></td>
<td class="boardtitle" width="10%" align="center"><b>$msg{'157'}</b></td>
<td class="boardtitle" width="20%" align="center"><b>$msg{'103'}</b></td>
~;

open (FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        chomp(@messages = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $messagecount = 0;
        $threadcount = 0;

        for ($a = 0; $a < @messages; $a++) {
                ($mnum[$a], $msub[$a], $mname[$a], $musername[$a], $memail[$a], $mdate[$a], $mreplies[$a], $stickyviews[$a], $mlpname[$a], $micon[$a], $mstate[$a]) = split(/\|/, $messages[$a]);
                $messagecount++;

                if ($mfollow[$a] == 1) { $threadcount++; }
        }

        $writedate = "$mdate[0]";
        writelog("$currentboard");

if ( $messagecount != 0 ) {

        if ($info{'start'} eq "") { $start = 0; }
        else { $start = "$info{'start'}"; }

        $numshown = 0;

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        chomp(@censored = <CENSOR>);
        unfile_lock(CENSOR);
        close(CENSOR);

        $second="forumwindow3";
        for ($b = $start; $b < @messages; $b++) {
                if ($second eq "forumwindow3") { $second="forumwindow2"; }
                else { $second="forumwindow3"; }
                $numshown++;

                if ($username ne "$anonuser") {
                $date1 = readlog("$mnum[$b]");
                $date2 = "$mdate[$b]";

                checkfornew();

                }

                if ($musername[$b] ne "$anonuser") { }

                foreach $censor (@censored) {
                        ($word, $censored) = split(/\=/, $censor);
                        $msub[$b] =~ s/$word/$censored/g;
                }

                if ($mstate[$b] == 0) { $type = "stickythread"; $typealt = "$msg{'493'}"; }
                if ($mreplies[$b] >= 15 || $stickyviews[$b] >= 75) { $type = "stickyhotthread"; $typealt = "$msg{'495'}"; }
                if ($mreplies[$b] >= 25 || $stickyviews[$b] >= 100) { $type = "stickyveryhotthread"; $typealt = "$msg{'496'}" }
                if ($mstate[$b] == 1) { $type = "stickylocked"; $typealt = "$msg{'497'}" }

                $nummessages = $mreplies[$b]+1;
                $c = 0;
                $pages = "";
                if ($nummessages > $maxmessagedisplay) {
                        while (($c*$maxmessagedisplay) < $nummessages) {
                                $viewc = $c+1;
                                $strt = ($c*$maxmessagedisplay);
                                $pages = qq~$pages<a href="$forum&amp;op=displaysticky&amp;num=$mnum[$b]&amp;start=$strt">$viewc</a>~;
                                $c++;
                        }
                        $pages =~ s/\n$//g;
                        $pages = qq~( <img src="$imagesurl/forum/multipage.gif" alt=""> $pages )~;
                }

                symbol_alt($micon[$b]);

                display_date($mdate[$b]); $mdate[$b] = $user_display_date;

                print qq~<tr>
<td width="16" class="forumwindow1"><img src="$imagesurl/forum/$type.gif" alt="$typealt"></td>
<td width="15" class="forumwindow1"><img src="$imagesurl/forum/$micon[$b].gif" alt="$symbolalt" border="0" align="middle"></td>
<td width="40%" class="forumwindow1"><a href="$forum&amp;op=displaysticky&amp;num=$mnum[$b]" class="forumlink"><b>$msub[$b]</b></a> $new $pages</td>
<td width="20%" class="forumwindow1">$mname[$b]</td>
<td width="10%" align="center" class="forumwindow1">$mreplies[$b]</td>
<td width="10%" align="center" class="forumwindow1">$stickyviews[$b]</td>
<td width="20%" align="center" class="forumwindow1" nowrap>$mdate[$b]<br>$msg{'042'} $mlpname[$b]</td>
</tr>
~;
                $lastposter = "";
                if ($numshown >= $maxdisplay && $info{'view'} ne 'all') { $b = @messages; }
        }
}

        open (FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        chomp(@messages = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $messagecount = 0;
        $threadcount = 0;

        for ($a = 0; $a < @messages; $a++) {
                ($mnum[$a], $msub[$a], $mname[$a], $musername[$a], $memail[$a], $mdate[$a], $mreplies[$a], $mviews[$a], $mlpname[$a], $micon[$a], $mstate[$a]) = split(/\|/, $messages[$a]);
                $messagecount++;
                if ($mfollow[$a] == 1) { $threadcount++; }
        }

        $writedate = "$mdate[0]";
        writelog("$currentboard");

        if ($info{'start'} eq "") { $start = 0; }
        else { $start = "$info{'start'}"; }

        $numshown = 0;

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        chomp(@censored = <CENSOR>);
        unfile_lock(CENSOR);
        close(CENSOR);

        $second="forumwindow3";
        for ($b = $start; $b < @messages; $b++) {
                if ($second eq "forumwindow2") { $second="forumwindow3"; }
                else { $second="forumwindow2"; }
                $numshown++;

                if ($username ne "$anonuser") {
                $date1 = readlog("$mnum[$b]");
                $date2 = "$mdate[$b]";

                checkfornew();
                }

                if ($musername[$b] ne "$anonuser") { }

                foreach $censor (@censored) {
                        ($word, $censored) = split(/\=/, $censor);
                        $msub[$b] =~ s/$word/$censored/g;
                }

                if ($mstate[$b] == 0) { $type = "thread"; $typealt = "$msg{'490'}"; }
                if ($mreplies[$b] >= 15 || $mviews[$b] >= 75) { $type = "hotthread"; $typealt = "$msg{'491'}"; }
                if ($mreplies[$b] >= 25 || $mviews[$b] >= 100) { $type = "veryhotthread"; $typealt = "$msg{'492'}"; }
                if ($mstate[$b] == 1) { $type = "locked"; $typealt = "$msg{'494'}"; }

                $nummessages = $mreplies[$b]+1;
                $c = 0;
                $pages = "";
                if ($nummessages > $maxmessagedisplay) {
                        while (($c*$maxmessagedisplay) < $nummessages) {
                                $viewc = $c+1;
                                $strt = ($c*$maxmessagedisplay);
                                $pages = qq~$pages<a href="$forum&amp;op=display&amp;num=$mnum[$b]&amp;start=$strt" class="forumlink">$viewc</a>~;
                                $c++;
                        }
                        $pages =~ s/\n$//g;
                        $pages = qq~( <img src="$imagesurl/forum/multipage.gif" alt=""> $pages )~;
                }

                symbol_alt($micon[$b]);

                display_date($mdate[$b]); $mdate[$b] = $user_display_date;

                print qq~<tr>
<td width="16" class="$second"><img src="$imagesurl/forum/$type.gif" alt="$typealt"></td>
<td width="15" class="$second"><img src="$imagesurl/forum/$micon[$b].gif" alt="$symbolalt" border="0" align="middle"></td>
<td width="40%" class="$second"><a href="$forum&amp;op=display&amp;num=$mnum[$b]" class="forumlink"><b>$msub[$b]</b></a> $new $pages</td>
<td width="20%" class="$second">$mname[$b]</td>
<td width="10%" align="center" class="$second">$mreplies[$b]</td>
<td width="10%" align="center" class="$second">$mviews[$b]</td>
<td width="20%" align="center" class="$second" nowrap>$mdate[$b]<br>$msg{'042'} $mlpname[$b]</td>
</tr>
~;
                $lastposter = "";
                if ($numshown >= $maxdisplay && $info{'view'} ne 'all') { $b = @messages; }
        }
        print qq~</table>
</td>
</tr>
</table>
<table border="0" width="100%">
<tr>
<td valign="top" class="forumtext">
<img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;$boardname
<br>
<img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$cgi?action=forum&amp;board=" class="forumnav">$nav{'003'}</a></td>
<td align="right" valign="top">
<a href="$forum&amp;op=post&amp;title=start+new+thread"><img src="$imagesurl/$langgfx/new_thread.gif" alt="$msg{'100'}" border="0"></a>

<!-- My Code Additions -->

~;
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

if ($access[28] eq "on") { print qq~
&nbsp;&nbsp;

<a href="$forum&amp;op=poststicky&amp;title=start+new+sticky"><img src="$imagesurl/$langgfx/sticky.gif" alt="$msg{'461'}" border="0"></a>

~;
}
print qq~
<!-- End my code additions -->

</td>
</tr>
<tr>
<td valign="top" class="forumtext"><b>$msg{'039'}</b>
~;
        $nummessages = @messages;
        $c = 0;
        while (($c*$maxdisplay) < $nummessages) {
                $viewc = $c+1;
                $strt = ($c*$maxdisplay);
                if ($start == $strt) { print "[$viewc] "; }
                else { print qq~<a href="$forum&amp;start=$strt" class="forumnav">$viewc</a> ~; }
                ++$c;
        }

        jumpto();

        print qq~</td>
~;

if ($username ne "$anonuser") {

print qq~
<tr>
        <td align="left" class="forumnav">
        <a href="$cgi?action=markpostsread&board=$currentboard" class="forumnav">Mark Posts as Read</a>&nbsp;~;

}

#print qq~
#<td colspan="2" align="right" valign="top" class="forumtext"><form action="$cgi" method="get">$msg{'104'}
#<input type="hidden" name="action" value="forum">
#<select name="board">
#$selecthtml
#</select>
#<input type="submit" class="button" value="$btn{'014'}">
#</form></td>
print qq~</tr>
</table>
~;
        print_bottom();
        exit;
}

if (-e "$scriptdir/user-lib/forum.pl") {require "$scriptdir/user-lib/forum.pl"}

1; # return true
