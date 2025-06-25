#!/usr/bin/perl

  read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
  if (length($buffer) < 5) {
    $buffer = $ENV{QUERY_STRING};
  }

  @pairs = split(/&/, $buffer);
  foreach $pair (@pairs) {
    ($name, $value) = split(/=/, $pair);

    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $value =~ s/[\;\|\\ ]/ /ig;
    $INPUT{$name} = $value;
}


require "config.pl";
require "$sourcedir/subs.pl";

$username = "$INPUT{'user'}";

 if ($username eq "") {
 print "Content-type: text\n\n";
 print "Username Error";
  }
 else {

$newmess = 0;
$newposts = 0;
$newemal = 0;


$USER = "webmaster\@sanctuaryeq2.com";
$PASSWORD = "dragon45";
$HOST = "mail.sanctuaryeq2.com";
$DOMAIN = "sanctuaryeq2.com";
$SCRIPTURL = "http://www.sanctuaryeq2.com/cgi-bin/updater.cgi";
$mailprog = "/usr/sbin/sendmail";

#### MESSAGES ####


                 open(IM, "$memberdir/$username.msg");
                 file_lock(IM);
                 @immessages = <IM>;
                 unfile_lock(IM);
                 close(IM);

                 $mnum = @immessages;
                 $messnum = "$mnum";

open(FILE, "$memberdir/$username.upder");
file_lock(FILE);
chomp(@pref = <FILE>);
unfile_lock(FILE);
close(FILE);

$newmess = $mnum - $pref[0];

open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "$mnum\n";
unfile_lock(FILE);
close(FILE);


#### FOURMS ####

          open(FILE, "$memberdir/$username.dat");
                file_lock(FILE);
                @settings = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                for( $i = 0; $i < @settings; $i++ ) {
                        $settings[$i] =~ s~[\n\r]~~g;
                }



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

                                if ($dlp ne "$postdate" && $postdate ne "???" && $username ne "$anonuser" && $difference <= "$max_log_days_old") { $newposts = $newposts + 1; }

                                if ($poster eq "") { $poster = "???"; }
                                else { $poster = "$poster"; }


                        }
                }
        }

#### EMAIL ####

$shown = 0;

use Mail::POP3Client;
$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $input{'DEBUG'});
  for( $i = 1; $i <= $pop->Count(); $i++ ) {
    $_ = $pop->List($i);
    ($no, $size) = split(/ /);
    $size[$no] = $size;

    foreach( $pop->Head( $i ) ) {
      $to[$no] = $_ if (/To:/);
      $date[$no] = $_ if (/Date:/);
      $from[$no] = $_ if (/From:/);
      $returnpath[$no] = $_ if (/Return-Path:/);
      $replypath[$no] = $_ if (/Reply-Path:/);
      $subject[$no] = $_ if (/Subject:/);
    }

  }
$popstate = $pop->State();
$pop->Close();

if (($popstate eq "TRANSACTION") && (@size)) {

for ($i=1;$i<=(scalar @size)-1;$i++) {

$to[$i] =~ s/To: //gi;
#$from[$i] =~ s/From: //gi;
$date[$i] =~ s/Date: //gi;
$subject[$i] =~ s/Subject: //gi;
$returnpath[$i] =~ s/Return-Path: <//gi;
$returnpath[$i] =~ s/>//gi;


        #if ($from[$i] !~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/ ||
        #$from[$i] !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/) {
        #        $returnpath[$i] = $from[$i];
        #}



$checkuser = $username;
$checkuser =~ tr/A-Z/a-z/;
$checkto = $to[$i];
$checkto =~ s/reply-//gi;
$checkto =~ tr/A-Z/a-z/;

if ($checkto eq "$checkuser\@$DOMAIN") {

$shown++;
}#if
}#for




}

open(FILE, "$memberdir/$username.ema");
file_lock(FILE);
chomp(@prefemal = <FILE>);
unfile_lock(FILE);
close(FILE);

$newemal = $shown - $prefemal[0];

open(FILE, ">$memberdir/$username.ema");
file_lock(FILE);
print FILE "$shown\n";
unfile_lock(FILE);
close(FILE);


#### LOG IT ####
     getdate();

        open(LOG, "$datadir/logs/$visitdate.dat");
        file_lock(LOG);
        chomp(@entries = <LOG>);
        unfile_lock(LOG);
        close(LOG);

        open(LOG, ">$datadir/logs/$visitdate.dat");
        file_lock(LOG);
        $field = $username;
        $myCount = 1;

        if ($field eq $anonuser) { $field = "$ENV{'REMOTE_ADDR'}"; }

         $field = "$field (Updater)";

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


#### PRINT IT OUT ####

          print "Content-type: text\n\n";

## Message Count, New Messages, New Posts, E-Mails, New E-Mails

print qq~$mnum, $newmess, $newposts, $shown, $newemal~;

}