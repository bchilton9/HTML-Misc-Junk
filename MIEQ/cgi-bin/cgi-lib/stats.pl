###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# stats.pl                                        	             	      #
# v0.9.9 - Requin                  								#
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
# File: Last modified: 08/01/02                                               #
###############################################################################
###############################################################################

# reformatting of HTML by Brad (webmaster@indie-central.ca) 07 May 2002
# also added newest user and download information
# added test for admin if Statistics Link is Hidden - Floyd 05/11/02

###########
sub stats {
###########

	#if ($dispstat eq "0" && $username ne "admin") { error("$err{'011'}"); }
	#if ($dispstat eq "1" && $username eq "$anonuser") { error("$err{'011'}"); }

	$|++;
	$navbar = "$btn{'014'} $nav{'006'}";
	parse_log();
	print_top();
	print qq~<BR><table border="0" cellpadding="5" cellspacing="0" width="100%"><tr><td valign="top" width="50%">~;	
	topbar();
	print qq~</td>~;#<td valign="top" width="50%">~;
	#html_browser();
	print qq~</tr><tr><td valign="top" width="50%">~;
	site_stats();
	print qq~</td>~;#<td valign="top" width="50%">~;
	#os_system();
	print qq~</tr></table>~;
	print_bottom();
	exit;
}

###############
sub parse_log {
###############
	open(DATA,"$logdir/stats.dat") || error("$err{'001'} $logdir/stats.dat");
	@lines = <DATA>;
	close(DATA);
	$total = @lines;
	foreach $line (@lines) {
		if ($line =~ /(.*) - (.*) - \"(.*)\" - \"(.*)\"/) {
			$date = $1;
			($weekday, $day, $time) = split(/ /, $date);
			($hour, $minute) = split(/:/, $time);
			($temp, $month,$year) = split (/-/, $day);
			$host_name = $2;
			$user_agent = $3;
			$referer = $4;
			$day = "$day "."$weekday";
			$referer{$referer}++;
			$day{$day}++;
			$week_days{$weekday}++;
			$hour{$hour}++;
			push(@USER_AGENT, $user_agent);
		}
	}
	$total_agent = @USER_AGENT;
	if ($top_os == 1) {
		$os{'Windows'} = 0;
		$os{'Mac/PPC'} = 0;
		$os{'Linux'} = 0;
		$os{'SunOS'} = 0;
		$os{'BSD'} = 0;
		$os{'AIX'} = 0;
		$os{'OS/2'} = 0;
		$os{'Irix'} = 0;
		$os{'BeOS'} = 0;
		$os{"$msg{'067'}"} = 0;

		foreach $user_agent (@USER_AGENT) {
			if ($user_agent =~ /MSIE/i) {
				if ($user_agent =~ /Windows 98/i) {
					$os{'Windows'}++;
					next;
				}
				elsif ($user_agent =~ /Windows NT/i) {
					$os{'Windows'}++;
					next;
				}
				elsif ($user_agent =~ /Windows 95/i) {
					$os{'Windows'}++;
					next;
				}
				elsif ($user_agent =~ /Mac_PowerPC/i || $user_agent =~ /Macintosh/i) {
					$os{'Mac/PPC'}++;
					next;
				}
			}
			elsif  ($user_agent =~ /Win98/i || $user_agent =~ /Windows 98/i) {
				$os{'Windows'}++;
		   		next;
			}
			elsif  ($user_agent =~ /WinNT/i || $user_agent =~ /Windows NT/i) {
				$os{'Windows'}++;
				next;
			}
			elsif  ($user_agent =~ /Win95/i || $user_agent =~ /Windows 95/i) {
				$os{'Windows'}++;
				next;
			}
			elsif ($user_agent =~ /Mac_PowerPC/i || $user_agent =~ /Macintosh/i) {
				$os{'Mac/PPC'}++;
				next;
			}
			elsif  ($user_agent =~ /X11/i) {
				if  ($user_agent =~ /Linux/i) {
					$os{'Linux'}++;
					next;
				}
				elsif  ($user_agent =~ /SunOS/i) {
					$os{'SunOS'}++;
					next;
			   	}
			   	elsif  ($user_agent =~ /AIX/i) {
			   		$os{'AIX'}++;
		   			next;
	   			}
				elsif  ($user_agent =~ /Amiga/i) {
					$os{'Irix'}++;
					next;
				}
			   	else {
	   				$os{'BSD'}++;
		   			next;
			   	}
			}
			elsif  ($user_agent =~ /Linux/i) {
				$os{'Linux'}++;
				next;
			}
			elsif  ($user_agent =~ /Win16/i || $user_agent =~ /Windows 3\.1/i) {
				$os{'Windows'}++;
				next;
			}
			elsif  ($user_agent =~ /OS\/2/i) {
				$os{'OS/2'}++;
				next;
			}
			elsif  ($user_agent =~ /BeOS/i) {
				$os{'BeOS'}++;
				next;
			}
			else {
				$os{"$msg{'067'}"}++;
				next;
			}
		}
	}
	if ($top_browsers == 1) {
		$browser{'Opera'} = 0;
		$browser{'Lynx'} = 0;
		$browser{'MSIE'} = 0;
		$browser{"$msg{'066'}"} = 0;
		$browser{'Konqueror'} = 0;
		$browser{'WebTV'} = 0;
		$browser{'Netscape'} = 0;
		$browser{"$msg{'067'}"} = 0;

		foreach $agent (@USER_AGENT) {
			if ($agent =~ /Opera/i) {
				$browser{'Opera'}++;
				next;
			}
			elsif ($agent =~ /Lynx/i) {
				$browser{"Lynx"}++;
				next;
			}
			elsif ($agent =~ /Konqueror\/(\d)/i || $agent =~ /Konqueror (\d)/i) {
				$browser{"Konqueror"}++;
				next;
			}
			elsif ($agent =~ /MSIE/i) {
				if ($agent =~ /MSIE (\d)/i) {
					$browser{"MSIE"}++;
					next;
				}
				else {
					$browser{"$msg{'066'}"}++;
				}
			}
			elsif ($agent =~ /Mozilla/i) {
				if ($agent =~ /Mozilla\/5/i || $agent =~ /Mozilla 5/i) {
					$browser{'Netscape'}++;
					next;
				}
				elsif ($agent =~ /Mozilla\/(\d)/i || $agent =~ /Mozilla (\d)/i) {
					$browser{"Netscape"}++;
					next;
				}
				else {
					$browser{"$msg{'066'}"}++;
				}
			}
			elsif ($agent ne "") {
				$browser{"$msg{'067'}"}++;
				next;
			}
			else {
				$browser{"$msg{'067'}"}++;
			}
		}
	}
	foreach $count (keys %day) {
		$total_days++;
	}
	$hits_per_day = sprintf ("%.2f",($total/$total_days));
	$hits_per_hour = sprintf ("%.2f",($total/$total_days/24));
}

############
sub topbar {
############

open(MEMBERS, "$memberdir/memberlist.dat");
	file_lock(MEMBERS);
	@memberlist = <MEMBERS>;
	$mcount = @memberlist;
	unfile_lock(MEMBERS);
close(MEMBERS);

open(MEMBERS, "$memberdir/memberlist.dat");
	file_lock(MEMBERS);
	chomp(@memberlist = <MEMBERS>);	
	unfile_lock(MEMBERS);
close(MEMBERS);

$thelatestmember = $memberlist[$#memberlist];

open(FILE, "$memberdir/$thelatestmember.dat");
	file_lock(FILE);
	chomp(@lmsettings = <FILE>);
	unfile_lock(FILE);
close(FILE);	

$tlmname = @lmsettings[1];

print qq~
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable" background="$themesurl/$usertheme/images/boxhead.gif">
<tr>
<td>&nbsp;$btn{'014'}&nbsp;$pagename</td>
</tr>
</table>
<table border="0" cellpadding="1" cellspacing="0" width="100%" height="100%" class="menubordercolor">
<tr>
<td>
<table border="0" cellpadding="3" cellspacing="0" width="100%" height="100%" class="menubackcolor">
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/forum/ip.gif" align="absmiddle">&nbsp;$msg{'068'}</td>
<td width="10%" class="statstextbold">$total</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/forum/exclamation.gif" align="absmiddle">&nbsp;$msg{'069'}</td>
<td width="10%" class="statstextbold">$total_days</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/forum/smilies/eek.gif" align="absmiddle">&nbsp;$msg{'070'}</td>
<td width="10%" class="statstextbold">$hits_per_day</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/forum/smilies/smile.gif" align="absmiddle">&nbsp;$msg{'071'}</td>
<td width="10%" class="statstextbold">$hits_per_hour</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/forum/thumbup.gif" align="absmiddle">&nbsp;$msg{'074'}</td>
<td width="10%" class="statstextbold">$mcount</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/forum/lamp.gif" align="absmiddle">&nbsp;$msg{'028'}</td>
~;
if ($username ne "$anonuser") {
	print qq~<td width="10%"><b><a href="$cgi?action=viewprofile&amp;username=$thelatestmember"  class="menu">$tlmname</a></b></td>~;
}
else {
	print qq~<td width="10%" class="statstextbold">$tlmname</td>~;
}
print qq~
</tr>
</table>
</td>
</tr>
</table>
~;
}

##################
sub html_browser {
##################
	print qq~
	<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable" background="$themesurl/$usertheme/images/boxhead.gif">
<tr>
<td>&nbsp;$btn{'014'}&nbsp;$msg{'072'}</td>
</tr>
</table>
<table border="0" cellpadding="1" cellspacing="0" width="100%" height="100%" class="menubordercolor">
<tr>
<td>
<table border="0" cellpadding="3" cellspacing="0" width="100%" height="100%" class="menubackcolor">
~;
	my $flag=0;
	my $num=0;
	my ($top_pos, $img_width, $percent);
	foreach $brow (sort { $browser{$b} <=> $browser{$a} } keys %browser) {
		$top_pos = $browser{$brow} if ($flag == 0);
		$img_width = int($browser{$brow}*100/$top_pos);
		$percent = sprintf ("%.2f", ($browser{$brow}/$total_agent*100));
		$brow_pic = $brow;
		$brow_pic =~ tr/A-Z/a-z/;
		if ($brow eq "$msg{'066'}") { $brow_pic = "searchengines"; }
		if ($brow eq "$msg{'067'}") { $brow_pic = "unknown"; }
		print qq~<tr>
<td><img src="$imagesurl/stats/$brow_pic.gif" alt=""></td>
<td width="90" class="statstext">$brow</td><td align="center" class="statstextbold">$browser{$brow}</td>
<td align="left" class="statstext">($percent\%)</td>
<td><img src="$imagesurl/leftbar.gif" width="7" height="14" alt="$percent\%"><img src="$imagesurl/mainbar.gif" width="$img_width" height="14" alt="$percent\%"><img src="$imagesurl/rightbar.gif" width="7" height="14" alt="$percent\%"></td>
</tr>
~;
		$flag = 1;
	}
	print qq~</table>
	</td>
</tr>
</table>~;
}

###############
sub os_system {
###############
	print qq~
	<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable" background="$themesurl/$usertheme/images/boxhead.gif">
<tr>
<td>&nbsp;$btn{'014'}&nbsp;$msg{'073'}</td>
</tr>
</table>
<table border="0" cellpadding="1" cellspacing="0" width="100%" height="100%" class="menubordercolor">
<tr>
<td>
<table border="0" cellpadding="3" cellspacing="0" width="100%" height="100%" class="menubackcolor">
~;
	my $flag = 0;
	my $num = 0;
	my ($top_pos, $img_width, $percent);
	foreach $os_sys (sort { $os{$b} <=> $os{$a} } keys %os) {
		$top_pos = $os{$os_sys} if ($flag == 0);
		$img_width = int($os{$os_sys}*100/$top_pos);
		$percent = sprintf ("%.2f", ($os{$os_sys}/$total_agent*100));
		$os_pic = $os_sys;
		$os_pic =~ tr/A-Z/a-z/;
		if ($os_pic eq "mac/ppc") { $os_pic = "mac"; }
		if ($os_pic eq "os/2") { $os_pic = "os2"; }
		if ($os_sys eq "$msg{'067'}") { $os_pic = "unknown"; }
		print qq~<tr>
<td><img src="$imagesurl/stats/$os_pic.gif" alt=""></td>
<td width="90" class="statstext">$os_sys</td><td align="center" class="statstextbold">$os{$os_sys}</td>
<td align="left" class="statstext">($percent\%)</td>
<td><img src="$imagesurl/leftbar.gif" width="7" height="14" alt="$percent\%"><img src="$imagesurl/mainbar.gif" width="$img_width" height="14" alt="$percent\%"><img src="$imagesurl/rightbar.gif" width="7" height="14" alt="$percent\%"></td>
</tr>
~;
		$flag = 1;
	}
	print qq~</table>
	</td>
</tr>
</table>~;
}

################
sub site_stats {
################

	undef @catnames;
	undef @catlinks;

	open(TOPICS, "$topicsdir/cats.dat");
	file_lock(TOPICS);
	chomp(@topicscat = <TOPICS>);
	unfile_lock(TOPICS);
	close(TOPICS);
	for ($i = 0; $i < @topicscat; $i++) { $topicscatcount++; }

	foreach (@topicscat) {
		@item = split(/\|/, $_);
		push(@catnames, $item[0]);
		push(@catlinks, $item[1]);
	}

	foreach $curcat (@catlinks) {
		open(FILE, "$topicsdir/$curcat.cat");
		file_lock(FILE);
		chomp(@articles = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		$articlecount = 0;
		for ($a = 0; $a < @articles; $a++) {
			($dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $areplies) = split(/\|/, $articles[$a]);
			$articlecount++;
			$repcount = $repcount+$areplies;
		}
		$totala = $totala+$articlecount;
		if ($repcount == 0) { $repcount = "0"; }
	}

	open (NEWARTICLES, "$topicsdir/newarticles.dat");
	file_lock(NEWARTICLES);
	@newarticles = <NEWARTICLES>;
	unfile_lock(NEWARTICLES);
	close(NEWARTICLES);
	if (@newarticles == 0) { $newarticlescount = "0"; }
	for ($i = 0; $i < @newarticles; $i++) { $newarticlescount++; }

	open(FILE, "$boardsdir/cats.txt");
	file_lock(FILE);
	chomp(@categories = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	$totalm = 0;
	$totalt = 0;
	foreach $curcat (@categories) {
		open(FILE, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
		file_lock(FILE);
		chomp(@catinfo = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		if ($catinfo[1] ne "") {
			if ($settings[7] ne $userlevel[0] && $settings[7] ne $catinfo[1]) { next; }
		}

		$curcatname = "$catinfo[0]";

		foreach $curboard (@catinfo) {
			if ($curboard ne $catinfo[0] && $curboard ne $catinfo[1]) {

				open(FILE, "$boardsdir/$curboard.txt") || error("$err{'001'} $boardsdir/$curboard.txt");
				file_lock(FILE);
				chomp(@messages = <FILE>);
				unfile_lock(FILE);
				close(FILE);

				$tm = @messages;
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

	open(LNKCAT, "$linksdir/linkcats.dat");
	file_lock(LNKCAT);
	@lnkcatscount = <LNKCAT>;
	unfile_lock(LNKCAT);
	close(LNKCAT);
	$lnkcatscount = 0;
	for ($i = 0; $i < @lnkcatscount; $i++) { $lnkcatscount++; }

	open(LNKCNT, "$linksdir/linkcats.cnt");
	file_lock(LNKCNT);
	$lnkcount = <LNKCNT>;
	unfile_lock(LNKCNT);
	close(LNKCNT);
	
	open(CNT, "$downloadsdir/downloadcats.cnt") || error("$err{'001'} $downloadsdir/downloadcats.cnt");
		file_lock(CNT);
		$dlcount = <CNT>;
		unfile_lock(CNT);
	close(CNT);

	print qq~
	<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable" background="$themesurl/$usertheme/images/boxhead.gif">
<tr>
<td>&nbsp;$btn{'014'}&nbsp;$msg{'149'}</td>
</tr>
</table>
<table border="0" cellpadding="1" cellspacing="0" width="100%" height="100%" class="menubordercolor">
<tr>
<td>
<table border="0" cellpadding="3" cellspacing="0" width="100%" height="100%" class="menubackcolor">
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/topics.gif" align="absmiddle" alt="">&nbsp;$msg{'075'} </td>
<td width="10%" class="statstextbold">$topicscatcount</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/articles.gif" align="absmiddle" alt="">&nbsp;$msg{'076'} </td>
<td width="10%" class="statstextbold">$totala</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/waiting.gif" align="absmiddle" alt="">&nbsp;$msg{'077'} </td>
<td width="10%" class="statstextbold">$newarticlescount</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/comments.gif" align="absmiddle" alt="">&nbsp;$msg{'078'} </td>
<td width="10%" class="statstextbold">$repcount</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/topics.gif" align="absmiddle" alt="">&nbsp;$msg{'079'} </td>
<td width="10%" class="statstextbold">$totalt</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/forummessages.gif" align="absmiddle" alt="">&nbsp;$msg{'080'} </td>
<td width="10%" class="statstextbold">$totalm</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/topics.gif" align="absmiddle" alt="">&nbsp;$msg{'081'}</td>
<td width="10%" class="statstextbold">$lnkcatscount</td>
</tr>
<tr>
<td width="90%" class="statstext"><img src="$imagesurl/stats/links.gif" align="absmiddle" alt="">&nbsp;$msg{'082'} </td>
<td width="10%" class="statstextbold">$lnkcount</td>
</tr>


</table>
	</td>
</tr>
</table>
~;

}

if (-e "$scriptdir/user-lib/stats.pl") {require "$scriptdir/user-lib/stats.pl"} 

1; # return true