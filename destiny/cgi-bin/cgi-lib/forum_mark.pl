###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# forum.pl 						                                    #
# v0.9.9 - Requin                                                             #
#                                                                             #
# Copyright (C) 2002 by WebAPP (webapp@attbi.com)                             #
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
# File: Last modified: 03/26/03                                       		#
###############################################################################
###############################################################################


##################
sub mark_as_read {
##################

if ($info{'board'} eq "") {

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
			if ($settings[14] ne "$root" && $settings[14] ne "$catinfo[1]") {	next; }
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

	foreach $curcat (@categories) {
		$curcat =~ s/[\n\r]//g;

		open(FILE, "$boardsdir/$curcat.cat");
		file_lock(FILE);
		chomp(@catinfo = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		$catinfo[1] =~ s/[\n\r]//g;
		if ($catinfo[1] ne "") {
			if ($settings[14] ne "$root" && $settings[14] ne "$catinfo[1]") { next; }
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
				chomp(@mymessages = <FILE>);
				unfile_lock(FILE);
				close(FILE);
				
				
				open(FILE2, "<$boardsdir/$curboard.sticky");
				file_lock(FILE2);
				chomp(@messagessticky = <FILE2>);
				unfile_lock(FILE2);
				close(FILE2);
				@messages = (@mymessages, @messagessticky);
				

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

				open(FILE, "$memberdir/$boardinfo[2].dat");
				file_lock(FILE);
				chomp(@modprop = <FILE>);
				unfile_lock(FILE);
				close(FILE);

				$boardmoderator = $modprop[1];


		if ($username ne "$anonuser") {
		open(LOG, "$memberdir/$username.log");
		file_lock(LOG);
		@entries = <LOG>;
		unfile_lock(LOG);
		close(LOG);

		open(LOG, ">$memberdir/$username.log");
		file_lock(LOG);
		print LOG "$curboard|$postdate\n";
		foreach $curentry (@entries) {
			$curentry =~ s/[\n\r]//g;
			($name, $value) = split(/\|/, $curentry);
			$date1 = "$value";
			$date2 = "$date";
			calcdifference();
			if ($name ne "$curboard" && $result <= $max_log_days_old) { print LOG "$curentry\n"; }
		}
		unfile_lock(LOG);
		close(LOG);
	}


		}
	}
}

}

else {

$writedate = "$date";
writelog("$currentboard");

}

print "Location: $cgi\?action=forum\&board=$currentboard\n\n"; 

}


#####################
sub mark_posts_read {
#####################

$currentboard = $info{'board'};

if ($currentboard ne "") {

	open (FILE, "$boardsdir/$currentboard.txt") || error("$err{'001'} $boardsdir/$currentboard.txt");
	file_lock(FILE);
	chomp(@mymessages = <FILE>);
	unfile_lock(FILE);
	close(FILE);

				
				open(FILE2, "<$boardsdir/$currentboard.sticky");
				file_lock(FILE2);
				chomp(@messagessticky = <FILE2>);
				unfile_lock(FILE2);
				close(FILE2);
				@messages = (@mymessages, @messagessticky);
				

	$messagecount = 0;

	for ($a = 0; $a < @messages; $a++) {
		($mnum[$a], $msub[$a], $mname[$a], $musername[$a], $memail[$a], $mdate[$a], $mreplies[$a], $mviews[$a], $mlpname[$a], $micon[$a], $mstate[$a]) = split(/\|/, $messages[$a]);
		$messagecount++;

	if ($username ne "$anonuser") {
		open(LOG, "$memberdir/$username.log");
		file_lock(LOG);
		@entries = <LOG>;
		unfile_lock(LOG);
		close(LOG);

		open(LOG, ">$memberdir/$username.log");
		file_lock(LOG);
		print LOG "$mnum[$a]|$mdate[$a]\n";
		foreach $curentry (@entries) {
			$curentry =~ s/[\n\r]//g;
			($name, $value) = split(/\|/, $curentry);
			$date1 = "$value";
			$date2 = "$date";
			calcdifference();
			if ($name ne "$mnum[$a]" && $result <= $max_log_days_old) { print LOG "$curentry\n"; }
		}
		unfile_lock(LOG);
		close(LOG);
	}
	}

}

print "Location: $cgi\?action=forum\&board=$currentboard\n\n"; 

}


if (-e "$scriptdir/user-lib/forum_mark.pl") {require "$scriptdir/user-lib/forum_mark.pl"} 

1; # return true

