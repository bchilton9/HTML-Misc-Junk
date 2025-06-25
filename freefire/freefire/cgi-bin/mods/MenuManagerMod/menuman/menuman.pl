#---------------------------------------------------------
#  WebApp Menu Manager Mod
#
#  Written by Ted Loomos
#  Get the latest updates from www.devdesk.com
#
#  Revision History:
#  2002-08-31  Script Created
#  2002-09-02  Fixed bug that caused problems with the "Edit Profile" function
#  2002-09-03  Allow target & icon to be specified
#  2002-09-04  Allow any $ variable to be used in title, url or icon
#  2002-09-12  Added personal menu support
#---------------------------------------------------------
sub mm_showMenu {
	my ($menu) = @_;
	my @memsettings;

	require "$scriptdir/mods/menuman/config.pl";

	open (MENUFILE,"<$mm_dataDir/$menu.dat") || error("$err{'001'} $mm_dataDir/$menu.dat");
	@menuitems=<MENUFILE>;
	close (MENUFILE);

	if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
		file_lock(FILE);
		chomp(@memsettings = <FILE>);
		unfile_lock(FILE);
		close(FILE);
	}

	MENUITEM: foreach $entry (@menuitems) {
		chomp($entry);

		($id, $url, $title, $access, $target, $icon) = split(/\|/,$entry);

		$title = eval "\"$title\"";
		$url   = eval "\"$url\"";
		$icon  = eval "\"$icon\"";

		if ($menu ne $username) {
			$access = ",$access,";

			if 	  ($access =~ ",-public-,") {}
			elsif ($access =~ ",-member-," && $username ne $anonuser) {}
			elsif ($access =~ ",-admin-," && $settings[7] eq "Administrator") {}
			elsif ($access =~ ",-guest-," && $username eq $anonuser) {}
			elsif ($access =~ ",$memsettings[14],") {}
			else  {next MENUITEM}
		}

		menuitem($url, $title, $target, $icon);
	}

}

sub mm_showMenuBar{
	my ($menu) = @_;
	my @memsettings;

	require "$scriptdir/mods/menuman/config.pl";

	open (MENUFILE,"<$mm_dataDir/$menu.dat") || error("$err{'001'} $mm_dataDir/$menu.dat");
	@menuitems=<MENUFILE>;
	close (MENUFILE);

	if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
		file_lock(FILE);
		chomp(@memsettings = <FILE>);
		unfile_lock(FILE);
		close(FILE);
	}

	print "<table border='0' cellpadding='0' cellspacing='0' width='100%' class='navbar'$background><tr>";

	MENUITEM: foreach $entry (@menuitems) {
		chomp($entry);

		($id, $url, $title, $access, $target, $nothing) = split(/\|/,$entry);

		$title = eval "\"$title\"";
		$url   = eval "\"$url\"";

		$access = ",$access,";

		if 	  ($access =~ ",-public-,") {}
		elsif ($access =~ ",-member-," && $username ne $anonuser) {}
		elsif ($access =~ ",-admin-," && $username eq "admin") {}
		elsif ($access =~ ",-guest-," && $username eq $anonuser) {}
		elsif ($access =~ ",$memsettings[14],") {}
		else  {next MENUITEM}




if ($url =~ m/^http:\/\//i) {

print qq~
<td align='center'>&nbsp;<a href='$url' class='nav' target='$target'>$title</a>&nbsp;</td>
~;

} 
else {
			
print "<td align='center'>&nbsp;<a href='$pageurl/$cgi\?action=$url' class='nav' target='$target'>$title</a>&nbsp;</td>";
		
}



	}

	print "</tr></table>";

}


1;