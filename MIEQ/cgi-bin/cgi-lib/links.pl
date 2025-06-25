###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# links.pl 	                      							      #
# v0.9.9 - Requin                  								#
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
sub links {
###########

	reindexlinks();  # trial... reindex links so admin doesn't have to ? carter

	if ($info{'cat'} eq "") {
		open(CAT, "$linksdir/linkcats.dat") || error("$err{'001'} $linksdir/linkcats.dat");
		file_lock(CAT);
		@cats = <CAT>;
		unfile_lock(CAT);
		close(CAT);

		open(CNT, "$linksdir/linkcats.cnt") || error("$err{'001'} $linksdir/linkcats.cnt");
		file_lock(CNT);
		$catscount = <CNT>;
		unfile_lock(CNT);
		close(CNT);

		$navbar = "$btn{'014'} $nav{'005'}";
		print_top();
		print qq~<table align="center" border="0" cellpadding="3" cellspacing="10">
<tr>
~;
		foreach $category (@cats) {
			@fields = split (/\|/, $category);
			if (-e "$linksdir/$fields[1].dat") {
				open(CNTFILE,"$linksdir/$fields[1].cnt");
				file_lock(CNTFILE);
				$cnt = <CNTFILE>;
				unfile_lock(CNTFILE);
				close(CNTFILE);


##STEVE##IVE ADDED FOLDER ICONS THAT GREY OUT IN HERE

				print qq~<td valign="top" width="50%">

<table>
<tr>
<td colspan="2"><img src="$imagesurl/dir.gif" border="0" alt="">&nbsp;&nbsp;<b><a href="$cgi?action=links&amp;cat=$fields[1]">$fields[0]</a></b> <i>($cnt)</i></td>
</tr>
<tr>
<td width="20">&nbsp;</td>
<td>$fields[2]</td>
</tr>
</table>
</td>
~;
			} 
			else {
				print qq~<td valign="top" width="50%">
<table>
<tr>
<td colspan="2"><img src="$imagesurl/dirempty.gif" border="0" alt="">&nbsp;&nbsp;<font color="#888888"><b>$fields[0]</b> <i>(0)</i></font></td>
</tr>
<tr>
<td width="20">&nbsp;</td>
<td><font color="#888888">$fields[2]</font></td>
</tr>
</table>
</td>
~;
			}
			$count++;
			if ($count == 2) {
				print qq~</tr>
				<tr>
~;
				$count = 0;
			}
		}

		print qq~<tr><td colspan=3><hr></td></tr>~;

		if ($catscount == 1) { $linkcount = "$msg{'084'} <b>1</b> $msg{'085'}"; }
		else { $linkcount = "$msg{'086'} <b>$catscount</b> $msg{'087'}"; }

		print qq~</table>
<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">
<tr>
<td align="center">$linkcount</td>
</tr>~;

if ($adminonlyl eq "1") { 

		if ($access[29] eq "on") {
		print qq~<tr>
		<td align="center"><a href="$cgi?action=addlink">$nav{'030'}</a></td>
		</tr>~;
		}
}
	
if ($adminonlyl ne "1") {
	if($username ne "$anonuser") {
		print qq~<tr>
		<td align="center"><a href="$cgi?action=addlink">$nav{'030'}</a></td>
		</tr>~;
	}
}
	
print qq~</table>~;
	
	show_latestlinks();
	
	link_search();
	
	print qq~</table>~;
	print_bottom();
	exit;
	}
	else {
		
		open(LNKCATS, "$linksdir/linkcats.dat") || error("$err{'001'} $linksdir/linkcats.dat");
		file_lock(LNKCATS);
		@catsname = <LNKCATS>;
		unfile_lock(LNKCATS);
		close(LNKCATS);

		for ($a = 0; $a < @catsname; $a++) {
			($lnname[$a], $lnfolder[$a], $dummy) = split(/\|/, $catsname[$a]);
			if ($info{'cat'} eq $lnfolder[$a]) { 
				$lnkcatsname = $lnname[$a];
			}
		}
			
		$navbar = "$btn{'014'} $nav{'005'} $btn{'014'} $lnkcatsname";
		print_top();

            if ($info{'cat'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
		
		open(CATS, "$linksdir/$info{'cat'}.dat") || error("$err{'001'} $linksdir/$info{'cat'}.dat");
		file_lock(CATS);
		@lnkcats = <CATS>;
		unfile_lock(CATS);
		close(CATS);

		for ($a = 0; $a < @lnkcats; $a++) {
			($id[$a], $name[$a], $url[$a], $desc[$a], $date[$a], $linkposter[$a], $hits[$a], $votes[$a], $score[$a]) = split(/\|/, $lnkcats[$a]);
		}

		if ($info{'start'} eq "") { $start = 0; }
		else { $start = "$info{'start'}"; }
		$numshown = 0;

		print qq~<table border="0" cellpadding="1" cellspacing="0" width="100%">
		~;

		for ($b = $start; $b < @lnkcats; $b++) {
			++$numshown;
			display_date($date[$b]); $date[$b] = $user_display_date;
						$message = $desc[$b];
						if (length($message) > 100) {
						$tmpmessage = substr($message, 0, 100);
						$tmpmessage =~ s/(.*)\s.*/$1/;
						$oneliner = "$tmpmessage...";
						}
						else {
						$oneliner = $message;
						}
			$averagescore = "0";

			if ($votes[$b] > 0) { #STOPS DIVISION BY ZERO!
				$averagescore = "0";
				$averagescore = int(($score[$b] * 10) / $votes[$b]);
			}
##STEVE##27-03-02## MODS HERE!
			print qq~<tr>
<td><img src="$imagesurl/search/link.gif" border="0" alt="">&nbsp;&nbsp;<b><a href="$pageurl/$cgi?action=linkinfo&amp;cat=$info{'cat'}&amp;id=$id[$b]">$name[$b]</a></b></td>
</tr><tr>
<td>$oneliner</td>
</tr><tr>
<td><small>$msg{'089'} $date[$b] $nav{'134'} $hits[$b] $msg{'065'} $votes[$b] $msg{'447'} $score[$b] $msg{'448'} $averagescore%</small></td>
</tr><tr>
<td><small>~;

#THIS WORKS QUICKER COS ITS JUST 100PIXELS = 100PERCENT SO NO NEED FOR ANY DAFT LOOPS SO LONG AS BAR IS 100PX WIDE JUST DIVIDE B4HAND IF YOU JUST WANT 50PX OR WHATEVER :)
if ($averagescore > 0) {
	$greycells = 100 - $averagescore;
	print qq~0%&nbsp;<img src="$imagesurl/rategreen.gif" height="8" width="$averagescore" border="0" alt=""><img src="$imagesurl/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp;100%&nbsp;&nbsp;~;
}else{
	print qq~0%&nbsp;<img src="$imagesurl/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp;100%&nbsp;&nbsp;~;
}

print qq~<br><a href="$pageurl/$cgi?action=redirect&amp;cat=$info{'cat'}&amp;id=$id[$b]" target="_blank">$msg{'647'}</a>~;

if ($username ne $anonuser) {
if ($username ne $linkposter[$b]) {print qq~ | <a href="$pageurl/$cgi?action=ratelinks\&cat=$info{'cat'}\&id=$id[$b]">$nav{'031'}</a>~;
}
print qq~ | <a href="$pageurl/$cgi?action=imsend&amp;to=admin&amp;subject=$nav{'032'}&amp;msg=$name[$b] ($id[$b]) $nav{'032'} ($msg{'467'})">$nav{'032'}</a>~;
}

if ($access[29] eq "on") {
print qq~ | <a href="$cgi?action=editlinks\&cat=$info{'cat'}\&id=$id[$b]">$nav{'139'}</a>~;
print qq~ | <a href="$cgi?action=deletelinks\&cat=$info{'cat'}\&id=$id[$b]">$nav{'140'}</a>~; ##STEVE##23-03-02##
print qq~ | <a href="$cgi?action=movelinks\&cat=$info{'cat'}\&id=$id[$b]">$nav{'141'}</a>~; ##STEVE##23-03-02##
}

print qq~
</small></td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
~;
			if ($numshown >= $maxlinks) { $b = @lnkcats; }
		}
		print qq~<tr>
<td>
~;
		if ($numshown >= $maxlinks) {
			print qq~<hr noshade="noshade" size="1">
$msg{'039'} 
~;
			$numlinks = @lnkcats;
			$c = 0;
			while (($c*$maxlinks) < $numlinks) {
				$viewc = $c+1;
				$strt = ($c*$maxlinks);
				if ($start == $strt) { print "$viewc "; }
				elsif ($strt == 0) { print qq~<a href="$cgi?action=links&amp;cat=$info{'cat'}">$viewc</a> ~; }
				else { print qq~<a href="$cgi?action=links&amp;cat=$info{'cat'}&amp;start=$strt">$viewc</a> ~; }
				++$c;
			}
		}
		print qq~</td>
</tr>
</table>
<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">
~;

	if ($adminonlyl eq "1") {
	if ($access[29] eq "on") {
		print qq~<tr>
<td align="center"><a href="$cgi?action=links">$nav{'005'} $nav{'033'}</a> | <a href="$cgi?action=addlink">$nav{'030'}</a></td>
</tr>
~;
}
}	

	if($username ne "$anonuser") {
	if ($adminonlyl ne "1") {
		print qq~<tr>
<td align="center"><a href="$cgi?action=links">$nav{'005'} $nav{'033'}</a> | <a href="$cgi?action=addlink">$nav{'030'}</a></td>
</tr>
~;
	}
	}
		else {
		print qq~<tr>
<td align="center"><a href="$cgi?action=links">$nav{'005'} $nav{'033'}</a></td>
</tr>
~;
		}
		print qq~</table>~;
		print_bottom();
		exit;
	}
}

#############
sub link_info {
#############

		if ($info{'cat'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
		open(CATS, "$linksdir/$info{'cat'}.dat") || error("$err{'001'} $linksdir/$info{'cat'}.dat");
		file_lock(CATS);
		@dnlcats = <CATS>;
		unfile_lock(CATS);
		close(CATS);
		
		open(CAT, "$linksdir/linkcats.dat") || error("$err{'001'} $linksdir/linkcats.dat");
		file_lock(CAT);
		@allcats = <CAT>;
		unfile_lock(CAT);
		close(CAT);
		
		$thiscat = "";
		
		foreach $allcategory (@allcats) {
			@allfields = split (/\|/, $allcategory);
			if ($info{'cat'} eq $allfields[1]) {$thiscat = "$allfields[0]";}
		}

		for ($a = 0; $a < @dnlcats; $a++) {
			($id[$a], $name[$a], $url[$a], $desc[$a], $date[$a], $linkposter[$a], $hits[$a], $votes[$a], $score[$a]) = split(/\|/, $dnlcats[$a]);
		  if ($info{'id'} eq $id[$a]) {
				 display_date($date[$a]); $date[$a] = $user_display_date;
				 if ($votes[$a] eq "") {$votes[$a] = "0";}
				 if ($score[$a] eq "") {$score[$a] = "0";}
				 $navbar = "$btn{'014'} $nav{'005'} $btn{'014'} $thiscat $btn{'014'} $name[$a]";
				 print_top();
				 print qq~<table width="100%" border="0" cellpadding="3" cellspacing="1">
				 <tr><td><table width="60%" border="0" cellpadding="3" cellspacing="0">
				 <tr>
				 <td>&nbsp;<img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$pageurl/$cgi?action=links">$nav{'005'}</a>
				 <br>
				 <img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$pageurl/$cgi?action=links\&cat=$info{'cat'}">$thiscat</a></td>
				 </tr><tr>
				 <td class="forumwindow3">&nbsp;<img src="$imagesurl/search/link.gif" border="0" alt="">&nbsp;&nbsp;<b>$name[$a]</b>
				 <br><small>&nbsp;$msg{'089'} $date[$a] $nav{'134'} $hits[$a] $msg{'065'} $votes[$a] $msg{'447'} $score[$a]</small></td>
				 </tr><tr>
				 <td class="forumwindow1">$desc[$a]</td>
				 </tr><tr>
				 <td class="forumwindow1" align="right"><a href="$pageurl/$cgi?action=redirect&amp;cat=$info{'cat'}&amp;id=$id[$a]" class="polllink" target="_blank">$msg{'647'}</a>&nbsp;</td>
				 </tr>~;
				 
				 if ($votes[$a] > 0) { #STOPS DIVISION BY ZERO!
				 		$averagescore = "0";
						$averagescore = int(($score[$a] * 10) / $votes[$a]);
				 }
				 
				 print qq~<tr>
				 <td class="forumwindow3" align="center"><small>~;
				 
				 if ($votes[$a] > 0) {
				 $greycells = 100 - $averagescore;
				 print qq~0%&nbsp;<img src="$imagesurl/rategreen.gif" height="8" width="$averagescore" border="0" alt="$averagescore%"><img src="$imagesurl/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp;100%&nbsp;&nbsp;<br>~;
				 }else{
				 print qq~0%&nbsp;<img src="$imagesurl/rategrey.gif" height="8" width="100" border="0" alt="$averagescore%">&nbsp;100%&nbsp;&nbsp;<br>~;
				 }				 
				 
				 if ($username ne $anonuser) {
				 if ($username ne $linkposter[$a]) {print qq~<a href="$cgi?action=ratelinks\&cat=$info{'cat'}\&id=$id[$a]">$nav{'031'}</a> | ~;
				 }
				 print qq~<a href="$pageurl/$cgi?action=imsend&amp;to=admin&amp;subject=$nav{'032'}&amp;msg=$name[$b] ($id[$b]) $nav{'032'} ($msg{'467'})">$nav{'032'}</a>~;
				 }
				 				 
				 if ($access[29] eq "on") {
				 print qq~ | <a href="$pageurl/$cgi?action=editlinks\&cat=$info{'cat'}\&id=$id[$a]">$nav{'139'}</a>~;
				 print qq~ | <a href="$pageurl/$cgi?action=deletelinks\&cat=$info{'cat'}\&id=$id[$a]">$nav{'140'}</a>~; 
				 print qq~ | <a href="$pageurl/$cgi?action=movelinks\&cat=$info{'cat'}\&id=$id[$a]">$nav{'141'}</a>~;
				 }

				 print qq~</small></td>
				 </tr></table>
				 </td></tr></table><br>~;
				 print_bottom();
				 exit;
			}
		}

}

#############
sub addlink {
#############
	if ($username eq "$anonuser" && $adminonlyl ne "1") { error("noguests"); }
	
	if ($adminonlyl eq "1") {
	if ($access[29] ne "on") { error("$err{'011'}"); }
	}	

	open(FILE, "$linksdir/linkcats.dat") || error("linkcats.dat Not Found");
	file_lock(FILE);
	@cats=<FILE>;
	unfile_lock(FILE);
	close(FILE);

	$navbar = "$btn{'014'} $nav{'005'} $btn{'014'} $nav{'030'}";
	print_top();
	print qq~<form onSubmit="submitonce(this)" onSubmit="submitonce(this)" method="post" action="$cgi?action=addlink2">
<table border="0" cellpadding="5" cellspacing="0">
<tr>
<td><b>$msg{'090'}</b></td>
<td><input type="text" name="title" size=40" maxlength="100"></td>
</tr>
<tr>
<td><b>$msg{'091'}</b></td>
<td><input type="text" name="url" size="40" maxlength="150" value="http://"></td>
</tr>
<tr>
<td><b>$msg{'092'}</b></td>
<td><select name="cat">
~;
	foreach $category (@cats) {
		@fields = split (/\|/, $category);
		$cat[$i] =~ s/\n//g;
		$cat[$i] =~ s/\r//g;
		print qq~<option value="$fields[1]">$fields[0]~;
	}
	print qq~</select><td>
</tr>
<tr>
<td valign="top"><b>$msg{'093'}</b></td>
<td><textarea name="desc" cols="40" rows="5" maxlength="1500"></textarea><br>$msg{'645'}</td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$btn{'013'}"></td>
</tr>
</table>
</form>
~;
	print_bottom();
	exit;
}

##############
sub addlink2 {
##############
	if ($adminonlyl eq "1") { if ($access[29] ne "on") { error("$err{'011'}"); }}
	error("$err{'031'}") unless ($input{'cat'});
	error("$err{'021'}") unless ($input{'title'});
	error("$err{'022'}") unless ($input{'url'});
	error("$err{'023'}") unless ($input{'desc'});
	if (length($input{'desc'}) > 1500) { $input{'desc'} = substr($input{'desc'},0,1500); }
	if($username eq "$anonuser") { error("$err{'011'}"); }
	
	open (DATA, "<$linksdir/$input{'cat'}.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }

	$count = $a;
	$i = 0;
	$id = $count +1;

	chomp($input{'desc'});
	chomp($input{'title'});
	chomp($input{'url'});

	$title = htmlescape($input{'title'});
	$desc = htmlescape($input{'desc'});

	open (DATABASE,">$linksdir/$input{'cat'}.dat");
	file_lock(DATABASE);
	print DATABASE "$id|$title|$input{'url'}|$desc|$date|$username|0|0|0|\n";
	while ($i < $count) {
		($id, $name, $url, $text, $postdate, $linkposter, $hits, $votes, $score) = split(/\|/, $datas[$i]);
		chomp($message);
		chomp($subject);
		chomp($name);
		print DATABASE "$id|$name|$url|$text|$postdate|$linkposter|$hits|$votes|$score|\n";
		$i++;
	}
	unfile_lock(DATABASE);
	close(DATABASE);

	open(CNT, "<$linksdir/$input{'cat'}.cnt");
	file_lock(CNT);
	$catscount = <CNT>;
	unfile_lock(CNT);
	close(CNT);
	open(LCNT, "$linksdir/linkcats.cnt");
	file_lock(LCNT);
	$linkcatscount = <LCNT>;
	unfile_lock(LCNT);
	close(LCNT);

	$catscount++;
	$linkcatscount++;

	open(CNT, ">$linksdir/$input{'cat'}.cnt");
	file_lock(CNT);
	print CNT "$catscount";
	unfile_lock(CNT);
	close(CNT);
	open(LCNT, ">$linksdir/linkcats.cnt");
	file_lock(LCNT);
	print LCNT "$linkcatscount";
	unfile_lock(LCNT);
	close(LCNT);

	success();
}


#############
sub success {
#############
	print_top();
	print qq~<b>$nav{'027'}</b><br>
$inf{'015'}
~;
	print_bottom();
	exit;
}

##############
sub redirect {
##############

	if ($info{'cat'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,">$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($id_temp, $name, $url, $desc, $addate, $linkposter, $hits_temp, $votes, $score) = split(/\|/, $datas[$i]);

		if ($id_temp eq $info{'id'}) {
			$theurl = $url;
			$hits = $hits_temp +1;
			print DATA "$id_temp|$name|$url|$desc|$addate|$linkposter|$hits|$votes|$score|\n";
		}
		else { print DATA "$id_temp|$name|$url|$desc|$addate|$linkposter|$hits_temp|$votes|$score|\n"; }
		$i++;
	}
	unfile_lock(DATA);
	close(DATA);

	print "Location: $theurl\n\n";	
}


###############
sub editlinks {   
###############

if ($access[29] ne "on") { error("$err{'011'}"); }

$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		$linkname = htmltotext($linkname);
		$desc = htmltotext($desc);
	
	$navbar = "$btn{'014'} Links $btn{'014'} $nav{'139'}";

	print_top();


##STEVE## IVE REMOVED EDITING OF THE ID NUMBER + MADE DESC A TEXT AREA TOO

	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form onSubmit="submitonce(this)" action="$cgi?action=editlinks2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$nav{'139'}</b></td>
</tr>
<tr>
<td>$msg{'449'}</td>
<td><input type="hidden" name="idtemp" value="$idtemp" size="3">$idtemp</td>
</tr>
<tr>
<td>$msg{'450'}</td>
<td><input type="text" name="nlinkname" value="$linkname" size="30"></td>
</tr>
<tr>
<td>$msg{'451'}</td>
<td><input type="text" name="ntheurl" value="$theurl" size="30"></td>
</tr>
<tr>
<td>$msg{'452'}</td>
<td><textarea name="ndesc" cols="40" rows="5" maxlength="1500">$desc</textarea></td>
</tr>
<tr>
<td>$msg{'453'}</td>
<td><input type="text" name="nthedate" value="$thedate" size="30"></td>
</tr>
<tr>
<td>$msg{'454'}</td>
<td><input type="text" name="nlinkposter" value="$linkposter" size="10"></td>
</tr>
<tr>
<td>$msg{'455'}</td>
<td><input type="text" name="nhits" value="$nhits" size="3"></td>
</tr>
<tr>
<td>$msg{'458'}</td>
<td><input type="hidden" name="nvotes" value="$votes" size="3">$votes</td>
</tr>
<tr>
<td>$msg{'459'}</td>
<td><input type="hidden" name="nscore" value="$score" size="3">$score</td>
</tr>
<tr>
<td colspan="2"><hr></td>
</tr>
<tr>
<td align="center" colspan="2"><input type="submit" value="$btn{'016'}"></td>
</tr>
</form>
</td>
</tr>
</table>
~;
print_bottom();
			
}
$i++;
	}
	unfile_lock(DATA);
	close(DATA);

	

exit;
}
	

################
sub editlinks2 { 
################

if ($access[29] ne "on") { error("$err{'011'}"); }
	error("$err{'021'}") unless ($input{'nlinkname'});
	error("$err{'022'}") unless ($input{'ntheurl'});
	error("$err{'023'}") unless ($input{'ndesc'});
	error("$err{'006'}") unless ($input{'nlinkposter'});
	error("$err{'006'}") unless ($input{'nthedate'});
	if ($input{'nhits'} eq "") { error("$err{'006'}"); }
	if (length($input{'ndesc'}) > 1500) { $input{'ndesc'} = substr($input{'ndesc'},0,1500); }
	
	$input{'ndesc'} = htmlescape($input{'ndesc'});
	$input{'nlinkname'} = htmlescape($input{'nlinkname'});
	
	if ($input{'nvotes'} eq "") {$input{'nvotes'} = "0";}
	if ($input{'nscore'} eq "") {$input{'nscore'} = "0";}
	
	$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	open(EDITDATA,">$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(EDITDATA);
	for ($a = 0; $a < @datas; $a++) {
		($idtemp, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $datas[$a]);
		if ($idtemp eq $info{'id'}) {
		print EDITDATA "$input{'newtemp'}|$input{'nlinkname'}|$input{'ntheurl'}|$input{'ndesc'}|$input{'nthedate'}|$input{'nlinkposter'}|$input{'nhits'}|$input{'nvotes'}|$input{'nscore'}|\n";
		}	else { print EDITDATA "$datas[$a]"; }
	}
	unfile_lock(EDITDATA);
	close(EDITDATA);
	
	print "Location: $cgi\?action=links\n\n";
	exit;
}

##STEVE##23-03-02## ADDED THE FOLLOWING TWO SUBS TO DELETE LINKS
#################
sub deletelinks {   
#################
if ($access[29] ne "on") { error("$err{'011'}"); }

$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		
	$navbar = "$btn{'014'} Links $btn{'014'} $msg{'058'} $nav{'005'}";

	print_top();
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form onSubmit="submitonce(this)" action="$cgi?action=deletelinks2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$nav{'140'}</b></td>
</tr>
<tr>
<td>$msg{'449'}</td>
<td>$idtemp</td>
</tr>
<tr>
<td>$msg{'450'}</td>
<td>$linkname</td>
</tr>
<tr>
<td>$msg{'451'}</td>
<td>$theurl</td>
</tr>
<tr>
<td>$msg{'452'}</td>
<td>$desc</td>
</tr>
<tr>
<td>$msg{'453'}</td>
<td>$thedate</td>
</tr>
<tr>
<td>$msg{'454'}</td>
<td>$linkposter</td>
</tr>
<tr>
<td>$msg{'455'}</td>
<td>$nhits</td>
</tr>
<tr>
<td>$msg{'458'}</td>
<td>$votes</td>
</tr>
<tr>
<td>$msg{'459'}</td>
<td>$score</td>
</tr>
<tr>
<td colspan="2">
<hr>
</td>
</tr>
<tr>
<td align="center" colspan="2"><input type="submit" value="$btn{'011'}"></td>
</tr>
</form>
</td>
</tr>
</table>
~;
print_bottom();
			
}
$i++;
	}
	unfile_lock(DATA);
	close(DATA);

exit;
}
	

##STEVE##23-03-02##
################
sub deletelinks2 { 
################

if ($access[29] ne "on") { error("$err{'011'}"); }

	$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

#	$a = 0;
#	while ($datas[$a] ne '') { $a++; }
#	$count = $a;
#	$i = 0;
#	$num = $count +1;
#
#	open(DATA,">$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
#	while ($i < $count) {
#		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);
#
#		if ($idtemp ne $info{'id'}) {
#			print DATA "$idtemp|$linkname|$theurl|$desc|$thedate|$linkposter|$nhits|$votes|$score|\n";
#		}
#		$i++;
#	}
#	close(DATA);


	open(DATA,">$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	foreach $datas (@datas) {
		chomp($datas);
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $datas);
	
		if ($idtemp ne $info{'id'}) {
			print DATA "$idtemp|$linkname|$theurl|$desc|$thedate|$linkposter|$nhits|$votes|$score|\n";
		}
	}
	unfile_lock(DATA);
	close(DATA);

	$lines = 0;
	open(DATA,"<$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while (sysread DATA, $buffer, 4096) {
        	$lines += ($buffer =~ tr/\n//);
	}
	unfile_lock(DATA);
	close(DATA);

	if ($lines == 0) {
		unlink "$linksdir/$info{'cat'}.dat";
		unlink "$linksdir/$info{'cat'}.cnt";
	}else{
		open(CNT, "$linksdir/$info{'cat'}.cnt") or error("$err{'016'} $linksdir/$info{'cat'}.cnt");#
		file_lock(CNT);
		$catscount = <CNT>;
		unfile_lock(CNT);
		close(CNT);

		$catscount--;

		open(CNT, ">$linksdir/$info{'cat'}.cnt") or error("$err{'016'} $linksdir/$info{'cat'}.cnt");#
		file_lock(CNT);
		print CNT "$catscount";
		unfile_lock(CNT);
		close(CNT);
	}

	open(LCNT, "$linksdir/linkcats.cnt") or error("$err{'016'} $linksdir/linkcats.cnt");#
	file_lock(LCNT);
	$linkcatscount = <LCNT>;
	unfile_lock(LCNT);
	close(LCNT);

	$linkcatscount--;

	open(LCNT, ">$linksdir/linkcats.cnt") or error("$err{'016'} $linksdir/linkcats.cnt");#
	file_lock(LCNT);
	print LCNT "$linkcatscount";
	unfile_lock(LCNT);
	close(LCNT);

	print "Location: $cgi\?action=links\n\n";
	exit;
}

##STEVE##23-03-02## ADDED THE FOLLOWING TWO SUBS TO MOVE LINKS
###############
sub movelinks {   
###############
if ($access[29] ne "on") { error("$err{'011'}"); }

$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	open(FILE, "$linksdir/linkcats.dat") || error("linkcats.dat Not Found");
	file_lock(FILE);
	@cats2=<FILE>;
	unfile_lock(FILE);
	close(FILE);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $hits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		
	$navbar = "$btn{'014'} Links $btn{'014'} $nav{'141'}";

	print_top();
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form onSubmit="submitonce(this)" action="$cgi?action=movelinks2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$nav{'141'}:</b></td>
</tr>
<tr>
<td>$msg{'449'}</td>
<td><input type="hidden" name="idtemp" value="$idtemp" size="3">$idtemp</td>
</tr>
<tr>
<td>$msg{'450'}</td>
<td><input type="hidden" name="mlinkname" value="$linkname" size="30">$linkname</td>
</tr>
<tr>
<td>$msg{'451'}</td>
<td><input type="hidden" name="mtheurl" value="$theurl" size="30">$theurl</td>
</tr>
<tr>
<td>$msg{'452'}</td>
<td><input type="hidden" name="mdesc" value="$desc" size="50">$desc</td>
</tr>
<tr>
<td>$msg{'453'}</td>
<td><input type="hidden" name="mthedate" value="$thedate" size="30">$thedate</td>
</tr>
<tr>
<td>$msg{'454'}</td>
<td><input type="hidden" name="mlinkposter" value="$linkposter" size="10">$linkposter</td>
</tr>
<tr>
<td>$msg{'455'}</td>
<td><input type="hidden" name="mhits" value="$hits" size="3">$hits</td>
</tr>
<tr>
<td>$msg{'458'}</td>
<td><input type="hidden" name="mvotes" value="$votes" size="3">$votes</td>
</tr>
<tr>
<td>$msg{'459'}</td>
<td><input type="hidden" name="mscore" value="$score" size="3">$score</td>
</tr>
<tr>
<td><b>$msg{'456'}$msg{'092'}</b></td>
<td><select name="cat2">
~;
	foreach $category (@cats2) {
		@fields = split (/\|/, $category);
		$cat2[$i] =~ s/\n//g;
		$cat2[$i] =~ s/\r//g;
		if ($fields[1] ne $info{'cat'}) {print qq~<option value="$fields[1]">$fields[0]~;}
	}
	print qq~</select><td>
</tr>
<tr>
<td colspan="2">
<hr>
</td>
</tr>
<tr>
<td align="center" colspan="2"><input type="submit" value="$btn{'029'}"></td>
</tr>
</form>
</td>
</tr>
</table>
~;
print_bottom();
			
}
$i++;
	}
	unfile_lock(DATA);
	close(DATA);

exit;
}

##STEVE##23-03-02##
################
sub movelinks2 { 
################

if ($access[29] ne "on") { error("$err{'011'}"); }

	if ($input{'cat2'} eq "") {$input{'cat2'} = "$info{'cat'}";}
	$filetoopen = "$info{'cat'}.dat";

	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,">$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $hits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp ne $info{'id'}) {
			print DATA "$idtemp|$linkname|$theurl|$desc|$thedate|$linkposter|$hits|$votes|$score|\n";
		}
		$i++;
	}
	unfile_lock(DATA);
	close(DATA);

	open(CNT, "$linksdir/$input{'cat2'}.cnt");
	file_lock(CNT);
	$catscount = <CNT>;
	unfile_lock(CNT);
	close(CNT);

	$idnew = $catscount +1;

	$filetomove2 = "$input{'cat2'}.dat";
	open(DATA2,">>$linksdir/$filetomove2") or error("$err{'016'} $filetomove2");
	file_lock(DATA2);
			print DATA2 "$idnew|$input{'mlinkname'}|$input{'mtheurl'}|$input{'mdesc'}|$input{'mthedate'}|$input{'mlinkposter'}|$input{'mhits'}|$input{'mvotes'}|$input{'mscore'}|\n";
	unfile_lock(DATA2);
	close(DATA2);

	$lines = 0;
	open(DATA,"<$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while (sysread DATA, $buffer, 4096) {
        	$lines += ($buffer =~ tr/\n//);
	}
	unfile_lock(DATA);
	close(DATA);

	if ($lines == 0) {
		unlink "$linksdir/$info{'cat'}.dat";
		unlink "$linksdir/$info{'cat'}.cnt";
	}else{
		open(CNT, "$linksdir/$info{'cat'}.cnt");
		file_lock(CNT);
		$catscount = <CNT>;
		unfile_lock(CNT);
		close(CNT);

		$catscount--;

		open(CNT, ">$linksdir/$info{'cat'}.cnt");
		file_lock(CNT);
		print CNT "$catscount";
		unfile_lock(CNT);
		close(CNT);
	}

	open(LCNT, "$linksdir/linkcats.cnt");
	file_lock(LCNT);
	$linkcatscount = <LCNT>;
	unfile_lock(LCNT);
	close(LCNT);

	$linkcatscount--;

	open(LCNT, ">$linksdir/linkcats.cnt");
	file_lock(LCNT);
	print LCNT "$linkcatscount";
	unfile_lock(LCNT);
	close(LCNT);

	open(CNT, "$linksdir/$input{'cat2'}.cnt");
	file_lock(CNT);
	$catscount = <CNT>;
	unfile_lock(CNT);
	close(CNT);
	open(LCNT, "$linksdir/linkcats.cnt");
	file_lock(LCNT);
	$linkcatscount = <LCNT>;
	unfile_lock(LCNT);
	close(LCNT);

	$catscount++;
	$linkcatscount++;

	open(CNT, ">$linksdir/$input{'cat2'}.cnt");
	file_lock(CNT);
	print CNT "$catscount";
	unfile_lock(CNT);
	close(CNT);
	open(LCNT, ">$linksdir/linkcats.cnt");
	file_lock(LCNT);
	print LCNT "$linkcatscount";
	unfile_lock(LCNT);
	close(LCNT);

	print "Location: $cgi\?action=links\n\n";
	exit;
}

##STEVE##27-03-02## ADDED THE FOLLOWING TWO SUBS TO RATE LINKS
###############
sub ratelinks {   
###############

######## Carter.... Added Security and language compatability

if ($username eq "$anonuser") { error("noguests"); }

$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		
		if ($username eq "$linkposter") { error("$err{'033'}"); }
		
	$navbar = "$btn{'014'} Links $btn{'014'} $msg{'457'}";

	print_top();
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form onSubmit="submitonce(this)" action="$cgi?action=ratelinks2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$msg{'457'}:</b></td>
</tr>
<tr>
<td>$msg{'449'}</td>
<td><input type="hidden" name="idtemp" value="$idtemp" size="3">$idtemp</td>
</tr>
<tr>
<td>$msg{'450'}</td>
<td><input type="hidden" name="linkname" value="$linkname" size="30">$linkname</td>
</tr>
<tr>
<td>$msg{'451'}</td>
<td><input type="hidden" name="theurl" value="$theurl" size="30">$theurl</td>
</tr>
<tr>
<td>$msg{'452'}</td>
<td><input type="hidden" name="desc" value="$desc" size="50">$desc</td>
</tr>
<tr>
<td>$msg{'453'}</td>
<td><input type="hidden" name="thedate" value="$thedate" size="30">$thedate</td>
</tr>
<tr>
<td>$msg{'454'}</td>
<td><input type="hidden" name="linkposter" value="$linkposter" size="10">$linkposter</td>
</tr>
<tr>
<td>$msg{'455'}</td>
<td><input type="hidden" name="nhits" value="$nhits" size="3">$nhits</td>
</tr>
<tr>
<td>$msg{'458'}</td>
<td><input type="hidden" name="votes" value="$votes" size="3">$votes</td>
</tr>
<tr>
<td>$msg{'459'}</td>
<td><input type="hidden" name="score" value="$score" size="3">$score</td>
</tr>
<tr>
<td><b>$msg{'460'}</b></td>
<td><select name="rateval">
<option value="1">1
<option value="2">2
<option value="3">3
<option value="4">4
<option value="5">5
<option value="6">6
<option value="7">7
<option value="8">8
<option value="9">9
<option value="10">10
</select><td>
</tr>
<tr>
<td colspan="2">
<hr>
</td>
</tr>
<tr>
<td align="center" colspan="2"><input type="submit" value="$btn{'040'}"></td>
</tr>
</form>
</td>
</tr>
</table>
~;
print_bottom();
			
}
$i++;
	}
	unfile_lock(DATA);
	close(DATA);

exit;
}

##STEVE##27-03-02## MODS HERE!
################
sub ratelinks2 { 
################

######## Carter.... Added Security and language compatability

if ($username eq "$anonuser") { error("noguests"); }

	$filetoopen = "$info{'cat'}.dat";

	open (DATA, "<$linksdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,">$linksdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
			if ($username eq "$linkposter") { error("$err{'033'}"); }
			$votes++;
			$score = $score + $input{'rateval'};
			print DATA "$idtemp|$linkname|$theurl|$desc|$thedate|$linkposter|$nhits|$votes|$score|\n";
		}else{
			print DATA "$idtemp|$linkname|$theurl|$desc|$thedate|$linkposter|$nhits|$votes|$score|\n";
		}
		$i++;
	}
	unfile_lock(DATA);
	close(DATA);

	print "Location: $cgi\?action=linkinfo\&cat=$info{'cat'}\&id=$info{'id'}\n\n";
	exit;
}

########################
sub link_search {
########################

print qq~<table align="center" border="0" cellpadding="3" cellspacing="1" width="80%">
<tr><td align="center" class="forumwindow3" colspan="3"><b>$nav{'039'} $nav{'005'}</b></td></tr>
<tr>
<td align="center" colspan="3">
<form onSubmit="submitonce(this)" method="POST" action="$pageurl/$cgi\?action=search">
<input type="hidden" name="action" value="search">
<input type="text" name="pattern" size="30" class="text">&nbsp;<input type="submit" class="button" value="$btn{'001'}">
<input type="hidden" name="articleson" value="off">
<input type="hidden" name="forumson" value="off">
<input type="hidden" name="linkson" value="on">
<input type="hidden" name="downloadson" value="off">
</form>
</td>
</tr></table>~;

}

##########################
sub show_latestlinks {
##########################

if ($showlatestlinks eq "") {$showlatestlinks = "1";}

if ($showlatestlinks eq "1") {

latestlinks();

print qq~<table align="center" border="0" cellpadding="3" cellspacing="1" width="80%">
<tr><td align="center" class="forumwindow3" colspan="3"><b>$msg{'674'}</b></td></tr>
<tr><td align="left" class="forumwindow1"><b>$msg{'450'}:</b></td><td align="left" class="forumwindow1"><b>$msg{'088'}</b></td><td align="left" class="forumwindow1"><b>$msg{'110'}</b></td></tr>~;

if (@_ltfinallinks) {
   for ($_ltl = 0; $_ltl < @_ltfinallinks && $_ltl < 5; $_ltl++) {
      ($_ltlcat, $_ltlid, $_ltlname, $_ltldateref, $_ltldate, $_ltlcount, $_ltldescription) = split(/\|/, $_ltfinallinks[$_ltl]);
						display_date($_ltldate); $_ltldate = $user_display_date;
						$message = $_ltldescription;
						$_ltlname = htmltotext($_ltlname);
						$message = htmltotext($message);
						if (length($message) > 70) {
						$tmpmessage = substr($message, 0, 70);
						$tmpmessage =~ s/(.*)\s.*/$1/;
						$_ltloneliner = "$tmpmessage...";
						}
						else {
						$_ltloneliner = $message;
						}
						print qq~<tr><td align="left" nowrap><a href="$scripturl/$cgi?action=linkinfo&amp;cat=$_ltlcat&amp;id=$_ltlid" class="whomenu">$_ltlname</a>~; if ($_ltlcount eq "0") {print qq~&nbsp;<img src="$imagesurl/forum/new.gif" border="0">~;} print qq~</td><td align="left"><small>$_ltloneliner</small></td><td align="left" nowrap><small>$_ltldate</small></td></tr>~;
			
   }
} else {
	 print qq~<tr><td align="left" colspan="3">$msg{'678'}</td></tr>~;
}

print qq~</table>~;

}

}

if (-e "$scriptdir/user-lib/links.pl") {require "$scriptdir/user-lib/links.pl"} 

1; # return true

