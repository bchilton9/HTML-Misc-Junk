###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# downloads.pl                                 					      #
# v0.9.9 - Requin     		                                                #
# Delete Download Error Fixed by: Carter for v0.9.7                           #
# Display Alterations by: Floyd for v0.9.8                                    #
# Rate Downloads by: Carter for v0.9.8                                        #
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
# File: Last modified: 03/26/03                                               #
###############################################################################
###############################################################################


###############
sub downloads {
###############

	reindexdownloads();   # this fixes the downloads incase they were edited....

	if ($info{'cat'} eq "") {
		open(CAT, "$downloadsdir/downloadcats.dat") || error("$err{'001'} $downloadsdir/downloadcats.dat");
		file_lock(CAT);
		@cats = <CAT>;
		unfile_lock(CAT);
		close(CAT);

		open(CNT, "$downloadsdir/downloadcats.cnt") || error("$err{'001'} $downloadsdir/downloadcats.cnt");
		file_lock(CNT);
		$catscount = <CNT>;
		unfile_lock(CNT);
		close(CNT);

		$navbar = "$btn{'014'} $nav{'056'}";
		print_top();
		print qq~<table align="center" border="0" cellpadding="3" cellspacing="10">
<tr>
~;
		foreach $category (@cats) {
			@fields = split (/\|/, $category);
			if (-e "$downloadsdir/$fields[1].dat") {
				open(CNTFILE,"$downloadsdir/$fields[1].cnt");
				file_lock(CNTFILE);
				$cnt = <CNTFILE>;
				unfile_lock(CNTFILE);
				close(CNTFILE);
				print qq~<td valign="top" width="50%">
<table>
<tr>
<td colspan="2"><img src="$imagesurl/dir.gif" border="0" alt="">&nbsp;&nbsp;<b><a href="$cgi?action=downloads&amp;cat=$fields[1]">$fields[0]</a></b> <i>($cnt)</i></td>
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
</td>~;
			}
			$count++;
			if ($count == 2) {
				print qq~</tr>
				<tr>~;
				$count = 0;
			}
		}
		
		print qq~<tr><td colspan="3"><hr></td></tr>~;

		if ($catscount == 1) { $downloadscount = "$msg{'084'} <b>1</b> $msg{'169'}"; }
		else { $downloadscount = "$msg{'086'} <b>$catscount</b> $msg{'170'}"; }

		print qq~</table>
<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">
<tr>
<td align="center">$downloadscount</td>
</tr>~;

if ($adminonlyd eq "1") {
	check_access(editdown); 
		if ($access_granted eq "1") {
		print qq~<tr>
		<td align="center"><a href="$cgi?action=adddownload">$nav{'058'}</a></td>
		</tr>~;
		}
}	

if($username ne "$anonuser") {
	if ($adminonlyd ne "1") {
		print qq~<tr>
		<td align="center"><a href="$cgi?action=adddownload">$nav{'058'}</a></td>
		</tr>~;
	}
}

print qq~</table>~;
	
	show_latestdownloads();
	
	downloads_search();
	
	print qq~</table>~;
	print_bottom();
	exit;
	}
	else {
		
		open(DLNCATS, "$downloadsdir/downloadcats.dat") || error("$err{'001'} $downloadsdir/downloadcats.dat");
		file_lock(DLNCATS);
		@catsname = <DLNCATS>;
		unfile_lock(DLNCATS);
		close(DLNCATS);

		for ($a = 0; $a < @catsname; $a++) {
			($dlname[$a], $dlfolder[$a], $dummy) = split(/\|/, $catsname[$a]);
			if ($info{'cat'} eq $dlfolder[$a]) { 
				$dnlcatsname = $dlname[$a];
			}
		}
		
		$navbar = "$btn{'014'} $nav{'056'} $btn{'014'} $dnlcatsname";
		print_top();

		if ($info{'cat'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
		open(CATS, "$downloadsdir/$info{'cat'}.dat") || error("$err{'001'} $downloadsdir/$info{'cat'}.dat");
		file_lock(CATS);
		@dnlcats = <CATS>;
		unfile_lock(CATS);
		close(CATS);

		for ($a = 0; $a < @dnlcats; $a++) {
			($id[$a], $name[$a], $url[$a], $desc[$a], $date[$a], $downloadposter[$a], $hits[$a], $votes[$a], $score[$a]) = split(/\|/, $dnlcats[$a]);
		}

		if ($info{'start'} eq "") { $start = 0; }
		else { $start = "$info{'start'}"; }
		$numshown = 0;

		print qq~<table border="0" cellpadding="1" cellspacing="0" width="100%">~;
		
		for ($b = $start; $b < @dnlcats; $b++) {
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
			
			print qq~<tr>
			<td><img src="$imagesurl/search/dnld.gif" border="0" alt="">&nbsp;&nbsp;<b><a href="$cgi?action=downloadinfo&amp;cat=$info{'cat'}&amp;id=$id[$b]">$name[$b]</a></b></td>
			</tr><tr>
			<td>$oneliner</td>
			</tr><tr>~;
			
			if ($votes[$b] eq "") {$votes[$b] = "0";}
			if ($score[$b] eq "") {$score[$b] = "0";}

			if ($votes[$b] > 0) { #STOPS DIVISION BY ZERO!
				$averagescore = "0";
				$averagescore = int(($score[$b] * 10) / $votes[$b]);
			}

			print qq~<td><small>$msg{'089'} $date[$b] $nav{'134'} $hits[$b] $msg{'065'} $votes[$b] $msg{'447'} $score[$b]</small></td>
			</tr>~;


			print qq~<tr><td><small>~;

if ($votes[$b] > 0) {
	$greycells = 100 - $averagescore;
	print qq~0%&nbsp;<img src="$imagesurl/rategreen.gif" height="8" width="$averagescore" border="0" alt=""><img src="$imagesurl/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp;100%&nbsp;&nbsp;~;
}else{
	print qq~0%&nbsp;<img src="$imagesurl/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp;100%&nbsp;&nbsp;~;
}

 			print qq~<br><a href="$pageurl/$cgi?action=redirectd&amp;cat=$info{'cat'}&amp;id=$id[$b]" target="_blank">$msg{'646'}</a>~;
			
			if ($username ne $anonuser) {
			if ($username ne $downloadposter[$b]) {print qq~ | <a href="$cgi?action=ratedownloads\&cat=$info{'cat'}\&id=$id[$b]">$nav{'059'}</a>~;
			}
			print qq~&nbsp;|&nbsp;<a href="$pageurl/$cgi?action=imsend&amp;to=admin&amp;subject=$nav{'060'}&amp;msg=$name[$b] ($id[$b]) $msg{'468'} ($msg{'467'})">$nav{'060'}</a>~;
			}

			check_access(editdown); if ($access_granted eq "1") {
			
			print qq~ | <a href="$cgi?action=editdownloads\&cat=$info{'cat'}\&id=$id[$b]">$nav{'131'}</a>~;
			print qq~ | <a href="$cgi?action=deletedownload\&cat=$info{'cat'}\&id=$id[$b]">$nav{'132'}</a>~; 
			print qq~ | <a href="$cgi?action=movedownload\&cat=$info{'cat'}\&id=$id[$b]">$nav{'133'}</a>~;
			print qq~</small></td></tr>~;
			}
			else { print qq~</small></td></tr>~; }

print qq~<tr>
<td>&nbsp;</td>
</tr>
~;
			if ($numshown >= $maxlinks) { $b = @dnlcats; }
		}
		print qq~<tr>
<td>
~;
		if ($numshown >= $maxlinks) {
			print qq~<hr noshade="noshade" size="1">
$msg{'039'} 
~;
			$numlinks = @dnlcats;
			$c = 0;
			while (($c*$maxlinks) < $numlinks) {
				$viewc = $c+1;
				$strt = ($c*$maxlinks);
				if ($start == $strt) { print "$viewc "; }
				elsif ($strt == 0) { print qq~<a href="$cgi?action=downloads&amp;cat=$info{'cat'}">$viewc</a> ~; }
				else { print qq~<a href="$cgi?action=downloads&amp;cat=$info{'cat'}&amp;start=$strt">$viewc</a> ~; }
				++$c;
			}
		}
		print qq~</td>
</tr>
</table>
<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">
~;

	if ($adminonlyd eq "1") {
	check_access(editdown); if ($access_granted eq "1") {
		print qq~<tr>
<td align="center"><a href="$cgi?action=downloads">$nav{'056'} $nav{'033'}</a> | <a href="$cgi?action=adddownload">$nav{'058'}</a></td>
</tr>
~;
}
}	

	if($username ne "$anonuser") {
	if ($adminonlyd ne "1") {
		print qq~<tr>
<td align="center"><a href="$cgi?action=downloads">$nav{'056'} $nav{'033'}</a> | <a href="$cgi?action=adddownload">$nav{'058'}</a></td>
</tr>
~;
	}
	}
		else {
		print qq~<tr>
<td align="center"><a href="$cgi?action=downloads">$nav{'056'} $nav{'033'}</a></td>
</tr>
~;
		}
		print qq~</table>~;
		print_bottom();
		exit;
	}
}

#############
sub download_info {
#############

		if ($info{'cat'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
		open(CATS, "$downloadsdir/$info{'cat'}.dat") || error("$err{'001'} $downloadsdir/$info{'cat'}.dat");
		file_lock(CATS);
		@dnlcats = <CATS>;
		unfile_lock(CATS);
		close(CATS);
		
		open(CAT, "$downloadsdir/downloadcats.dat") || error("$err{'001'} $downloadsdir/downloadcats.dat");
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
			($id[$a], $name[$a], $url[$a], $desc[$a], $date[$a], $downloadposter[$a], $hits[$a], $votes[$a], $score[$a]) = split(/\|/, $dnlcats[$a]);
		  if ($info{'id'} eq $id[$a]) {
				 display_date($date[$a]); $date[$a] = $user_display_date;
				 if ($votes[$a] eq "") {$votes[$a] = "0";}
				 if ($score[$a] eq "") {$score[$a] = "0";}
				 $navbar = "$btn{'014'} $nav{'056'} $btn{'014'} $thiscat $btn{'014'} $name[$a]";
				 print_top();
				 print qq~<table width="100%" border="0" cellpadding="3" cellspacing="1">
				 <tr><td><table width="60%" border="0" cellpadding="3" cellspacing="0">
				 <tr>
				 <td>&nbsp;<img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$pageurl/$cgi?action=downloads">$nav{'056'}</a>
				 <br>
				 <img src="$imagesurl/forum/tline.gif" width="12" height="12" border="0" alt=""><img src="$imagesurl/forum/open.gif" width="17" height="15" border="0" alt="">&nbsp;&nbsp;<a href="$pageurl/$cgi?action=downloads\&cat=$info{'cat'}">$thiscat</a></td>
				 </tr><tr>
				 <td class="forumwindow3">&nbsp;<img src="$imagesurl/search/dnld.gif" border="0" alt="">&nbsp;&nbsp;<b>$name[$a]</b>
				 <br><small>&nbsp;$msg{'089'} $date[$a] $nav{'134'} $hits[$a] $msg{'065'} $votes[$a] $msg{'447'} $score[$a]</small></td>
				 </tr><tr>
				 <td class="forumwindow1">$desc[$a]</td>
				 </tr><tr>
				 <td class="forumwindow1" align="right"><a href="$pageurl/$cgi?action=redirectd&amp;cat=$info{'cat'}&amp;id=$id[$a]" class="polllink" target="_blank">$msg{'646'}</a>&nbsp;</td>
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
				 if ($username ne $downloadposter[$a]) {print qq~<a href="$cgi?action=ratedownloads\&cat=$info{'cat'}\&id=$id[$a]">$nav{'059'}</a>&nbsp;|&nbsp;~;
				 }
				 print qq~<a href="$pageurl/$cgi?action=imsend&amp;to=admin&amp;subject=$nav{'060'}&amp;msg=$name[$a] ($id[$a]) $msg{'468'} ($msg{'467'})">$nav{'060'}</a>~;
				 }
				 
				 check_access(editdown); if ($access_granted eq "1") {
				 print qq~ | <a href="$pageurl/$cgi?action=editdownloads\&cat=$info{'cat'}\&id=$id[$a]">$nav{'131'}</a>~;
				 print qq~ | <a href="$pageurl/$cgi?action=deletedownload\&cat=$info{'cat'}\&id=$id[$a]">$nav{'132'}</a>~; 
				 print qq~ | <a href="$pageurl/$cgi?action=movedownload\&cat=$info{'cat'}\&id=$id[$a]">$nav{'133'}</a>~;
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
sub adddownload {
#############
	if ($username eq "$anonuser" && $adminonlyd ne "1") { error("noguests"); }
	
	if ($adminonlyd eq "1") {
	check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
	}

	open(FILE, "$downloadsdir/downloadcats.dat") || error("downloadcats.dat not found!");
	file_lock(FILE);
	@cats=<FILE>;
	unfile_lock(FILE);
	close(FILE);

	$navbar = "$btn{'014'} $nav{'056'} $btn{'014'} $nav{'058'}";
	print_top();
	print qq~<form method="post" action="$cgi?action=adddownload2">
<table border="0" cellpadding="5" cellspacing="0">
<tr>
<td><b>$msg{'167'}</b></td>
<td><input type="text" name="title" size="40" maxlength="100"></td>
</tr>
<tr>
<td><b>$msg{'168'}</b></td>
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
<td colspan="2"><input type="submit" value="$btn{'018'}"></td>
</tr>
</table>
</form>
~;
	print_bottom();
	exit;
}

##############
sub adddownload2 {
##############
	if ($adminonlyd eq "1") {check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }}
	error("$err{'031'}") unless ($input{'cat'});
	error("$err{'021'}") unless ($input{'title'});
	error("$err{'022'}") unless ($input{'url'});
	error("$err{'023'}") unless ($input{'desc'});
	if (length($input{'desc'}) > 1500) { $input{'desc'} = substr($input{'desc'},0,1500); }
	if($username eq "$anonuser") { error("$err{'011'}"); }
	
	open (DATA, "<$downloadsdir/$input{'cat'}.dat");
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

	open (DATABASE,">$downloadsdir/$input{'cat'}.dat");
	file_lock(DATABASE);
	print DATABASE "$id|$title|$input{'url'}|$desc|$date|$username|0|0|0|\n";
	while ($i < $count) {
		($id, $name, $url, $text, $postdate, $downloadposter, $hits, $votes, $score) = split(/\|/, $datas[$i]);
		chomp($message);
		chomp($subject);
		chomp($name);
		print DATABASE "$id|$name|$url|$text|$postdate|$downloadposter|$hits|$votes|$score|\n";
		$i++;
	}
	unfile_lock(DATABASE);
	close(DATABASE);

	open(CNT, "$downloadsdir/$input{'cat'}.cnt");
	file_lock(CNT);
	$catscount = <CNT>;
	unfile_lock(CNT);
	close(CNT);
	open(DCNT, "$downloadsdir/downloadcats.cnt");
	file_lock(DCNT);
	$downloadcatscount = <DCNT>;
	unfile_lock(DCNT);
	close(DCNT);

	$catscount++;
	$downloadcatscount++;

	open(CNT, ">$downloadsdir/$input{'cat'}.cnt");
	file_lock(CNT);
	print CNT "$catscount";
	unfile_lock(CNT);
	close(CNT);
	open(DCNT, ">$downloadsdir/downloadcats.cnt");
	file_lock(DCNT);
	print DCNT "$downloadcatscount";
	unfile_lock(DCNT);
	close(DCNT);

	success();
}

#############
sub success {
#############
	print_top();
	print qq~<b>$nav{'027'}</b><br>$inf{'019'}~;
	print_bottom();
	exit;
}

##############
sub redirect {
##############
	if ($username eq "$anonuser" ) {       
	if ( $antileech eq "1" ) { error( "$err{'026'}" ); }      } 
	if ($info{'cat'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
	$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$downloadsdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,">$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($id_temp, $name, $url, $desc, $addate, $downloadposter, $hits_temp, $votes, $score) = split(/\|/, $datas[$i]);

		if ($id_temp eq $info{'id'}) {
			$theurl = $url;
			$hits = $hits_temp +1;
			print DATA "$id_temp|$name|$url|$desc|$addate|$downloadposter|$hits|$votes|$score|\n";
		}
		else { print DATA "$id_temp|$name|$url|$desc|$addate|$downloadposter|$hits_temp|$votes|$score|\n"; }
		$i++;
	}
	unfile_lock(DATA);
	close(DATA);

	print "Location: $theurl\n\n";	
}

###################
sub editdownloads {   
###################
	check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }

$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$downloadsdir/$filetoopen") || error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $downloadposter, $hits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		$linkname = htmltotext($linkname);
		$desc = htmltotext($desc);
		
	
	$navbar = "$btn{'014'} $nav{'056'} $btn{'014'} $msg{'385'}";

	print_top();
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form action="$cgi?action=editdownloads2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$msg{'385'}</b></td>
</tr>
<tr>
<td>$msg{'386'}</td>
<td><input type="hidden" name="newtemp" value="$idtemp" size="3">$idtemp</td>
</tr>
<tr>
<td>$msg{'387'}</td>
<td><input type="text" name="nlinkname" value="$linkname" size="30"></td>
</tr>
<tr>
<td>$msg{'388'}</td>
<td><input type="text" name="ntheurl" value="$theurl" size="30"></td>
</tr>
<tr>
<td>$msg{'389'}</td>
<td><textarea name="ndesc" cols="40" rows="5" maxlength="1500">$desc</textarea></td>
</tr>
<tr>
<td>$msg{'390'}</td>
<td><input type="text" name="nthedate" value="$thedate" size="30"></td>
</tr>
<tr>
<td>$msg{'391'}</td>
<td><input type="text" name="ndownloadposter" value="$downloadposter" size="10"></td>
</tr>
<tr>
<td>$msg{'626'}</td>
<td><input type="text" name="nhits" value="$hits" size="3"></td>
</tr>
<tr>
<td>$msg{'627'}</td>
<td><input type="hidden" name="nvotes" value="$votes" size="3">$votes</td>
</tr>
<tr>
<td>$msg{'628'}</td>
<td><input type="hidden" name="nscore" value="$score" size="3">$score</td>
</tr>
<tr>
<td colspan="2"><hr></td>
</tr>
<tr>
<td align="center" colspan="2"><input type="submit" value="$btn{'022'}"></td>
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
	

####################
sub editdownloads2 { 
####################
	check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
	error("$err{'021'}") unless ($input{'nlinkname'});
	error("$err{'022'}") unless ($input{'ntheurl'});
	error("$err{'023'}") unless ($input{'ndesc'});
	error("$err{'006'}") unless ($input{'ndownloadposter'});
	error("$err{'006'}") unless ($input{'nthedate'});
	if ($input{'nhits'} eq "") { error("$err{'006'}"); }
	if (length($input{'ndesc'}) > 1500) { $input{'ndesc'} = substr($input{'ndesc'},0,1500); }
	
	$input{'ndesc'} = htmlescape($input{'ndesc'});
	$input{'nlinkname'} = htmlescape($input{'nlinkname'});
	
	if ($input{'nvotes'} eq "") {$input{'nvotes'} = "0";}
	if ($input{'nscore'} eq "") {$input{'nscore'} = "0";}
	
	$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$downloadsdir/$filetoopen") || error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	open(EDITDATA,">$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(EDITDATA);
	for ($a = 0; $a < @datas; $a++) {
		($idtemp, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $datas[$a]);
		if ($idtemp eq $info{'id'}) {
		print EDITDATA "$input{'newtemp'}|$input{'nlinkname'}|$input{'ntheurl'}|$input{'ndesc'}|$input{'nthedate'}|$input{'ndownloadposter'}|$input{'nhits'}|$input{'nvotes'}|$input{'nscore'}|\n";
		}	else { print EDITDATA "$datas[$a]"; }
	}
	unfile_lock(EDITDATA);
	close(EDITDATA);
	
	print "Location: $cgi\?action=downloads\n\n";
	exit;
}


####################
sub deletedownload {   
####################
	check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
	$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$downloadsdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $downloadposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		
	$navbar = "$btn{'014'} $nav{'056'} $btn{'014'} $nav{'132'}";

	print_top();
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form action="$cgi?action=deletedownload2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$nav{'132'}:</b></td>
</tr>
<tr>
<td>$msg{'386'}</td>
<td>$idtemp</td>
</tr>
<tr>
<td>$msg{'387'}</td>
<td>$linkname</td>
</tr>
<tr>
<td>$msg{'388'}</td>
<td>$theurl</td>
</tr>
<tr>
<td>$msg{'389'}</td>
<td>$desc</td>
</tr>
<tr>
<td>$msg{'390'}</td>
<td>$thedate</td>
</tr>
<tr>
<td>$msg{'391'}</td>
<td>$downloadposter</td>
</tr>
<tr>
<td>$msg{'392'}</td>
<td>$nhits</td>
<input type="hidden" name="score" value="$score">
<input type="hidden" name="votes" value="$votes">
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
	


################
sub deletedownload2 { 
################
	check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
	$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$downloadsdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	open(DATA,">$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
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
	open(DATA,"<$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while (sysread DATA, $buffer, 4096) {
        	$lines += ($buffer =~ tr/\n//);
	}
	unfile_lock(DATA);
	close(DATA);

	if ($lines == 0) {
		unlink "$downloadsdir/$info{'cat'}.dat";
		unlink "$downloadsdir/$info{'cat'}.cnt";
	}else{
		open(CNT, "$downloadsdir/$info{'cat'}.cnt") or error("$err{'016'} $downloadsdir/$info{'cat'}.cnt");#
		file_lock(CNT);
		$catscount = <CNT>;
		unfile_lock(CNT);
		close(CNT);

		$catscount--;

		open(CNT, ">$downloadsdir/$info{'cat'}.cnt") or error("$err{'016'} $downloadsdir/$info{'cat'}.cnt");#
		file_lock(CNT);
		print CNT "$catscount";
		unfile_lock(CNT);
		close(CNT);
	}

	open(LCNT, "$downloadsdir/downloadcats.cnt") or error("$err{'016'} $downloadsdir/downloadcats.cnt");#
	file_lock(LCNT);
	$linkcatscount = <LCNT>;
	unfile_lock(LCNT);
	close(LCNT);

	$linkcatscount--;

	open(LCNT, ">$downloadsdir/downloadcats.cnt") or error("$err{'016'} $downloadsdir/downloadcats.cnt");
	file_lock(LCNT);
	print LCNT "$linkcatscount";
	unfile_lock(LCNT);
	close(LCNT);

	print "Location: $cgi\?action=downloads\n\n";
	exit;
}


##################
sub movedownload {   
##################
	check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$downloadsdir/$filetoopen") || error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	open(FILE, "$downloadsdir/downloadcats.dat") || error("downloadcats.dat Not Found");
	file_lock(FILE);
	@cats2=<FILE>;
	unfile_lock(FILE);
	close(FILE);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$downloadsdir/$filetoopen") || error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $linkname, $theurl, $desc, $thedate, $linkposter, $hits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		
	$navbar = "$btn{'014'} $nav{'056'} $btn{'014'} $nav{'133'}";

	print_top();
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form action="$cgi?action=movedownload2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$nav{'133'}</b></td>
</tr>
<tr>
<td>$msg{'386'}</td>
<td><input type="hidden" name="idtemp" value="$idtemp" size="3">$idtemp</td>
</tr>
<tr>
<td>$msg{'387'}</td>
<td><input type="hidden" name="mlinkname" value="$linkname" size="30">$linkname</td>
</tr>
<tr>
<td>$msg{'388'}</td>
<td><input type="hidden" name="mtheurl" value="$theurl" size="30">$theurl</td>
</tr>
<tr>
<td>$msg{'389'}</td>
<td><input type="hidden" name="mdesc" value="$desc" size="50">$desc</td>
</tr>
<tr>
<td>$msg{'390'}</td>
<td><input type="hidden" name="mthedate" value="$thedate" size="30">$thedate</td>
</tr>
<tr>
<td>$msg{'391'}</td>
<td><input type="hidden" name="mlinkposter" value="$linkposter" size="10">$linkposter</td>
</tr>
<tr>
<td>$msg{'392'}</td>
<td><input type="hidden" name="mhits" value="$hits" size="3">$hits</td>
<input type="hidden" name="mvotes" value="$votes">
<input type="hidden" name="mscore" value="$score">
</tr>
<tr>
<td><b>$msg{'393'} $msg{'092'}</b></td>
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


###################
sub movedownload2 { 
###################
	check_access(editdown); if ($access_granted ne "1") { error("$err{'011'}"); }
	if ($input{'cat2'} eq "") {$input{'cat2'} = "$info{'cat'}";}
	$filetoopen = "$info{'cat'}.dat";

	open (DATA, "<$downloadsdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,">$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
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

	open(CNT, "$downloadsdir/$input{'cat2'}.cnt");
	file_lock(CNT);
	$catscount = <CNT>;
	unfile_lock(CNT);
	close(CNT);

	$idnew = $catscount +1;

	$filetomove2 = "$input{'cat2'}.dat";
	open(DATA2,">>$downloadsdir/$filetomove2") or error("$err{'016'} $filetomove2");
	file_lock(DATA2);
			print DATA2 "$idnew|$input{'mlinkname'}|$input{'mtheurl'}|$input{'mdesc'}|$input{'mthedate'}|$input{'mlinkposter'}|$input{'mhits'}|$input{'mvotes'}|$input{'mscore'}|\n";
	unfile_lock(DATA2);
	close(DATA2);

	$lines = 0;
	open(DATA,"<$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while (sysread DATA, $buffer, 4096) {
        	$lines += ($buffer =~ tr/\n//);
	}
	unfile_lock(DATA);
	close(DATA);

	if ($lines == 0) {
		unlink "$downloadsdir/$info{'cat'}.dat";
		unlink "$downloadsdir/$info{'cat'}.cnt";
	}else{
		open(CNT, "$downloadsdir/$info{'cat'}.cnt");
		file_lock(CNT);
		$catscount = <CNT>;
		unfile_lock(CNT);
		close(CNT);

		$catscount--;

		open(CNT, ">$downloadsdir/$info{'cat'}.cnt");
		file_lock(CNT);
		print CNT "$catscount";
		unfile_lock(CNT);
		close(CNT);
	}

	open(LCNT, "$downloadsdir/downloadcats.cnt");
	file_lock(LCNT);
	$linkcatscount = <LCNT>;
	unfile_lock(LCNT);
	close(LCNT);

	$linkcatscount--;

	open(LCNT, ">$downloadsdir/downloadcats.cnt");
	file_lock(LCNT);
	print LCNT "$linkcatscount";
	unfile_lock(LCNT);
	close(LCNT);

	open(CNT, "$downloadsdir/$input{'cat2'}.cnt");
	file_lock(CNT);
	$catscount = <CNT>;
	unfile_lock(CNT);
	close(CNT);
	open(LCNT, "$downloadsdir/downloadcats.cnt");
	file_lock(LCNT);
	$linkcatscount = <LCNT>;
	unfile_lock(LCNT);
	close(LCNT);

	$catscount++;
	$linkcatscount++;

	open(CNT, ">$downloadsdir/$input{'cat2'}.cnt");
	file_lock(CNT);
	print CNT "$catscount";
	unfile_lock(CNT);
	close(CNT);
	open(LCNT, ">$downloadsdir/downloadcats.cnt");
	file_lock(LCNT);
	print LCNT "$linkcatscount";
	unfile_lock(LCNT);
	close(LCNT);

	print "Location: $cgi\?action=downloads\n\n";
	exit;
}

###################
sub ratedownloads {   
###################

if ($username eq "$anonuser") { error("noguests"); }

$filetoopen = "$info{'cat'}.dat";
	open (DATA, "<$downloadsdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,"$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $downloadname, $theurl, $desc, $thedate, $downloadposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		
		if ($username eq "$downloadposter") { error("$err{'033'}"); }
		
	$navbar = "$btn{'014'} $nav{'056'} $btn{'014'} $nav{'059'}";

	print_top();
	print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form action="$cgi?action=ratedownloads2\&cat=$info{'cat'}\&id=$info{'id'}" method="post">
<td>
</tr>
<tr>
<td colspan="2"><b>$msg{'619'}:</b></td>
</tr>
<tr>
<td>$msg{'620'}</td>
<td><input type="hidden" name="idtemp" value="$idtemp" size="3">$idtemp</td>
</tr>
<tr>
<td>$msg{'621'}</td>
<td><input type="hidden" name="linkname" value="$linkname" size="30">$downloadname</td>
</tr>
<tr>
<td>$msg{'622'}</td>
<td><input type="hidden" name="theurl" value="$theurl" size="30">$theurl</td>
</tr>
<tr>
<td>$msg{'623'}</td>
<td><input type="hidden" name="desc" value="$desc" size="50">$desc</td>
</tr>
<tr>
<td>$msg{'624'}</td>
<td><input type="hidden" name="thedate" value="$thedate" size="30">$thedate</td>
</tr>
<tr>
<td>$msg{'625'}</td>
<td><input type="hidden" name="linkposter" value="$linkposter" size="10">$downloadposter</td>
</tr>
<tr>
<td>$msg{'626'}</td>
<td><input type="hidden" name="nhits" value="$nhits" size="3">$nhits</td>
</tr>
<tr>
<td>$msg{'627'}</td>
<td><input type="hidden" name="votes" value="$votes" size="3">$votes</td>
</tr>
<tr>
<td>$msg{'628'}</td>
<td><input type="hidden" name="score" value="$score" size="3">$score</td>
</tr>
<tr>
<td><b>$msg{'629'}</b></td>
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


####################
sub ratedownloads2 { 
####################

if ($username eq "$anonuser") { error("noguests"); }

	$filetoopen = "$info{'cat'}.dat";

	open (DATA, "<$downloadsdir/$filetoopen") or error("$err{'001'} $filetoopen.dat");
	file_lock(DATA);
	@datas=<DATA>;
	unfile_lock(DATA);
	close(DATA);

	$a = 0;
	while ($datas[$a] ne '') { $a++; }
	$count = $a;
	$i = 0;
	$num = $count +1;

	open(DATA,">$downloadsdir/$filetoopen") or error("$err{'016'} $filetoopen");
	file_lock(DATA);
	while ($i < $count) {
		($idtemp, $downloadname, $theurl, $desc, $thedate, $downloadposter, $nhits, $votes, $score) = split(/\|/, $datas[$i]);

		if ($idtemp eq $info{'id'}) {
		
		if ($username eq "$downloadposter") { error("$err{'033'}"); }
			
			$votes++;
			$score = $score + $input{'rateval'};
			print DATA "$idtemp|$downloadname|$theurl|$desc|$thedate|$downloadposter|$nhits|$votes|$score|\n";
		}else{
			print DATA "$idtemp|$downloadname|$theurl|$desc|$thedate|$downloadposter|$nhits|$votes|$score|\n";
		}
		$i++;
	}
	unfile_lock(DATA);
	close(DATA);

	print "Location: $cgi\?action=downloadinfo\&cat=$info{'cat'}\&id=$info{'id'}\n\n";
	exit;
}


########################
sub downloads_search {
########################

print qq~<table align="center" border="0" cellpadding="3" cellspacing="1" width="80%">
<tr><td align="center" class="forumwindow3" colspan="3"><b>$nav{'039'} $nav{'056'}</b></td></tr>
<tr>
<td align="center" colspan="3">
<form method="POST" action="$pageurl/$cgi\?action=search">
<input type="hidden" name="action" value="search">
<input type="hidden" name="type" value="advanced">
<input type="text" name="pattern_phrase" size="30" class="text">&nbsp;<input type="submit" class="button" value="$btn{'001'}">
<input type="hidden" name="articleson" value="off">
<input type="hidden" name="forumson" value="off">
<input type="hidden" name="linkson" value="off">
<input type="hidden" name="downloadson" value="on">
</form>
</td>
</tr></table>~;

}

##########################
sub show_latestdownloads {
##########################

if ($showlatestdownloads eq "") {$showlatestdownloads = "1";}

if ($showlatestdownloads eq "1") {

latestdownloads();

print qq~<table align="center" border="0" cellpadding="3" cellspacing="1" width="80%">
<tr><td align="center" class="forumwindow3" colspan="3"><b>$msg{'673'}</b></td></tr>
<tr><td align="left" class="forumwindow1"><b>$msg{'167'}</b></td><td align="left" class="forumwindow1"><b>$msg{'088'}</b></td><td align="left" class="forumwindow1"><b>$msg{'110'}</b></td></tr>~;

if (@_ltfinaldownloads) {
   for ($_dtl = 0; $_dtl < @_ltfinaldownloads && $_dtl < 5; $_dtl++) {
      ($_dtlcat, $_dtlid, $_dtlname, $_dtldateref, $_dtldate, $_dtlcount, $_dtldescription) = split(/\|/, $_ltfinaldownloads[$_dtl]);
						display_date($_dtldate); $_dtldate = $user_display_date;
						$message = $_dtldescription;
						$_dtlname = htmltotext($_dtlname);
						$message = htmltotext($message);
						if (length($message) > 70) {
						$tmpmessage = substr($message, 0, 70);
						$tmpmessage =~ s/(.*)\s.*/$1/;
						$_ltdoneliner = "$tmpmessage...";
						}
						else {
						$_ltdoneliner = $message;
						}
						print qq~<tr><td align="left" nowrap><a href="$scripturl/$cgi?action=downloadinfo&amp;cat=$_dtlcat&amp;id=$_dtlid" class="whomenu">$_dtlname</a>~; if ($_dtlcount eq "0" && $_dtldateref < 5) {print qq~&nbsp;<img src="$imagesurl/forum/new.gif" border="0">~;} print qq~</td><td align="left"><small>$_ltdoneliner</small></td><td align="left" nowrap><small>$_dtldate</small></td></tr>~;
			
   }
} else {
	 print qq~<tr><td align="left" colspan="3">$msg{'677'}</td></tr>~;
}

print qq~</table>~;

}

}

if (-e "$scriptdir/user-lib/downloads.pl") {require "$scriptdir/user-lib/downloads.pl"} 

1; # return true

