###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# search.pl	                                                                  #
# v0.9.9 - Requin       									#
#                                                                             #
# Copyright (C) 2002 by WebAPP (webapp@attbi.com)                             #
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
# File: Last modified: 11/09/02                                               #
###############################################################################
###############################################################################

###____________________________________________________________________________________
###
###  PUBLIC VARIABLES DEFINED IN THIS FILE
###
###  %searchdefaults   - Default settings for the search module
###  %searchdata       - copy of $info or $input hash as appropriate
###  $pattern          - The pattern that is currently being matched
###  @patterns         - 2-dimensional array of regex's to be used for matching
###  $searchednum      - Number of data strings that were searched
###  $filecount        - Number of files that were searched
###  $matchednum       - Number of matches that were found
###  @matches          - Array of items that matched the search criteria
###  $pagenum          - Page number we are displaying
###  $fcheck, $fenable - Enable/Disable searching Forums
###  $acheck, $aenable - Enable/Disable searching Articles
###  $lcheck, $lenable - Enable/Disable searching Links
###  $dcheck, $denable - Enable/Disable searching Downloads
###____________________________________________________________________________________
###

###____________________________________________________________________________________
###
###  Function:    find
###  Parameters:  none
###  Usage:       for compatability reasons only
###               some people have find and some have search in their index.cgi
###____________________________________________________________________________________
###
sub find {
	search ();
}

###____________________________________________________________________________________
###
###  Function:    search
###  Parameters:  none
###  Usage:       This is the main entry point for the search engine
###               Called by the main WebApp index.cgi
###____________________________________________________________________________________
###
sub search {

	my $id, $line, $forum, $mdate, $ext;

	#store defaults in this hash - eventually these should move into the admin control panel
	%searchdefaults = (
		forumson          => on,
		articleson        => on,
		linkson           => off,
		downloadson       => off,
		casesensitive     => 'no',
		pagesize          => 20,
		recentsearchcount => 10
	);

	if ($info{'type'} eq "recent") {
		$navbar = "$btn{'014'} $msg{'557'}";
		show_page();
		show_recent_searches();
	}
	elsif ($info{'task'} eq "comment" ) {
		$navbar = "$btn{'014'} $nav{'039'} $btn{'014'} $msg{'407'}";
		show_page();

		$id = $info{'id'};
	 	if ($info{'id'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print "$msg{'630'}"; print_bottom(); exit; }

		$line = $info{'line'};
		show_comment($id, $line);
	}
	elsif ($info{'task'} eq "post") {
		$navbar = "$btn{'014'} $nav{'039'} $btn{'014'} $msg{'408'}";
		show_page();

		$forum = $info{'forum'};
		$mdate = $info{'date'};
		$mdate =~ s/\./\//g;
		$id = $info{'id'};
		if ($info{'id'} =~ /(\$+|\?+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print "$msg{'630'}"; print_bottom(); exit; }

		$ext = $info{'ext'};
		show_post($forum, $id, $mdate, $ext);
	}
	elsif (exists($info{'pattern'}) || exists($input{'pattern'})) {
		$navbar = "$btn{'014'} $nav{'039'}";
		show_page();
		process_search();
	}
	elsif (exists($input{'pattern_all'}) || exists($input{'pattern_any'}) || exists($input{'pattern_phrase'}) || exists($input{'pattern_user'})) {
		$navbar = "$btn{'014'} $nav{'154'}";
		show_page();
		build_pattern();
		process_search();
	}
	elsif ($info{'type'} eq "standard") {
		$navbar = "$btn{'014'} $nav{'039'}";
		show_page();
		show_search_form();
	}
	elsif ($info{'type'} eq "advanced" || $info{'keyword'} eq "AdvancedSearch") {
		# keyword = AdvancedSearch is for compatibility with existing themes.
		$info{'type'} = "advanced";

		$navbar = "$btn{'014'} $nav{'154'}";
		show_page();
		show_search_form();
	}
	else {
		error("$err{'006'}");
	}

	print_bottom();
	exit;
}

###____________________________________________________________________________________
###
###  Function:    build_pattern
###  Parameters:  none
###  Usage:       This function will parse the criteria that is passed in and create
###               a 2-dimensional array containing regex expressions.
###               The first dimension of the array handles OR's and the second
###               dimension handles AND's.
###____________________________________________________________________________________
###
sub build_pattern {

	my $temp = "";
	my $crit, $user, @tmp;
	my @patterns;  #each element in this array will be OR'd together to create the final pattern
	my @criteria = split(/ /,$input{'pattern_any'});
	my @users    = split(/ /,$input{'pattern_user'});

	if ($input{'pattern_all'})    {$temp =  $input{'pattern_all'}};
	if ($input{'pattern_phrase'}) {$temp .= "\"$input{'pattern_phrase'}\""};

	#load OR'd conditions into the @patterns
	foreach $crit (@criteria) {
		push @patterns, "$temp $crit";
	}

	if (scalar(@patterns) == 0) {
		#there were no OR'd conditions - load OR'd users into the array
		foreach $user (@users) {
			push @patterns, "$temp \@$user";
		}
	}
	else {
		#create an element for each combination of existing criteria and user
		if (scalar(@users) != 0) {
			@tmp = (@patterns);
			@patterns = ();
			foreach $user (@users) {
				foreach $crit (@tmp) {
					push @patterns, "$crit \@$user";
				}
			}
		}
	}

	if (scalar(@patterns) == 0) { push @patterns, $temp;}

	$pattern = join " or ", @patterns;
}

###____________________________________________________________________________________
###
###  Function:    parse_pattern
###  Parameters:  none
###  Usage:       This function will parse the criteria that is passed in and create
###               a 2-dimensional array containing regex expressions.
###               The first dimension of the array handles OR's and the second
###               dimension handles AND's.
###____________________________________________________________________________________
###
sub parse_pattern {

	my @criteria  = split(/ /,$pattern);
	my $inphrase  = 0;
	my $group     = 0;
	my $crit      = "";
	my $regex	  = "";
	my $type      = "";

	$#patterns = -1;

	CRITERIA: foreach $crit (@criteria) {
		#are we building a phrase?
		if ($inphrase) {
			#check if this part of the phrase ends with a "
			if ($crit =~ /\"$/) {
				$crit = substr($crit,0,-1);
				$inphrase=0;
			#check if this part of the phrase ends with a "*
			} elsif ($crit =~ /(\"\*)$/) {
				$crit = substr($crit,0,-2)."*";
				$inphrase=0;
			#still in the phrase - tack this part on and get the next part.
			} else {
				$regex .= "$crit ";
				next CRITERIA;
			}

 		}
 		else {
			$regex = "";
			$type  = "data";

			# is this an OR operator?
 			if ($crit =~ /^(or)$/i) {
	 			$group++;
 				next CRITERIA;
 			}

			#are we starting with a wildcard?
			if ($crit =~ /^\*/) {
				$regex .= "(";
				$crit = substr($crit,1);
			}
			else {
				$regex .= "(\\b";
			}
			$regex .= "(";

			#are we searching on username?
			if ($crit =~ /^\@/) {
				$crit = substr($crit,1);
				$type = "user";
			}

			#are we starting a phrase?
 			if ($crit =~ /^\"/) {
 				$crit = substr($crit,1);
 				#does the phrase end here too?  (a one-word phrase)
 				if ($crit =~ /\"$/) {
 					$crit = substr($crit,0,-1);
 				#does the phrase end here with a wildcard?   (a one-word phrase)
				} elsif ($crit =~ /(\"\*)$/) {
					$crit = substr($crit,0,-2)."*";
				# start the phrase then get the next part
 				} else {
 					$regex .= "$crit ";
 					$inphrase=1;
 					next CRITERIA;
 				}
 			}
 		}

		#are we ending with a wildcard?
		if ($crit =~ /\*$/) {
			$crit = substr($crit,0,-1);
			$regex .= "$crit))";
		} else {
			$regex .= "$crit)\\b)";
		}

		#handle case-sensitive searches
		if ( exists($searchdata{'casesensitive'}) ) {
			if ( $searchdata{'casesensitive'} =~ /(n|no)/i ) {
				$regex = "(?i)$regex";
			}
		} elsif ( $searchdefaults{'casesensitive'} =~ /(n|no)/i ) {
			$regex = "(?i)$regex";
		}

		#we have the full expression - compile and store it

		$serverperlversion = $];
		if ($serverperlversion eq "") { ### Default setting that assumes pre version 5.005 of Perl
 		push @{$patterns[$group]}, { type => $type, regex => $regex};
		}
		if ($serverperlversion < "5.005") { ### Use this with Perl versions before 5.005
 		push @{$patterns[$group]}, { type => $type, regex => $regex};
		}
		if ($serverperlversion >= "5.005") { ### Use this with Perl 5.005+   This one is slightly faster.
		push @{$patterns[$group]}, { type => $type, regex => qr/$regex/};
		}
	}
}

###____________________________________________________________________________________
###
###  Function:    process_search
###  Parameters:  none
###  Usage:       This is a control routine that calls the support functions
###               required to perform the search and display the results.
###____________________________________________________________________________________
###
sub process_search {

	my %searchsettings;
	my $starttime, $endtime, $elapsedtime;
	my $i, $numofpages;

	$searchednum = 0;
	$filecount   = 0;
	$matchednum  = 0;
	$#matches    = -1;

	#determine whether to use the $info or $input hash and set the starting page number
	if ($info{'pattern'} ne "" || $info{'type'} eq "advanced") {
		## passed in via URL
		if ($info{'page'} eq "")      { $pagenum = 1; }  else { $pagenum = $info{'page'}; }
		%searchdata = (%info);
	}
	elsif ($input{'pattern'} ne "" || $input{'type'} eq "advanced") {
		## passed in via form submission (user-entered data)
		$pagenum = 1;
		%searchdata = (%input);
	}

	if ($searchdata{'type'} ne "advanced") { $pattern = $searchdata{pattern}; }
	if ($searchdata{'type'} eq "quick")    { %searchsettings = (%searchdefaults)} else {	%searchsettings = (%searchdata) }

	#determine which areas to search
	if ( $searchsettings{'forumson'}    eq "on" ) { $fcheck = "checked"; $fenable = "on" ;} else { $fcheck = "unchecked"; $fenable = "";}
	if ( $searchsettings{'articleson'}  eq "on" ) { $acheck = "checked"; $aenable = "on" ;} else { $acheck = "unchecked"; $aenable = "";}
	if ( $searchsettings{'linkson'}     eq "on" ) { $lcheck = "checked"; $lenable = "on" ;} else { $lcheck = "unchecked"; $lenable = "";}
	if ( $searchsettings{'downloadson'} eq "on" ) { $dcheck = "checked"; $denable = "on" ;} else { $dcheck = "unchecked"; $denable = "";}

	parse_pattern();

	#Start Searching...
	$starttime=time();

	if ($acheck eq "checked") {search_articles();}
	if ($fcheck eq "checked") {search_posts();}
	if ($lcheck eq "checked") {search_links();}
	if ($dcheck eq "checked") {search_downloads();}

	$endtime=time();
	$elapsedtime = $endtime-$starttime;
	#Finished Searching!

	#Start printing the results
	print qq~
	<hr>
	<table>
	<tr><td>$msg{'403'} $matchednum<br>$msg{'404'} $pagenum</td></tr>
	<tr><td>~;

	show_search_form();
	show_results();
	save_recent_search();

	## Print the page numbers
	$numofpages = $matchednum / $searchdefaults{'pagesize'};
	if ($numofpages > int ($numofpages)) { $numofpages = int ($numofpages) +1; } else { $numofpages = int ($numofpages); }
	if ($numofpages > 1) {
		print qq~<b>$msg{'039'}</b>&nbsp;~;
		for ( $i = 1 ; $i <= $numofpages ; $i++) {
			if ( $i == $pagenum ) {
				print qq~[$i]&nbsp; ~;
			}
			else {
				print qq~<a href="$scripturl/$cgi?action=search&pattern=$pattern&page=$i&articleson=$aenable&forumson=$fenable&linkson=$lenable&downloadson=$denable">$i</a>&nbsp~;
			}
		}
	}

	#print a footer based on whether any matches were found
	if ($matchednum == 0) {
		print qq~<br><br>$msg{'631'} <b>"$pattern"</b>.</td></tr></table>~;
	} else {
		print qq~<br><br><a href="#top">$msg{'406'}</a></td></tr></table>~;
	}

	print qq~<BR>$msg{'632'} $searchednum $msg{'633'} $filecount $msg{'634'} $elapsedtime $msg{'635'}.~;

}

###____________________________________________________________________________________
###
###  Function:    execute_search
###  Parameters:  $data - The data to be searched
###               $user - The user who created the data that's being searched
###  Public Vars: IN:     @patterns    - The criteria we're looking for
###               IN/OUT: $searchednum - Counter of number of items we've searched
###                       $matchednum  - Counter of the number of matches we've found
###  Usage:       Loop through all of the conditions to see if we have a match.
###____________________________________________________________________________________
###
sub execute_search {

	my ($data, $user) = @_;

	my $grp, $reg, $comp;

	$searchednum++;

	GROUP: foreach $grp (@patterns) {
		foreach $reg (@$grp) {
			if ($$reg{'type'} eq "user") {
				$comp = $user;
		 	} else {
			 	$comp = $data;
		 	}
		 	if ($comp !~ /$$reg{'regex'}/) {
				# As soon as an AND-ed condition is false, we move on.
		 		next GROUP;
		 	}
	 	}
		# As soon as an OR-ed condition is true, we have a match
		$matchednum++;
		return 1;
	}

	return 0;
}

###____________________________________________________________________________________
###
###  Function:    search_articles
###  Parameters:  none
###  Usage:       Search the articles & article comments
###____________________________________________________________________________________
###
sub search_articles {

	my $curfile, @files, $curarticle, @articles;
	my $title, $realname, $username, $email, $date, $body;
	my $line, $sstring, $type;

	#get a list of files in the articles folder
	opendir (DIR, "$topicsdir/articles");
	@files = readdir(DIR);
	closedir (DIR);

	#filter to include only .txt files
	@files = grep (/\.txt/, @files);

	#search each line in each file
	foreach $curfile (@files) {
		$filecount++;

		open (FILE, "$topicsdir/articles/$curfile");
		@articles = <FILE>;
		close (FILE);

		$line = 0;
		foreach $curarticle (@articles) {
			$line++;
			($title, $realname, $username, $email, $date, $body) = split ( /\|/, $curarticle);
			$sstring = join "|",$title,$body;
			if (execute_search($sstring,$username)) {
				if ($line == 1) {$type = "article";} else {$type = "comment";}
				$curarticle = join '|', $type, $curfile, $line, $title, $title, $realname, $username, $email, $date ;
				push @matches, $curarticle;
			}
		}
	}
}

###____________________________________________________________________________________
###
###  Function:    search_posts
###  Parameters:  none
###  Usage:       Search the forums
###____________________________________________________________________________________
###
sub search_posts {

	my $line, @categories, @checkcats, $curfile, @files, $pointer, @postpointer, $curpost, @posts;
	my $filenum , $title, $realname, $username, $email, $date, $dummy;
	my $i, $sstring;

	open (FILE, "$boardsdir/cats.txt");
	chomp(@categories = <FILE>);
	close (FILE);

	foreach $line (@categories) {
		open (FILE, "$boardsdir/$line.cat");
		chomp(@checkcats = <FILE>);
		close (FILE);
        $checkcats[1] =~ s/[\n\r]//g;
		$checkcats[2] =~ s/[\n\r]//g;

		if ($checkcats[1] ne "") { 	if ($settings[7] ne "$root" && $settings[7] ne "$checkcats[1]") { next; }		}
		for ($i=2;$i<= $#checkcats ; $i++) {
			 push @files, "$checkcats[$i].txt";
			 push @files, "$checkcats[$i].sticky";
		}
	}

	foreach $curfile (@files) {
		$filecount++;

		open (FILE, "$boardsdir/$curfile");
		@postpointer = <FILE>;
		close (FILE);

		foreach $pointer (@postpointer) {

			($filenum , $title, $realname, $username, $email, $date, $dummy, $dummy, $dummy, $dummy, $dummy) = split ( /\|/, $pointer );

			if ($filenum =~ /\d/) {
				open (FILE, "$messagedir/$filenum.txt");
				@posts = <FILE>;
				close (FILE);

				foreach $curpost (@posts) {
					($title, $realname, $email, $date, $username, $dummy, $dummy, $body) = split ( /\|/, $curpost);
					$sstring = join "|",$title,$body;
					if (execute_search($sstring,$username)) {
						$curpost = join '|', "post", $curfile, $filenum, $title, $realname, $username, $email, $date ;
						push @matches, $curpost;
					}
				}
			}
		}
	}
}

###____________________________________________________________________________________
###
###  Function:    search_links
###  Parameters:  none
###  Usage:       Search the links area
###____________________________________________________________________________________
###
sub search_links {

	my $category, @cats, @fields, $cur_cat, @cat_dat;
	my $id, $name, $url, $description, $date, $username, $junk;
	my $sstring;

	if ($info{'cat'} eq "") {
		$filecount++;
		open(CAT, "$linksdir/linkcats.dat") || error("$err{'001'} $linksdir/linkcats.dat");
		file_lock(CAT);
		@cats = <CAT>;
		unfile_lock(CAT);
		close(CAT);

		foreach $category (@cats) {
			@fields = split (/\|/, $category);
			if (-e "$linksdir/$fields[1].dat") {
				open(DATFILE,"$linksdir/$fields[1].dat");
				@cat_dat = <DATFILE>;
				close (DATFILE);

				foreach $cur_cat (@cat_dat)	{
					($id,$name,$url,$description,$date,$username,$junk) = split (/\|/,$cur_cat);
					$sstring = join "|",$name,$url,$description;
					if (execute_search($sstring,$username)) {
						$cur_cat = join "|", "link", $id,$fields[0],$fields[1], $name,$url,$description,$date,$username;
						push @matches, $cur_cat;
					}
				}
			}
		}
	}
}

###____________________________________________________________________________________
###
###  Function:    search_downloads
###  Parameters:  none
###  Usage:       Search the downloads area
###____________________________________________________________________________________
###
sub search_downloads {

	my $category, @cats, @fields, $cur_cat, @cat_dat;
	my $id, $name, $url, $description, $date, $username, $junk;
	my $sstring;

	if ($info{'cat'} eq "") {
		$filecount++;
		open(CAT, "$downloadsdir/downloadcats.dat") || error("$err{'001'} $downloadsdir/downloadcats.dat");
		file_lock(CAT);
		@cats = <CAT>;
		unfile_lock(CAT);
		close(CAT);

		foreach $category (@cats) {
			@fields = split (/\|/, $category);
			if (-e "$downloadsdir/$fields[1].dat") {
				open(DATFILE,"$downloadsdir/$fields[1].dat");
				@cat_dat = <DATFILE>;
				close (DATFILE);

				foreach $cur_cat (@cat_dat)	{
					($id,$name,$url,$description,$date,$username,$junk) = split (/\|/,$cur_cat);
					$sstring = join "|",$name,$url,$description;
					if (execute_search($sstring,$username)) {
						$cur_cat = join "|", "dloads", $id,$fields[0], $fields[1],$name,$url,$description,$date,$username;
						push @matches, $cur_cat;
					}
				}
			}
		}
	}
}

###____________________________________________________________________________________
###
###  Function:    show_page
###  Parameters:  none
###  Usage:       Show WebApp framework & the appropriate search menu options
###____________________________________________________________________________________
###
sub show_page {

	print_top();

	if ($info{'type'} eq "advanced") {
		print qq~<a href="$pageurl/$cgi?action=search&type=standard" class="menu">$msg{'143'} $nav{'039'}</a>~;
	} else {
		print qq~<a href="$pageurl/$cgi?action=search&type=advanced" class="menu">$nav{'154'}</a>~;
	}
	print qq~ | <a href="$pageurl/$cgi?action=search&type=recent" class="menu">$msg{'557'}</a>~;

}

###____________________________________________________________________________________
###
###  Function:    show_search_form
###  Parameters:  none
###  Usage:       Show the standard or advanced search form
###____________________________________________________________________________________
###
sub show_search_form {

	my $csnoval, $csyesval;

	if ($info{'type'} eq "advanced" || $info{'type'} eq "standard" || $info{'type'} eq "recent") {
		if ( $searchdefaults{'forumson'}    eq "on" ) { $fcheck = "checked";} else { $fcheck = "unchecked"; }
		if ( $searchdefaults{'articleson'}  eq "on" ) { $acheck = "checked";} else { $acheck = "unchecked"; }
		if ( $searchdefaults{'linkson'}     eq "on" ) { $lcheck = "checked";} else { $lcheck = "unchecked"; }
		if ( $searchdefaults{'downloadson'} eq "on" ) { $dcheck = "checked";} else { $dcheck = "unchecked"; }
	}

	print qq~
	<hr>
	<form onSubmit="submitonce(this)" method="POST" action="$pageurl/$cgi\?action=search">
	<input type="hidden" name="action" value="search">
	<table border="0" cellpadding="3" cellspacing="0">
	~;

	if ($info{'type'} eq "advanced") {
		print qq~
		<input type="hidden" name="type" value="advanced">
		<TR><TD><b>$msg{'636'}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b></td><td>$msg{'637'}</td><td><input type="text" name="pattern_all" size="25" class="text"></td><td><input type="submit" class="button" value="$btn{'001'}"></td></tr>
		<TR><TD></TD><TD>$msg{'638'}</B></td><td><input type="text" name="pattern_phrase" size="25" class="text"></td><td></td>
		<TR><TD></TD><TD>$msg{'639'}</td><td><input type="text" name="pattern_any" size="25" class="text"></td><td></td></tr>
		<TR><TD></TD><TD>$msg{'640'}</td><td><input type="text" name="pattern_user" size="25" class="text"></td><td></td></tr>
		<TR><TD><b>$msg{'641'}</b></td><td colspan="3">
		~;
	} else {
		$pattern =~ s/\"/&quot;/g;
		print qq~
		<input type="hidden" name="type" value="standard">
		<tr><td colspan="4"><b>$msg{'402'}</b>&nbsp;&nbsp;&nbsp;<input type="text" name="pattern" size="50" value="$pattern">&nbsp;<input type="submit" class="button" value="$btn{'001'}"></td></tr>
		<TR><TD colspan="4" align="center">
		~;
	}

	print qq~
		<input type="checkbox" name="articleson" value="on" $acheck>&nbsp;$nav{'004'}&nbsp;&nbsp;&nbsp;
		<input type="checkbox" name="forumson" value="on" $fcheck>&nbsp;$nav{'003'}&nbsp;&nbsp;&nbsp;
		<input type="checkbox" name="linkson" value="on" $lcheck>&nbsp;$nav{'005'}</tr>
		~;

	if ($info{'type'} eq "advanced") {
		if ($searchdefaults{'casesensitive'} =~ /(y|yes)/i) {
			$csnoval = "";
			$csyesval = "checked";
		} else {
			$csnoval = "checked";
			$csyesval = "";
		}
		print qq~
			<TR>
				<TD><b>$msg{'642'}</b></td>
				<td>$msg{'643'}</td>
				<td colspan="2"><input type="radio" value="yes" name="casesensitive" $csyesval>$nav{'047'}&nbsp;&nbsp;<input type="radio" value="no" name="casesensitive" $csnoval>$nav{'048'}</td>
			</tr>
		~;
	}

	print "</table></form><hr>";

}

###____________________________________________________________________________________
###
###  Function:    show_results
###  Parameters:  none
###  Usage:       Display the results of the search
###____________________________________________________________________________________
###
sub show_results {

	my $i, $testval, $curfle;
	my $type, $curfile, $line, $maintitle, $title, $realname, $username, $email, $date;
	my $type2, $curfile2, $forum, $urldate, $ext, $filenum, $filenum2;
	my $id, $dummy, @lines, $num;
	my $category, $category1, $name, $url, $description;

	print qq~	<table border="0" cellpadding="3" cellspacing="0">~;
	for ($i = ($pagenum * $searchdefaults{'pagesize'}) - ($searchdefaults{'pagesize'})  ; $i <= (($pagenum * $searchdefaults{'pagesize'})-1); $i++) {
		if ($matches[$i] ne ""){
			($type, $curfle) = split (/\|/, $matches[$i]);
			if ($type eq "article") {
				( $type, $curfile, $line, $maintitle, $title, $realname, $username, $email, $date ) = split ( /\|/ , $matches[$i] );
				($id, $dummy) = split ( /\./ , $curfile );
				$date = display_date($date);
				print qq~<img src="$imagesurl/search/topic.gif" alt="$nav{'004'}">&nbsp;<a href="$scripturl/$cgi?action=viewnews&amp;id=$id">$title</a><br>$msg{'110'} $date $msg{'042'}~;
				show_user_link($username, $email);

				$testval = 0;
				while ($testval eq 0) {
					($type2, $curfile2, $line, $maintitle, $title, $realname, $username, $email, $date  ) = split ( /\|/ , $matches[$i+1] );
					if ($curfile eq $curfile2) {
						$i++;
						$date = display_date($date);
						print qq~<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="$imagesurl/search/comments.gif" alt="comment">&nbsp;<a href="$scripturl/$cgi?action=search&amp;task=comment&amp;id=$id&amp;line=$line">$title</a>&nbsp;&nbsp;$msg{'110'} $date $msg{'042'}~;
						show_user_link($username, $email);
					}
					else {
						print "<hr>";
						$testval = 1;
					}
				}
			}
			elsif ($type eq "comment") {
				( $type, $curfile, $line, $maintitle, $title, $realname, $username, $email, $date ) = split ( /\|/ , $matches[$i] );
				($id, $dummy) = split ( /\./ , $curfile );
				$date = display_date($date);
				print qq~<img src="$imagesurl/search/comments.gif" alt="comment">&nbsp;<a href="$scripturl/$cgi?action=search&amp;task=comment&amp;id=$id&amp;line=$line">$title</a><br>$msg{'110'} $date $msg{'042'}~;

				show_user_link($username, $email);
				print qq~<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="$imagesurl/search/bullet.gif" border="0"></a>&nbsp;$msg{'405'} <a href="$scripturl/$cgi?action=viewnews&amp;id=$id">$maintitle</a><hr>~;
			}
			elsif ($type eq "post") {
				( $type, $curfile, $filenum, $title, $realname, $username, $email, $date ) = split ( /\|/ , $matches[$i] );
				$urldate = $date;
				$urldate =~ s/\//\./g;
				($forum, $ext) = split ( /\./ , $curfile );
				$date = display_date($date);
				print qq~<img src="$imagesurl/search/thread.gif" alt="$nav{'003'}">&nbsp;<a href="$scripturl/$cgi?action=search&amp;task=post&amp;id=$filenum&amp;forum=$forum&amp;date=$urldate&amp;ext=$ext">$title</a>&nbsp;&nbsp;$msg{'110'} $date $msg{'042'}~;

				show_user_link($username, $email);
				$testval = 0;
				while ( $testval eq 0 ) {
					($type2, $curfile2, $filenum2, $title, $realname, $username, $email, $date  ) = split ( /\|/ , $matches[$i+1] );
					$urldate = $date;
					$urldate =~ s/\//\./g;
					if ( $type2 eq "post" && $filenum eq $filenum2) {
						$i++;
						$date = display_date($date);
						print qq~<br>&nbsp;&nbsp;<img src="$imagesurl/search/thread.gif" alt="$nav{'003'}">&nbsp;<a href="$scripturl/$cgi?action=search&amp;task=post&amp;id=$filenum&amp;date=$urldate&amp;ext=$ext">$title</a>&nbsp;&nbsp;$msg{'110'} $date $msg{'042'}~;

						show_user_link($username, $email);
					}
					else {
						($type2, $curfile2, $filenum2, $title, $realname, $username, $email, $date  ) = split ( /\|/ , $matches[$i] );

						open (FILE, "$boardsdir/$curfile2");
						@lines = <FILE>;
						close (FILE);

						foreach $line (@lines) {
							($num, $maintitle, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy, $dummy ) = split ( /\|/ , $line );
							if  ($num eq $filenum) {
								print qq~<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="$imagesurl/search/bullet.gif" border="0"></a>&nbsp;$msg{'559'} <a href="$scripturl/$cgi?action=forum&amp;board=$forum&amp;op=display&amp;num=$num">$maintitle</a><hr>~;
							}
						}
						$testval = 1;
					}
				}
			}

			###  Search added for link and download sections
			###  Added 06/07/2002 sburg
			elsif ($type eq "link" ) {
				( $type, $id, $category, $category1, $name, $url, $description ,$date,$username) = split ( /\|/ , $matches[$i] );
				$date = display_date($date);
				print qq~<img src="$imagesurl/search/link.gif" alt="$nav{'005'}">&nbsp;<a href="index.cgi?action=redirect&amp;cat=$category1&amp;id=$id" target="_blank">$name</a><br>$msg{'560'} $nav{'005'}: $category on $date by ~;

				show_user_link($username, $email);
				print qq~<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$msg{'088'} $description<hr>~;
			}
			elsif ($type eq "dloads") {
				( $type, $id, $category, $category1, $name, $url, $description ,$date,$username) = split ( /\|/ , $matches[$i] );
				$date = display_date($date);
				print qq~<img src="$imagesurl/search/dnld.gif" alt="$nav{'056'}">&nbsp;<a href="index.cgi?action=redirectd&amp;cat=$category1&amp;id=$id" target="_blank">$name</a><br>$msg{'560'} $nav{'056'}: $category on $date by ~;

				show_user_link($username, $email);
				print qq~<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$msg{'088'} $description<hr>~;
			}
		}
	}

}

###____________________________________________________________________________________
###
###  Function:    show_comment
###  Parameters:  $id
###               $line
###  Usage:       Show an article or article comment
###____________________________________________________________________________________
###
sub show_comment {

	my ($id, $line) = @_;

	my $viewscount, @comment;
	my $title, $realname, $pusername, $email, $date, $body, $message;

	open (FILE, "$topicsdir/articles/$id.txt");
	@comment = <FILE>;
	close (FILE);

	#increment the view count
	open(CNT, "+<$topicsdir/articles/$id.cnt");
	file_lock(CNT);
	$viewscount = <CNT>;
	$viewscount++;
	seek CNT, 0, 0;
	print CNT "$viewscount";
	unfile_lock(CNT);
	close(CNT);

	#get & display the comment
	($title, $realname, $pusername, $email, $date, $body) = split ( /\|/, $comment[$line-1]);
	$date = display_date($date);

	print qq~<br><table border="0" cellpadding="0" cellspacing="0" width="100%">
	<tr>
	<td class="texttitle">$title</td>
	</tr>
	<tr>
	<td class="textsmall">$date $msg{'042'}
	~;

	show_user_link($pusername,$email);

	print qq~</td>
	</tr>
	<td>&nbsp;</td>
	</tr>
	<tr>
	<td valign="top">
	~;

	$message = "$body";
	if ($enable_ubbc)  { doubbc(); }
	if ($enable_smile) { dosmilies(); }

	print qq~
	$message</td>
	</tr>
	</table>
	<br><hr>
	&nbsp;<a href="$scripturl/$cgi?action=viewnews&id=$id"><img src="$imagesurl/search/bullet.gif" border="0">&nbsp;$msg{'405'}</a>
	~;

}

###____________________________________________________________________________________
###
###  Function:    show_post
###  Parameters:  none
###  Usage:       Show a post
###____________________________________________________________________________________
###
sub show_post {
	my ($forum, $id, $mdate, $ext) = @_;

	my $curline, @lines, @settings, $message;
	my $title, $realname, $email, $date, $username, $dummy,  $body;


	open (FILE, "$messagedir/$id.txt");
	@lines = <FILE>;
	close (FILE);

	foreach $curline (@lines) {
		if ($curline =~ $mdate ) {
			( $title, $realname, $email, $date, $username, $dummy, $dummy,  $body)  = split ( /\|/, $curline);
		}
	}

	open (FILE, "$memberdir/$username.dat");
	@settings = <FILE>;
	close (FILE);

	$mdate = display_date($mdate);

	print qq~
	<table width="100%" bgcolor="#000000" border="0" cellspacing="0" cellpadding="0">
	<tr>
	<td>
	<table width="100%" border="0" cellspacing="1" cellpadding="2">
	<tr>
	<td bgcolor="#eeeeee">
	<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr>
	<td><img src="$imagesurl/forum/thread.gif" alt=""></td>
	<td>&nbsp;<b>$msg{'049'}</b></td>
	</tr>
	</table>
	</td>
	<td bgcolor="#eeeeee"><b>$msg{'409'} $forum</b></td>
	</tr>
	<tr>
	<td bgcolor="#ffffff" width="140" valign="top"><b>$username</b><br>
	<img src="
	~;

	if ($settings[9] !~ /http\:\/\//) {print qq~$imagesurl/avatars/$settings[9]~;} else { print qq~$settings[9]~ ; }

	print qq~" width="60" height="93" border="0" alt=""></a><br>
	<br><br><br>
	Forumposts: $settings[6]<br>
	Articles: $settings[11]<br>
	Comments: $settings[12]<br>
	<br>
	</td>
	<td bgcolor="#ffffff" valign="top">
	<table border="0" cellspacing="0" cellpadding="0" width="100%">
	<tr>
	<td><img src="$imagesurl/forum/xx.gif" alt=""></td>
	<td width="100%">&nbsp;<b>$title</b></td>
	<td align="right" nowrap>&nbsp;<b>$msg{'110'}</b> $mdate </td>
	</tr>
	</table>
	<hr noshade="noshade" size="1">
	~;

	$message = "$body";
	if ($enable_ubbc)  { doubbc(); }
	if ($enable_smile) { dosmilies(); }

	print qq~
	$message
	<br> <br> <br>
	----------------- <br>
	$settings[5]
	<br>
	</td>
	</tr>
	</table>
	</td>
	</tr>
	</table>
	<br><hr>
	<br>&nbsp;<a href="$scripturl/$cgi?action=forum&board=$forum&op=display&num=$id"><img src="$imagesurl/search/bullet.gif" border="0">&nbsp;$msg{'559'} </a>
	~;

}

###____________________________________________________________________________________
###
###  Function:    show_user_link
###  Parameters:  $username - a users name
###               $email    - a users email address
###  Usage:       Show a user link - handles hiding email addresses if necessary
###____________________________________________________________________________________
###
sub show_user_link {
	my ($username, $email) = @_;

	if ($hidemail eq "1" || $hidemail eq "") {
		if ($username eq $anonuser) {
			print qq~<b> $username</b>~;
		} else {
			print qq~<a href="$cgi?action=anonemail&sendto=$username"> $username</a>~;
		}
	} else {
		print qq~<a href="mailto:$email"> $username</a>~;
	}
}

###____________________________________________________________________________________
###
###  Function:    save_recent_search
###  Parameters:  none
###  Usage:       Save info about the search that was just performed
###____________________________________________________________________________________
###
sub save_recent_search {

	my $search, @searches, @oldsearches;
	my $srch, $mtch;

	open(FILE,"$datadir/searches.txt");
	@searches = <FILE>;
	close(FILE);

	#Check if recent searches contains this search
	foreach $search(@searches) {
		($srch, $mtch) = split (/\|/, $search);
		chomp($srch);
		if ($pattern eq $srch){
			return;
		}
	}

	if ($#searches <= ($searchdefaults{'recentsearchcount'} - 1)) {
		#we don't have the max number of recent searches yet, so just append the current search to the list.
		open(FILE, ">>$datadir/searches.txt");
		file_lock(FILE);
		print FILE "$pattern|$matchednum\n";
		unfile_lock(FILE);
		close(FILE);
	} else {
		#we have the max number of recent searches, so remove the first one, shift the rest up and add this one to the end.
		open(FILE,"$datadir/searches.txt");
		chomp(@oldsearches = <FILE>);
		close(FILE);
		open(FILE, ">$datadir/searches.txt");
		file_lock(FILE);
		for (1 .. ($searchdefaults{'recentsearchcount'} - 1)) {
			print FILE "$oldsearches[$_]\n";
		}
		print FILE "$pattern|$matchednum\n";
		unfile_lock(FILE);
		close(FILE);
	}

}

###____________________________________________________________________________________
###
###  Function:    show_recent_searches
###  Parameters:  none
###  Usage:       Show a list of the most recent searches
###____________________________________________________________________________________
###
sub show_recent_searches {

	my $search, @searches, $censor, @censored;
	my $srch, $mtch, $word, $censored;
	my $n;

	open(FILE,"$datadir/searches.txt");
	@searches = <FILE>;
	close(FILE);

	open(CENSOR, "$boardsdir/censor.txt");
	chomp(@censored = <CENSOR>);
	close(CENSOR);

	print qq~
	<hr>
	<table border="0" cellpadding="3" cellspacing="0">
	~;

	$n=0;
	foreach $search(@searches) {
		chomp($search);
		($srch, $mtch) = split (/\|/, $search);
		if ($srch ne ""){
			$n++;

			foreach $censor (@censored) {
				($word, $censored) = split(/\=/, $censor);
				$srch =~ s/$word/$censored/g;
			}

			print qq~<tr><td>$n.</td><td><a href="$pageurl/$cgi?action=search&type=quick&pattern=$srch&page=1&articleson=on&forumson=on&linkson=on&downloadson=on" class="menu">$srch</a>&nbsp;($mtch)</td></tr>~;
		}
	}

	if ($n eq 0) {
		print qq~<tr><td><b>$msg{'558'}</b></td></tr>~;
	}

	print "</table>";

	show_search_form();

}

if (-e "$scriptdir/user-lib/search.pl") {require "$scriptdir/user-lib/search.pl"}

1; # return true