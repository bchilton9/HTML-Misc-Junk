##############
sub postnews {
##############
        if ($access[1] ne "on") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'023'}";
        print_top();
        print qq~<form   action="$cgi?action=postnews2" method="post" name="creator">
<table border="0" cellspacing="1">
<tr>
<td class="formstextnormal">$msg{'013'}</td>
<td class="formstext">$realname</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'007'}</td>
<td class="formstext">$realemail</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'034'}</td>
<td><select name="cat">
~;
        open(FILE, "$topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        foreach $line (@cats) {
                @item = split(/\|/, $line);
                print qq~<option value="$item[1]">$item[0]</option>\n~;
        }
        print qq~</select></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'037'}</td>
<td><input type="text" name="subject" size="40" maxlength="50"></td>
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
function upload() {
window.open("$pageurl/$cgi?action=uploadpicture","","width=300,height=150,scrollbars")
}
// -->
</script>
<textarea name="message" rows="10" cols="40"></textarea></td>
</tr>
~;

if ($username eq "admin" || $topicimgupld eq "1" && $username ne "$anonuser") {
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
</td>
</tr>~;}

topicssmilieblock();

topicsshow_legend();

        if ($settings[7] eq "$root") { $approved = "1"; }
        else { $approved = "0"; }

        print qq~
<tr>
<td colspan="2"><input type="hidden" name="approved" value="$approved">
<input type="submit" class="button" name="moda" value="$btn{'044'}">&nbsp;<input type="submit" class="button" value="$btn{'008'}">&nbsp;&nbsp;<input type="reset" class="button" value="$btn{'009'}"></td>
</tr>
</table>
</form>
~;
        print_bottom();
        exit;
}

###############
sub postnews2 {
###############
        #if (($username eq $anonuser) || (($enable_userarticles == 0) && ($username ne "admin"))) { error("noguests"); }
         if ($access[1] ne "on") { error("noguests"); }

        error("$err{'014'}") unless ($input{'subject'});
        error("$err{'015'}") unless ($input{'message'});

      if ($input{'subject'} =~ /(\#)/) { print_top();  print "\# Signs Are Not Allowed in Subjects..."; print_bottom(); exit; }

        if ($enable_autopublish eq "") {$enable_autopublish = "0";}
        if ($enable_autopublish eq "0" && $username ne "admin") {$input{'approved'} = "0";}
        if ($username eq "admin") {$input{'approved'} = "1";}
        if ($username eq $article_imrecip) {$input{'approved'} = "1";}

if ($input{'moda'} eq "$btn{'044'}") {

# Put the preview code here....
#######################################################################################

                $navbar = "$btn{'014'} $nav{'004'} $btn{'014'} $nav{'155'}";
                print_top();

                $nmessage = previewstrip($input{'message'});
                $message = $input{'message'};

                        if ($enable_ubbc) { doubbctopic(); }
                        if ($enable_smile) { dosmilies(); }
                        $message = censor_it($message);

                        print qq~<form  action="$cgi?action=postnews2" method="post" name="creator">
<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
<td class="fullnewstitle">$input{'subject'}</td>
</tr>
<tr>
<td class="newstextsmall">$msg{'612'} $date $msg{'042'} $username
</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top"><img src="$imagesurl/topics/$input{'cat'}.gif" border="0" align="right" vspace="5" alt="$input{'cat'}"></a>
$message</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td align="left" valign="middle">
&nbsp;<img src="$imagesurl/print.gif" border="0" alt="$msg{'106'} - $subject" align="absmiddle">&nbsp;&nbsp;<img src="$imagesurl/friend.gif" border="0" alt="$msg{'055'}" align="absmiddle">
&nbsp;&nbsp;&nbsp;$readcount</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top" align="center">

<input type="hidden" name="subject" value="$input{'subject'}">
<input type="hidden" name="message" value="$nmessage">
<input type="hidden" name="cat" value="$input{'cat'}">

<INPUT type="button" class="button" value="$btn{'030'}" onClick="history.back()"><!-- edit -->
<input type="submit" class="button" value="$btn{'043'}"><!-- Post Message -->
<input type="submit" class="button" name="moda" value="$btn{'011'}"><!-- Delete --></td>
</tr>
</form>
</table>
~;

print_bottom();

exit;
}
#########################################################################################

elsif ($input{'moda'} eq "$btn{'011'}") {

        print "Location: $pageurl/$cgi\n\n";

}
else {

        opendir (DIR, "$topicsdir/articles");
        @files = readdir(DIR);
        closedir (DIR);
        @files = grep(/txt/,@files);
        @files = reverse(sort { $a <=> $b } @files);
        $postnum = @files[0];
        $postnum =~ s/.txt//;
        $postnum++;

        chomp($input{'message'});
        chomp($input{'subject'});

        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});

        if ($input{'approved'} eq "1") {
                open (FILE, "$topicsdir/$input{'cat'}.cat");
                file_lock(FILE);
                @articles = <FILE>;
                unfile_lock(FILE);
                close (FILE);

                open(FILE, ">$topicsdir/$input{'cat'}.cat");
                file_lock(FILE);
                print FILE "$postnum|$subject|$realname|$username|$realemail|$date|0\n";
                print FILE @articles;
                unfile_lock(FILE);
                close(FILE);

                open(FILE, ">$topicsdir/articles/$postnum.txt") || error("$err{'016'} $topicsdir/articles/$postnum.txt");
                file_lock(FILE);
                print FILE "$subject|$realname|$username|$realemail|$date|$message\n";
                unfile_lock(FILE);
                close(FILE);

                open(CNT, ">$topicsdir/articles/$postnum.cnt");
                file_lock(CNT);
                print CNT "0";
                unfile_lock(CNT);
                close(CNT);

                open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
                file_lock(FILE);
                chomp(@settings = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                $settings[11]++;

                open(FILE, ">$memberdir/$username.dat");
                file_lock(FILE);
                for ($i = 0; $i < @settings; $i++) {
                        print FILE "$settings[$i]\n";
                }
                unfile_lock(FILE);
                close(FILE);
        }
        else {

        if ($settings[7] eq "$root" && $input{'puddate'} ne "") {$pubdate = "$input{'puddate'}";
        } else {$pubdate = "check";}

                open (FILE, "$topicsdir/newarticles.dat");
                file_lock(FILE);
                @articles = <FILE>;
                unfile_lock(FILE);
                close (FILE);

($num, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy ) = split(/\|/, $articles[0]);
$num++;

open(FILE, ">$topicsdir/newarticles.dat");
file_lock(FILE);
print FILE "$postnum|$input{'cat'}|$subject|$realname|$username|$realemail|$date|$message\n";
print FILE @articles;
unfile_lock(FILE);
close(FILE);

if ($article_im eq "1") {
                                                                 $msgid = time;
                                                                $imsubj = "$msg{'463'} $subject";
                                                                $formatmsg = "$msg{'420'}$realname$msg{'464'}";

                                                                open (AFILE, "$memberdir/$article_imrecip.msg") || error("$err{'001'} $memberdir/$article_imrecip.msg");
                                                                file_lock(AFILE);
                                                                @imessages = <AFILE>;
                                                                unfile_lock(AFILE);
                                                                close (AFILE);

                                                                open (AFILE, ">$memberdir/$article_imrecip.msg") || error("$err{'001'} $memberdir/$article_imrecip.msg");
                                                                file_lock(AFILE);
                                                                print AFILE "$realname|$imsubj|$date|$formatmsg|$msgid\n";
                                                                foreach $curm (@imessages) { print AFILE "$curm"; }
                                                                unfile_lock(AFILE);
                                                                close(AFILE);
}

}
}
        xml();
        success();
}

##############
sub viewnews {
##############
        undef @catnames;
        undef @catlinks;

        @cats = chomp_database("$topicsdir/cats.dat");

        foreach (@cats) {
                @item = split(/\|/, $_);
                push(@catnames, $item[0]);
                push(@catlinks, $item[1]);
        }

        if ($info{'id'} eq "") {
                $navbar = " ";
                print_top();
                print $welcome;

newsheader();

                %data = ();

                foreach $curcat (@catlinks) {
                        if (-e("$topicsdir/$curcat.cat")) {
                                foreach (@cats) {
                                        @item = split(/\|/, $_);
                                        if ($curcat eq "$item[1]") { $curcatname = "$item[0]"; }
                                }

                                @articles = chomp_database("$topicsdir/$curcat.cat");

                                for ($a = 0; $a < @articles && $a <= $maxnews; $a++) {
                                        ($id, $subject, $nick, $poster, $email, $postdate, $comments) = split(/\|/, $articles[$a]);

                                        if ($comments == 1) { $commentscnt = "$comments $msg{'040'}"; }
                                        else { $commentscnt = "$comments $msg{'041'}"; }

                                        display_date($postdate); $postdatenew = $user_display_date;        $postdateold = $postdate;

                                        $text = chomp_datatext("$topicsdir/articles/$id.txt");

                                        read_count($id);

                                        @text = split(/\|/, $text);

                                        $message = $text[5];
                                        if ($enable_ubbc) { doubbctopic(); }
                                        if ($enable_smile) { dosmilies(); }
                                        $message = censor_it($message);
                                        $subject = censor_it($subject);

if ($info{'id'} eq "") {
                                        $postdate = $postdatenew; newstop(); $postdate = $postdateold;
}

                                        if (length($message) > 250) {
                                                $tmpmessage = substr($message, 0, 250);
                                                $tmpmessage =~ s/(.*)\s.*/$1/;
                                                newslong();
                                        }
                                        else {
                                                newsshort();
                                        }
                                        ($chkdate, $chktime) = split(/ - /, $postdate);
                                        ($chkmonth, $chkday, $chkyear) = split(/\//, $chkdate);
                                        ($chkhour, $chkmin, $chksec) = split (/:/, $chktime);
                                        $chkyear = (2000+$chkyear);

                                        $sortedentry = "$chkyear$chkmonth$chkday$chkhour$chkmin$chksec";
                                        $data{$sortedentry} = $post;

                                }
                        }
                }
                @num = sort {$b <=> $a } keys %data;
                $j = 0;
                while ($j < $maxnews) {
                        print "$data{$num[$j]}";
                        $j++;
                }
                print qq~
                </td>
                </tr>
                </table>~;
                print_poll();
                exit;
        }
        else {
                if ($info{'id'} !~ /^[0-9]+$/) { error("$err{'006'}" ); }

                foreach $curcat (@catlinks) {
                        if (-e("$topicsdir/$curcat.cat")) {

                                @articles = chomp_database("$topicsdir/$curcat.cat");

                                for ($a = 0; $a < @articles; $a++) {
                                        ($id, $dummy, $dummy, $dummy, $dummy, $dummy, $comments) = split(/\|/, $articles[$a]);
                                        if ($info{'id'} eq $id) {
                                                foreach (@cats) {
                                                        @item = split(/\|/, $_);
                                                        if ($curcat eq "$item[1]") { $curcatname = "$item[0]"; }
                                                        if ($curcat eq "$item[1]") { $curcatlink = "$item[1]"; }
                                                        $newsid = $info{'id'};
                                                }
                                                if ($comments == 1) { $commentscnt = "$comments $msg{'040'}"; }
                                                else { $commentscnt = "$comments $msg{'041'}"; }
                                        }
                                }
                        }
                }

                @datas = chomp_database("$topicsdir/articles/$info{'id'}.txt");

                $viewid = $info{'id'};

                view_count();

                read_count($viewid);

                $navbar = "$btn{'014'} $nav{'004'} $btn{'014'} $curcatname";
                print_top();

                foreach $line (@datas) { $numshown++; }

                for ($a = 0; $a < 1; $a++) {
                        @item = split (/\|/, $datas[$a]);

                        $message = $item[5];
                        if ($enable_ubbc) { doubbctopic(); }
                        if ($enable_smile) { dosmilies(); }
                        $message = censor_it($message);
                        $item[0] = censor_it($item[0]);

                        display_date($item[4]); $item[4] = $user_display_date;

                        print qq~<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
<td class="fullnewstitle">$item[0]</td>
</tr>
<tr>
<td class="newstextsmall">$msg{'612'} $item[4] $msg{'042'} ~;

# If the names left blank.. their an "anonymous coward" #

if ($item[1] eq "") { print qq~$msg{'183'}~; };

# If the names not blank.. and their a guest... post the name and email #

if ($item[2] eq "$anonuser") {
print qq~<a href="mailto:$item[3]" class="smallnewslink">$item[1]</a>~;
}

# If the names not blank, and their not a guest.. find out if I need to
# hide the email or not.... #

if ($item[2] ne "$anonuser") {

if ($hidemail eq "1" || $hidemail eq "") {
print qq~<a href="$cgi?action=anonemail&sendto=$item[2]" class="smallnewslink">$item[1]</a>~;
}

else {
print qq~
<a href="mailto:$item[3]" class="smallnewslink">$item[1]</a>~;
}
}

print qq~</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top" class="newstextnormal"><a href="$cgi?action=topics&viewcat=$curcatlink"><img src="$imagesurl/topics/$curcatlink.gif" border="0" align="right" vspace="5" alt="$curcatname"></a>
$message</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td align="left" valign="middle">
&nbsp;<a href="$cgi?action=printtopic&amp;id=$newsid&amp;curcatname=$curcatname&amp;img=$curcatlink" target="_blank"><img src="$imagesurl/print.gif" border="0" alt="$msg{'106'} - $subject" align="absmiddle"></a>&nbsp;&nbsp;<a href="$cgi?action=emailtopic&amp;id=$newsid&amp;curcatname=$curcatname"><img src="$imagesurl/friend.gif" border="0" alt="$msg{'055'}" align="absmiddle"></a>
&nbsp;&nbsp;&nbsp;$readcount</td>
</tr>
<tr>
<td class="newstextsmall" align="center">$msg{'613'} <a href="$cgi?action=otherarticles&amp;writer=$item[2]&amp;real=$item[1]&amp;not=$viewid" class="smallnewslink">$item[1]</a></td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top">~;
                }
                if ($numshown > 1) {print qq~

<table border="0" cellpadding="0" cellspacing="0" width="100%" class="newsbordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="newsbackcolor">
<tr>
<td valign="top" width="100%">

<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable"$background>
<tr>
<td>&nbsp;&nbsp;$msg{'158'}</td>
</tr>
<tr>
<td class="newstexttitle"><a name="topcomment"></a>&nbsp;

$item[0] | $commentscnt ~;

if ($username eq "$anonuser" && $enable_topicguestposting eq "0") { print qq~| <a href="$cgi?action=register" class="commentlink">$nav{'011'}</a> ~; }

if ($enable_topicguestposting eq "1" || $username ne "$anonuser") {        print qq~| <a href="\#comment" class="commentlink">$btn{'012'}</a>~; }

print qq~</td>
</tr>
</table>

<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td class="newssubtitle" align="center">$msg{'159'}~;
if ($enable_topicguestposting eq "0" && $username eq "$anonuser") {        print qq~<br>$msg{'488'}~; }
print qq~</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top">
~;
                        for ($a = 1; $a < @datas; $a++) {
                                @item = split (/\|/, $datas[$a]);

                                display_date($item[4]); $item[4] = $user_display_date;
                                $message = $item[5];
                                if ($enable_ubbc) { doubbctopic(); }
                                if ($enable_smile) { dosmilies(); }
                                $message = censor_it($message);
                                $item[0] = censor_it($item[0]);

                                if (@item == 0) { }

                                else {

                                print qq~
                                <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                <td class="commenttitleback">&nbsp;$item[0]</td>
                                </tr>
                                <tr>
                                <td class="commentsubtitleback">&nbsp;$msg{'054'} $item[4] $msg{'042'} ~;

                                if ($item[1] eq "" ) { print qq~$msg{'183'}~; }

                                        if ($item[1] ne "" && $item[2] eq "$anonuser") {
                                        print qq~<a href="mailto:$item[3]" class="smallnewslink">$item[1]</a>~;
                                        }

                                        if ($item[1] ne "" && $item[2] ne "$anonuser") {
                                                if ($hidemail eq "1" || $hidemail eq "") {
                                                print qq~<a href="$cgi?action=anonemail&sendto=$item[2]" class="smallnewslink">$item[1]</a>~;
                                                }
                                        else {
                                        print qq~<a href="mailto:$item[3]" class="smallnewslink">$item[1]</a>~;
                                        }
                                        }
                                print qq~

                                </td></tr>
                                <tr>
                                <td valign="top">$message</td>
                                </tr>
                                <tr>
                                <td>&nbsp;</td>
                                </tr>
                                ~;

                                }
                        }
                }
                else {
                        print qq~
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable"$background>
<tr>
<td>&nbsp;$msg{'158'}</td>
</tr>
</table>

<table border="0" cellpadding="0" cellspacing="2" width="100%" class="menutable"$background>
<tr>
<td class="newstexttitle"><a name="topcomment"></a>

$item[0] | $commentscnt ~;

if ($username eq "$anonuser" && $enable_topicguestposting eq "0") { print qq~| <a href="$cgi?action=register" class="commentlink">$nav{'011'}</a> ~; }

if ($enable_topicguestposting eq "1" || $username ne "$anonuser") {        print qq~| <a href="\#comment" class="commentlink">$btn{'012'}</a>~; }

print qq~</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="2" width="100%" class="commentbordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="commentbackcolor">
<tr>
<td valign="top" width="100%">
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td class="newssubtitle" align="center">$msg{'159'}~;
if ($enable_topicguestposting eq "0" && $username eq "$anonuser") {        print qq~<br>$msg{'488'}~; }
print qq~</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top">

$msg{'043'}
</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>~;
                }
if ($enable_topicguestposting eq "1" || $enable_topicguestposting eq "" ) {
                        print qq~<tr><td>

<table border="0" cellpadding="0" cellspacing="2" width="100%" class="menutable"$background>
<tr>
<td>&nbsp;$msg{'044'}</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="commentsbordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="commentsbackcolor">
<tr>
<td valign="top" width="100%">

<form  action="$cgi?action=commentnews" method="post">
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><a name="comment"></a>&nbsp;</td>
</tr>
~;
if ($username ne "$anonuser") { print qq~
<tr>
<td class="formstextnormal">$msg{'013'}</td><td class="formstext">$realname<input type="hidden" name="name" value="$realname"><input type="hidden" name="email" value="$realemail"></td>
</tr>
~;
}
if ($username eq "$anonuser") { print qq~
<tr>
<td class="formstextnormal">$msg{'013'}</td><td><input type="text" name="name" size="40" maxlength="20" value="$realname"></td>
</tr>
<tr><td></td><td>$msg{'180'}</td></tr>
<tr>
<td class="formstextnormal">$msg{'007'}</td><td><input type="text" name="email" size="40" maxlength="40" value="$realemail"></td>
</tr>
~;
}
print qq~
<tr>
<td class="formstextnormal">$msg{'037'}</td><td><input type="text" name="subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'038'}</td><td><textarea name="message" rows="10" cols="40"></textarea></td>
</tr>
<tr>
<td colspan="2"><input type="hidden" value="$info{'id'}" name="id">
<input type="hidden" value="$curcatlink" name="cat">
<input type="submit" class="button" value="$btn{'012'}"><input type="reset" class="button" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
</td>
</tr>
</table>

~;
                }

                else {

if ($username ne "$anonuser") {
        print qq~<table border="0" cellpadding="0" cellspacing="2" width="100%" class="menutable"$background>
<tr>
<td>&nbsp;$msg{'044'}</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="commentsbordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="commentsbackcolor">
<tr>
<td valign="top" width="100%">
<form  action="$cgi?action=commentnews" method="post">
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><a name="comment"></a>&nbsp;</td>
</tr>
<tr>
<td class="formstextnormal">$msg{'013'}</td><td class="formstext">$realname<input type="hidden" name="name" value="$realname"><input type="hidden" name="email" value="$realemail"></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'037'}</td><td><input type="text" name="subject" size="40" maxlength="50"></td>
</tr>
<tr>
<td class="formstextnormal">$msg{'038'}</td><td><textarea name="message" rows="10" cols="40"></textarea></td>
</tr>
<tr>
<td colspan="2"><input type="hidden" value="$info{'id'}" name="id">
<input type="hidden" value="$curcatlink" name="cat">
<input type="submit" class="button" value="$btn{'012'}"><input type="reset" class="button" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
</td>
</tr>
</table>

~;
                }
}
                print qq~
                </td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
                </td>
                </tr>
                </table>
                ~;
                print_bottom();
                exit;
        }
}

#################
sub commentnews {
#################
if ($enable_topicguestposting eq "1" || $enable_topicguestposting eq "" ) { }
        else {
                        if($username eq "$anonuser") { error("noguests"); }
                }
        error("$err{'014'}") unless ($input{'subject'});
        error("$err{'015'}") unless ($input{'message'});

        open(FILE, "$topicsdir/$input{'cat'}.cat") || error("$err{'001'} $topicsdir/$input{'cat'}.cat");
        file_lock(FILE);
        chomp(@datas = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $a = 0;
        while ($datas[$a] ne '') { $a++; }
        $count = $a;
        $i = 0;

        chomp($input{'message'});
        chomp($input{'subject'});

        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});

        open(FILE, ">$topicsdir/$input{'cat'}.cat") || error("$err{'016'} $topicsdir/$input{'cat'}.cat");
        file_lock(FILE);
        while ($i < $count) {
                ($id_temp, $subj, $nick, $poster, $email, $postdate, $comments) = split(/\|/, $datas[$i]);

                if ($id_temp eq $input{'id'}) {
                        $comments++;
                        print FILE "$id_temp|$subj|$nick|$poster|$email|$postdate|$comments\n";
                }
                else { print FILE "$id_temp|$subj|$nick|$poster|$email|$postdate|$comments\n"; }

                $i++;
        }
        unfile_lock(FILE);
        close(FILE);

# This code below will post according to a logged in user or not

        if ($username ne "$anonuser") {
        open(FILE, ">>$topicsdir/articles/$input{'id'}.txt") || error("$err{'016'} $topicsdir/articles/$input{'id'}.txt");
        file_lock(FILE);
        print FILE "$subject|$realname|$username|$realemail|$date|$message\n";
        unfile_lock(FILE);
        close(FILE);
        }

        if ($username eq "$anonuser") {
        open(FILE, ">>$topicsdir/articles/$input{'id'}.txt") || error("$err{'016'} $topicsdir/articles/$input{'id'}.txt");
        file_lock(FILE);
        print FILE "$subject|$input{'name'}|$username|$input{'email'}|$date|$message\n";
        unfile_lock(FILE);
        close(FILE);
        }

        if ($username ne "$anonuser") {
                open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
                file_lock(FILE);
                chomp(@settings = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                $settings[12]++;

                open(FILE, ">$memberdir/$username.dat");
                file_lock(FILE);
                for ($i = 0; $i < @settings; $i++) {
                        print FILE "$settings[$i]\n";
                }
                unfile_lock(FILE);
                close(FILE);
        }

# Send IM to Articles Author and Editor

                open(FILE, "$topicsdir/articles/$input{'id'}.txt") || error("$err{'016'} $topicsdir/articles/$input{'id'}.txt");
                file_lock(FILE);
                chomp($thecomments = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                @articledata = split(/\|/, $thecomments);
                $authorssubject = $articledata[0];
                $authorsusername = $articledata[2];

if ($username ne $authorsusername) { # No Need to IM as Author posting Comment
        $msgid = time;
        $imsubj = "$msg{'681'}";

if ($username ne "$anonuser") {
        $formatmsg = qq~$realname $msg{'682'} <a href="$scripturl/$cgi?action=viewnews&amp;id=$input{'id'}#topcomment">$authorssubject</a>.~;
}

if ($username eq "$anonuser") {
        $realname = $input{'name'};
        $formatmsg = qq~$realname $msg{'682'} <a href="$scripturl/$cgi?action=viewnews&amp;id=$input{'id'}#topcomment">$authorssubject</a>.~;
}

        open (AFILE, "$memberdir/$article_imrecip.msg") || error("$err{'001'} $memberdir/$article_imrecip.msg");
        file_lock(AFILE);
        @editormessages = <AFILE>;
        unfile_lock(AFILE);
        close (AFILE);

        open (AFILE, ">$memberdir/$article_imrecip.msg") || error("$err{'001'} $memberdir/$article_imrecip.msg");
        file_lock(AFILE);
        print AFILE "$realname|$imsubj|$date|$formatmsg|$msgid\n";
        foreach $curm (@editormessages) { print AFILE "$curm"; }
        unfile_lock(AFILE);
        close(AFILE);

        if ($authorsusername ne $article_imrecip) { # No need to send twice!
        open (BFILE, "$memberdir/$authorsusername.msg") || error("$err{'001'} $memberdir/$authorsusername.msg");
        file_lock(BFILE);
        @authormessages = <BFILE>;
        unfile_lock(BFILE);
        close (BFILE);

        open (BFILE, ">$memberdir/$authorsusername.msg") || error("$err{'001'} $memberdir/$authorsusername.msg");
        file_lock(BFILE);
        print BFILE "$realname|$imsubj|$date|$formatmsg|$msgid\n";
        foreach $curm (@authormessages) { print BFILE "$curm"; }
        unfile_lock(BFILE);
        close(BFILE);
        }
}

#######################################

        print "Location: $pageurl/$cgi?action=viewnews&id=$input{'id'}\n\n";
}

#############
sub success {
#############
        $navbar = "$btn{'014'} $nav{'004'} $btn{'014'} $nav{'023'} $nav{'027'}";
        print_top();
        print qq~<b>$nav{'027'}</b><br>
        $inf{'009'}
        ~;
        print_bottom();
        exit;
}

############
sub topics {
############
        open(FILE, "$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        if ($info{'viewcat'} eq "") {
                $navbar = "$btn{'014'} $nav{'004'}";
                print_top();
                print qq~<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
<td align="center" class="articlecattitle">$msg{'045'}</td>
</tr>
</table>
<br>
<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
~;
                for ($i = 0; $i < @cats; $i++) {
                        @item = split (/\|/, $cats[$i]);
                        open(FILE, "$topicsdir/$item[1].cat") || error("$err{'001'} $topicsdir/$item[1].cat");
                        file_lock(FILE);
                        chomp(@articles = <FILE>);
                        unfile_lock(FILE);
                        close(FILE);
                        $articlenumber = 0;
                        foreach $line (@articles) {
                              $line =~ s/[\n\r]//g;
                                                $articlenumber++;
                                                }
                        if ($articlenumber eq "0") {
                        print qq~<td align="center" class="articlecatnormal" valign="bottom"><img src="$imagesurl/topics/$item[1].gif" border="0" alt="$item[0]"><br>$item[0] ($articlenumber)</td>~;
                        } else {
                        print qq~<td align="center" class="articlecatnormal" valign="bottom"><a href="$cgi?action=topics&amp;viewcat=$item[1]"><img src="$imagesurl/topics/$item[1].gif" border="0" alt="$item[0]"></a><br>$item[0] ($articlenumber)</td>~;
                        }

                        $count++;
                        if ($count == 3) {
                                print "</tr>\n<tr>\n";
                                $count = 0;

                        }
                }

print qq~
</table>
<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">
<tr>
<td><hr></td>
</tr>
~;

#if ($enable_userarticles eq "1" && $username ne "$anonuser") {
#print qq~
#<tr>
#<td align="center"><a href="$pageurl/$cgi\?action=postnews" class="menu">$nav{'023'}</a></td>
#</tr>
#~;
#}

article_search();

print qq~
</table>
~;

                print_bottom();
                exit;
        }
        else {
                for ($i = 0; $i < @cats; $i++) {
                        @item = split (/\|/, $cats[$i]);
                        if ($info{'viewcat'} eq "$item[1]") { $curcatname = "$item[0]"; }
                }

                $navbar = "$btn{'014'} $nav{'004'} $btn{'014'} $curcatname";
                print_top();
                        print qq~<table align="center" border="0" cellpadding="3" cellspacing="0">
<tr>
<td align="center" class="articlecattitle">$msg{'046'} "$curcatname"</td>
</tr>
</table>
<br>
~;

                if (-e("$topicsdir/$info{'viewcat'}.cat")) {
                        open (FILE, "<$topicsdir/$info{'viewcat'}.cat");
                        file_lock(FILE);
                        chomp(@datas=<FILE>);
                        unfile_lock(FILE);
                        close(FILE);

                        print qq~<table border="0" cellpadding="1" cellspacing="0" width="100%">~;
                        if ($info{'start'} eq "") { $start = 0; }
                        else { $start = "$info{'start'}"; }

                        $numshown = 0;
                        for ($b = $start; $b < @datas; $b++) {
                                $numshown++;
                                @item = split(/\|/, $datas[$b]);
if ($numshown > $maxtopics) { $datas[$b] = @datas; }

if ($numshown <= $maxtopics) {


                                if ($item[6] == 1) { $commentscnt = "$item[6] $msg{'040'}"; }
                                elsif ($item[6] == -1) { $commentscnt = "0 $msg{'041'}"; }
                                else { $commentscnt = "$item[6] $msg{'041'}"; }

                                read_count($item[0]);

                                open (FILE, "$topicsdir/articles/$item[0].txt");
                                file_lock(FILE);
                                chomp($text = <FILE>);
                                unfile_lock(FILE);
                                close(FILE);

                                @text = split(/\|/, $text);

                                $message = htmltotext($text[5]);
                                $message = htmlescape($message);
                                $message = censor_it($message);
                                $item[1] = censor_it($item[1]);
                                undosmilies();
                                undoubbc();
                                display_date($item[5]); $item[5] = $user_display_date;

                                if (length($message) > 100) {
                                                $tmpmessage = substr($message, 0, 100);
                                                $tmpmessage =~ s/(.*)\s.*/$1/;
                                                $oneliner = "$tmpmessage...";
                                }
                                else {
                                $oneliner = $message;
                                }

                                print qq~<tr>
<td><img src="$imagesurl/search/topic.gif" border="0" alt="" valign="middle">&nbsp;<a href="$cgi?action=viewnews&amp;id=$item[0]">$item[1]</a></td>
</tr>
<tr>
<td>$oneliner</td>
</tr>
<tr>
<td>$msg{'047'} $item[2] $msg{'048'} $item[5]</td>
</tr>
<tr>
<td>$curcatname ($commentscnt)</td>
</tr>
<tr>
<td>$readcount.</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
~;
                        }
                        }
                        print qq~<tr><td>~;
                        if ($numshown >= $maxtopics) {
                                print qq~<hr noshade="noshade" size="1">
$msg{'039'}
~;
                                $numtopics = @datas;
                                $c = 0;
                                while (($c*$maxtopics) < $numtopics) {
                                        $viewc = $c+1;
                                        $strt = ($c*$maxtopics);
                                        if ($start == $strt) { print "[$viewc] "; }
                                        elsif ($strt == 0) { print qq~<a href="$cgi?action=topics&amp;viewcat=$info{'viewcat'}">$viewc</a> ~; }
                                        else { print qq~<a href="$cgi?action=topics&amp;viewcat=$info{'viewcat'}&amp;start=$strt">$viewc</a> ~; }
                                        $c++;
                                }
                        }

else {
                        if ($numshown < $maxtopics) {
                                print qq~<hr noshade="noshade" size="1">
$msg{'039'}
~;
                                $numtopics = @datas;
                                $c = 0;
                                while (($c*$maxtopics) < $numtopics) {
                                        $viewc = $c+1;
                                        $strt = ($c*$maxtopics);
                                        if ($start == $strt) { print "[$viewc] "; }
                                        elsif ($strt == 0) { print qq~<a href="$cgi?action=topics&amp;viewcat=$info{'viewcat'}">$viewc</a> ~; }
                                        else { print qq~<a href="$cgi?action=topics&amp;viewcat=$info{'viewcat'}&amp;start=$strt">$viewc</a> ~; }
                                        $c++;
                                }
                        }
}
print qq~</td></tr></table>~;
                }
                print_bottom();
                exit;
        }
}

################
sub printtopic {
################
            if ($info{'id'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

print "Content-type: text/html\n\n";
print qq~
<html>
<head>
<title>
$pagename
</title>
</head>
<body>~;

                open(FILE, "<$topicsdir/articles/$info{'id'}.txt") || error("$err{'001'} $topicsdir/articles/$info{'id'}.txt");
                file_lock(FILE);
                chomp(@datas = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                foreach $line (@datas) { $numshown++; }

                for ($a = 0; $a < 1; $a++) {
                        @item = split (/\|/, $datas[$a]);

                        $message = $item[5];
                        if ($enable_ubbc) { doubbctopic(); }
                        if ($enable_smile) { dosmilies(); }
                        $message = censor_it($message);
                        $item[0] = censor_it($item[0]);
                        display_date($item[4]); $item[4] = "$msg{'054'} $user_display_date";
                        if ($item[1] eq "") { $item[1] = "$msg{'183'}"; }
                }

                        print qq~
                        <table border="0" cellpadding="3" cellspacing="3" width="100%">
                        <tr>
                        <td><font face="arial" size="4" color="#003399"><img src="$imagesurl/search/topic.gif" alt="">&nbsp;<b>$item[0]</b></font></td>
                        </tr>
                        <tr>
                        <td><font face="arial" size="-3" color="#000000">$item[4] $msg{'042'} <b>$item[1]</b>
                        </td>
                        </tr>
                        <tr>
                        <td valign="top"><img src="$imagesurl/topics/$info{'img'}.gif" border="0" align="right" vspace="5" alt="$info{'curcatname'}">
                        <font face="arial" size="-1" color="#000000">$message</font></td>
                        </tr>~;

        if ($numshown > 1) {print qq~
                                 <tr>
                                 <td><hr align="left" width="200"><font face="arial" size="3" color="#003399"><b>$msg{'158'}</b></font></td>
                                 </tr>
                                 <tr>
                                 <td>&nbsp;</td>
                                 </tr>~;

                for ($a = 1; $a < $numshown; $a++) {
                        @item = split (/\|/, $datas[$a]);

                        $message = $item[5];
                        if ($enable_ubbc) { doubbctopic(); }
                        if ($enable_smile) { dosmilies(); }
                        $message = censor_it($message);
                                $item[0] = censor_it($item[0]);
                        display_date($item[4]); $item[4] = "$msg{'054'} $user_display_date";
                        if ($item[1] eq "") { $item[1] = "$msg{'183'}"; }

                        if ($item[5] ne "") { print qq~
                        <tr>
                        <td><font face="arial" size="2" color="#003399"><img src="$imagesurl/search/comments.gif" alt="">&nbsp;<b>$item[0]</b></font></td>
                        </tr>
                        <tr>
                        <td><font face="arial" size="-3" color="#000000">$item[4] $msg{'042'} <b>$item[1]</b>
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
                        <td><hr><center><small>$msg{'465'} <b>$pagename</b><br>$msg{'159'}<br></small></center></td>
                        </tr>
                        </table>
                        </body>
                        </html>~;


exit;

}


################
sub emailtopic {
################
            if ($info{'id'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

                if ($username eq "$anonuser") { error("noguests"); }

                open(FILE, "<$topicsdir/articles/$info{'id'}.txt") || error("$err{'001'} $topicsdir/articles/$info{'id'}.txt");
                file_lock(FILE);
                chomp(@datas = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                foreach $line (@datas) { $numshown++; }

                for ($a = 0; $a < 1; $a++) {
                        @item = split (/\|/, $datas[$a]);

                        }

                $title = $item[0];

        $navbar = "$btn{'014'} $mnu{'041'} $btn{'014'} $info{'curcatname'}: $title";
        print_top();
        print qq~<br>
        <form  action="$cgi?action=emailtopic2&amp;sendto=$sendto&amp;from=$from&amp;id=$info{'id'}&amp;curcatname=$info{'curcatname'}" method="post">
        <table border="0" width="100%" cellpading="0" cellspacing="0">
        <tr>
        <td colspan="2" class="formstextnormal" align="center">$msg{'489'}</td>
        </tr>
        <tr>
        <td colspan="2">&nbsp;</td>
        </tr>
        <tr>
        <td width="20%" class="formstextnormal" nowrap>$msg{'182'}</td>
        <td width="80%"><input type="text" name="name" value="$realname" size="40"></td>
        </tr>
        <tr>
        <td width="20%" class="formstextnormal" nowrap>From E-Mail:</td>
        <td width="80%"><input type="text" name="from" value="$realemail" size="40"></td>
        </tr>
  <tr>
        <td width="20%" class="formstextnormal" nowrap>$msg{'181'}</td>
        <td width="80%"><input type="text" name="sendto" size="40"></td>
        </tr>
        <tr>
        <td colspan="2">&nbsp;</td>
        </tr>
        <tr>
        <td colspan="2" align="center"><input type="submit" class="button" name="sendarticle" value="$btn{'045'}">&nbsp;<input type="submit" class="button" name="sendarticle" value="$btn{'046'}">&nbsp;<input type="reset" class="button" value="$btn{'009'}"></td>
        </tr>
        </table>
        </form>
~;
        print_bottom();
        exit;

}

#################
sub emailtopic2 {
#################
      if ($info{'id'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        if ($username eq "$anonuser")  { error("noguests"); }
        error("$err{'005'}") unless ($input{'sendto'});
        error("$err{'014'}") unless ($input{'from'});

                open(FILE, "<$topicsdir/articles/$info{'id'}.txt") || error("$err{'001'} $topicsdir/articles/$info{'id'}.txt");
                file_lock(FILE);
                chomp(@datas = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                foreach $line (@datas) { $numshown++; }

                for ($a = 0; $a < 1; $a++) {
                        @item = split (/\|/, $datas[$a]);
                        }
                        $message = $item[5];
                        $message = censor_it($message);
                                $item[0] = censor_it($item[0]);
                        doubbc();
                        $message = htmltotext($message);
                        $message = convert_newsletter($message);

        $head = "$input{'name'} $msg{'584'} $pagename\n\n";
        $foot = "\n\n$msg{'465'} $pagename\n$msg{'466'}$input{'name'}";
        $title = ": $item[0]";

if ($input{'sendarticle'} eq "$btn{'045'}") {
        $mailmessage = "$head$message.$foot";
}

if ($input{'sendarticle'} eq "$btn{'046'}") {
        $mailmessage = "$head$pageurl/$cgi?action=viewnews&id=$info{'id'}.$foot";
}

        $mailsubject = $info{'curcatname'}.$title;
        $mailto = $input{'sendto'};
        $mailfrom = $input{'from'};

sendemail($mailto, $mailsubject, $mailmessage, $mailfrom);

print "Location: $pageurl/$cgi?action=viewnews&id=$info{'id'}\n\n";

exit;
}

####################
sub topicssmilieblock {
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
sub topicsshow_legend {
####################

                if ($enable_ubbc eq "1") {

                         if ($username ne "$anonuser") {

                                         open(FILE, "$memberdir/$username.pref") || error("$err{'010'}");
                                        file_lock(FILE);
                                        chomp(@preferences = <FILE>);
                                        unfile_lock(FILE);
                                        close(FILE);

                                                                                        if ($preferences[7] == 1 || $preferences[7] eq "" ) {topicslegend();
                                                                                        }
                                } else {topicslegend();}
                }

}

#####################
sub topicslegend {
#####################

print qq~
<tr>
<td>&nbsp;</td><td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td><td align="center" valign="top">
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
</tr>
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

##################
sub view_count {
##################

                open(CNT, "<$topicsdir/articles/$viewid.cnt");
                file_lock(CNT);
                $viewscount = <CNT>;
                unfile_lock(CNT);
                close(CNT);

                $viewscount++;

                open(CNT, ">$topicsdir/articles/$viewid.cnt");
                file_lock(CNT);
                print CNT "$viewscount";
                unfile_lock(CNT);
                close(CNT);

}

####################
sub read_count {
####################

my ($counter) = @_;

                                        $readcount = "";
                                        $viewscount = "0";

                                        open(CNT, "$topicsdir/articles/$counter.cnt");
                                        file_lock(CNT);
                                        $viewscount = <CNT>;
                                        unfile_lock(CNT);
                                        close(CNT);

                                        if ($viewscount eq "") {$readcount = qq~<img src="$imagesurl/forum/new.gif" alt="">~;}
                                        if ($viewscount eq "0") {$readcount = qq~<img src="$imagesurl/forum/new.gif" alt="">~;}
                                        if ($viewscount eq "1") {$readcount = "($viewscount $nav{'152'})";}
                                        if ($viewscount eq "2") {$readcount = "($viewscount $nav{'151'})";}
                                        if ($viewscount > "2") {$readcount = "($viewscount $nav{'151'})";}

}

########################
sub article_search {
########################

print qq~
<tr>
<td>
<form  method="POST" action="$pageurl/$cgi\?action=search">
<input type="hidden" name="action" value="search">
<b>$nav{'039'} $nav{'004'}:</b>&nbsp;&nbsp;<input type="text" name="pattern" size="16" class="text">&nbsp;<input type="submit" class="button" value="$btn{'001'}">
<input type="hidden" name="articleson" value="on">
<input type="hidden" name="forumson" value="off">
<input type="hidden" name="linkson" value="off">
<input type="hidden" name="downloadson" value="off">
</form>
</td>
</tr>
~;
}

########################
sub other_articles {
########################

        if ($info{'page'} eq "") { $pagenum = 1; }  else { $pagenum = $info{'page'}; }
        $numresults = 20;  # Change this # here to specify number of results per page.
        $casesensitive = 1;
        $matchednum = 0;
        @matches = "";
        $pattern = $info{'writer'};
        $ignore = $info{'not'};
        $writername = $info{'real'};

        other_articles2();

        @matches = reverse sort { $b->[1] <=> $a->[1] } @matches;

        if ($ignore ne "") {$othernum = $matchednum-1; $othertext ="$msg{'614'}";} else {$othernum = $matchednum; $othertext ="$msg{'615'}";}
        if ($othernum < 1) {$othernum = 0;}

        $navbar = "$btn{'014'} $othertext $msg{'042'} $writername";
        print_top();
        print qq~
        <table cellspacing="1" cellpadding="3" border="0" width="100%">
        <tr>
<td>$writername $msg{'616'} $othernum $othertext.<br>$msg{'404'} $pagenum</td>
</tr>
<tr><td>&nbsp;</td></tr>
~;

for ($i = ($pagenum * $numresults) - ($numresults)  ; $i <= ($pagenum * $numresults); $i++) {
        if ($matches[$i] ne ""){
                ($type, $curfle) = split (/\|/, $matches[$i]);
                if ($type eq "article") {
                        ( $type, $curfile, $line, $maintitle, $title, $realname, $ausername, $email, $otherdate ) = split ( /\|/ , $matches[$i] );
                        ($id, $dummy) = split ( /\./ , $curfile );

                        open(FILE, "<$topicsdir/articles/$id.txt") || error("$err{'001'} $topicsdir/articles/$id.txt");
                        file_lock(FILE);
                        chomp($text = <FILE>);
                        unfile_lock(FILE);
                        close(FILE);

                                @text = split(/\|/, $text);

                                $message = htmltotext($text[5]);
                                $message = htmlescape($message);
                                undosmilies();
                                undoubbc();
                                $message = censor_it($message);
                                $title = censor_it($title);
                                display_date($otherdate); $otherdate = $user_display_date;

                                if (length($message) > 100) {
                                                $tmpmessage = substr($message, 0, 100);
                                                $tmpmessage =~ s/(.*)\s.*/$1/;
                                                $oneliner = "$tmpmessage...";
                                }
                                else {
                                $oneliner = $message;
                                }

                        if ($id ne $ignore) {print qq~<tr><td><img src="$imagesurl/search/topic.gif" alt="$nav{'004'}">&nbsp;<a href="$scripturl/$cgi?action=viewnews&amp;id=$id">$title</a><br>$oneliner<br>$msg{'110'} $otherdate</td></tr>~; }
                }
        }
}

print qq~<tr><td>&nbsp;</td></tr><tr><td><a href="#top">$msg{'406'}</a></td></tr><tr><td>~;

$numofpages = $matchednum / $numresults;
if ($numofpages > int ($numofpages)) { $numofpages = int ($numofpages) +1; } else { $numofpages = int ($numofpages); }
if ($numofpages > 1) {
        print qq~<b>$msg{'039'}</b>&nbsp;~;
        for ( $i = 1 ; $i <= $numofpages ; $i++) {
                if ( $i == $pagenum ) { print qq~[$i]&nbsp;~ ; }
                else { print qq~<a href="$scripturl/$cgi?action=otherarticles&amp;writer=$pattern&amp;real=$writername&amp;not=$ignore&amp;page=$i">$i</a>&nbsp~; }
        }
}

print qq~</td></tr></table>~;

print_bottom();

exit;

}

########################
sub other_articles2 {
########################

        opendir (DIR, "$topicsdir/articles");
        @files = readdir(DIR);
        closedir (DIR);

        @files = grep (/\.txt/, @files);
        foreach $curfile (@files) {

                open (FILE, "$topicsdir/articles/$curfile");
                @articles = <FILE>;
                close (FILE);

                $line = 0;
                foreach $curarticle (@articles) {
                        $line++;
                        ($title, $realname, $ausername, $email, $date, $body) = split ( /\|/, $curarticle);
                        $maintitle = $title;
                        if ($casesensitive == 0) {
                                if ($realname =~ $pattern || $ausername =~ $pattern ) {
                                        if ($line == 1) {$type = "article"; $matchednum++;} else {$type = "comment";}
                                        $curarticle = join '|', $type, $curfile, $line, $maintitle, $title, $realname, $ausername, $email, $date ;
                                        push @matches, $curarticle;
                                }
                        }
                        else {
                                if ( lc($realname) =~ lc($pattern) || lc($ausername) =~ lc($pattern) ) {
                                        if ($line == 1) { $type = "article"; $matchednum++;} else {$type = "comment";};
                                        $curarticle = join '|', $type, $curfile, $line, $maintitle, $title, $realname, $ausername, $email, $date ;
                                        push @matches, $curarticle;
                                }
                        }
                }
        }
}

if (-e "$scriptdir/user-lib/topics.pl") {require "$scriptdir/user-lib/topics.pl"}

1; # return true