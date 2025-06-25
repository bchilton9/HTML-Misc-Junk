###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# top10.pl                  								      #
# v0.9.9 - Requin                                                             #
#                                                                             #
# Copyright (C) 2002 by Carter (carter@mcarterbrown.com)                      #
# Added by Shawn Raloff                                                       #
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

#
# Based on top10.pl from YaWPS - Yet another web Portal System 
#
# Copyright (C) 2001 by Adrian Heiszler (heiszler@gmx.net) 
#
# Edited to be compatable with WebAPP
#
# Thanks to Adrian for making a great script!
#
# Edited 6-20-02 by Carter
#

####################
sub top10_articles {
####################
	my $_query = shift;
	my (@_tarticles, @_tasorted, @_tadata, @_tasortedtarticles) = ();

	opendir (DIR, "$topicsdir");
	@_files = readdir(DIR);
	closedir (DIR);
	@_tcatfiles = grep(/cat/, @_files);

	foreach $t (@_tcatfiles) {
		open(FILE, "<$topicsdir/$t") || error("$err{'001'} $topicsdir/$t");
		chomp(@_ttopicdata = <FILE>);
		close(FILE);
		for ($x = 0; $x < @_ttopicdata; $x++) {
			($_ttnum, $_ttsubject, $dummy, $dummy, $dummy, $dummy, $_ttcomments, $_ttviews) = split(/\|/, $_ttopicdata[$x]);
			if ($_query != 1) {
				if ($_ttviews != 0) {
					push (@_tarticles, join ("\|", $_ttnum, $_ttsubject, $_ttviews));
				}
			}
			else {
				if ($_ttcomments != 0) {
					push (@_tarticles, join ("\|", $_ttnum, $_ttsubject, $_ttcomments));
				}
			}
		}
	}

	for (0..$#_tarticles) {
		@_tafields = split(/\|/, $_tarticles[$_]);
		for $i (0..$#_tafields) {
			$_tadata[$_][$i] = $_tafields[$i];
		}
	}
	@_tasorted = reverse sort { $a->[2] <=> $b->[2] } @_tadata;
	for (@_tasorted) { 
		$_tasortedrow = join ("|", @$_);
		push (@_tasortedtarticles, $_tasortedrow);
	}

	for ($_tt = 0; $_tt < @_tasortedtarticles && $_tt < 10; $_tt++) {
		($tanum, $tasubject, $tacount) = split(/\|/, $_tasortedtarticles[$_tt]);
		print qq~<li><a href="$cgi?action=viewnews&amp;id=$tanum">$tasubject</a> ($tacount)</li>\n~;
	}
}

########################
sub top10_article_cats {
########################
	open(FILE, "<$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
	chomp(@tcats = <FILE>);
	close(FILE);

	foreach (@tcats) {
		@item = split(/\|/, $_);
		if (-e("$topicsdir/$item[1].cat")) {
			open(FILE, "<$topicsdir/$item[1].cat") || error("$err{'001'} $topicsdir/$item[1].cat");
			@content = <FILE>;
			close(FILE);
			$ccount = @content;

			if ($ccount != 0) {
				push (@_tcats, join ("\|", $item[0], $item[1], $ccount));
			}
		}
	}

	for (0..$#_tcats) {
		@_tcfields = split(/\|/, $_tcats[$_]);
		for $i (0..$#_tcfields) {
			$_tcdata[$_][$i] = $_tcfields[$i];
		}
	}
	@_tcsorted = reverse sort { $a->[2] <=> $b->[2] } @_tcdata;
	for (@_tcsorted) { 
		$_tcsortedrow = join ("|", @$_);
		push (@_tcsortedtcats, $_tcsortedrow);
	}

	for ($_tc = 0; $_tc < @_tcsortedtcats && $_tc < 10; $_tc++) {
		($tcname, $tclink, $tccount) = split(/\|/, $_tcsortedtcats[$_tc]);
		print qq~<li><a href="$cgi?action=topics&amp;viewcat=$tclink">$tcname</a> ($tccount)</li>~;
	}
}

######################
sub top10_forumposts {
######################
	my $_query = shift;
	my (@_tposts, @_tpsorted, @_tpdata, @_tpsortedtposts) = ();

	open(FILE, "<$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
	@_tfcats = <FILE>;
	close(FILE);

	foreach $_tf (@_tfcats) {
		chomp($_tf);

						if ($_tf[1] ne "") {
						if ($settings[7] ne "$root" && $settings[7] ne "$_tf[1]") {      next; }
						}

		open(FILE, "<$boardsdir/$_tf.cat") || error("$err{'001'} $boardsdir/$_tf.cat");
		@_tcatinfo = <FILE>;
		close(FILE);

		$_tcatinfo[1] =~ s/[\n\r]//g;
		foreach $_tboard (@_tcatinfo) {
			if ($_tboard ne $_tcatinfo[0] && $_tboard ne $_tcatinfo[1]) {
				$_tboard =~ s/[\n\r]//g;
										if ($_tcatinfo[1] ne "") {
						if ($settings[7] ne "$root" && $settings[7] ne "$_tcatinfo[1]") {      next; }
						}

				open(FILE, "<$boardsdir/$_tboard.txt") || error("$err{'001'} $boardsdir/$_tboard.txt");
				file_lock(FILE);
				@_tfmessages = <FILE>;
				unfile_lock(FILE);
				close(FILE);
				
				####### abywn: added to include stickies
				open(FILE, "<$boardsdir/$_tboard.sticky") || error("$err{'001'} $boardsdir/$_tboard.sticky");
				@_tfmessagessticky = <FILE>;
				close(FILE);
				@_tfmessages = (@_tfmessages, @_tfmessagessticky);
				####### abywn: end of added code
				
				for ($_tf = 0; $_tf < @_tfmessages; $_tf++) {
					($_tfmnum, $_tfmsub, $dummy, $dummy, $dummy, $dummy, $_tfmreplies, $_tfmviews, $dummy, $dummy, $dummy) = split(/\|/, $_tfmessages[$_tf]);
					if ($_query != 1) {
						if ($_tfmviews != 0) {
							push (@_tposts, join ("\|", $_tfmnum, $_tboard, $_tfmsub, $_tfmviews));
						}
					}
					else {
						if ($_tfmreplies != 0) {
							push (@_tposts, join ("\|", $_tfmnum, $_tboard, $_tfmsub, $_tfmreplies));
						}
					}
				}
			}
		}
	}

	for (0..$#_tposts) {
		@_tpfields = split(/\|/, $_tposts[$_]);
		for $i (0..$#_tpfields) {
			$_tpdata[$_][$i] = $_tpfields[$i];
		}
	}
	@_tpsorted = reverse sort { $a->[3] <=> $b->[3] } @_tpdata;
	for (@_tpsorted) { 
		$_tpsortedrow = join ("|", @$_);
		push (@_tpsortedtposts, $_tpsortedrow);
	}

	for ($_tp = 0; $_tp < @_tpsortedtposts && $_tp < 10; $_tp++) {
		($_tpnum, $_tpboard, $_tpsub, $_tpcount) = split(/\|/, $_tpsortedtposts[$_tp]);
		print qq~<li><a href="$cgi?action=forum&amp;board=$_tpboard&amp;op=display&amp;num=$_tpnum">$_tpsub</a> ($_tpcount)</li>~;
	}
}

###########################
sub top10_forumposts_cats {
###########################
	open(FILE, "<$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
	@_tbcats = <FILE>;
	close(FILE);

	foreach $_tb (@_tbcats) {
		chomp($_tb);
		open(FILE, "<$boardsdir/$_tb.cat") || error("$err{'001'} $boardsdir/$_tb.cat");
		@_tbcatinfo = <FILE>;
		close(FILE);

		$_tbcatinfo[1] =~ s/[\n\r]//g;
		foreach $_tbboard (@_tbcatinfo) {
			if ($_tbboard ne $_tbcatinfo[0] && $_tbboard ne $_tbcatinfo[1]) {
				$_tbboard =~ s/[\n\r]//g;
											if ($_tbcatinfo[1] ne "") {
						if ($settings[7] ne "$root" && $settings[7] ne "$_tbcatinfo[1]") {      next; }
						}

				open(FILE, "<$boardsdir/$_tbboard.dat") || error("$err{'001'} $boardsdir/$_tbboard.dat");
				@_tbdesc = <FILE>;
				close(FILE);
				$_tbboardname = $_tbdesc[0];

				open(FILE, "<$boardsdir/$_tbboard.txt") || error("$err{'001'} $boardsdir/$_tbboard.txt");
				@_tbmessages = <FILE>;
				close(FILE);
				$_tbcount = @_tbmessages;

				if ($_tbcount != 0) {
					push (@_tboards, join ("\|", $_tbboardname, $_tbboard, $_tbcount));
				}
			}
		}
	}

	for (0..$#_tboards) {
		@_tbfields = split(/\|/, $_tboards[$_]);
		for $i (0..$#_tbfields) {
			$_tbdata[$_][$i] = $_tbfields[$i];
		}
	}
	@_tbsorted = reverse sort { $a->[2] <=> $b->[2] } @_tbdata;
	for (@_tbsorted) { 
		$_tbsortedrow = join ("|", @$_);
		push (@_tbsortedtposts, $_tbsortedrow);
	}

	for ($_tb = 0; $_tb < @_tbsortedtposts && $_tb < 10; $_tb++) {
		($_tbn, $_tbb, $_tbc) = split(/\|/, $_tbsortedtposts[$_tb]);
		print qq~<li><a href="$cgi?action=forum&amp;board=$_tbb">$_tbn</a> ($_tbc)</li>~;
	}
}

#################
sub top10_polls {
#################
	open(FILE, "<$datadir/polls/polls.txt");
	@_polls = <FILE>;
	close(FILE);

	foreach (@_polls) {
		@_pitem = split(/\|/, $_);

		open(FILE, "<$datadir/polls/$_pitem[0]_a.dat") || error("$err{'001'} $datadir/polls/$_pitem[0]_a.dat");
		chomp(@_polldata = <FILE>);
		close(FILE);

		$_sum = 0;
		foreach (@_polldata) { 
			$_sum += $_; 
		}
		if ($_sum != 0) {
			push (@_tpolls, join ("\|", $_pitem[0], $_pitem[1], $_sum));
		}
	}

	for (0..$#_tpolls) {
		@_tpofields = split(/\|/, $_tpolls[$_]);
		for $i (0..$#_tpofields) {
			$_tpodata[$_][$i] = $_tpofields[$i];
		}
	}
	@_tposorted = reverse sort { $a->[2] <=> $b->[2] } @_tpodata;
	for (@_tposorted) { 
		$_tposortedrow = join ("|", @$_);
		push (@_toppolls, $_tposortedrow);
	}

	for ($_tpo = 0; $_tpo < @_toppolls && $_tpo < 10; $_tpo++) {
		($_tpoid, $_tponame, $_tpocount) = split(/\|/, $_toppolls[$_tpo]);
		print qq~<li><a href="$cgi?action=pollit2&amp;id=$_tpoid&amp;title=$_tponame">$_tponame</a> ($_tpocount)</li>~;
	}
}

#################
sub top10_links {
#################

@_lcats = ();
@_litem = ();
@_lcontent = ();
@_tlcats = ();
@_tlfields = ();
@_tlsorted = ();
@_tlinks = ();

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
				($_lid, $_lname, $_lurl, $dummy, $dummy, $dummy, $_lcount) = split(/\|/, $_lcontent[$_tl]);
				if ($_lcount != 0) {
					push (@_tlcats, join ("\|", $_litem[1], $_lid, $_lname, $_lcount));
				}
			}
		}
	}

	for (0..$#_tlcats) {
		@_tlfields = split(/\|/, $_tlcats[$_]);
		for $i (0..$#_tlfields) {
			$_tldata[$_][$i] = $_tlfields[$i];
		}
	}
	@_tlsorted = reverse sort { $a->[3] <=> $b->[3] } @_tldata;
	for (@_tlsorted) { 
		$_tlsortedrow = join ("|", @$_);
		push (@_tlinks, $_tlsortedrow);
	}

	for ($_tl = 0; $_tl < @_tlinks && $_tl < 10; $_tl++) {
		($_tlcat, $_tlid, $_tlname, $_tlcount) = split(/\|/, $_tlinks[$_tl]);
		print qq~<li><a href="$cgi?action=redirect&amp;cat=$_tlcat&amp;id=$_tlid" target="_blank">$_tlname</a> ($_tlcount)</li>~;
	}
}

######################
sub top10_links_cats {
######################

@_lcats = ();
@_litem = ();
@_tlcatcount = ();
@_tlcfields = ();
@_tlcfields = ();
@_tlcsorted = ();
@_tlinkcats = ();

	open(CAT, "<$linksdir/linkcats.dat") || error("$err{'001'} $linksdir/linkcats.dat");
	@_lcats = <CAT>;
	close(CAT);

	foreach (@_lcats) {
		@_litem = split(/\|/, $_);
		if (-e("$linksdir/$_litem[1].dat")) {
			open(FILE, "<$linksdir/$_litem[1].cnt") || error("$err{'001'} $linksdir/$_litem[1].cnt");
			chomp($_lcatcount = <FILE>);
			close(FILE);

			push (@_tlcatcount, join ("\|", $_litem[0], $_litem[1], $_lcatcount));
		}
	}

	for (0..$#_tlcatcount) {
		@_tlcfields = split(/\|/, $_tlcatcount[$_]);
		for $i (0..$#_tlcfields) {
			$_tlcdata[$_][$i] = $_tlcfields[$i];
		}
	}
	@_tlcsorted = reverse sort { $a->[2] <=> $b->[2] } @_tlcdata;
	for (@_tlcsorted) { 
		$_tlcsortedrow = join ("|", @$_);
		push (@_tlinkcats, $_tlcsortedrow);
	}

	for ($_tlc = 0; $_tlc < @_tlinkcats && $_tlc < 10; $_tlc++) {
		($_tlcname, $_tlccat, $_tlccount) = split(/\|/, $_tlinkcats[$_tlc]);
		print qq~<li><a href="$cgi?action=links&amp;cat=$_tlccat">$_tlcname</a> ($_tlccount)</li>~;
	}
}

#################
sub top10_users {
#################
	open(FILE, "<$memberdir/memberlist.dat");
	chomp(@_memberlist = <FILE>);
	close(FILE);

	foreach $_tmember (@_memberlist) {
		open(FILE, "<$memberdir/$_tmember.dat");
		chomp(@_members = <FILE>);
		close(FILE);

		$_tusr = $_members[6]+$_members[11]+$_members[12];

		if ($_tusr != 0) {
			push (@_tmembers, join ("\|", $_tmember, $_members[1], $_tusr));
		}
	}

	for (0..$#_tmembers) {
		@_tmfields = split(/\|/, $_tmembers[$_]);
		for $i (0..$#_tmfields) {
			$_tmdata[$_][$i] = $_tmfields[$i];
		}
	}
	@_tmsorted = reverse sort { $a->[2] <=> $b->[2] } @_tmdata;
	for (@_tmsorted) { 
		$_tmsortedrow = join ("|", @$_);
		push (@_tusers, $_tmsortedrow);
	}

	for ($_tm = 0; $_tm < @_tusers && $_tm < 10; $_tm++) {
		($_tmid, $_tmname, $_tmc) = split(/\|/, $_tusers[$_tm]);
		print qq~<li><a href="$cgi?action=viewprofile&amp;username=$_tmid">$_tmname</a> ($_tmc)</li>~;
	}
}

################
sub show_top10 {
################
	$navbar = "$btn{'014'} $nav{'007'}";
	print_top();
	print qq~

<ul>
~;
	top10_articles();
	print qq~</ul>
<b>$nav{'142'}</b><br>
<ul>
~;
	top10_articles(1);
	print qq~</ul>
<b>$nav{'143'}</b><br>
<ul>
~;
	top10_article_cats();
	print qq~</ul>
<b>$nav{'144'}</b><br>
<ul>
~;
	top10_forumposts();
	print qq~</ul>
<b>$nav{'145'}</b><br>
<ul>
~;
	top10_forumposts(1);
	print qq~</ul>
<b>$nav{'146'}</b><br>
<ul>
~;
	top10_forumposts_cats();
	print qq~</ul>
<b>$nav{'147'}</b><br>
<ul>
~;
	top10_links();
	print qq~</ul>
<b>$nav{'148'}</b><br>
<ul>
~;
	top10_links_cats();
	print qq~</ul>
<b>$nav{'149'}</b><br>
<ul>
~;
	top10_polls();
	print qq~</ul>
<b>$nav{'150'}</b><br>
<ul>
~;
	top10_users();
	print "</ul>";
	print_bottom();
	exit;
}

if (-e "$scriptdir/user-lib/top10.pl") {require "$scriptdir/user-lib/top10.pl"} 

1; # return true
