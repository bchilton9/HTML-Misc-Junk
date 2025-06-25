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
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD><IMG src="$themesurl/$usertheme/pictures/group1-1.gif" width="21" height="26" border="0"></TD>
      <TD><IMG src="$themesurl/$usertheme/pictures/group1-2.gif" width="49" height="26" border="0"></TD>
      <TD width="100%" BACKGROUND="$themesurl/$usertheme/pictures/group1-3.gif"><CENTER>
&nbsp;
	  </CENTER></TD>
      <TD><IMG src="$themesurl/$usertheme/pictures/group1-4.gif" width="38" height="26" border="0"></TD>
      <TD><IMG src="$themesurl/$usertheme/pictures/group1-5.gif" width="22" height="26" border="0"></TD>
    </TR>
    <TR>
      <TD VALIGN="Top" BACKGROUND="$themesurl/$usertheme/pictures/group3-1.gif"><IMG src="$themesurl/$usertheme/pictures/group2-1.gif"
	    width="21" height="51" border="0"></TD>
      <TD ROWSPAN="3" COLSPAN="3" BGCOLOR="#000000" BACKGROUND="$themesurl/$usertheme/pictures/group2-2.gif" VALIGN="Top">
	  <CENTER><font color=white>&nbsp;Buddy List</FONT></CENTER><HR>
	  <table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="3" width="100%" >
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
	</TD>
      <TD VALIGN="Top" BACKGROUND="$themesurl/$usertheme/pictures/group3-5.gif"><IMG src="$themesurl/$usertheme/pictures/group2-5.gif"
	    width="22" height="51" border="0"></TD>
    </TR>
    <TR>
      <TD BACKGROUND="$themesurl/$usertheme/pictures/group3-1.gif"><IMG src="$themesurl/$usertheme/pictures/group3-1.gif" width="21"
	    height="84" border="0"></TD>
      <TD BACKGROUND="$themesurl/$usertheme/pictures/group3-5.gif"><IMG src="$themesurl/$usertheme/pictures/group3-5.gif" width="22"
	    height="84" border="0"></TD>
    </TR>
    <TR>
      <TD VALIGN="Bottom" BACKGROUND="$themesurl/$usertheme/pictures/group3-1.gif"><IMG src="$themesurl/$usertheme/pictures/group4-1.gif"
	    width="21" height="30" border="0"></TD>
      <TD VALIGN="Bottom" BACKGROUND="$themesurl/$usertheme/pictures/group3-5.gif"><IMG src="$themesurl/$usertheme/pictures/group4-5.gif"
	    width="22" height="30" border="0"></TD>
    </TR>
    <TR>
      <TD><IMG src="$themesurl/$usertheme/pictures/group5-1.gif" width="21" height="12" border="0"></TD>
      <TD><IMG src="$themesurl/$usertheme/pictures/group5-2.gif" width="49" height="12" border="0"></TD>
      <TD BACKGROUND="$themesurl/$usertheme/pictures/group5-3.gif"><IMG src="$themesurl/$usertheme/pictures/group5-3.gif" width="26"
	    height="12" border="0"></TD>
      <TD><IMG src="$themesurl/$usertheme/pictures/group5-4.gif" width="38" height="12" border="0"></TD>
      <TD><IMG src="$themesurl/$usertheme/pictures/group5-5.gif" width="22" height="12" border="0"></TD>
    </TR>
  </TABLE>
</CENTER>
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
