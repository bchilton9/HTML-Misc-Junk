#---------------------------------------------------------
#  Subroutine:   menuitem
#  Written By:   Ted Loomos
#  Description:  Modified for Menu Manager Mod
#                Get the latest updates from www.devdesk.com
#
#  Revision History:
#  2002-08-31  Function Created
#  2002-09-03  Allow target & icon to be specified
#---------------------------------------------------------
##############
sub menuitem {
##############

my ($url, $title, $target, $icon) = @_;



if ($target eq "frameless") {

		print qq~<tr>
		<td class="cat"><img src="$icon">&nbsp;<a href="$url" class="menu" onclick="NewWindow(this.href,'name','1055','600','yes');return false;">$title</a></td>
		</tr>
		~;

}
elsif ($target eq "chat") {

		print qq~<tr>
		<td class="cat"><img src="$icon">&nbsp;<a href="$url" class="menu" onclick="NewWindow(this.href,'name','350','100','no');return false;">$title</a></td>
		</tr>
		~;

}
else {

	if ($url =~ m/^http:\/\//i) {

		print qq~<tr>
		<td class="cat"><img src="$icon">&nbsp;<a href="$url" class="menu" target="$target">$title</a></td>
		</tr>
		~;
	} else {
		print qq~<tr>
		<td class="cat"><img src="$icon">&nbsp;<a href="$pageurl/$cgi\?action=$url" class="menu" target="$target">$title</a></td>
		</tr>
		~;
	}
}

}

#---------------------------------------------------------
#  Subroutine:   main_menu
#  Written By:   Ted Loomos
#  Description:  Modified for Menu Manager Mod
#                Get the latest updates from www.devdesk.com
#
#  Revision History:
#  2002-08-31  Function Created
#  2002-09-12  Added personal menu support
#---------------------------------------------------------
#######################
sub main_menu {
#######################

	boxheader("$nav{'038'}");

	require "$scriptdir/mods/menuman/menuman.pl";
	mm_showMenu("mainmenu");

	boxfooter();

	if (-e "$mm_dataDir/$username.dat") {
		boxheader("My Menu");

		mm_showMenu("$username");

		boxfooter();
	}

}


#---------------------------------------------------------
#  Subroutine:   member_panel
#  Written By:   Ted Loomos
#  Description:  Modified for Menu Manager Mod
#                Get the latest updates from www.devdesk.com
#
#  Revision History:
#  2002-08-31  Function Created
#---------------------------------------------------------
######################
sub member_panel {
######################


	boxheader("$pagename");

	require "$scriptdir/mods/menuman/menuman.pl";
	mm_showMenu("memberpanel");

	boxfooter();

print qq~
<TR><TD>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable">
<tr>
<td>&nbsp;Buddy List!</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menubordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="3" width="100%" class="menubackcolor">
<tr><td>

<center><table colspacing=0 colpadding=0>
~;

require "$scriptdir/user-lib/buddylist.pl";
blist();

print qq~
</table></center>
<HR>
<div ALIGN=right>
<a href="$pageurl/$cgi?action=memberlist"><img src="$imagesurl/buddy/guest.gif" border=0 alt="$bud{'009'}"></a>
&nbsp;
<a href="$pageurl/$cgi?action=blistedit"><img src="$imagesurl/forum/modify.gif" alt="$bud{'006'}" border=0></a>

</td></tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
~;

}

#---------------------------------------------------------
#  Subroutine:   member_panel
#  Written By:   Ted Loomos
#  Description:  Modified for Menu Manager Mod
#                Get the latest updates from www.devdesk.com
#
#  Revision History:
#  2002-09-14  Function Created
#---------------------------------------------------------
######################
sub menu_bar {
#######################

	require "$scriptdir/mods/menuman/menuman.pl";
	mm_showMenuBar("menubar");

}


1; # return true
