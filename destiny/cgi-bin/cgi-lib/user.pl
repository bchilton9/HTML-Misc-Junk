###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# user.pl                                                                     #
# v0.9.9 - Requin                                                             #
# User Profile changes by: Kat, Floyd & Carter for v0.9.8                     #
# Error Messages & Alternate Sign Up methods by: Floyd for v0.9.8             #
#                                                                             #
# Copyright (C) 2002 by Carter (carter@mcarterbrown.com)                      #
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
# File: Last modified: 11/13/02                                                     #
###############################################################################
###############################################################################


##############
sub register {
##############

        local($errmsg, $errvalue1, $errvalue2) = @_;
        if ($signupmethod eq "") {$signupmethod = "0";}

        $navbar = "$btn{'014'} $nav{'011'}";
        print_top();
        print qq~
        <form onSubmit="submitonce(this)" onSubmit="submitonce(this)" action="$pageurl/$cgi?action=register2" method="post">
        <table border="0" cellspacing="1">~;
        if ($errmsg ne "") {
        print qq~
        <tr>
        <td colspan="2" class="formstextnormal"><font color="#ff0000">$errmsg</font></td>
        </tr>
        <tr>
        <td colspan="2" align="center">&nbsp;<br></td>
        </tr>~;
        }
        print qq~<tr>
        <td width="15%" class="formstextnormal">$msg{'006'}</td>
        <td width="85%"><input type="text" name="username" size="30" maxlength="20" value="$errvalue1"></td>
        </tr>~;
        if ($signupmethod eq "1") {
        print qq~<tr>
        <td width="15%" class="formstextnormal">$msg{'009'}</td>
        <td width="85%"><input type="password" name="passwrd1" size="30" maxlength="100"></td>
        </tr>
        <tr>
        <td width="15%" class="formstextnormal">$msg{'537'}:</td>
        <td width="85%"><input type="password" name="passwrd2" size="30" maxlength="100"></td>
        </tr>~;
        }
        print qq~
        <tr>
        <td width="15%" class="formstextnormal">$msg{'007'}</td>
        <td width="85%"><input type="text" name="email" size="30" maxlength="100" value="$errvalue2"></td>
        </tr>
        ~;

        if ($letmemlng eq "1") {print qq~
<tr>
<td width="15%" valign="top" class="formstextnormal">$msg{'412'}</td>
<td width="85%"><select name="picklanguage">
~;
     open(FILE, "$scriptdir/lang/languages.dat" );
     file_lock(FILE);
     @lang = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@lang) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($item[0] ne "" && $item[1] eq $language) { print qq~<option selected value="$item[1]">$item[0]</option>~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>~; }
                                         }
           }
     print qq~</select>
</td>
</tr>
~; }

        if (($modulenlmem eq "1") || ($modulenl eq "1")) {
        print qq~<tr><td width="15%" class="formstextnormal">$msg{'172'}</td><td width="85%"><INPUT TYPE="checkbox" NAME="newsletter" CHECKED></td></tr>~;
        }

# Eula

open(FILE, "$datadir/agreement.txt");
file_lock(FILE);
chomp(@text = <FILE>);
unfile_lock(FILE);
close(FILE);

print qq~<tr>
        <td colspan="2" align="center">&nbsp;<br></td>
        </tr>
        <tr>
        <td colspan="2"><b>$msg{'570'}:</b></td>
        </tr>
        <tr><td colspan="2">~;

foreach $line (@text) {

        $line =~ s/WEBSITE/$pagename/g;

        print qq~$line~;

        }

print qq~</td></tr>~;

# End Eula

        print qq~
        <tr>
        <td colspan="2" align="center"><input type="submit" class="button" value="$msg{'568'}">
        </td>
        </tr>
        <tr>
        <td colspan="2" align="center">&nbsp;<br></td>
        </tr>~;

if ($signupmethod ne "2") {
print qq~
        <tr>
        <td colspan="2" align="center" class="formstextnormal">$msg{'583'}</td>
        </tr>~;
}


else {

print qq~
        <tr>
        <td colspan="2" align="center" class="formstextnormal">$inf{'022'} $inf{'026'}</td>
        </tr>~;

}

print qq~
        <tr>
        <td colspan="2" align="center">&nbsp;<br></td>
        </tr>
        </table>
        </form>
        ~;

        print_bottom();
        exit;
}

###############
sub register2 {
###############

        $input{'username'} = censor_it($input{'username'});

  if ($input{'username'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<+|\%)/) { error("invalidusername", "", $input{'email'}) }
        error("nousername", "", $input{'email'}) if ($input{'username'} eq "");
        error("invalidusername", "", $input{'email'}) if ($input{'username'} !~ /^[0-9A-Za-z#%+,-\.:=?@^_]+$/ || $input{'username'} eq "|" || $input{'username'} =~ "$anonuser");
        error("noemail", $input{'username'}, "") if ($input{'email'} eq "");
        error("invalidemail", $input{'username'}, "") if ($input{'email'} !~ /^[0-9A-Za-z@\._\-]+$/ || $input{'email'} =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)|(\.$)/) || ($input{'email'} !~ /\A.+@\[?(\w|[-.])+\.[a-zA-Z]{2,4}|[0-9]{1,4}\]?\Z/);
        error("existsusername", "", $input{'email'}) if (-e ("$memberdir/$input{'username'}.dat"));

        if ($input{'picklanguage'} eq "") {$userlanguage = "$language";
        } else {$userlanguage = "$input{'picklanguage'}";}

        if ($signupmethod eq "") {$signupmethod ="0";}

        if ($signupmethod eq "1") {
                 if ($input{'passwrd1'} ne "$input{'passwrd2'}") { error("nopassmatch", "$input{'username'}", "$input{'email'}"); }
        }

#Brad M. Mod - do a more thorough check for username

                                open (MEMBERS,"$memberdir/memberlist.dat") || die "I can't open user database\n";
                                while(<MEMBERS>) {
                                chop;
                                @allnames = split(/\n/);
                                $checkusername = $input{'username'};
                                if (grep (/\b^$checkusername\b/i, @allnames) ne "0" ) { error("existsusername", "", "$input{'email'}");}
                                }
                                close(MEMBERS);

# end Brad M. Mod

# Check the Restricted UserName file

                                open (FILE,"$memberdir/restrictedmemberlist.dat") || die "I can't open user database\n";
                                while(<FILE>) {
                                chop;
                                @allnames = split(/\n/);
                                $checkusername = $input{'username'};
                                if (grep (/\b^$checkusername\b/i, @allnames) ne "0" ) { error("invalidusername", "", $input{'email'});}
                                }
                                close(FILE);

# end

# Check the For Approval UserName file

                                open (FILE,"$memberdir/forapprovallist.dat") || die "I can't open user database\n";
                                while(<FILE>) {
                                chop;
                                @allnames = split(/\n/);
                                $checkusername = $input{'username'};
                                if (grep (/\b^$checkusername\b/i, @allnames) ne "0" ) { error("existsusername", "", $input{'email'});}
                                }
                                close(FILE);

# end

        srand(time ^ $$);
        my @passset = ('a'..'k', 'm'..'n', 'p'..'z', '2'..'9');
        my $passwrd1 = "";
        for ($i=0; $i<8; $i++) { $passwrd1 .= $passset[int(rand($#passset + 1))]; }

        if ($signupmethod ne "1") {
        $passwrd = crypt($passwrd1, substr($input{'username'}, 0, 2));
        } else {
        $passwrd = crypt($input{'passwrd1'}, substr($input{'username'}, 0, 2));
        }

        if ($signupmethod ne "2") {
        open(FILE, ">$memberdir/$input{'username'}.dat");
        file_lock(FILE);
        print FILE "$passwrd\n";
        print FILE "$input{'username'}\n";
        print FILE "$input{'email'}\n";
        print FILE "\n";
        print FILE "\n";
        print FILE "$input{'username'}\n";
        print FILE "0\n";
        print FILE "Friend\n";
        print FILE "\n";
        print FILE "\n";
        print FILE "$date\n";
        print FILE "0\n";
        print FILE "0\n";
        print FILE "$defaulttheme\n";
        print FILE "Friend\n";
        print FILE "$userlanguage\n";
        print FILE "\n";
        print FILE "\n";
        print FILE "\n";
        print FILE "\n";
        print FILE "\n";
        print FILE "\n";
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$memberdir/$input{'username'}.pref");
        file_lock(FILE);
        print FILE "1\n";
        print FILE "1\n";
        print FILE "1\n";
        print FILE "1\n";
        print FILE "0\n";
        print FILE "\n";
        print FILE "0\n";
        print FILE "1\n";
        unfile_lock(FILE);
        close(FILE);
        }

        if ($signupmethod eq "2") {
        open(FILE, "$memberdir/forapproval.dat");
        file_lock(FILE);
        @pendingmembers = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$memberdir/forapproval.dat");
        file_lock(FILE);
        foreach $curpendingmembers (@pendingmembers) { print FILE "$curpendingmembers"; }
        print FILE "$passwrd1|$passwrd|$input{'username'}|$input{'email'}|$input{'newsletter'}|$userlanguage\n";
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$memberdir/forapprovallist.dat");
        file_lock(FILE);
        @members = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$memberdir/forapprovallist.dat");
        file_lock(FILE);
        foreach $curmem (@members) { print FILE "$curmem"; }
        print FILE "$input{'username'}\n";
        unfile_lock(FILE);
        close(FILE);


# Send IM to Admin that a member needs approving!

        #$msgid = time;
        #$imsubj = "$msg{'422'}";
        #$formatmsg = "$msg{'420'}$input{'username'}$msg{'421'} $msg{'687'}";
        #open (FILE, "$memberdir/admin.msg") || error("$err{'001'} $memberdir/admin.msg");
        #file_lock(FILE); @imessages = <FILE>;
        #unfile_lock(FILE);
        #close (FILE);
        #open (FILE, ">$memberdir/admin.msg") || error("$err{'001'} $memberdir/admin.msg");
        #file_lock(FILE);
        #print FILE "$username|$imsubj|$date|$formatmsg|$msgid\n";

        #foreach $curm (@imessages) { print FILE "$curm"; }
        #unfile_lock(FILE);
        #close(FILE);

        }

        if ($signupmethod ne "2") {
                 if ($welcome_im == 1) {
                  open(FILE, "$datadir/welcomeim.txt");
                  file_lock(FILE);
                  chomp(@lines = <FILE>);
                  unfile_lock(FILE);
                  close(FILE);

                  open(FILE, ">$memberdir/$input{'username'}.msg");
                  file_lock(FILE);
                  print FILE "admin|$lines[0]|$date|$lines[1]|\n";
                  unfile_lock(FILE);
                  close(FILE);
                 }

        open(FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        @members = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$memberdir/memberlist.dat");
        file_lock(FILE);
        foreach $curmem (@members) { print FILE "$curmem"; }
        print FILE "$input{'username'}\n";
        unfile_lock(FILE);
        close(FILE);


        if ($input{'newsletter'}) {
                open(FILE,"$datadir/newsletter/emails.txt");
                @subscribers = <FILE>;
                close(FILE);
                $x=0;
                foreach $subscriber(@subscribers) {chomp($subscriber); if ($input{'email'} eq $subscriber){  $x=1;}}
                if ($x eq 0) {
                        open(FILE, ">>$datadir/newsletter/emails.txt") || (print "Error");
                        file_lock(FILE);
                        print FILE "$input{'email'}\n";
                        unfile_lock(FILE);
                        close(FILE);
                }
        }
        }

        $subject = "$msg{'008'} $pagename";
        if ($signupmethod eq "2") {
        $message = qq~$inf{'021'}~;
        } else {
                if ($signupmethod ne "1") {
                $message = qq~$inf{'002'}
                $msg{'006'} $input{'username'}
                $msg{'009'} $passwrd1~;
                } else {
                $message = qq~$inf{'020'}
                $msg{'006'} $input{'username'}
                $msg{'009'} $input{'passwrd1'}~;
                }
        }
        sendemail($input{'email'}, $subject, $message, $webmaster_email);

        if ($newuser_im eq "1" && $signupmethod ne "2") {
        $msgid = time;
        $imsubj = "$msg{'422'}";
        $formatmsg = "$msg{'420'}$input{'username'}$msg{'421'}";
        open (FILE, "$memberdir/admin.msg") || error("$err{'001'} $memberdir/admin.msg");
        file_lock(FILE); @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);
        open (FILE, ">$memberdir/admin.msg") || error("$err{'001'} $memberdir/admin.msg");
        file_lock(FILE);
        print FILE "$username|$imsubj|$date|$formatmsg|$msgid\n";

        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);
        }

        open(LOG, "$datadir/log.dat");
        file_lock(LOG);
        @entries = <LOG>;
        unfile_lock(LOG);
        close(LOG);

        open(LOG, ">$datadir/log.dat");
        file_lock(LOG);
                                $field="$username";
        foreach $curentry (@entries) {
                $curentry =~ s/\n//g;
                     ($name, $value) = split(/\|/, $curentry);
                if($name ne "$field") {
                        print LOG "$curentry\n";
                }
        }
        unfile_lock(LOG);
        close(LOG);

        print qq~Set-Cookie: $cookieusername=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
        print qq~Set-Cookie: $cookiepassword=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
        print qq~Set-Cookie: $cookieusertheme=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
        print qq~Set-Cookie: $cookieuserlang=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;

        $username = "$anonuser";
        $password = "";
        $usertheme = "$defaulttheme";
        $userlang = $language;
        @settings = ();
        $realname = "";
        $realemail = "";
        $ENV{'HTTP_COOKIE'} = "";
        $user_check_date = $check_date;
        $user_check_time = $timezone;

        logvisitors();
        new_userpage();
}

###########
sub login {
###########

print "Location: $scripturl/$cgi?\&action=\n\n";
exit;

}

############
sub login2 {
############

        error("$err{'003'}") if ($input{'username'} eq "");
        error("$err{'009'}") if ($input{'passwrd'} eq "");
        error("$err{'006'}") if ($input{'username'} !~ /^[0-9A-Za-z#%+,-\.:=?@^_]+$/ || $input{'passwrd'} !~ /^[0-9A-Za-z!@#$%\^&*\(\)_\+|`~\-=\\:;'",\.\/?\[\]\{\}]+$/);

        $returnpage1 = $input{'returnpage1'};
        $returnpage2 = $input{'returnpage2'};
        $returnpage3 = $input{'returnpage3'};
        $returnpage4 = $input{'returnpage4'};
        $returnpage5 = $input{'returnpage5'};
        $returnpage6 = $input{'returnpage6'};
        if ($returnpage1 eq "forum") {if ($returnpage2 eq "") {$returnpage = "forum&board=";}}
        if ($returnpage1 eq "forum") {if ($returnpage2 ne "" && $returnpage5 eq "") {$returnpage = "forum&board=$returnpage2";}}
        if ($returnpage1 eq "forum") {if ($returnpage2 ne "" && $returnpage5 ne "") {$returnpage = "forum&board=$returnpage2&op=display&num=$returnpage5";}}
        if ($returnpage1 eq "links") {if ($returnpage3 eq "") {$returnpage = "links";}
         else {$returnpage = "links&cat=$returnpage3";}}
        if ($returnpage1 eq "downloads") {if ($returnpage3 eq "") {$returnpage = "downloads";}
         else {$returnpage = "downloads&cat=$returnpage3";}}
        if ($returnpage1 eq "topics") {if ($returnpage4 eq "") {$returnpage = "topics";}}
        if ($returnpage1 eq "topics") {if ($returnpage4 ne "") {$returnpage = "topics&viewcat=$returnpage4";}}
        if ($returnpage1 eq "viewnews") {if ($returnpage6 eq "") {$returnpage = "viewnews";}
         else {$returnpage = "viewnews&id=$returnpage6";}}
        if ($returnpage1 eq "logout") {$returnpage = "";}
        if ($returnpage1 eq "register") {$returnpage = "";}


        if (-e("$memberdir/$input{'username'}.dat")) {
                open(FILE, "$memberdir/$input{'username'}.dat");
                file_lock(FILE);
                @settings = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                for( $i = 0; $i < @settings; $i++ ) {
                        $settings[$i] =~ s~[\n\r]~~g;
                }
                $passwrd = crypt($input{'passwrd'}, substr($input{'username'}, 0, 2));
                if ($settings[0] ne $passwrd) { error("$err{'002'}"); }
        }
        else { error("$err{'010'}"); }

     if ($input{'rememberme'}) {

                 print qq~Set-Cookie: $cookieusername=$input{'username'}; path=/; expires=$cookie_expdate;\n~;
                 print qq~Set-Cookie: $cookiepassword=$passwrd; path=/; expires=$cookie_expdate;\n~;
                 print qq~Set-Cookie: $cookieusertheme=$settings[13]; path=/; expires=$cookie_expdate;\n~;
                 print qq~Set-Cookie: $cookieuserlang=$settings[15]; path=/; expires=$cookie_expdate;\n~;

        $username = $input{'username'};
        $password = $passwrd;
        $usertheme = $settings[13];
        $userlang = $settings[15];
        $user_check_date = $settings[25];
        $user_check_time = $settings[26];

        $writedate = $date;
        writelog("Last_Visited");

        loaduser();
        logvisitors();
        welcome($username);
      }
     else {

      print qq~Set-Cookie: $cookieusername=$input{'username'}; path=/; expires=\n~;
                        print qq~Set-Cookie: $cookiepassword=$passwrd; path=/; expires=\n~;
                        print qq~Set-Cookie: $cookieusertheme=$settings[13]; path=/; expires=\n~;
                        print qq~Set-Cookie: $cookieuserlang=$settings[15]; path=/; expires=\n~;

        $username = $input{'username'};
        $password = $passwrd;
        $usertheme = $settings[13];
        $userlang = $settings[15];

        $writedate = $date;
        writelog("Last_Visited");

        loaduser();
        logvisitors();
        welcome($username);

      }

}

############
sub logout {
############

  $writedate = $date;
        writelog("Logged_Off");

                                open(LOG, "$datadir/log.dat");
        file_lock(LOG);
        @entries = <LOG>;
        unfile_lock(LOG);
        close(LOG);

        open(LOG, ">$datadir/log.dat");
        file_lock(LOG);
                                $field="$username";
        foreach $curentry (@entries) {
                $curentry =~ s/\n//g;
                     ($name, $value) = split(/\|/, $curentry);
                if($name ne "$field") {
                        print LOG "$curentry\n";
                }
        }
        unfile_lock(LOG);
        close(LOG);

        print qq~Set-Cookie: $cookieusername=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
        print qq~Set-Cookie: $cookiepassword=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
        print qq~Set-Cookie: $cookieusertheme=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
        print qq~Set-Cookie: $cookieuserlang=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;

        $username = "$anonuser";
        $password = "";
        $usertheme = "$defaulttheme";
        $userlang = $language;
        @settings = ();
        $realname = "";
        $realemail = "";
        $ENV{'HTTP_COOKIE'} = "";

        logvisitors();
        byebye();
}

##############
sub redirect {
##############

        my $username = @_;
        if ($username) { welcome($username); }
        else { print_main(); }
}

##############
sub reminder {
##############

        $navbar = "$btn{'014'} $nav{'015'}";
        print_top();
        print qq~
        <form onSubmit="submitonce(this)" onSubmit="submitonce(this)" method="post" action="$pageurl/$cgi?action=reminder2">
        <table border="0" cellpading="2" cellspacing="1">
        <tr>
        <td>$msg{'006'}</td><td> <input type="text" name="username"></td>
        </tr>
        <tr>
        <td>$msg{'007'}</td><td> <input type="text" name="email"></td>
        </tr>
        <tr>
        <td align"center">
        <input type="submit" class="button" value="$btn{'005'}"></td>
        </tr>
        </table>
        </form>
        ~;

        print_bottom();
        exit;
}

###############
sub reminder2 {
###############
      if ($input{'username'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<+|\%)/) { error("$err{'004'}") }


        if ($input{'username'} eq "") { error ("$err{'003'}"); }
        if ($input{'email'} eq "") { error ("$err{'005'}"); }


        open(FILE, "$memberdir/$input{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@settings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        for ($i = 0; $i < @settings; $i++) { $settings[$i] =~ s~[\n\r]~~g; }
      if ($input{'email'} ne $settings[2]) { error ("$err{'028'}"); }


        srand(time ^ $$);
        my @passset = ('a'..'k', 'm'..'n', 'p'..'z', '2'..'9');
        my $passwrd1 = "";
        for ($i=0; $i<8; $i++) { $passwrd1 .= $passset[int(rand($#passset + 1))]; }

        $newpasswrd = crypt($passwrd1, substr($input{'username'}, 0, 2));

        open(FILE, ">$memberdir/$input{'username'}.dat");
        file_lock(FILE);
        print FILE "$newpasswrd\n";
        for ($i = 1; $i < @settings; $i++) { print FILE "$settings[$i]\n"; }
        unfile_lock(FILE);
        close(FILE);

        $subject = "$pagename - $msg{'010'} $settings[1]";
        $message = qq~$inf{'005'} $ENV{'REMOTE_ADDR'} $inf{'006'} $input{'username'} $inf{'007'}

 $msg{'006'} $input{'username'}
 $msg{'009'} $passwrd1
 $msg{'011'} $settings[7]
 $inf{'008'}
 ~;

        sendemail($settings[2], $subject, $message);

        print_top();
        $navbar = "$btn{'014'} $nav{'015'}";
        print qq~
        $inf{'003'} <b>$settings[2]</b>
        ~;

        print_bottom();
        exit;
}


#############
sub welcome {
#############

        if ($returnpage ne "") {print "Location: $scripturl/$cgi?\&action=$returnpage\n\n"; exit;}

        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

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

        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $umessageid = $info{"messageid"};

        if ($memsettings[9] eq "") { $memsettings[9] = "_nopic.gif"; }
        if ($memsettings[9] =~ /^\http:\/\// ) {
                #if ($memberpic_width ne 0) { $tmp_width = qq~width="60"~; }
                #else { $tmp_width = ""; }
                #if ($memberpic_height ne 0) { $tmp_height = qq~height="100"~; }
                #else { $tmp_height = ""; }
                $memberpic = qq~<img src="$memsettings[9]"></a>~; #$tmp_width $tmp_height border="0" alt=""></a>~;
        }
        else {
                $memberpic = qq~<img src="$imagesurl/avatars/$memsettings[9]" border="0" alt=""></a>~;
        }

        $lastvisited = readlog("Last_Visited");

                censor_it($memsettings[16]);
                censor_it($memsettings[18]);

        myprofile();
}

##############
sub myprofile {
##############

        $navbar = "$btn{'014'} $msg{'305'}$memsettings[1]";
        print_top();

        $about = "$memsettings[16]";
        $about =~ s/\&\&/<br>\n/g;

        print qq~<table cellpadding="3" cellspacing="3" width="100%" border="0"><tr>
        <td colspan="2" class="texttitle">$memsettings[1], $msg{'163'}</td>
        </tr>
        </table>


<table cellpadding="3" cellspacing="3" width="100%" border="0">
<TR><TD VALIGN="Top">

<TABLE cellpadding="2" cellspacing="2" border="0" WIDTH="75%">
  <TR>
    <TD class="forumwindow3">&nbsp; &nbsp;Pick a Task:</TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<a href="$pageurl/$cgi?action=viewprofile&username=$username">$nav{'017'}</a></TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<a href="$pageurl/$cgi?action=editemail&username=$username">Edit E-Mail Address</A></TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<a href="$pageurl/$cgi?action=editpassword&username=$username">Change Password</A></TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<a href="$pageurl/$cgi?action=editprofile2&username=$username">$nav{'161'}</a></TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<a href="$pageurl/$cgi?action=editoptions&username=$username">Member Options</A></TD>
  </TR>

  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<a href="$pageurl/$cgi?action=editsig&username=$username">Edit Signature/Member Pic</A></TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<a href="$cgi?action=im">$nav{'102'} ($mnum)</a></TD>
  </TR>

</TABLE>


</TD><TD VALIGN="Top">
<P ALIGN="RIGHT">

<!-- Start Buddy List table -->

<TABLE BORDER=0 CELLPADDING="2" width=75%>
  <TR>
    <TD class="forumwindow3"><P ALIGN=Left>&nbsp; &nbsp;Buddy List:</TD>
  </TR>
  <TR>
    <TD VALIGN="Top" class="forumwindow1">
<TABLE BORDER=0 CELLPADDING="2">
~;

   ##############################################################
### Hack-Modification by joseedwin 04/29/2003
### This Hack calls up a subroutine in the /user-lib/buddylist.pl file

require "$scriptdir/user-lib/buddylist.pl";
blist();

### End Hack
##############################################################

  print qq~

</TABLE>
</TD>
  </TR>
  <TR>
    <TD class="forumwindow3">
<P ALIGN="RIGHT">
<a href="$cgi?action=memberlist"><img src="$imagesurl/buddy/guest.gif" border=0 alt="$bud{'009'}"></a>
&nbsp;<a href="$cgi?action=blistedit"><img src="$imagesurl/forum/modify.gif" alt="$bud{'006'}" border=0></a>

</TD>
  </TR>
</TABLE>
<br>

<!-- End Buddy List table -->
</TD>
</TR>
</TABLE>

<HR>
<table cellpadding="3" cellspacing="3" width="100%" border="0"><tr>
        <td colspan="2" class="texttitle">About $memsettings[1].</td>
        </tr>
        </table>

<table cellpadding="3" cellspacing="3" width="100%" border="0">
<TD valign="top">

        <table cellpadding="0" cellspacing="0" width="100%" border="0">

<tr>
        <td width="30%" align="center">$memberpic</td>

        <td width="70%" valign="top">


        <table cellpadding="2" cellspacing="2" border="0" WIDTH=100%><tr>
        <td class="forumwindow3" width="25%">$msg{'013'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[1]</td>
        </tr><tr>
        <td class="forumwindow3" width="25%">$msg{'650'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[22]</td>
        </tr><tr>
        <td class="forumwindow3" width="25%">$msg{'651'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[17]</td>
        </tr><tr>
        <td class="forumwindow3" width="25%">$msg{'652'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[19]</td>
        </tr><tr>
        <td class="forumwindow3" width="25%">$msg{'653'}</td>
        <td class="forumwindow1" nowrap>$memsettings[21]</td>
        </tr><tr>
        <td class="forumwindow3" width="25%">$msg{'654'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[20]</td>
        </tr><tr>
        <td class="forumwindow3" width="25%">$msg{'014'}</td>
        <td class="forumwindow1" width="75%" nowrap><a href="$memsettings[4]" target="_blank">$memsettings[3]</a></td>
        </tr>

        <tr>
        <td class="forumwindow3" width="25%">$msg{'024'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[7]</td>
        </tr>
        <tr>
        <td class="forumwindow3" width="25%">$msg{'178'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[14]</td>
        </tr>
        <tr>
        <td class="forumwindow3" width="25%">$msg{'021'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[6]</td>
        </tr>
        <tr>
        <td class="forumwindow3" width="25%">$msg{'022'}</td>
        <td class="forumwindow1" width="75%" nowrap>$memsettings[11]</td>
        </tr>

        </table>


</TD>

</TR>
<TR>

<TD COLSPAN=2 VALIGN="Top" height="100%">

        <table cellpadding="3" cellspacing="3" width="100%" border="0"><tr>
        <td class="forumwindow3" valign="top" width="25%">$msg{'655'}</td>
        <td class="forumwindow1" valign="top" width="75%">$about</font></td></tr><tr>
        <td class="forumwindow3" valign="top" width="25%">$msg{'656'}</td>
        <td class="forumwindow1" valign="top" width="75%">$memsettings[18]</td></tr><tr>
        </tr></table></td>

</td>
</TR>


</table>

</TD>
  </TR>
</TABLE>

<CENTER>
~;

if ($memsettings[24] ne "") {
print qq~
<IFRAME frameborder=2 style="height:600;width:800;scrolling:;" class=iframe name=cwindow src='$memsettings[24]'></IFRAME>
<A HREF=http://www.magelo.com TARGET=_new>Magelo Profile</A>
~;
}

print qq~
</CENTER>

<br>~;




print_bottom();
}

############
sub byebye {
############
        $navbar = "$btn{'014'} $msg{'411'}";
        print_top();
        print qq~$inf{'017'}
        <a href="$pageurl/$cgi">$nav{'052'}</a>~;
        print_bottom();
        exit;
}

#################
sub new_userpage {
#################

        if ($signupmethod eq "") {$signupmethod ="0";}

        $navbar = "$btn{'014'} $msg{'008'}&nbsp;$pagename.";
        print_top();
        print qq~
        <table border="0" cellspacing="1">
        <tr>~;
        if ($signupmethod eq "2") {
        print qq~<td>$inf{'022'} <b>$input{'email'}</b></td>~;
        } else {
                if ($signupmethod eq "1") {
                print qq~<form onSubmit="submitonce(this)" action="$pageurl/$cgi?action=login2" method="post">
                <input type="hidden" name="username" value="$input{'username'}">
                <input type="hidden" name="passwrd" value="$input{'passwrd1'}">
                <input type="hidden" name="rememberme" value="on">
                <td class="articlecattitle">
                &nbsp;$msg{'577'} $input{'username'}. $msg{'578'}<br><br>
                &nbsp;<input type="submit" class="button" value="$btn{'017'}"><br>
                </form>
                </td>~;
                } else {
                print qq~<td>
                $inf{'003'} <b>$input{'email'}</b><br>
                $inf{'004'}
                </td>~;
                }
        }
        print qq~</tr>
        </table>~;

        print_bottom();
        exit;

}

#################
sub editprofile { # My Profile View!
#################

welcome($username);

}

#################
sub editsig {
#################
  if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }
        if ($username ne $info{'username'}) { error("$err{'011'}" ); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$memsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$memsettings[16]";
        $about =~ s/\&\&/\n/g;

        $navbar = "$btn{'014'} $nav{'161'}";
        print_top();

        print qq~

<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=editprofile3" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Edit Signature</td>


<input type="hidden" name="passwrd1" size="20" value="$memsettings[0]">
<input type="hidden" name="passwrd2" size="20" value="$memsettings[0]">
<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="rememberme" value="1">
<input type="hidden" name="email" size="40" value="$memsettings[2]">
<input type="hidden" name="name" size="40" value="$memsettings[1]">
<input type="hidden" name="websitetitle" size="40" value="$memsettings[3]">
<input type="hidden" name="websiteurl" size="40" value="$memsettings[4]">
<input type="hidden" name="icq" size="40" value="$memsettings[8]">
<input type="hidden" name="aim" size="40" value="$memsettings[23]">
<input type="hidden" name="yahoo" size="40" value="$memsettings[24]">
<input type="hidden" name="gen" value="$memsettings[22]">
<input type="hidden" name="ages" value="$memsettings[17]">
<input type="hidden" name="marstat" value="$memsettings[20]">
<input type="hidden" name="about" value="$about">
<input type="hidden" name="state" value="$memsettings[19]">
<input type="hidden" name="profession" value="$memsettings[21]">
<input type="hidden" name="fav" value="$memsettings[18]">
~;

$signature =~ s/"//gi;

print qq~

<TR>
<td valign="top" class="formstextnormal" width="30%">$msg{'017'}</td>
<td width="70%"><textarea name="signature" rows="6" cols="50" wrap="virtual">$signature</TEXTAREA></td>
</tr>



<input type="hidden" name="language" value="$memsettings[15]">
<input type="hidden" name="theme" value="$memsettings[13]">
<input type="hidden" name="user_check_date" value="$memsettings[25]">
<input type="hidden" name="user_check_time" value="$memsettings[26]">


<TR>
<td class="formstexttitle" colspan="2"></td>
</TR>
<TR>
<td class="formstexttitle" colspan="2">Edit Member Pic</td>
</TR>
~;


        opendir(DIR, "$imagesdir/avatars");
        @contents = readdir(DIR);
        closedir(DIR);

        $images = "";
        if ($memsettings[9] eq "") { $memsettings[9] = "_nopic.gif"; }
        foreach $line (sort @contents) {
                ($name, $extension) = split (/\./, $line);
                $checked = "";
                if ($line eq $memsettings[9]) { $checked = " selected"; }
                if ($memsettings[9] =~ m~\Ahttp://~ && $line eq "") { $checked = " selected"; }
                if ($extension =~ /gif/i || $extension =~ /jpg/i || $extension =~ /jpeg/i || $extension =~ /png/i ) {
                        if ($line eq "_nopic.gif") {
                                $name = "";
                                $pic = "_nopic.gif";
                        }
                        $images .= qq~<option value="$line"$checked>$name</option>\n~;
                }
        }
        if ($memsettings[9] =~ m~\Ahttp://~) {
                $pic = "$memsettings[9]";
                $checked = " checked";
                $tmp = $memsettings[9];
        }
        else {
                $pic = "$imagesurl/avatars/$memsettings[9]";
                $tmp = "http://";
        }
        print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'018'}</td>
<td class="formstext" width="70%">$msg{'012'}</td>
</tr>
<tr>
<td width="30%">&nbsp;</td>
<td width="70%"><script language="javascript" type="text/javascript">
<!--
function showImage() {
document.images.avatars.src="$imagesurl/avatars/"+document.creator.memberpic.options[document.creator.memberpic.selectedIndex].value;
}
// -->
</script>
<select name="memberpic" onChange="showImage()" size="6">
$images</select>&nbsp;
<img src="$pic" name="avatars" border="0" hspace="15"></td>
</tr>
<tr>
<td width="30%">&nbsp;</td>
<td class="formstext" width="70%">$msg{'020'}</td>
</tr>
<tr>
<td width="30%">&nbsp;</td>
<td class="formstext" width="70%"><input type="checkbox" name="memberpicpersonalcheck"$checked>&nbsp;
<input type="text" name="memberpicpersonal" size="40" value="$tmp"><br>
$msg{'019'}</td>
</tr>~;


if ($memsettings[7] eq "Administrator") {

print qq~
<input type="hidden" name="settings14" value="$memsettings[14]">
<input type="hidden" name="settings7" value="$memsettings[7]">
~;

}

        open(FILE, "$memberdir/$info{'username'}.pref") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@preferences = <FILE>);
        unfile_lock(FILE);
        close(FILE);

if ($preferences[0] eq "1") { $checked0 = "on"; }
else { $checked0 = ""; }
if ($preferences[1] eq "1") { $checked1 = "on"; }
else { $checked1 = ""; }
if ($preferences[2] eq "1") { $checked2 = "on"; }
else { $checked2 = ""; }
if ($preferences[3] eq "1") { $checked3 = "on"; }
else { $checked3 = ""; }
if ($preferences[4] eq "1") { $checked4 = "on"; }
else { $checked4 = ""; }
if ($preferences[7] eq "1") { $checked7 = "on"; }
else { $checked7 = ""; }


print qq~
<input type="hidden" name="impopup" value="$checked0">
<input type="hidden" name="infoblock" value="$checked1">
<input type="hidden" name="freeadblock" value="$checked2">
<input type="hidden" name="welcomemessage" value="$checked3">
<input type="hidden" name="showlegend" value="$checked7">

~;


if ($memsettings[7] eq "Administrator") {
print qq~

<input type="hidden" name="broadcastmessage" value="$checked4">
<input type="hidden" name="saybroadcast" value="$preferences[5]">

~;
}


print qq~
<tr>
<td colspan="2">&nbsp;</td>
</tr>

<tr>
<td colspan="2">

<input type="hidden" name="settings6" value="$memsettings[6]">
<input type="hidden" name="settings7" value="$memsettings[7]">
<input type="hidden" name="settings8" value="$memsettings[8]">
<input type="hidden" name="settings10" value="$memsettings[10]">
<input type="hidden" name="settings11" value="$memsettings[11]">
<input type="hidden" name="settings12" value="$memsettings[12]">
<input type="hidden" name="preferences[6]" value="$preferences[6]">

<input type="submit" class="button" name="moda" value="$btn{'047'}">&nbsp;&nbsp;~;


print qq~
</td>
</tr>
</form>
<tr>
<td colspan="2">&nbsp;</td>
</tr>~;



print qq~
</table>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}




#################
sub editemail {
#################
  if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }
        if ($username ne $info{'username'}) { error("$err{'011'}" ); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$memsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$memsettings[16]";
        $about =~ s/\&\&/\n/g;

        $navbar = "$btn{'014'} $nav{'161'}";
        print_top();

        print qq~

<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=editprofile3" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Edit E-Mail Address</td>

<tr>
<td class="formstextnormal" width="30%">$msg{'007'}</td>
<td class="formstext" width="70%">
<input type="text" name="email" size="40" value="$memsettings[2]">
</td>
</tr>

<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="rememberme" value="1">
<input type="hidden" name="passwrd1" size="20" value="$memsettings[0]">
<input type="hidden" name="passwrd2" size="20" value="$memsettings[0]">
<input type="hidden" name="name" size="40" value="$memsettings[1]">
<input type="hidden" name="websitetitle" size="40" value="$memsettings[3]">
<input type="hidden" name="websiteurl" size="40" value="$memsettings[4]">
<input type="hidden" name="icq" size="40" value="$memsettings[8]">
<input type="hidden" name="aim" size="40" value="$memsettings[23]">
<input type="hidden" name="yahoo" size="40" value="$memsettings[24]">
<input type="hidden" name="gen" value="$memsettings[22]">
<input type="hidden" name="ages" value="$memsettings[17]">
<input type="hidden" name="marstat" value="$memsettings[20]">
<input type="hidden" name="about" value="$about">
<input type="hidden" name="state" value="$memsettings[19]">
<input type="hidden" name="profession" value="$memsettings[21]">
<input type="hidden" name="fav" value="$memsettings[18]">
~;

$signature =~ s/"//gi;

print qq~
<input type="hidden" name="signature" value="$signature">
<input type="hidden" name="language" value="$memsettings[15]">
<input type="hidden" name="theme" value="$memsettings[13]">
<input type="hidden" name="user_check_date" value="$memsettings[25]">
<input type="hidden" name="user_check_time" value="$memsettings[26]">
<input type="hidden" name="memberpic" value="$memsettings[9]">

~;

if ($memsettings[7] eq "Administrator") {

print qq~
<input type="hidden" name="settings14" value="$memsettings[14]">
<input type="hidden" name="settings7" value="$memsettings[7]">
~;

}

        open(FILE, "$memberdir/$info{'username'}.pref") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@preferences = <FILE>);
        unfile_lock(FILE);
        close(FILE);

if ($preferences[0] eq "1") { $checked0 = "on"; }
else { $checked0 = ""; }
if ($preferences[1] eq "1") { $checked1 = "on"; }
else { $checked1 = ""; }
if ($preferences[2] eq "1") { $checked2 = "on"; }
else { $checked2 = ""; }
if ($preferences[3] eq "1") { $checked3 = "on"; }
else { $checked3 = ""; }
if ($preferences[4] eq "1") { $checked4 = "on"; }
else { $checked4 = ""; }
if ($preferences[7] eq "1") { $checked7 = "on"; }
else { $checked7 = ""; }

print qq~
<input type="hidden" name="impopup" value="$checked0">
<input type="hidden" name="infoblock" value="$checked1">
<input type="hidden" name="freeadblock" value="$checked2">
<input type="hidden" name="welcomemessage" value="$checked3">
<input type="hidden" name="showlegend" value="$checked7">

~;


if ($memsettings[7] eq "Administrator") {
print qq~

<input type="hidden" name="broadcastmessage" value="$checked4">
<input type="hidden" name="saybroadcast" value="$preferences[5]">

~;
}


print qq~
<tr>
<td colspan="2">&nbsp;</td>
</tr>

<tr>
<td colspan="2">

<input type="hidden" name="settings6" value="$memsettings[6]">
<input type="hidden" name="settings7" value="$memsettings[7]">
<input type="hidden" name="settings8" value="$memsettings[8]">
<input type="hidden" name="settings10" value="$memsettings[10]">
<input type="hidden" name="settings11" value="$memsettings[11]">
<input type="hidden" name="settings12" value="$memsettings[12]">
<input type="hidden" name="preferences[6]" value="$preferences[6]">

<input type="submit" class="button" name="moda" value="$btn{'047'}">&nbsp;&nbsp;~;

print qq~
</td>
</tr>
</form>
<tr>
<td colspan="2">&nbsp;</td>
</tr>~;



print qq~
</table>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}


#################
sub editprofile2 {
#################
  if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }
        if ($username ne $info{'username'}) { error("$err{'011'}" ); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$memsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$memsettings[16]";
        $about =~ s/\&\&/\n/g;

        $navbar = "$btn{'014'} $nav{'161'}";
        print_top();

        print qq~
<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=editprofile3" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">$nav{'161'}</td>
</tr>

<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="rememberme" value="1">
<input type="hidden" name="passwrd1" size="20" value="$memsettings[0]">
<input type="hidden" name="passwrd2" size="20" value="$memsettings[0]">
<input type="hidden" name="email" size="40" value="$memsettings[2]">
<input type="hidden" name="language" value="$memsettings[15]">
<input type="hidden" name="theme" value="$memsettings[13]">
<input type="hidden" name="user_check_date" value="$memsettings[25]">
<input type="hidden" name="user_check_time" value="$memsettings[26]">
<input type="hidden" name="memberpic" value="$memsettings[9]">
<input type="hidden" name="yahoo" size="40" value="$memsettings[24]">

~;

if ($memsettings[7] eq "Administrator") {

print qq~
<input type="hidden" name="settings14" value="$memsettings[14]">
<input type="hidden" name="settings7" value="$memsettings[7]">


~;

}

        open(FILE, "$memberdir/$info{'username'}.pref") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@preferences = <FILE>);
        unfile_lock(FILE);
        close(FILE);

if ($preferences[0] eq "1") { $checked0 = "on"; }
else { $checked0 = ""; }
if ($preferences[1] eq "1") { $checked1 = "on"; }
else { $checked1 = ""; }
if ($preferences[2] eq "1") { $checked2 = "on"; }
else { $checked2 = ""; }
if ($preferences[3] eq "1") { $checked3 = "on"; }
else { $checked3 = ""; }
if ($preferences[4] eq "1") { $checked4 = "on"; }
else { $checked4 = ""; }
if ($preferences[7] eq "1") { $checked7 = "on"; }
else { $checked7 = ""; }


print qq~
<input type="hidden" name="impopup" value="$checked0">
<input type="hidden" name="infoblock" value="$checked1">
<input type="hidden" name="freeadblock" value="$checked2">
<input type="hidden" name="welcomemessage" value="$checked3">
<input type="hidden" name="showlegend" value="$checked7">

~;

if ($memsettings[7] eq "Administrator") {

print qq~
<input type="hidden" name="broadcastmessage" value="$checked4">
<input type="hidden" name="saybroadcast" value="$preferences[5]">
~;
}


$signature =~ s/"//gi;

print qq~
<input type="hidden" name="signature" value="$signature">

<tr>
<td class="formstextnormal" width="30%">$msg{'011'}</td>
<td class="formstext" width="70%">$memsettings[14]</td>
</tr>
~;

print qq~


<tr>
<td class="formstextnormal" width="30%">$msg{'013'}</td>
<td class="formstext" width="70%"><input type="text" name="name" size="40" value="$memsettings[1]">*</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'014'}</td>
<td width="70%"><input type="text" name="websitetitle" size="40" value="$memsettings[3]"></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'015'}</td>
<td width="70%"><input type="text" name="websiteurl" size="40" value="$memsettings[4]"></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'016'}</td>
<td width="70%"><input type="text" name="icq" size="40" value="$memsettings[8]"></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'661'}:</td>
<td width="70%"><input type="text" name="aim" size="40" value="$memsettings[23]"></td>
</tr>
~;
print qq~
<tr>
<td class="formstextnormal" width="30%">$msg{'650'}:</td>
<td width="70%"><select name="gen">
~;
     open(FILE, "$memberdir/prodata/gen.dat" );
     file_lock(FILE);
     @gen = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@gen) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($memsettings[22] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option>\n~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>\n~; }
                                         }
           }
     print qq~</select>
</td>
</tr>
<tr>
~;
print qq~
<tr>
<td class="formstextnormal" width="30%">$msg{'651'}:</td>
<td width="70%"><select name="ages">
~;
     open(FILE, "$memberdir/prodata/ages.dat" );
     file_lock(FILE);
     @ages = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@ages) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($memsettings[17] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option>\n~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>\n~; }
                                         }
           }
     print qq~</select>
</td>
</tr>
<tr>
~;
print qq~
<tr>
<td class="formstextnormal" width="30%">$msg{'654'}:</td>
<td width="70%"><select name="marstat">
~;
     open(FILE, "$memberdir/prodata/marstat.dat" );
     file_lock(FILE);
     @mar = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@mar) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($memsettings[20] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option>\n~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>\n~; }
                                         }
           }
     print qq~</select>
</td>
</tr>

<tr>
<td class="formstextnormal" width="30%">$msg{'653'}:</td>
<td width="70%"><select name="profession">
~;
     open(FILE, "$memberdir/prodata/profession.dat" );
     file_lock(FILE);
     @prof = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@prof) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($memsettings[21] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option>\n~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>\n~; }
                                         }
           }
     print qq~</select>
</td>
</tr>


<tr>
<td class="formstextnormal" width="30%">$msg{'652'}:</td>
<td width="70%"><select name="state">
~;
     open(FILE, "$memberdir/prodata/states.dat" );
     file_lock(FILE);
     @states = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@states) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($memsettings[19] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option>\n~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>\n~; }
                                         }
           }
     print qq~</select>
</td>
</tr>
<tr>
~;

print qq~
<tr>
<td class="formstextnormal" width="30%" valign="top"><b>$msg{'655'}:</b></td>
<td class="formstextnormal" width="70%"><textarea name="about" rows="4" cols="35" maxlength="50" wrap="virtual">$about</TEXTAREA></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'656'}:</td>
<td><input type="text" name="fav" size="40" maxlength="200" value="$memsettings[18]"></td>
</tr>
</tr>

</tr>~;



print qq~
<tr>
<td colspan="2">&nbsp;</td>
</tr>
<tr>
<td colspan="2" class="formstextsmall" width="30%">* $msg{'025'}</td>
</tr>
<tr>
<td colspan="2">
<input type="hidden" name="settings6" value="$memsettings[6]">
<input type="hidden" name="settings7" value="$memsettings[7]">
<input type="hidden" name="settings8" value="$memsettings[8]">
<input type="hidden" name="settings10" value="$memsettings[10]">
<input type="hidden" name="settings11" value="$memsettings[11]">
<input type="hidden" name="settings12" value="$memsettings[12]">
<input type="hidden" name="preferences[6]" value="$preferences[6]">
<input type="submit" class="button" name="moda" value="$btn{'047'}">

</td>
</tr>
</form>
<tr>
<td colspan="2">&nbsp;</td>
</tr>~;

if (($modulenl eq "1") || ($modulenlmem eq "1")) {
        $found= 0 ;
        open(FILE,"$datadir/newsletter/emails.txt");
        @addresses=<FILE>;
        close(FILE);
        foreach $check (@addresses) {
                chomp($check);
        $check =~ tr/A-Z/a-z/;
        $usermail = $memsettings[2];
        $usermail =~ tr/A-Z/a-z/;
                if ($usermail eq $check){$found=1; $checkunsub="checked";}
    }
        if ($found eq 1){
                print qq~
                <tr>
            <td width="30%">&nbsp;</td>
            <td width="70%"><B>$msg{'173'}</B></td>
                </tr>~;
        } else {
                print qq~
                <tr>
            <td width="30%">&nbsp;</td>
            <td width="70%"><B>$msg{'174'}</B></td>
                </tr>~;
        }
        print qq~
</table>
</form>

<form onSubmit="submitonce(this)" action="$pageurl/$cgi?action=subscribe" method="POST">
        <TABLE border="0">
        <TR>
                <td width="30%">&nbsp;</td>
                <td width="70%">
                                $msg{'176'} <INPUT TYPE=radio NAME=action VALUE=subscribe CHECKED> |
                $msg{'177'} <INPUT TYPE=radio NAME=action VALUE=remove $checkunsub>
                                <input type="text" name="joinnl" value="$memsettings[2]" size="16" class="text">
                                <input type="submit" class="button" value="$btn{'015'}">
                </TD>
        </TR>
        </TABLE>
</form>

        ~;
}

print qq~
</table>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}


#################
sub editpassword {
#################
  if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }
        if ($username ne $info{'username'}) { error("$err{'011'}" ); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$memsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$memsettings[16]";
        $about =~ s/\&\&/\n/g;

        $navbar = "$btn{'014'} $nav{'161'}";
        print_top();

        print qq~

<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=editprofile3" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Change Password</td>


<tr>
<td class="formstextnormal" width="30%">$msg{'009'}</td>
<td class="formstext" width="70%"><input type="password" name="passwrd1" size="20" value="$memsettings[0]"></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'537'}</td>
<td class="formstext" width="70%"><input type="password" name="passwrd2" size="20" value="$memsettings[0]"></td>
</tr>

<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="rememberme" value="1">
<input type="hidden" name="email" size="40" value="$memsettings[2]">
<input type="hidden" name="name" size="40" value="$memsettings[1]">
<input type="hidden" name="websitetitle" size="40" value="$memsettings[3]">
<input type="hidden" name="websiteurl" size="40" value="$memsettings[4]">
<input type="hidden" name="icq" size="40" value="$memsettings[8]">
<input type="hidden" name="aim" size="40" value="$memsettings[23]">
<input type="hidden" name="yahoo" size="40" value="$memsettings[24]">
<input type="hidden" name="gen" value="$memsettings[22]">
<input type="hidden" name="ages" value="$memsettings[17]">
<input type="hidden" name="marstat" value="$memsettings[20]">
<input type="hidden" name="about" value="$about">
<input type="hidden" name="state" value="$memsettings[19]">
<input type="hidden" name="profession" value="$memsettings[21]">
<input type="hidden" name="fav" value="$memsettings[18]">
~;

$signature =~ s/"//gi;

print qq~
<input type="hidden" name="signature" value="$signature">
<input type="hidden" name="language" value="$memsettings[15]">
<input type="hidden" name="theme" value="$memsettings[13]">
<input type="hidden" name="user_check_date" value="$memsettings[25]">
<input type="hidden" name="user_check_time" value="$memsettings[26]">
<input type="hidden" name="memberpic" value="$memsettings[9]">

~;

if ($memsettings[7] eq "Administrator") {

print qq~
<input type="hidden" name="settings14" value="$memsettings[14]">
<input type="hidden" name="settings7" value="$memsettings[7]">
~;

}

        open(FILE, "$memberdir/$info{'username'}.pref") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@preferences = <FILE>);
        unfile_lock(FILE);
        close(FILE);

if ($preferences[0] eq "1") { $checked0 = "on"; }
else { $checked0 = ""; }
if ($preferences[1] eq "1") { $checked1 = "on"; }
else { $checked1 = ""; }
if ($preferences[2] eq "1") { $checked2 = "on"; }
else { $checked2 = ""; }
if ($preferences[3] eq "1") { $checked3 = "on"; }
else { $checked3 = ""; }
if ($preferences[4] eq "1") { $checked4 = "on"; }
else { $checked4 = ""; }
if ($preferences[7] eq "1") { $checked7 = "on"; }
else { $checked7 = ""; }

print qq~
<input type="hidden" name="impopup" value="$checked0">
<input type="hidden" name="infoblock" value="$checked1">
<input type="hidden" name="freeadblock" value="$checked2">
<input type="hidden" name="welcomemessage" value="$checked3">
<input type="hidden" name="showlegend" value="$checked7">

~;


if ($memsettings[7] eq "Administrator") {
print qq~

<input type="hidden" name="broadcastmessage" value="$checked4">
<input type="hidden" name="saybroadcast" value="$preferences[5]">

~;
}


print qq~
<tr>
<td colspan="2">&nbsp;</td>
</tr>

<tr>
<td colspan="2">

<input type="hidden" name="settings6" value="$memsettings[6]">
<input type="hidden" name="settings7" value="$memsettings[7]">
<input type="hidden" name="settings8" value="$memsettings[8]">
<input type="hidden" name="settings10" value="$memsettings[10]">
<input type="hidden" name="settings11" value="$memsettings[11]">
<input type="hidden" name="settings12" value="$memsettings[12]">
<input type="hidden" name="preferences[6]" value="$preferences[6]">

<input type="submit" class="button" name="moda" value="$btn{'047'}">&nbsp;&nbsp;~;


print qq~
</td>
</tr>
</form>
<tr>
<td colspan="2">&nbsp;</td>
</tr>~;



print qq~
</table>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}


#################
sub editoptions {
#################
  if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }
        if ($username ne $info{'username'}) { error("$err{'011'}" ); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$memsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$memsettings[16]";
        $about =~ s/\&\&/\n/g;

        $navbar = "$btn{'014'} $nav{'161'}";
        print_top();

        print qq~

<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=editprofile3" method="post" name="creator">
<table border="0">
~;

if ($letmemlng eq "1") {

print qq~
<tr>
<td class="formstexttitle" colspan="2">Language Settings</td>
</TR>
<tr>
<td class="formstextnormal" width="30%">$msg{'412'}</td>
<td width="70%"><select name="language">
~;
     open(FILE, "$scriptdir/lang/languages.dat" );
     file_lock(FILE);
     @lang = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@lang) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($memsettings[15] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option>\n~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>\n~; }
                                         }
           }
     print qq~</select>
</td>
</tr>
<tr>
<td colspan="2">&nbsp;</td>
</tr>
~; }



if ($letmemthm eq "1") {print qq~
<tr>
<td class="formstexttitle" colspan="2">Theme Settings</td>
</TR>
<tr>
<td class="formstextnormal" width="30%">$msg{'161'}</td>
<td width="70%"><select name="theme">
~;
     open(FILE, "$themesdir/themes.dat" );
     file_lock(FILE);
     @themes = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@themes) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($memsettings[13] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option><br>~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option><br>~; }
                                         }
                                         }
     print qq~</select>
</td>
</tr>
<tr>
<td colspan="2">&nbsp;</td>
</tr>
~; }

print qq~
<tr>
<td class="formstexttitle" colspan="2">Time Settings</td>


<input type="hidden" name="passwrd1" size="20" value="$memsettings[0]">
<input type="hidden" name="passwrd2" size="20" value="$memsettings[0]">
<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="rememberme" value="1">
<input type="hidden" name="email" size="40" value="$memsettings[2]">
<input type="hidden" name="name" size="40" value="$memsettings[1]">
<input type="hidden" name="websitetitle" size="40" value="$memsettings[3]">
<input type="hidden" name="websiteurl" size="40" value="$memsettings[4]">
<input type="hidden" name="icq" size="40" value="$memsettings[8]">
<input type="hidden" name="aim" size="40" value="$memsettings[23]">
<input type="hidden" name="yahoo" size="40" value="$memsettings[24]">
<input type="hidden" name="gen" value="$memsettings[22]">
<input type="hidden" name="ages" value="$memsettings[17]">
<input type="hidden" name="marstat" value="$memsettings[20]">
<input type="hidden" name="about" value="$about">
<input type="hidden" name="state" value="$memsettings[19]">
<input type="hidden" name="profession" value="$memsettings[21]">
<input type="hidden" name="fav" value="$memsettings[18]">
~;

$signature =~ s/"//gi;

print qq~

<input type="hidden" name="signature" value="$signature">
<input type="hidden" name="memberpic" value="$memsettings[9]">


~;


print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'664'}</td>
<td width="70%">~;

# For backwards compatability
if ($memsettings[25] eq "") { print qq~
<select name="user_check_date">
<option selected value="american">$msg{'555'}</option>
<option value="european">$msg{'556'}</option>~;
}
if ($memsettings[25] eq "american") { print qq~
<select name="user_check_date">
<option selected value="american">$msg{'555'}</option>
<option value="european">$msg{'556'}</option>~;
}
if ($memsettings[25] eq "european") { print qq~
<select name="user_check_date">
<option selected value="european">$msg{'556'}</option>
<option value="american">$msg{'555'}</option>~;
}

print qq~</select>
</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'663'}</td>
<td width="70%"><select name="user_check_time">~;

                        open (ZONES,"<$datadir/timezones.dat") || error("$err{'016'} $datadir/timezones.dat");
      @timezones=<ZONES>;
      close (ZONES);

                        if ($memsettings[26] eq "") { $memsettings[26] = $timezone; }

                        foreach $zone (@timezones) {
                                                $zone =~ s/[\n\r]//g;
                                                @zitem = split(/\|/, $zone);

                                                if ($zitem[0] eq $memsettings[26]) {print qq~<option value="$zitem[0]" selected>$zitem[2] $zitem[3]: $zitem[5]</option>~;} else {print qq~<option value="$zitem[0]">$zitem[2] $zitem[3]: $zitem[5]</option>~;}
                        }

print qq~
</select>
</td>
</tr>

<input type="hidden" name="settings14" value="$memsettings[14]">
<input type="hidden" name="settings7" value="$memsettings[7]">
~;


        open(FILE, "$memberdir/$info{'username'}.pref") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@preferences = <FILE>);
        unfile_lock(FILE);
        close(FILE);





        if ($preferences[0] eq "1") {$checked0 = "checked";
        } else {$checked0 = "";}
        if ($preferences[1] eq "1") {$checked1 = "checked";
        } else {$checked1 = "";}
        if ($preferences[2] eq "1") {$checked2 = "checked";
        } else {$checked2 = "";}
        if ($preferences[3] eq "1") {$checked3 = "checked";
        } else {$checked3 = "";}
        if ($preferences[4] eq "1") {$checked4 = "checked";
        } else {$checked4 = "";}
        if ($preferences[7] eq "1") {$checked7 = "checked";
        } else {$checked7 = "";}

print qq~
<tr>
<td colspan="2">&nbsp;</td>
</tr>
<tr>
<td class="formstexttitle" colspan="2">$nav{'088'}</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'413'}</td>
<td width="70%"><input type="checkbox" name="impopup"$checked0></td>
</tr>~;

if ($infoblockmod eq 1) {print qq~
<tr>
<td class="formstextnormal" width="30%">$msg{'414'}</td>
<td width="70%"><input type="checkbox" name="infoblock"$checked1></td>
</tr>~;
}

if ($dispfrad eq 1) {print qq~
<tr>
<td class="formstextnormal" width="30%">$msg{'416'}</td>
<td width="70%"><input type="checkbox" name="freeadblock"$checked2></td>
</tr>~;
}
print qq~


</td>
</tr>~;


print qq~
<tr>
<td colspan="2">&nbsp;</td>
</tr>

<tr>
<td colspan="2">

<input type="hidden" name="broadcastmessage" value="$checked4">
<input type="hidden" name="saybroadcast" value="$preferences[5]">

<input type="hidden" name="showlegend" value="on">
<input type="hidden" name="welcomemessage" value="on">

<input type="hidden" name="settings6" value="$memsettings[6]">
<input type="hidden" name="settings7" value="$memsettings[7]">
<input type="hidden" name="settings8" value="$memsettings[8]">
<input type="hidden" name="settings10" value="$memsettings[10]">
<input type="hidden" name="settings11" value="$memsettings[11]">
<input type="hidden" name="settings12" value="$memsettings[12]">
<input type="hidden" name="preferences[6]" value="$preferences[6]">

<input type="submit" class="button" name="moda" value="$btn{'047'}">&nbsp;&nbsp;~;

if ($letmemdel eq "1" && $info{'username'} ne "admin") {

print qq~
<input type="submit" class="button" name="delt" value="$btn{'007'}">

~;

}
print qq~
</td>
</tr>
</form>
<tr>
<td colspan="2">&nbsp;</td>
</tr>~;



print qq~
</table>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}

##################
sub editprofile3 {
##################
        if ($info{'username'} =~ /\//) { error("$err{'004'}" ); }
        if ($input{'passwrd1'} ne "$input{'passwrd2'}") { error("$err{'012'}"); }
        if ($input{'passwrd1'} eq "") { error("$err{'009'}"); }
        if ($input{'name'} eq "") { error("$err{'013'}"); }
        if ($input{'name'} !~ /^[0-9A-Za-z#%+,-\.:=?@^_ ]+$/ || $input{'name'} eq "|" || $input{'name'} =~ /$anonuser/i) { error("$err{'006'}"); }
        if ($input{'email'} eq "") { error("$err{'005'}"); }
        if ($input{'theme'} eq "") { $input{'theme'} = "$defauttheme"; }
        if ($input{'language'} eq "") { $input{'language'} = "$language"; }

        if ($input{'impopup'} eq "on") { $input{'impopup'} = "1";
        } else { $input{'impopup'} = "0"; }
        if ($input{'infoblock'} eq "on") { $input{'infoblock'} = "1";
        } else { $input{'infoblock'} = "0"; }
        if ($input{'freeadblock'} eq "on") { $input{'freeadblock'} = "1";
        } else { $input{'freeadblock'} = "0"; }
        if ($input{'welcomemessage'} eq "on") { $input{'welcomemessage'} = "1";
        } else { $input{'welcomemessage'} = "0"; }
        if ($input{'showlegend'} eq "on") { $input{'showlegend'} = "1";
        } else { $input{'showlegend'} = "0"; }
        #if ($username eq "admin") {

        if ($infoblockmod eq 2) {$input{'infoblock'} = "1";}
        if ($dispfrad eq 2) {$input{'freeadblock'} = "1";}

        if ($input{'memberpicpersonalcheck'} && ( $input{'memberpicpersonal'} =~ m/\.gif\Z/i || $input{'memberpicpersonal'} =~ m/\.jpg\Z/i || $input{'memberpicpersonal'} =~ m/\.jpeg\Z/i || $input{'memberpicpersonal'} =~ m/\.png\Z/i ) ) {
                $input{'memberpic'} = $input{'memberpicpersonal'};
        }

        #if ($input{'memberpic'} !~ m^\A[0-9a-zA-Z_\.\#\%\-\:\+\?\$\&\~\.\,\@/]+\Z^) { error("$err{'006'}"); }

    if ($input{'ages'} eq "") {$ages = "";
        } else {$ages = "$input{'ages'}";}
        if ($input{'marstat'} eq "") {$marstat = "";
        } else {$marstat = "$input{'marstat'}";}
        if ($input{'aim'} eq "") {$aim = "";
        } else {$aim = "$input{'aim'}";}
        if ($input{'state'} eq "") {$state = "";
        } else {$state = "$input{'state'}";}
        if ($input{'gen'} eq "") {$gen = "";
        } else {$gen = "$input{'gen'}";}
        if ($input{'profession'} eq "") {$profession = "";
        } else {$profession = "$input{'profession'}";}
        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        if ($input{'passwrd1'} eq $memsettings[0]) { $passwrd = $input{'passwrd1'}; }
        else { $passwrd = crypt($input{'passwrd1'}, substr($input{'username'}, 0, 2)); }
    if ($input{'name'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'icq'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'aim'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'yahoo'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'email'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'websiteurl'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'websitetitle'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'signature'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'settings6'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'settings8'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'memberpic'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'settings10'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'settings11'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'settings12'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'theme'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'language'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'about'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'ages'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'favs'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'profession'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'gen'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'marstat'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
    if ($input{'state'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }


                if ($username ne "admin") {
                         $input{'settings7'} =  $memsettings[7];     # this is the RANK
                         $input{'settings6'} =  $memsettings[6];     # this is the FORUMPOSTS
                         $input{'settings10'} =  $memsettings[10];   # this is the MEMBERSINCE
                         $input{'settings11'} =  $memsettings[11];   # this is the ARTICLES
                         $input{'settings12'} =  $memsettings[12];   # this is the ??? COMMENTS
                         $input{'settings14'} =  $memsettings[14];   # this is the STATUS
                }

    if ($input{'moda'} eq "$btn{'047'}") {
                open(FILE, ">$memberdir/$username.dat") || error("$err{'016'} $input{'username'}.dat");
                file_lock(FILE);
                print FILE "$passwrd\n";
                print FILE "$input{'name'}\n";
                print FILE "$input{'email'}\n";
                print FILE "$input{'websitetitle'}\n";
                print FILE "$input{'websiteurl'}\n";
                if ($input{'signature'} eq "") { $input{'signature'} = "$msg{'026'}"; }
                $input{'signature'} =~ s/\n/\&\&/g;
                $input{'signature'} =~ s/\r//g;
                print FILE "$input{'signature'}\n";
                print FILE "$input{'settings6'}\n";
                print FILE "$input{'settings7'}\n";
                print FILE "$input{'icq'}\n";
                print FILE "$input{'memberpic'}\n";
                print FILE "$input{'settings10'}\n";
                print FILE "$input{'settings11'}\n";
                print FILE "$input{'settings12'}\n";
                print FILE "$input{'theme'}\n";

                if ($username eq "admin") {
                print FILE "$input{'settings14'}\n";
                }
                if ($username ne "admin") {
                print FILE "$memsettings[14]\n";
                }

                print FILE "$input{'language'}\n";
                if ($input{'about'} eq "") { $input{'about'} = ""; }
                $input{'about'} =~ s/\n/\&\&/g;
                $input{'about'} =~ s/\r//g;
                print FILE "$input{'about'}\n";
                print FILE "$input{'ages'}\n";
                print FILE "$input{'fav'}\n";
                print FILE "$input{'state'}\n";
                print FILE "$input{'marstat'}\n";
                print FILE "$input{'profession'}\n";
                print FILE "$input{'gen'}\n";
                print FILE "$input{'aim'}\n";
                print FILE "$input{'yahoo'}\n";
                print FILE "$input{'user_check_date'}\n";
                print FILE "$input{'user_check_time'}\n";
                unfile_lock(FILE);
                close(FILE);

                        open(FILE, ">$memberdir/$username.pref") || error("$err{'016'} $username.pref");
                        file_lock(FILE);
                        print FILE "$input{'impopup'}\n";
                        print FILE "$input{'infoblock'}\n";
                        print FILE "$input{'freeadblock'}\n";
                        print FILE "$input{'welcomemessage'}\n";
                                                 print FILE "0\n";
                                                 print FILE "\n";
                                                print FILE "$input{'preferences[6]'}\n";
                                                 print FILE "$input{'showlegend'}\n";

                          unfile_lock(FILE);
                         close(FILE);

                open(FILE, "$memberdir/$username.dat");
                file_lock(FILE);
                @settings = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                for( $i = 0; $i < @settings; $i++ ) {
                        $settings[$i] =~ s~[\n\r]~~g;
                }
                $username = $input{'username'};
                $password = $settings[0];
                $usertheme = $settings[13];
                $userlang = $settings[15];
                if ($input{'username'} eq $username) {
                        $password = $passwrd;
                        print qq~Set-Cookie: $cookieusername=$username; path=/; expires=$cookie_expdate;\n~;
                        print qq~Set-Cookie: $cookiepassword=$password; path=/; expires=$cookie_expdate;\n~;
                        print qq~Set-Cookie: $cookieusertheme=$usertheme; path=/; expires=$cookie_expdate;\n~;
                        print qq~Set-Cookie: $cookieuserlang=$userlang; path=/; expires=$cookie_expdate;\n~;
                }

                loaduser();
                logvisitors();
                welcome($username);
        }

        if ($input{'delt'} eq "$btn{'007'}") {areyou_sure();
                }
}

##################
sub viewprofile {
##################
        if ($info{'username'} =~ /\//) { error("$err{'004'}"); }
        if ($info{'username'} =~ /\\/) { error("$err{'004'}"); }
        if ($username eq $anonuser) { error("noguests"); }
        if ($username ne "admin") {
        if ($hidememlist eq "1" && $username ne $info{'username'}) { error("$err{'011'}"); }
        }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        if ($memsettings[9] eq "") { $memsettings[9] = "_nopic.gif"; }
        if ($memsettings[9] =~ /^\http:\/\// ) {
                #if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                #else { $tmp_width = ""; }
                #if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                #else { $tmp_height = ""; }
                $memberpic = qq~<img src="$memsettings[9]"></a>~; #$tmp_width $tmp_height border="0" alt=""></a>~;
        }
        else {
                $memberpic = qq~<img src="$imagesurl/avatars/$memsettings[9]" border="0" alt=""></a>~;
        }

        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $memberinfo = $membergroups[2];

        $ranking = $memsettings[6]+$memsettings[11]+$memsettings[12];
        if ($ranking > 25) { $memberinfo = $membergroups[3]; }
        if ($ranking > 50) { $memberinfo = $membergroups[4]; }
        if ($ranking > 75) { $memberinfo = $membergroups[5]; }
        if ($ranking > 100) { $memberinfo = $membergroups[6]; }
        if ($ranking > 250) { $memberinfo = $membergroups[7]; }
        if ($ranking > 500) { $memberinfo = $membergroups[8]; }
        if ($memsettings[7] ne "") { $memberinfo = $memsettings[7]; }
        if ($memsettings[7] eq $root) { $memberinfo = $membergroups[0]; }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);
    $ssettings1 = showhtml("$memsettings[1]");
                $ssettings2 = showhtml("$memsettings[2]");
    $ssettings3 = showhtml("$memsettings[3]");
    $ssettings4 = showhtml("$memsettings[4]");
    $ssettings6 = showhtml("$memsettings[6]");
    $ssettings7 = showhtml("$memsettings[7]");
    $ssettings8 = showhtml("$memsettings[8]");
    $ssettings9 = showhtml("$memsettings[9]");
    $ssettings10 = showhtml("$memsettings[10]");
    $ssettings11 = showhtml("$memsettings[11]");
    $ssettings12 = showhtml("$memsettings[12]");
    $ssettings13 = showhtml("$memsettings[13]");
    $ssettings14 = showhtml("$memsettings[14]");
    $ssettings16 = showhtml("$memsettings[16]");
    $ssettings17 = showhtml("$memsettings[17]");
    $ssettings18 = showhtml("$memsettings[18]");
    $ssettings19 = showhtml("$memsettings[19]");
    $ssettings20 = showhtml("$memsettings[20]");
    $ssettings21 = showhtml("$memsettings[21]");
    $ssettings22 = showhtml("$memsettings[22]");
    $ssettings23 = showhtml("$memsettings[23]");
    $ssettings24 = showhtml("$memsettings[24]");
    $smemberpic = showhtml("$memberpic");
                $lastvisited = readlog("Last_Visited","$info{'username'}");
                if ($lastvisited eq "") {$lastvisited = $ssettings10;}
                display_date($lastvisited); $lastvisited = $user_display_date;
                if ($ssettings10 ne "forever") {$membersince = display_date($ssettings10);} else {$membersince = "forever";}

        $navbar = "$btn{'014'} $nav{'017'} $btn{'014'} $ssettings1";
        print_top();


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

                $catinfo[1] =~ s/[\n\r]//g;
                if ($catinfo[1] ne "") {
                        if ($settings[7] ne "$root" && $settings[7] ne "$catinfo[1]") {        next; }
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
                        }
                }
        }
$pcoftotpost = 0;
$msgpd = 0;

if ($ssettings6 ne "0" && $totalm ne "0") {$pcoftotpost = sprintf ("%.2f",(100/$totalm)*$ssettings6);}
if ($ssettings10 ne "forever") {$date2 = $date; $date1 = $ssettings10;        calcdifference(); $tdmem = $result;
} else {
require "$sourcedir/stats.pl"; parse_log();
$tdmem = $total_days;
}

if ($ssettings6 ne "0" && $tdmem ne "0") {$msgpd = sprintf ("%.2f",($ssettings6/$tdmem));}


print qq~

<TABLE BORDER=0 WIDTH=100%>
<TR>
<TD>
<div align=right>
<a href="$pageurl/$cgi?action=blistedit&buddy=$info{'username'}" onMouseOver="stm(Text[0],Style[0])" onMouseOut="htm()"><img src="$imagesurl/buddy/guest.gif" border=0 alt="Add $info{'username'} to Buddy List"></a>

<a href="index.cgi?action=anonemail&sendto=$info{'username'}" onMouseOver="stm(Text[1],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/email.gif" alt="Send an e-mail to $info{'username'}" border="0"></a>

<a href="index.cgi?action=imsend&to=$info{'username'}" onMouseOver="stm(Text[3],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/message.gif" alt="Send a message to $info{'username'}" border="0"></a>

~;

if ($access[19] eq "on") { print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~; }
elsif ($access[23] eq "on") { print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~; }
elsif ($access[25] eq "on") { print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~; }
elsif ($access[26] eq "on") { print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~; }

else {
         if ($info{'username'} eq $username) { print qq~<a href="$cgi?action=editprofile2&username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~;
         }
}

print qq~
</TD>
</TR>
</TABLE>
~;



        $about = "$ssettings16";
        $about =~ s/\&\&/<br>\n/g;

        print qq~

<table cellpadding="3" cellspacing="3" width="100%" border="0">
<TD valign="top">

<table cellpadding="0" cellspacing="0" width="100%" border="0"><tr>
        <td width="20%" align="center">$memberpic</td>
        <td width="80%" valign="top">
        <table cellpadding="2" cellspacing="2" border="0" WIDTH="100%"><tr>
        <td class="forumwindow3" width="25%">$msg{'013'}</td>
        <td class="forumwindow1" width="75%" nowrap>$ssettings1</td>
        </tr>

<tr>
<td class="forumwindow3" width="25%" nowrap>Rank:</td>
<td class="forumwindow1" width="75%" nowrap>$ssettings14</td>
</tr>

<tr>
~;
if ( $ssettings22 ne "") {
print qq~
        <td class="forumwindow3" width="25%">$msg{'650'}:</td>
        <td class="forumwindow1" width="75%" nowrap>$ssettings22</td>
        </tr><tr>~;}
if ( $ssettings17 ne "") {
print qq~
<td class="forumwindow3" width="25%">$msg{'651'}:</td>
        <td class="forumwindow1" width="75%" nowrap>$ssettings17</td>
        </tr><tr>~;}
if ( $ssettings19 ne "") {
print qq~
<td class="forumwindow3" width="25%">$msg{'652'}:</td>
        <td class="forumwindow1" width="75%" nowrap>$ssettings19</td>
        </tr><tr>~;}
if ( $ssettings21 ne "") {
print qq~
<td class="forumwindow3" width="25%">$msg{'653'}:</td>
        <td class="forumwindow1" width="75%" nowrap>$ssettings21</td>
        </tr><tr>~;}
if ( $ssettings20 ne "") {
print qq~
<td class="forumwindow3" width="25%">$msg{'654'}:</td>
        <td class="forumwindow1" width="75%" width="75%" nowrap>$ssettings20</td>
        </tr><tr>~;}
if ( $ssettings4 ne "") {
print qq~
<td class="forumwindow3" width="25%">$msg{'014'}</td>
        <td class="forumwindow1" width="75%" nowrap><a href="$ssettings4" target="_blank">$ssettings3</a></td>
        </tr><tr>~;}
print qq~

<td class="forumwindow3" width="25%" nowrap>$msg{'027'}</td>
<td class="forumwindow1" width="75%" nowrap>$membersince</td>
</tr>

~;

if ($ssettings8 ne "") {
print qq~
<tr>
<td class="forumwindow3" width="25%" nowrap>ICQ:</td>
<td class="forumwindow1" width="75%" nowrap>
<a href="http://www.icq.com/$ssettings8" target="_blank">
<img src="http://web.icq.com/whitepages/online?img=5&icq=$ssettings8" alt="$msg{'052'} $ssettings1" border="0"> $ssettings8
</a>
</td>
</tr>
~;
}

if ($ssettings23 ne "") {
print qq~
<tr>
<td class="forumwindow3" width="25%" nowrap>AOL:</td>
<td class="forumwindow1" width="75%" nowrap>
<a href="aim:goim?screenname=$ssettings23&message=Hi.+Are+you+there?">
<img src="$imagesurl/aimyel_im.gif" alt="$msg{'661'} $ssettings1" border="0"> $ssettings23
</a>
</td>
</tr>
~;
}

print qq~
<tr>
<td class="forumwindow3" width="25%" nowrap>$msg{'021'}</td>
<td class="forumwindow1" width="75%" nowrap>$ssettings6</td>
</tr>

~;

if ($ssettings11 ne "0") {
print qq~
<tr>
<td class="forumwindow3" width="25%" nowrap>$msg{'022'}</td>
<td class="forumwindow1" width="75%" nowrap>
<a href="$scripturl/$cgi?action=otherarticles&amp;writer=$info{'username'}&amp;real=$ssettings1">
$ssettings11
</a>
</td>
</tr>
~;
}
else {
print qq~
<tr>
<td class="forumwindow3" width="25%" nowrap>$msg{'022'}</td>
<td class="forumwindow1" width="75%" nowrap>$ssettings11</td>
</tr>
~;
 }




print qq~

</table></td>  </tr></table>



        <table cellpadding="3" cellspacing="3" width="100%" border="0">
~;
if ( $ssettings16 ne "") {
print qq~<tr>
<td class="forumwindow3" valign="top" width="25%">$msg{'655'}:</td>
        <td class="forumwindow1" valign="top" width="75%">$about</font></td></tr>~;}
if ( $ssettings18 ne "") {
print qq~<tr>
<td class="forumwindow3" valign="top" width="25%">$msg{'656'}:</td>
        <td class="forumwindow1" valign="top" width="75%">$ssettings18</td></tr>~;}
print qq~
<tr>
<td class="forumwindow3" valign="top" width="25%">Info:</td>
<td class="forumwindow1" valign="top" width="75%">
$ssettings1 $msg{'588'}  $tdmem $msg{'589'}<BR>
$ssettings1 $msg{'590'} $msgpd $msg{'591'}<BR>
$msg{'592'} $pcoftotpost% $msg{'593'}<BR>
$msg{'535'}: $lastvisited
</td>
</tr>

</table> </td>



</TD>
  </TR>
</TABLE>
<CENTER>
~;

if ($ssettings24 ne "") {
print qq~
<IFRAME frameborder=2 style="height:600;width:800;scrolling:;" class=iframe name=cwindow src='$ssettings24'></IFRAME>
<A HREF=http://www.magelo.com TARGET=_new>Magelo Profile</A>
~;
}

print qq~

<TABLE BORDER=0 WIDTH=100%>
<TR>
<TD>
<div align=right>
<a href="$pageurl/$cgi?action=blistedit&buddy=$info{'username'}" onMouseOver="stm(Text[0],Style[0])" onMouseOut="htm()"><img src="$imagesurl/buddy/guest.gif" border=0 alt="Add $info{'username'} to Buddy List"></a>

<a href="index.cgi?action=anonemail&sendto=$info{'username'}" onMouseOver="stm(Text[1],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/email.gif" alt="Send an e-mail to $info{'username'}" border="0"></a>

<a href="index.cgi?action=imsend&to=$info{'username'}" onMouseOver="stm(Text[3],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/message.gif" alt="Send a message to $info{'username'}" border="0"></a>

~;

if ($access[19] eq "on") { # && $info{'username'} ne $username
print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~;
         }
elsif ($access[23] eq "on") { print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~; }
elsif ($access[25] eq "on") { print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~; }
elsif ($access[26] eq "on") { print qq~<a href="$cgi?action=admineditmember&amp;username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~; }


else {
         if ($info{'username'} eq $username) { print qq~<a href="$cgi?action=editprofile2&username=$info{'username'}" class="formslink" onMouseOver="stm(Text[4],Style[0])" onMouseOut="htm()"><img src="http://www.sanctuaryeq2.com/images/forum/modify.gif" alt="Edit $info{'username'}" border=0></a>~;
         }
}

print qq~
</TD>
</TR>
</TABLE>
~;


        print_bottom();
        exit;
}

################
sub editpb {
################
        if ($username eq "$anonuser") { error("$err{'011'}"); }

        print "Location: $pageurl/$cgi?action=editprofile2&username=$username\n\n";
        exit;

}

################
sub editpb2 {
################
        if ($username eq "$anonuser") { error("$err{'011'}"); }

        print "Location: $pageurl/$cgi?action=editprofile2&username=$username\n\n";
        exit;

}

#######################
sub areyou_sure {
#######################

        $navbar = "$btn{'014'} $btn{'007'}";
        print_top();
        print qq~<b>$btn{'007'}?</b><br>
<a href="$cgi\?action=deleteprofile&deleteduser=$input{'username'}" class="formslink">$nav{'047'}</a> - <a href="$cgi\?action=editprofile2&username=$input{'username'}" class="formslink">$nav{'048'}</a>
~;
        print_bottom();
        exit;

}

#########################
sub deleteprofile {
#########################
                if ($letmemdel eq "1") {
                $deleteduser = $info{'deleteduser'};

                if ($username eq $deleteduser) {
                if ($deleteduser ne "admin") {
                unlink("$memberdir/$deleteduser.dat");
                unlink("$memberdir/$deleteduser.msg");
                unlink("$memberdir/$deleteduser.log");
                unlink("$memberdir/$deleteduser.pref");

                open(FILE, "$memberdir/memberlist.dat");
                file_lock(FILE);
                chomp(@members = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                open(FILE, ">$memberdir/memberlist.dat");
                file_lock(FILE);
                foreach $curmem (@members) {
                        if ($curmem ne $deleteduser) { print FILE "$curmem\n"; }
                }
                unfile_lock(FILE);
                close(FILE);

                        print qq~Set-Cookie: $cookieusername=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookiepassword=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookieusertheme=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookieuserlang=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;

                        $username = $anonuser;
                        $password = "";
                        $usertheme = "$defaulttheme";
                        $userlang = $language;
                        @settings = ();
                        $realname = "";
                        $realemail = "";
                        $ENV{'HTTP_COOKIE'} = "";

                        logvisitors();
                        byebye();
                        } else {
                        print "Location: $pageurl/$cgi\n\n";
                        exit;
                        }
                        } else {
                        print "Location: $pageurl/$cgi\n\n";
                        exit;
                        }
                } else {error("$err{'011'}"); }

}

#########################
sub admindeleteprofile {
#########################

use DBI;

        if ($settings[7] ne "Administrator") { error("$err{'011'}"); }

                $deleteduser = $info{'deleteduser'};

                if ($deleteduser ne "admin") {
                unlink("$memberdir/$deleteduser.dat");
                unlink("$memberdir/$deleteduser.msg");
                unlink("$memberdir/$deleteduser.log");
                unlink("$memberdir/$deleteduser.pref");

                open(FILE, "$memberdir/memberlist.dat");
                file_lock(FILE);
                chomp(@members = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                open(FILE, ">$memberdir/memberlist.dat");
                file_lock(FILE);
                foreach $curmem (@members) {
                        if ($curmem ne $deleteduser) { print FILE "$curmem\n"; }
                }
                unfile_lock(FILE);
                close(FILE);
                  print "Location: $pageurl/$cgi?action=memberlist\n\n";
                        exit;
                        } else {
                        print "Location: $pageurl/$cgi?action=memberlist\n\n";
                        exit;
                        }
}
if (-e "$scriptdir/user-lib/user.pl") {require "$scriptdir/user-lib/user.pl"}
1; # return true





