###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# user.pl                                                                     #
# v0.9.9.2 - Requin                                                           #
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
# File: Last modified: 2005                                                   #
###############################################################################
###############################################################################

##############
sub register {
##############

	local($errmsg, $errvalue1, $errvalue2) = @_;
	if ($signupmethod eq "") {$signupmethod = "0";}

	if (!defined $errmsg) { $errmsg = ""; }
	if (!defined $errvalue1) { $errvalue1 = ""; }
	if (!defined $errvalue2) { $errvalue2 = ""; }

	$navbar = "$btn{'014'} $nav{'011'}";
	print_top();

	print qq~<form action="$pageurl/$cgi?action=register2" method="post" onSubmit="oneclick(this)">
<table border="0" cellspacing="1">
~;
	if ($errmsg ne "") {
		print qq~<tr>
<td colspan="2" class="formstextnormal"><font color="#ff0000">$errmsg</font></td>
</tr>
<tr>
<td colspan="2" align="center">&nbsp;<br></td>
</tr>
~;
	}
	print qq~<tr>
<td width="15%" class="formstextnormal">$msg{'006'}</td>
<td width="85%"><input type="text" name="username" size="30" maxlength="20" value="$errvalue1"></td>
</tr>
~;

	if ($signupmethod eq "1") {
		print qq~<tr>
<td width="15%" class="formstextnormal">$msg{'009'}</td>
<td width="85%"><input type="password" name="passwrd1" size="30" maxlength="100"></td>
</tr>
<tr>
<td width="15%" class="formstextnormal">$msg{'537'}:</td>
<td width="85%"><input type="password" name="passwrd2" size="30" maxlength="100"></td>
</tr>
~;
	}
	print qq~<tr>
<td width="15%" class="formstextnormal">$msg{'007'}</td>
<td width="85%"><input type="text" name="email" size="30" maxlength="100"
 value="$errvalue2"></td>
</tr>
~;

	if ($letmemlng eq "1") {
		print qq~<tr>
<td width="15%" valign="top" class="formstextnormal">$msg{'412'}</td>
<td width="85%"><select name="picklanguage">~;

		open(FILE, "$scriptdir/lang/languages.dat" );
		hold(FILE);
		@lang = <FILE>;
		release(FILE);
		close(FILE);

		foreach $line (@lang) {
			$line =~ s/[\n\r]//g;
			@item = split(/\|/, $line);
			if ($item[2] ne "0") {
				if ($item[0] ne "" && $item[1] eq $language) {
					print qq~<option selected value="$item[1]">$item[0]</option>~;
				} else {
					print qq~<option value="$item[1]">$item[0]</option>~;
				}
			}
		}
		print qq~</select>
</td>
</tr>
~;
	}

	if (($modulenlmem eq "1") || ($modulenl eq "1")) {
		print qq~<tr>
<td width="15%" class="formstextnormal">$msg{'172'}</td>
<td width="85%"><INPUT TYPE="checkbox" NAME="newsletter" CHECKED></td>
</tr>
~;
	}

# Eula

	open(FILE, "$datadir/agreement.txt");
	hold(FILE);
	chomp(@text = <FILE>);
	release(FILE);
	close(FILE);

	print qq~<tr>
<td colspan="2" align="center">&nbsp;<br></td>
</tr>
<tr>
<td colspan="2"><b>$msg{'570'}:</b></td>
</tr>
<tr>
<td colspan="2">~;

	foreach $line (@text) {
		$line =~ s/WEBSITE/$pagename/g;
		print qq~$line~;
	}

print qq~</td>
</tr>
~;

# End Eula

	print qq~<tr>
<td colspan="2" align="center"><input
 type="submit" class="button" value="$msg{'568'}"></td>
</tr>
<tr>
<td colspan="2" align="center">&nbsp;<br></td>
</tr>
~;

	if ($signupmethod ne "2") {
		print qq~<tr>
<td colspan="2" align="center" class="formstextnormal">$msg{'583'}</td>
</tr>
~;
	} else {
		print qq~<tr>
<td colspan="2" align="center" class="formstextnormal">$inf{'022'} $inf{'026'}</td>
</tr>
~;
	}

	print qq~<tr>
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

	if (($input{'username'} =~ /[^\w-]/) || ($input{'username'} =~ /^$anonuser$/i)) { error("invalidusername", "", $input{'email'}) } # allow only a-zA-Z0-9_ or - and not $anonuser


	error("nousername", "", $input{'email'}) if ($input{'username'} eq "");
	error("noemail", $input{'username'}, "") if ($input{'email'} eq "");
	error("invalidemail", $input{'username'}, "") if ($input{'email'} !~ /^[0-9A-Za-z@\._\-]+$/ || $input{'email'} =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)|(\.$)/) || ($input{'email'} !~ /\A.+@\[?(\w|[-.])+\.[a-zA-Z]{2,4}|[0-9]{1,4}\]?\Z/);
	error("existsusername", "", $input{'email'}) if (-e ("$memberdir/$input{'username'}.dat"));

	if ($input{'picklanguage'} eq "") { $userlanguage = "$language";
	} else { $userlanguage = "$input{'picklanguage'}"; }

	if ($signupmethod eq "") { $signupmethod ="0"; }

	if ($signupmethod eq "1") {
		 if ($input{'passwrd1'} ne "$input{'passwrd2'}") { error("nopassmatch", "$input{'username'}", "$input{'email'}"); }
	}

	open (MEMBERS,"<$memberdir/memberlist.dat") || &die("I can't open user database\n");
	while(<MEMBERS>) {
		chomp;
		if ($input{'username'} =~ /\b^$_\b/i) {
			&error("existsusername", "", "$input{'email'}");
		}
	}
	close (MEMBERS); #anton - eliminate looping and splitting on nonexistent \n

	open (FILE,"$memberdir/restrictedmemberlist.dat") || &die("I can't open user database\n");
	while(<FILE>) {
		chop;
		@allnames = split(/\n/);
		$checkusername = $input{'username'};
		if (grep (/\b^$checkusername\b/i, @allnames) ne "0" ) { error("existsusername", "", $input{'email'});} # give registrant "user already exists" message
	}
	close(FILE);

	open (FILE,"$memberdir/forapprovallist.dat") || &die("I can't open user database\n");
	while(<FILE>) {
		chop;
		@allnames = split(/\n/);
		$checkusername = $input{'username'};
		if (grep (/\b^$checkusername\b/i, @allnames) ne "0" ) { error("existsusername", "", $input{'email'});}
	}
	close(FILE);

	srand(time ^ $$);
	my @passset = ('a'..'k', 'm'..'n', 'p'..'z', '2'..'9');
	my $passwrd1 = "";
	for ($i=0; $i<8; $i++) { $passwrd1 .= $passset[int(rand($#passset + 1))]; }

	if ($signupmethod ne "1") {

### begin Carters new password encryption: ###
		$cryptedpass = crypt($passwrd1, substr($input{'username'}, 0, 2));
		
		use Babel;
			
		$y = new Babel;
		$passwrd = $y->encode($cryptedpass, "$passwrd1");
			
	} else {
		$cryptedpass = crypt($input{'passwrd1'}, substr($input{'username'}, 0, 2));

		use Babel;
			
		$y = new Babel;
		$passwrd = $y->encode($cryptedpass, "$input{'passwrd1'}");
	}
### end Carters new password encryption: ###

	if ($signupmethod ne "2") {
		open(FILE, ">$memberdir/$input{'username'}.dat");
		hold(FILE);
		print FILE "$passwrd\n";
		print FILE "$input{'username'}\n";
		print FILE "$input{'email'}\n";
		print FILE "\n";
		print FILE "\n";
		print FILE "$msg{'026'}\n";
		print FILE "0\n";
		print FILE "\n";
		print FILE "\n";
		print FILE "\n";
		print FILE "$date\n";
		print FILE "0\n";
		print FILE "0\n";
		print FILE "$defaulttheme\n";
		print FILE "\n";
		print FILE "$userlanguage\n";
		print FILE "\n";
		print FILE "\n";
		print FILE "\n";
		print FILE "\n";
		print FILE "\n";
		print FILE "\n";
		release(FILE);
		close(FILE);

		open(FILE, ">$memberdir/$input{'username'}.pref");
		hold(FILE);
		print FILE "1\n";
		print FILE "1\n";
		print FILE "1\n";
		print FILE "1\n";
		print FILE "0\n";
		print FILE "\n";
		print FILE "0\n";
		print FILE "1\n";
		release(FILE);
		close(FILE);
	}

	if ($signupmethod eq "2") {
		open(FILE, "$memberdir/forapproval.dat");
		hold(FILE);
		@pendingmembers = <FILE>;
		release(FILE);
		close(FILE);

		open(FILE, ">$memberdir/forapproval.dat");
		hold(FILE);
		foreach $curpendingmembers (@pendingmembers) { print FILE "$curpendingmembers"; }
		print FILE "$passwrd1|$passwrd|$input{'username'}|$input{'email'}|$input{'newsletter'}|$userlanguage\n";
		release(FILE);
		close(FILE);

		open(FILE, "$memberdir/forapprovallist.dat");
		hold(FILE);
		@members = <FILE>;
		release(FILE);
		close(FILE);

		open(FILE, ">$memberdir/forapprovallist.dat");
		hold(FILE);
		foreach $curmem (@members) { print FILE "$curmem"; }
		print FILE "$input{'username'}\n";
		release(FILE);
		close(FILE);


# Send IM to Admin that a member needs approving!

		$msgid = time;
		$imsubj = "$msg{'422'}";
		$formatmsg = "$msg{'420'}$input{'username'}$msg{'421'} $msg{'687'}";
		open (FILE, "$memberdir/admin.msg") || error("$err{'001'} $memberdir/admin.msg");
		hold(FILE); @imessages = <FILE>;
		release(FILE);
		close (FILE);
		open (FILE, ">$memberdir/admin.msg") || error("$err{'001'} $memberdir/admin.msg");
		hold(FILE);
		print FILE "$username|$imsubj|$date|$formatmsg|$msgid\n";

		foreach $curm (@imessages) { print FILE "$curm"; }
		release(FILE);
		close(FILE);
	}

	if ($signupmethod ne "2") {
		if ($welcome_im == 1) {
			open(FILE, "$datadir/welcomeim.txt");
			hold(FILE);
			chomp(@lines = <FILE>);
			release(FILE);
			close(FILE);

			$msgid = time;

			open(FILE, ">$memberdir/$input{'username'}.msg");
			hold(FILE);
			print FILE "admin|$lines[0]|$date|$lines[1]|$msgid\n";
			release(FILE);
			close(FILE);
		}

		open(FILE, "$memberdir/memberlist.dat");
		hold(FILE);
		@members = <FILE>;
		release(FILE);
		close(FILE);

		open(FILE, ">$memberdir/memberlist.dat");
		hold(FILE);
		foreach $curmem (@members) { print FILE "$curmem"; }
		print FILE "$input{'username'}\n";
		release(FILE);
		close(FILE);

		if ($input{'newsletter'}) {
			open(FILE,"$datadir/newsletter/emails.txt");
			@subscribers = <FILE>;
			close(FILE);
			$x=0;
			foreach $subscriber(@subscribers) {chomp($subscriber); if ($input{'email'} eq $subscriber){  $x=1;}}
			if ($x eq 0) {
				open(FILE, ">>$datadir/newsletter/emails.txt") || (print "Error");
				hold(FILE);
				print FILE "$input{'email'}\n";
				release(FILE);
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
		hold(FILE); @imessages = <FILE>;
		release(FILE);
		close (FILE);
		open (FILE, ">$memberdir/admin.msg") || error("$err{'001'} $memberdir/admin.msg");
		hold(FILE);
		print FILE "$username|$imsubj|$date|$formatmsg|$msgid\n";

		foreach $curm (@imessages) { print FILE "$curm"; }
		release(FILE);
		close(FILE);
	}

	open(LOG, "$datadir/log.dat");
	hold(LOG);
	@entries = <LOG>;
	release(LOG);
	close(LOG);

	open(LOG, ">$datadir/log.dat");
	hold(LOG);
	$field="$username";
	foreach $curentry (@entries) {
		$curentry =~ s/\n//g;
		($name, $value) = split(/\|/, $curentry);
		if($name ne "$field") {
			print LOG "$curentry\n";
		}
	}
	release(LOG);
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

	if($input{'username'} eq "$anonuser" || $input{'username'} eq "") {
		&data_error;
	}

	if (-e("$memberdir/$input{'username'}.dat")) {
		open(FILE, "$memberdir/$input{'username'}.dat");
		hold(FILE);
		@settings = <FILE>;
		release(FILE);
		close(FILE);

		for( $i = 0; $i < @settings; $i++ ) {
			$settings[$i] =~ s~[\n\r]~~g;
		}

### begin Carters new password encryption: ###
		$cryptedpass = crypt($input{'passwrd'}, substr($input{'username'}, 0, 2));

		use Babel;
			
		$y = new Babel;
		$passwrd = $y->encode($cryptedpass, "$input{'passwrd'}");
		$passwrdold = $y->encode($cryptedpass, $cryptedpass);

		if ($settings[0] ne $passwrd  && $settings[0] ne $passwrdold) { 

			if ($settings[0] eq "$cryptedpass") { # fix it
				
				use Babel;
			
				$y = new Babel;
				$newpasswrd = $y->encode($cryptedpass, "$input{'passwrd'}");

				open(FILE, ">$memberdir/$input{'username'}.dat");
				hold(FILE);
				print FILE "$newpasswrd\n";
				for ($i = 1; $i < @settings; $i++) { print FILE "$settings[$i]\n"; }
				release(FILE);
				close(FILE);

			}
		
		# ---------------------------------------------------------
		# This part will no longer be needed once all the passwords have been run through
		# for the beta testers and the original site

#			if ($settings[0] eq $passwrdold) { #Then change it back

#				use Babel;
			
#				$y = new Babel;
#				$newpasswrd = $y->encode($cryptedpass, "$input{'passwrd'}");

#				open(FILE, ">$memberdir/$input{'username'}.dat");
#				hold(FILE);
#				print FILE "$newpasswrd\n";
#				for ($i = 1; $i < @settings; $i++) { print FILE "$settings[$i]\n"; }
#				release(FILE);
#				close(FILE);

#			}

		# End no longer needed code.  Delete at a later date ^^^^^
		#----------------------------------------------------------

			else { error("$err{'002'}"); }
		}

### end Carters new password encryption: ###
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
        hold(LOG);
        @entries = <LOG>;
        release(LOG);
        close(LOG);

        open(LOG, ">$datadir/log.dat");
        hold(LOG);
				$field="$username";
        foreach $curentry (@entries) {
                $curentry =~ s/\n//g;
     		($name, $value) = split(/\|/, $curentry);
                if($name ne "$field") {
                        print LOG "$curentry\n";
                }
        }
        release(LOG);
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

############## # can't see where this is used
sub redirect {
############## # redirect action for links, redirect sub in links and downloads pl's

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
	<form method="post" action="$pageurl/$cgi?action=reminder2">
	<table border="0" cellpadding="2" cellspacing="1">
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
	hold(FILE);
	chomp(@settings = <FILE>);
	release(FILE);
	close(FILE);

	for ($i = 0; $i < @settings; $i++) {
		$settings[$i] =~ s~[\n\r]~~g;
	}
	if ($input{'email'} !~ /^$settings[2]$/i) { error ("$err{'028'}"); } #BradC
	srand(time ^ $$);
	my @passset = ('a'..'k', 'm'..'n', 'p'..'z', '2'..'9');
	my $passwrd1 = "";
	for ($i=0; $i<8; $i++) { $passwrd1 .= $passset[int(rand($#passset + 1))]; }

### begin Carters new password encryption: ###
	$cryptedpass = crypt($passwrd1, substr($input{'username'}, 0, 2));

	use Babel;

	$y = new Babel;
	$newpasswrd = $y->encode($cryptedpass, "$passwrd1");
### end Carters new password encryption: ###

	open(FILE, ">$memberdir/$input{'username'}.dat");
	hold(FILE);
	print FILE "$newpasswrd\n";
	for ($i = 1; $i < @settings; $i++) { print FILE "$settings[$i]\n"; }
	release(FILE);
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
# called after loaduser in all but redirect (not used?) and editprofile (User doesn't exist! error if not logged in)

	if (!defined $returnpage) { $returnpage = ""; }
	if ($returnpage ne "") { print "Location: $scripturl/$cgi?action=$returnpage\n\n"; exit; }

	open(FILE, "$memberdir/$username.dat") || error("$err{'010'}"); # User doesn't exist!
	hold(FILE);
	chomp(@memsettings = <FILE>); # resets what is already set as settings in loaduser - memsettings used for others, not self
	release(FILE);
	close(FILE); # loaduser does all this

	open(FILE, "$memberdir/$username.msg");
	hold(FILE);
	@imessages = <FILE>;
	release(FILE);
	close(FILE);

	open(FILE, "$memberdir/membergroups.dat");
	hold(FILE);
	@membergroups = <FILE>;
	release(FILE);
	close(FILE);

	$umessageid = $info{"messageid"};

	if ($memsettings[9] eq "") { $memsettings[9] = "_nopic.gif"; }
	if ($memsettings[9] =~ /^http:\/\// ) {
		if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
		else { $tmp_width = ""; }
		if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
		else { $tmp_height = ""; }
		$memberpic = qq~<img src="$memsettings[9]" $tmp_width $tmp_height border="0" alt=""></a>~;
	}
	else {
		$memberpic = qq~<img src="$imagesurl/avatars/$memsettings[9]" border="0" alt=""></a>~;
	}

	$lastvisited = readlog("Last_Visited");

	censor_it($memsettings[16]);
	censor_it($memsettings[18]);

	myprofile();

}

###############
sub myprofile {
###############
# called only from welcome sub

	if (!defined $memsettings[3]) { $memsettings[3] = ""; } # website title
	if (!defined $memsettings[4]) { $memsettings[4] = ""; } # website URL
	if (!defined $memsettings[6]) { $memsettings[6] = ""; } # forum posts
	if (!defined $memsettings[7]) { $memsettings[7] = ""; } # rank - set to $userrank in loaduser sub
	if (!defined $memsettings[11]) { $memsettings[11] = ""; } # articles - set to $userstatus in loaduser sub
	if (!defined $memsettings[14]) { $memsettings[14] = ""; } # status
	if (!defined $memsettings[16]) { $memsettings[16] = ""; } # about
	if (!defined $memsettings[17]) { $memsettings[17] = ""; } # age
	if (!defined $memsettings[18]) { $memsettings[18] = ""; } # favorite activities
	if (!defined $memsettings[19]) { $memsettings[19] = ""; } # geographical location
	if (!defined $memsettings[20]) { $memsettings[20] = ""; } # marital status
	if (!defined $memsettings[21]) { $memsettings[21] = ""; } # profession
# by default, new member file is only printed through 21

	$#memsettings = 26; # set length so presets will stick

	if (!defined $memsettings[22]) { $memsettings[22] = ""; } # gender

	$navbar = "$btn{'014'} $msg{'305'}$memsettings[1]";
	print_top();

	$about = "$memsettings[16]";
	$about =~ s/\&\&/<br>\n/g;

	print qq~<table cellpadding="3" cellspacing="3" width="100%" border="0"><tr>
<td colspan="2" class="texttitle">$memsettings[1], $msg{'163'}</td>
</tr>
<tr>
<td colspan="2" class="whocat">$msg{'586'}</td>
</tr>
<tr>
<td colspan="2" class="whocat">$msg{'342'}<a
 href="$pageurl/$cgi?action=im" class="whomenu">$mnum</a>$msg{'343'}</td>
</tr>
</table>
<table cellpadding="3" cellspacing="3" width="100%" border="0">
<tr>
<td width="20%" align="center">$memberpic</td>
<td width="80%" valign="top">
<table cellpadding="2" cellspacing="2" border="0">
<tr>
<td class="forumwindow3" width="25%">$msg{'013'}</td>
<td class="forumwindow1" width="75%" nowrap>$memsettings[1]</td>
</tr>
<tr>
<td class="forumwindow3" width="25%">$msg{'650'}</td>
<td class="forumwindow1" width="75%" nowrap>$memsettings[22]</td>
</tr>
<tr>
<td class="forumwindow3" width="25%">$msg{'651'}</td>
<td class="forumwindow1" width="75%" nowrap>$memsettings[17]</td>
</tr>
<tr>
<td class="forumwindow3" width="25%">$msg{'652'}</td>
<td class="forumwindow1" width="75%" nowrap>$memsettings[19]</td>
</tr>
<tr>
<td class="forumwindow3" width="25%">$msg{'653'}</td>
<td class="forumwindow1" width="75%" nowrap>$memsettings[21]</td>
</tr>
<tr>
<td class="forumwindow3" width="25%">$msg{'654'}</td>
<td class="forumwindow1" width="75%" width="75%" nowrap>$memsettings[20]</td>
</tr>
<tr>
<td class="forumwindow3" width="25%">$msg{'014'}</td>
<td class="forumwindow1" width="75%" nowrap><a
 href="$memsettings[4]" target="_blank">$memsettings[3]</a></td>
</tr>
</table></td>
</tr>
</table>
<table cellpadding="3" cellspacing="3" width="100%" border="0">
<tr>
<td width="100%" valign="top"><table
 cellpadding="3" cellspacing="3" width="100%" border="0">
<tr>
<td class="forumwindow3" valign="top" width="25%">$msg{'655'}</td>
<td class="forumwindow1" valign="top" width="75%">$about</font></td>
</tr>
<tr>
<td class="forumwindow3" valign="top" width="25%">$msg{'656'}</td>
<td class="forumwindow1" valign="top" width="75%">$memsettings[18]</td>
</tr>
<tr>
</tr>
</table></td>
</tr>
</table>
<table cellpadding="3" cellspacing="3" width="100%" border="0">
<tr>
<td class="forumwindow1" width="25%">$msg{'024'}&nbsp;$memsettings[7]</td>
<td class="forumwindow1" width="25%">$msg{'178'}&nbsp;$memsettings[14]</td>
<td class="forumwindow1" width="25%">$msg{'021'}&nbsp;$memsettings[6]</td>
<td class="forumwindow1" width="25%">$msg{'022'}&nbsp;$memsettings[11]</td>
</tr>
<tr>
<td class="forumwindow3" align="center" width="25%"><a
 href="$pageurl/$cgi?action=viewprofile&username=$username">$nav{'017'}</a></td>
<td class="forumwindow3" align="center" width="25%"><a
 href="$pageurl/$cgi?action=editprofile2&username=$username">$nav{'161'}</a></td>
<td class="forumwindow3" colspan="2" align="center" width="50%"><a
 href="$pageurl/$cgi?action=logout">$nav{'034'}</a></td>
</tr>
</table>
<br>
~;

	if (!defined $umessageid) { $umessageid = ""; }

	if ($umessageid ne "") {
		imview();
	}

 	print qq~<table
 cellpadding="3" cellspacing="3" width="100%" border="0">
<tr>
<td align="center" class="forumwindow3"><a
 href="$pageurl/$cgi?action=imsend">$nav{'029'}</a></td>
<td colspan="2" align="center" class="forumwindow3"><a
 href="$pageurl/$cgi?action=im">$nav{'102'}</a></td>
<td align="center" class="forumwindow3"><a
 href="$pageurl/$cgi?action=imremove&amp;id=all">$msg{'576'}</a></td>
</tr>
</table>
<table width="99%" bgcolor="#000000" border="0" cellspacing="1" cellpadding="2">
<tr>
<td class="imtitle" width="10%"><b>$msg{'182'}</b></td>
<td class="imtitle" width="20%"><b>$msg{'214'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>
</tr>
~;

	if (@imessages == 0) {
		print qq~<tr>
<td colspan="4" class="imwindow1">$msg{'050'}</td>
</tr>
~;
	} else {

		$second = "imwindow2";
		for ($a = 0; $a < @imessages; $a++) {
			if ($second eq "imwindow1") { $second="imwindow2"; }
			else { $second="imwindow1"; }

			($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);

			chomp($messageid[$a]);

			if ($messageid[$a] < 100) { $messageid[$a] = $a; }
			$subject = "$msub[$a]";
			if ($subject eq "") { $subject="---"; }

			$mmessage[$a] =~ s/\n//g;
			$mmessage[$a] =~ s/\r//g;
			$message="$mmessage[$a]";
			$mdate = "$mdate[$a]";
			$postinfo = "";
			$signature = "";
			$viewd = "";
			$icq = "";
			$star = "";
			$newim = "";
			$imnav = "oldimlink";

			if (!defined $mviewed[$a]) { $mviewed[$a] = ""; }

			if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
				$newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~;
				$imnav = "newimlink";
			}
			elsif ($umessageid eq $messageid[$a]) {
				$second = "imselected";
			}

			display_date($mdate); $mdate = $user_display_date;

			print qq~<tr>~;
			if ($musername[$a] eq "$anonuser") {
				print qq~<td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
			} else {
				print qq~<td class="$second" width="10%"><a
 href="$pageurl/$cgi?action=imsend&to=$musername[$a]" class="$imnav">$musername[$a]</a></td>
~;
			}

			print qq~<td class="$second" width="20%">$mdate</td>
<td class="$second" width="60%"><a
 href="$pageurl/$cgi?action=im&amp;from=$musername[$a]&amp;messageid=$messageid[$a]"
 class="$imnav">$newim$msub[$a]</td>
~;

			if ($musername[$a] eq "$anonuser") {
				print qq~<td class="$second" width="10%"><center><a
 href="$pageurl/$cgi?action=imremove&id=$messageid[$a]"><img
 src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>
~;
			} else {
				print qq~<td class="$second" width="10%"><center><a
 href="$pageurl/$cgi?action=imsend&to=$musername[$a]&num=$messageid[$a]"><img
 src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>&nbsp;&nbsp;<a
 href="$pageurl/$cgi?action=imremove&id=$messageid[$a]"><img
 src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>
~;
			}

			print qq~</tr>
	~;
		}
	}

	if ($username eq "admin") {
		print qq~<tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$pageurl/$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$pageurl/$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$pageurl/$cgi?action=modim">$msg{'594'}</a></td>
</tr>
~;
	}

	if ($username ne "admin" && $userrank eq "$root") {
		print qq~<tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$pageurl/$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$pageurl/$cgi?action=modim">$msg{'594'}</a></td>
</tr>
~;
	}

	if ($username ne "admin" && $userrank ne "$root" && $userrank eq "$boardmoderator") {
		print qq~<tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$pageurl/$cgi?action=modim">$msg{'594'}</a></td>
</tr>
~;
	}

	print qq~</table>
<br>
~;

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
		print qq~<form action="$pageurl/$cgi?action=login2" method="post">
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

##################
sub editprofile2 {
##################

	if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
	if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }
	if ($username ne $info{'username'}) { error("$err{'011'}" ); }

	open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
	hold(FILE);
	chomp(@memsettings = <FILE>);
	release(FILE);
	close(FILE);

	if (!defined $memsettings[1]) { $memsettings[1] = ""; } # real name
	if (!defined $memsettings[2]) { $memsettings[2] = ""; } # email
	if (!defined $memsettings[3]) { $memsettings[3] = ""; } # website title
	if (!defined $memsettings[4]) { $memsettings[4] = ""; } # website URL
	if (!defined $memsettings[5]) { $memsettings[5] = ""; } # signature
	if (!defined $memsettings[6]) { $memsettings[6] = 0; } # forum posts
	if (!defined $memsettings[7]) { $memsettings[7] = ""; } # rank - set to $userrank in loaduser sub
	if (!defined $memsettings[8]) { $memsettings[8] = ""; } # icq
	if (!defined $memsettings[9]) { $memsettings[9] = ""; } # avatar
	if (!defined $memsettings[10]) { $memsettings[10] = ""; } # member since
	if (!defined $memsettings[11]) { $memsettings[11] = 0; } # articles
	if (!defined $memsettings[12]) { $memsettings[12] = 0; } # comments
	if (!defined $memsettings[13]) { $memsettings[13] = ""; } # theme
	if (!defined $memsettings[14]) { $memsettings[14] = ""; } # status - set to $userstatus in loaduser sub
	if (!defined $memsettings[15]) { $memsettings[15] = ""; } # language
	if (!defined $memsettings[16]) { $memsettings[16] = ""; } # about
	if (!defined $memsettings[17]) { $memsettings[17] = ""; } # age
	if (!defined $memsettings[18]) { $memsettings[18] = ""; } # favorite activities
	if (!defined $memsettings[19]) { $memsettings[19] = ""; } # geographical location
	if (!defined $memsettings[20]) { $memsettings[20] = ""; } # marital status
	if (!defined $memsettings[21]) { $memsettings[21] = ""; } # profession
# this is the last line printed for a new member ($memsettings[21])

	$#memsettings = 26; # set length so presets will stick

	if (!defined $memsettings[22]) { $memsettings[22] = ""; } # gender
	if (!defined $memsettings[23]) { $memsettings[23] = ""; } # aim
	if (!defined $memsettings[24]) { $memsettings[24] = ""; } # yahoo
	if (!defined $memsettings[25]) { $memsettings[25] = ""; } # date format
	if (!defined $memsettings[26]) { $memsettings[26] = ""; } # timezone

	$signature = "$memsettings[5]";
	$signature =~ s/\&\&/\n/g;

	$about = "$memsettings[16]";
	$about =~ s/\&\&/\n/g;

	$navbar = "$btn{'014'} $nav{'161'}";
	print_top();

	print qq~<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=editprofile3" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">$nav{'161'}</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'006'}</td>
<td class="formstext" width="70%"><input type="hidden" name="username" value="$info{'username'}">$info{'username'}
<input type="hidden" name="rememberme" value="1"></td>
</tr>
~;
	if ($username eq "admin") {
		print qq~
<tr>
<td class="formstextnormal" width="30%">$msg{'011'}</td>
<td class="formstext" width="70%"><input type="hidden" name="status" value="$memsettings[14]">$memsettings[14]</td>
</tr>
~;
	}
	if ($username ne "admin") {
		print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'011'}</td>
<td class="formstext" width="70%">$memsettings[14]</td>
</tr>
~;
	}
	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'009'}</td>
<td class="formstext" width="70%"><input type="password" name="passwrd1" size="20" value="$memsettings[0]">*</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'537'}</td>
<td class="formstext" width="70%"><input type="password" name="passwrd2" size="20" value="$memsettings[0]">*</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'013'}</td>
<td class="formstext" width="70%"><input type="text" name="name" size="40" value="$memsettings[1]">*</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'007'}</td>
<td class="formstext" width="70%"><input type="text" name="email" size="40" value="$memsettings[2]">*</td>
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
<tr>
<td class="formstextnormal" width="30%">$msg{'662'}:</td>
<td width="70%"><input type="text" name="yahoo" size="40" value="$memsettings[24]"></td>
</tr>
~;

	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'650'}:</td>
<td width="70%"><select name="gen">
~;

	open(FILE, "$memberdir/prodata/gen.dat" );
	hold(FILE);
	@gen = <FILE>;
	release(FILE);
	close(FILE);

	foreach $line (@gen) {
		$line =~ s/[\n\r]//g;
		@item = split(/\|/, $line);
		if ($item[2] ne "0") {
			if ($memsettings[22] eq $item[1]) {
				print qq~<option selected value="$item[1]">$item[0]</option>\n~;
			} else {
				print qq~<option value="$item[1]">$item[0]</option>\n~;
			}
		}
   }

	print qq~</select></td>
</tr>
<tr>
~;

	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'651'}:</td>
<td width="70%"><select name="ages">~;

	open(FILE, "$memberdir/prodata/ages.dat" );
	hold(FILE);
	@ages = <FILE>;
	release(FILE);
	close(FILE);

	foreach $line (@ages) {
		$line =~ s/[\n\r]//g;
		@item = split(/\|/, $line);
		if ($item[2] ne "0") {
			if ($memsettings[17] eq $item[1]) {
				print qq~<option selected value="$item[1]">$item[0]</option>
~;
			} else {
				print qq~<option value="$item[1]">$item[0]</option>
~;
			}
		}
	}

	print qq~</select></td>
</tr>
~;

	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'654'}:</td>
<td width="70%"><select name="marstat">~;

	open(FILE, "$memberdir/prodata/marstat.dat" );
	hold(FILE);
	@mar = <FILE>;
	release(FILE);
	close(FILE);

	foreach $line (@mar) {
		$line =~ s/[\n\r]//g;
		@item = split(/\|/, $line);
		if ($item[2] ne "0") {
			if ($memsettings[20] eq $item[1]) {
				print qq~<option selected value="$item[1]">$item[0]</option>\n~;
			} else {
				print qq~<option value="$item[1]">$item[0]</option>\n~;
			}
		}
	}

	print qq~</select></td>
</tr>
<tr>
<td class="formstextnormal" width="30%" valign="top"><b>$msg{'655'}:</b></td>
<td class="formstextnormal" width="70%"><textarea name="about" rows="4" cols="35" maxlength="50" wrap="virtual">$about</TEXTAREA></td>
</tr>
~;

	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'652'}:</td>
<td width="70%"><select name="state">~;

	open(FILE, "$memberdir/prodata/states.dat");
	hold(FILE);
	@states = <FILE>;
	release(FILE);
	close(FILE);

	foreach $line (@states) {
		$line =~ s/[\n\r]//g;
		@item = split(/\|/, $line);
		if ($item[2] ne "0") {
			if ($memsettings[19] eq $item[1]) {
				print qq~<option selected value="$item[1]">$item[0]</option>\n~;
			} else {
				print qq~<option value="$item[1]">$item[0]</option>\n~; }
			}
		}

		print qq~</select></td>
</tr>
<tr>
~;

		print qq~
<tr>
<td class="formstextnormal" width="30%">$msg{'653'}:</td>
<td width="70%"><select name="profession">
~;

	open(FILE, "$memberdir/prodata/profession.dat" );
	hold(FILE);
	@prof = <FILE>;
	release(FILE);
	close(FILE);

	foreach $line (@prof) {
		$line =~ s/[\n\r]//g;
		@item = split(/\|/, $line);
		if ($item[2] ne "0") {
			if ($memsettings[21] eq $item[1]) {
				print qq~<option selected value="$item[1]">$item[0]</option>\n~;
			} else {
				print qq~<option value="$item[1]">$item[0]</option>\n~;
			}
		}
	}

	print qq~</select></td>
</tr>
~;

	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'656'}:</td>
<td><input type="text" name="fav" size="40" maxlength="200" value="$memsettings[18]"></td>
</tr>
</tr>
<td valign="top" class="formstextnormal" width="30%">$msg{'017'}</td>
<td width="70%"><textarea name="signature" rows="4" cols="35" wrap="virtual">$signature</TEXTAREA></td>
</tr>
~;

	if ($letmemlng eq "1") {
		print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'412'}</td>
<td width="70%"><select name="language">~;

		open(FILE, "$scriptdir/lang/languages.dat" );
		hold(FILE);
		@lang = <FILE>;
		release(FILE);
		close(FILE);

		foreach $line (@lang) {
			$line =~ s/[\n\r]//g;
			@item = split(/\|/, $line);
			if ($item[2] ne "0") {
				if ($memsettings[15] eq $item[1]) {
					print qq~<option selected value="$item[1]">$item[0]</option>
~;
				} else {
					print qq~<option value="$item[1]">$item[0]</option>
~;
				}
			}
		}

		print qq~</select></td>
</tr>
~;
	}

	if ($letmemthm eq "1") {
		print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'161'}</td>
<td width="70%"><select name="theme">~;

		open(FILE, "$themesdir/themes.dat" );
		hold(FILE);
		@themes = <FILE>;
		release(FILE);
		close(FILE);

		foreach $line (@themes) {
			$line =~ s/[\n\r]//g;
			@item = split(/\|/, $line);
			if ($item[2] ne "0") {
				if ($memsettings[13] eq $item[1]) {
					print qq~<option selected value="$item[1]">$item[0]</option><br>~;
				} else {
					print qq~<option value="$item[1]">$item[0]</option><br>~;
				}
			}
		}

		print qq~</select>
</td>
</tr>
~;
	}

	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'664'}</td>
<td width="70%">~;

# For backwards compatability
	if ($memsettings[25] eq "") {
		print qq~<select name="user_check_date">
<option selected value="american">$msg{'555'}</option>
<option value="european">$msg{'556'}</option></select>
~;
	}
	if ($memsettings[25] eq "american") {
		print qq~<select name="user_check_date">
<option selected value="american">$msg{'555'}</option>
<option value="european">$msg{'556'}</option></select>
~;
	}
	if ($memsettings[25] eq "european") {
		print qq~<select name="user_check_date">
<option selected value="european">$msg{'556'}</option>
<option value="american">$msg{'555'}</option></select>
~;
	}

	print qq~</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'663'}</td>
<td width="70%"><select name="user_check_time">~;

	open (ZONES,"<$datadir/timezones.dat") || error("$err{'016'} $datadir/timezones.dat");
	@timezones=<ZONES>;
	close (ZONES);

	if ($memsettings[26] eq "") { $memsettings[26] = $timezone; } # $timezone set in config.pl

	foreach $zone (@timezones) {
		$zone =~ s/[\n\r]//g;
		@zitem = split(/\|/, $zone);

		if ($zitem[0] eq $memsettings[26]) {
			print qq~<option value="$zitem[0]" selected>$zitem[2] $zitem[3]: $zitem[5]</option>~;
		} else {
			print qq~<option value="$zitem[0]">$zitem[2] $zitem[3]: $zitem[5]</option>~;
		}
	}

	print qq~</select>
</td>
</tr>
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
	} else {
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
</tr>
~;

	if ($username eq "admin") {

		open(FILE, "$memberdir/membergroups.dat");
		hold(FILE);
		@groups = <FILE>;
		release(FILE);
		close(FILE);

		my @superusers = @groups[0..9];

		$position = "";
		if ($memsettings[7] eq "") {
			$position = qq~$position<option value="$line" selected>$line</option>\n~;
		}
		foreach $line (@superusers) {
			$line =~ s/[\n\r]//g;
			if ($memsettings[7] eq $line) {
				$position = qq~$position<option value="$line" selected>$line</option>\n~;
			} else {
				$position = qq~$position<option value="$line">$line</option>\n~;
			}
		}

		open(FILE, "$memberdir/memberstatus.dat");
		hold(FILE);
		@groups = <FILE>;
		release(FILE);
		close(FILE);

		@superusers = @groups[0..9];

		$position1 = "";
		if ($memsettings[14] eq "") {
			$position1 = qq~$position1<option value="$line" selected>$line</option>\n~;
		}
		foreach $line (@superusers) {
			$line =~ s/[\n\r]//g;
			if ($memsettings[14] eq $line) {
				$position1 = qq~$position1<option value="$line" selected>$line</option>\n~;
			} else {
				$position1 = qq~$position1<option value="$line">$line</option>\n~;
			}
		}

		print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'011'}</td>
<td width="70%"><select name="settings14">
$position1</select></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'024'}</td>
<td width="70%"><select name="settings7">
$position</select></td>
</tr>
~;
	}

	open(FILE, "$memberdir/$info{'username'}.pref") || error("$err{'010'}");
	hold(FILE);
	chomp(@preferences = <FILE>);
	release(FILE);
	close(FILE);

	if ($preferences[0] eq "1") { $checked0 = " checked";	} else { $checked0 = ""; }
	if ($preferences[1] eq "1") { $checked1 = " checked";	} else { $checked1 = ""; }
	if ($preferences[2] eq "1") { $checked2 = " checked";	} else { $checked2 = ""; }
	if ($preferences[3] eq "1") { $checked3 = " checked";	} else { $checked3 = ""; }
	if ($preferences[4] eq "1") { $checked4 = " checked";	} else { $checked4 = ""; }
	if ($preferences[7] eq "1") { $checked7 = " checked";	} else { $checked7 = ""; }

	print qq~<tr>
<td colspan="2">&nbsp;</td>
</tr>
<tr>
<td class="formstexttitle" colspan="2">$nav{'088'}</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'413'}</td>
<td width="70%"><input type="checkbox" name="impopup"$checked0></td>
</tr>
~;

	if ($infoblockmod eq 1) {
		print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'414'}</td>
<td width="70%"><input type="checkbox" name="infoblock"$checked1></td>
</tr>
~;
	}

	if ($dispfrad eq 1) {
		print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'416'}</td>
<td width="70%"><input type="checkbox" name="freeadblock"$checked2></td>
</tr>
~;
	}

	print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'417'}</td>
<td width="70%"><input type="checkbox" name="welcomemessage"$checked3></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'536'}</td>
<td width="70%"><input type="checkbox" name="showlegend"$checked7></td>
</tr>
</td>
</tr>
~;

	if ($username eq "admin") {
		print qq~<tr>
<td class="formstextnormal" width="30%">$msg{'418'}</td>
<td width="70%"><input type="checkbox" name="broadcastmessage"$checked4></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'419'}</td>
<td width="70%"><input type="text" name="saybroadcast" value="$preferences[5]" size="60"></td>
</tr>
~;
	}

	print qq~<tr>
<td colspan="2">&nbsp;</td>
</tr>
<tr>
<td colspan="2" class="formstextsmall" width="30%">* $msg{'025'}</td>
</tr>
<tr>
<td colspan="2"><input type="hidden" name="settings6" value="$memsettings[6]">
<input type="hidden" name="settings7" value="$memsettings[7]">
<input type="hidden" name="settings8" value="$memsettings[8]">
<input type="hidden" name="settings10" value="$memsettings[10]">
<input type="hidden" name="settings11" value="$memsettings[11]">
<input type="hidden" name="settings12" value="$memsettings[12]">
<input type="hidden" name="preferences[6]" value="$preferences[6]">
<input type="submit" class="button" name="moda" value="$btn{'047'}">&nbsp;&nbsp;~;

	if ($letmemdel eq "1" && $info{'username'} ne "admin") {
		print qq~<input type="submit" class="button" name="delt" value="$btn{'007'}">~;
	}

	print qq~</td>
</tr>
</form>
<tr>
<td colspan="2">&nbsp;</td>
</tr>
~;

	if (($modulenl eq "1") || ($modulenlmem eq "1")) {
		$found= 0 ;
		$checkunsub="";
		open(FILE,"$datadir/newsletter/emails.txt");
		@addresses=<FILE>;
		close(FILE);

		foreach $check (@addresses) {
			chomp($check);
			$check =~ tr/A-Z/a-z/;
			$usermail = $memsettings[2];
			$usermail =~ tr/A-Z/a-z/;
			if ($usermail eq $check){
				$found=1;
				$checkunsub="checked";
			}
		}
		if ($found eq 1) {
			print qq~<tr>
<td width="30%">&nbsp;</td>
<td width="70%"><B>$msg{'173'}</B></td>
</tr>
~;
		} else {
			print qq~<tr>
<td width="30%">&nbsp;</td>
<td width="70%"><B>$msg{'174'}</B></td>
</tr>
~;
		}

		print qq~</table>
</form>

<form action="$pageurl/$cgi?action=subscribe" method="POST">
<table border="0">
<tr>
<td width="30%">&nbsp;</td>
<td width="70%">$msg{'176'} <input
 type=radio name=action value=subscribe checked> | $msg{'177'} <input
 type=radio name=action value=remove $checkunsub> <input
 type="text" name="joinnl" value="$memsettings[2]" size="16" class="text"> <input
 type="submit" class="button" value="$btn{'015'}"></td>
</tr>
</table>
</form>
~;
	}

	print qq~</table></td>
</tr>
</table>
~;

	print_bottom();
	exit;

}

##################
sub editprofile3 {
##################

	if (!defined $info{'username'}) { $info{'username'} = ""; }
	if (!defined $input{'passwrd1'}) { $input{'passwrd1'} = ""; }
	if (!defined $input{'name'}) { $input{'name'} = ""; }
	if (!defined $input{'email'}) { $input{'email'} = ""; }
	if (!defined $input{'theme'}) { $input{'theme'} = ""; }
	if (!defined $input{'language'}) { $input{'language'} = ""; }
	if (!defined $input{'impopup'}) { $input{'impopup'} = ""; }
	if (!defined $input{'infoblock'}) { $input{'infoblock'} = ""; }
	if (!defined $input{'freeadblock'}) { $input{'freeadblock'} = ""; }
	if (!defined $input{'welcomemessage'}) { $input{'welcomemessage'} = ""; }
	if (!defined $input{'showlegend'}) { $input{'showlegend'} = ""; }
	if (!defined $input{'broadcastmessage'}) { $input{'broadcastmessage'} = ""; }
	if (!defined $input{'saybroadcast'}) { $input{'saybroadcast'} = ""; }
	if (!defined $input{'memberpicpersonalcheck'}) { $input{'memberpicpersonalcheck'} = ""; }
	if (!defined $input{'memberpicpersonal'}) { $input{'memberpicpersonal'} = ""; }
	if (!defined $input{'memberpic'}) { $input{'memberpic'} = ""; }
	if (!defined $input{'ages'}) { $input{'ages'} = ""; }
	if (!defined $input{'marstat'}) { $input{'marstat'} = ""; }
	if (!defined $input{'aim'}) { $input{'aim'} = ""; }
	if (!defined $input{'state'}) { $input{'state'} = ""; }
	if (!defined $input{'gen'}) { $input{'gen'} = ""; }
	if (!defined $input{'profession'}) { $input{'profession'} = ""; }
	if (!defined $input{'websiteurl'}) { $input{'websiteurl'} = ""; }
	if (!defined $input{'websitetitle'}) { $input{'websitetitle'} = ""; }
	if (!defined $input{'signature'}) { $input{'signature'} = ""; }
	if (!defined $input{'settings6'}) { $input{'settings6'} = ""; }
	if (!defined $input{'settings8'}) { $input{'settings8'} = ""; }
	if (!defined $input{'settings10'}) { $input{'settings10'} = ""; }
	if (!defined $input{'settings11'}) { $input{'settings11'} = ""; }
	if (!defined $input{'settings12'}) { $input{'settings12'} = ""; }
	if (!defined $input{'about'}) { $input{'about'} = ""; }
	if (!defined $input{'fav'}) { $input{'fav'} = ""; }
	if (!defined $memsettings[7]) { $memsettings[7] = ""; }
	if (!defined $memsettings[14]) { $memsettings[14] = ""; }
	if (!defined $input{'moda'}) { $input{'moda'} = ""; }
	if (!defined $input{'icq'}) { $input{'icq'} = ""; }
	if (!defined $input{'yahoo'}) { $input{'yahoo'} = ""; }
	if (!defined $input{'user_check_date'}) { $input{'user_check_date'} = ""; }
	if (!defined $input{'user_check_time'}) { $input{'user_check_time'} = ""; }
	if (!defined $input{'preferences[6]'}) { $input{'preferences[6]'} = ""; }

	if ($info{'username'} =~ /\//) { error("$err{'004'}" ); }
	if ($input{'passwrd1'} ne "$input{'passwrd2'}") { error("$err{'012'}"); }
	if ($input{'passwrd1'} eq "") { error("$err{'009'}"); }
	if ($input{'name'} eq "") { error("$err{'013'}"); }
	if ($input{'name'} !~ /^[0-9A-Za-z#%+,-\.:=?@^_ ]+$/ || $input{'name'} eq "|" || $input{'name'} =~ /$anonuser/i) { error("$err{'006'}"); }
	if ($input{'email'} eq "") { error("$err{'005'}"); }
	if ($input{'theme'} eq "") { $input{'theme'} = "$defaulttheme"; }
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
	if ($username eq "admin") {
		if ($input{'broadcastmessage'} eq "on") { $input{'broadcastmessage'} = "1";
		} else { $input{'broadcastmessage'} = "0"; }
		if ($input{'broadcastmessage'} eq "1" && $input{'saybroadcast'} eq "") {
		error("$err{'015'}"); }
	}

	if ($infoblockmod eq 2) { $input{'infoblock'} = "1"; }
	if ($dispfrad eq 2) { $input{'freeadblock'} = "1"; }

	if ($input{'memberpicpersonalcheck'} && ( $input{'memberpicpersonal'} =~ m/\.gif\Z/i || $input{'memberpicpersonal'} =~ m/\.jpg\Z/i || $input{'memberpicpersonal'} =~ m/\.jpeg\Z/i || $input{'memberpicpersonal'} =~ m/\.png\Z/i ) ) {
		$input{'memberpic'} = $input{'memberpicpersonal'};
	}
	if ($input{'memberpic'} !~ m^\A[0-9a-zA-Z_\.\#\%\-\:\+\?\$\&\~\.\,\@/]+\Z^) { error("$err{'006'}"); }
	if ($input{'ages'} eq "") { $ages = "";
	} else { $ages = "$input{'ages'}"; }
	if ($input{'marstat'} eq "") { $marstat = "";
	} else { $marstat = "$input{'marstat'}"; }
	if ($input{'aim'} eq "") { $aim = "";
	} else { $aim = "$input{'aim'}"; }
	if ($input{'state'} eq "") { $state = "";
	} else { $state = "$input{'state'}"; }
	if ($input{'gen'} eq "") { $gen = "";
	} else { $gen = "$input{'gen'}"; }
	if ($input{'profession'} eq "") { $profession = "";
	} else { $profession = "$input{'profession'}"; }
	open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
	hold(FILE);
	chomp(@memsettings = <FILE>);
	release(FILE);
	close(FILE);

	if ($input{'passwrd1'} eq $memsettings[0]) { $passwrd = $input{'passwrd1'}; }

### begin Carters new password encryption: ###
	else {
		$cryptedpass = crypt($input{'passwrd1'}, substr($input{'username'}, 0, 2)); 
		use Babel;
	
		$y = new Babel;
		$passwrd = $y->encode($cryptedpass, "$input{'passwrd1'}");
	}
### end Carters new password encryption ###

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
	if ($input{'fav'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	if ($input{'profession'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	if ($input{'gen'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	if ($input{'marstat'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	if ($input{'state'} =~ /(\<s+|\<S+|\<j+|\<J)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	if ($username ne "admin") {
		$input{'settings7'} =  $memsettings[7];     # RANK
		$input{'settings6'} =  $memsettings[6];     # FORUMPOSTS
		$input{'settings10'} =  $memsettings[10];   # MEMBERSINCE
		$input{'settings11'} =  $memsettings[11];   # ARTICLES
		$input{'settings12'} =  $memsettings[12];   # COMMENTS
		$input{'settings14'} =  $memsettings[14];   # STATUS
	}

	if ($input{'moda'} eq "$btn{'047'}") {

		if ($username ne "admin") { #jos

			if ($realname ne $input{'name'} ) { #on
				open(FILE, "$memberdir/memberlist.dat");
				@memberlist = <FILE>;
				close(FILE);
				foreach $curmember (@memberlist) {
	         	$curmember =~ s/[\n\r]//g;
					open(FILE, "$memberdir/$curmember.dat");
					@memberinfo = <FILE>;
					$memberinfo[1] =~ s/[\n\r]//g;
					$checkname = $input{'name'};
					if (grep (/\b^$checkname\b/, $memberinfo[1]) ne "0" ) {
						error("$err{'004'}");
					}
				}
				close(FILE);
			} #on to here

			open(FILE,"$memberdir/restrictedmemberlist.dat") || &die("I can't open user database\n");
			while(<FILE>) {
				chop;
				@allnames = split(/\n/);
				$checkusername = $input{'name'};
				if (grep (/^$checkusername/i, @allnames) ne "0") { error("$err{'004'}"); }
			}
			close(FILE);
		} #anton to here

		open(FILE, ">$memberdir/$username.dat") || error("$err{'016'} $input{'username'}.dat");
		hold(FILE);
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
		print FILE "$memsettings[7]\n";
		print FILE "$input{'icq'}\n";
		print FILE "$input{'memberpic'}\n";
		print FILE "$memsettings[10]\n";
		print FILE "$memsettings[11]\n";
		print FILE "$memsettings[12]\n";
		print FILE "$input{'theme'}\n";

		if ($username eq "admin") {
			print FILE "$memsettings[14]\n";
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
		release(FILE);
		close(FILE);

		open(FILE, ">$memberdir/$username.pref") || error("$err{'016'} $username.pref");
		hold(FILE);
		print FILE "$input{'impopup'}\n";
		print FILE "$input{'infoblock'}\n";
		print FILE "$input{'freeadblock'}\n";
		print FILE "$input{'welcomemessage'}\n";

		if ($username eq "admin") {
			print FILE "$input{'broadcastmessage'}\n";
			print FILE "$input{'saybroadcast'}\n";
		} else {
			print FILE "0\n";
			print FILE "\n";
		}
		print FILE "$input{'preferences[6]'}\n";
		print FILE "$input{'showlegend'}\n";

 	 	release(FILE);
	 	close(FILE);

		open(FILE, "$memberdir/$username.dat");
		hold(FILE);
		@settings = <FILE>;
		release(FILE);
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

	if (!defined $input{'delt'}) { $input{'delt'} = ""; }
	if ($input{'delt'} eq "$btn{'007'}") { areyou_sure(); }

}

#################
sub viewprofile {
#################

	if ($info{'username'} =~ /\//) { error("$err{'004'}"); }
	if ($info{'username'} =~ /\\/) { error("$err{'004'}"); }
	if ($username eq $anonuser) { error("noguests"); }
	if ($username ne "admin") {
		if ($hidememlist eq "1" && $username ne $info{'username'}) { error("$err{'011'}"); }
	}

	open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
	hold(FILE);
	chomp(@memsettings = <FILE>);
	release(FILE);
	close(FILE);

	if ($memsettings[9] =~ /^http:\/\// ) {
		if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
		else { $tmp_width = ""; }
		if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
		else { $tmp_height = ""; }
		$memberpic = qq~<a href="$memsettings[9]" target="_blank"><img
 src="$memsettings[9]" $tmp_width $tmp_height border="0" alt="click for actual size"></a>~;
	} else {
	if ($memsettings[9] eq "") { $memsettings[9] = "_nopic.gif"; }
		$memberpic = qq~<img src="$imagesurl/avatars/$memsettings[9]" border="0" alt="">~;
	}

	open(FILE, "$memberdir/membergroups.dat");
	hold(FILE);
	@membergroups = <FILE>;
	release(FILE);
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
	hold(FILE);
	chomp(@memsettings = <FILE>);
	release(FILE);
	close(FILE);
	$ssettings1 = $memsettings[1];
	$ssettings3 = $memsettings[3];
	$ssettings4 = $memsettings[4];
	$ssettings6 = $memsettings[6];
	$ssettings7 = $memsettings[7];
	$ssettings8 = $memsettings[8];
	$ssettings10 = $memsettings[10];
	$ssettings11 = $memsettings[11];
	$ssettings12 = $memsettings[12];
	$ssettings14 = $memsettings[14];
	$ssettings16 = $memsettings[16]; # about
	$ssettings17 = $memsettings[17];
	$ssettings18 = $memsettings[18];
	$ssettings19 = $memsettings[19];
	$ssettings20 = $memsettings[20];
	$ssettings21 = $memsettings[21];
	$ssettings22 = $memsettings[22];
	$ssettings23 = $memsettings[23];
	$ssettings24 = $memsettings[24];
	$lastvisited = readlog("Last_Visited","$info{'username'}");
	if ($lastvisited eq "") {
		$lastvisited = $ssettings10;
	}
	display_date($lastvisited);
	$lastvisited = $user_display_date;
	if ($ssettings10 ne "forever") {
		$membersince = display_date($ssettings10);
	} else {
		$membersince = "forever";
	}

	$navbar = "$btn{'014'} $nav{'017'} $btn{'014'} $ssettings1";
	print_top();

	$about = "$ssettings16";
	$about =~ s/&&/<br>/g;

	print qq~<table cellpadding="3" cellspacing="3" width="100%" border="0">
<tr>
<td width="20%" align="center">$memberpic</td>
<td width="80%" valign="top"><table cellpadding="2" cellspacing="2" border="0">
<tr>
<td width="25%" class="forumwindow3">$msg{'013'}</td>
<td width="75%" class="forumwindow1" style="white-space: nowrap">$ssettings1</td>
</tr>
<tr>
~;

	if ((defined $ssettings22) && ($ssettings22 ne "")) {
		print qq~<td class="forumwindow3">$msg{'650'}:</td>
<td class="forumwindow1" style="white-space: nowrap">$ssettings22</td>
</tr>
<tr>
~;
	}
	if ($ssettings17 ne "") {
		print qq~<td class="forumwindow3">$msg{'651'}:</td>
<td class="forumwindow1" style="white-space: nowrap">$ssettings17</td>
</tr>
<tr>
~;
	}
	if ($ssettings19 ne "") {
		print qq~<td class="forumwindow3">$msg{'652'}:</td>
<td class="forumwindow1" style="white-space: nowrap">$ssettings19</td>
</tr>
<tr>
~;
	}
	if ($ssettings21 ne "") {
		print qq~<td class="forumwindow3">$msg{'653'}:</td>
<td class="forumwindow1" style="white-space: nowrap">$ssettings21</td>
</tr>
<tr>
~;
	}
	if ($ssettings20 ne "") {
		print qq~<td class="forumwindow3">$msg{'654'}:</td>
<td class="forumwindow1" style="white-space: nowrap">$ssettings20</td>
</tr>
<tr>
~;
	}
	if ($ssettings4 ne "") {
		print qq~<td class="forumwindow3">$msg{'014'}</td>
<td class="forumwindow1" style="white-space: nowrap"><a
 href="$ssettings4" target="_blank">$ssettings3</a></td>
</tr>
<tr>
~;
	}
	print qq~<td class="forumwindow3" style="white-space: nowrap">$msg{'027'}</td>
<td class="forumwindow1" style="white-space: nowrap">$membersince</td>
</tr>
</table></td>
</tr>
</table>

<table align="center" width="98%" cellpadding="3" cellspacing="2" border="0">
~;
	if ($ssettings16 ne "") {
		print qq~<tr>
<td class="forumwindow3" valign="top" width="25%">$msg{'655'}:</td>
<td class="forumwindow1" valign="top" width="75%">$about</font></td>
</tr>
~;
	}
	if ($ssettings18 ne "") {
		print qq~<tr>
<td class="forumwindow3" valign="top">$msg{'656'}:</td>
<td class="forumwindow1" valign="top">$ssettings18</td>
</tr>
~;
	}
	print qq~</table>
~;

	print qq~<table cellpadding="2" cellspacing="2" width="100%" border="0">
<tr>
<td class="forumwindow1" width="50%" colspan="2">$msg{'024'}&nbsp;$memberinfo</td>
<td class="forumwindow1" width="50%" colspan="2">$msg{'178'}:&nbsp;~;
	if ($ssettings14 ne "") {
		print qq~$ssettings14~;
	} else {
		print qq~n/a~;
	}
	print qq~</td>
</tr>
<tr>
<td class="forumwindow1" width="25%">~;
	if ($ssettings11 ne "0") {
		print qq~$msg{'022'}&nbsp;<a
 href="$scripturl/$cgi?action=otherarticles&amp;writer=$info{'username'}&amp;real=$ssettings1">$ssettings11</a>~;
	} else {
		print qq~$msg{'022'}&nbsp;$ssettings11~;
	}
	print qq~</td>
<td class="forumwindow1" width="25%">$msg{'023'}&nbsp;$ssettings12</td>
<td class="forumwindow1" width="25%">$msg{'021'}&nbsp;$ssettings6</td>
<td class="forumwindow1" width="25%">&nbsp;</td>
</tr>
~;

	open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
	hold(FILE);
	@categories = <FILE>;
	release(FILE);
	close(FILE);

	open(FILE, "$memberdir/memberlist.dat") || error("$err{'001'} $memberdir/memberlist.dat");
	hold(FILE);
	@memberlist = <FILE>;
	release(FILE);
	close(FILE);

	$totalm = 0;
	$totalt = 0;

	foreach $curcat (@categories) {
		$curcat =~ s/[\n\r]//g;

		open(FILE, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
		hold(FILE);
		@catinfo = <FILE>;
		release(FILE);
		close(FILE);

		$catinfo[1] =~ s/[\n\r]//g;
		if ($catinfo[1] ne "") {
			if ($userrank ne "$root" && $userrank ne "$catinfo[1]") { next; }
		}

		$curcatname = "$catinfo[0]";
		foreach $curboard (@catinfo) {
			if ($curboard ne "$catinfo[0]" && $curboard ne "$catinfo[1]") {
				$curboard =~ s/[\n\r]//g;

				open(FILE, "$boardsdir/$curboard.txt") || error("$err{'001'} $boardsdir/$curboard.txt");
				hold(FILE);
				chomp(@messages = <FILE>);
				release(FILE);
				close(FILE);

				$tm = @messages;

				$postdate = (split(/\|/, $messages[0]))[5];
				$messagecount = 0;
				for ($a = 0; $a < @messages; $a++) {
					$mreplies = (split(/\|/, $messages[$a]))[6];
					$messagecount++;
					$messagecount = $messagecount+$mreplies;
				}
				$totalm = $totalm+$messagecount;
			}
		}
	}
	$pcoftotpost = 0;
	$msgpd = 0;
	if ($ssettings6 ne "0" && $totalm ne "0") {
		$pcoftotpost = sprintf("%.2f",(100/$totalm)*$ssettings6);
	}
	if ($ssettings10 ne "forever") {
		$date2 = $date; $date1 = $ssettings10;	calcdifference(); $tdmem = $result;
	} else {
		require "$sourcedir/stats.pl"; parse_log();
		$tdmem = $total_days;
	}
	if ($ssettings6 ne "0" && $tdmem ne "0") {
		$msgpd = sprintf("%.2f",($ssettings6/$tdmem));
	}

	print qq~<tr>
<td colspan="4" align="center" class="forumwindow1">$ssettings1 $msg{'588'}  $tdmem $msg{'589'}</td>
</tr>
<tr>
<td colspan="2" align="center" class="forumwindow1" width="50%">$ssettings1 $msg{'590'} $msgpd $msg{'591'}</td>
<td colspan="2" align="center" class="forumwindow1" width="50%">$msg{'592'} $pcoftotpost% $msg{'593'}</td>
</tr>~;
	if ($username ne $anonuser) {
		print qq~<tr>
<td colspan="4" align="center" class="forumwindow3"><a
 href="$pageurl/$cgi?action=anonemail&sendto=$info{'username'}">$msg{'394'}</a></td>
</tr>
~;
	}

	if (!defined $ssettings8) { $ssettings8 = ""; }
	if (!defined $ssettings23) { $ssettings23 = ""; }
	if (!defined $ssettings24) { $ssettings24 = ""; }

	if ($ssettings8 eq "" &&  $ssettings23 eq "" && $ssettings24 eq "") { $msgspan1 = "4"; }
	if ($ssettings8 ne "" &&  $ssettings23 eq "" && $ssettings24 eq "") { $msgspan1 = "3"; }
	if ($ssettings8 eq "" &&  $ssettings23 ne "" && $ssettings24 eq "") { $msgspan1 = "3"; }
	if ($ssettings8 eq "" &&  $ssettings23 eq "" && $ssettings24 ne "") { $msgspan1 = "3"; }
	if ($ssettings8 ne "" &&  $ssettings23 ne "" && $ssettings24 eq "") { $msgspan1 = "2"; }
	if ($ssettings8 ne "" &&  $ssettings23 eq "" && $ssettings24 ne "") { $msgspan1 = "2"; }
	if ($ssettings8 eq "" &&  $ssettings23 ne "" && $ssettings24 ne "") { $msgspan1 = "2"; }
	if ($ssettings8 ne "" &&  $ssettings23 ne "" && $ssettings24 ne "") { $msgspan1 = "1"; }

	print qq~<tr>
<td class="forumwindow3" align="center" colspan="$msgspan1">~;

	if ($username ne $anonuser) {
		print qq~<a
 href="$pageurl/$cgi?action=imsend&amp;to=$info{'username'}">$nav{'018'}</a></b>~;
	}
	print qq~&nbsp;</td>
~;
	if ($ssettings8 ne "") {
		print qq~<td align="center" class="forumwindow3" style="white-space: nowrap"><a href="http://www.icq.com/$ssettings8" target="_blank"><img src="http://web.icq.com/whitepages/online?icq=$ssettings8&img=5" alt="$msg{'052'} $ssettings1" border="0"></a></td>
~;
	}
	if ($ssettings23 ne "") {
		print qq~<td align="center" class="forumwindow3" align="center"><a href="aim:goim?screenname=$ssettings23&amp;message=Hi.+Are+you+there?"><img src="$imagesurl/aimyel_im.gif" alt="$msg{'661'} $ssettings1" border="0"></a></td>
~;
	}
	if ($ssettings24 ne "") {
		print qq~<td align="center" class="forumwindow3" align="center"><a href="http://edit.yahoo.com/config/send_webmesg?.target=$ssettings24&.src=pg"><img border="0" src="http://opi.yahoo.com/online?u=$ssettings24&m=g&t=1" alt="$msg{'662'} $ssettings1"></a></td>
~;
	}

	print qq~
</tr>
<tr>
<td align="center" class="forumwindow1" colspan="4" width="100%">$msg{'535'}: $lastvisited</td>
</tr>
<tr>
<td align="center" class="forumwindow3" colspan="4" width="100%">~;

	if ($username eq "admin" && $info{'username'} ne "admin") {
		print qq~<a href="$pageurl/$cgi?action=admineditprofile&amp;username=$info{'username'}">$nav{'161'}</a>~;
	} else {
		if ($info{'username'} eq $username) {
			print qq~<a href="$pageurl/$cgi?action=editprofile2&amp;username=$info{'username'}">$nav{'161'}</a>~;
		}
	}

	print qq~</td>
</tr>
</table>
<br>
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
<a href="$pageurl/$cgi?action=deleteprofile&deleteduser=$input{'username'}" class="formslink">$nav{'047'}</a> - <a href="$pageurl/$cgi?action=editprofile2&username=$input{'username'}" class="formslink">$nav{'048'}</a>
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
		hold(FILE);
		chomp(@members = <FILE>);
		release(FILE);
		close(FILE);

		open(FILE, ">$memberdir/memberlist.dat");
		hold(FILE);
		foreach $curmem (@members) {
			if ($curmem ne $deleteduser) { print FILE "$curmem\n"; }
		}
		release(FILE);
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
	if ($username ne "admin") { error("$err{'011'}"); }

		$deleteduser = $info{'deleteduser'};

		if ($deleteduser ne "admin") {
		unlink("$memberdir/$deleteduser.dat");
		unlink("$memberdir/$deleteduser.msg");
		unlink("$memberdir/$deleteduser.log");
		unlink("$memberdir/$deleteduser.pref");

		open(FILE, "$memberdir/memberlist.dat");
		hold(FILE);
		chomp(@members = <FILE>);
		release(FILE);
		close(FILE);

		open(FILE, ">$memberdir/memberlist.dat");
		hold(FILE);
		foreach $curmem (@members) {
			if ($curmem ne $deleteduser) { print FILE "$curmem\n"; }
		}
		release(FILE);
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

