###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# poll.pl                                                  			      #
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
# File: Last modified: 07/30/02                                               #
###############################################################################
###############################################################################


##########
sub poll {
##########

	check_ip();


	open(FILE, "$datadir/polls/polls.txt");
	file_lock(FILE);
	@polls = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	($id[0], $name[0]) = split(/\|/, $polls[0]);

	if (@polls ==0) {
		print qq~<tr>
<td align="center" class="poll">$msg{'153'}</td>
</tr>
~;
	}
	else {
		print qq~<tr>
<td class="poll">
~;
		open(FILE, "$datadir/polls/$id[0]_q.dat");
		file_lock(FILE);
		chomp(@data = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		print qq~<form onSubmit="submitonce(this)" action="$cgi?action=pollit" method="post">
<table cellpadding="0" cellspacing="0" border="0" align="center" width="100%">
<tr>
<td class="pollquestion" align="center">$name[0]</td>
</tr>
<tr>
<td> </td>
</tr>
~;
		for ($i = 0; $i < @data; $i++) {
			print qq~<tr>
<td valign="top" class="poll"><input type="radio" name="answer" value="$i">$data[$i]</td>
</tr>
~;
		}
print qq~<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td align="center"><input type="hidden" name="id" value="$id[0]">
<input type="hidden" name="submitted" value="1">
<input type="submit" class="button" value="$btn{'002'}"><br><br>
<div><a href="$cgi?action=pollit2&amp;id=$id[0]" class="polllink">$nav{'013'}</a></div></td>
</tr>
</table>
</form>
</td>
</tr>
<!-- -->
~;

	}
}

############
sub pollit {
############

if (($multiplevoting eq "0") || ($multiplevoting eq "")) {
	check_ip();
	}

	if ($input{'answer'} eq "") { error("$err{'019'}"); }

	open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
	file_lock(FILE);
	@polls = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	open(FILE, "$datadir/polls/$input{'id'}_a.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_a.dat");
	file_lock(FILE);
	chomp(@data = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	open(FILE, ">$datadir/polls/$input{'id'}_a.dat") || error("$err{'016'} $datadir/polls/$input{'id'}_a.dat");
	file_lock(FILE);
	for ($i = 0; $i < @data; $i++) {
		if ($i == $input{'answer'}) {
			$count = $data[$i] + 1;
			print FILE "$count\n";
		}
		else { print FILE "$data[$i]\n"; }
	}
	unfile_lock(FILE);
	close(FILE);

	open(LOG, ">>$datadir/polls/$input{'id'}_ip.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_ip.dat");
	file_lock(LOG);
	print LOG "$ENV{'REMOTE_ADDR'}|$ENV{'REMOTE_HOST'}\n";
	unfile_lock(LOG);
	close(LOG);

	print "Location: $cgi\?action=pollit2\&id=$input{'id'}\n\n";
}

#############
sub pollit2 {
#############
	open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
	file_lock(FILE);
	@polls = <FILE>;
	unfile_lock(FILE);
	close(FILE);

			foreach $line (@polls) {
			($pollid, $pollname) = split(/\|/, $line);
			if ($pollid eq $info{'id'}) {$polltitle = $pollname;}
			}

      if ($info{'id'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	open(FILE, "$datadir/polls/$info{'id'}_q.dat") || error("$err{'001'} $datadir/polls/$info{'id'}_q.dat!");
	file_lock(FILE);
	chomp(@questions = <FILE>);
	unfile_lock(FILE);
	close(FILE);

      if ($info{'id'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	open(FILE, "$datadir/polls/$info{'id'}_a.dat") || error("$err{'001'} $datadir/polls/$info{'id'}_a.dat!");
	file_lock(FILE);
	chomp(@answers = <FILE>);
	unfile_lock(FILE);
	close(FILE);
	
	open(FILE, "$datadir/polls/$info{'id'}_c.dat");
	file_lock(FILE);
	chomp(@comments = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	$totalvotes = 0;
	for ($x = 0; $x < @answers; $x++) {
		$totalvotes = $totalvotes + $answers[$x];	

	}
	
	$navbar = "$btn{'014'} $nav{'013'}";
	print_top();
	print qq~<table align="center" cellpadding="0" cellspacing="0" border="0">
<tr>
<td colspan="2" align="center"><b>$msg{'064'} $polltitle</b></td>
</tr>
<tr>
<td colspan="2"> </td>
</tr>
~;
	for ($i = 0; $i < @answers; $i++) {
		if ($totalvotes ne 0) {
			$pixels = int((($answers[$i]/$totalvotes) * 100)/2);
			$procent = ($answers[$i]/$totalvotes) * 100;
			$c = int(10*($procent*10 - int($procent*10)));
			$b = int(10*($procent - int($procent)));
			$a = int($procent);
			if ($c >= 5) { $b++ }
		} else { 
			$a = 0; 
			$b = 0;
		}
		$procent = $a.".".$b;

		print qq~<tr>
<td>$questions[$i]:</td>
<td><img src="$imagesurl/leftbar.gif" width="7" height="14" alt=""><img src="$imagesurl/mainbar.gif" width="$pixels" height="14" alt=""><img src="$imagesurl/rightbar.gif" width="7" height="14" alt="">  ($procent%)</td>
</tr>
~;
	}
	print qq~<tr>
<td colspan="2"> </td>
</tr>
<tr>
<td colspan="2" align="center">$msg{'065'} $totalvotes</td>
</tr>
</table>
<br>
<table border="0" cellpadding="1" cellspacing="3" width="100%">
<tr>
<td colspan="2" align="center" class="commenttitleback">$msg{'617'} $polltitle</td>
</tr>
<tr>
<td colspan="2" align="center" class="newssubtitle">$msg{'159'}~; if ($username eq $anonuser) {print qq~<br>$msg{'611'}~;} print qq~</td>
</tr>~;

if (@comments) {
for ($a = 0; $a < @comments; $a++) {
				@item = split (/\|/, $comments[$a]);
				display_date($item[2]); $item[2] = $user_display_date;
				$message = $item[3];
				$message = censor_it($message);
				if ($enable_ubbc) { doubbc(); }
				if ($enable_smile) { dosmilies(); }
				
		print qq~<tr><td class="commentsubtitleback" valign="top" colspan="2">$msg{'110'} $item[2] $msg{'042'} ~;
		if ($username ne $anonuser) {print qq~<a href="$pageurl/$cgi?action=imsend&amp;to=$item[0]">$item[1]</a>~;} else { print qq~<b>$item[1]</b>~;} if ($username eq "admin") {print qq~&nbsp;&nbsp;-&nbsp;&nbsp;<a href="$cgi?action=editpollcomment&id=$info{'id'}&num=$a">[Edit]</a>&nbsp;&nbsp;<a href="$cgi?action=removepollcomment&id=$info{'id'}&num=$a">[Remove]</a>~;} if ($settings[7] eq "$root" && $editpoll eq "1" && $username ne "admin") {print qq~&nbsp;&nbsp;-&nbsp;&nbsp;<a href="$cgi?action=editpollcomment&id=$info{'id'}&num=$a">[Edit]</a>&nbsp;&nbsp;<a href="$cgi?action=removepollcomment&id=$info{'id'}&num=$a">[Remove]</a>~;} print qq~</td></tr><tr><td valign="top" colspan="2">$message</td></tr>~;
}
} else {print qq~<tr><td align="center" colspan="2">$msg{'043'}</td></tr><tr><td colspan="2" align="center">&nbsp;</td></tr>~; 
}

if ($username ne $anonuser) {
print qq~<tr>
<td colspan="2" align="center" class="commenttitleback">$msg{'618'} $polltitle</td>
</tr>
<form action="$cgi?action=commentpoll" method="post">
<tr>
<td class="formstextnormal" valign="top">$msg{'023'}</td><td><textarea name="message" rows="5" cols="40"></textarea></td>
</tr>
<tr>
<td colspan="2">
<input type="hidden" value="$info{'id'}" name="id">
<input type="hidden" name="rname" value="$realname">
<input type="hidden" name="uname" value="$username">
<input type="submit" class="button" value="$btn{'012'}"><input type="reset" class="button" value="$btn{'009'}"></td>
</tr>
</form>~;
}

print qq~</table><br>~;

	if (@polls > 1) { print qq~<div align="center"><table border="0" cellpadding="1" cellspacing="3" width="80%">
		<tr>
		<td colspan="2" align="center" class="commenttitleback"><b>$msg{'150'}</b></td>
		</tr>~;
		
		foreach $line (@polls) {
			@item = split(/\|/, $line);
			if ($item[0] ne $info{'id'}) {print qq~<tr>
			<td width="70%" class="forumwindow3">&nbsp;$item[1]</td>
			<td width="30%" class="forumwindow1">&nbsp;<a href="$cgi?action=pollit2&id=$item[$0]">$nav{'013'}</a></td>
			</tr>~;
			}
		}
		print qq~</table></div>~;
	}
	print_bottom();
	exit;
}

##############
sub check_ip {
##############
	open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
	file_lock(FILE);
	@polls = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	($id[0], $name[0]) = split(/\|/, $polls[0]);
	$usersip = $ENV{'REMOTE_ADDR'};

	open('LOG', "$datadir/polls/$id[0]_ip.dat") || error("$err{'001'} $datadir/polls/$id[0]_ip.dat");
	file_lock(LOG);
	@entries = <LOG>;
	unfile_lock(LOG);
	close(LOG);

	foreach $curentry (@entries) {
		$curentry =~ s/\n//g;
		$curentry =~ s/\r//g;
		($ip, $host) = split(/\|/, $curentry);

		if ($usersip eq "$ip") { 

#error("$err{'020'}")

print qq~
<tr>
<td class="poll">

<table cellpadding="0" cellspacing="0" border="0" align="center" width="100%">
<tr>
<td class="pollquestion" align="center">$name[0]<BR><BR></td>
</tr>

<tr>
<td valign="top" class="poll"><CENTER>You have already voted!</td>
</tr>

<tr>
<td align="center">
<br>
<div>
<a href="$cgi?action=pollit2&id=$id[0]" class="polllink">$nav{'013'}</a>
</div>
</td>
</tr>

</table>

</td>
</tr>
<!--
~;

 }
	}
}

#################
sub commentpoll {
#################
	if($username eq "$anonuser") { error("noguests"); }

	error("$err{'015'}") unless ($input{'message'});

	open(FILE, "$datadir/polls/$input{'id'}_c.dat");
	file_lock(FILE);
	@datas = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	$message = htmlescape($input{'message'});

	open(FILE, ">$datadir/polls/$input{'id'}_c.dat");
	file_lock(FILE);
	print FILE "$input{'uname'}|$input{'rname'}|$date|$message\n";
	print FILE @datas;
	unfile_lock(FILE);
	close(FILE);

	print "Location: $pageurl/$cgi?action=pollit2&id=$input{'id'}\n\n";
}

#################
sub removepollcomment {
#################
	if ($settings[7] ne "$root") {error("$err{'011'}");}
	if ($username ne "admin" &&  $settings[7] eq "$root" && $editpoll ne "1") { error("$err{'011'}"); }

	open(FILE, "$datadir/polls/$info{'id'}_c.dat");
	file_lock(FILE);
	chomp(@datas = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	open(FILE, ">$datadir/polls/$info{'id'}_c.dat");
	file_lock(FILE);
	for ($a = 0; $a < @datas; $a++) {
	@item = split (/\|/, $datas[$a]);
	if ($a ne $info{'num'}) {		
	print FILE "$item[0]|$item[1]|$item[2]|$item[3]\n";}
	}
	unfile_lock(FILE);
	close(FILE);

	print "Location: $pageurl/$cgi?action=pollit2&id=$info{'id'}\n\n";
}

#################
sub editpollcomment {
#################
	if ($settings[7] ne "$root") {error("$err{'011'}");}
	if ($username ne "admin" &&  $settings[7] eq "$root" && $editpoll ne "1") { error("$err{'011'}"); }

	open(FILE, "$datadir/polls/$info{'id'}_c.dat");
	file_lock(FILE);
	chomp(@datas = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	for ($a = 0; $a < @datas; $a++) {
	@citem = split (/\|/, $datas[$a]);
	if ($a eq $info{'num'}) {
	$message = htmltotext($citem[3]);		
	$navbar = "$btn{'014'} $nav{'035'}";
	print_top();
	print qq~<table border="0" cellpadding="1" cellspacing="3" width="100%">
	<form action="$cgi?action=editpollcomment2" method="post">
	<tr>
			<td class="formstextnormal" valign="top">$msg{'023'}</td><td><textarea name="message" rows="5" cols="40">$message</textarea></td>
	</tr>
	<tr>
			<td colspan="2">
			<input type="hidden" value="$info{'id'}" name="id">
			<input type="hidden" value="$info{'num'}" name="num">
			<input type="hidden" name="rname" value="$citem[1]">
			<input type="hidden" name="uname" value="$citem[0]">
			<input type="hidden" name="cdate" value="$citem[2]">
			<input type="submit" class="button" value="$btn{'030'}"><input type="reset" class="button" value="$btn{'009'}"></td>
	</tr>
	</form>
	</table>~;
	
	print_bottom();
	exit;}
	}


}

#################
sub editpollcomment2 {
#################
	if ($settings[7] ne "$root") {error("$err{'011'}");}
	if ($username ne "admin" &&  $settings[7] eq "$root" && $editpoll ne "1") { error("$err{'011'}"); }

	error("$err{'015'}") unless ($input{'message'});

	open(FILE, "$datadir/polls/$input{'id'}_c.dat");
	file_lock(FILE);
	chomp(@datas = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	$message = htmlescape($input{'message'});

	open(FILE, ">$datadir/polls/$input{'id'}_c.dat");
	file_lock(FILE);
	for ($a = 0; $a < @datas; $a++) {
	@citem = split (/\|/, $datas[$a]);
		 if ($a eq $input{'num'}) {		
		 print FILE "$input{'uname'}|$input{'rname'}|$input{'cdate'}|$message\n";
		 } else {
		 print FILE "$citem[0]|$citem[1]|$citem[2]|$citem[3]\n";
		 }
	}
	unfile_lock(FILE);
	close(FILE);

	print "Location: $pageurl/$cgi?action=pollit2&id=$input{'id'}\n\n";
}

if (-e "$scriptdir/user-lib/poll.pl") {require "$scriptdir/user-lib/poll.pl"} 

1; # return true