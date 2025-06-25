###############################################################################

################
sub loadcookie {
################
        if ($input{'rememberme'}) {
        $cookie_expdate = "Thu, 01-Jan-2099 00:00:00 GMT";
        }
        else {
        $cookie_expdate = "$days[$wday], $mday-$mon_num-$saveyear $hour\:$min\:$sec+10";
        }
        foreach (split(/; /,$ENV{'HTTP_COOKIE'})) {
                ($cookie, $value) = split(/=/);
                if ($cookie eq $cookieusername) { $username = $value; }
                if ($cookie eq $cookiepassword) { $password = $value; }
                if ($cookie eq $cookieusertheme) { $usertheme = $value; }
                if ($cookie eq $cookieuserlang) { $userlang = $value; }
        }
}

##############
sub loaduser {
##############
        if ($username eq "") {
                $username = $anonuser;
                $usertheme = "$defaulttheme";
                $userlang = $language;

        }
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
                        $usertheme = $settings[13];
                        $userlang = $settings[15];
                        $user_check_date = $settings[25];
                        $user_check_time = $settings[26];
                        $writedate = $date;
                        writelog("Last_Visited");

                open(FILE, "$memberdir/$username.acc");
                file_lock(FILE);
                @access = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                for( $i = 0; $i < @access; $i++ ) {
                        $access[$i] =~ s~[\n\r]~~g;
                }


                        }
        }
        unless ($username) {
                print qq~Set-Cookie: $cookieusername=; path=/; expires=$cookie_expdate;\n~;
                print qq~Set-Cookie: $cookiepassword=; path=/; expires=$cookie_expdate;\n~;
                print qq~Set-Cookie: $cookieusertheme=; path=/; expires=$cookie_expdate;\n~;
                print qq~Set-Cookie: $cookieuserlang=; path=/; expires=$cookie_expdate;\n~;

                $username = $anonuser;
                $password = "";
                $usertheme = $defaulttheme;
                $userlang = $language;
                @settings = ();
                $realname = "";
                $realemail = "";
                $ENV{'HTTP_COOKIE'} = "";
                $user_check_date = $check_date;
                $user_check_time = $timezone;

        }
if ($usertheme eq "") {$usertheme = "$defaulttheme";}
if ($userlang eq "") { $userlang = $language; }
getlanguage();

}

#################
sub logvisitors {
#################
        open(LOG, "$datadir/log.dat");
        file_lock(LOG);
        chomp(@entries = <LOG>);
        unfile_lock(LOG);
        close(LOG);

        open(LOG, ">$datadir/log.dat");
        file_lock(LOG);
        $field = $username;
        if ($field eq $anonuser) { $field = "$ENV{'REMOTE_ADDR'}"; }
        print LOG "$field|$date\n";
        foreach $curentry (@entries) {
                ($name, $value) = split(/\|/, $curentry);
                $date1 = "$value";
                $date2 = "$date";
                calctime();
                if ($name ne $field && $result <= 15 && $result >= 0) { print LOG "$curentry\n"; }
        }
        unfile_lock(LOG);
        close(LOG);

        #DAYLY LOG

        open(LOG, "$datadir/logs/$visitdate.dat");
        file_lock(LOG);
        chomp(@entries = <LOG>);
        unfile_lock(LOG);
        close(LOG);

        open(LOG, ">$datadir/logs/$visitdate.dat");
        file_lock(LOG);
        $field = $username;
        $myCount = 1;
        if ($field eq $anonuser) { $field = "Guest ($ENV{'REMOTE_ADDR'})"; }

        foreach $curentry (@entries) {
                ($name, $addr, $value, $pages) = split(/\|/, $curentry);
                $date1 = "$value";
                $date2 = "$date";
                if ($name ne $field) {
                print LOG "$curentry\n";
                 } else {
                 $myCount = $myCount + $pages;
                 }
        }

        print LOG "$field|$ENV{'REMOTE_ADDR'}|$date|$myCount\n";

        unfile_lock(LOG);
        close(LOG);



}

################
sub print_main {
################
                if ($username ne "$anonuser") {

                open(FILE, "$memberdir/$username.pref") || error("$err{'010'}");
                file_lock(FILE);
                chomp(@preferences = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                if ($preferences[3] == 1 || $preferences[3] eq "" ) {

        open(FILE, "$datadir/welcomemsg.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $message = $lines[1];

        if ($enable_ubbc) { doubbctopic(); }
        if ($enable_smile) { dosmilies(); }
        $welcometitle = showhtml("$lines[0]");
        $welcomebody = showhtml("$message");

        $welcome = qq~<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><p class="texttitle">$welcometitle</p>
$welcomebody<br>
<br><br></td>
</tr>
</table>
~;
        }
        }

if ($username eq "$anonuser") {
open(FILE, "$datadir/welcomemsg.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $welcometitle = showhtml("$lines[0]");
        $welcomebody = showhtml("$lines[1]");


        $welcome = qq~<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><p class="texttitle">$welcometitle</p>
$welcomebody<br>
<br><br></td>
</tr>
</table>
~;
}

        require "$sourcedir/topics.pl";
        viewnews();

        exit;
}


###############
sub print_top {
###############
        require "$scriptdir/config.pl";
        require "$sourcedir/plugins.pl";
        require "$themesdir/standard/theme.pl"; getvars();
        require "$themesdir/standard/header.pl";
}

##################
sub print_bottom {
##################
        require "$scriptdir/config.pl";
        require "$sourcedir/plugins.pl";
        require "$themesdir/standard/footer.pl";
}

##################
sub print_poll {
##################
        require "$scriptdir/config.pl";
        require "$sourcedir/plugins.pl";
        require "$themesdir/standard/pollfooter.pl";
}

######################
sub latestforumposts {
######################
      open(FILE, "<$boardsdir/cats.txt");
                        @fcats = <FILE>;
                        close(FILE);

                        %myforumdata= ();

                        foreach $fcat (@fcats) {
                              $fcat =~ s/[\n\r]//g;

                                                open(FILE, "<$boardsdir/$fcat.cat");
                                                @fcatinfo = <FILE>;
                                                close(FILE);

                                                $fcatinfo[1] =~ s/[\n\r]//g;
                                                foreach $selboard (@fcatinfo) {

                        if ($selboard ne $fcatinfo[0] && $selboard ne $fcatinfo[1]) {
                                                $selboard =~ s/[\n\r]//g;

                                                if ($fcatinfo[1] ne "") {
                                                if ($settings[7] ne "$root" && $settings[7] ne "$fcatinfo[1]") {      next; }
                                                }

                                                 open(FILE, "<$boardsdir/$selboard.txt");                                                                         @fposts = <FILE>;
                                                 close(FILE);

for ($f = 0; $f < @fposts; $f++) {
                                                                                                                                                  ($fpnum, $fptitle, $dummy, $dummy, $dummy, $fpdate, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $fposts[$f]);
                                                                                                                                                chomp($dummy);
                                                                                                                                                $lfptitle = censor_it($fptitle);
                                                                                                                                                $myforumlink = qq~<a href="$scripturl/$cgi?action=forum&amp;board=$selboard&amp;op=display&amp;num=$fpnum" class="mycontentlink">$lfptitle</a>~;


                                        ($chkdate, $chktime) = split(/ - /, $fpdate);
                                        ($chkmonth, $chkday, $chkyear) = split(/\//, $chkdate);
                                        ($chkhour, $chkmin, $chksec) = split (/:/, $chktime);
                                        $chkyear = (2000+$chkyear);

                                        $sortedentry = "$chkyear$chkmonth$chkday$chkhour$chkmin$chksec";
                                                                                                                 $myforumdata{$sortedentry} = $myforumlink;
                                                                                                                 }
                                                                                  }
                                                        }
       }
                         @myforumnum = sort { $b <=> $a } keys %myforumdata;
}

##############
sub menuitem {
##############
        require "$themesdir/$usertheme/theme.pl"; menuitem();
}

###############
sub boxheader {
###############
        require "$themesdir/$usertheme/theme.pl"; boxheader();
}

###############
sub boxfooter {
###############
        require "$themesdir/$usertheme/theme.pl"; boxfooter();
}

################
sub userstatus {
################
     $guests = 0;
     $users = 0;

     open(LOG, "$datadir/log.dat");
     file_lock(LOG);
     chomp(@entries = <LOG>);
     unfile_lock(LOG);
     close(LOG);

     foreach $curentry (@entries) {
           ($name, $value) = split(/\|/, $curentry);
           if($name =~ /\./) { ++$guests }
           else { ++$users      }
     }
     if ($username ne "$anonuser") {

           open(MEM, "$memberdir/$username.dat");
           file_lock(MEM);
           chomp(@sett = <MEM>);
           unfile_lock(MEM);
           close(MEM);

           if ($username ne "$anonuser") {
                 open(IM, "$memberdir/$username.msg");
                 file_lock(IM);
                 @immessages = <IM>;
                 unfile_lock(IM);
                 close(IM);

                 $mnum = @immessages;
                 $messnum = "$mnum";
           }
           print qq~<tr>
<td class="whocat">$msg{'002'} '$sett[1]'</td>
</tr>
<tr>
<td class="whocat">$msg{'342'}<a href="$pageurl/$cgi?action=im" class="whomenu">$mnum</a>$msg{'343'}</td>
</tr>
~;

if ($mnum >= 0) {


                open(FILE, "$memberdir/$username.pref") || error("$err{'010'}");
                file_lock(FILE);
                chomp(@preferences = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                if ($preferences[0] == 1 || $preferences[0] eq "" ) {
                require "$sourcedir/subs.pl";
                if ($preferences[6] < $mnum) { require "$sourcedir/subs.pl"; imalert(); }

if ($username ne "admin") {

open(FILE, ">$memberdir/$username.pref") || error("$err{'010'}");
file_lock(FILE);
print FILE "$preferences[0]\n";
print FILE "$preferences[1]\n";
print FILE "$preferences[2]\n";
print FILE "$preferences[3]\n";
print FILE "\n";
print FILE "\n";
print FILE "$mnum\n";
print FILE "$preferences[7]\n";
unfile_lock(FILE);
close(FILE);
}

if ($username eq "admin") {

open(FILE, ">$memberdir/$username.pref") || error("$err{'010'}");
file_lock(FILE);
print FILE "$preferences[0]\n";
print FILE "$preferences[1]\n";
print FILE "$preferences[2]\n";
print FILE "$preferences[3]\n";
print FILE "$preferences[4]\n";
print FILE "$preferences[5]\n";
print FILE "$mnum\n";
print FILE "$preferences[7]\n";
unfile_lock(FILE);
close(FILE);

}                 }
           }

     }

     open(CNT, "$memberdir/mostonline.cnt");
     file_lock(CNT);
     $oldcount = <CNT>;
     unfile_lock(CNT);
     close(CNT);

     $newcount = $guests + $users;

     if ($newcount > $oldcount) {
     open(CNT, ">$memberdir/mostonline.cnt");
     file_lock(CNT);
     print CNT "$newcount";
     unfile_lock(CNT);
     close(CNT);
     $mostonline = $newcount;
     } else {
     $mostonline = $oldcount; }

     print qq~<tr>
<td class="whocat">$msg{'344'}$guests$msg{'346'}
~;

if ($username eq "$anonuser") { print qq~
$users$msg{'347'}</td></tr>~;

if ($dispmost eq "1") {print qq~
     <tr>
     <td class="whocat">$msg{'345'}$mostonline.</td>
     </tr>~; }
}

if ($username ne "$anonuser") { print qq~
<a href="$pageurl/$cgi?action=who" class="whomenu"><u>$users</u></a>$msg{'347'}</td>
</tr>~;

if ($dispmost eq "1") {print qq~
     <tr>
     <td class="whocat">$msg{'345'}$mostonline.</td>
     </tr>~; }
}
}

#############
sub readlog {
#############
        local ($field, $readuser) = @_;
        if ($readuser eq "") {$readuser = $username;}
        if($readuser ne "$anonuser") {
                open(LOG, "$memberdir/$readuser.log");
                file_lock(LOG);
                @entries = <LOG>;
                unfile_lock(LOG);
                close(LOG);

                foreach $curentry (@entries) {
                        $curentry =~ s/[\n\r]//g;
                        ($name, $value) = split(/\|/, $curentry);
                        if ($name eq "$field") { return "$value"; }
                }
        }
}

##############
sub writelog {
##############
        local($field) = @_;
        if ($username ne "$anonuser") {
                open(LOG, "<$memberdir/$username.log");
                file_lock(LOG);
                @entries = <LOG>;
                unfile_lock(LOG);
                close(LOG);

                open(LOG, ">$memberdir/$username.log");
                file_lock(LOG);
                print LOG "$field|$writedate\n";
                foreach $curentry (@entries) {
                        $curentry =~ s/[\n\r]//g;
                        ($name, $value) = split(/\|/, $curentry);
                        $date1 = "$value";
                        $date2 = "$date";
                        calcdifference();
                        if ($name ne "$field" && $result <= $max_log_days_old) { print LOG "$curentry\n"; }
                }
                unfile_lock(LOG);
                close(LOG);
        }
}

############
sub logips {
############
        @skip = ('127.0.0.1');
        $ip_time = 5;
        $check = 0;

        if (@skip) {
                foreach $ips (@skip) {
                        if ($ENV{'REMOTE_ADDR'} =~ /$ips/) {
                                $check = 1;
                                last;
                        }
                }
        }
        if ($check == 0) {
                my $this_time = time();

                open(FILE,"$logdir/ip.log");
                file_lock(FILE);
                my @lines = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                open(FILE,">$logdir/ip.log");
                file_lock(FILE);
                foreach $visitor (@lines) {
                        ($ip_addr,$time_stamp) = split(/\|/, $visitor);
                        if ($this_time < $time_stamp + (60*$ip_time)) {
                                if ($ip_addr eq $ENV{'REMOTE_ADDR'}) { $check = 1; }
                                else { print FILE "$ip_addr|$time_stamp"; }
                        }
                }
                print FILE "$ENV{'REMOTE_ADDR'}|$this_time\n";
                unfile_lock(FILE);
                close(FILE);
        }

        if ($check == 0) {
                if ($ENV{'REMOTE_HOST'}) { $host = $ENV{'REMOTE_HOST'}; }
                else {
                        $ip_address = $ENV{'REMOTE_ADDR'};
                        @numbers = split(/\./, $ip_address);
                        $ip_number = pack("C4", @numbers);
                        $host = (gethostbyaddr($ip_number, 2))[0];
                }
                if ($host eq "") { $host = "$ENV{'REMOTE_ADDR'}"; }

                ($value, $referer) = split(/=/, $query);
                if ($referer) {
                        if ($referer =~ /(http:\/\/.*\.[a-z]{2,4}\/)/i) { $referer = $1; }
                }
                else { $referer = "-"; }

                open(DATA, ">>$logdir/stats.dat");
                file_lock(DATA);
                print DATA ("$logdate - $host - \"$ENV{'HTTP_USER_AGENT'}\" - \"$referer\"\n");
                unfile_lock(DATA);
                close (DATA);
        }
}

################
sub htmlescape {
################
        my $text = shift;

        $text =~ s/&/&amp;/g;
        $text =~ s/"/&quot;/g;
        $text =~ s/  / \&nbsp;/g;
        $text =~ s/</&lt;/g;
        $text =~ s/>/&gt;/g;
        $text =~ s/\t/ \&nbsp; \&nbsp; \&nbsp;/g;
        $text =~ s/\cM//g;
        $text =~ s/\n/<br>/g;
        $text =~ s/\|/<pipe>/g;

        return $text;
}

##################
sub previewstrip {
##################
        my $text = shift;

        $text =~ s/&/&amp;/g;
        $text =~ s/"/&quot;/g;
        $text =~ s/  / \&nbsp;/g;
        $text =~ s/</&lt;/g;
        $text =~ s/>/&gt;/g;
        $text =~ s/\t/ \&nbsp; \&nbsp; \&nbsp;/g;
        $text =~ s/\cM//g;
        $text =~ s/\|/<pipe>/g;

        return $text;
}

################
sub htmltotext {
################
        my $html = shift;

        $html =~ s~<br>~\n~gi;
        $html =~ s~<\/*(blockquote|ul|li|p)[^<>]*>~\n\n~gi;
        $html =~ s~<a href=\"*([^\s<>\"]+)\"*[^>]*>([\s\S]+?)<\/a>~$2 (link: $1)~gi;
        $html =~ s~<[^>]+>~~g;
        $html =~ s~\"~&quot;~g;
        $html =~ s/ \&nbsp;/  /g;
        $html =~ s~<pipe>~\|~g;

        return $html;
}

#########################
sub convert_newsletter {
#########################

my $text = shift;

        $text =~ s/<pipe>/\|/g;
        $text =~ s/<br>/\n/g;
        $text =~ s/&lt;/</g;
        $text =~ s/&gt;/>/g;
        $text =~ s/ \&nbsp;/  /g;
        $text =~ s/&amp;/&/g;
        $text =~ s/&quot;/"/g;

return $text;

}

##############
sub showhtml {
##############

my $text = shift;

if ($allow_html == 1) {

        $text =~ s/&amp;/&/g;
        $text =~ s/&quot;/"/g;
        $text =~ s/ \&nbsp;/  /g;
        $text =~ s/&lt;/</g;
        $text =~ s/&gt;/>/g;
        $text =~ s/ \&nbsp; \&nbsp; \&nbsp;/\t/g;
        $text =~ s/\n/<br>/g;
        $text =~ s/<pipe>/\|/g;

                $text =~ s~(\<|&lt;?)(.*?)color=([\w#]+)(\>|&gt;?)(.*?)(\<|&lt;?)/color(\>|&gt;?)~<font color="$2">$3</font>~isg;

                $text =~ s~(\<|&lt;?)hr(\>|&gt;?)~<hr size="1">~g;

        $text =~ s~([^\w\"\=\[\]]|[\A\n\b])\\*(\w+://[^<>\s\n\"\]\[]+)~$1<a href="$2" target="_blank">$2</a>~isg;
        $text =~ s~([^\"\=\[\]/\:]|[\A\n\b])\\*(www\.[^<>\s\n\]\[]+)~$1<a href="http://$2" target="_blank">$2</a>~isg;

        $text =~ s~([^\f\"\=\[\]]|[\A\n\b])\\*(\f+://[^<>\s\n\"\]\[]+)~$1<a href="$2" target="_blank">$2</a>~isg;
        $text =~ s~([^\"\=\[\]/\:]|[\A\n\b])\\*(ftp\.[^<>\s\n\]\[]+)~$1<a href="ftp://$2" target="_blank">$2</a>~isg;

        # $text =~ s~(\S+?)\@(\S+)~<a href="mailto:$1\@$2">$1\@$2</a>~gi;
        }

        $text =~ s/<s/&lt;s/g;
        $text =~ s/<s/&lt;j/g;
        $text =~ s/<s/&lt;S/g;
        $text =~ s/<s/&lt;J/g;
        return $text;
}

############
sub doubbc {
############


        $message =~ s~\[\[~\{\{~g;
        $message =~ s~\]\]~\}\}~g;
        $message =~ s~\n\[~\[~g;
        $message =~ s~\]\n~\]~g;

        $message =~ s~\<br\>~ <br>~g;
        $message =~ s~\<pipe\>~\|~g;
        $message =~ s~\[hr\]\n~<hr size="1">~g;
        $message =~ s~\[hr\]~<hr size="1">~g;

        $message =~ s~\[b\]~<b>~isg;
        $message =~ s~\[\/b\]~</b>~isg;

        $message =~ s~\[i\]~<i>~isg;
        $message =~ s~\[\/i\]~</i>~isg;

        $message =~ s~\[u\]~<u>~isg;
        $message =~ s~\[\/u\]~</u>~isg;

        if ($imageicons eq "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<a href="$1" target="_blank"><img src="$1" width="150" height="150" alt="" border="0"></a>~isg;
                }
        if ($imageicons ne "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<img src="$1" alt="" border="0">~isg;
                }

        $message =~ s~\[color=(\S+?)\]~<font color="$1">~isg;
        $message =~ s~\[\/color\]~</font>~isg;

        $message =~ s~\[quote=\s*(\w+\+?)\](.+?)\s*\[/quote\]~<blockquote><b>$1 $msg{'685'}</b><hr width="400" align="left"><cite>$2</cite><hr width="400" align="left"></blockquote>~isg;
        $message =~ s~\[quote\]<br>(.+?)<br>\[\/quote\]~<blockquote><hr width="400" align="left"><cite>$1</cite><hr width="400" align="left"></blockquote>~isg;
        $message =~ s~\[quote\](.+?)\[\/quote\]~<blockquote><hr width="400" align="left"><cite>$1</cite><hr width="400" align="left"></blockquote>~isg;

        $message =~ s~\[fixed\]~<font face="Courier New">~isg;
        $message =~ s~\[\/fixed\]~</font>~isg;

        $message =~ s~\[sup\]~<sup>~isg;
        $message =~ s~\[\/sup\]~</sup>~isg;

        $message =~ s~\[strike\]~<strike>~isg;
        $message =~ s~\[\/strike\]~</strike>~isg;

        $message =~ s~\[sub\]~<sub>~isg;
        $message =~ s~\[\/sub\]~</sub>~isg;

        $message =~ s~\[left\]~<div align="left">~isg;
        $message =~ s~\[\/left\]~</div>~isg;
        $message =~ s~\[center\]~<center>~isg;
        $message =~ s~\[\/center\]~</center>~isg;
        $message =~ s~\[right\]~<div align="right">~isg;
        $message =~ s~\[\/right\]~</div>~isg;

        $message =~ s~\[list\]~<ul>~isg;
        $message =~ s~\[\*\]~<li>~isg;
        $message =~ s~\[\/list\]~</ul>~isg;

        $message =~ s~\[pre\]~<pre>~isg;
        $message =~ s~\[\/pre\]~</pre>~isg;

        $message =~ s~\[code\](.+?)\[\/code\]~<blockquote><p class="forumtextbold">$msg{'684'}<hr width="400" align="left"></p><code>$1</code><p><hr width="400" align="left"></p></blockquote>~isg;

        $message =~ s~\[email\](.+?)\[\/email\]~<a href="mailto:$1">$1</a>~isg;

        $message =~ s~\[url\]www\.\s*(.+?)\s*\[/url\]~<a href="http://www.$1" target="_blank">www.$1</a>~isg;
        $message =~ s~\[url=\s*(\w+\://.+?)\](.+?)\s*\[/url\]~<a href="$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url=\s*(.+?)\]\s*(.+?)\s*\[/url\]~<a href="http://$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url\]\s*(.+?)\s*\[/url\]~<a href="$1" target="_blank">$1</a>~isg;

        $message =~ s~([^\w\"\=\[\]]|[\n\b]|\A)\\*(\w+://[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="$2" target="_blank">$2</a>~isg;
        $message =~ s~([^\"\=\[\]/\:\.]|[\n\b]|\A)\\*(www\.[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="http://$2" target="_blank">$2</a>~isg;

        $message =~ s~\{\{~\[~g;
        $message =~ s~\}\}~\]~g;
}

############
sub undoubbc {
############

        $message =~ s~\[\[~\{\{~g;
        $message =~ s~\]\]~\}\}~g;
        $message =~ s~\n\[~\[~g;
        $message =~ s~\]\n~\]~g;

        $message =~ s~\<br\>~ ~g;
        $message =~ s~\<pipe\>~ ~g;
        $message =~ s~\[hr\]\n~ ~g;
        $message =~ s~\[hr\]~ ~g;

        $message =~ s~\[b\]~<b>~isg;
        $message =~ s~\[\/b\]~</b>~isg;

        $message =~ s~\[i\]~<i>~isg;
        $message =~ s~\[\/i\]~</i>~isg;

        $message =~ s~\[u\]~<u>~isg;
        $message =~ s~\[\/u\]~</u>~isg;

        $message =~ s~\[img\](.+?)\[\/img\]~Image~isg;

        $message =~ s~\[color=(\S+?)\]~<font color="$1">~isg;
        $message =~ s~\[\/color\]~</font>~isg;

        $message =~ s~\[quote\]<br>(.+?)<br>\[\/quote\]~<b>$1</b>~isg;
        $message =~ s~\[quote\](.+?)\[\/quote\]~<b>$1</b>~isg;

        $message =~ s~\[fixed\]~ ~isg;
        $message =~ s~\[\/fixed\]~ ~isg;

        $message =~ s~\[sup\]~ ~isg;
        $message =~ s~\[\/sup\]~ ~isg;

        $message =~ s~\[strike\]~ ~isg;
        $message =~ s~\[\/strike\]~ ~isg;

        $message =~ s~\[sub\]~ ~isg;
        $message =~ s~\[\/sub\]~ ~isg;

        $message =~ s~\[left\]~ ~isg;
        $message =~ s~\[\/left\]~ ~isg;
        $message =~ s~\[center\]~ ~isg;
        $message =~ s~\[\/center\]~ ~isg;
        $message =~ s~\[right\]~ ~isg;
        $message =~ s~\[\/right\]~ ~isg;

        $message =~ s~\[list\]~ ~isg;
        $message =~ s~\[\*\]~ ~isg;
        $message =~ s~\[\/list\]~ ~isg;

        $message =~ s~\[pre\]~ ~isg;
        $message =~ s~\[\/pre\]~ ~isg;

        $message =~ s~\[code\](.+?)\[\/code\]~<b>$1</b>~isg;

        $message =~ s~\[email\](.+?)\[\/email\]~<a href="mailto:$1">$1</a>~isg;

        $message =~ s~\[url\]www\.\s*(.+?)\s*\[/url\]~www.$1~isg;
        $message =~ s~\[url=\s*(\w+\://.+?)\](.+?)\s*\[/url\]~$2~isg;
        $message =~ s~\[url=\s*(.+?)\]\s*(.+?)\s*\[/url\]~$2~isg;
        $message =~ s~\[url\]\s*(.+?)\s*\[/url\]~$1~isg;

        $message =~ s~([^\w\"\=\[\]]|[\n\b]|\A)\\*(\w+://[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1 $2~isg;
        $message =~ s~([^\"\=\[\]/\:\.]|[\n\b]|\A)\\*(www\.[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1 $2~isg;

        $message =~ s~\{\{~\[~g;
        $message =~ s~\}\}~\]~g;
}

#################
sub doubbctopic {
#################

        $message =~ s/&amp;/&/g;
        $message =~ s/&quot;/"/g;
        $message =~ s/ \&nbsp;/  /g;
        $message =~ s/&lt;script&gt;/<skript>/g;
        $message =~ s/&lt;\\script&gt;/<\\skript>/g;
        $message =~ s/&lt;javascript&gt;/<javaskript>/g;
        $message =~ s/&lt;\\javascript&gt;/<\\javaskript>/g;
        $message =~ s/&lt;/</g;
        $message =~ s/&gt;/>/g;
        $message =~ s/ \&nbsp; \&nbsp; \&nbsp;/\t/g;
        $message =~ s/\n/<br>/g;
        $message =~ s/\|/<pipe>/g;

        $message =~ s~\[\[~\{\{~g;
        $message =~ s~\]\]~\}\}~g;
        $message =~ s~\n\[~\[~g;
        $message =~ s~\]\n~\]~g;

        $message =~ s~\<br\>~ <br>~g;
        $message =~ s~\<pipe\>~\|~g;
        $message =~ s~\[hr\]\n~<hr size="1">~g;
        $message =~ s~\[hr\]~<hr size="1">~g;

        $message =~ s~\[b\]~<b>~isg;
        $message =~ s~\[\/b\]~</b>~isg;

        $message =~ s~\[i\]~<i>~isg;
        $message =~ s~\[\/i\]~</i>~isg;

        $message =~ s~\[u\]~<u>~isg;
        $message =~ s~\[\/u\]~</u>~isg;

        if ($imageicons eq "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<a href="$1" target="_blank"><img src="$1" width="150" height="150" alt="" border="0"></a>~isg;
                }
        if ($imageicons ne "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<img src="$1" alt="" border="0">~isg;
                }

        $message =~ s~\[color=(\S+?)\]~<font color="$1">~isg;
        $message =~ s~\[\/color\]~</font>~isg;

        $message =~ s~\[quote=\s*(\w+\+?)\](.+?)\s*\[/quote\]~<blockquote><b>$1 $msg{'685'}</b><hr width="400" align="left"><cite>$2</cite><hr width="400" align="left"></blockquote>~isg;
        $message =~ s~\[quote\]<br>(.+?)<br>\[\/quote\]~<blockquote><hr width="400" align="left"><cite>$1</cite><hr width="400" align="left"></blockquote>~isg;
        $message =~ s~\[quote\](.+?)\[\/quote\]~<blockquote><hr width="400" align="left"><cite>$1</cite><hr width="400" align="left"></blockquote>~isg;

        $message =~ s~\[fixed\]~<font face="Courier New">~isg;
        $message =~ s~\[\/fixed\]~</font>~isg;

        $message =~ s~\[sup\]~<sup>~isg;
        $message =~ s~\[\/sup\]~</sup>~isg;

        $message =~ s~\[strike\]~<strike>~isg;
        $message =~ s~\[\/strike\]~</strike>~isg;

        $message =~ s~\[sub\]~<sub>~isg;
        $message =~ s~\[\/sub\]~</sub>~isg;

        $message =~ s~\[left\]~<div align="left">~isg;
        $message =~ s~\[\/left\]~</div>~isg;
        $message =~ s~\[center\]~<center>~isg;
        $message =~ s~\[\/center\]~</center>~isg;
        $message =~ s~\[right\]~<div align="right">~isg;
        $message =~ s~\[\/right\]~</div>~isg;

        $message =~ s~\[list\]~<ul>~isg;
        $message =~ s~\[\*\]~<li>~isg;
        $message =~ s~\[\/list\]~</ul>~isg;

        $message =~ s~\[pre\]~<pre>~isg;
        $message =~ s~\[\/pre\]~</pre>~isg;

        $message =~ s~\[code\](.+?)\[\/code\]~<blockquote><p class="forumtextbold">$msg{'684'}<hr width="400" align="left"></p><code>$1</code><p><hr width="400" align="left"></p></blockquote>~isg;

        $message =~ s~\[email\](.+?)\[\/email\]~<a href="mailto:$1">$1</a>~isg;

        $message =~ s~\[url\]www\.\s*(.+?)\s*\[/url\]~<a href="http://www.$1" target="_blank">www.$1</a>~isg;
        $message =~ s~\[url=\s*(\w+\://.+?)\](.+?)\s*\[/url\]~<a href="$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url=\s*(.+?)\]\s*(.+?)\s*\[/url\]~<a href="http://$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url\]\s*(.+?)\s*\[/url\]~<a href="$1" target="_blank">$1</a>~isg;

        $message =~ s~([^\w\"\=\[\]]|[\n\b]|\A)\\*(\w+://[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="$2" target="_blank">$2</a>~isg;
        $message =~ s~([^\"\=\[\]/\:\.]|[\n\b]|\A)\\*(www\.[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="http://$2" target="_blank">$2</a>~isg;

        $message =~ s~\{\{~\[~g;
        $message =~ s~\}\}~\]~g;

        $message =~ s/<s/&lt;s/g;
        $message =~ s/<s/&lt;j/g;
        $message =~ s/<s/&lt;S/g;
        $message =~ s/<s/&lt;J/g;
}

############
sub undosmilies {
############

                $message =~ s~\[bones\]~ox~g;
                $message =~ s~\[bounce\]~I~g;
                $message =~ s~\:-\?~:-?~g;
                $message =~ s~\[confused\]~:-?~g;
                $message =~ s~\Q8\)~Q8~g;
                $message =~ s~\Q8-\)~Q8~g;
                $message =~ s~\[cool\]~Q8~g;
                $message =~ s~\[cry\]~:'-(~g;
                $message =~ s~\:o~:o~g;
                $message =~ s~\:\-o~:-o~g;
                $message =~ s~\[eek\]~:-o~g;
                $message =~ s~\[evil\]~>;->~g;
                $message =~ s~\:\(~:-(~g;
                $message =~ s~\:-\(~(:-(~g;
                $message =~ s~\[frown\]~(:-(~g;
                $message =~ s~\:D~:D~g;
                $message =~ s~\:-D~:-D~g;
                $message =~ s~\[grin\]~:-D~g;
                $message =~ s~\[lol\]~LoL~g;
                $message =~ s~\:x~:x~g;
                $message =~ s~\:-x~:-x~g;
                $message =~ s~\[mad\]~:-x~g;
                $message =~ s~\[ninja\]~(:)-)~g;
                $message =~ s~\[nonsense\]~:-?~g;
                $message =~ s~\[oops\]~8-)~g;
                $message =~ s~\[razz\]~:PP~g;
                $message =~ s~\[rolleyes\]~oo~g;
                $message =~ s~\:\)~:-)~g;
                $message =~ s~\:-\)~:-)~g;
                $message =~ s~\[smile\]~:-)~g;
                $message =~ s~\:P~:P~g;
                $message =~ s~\:-P~:-P~g;
                $message =~ s~\[tongue\]~:P~g;
                $message =~ s~\;-\)~;-)~g;
                $message =~ s~\[wink\]~;-)~g;
                $message =~ s~\[tarzan\]~Tz~g;

}

############
sub dosmilies {
############

                $message =~ s~\[bones\]~<img src="$imagesurl/forum/smilies/bones.gif" alt="">~g;
                $message =~ s~\[bounce\]~<img src="$imagesurl/forum/smilies/bounce.gif" alt="">~g;
                $message =~ s~\:-\?~<img src="$imagesurl/forum/smilies/confused.gif" alt="">~g;
                $message =~ s~\[confused\]~<img src="$imagesurl/forum/smilies/confused.gif" alt="">~g;
                $message =~ s~\Q8)\E~<img src="$imagesurl/forum/smilies/cool.gif" alt="">~g;
                $message =~ s~\Q8-)\E~<img src="$imagesurl/forum/smilies/cool.gif" alt="">~g;
                $message =~ s~\[cool\]~<img src="$imagesurl/forum/smilies/cool.gif" alt="">~g;
                $message =~ s~\[cry\]~<img src="$imagesurl/forum/smilies/cry.gif" alt="">~g;
                $message =~ s~\:o~<img src="$imagesurl/forum/smilies/eek.gif" alt="">~g;
                $message =~ s~\:\-o~<img src="$imagesurl/forum/smilies/eek.gif" alt="">~g;
                $message =~ s~\[eek\]~<img src="$imagesurl/forum/smilies/eek.gif" alt="">~g;
                $message =~ s~\[evil\]~<img src="$imagesurl/forum/smilies/evil.gif" alt="">~g;
                $message =~ s~\:\(~<img src="$imagesurl/forum/smilies/frown.gif" alt="">~g;
                $message =~ s~\:-\(~<img src="$imagesurl/forum/smilies/frown.gif" alt="">~g;
                $message =~ s~\[frown\]~<img src="$imagesurl/forum/smilies/frown.gif" alt="">~g;
                $message =~ s~\:D~<img src="$imagesurl/forum/smilies/grin.gif" alt="">~g;
                $message =~ s~\:-D~<img src="$imagesurl/forum/smilies/grin.gif" alt="">~g;
                $message =~ s~\[grin\]~<img src="$imagesurl/forum/smilies/grin.gif" alt="">~g;
                $message =~ s~\[lol\]~<img src="$imagesurl/forum/smilies/lol.gif" alt="">~g;
                $message =~ s~\:x~<img src="$imagesurl/forum/smilies/mad.gif" alt="">~g;
                $message =~ s~\:-x~<img src="$imagesurl/forum/smilies/mad.gif" alt="">~g;
                $message =~ s~\[mad\]~<img src="$imagesurl/forum/smilies/mad.gif" alt="">~g;
                $message =~ s~\[ninja\]~<img src="$imagesurl/forum/smilies/ninja.gif" alt="">~g;
                $message =~ s~\[nonsense\]~<img src="$imagesurl/forum/smilies/nonsense.gif" alt="">~g;
                $message =~ s~\[oops\]~<img src="$imagesurl/forum/smilies/oops.gif" alt="">~g;
                $message =~ s~\[razz\]~<img src="$imagesurl/forum/smilies/razz.gif" alt="">~g;
                $message =~ s~\[rolleyes\]~<img src="$imagesurl/forum/smilies/rolleyes.gif" alt="">~g;
                $message =~ s~\:\)~<img src="$imagesurl/forum/smilies/smile.gif" alt="">~g;
                $message =~ s~\:-\)~<img src="$imagesurl/forum/smilies/smile.gif" alt="">~g;
                $message =~ s~\[smile\]~<img src="$imagesurl/forum/smilies/smile.gif" alt="">~g;
                $message =~ s~\:P~<img src="$imagesurl/forum/smilies/tongue.gif" alt="">~g;
                $message =~ s~\:-P~<img src="$imagesurl/forum/smilies/tongue.gif" alt="">~g;
                $message =~ s~\[tongue\]~<img src="$imagesurl/forum/smilies/tongue.gif" alt="">~g;
                $message =~ s~\;-\)~<img src="$imagesurl/forum/smilies/wink.gif" alt="">~g;
                $message =~ s~\[wink\]~<img src="$imagesurl/forum/smilies/wink.gif" alt="">~g;
                $message =~ s~\[tarzan\]~<img src="$imagesurl/forum/smilies/tarzan.gif" alt="">~g;

}

############
sub getcgi {
############
        read(STDIN, $input, $ENV{'CONTENT_LENGTH'});
        @pairs = split(/&/, $input);
        foreach $pair(@pairs) {

                ($name, $value) = split(/=/, $pair);
                $name =~ tr/+/ /;
                $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
                $value =~ tr/+/ /;
                $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
                                        $value =~ s/< *(\/*)[^>]*script[^>]*>/<\1scrypt>/ig;
                                        $value =~ s/< *(\/*)[^>]*iframe([^>]*)>/\*\1yframe\2\*/ig;
                $input{$name} = $value;
        }
        @vars = split(/&/, $ENV{QUERY_STRING});
        foreach $var(@vars) {
                ($v,$i) = split(/=/, $var);
                $v =~ tr/+/ /;
                $v =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
                $i =~ tr/+/ /;
                $i =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
                $i =~ s/<!--(.|\n)*-->//g;
                $info{$v} = $i;
        }

        $action = $info{'action'};
        $currentboard = $info{'board'};
        $op = $info{'op'};
        $cat = $info{'cat'};
        $viewcat = $info{'viewcat'};
        $num = $info{'num'};
        $id = $info{'id'};
}

#############
sub getdate {
#############

        ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time + 3600*$timeoffset);
        $mon_num = $mon+1;
        $savehour = $hour;
        $hour = "0$hour" if ($hour < 10);
        $min = "0$min" if ($min < 10);
        $sec = "0$sec" if ($sec < 10);
        $saveyear = ($year % 100);
        $year = 1900 + $year;
        $mon_num = "0$mon_num" if ($mon_num < 10);
        $mday = "0$mday" if ($mday < 10);
        $saveyear = "0$saveyear" if ($saveyear < 10);

        $date = "$mon_num/$mday/$saveyear - $hour\:$min\:$sec";
        $shortdate = "$days[$wday], $mon_num.$mday.$year";
        $logdate = "$days[$wday] $mday-$months[$mon]-$year $hour:$min";
        $visitdate = "$mon_num-$mday-$saveyear";
}

################################################################################
# Date/Time and Timezone routines. Added by Floyd with help from Ted. v0.9.8   #
################################################################################

####################
sub display_date {
####################

my ($convertdatetime) = @_;

($cnvdate, $cnvtime) = split(/ - /, $convertdatetime);
($cnvmonth, $cnvday, $cnvyear) = split(/\//, $cnvdate);

if ($user_check_date eq "") {$user_check_date = $check_date;}

if ($user_check_date eq "american") {getTimezones(); getNewtime($cnvdate, $cnvtime);
        $user_display_date = "$newcnvmonth/$newcnvday/$newcnvyear $msg{'580'} $newcnvhour:$newcnvmin:$newcnvsec $displaytimezone";
        }
if ($user_check_date eq "european") {getTimezones(); getNewtime($cnvdate, $cnvtime);
        $user_display_date = "$newcnvday/$newcnvmonth/$newcnvyear $msg{'580'} $newcnvhour:$newcnvmin:$newcnvsec $displaytimezone";
        }

return($user_display_date);

}

###################
sub getTimezones {
###################

      my ($sitetimezone) = @_;

                        if ($user_check_time eq "") {$user_check_time = $timezone;}
                        if ($sitetimezone eq $timezone) {$user_check_time = $sitetimezone;}

                        open (ZONES,"<$datadir/timezones.dat") || error("$err{'016'} $datadir/timezones.dat");
      @timezones=<ZONES>;
      close (ZONES);

                        $displaytimezone = "";

      foreach $zone (@timezones) {
                                                $zone =~ s/[\n\r]//g;
                                                @zitem = split(/\|/, $zone);

            if ($zitem[0] eq $user_check_time) {
                                                         if ($zitem[3] eq "") {$displaytimezone = "$zitem[2]";
                                                         } else {$displaytimezone = "$zitem[3]";
                                                         }
                                                }
      }
}

####################
sub getNewtime {
####################

my ($convertdate, $converttime) = @_;

($cnvhour, $cnvmin, $cnvsec) = split(/:/, $converttime);
if ($convertdate ne "") { ($ncnvmonth, $ncnvday, $ncnvyear) = split(/\//, $convertdate); }

if ($user_check_time eq "") {$user_check_time = $timezone;}

$makeyearnumber = ($ncnvyear*365);
$makemonthnumber = ($ncnvmonth*30);
$makedaynumber = abs($ncnvday);
$monthtraversal = 0;
$leapyear = 0;
if (($makeyearnumber/4) eq int($makeyearnumber/4)) {$leapyear = 1;}

$makehournumber = ($cnvhour*60);
$makeminutenumber = abs($cnvmin);

($tzoffset1, $tzoffset2) = split(/\./, $user_check_time);
($tzoffset3, $tzoffset4) = split(/\./, $timezone);

$nettzoffset = $tzoffset1 - $tzoffset3;

$tzoffset1 = ($nettzoffset*60);
$tzoffset2 = abs($tzoffset2);

if ($tzoffset2 > 24) {
         if ($tzoffset2 eq 25) {$tzoffset2 = abs(60/4);}
         if ($tzoffset2 eq 50) {$tzoffset2 = abs(60/2);}
         if ($tzoffset2 eq 75) {$tzoffset2 = abs((60/4)*3);}
} else {$tzoffset2 = 0;}

if ($tzoffset1 ne 0) {$makehournumber = $makehournumber+$tzoffset1;}
if ($tzoffset2 ne 0 && $tzoffset1 > 0) {$makeminutenumber = $makeminutenumber+$tzoffset2;}
if ($tzoffset2 ne 0 && $tzoffset1 < 0) {$makeminutenumber = $makeminutenumber-$tzoffset2;}

if ($makeminutenumber < 0) {$makeminutenumber = $makeminutenumber+60; $makehournumber = $makehournumber-60;}
if ($makeminutenumber > 59) {$makeminutenumber = $makeminutenumber-60; $makehournumber = $makehournumber+60;}

if ($makehournumber < 0) {$makehournumber = $makehournumber+1440; $makedaynumber = $makedaynumber-1;}
if ($makehournumber > 1439) {$makehournumber = $makehournumber-1440; $makedaynumber = $makedaynumber+1;}

if ($makedaynumber < 1) {$makedaynumber = 31; $makemonthnumber = $makemonthnumber-30; $monthtraversal = 1;}
if ($makedaynumber > 31) {$makedaynumber = 1; $makemonthnumber = $makemonthnumber+30; $monthtraversal = 1;}

#if ($makemonthnumber eq 120 or $makemonthnumber eq 180 or $makemonthnumber eq 270 or $makemonthnumber eq 330 && $monthtraversal eq 1) {$makedaynumber = 30;}

if ($makemonthnumber eq 60 && $monthtraversal eq 1) {
         if ($leapyear eq 1) {$makedaynumber = 29;} else {$makedaynumber = 28;}
}

if ($makedaynumber eq 31 && $makemonthnumber eq 0 && $monthtraversal eq 1) {$makeyearnumber = $makeyearnumber-365; $makemonthnumber = 360;}
if ($makedaynumber eq 1 && $makemonthnumber eq 390 && $monthtraversal eq 1) {$makeyearnumber = $makeyearnumber+365; $makemonthnumber = 30;}

if ($makeyearnumber > 36135) {$makeyearnumber = 0;}
if ($makeyearnumber < 0) {$makeyearnumber = 36135;}

if ($makeyearnumber ne 0) {$newcnvyear = ($makeyearnumber/365);} else {$newcnvyear = 0;}

$newcnvmonth = ($makemonthnumber/30);
$newcnvday = $makedaynumber;
$newcnvhour = ($makehournumber/60);
$newcnvmin = $makeminutenumber;
$newcnvsec = $cnvsec;

if ($newcnvyear < 10) {$newcnvyear = "0$newcnvyear";}
if ($newcnvmonth < 10) {$newcnvmonth = "0$newcnvmonth";}
if ($newcnvday < 10) {$newcnvday = "0$newcnvday";}

if ($newcnvhour < 10) {$newcnvhour = "0$newcnvhour";}
if ($newcnvmin < 10) {$newcnvmin = "0$newcnvmin";}

return($newcnvmonth, $newcnvday, $newcnvyear, $newcnvhour, $newcnvmin, $newcnvsec);

}

################################################################################
# End of new Date/Time and Timezone routines.                                  #
################################################################################

####################
sub calcdifference {
####################
        ($dates, $dummy) = split(/ /, $date1);
        ($month, $day, $year) = split(/\//, $dates);
        $number1 = ($year*365)+($month*30)+$day;
        ($dates, $dummy) = split(/ /, $date2);
        ($month, $day, $year) = split(/\//, $dates);
        $number2 = ($year*365)+($month*30)+$day;
        $result = $number2-$number1;
}

##############
sub calctime {
##############
        ($dummy, $times) = split(/ - /, $date1);
        ($hour, $min, $sec) = split(/:/, $times);
        $number1 = ($hour*60)+$min;
        ($dummy, $times) = split(/ - /, $date2);
        ($hour, $min, $sec) = split(/:/, $times);
        $number2 = ($hour*60)+$min;
        $result = $number2-$number1;
}

################
sub ban {
################

        open (FILE,">>$datadir/stats/stats.dat")|| warn "Cannot open file: $!";
        open (BANNED , "$datadir/banned/banned_ip.txt") || warn "Cannot open $ban_list file: $!";
        file_lock (FILE);
        file_lock (BANNED);
        while (<BANNED>) {

                         chomp;
                         if ($_ eq  $ENV{REMOTE_ADDR}) {
                                 print "Content-type: text/html\n\n";
                                 print "$msg{'475'} $ENV{REMOTE_ADDR}<br>";
                                 print FILE "[BANNED_IP] $_ $msg{'476'}";
                                 print "$msg{'477'}"; exit;
                         }
                }
        unfile_lock (FILE);
        unfile_lock (BANNED);
        close FILE;
        close BANNED;

}

###########
sub error {
###########
      local($e, $e1, $e2) = @_;

      if ($e eq "noguests") { require "$sourcedir/user.pl"; register("$err{'029'}"); }
      elsif ($e eq "nopassmatch") { require "$sourcedir/user.pl"; register("$err{'012'}", "$e1", "$e2"); }
      elsif ($e eq "nousername") { require "$sourcedir/user.pl"; register("$err{'003'}", "$e1", "$e2"); }
      elsif ($e eq "invalidusername") { require "$sourcedir/user.pl"; register("$err{'004'}", "$e1", "$e2"); }
      elsif ($e eq "noemail") { require "$sourcedir/user.pl"; register("$err{'005'}", "$e1", "$e2"); }
      elsif ($e eq "invalidemail") { require "$sourcedir/user.pl"; register("$err{'030'}", "$e1", "$e2"); }
      elsif ($e eq "existsusername") { require "$sourcedir/user.pl"; register("$err{'007'}", "$e1", "$e2"); }
                        else {
            if ($settings[7] ne $root) { $e =~ s/$basedir\/[^\.]*\///ig }
       }

      $navbar = "$btn{'014'} $nav{'001'}";
      print_top();
      print qq~

    <p>
        <b>$msg{'001'}</b><br>
        $e
    </p>
    ~;
      print_bottom();
      exit;
}


#########
sub ver {
#########
        $navbar = "$btn{'014'} Version";
        print_top();
        print qq~<center><br><br>
        Powered by Web-APP<br>
        <b>v$scriptver $updatever</b><br>
        <b><small>Build: $scriptbuildnumber</small></b>
        <br>
        <hr><br><br>Work by: Carter, Floyd, Steve, Paul, Schelly, Kat, BigR, Abywn, Ted <br><br>
      Security Checks by: Juuso & BigR<br>
                        Security Patch by: BigR - Patching System by: Floyd<br><br>
      Documentation and Moderation by: Kat & Schelly<br><br>
                        German Translation by: Frank<br>
                        Portuguese Translation by: Yaza<br><br>
                        And a BIG Thanks to all contributors!</center><br><br>~;
        print_bottom();
        exit;
}

#########
sub die {
#########
        local($e) = @_;
        print qq~<p>
<b>$msg{'001'}</b><br>
$e
~;
die $error;
}

##########
sub file_lock {
##########
        local($file) = @_;
        if ($use_flock eq "1") { flock($file, $LOCK_EX); }
}

############
sub unfile_lock {
############
        local($file) = @_;
        if ($use_flock eq "1") { flock($file, $LOCK_UN); }
}

#############
sub imalert {
#############

print qq~

<script>

var alertmessage="$msg{'478'}"

///No editing required beyond here/////

//Alert only once per browser session (0=no, 1=yes)

var once_per_session=0

function get_cookie(Name) {
  var search = Name + "="
  var returnvalue = "";
  if (document.cookie.length > 0) {
    offset = document.cookie.indexOf(search)
    if (offset != -1) { // if cookie exists
      offset += search.length
      // set index of beginning of value
      end = document.cookie.indexOf(";", offset);
      // set index of end of cookie value
      if (end == -1)
         end = document.cookie.length;
      returnvalue=unescape(document.cookie.substring(offset, end))
      }
   }
  return returnvalue;
}

function alertornot(){
if (get_cookie('alerted')==''){
loadalert()
document.cookie="alerted=yes"
}
}

function loadalert(){
alert(alertmessage)
}

if (once_per_session==0)
loadalert()
else
alertornot()

</script>

~;
}

############
sub sendim {
############
#
# usage:  sendim(sending_to, subject, message, from);
#

        my ($to, $subject, $message, $from) = @_;

        error("$err{'014'}") unless($subject);
        error("$err{'015'}") unless($message);

        if ($from eq "") { $from = $username; }

        $messageid = time;
        $subj = htmlescape($subject);
        $mesg = $message;

        if (-e("$memberdir/$to.dat")) { } else { }

        open (FILE, "$memberdir/$to.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$to.msg");
        file_lock(FILE);
        print FILE "$from|$subj|$date|$mesg|$messageid\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);

}

###############
sub sendemail {
###############
        my ($to, $subject, $message, $from) = @_;

        if ($from) { $webmaster_email = $from; }
        $to =~ s/[ \t]+/, /g;
        $webmaster_email =~ s/.*<([^\s]*?)>/$1/;
        $message =~ s/^\./\.\./gm;
        $message =~ s/\r\n/\n/g;
        $message =~ s/\n/\r\n/g;
        $smtp_server =~ s/^\s+//g;
        $smtp_server =~ s/\s+$//g;

         if ($mailtype == 1) {
                ($x, $x, $x, $x, $here) = gethostbyname($null);
                ($x, $x, $x, $x, $there) = gethostbyname($smtp_server);
                $thisserver = pack('S n a4 x8', 2, 0, $here);
                $remoteserver = pack('S n a4 x8', 2, 25, $there);
                (!(socket(S, 2, 1, 6))) && (error("Connect error! socket"));
                (!(bind(S, $thisserver))) && (error("Connect error! bind"));
                (!(connect(S, $remoteserver))) && (error("!! connection to $smtp_server has failed!"));

                my ($oldfh) = select(S);
                $| = 1;
                select($oldfh);

                $_ = <S>;
                ($_ !~ /^220/) && (error("Sending Email: data in Connect error - 220"));

                print S "HELO $smtp_server\r\n";
                $_ = <S>;
                ($_ !~ /^250/) && (error("Sending Email: data in Connect error - 250"));

                print S "MAIL FROM:<$webmaster_email>\n";
                $_ = <S>;
                ($_ !~ /^250/) && (error("Sending Email: 'From' address not valid"));

                print S "RCPT TO:<$to>\n";
                $_ = <S>;
                ($_ !~ /^250/) && (error("Sending Email: 'Recipient' address not valid"));

                print S "DATA\n";
                $_ = <S>;
                ($_ !~ /^354/) && (error("Sending Email: Message send failed - 354"));
        }

        if ($mailtype == 0) {
                open(S,"| $mailprogram -t") || error("$err{'008'}");
        }

        print S "To: $to\n";
        print S "From: $webmaster_email\n";
        print S "Subject: $subject\n\n";
        print S "$message";
        print S "\n.\n";

        if ($mailtype == 1) {
                $_ = <S>;
                ($_ !~ /^250/) && (error("Sending Email: Message send failed - try again - 250"));
                print S "QUIT\r\n";
        }

        close(S);
        return(1);
}

############
sub mystatus {
############
#
# Usage:
#         mystatus(moderators);
#         if ($mystatus eq "yes") { show this code to that group; }
#
        my ($status) = @_;

        open(FILE, "<$memberdir/$username.dat");
        file_lock(FILE);
        chomp(@statusdata = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        if ($statusdata[14] eq "$status") { $mystatus = "yes"; }
        if ($statusdata[14] ne "$status") { $mystatus = "no"; }

}

##################
sub reindexlinks {
##################

open(LCATS, "$linksdir/linkcats.dat");
file_lock(LCATS);
@LCATS = <LCATS>;
unfile_lock(LCATS);
close(LCATS);

$totallinks = 0;

foreach $lcat (@LCATS) {
        ($catname,$catfile,$catdesc) = split(/\|/, $lcat);

        $lines = 0;
        open(DATA,"<$linksdir/$catfile.dat");
        file_lock(DATA);
        while (sysread DATA, $buffer, 4096) {
                $lines += ($buffer =~ tr/\n//);
        }
        unfile_lock(DATA);
        close DATA;

        if ($lines == 0) {
                # unlink "$linksdir/$catfile.dat";
                # unlink "$linksdir/$catfile.cnt";
        }else{
                open(CAT, "<$linksdir/$catfile.dat");
                file_lock(CAT);
                @LINKS = <CAT>;
                unfile_lock(CAT);
                close(CAT);

                open(CAT, ">$linksdir/$catfile.dat");
                file_lock(CAT);
                $idnew = 0;

                foreach $link (@LINKS) {
                        chomp($link);
                        $idnew++;
                        ($id, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $link);

##STEVE##27-03-02## MODS HERE!
                        if ($votes eq "") { #IF THERE ARE NO VOTES THEN THIS IS AN OLD VER FILE SO MAKE THE NEW FIELDS AND PUT 0 IN EM
                                $votes = "0";
                                $score = "0";
                        }

                        print CAT "$idnew|$linkname|$theurl|$desc|$thedate|$linkposter|$nhits|$votes|$score|\n";

                }

                unfile_lock(CAT);
                close(CAT);

                open(CNT, ">$linksdir/$catfile.cnt");
                file_lock(CNT);
                print CNT "$idnew";
                unfile_lock(CNT);
                close(CNT);

                $totallinks = $totallinks + $idnew;

                open(LCNT, ">$linksdir/linkcats.cnt");
                file_lock(LCNT);
                print LCNT "$totallinks";
                unfile_lock(LCNT);
                close(LCNT);
        }

}

}

######################
sub reindexdownloads {
######################

open(LCATS, "$downloadsdir/downloadcats.dat");
file_lock(LCATS);
@LCATS = <LCATS>;
unfile_lock(LCATS);
close(LCATS);

$totallinks = 0;

foreach $lcat (@LCATS) {
        ($catname,$catfile,$catdesc) = split(/\|/, $lcat);

        $lines = 0;
        open(DATA,"<$downloadsdir/$catfile.dat");
        file_lock(DATA);
        while (sysread DATA, $buffer, 4096) {
                $lines += ($buffer =~ tr/\n//);
        }
        unfile_lock(DATA);
        close DATA;

        if ($lines == 0) {
                # unlink "$downloadsdir/$catfile.dat";
                # unlink "$downloadsdir/$catfile.cnt";
        }else{
                open(CAT, "<$downloadsdir/$catfile.dat");
                file_lock(CAT);
                @LINKS = <CAT>;
                unfile_lock(CAT);
                close(CAT);

                open(CAT, ">$downloadsdir/$catfile.dat");
                file_lock(CAT);
                $idnew = 0;

                foreach $link (@LINKS) {
                        chomp($link);
                        $idnew++;
                        ($id, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $link);

                        print CAT "$idnew|$linkname|$theurl|$desc|$thedate|$linkposter|$nhits|$votes|$score|\n";

                }

                unfile_lock(CAT);
                close(CAT);

                open(CNT, ">$downloadsdir/$catfile.cnt");
                file_lock(CNT);
                print CNT "$idnew";
                unfile_lock(CNT);
                close(CNT);

                $totallinks = $totallinks + $idnew;

                open(LCNT, ">$downloadsdir/downloadcats.cnt");
                file_lock(LCNT);
                print LCNT "$totallinks";
                unfile_lock(LCNT);
                close(LCNT);
        }

}

}

# For Language Support - Added by Floyd 05/05/02 #
##################
sub getlanguage {
##################

     open(FILE, "$scriptdir/lang/languages.dat" );
     file_lock(FILE);
     @lang = <FILE>;
     unfile_lock(FILE);
     close(FILE);

                 foreach $line (@lang) {
       $line =~ s/[\n\r]//g;
       @item = split(/\|/, $line);
         if ($item[2] ne "0" && $item[1] eq $userlang) {
                                 $getuserlang = $item[1]; $langgfx = $item[3];
                                 }
                                 if ($item[2] eq "0") {
                                 $getuserlang = $language;
                                 ($langgfx,$dummy)=split(/\./,$getuserlang);
                                 }
                        }

if ($getuserlang eq "") { $getuserlang = $language; }

if ($langgfx eq "") {
         $getuserlang = $language;
         ($langgfx,$dummy)=split(/\./,$getuserlang);
}

eval {
        require "$langdir/$getuserlang";

        if ($IIS != 2) {
                if ($IIS == 0) {
                        if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
                }
                if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
                if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
        }
};

if ($@) {language_fail();}

}

########################
sub language_fail {
########################

eval {
        require "$lang";

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
print qq~<h1>Language File Error:</h1>
Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
<pre>$@</pre>
<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
~;
        exit;
}

}

##################
sub xml {
##################

open(XML, ">$basedir/webapp.xml");
file_lock(XML);

print XML qq~<?xml version="1.0" encoding="ISO-8859-1"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://purl.org/rss/1.0/">
<channel rdf:about="$baseurl">
<title>$pagetitle</title>
<link>$scripturl/$cgi</link>
<description>$pagetitle - News to Go</description>
<items>
<rdf:Seq>
~;

        undef @catnames;
        undef @catlinks;

        open(FILE, "$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);

        close(FILE);

        foreach (@cats) {
                @item = split(/\|/, $_);
                push(@catnames, $item[0]);
                push(@catlinks, $item[1]);
        }

        if ($info{'id'} eq "") {

                %data = ();

                foreach $curcat (@catlinks) {
                        if (-e("$topicsdir/$curcat.cat")) {
                                foreach (@cats) {
                                        @item = split(/\|/, $_);
                                        if ($curcat eq "$item[1]") { $curcatname = "$item[0]"; }
                                }

                                open(FILE, "$topicsdir/$curcat.cat");
                                file_lock(FILE);
                                chomp(@articles = <FILE>);

                                close(FILE);

                                for ($a = 0; $a < @articles && $a <= $maxnews; $a++) {
                                        ($id, $subject, $nick, $poster, $email, $postdate, $comments) = split(/\|/, $articles[$a]);

                                        if ($comments == 1) { $commentscnt = "$comments $msg{'040'}"; }
                                        else { $commentscnt = "$comments $msg{'041'}"; }

                                        open (FILE, "$topicsdir/articles/$id.txt");
                                        file_lock(FILE);
                                        chomp($text = <FILE>);

                                        close(FILE);

                                        @text = split(/\|/, $text);
                                        $message = showhtml("$text[5]");


$post = qq~<rdf:li resource="$scripturl/index.cgi?action=viewnews\&amp;id=$id" />
~;

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
                        print XML "$data{$num[$j]}";
                        $j++;
                }
        }

# continuing with the xml shit

print XML qq~</rdf:Seq>
</items>
</channel>
~;

undef @catnames;
        undef @catlinks;

        open(FILE, "$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);

        close(FILE);

        foreach (@cats) {
                @item = split(/\|/, $_);
                push(@catnames, $item[0]);
                push(@catlinks, $item[1]);
        }

        if ($info{'id'} eq "") {

                %data = ();

                foreach $curcat (@catlinks) {
                        if (-e("$topicsdir/$curcat.cat")) {
                                foreach (@cats) {
                                        @item = split(/\|/, $_);
                                        if ($curcat eq "$item[1]") { $curcatname = "$item[0]"; }
                                }

                                open(FILE, "$topicsdir/$curcat.cat");
                                file_lock(FILE);
                                chomp(@articles = <FILE>);

                                close(FILE);

                                for ($a = 0; $a < @articles && $a <= $maxnews; $a++) {
                                        ($id, $subject, $nick, $poster, $email, $postdate, $comments) = split(/\|/, $articles[$a]);

                                        if ($comments == 1) { $commentscnt = "$comments $msg{'040'}"; }
                                        else { $commentscnt = "$comments $msg{'041'}"; }

                                        open (FILE, "$topicsdir/articles/$id.txt");
                                        file_lock(FILE);
                                        chomp($text = <FILE>);

                                        close(FILE);

                                        @text = split(/\|/, $text);
                                        $message = showhtml("$text[5]");


$post = qq~
<item rdf:about="$scripturl/index.cgi?action=viewnews\&amp;id=$id">
<title>$subject</title>
<link>$scripturl/index.cgi?action=viewnews\&amp;id=$id</link>
</item>
~;
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
                        print XML "$data{$num[$j]}";
                        $j++;
                }
        }

print XML qq~</rdf:RDF>
~;

unfile_lock(XML);
close(XML);

}

###############
sub check_access {
###############

$access_granted = 0;

if ($username ne "admin") {

my ($actrequest) = @_;
# Are YOU actually allowed to be here at all!
if ($actrequest eq "siteadmin") {
         if ($username ne "$article_imrecip") {
                         if ($settings[7] ne "$root") { error("$err{'011'}"); }
         }
}
# Are YOU actually allowed to see the link
if ($actrequest eq "siteadminlink") {
         if ($username ne "$article_imrecip") {
                         $adminlinkprinted = 0;
                         if ($settings[7] eq "$root") { $adminlinkprinted = 1; menuitem("admin\&amp\;op=siteadmin", "$nav{'042'}"); }
         }
         if ($username eq "$article_imrecip") {
                         if ($adminlinkprinted ne 1) { menuitem("admin\&amp\;op=siteadmin", "$nav{'042'}"); }
         }
}


# Site Admin Section
if ($actrequest eq "editwelc" && $editwelc eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editabout" && $editabout eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editim" && $editim eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editbanner" && $editbanner eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editfaq" && $editfaq eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editdown" && $editdown eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editlink" && $editlink eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "modadmin" && $modadmin eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}


# Forum Admin Section
if ($actrequest eq "editcats" && $editcats eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editboards" && $editboards eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editcensor" && $editcensor eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}


# Poll Admin Section
if ($actrequest eq "editpoll" && $editpoll eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}


# News Admin Section
if ($actrequest eq "pubnews" && $pubnews eq 1) {
         if ($username ne "$article_imrecip") {
                         if ($settings[7] eq "$root") { $access_granted = 1; }
         } else { $access_granted = 1; }
}
if ($actrequest eq "editnews" && $editnews eq 1) {
         if ($username ne "$article_imrecip") {
                         if ($settings[7] eq "$root") { $access_granted = 1; }
         } else { $access_granted = 1; }
}
if ($actrequest eq "edittops" && $edittops eq 1) {
         if ($username ne "$article_imrecip") {
                         if ($settings[7] eq "$root") { $access_granted = 1; }
         } else { $access_granted = 1; }
}


# Block Admin Section
if ($actrequest eq "editlblk" && $editlblk eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editrblk" && $editrblk eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}


# Module Admin Section
if ($actrequest eq "editcal" && $editcal eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}
if ($actrequest eq "editnl" && $editnl eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}


# Security Admin Section
if ($actrequest eq "editip" && $editip eq 1) {
         if ($settings[7] eq "$root") { $access_granted = 1; }
}

}


if ($username eq "admin") { $access_granted = 1; }


}

# Mod Language Support Routines - Floyd: 01/22/03 ##############################

###########################
sub mod_getlanguage {
###########################
my ($modrequest, $moddefaultlanguage)=@_;

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
                ($modlang,$dummy)=split(/\./,$userlang);

eval {
        require "$scriptdir/mods/$modrequest/language/$modlang.dat";

        if ($IIS != 2) {
                if ($IIS == 0) {
                        if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
                }
                if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
                if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
        }
};

if ($@) { mod_getlanguagefail($modrequest, $moddefaultlanguage);}

}

########################
sub mod_getlanguagefail {
########################
my ($modrequest, $moddefaultlanguage)=@_;

eval {
        require "$scriptdir/mods/$modrequest/language/$moddefaultlanguage";

        if ($IIS != 2) {
                if ($IIS == 0) {
                        if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
                }
                if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
                if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
        }
};

if ($@) {mod_getlanguagecritical($modrequest);}

}

########################
sub mod_getlanguagecritical {
########################
my ($modrequest)=@_;

eval {
        require "$scriptdir/mods/$modrequest/language/english.dat";

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
print qq~<h1>Mod Error</h1>
<b>NO LANGUAGE FILES WERE FOUND!</b><br><br>
If this problem persits, please contact the webmaster and inform him about date and time you recieved this error.~;
        exit;
}

}

# Latest Links & Downloads Routines - Floyd: 01/22/03

##################
sub latestlinks {
##################

@_lcats = ();
@_litem = ();
@_lcontent = ();
@_tlcats = ();
@_tlfields = ();
@_ltlsorted = ();
@_tlinks = ();
@_ltlresorted = ();
@_ltlresortedfields = ();
@_ltlfinalsort = ();
@_ltfinallinks = ();

        open(CAT, "<$linksdir/linkcats.dat") || error("$err{'001'} $linksdir/linkcats.dat");
        @_lcats = <CAT>;
        close(CAT);

        foreach (@_lcats) {
                @_litem = split(/\|/, $_);
                if (-e("$linksdir/$_litem[1].dat")) {
                        open(FILE, "<$linksdir/$_litem[1].dat") || error("$err{'001'} $linksdir/$_litem[1].dat");
                        @_lcontent = <FILE>;
                        close(FILE);

                        for ($_tl = 0; $_tl < @_lcontent; $_tl++) {
                                ($_lid, $_lname, $dummy, $_ldescription, $_ldate, $dummy, $_lcount, $dummy, $dummy) = split(/\|/, $_lcontent[$_tl]);
                                        push (@_tlcats, join ("\|", $_litem[1], $_lid, $_lname, $_ldate, $_lcount, $_ldescription));
                        }
                }
        }

        for (0..$#_tlcats) {
                @_tlfields = split(/\|/, $_tlcats[$_]);
                for $i (0..$#_tlfields) {
                        $_tldata[$_][$i] = $_tlfields[$i];
                }
        }
        @_tlsorted = reverse sort { $b->[3] <=> $a->[3] } @_tldata;
        for (@_tlsorted) {
                $_tlsortedrow = join ("|", @$_);
                push (@_tlinks, $_tlsortedrow);
        }

         for ($_rel = 0; $_rel < @_tlinks; $_rel++) {
   ($_ltlcat, $_ltlid, $_ltlname, $_ltldate, $_ltlcount, $_ltldescription) = split(/\|/, $_tlinks[$_rel]);
                                $date2 = $date; $date1 = $_ltldate;        calcdifference();
                                $_ltldateref = $result;
                        push (@_ltlresorted, join ("\|", $_ltlcat, $_ltlid, $_ltlname, $_ltldateref, $_ltldate, $_ltlcount, $_ltldescription));
   }

   for (0..$#_ltlresorted) {
      @_ltlresortedfields = split(/\|/, $_ltlresorted[$_]);
      for $i (0..$#_ltlresortedfields) {
         $_ltlresorteddata[$_][$i] = $_ltlresortedfields[$i];
      }
   }

         @_ltlfinalsort = reverse sort { $b->[3] <=> $a->[3] } @_ltlresorteddata;
   for (@_ltlfinalsort) {
      $_ltlfinalsortrow = join ("\|", @$_);
      push (@_ltfinallinks, $_ltlfinalsortrow);
   }

}

##################
sub latestdownloads {
##################

@_dlcats = ();
@_dlitem = ();
@_dlcontent = ();
@_dtlcats = ();
@_dtlfields = ();
@_dtlsorted = ();
@_dtlinks = ();
@_dtlresorted = ();
@_dtlresortedfields = ();
@_dtlfinalsort = ();
@_ltfinaldownloads = ();

open(CAT, "<$downloadsdir/downloadcats.dat") || error("$err{'001'} $downloadsdir/downloadcats.dat");
@_dlcats = <CAT>;
close(CAT);

   foreach (@_dlcats) {
      @_dlitem = split(/\|/, $_);
      if (-e("$downloadsdir/$_dlitem[1].dat")) {
         open(FILE, "<$downloadsdir/$_dlitem[1].dat") || error("$err{'001'} $downloadsdir/$_dlitem[1].dat");
         @_dlcontent = <FILE>;
         close(FILE);

         for ($_dtl = 0; $_dtl < @_dlcontent; $_dtl++) {
            ($_dlid, $_dlname, $dummy, $_ddescription, $_dldate, $dummy, $_dlcount, $dummy) = split(/\|/, $_dlcontent[$_dtl]);
               push (@_dtlcats, join ("|", $_dlitem[1], $_dlid, $_dlname, $_dldate, $_dlcount, $_ddescription));
         }
      }
   }

   for (0..$#_dtlcats) {
      @_dtlfields = split(/\|/, $_dtlcats[$_]);
      for $i (0..$#_dtlfields) {
         $_dtldata[$_][$i] = $_dtlfields[$i];
      }
   }

   @_dtlsorted = reverse sort { $b->[3] <=> $a->[3] } @_dtldata;
   for (@_dtlsorted) {
      $_dtlsortedrow = join ("|", @$_);
      push (@_dtlinks, $_dtlsortedrow);
   }

            for ($_res = 0; $_res < @_dtlinks; $_res++) {
      ($_dtlcat, $_dtlid, $_dtlname, $_dtldate, $_dtlcount, $_dtldescription) = split(/\|/, $_dtlinks[$_res]);
                                                $date2 = $date; $date1 = $_dtldate;        calcdifference();
                                                $_dtldateref = $result;
                                                push (@_dtlresorted, join ("|", $_dtlcat, $_dtlid, $_dtlname, $_dtldateref, $_dtldate, $_dtlcount, $_dtldescription));
      }

   for (0..$#_dtlresorted) {
      @_dtlresortedfields = split(/\|/, $_dtlresorted[$_]);
      for $i (0..$#_dtlresortedfields) {
         $_dtlresorteddata[$_][$i] = $_dtlresortedfields[$i];
      }
   }

         @_dtlfinalsort = reverse sort { $b->[3] <=> $a->[3] } @_dtlresorteddata;
   for (@_dtlfinalsort) {
      $_dtlfinalsortrow = join ("|", @$_);
      push (@_ltfinaldownloads, $_dtlfinalsortrow);
   }

}

#################
sub saveConfig {
#################

 my $cref=shift;
 my $thing='';
 my $filename="$config_dir/config.dat";
 my %new_conf=();
 foreach $thing (keys %waconf)
   { $new_conf{$thing}=defined $$cref{$thing}?$$cref{$thing}:$waconf{$thing}; }
 open OFCFG,">$filename";
 foreach $thing (keys %new_conf)
   { print OFCFG "$thing\|$new_conf{$thing}\n"; }
 close OFCFG;
 }

##################
sub censor_it {
##################
# Use: $text_to_censor = censor_it($text_to_censor);
##################
my ($texttocensor)=@_;
open(CENSOR, "$boardsdir/censor.txt");
file_lock(CENSOR);
chomp(@censored = <CENSOR>);
unfile_lock(CENSOR);
close(CENSOR);

foreach $censor (@censored) {
 ($word, $censored) = split(/\=/, $censor);
 $texttocensor =~ s/\b$word\b/$censored/gi;
}
return $texttocensor;
}

###################
sub read_database {
###################
# Use: @array = read_database("path_to_file/filename_to_read");
###################
my ($filetoread)=@_;
@readfile = ();

        open(DATABASE, "$filetoread") || error("$err{'001'} $filetoread");
        file_lock(DATABASE);
        @readfile = <DATABASE>;
        unfile_lock(DATABASE);
        close(DATABASE);

return @readfile;
}

###################
sub chomp_database {
###################
# Use: @array = chomp_database("path_to_file/filename_to_read");
###################
my ($filetochomp)=@_;
@chompedfile = ();

        open(DATABASE, "$filetochomp") || error("$err{'001'} $filetochomp");
        file_lock(DATABASE);
        chomp(@chompedfile = <DATABASE>);
        unfile_lock(DATABASE);
        close(DATABASE);

return @chompedfile;
}

###################
sub chomp_datatext {
###################
# Use: $variable = chomp_datatext("path_to_file/filename_to_read");
###################
my ($filetochomp)=@_;
$chompedtext = "";

        open(DATABASE, "$filetochomp") || error("$err{'001'} $filetochomp");
        file_lock(DATABASE);
        chomp($chompedtext = <DATABASE>);
        unfile_lock(DATABASE);
        close(DATABASE);

return $chompedtext;
}

if (-e "$scriptdir/user-lib/subs.pl") {require "$scriptdir/user-lib/subs.pl"}

1; # return true