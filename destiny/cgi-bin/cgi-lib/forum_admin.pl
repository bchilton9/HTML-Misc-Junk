###############################################################################
############################################################################### # CollapsedSubs: modifystickymessage  modifystickymessage2  movestickythread  movestickythread2  removestickythread  removestickythread2  lockstickythread  modifymessage  modifymessage2  movethread  removethread  removethread2  lockthread


#########################
sub modifystickymessage {
#########################

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
        open(FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        chomp(@threads = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        for ($x = 0; $x < @threads; $x++) {
($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$x]);
                if ($info{'thread'} eq $mnum && $mstate == 1) {
                        error("$err{'024'}");
                        $x = @threads;
                }
        }

        $viewnum = $info{'message'};
        $viewnum = int($viewnum);

        open (FILE, "$messagedir/$info{'thread'}.txt") || error("$err{'001'} $messagedir/$info{'thread'}.txt");
        file_lock(FILE);
        chomp(@messages = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        ($msubject, $mname, $memail, $mdate, $musername, $micon, $mip,  $mmessage) = split(/\|/, $messages[$viewnum]);
        $mmessage = htmltotext($mmessage);

        if($musername ne "$username" && $access[30] ne "on" || $username eq "$anonuser") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'003'} $btn{'014'} $nav{'035'}";
        print_top();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
<td><form onSubmit="submitonce(this)" action="$forum$curboard&op=modifystickymessage2" method="post" name="creator">
<input type="hidden" name="viewnum" value="$viewnum">
<input type="hidden" name="thread" value="$info{'thread'}">
<table border="0">
<tr>
<td class="formstextnormal">$msg{'013'}</td>
<td>$mname</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'007'}</td>
<td>~;

if ($hidemail eq "1" || $hidemail eq "") { print qq~???~; }
if ($hidemail eq "0") { print qq~$memail~; }

print qq~</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'037'}</td>
<td><input type=text name="subject" value="$msubject" size="40" maxlength="50"></font></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'116'}</td>
<td><script language="javascript" type="text/javascript">
<!--
function showImage() {
document.images.icons.src="$imagesurl/forum/"+document.creator.icon.options[document.creator.icon.selectedIndex].value+".gif";
// -->
}
</script>
<select name="icon" onChange="showImage()">
<option value="$micon">$msg{'142'}</option>
<option value="xx">$msg{'143'}</option>
<option value="thumbup">$msg{'144'}</option>
<option value="thumbdown">$msg{'145'}</option>
<option value="exclamation">$msg{'146'}</option>
<option value="question">$msg{'147'}</option>
<option value="lamp">$msg{'148'}</option>
</select>
<img src="$imagesurl/forum/$micon.gif" name="icons" width="15" height="15" border="0" hspace="15"></td>
</tr>
<tr>
<td class="formstextnormal" valign="top">$msg{'038'}</td>
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
<textarea name="message" rows="10" cols="40">$mmessage</textarea></td>
~;
if ($enable_ubbc eq "1") {print qq~
<tr>
<td class="formstextnormal">$msg{'156'}</td>
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
</tr>~; }

#smiliebfile_lock();

print qq~
</tr>
<tr>
<td align=center colspan="2"><input type="submit" class="button" name="moda" value="$btn{'015'}">&nbsp;<input type="submit" class="button" name="moda" value="$btn{'011'}"></td>
</tr>
</form>
</td>
</tr>~;
show_legend();
print qq~
</table>
~;

        print_bottom();
        exit;
}

####################
sub modifystickymessage2 {
####################
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

        if ($info{'d'} eq "1") {
                if($access[30] ne "on") { error("$err{'011'}"); }
                $input{'viewnum'} = "$info{'id'}";
                $input{'thread'} = $info{'thread'};
                $input{'moda'} = "$btn{'016'}";
        }

        open (FILE, "$messagedir/$input{'thread'}.txt") || error("$err{'001'} $messagedir/$input{'thread'}.txt");
        file_lock(FILE);
        @messages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        for ($a = 0; $a < @messages; $a++) {
                ($msub[$a], $mname[$a], $memail[$a], $mdate[$a], $musername[$a], $micon[$a], $mip[$a], $mmessage[$a]) = split(/\|/, $messages[$a]);
        }
        $count = $a;
        if ($input{'viewnum'} == 0 && $count > 1 && $input{'moda'} eq $btn{'016'}) { error("$err{'025'}"); }
        if ($a eq $input{'viewnum'}) {
                if ($musername[$a] ne "$username" && (!exists $moderators{$username}) && $access[30] ne "on" || $username eq "$anonuser") { error("$err{'011'}"); }
        }

        open (FILE, ">$messagedir/$input{'thread'}.txt") || error("$err{'001'} $messagedir/$input{'thread'}.txt");
        file_lock(FILE);
        for ($x = 0; $x < @messages; $x++) {
                if ($input{'viewnum'} eq $x) {
                        if ($input{'moda'} eq $btn{'016'}) {
                                open (FILE2, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.dat");
                                file_lock(FILE2);
                                @threads = <FILE2>;
                                unfile_lock(FILE2);
                                close (FILE2);

                                open (FILE2, ">$boardsdir/$currentboard.sticky") || error("$err{'016'} $boardsdir/$currentboard.dat");
                                file_lock(FILE2);
                                for ($a = 0; $a < @threads; $a++) {
                                        if ($x == (@messages-1)) { $tdate = "$mdate[@messages-2]"; }
                                        if ($x == (@messages-1)) { $tlpname = "$mname[@messages-2]"; }
                                        else { $tdate = "$mdate[$x]"; }

                                        ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$a]);
                                        $mstate =~ s/[\n\r]//g;
                                        $mreplies--;

                                        if ($mnum == $input{'thread'}) {
                                                print FILE2 "$mnum|$msub|$mname|$musername|$memail|$tdate|$mreplies|$stickyviews|$tlpname|$micon|$mstate\n";
                                        }
                                        else { print FILE2 "$threads[$a]"; }
                                }
                                unfile_lock(FILE2);
                                close(FILE2);

                                if($musername[$x] ne "$anonuser") {

                                if (-e ("$memberdir/$musername[$x].dat")) {

                                        open(FILE2, "$memberdir/$musername[$x].dat") || error("$err{'010'}");
                                        file_lock(FILE2);
                                        chomp(@memsett = <FILE2>);
                                        unfile_lock(FILE2);
                                        close(FILE2);

                                        $memsett[6]--;
                                        open(FILE2, ">$memberdir/$musername[$x].dat") || error("$err{'016'} $memberdir/$musername[$x].dat");
                                        file_lock(FILE2);
                                        for ($i = 0; $i < @memsett; $i++) {
                                                print FILE2 "$memsett[$i]\n";
                                        }
                                        unfile_lock(FILE2);
                                        close(FILE2);
                                        }
                                }
                        }
                        else {
                                $name = htmlescape($input{'name'});
                                $email = htmlescape($input{'email'});
                                $subject = htmlescape($input{'subject'});
                                $message = htmlescape($input{'message'});
                                $icon = "$input{'icon'}";

                                if ($input{'viewnum'} == 0) {
                                        open (FILE2, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.dat");
                                        file_lock(FILE2);
                                        @threads = <FILE2>;
                                        unfile_lock(FILE2);
                                        close (FILE2);

                                        open (FILE2, ">$boardsdir/$currentboard.sticky");
                                        file_lock(FILE2);
                                        for ($a = 0; $a < @threads; $a++) {
                                                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$a]);
                                                $mstate =~ s/[\n\r]//g;
                                                if ($mnum eq "$input{'thread'}") {
                                                        print FILE2 "$mnum|$subject|$mname|$musername|$memail|$mdate|$mreplies|$stickyviews|$mlpname|$icon|$mstate\n";
                                                }
                                                else { print FILE2 "$threads[$a]"; }
                                        }
                                        unfile_lock(FILE2);
                                        close(FILE2);
                                }

                                print FILE "$subject|$mname[$x]|$memail[$x]|$mdate[$x]|$musername[$x]|$icon|$ENV{REMOTE_ADDR}|$message\n";
                        }
                }
                else { print FILE $messages[$x]; }
        }
        unfile_lock (FILE);
        close (FILE);

        print "Location: $pageurl/$cgi\?action=forum\&board=$currentboard\&op=displaysticky\&num=$input{'thread'}\n\n";
        exit;
}

################
sub movestickythread {
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

        if($username ne "$boardmoderator" && $access[32] ne "on") { error("$err{'011'}"); }

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        chomp(@categories = <FILE>);
        unfile_lock(FILE);
        close(FILE);

$boardlist="";
foreach $curcat (@categories) {
    open(CAT, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
    file_lock(CAT);
    chomp(@catinfo = <CAT>); # here we have the boards starting in line 3 going up to @catinfo
    unfile_lock(CAT);
    close(CAT);

    for ($i=2;$i<@catinfo ;$i++) {
                $thisboard = $catinfo[$i];
                    open(CURBOARD, "$boardsdir/$thisboard.dat") || error("$err{'001'} $boardsdir/$thisboard.dat");
                    file_lock(CURBOARD);
                                                                                chomp(@curboardinfo = <CURBOARD>);
                                                                                unfile_lock(CURBOARD);
                    close(CURBOARD);
                $curboardname=$curboardinfo[0];

            $boardlist=$boardlist.qq~<option value="$thisboard" >$curboardname</option>~;
    }
}

        $navbar = "$btn{'014'} $nav{'046'}";
        print_top();
        print qq~<form onSubmit="submitonce(this)" action="$forum$curboard&op=movestickythread2&thread=$info{'thread'}" method="post">
<b>$msg{'151'}</b> <select name="toboard">$boardlist</select>
<input type="submit" class="button" value="$btn{'041'}">
</form>
~;
        print_bottom();
        exit;

}

#################
sub movestickythread2 {
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

        if($username ne "$boardmoderator" && $access[32] ne "on") { error("$err{'011'}"); }

        open (FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$boardsdir/$currentboard.sticky") || error("$err{'016'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($mnum, $msub, $mname, $musername, $memail, $date, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/,$threads[$a]);
                $mstate =~ s~[\n\r]~~g;
                if ($mnum ne $info{'thread'}) { print FILE "$threads[$a]"; }
                else { $linetowrite = "$threads[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);

        open (FILE, "$boardsdir/$input{'toboard'}.sticky");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);
        open (FILE, ">>$boardsdir/$input{'toboard'}.sticky");
        close(FILE);

        open (FILE, ">$boardsdir/$input{'toboard'}.sticky");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $line (@threads) {
                print FILE "$line";
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$cgi\?action=forum\&board=$input{'toboard'}\&op=displaysticky\&num=$info{'thread'}\n\n";
        exit;
}

##################
sub removestickythread {
##################
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

        if($username ne "$boardmoderator" && $access[31] ne "on") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $msg{'462'}";
        print_top();
        print qq~$msg{'152'}<br>
<a href="$forum$curboard&op=removestickythread2&thread=$info{'thread'}">$nav{'047'}</a> - <a href="$cgi\?action=forum\&board=$currentboard\&op=displaysticky\&num=$info{'thread'}">$nav{'048'}</a>
~;
        print_bottom();
        exit;

}


###################
sub removestickythread2 {
###################
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

        if($username ne "$boardmoderator" && $access[31] ne "on") { error("$err{'011'}"); }

        open (FILE, "$messagedir/$info{'thread'}.txt") || error("$err{'001'} $messagedir/$info{'thread'}.txt");
        file_lock(FILE);
        @messages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        # if (@messages != 0) { error("$err{'025'}"); }

        open (FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$boardsdir/$currentboard.sticky") || error("$err{'016'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/,$threads[$a]);
                $mstate =~ s~[\n\r]~~g;
                if ($mnum ne $info{'thread'}) { print FILE "$threads[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

$date = "$mon-$mday-$year";

open (DATA, "$messagedir/delete.log");
@data = <DATA>;
close DATA;
open(DATA, ">$messagedir/delete.log");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$username|$info{'thread'}|$date|$currentboard\n";
close DATA;

        #unlink("$messagedir/$info{'thread'}.txt");
        #unlink("$messagedir/$info{'thread'}.mail");
        print "Location: $pageurl/$cgi\?action=forum\&board=$currentboard\n\n";
        exit;
}

################
sub lockstickythread {
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

        if($username ne "$boardmoderator" && $access[30] ne "on") { error("$err{'011'}"); }

        open (FILE, "$boardsdir/$currentboard.sticky") || error("$err{'001'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$boardsdir/$currentboard.sticky") || error("$err{'016'} $boardsdir/$currentboard.sticky");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $stickyviews, $mlpname, $micon, $mstate) = split(/\|/,$threads[$a]);
                $mstate =~ s~[\n\r]~~g;
                if ($mnum eq $info{'thread'}) {
                        if ($mstate == 1) { $mnewstate = 0; }
                        else { $mnewstate = 1; }
                        print FILE "$mnum|$msub|$mname|$musername|$memail|$date|$mreplies|$stickyviews|$mlpname|$micon|$mnewstate\n";
                }
                else { print FILE "$threads[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$cgi\?action=forum\&board=$currentboard\&op=displaysticky\&num=$info{'thread'}\n\n";
        exit;
}

###################
sub modifymessage {
###################
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

        open(FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        chomp(@threads = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        for ($x = 0; $x < @threads; $x++) {
($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$x]);
                if ($info{'thread'} eq $mnum && $mstate == 1) {
                        error("$err{'024'}");
                        $x = @threads;
                }
        }

        $viewnum = $info{'message'};
        $viewnum = int($viewnum);

        open (FILE, "$messagedir/$info{'thread'}.txt") || error("$err{'001'} $messagedir/$info{'thread'}.txt");
        file_lock(FILE);
        chomp(@messages = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        ($msubject, $mname, $memail, $mdate, $musername, $micon, $mip,  $mmessage) = split(/\|/, $messages[$viewnum]);
        $mmessage = htmltotext($mmessage);

        if($musername ne "$username" && $boardmoderator ne "$username" && $access[30] ne "on" || $username eq "$anonuser") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'003'} $btn{'014'} $nav{'035'}";
        print_top();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="1">
<tr>
<td><form onSubmit="submitonce(this)" action="$forum$curboard&op=modify2" method="post" name="creator">
<input type="hidden" name="viewnum" value="$viewnum">
<input type="hidden" name="thread" value="$info{'thread'}">
<table border="0">
<tr>
<td class="formstextnormal">$msg{'013'}</td>
<td>$mname</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'007'}</td>
<td>~;

if ($hidemail eq "1" || $hidemail eq "") { print qq~???~; }
if ($hidemail eq "0") { print qq~$memail~; }

print qq~</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'037'}</td>
<td><input type=text name="subject" value="$msubject" size="40" maxlength="50"></font></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'116'}</td>
<td><script language="javascript" type="text/javascript">
<!--
function showImage() {
document.images.icons.src="$imagesurl/forum/"+document.creator.icon.options[document.creator.icon.selectedIndex].value+".gif";
// -->
}
</script>
<select name="icon" onChange="showImage()">
<option value="$micon">$msg{'142'}</option>
<option value="xx">$msg{'143'}</option>
<option value="thumbup">$msg{'144'}</option>
<option value="thumbdown">$msg{'145'}</option>
<option value="exclamation">$msg{'146'}</option>
<option value="question">$msg{'147'}</option>
<option value="lamp">$msg{'148'}</option>
</select>
<img src="$imagesurl/forum/$micon.gif" name="icons" width="15" height="15" border="0" hspace="15"></td>
</tr>
<tr>
<td class="formstextnormal" valign="top">$msg{'038'}</td>
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
<textarea name="message" rows="10" cols="40">$mmessage</textarea></td>
</tr>
~;
if ($enable_ubbc eq "1") {print qq~
<tr>
<td class="formstextnormal">$msg{'156'}</td>
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
</tr>~; }

&smilieblock; #file_lock();

print qq~
</tr>
<tr>
<td align=center colspan="2"><input type="submit" class="button" name="moda" value="$btn{'015'}">&nbsp;<input type="submit" class="button" name="moda" value="$btn{'011'}"></td>
</tr>
</form>
</td>
</tr>~;
show_legend();
print qq~
</table>
~;

        print_bottom();
        exit;
}

####################
sub modifymessage2 {
####################
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

        if ($info{'d'} eq "1") {
                if($username ne "$boardmoderator" && $access[30] ne "on") { error("$err{'011'}"); }
                $input{'viewnum'} = "$info{'id'}";
                $input{'thread'} = $info{'thread'};
                $input{'moda'} = "$btn{'016'}";
        }

        open (FILE, "$messagedir/$input{'thread'}.txt") || error("$err{'001'} $messagedir/$input{'thread'}.txt");
        file_lock(FILE);
        @messages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        for ($a = 0; $a < @messages; $a++) {
                ($msub[$a], $mname[$a], $memail[$a], $mdate[$a], $musername[$a], $micon[$a], $mip[$a], $mmessage[$a]) = split(/\|/, $messages[$a]);
        }
        $count = $a;
        if ($input{'viewnum'} == 0 && $count > 1 && $input{'moda'} eq $btn{'016'}) { error("$err{'025'}"); }
        if ($a eq $input{'viewnum'}) {
                if ($musername[$a] ne "$username" && (!exists $moderators{$username}) && $access[30] ne "on" || $username eq "$anonuser") { error("$err{'011'}"); }
        }

        open (FILE, ">$messagedir/$input{'thread'}.txt") || error("$err{'001'} $messagedir/$input{'thread'}.txt");
        file_lock(FILE);
        for ($x = 0; $x < @messages; $x++) {
                if ($input{'viewnum'} eq $x) {
                        if ($input{'moda'} eq $btn{'016'}) {
                                open (FILE2, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.dat");
                                file_lock(FILE2);
                                @threads = <FILE2>;
                                unfile_lock(FILE2);
                                close (FILE2);

                                open (FILE2, ">$boardsdir/$currentboard.txt") || error("$err{'016'} $boardsdir/$currentboard.dat");
                                file_lock(FILE2);
                                for ($a = 0; $a < @threads; $a++) {
                                        if ($x == (@messages-1)) { $tdate = "$mdate[@messages-2]"; }
                                        if ($x == (@messages-1)) { $tlpname = "$mname[@messages-2]"; }
                                        else { $tdate = "$mdate[$x]"; }

                                        ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$a]);
                                        $mstate =~ s/[\n\r]//g;
                                        $mreplies--;

                                        if ($mnum == $input{'thread'}) {
                                                print FILE2 "$mnum|$msub|$mname|$musername|$memail|$tdate|$mreplies|$mviews|$tlpname|$micon|$mstate\n";
                                        }
                                        else { print FILE2 "$threads[$a]"; }
                                }
                                unfile_lock(FILE2);
                                close(FILE2);

                                if($musername[$x] ne "$anonuser") {

                                if (-e ("$memberdir/$musername[$x].dat")) {

                                        open(FILE2, "$memberdir/$musername[$x].dat") || error("$err{'010'}");
                                        file_lock(FILE2);
                                        chomp(@memsett = <FILE2>);
                                        unfile_lock(FILE2);
                                        close(FILE2);

                                        $memsett[6]--;
                                        open(FILE2, ">$memberdir/$musername[$x].dat") || error("$err{'016'} $memberdir/$musername[$x].dat");
                                        file_lock(FILE2);
                                        for ($i = 0; $i < @memsett; $i++) {
                                                print FILE2 "$memsett[$i]\n";
                                        }
                                        unfile_lock(FILE2);
                                        close(FILE2);
                                        }
                                }
                        }
                        else {
                                $name = htmlescape($input{'name'});
                                $email = htmlescape($input{'email'});
                                $subject = htmlescape($input{'subject'});
                                $message = htmlescape($input{'message'});
                                $icon = "$input{'icon'}";

                                if ($input{'viewnum'} == 0) {
                                        open (FILE2, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.dat");
                                        file_lock(FILE2);
                                        @threads = <FILE2>;
                                        unfile_lock(FILE2);
                                        close (FILE2);

                                        open (FILE2, ">$boardsdir/$currentboard.txt");
                                        file_lock(FILE2);
                                        for ($a = 0; $a < @threads; $a++) {
                                                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/, $threads[$a]);
                                                $mstate =~ s/[\n\r]//g;
                                                if ($mnum eq "$input{'thread'}") {
                                                        print FILE2 "$mnum|$subject|$mname|$musername|$memail|$mdate|$mreplies|$mviews|$mlpname|$icon|$mstate\n";
                                                }
                                                else { print FILE2 "$threads[$a]"; }
                                        }
                                        unfile_lock(FILE2);
                                        close(FILE2);
                                }

                                print FILE "$subject|$mname[$x]|$memail[$x]|$mdate[$x]|$musername[$x]|$icon|$ENV{REMOTE_ADDR}|$message\n";
                        }
                }
                else { print FILE $messages[$x]; }
        }
        unfile_lock (FILE);
        close (FILE);

        print "Location: $pageurl/$cgi\?action=forum\&board=$currentboard\&op=display\&num=$input{'thread'}\n\n";
        exit;
}

################
sub movethread {
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

        if($username ne "$boardmoderator" && $access[32] ne "on") { error("$err{'011'}"); }

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        chomp(@categories = <FILE>);
        unfile_lock(FILE);
        close(FILE);

$boardlist="";
foreach $curcat (@categories) {
    open(CAT, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
    file_lock(CAT);
    chomp(@catinfo = <CAT>); # here we have the boards starting in line 3 going up to @catinfo
    unfile_lock(CAT);
    close(CAT);

    for ($i=2;$i<@catinfo ;$i++) {
                $thisboard = $catinfo[$i];
                    open(CURBOARD, "$boardsdir/$thisboard.dat") || error("$err{'001'} $boardsdir/$thisboard.dat");
                    file_lock(CURBOARD);
                                                                                chomp(@curboardinfo = <CURBOARD>);
                                                                                unfile_lock(CURBOARD);
                    close(CURBOARD);
                $curboardname=$curboardinfo[0];

            $boardlist=$boardlist.qq~<option value="$thisboard" >$curboardname</option>~;
    }
}

        $navbar = "$btn{'014'} $nav{'046'}";
        print_top();
        print qq~<form onSubmit="submitonce(this)" action="$forum$curboard&op=movethread2&thread=$info{'thread'}" method="post">
<b>$msg{'151'}</b> <select name="toboard">$boardlist</select>
<input type="submit" class="button" value="$btn{'029'}">
</form>
~;
        print_bottom();
        exit;

}

#################
sub movethread2 {
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

        if($username ne "$boardmoderator" && $access[32] ne "on") { error("$err{'011'}"); }

        open (FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$boardsdir/$currentboard.txt") || error("$err{'016'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/,$threads[$a]);
                $mstate =~ s~[\n\r]~~g;
                if ($mnum ne $info{'thread'}) { print FILE "$threads[$a]"; }
                else { $linetowrite = "$threads[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);

        open (FILE, "$boardsdir/$input{'toboard'}.txt") || error("$err{'001'} $input{'toboard'}.txt");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$boardsdir/$input{'toboard'}.txt") || error("$err{'016'} $boardsdir/$input{'toboard'}.txt");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $line (@threads) {
                print FILE "$line";
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$cgi\?action=forum\&board=$input{'toboard'}\&op=display\&num=$info{'thread'}\n\n";
        exit;
}

##################
sub removethread {
##################

      if ($info{'thread'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

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

        if($username ne "$boardmoderator" && $access[31] ne "on") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $msg{'462'}";
        print_top();
        print qq~$msg{'152'}<br>
<a href="$forum$curboard&op=removethread2&thread=$info{'thread'}">$nav{'047'}</a> - <a href="$cgi\?action=forum\&board=$currentboard\&op=display\&num=$info{'thread'}">$nav{'048'}</a>
~;
        print_bottom();
        exit;

}

###################
sub removethread2 {
###################

      if ($info{'thread'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

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

        if($username ne "$boardmoderator" && $access[31] ne "on") { error("$err{'011'}"); }

        open (FILE, "$messagedir/$info{'thread'}.txt") || error("$err{'001'} $messagedir/$info{'thread'}.txt");
        file_lock(FILE);
        @messages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        #if (@messages != 0) { error("$err{'025'}"); }

        open (FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$boardsdir/$currentboard.txt") || error("$err{'016'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/,$threads[$a]);
                $mstate =~ s~[\n\r]~~g;
                if ($mnum ne $info{'thread'}) { print FILE "$threads[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

$date = "$mon-$mday-$year";

open (DATA, "$messagedir/delete.log");
@data = <DATA>;
close DATA;
open(DATA, ">$messagedir/delete.log");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$username|$info{'thread'}|$date|$currentboard\n";
close DATA;


        #unlink("$messagedir/$info{'thread'}.txt");
        #unlink("$messagedir/$info{'thread'}.mail");
        print "Location: $pageurl/$cgi\?action=forum\&board=$currentboard\n\n";
        exit;
}

################
sub lockthread {
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

        if($username ne "$boardmoderator" && $access[30] ne "on") { error("$err{'011'}"); }

        open (FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$boardsdir/$currentboard.txt") || error("$err{'016'} $boardsdir/$currentboard.txt");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($mnum, $msub, $mname, $musername, $memail, $mdate, $mreplies, $mviews, $mlpname, $micon, $mstate) = split(/\|/,$threads[$a]);
                $mstate =~ s~[\n\r]~~g;
                if ($mnum eq $info{'thread'}) {
                        if ($mstate == 1) { $mnewstate = 0; }
                        else { $mnewstate = 1; }
                        print FILE "$mnum|$msub|$mname|$musername|$memail|$date|$mreplies|$mviews|$mlpname|$micon|$mnewstate\n";
                }
                else { print FILE "$threads[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$cgi\?action=forum\&board=$currentboard\&op=display\&num=$info{'thread'}\n\n";
        exit;
}


if (-e "$scriptdir/user-lib/forum_admin.pl") {require "$scriptdir/user-lib/forum_admin.pl"}

1; # return true