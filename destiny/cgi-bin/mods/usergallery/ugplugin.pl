###############################################################################
###############################################################################
# ugplugin.pl for User Gallery v1.1                                           #
# Copyright (C) 2002 by Floyd (webmaster@diminishedresponsibility.co.uk)      #
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
# Last Updated: 10/19/02																											#
###############################################################################
###############################################################################

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
elsif ($ugplugin eq "2") { admin_monitor(); }
elsif ($ugplugin eq "3") { administrator_monitor(); }
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
	lock(FILE);
	chomp(@pcats = <FILE>);
	unlock(FILE);
	close(FILE);
	
	foreach $curalb (@pcats) {
	$curalb =~ s/[\n\r]//g;
	@curitem = split (/\|/, $curalb);
			open(FILE, "$usergallerydb/$curitem[0].cat");
			lock(FILE);
			chomp(@palbums = <FILE>);
			unlock(FILE);
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
	lock(FILE);
	chomp(@pcats = <FILE>);
	unlock(FILE);
	close(FILE);
	
	foreach $curalb (@pcats) {
	$curalb =~ s/[\n\r]//g;
	@curitem = split (/\|/, $curalb);
			open(FILE, "$usergallerydb/$curitem[0].cat");
			lock(FILE);
			chomp(@palbums = <FILE>);
			unlock(FILE);
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

###################
sub admin_monitor {
###################

if ($username eq "admin") {
boxheader("$ugadmin{'035'}");

	open(FILE2, "<$scriptdir/mods/usergallery/db/newugs.dat"); 
	lock(FILE2); 
	chomp(@pendingugpics = <FILE2>); 
	unlock(FILE2); 
	close(FILE2);
	
	$newugpics = 0;
	foreach $line (@pendingugpics) {
	$line =~ s/[\n\r]//g;
	$newugpics++; 
	}

if ($newugpics eq "0") {
print qq~<tr><td align="center" class="whocat">$ugadmin{'036'}</td></tr>~;
} else {
print qq~<tr><td align="center" class="whocat"><a href="$pageurl/mods/usergallery/admin/admin.cgi?op=verifypictures" class="whomenu">$newugpics $ugadmin{'037'}</a></td></tr>~;
}

boxfooter();
}

}

###################
sub administrator_monitor {
###################

if ($settings[7] eq "$root") {
boxheader("$ugadmin{'035'}");

	open(FILE2, "<$scriptdir/mods/usergallery/db/newugs.dat"); 
	lock(FILE2); 
	chomp(@pendingugpics = <FILE2>); 
	unlock(FILE2); 
	close(FILE2);
	
	$newugpics = 0;
	foreach $line (@pendingugpics) {
	$line =~ s/[\n\r]//g;
	$newugpics++; 
	}

if ($newugpics eq "0") {
print qq~<tr><td align="center" class="whocat">$ugadmin{'036'}</td></tr>~;
} else {
print qq~<tr><td align="center" class="whocat"><a href="$pageurl/mods/usergallery/admin/admin.cgi?op=verifypictures" class="whomenu">$newugpics $ugadmin{'037'}</a></td></tr>~;
}

boxfooter();
}

}

###################
sub ugplugin1 {
###################

if ($info{'action'} eq "createalbum") {createalbum();}
elsif ($info{'action'} eq "createalbum2") {createalbum2();}
elsif ($info{'action'} eq "openalbum") {openalbum();}
elsif ($info{'action'} eq "showpicture") {showpicture();}
elsif ($info{'action'} eq "addpicture") {addpicture();}
elsif ($info{'action'} eq "addpicture2") {addpicture2();}
elsif ($info{'action'} eq "editpicture") {editpicture();}
elsif ($info{'action'} eq "editpicture2") {editpicture2();}
elsif ($info{'action'} eq "removepicture") {removepicture();}
elsif ($info{'action'} eq "movepicture2") {movepicture2();}
elsif ($info{'action'} eq "movepicture") {movepicture();}
elsif ($info{'action'} eq "removepicture2") {removepicture2();}
elsif ($info{'action'} eq "editalbum") {editalbum();}
elsif ($info{'action'} eq "editalbum2") {editalbum2();}
elsif ($info{'action'} eq "removealbum") {removealbum();}
elsif ($info{'action'} eq "removealbum2") {removealbum2();}
else {doorway();}

}

###################
sub ugplugin2 {
###################

# not used! #

}

###################
sub ugadminplugin1 {
###################

if ($op eq "verifypictures") { verifypictures(); }
elsif ($op eq "verifypictures2") { verifypictures2(); }
elsif ($op eq "setup") { setup(); }
elsif ($op eq "setup2") { setup2(); }
elsif ($op eq "viewfailed") { view_failed(); }
elsif ($op eq "resetfailed") { reset_failed(); }
else { doorway(); }

}

###################
sub ugadminplugin2 {
###################

# not used! #

}

###########################
sub mod_langsupp {
###########################

$modlangfail = "0";

if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat");
		lock(FILE);
		@settings = <FILE>;
		unlock(FILE);
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

1;
