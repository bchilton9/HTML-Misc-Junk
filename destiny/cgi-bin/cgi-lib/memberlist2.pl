###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# memberlist.pl                     						      #
# v0.9.9 - Requin                                                             #
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


###########
sub mlist {
###########

	#if ($username eq "$anonuser") { error("$err{'011'}"); }
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
	$users = "";
	$mycount = 0;
	$officercount = 0;
	$friendcount = 0;

	open(FILE, "$datadir/log.dat");
	file_lock(FILE);
	@entries = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	foreach $curentry (@entries) {
		$curentry =~ s/[\n\r]//g;
		($name, $value) = split(/\|/, $curentry);
		if ($name =~ /\./) {  }
		else {
			open(FILE, "$memberdir/$name.dat");
			file_lock(FILE);
			chomp(@msettings = <FILE>);
			unfile_lock(FILE);
			close(FILE);

			$users = qq~$users <a href="$cgi?action=viewprofile&amp;username=$name">$msettings[1]</a>\n~;
		}
	}

	open(FILE, "$memberdir/membergroups.dat");
	file_lock(FILE);
	@membergroups = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	foreach $member (@memberlist) {
		open(FILE, "$memberdir/$member.dat");
		file_lock(FILE);
		chomp(@members = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		$id++;
		$searchname = lc $members[1];
		$posts = $members[6]+$members[11]+$members[12];

		$rank = 3;
		$memberinfo = "$members[14]";

		if ($memberinfo eq "Guild Leader") { $rank = 1; $officercount++; }
		if ($memberinfo eq "Officer") { $rank = 2; $officercount++; }
		if ($memberinfo eq "Member") { $rank = 3; $mycount++; }
		if ($memberinfo eq "Friend") { $rank = 4; $friendcount++; }
		

		#$memberinfo = "$membergroups[2]";
		#$rank = 8;

		#if ($posts > 25) { $memberinfo = "$membergroups[3]"; $rank = 6; }
		#if ($posts > 50) { $memberinfo = "$membergroups[4]"; $rank = 5; }
		#if ($posts > 75) { $memberinfo = "$membergroups[5]"; $rank = 4; }
		#if ($posts > 100) { $memberinfo = "$membergroups[6]"; $rank = 3; }
		#if ($posts > 250) { $memberinfo = "$membergroups[7]"; $rank = 2; }
		#if ($posts > 500) { $memberinfo = "$membergroups[8]"; $rank = 1; }

		push (@allmembers, join ("\|", "$searchname|$members[1]|$members[2]|$members[10]|$members[17]|$rank|$memberinfo|$posts|$members[20]|$member|$members[21]\n"));
	}

	for (0..$#allmembers) {
		@fields = split(/\|/, $allmembers[$_]);
		for $i (0..$#fields) {
			$data[$_][$i] = $fields[$i];
		}
	}

	if ($info{'sort'} eq "") {
	$info{'sort'} = 4;
	}

	if ($info{'sort'} == 0) {
		@sorted = sort { $a->[0] cmp $b->[0] } @data;
	}


	if ($info{'sort'} == 4) {
@sorted = sort { $a->[5] <=> $b->[5] or $a->[0] cmp $b->[0] } @data;
	}



	for (@sorted) { 
		$sortedrow = join ("|", @$_);
		push (@sortedmembers, $sortedrow);
	}


	$navbar = "$btn{'014'} Roster";
	print_top();

$showcount = $officercount + $mycount;

	print qq~
<table border="0" cellspacing="1" width=15%>
<tr>
<td valign="top">Officers:</TD><TD>$officercount</td>
</tr><tr>
<td valign="top">Members:</TD><TD>$mycount</td>
</tr><tr>
<td valign="top">Total:</TD><TD>$showcount</td>

</tr>
</table>

<CENTER>
<br>

<table width="80%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor="$windowbg" width=40%><b>$msg{'013'}</b></td>
<td bgcolor="$windowbg" width=25%><b>$msg{'024'}</b></td>
<td bgcolor="$windowbg" width=5%><b>Lvl:</b></td>
<td bgcolor="$windowbg" width=15%><b>Class:</b></td>
<td bgcolor="$windowbg" width=15%><b>Race:</b></td>


</tr>
~;



	if (@allmembers == 0) { }

	if ($info{'start'} eq "") { $start = 0; }
	else { $start = "$info{'start'}"; }

	$count = 0;
	$second = "$windowbg3";
	for ($i = $start; $i < @sortedmembers; $i++) {
		if ($second eq "$windowbg2") { $second="$windowbg3"; }
		else { $second="$windowbg2"; }
		($dummy, $mname, $memail, $msince, $mlvl, $mranknum, $mrank, $mposts, $mclass, $musername, $mrace) = split(/\|/, $sortedmembers[$i]);
		$count++;
		$icq = "";

		#if ($micq ne "") {
			#$icq = qq~$micq~;
		#}

		if ($musername eq "") { next; }
		if ($mrank eq "Friend") { next; }

		if ($musername eq "admin") { next; }
		if ($musername eq "admin2") { next; }


print qq~<tr>
<td bgcolor="$second">$mname</td>
<td bgcolor="$second">$mrank</td>
<td bgcolor="$second">$mlvl</td>
<td bgcolor="$second">$mclass</td>
<td bgcolor="$second">$mrace</td>
</tr>
~;

		#if ($count >= $maxmessagedisplay) { $i = @allmembers; }
	}
	print qq~</table>
</td>
</tr>
</table>
<br>
~;

#	print "<b>$msg{'039'}</b>";
#	$nummembers = @allmembers;
#	$count = 0;
#	while (($count*$maxmessagedisplay) < $nummembers) {
#		$view = $count+1;
#		$offset = ($count*$maxmessagedisplay);
#		if ($start == $offset) { print qq~[$view] ~; }
#		elsif ($offset == 0) { print qq~<a href="$cgi?action=memberlist2&amp;sort=$info{'sort'}">$view</a> ~; }
#		else { print qq~<a href="$cgi?action=memberlist2&amp;sort=$info{'sort'}&amp;start=$offset">$view</a> ~; }
#		$count++;
#	}
#	print "\n";

	print_bottom();
	exit;
}



if (-e "$scriptdir/user-lib/memberlist.pl") {require "$scriptdir/user-lib/memberlist.pl"} 

1; # return true
