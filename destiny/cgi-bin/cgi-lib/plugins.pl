###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# plugins.pl 			                                                #
# v0.9.9 - Requin                                                             #
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
# File: Last modified: 08/01/02                                               #
###############################################################################
###############################################################################

###############################################################################
###############################################################################
# About:                                                                      #
# The object of this file is to make the themes upwards compatible.           #
#                                                                             #
#                                                                             #
# There are Four sections:                                                    #
# left_top_plugins();                                                         #
# left_bottom_plugins();                                                      #
# right_top_plugins();                                                        #
# right_bottom_plugins();                                                     #
#                                                                             #
#                                                                             #
# This way the programmes can add code here, to add new sections to the themes#
# and not affect the themes themeselves.  Allowing users to keep customized   #
# themes, and keeping us from messing them up.                                #
#                                                                             #
#                                                                             #
# These are currently left blank intentionally...                             #
# Current Date: 07/24/02                                                      #
###############################################################################
###############################################################################


######################
sub left_top_plugins {
######################
# these blocks will be located below the main me


}


#########################
sub left_bottom_plugins {
#########################
# These blocks will be located above the left blocks

}


#######################
sub right_top_plugins {
#######################
# These blocks are located below the poll

boxheader("Guild Information");

print qq~<tr><td><TABLE BORDER=0 WIDTH=100%>~; 

$url = "http://eq2players.station.sony.com/en/guild.vm?guildId=432113";

use CGI qw(param);
use LWP::Simple;

$page = get($url);


$page =~ /<span class="field_name_small">Members:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD>Members:</TD><TD><B>$1</B></TD></TR>";


$page =~ /<span class="field_name_small">Guild Level:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD>Guild Level:</TD><TD><B>$1</B></TD></TR>";


$page =~ /<span class="field_name_small">Status:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD>Status:</TD><TD><B>$1</B></TD></TR>";


print qq~
<TR><TD>
<A HREF=http://www.sanctuaryeq2.com/cgi-bin/mods/showhtml/showhtml.pl?id=stats>More...</A></TD><TD></TD></TR>

</TABLE></td></td>
~; 

boxfooter(); 

}


##########################
sub right_bottom_plugins {
##########################
# These blocks will be located above the info block

#boxheader("Future Events");

#print qq~<tr><td>~; 
#require "$scriptdir/mods/calendar/futureevents.cgi"; 

#cal_displayfutureevents(); 
#print qq~</td></td>~; 

#boxfooter(); 
 


#ugdisplay(0);

}

###################
sub ugdisplay {
###################

my ($ugplugin)=@_;

require "$scriptdir/mods/usergallery/usergallery.cfg"; # User Gallery config
require "$scriptdir/mods/usergallery/admin/ugsetup.dat"; # User Gallery settings
require "$scriptdir/mods/usergallery/config.dat"; # User Gallery config.dat file

mod_langsupp();

if ($ugplugin eq "0") { ugpotm(); }
elsif ($ugplugin eq "1") { ughotpics(); }
else { ugpotm(); }

}

###################
sub ugpotm {
###################

@pcats = ();
@palbums = ();
@ppictures = ();
@showpicitem = ();

	open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
	file_lock(FILE);
	chomp(@pcats = <FILE>);
	unfile_lock(FILE);
	close(FILE);
	
	foreach $curalb (@pcats) {
	$curalb =~ s/[\n\r]//g;
	@curitem = split (/\|/, $curalb);
			open(FILE, "$usergallerydb/$curitem[0].cat");
			file_lock(FILE);
			chomp(@palbums = <FILE>);
			unfile_lock(FILE);
			close(FILE);
			
			foreach $curpic (@palbums) {
			$curpic =~ s/[\n\r]//g;
			@curpicitem = split (/\|/, $curpic);
			$thepictures = join '|', $curitem[0], $curitem[1], $curpicitem[0], $curpicitem[2], $curpicitem[3] ;
			push @ppictures, $thepictures;
			}
	}

$randint = int rand @ppictures;
@showpicitem = split (/\|/, $ppictures[$randint]);			

boxheader("$ug{'049'}");

print qq~
   <tr><td align="center" class="newstextsmall">			
<a href="$usergalleryurl/index.cgi?action=showpicture&amp;album=$showpicitem[0]&amp;id=$showpicitem[2]&amp;albumname=$showpicitem[1]"><img src="$usergalleryimagesurl/$showpicitem[4]" border="0" width="140" height="140" alt="$showpicitem[3]"></a><br><b>$showpicitem[3]</b>
   </td></tr>
~;

boxfooter();
@pcats = ();
@palbums = ();
@ppictures = ();
@showpicitem = ();

}

###################
sub ughotpics {
###################

@pcats = ();
@palbums = ();
@_uglist = ();
@_ugfields = ();
@_ugdata = ();
@_ugsorted = ();
@_ugsortedrow = ();
@_ugdone = ();

	open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
	file_lock(FILE);
	chomp(@pcats = <FILE>);
	unfile_lock(FILE);
	close(FILE);
	
	foreach $curalb (@pcats) {
	$curalb =~ s/[\n\r]//g;
	@curitem = split (/\|/, $curalb);
			open(FILE, "$usergallerydb/$curitem[0].cat");
			file_lock(FILE);
			chomp(@palbums = <FILE>);
			unfile_lock(FILE);
			close(FILE);
			
			foreach $curpic (@palbums) {
			$curpic =~ s/[\n\r]//g;
			@curpicitem = split (/\|/, $curpic);
			$thepictures = join '|', $curpicitem[5], $curitem[0], $curitem[1], $curpicitem[0], $curpicitem[2] ;
			push @_uglist, $thepictures;
			}
	}
	
	for (0..$#_uglist) {
		@_ugfields = split(/\|/, $_uglist[$_]);
		for $i (0..$#_ugfields) {
			$_ugdata[$_][$i] = $_ugfields[$i];
		}
	}

@_ugsorted = reverse sort { $a->[0] <=> $b->[0] } @_ugdata;

for (@_ugsorted) { 
		$_ugsortedrow = join ("|", @$_);
		push (@_ugdone, $_ugsortedrow);
}
	
boxheader("$ug{'048'}");	
	
	for ($_tug = 0; $_tug < @_ugdone && $_tug < 10; $_tug++) {
		($_tugcount, $_tugaid, $_tugalbum, $_tugpid, $_tugname) = split(/\|/, $_ugdone[$_tug]);
		$tugnumber = $_tug+1; print qq~<tr><td align="left" class="whocat">$tugnumber.</td><td align="left" class="whocat"><a href="$usergalleryurl/index.cgi?action=showpicture&amp;album=$_tugaid&amp;id=$_tugpid&amp;albumname=$_tugalbum" class="whomenu">$_tugname</a></td><td align="left" class="whocat">$_tugcount</td></tr>~;
	}			

print qq~<tr><td align="right" class="whocat" colspan="3"><a href="$usergalleryurl/index.cgi" class="whomenu">$ug{'001'}</a></td></tr>~;

boxfooter();
@pcats = ();
@palbums = ();
@_uglist = ();
@_ugfields = ();
@_ugdata = ();
@_ugsorted = ();
@_ugsortedrow = ();
@_ugdone = ();


}


###########################
sub mod_langsupp {
###########################

$modlangfail = "0";

if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat");
		file_lock(FILE);
		@settings = <FILE>;
		unfile_lock(FILE);
		close(FILE);

		for( $i = 0; $i < @settings; $i++ ) {
			$settings[$i] =~ s~[\n\r]~~g;
		}
		
		if ($settings[0] ne $password && $action ne "logout") { error("$err{'002'}"); }
		else {
			$realname = $settings[1];
			$realemail = $settings[2];
			$userlang = $settings[15];
		}
		
}

		if ($userlang eq "") { $userlang = $language; }
						
			 if ($modlangfail ne "1") {
			 @modlanguage = $userlang;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
			 } else {
			 @modlanguage = $language;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
		}

eval {
	require "$languagedir/$modlang.dat";
	
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};

if ($@) {$modlangfail = "1"; mod_langsuppfail();}

}

########################
sub mod_langsuppfail {
########################

eval {
	require "$languagedir/$mod_lang";
	
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};
if ($@) {
print "Content-type: text/html\n\n";
print qq~<h1>Software Error:</h1>
Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
<pre>$@</pre>
<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
~;
	exit;
}

}


if (-e "$scriptdir/user-lib/plugins.pl") {require "$scriptdir/user-lib/plugins.pl"} 




1;
