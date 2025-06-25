###############################################################################
###############################################################################
# theme.pl - Sub-Routines                                                     #
# v0.9.7                                                                      #
#                                                                             #
# Copyright (C) 2001 by carter		                                    #
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
# Last modified: 07/24/02                                                     #
###############################################################################
###############################################################################


#############
sub getvars {
#############
	$titlebg = "#000000";
	$titletext = "#000000";
	$windowbg = "#eeeeee";
	$windowbg2 = "#ffffff";
	$windowbg3 = "#eeeeee";
}


##############
sub menuitem {
##############

my ($url, $title) = @_;
print qq~<tr>
<td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="$pageurl/$cgi\?action=$url" class="menu">$title</a></td>
</tr>
~;

}

###############
sub boxheader {
###############

my ($title) = @_;
print qq~<tr><td>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable"$background>
<tr>
<td>&nbsp;$title</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menubordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="3" width="100%" class="menubackcolor">
~;

}

###############
sub boxfooter {
###############

print qq~</table>
</td>
</tr>
</table>
</td>
</tr>
~;

}

#############
sub getvars {
#############
	$titlebg = "#000000";
	$titletext = "#000000";
	$windowbg = "#eeeeee";
	$windowbg2 = "#ffffff";
	$windowbg3 = "#eeeeee";
}

#####################
sub nav_bar {
#####################

print qq~
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable"$background>
<tr>
<td>&nbsp;$nav{'002'} $navbar</td>
</tr>
</table>
<table bgcolor="$bgcolor" border="0" cellpadding="0" cellspacing="0" width="100%" class="menubordercolor">
<tr>
<td width="100%">
<table bgcolor="$bgcolor" border="0" cellpadding="0" cellspacing="3" width="100%" class="menubackcolor">
<tr>
<td valign="top" width="100%">
~;

}

#####################
sub logo_block {
#####################

print qq~

<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="530">
	<TR>
	  <TD><IMG SRC="$themesurl/$usertheme/images/UL.gif" WIDTH="15" HEIGHT="15"></TD>
	  <TD WIDTH="100%" BACKGROUND="$themesurl/$usertheme/images/U.gif"><IMG SRC="$themesurl/$usertheme/images/U.gif" WIDTH="15" HEIGHT="15"></TD>
	  <TD><IMG SRC="$themesurl/$usertheme/images/UR.gif" WIDTH="15" HEIGHT="15"></TD>
	</TR>
	<TR>
	  <TD BACKGROUND="$themesurl/$usertheme/images/LS.gif"><IMG SRC="$themesurl/$usertheme/images/LS.gif" WIDTH="15" HEIGHT="15"></TD>
	  <TD BGCOLOR="#ffffff"><CENTER>
	      <IMG SRC="$themesurl/$usertheme/images/logo.gif" WIDTH="465" HEIGHT="73">
	    </CENTER>
	  </TD>
	  <TD BACKGROUND="$themesurl/$usertheme/images/RS.gif"><IMG SRC="$themesurl/$usertheme/images/RS.gif" WIDTH="15" HEIGHT="15"></TD>
	</TR>
	<TR>
	  <TD><IMG SRC="$themesurl/$usertheme/images/BLL.gif" WIDTH="15" HEIGHT="25"></TD>
	  <TD BACKGROUND="$themesurl/$usertheme/images/BL.gif"><IMG SRC="$themesurl/$usertheme/images/tail.gif" WIDTH="83" HEIGHT="25"></TD>
	  <TD><IMG SRC="$themesurl/$usertheme/images/BLR.gif" WIDTH="15" HEIGHT="25"></TD>
	</TR>
      </TABLE>
<P>
<BR>

<!--
<table class="myheadertable"> 
          <tr> 
            <td>
<CENTER>
<img src="$themesurl/$usertheme/images/dragon.gif" alt="$pagename">
<img src="$themesurl/$usertheme/images/$langgfx/logo.gif" alt="$pagename">
<img src="$themesurl/$usertheme/images/dragon2.gif" alt="$pagename">

            </td> 
          </tr>
</table>
-->

~;




}


####################
sub checkforbanner {
####################
	
	if ($dispfrad ne "0") { banner_disp(); }

}

####################
sub show_banner {
####################

print qq~ 
 
<div align="center"> 
<table class="pagetable"> 
<tr><td> 
<table class="bannertable"> 
    <tr> 
      <td class="bannertexttitle"> 
<div align="center"> 
~; 

	require "$sourcedir/ads.pl"; 
	OutputJava(); 
 
print qq~ 
 
</div> 
 
 
</td> 
    </tr> 
  </table> 
</td> 
</tr> 
</table> 
</div> 
~; 

}

#######################
sub menu_bar {
#######################

print qq~<table border="0" cellpadding="0" cellspacing="0" width="100%" class="navbar"$background> 
          <tr>  
	    <td width="20%" align="center">&nbsp;<a href="$pageurl/$cgi" class="nav">$nav{'002'}</a>&nbsp;</td> 
            <td width="20%" align="center">&nbsp;<a href="$pageurl/$cgi?action=topics" class="nav">$nav{'004'}</a>&nbsp;</td> 
	    <td width="20%" align="center">&nbsp;<a href="$pageurl/$cgi?action=forum&amp;board=" class="nav">$nav{'003'}</a>&nbsp;</td> 
            <td width="20%" align="center">&nbsp;<a href="$pageurl/$cgi?action=links" class="nav">$nav{'005'}</a>&nbsp;</td> 
			<td width="20%" align="center">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/calendar/index.cgi?vsSD=1" class="nav">Calendar</a>&nbsp;</td> 
          </tr> 
        </table>~;

}

#######################
sub main_menu {
#######################

      boxheader("$nav{'038'}");
      
      menuitem(" ", "$nav{'002'}");
      menuitem("topics", "$nav{'004'}");
      menuitem("forum&board=", "$nav{'003'}");
      menuitem("links", "$nav{'005'}");

 print qq~<tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/calendar/index.cgi?vsSD=1" class="menu">Calendar</a></td>
 </tr>
 <tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/apage/apage.cgi?f=charter.html" class="menu">Charter/Rules</a></td>
 </tr>
 <tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/gallery/index.cgi" class="menu">Gallery</a></td>
 </tr>
 <tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/index.cgi?action=memberlist2" class="menu">Roster</a></td>
 </tr>
 <tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/bank/bank.cgi" class="menu">Guild Bank</a></td>
 </tr>
 <tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/flagging/chart.cgi" class="menu" onclick="NewWindow(this.href,'name','950','600','yes');return false;">Flagging</a></td>
 </tr>
 <tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/showhtml/showhtml.pl?url=www.destinyeq2.com/cgi-bin/mods/chat/index.cgi" class="menu">Chat Room</a></td>
 </tr>
~;


###########################################################################
# Adding a new link Example (possible uses: with new mods)
#
# print qq~<tr>
# <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.mydomain.com/cgi-bin/mods/newmod/newmod.cgi" class="menu">New Mod</a></td>
# </tr>~;
#
###########################################################################                  
     
	 boxfooter();



}

########################
sub search_block {
########################

if ($searchmod eq "2") {


boxheader("$nav{'039'}");
print qq~<tr>
<td align="center">
<table cellspacing="3" cellpadding="0" border="0" width="100%">
<form onSubmit="submitonce(this)" method="POST" action="$pageurl/$cgi\?action=search">
<input type="hidden" name="action" value="search">
<tr>
<td align="center"><input type="text" name="pattern" size="16" class="text"></td>
</tr>
<tr>
<td align="center"><input type="submit" class="searchbutton" value="$btn{'001'}"></td>
</tr>
<tr>
<td align="center"><a href="$pageurl/$cgi?action=search&keyword=AdvancedSearch&amp;page=0&amp;articleson=on&amp;forumson=off&amp;linkson=off&amp;downloadson=off" class="menu">$nav{'154'}</a></td>
</tr>
<input type="hidden" name="articleson" value="on">
<input type="hidden" name="forumson" value="on">
<input type="hidden" name="linkson" value="off">
<input type="hidden" name="downloadson" value="off">
</form>
</table>
</td>
</tr>
~;
	boxfooter();


}

}

#######################
sub search_module {
#######################

print qq~
<tr> 
    <td align="right" valign="bottom" width="50%"><form onSubmit="submitonce(this)" method="POST" action="$pageurl/$cgi\?action=search"><input type="hidden" name="action" value="search"><input type="text" name="pattern" size="16" class="text"><input type="submit" class="searchbutton" value="$btn{'001'}"> 
		<br><a href="$pageurl/$cgi?action=search&keyword=AdvancedSearch&amp;page=0&amp;articleson=on&amp;forumson=off&amp;linkson=off&amp;downloadson=off" class="helps">$nav{'154'}</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		<input type="hidden" name="articleson" value="on">
		<input type="hidden" name="forumson" value="on">
		<input type="hidden" name="linkson" value="off">
		<input type="hidden" name="downloadson" value="off"></form></td> 
</tr>
~;

}

########################
sub mysite_block {
########################

	if ($username eq "$anonuser") {
	login_panel();
	} else {
	member_panel();
	}

}

##########################
sub status_block {
##########################


	boxheader("$nav{'040'}");
	userstatus();
	boxfooter();


}

############################
sub leftblock_block {
############################

	require "$sourcedir/block.pl";
	block_left();

}

#############################
sub poll_block {
#############################

if ($pollmod eq "" || $pollmod eq "1") {


	boxheader("$nav{'041'}");
	require "$sourcedir/poll.pl"; poll();
	boxfooter();

}

}

###########################
sub rightblock_block {
###########################

		require "$sourcedir/block.pl";
		block_right();

}

######################
sub calendar_block {
######################

if ($modulecal == 1) {


boxheader("$msg{'284'}");
require "$sourcedir/showcal.pl";
displayCal();
boxfooter();

}

}

#######################
sub newsletter_block {
#######################

if ($modulenl eq "1") {
if ($modulenlmem eq "1" && $username ne "$anonuser") { 
newsletter_display();
}
if ($modulenlmem eq "0") {
newsletter_display();
}
}
}

########################
sub newsletter_display {
########################


	boxheader("$mnu{'038'}");
	print qq~<form onSubmit="submitonce(this)" action="$pageurl/$cgi\?action=subscribe" method="POST">
<tr>
<td align="center" class="cat">
$msg{'487'}<p class="cat">$msg{'007'}<br><input type="text" name="joinnl" value="" size="12">
</td>
</tr>
<tr>
<td align="center" class="cat">~; print "$msg{'176'}"; print qq~<input type="radio" name="action" value="subscribe" checked></td></tr><tr><td align="center" class="cat">~; print "$msg{'177'}"; print qq~<input type="radio" name="action" value="remove"></td></tr>
<tr><td align="center">
<input type="submit" value="$btn{'016'}" class="newsletterbutton"></td></tr>
</form>
</td>
</tr>
~;
	boxfooter();
}

########################
sub info_block {
########################

if ($infoblockmod eq "1") {


		if ($username ne "$anonuser") {

		open(FILE, "$memberdir/$username.pref") || error("$err{'010'}");
		file_lock(FILE);
		chomp(@preferences = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		if ($preferences[1] == 1 || $preferences[1] eq "" ) {
	
	boxheader("$msg{'486'}");
	print qq~<tr>
<td align="center" class="cat"><a href="$link1" target="_blank"><img alt="" border="0" src="$image1"></a></td>
</tr>
<tr>
<td align="center" class="cat"><a href="$link2" target="_blank"><img alt="" border="0" src="$image2"></a></td>
</tr>
<tr>
<td align="center" class="cat"><a href="$link3" target="_blank"><img alt="" border="0" src="$image3"></a></td>
</tr>
~;
	boxfooter();

}
} else {
	boxheader("$msg{'486'}");
	print qq~<tr>
<td align="center" class="cat"><a href="$link1" target="_blank"><img alt="" border="0" src="$image1"></a></td>
</tr>
<tr>
<td align="center" class="cat"><a href="$link2" target="_blank"><img alt="" border="0" src="$image2"></a></td>
</tr>
<tr>
<td align="center" class="cat"><a href="$link3" target="_blank"><img alt="" border="0" src="$image3"></a></td>
</tr>
~;
	boxfooter();
}
}

	if ($infoblockmod eq "2") {
	

boxheader("$msg{'486'}");
	print qq~<tr>
<td align="center" class="cat"><a href="$link1" target="_blank"><img alt="" border="0" src="$image1"></a></td>
</tr>
<tr>
<td align="center" class="cat"><a href="$link2" target="_blank"><img alt="" border="0" src="$image2"></a></td>
</tr>
<tr>
<td align="center" class="cat"><a href="$link3" target="_blank"><img alt="" border="0" src="$image3"></a></td>
</tr>
~;
	boxfooter();
}
}

###########################
sub mycontent_block {
###########################

	if ($showcon eq "1") {

print qq~ 
 
<div align="center"> 
<table class="pagetable" width="100%"> 
<tr> 
<td>
 
<table class="mycontenttable" width="100%"> 
    <tr> 
      <td> 
<div align="center"> 
~; 
      boxheader("$nav{'093'}" ); 
      latestforumposts(); 
      if (@myforumnum) { 
            for ($myflcounter = 0; $myflcounter < @myforumnum && $myflcounter < 5; $myflcounter++) { 
                  print qq~<tr> 
<td><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;$myforumdata{$myforumnum[$myflcounter]}</td> 
</tr> 
~; 
            } 
      } 
      else { 
            print qq~<tr> 
<td>$msg{'179'}</td> 
</tr> 
~; 
      } 
      boxfooter(); 
 
      print qq~ 
 
</div>     
  </td> 
    </tr> 
  </table>
</td> 
</tr> 
</table> 
~;
	
}

}

######################
sub mycontent_block2 {
######################

	if ($showcon2 eq "1") {

print qq~ 
 
<div align="center"> 
<table class="pagetable" width="100%"> 
<tr> 
<td>
 
<table class="mycontenttable" width="100%"> 
    <tr> 
      <td> 
<div align="center"> 
~; 
      boxheader("$nav{'093'}" ); 
      latestforumposts(); 
      if (@myforumnum) { 
            for ($myflcounter = 0; $myflcounter < @myforumnum && $myflcounter < 5; $myflcounter++) { 
                  print qq~<tr> 
<td><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;$myforumdata{$myforumnum[$myflcounter]}</td> 
</tr> 
~; 
            } 
      } 
      else { 
            print qq~<tr> 
<td>$msg{'179'}</td> 
</tr> 
~; 
      } 
      boxfooter(); 
 
      print qq~ 
 
</div>     
  </td> 
    </tr> 
  </table>
</td> 
</tr> 
</table> 
~;
	
}

}

###########################
sub about_bar {
###########################

print qq~<table class="helpsnavtable">
    <tr>
      <td>
~; 

	open(DATA,"$logdir/stats.dat") || error("$err{'001'} $logdir/stats.dat");
	@lines = <DATA>;
	close(DATA);
	$total = @lines;

print qq~
<CENTER>We have had $total Visitor's to the site.
</td></tr>
	</table>~;
	
}

############################
sub wepapp_bar {
############################

print qq~<table border="0" cellpadding="0" cellspacing="0" align="center">
<tr>
<td><br></td>
</tr>
<tr>
<td align="center" class="webapptext">
$msg{'399'}<a href="http://www.web-app.org/cgi-bin/index.cgi" target="_blank" class="webapplink">WebAPP v$scriptver</a>$msg{'400'}<br>
$msg{'401'}
<br><br>
<br>
</td>
</tr>
</table>~;

}

#############################
sub login_panel {
#############################

getcgi();

$returnpage1 = $action;
$returnpage2 = $currentboard;
$returnpage3 = $cat;
$returnpage4 = $viewcat;
$returnpage5 = $num;
$returnpage6 = $id;


boxheader("$nav{'012'}");
print qq~
	 
	<form onSubmit="submitonce(this)" method="post" action="$pageurl/$cgi?action=login2">
	<input type="hidden" name="returnpage1" value="$returnpage1">
	<input type="hidden" name="returnpage2" value="$returnpage2">
	<input type="hidden" name="returnpage3" value="$returnpage3">
	<input type="hidden" name="returnpage4" value="$returnpage4">
	<input type="hidden" name="returnpage5" value="$returnpage5">
	<input type="hidden" name="returnpage6" value="$returnpage6">
	<tr>
	<td align="center" class="whocat">$msg{'006'}<br><input type="text" name="username" size="8"></td> 
	</tr>
	<tr>  
	<td align="center" class="whocat">$msg{'009'}<br><input type="password" name="passwrd" size="8"></td> 
	</tr>
	<tr>
	<td align="center" class="whocat"><input type="checkbox" name="rememberme" checked>&nbsp;$msg{'410'}</td> 
	</tr> 
	<tr> 
	<td colspan="2" align="center"><input type="submit" class="button" value="$btn{'017'}"></td> 
	</tr>
	<tr> 
	<td colspan="2" align="center" class="whocat"><a href="$pageurl/$cgi?action=reminder">$nav{'014'}</a></td> 
	</tr> 
	<tr> 
	<td colspan="2" align="center" class="whocat">$msg{'340'}<a href="$pageurl/$cgi\?action=register" class="menu"><u>$msg{'341'}</u></a>.</td> 
	</tr>
	
	</form> 
	~;
	
boxfooter();


}

######################
sub member_panel {
######################


boxheader("$pagename");

	menuitem("editprofile&amp;username=$username", "$nav{'016'}");

 print qq~<tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="http://www.destinyeq2.com/cgi-bin/mods/office/journal.cgi" class="menu">Journal</a></td>
 </tr>~;
		
	if ($hidememlist ne "1") {menuitem("memberlist", "$nav{'019'}");}
		
	if ($username eq "admin") { 
	menuitem("admin\&amp\;op=siteadmin", "$nav{'042'}");
	#&display_aprovals;

	menuitem("postnews", "Write News");	

	&show_stats;
	

	if ($hidememlist eq "1") {menuitem("memberlist", "$nav{'019'}");} 
	}

	if ($username ne "$anonuser" && $username ne "admin") {
	
	open(FILE, "$memberdir/$username.dat") || error("$err{'010'}"); 
	file_lock(FILE); 
	chomp(@memsettings = <FILE>); 
	unfile_lock(FILE); 
	close(FILE); 

	if ($memsettings[7] eq "$root") { 
		menuitem("adminlite\&amp\;op=siteadmin", "$nav{'042'}");
		#&display_aprovals; 

		menuitem("postnews", "Write News");

		&show_stats;
	}

}

 	menuitem("logout", "$nav{'034'}");

print "BLABLABLA";

	boxfooter();



	
}

###############
sub display_aprovals {
###############

$memcount = 0;

open(data, "$memberdir/forapproval.dat");
@data=<data>;
close(data);


foreach $line (@data){

$memcount = $memcount + 1;

}

close(data);

if ($memcount ne 0) {

print qq~


$memcount Aprovals



~;

}

}

###############
sub newsheader {
###############

print qq~
</td>
</tr>
</table>
</td>
</tr>
</table>
<br>
~;

}

#################
sub newstop {
#################

$post = qq~
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menutable"$background>
<tr>
<td class="newstexttitle">&nbsp;$subject</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="menubordercolor">
<tr>
<td width="100%">
<table border="0" cellpadding="0" cellspacing="3" width="100%" class="menubackcolor">
<tr>
<td valign="top" width="100%">
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td class="newssubtitle">$curcatname: $postdate $msg{'042'} <a href="$cgi?action=anonemail&sendto=$poster" class="smallnewslink">$nick</a>
</td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top" class="newstextnormal">
~;

}

##################
sub newsshort {
##################

$post = qq~$post<img src="$imagesurl/topics/$curcat.gif" border="0" align="right" vspace="5" alt="$curcatname">
$message
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
</td>
</tr>
<tr>
<td width="100%">
<table class="newsfootertable">
<tr>
<td align="left" valign="middle">&nbsp;
<a href="$cgi?action=printtopic&amp;id=$id&amp;curcatname=$curcatname&amp;img=$curcat"><img src="$imagesurl/print.gif" border="0" alt="$msg{'106'} - $subject" align="absmiddle"></a>&nbsp;&nbsp;<a href="$cgi?action=emailtopic&amp;id=$id&amp;curcatname=$curcatname"><img src="$imagesurl/friend.gif" border="0" alt="$msg{'055'}" align="absmiddle"></a>&nbsp;&nbsp;$readcount</td>
<td align="right" valign="middle" class="newsfootertext"> [ <a href="$cgi?action=viewnews&amp;id=$id#topcomment" class="newslink">$commentscnt</a> ]&nbsp;</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<br>
~;

}

##################
sub newslong {
##################

$post = qq~$post<img src="$imagesurl/topics/$curcat.gif" border="0" align="right" vspace="5" alt="$curcatname">
$tmpmessage ...
</tr>
<tr>
<td>&nbsp;</td>
</tr>
</table>
</td>
</tr>
<tr>
<td width="100%">
<table class="newsfootertable">
<tr>
<td align="left" valign="middle">&nbsp;
<a href="$cgi?action=printtopic&amp;id=$id&amp;curcatname=$curcatname&amp;img=$curcat"><img src="$imagesurl/print.gif" border="0" alt="$msg{'106'} - $subject" align="absmiddle"></a>&nbsp;&nbsp;<a href="$cgi?action=emailtopic&amp;id=$id&amp;curcatname=$curcatname"><img src="$imagesurl/friend.gif" border="0" alt="$msg{'055'}" align="absmiddle"></a>&nbsp;&nbsp;$readcount</td>
<td align="right" valign="middle" class="newsfootertext"> [ <b><a href="$cgi?action=viewnews&amp;id=$id" class="newslink">$nav{'025'}</a></b> ]&nbsp;&nbsp;[ <a href="$cgi?action=viewnews&amp;id=$id#topcomment" class="newslink">$commentscnt</a> ]&nbsp;</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<br>
~;

}

########################
sub show_stats {
########################

 print qq~<tr>
 <td class="cat"><img src="$themesurl/$usertheme/images/dot.gif">&nbsp;<a href="$pageurl/$cgi?action=stats" class="menu">$nav{'006'}</a></td>
 </tr>~;

}

######################
sub banner_disp {
######################

if ($dispfrad eq "1" && $username ne "$anonuser") {

	 						open(FILE, "$memberdir/$username.pref") || error("$err{'010'}");
							file_lock(FILE);
							chomp(@preferences = <FILE>);
							unfile_lock(FILE);
							close(FILE);

		if ($preferences[2] eq "1") {
		show_banner(); }
 else { }
}

if ($dispfrad eq "2" || $username eq "$anonuser") {
 show_banner(); }

}

######################
sub broadcastmessage {
######################

if ($username ne "$anonuser") { 
 
# This is to broadcast an alert message to everyone online at that time 
 
		open(FILE, "$datadir/broadcast.txt") || error("$err{'010'}"); 
		file_lock(FILE); 
		chomp(@preferences = <FILE>); 
		unfile_lock(FILE);
		close(FILE); 
 
 
		if ($preferences[0] eq "on") { 
		 
		print qq~ 
 
<script language="JavaScript1.2"> 
 
 
var ns4=document.layers 
var ie4=document.all 
var ns6=document.getElementById&&!document.all 
 
 
var dragswitch=0 
var nsx 
var nsy 
var nstemp 
 
function drag_dropns(name){ 
if (!ns4) 
return 
temp=eval(name) 
temp.captureEvents(Event.MOUSEDOWN | Event.MOUSEUP) 
temp.onmousedown=gons 
temp.onmousemove=dragns 
temp.onmouseup=stopns 
} 
 
function gons(e){ 
temp.captureEvents(Event.MOUSEMOVE) 
nsx=e.x 
nsy=e.y 
} 
function dragns(e){ 
if (dragswitch==1){ 
temp.moveBy(e.x-nsx,e.y-nsy) 
return false 
} 
} 
 
function stopns(){ 
temp.releaseEvents(Event.MOUSEMOVE) 
} 
 
 
 
function drag_drop(e){ 
if (ie4&&dragapproved){ 
crossobj.style.left=tempx+event.clientX-offsetx 
crossobj.style.top=tempy+event.clientY-offsety 
return false 
} 
else if (ns6&&dragapproved){ 
crossobj.style.left=tempx+e.clientX-offsetx 
crossobj.style.top=tempy+e.clientY-offsety 
return false 
} 
} 
 
function initializedrag(e){ 
crossobj=ns6? document.getElementById("showimage") : document.all.showimage 
 
var firedobj=ns6? e.target : event.srcElement 
var topelement=ns6? "HTML" : "BODY" 
 
while (firedobj.tagName!=topelement&&firedobj.id!="dragbar"){ 
firedobj=ns6? firedobj.parentNode : firedobj.parentElement 
} 
 
if (firedobj.id=="dragbar"){ 
offsetx=ie4? event.clientX : e.clientX 
offsety=ie4? event.clientY : e.clientY 
 
tempx=parseInt(crossobj.style.left) 
tempy=parseInt(crossobj.style.top) 
 
dragapproved=true 
document.onmousemove=drag_drop 
} 
} 
document.onmousedown=initializedrag 
document.onmouseup=new Function("dragapproved=false") 
 
 
function hidebox(){ 
if (ie4||ns6) 
crossobj.style.visibility="hidden" 
else if (ns4) 
document.showimage.visibility="hide" 
} 
 
</script> 
 
<div id="showimage" style="position:absolute;width:250px;left:250;top:250"> 
 
<table border="0" width="250" bgcolor="$bmheadercolor" cellspacing="2" cellpadding="0"> 
  <tr> 
    <td width="100%"><table border="0" width="100%" cellspacing="0" cellpadding="0" 
    height="36"> 
      <tr> 
        <td id="dragbar" style="cursor:hand" width="100%"><ilayer width="100%" onSelectStart="return false"><layer width="100%" onMouseover="dragswitch=1;if (ns4) drag_dropns(showimage)" onMouseout="dragswitch=0"><font face="Verdana" 
        color="$bmbgcolor"><strong><small>Admin Broadcast Message</small></strong></font></layer></ilayer></td> 
        <td style="cursor:hand"><a href="#" onClick="hidebox();return false"><img src="$themesurl/standard/images/close.gif" width="16" 
        height="14" border=0></a></td> 
      </tr> 
      <tr> 
        <td width="100%" bgcolor="$bmbgcolor" style="padding:4px" colspan="2"> 
 
<!-- PUT YOUR CONTENT BETWEEN HERE ----> 
 
$preferences[1]  
 
<!-- END YOUR CONTENT HERE-----> 
 
</td> 
      </tr> 
    </table> 
    </td> 
  </tr> 
</table> 
</div> 
 
 
~; 
 
		} 
} 
 
# End broadcast java alert message 

}


1; # return true
