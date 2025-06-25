##########################
sub imxversion              {
##########################

}

##################
# admin subs     #
##################

####################
sub imxsmilie {
####################

print qq~
<table>
<tr>
<td align=center valign="middle">
<a href="javascript:addCode('[imxconfused]')"><img src="$imagesurl/im/smilies/confused.gif" border="0"></a>
<a href="javascript:addCode('[imxcool]')"><img src="$imagesurl/im/smilies/cool.gif" border="0"></a>
<a href="javascript:addCode('[imxlove]')"><img src="$imagesurl/im/smilies/iheartu.gif" border="0"></a>
<a href="javascript:addCode('[imxpray]')"><img src="$imagesurl/im/smilies/pray.gif" border="0"></a>
<a href="javascript:addCode('[imxhuh]')"><img src="$imagesurl/im/smilies/huh.gif" border="0"></a>
<a href="javascript:addCode('[imxgrin]')"><img src="$imagesurl/im/smilies/grin.gif" border="0"></a>
<a href="javascript:addCode('[imxlol]')"><img src="$imagesurl/im/smilies/haha.gif" border="0"></a>
<a href="javascript:addCode('[imxclap]')"><img src="$imagesurl/im/smilies/applaud.gif" border="0"></a>
<a href="javascript:addCode('[imxcry]')"><img src="$imagesurl/im/smilies/cry.gif" border="0"></a>
<a href="javascript:addCode('[imxsmile]')"><img src="$imagesurl/im/smilies/smile.gif" border="0"></a>
<a href="javascript:addCode('[imxwink]')"><img src="$imagesurl/im/smilies/wink.gif" border="0"></a>
<a href="javascript:addCode('[imxangel]')"><img src="$imagesurl/im/smilies/angel.gif" border="0"></a>
<a href="javascript:addCode('[imxkiss]')"><img src="$imagesurl/im/smilies/kiss.gif" border="0"></a>
<a href="javascript:addCode('[imxsad]')"><img src="$imagesurl/im/smilies/sad.gif" border="0"></a>
<a href="javascript:addCode('[imxzzz]')"><img src="$imagesurl/im/smilies/zzz.gif" border="0"></a>
<a href="javascript:addCode('[imxshy]')"><img src="$imagesurl/im/smilies/shy.gif" border="0"></a>
</td>
</tr></table>
~;
}

#############
sub mytopbar5  {
#############

open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) { ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $dummy, $theme, $themecolor) = split(/\|/, $curentry);}

if ($theme eq ""){$preftheme = "original";}else{$preftheme = "$theme";}
if ($themecolor eq ""){$prefthemecolor = "#CEE3F8";}else{$prefthemecolor = "#$themecolor";}
print qq~



<!-- topbar -->
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=80% valign=top><img src="$imagesurl/im/folders/1folder.gif" atl="$mytopbar"><b>$mytopbar</b></td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$cgi?action=folder>$imx{'051'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=imsend>$imx{'046'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=im>$imx{'001'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
</tr>
<tr bgcolor="$prefthemecolor"><td height=4 colspan=4></td></tr>
</table>
<!-- topbar end -->


~;

}
#############
sub mymaintopbar  {
#############


open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) { ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $theme, $themecolor) = split(/\|/, $curentry);}

if ($theme eq ""){$preftheme = "original";}else{$preftheme = "$theme";}
if ($themecolor eq ""){$prefthemecolor = "#CEE3F8";}else{$prefthemecolor = "#$themecolor";}
print qq~

<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=80%><img src="$imagesurl/im/folders/1folder.gif" alt="$mytopbar"> $mytopbar</td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=folder>$imx{'051'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>

</td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=contacts>$imx{'045'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=imsend>$imx{'046'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
</tr>
<tr bgcolor=$prefthemecolor><td height=4 colspan=4></td></tr>
</table>
<!-- topbar end -->


~;
}

#############
sub mymaintopbar2  {
#############


open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) { ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $theme, $themecolor) = split(/\|/, $curentry);}

if ($theme eq ""){$preftheme = "original";}else{$preftheme = "$theme";}
if ($themecolor eq ""){$prefthemecolor = "#CEE3F8";}else{$prefthemecolor = "#$themecolor";}
print qq~

<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=80%><img src="$imagesurl/im/folders/globe.gif" alt="$mytopbar"> $mytopbar</td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=#folder>$imx{'051'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>

</td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=contacts>$imx{'045'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=imsend>$imx{'046'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
</tr>
<tr bgcolor=$prefthemecolor><td height=4 colspan=4></td></tr>
</table>
<!-- topbar end -->


~;
}

#############
sub mytopbar4  {
#############

open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) { ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $dummy, $theme, $themecolor) = split(/\|/, $curentry);}

if ($theme eq ""){$preftheme = "original";}else{$preftheme = "$theme";}
if ($themecolor eq ""){$prefthemecolor = "#CEE3F8";}else{$prefthemecolor = "#$themecolor";}
print qq~



<!-- topbar -->
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=80% valign=top><img src="$imagesurl/im/folders/globe.gif" atl="$mytopbar" height=35><b>$mytopbar</b></td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$cgi?action=folder>$imx{'051'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=imsend>$imx{'046'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=im>$imx{'001'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
</tr>
<tr bgcolor="$prefthemecolor"><td height=4 colspan=4></td></tr>
</table>
<!-- topbar end -->


~;

}



#############
sub mytopbar3  {
#############

open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) { ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $dummy, $theme, $themecolor) = split(/\|/, $curentry);}

if ($theme eq ""){$preftheme = "original";}else{$preftheme = "$theme";}
if ($themecolor eq ""){$prefthemecolor = "#CEE3F8";}else{$prefthemecolor = "#$themecolor";}

print qq~
<!-- topbar -->
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=80% valign=bottom><img src="$imagesurl/im/folders/text-doc.gif" alt="$mytopbar"> <b>$mytopbar</b></td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$cgi?action=folder>$imx{'051'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=contacts>$imx{'045'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=im>$imx{'001'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
</tr>
<tr bgcolor="$prefthemecolor"><td height=4 colspan=4></td></tr>
</table>
<!-- topbar end -->


~;

}


#############
sub mytopbar2  {
#############

open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) { ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $dummy, $theme, $themecolor) = split(/\|/, $curentry);}

if ($theme eq ""){$preftheme = "original";}else{$preftheme = "$theme";}
if ($themecolor eq ""){$prefthemecolor = "#CEE3F8";}else{$prefthemecolor = "#$themecolor";}
print qq~

<!-- topbar -->
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=80% valign=bottom><img src="$imagesurl/im/folders/users-folder.gif" alt="$mytopbar"> <b>$mytopbar</b></td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$cgi?action=imsend>$imx{'046'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>

</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=contacts>$imx{'045'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor=$prefthemecolor align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=im>$imx{'001'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
</tr>
<tr bgcolor=$prefthemecolor><td height=4 colspan=4></td></tr>
</table>

<!-- topbar end -->


~;

}

#############
sub mytopbar  {
#############

open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) { ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $dummy, $theme, $themecolor) = split(/\|/, $curentry);}

if ($theme eq ""){$preftheme = "original";}else{$preftheme = "$theme";}
if ($themecolor eq ""){$prefthemecolor = "#CEE3F8";}else{$prefthemecolor = "#$themecolor";}
print qq~



<!-- topbar -->
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=80% valign=bottom><img src="$imagesurl/im/folders/utility-folder.gif" atl="$mytopbar"> <b>$mytopbar</b></td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$cgi?action=folder>$imx{'051'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=imsend>$imx{'046'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
<td valign=bottom>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="$imagesurl/im/left$preftheme.gif"></td>
<td bgcolor="$prefthemecolor" align=center height=6 valign=top><img src=$imagesurl/im/top$preftheme.gif><br>
<b><a href=$pageurl/$cgi?action=im>$imx{'001'}</a></b></td>
<td><img src=$imagesurl/im/right$preftheme.gif></td></tr></table>
</td>
</tr>
<tr bgcolor="$prefthemecolor"><td height=4 colspan=4></td></tr>
</table>
<!-- topbar end -->


~;

}


#############
sub messageadmin {
#############
if ($access[35] ne "on") { error("$err{'011'}"); }


unless (-e("$memberdir/saved"))
{
   mkdir("$memberdir/saved",0777);
   chmod(0777,"$memberdir/saved");
}
unless (-e("$memberdir/backup"))
{
   mkdir("$memberdir/backup",0777);
   chmod(0777,"$memberdir/backup");
}
unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}
        open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) {

        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $themegif, $themecolor, $image, $contactnum, $myoffice) = split(/\|/, $curentry);}
        $navbar = "$btn{'014'} Message Admin";
        $mytopbar = "Message Admin";
        print_top();
        mytopbar();
        print qq~

<table width=100% colspan=0 cellspan=0>
<tr class=helpsnavtable><td><font color=orange><b>$imx{'035'}</b></font></td></tr><tr class=forumwindow3>
<td>  <form action="$pageurl/$cgi?action=messageadmin2" method="post" onSubmit="submitonce(this)">
<input type="text" name="message" size=10 maxlength=3 value="$imxinbox"><B>$imx{'032'}</b>

<br>
<input type="text" name="message1" size=10 maxlength=3 value="$imxsaved"><B>$imx{'034'}</b>

<br>
<input type="text" name="message2" size=10 maxlength=3 value="$imxsent"><B>$imx{'033'}</b>

<br>
<input type="text" name="message3" size=10 maxlength=3 value="$imxfolders"><B>$imx{'051'}</b>
</td></tr></table>
<br>
<table width=100% colspan=0 cellspan=0>

<tr class=helpsnavtable><td><font color=orange><b>$imx{'051'}</font></td></tr>
<tr class=forumwindow3><Td>
<input type="text" name="message4" size=10 maxlength=3 value="$numfolders"><B>$imx{'052'}</b>
</td></tr></table>
<br>
<table width=100% colspan=0 cellspan=0>

<tr class=helpsnavtable><td><font color=orange><b>$imx{'055'} $msg{'161'}</b></font></td></tr><tr class=forumwindow3><Td>~;

$check = "";
$check1 = "";
$check2 = "";
$check3 = "";
$check4 = "";

if ($themegif eq "original") { $check = " checked"; }
if ($themegif eq "red") { $check1 = " checked"; }
if ($themegif eq "purple") { $check2 = " checked"; }
if ($themegif eq "brown") { $check3 = " checked"; }
if ($themegif eq "green") { $check4 = " checked"; }

print qq~
<input type="radio" name="themegif" value="original"$check><img src=$imagesurl/im/toporiginal.gif alt="">   - [IMX ORIGINAL]<br>
<input type="radio" name="themegif" value="red"$check1><img src=$imagesurl/im/topred.gif alt="">   - [IMX BARBIE]<br>
<input type="radio" name="themegif" value="purple"$check2><img src=$imagesurl/im/toppurple.gif alt="">   - [IMX GRAPE]<br>
<input type="radio" name="themegif" value="brown"$check3><img src=$imagesurl/im/topbrown.gif alt="">   - [IMX COCOA]<br>
<input type="radio" name="themegif" value="green"$check4><img src=$imagesurl/im/topgreen.gif alt="">   - [IMX FOREST]<br>
</td></tr></table>
~;
$checked = "";
$checked1 = "";
if ($image eq "1") { $checked = " checked"; }
if ($myoffice eq "1") { $checked1 = " checked"; }
print qq~
<br>
<table width=100% colspan=0 cellspan=0>

<tr class=helpsnavtable><td><font color=orange><b>$imx{'014'} </b></font></td></tr><tr class=forumwindow3><Td>
$msg{'606'}<Br>
<input type="checkbox" value="on" name="image"$checked>$msg{'299'}
<Br>
<Br>
<input type="text" size=5 maxlength=2 value="$contactnum" name="maxcontact">Quicklist #
</td></tr></table>

<br><br>
<input type="submit" value="$imx{'040'}">

 </form>
<br><br><br>~;
 mytopbar();
 print qq~
<table cellspadding=2 cellspacing=0 width=100%>
<tr class=menutable><a name=alertlog></a>
 <td valign=top align=center colspan=5><b></b></td></tr>

<tr bgcolor=$windowbg>
 <td valign=top></td>
 <td valign=top width=50%>$msg{'006'}</td>

 <td valign=top>Folder</td>
 <td valign=top>$msg{'214'} Notified</td>
<td valign=top>$msg{'226'}</td>
</tr>
~;
        open(FILE, "$memberdir/adminim/inbox.txt");
      file_lock(FILE);
      chomp(@alerts = <FILE>);
      unfile_lock(FILE);
      close(FILE);


foreach $curentry (@alerts) { $curentry =~ s/[\n\r]//g; ($myuser, $myuserdate, $fldr) = split(/\|/, $curentry);
if ($fldr eq "inbox"){$linkup = qq~<a href="$pageurl/$cgi?action=userimindex&viewthisuser=$myuser">$fldr</a>~;}
elsif ($fldr eq "sent"){$linkup = qq~<a href="$pageurl/$cgi?action=userimindex2&viewthisuser=$myuser">$fldr</a>~;}
elsif ($fldr eq "saved"){$linkup = qq~<a href="$pageurl/$cgi?action=userimindex3&viewthisuser=$myuser">$fldr</a>~;}
else{$linkup = qq~<a href="$pageurl/$cgi?action=userimindex4&folder=$fldr&viewthisuser=$myuser">$fldr</a>~;}
print qq~<tr bgcolor=$windowbg2><td><img src="$imagesurl/im/aicon1.gif" alt="">
 </td><td valign=top><b><a href="$cgi?action=imsend&to=$myuser">$myuser</a></b></td>
<td>$linkup</td>
<td>$myuserdate</td>
<td>[<a href="$pageurl/$cgi?action=deletefromylog&$ip=$myuser|$myuserdate|$fldr">$nav{'097'}</a>]</td>
</tr>~;}


print qq~
<tr class=forumwindow1><td colspan=5 align=right><a href="$cgi?action=deletefromylog&amp;id=all">$msg{'576'}</a></td></tr>


 </table>
<form action=$pageurl/$cgi?action=userimindex method=post>
$btn{'001'} : <input type=text value="username" name="viewthisuser" size=15 maxlength=85><input type=submit value=$btn{'005'}></form><br>
<br>~;
 imxversion();
 print qq~<br>~;
print_bottom();
}

#############
sub messageadmin2 {
#############





if ($input{'message'} eq "" || $input{'message1'} eq "" || $input{'message2'} eq "" || $input{'message3'} eq "" || $input{'message4'} eq "") {
$navbar ="$btn{'014'} $imx{'030'}";

    print_top();
print qq~<b>$err{'015'}</b><br>

    <br><br><p><b><a href="$pageurl/$cgi?action=messageadmin">Message admin</a></b><br>

    ~;
    print_bottom();
} else {



if ($input{'image'} eq "on"){$image ="1";}else{$image ="0";}

if ($input{'office'} eq "on"){$office ="1";}else{$office ="0";}

    if ($input{'themegif'} eq "original"){$themecolor ="D2E2F6";}
    elsif ($input{'themegif'} eq "red"){$themecolor ="FF39B2";}
    elsif ($input{'themegif'} eq "purple"){$themecolor ="DBCFF2";}
    elsif ($input{'themegif'} eq "green"){$themecolor ="DCE6E7";}
    elsif ($input{'themegif'} eq "brown"){$themecolor ="E7D0C5";}




    open (FILE , ">$memberdir/adminim/admin.txt");
    file_lock(FILE);
    print FILE "$input{'message'}|$input{'message1'}|$input{'message2'}|$input{'message3'}|$input{'message4'}|rategreen|$input{'themegif'}|$themecolor|$image|$input{'maxcontact'}|$office";
    unfile_lock (FILE);
    close (FILE);


        print "Location: $pageurl/$cgi\?action=im\n\n";
    exit;
}




}

####################
sub deletefromylog {
####################

    my %linea;


if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);

}

else {

    open (FILE , "$memberdir/adminim/inbox.txt");
    file_lock(FILE);
    while (<FILE>) {
    $li = $_;
        chomp;
        $linea{$_} = '1';
    }
    unfile_lock (FILE);
    close (FILE);
    open (FILE2 , "+>$memberdir/adminim/inbox.txt");
    foreach $clave (keys %linea) {
            if ($clave eq $info{$ip}) {
                $linea{$info{$ip}} = 0;
                print "$info{$ip} was removed";
            }
            else {
              print FILE2 "$clave\n";
            }

    }
    close (FILE2);
    unfile_lock (FILE2);
}
    print "Location: $pageurl/$cgi\?action=im\n\n";
    exit;
}

##################
# contact subs   #
##################

###################
sub blist
###################
{
unless (-e("$memberdir/adminim/contact"))
{
   mkdir("$memberdir/adminim/contact",0777);
   chmod(0777,"$memberdir/adminim/contact");
}


open(FILE, "<$memberdir/adminim/contact/$username.lst");
file_lock(FILE);
my @buddydata = <FILE>;
unfile_lock(FILE);
close(FILE);
$maxcount = 0;
     @buddydata = (sort { lc($a) cmp lc($b) }@buddydata);

foreach (@buddydata) {
     chomp;
$maxcount++;

open(FILE, "$datadir/log.dat");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);

   foreach $curentry (@entries) {
   chomp;
$curentry =~ s/[\n\r]//g; ($name, $value) = split(/\|/, $curentry);
$listcount  = 0;
        if ($name eq "$_") {  print qq~<tr valign=top>
<td><img src="$imagesurl/im/on.gif"><a href="$pageurl/$cgi?action=imsend&to=$_">$_</a></td>
<td>&nbsp;</td><td><a href="$pageurl/$cgi?action=imsend&to=$_"><img src="$imagesurl/forum/message.gif" border=0 alt="$nav{'029'}"></a></td>
<td>&nbsp;</td><td><a href="$pageurl/$cgi?action=viewprofile&username=$_"><img src="$imagesurl/forum/profile.gif" border=0 alt="$msg{'051'} $_"></a></td></tr>~;}

}
$listcount++;

}
print qq~<tr><td colspan=5>&nbsp;</td></tr>~;

}
##########################
sub quicklist
##########################
{
unless (-e("$memberdir/quickim"))
{
   mkdir("$memberdir/quickim",0777);
   chmod(0777,"$memberdir/quickim");
}
print qq~<tr><td class=menutable colspan=5 align=center><B>Lista Rápida</b></td></tr>

 ~;

open(FILE, "<$memberdir/quickim/$username.lst");
file_lock(FILE);
chomp(@myfavdata = <FILE>);
unfile_lock(FILE);
close(FILE);

  @myfavdata = (sort { lc($a) cmp lc($b) }@myfavdata);
foreach $curentry (@myfavdata) {
                ($name, $value) = split(/\|/, $curentry);

     print qq~<tr valign=top>
<td><a href="$pageurl/$cgi?action=imsend&to=$name">$name</a></td>
</tr>~;}


print qq~
<tr><td>&nbsp;</td></tr>
<tr>
    <td bgcolor="#FFFFFF" valign=bottom height="5" align="right">
<a href="$cgi?action=memberlist"><img src="$imagesurl/yabb/guest.gif" border=0 alt="$bud{'009'}"></a>
&nbsp;<a href="$cgi?action=quicklistedit"><img src="$imagesurl/forum/modify.gif" alt="$bud{'006'}" border=0></a>
<br><small><i><b>
<A HREF="javascript:void()" onclick="window.open('http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=quicklistedit', 'QuickList', 'height=200,width=300', false);">
$bud{'006'}</a></small></i></b>
   </td>
  </tr>~;

}


##############
sub contact {
##############

unless (-e("$memberdir/adminim/contact"))
{
   mkdir("$memberdir/adminim/contact",0777);
   chmod(0777,"$memberdir/adminim/contact");
}

if ($info{'buddy'} ne "") {
           $buddy = $info{'buddy'}; }

$navbar = "$btn{'014'} $imx{'045'}";

$mytopbar = "$imx{'045'}";

        print_top();
        mytopbar4();
        print qq~
<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor=#FAFAEF>


  <tr class=menutable>
  <td><b>$msg{'006'}</b></td>
<td><b></b></td>
  <td><b>$msg{'226'}</b></td> </tr>
~;
 open(FILE, "<$memberdir/adminim/contact/$username.lst");
file_lock(FILE);
chomp(@myfavdata = <FILE>);
unfile_lock(FILE);
close(FILE);

@myfavdata = (sort { lc($a) cmp lc($b) }@myfavdata);
foreach $curentry (@myfavdata) {
                ($name, $value) = split(/\|/, $curentry);
     print qq~<tr bgcolor=#FAFAEF>
     <td><a href="$pageurl/$cgi?action=imsend&to=$name">$name</a></td> <td><a href="$pageurl/$cgi?action=imsend&to=$name">$value</a></td>
     <td>[<a href="$pageurl/$cgi?action=deletecontact&amp;$ip=$name">$nav{'097'}</a>]

</td> </tr>
      ~;
    }
        print qq ~ </table>
<table width="100%" bgcolor=#FAFAEF border="0" cellspacing="0" cellpadding="0">
  <form action="$pageurl/$cgi?action=addcontact" method="post" onSubmit="submitonce(this)">
  <tr><td colspan=2><hr><br><br><br></td></tr>
<td colspan=2><b>$btn{'027'} $imx{'045'}</b></td></tr>
<tr class=menutable><td><b>$msg{'006'}</b></center></td><td><b>$imx{'047'}</b></td></tr>
<tr bgcolor="#d4d7cf">
    <td valing=top>
      <input type="text" name="buddy" size=30 maxlength=150 value="$buddy"> </td><Td><table>
~;
blist();
print qq~
     </table> </td></tr>


<tr bgcolor=#FAFAEF><td colspan=2><input type="submit" name="moda" value="$btn{'027'}"><input type="reset" value="$nav{'097'}"></td>
    </td>
  </tr>

 </form>
  </table>
<br><br><br>
<br><a href="$pageurl/$cgi?action=im">$nav{'028'}</a><br><a href="$pageurl/$cgi?action=memberlist">$nav{'019'}</a>
  ~;
  print_bottom();
}

##########################
sub editcontact{
##########################

   unless (-e("$memberdir/adminim/contact")) {
        mkdir("$memberdir/adminim/contact",0777);
        chmod(0777,"$memberdir/adminim/contact");
   }

if ($info{'buddy'} ne "") {
           $buddy = htmlescape("$info{'buddy'}"); }
if ($info{'heading'} ne "") {
           $heading = $info{'buddy'}; }



$navbar = "$btn{'014'} $imx{'045'}";
        print_top();
        print qq~
 <center><b><h3>$imx{'045'}</b></h3></center><p>

<center>
<table width="80%" bgcolor=#FAFAEF border="0" cellspacing="0" cellpadding="0">
  <form action="$pageurl/$cgi?action=addcontact2" method="post" onSubmit="submitonce(this)">
  <tr><td colspan=2><hr><br><br><br></td></tr>
<td colspan=2><b>$btn{'015'}</b></td></tr>
<tr bgcolor=#FAFAEF><td><b>$msg{'006'}</b></center></td><td><b></b></center></td></tr><tr bgcolor="#d4d7cf">
    <td valign=top>
      <input type="text" name="buddy" size=40 maxlength=150 value="$buddy"> </td><Td valign=top>
<input type="hidden" name="heading" size=30 maxlength=150 value="$buddy" readonly>

      </td></tr>


<tr><td colspan=2><input type="hidden" name="oldcat2" value="$heading">
<input type="hidden" name="oldcat" value="$buddy">
<input type="submit" name="moda" value="$btn{'015'}"></td>
    </td>
  </tr>

 </form>
  </table>
<br><br><br><a href="$pageurl/$cgi?action=contacts">$imx{'045'}</a>
<br><a href="$pageurl/$cgi?action=im">$nav{'028'}</a>
  ~;
  print_bottom();
}



#################
sub addcontact {
#################


unless (-e("$memberdir/adminim/contact"))
{
   mkdir("$memberdir/adminim/contact",0777);
   chmod(0777,"$memberdir/adminim/contact");
}

   if (-e("$memberdir/$input{'buddy'}.dat")) { } else { error("$err{'010'}"); }

   $buddy = $input{'buddy'};

      open (FILE , "$memberdir/adminim/contact/$username.lst");
      file_lock(FILE);
      chomp(@entries = <FILE>);
      unfile_lock(FILE);
      close(FILE);

   foreach $curentry (@entries) {($name, $dummy) = split(/\|/, $curentry);}

    if ($name ne "$buddy") {

    open (FILE2 , ">>$memberdir/adminim/contact/$username.lst");
    file_lock(FILE2);
    print FILE2 "$buddy\n";
    unfile_lock (FILE2);
    close (FILE2);
    print "Location: $pageurl/$cgi\?action=contacts\n\n";
    exit;

}else{



    print "Location: $pageurl/$cgi\?action=contacts\n\n";
   exit;

     }



}

#################
sub addcontact2 {
#################
 $navbar ="$btn{'014'} $imx{'045'}";
    print_top();
 if (-e("$memberdir/$input{'buddy'}.dat")) { } else { error("$err{'010'}"); }
if ($input{'heading'} eq "$input{'buddy'}") { error("$imx{'047'} $imx{'049'} $msg{'006'}"); }
$mybuddy = htmltotext("$input{'buddy'}");


      open(FILE, "$memberdir/adminim/contact/$username.lst") || error("$err{'001'} $memberdir/adminim/contact/$username.lst");
        file_lock(FILE);
        @cats = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        if ($input{'moda'} eq $btn{'015'}) {
                chomp($input{'oldcat'});
                chomp($input{'oldcat2'});
                open(FILE, ">$memberdir/adminim/contact/$username.lst") || error("$err{'016'} $memberdir/adminim/contact/$username.lst");
                file_lock(FILE);
                foreach $line (@cats) {
                        chomp($line);
                        ($name,$value) = split(/\|/, $line);
                        if ($name eq $input{'oldcat'} || $name eq $input{'buddy'}) { print FILE "$mybuddy\n";  }
                        else { print FILE "$line\n"; }
                }
                unfile_lock(FILE);
                close(FILE);
}
    print "$input{'heading'} $imx{'048'}";
    print qq ~ <br>
    <p><b><a href="$pageurl/$cgi?action=contacts">$imx{'045'}</a></b><br>
        <b><a href="$pageurl/$cgi?action=im">$nav{'028'}</a></b>
    ~;
    print_bottom();





}


####################
sub deletecontact {
####################


    my %linea;
    $navbar ="$btn{'014'} $imx{'045'}";
    print_top();
    print_top();
    open (FILE , "$memberdir/adminim/contact/$username.lst");
    file_lock(FILE);
    while (<FILE>) {
    $li = $_;
        chomp;
        $linea{$_} = '1';
    }
    unfile_lock (FILE);
    close (FILE);
    open (FILE2 , "+>$memberdir/adminim/contact/$username.lst");
    foreach $clave (keys %linea) {
            if ($clave eq $info{$ip}) {
                $linea{$info{$ip}} = 0;
                print "$info{$ip} $msg{'228'}";
            }
            else {
              print FILE2 "$clave\n";
            }

    }
    close (FILE2);
    unfile_lock (FILE2);
    print qq ~

    <p><b>$msg{'229'} $msg{'224'}</b>
<Br><br>
<a href="$pageurl/$cgi?action=im">$nav{'028'}</a><br><a href="$pageurl/$cgi?action=contacts">$imx{'045'}</a>

    ~;
    print_bottom();
}


####################
# imindexes subs   #
####################


#############
sub imindex {
#############
        if ($username eq "$anonuser") { error("noguests"); }



        open(FILE, "$memberdir/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $mnum1 = @imessages;

        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);
                  open(IM3, "$memberdir/saved/$username.msg");
                  file_lock(IM3);
                  @immessages3 = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum3 = @immessages3;

                  open(IM, "$memberdir/backup/$username.msg");
                  file_lock(IM);
                  @immessages2 = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum2 = @immessages2;
                  $messnum = "$mnum2";

        $umessageid = $info{"messageid"};
        $navbar = "$btn{'014'} $nav{'028'}";
        $mytopbar = "<b>$imx{'001'}  </b>($mnum1)";
        print_top();
        mymaintopbar();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
~;
if ($umessageid ne "") {
        imview();
}
print qq~<table cellpadding="0" cellspacing="0" width="100%" border="0">
<!--<tr class=menutable><td colspan=4><B>$imx{'001'}</b> ($mnum1)</td></tr>-->



</table>

        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1">
<tr class=forumwindow1>
<td><b>&nbsp;</b></td>
<td width="10%"><b>$msg{'182'}</b></td>
<td width="20%"><b>$msg{'214'}:</b></td>
<td width="50%"><b>$msg{'037'}</b></td>
<td width=15%><b>$msg{'208'}:</b></td>

</tr>

~;

        if (@imessages == 0) {

                print qq~<tr>
<td colspan="5" class="imwindow2">$msg{'050'}</td>
</tr>~;
}
$notseen = "0";

        $second = "imwindow1";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow2") { $second="imwindow1"; }
                else { $second="imwindow2"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);

                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }
                if ($micon[$a] eq "" || $micon[$a] eq "1") {$micon[$a] ="aicon"; }
                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";

                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";
if ($musername[$a] eq ""){$whoiam = $msg{'183'};}else{$whoiam = $musername[$a];}
foreach (@imessages) {
open(FILE, "$datadir/log.dat");
file_lock(FILE);
@entries = <FILE>;
unfile_lock(FILE);
close(FILE);
 $foundit = 0;

foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($name, $value) = split(/\|/, $curentry);
                  if ($name eq "$musername[$a]" && $name eq "$anonuser") {
$amionline = qq~<img src=$imagesurl/im/online.gif alt=$imx{'043'}> <font size=1pt>$whoiam</font>~; $foundit = 1; }
elsif ($name eq "$musername[$a]" && $name ne "$anonuser") {
$amionline = qq~<img src=$imagesurl/im/online.gif alt=$imx{'043'}> <a href="$cgi?action=imsend&to=$whoiam">$whoiam</a>~; $foundit = 1; }
else { unless ($foundit == "1") { $amionline = qq~<img src=$imagesurl/im/offline.gif alt=$imx{'044'}> <font size=1pt>$whoiam</font>~;} }

}
}
if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";

        $notseen++;
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}
if ($info{'start'} eq "") { $start = 0; }
        else { $start = "$info{'start'}"; }

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
$notread = qq~<img src="$imagesurl/im/envelope.gif" border="0" alt="">~;}
else{$notread = qq~<img src="$imagesurl/im/reademail.gif" alt="" border="0">~;}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;


#print qq~<td class=$second align=center>
#<a href="$cgi?action=im&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$notseen</a></td>~;

print qq~<td class="$second" align=center><b>
<font color=navy>
<a href="$cgi?action=im&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">
$notread
</a></font></b></td>
<td class="$second" nowrap>$amionline</td>
<td class="$second" width="20%" nowrap>&nbsp;$mdate[$a]&nbsp;</td>
<td class="$second" width="50%">&nbsp;<a href="$cgi?action=im&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$newim$msub[$a]</a>&nbsp;</td>~;

if ($msuername[$a] eq "$anonuser"){
print qq~<td class="$second">
<a href="$cgi?action=imremove&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>~;
} else {

print qq~<td class="$second" width="10%">

<a href="$cgi?action=imsend&to=$musername[$a]&num=$messageid[$a]"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>
&nbsp;&nbsp;

<a href="$cgi?action=imremove&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a>~;
}

print qq~</td></tr>~;
}


print qq~
<tr bgcolor=$prefthemecolor><td colspan=5 align=right><a href="$cgi?action=imremove&amp;id=all">$msg{'576'}</a></td></tr>
<tr bgcolor=$prefthemecolor><td colspan=5 align=right></td></tr>
        </table>
<table width=100% border=0 cellpadding=1 cellspacing=0><tr><td valign=top>
~;

jumplist("inbox");

print qq~<hr><font color=navy face=Helvetica>
$msg{'305'} <b>$memsettings[1]</b>, <br>$msg{'342'} $notseen $imx{'058'}.  </font>
</td><td valign=top align=right>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=100% align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;
open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar, $themegif, $themecolor, $image, $contactnum, $myoffice) = split(/\|/, $curentry);}

if ($imxinbox eq ""){$messages = "25";}
else{$messages = "$imxinbox";}

$averagescore = "$mnum1";

$multiply = ((100/$messages));
$usando = ($messages-$averagescore)*$multiply;
$actual = $averagescore*$multiply;
$greycells = $usando;
$myratebar = $myratebar;

$aa = $actual;
$bb = sprintf("%.f", $aa);

if ($bb <= "-1"){$bb = "0";}
else{$bb = $bb;}

if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt="$bb%"><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt="$bb%"><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;

        unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}


        open (FILE, "$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        @imalerts = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        $date = "$date";
        open (FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "$username|$date|inbox\n";
        foreach $curm (@imalerts) { print FILE "$curm"; }
        unfile_lock(FILE);
        close (FILE);







}


print qq~</td></tr>

<tr><td></td></tr>
<tr><td>
$usando3~;

if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}

$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}

print qq~
$imx{'003'} = <b>$b%  </b>  <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table></td></tr></table>

<table width=100% cellspacing="0" cellpadding="0" bordercolor=white border=1><tr>

<td valign=top width=100%>

<table cellpadding="4" cellspacing="0" width="100%" border="0">

<tr><td colspan=4 align=right bgcolor=$prefthemecolor height=2><b>$imx{'001'} </b> ($mnum1)</td></tr>

<tr>
<td width=55% align=left valign=top>&nbsp; ~;


#if ($myoffice eq "1"){print qq~
#<table cellpadding="2" cellspacing="0" border=1 bordercolor=$prefthemecolor><tr><td>
#<a href="$pageurl/mods/office/index.cgi">
#<img src="$imagesurl/im/office/office_small.gif" border="0"></a>
#<a href="$pageurl/mods/office/calendar.cgi">
#<img src="$imagesurl/im/office/calendar_small.gif" border="0"></a>
#<a href="$pageurl/mods/office/tasks.cgi">
#<img src="$imagesurl/im/office/task_small.gif" border="0"></a>
#<a href="$pageurl/mods/office/journal.cgi">
#<img src="$imagesurl/im/office/journal_small.gif" border="0"></a>
#<a href="$pageurl/mods/office/contacts.cgi">
#<img src="$imagesurl/im/office/contact_small.gif" border="0"></a>
#</td></tr><tr bgcolor=$prefthemecolor><td><center>WebOffice</center></td></tr></table>
#~;}


print qq~
</td>
<td valign=top><table width=100%><tr>
<td align="right"><a href="$cgi?action=imsend"><img src=$imagesurl/im/icon_reply.gif border=0 alt=$nav{'029'}></a></td>
<td align="center"><a href="$cgi?action=imfolder"><img src=$imagesurl/im/icon_return.gif border=0 alt="$imx{'008'}"></a></td>
<td align="center"><a href="$cgi?action=saveim"><img src=$imagesurl/im/icon_save.gif border=0 alt="$imx{'010'}"></a></td>
</tr>
<tr>
<td align="right" valign=top>$nav{'029'}</td>
<td align="center" valign=top>$imx{'005'}<br> ($mnum2)</td>
<td align="center" valign=top>$imx{'006'}<br> ($mnum3)</td>
</tr>


</table>
</td></tr>
</table><br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<br><table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}

#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>
~;
}





print qq~</td></tr></table><br>~;

print_bottom();
}


#############
sub userimindex {
#############
        if ($username ne "admin") { error("noguests"); }

if ($info{'viewthisuser'} ne "") { $myuser = $info{'viewthisuser'}; }
if ($input{'viewthisuser'} ne "") { $myuser = $input{'viewthisuser'}; }
        open(FILE, "$memberdir/$myuser.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $mnum1 = @imessages;

        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$myuser.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);
                  open(IM3, "$memberdir/saved/$myuser.msg");
                  file_lock(IM3);
                  @immessages3 = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum3 = @immessages3;

                  open(IM, "$memberdir/backup/$myuser.msg");
                  file_lock(IM);
                  @immessages2 = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum2 = @immessages2;
                  $messnum = "$mnum2";

        $umessageid = $info{"messageid"};
        $navbar = " $btn{'014'} $nav{'062'} - $myuser";
        $mytopbar= " <b>$myuser</b> ";

        print_top();
        mytopbar5();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>

        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1"><tr>
<td class="imtitle"><b></b></td>
<td class="imtitle" width="10%"><b>$msg{'182'}</b></td>
<td class="imtitle" width="20%"><b>$msg{'214'}:</b></td>
<td class="imtitle" width="50%"><b>$msg{'037'}</b></td>
<td class="imtitle" width=15%><b>$msg{'208'}:</b></td>

</tr>

~;

        if (@imessages == 0) {
                print qq~<tr>
<td colspan="5" class="imwindow1">$msg{'050'}</td>
</tr>~;
}
        $second = "imwindow2";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow1") { $second="imwindow2"; }
                else { $second="imwindow1"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);

                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                if ($micon[$a] eq "") {$micon[$a] ="aicon"; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }

                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;
$numbers = $a+1;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" align=center><b>
<font color=navy>$numbers</font></b></td><td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second" align=center><b><font color=navy>$numbers</font></b></td><td class="$second" width="10%"> <a href="$cgi?action=imsend&to=$musername[$a]" class="$imnav">$musername[$a]</a></td>~;
}

print qq~<td class="$second" width="20%" nowrap>$mdate[$a]</td>
<td class="$second" width="50%">$msub[$a]</td>


<td class="$second" width="10%"><center>

<a href="$cgi?action=myuserremove&id=$messageid[$a]&viewthisuser=$myuser"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>
</tr>        ~;}
print qq~


</table>
<p align=right>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=200 align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;
open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}
$bar = "$bar";
if ($imxinbox eq ""){$messages = "25";}
else{$messages = "$imxinbox";}
$averagescore = "$mnum1";
$multiply = ((100/$messages));

$usando = ($messages-$averagescore)*$multiply;
$actual =$averagescore*$multiply;
$greycells = "$usando";
$myratebar = $myratebar;

if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;



}


print qq~</td></tr>

<tr><td></td></tr>
<tr><td>
$usando3~;

if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}

if ($usando <= "-1"){
unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}


        open (FILE, "$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        @imalerts = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        $date = "$date";
        open (FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "$username|$date|inbox\n";
        foreach $curm (@imalerts) { print FILE "$curm"; }
        unfile_lock(FILE);
        close (FILE);
}

$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}

print qq~
$imx{'003'} = <b>$b%  </b> <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table>~;
print qq~</p>
<table cellpadding="0" cellspacing="0" width="100%" border="0">
<tr class=boardtitle><td colspan=4><B>$imx{'001'}</b> ($mnum1)</td></tr>

<tr>
<td width=55% valign=top>&nbsp;~;

if($username eq "admin"){print qq~<form name="jump">
$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
<option value="#">-- $imx{'051'} --</option>~;

open(FILE, "<$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        my @folder = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $imxmnum = @folder;
        @folder = (sort { lc($a) cmp lc($b) } @folder);
 foreach $line (@folder) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[0] eq "") { }
           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
}
print qq~
<option value="$pageurl/$cgi?action=im">$imx{'001'}</option>
<option value="$pageurl/$cgi?action=messageadmin">IMX Admin</option>
</select>
</form>~;}


print qq~
</td>
<td align="right"></td>
<td align="right"><a href="$pageurl/$cgi?action=userimindex2&viewthisuser=$myuser"><img src=$imagesurl/im/icon_return.gif border=0 alt="$imx{'008'}"></a></td>
<td align="right"><a href="$pageurl/$cgi?action=userimindex3&viewthisuser=$myuser"><img src=$imagesurl/im/icon_save.gif border=0 alt="$imx{'010'}"></a></td>


        </tr>

<tr bgcolor=white>
<td width=55%>&nbsp;</td>
<td align="right" valign=top></td>
<td align="right" valign=top>$imx{'005'}<br> ($mnum2)</td>
<td align="right" valign=top>$imx{'006'}<br> ($mnum3)</td>
</tr>
<tr class=menutable><td colspan=4 align=right>&nbsp;</td></tr>

</table><br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}

#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}



print qq~<br>~;

print_bottom();
}


#############
sub imfolder {
#############

{
unless (-e("$memberdir/backup"))
{
   mkdir("$memberdir/backup",0777);
   chmod(0777,"$memberdir/backup");
}
        if ($username eq "$anonuser") { error("noguests"); }
        open(IM, "$memberdir/$username.msg");
                  file_lock(IM);
                  @buzonmessages = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum2 = @buzonmessages;


        open(IM2, "$memberdir/backup/$username.msg");
                  file_lock(IM2);
                  @imessages = <IM2>;
                  unfile_lock(IM2);
                  close(IM2);
                  $mnum1 = @imessages;
        open(IM3, "$memberdir/saved/$username.msg");
                  file_lock(IM3);
                  @immessages3 = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum3 = @immessages3;


        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        $umessageid = $info{"messageid"};
        $navbar = "$btn{'014'} $imx{'008'}";
        $mytopbar ="<B>$imx{'008'}</b> ($mnum1)";
        print_top();
        mymaintopbar();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
~;
if ($umessageid ne "") {
        imview2();
}
print qq~<table cellpadding="0" cellspacing="0" width="100%" border="0">
<!--<tr class=menutable><td colspan=4><B>$imx{'008'}</b> ($mnum1)</td></tr>-->


</table>
        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1"><tr>
<td class="imtitle" width="5%"><b>&nbsp;</b></td>
<td class="imtitle" width="10%"><b>$msg{'320'}</b></td>
<td class="imtitle" width="20%"><b>$msg{'214'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>
</tr>
~;

        if (@imessages == 0) {
                print qq~<tr>
<td colspan="5" class="imwindow1">$imx{'025'}</td>
</tr>~;
}
        $second = "imwindow2";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow1") { $second="imwindow2"; }
                else { $second="imwindow1"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $recipient, $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);

                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                if ($micon[$a] eq "") {$micon[$a] ="aicon"; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }

                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;
$numbers=$a+1;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" align=center><b>
<font color=navy><a href="$cgi?action=im2&amp;to=$recipient&amp;messageid=$messageid[$a]" class="$imnav">
<img src="$imagesurl/im/aicon1.gif" border=0></a></font></b>
</td><td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second" align=center><b><font color=navy><a href="$cgi?action=im2&amp;to=$recipient&amp;messageid=$messageid[$a]" class="$imnav">
<img src="$imagesurl/im/$micon[$a].gif" border=0>
</font></b></td><td class="$second" width="10%"><a href="$cgi?action=imsend&to=$recipient" class="$imnav">$recipient</a></td>~;
}

print qq~<td class="$second" width="20%" nowrap>&nbsp;$mdate[$a]&nbsp;</td>
<td class="$second" width="60%">&nbsp;<a href="$cgi?action=im2&amp;to=$recipient&amp;messageid=$messageid[$a]" class="$imnav">$msub[$a]</a>&nbsp;</td>~;

if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imremove2&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
} else {print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imsend&to=$musername[$a]&num=$messageid[$a]"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>&nbsp;&nbsp;<a href="$cgi?action=imremove2&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
}
print qq~</tr>~;
}

print qq~<tr bgcolor="$prefthemecolor"><td colspan=5 align=right><a href="$cgi?action=imremove2&amp;id=all">$msg{'576'}</a></td></tr>
</table>
<p align=right>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=200 align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;

open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}

if ($imxsent eq ""){$messages = "25";}
else{$messages = "$imxsent";}
$averagescore = "$mnum1";


$multiply = ((100/$messages));


$usando = ($messages-$averagescore)*$multiply;
$actual =$averagescore*$multiply;
$greycells = "$usando";
$myratebar = $myratebar;

if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;

        unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}


        open (FILE, "$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        @imalerts = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        $date = "$date";
        open (FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "$username|$date|sent\n";
        foreach $curm (@imalerts) { print FILE "$curm"; }
        unfile_lock(FILE);
        close (FILE);







}


print qq~</td></tr>

<tr><td></td></tr>
<tr><td>$usando3~;
if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}

$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}

print qq~
$imx{'003'} = <b>$b%  </b> <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table>~;

print qq~</p><a name=folder></a>
<table cellpadding="0" cellspacing="0" width="100%" border="1" bordercolor=white><tr><Td>
<table cellpadding="0" cellspacing="0" width="100%" border="0">
<tr><td colspan=4 align=right bgcolor=$prefthemecolor><B>$imx{'008'}</b> ($mnum1)</td></tr>

<tr>
<td width=55% align=left>
~;

jumplist("sent");


#<form name="jump">
#$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
#<option value="#">-- $imx{'051'} --</option>


#<option value="$pageurl/$cgi?action=imfolder">My Inbox</option>
#<option value="$pageurl/$cgi?action=saveim">Saved Message's</option>

#~;

#open(FILE, "<$memberdir/adminim/folder/$username.txt");
#        file_lock(FILE);
#        my @folder = <FILE>;
#        unfile_lock(FILE);
#        close(FILE);
#        $imxmnum = @folder;
#        @folder = (sort { lc($a) cmp lc($b) } @folder);
# foreach $line (@folder) {
#           $line =~ s/[\n\r]//g;
#           @item = split(/\|/, $line);
#           if ($item[0] eq "") { }
#           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
#}
#print qq~
#<option value="$pageurl/$cgi?action=folder">$btn{'015'} $imx{'051'}</option>~;
#if($username eq "admin"){print qq~<option value="$pageurl/$cgi?action=messageadmin">IMX Admin</option>~;}
#print qq~
#</select>
#</form>


print qq~
</td>
<td><table width=100% cellpadding=4 cellspacing=0><tr>

<td align="center"><a href="$cgi?action=im"><img src=$imagesurl/im/message.gif border=0 alt="$imx{'001'}"></a></td>
<td align="center"><a href="$cgi?action=saveim"><img src=$imagesurl/im/icon_save.gif border=0 alt="$imx{'010'}"></a></td>
<td align="center"><a href="$cgi?action=imsend"><img src=$imagesurl/im/icon_reply.gif border=0 alt=$nav{'029'}></a></td>
</tr>

<tr>

<td align="center" valign=top>$imx{'001'}<br> ($mnum2)</td>
<td align="center" valign=top>$imx{'006'}<br> ($mnum3)</td>
<td align="center" valign=top>$nav{'029'}</td>
</tr></table></td></tr>

</table><br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}


#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}



print qq~</td></tr></table></td></tr></table><br>~;

print_bottom();
}

}


#############
sub userimindex2 {
#############



{
unless (-e("$memberdir/backup"))
{
   mkdir("$memberdir/backup",0777);
   chmod(0777,"$memberdir/backup");
}
        if ($username ne "admin") { error("noguests"); }

        if ($info{'viewthisuser'} ne "") {
           $myuser = $info{'viewthisuser'}; }

        open(IM, "$memberdir/$myuser.msg");
                  file_lock(IM);
                  @buzonmessages = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum2 = @buzonmessages;


        open(IM2, "$memberdir/backup/$myuser.msg");
                  file_lock(IM2);
                  @imessages = <IM2>;
                  unfile_lock(IM2);
                  close(IM2);
                  $mnum1 = @imessages;
        open(IM3, "$memberdir/saved/$myuser.msg");
                  file_lock(IM3);
                  @immessages3 = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum3 = @immessages3;


        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$myuser.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        $umessageid = $info{"messageid"};
        $navbar = "$btn{'014'} $nav{'062'} - $imx{'008'} - $myuser";
        $mytopbar= " &nbsp;<b>$imx{'008'} - $myuser</b> ";

        print_top();
        mytopbar5();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>


        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1"><tr>
<td class="imtitle"><b></b></td>
<td class="imtitle" width="10%"><b>$msg{'320'}</b></td>
<td class="imtitle" width="20%"><b>$msg{'214'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>
</tr>
~;

        if (@imessages == 0) {
                print qq~<tr>
<td colspan="5" class="imwindow1">$imx{'025'}</td>
</tr>~;
}
        $second = "imwindow2";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow1") { $second="imwindow2"; }
                else { $second="imwindow1"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $recipient, $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);

                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                if ($micon[$a] eq "") {$micon[$a] ="aicon"; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }

                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;
$numbers=$a+1;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" align=center><b><font color=navy>$numbers</font></b></td><td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second" align=center><b><font color=navy>$numbers</font></b></td><td class="$second" width="10%"><a href="$cgi?action=imsend&to=$recipient" class="$imnav">$recipient</a></td>~;
}

print qq~<td class="$second" width="20%" nowrap>$mdate[$a]</td>
<td class="$second" width="60%">$msub[$a]</td>~;

if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><center><a href="$cgi?action=myuserremove2&id=$messageid[$a]&viewthisuser=$myuser"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
} else {print qq~<td class="$second" width="10%"><center>
&nbsp;&nbsp;<a href="$cgi?action=myuserremove2&id=$messageid[$a]&viewthisuser=$myuser"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
}
print qq~</tr>~;
}

print qq~</table>
<p align=right>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=200 align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;

open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}

if ($imxsent eq ""){$messages = "25";}
else{$messages = "$imxsent";}
$averagescore = "$mnum1";


$multiply = ((100/$messages));


$usando = ($messages-$averagescore)*$multiply;
$actual =$averagescore*$multiply;
$greycells = "$usando";
$myratebar = $myratebar;
if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;

        unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}


        open (FILE, "$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        @imalerts = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        $date = "$date";
        open (FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "$username|$date|sent\n";
        foreach $curm (@imalerts) { print FILE "$curm"; }
        unfile_lock(FILE);
        close (FILE);







}


print qq~</td></tr>

<tr><td></td></tr>
<tr><td>$usando3~;
if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}

$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}

print qq~
$imx{'003'} = <b>$b%  </b> <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table>~;

print qq~</p>
<table cellpadding="0" cellspacing="0" width="100%" border="0">
<tr><td colspan=4 bgcolor=$prefthemecolor>&nbsp;<b>$imx{'008'} - $myuser</b> ($mnum1)</td></tr>

<tr bgcolor=white>
<td width=55% valign=top>&nbsp;~;


if($username eq "admin"){print qq~<form name="jump">
$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
<option value="#">-- $imx{'051'} --</option>
~;

open(FILE, "<$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        my @folder = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $imxmnum = @folder;
        @folder = (sort { lc($a) cmp lc($b) } @folder);
 foreach $line (@folder) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[0] eq "") { }
           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
}
print qq~
<option value="$pageurl/$cgi?action=im">$imx{'001'}</option>
<option value="$pageurl/$cgi?action=messageadmin">IMX Admin</option>
</select>
</form>~;

}

print qq~
</td>
<td align="center"></td>

<td align="center"><a href="$pageurl/$cgi?action=userimindex&viewthisuser=$myuser"><img src=$imagesurl/im/message.gif border=0 alt="$imx{'001'}"></a></td>
<td align="center"><a href="$pageurl/$cgi?action=userimindex3&viewthisuser=$myuser"><img src=$imagesurl/im/icon_save.gif border=0 alt="$imx{'010'}"></a></td>


        </tr>

<tr bgcolor=white>
<td width=55%>&nbsp;</td>
<td align="center" valign=top></td>
<td align="center" valign=top>$imx{'001'}<br> ($mnum2)</td>
<td align="center" valign=top>$imx{'006'}<br> ($mnum3)</td>
</tr>
<tr class=menutable><td colspan=4 align=right></td></tr>

</table><br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}


#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}



print qq~<br>~;

print_bottom();
}

}



#############
sub userimindex3 {
#############

{
unless (-e("$memberdir/saved"))
{
   mkdir("$memberdir/saved",0777);
   chmod(0777,"$memberdir/saved");
}



        if ($username ne "admin") { error("noguests"); }

        if ($info{'viewthisuser'} ne "") {
           $myuser = $info{'viewthisuser'}; }

        open(IM3, "$memberdir/$myuser.msg");
                  file_lock(IM3);
                  @buzonmessages = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum2 = @buzonmessages;

            open(IM, "$memberdir/backup/$myuser.msg");
                  file_lock(IM);
                  @foldermessages = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum3 = @foldermessages;


        open(IM2, "$memberdir/saved/$myuser.msg");
                  file_lock(IM2);
                  @imessages = <IM2>;
                  unfile_lock(IM2);
                  close(IM2);
                  $mnum1 = @imessages;


        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        $umessageid = $info{"messageid"};
        $navbar = "$btn{'014'} $nav{'062'} - $imx{'010'} - $myuser";
        $mytopbar= " &nbsp;<b>$imx{'010'} - $myuser</b> ";
        print_top();
        mytopbar5();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>


        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1"><tr>
<td class="imtitle"><b></b></td>
<td class="imtitle" width="10%"><b>$msg{'182'}</b></td>
<td class="imtitle" width="20%"><b>$imx{'006'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>

</tr>
~;

        if (@imessages == 0) {
                print qq~<tr>
<td colspan="5" class="imwindow1">$imx{'026'}</td>
</tr>~;
}
        $second = "imwindow2";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow1") { $second="imwindow2"; }
                else { $second="imwindow1"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);





                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                if ($micon[$a] eq "") {$micon[$a] ="aicon"; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }

                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;
$numbers = $a+1;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" align=center><b><font color=navy><a href="$cgi?action=im3&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$numbers</a></font></b></td><td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second" align=center><b><font color=navy>$numbers</font></b></td><td class="$second" width="10%"> <a href="$cgi?action=imsend&to=$musername[$a]" class="$imnav">$musername[$a]</a></td>~;
}

print qq~<td class="$second" width="20%" nowrap>$mdate[$a]</td>
<td class="$second" width="60%">$msub[$a]</td>~;

if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><center><a href="$cgi?action=myuserremove3&id=$messageid[$a]&viewthisuser=$myuser"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
} else {print qq~<td class="$second" width="10%"><center><a href="$cgi?action=myuserremove3&id=$messageid[$a]&viewthisuser=$myuser"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
}
print qq~</tr>~;
}

print qq~</table>

<p align=right>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=200 align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;

open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}

if ($imxsaved eq ""){$messages = "25";}
else{$messages = "$imxsaved";}
$averagescore = "$mnum1";


$multiply = ((100/$messages));


$usando = ($messages-$averagescore)*$multiply;
$actual =$averagescore*$multiply;
$greycells = "$usando";
$myratebar = $myratebar;

if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;

        unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}


        open (FILE, "$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        @imalerts = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        $date = "$date";
        open (FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "$username|$date|saved\n";
        foreach $curm (@imalerts) { print FILE "$curm"; }
        unfile_lock(FILE);
        close (FILE);







}


print qq~</td></tr>

<tr><td></td></tr>
<tr><td>
$usando3~;

if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}

$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}

print qq~
$imx{'003'} = <b>$b%  </b> <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table>~;

print qq~</p>
<table cellpadding="0" cellspacing="0" width="100%" border="0">
<tr class=boardtitle><td colspan=4><B>$imx{'010'}</b> ($mnum1)</td></tr>

<tr bgcolor=white>
<td width=55% valign=top>&nbsp;~;

if($username eq "admin"){print qq~<form name="jump">
$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
<option value="#">-- $imx{'051'} --</option>~;

open(FILE, "<$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        my @folder = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $imxmnum = @folder;
        @folder = (sort { lc($a) cmp lc($b) } @folder);
 foreach $line (@folder) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[0] eq "") { }
           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
}
print qq~
<option value="$pageurl/$cgi?action=im">$imx{'001'}</option>
<option value="$pageurl/$cgi?action=messageadmin">IMX Admin</option>
</select>
</form>~;}


print qq~
</td>
<td align="right"></td>
<td align="right"><a href="$pageurl/$cgi?action=userimindex2&viewthisuser=$myuser"><img src=$imagesurl/im/icon_return.gif border=0 alt="$imx{'008'}"></a></td>
<td align="right"><a href="$pageurl/$cgi?action=userimindex&viewthisuser=$myuser"><img src=$imagesurl/im/message.gif border=0 alt="$imx{'001'}"></a></td>


        </tr>

<tr bgcolor=white>
<td width=55%>&nbsp;</td>
<td align="right" valign=top></td>
<td align="right" valign=top>$imx{'005'}<br> ($mnum3)</td>
<td align="right" valign=top>$imx{'001'}<br> ($mnum2)</td>
</tr>
<tr class=menutable><td colspan=4 align=right></td></tr>

</table>
<br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}


#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}



print qq~<br>~;

print_bottom();
}

}



#############
sub userimindex4 {
#############

if ($username ne "admin") { error("noguests"); }

        if ($info{'viewthisuser'} ne "") {
           $myuser = $info{'viewthisuser'}; }


unless (-e("$memberdir/adminim/$myuser"))
{
   mkdir("$memberdir/adminim/$myuser",0777);
   chmod(0777,"$memberdir/adminim/$myuser");
}


$folder = $info{"folder"};

unless (-e("$memberdir/adminim/$myuser/$folder"))
{
   mkdir("$memberdir/adminim/$myuser/$folder",0777);
   chmod(0777,"$memberdir/adminim/$myuser/$folder");
}




        if ($username eq "$anonuser") { error("noguests"); }
        open(IM3, "$memberdir/$myuser.msg");
                  file_lock(IM3);
                  @buzonmessages = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum2 = @buzonmessages;

            open(IM, "$memberdir/backup/$myuser.msg");
                  file_lock(IM);
                  @foldermessages = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum3 = @foldermessages;


        open(IM2, "$memberdir/adminim/$myuser/$folder/$myuser.msg");
                  file_lock(IM2);
                  @imessages = <IM2>;
                  unfile_lock(IM2);
                  close(IM2);
                  $mnum1 = @imessages;


        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$myuser.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        $umessageid = $info{"messageid"};
        $navbar = "$btn{'014'} $nav{'062'} - $folder - $myuser";
        $mytopbar= " &nbsp;<b>$folder - $myuser</b> ";
        print_top();
        mytopbar5();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table cellpadding="0" cellspacing="0" width="100%" border="0">
<!--<tr class=menutable><td colspan=4><B>$folder</b> ($mnum1)</td></tr>-->


</table>
        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1"><tr>
<td class="imtitle" width="5%"><b>&nbsp;</b></td>
<td class="imtitle" width="10%"><b>$msg{'182'}</b></td>
<td class="imtitle" width="20%"><b>$imx{'006'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>

</tr>
~;

        if (@imessages == 0) {
                print qq~<tr>
<td colspan="5" class="imwindow1">$msg{'050'}</td>
</tr>~;
}
        $second = "imwindow2";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow1") { $second="imwindow2"; }
                else { $second="imwindow1"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);





                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                if ($micon[$a] eq "") {$micon[$a] ="aicon"; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }

                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;
$numbers = $a+1;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" align=center><b><font color=navy>$numbers</font></b></td><td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second" align=center><b><font color=navy>$numbers</font></b></td><td class="$second" width="10%"> <a href="$cgi?action=imsend&to=$musername[$a]" class="$imnav">$musername[$a]</a></td>~;
}

print qq~<td class="$second" width="20%" nowrap>$mdate[$a]</td>
<td class="$second" width="60%">$msub[$a]</td>~;

if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imremove5&id=$messageid[$a]&folder=$folder&user=$myuser"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
} else {print qq~<td class="$second" width="10%">
<center>

<a href="$cgi?action=imremove5&id=$messageid[$a]&folder=$folder&user=$myuser"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
}
print qq~</tr>~;
}

print qq~<tr bgcolor="$prefthemecolor"><td colspan=5 align=right><a href="$cgi?action=imremove5&amp;id=all&folder=$folder&user=$myuser">$msg{'576'}</a></td></tr>
</table>
<p align=left>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=200 align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;

open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}

if ($imxfolders eq ""){$messages = "25";}
else{$messages = "$imxfolders";}
$averagescore = "$mnum1";


$multiply = ((100/$messages));


$usando = ($messages-$averagescore)*$multiply;
$actual =$averagescore*$multiply;
$greycells = "$usando";
$myratebar = $myratebar;

if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;


}






print qq~</td></tr>

<tr><td></td></tr>
<tr><td>
$usando3~;

if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}


$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}


print qq~
$imx{'003'} = <b>$b%  </b> <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table>~;


print qq~</p><a name=folder></a>
<table cellpadding="0" cellspacing="0" width="100%" border="0">
<tr class=menutable><td colspan=4 align=right><B>$folder</b> ($mnum1)</td></tr>

<tr bgcolor=white>
<td width=55%>

<form name="jump">
$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
<option value="#">-- $imx{'051'} --</option>~;

open(FILE, "<$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        my @folder = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $imxmnum = @folder;
        @folder = (sort { lc($a) cmp lc($b) } @folder);
 foreach $line (@folder) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[0] eq "") { }
           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
}
print qq~
<option value="$pageurl/$cgi?action=folder">$btn{'015'} $imx{'051'}</option>~;
if($username eq "admin"){print qq~<option value="$pageurl/$cgi?action=messageadmin">IMX Admin</option>~;}
print qq~
</select>
</form>

</td>
<td align="right"><a href="$cgi?action=imsend"><img src=$imagesurl/im/icon_reply.gif border=0 alt=$nav{'029'}></a></td>
<td align="right"></td>
<td align="right"><a href="$cgi?action=im"><img src=$imagesurl/im/message.gif border=0 alt="$imx{'001'}"></a></td>


        </tr>

<tr bgcolor=white>
<td width=55%>&nbsp;</td>
<td align="right" valign=top>$nav{'029'}</td>
<td align="right" valign=top></td>
<td align="right" valign=top>$imx{'001'}<br> ($mnum2)</td>
</tr>


</table>
<br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}


#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}



print qq~<br>~;

print_bottom();
}



#############
sub imsaved {
#############

{
unless (-e("$memberdir/saved"))
{
   mkdir("$memberdir/saved",0777);
   chmod(0777,"$memberdir/saved");
}




        if ($username eq "$anonuser") { error("noguests"); }
        open(IM3, "$memberdir/$username.msg");
                  file_lock(IM3);
                  @buzonmessages = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum2 = @buzonmessages;

            open(IM, "$memberdir/backup/$username.msg");
                  file_lock(IM);
                  @foldermessages = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum3 = @foldermessages;


        open(IM2, "$memberdir/saved/$username.msg");
                  file_lock(IM2);
                  @imessages = <IM2>;
                  unfile_lock(IM2);
                  close(IM2);
                  $mnum1 = @imessages;


        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        $umessageid = $info{"messageid"};
        $navbar = "$btn{'014'} $imx{'010'}";
        $mytopbar = "<B>$imx{'010'}</b> ($mnum1)";
        print_top();
        mymaintopbar();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
~;
if ($umessageid ne "") {
        imview3();
}
print qq~<table cellpadding="0" cellspacing="0" width="100%" border="0">
<!--<tr class=menutable><td colspan=4><B>$imx{'010'}</b> ($mnum1)</td></tr>-->


</table>
        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1"><tr>
<td class="imtitle" width="5%"><b>&nbsp;</b></td>
<td class="imtitle" width="10%"><b>$msg{'182'}</b></td>
<td class="imtitle" width="20%"><b>$imx{'006'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>

</tr>
~;

        if (@imessages == 0) {
                print qq~<tr>
<td colspan="5" class="imwindow1">$imx{'026'}</td>
</tr>~;
}
        $second = "imwindow2";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow1") { $second="imwindow2"; }
                else { $second="imwindow1"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);





                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                if ($micon[$a] eq "") {$micon[$a] ="aicon"; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }

                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;
$numbers = $a+1;
print qq~<tr>~;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" align=center><b><font color=navy><a href="$cgi?action=im3&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav"><img src="$imagesurl/im/aicon1.gif" border=0></a></font></b></td><td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second"align=center><b><font color=navy><a href="$cgi?action=im3&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav"><img src="$imagesurl/im/$micon[$a].gif" border=0>
</a></font></b></td><td class="$second" width="10%"> <a href="$cgi?action=imsend&to=$musername[$a]" class="$imnav">$musername[$a]</a></td>~;
}

print qq~<td class="$second" width="20%" nowrap>&nbsp;$mdate[$a]&nbsp;</td>
<td class="$second" width="60%">&nbsp;<a href="$cgi?action=im3&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$msub[$a]</a>&nbsp;</td>~;

if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imremove3&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
} else {print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imsend&to=$musername[$a]&num=$messageid[$a]"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>&nbsp;&nbsp;

<a href="$cgi?action=imremove3&id=$messageid[$a]"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
}
print qq~</tr>~;
}

print qq~<tr bgcolor="$prefthemecolor"><td colspan=5 align=right><a href="$cgi?action=imremove3&amp;id=all">$msg{'576'}</a></td></tr>
</table>

<p align=right>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=200 align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;

open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}

if ($imxsaved eq ""){$messages = "25";}
else{$messages = "$imxsaved";}
$averagescore = "$mnum1";


$multiply = ((100/$messages));

$usando = ($messages-$averagescore)*$multiply;
$actual =$averagescore*$multiply;
$greycells = "$usando";
$myratebar = $myratebar;
if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;

        unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}


        open (FILE, "$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        @imalerts = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        $date = "$date";
        open (FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "$username|$date|saved\n";
        foreach $curm (@imalerts) { print FILE "$curm"; }
        unfile_lock(FILE);
        close (FILE);







}


print qq~</td></tr>

<tr><td></td></tr>
<tr><td>
$usando3~;

if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}

$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}

print qq~
$imx{'003'} = <b>$b%  </b> <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table>~;

print qq~</p><a name=folder></a>
<table cellpadding="0" cellspacing="0" width="100%" border="1" bordercolor=white><tr><td valign=top>
<table cellpadding="0" cellspacing="0" width="100%">
<tr bgcolor=$prefthemecolor><td colspan=4 align=right><B>$imx{'010'}</b> ($mnum1)</td></tr>

<tr>
<td width=55%>
~;

jumplist("saved");

#<form name="jump">
#$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
#<option value="#">-- $imx{'051'} --</option>~;

#open(FILE, "<$memberdir/adminim/folder/$username.txt");
#        file_lock(FILE);
#        my @folder = <FILE>;
#        unfile_lock(FILE);
#        close(FILE);
#        $imxmnum = @folder;
#        @folder = (sort { lc($a) cmp lc($b) } @folder);
# foreach $line (@folder) {
#           $line =~ s/[\n\r]//g;
#           @item = split(/\|/, $line);
#           if ($item[0] eq "") { }
#           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
#}
#print qq~
#<option value="$pageurl/$cgi?action=folder">$btn{'015'} $imx{'051'}</option>~;
#if($username eq "admin"){print qq~<option value="$pageurl/$cgi?action=messageadmin">IMX Admin</option>~;}
#print qq~
#</select>
#</form>

print qq~
</td><td><table width=100% cellpadding=5 cellspacing=0><tr>
<td align="right"><a href="$cgi?action=im"><img src=$imagesurl/im/message.gif border=0 alt="$imx{'001'}"></a></td>
<td align="right"><a href="$cgi?action=imfolder"><img src=$imagesurl/im/icon_return.gif border=0 alt="$imx{'008'}"></a></td>
<td align="right"><a href="$cgi?action=imsend"><img src=$imagesurl/im/icon_reply.gif border=0 alt=$nav{'029'}></a></td>


        </tr>

<tr>

<td align="right" valign=top>$imx{'001'}<br> ($mnum2)</td>
<td align="right" valign=top>$imx{'005'}<br> ($mnum3)</td>
<td align="right" valign=top>$nav{'029'}</td>
</tr></table>
</td></tr>

</table>
<br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}


#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}



print qq~</td></tr></table><br>~;

print_bottom();
}

}

#############
sub foldermessages {
#############



unless (-e("$memberdir/adminim/$username"))
{
   mkdir("$memberdir/adminim/$username",0777);
   chmod(0777,"$memberdir/adminim/$username");
}


$folder = $info{"folder"};

unless (-e("$memberdir/adminim/$username/$folder"))
{
   mkdir("$memberdir/adminim/$username/$folder",0777);
   chmod(0777,"$memberdir/adminim/$username/$folder");
}




        if ($username eq "$anonuser") { error("noguests"); }
        open(IM3, "$memberdir/$username.msg");
                  file_lock(IM3);
                  @buzonmessages = <IM3>;
                  unfile_lock(IM3);
                  close(IM3);

                  $mnum2 = @buzonmessages;

            open(IM, "$memberdir/backup/$username.msg");
                  file_lock(IM);
                  @foldermessages = <IM>;
                  unfile_lock(IM);
                  close(IM);

                  $mnum3 = @foldermessages;


        open(IM2, "$memberdir/adminim/$username/$folder/$username.msg");
                  file_lock(IM2);
                  @imessages = <IM2>;
                  unfile_lock(IM2);
                  close(IM2);
                  $mnum1 = @imessages;


        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(CENSOR, "$boardsdir/censor.txt");
        file_lock(CENSOR);
        @censored = <CENSOR>;
        unfile_lock(CENSOR);
        close(CENSOR);

        open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        $umessageid = $info{"messageid"};
        $mytopbar = "<B>$folder</b> - ($mnum1)";
        $navbar = "$btn{'014'} $folder";
        print_top();
        mymaintopbar();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
~;
if ($umessageid ne "") {
        imview4();
}
print qq~<table cellpadding="0" cellspacing="0" width="100%" border="0">
<!--<tr class=menutable><td colspan=4><B>$folder</b> ($mnum1)</td></tr>-->


</table>
        <table width="100%" bgcolor="$titlebg" border="0" cellspacing="2" cellpadding="1"><tr>
<td class="imtitle" width="5%"><b>&nbsp;</b></td>
<td class="imtitle" width="10%"><b>$msg{'182'}</b></td>
<td class="imtitle" width="20%"><b>$imx{'006'}:</b></td>
<td class="imtitle" width="60%"><b>$msg{'037'}</b></td>
<td class="imtitle" width="10%"><b>$msg{'208'}:</b></td>

</tr>
~;

        if (@imessages == 0) {
                print qq~<tr>
<td colspan="5" class="imwindow1">$msg{'050'}</td>
</tr>~;
}
        $second = "imwindow2";
        sort {$b[5] <=> $a[5]} @immessages;
        for ($a = 0; $a < @imessages; $a++) {
                if ($second eq "imwindow1") { $second="imwindow2"; }
                else { $second="imwindow1"; }

                ($musername[$a], $msub[$a], $mdate[$a], $mmessage[$a], $messageid[$a], $micon[$a], $mviewed[$a]) = split(/\|/, $imessages[$a]);





                if ($messageid[$a] < 100) { $messageid[$a] = $a; }
                if ($micon[$a] eq "") {$micon[$a] ="aicon"; }
                $subject = "$msub[$a]";
                if ($subject eq "") { $subject="---"; }

                $mmessage[$a] =~ s/\n//g;
                $mmessage[$a] =~ s/\r//g;
                $message="$mmessage[$a]";
                $name = "$mname[$a]";
                $mail = "$memset[2]";
                $date = "$mdate[$a]";
                $ip = "$mip[$a]";
                $postinfo = "";
                $signature = "";
                $viewd = "";
                $icq = "";
                $star = "";
                $newim = "";
                $imnav = "oldimlink";

if ($mviewed[$a] eq "" && $umessageid ne $messageid[$a]) {
        $newim = qq~<img src="$imagesurl/forum/new.gif" border="0" alt="$msg{'543'}">&nbsp;~; $imnav = "newimlink";
}
elsif ($umessageid eq $messageid[$a]) {
        $second = "imselected";
}

display_date($mdate[$a]); $mdate[$a] = $user_display_date;
$numbers = $a+1;
if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" align=center><b><font color=navy><a href="$cgi?action=im4&amp;folder=$folder&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$numbers</a></font></b></td><td class="$second" width="10%"><b>$msg{'668'}</b></td>~;
} else {print qq~<td class="$second" align=center><b><font color=navy><a href="$cgi?action=im4&amp;folder=$folder&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$numbers</a></font></b></td><td class="$second" width="10%"> <a href="$cgi?action=imsend&to=$musername[$a]" class="$imnav">$musername[$a]</a></td>~;
}

print qq~<td class="$second" width="20%" nowrap>$mdate[$a]</td>
<td class="$second" width="60%"><a href="$cgi?action=im4&amp;folder=$folder&amp;from=$musername[$a]&amp;messageid=$messageid[$a]" class="$imnav">$msub[$a]</a></td>~;

if ($musername[$a] eq "$anonuser") {
print qq~<td class="$second" width="10%"><center><a href="$cgi?action=imremove4&id=$messageid[$a]&folder=$folder"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
} else {print qq~<td class="$second" width="10%">
<center>

<a href="$cgi?action=imremove4&id=$messageid[$a]&folder=$folder"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></center></td>~;
}
print qq~</tr>~;
}

print qq~<tr bgcolor="$prefthemecolor"><td colspan=5 align=right><a href="$cgi?action=imremove4&amp;id=all&folder=$folder">$msg{'576'}</a></td></tr>
</table>
<p align=left>
<table width=200 border=1 border-style=solid cellpadding=0 cellspacing=0 bordercolor=$prefthemecolor><tr>
<td bgcolor=white align=center>
<table width=200 align=center><tr><td bgcolor=$prefthemecolor align=center><B>$imx{'002'}</B></td></tr>
<tr><Td bgcolor=white><center><table border=1 bordercolor=gray border-style=solid cellpadding=0 cellspacing=0><tr><Td nowrap>
~;

open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}

if ($imxfolders eq ""){$messages = "25";}
else{$messages = "$imxfolders";}
$averagescore = "$mnum1";


$multiply = ((100/$messages));


$usando = ($messages-$averagescore)*$multiply;
$actual =$averagescore*$multiply;
$greycells = "$usando";
$myratebar = $myratebar;

if ($averagescore = 0 || $actual < 80) {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategreen.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }

elsif ($actual => "80") {


                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/ratered.gif" height="8" width="$actual" border="0" alt=""><img src="$imagesurl/im/rategrey.gif" height="8" width="$greycells" border="0" alt="">&nbsp; 100%
                                                                                ~;
                                                                                }
                                                                                else{
$usando = "100";                                                                                print qq~
                                                                                0% &nbsp;<img src="$imagesurl/im/rategrey.gif" height="8" width="100" border="0" alt="">&nbsp; 100%
                                                                                ~;
}
print qq~</td></tr></table></center>~;
if ($usando < "21" && $usando > "2"){$usando2 = qq~<font color=red>$imx{'011'}</font><br> $imx{'012'}~;}else{$usando2 = qq~ &nbsp; ~;}
if ($usando <= "0"){$usando3 = qq~<h4><font color=red>$imx{'013'}</font></h4>~;

unless (-e("$memberdir/adminim"))
{
   mkdir("$memberdir/adminim",0777);
   chmod(0777,"$memberdir/adminim");
}


        open (FILE, "$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        @imalerts = <FILE>;
        unfile_lock(FILE);
        close (FILE);


        open (FILE, ">$memberdir/adminim/inbox.txt");
        file_lock(FILE);
        print FILE "$username|$date|$folder\n";
        foreach $curm (@imalerts) { print FILE "$curm"; }
        unfile_lock(FILE);
        close (FILE);
}






print qq~</td></tr>

<tr><td></td></tr>
<tr><td>
$usando3~;

if ($usando ne "0")
{$rd_value = int(($usando) + 1);} else {$rd_value = $usando;}

if ($rd_value >= "101"){$rd_v = "100";}
elsif ($usando <= "-1"){$rd_v = "0";}
else{$rd_v = $rd_value;}


$a = $usando;
$b = sprintf("%.f", $a);

if ($b <= "-1"){$b = "0";}
else{$b = $b;}

print qq~
$imx{'003'} = <b>$b%  </b> <br>$imx{'004'} = <B>$messages </b><br>$usando2 </td></tr>
</table></td></tr></table>~;


print qq~</p><a name=folder></a>
<table cellpadding="0" cellspacing="0" width="100%" border="0">
<tr class=menutable><td colspan=4 align=right><B>$folder</b> ($mnum1)</td></tr>

<tr bgcolor=white>
<td width=55%>
~;

jumplist("folder");

#<form name="jump">
#$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
#<option value="#">-- $imx{'051'} --</option>~;

#open(FILE, "<$memberdir/adminim/folder/$username.txt");
#        file_lock(FILE);
#        my @folder = <FILE>;
#        unfile_lock(FILE);
#        close(FILE);
#        $imxmnum = @folder;
#        @folder = (sort { lc($a) cmp lc($b) } @folder);
# foreach $line (@folder) {
#           $line =~ s/[\n\r]//g;
#           @item = split(/\|/, $line);
#           if ($item[0] eq "") { }
#           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
#}
#print qq~
#<option value="$pageurl/$cgi?action=folder">$btn{'015'} $imx{'051'}</option>~;
#if($username eq "admin"){print qq~<option value="$pageurl/$cgi?action=messageadmin">IMX Admin</option>~;}
#print qq~
#</select>
#</form>

print qq~
</td>
<td align="right"><a href="$cgi?action=imsend"><img src=$imagesurl/im/icon_reply.gif border=0 alt=$nav{'029'}></a></td>
<td align="right"></td>
<td align="right"><a href="$cgi?action=im"><img src=$imagesurl/im/message.gif border=0 alt="$imx{'001'}"></a></td>


        </tr>

<tr bgcolor=white>
<td width=55%>&nbsp;</td>
<td align="right" valign=top>$nav{'029'}</td>
<td align="right" valign=top></td>
<td align="right" valign=top>$imx{'001'}<br> ($mnum2)</td>
</tr>


</table>
<br>~;

if ($memsettings[7] eq "Administrator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=siteim">$msg{'562'}</a><br>
<a href="$cgi?action=adminim">$msg{'595'}</a><br>
<a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}


#if ($username ne "admin" && $settings[7] eq "$root") {
#print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
#<td colspan="4" class="imtitle"><b>$msg{'561'}</b></td>
#<tr>
#<td colspan="4" class="imwindow1"><a href="$cgi?action=adminim">$msg{'595'}</a><br>
#<a href="$cgi?action=modim">$msg{'594'}</a></td>
#</tr>
#</table>~;
#}

if ($username ne "admin" && $settings[7] eq "$boardmoderator") {
print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="1" cellpadding="2"><tr>
<td colspan="4" class="imtitle"><b>$msg{'596'}</b></td>
<tr>
<td colspan="4" class="imwindow1"><a href="$cgi?action=modim">$msg{'594'}</a></td>
</tr>
</table>~;
}



print qq~<br>~;

print_bottom();
}

##################
# folders subs   #
##################

#################
sub showfolder {
#################

unless (-e("$memberdir/adminim/$username"))
{
   mkdir("$memberdir/adminim/$username",0777);
   chmod(0777,"$memberdir/adminim/$username");
}
unless (-e("$memberdir/adminim/folder"))
{
   mkdir("$memberdir/adminim/folder",0777);
   chmod(0777,"$memberdir/adminim/folder");
}
if ($username eq "$anonuser") { error("$err{'011'}"); }else{

print qq~
<table cellpadding=1 cellspacing=0 width=155 class=menutable><tr><td>
<table cellpadding=0 cellspacing=0 width=150 bgcolor=white>
<tr class=menutable><a name=folder></a>
 <td colspan=2 valign=top align=center></td></tr>
<tr class=forumwindow1>
<td valign=top><img src="$imagesurl/forum/open.gif" alt="$imx{'001'}"><a href="$pageurl/$cgi?action=im">
$imx{'001'}</a></td>
     <td valign=top></td>
</tr>
<tr class=forumwindow1>
<td valign=top><img src="$imagesurl/forum/open.gif" alt="$imx{'006'}"><a href="$pageurl/$cgi?action=saveim">
$imx{'006'}</a></td>
     <td valign=top></td>
</tr>
<tr class=forumwindow1>
<td valign=top><img src="$imagesurl/forum/open.gif" alt="$imx{'005'}"><a href="$pageurl/$cgi?action=imfolder">
$imx{'005'}</a></td>
     <td valign=top></td>
</tr>
 ~;

        open(FILE, "<$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        my @folder = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $imxmnum = @folder;
        @folder = (sort { lc($a) cmp lc($b) } @folder);

 foreach (@folder) {



     print qq~<tr class=forumwindow1>
     <td><img src="$imagesurl/forum/open.gif" alt="$_"><a href="$pageurl/$cgi?action=messagefolder&folder=$_">
$_</a></td>
     <td align=right>[<a href="$pageurl/$cgi?action=folder">$btn{'030'}</a>]</td>
      ~;
    }

        print qq~ </tr>

<tr><td valign=top colspan=2>&nbsp;</td></tr>
<form action="$pageurl/$cgi?action=addfolder" method="post" onSubmit="submitonce(this)">
<tr class=menutable><td valign=top align=center colspan=2><b>$msg{'356'}</b></td></tr>
<tr><td valign=top colspan=2>&nbsp;</td></tr>
<tr> <td align=right valign=top width=50%><input type="text" name="folder" value="" size=10>
   </td><td align=center valign=top><input type="submit" name="moda" value="$btn{'027'}">
</td>

  </tr>

<tr><td valign=top colspan=2>&nbsp;</td></tr>
<tr><td valign=top colspan=2>&nbsp;</td></tr>
  </form>
<tr class=menutable>
<td valign=bottom width=50%><b>$imx{'051'}</b></td>
     <td valign=bottom width=50% align=right>$imxmnum / $numfolders <a href=$pageurl/$cgi?action=folder><img src="$imagesurl/forum/modify.gif" alt="" border=0></a></td>
</tr>

</td></tr>


  </table></td></tr></table>~;

}

}

#################
sub folder {
#################

unless (-e("$memberdir/adminim/$username"))
{
   mkdir("$memberdir/adminim/$username",0777);
   chmod(0777,"$memberdir/adminim/$username");
}
unless (-e("$memberdir/adminim/folder"))
{
   mkdir("$memberdir/adminim/folder",0777);
   chmod(0777,"$memberdir/adminim/folder");
}
if ($username eq "$anonuser") { error("$err{'011'}"); }else{
$mytopbar = "$imx{'051'}";
$navbar = "$btn{'014'} $imx{'051'}";
        print_top();
        mytopbar2();
print qq~<table cellpadding=0 cellspacing=0 width=100%>
<tr class=menutable><a name=folder></a>
 <td valign=top align=center colspan=5><b></b></td></tr>

<tr class=menubackcolor><td valign=top>
 ~;
         open(FILE, "$memberdir/adminim/admin.txt");
      file_lock(FILE);
      @entries = <FILE>;
      unfile_lock(FILE);
      close(FILE);
for $curentry (@entries) { $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $myratebar) = split(/\|/, $curentry);}

        open(FILE, "<$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        my @folder = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        @folder = (sort { lc($a) cmp lc($b) } @folder);
        $myfolcount = @folder;
print qq~


 <form action="$pageurl/$cgi?action=addfolder" method="post" onSubmit="submitonce(this)">
 <center> <table border="0" cellspacing="3" cellpadding="0" width=100%>
  <tr>
    <td valign=top>

  <center><table border="0" width=100% cellspacing="0" cellpadding="0">

~;
 foreach (@folder) {
     chomp;
     print qq~<tr>
     <td valign=top><img src="$imagesurl/forum/open.gif" alt="$_"><a href="$pageurl/$cgi?action=messagefolder&folder=$_">
$_</a></td>
     <td valign=top>[<a href="$pageurl/$cgi?action=deletefolder&amp;$ip=$_">$nav{'097'}</a>] <font color=red>*</font></td>
      ~;
    }
        print qq~

  </table></center><br><b><img src="$imagesurl/im/folders/1folder.gif" alt="$myfolcount / $numfolders"> $imx{'051'}     $myfolcount / $numfolders</b><br>
    </td>
    <td valign=top>
      <input type="text" name="folder" value="">
     <input type="submit" name="moda" value="$btn{'027'}"><input type="reset" name="reset" value="$btn{'009'}"><br>$msg{'356'}

  </form>

</td></tr>

</table></center>
</td></tr></table>
<table width=100%><tr><td bgcolor=$prefthemecolor>
<font color=red>*</font><font color=navy>$imx{'053'}</font><br>
       <br><br> <center><b><a href="$pageurl/$cgi?action=im">$nav{'102'}</a></b></center></td></tr></table>~;





}
print_bottom();
}
#################
sub addfolder {
#################


        open(FILE, "$memberdir/adminim/admin.txt");
        file_lock(FILE);
        @entries2 = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        foreach $curentry (@entries2) {
        $curentry = ($imxinbox,$imxsaved,$imxsent,$imxfolders,$numfolders) = split(/\|/, $curentry);}

        open(FILE2, "$memberdir/adminim/folder/$username.txt");
        file_lock(FILE2);
        chomp(@folder2 = <FILE2>);
        unfile_lock(FILE2);
        close(FILE2);
        foreach $curentry2 (@folder2) {
        $curentry2 = ($desc,$dummy) = split(/\|/, $curentry2);}

        $imxmnum = @folder2;

if ($numfolders eq ""){$messages = "5";}
else{$messages = "$numfolders";}

$folder = $input{"folder"};

if ($imxmnum >= "$messages") {

$navbar ="$btn{'014'} $imx{'051'}";
    print_top();
print qq~<b><font color=red>$imx{'002'} Error: </font> $messages $imx{'031'} $msg{'580'} $imx{'051'}.</b>

    <br><br><Br>
        <b><a href="$pageurl/$cgi?action=folder">$imx{'051'}</a></b>
        <br>
        <b><a href="$pageurl/$cgi?action=im">$nav{'102'}</a></b>
    ~;
    print_bottom();

} elsif ($folder eq "$desc"){

$navbar ="$btn{'014'} $imx{'051'}";
    print_top();
print qq~<b><font color=red>Error: </font> $err{'037'}</b>

    <br><br><Br>
        <b><a href="$pageurl/$cgi?action=folder">$imx{'051'}</a></b>
        <br>
        <b><a href="$pageurl/$cgi?action=im">$nav{'102'}</a></b>
    ~;
    print_bottom();

}else {

$folder = $input{"folder"};

unless (-e("$memberdir/adminim/$username/$folder"))
{
   mkdir("$memberdir/adminim/$username/$folder",0777);
   chmod(0777,"$memberdir/adminim/$username/$folder");
}
    open (FILE , ">>$memberdir/adminim/folder/$username.txt");
    file_lock(FILE);
    print FILE "$input{'folder'}\n";
    unfile_lock (FILE);
    close (FILE);

   print "Location: $pageurl/$cgi\?action=im\n\n";}
   exit;
}



####################
sub deletefolder  {
####################


    my %linea;
    open (FILE , "$memberdir/adminim/folder/$username.txt");
    file_lock(FILE);
    while (<FILE>) {
    $li = $_;
        chomp;
        $linea{$_} = '1';

    }
    unfile_lock (FILE);
    close (FILE);
    open (FILE2 , "+>$memberdir/adminim/folder/$username.txt");
    foreach $clave (keys %linea) {
            if ($clave eq $info{$ip}) {
                    open (FILE3, "+>$memberdir/adminim/$username/$info{$ip}/$username.msg");
                    file_lock (FILE3);
                    print "";
                    close (FILE3);
                    unfile_lock (FILE3);
                $linea{$info{$ip}} = 0;

                #print "$info{$ip} $bud{'014'}";

            }
            else {
            print FILE2 "$clave\n";
            }

    }
    close (FILE2);
    unfile_lock (FILE2);

    print "Location: $pageurl/$cgi\?action=folder\n\n";
    exit;
}

####################
sub ogdeletefolder  {
####################


    my %linea;
    $navbar ="$btn{'014'} $imx{'051'}";
    print_top();
    print_top();
    open (FILE , "$memberdir/adminim/folder/$username.txt");
    file_lock(FILE);
    while (<FILE>) {
    $li = $_;
        chomp;
        $linea{$_} = '1';

    }
    unfile_lock (FILE);
    close (FILE);
    open (FILE2 , "+>$memberdir/adminim/folder/$username.txt");
    foreach $clave (keys %linea) {
            if ($clave eq $info{$ip}) {
                    open (FILE3, "+>$memberdir/adminim/$username/$info{$ip}/$username.msg");
                    file_lock (FILE3);
                    print "";
                    close (FILE3);
                    unfile_lock (FILE3);
                $linea{$info{$ip}} = 0;

                print "$info{$ip} $bud{'014'}";

            }
            else {
            print FILE2 "$clave\n";
            }

    }
    close (FILE2);
    unfile_lock (FILE2);

    print qq ~

    <p><b>$msg{'229'} $msg{'224'}</b>
<Br><br>
<a href="$pageurl/$cgi?action=im">$nav{'102'}</a>

    ~;
    print_bottom();
}

##################
# imviews subs   #
##################

#############
sub imview {
#############
  if ($username eq "$anonuser") { error("noguests"); }
        #if ($info{'from'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }
        $from = $info{"from"};

        open(FILE, "$memberdir/$from.dat");
        file_lock(FILE);
        @memset = <FILE>;
        unfile_lock(FILE);
        close(FILE);

                open(FILE, ">$memberdir/$username.msg");
                file_lock(FILE);
                foreach $msg (@imessages) {
                chomp $msg;
                ($t, $t, $t, $t, $messageid1, $t) = split(/\|/, $msg);
                if ($umessageid == $messageid1) {
                        ($musername, $msub, $mdate, $mmessage, $messageid, $micon, $mviewed) = split(/\|/, $msg);
                        $subject = $msub; $message = $mmessage;
                        print FILE "$msg|1\n";
                }
                else {
                        print FILE "$msg\n" ;
                }
        }
        unfile_lock(FILE);
        close(FILE);


                $ranking = $memset[6]+$memset[11]+$memset[12];

                $postinfo = qq~$msg{'021'} $memset[6]<br>
$msg{'022'} $memset[11]<br>
$msg{'023'} $memset[12]<br>
~;
                $viewd = qq~&nbsp;&nbsp;<a href="$cgi\?action=viewprofile&username=$musername"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $musername[$a]" border="0"></a>~;
                $memberinfo = "$membergroups[2]";
                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                if ($ranking > 25) {
                        $memberinfo = "$membergroups[3]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 50) {
                        $memberinfo = "$membergroups[4]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 75) {
                        $memberinfo = "$membergroups[5]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 100) {
                        $memberinfo = "$membergroups[6]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 250) {
                        $memberinfo = "$membergroups[7]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 500) {
                        $memberinfo = "$membergroups[8]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
                if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
                if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }
                $signature = "$memset[5]";
                $signature =~ s/\&\&/<br>/g;
                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;
                $memset[8] =~ s/\n//g;
                $memset[8] =~ s/\r//g;
                if ($memset[8] ne "") {
                        if (!($memset[8] =~ /\D/)) {
                                $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
                        }
                }
                $message = "$message\n$signature";
                if ($enable_ubbc) { imxdoubbc(); }
                if ($enable_smile) { imxdosmilies(); }
                $url = "";
                if ($memset[3] ne "\n" && $musername ne "$anonuser") {
                        $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
                }
                foreach $censor (@censored) {
                        $censor =~ s/\n//g;
                        ($word, $censored) = split(/\=/, $censor);
                        $message =~ s/$word/$censored/g;
                        $subject =~ s/$word/$censored/g;
                }

$memberpic ="";

                if ($musername ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                if ($micon eq "" || $micon eq "1") {$micon ="aicon"; }
}
if ($musername eq ""){$whoiam = $msg{'183'};}else{$whoiam = $from;}


if ($musername ne "$anonuser"){
open(FILE, "$datadir/log.dat");
file_lock(FILE);
@entries = <FILE>;
unfile_lock(FILE);
close(FILE);
 $foundit = 0;

foreach $curentry (@entries) {

                        $curentry =~ s/[\n\r]//g; ($name, $value) = split(/\|/, $curentry);
                  if ($name eq "$musername") {
$amionline = qq~<img src=$imagesurl/im/online.gif alt=$imx{'043'}>~; $foundit = 1; }
else { unless ($foundit == "1") { $amionline = qq~<img src=$imagesurl/im/offline.gif alt=$imx{'044'}>~;} }

}
}
                display_date($mdate); $mdate = $user_display_date;
                print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor="$prefthemecolor"><b>$msg{'049'}</b></td>
<td bgcolor="$prefthemecolor"><b>$msg{'037'}</b></td>
</tr>
<tr>
<td bgcolor="#ffffff" width="140" valign="top" rowspan="2">
$amionline  <b>$whoiam</b><br>
~;
if ($musername ne "" && $musername ne "$anonuser"){print qq~
<small>$memberinfo<br>
$star<br>
$postinfo<br>
<center>$memberpic
~;



print qq~
<br>

</center>
~;}
print qq~
</td>
<td bgcolor="#ffffff" valign="top">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td width="100%">
<img src="$imagesurl/im/$micon.gif">&nbsp;<b>$subject</b></td>
<td align="right" nowrap><b>$msg{'054'}</b> $mdate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
</td>
</tr>
<tr>
<td bgcolor="#ffffff">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td>~;
if ($musername ne "$anonuser" && $musername ne "") {print qq~$url~;
if ($hidemail eq "1" || $hidemail eq "" || $musername ne "") {
print qq~<a href="$cgi?action=anonemail&sendto=$memset[1]">~;
}
else {
print qq~<a href="mailto:$mail">~;
}
print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $musername" border="0"></a>$viewd$icq~;
}
print qq~</td><td align="right">~;
if ($musername ne "$anonuser" && $musername ne "") {print qq~
<a href="$cgi?action=imsend&num=$messageid&quote=1&to=$musername"><img src="$imagesurl/forum/quote.gif" alt="$msg{'056'}" border="0"></a>&nbsp;&nbsp;<a href="$cgi?action=imsend&to=$musername&num=$messageid"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>&nbsp;&nbsp;~;
}
print qq~<a href="$cgi?action=imremove&id=$messageid"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>
</tr>
</table>
</td>
</tr>
<tr class=helpsnavtable><td colspan=3 align=right><b><a href=$cgi?action=im>$imx{'007'}</a></b></td></tr>

</table>

</td>
</tr>
</table>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
~;
        open(FILE, "$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        chomp(@folders = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        foreach $folderlist (@folders) {
                chomp($folderlist);
                ($name, $link) = split(/\|/, $folderlist);
                if ($info{'messageid'} eq $link) { $sel = "selected"; }
                else { $sel = ""; }
                $folderdropdown = qq~$folderdropdown\n<option value="$name" $sel>$name~;
        }
        if ($memset[1] ne "$anonuser" && $memset[1] ne "") {print qq~
<form action="$pageurl/$cgi?action=moveim" method="post" onSubmit="submitonce(this)">

<tr>
<td colspan=2 align=right bgcolor=$prefthemecolor>
<b>$msg{'151'} </b><select name="tocat">
<option value="saved" selected>$imx{'034'}</option>
$folderdropdown
</select>
<input type="hidden" name="topic" value="$info{'messageid'}">
<input type="hidden" name="whatfolder2" value="$folder">
<input type="submit" value="$btn{'016'}"><br>
<input type=hidden value=$folder name=folder></td>
</tr>
</form> ~;}
print qq~

</table><br>
<br><br>
~;
}


#############
sub oldimview {
#############
  if ($username eq "$anonuser") { error("noguests"); }
        if ($info{'from'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        $to = $info{"from"};

        open(FILE, "$memberdir/$to.dat");
        file_lock(FILE);
        @memset = <FILE>;
        unfile_lock(FILE);
        close(FILE);

                open(FILE, ">$memberdir/$username.msg");
                file_lock(FILE);
                foreach $msg (@imessages) {
                chomp $msg;
                ($t, $t, $t, $t, $messageid1, $t, $t) = split(/\|/, $msg);
                if ($umessageid == $messageid1) {
                        ($musername, $msub, $mdate, $mmessage, $messageid, $micon, $mviewed) = split(/\|/, $msg);
                        $subject = $msub; $message = $mmessage;
                        if ($mviewed ne "1") {
                       print FILE "$msg|1\n";
                 }
                 else {
                       print FILE "$msg\n" ;
                 }

        }
        }
        unfile_lock(FILE);
        close(FILE);


                $ranking = $memset[6]+$memset[11]+$memset[12];

                $postinfo = qq~<small>$msg{'021'} $memset[6]<br>
$msg{'022'} $memset[11]<br>
$msg{'023'} $memset[12]</small><br>
~;
                $viewd = qq~&nbsp;&nbsp;<a href="$cgi\?action=viewprofile&username=$musername"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $musername" border="0"></a>~;
                $memberinfo = "$membergroups[2]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                if ($ranking > 25) {
                        $memberinfo = "$membergroups[3]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 50) {
                        $memberinfo = "$membergroups[4]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 75) {
                        $memberinfo = "$membergroups[5]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 100) {
                        $memberinfo = "$membergroups[6]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 250) {
                        $memberinfo = "$membergroups[7]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 500) {
                        $memberinfo = "$membergroups[8]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
                if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
                if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }

                $signature = "$memset[5]";
                $signature =~ s/\&\&/<br>/g;
                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;
                $memset[8] =~ s/\n//g;
                $memset[8] =~ s/\r//g;
                if ($memset[8] ne "") {
                        if (!($memset[8] =~ /\D/)) {
                                $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
                        }
                }
                $message = "$message\n$signature";

                if ($enable_ubbc) { imxdoubbc(); }
                if ($enable_smile) { imxdosmilies(); }

                $url = "";
                if ($memset[3] ne "\n" && $musername ne "$anonuser") {
                        $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
                }

                foreach $censor (@censored) {
                        $censor =~ s/\n//g;
                        ($word, $censored) = split(/\=/, $censor);
                        $message =~ s/$word/$censored/g;
                        $subject =~ s/$word/$censored/g;
                }
        $memberpic ="";

                if ($musername ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                }




                display_date($mdate); $mdate = $user_display_date;
                print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="0" cellpadding="2">
<tr bgcolor=#FFFFFF><td colspan=2 align=right valign=bottom><font color=navy><b><a href=$cgi?action=im>$imx{'007'}</a></font></b></td></tr>
<tr>
<td class="forumwindow1"><b><u>$msg{'006'}</u></b></td>
<td class="forumwindow1"><b><u>$msg{'037'}</u></b></td>
</tr>

<td bgcolor="#ffffff" width="20%" valign="top" rowspan="2">
<b><font color=red face=Helvetica size=4>~;if ($memset[1] eq ""){print qq~$imx{'029'}~;}else{print qq~$memset[1]~;}
print qq~
</font></b>
~;
if ($memset[1] eq ""){ print qq~ &nbsp ~;} else {
print qq~
<br>$memberinfo
<br>
$star
<br>
$postinfo
<br><center>$memberpic
~;
}

open(FILE, "$datadir/log.dat");
file_lock(FILE);
@entries = <FILE>;
unfile_lock(FILE);
close(FILE);

@entries = (sort { lc($a) cmp lc($b) } @entries);

                 foreach $lline (@entries){
                       ($lname,$dummy,$dummy) = split(/\|/, $lline);
                       if($lname eq "$to"){
                       $lstat = "<div align=center><iframe id=frame src=http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi width=150 height=350 marginwidth=0 marginheight=0 hspace= vspace=0 frameborder=0 scrolling=no></iframe>
<Br><a href=javascript:loadwindow('http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi',190,310)>Notas Instantaneas</a></div>";
                       $amionline = "<font color=green><h4>$imx{'043'}</h4></font><br>";}
                             else {
$lstat = "";
$amionline = "<font color=red><h4>$imx{'044'}</h4></font><br>";}
}
if ($memset[1] ne ""){
print qq~
$amionline
~;}
print qq~
<br>

</center>
</td>
<td bgcolor="#FFFFFF" valign="top" width=100%>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td width="100%">&nbsp;<b><font face=Helvetica size=4>~;if ($micon ne "1" && $memset[1] ne ""){print qq~
<img src="$imagesurl/im/$micon.gif">&nbsp; ~;}else{print qq~
<img src="$imagesurl/im/aicon1.gif">&nbsp; ~;} print qq~$subject</b></font></td>
<td align="right" nowrap><b>$msg{'054'}</b> $mdate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message

</td>
</tr>
<tr>
<td class=menutable valign=top>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td>~;
if ($musername ne "$anonuser" && $memset[1] ne "") {print qq~$url~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~<a href="$cgi?action=anonemail&sendto=$musername">~;
}
else {
print qq~<a href="mailto:$mail">~;
}
print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $musername" border="0"></a>$viewd$icq~;
}
print qq~</td><td align="right">~;

if ($memset[1] ne "$anonuser" && $memset[1] ne "") {print qq~
<a href="$cgi?action=imsend&num=$messageid&quote=1&to=$musername"><img src="$imagesurl/forum/quote.gif" alt="$msg{'056'}" border="0"></a>&nbsp;&nbsp;<a href="$cgi?action=imsend&to=$musername&num=$messageid"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>~;}
print qq~
<a href="$cgi?action=imremove&id=$messageid"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>
</tr>

</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
~;
        open(FILE, "$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        chomp(@folders = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        foreach $folderlist (@folders) {
                chomp($folderlist);
                ($name, $link) = split(/\|/, $folderlist);
                if ($info{'messageid'} eq $link) { $sel = "selected"; }
                else { $sel = ""; }
                $folderdropdown = qq~$folderdropdown\n<option value="$name" $sel>$name~;
        }
        if ($memset[1] ne "$anonuser" && $memset[1] ne "") {print qq~
<form action="$pageurl/$cgi?action=moveim" method="post" onSubmit="submitonce(this)">
<tr class=boardtitle>
<td colspan=2 align=right>
$msg{'151'} <select name="tocat">
<option value="saved" selected>$imx{'034'}</option>
$folderdropdown
</select>
<input type="hidden" name="topic" value="$info{'messageid'}">
<input type="hidden" name="whatfolder" value="inbox">
<input type="submit" value="$btn{'016'}"></td>
</tr>
</form> ~;}
print qq~

</table><br>
<table width=100%><tr><td><hr></td></tr></table><br>
~;
}

#############
sub imuserview {
#############
  if ($username eq "$anonuser") { error("noguests"); }
        if ($info{'from'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        $to = $info{"from"};

        open(FILE, "$memberdir/$to.dat");
        file_lock(FILE);
        @memset = <FILE>;
        unfile_lock(FILE);
        close(FILE);

                open(FILE, ">$memberdir/$myuser.msg");
                file_lock(FILE);
                foreach $msg (@imessages) {
                chomp $msg;
                ($t, $t, $t, $t, $messageid1, $t, $t) = split(/\|/, $msg);
                if ($umessageid == $messageid1) {
                        ($musername, $msub, $mdate, $mmessage, $messageid, $micon, $mviewed) = split(/\|/, $msg);
                        $subject = $msub; $message = $mmessage;
                        if ($mviewed ne "1") {
                       print FILE "$msg|1\n";
                 }
                 else {
                       print FILE "$msg\n" ;
                 }
                }
        }
        unfile_lock(FILE);
        close(FILE);


                $ranking = $memset[6]+$memset[11]+$memset[12];

                $postinfo = qq~<small>$msg{'021'} $memset[6]<br>
$msg{'022'} $memset[11]<br>
$msg{'023'} $memset[12]</small><br>
~;
                $viewd = qq~&nbsp;&nbsp;<a href="$cgi\?action=viewprofile&username=$musername"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $musername" border="0"></a>~;
                $memberinfo = "$membergroups[2]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                if ($ranking > 25) {
                        $memberinfo = "$membergroups[3]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 50) {
                        $memberinfo = "$membergroups[4]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 75) {
                        $memberinfo = "$membergroups[5]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 100) {
                        $memberinfo = "$membergroups[6]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 250) {
                        $memberinfo = "$membergroups[7]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 500) {
                        $memberinfo = "$membergroups[8]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
                if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
                if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }

                $signature = "$memset[5]";
                $signature =~ s/\&\&/<br>/g;
                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;
                $memset[8] =~ s/\n//g;
                $memset[8] =~ s/\r//g;
                if ($memset[8] ne "") {
                        if (!($memset[8] =~ /\D/)) {
                                $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
                        }
                }
                $message = "$message\n$signature";

                if ($enable_ubbc) { imxdoubbc(); }
                if ($enable_smile) { imxdosmilies(); }

                $url = "";
                if ($memset[3] ne "\n" && $musername ne "$anonuser") {
                        $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
                }

                foreach $censor (@censored) {
                        $censor =~ s/\n//g;
                        ($word, $censored) = split(/\=/, $censor);
                        $message =~ s/$word/$censored/g;
                        $subject =~ s/$word/$censored/g;
                }
        $memberpic ="";

                if ($musername ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                }




                display_date($mdate); $mdate = $user_display_date;
                print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="0" cellpadding="2">
<tr bgcolor=#FFFFFF><td colspan=2 align=right valign=bottom><font color=navy><b><a href=$cgi?action=im>$imx{'007'}</a></font></b></td></tr>
<tr>
<tr>
<td class="forumwindow1"><b><u>$msg{'006'}</u></b></td>
<td class="forumwindow1"><b><u>$msg{'037'}</u></b></td>
</tr>

<td bgcolor="#ffffff" width="20%" valign="top" rowspan="2">
<b><font color=red face=Helvetica size=4>~;if ($memset[1] eq ""){print qq~$imx{'029'}~;}else{print qq~$memset[1]~;}
print qq~
</font></b>
~;
if ($memset[1] eq ""){ print qq~ &nbsp ~;} else {
print qq~
<br>$memberinfo
<br>
$star
<br>
$postinfo
<br><center>$memberpic

~;

}
print qq~</center>
</td>
<td bgcolor="#FFFFFF" valign="top" width=100%>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td width="100%">&nbsp;<b><font face=Helvetica size=4>~;if ($micon ne "1" && $memset[1] ne ""){print qq~
<img src="$imagesurl/im/$micon.gif">&nbsp; ~;}else{print qq~
<img src="$imagesurl/im/aicon1.gif">&nbsp; ~;} print qq~$subject</b></font></td>
<td align="right" nowrap><b>$msg{'054'}</b> $mdate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
</td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
<tr class=menutable>
<td>~;
if ($musername ne "$anonuser" && $memset[1] ne "") {print qq~$url~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~<a href="$cgi?action=anonemail&sendto=$musername">~;
}
else {
print qq~<a href="mailto:$mail">~;
}
print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $musername" border="0"></a>$viewd$icq~;
}
print qq~</td><td align="right">~;

if ($memset[1] ne "$anonuser" && $memset[1] ne "") {print qq~
<a href="$cgi?action=imsend&num=$messageid&quote=1&to=$musername"><img src="$imagesurl/forum/quote.gif" alt="$msg{'056'}" border="0"></a>&nbsp;&nbsp;<a href="$cgi?action=imsend&to=$musername&num=$messageid"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>~;}
print qq~
<a href="$cgi?action=imremove&id=$messageid"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>
</tr>

</table>
</td>
</tr>
</table>
</td>
</tr>
</table>

<table width=100%><tr><td><hr></td></tr></table><br>
~;
}
#############
sub imview2 {
#############
  if ($username eq "$anonuser") { error("noguests"); }
        #if ($info{'to'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        $to = $info{"to"};

        open(FILE, "$memberdir/$to.dat");
        file_lock(FILE);
        @memset = <FILE>;
        unfile_lock(FILE);
        close(FILE);

                open(FILE, ">$memberdir/backup/$username.msg");
                file_lock(FILE);
                foreach $msg (@imessages) {
                chomp $msg;
                ($t, $t, $t, $t, $messageid1, $t, $t, $t) = split(/\|/, $msg);
                if ($umessageid == $messageid1) {
                        ($musername, $msub, $mdate, $mmessage, $messageid, $recipient, $micon, $mviewed) = split(/\|/, $msg);
                        $subject = $msub; $message = $mmessage;
                        print FILE "$msg|1\n";
                }
                else {
                        print FILE "$msg\n" ;
                }

}
        unfile_lock(FILE);
        close(FILE);


                $ranking = $memset[6]+$memset[11]+$memset[12];

                $postinfo = qq~<small>$msg{'021'} $memset[6]<br>
$msg{'022'} $memset[11]<br>
$msg{'023'} $memset[12]</small><br>
~;
                $viewd = qq~&nbsp;&nbsp;<a href="$cgi\?action=viewprofile&username=$recipient"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $recipient" border="0"></a>~;
                        $memberinfo = "$membergroups[2]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                if ($ranking > 25) {
                        $memberinfo = "$membergroups[3]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 50) {
                        $memberinfo = "$membergroups[4]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 75) {
                        $memberinfo = "$membergroups[5]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 100) {
                        $memberinfo = "$membergroups[6]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 250) {
                        $memberinfo = "$membergroups[7]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 500) {
                        $memberinfo = "$membergroups[8]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
                if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
                if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }
                $signature = "$memset[5]";
                $signature =~ s/\&\&/<br>/g;
                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;
                $memset[8] =~ s/\n//g;
                $memset[8] =~ s/\r//g;
                if ($memset[8] ne "") {
                        if (!($memset[8] =~ /\D/)) {
                                $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
                        }
                }
                $message = "$message\n$signature";

                if ($enable_ubbc) { imxdoubbc(); }
                if ($enable_smile) { imxdosmilies(); }

                $url = "";
                if ($memset[3] ne "\n" && $musername ne "$anonuser") {
                        $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
                }

                foreach $censor (@censored) {
                        $censor =~ s/\n//g;
                        ($word, $censored) = split(/\=/, $censor);
                        $message =~ s/$word/$censored/g;
                        $subject =~ s/$word/$censored/g;
                }
        $memberpic ="";

                        if ($musername ne "$anonuser") {
                        if ($memset[9] eq "") {$memset[9] eq "_nopic.gif";}
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                }



                display_date($mdate); $mdate = $user_display_date;
                print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor=$prefthemecolor><b><u>$msg{'006'}</u></b></td>
<td bgcolor=$prefthemecolor><b><u>$msg{'037'}</u></b></td>
</tr>
<tr>
<td bgcolor="#ffffff" width="140" valign="top" rowspan="2">
<b><font color=red face=Helvetica size=4>$memset[1]</font></b>
~;
if ($memset[1] eq ""){ print qq~ &nbsp ~;} else {
print qq~
<br>$memberinfo
<br>
$star
<br>
$postinfo
<br><center>$memberpic
~;
}

open(FILE, "$datadir/log.dat");
file_lock(FILE);
@entries = <FILE>;
unfile_lock(FILE);
close(FILE);

@entries = (sort { lc($a) cmp lc($b) } @entries);

                 foreach $lline (@entries){
                       ($lname,$dummy,$dummy) = split(/\|/, $lline);
                       if($lname eq "$to"){
                       $lstat = "<div align=center><iframe id=frame src=http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi width=150 height=350 marginwidth=0 marginheight=0 hspace= vspace=0 frameborder=0 scrolling=no></iframe>
<Br><a href=javascript:loadwindow('http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi',190,310)>Notas Instantaneas</a></div>";
                       $amionline = "<font color=green><h4>$imx{'043'}</h4></font><br>";}
                             else {
$lstat = "";
$amionline = "<font color=red><h4>$imx{'044'}</h4></font><br>";}
}
if ($memset[1] ne ""){
print qq~
$amionline
~;}
print qq~
<br>


</center>

</td>
<td bgcolor="#FFFFFF" valign="top">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td width="100%">&nbsp;<b><font face=Helvetica size=4>~;if ($micon ne "1"){print qq~
<img src="$imagesurl/im/$micon.gif">&nbsp; ~;}else{print qq~
<img src="$imagesurl/im/aicon.gif">&nbsp; ~;} print qq~$subject</b></font></td>
<td align="right" nowrap><b>$msg{'054'}</b> $mdate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message

</td>
</tr>
<tr>
<td>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td bgcolor=white>~;
if ($musername ne "$anonuser") {print qq~$url~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~<a href="$cgi?action=anonemail&sendto=$recipient">~;
}
else {
print qq~<a href="mailto:$mail">~;
}
print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $recipient" border="0"></a>$viewd$icq~;
}
print qq~</td><td align="right" bgcolor=white>~;

print qq~<a href="$cgi?action=imremove2&id=$messageid"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>
</tr>
<tr class=menutable><td colspan=2 align=right><font color=navy><b><a href=$cgi?action=imfolder>$imx{'007'}</a></font></b></td></tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
<tr><td colspan=2 bgcolor=$prefthemecolor height=2></td></tr>
</table>
<br>
<br><br>
<table width=100%><tr><td class=forumwindow1><hr></td></tr></table><br><br>
~;
}

#############
sub imview3 {
#############

  if ($username eq "$anonuser") { error("noguests"); }
        #if ($info{'from'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        $to = $info{"from"};

        open(FILE, "$memberdir/$to.dat");
        file_lock(FILE);
        @memset = <FILE>;
        unfile_lock(FILE);
        close(FILE);

                open(FILE, ">$memberdir/saved/$username.msg");
                file_lock(FILE);
                foreach $msg (@imessages) {
                chomp $msg;
                ($t, $t, $t, $t, $messageid1, $t) = split(/\|/, $msg);
                if ($umessageid == $messageid1) {
                        ($musername, $msub, $mdate, $mmessage, $messageid, $micon, $mviewed) = split(/\|/, $msg);
                        $subject = $msub; $message = $mmessage;
                        print FILE "$msg|1\n";
                }
                else {
                        print FILE "$msg\n" ;
                }
        }
        unfile_lock(FILE);
        close(FILE);


                $ranking = $memset[6]+$memset[11]+$memset[12];

                $postinfo = qq~<small>$msg{'021'} $memset[6]<br>
$msg{'022'} $memset[11]<br>
$msg{'023'} $memset[12]</small><br>
~;
                $viewd = qq~&nbsp;&nbsp;<a href="$cgi\?action=viewprofile&username=$musername"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $musername" border="0"></a>~;
                        $memberinfo = "$membergroups[2]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                                if ($ranking > 25) {
                        $memberinfo = "$membergroups[3]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 50) {
                        $memberinfo = "$membergroups[4]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 75) {
                        $memberinfo = "$membergroups[5]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 100) {
                        $memberinfo = "$membergroups[6]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 250) {
                        $memberinfo = "$membergroups[7]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 500) {
                        $memberinfo = "$membergroups[8]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
                if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
                if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }
                $signature = "$memset[5]";
                $signature =~ s/\&\&/<br>/g;
                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;
                $memset[8] =~ s/\n//g;
                $memset[8] =~ s/\r//g;
                if ($memset[8] ne "") {
                        if (!($memset[8] =~ /\D/)) {
                                $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
                        }
                }
                $message = "$message\n$signature";

                if ($enable_ubbc) { imxdoubbc(); }
                if ($enable_smile) { imxdosmilies(); }

                $url = "";
                if ($memset[3] ne "\n" && $musername ne "$anonuser") {
                        $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
                }

                foreach $censor (@censored) {
                        $censor =~ s/\n//g;
                        ($word, $censored) = split(/\=/, $censor);
                        $message =~ s/$word/$censored/g;
                        $subject =~ s/$word/$censored/g;
                }
        $memberpic ="";

                                if ($musername ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                }



                display_date($mdate); $mdate = $user_display_date;
                print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor=$prefthemecolor><b><u>$msg{'006'}</u></b></td>
<td bgcolor=$prefthemecolor><b><u>$msg{'037'}</u></b></td>
</tr>
<tr>
<td bgcolor="#ffffff" width="140" valign="top" rowspan="2">
<b><font color=red face=Helvetica size=4>$memset[1]</font></b>
~;
if ($memset[1] eq ""){ print qq~ &nbsp ~;} else {
print qq~
<br>$memberinfo
<br>
$star
<br>
$postinfo
<br><center>$memberpic
<br>
~;
}

open(FILE, "$datadir/log.dat");
file_lock(FILE);
@entries = <FILE>;
unfile_lock(FILE);
close(FILE);

@entries = (sort { lc($a) cmp lc($b) } @entries);

                 foreach $lline (@entries){
                       ($lname,$dummy,$dummy) = split(/\|/, $lline);
                       if($lname eq "$to"){
                       $lstat = "<div align=center><iframe id=frame src=http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi width=150 height=350 marginwidth=0 marginheight=0 hspace= vspace=0 frameborder=0 scrolling=no></iframe>
<Br><a href=javascript:loadwindow('http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi',190,310)>Notas Instantaneas</a></div>";
                       $amionline = "<font color=green><h4>$imx{'043'}</h4></font><br>";}
                             else {
$lstat = "";
$amionline = "<font color=red><h4>$imx{'044'}</h4></font><br>";}
}
if ($memset[1] ne ""){
print qq~
$amionline
~;}
print qq~


</center>

</td>
<td bgcolor="#FFFFFF" valign="top">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td width="100%">&nbsp;<b><font face=Helvetica size=4>~;if ($micon ne "1"){print qq~
<img src="$imagesurl/im/$micon.gif">&nbsp; ~;}else{print qq~
<img src="$imagesurl/im/aicon.gif">&nbsp; ~;} print qq~$subject</b></font></td>
<td align="right" nowrap><b>$msg{'054'}</b> $mdate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
</td>
</tr>
<tr>
<td class="forumwindow1">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td bgcolor=white>~;
if ($musername ne "$anonuser") {print qq~$url~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~<a href="$cgi?action=anonemail&sendto=$musername">~;
}
else {
print qq~<a href="mailto:$mail">~;
}
print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $musername" border="0"></a>$viewd$icq~;
}
print qq~</td><td align="right" bgcolor=white>~;

if ($musername ne "$anonuser") {print qq~
<a href="$cgi?action=imsend&to=$musername&num=$messageid"><img src="$imagesurl/forum/replymsg.gif" alt="$msg{'057'}" border="0"></a>
~;}
print qq~<a href="$cgi?action=imremove3&id=$messageid"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>
</tr>
<tr class=menutable><td colspan=2 align=right><font color=navy><b><a href=$cgi?action=saveim>$imx{'007'}</a></font></b></td></tr>

</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
~;
        open(FILE, "$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        chomp(@folders = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        foreach $folderlist (@folders) {
                chomp($folderlist);
                ($name, $link) = split(/\|/, $folderlist);
                if ($info{'messageid'} eq $link) { $sel = "selected"; }
                else { $sel = ""; }
                $folderdropdown = qq~$folderdropdown\n<option value="$name" $sel>$name~;
        }
        if ($memset[1] ne "$anonuser" && $memset[1] ne "") {print qq~
<form action="$pageurl/$cgi?action=moveim3" method="post" onSubmit="submitonce(this)">
<tr>
<td colspan=2 align=right bgcolor=$prefthemecolor>
<b>$msg{'151'} </b><select name="tocat">
$folderdropdown
</select>
<input type="hidden" name="topic" value="$info{'messageid'}">
<input type="hidden" name="whatfolder" value="saved">
<input type="submit" value="$btn{'016'}"></td>
</tr>
</form> ~;}
print qq~

</table><br>
<br><br>
<table width=100%><tr><td class=forumwindow1><hr></td></tr></table><br><br>
~;
}





#############
sub imview4 {
#############

  if ($username eq "$anonuser") { error("noguests"); }
        if ($info{'from'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

        $to = $info{"from"};
        $folder = $info{'folder'};
        open(FILE, "$memberdir/$to.dat");
        file_lock(FILE);
        @memset = <FILE>;
        unfile_lock(FILE);
        close(FILE);

                open(FILE, ">$memberdir/adminim/$username/$folder/$username.msg");
                file_lock(FILE);
                foreach $msg (@imessages) {
                chomp $msg;
                ($t, $t, $t, $t, $messageid1, $t) = split(/\|/, $msg);
                if ($umessageid == $messageid1) {
                        ($musername, $msub, $mdate, $mmessage, $messageid, $micon, $mviewed) = split(/\|/, $msg);
                        $subject = $msub; $message = $mmessage;
                        print FILE "$msg|1\n";
                }
                else {
                        print FILE "$msg\n" ;
                }
        }
        unfile_lock(FILE);
        close(FILE);


                $ranking = $memset[6]+$memset[11]+$memset[12];

                $postinfo = qq~<small>$msg{'021'} $memset[6]<br>
$msg{'022'} $memset[11]<br>
$msg{'023'} $memset[12]</small><br>
~;
                $viewd = qq~&nbsp;&nbsp;<a href="$cgi\?action=viewprofile&username=$musername"><img src="$imagesurl/forum/profile.gif" alt="$msg{'051'} $musername" border="0"></a>~;
                        $memberinfo = "$membergroups[2]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                                if ($ranking > 25) {
                        $memberinfo = "$membergroups[3]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 50) {
                        $memberinfo = "$membergroups[4]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 75) {
                        $memberinfo = "$membergroups[5]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 100) {
                        $memberinfo = "$membergroups[6]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 250) {
                        $memberinfo = "$membergroups[7]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 500) {
                        $memberinfo = "$membergroups[8]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
                if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
                if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }
                $signature = "$memset[5]";
                $signature =~ s/\&\&/<br>/g;
                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;
                $memset[8] =~ s/\n//g;
                $memset[8] =~ s/\r//g;
                if ($memset[8] ne "") {
                        if (!($memset[8] =~ /\D/)) {
                                $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
                        }
                }
                $message = "$message\n$signature";

                if ($enable_ubbc) { imxdoubbc(); }
                if ($enable_smile) { imxdosmilies(); }

                $url = "";
                if ($memset[3] ne "\n" && $musername ne "$anonuser") {
                        $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
                }

                foreach $censor (@censored) {
                        $censor =~ s/\n//g;
                        ($word, $censored) = split(/\=/, $censor);
                        $message =~ s/$word/$censored/g;
                        $subject =~ s/$word/$censored/g;
                }
        $memberpic ="";

                                if ($musername ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }
                }



                display_date($mdate); $mdate = $user_display_date;
                print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor=$prefthemecolor><b><u>$msg{'006'}</u></b></td>
<td bgcolor=$prefthemecolor><b><u>$msg{'037'}</u></b></td>
</tr>
<tr>
<td bgcolor="#ffffff" width="140" valign="top" rowspan="2">
<b><font color=red face=Helvetica size=4>$memset[1]</font></b>
~;
if ($memset[1] eq ""){ print qq~ &nbsp ~;} else {
print qq~
<br>$memberinfo
<br>
$star
<br>
$postinfo
<br><center>$memberpic
~;
}

open(FILE, "$datadir/log.dat");
file_lock(FILE);
@entries = <FILE>;
unfile_lock(FILE);
close(FILE);

@entries = (sort { lc($a) cmp lc($b) } @entries);

                 foreach $lline (@entries){
                       ($lname,$dummy,$dummy) = split(/\|/, $lline);
                       if($lname eq "$to"){
                       $lstat = "<div align=center><iframe id=frame src=http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi width=150 height=350 marginwidth=0 marginheight=0 hspace= vspace=0 frameborder=0 scrolling=no></iframe>
<Br><a href=javascript:loadwindow('http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi',190,310)>Notas Instantaneas</a></div>";
                       $amionline = "<font color=green><h4>$imx{'043'}</h4></font><br>";}
                             else {
$lstat = "";
$amionline = "<font color=red><h4>$imx{'044'}</h4></font><br>";}
}
if ($memset[1] ne ""){
print qq~
$amionline
~;}
print qq~


</center>

</td>
<td bgcolor="#FFFFFF" valign="top">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td width="100%">&nbsp;<b><font face=Helvetica size=4>~;if ($micon ne "1"){print qq~
<img src="$imagesurl/im/$micon.gif">&nbsp; ~;}else{print qq~
<img src="$imagesurl/im/aicon.gif">&nbsp; ~;} print qq~$subject</b></font></td>
<td align="right" nowrap><b>$msg{'054'}</b> $mdate</td>
</tr>
</table>
<hr noshade="noshade" size="1">
$message
</td>
</tr>
<tr>
<td class="forumwindow1">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td bgcolor=white>~;
if ($musername ne "$anonuser") {print qq~$url~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~<a href="$cgi?action=anonemail&sendto=$musername">~;
}
else {
print qq~<a href="mailto:$mail">~;
}
print qq~<img src="$imagesurl/forum/email.gif" alt="$msg{'055'} $musername" border="0"></a>$viewd$icq~;
}
print qq~</td><td align="right" bgcolor=white>~;


print qq~<a href="$cgi?action=imremove4&id=$messageid&folder=$folder"><img src="$imagesurl/forum/delete.gif" alt="$msg{'058'}" border="0"></a></td>
</tr>
<tr class=menutable><td colspan=2 align=right><font color=navy><b><a href=$cgi?action=messagefolder&folder=$folder>$imx{'007'}</a></font></b></td></tr>

</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<table border="0" width="100%" cellpadding="0" cellspacing="0">
~;
        open(FILE, "$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        chomp(@folders = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        foreach $folderlist (@folders) {
                chomp($folderlist);
                ($name, $link) = split(/\|/, $folderlist);
                if ($info{'messageid'} eq $link) { $sel = "selected"; }
                else { $sel = ""; }
                $folderdropdown = qq~$folderdropdown\n<option value="$name" $sel>$name~;
        }
        if ($memset[1] ne "$anonuser" && $memset[1] ne "") {print qq~
<form action="$pageurl/$cgi?action=moveim4" method="post" onSubmit="submitonce(this)">

<tr>
<td colspan=2 align=right bgcolor=$prefthemecolor>
<b>$msg{'151'} </b><select name="tocat">
<option value="saved" selected>$imx{'034'}</option>
$folderdropdown
</select>
<input type="hidden" name="topic" value="$info{'messageid'}">
<input type="hidden" name="whatfolder2" value="$folder">
<input type="submit" value="$btn{'016'}"><br>
<input type=hidden value=$folder name=folder></td>
</tr>
</form> ~;}
print qq~

</table><br>
<br><br>
<table width=100%><tr><td class=forumwindow1><hr></td></tr></table><br><br>
~;
}


##################
# post subs     #
##################

###################
sub showcontactlist1  {
##################
print qq~
<table width=100% cellspacing="0" cellpadding="0">
<tr class="menutable"><td align=center><b>$imx{'045'}</b></td></tr></table>~;


unless (-e("$memberdir/adminim/contact"))
{
   mkdir("$memberdir/adminim/contact",0755);
   chmod(0755,"$memberdir/adminim/contact");
}

open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) {

        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $themegif, $themecolor, $image, $contactnum) = split(/\|/, $curentry);}


open(FILE, "<$memberdir/adminim/contact/$username.lst");
file_lock(FILE);
chomp(@mycontact = <FILE>);
unfile_lock(FILE);
close(FILE);
$countcontact = @mycontact;



if ($contactnum eq ""){$contactnum = 5;}

@mycontact = (sort { lc($a) cmp lc($b) }@mycontact);
if (@mycontact <= $contactnum){
for ($a = 0; $a < @mycontact; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);

print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
else {
                for ($a = 0; $a < $contactnum; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);
print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
print qq~<br>
 </td></tr>
<tr><td></td></tr>
<tr><td></td></tr>
</table>~;

}

############
sub impost {
############
if ($username eq "$anonuser") { error("$err{'011'}"); }

$mid = time;

        open(FILE, "$memberdir/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

         if ($info{'subject'} ne "") {
           $form_subject = $info{'subject'};
     }

     if ($info{'msg'} ne "") {
           $form_message = $info{'msg'};
     }

        if ($info{'num'} ne "") {
                foreach $line (@imessages) {
                        ($mfrom, $msubject, $mdate, $mmessage, $messageid) = split(/\|/, $line);
                        if ($info{'num'} eq $messageid) {
                                $msubject =~ s/Re: //g;
                                $form_subject = "Re: $msubject";
                                $msg = $mmessage;
                        }
                }
                if ($info{'quote'} == 1) {
                        $form_message =~ s/\[quote\](\S+?)\[\/quote\]//isg;
                        $form_message =~ s/\[(\S+?)\]//isg;
                        $mmessage = htmltotext($msg);
                        $form_message = "\n\n\[quote\]$mmessage\[/quote\]";
                }
        }

        open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) {

        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $themegif, $themecolor, $imximage, $contactnum) = split(/\|/, $curentry);}

        $mytopbar = "$imx{'014'}";
        $navbar = "$btn{'014'} $nav{'029'}";
        print_top();
        mytopbar3();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign=top>
<form action="$cgi?action=imsend2" name=creator method="post">
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top width=75%>
<table width=100% cellspacing="0" cellpadding="0"><tr class="menutable"><td align=center colspan=2><b>$imx{'014'}</b></td></tr></table>

<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="0" cellpadding=2 width=100%>

<tr bgcolor=#FFFFFF>
<td><b>Logon as: </b></td><td colspan=2><b> $username </b>~;if ($username ne "$anonuser"){print qq~
<a href=$pageurl/$cgi?action=logout><small>[$imx{'015'}]</small></a>~;}else{print qq~
<a href=$pageurl/$cgi?action=register><small>[$imx{'016'}]</small></a>~;}
print qq~

</td></tr>

<tr class="boardtitle">
<td><b>TO:</b></td>
~;
        if ($info{'to'} ne "") {
                print qq~<td valign=bottom><input type="text" name="to" value="$info{'to'}" size="28">~;
        }
        else {
                print qq~<td valign=bottom><select name="to">
~;
                open(MEM, "$memberdir/memberlist.dat");
                file_lock(MEM);
                @members = <MEM>;
                unfile_lock(MEM);
                close(MEM);
                @members = (sort { lc($a) cmp lc($b) } @members);
                for ($i = 0; $i < @members; $i++) {
                        $members[$i] =~ s/\n//g;
                        if ($members[$i] ne $username) {
if ($members[$i] ne "admin") {
if ($members[$i] ne "admin2") {
print qq~<option value="$members[$i]">$members[$i]</option>\n~;
}
}
}
                }
        print qq~</select>
~;
        }
        print qq~</td><td><b>BCC:</b> &nbsp;&nbsp;<input type="text" name="cc" value="$info{'cc'}" size="28">*</td></tr>

<tr class="forumtitlebackcolor">
<td><b>$msg{'037'}</b></td>
<td colspan=2><input type="text" name="subject" value="$form_subject" size="60" maxlength="50"></td>
</tr>
<tr class="boardtitle">
<td valign=top>
<b>$imx{'017'}:</b>
</td>
<td colspan=2>
<font size="1" face="Helvetica, Arial, Verdana">
   <input type="radio" name="icon" value="aicon2" CHECKED>&nbsp;
<img src="$imagesurl/im/aicon2.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="aicon1" >&nbsp;
<img src="$imagesurl/im/aicon1.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="icon3" >&nbsp;
<img src="$imagesurl/im/icon3.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="aicon4" >&nbsp;
<img src="$imagesurl/im/aicon4.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="aicon5" >&nbsp;
<img src="$imagesurl/im/aicon5.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="icon7" >&nbsp;
<img src="$imagesurl/im/icon7.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="aicon10" >&nbsp;
<img src="$imagesurl/im/aicon10.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;<br>
   <input type="radio" name="icon" value="aicon13" >&nbsp;
<img src="$imagesurl/im/aicon13.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="aicon14" >&nbsp;
<img src="$imagesurl/im/aicon14.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="icon1" >&nbsp;
<img src="$imagesurl/im/icon1.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="icon4" >&nbsp;
<img src="$imagesurl/im/icon4.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="icon5" >&nbsp;
<img src="$imagesurl/im/icon5.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="aicon9" >&nbsp;
<img src="$imagesurl/im/aicon9.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;
   <input type="radio" name="icon" value="icon10" >&nbsp;
<img src="$imagesurl/im/icon10.gif" height="15" width="15" align="middle" alt="">&nbsp;&nbsp;&nbsp;&nbsp;

</font>

</td>
</tr>
~;


if ($enable_ubbc eq "1") {print qq~

<script language="javascript" type="text/javascript">
<!-- #jeffcrawford ubbcfix, anon ubbc hack #


function AddText(NewCode) {
        if (document.creator.message.createTextRange && document.creator.message.caretPos) {
                var caretPos = document.creator.message.caretPos;
                caretPos.text = NewCode;
        } else {
                document.creator.message.value+=NewCode;
        }
        document.creator.message.focus();
}
function addCodeA(bCode1,bCode2) {
                var text = getText();
                AddTxt = bCode1 + text + bCode2;
                AddText(AddTxt);
}
function getText() {
        if (document.creator.message.createTextRange && document.creator.message.caretPos) {
                return document.creator.message.caretPos.text;
        } else {
                return '';
        }
}
function storeCaret(ftext) {
        if (ftext.createTextRange) {
                ftext.caretPos = document.selection.createRange().duplicate();
        }
}

function addCode(anystr) {
document.creator.message.value+=anystr;
}
function addCode2(anystr) {
document.creator.to.value+=anystr;
}
function showColor(color) {
document.creator.message.value+="[color="+color+"][/color]";
}
function showFont(font) {
document.creator.message.value+="[font="+font+"][/font]";
}
function showSize(size) {
document.creator.message.value+="[size="+size+"][/size]";
}
function upload() {
window.open("$pageurl/$cgi?action=uploadpicture","","width=300,height=150,scrollbars")
}
// -->
</script>


~;}
print qq~


</td>
</tr></table>

<table border="0" cellspacing="0" cellpadding="0" width=100%>
<tr class="boardtitle"><Td colspan=2 class=forumtitlebackcolor height=2>&nbsp;
</td></tr>
<tr class="boardtitle">
<td valign="top" width=15%>
~;
if ($enable_ubbc eq "1") {print qq~
<table><tr><td><b>$imx{'055'}:</b> </td><td><select name="color" onChange="showColor(this.options[this.selectedIndex].value)">
<option value="Black" selected>$msg{'127'}</option>
<option value="Red" style='color:red'>$msg{'128'}</option>
<option value="Yellow" style='color:yellow'>$msg{'129'}</option>
<option value="Pink" style='color:pink'>$msg{'130'}</option>
<option value="Green" style='color:green'>$msg{'131'}</option>
<option value="Orange" style='color:orange'>$msg{'132'}</option>
<option value="Purple" style='color:purple'>$msg{'133'}</option>
<option value="Blue" style='color:blue'>$msg{'134'}</option>
<option value="Beige" style='color:beige'>$msg{'135'}</option>
<option value="Brown" style='color:brown'>$msg{'136'}</option>
<option value="Teal" style='color:teal'>$msg{'137'}</option>
<option value="Navy" style='color:navy'>$msg{'138'}</option>
<option value="Maroon" style='color:maroon'>$msg{'139'}</option>
<option value="LimeGreen" style='color:limegreen'>$msg{'140'}</option>
</select></td></tr>
<tr><td>
<b>$imx{'056'}:</b> </td><td><select name="font" onChange="showFont(this.options[this.selectedIndex].value)">
<option value='Arial' style="font-family:Arial" selected>Arial</option>
<option value='Times New Roman' style="font-family:Times New Roman">Times New Roman</option>
<option value='Courier' style="font-family:Courier">Courier</option>
<option value='Impact' style="font-family:Impact">Impact</option>
<option value='Geneva' style="font-family:Geneva">Geneva</option>
<option value='Verdana' style="font-family:verdana">Verdana</option>
</select>
</td></tr>
<tr><td>
<b>$imx{'057'}:</b> </td><td><select name="size" onChange="showSize(this.options[this.selectedIndex].value)">
<option value='1'>$imx{'018'}</option>
<option value='3' selected>$imx{'019'}</option>
<option value='5'>$imx{'020'}</option>
<option value='7'>$imx{'021'}</option>
<option value='10'>$imx{'022'}</option>
</select></td></tr></table>~;
}
if ($imximage eq "1") {
print qq~<br>
<center><a href="javascript:upload()"><img src="$imagesurl/im/foto.gif" alt="" border=0><br><b>$msg{'598'}</b></a>
<br></center>~;}
print qq~
</td>
<td>

<input type=button onclick="javascript:addCodeA('[b]','[/b]')" value=" B ">

<input type=button onclick="javascript:addCodeA('[i]','[/i]')" value=" I ">

<input type=button onclick="javascript:addCodeA('[u]','[/u]')" value=" U ">

<input type=button onclick="javascript:addCodeA('[url]','[/url]')" value=" http:// ">

<input type=button onclick="javascript:addCodeA('[email]','[/email]')" value=" @ ">

<input type=button onclick="javascript:addCodeA('[img]','[/img]')" value=" IMG ">

<input type=button onclick="javascript:addCodeA('[quote]','[/quote]')" value=" $imx{'023'} "><br>
$msg{'038'}<br>
<textarea name="message" wrap=physical rows="8" cols="35" onselect="storeCaret(this);" onclick="storeCaret(this);" onkeyup="storeCaret(this);" onchange="storeCaret(this);">$form_message</textarea>

<br>
~;
imxsmilie();
print qq~
</td></tr>
<tr class="boardtitle">
<td colspan="2">
<input type="checkbox" name="copy_im"><small>$imx{'024'}</small>
<br>*<small><b>BCC</b>: $imx{'054'}</small>
</td>
<tr class="boardtitle">
<td colspan="2">

<input type="submit" class="button" name="impreview" value="$btn{'044'}">&nbsp;<input type="submit" class="button" value="$btn{'008'}">
<!-- <input type="reset" class="button" value="$btn{'009'}"> -->


</td></tr></table></form>
</td>
</td></tr></table>
</td><td valign=top>
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top>
~;
showcontactlist1();
print qq~
<br><br>
<center>
<table width=100%><tr class=menutable><td colspan=5 align=center><B>$imx{'045'} $imx{'047'}</b></td></tr>
<tr><td colspan=5>&nbsp;</td></tr>~;
blist();

print qq~
<tr><td colspan=5></td></tr>
<tr><td colspan=5 class=forumwindow1 align=right><a href="$pageurl/$cgi?action=contacts">$btn{'030'}</a><br><a href="$pageurl/$cgi?action=memberlist">$nav{'019'}</a></td></tr>

</table>
<p align=center>
~;

jumplist("sendim");

#<form name="jump">
#$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
#<option value="#">- $imx{'051'} -</option>~;

#open(FILE, "<$memberdir/adminim/folder/$username.txt");
#        file_lock(FILE);
#        my @folder = <FILE>;
#        unfile_lock(FILE);
#        close(FILE);
#        $imxmnum = @folder;
#        @folder = (sort { lc($a) cmp lc($b) } @folder);
# foreach $line (@folder) {
#           $line =~ s/[\n\r]//g;
#           @item = split(/\|/, $line);
#           if ($item[0] eq "") { }
#           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
#}
#print qq~
#<option value="$pageurl/$cgi?action=im">$imx{'001'}</option>
#<option value="$pageurl/$cgi?action=folder">$btn{'015'}</option>
#</select>
#</form>

print qq~
</p>
~;
imxversion();
print qq~</center>
</td></tr></table>
<br><br><Center><a href="$cgi?action=im">$nav{'102'}</a></center>~;

        print_bottom();
        exit;
}


#############
sub impost2 {
#############

        if (-e("$memberdir/$input{'to'}.dat")) { } else { error("$err{'010'}"); }
        if($input{'cc'} ne ""){if (-e("$memberdir/$input{'cc'}.dat")) { } else { error("BCC: $err{'010'}"); }}
        error("$err{'014'}") unless($input{'subject'});
        error("$err{'015'}") unless($input{'message'});


        $nsubject = previewstrip($input{'subject'});
        $nmessage = previewstrip($input{'message'});



        if ($input{'impreview'} eq "$btn{'011'}")  { print "Location: $cgi\?action=im\n\n"; }
        elsif ($input{'impreview'} eq "$btn{'044'}") {

        $messageid = $input{'messageid'};

        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});

        $recipient = $input{'to'};
        $recipient2 = $input{'cc'};
              $myicon = "$input{'icon'}";
        $newmessageid = "$input{'messageid'}$input{'messageid'}";

        open(FILE, "$memberdir/$recipient.dat");
        file_lock(FILE);
        @memset = <FILE>;
        unfile_lock(FILE);
        close(FILE);



                $ranking = $memset[6]+$memset[11]+$memset[12];

                $postinfo = qq~$msg{'021'} $memset[6]<br>$msg{'022'} $memset[11]<br>$msg{'023'} $memset[12]<br>~;
                $memberinfo = "$membergroups[2]";
                $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                if ($ranking > 25) {
                        $memberinfo = "$membergroups[3]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 50) {
                        $memberinfo = "$membergroups[4]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 75) {
                        $memberinfo = "$membergroups[5]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 100) {
                        $memberinfo = "$membergroups[6]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 250) {
                        $memberinfo = "$membergroups[7]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($ranking > 500) {
                        $memberinfo = "$membergroups[8]";
                        $star = qq~<img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0"><img src="$imagesurl/forum/star.gif" alt="" border="0">~;
                }
                if ($boardmoderator eq "$musername") { $memberinfo = "$membergroups[1]"; }
                if ($memset[7] ne "\n") { $memberinfo = "$memset[7]"; }
                if ($memberinfo eq "$root") { $memberinfo = "$membergroups[0]"; }
                $signature = "$memset[5]";
                $signature =~ s/\&\&/<br>/g;
                $signature = qq~<br><br><br>
-----------------<br>
$signature
~;
                $memset[8] =~ s/\n//g;
                $memset[8] =~ s/\r//g;
                if ($memset[8] ne "") {
                        if (!($memset[8] =~ /\D/)) {
                                $icq = qq~&nbsp;&nbsp;<a href="http://www.icq.com/$memset[8]" target="_blank"><img src="http://wwp.icq.com/scripts/online.dll?icq=$memset[8]&amp;img=5" alt="$msg{'052'} $memset[8]" border="0"></a>~;
                        }
                }
                imxdoubbc();
                imxdosmilies();
                $url = "";
                if ($memset[3] ne "\n" && $musername ne "$anonuser") {
                        $url = qq~<a href="$memset[4]" target="_blank"><img src="$imagesurl/forum/www.gif" alt="$msg{'053'} $musername" border="0"></a>&nbsp;&nbsp;~;
                }


$memberpic ="";

                if ($musername ne "$anonuser") {
                        if ($memset[9] eq "") { $memset[9] = "_nopic.gif"; }
                        if ($memset[9] =~ /^\http:\/\// ) {
                                if ($memberpic_width ne 0) { $tmp_width = qq~width="$memberpic_width"~; }
                                else { $tmp_width = ""; }
                                if ($memberpic_height ne 0) { $tmp_height = qq~height="$memberpic_height"~; }
                                else { $tmp_height = ""; }
                                $memberpic = qq~<img src="$memset[9]" $tmp_width $tmp_height border="0" alt="$info{'username'}"></a>~;
                        }
                        else {
                                $memberpic = qq~<img src="$imagesurl/avatars/$memset[9]" border="0" alt=""></a>~;
                        }

                display_date($date); $date = $user_display_date;


$navbar = "$btn{'014'} IMX $btn{'044'}";
        print_top();

                print qq~
<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign="top" width="100%">
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor="$windowbg"><b>$msg{'320'}</b></td>
<td bgcolor="$windowbg"><b>$msg{'037'}</b></td>
</tr>
<tr>
<td bgcolor="#ffffff" width="140" valign="top" rowspan="2"><b>$recipient</b><br>
<small>$memberinfo<br>
$star<br>
$postinfo<br>
<center>$memberpic
~;
}

open(FILE, "$datadir/log.dat");
file_lock(FILE);
@entries = <FILE>;
unfile_lock(FILE);
close(FILE);

@entries = (sort { lc($a) cmp lc($b) } @entries);

                 foreach $lline (@entries){
                       ($lname,$dummy,$dummy) = split(/\|/, $lline);
                       if($lname eq "$recipient"){
                       $lstat = "<div align=center><iframe id=frame src=http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi width=150 height=350 marginwidth=0 marginheight=0 hspace= vspace=0 frameborder=0 scrolling=no></iframe>
<Br><a href=javascript:loadwindow('http://www.iglesiadelpactorenacer.org/cgi-bin/mods/tagbox/tagbox.cgi',190,310)>Notas Instantaneas</a></div>";
                       $amionline = "<font color=green><h4>$imx{'043'}</h4></font><br>";}
                             else {
$lstat = "";
$amionline = "<font color=red><h4>$imx{'044'}</h4></font><br>";}
}
if ($memset[1] ne ""){
print qq~
$amionline
~;}

print qq~
<br>

</center>

</td>
<td bgcolor="#ffffff" valign="top">
<table border="0" width="100%" cellpadding="0" cellspacing="1">
<tr>
<td width="100%">
~;if ($myicon ne "1"){print qq~
<img src="$imagesurl/im/$myicon.gif">&nbsp; ~;}else{print qq~
<img src="$imagesurl/im/aicon.gif">&nbsp; ~;} print qq~
&nbsp;<b>$subject</b></td>
<td align="right" nowrap><b>$msg{'054'}</b> $date</td>
</tr>
</table>
<hr noshade="noshade" size="1">

$message

<br>


</td>
</tr>
</table>
<br>
<table width=100% bgcolor=white><tr><td class=helpsnavtable><font color=navy><b>$nav{'102'} Info:</b></font></td></tr><tr><td><font color=navy>~;
if ($input{'cc'} eq "admin" && $input{'to'} eq "admin"){$what = "      error... BCC: $username??";}
if ($input{'cc'} ne ""){
print qq~<b>BCC: </b><i>$input{'cc'}</i> &nbsp;<font color=red><b>$what</b></font>~;}else{print qq~<b>BCC:</b> -- ~;}
if ($input{'copy_im'} eq "on"){
print qq~<br><font color=navy>$imx{'009'} $msg{'003'} </font><b>$nav{'047'}</b>~;}else {print qq~<br><font color=navy>$imx{'009'} $msg{'003'} </font><b>No</b>~;}
print qq~
<hr><br>
<form action="$cgi?action=imsend2" name=creator method="post" onSubmit="submitonce(this)">

<input type=hidden name="subject" value="$nsubject">
<input type=hidden name="message" value="$nmessage">
<input type=hidden name="to" value="$recipient">
<input type=hidden name="cc" value="$recipient2">
<input type=hidden name="icon" value="$myicon">
<input type=hidden name="messageid" value="$messageid">
<input type=hidden name="newmessageid" value="$newmessageid">
<input type=hidden name="copy_im" value="$input{'copy_im'}">

<center><input type=button name="" value="$btn{'015'}" onClick="history.back()"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}" onClick="history.back()"></center></form>
</font></td></tr></table>
~;
print_bottom();
exit;
}

else {


        $messageid = $input{'messageid'};
        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});



        $recipient = $input{'to'};
        $recipient2 = $input{'cc'};
              $myicon = "$input{'icon'}";
        $newmessageid = "$input{'messageid'}$input{'messageid'}";


        open (FILE, "$memberdir/$input{'to'}.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'to'}.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$messageid|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);

        if ($input{'cc'} ne "") {
        open (FILE, "$memberdir/$input{'cc'}.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'cc'}.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$messageid|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);

        }

         if ($input{'copy_im'} eq "on") {
        $subject = htmlescape("$input{'subject'}");
         open (FILE, "$memberdir/backup/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/backup/$username.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$messageid|$recipient|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);}

        if ($input{'copy_im'} eq "on" && $input{'cc'} ne "") {
        $subject = htmlescape("$input{'subject'}");
         open (FILE, "$memberdir/backup/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/backup/$username.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$newmessageid|$recipient2|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);}

        if ($input{'tag'} eq "on") { print "Location: $pageurl/$cgi?action=im2&to=$recipient&messageid=$messageid\n\n";}else{

        print "Location: $pageurl/$cgi\?action=im\n\n";}
        exit;}

}

#############
sub originalimpost2 {
#############

        error("$err{'014'}") unless($input{'subject'});
        error("$err{'015'}") unless($input{'message'});
        $messageid = $input{'messageid'};
        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});


        if ($input{'tag'} eq "on") {
        $tag = "<br>";
        $message = "$message $tag";}


        $recipient = $input{'to'};
        $recipient2 = $input{'cc'};
              $myicon = "$input{'icon'}";
        $newmessageid = "$input{'messageid'}$input{'messageid'}";

        if (-e("$memberdir/$input{'to'}.dat")) { } else { error("$err{'010'}"); }

        open (FILE, "$memberdir/$input{'to'}.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'to'}.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$messageid|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);

        if ($input{'cc'} ne "") {
        open (FILE, "$memberdir/$input{'cc'}.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'cc'}.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$messageid|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);

        }

         if ($input{'copy_im'} eq "on") {
        $subject = htmlescape("$input{'subject'}");
         open (FILE, "$memberdir/backup/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/backup/$username.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$messageid|$recipient|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);}

        if ($input{'copy_im'} eq "on" && $input{'cc'} ne "") {
        $subject = htmlescape("$input{'subject'}");
         open (FILE, "$memberdir/backup/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/backup/$username.msg");
        file_lock(FILE);
        print FILE "$username|$subject|$date|$message|$newmessageid|$recipient2|$myicon\n";
        foreach $curm (@imessages) { print FILE "$curm"; }
        unfile_lock(FILE);
        close(FILE);}

        if ($input{'tag'} eq "on") { print "Location: $pageurl/$cgi?action=im2&to=$recipient&messageid=$messageid\n\n";}else{

        print "Location: $pageurl/$cgi\?action=im\n\n";}
        exit;

}


############
sub siteim {
############

        if ($memsettings[7] eq "Administrator") { error("$err{'011'}"); }

        open(FILE, "$memberdir/$username.dat");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

     $mid = time;

        $mytopbar = "";
        $navbar = "$btn{'014'} $nav{'029'}";
        print_top();
        mytopbar3();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign=top>
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td><form action="$cgi?action=siteim2" name=creator method="post" onSubmit="submitonce(this)">
<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="0" width=100%>
<tr class="menutable">
<td><b>$msg{'059'}</b></td>
<td>$msg{'563'}</td>
</tr>
<tr class="forumtitlebackcolor">
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>

~;
if ($enable_ubbc eq "1") {print qq~
<tr class="boardtitle">
<td valign=top><font size="1" face="Helvetica, Arial, Verdana">
<b>$msg{'156'}</b></font></td>
<td valign="top">
<table><tr><td>
<script language="javascript" type="text/javascript">
<!--
function addCode(anystr) {
document.creator.message.value+=anystr;
}
function showColor(color) {
document.creator.message.value+="[color="+color+"][/color]";
}
function showFont(font) {
document.creator.message.value+="[font="+font+"][/font]";
}
function showSize(size) {
document.creator.message.value+="[size="+size+"][/size]";
}
function upload() {
window.open("$pageurl/$cgi?action=uploadpicture","","width=300,height=150,scrollbars")
}
// -->
</script>
<select name="color" onChange="showColor(this.options[this.selectedIndex].value)">
<option value="Black" selected>$msg{'127'}</option>
<option value="Red" style='color:red'>$msg{'128'}</option>
<option value="Yellow" style='color:yellow'>$msg{'129'}</option>
<option value="Pink" style='color:pink'>$msg{'130'}</option>
<option value="Green" style='color:green'>$msg{'131'}</option>
<option value="Orange" style='color:orange'>$msg{'132'}</option>
<option value="Purple" style='color:purple'>$msg{'133'}</option>
<option value="Blue" style='color:blue'>$msg{'134'}</option>
<option value="Beige" style='color:beige'>$msg{'135'}</option>
<option value="Brown" style='color:brown'>$msg{'136'}</option>
<option value="Teal" style='color:teal'>$msg{'137'}</option>
<option value="Navy" style='color:navy'>$msg{'138'}</option>
<option value="Maroon" style='color:maroon'>$msg{'139'}</option>
<option value="LimeGreen" style='color:limegreen'>$msg{'140'}</option>
</select>
&nbsp;
<select name="font" onChange="showFont(this.options[this.selectedIndex].value)">
<option value='Arial' style="font-family:Arial" selected>Arial</option>
<option value='Times New Roman' style="font-family:Times New Roman">Times New Roman</option>
<option value='Courier' style="font-family:Courier">Courier</option>
<option value='Impact' style="font-family:Impact">Impact</option>
<option value='Geneva' style="font-family:Geneva">Geneva</option>
<option value='Verdana' style="font-family:verdana">Verdana</option>
</select>
&nbsp;
<select name="size" onChange="showSize(this.options[this.selectedIndex].value)">
<option value='1'>$imx{'018'}</option>
<option value='3' selected>$imx{'019'}</option>
<option value='5'>$imx{'020'}</option>
<option value='7'>$imx{'021'}</option>
<option value='10'>$imx{'022'}</option>
</select>

</td></tr>
<tr class="forumtitlebackcolor"><td valign=bottom>
<input type=button onclick="javascript:addCode('[b][/b]')" value=" B ">

<input type=button onclick="javascript:addCode('[i][/i]')" value=" I ">

<input type=button onclick="javascript:addCode('[u][/u]')" value=" U ">

<input type=button onclick="javascript:addCode('[url][/url]')" value=" http:// ">

<input type=button onclick="javascript:addCode('[email][/email]')" value=" E-mail ">

<input type=button onclick="javascript:addCode('[img][/img]')" value=" IMG ">

<input type=button onclick="javascript:addCode('[quote][/quote]')" value=" $imx{'023'} ">
</td></tr>
</td></table>
</td>
</tr>~;}
print qq~
<tr class="forumtitlebackcolor">
<td valign="top"><b>$msg{'038'}</b><br>

</td>

<td>
<textarea name="message" wrap=physical rows="10" cols="55">$form_message</textarea>~;
open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) {

        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $themegif, $themecolor, $imximage, $contactnum) = split(/\|/, $curentry);}


if ($imximage eq "1") {
print qq~<br>
<a href="javascript:upload()"><img src="$imagesurl/im/foto.gif" alt="" border=0><b>$msg{'598'}</b></a>
<br>~;}
print qq~
</td>
</tr>
<tr class="boardtitle">
<td colspan="2"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
</td></tr></table>
</td><td valign=top>
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top>
<table width=100% cellspacing="0" cellpadding="0">
<tr class="menutable"><td align=center><b>$imx{'045'}</b></td></tr></table>~;

unless (-e("$memberdir/adminim/contact"))
{
   mkdir("$memberdir/adminim/contact",0777);
   chmod(0777,"$memberdir/adminim/contact");
}
open(FILE, "<$memberdir/adminim/contact/$username.lst");
file_lock(FILE);
chop(@mycontact = <FILE>);
unfile_lock(FILE);
close(FILE);
$countcontact = @mycontact;

if (@mycontact <= 5){
for ($a = 0; $a < @mycontact; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);

print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
else {
                for ($a = 0; $a < 5; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);
print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
print qq~<br>Total = $countcontact $imx{'045'}</td></tr>
<tr><td></td></tr>
<tr><td></td></tr>
</table>
<br><br>
<center>
<table width=100%><tr class=menutable><td colspan=5 align=center><B>$imx{'045'} $imx{'047'}</b></td></tr>
<tr><td colspan=5>&nbsp;</td></tr>~;
blist();

print qq~
<tr><td colspan=5></td></tr>
<tr><td colspan=5 class=forumwindow1 align=right><a href="$pageurl/$cgi?action=contacts">$btn{'030'}</a><br><a href="$pageurl/$cgi?action=memberlist">$nav{'019'}</a></td></tr>

</table></center>
~;
imxversion();
print qq~
</td></tr></table>

<br><br><center><a href="$cgi?action=im">$nav{'102'}</a></center>
~;

        print_bottom();
        exit;

}

#############
sub siteim2 {
#############

        if ($memsettings[7] eq "Administrator") { error("$err{'011'}"); }

        open(FILE, "$memberdir/$username.dat");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        error("$err{'014'}") unless($input{'subject'});
        error("$err{'015'}") unless($input{'message'});

        $imsubj = htmlescape($input{'subject'});
        $formatmsg = htmlescape($input{'message'});


        open (FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        @sendingto = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        foreach $sitemember (@sendingto) {
                $sitemember =~ s/[\n\r]//g;


                                sendim($sitemember, $imsubj, $formatmsg, $username);


                }


        print "Location: $pageurl/$cgi\?action=im\n\n";
        exit;

}


#############
sub adminim {
#############
                                open (FILE, "$memberdir/$username.dat");
                                file_lock(FILE);
                                @settings = <FILE>;
                                unfile_lock(FILE);
                                close(FILE);
                                for( $i = 0; $i < @settings; $i++ ) {
                                $settings[$i] =~ s~[\n\r]~~g;
                                }
        if ($username ne "admin" && $settings[7] ne "$root") { error("$err{'011'}"); }
        open(FILE, "$memberdir/$username.dat");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);
     $mid = time;
        $mytopbar ="";
        $navbar = "$btn{'014'} $nav{'029'}";
        print_top();
        mytopbar3();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign=top>
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td><form action="$cgi?action=adminim2" name=creator method="post" onSubmit="submitonce(this)">
<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="0" width=100%>
<tr class="menutable"><td align=center colspan=2><b>$msg{'595'}</b></td></tr>


<tr bgcolor=#FFFFFF>
<td><b>$msg{'059'}</b></td>
<td>$msg{'595'}</td>
</tr>
<tr class="boardtitle">
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
~;
if ($enable_ubbc eq "1") {print qq~
<tr class="forumtitlebackcolor">
<td valign=top><font size="1" face="Helvetica, Arial, Verdana">
<b>$msg{'156'}</b></font></td>
<td valign="top">
<table><tr><td>
<script language="javascript" type="text/javascript">
<!--#jeffcrawford ubbcfix, anon ubbc hack #


function AddText(NewCode) {
        if (document.creator.message.createTextRange && document.creator.message.caretPos) {
                var caretPos = document.creator.message.caretPos;
                caretPos.text = NewCode;
        } else {
                document.creator.message.value+=NewCode;
        }
        document.creator.message.focus();
}
function addCodeA(bCode1,bCode2) {
                var text = getText();
                AddTxt = bCode1 + text + bCode2;
                AddText(AddTxt);
}
function getText() {
        if (document.creator.message.createTextRange && document.creator.message.caretPos) {
                return document.creator.message.caretPos.text;
        } else {
                return '';
        }
}
function storeCaret(ftext) {
        if (ftext.createTextRange) {
                ftext.caretPos = document.selection.createRange().duplicate();
        }
}
function addCode(anystr) {
document.creator.message.value+=anystr;
}
function showColor(color) {
document.creator.message.value+="[color="+color+"][/color]";
}

function showFont(font) {
document.creator.message.value+="[font="+font+"][/font]";
}
function showSize(size) {
document.creator.message.value+="[size="+size+"][/size]";
}
function upload() {
window.open("$pageurl/$cgi?action=uploadpicture","","width=300,height=150,scrollbars")
}
// -->
</script>
<select name="color" onChange="showColor(this.options[this.selectedIndex].value)">
<option value="Black" selected>$msg{'127'}</option>
<option value="Red" style='color:red'>$msg{'128'}</option>
<option value="Yellow" style='color:yellow'>$msg{'129'}</option>
<option value="Pink" style='color:pink'>$msg{'130'}</option>
<option value="Green" style='color:green'>$msg{'131'}</option>
<option value="Orange" style='color:orange'>$msg{'132'}</option>
<option value="Purple" style='color:purple'>$msg{'133'}</option>
<option value="Blue" style='color:blue'>$msg{'134'}</option>
<option value="Beige" style='color:beige'>$msg{'135'}</option>
<option value="Brown" style='color:brown'>$msg{'136'}</option>
<option value="Teal" style='color:teal'>$msg{'137'}</option>
<option value="Navy" style='color:navy'>$msg{'138'}</option>
<option value="Maroon" style='color:maroon'>$msg{'139'}</option>
<option value="LimeGreen" style='color:limegreen'>$msg{'140'}</option>
</select>
&nbsp;
<select name="font" onChange="showFont(this.options[this.selectedIndex].value)">
<option value='Arial' style="font-family:Arial" selected>Arial</option>
<option value='Times New Roman' style="font-family:Times New Roman">Times New Roman</option>
<option value='Courier' style="font-family:Courier">Courier</option>
<option value='Impact' style="font-family:Impact">Impact</option>
<option value='Geneva' style="font-family:Geneva">Geneva</option>
<option value='Verdana' style="font-family:verdana">Verdana</option>
</select>
&nbsp;
<select name="size" onChange="showSize(this.options[this.selectedIndex].value)">
<option value='1'>$imx{'018'}</option>
<option value='3' selected>$imx{'019'}</option>
<option value='5'>$imx{'020'}</option>
<option value='7'>$imx{'021'}</option>
<option value='10'>$imx{'022'}</option>
</select>

</td></tr>
<tr class="forumtitlebackcolor"><td valign=bottom>
<input type=button onclick="javascript:addCodeA('[b]','[/b]')" value=" B ">

<input type=button onclick="javascript:addCodeA('[i]','[/i]')" value=" I ">

<input type=button onclick="javascript:addCodeA('[u]','[/u]')" value=" U ">

<input type=button onclick="javascript:addCodeA('[url]','[/url]')" value=" http:// ">

<input type=button onclick="javascript:addCodeA('[email]','[/email]')" value=" @ ">

<input type=button onclick="javascript:addCodeA('[img]','[/img]')" value=" IMG ">

<input type=button onclick="javascript:addCodeA('[quote]','[/quote]')" value=" $imx{'023'} ">
</td></tr>
</td></table>
</td>
</tr>~;}
print qq~
<tr class="forumtitlebackcolor">
<td valign="top"><b>$msg{'038'}</b><br>

</td>

<td><textarea name="message" wrap=physical rows="10" cols="55"onselect="storeCaret(this);" onclick="storeCaret(this);" onkeyup="storeCaret(this);" onchange="storeCaret(this);">$form_message</textarea>
~;
open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) {

        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $themegif, $themecolor, $imximage, $contactnum) = split(/\|/, $curentry);}

if ($imximage eq "1") {
print qq~<br>
<a href="javascript:upload()"><img src="$imagesurl/im/foto.gif" alt="" border=0><b>$msg{'598'}</b></a>
<br>~;}
print qq~
</td>
</tr>
<tr class="boardtitle">
<td colspan="2"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
</td></tr></table>
</td><td valign=top>
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top>
<table width=100% cellspacing="0" cellpadding="0">
<tr class="menutable"><td align=center><b>$imx{'045'}</b></td></tr></table>~;

unless (-e("$memberdir/adminim/contact"))
{
   mkdir("$memberdir/adminim/contact",0777);
   chmod(0777,"$memberdir/adminim/contact");
}
open(FILE, "<$memberdir/adminim/contact/$username.lst");
file_lock(FILE);
chop(@mycontact = <FILE>);
unfile_lock(FILE);
close(FILE);
$countcontact = @mycontact;

if (@mycontact <= 5){
for ($a = 0; $a < @mycontact; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);

print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
else {
                for ($a = 0; $a < 5; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);
print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
print qq~<br>Total = $countcontact $imx{'045'}</td></tr>
<tr><td></td></tr>
<tr><td></td></tr>
</table>
<br><br>
<center>
<table width=100%><tr class=menutable><td colspan=5 align=center><B>$imx{'045'} $imx{'047'}</b></td></tr>
<tr><td colspan=5>&nbsp;</td></tr>~;
blist();

print qq~
<tr><td colspan=5></td></tr>
<tr><td colspan=5 class=forumwindow1 align=right><a href="$pageurl/$cgi?action=contacts">$btn{'030'}</a><br><a href="$pageurl/$cgi?action=memberlist">$nav{'019'}</a></td></tr>

</table></center>
~;
imxversion();
print qq~
</td></tr></table>

<br><center><a href=$pageurl/$cgi?action=im>$nav{'102'}</a></center>

~;
        print_bottom();
        exit;
}
##############
sub adminim2 {
##############
                                open (FILE, "$memberdir/$username.dat");
                                file_lock(FILE);
                                @settings = <FILE>;
                                unfile_lock(FILE);
                                close(FILE);
                                for( $i = 0; $i < @settings; $i++ ) {
                                $settings[$i] =~ s~[\n\r]~~g;
                                }
        if ($username ne "admin" && $settings[7] ne "$root") { error("$err{'011'}"); }
        open(FILE, "$memberdir/$username.dat");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        error("$err{'014'}") unless($input{'subject'});
        error("$err{'015'}") unless($input{'message'});

        $imsubj = htmlescape($input{'subject'});
        $formatmsg = htmlescape($input{'message'});

        open (FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        @sendingto = <FILE>;
        unfile_lock(FILE);
        close (FILE);
        foreach $sitemember (@sendingto) {
                $sitemember =~ s/[\n\r]//g;

                                open (FILE, "$memberdir/$sitemember.dat");
                                file_lock(FILE);
                                @settings = <FILE>;
                                unfile_lock(FILE);
                                close(FILE);
                                for( $i = 0; $i < @settings; $i++ ) {
                                $settings[$i] =~ s~[\n\r]~~g;
                                }
                                if ($settings[7] eq "$root") {
                                sendim($sitemember, $imsubj, $formatmsg, $username);
                                }
                }
        print "Location: $pageurl/$cgi\?action=im\n\n";
        exit;
}
###########
sub modim {
###########
                                open (FILE, "$memberdir/$username.dat");
                                file_lock(FILE);
                                @settings = <FILE>;
                                unfile_lock(FILE);
                                close(FILE);
                                for( $i = 0; $i < @settings; $i++ ) {
                                $settings[$i] =~ s~[\n\r]~~g;
                                }
        if ($username ne "admin" && $settings[7] ne "$root" && $settings[7] ne "$boardmoderator") { error("$err{'011'}"); }
        open(FILE, "$memberdir/$username.dat");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);
     $mid = time;
        $mytopbar = "";
        $navbar = "$btn{'014'} $msg{'594'}";
        print_top();
        mytopbar3();
        print qq~<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td valign=top>
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td><form action="$cgi?action=modim2" name=creator method="post" onSubmit="submitonce(this)">
<input name="messageid" value="$mid" type="hidden">
<table border="0" cellspacing="0" width=100%>
<tr class="menutable"><td align=center colspan=2><b>$msg{'594'}</b>
</td></tr>


<tr bgcolor=#FFFFFF>
<td><b>$msg{'059'}</b></td>
<td>~;
$howmany = 0;


print qq~&nbsp;&nbsp;&nbsp;  &nbsp;[ $msg{'099'}:  ~;
open (FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        @myuser = <FILE>;
        unfile_lock(FILE);
        close (FILE);
        foreach $sitemember (@myuser) {
        $howmany++;
                $sitemember =~ s/[\n\r]//g;
                                open (FILE, "$memberdir/$sitemember.dat");
                                file_lock(FILE);
                                @settings = <FILE>;
                                unfile_lock(FILE);
                                close(FILE);
                                for( $i = 0; $i < @settings; $i++ ) {
                                $settings[$i] =~ s~[\n\r]~~g;
                                }
                                if ($settings[7] eq "$boardmoderator") {
$sitemembermoderator = '';
$sitemembermoderator = qq~<a href="$cgi?action=imsend&username=$sitemember">$sitemember</a>~;



                                        print "$sitemembermoderator";
if ($howmany > 1) { print ", "; }
}
}
print qq~]</td>
</tr>
<tr class="boardtitle">
<td><b>$msg{'037'}</b></td>
<td><input type="text" name="subject" value="$form_subject" size="40" maxlength="50"></td>
</tr>
~;
if ($enable_ubbc eq "1") {print qq~
<tr class="forumtitlebackcolor">
<td valign=top><font size="1" face="Helvetica, Arial, Verdana">
<b>$msg{'156'}</b></font></td>
<td valign="top">
<table><tr><td>
<script language="javascript" type="text/javascript">
<!--#jeffcrawford ubbcfix, anon ubbc hack #


function AddText(NewCode) {
        if (document.creator.message.createTextRange && document.creator.message.caretPos) {
                var caretPos = document.creator.message.caretPos;
                caretPos.text = NewCode;
        } else {
                document.creator.message.value+=NewCode;
        }
        document.creator.message.focus();
}
function addCodeA(bCode1,bCode2) {
                var text = getText();
                AddTxt = bCode1 + text + bCode2;
                AddText(AddTxt);
}
function getText() {
        if (document.creator.message.createTextRange && document.creator.message.caretPos) {
                return document.creator.message.caretPos.text;
        } else {
                return '';
        }
}
function storeCaret(ftext) {
        if (ftext.createTextRange) {
                ftext.caretPos = document.selection.createRange().duplicate();
        }
}
function addCode(anystr) {
document.creator.message.value+=anystr;
}
function showColor(color) {
document.creator.message.value+="[color="+color+"][/color]";
}
function showFont(font) {
document.creator.message.value+="[font="+font+"][/font]";
}
function showSize(size) {
document.creator.message.value+="[size="+size+"][/size]";
}
function upload() {
window.open("$pageurl/$cgi?action=uploadpicture","","width=300,height=150,scrollbars")
}
// -->
</script>
<select name="color" onChange="showColor(this.options[this.selectedIndex].value)">
<option value="Black" selected>$msg{'127'}</option>
<option value="Red" style='color:red'>$msg{'128'}</option>
<option value="Yellow" style='color:yellow'>$msg{'129'}</option>
<option value="Pink" style='color:pink'>$msg{'130'}</option>
<option value="Green" style='color:green'>$msg{'131'}</option>
<option value="Orange" style='color:orange'>$msg{'132'}</option>
<option value="Purple" style='color:purple'>$msg{'133'}</option>
<option value="Blue" style='color:blue'>$msg{'134'}</option>
<option value="Beige" style='color:beige'>$msg{'135'}</option>
<option value="Brown" style='color:brown'>$msg{'136'}</option>
<option value="Teal" style='color:teal'>$msg{'137'}</option>
<option value="Navy" style='color:navy'>$msg{'138'}</option>
<option value="Maroon" style='color:maroon'>$msg{'139'}</option>
<option value="LimeGreen" style='color:limegreen'>$msg{'140'}</option>
</select>
&nbsp;
<select name="font" onChange="showFont(this.options[this.selectedIndex].value)">
<option value='Arial' style="font-family:Arial" selected>Arial</option>
<option value='Times New Roman' style="font-family:Times New Roman">Times New Roman</option>
<option value='Courier' style="font-family:Courier">Courier</option>
<option value='Impact' style="font-family:Impact">Impact</option>
<option value='Geneva' style="font-family:Geneva">Geneva</option>
<option value='Verdana' style="font-family:verdana">Verdana</option>
</select>
&nbsp;
<select name="size" onChange="showSize(this.options[this.selectedIndex].value)">
<option value='1'>$imx{'018'}</option>
<option value='3' selected>$imx{'019'}</option>
<option value='5'>$imx{'020'}</option>
<option value='7'>$imx{'021'}</option>
<option value='10'>$imx{'022'}</option>
</select>

</td></tr>
<tr class="forumtitlebackcolor"><td valign=bottom>
<input type=button onclick="javascript:addCodeA('[b]','[/b]')" value=" B ">

<input type=button onclick="javascript:addCodeA('[i]','[/i]')" value=" I ">

<input type=button onclick="javascript:addCodeA('[u]','[/u]')" value=" U ">

<input type=button onclick="javascript:addCodeA('[url]','[/url]')" value=" http:// ">

<input type=button onclick="javascript:addCodeA('[email]','[/email]')" value=" @ ">

<input type=button onclick="javascript:addCodeA('[img]','[/img]')" value=" IMG ">

<input type=button onclick="javascript:addCodeA('[quote]','[/quote]')" value=" $imx{'023'} ">
</td></tr>
</td></table>
</td>
</tr>~;}
print qq~
<tr class="forumtitlebackcolor">
<td valign="top"><b>$msg{'038'}</b><br>

</td>

<td><textarea name="message" wrap=physical rows="10" cols="55"onselect="storeCaret(this);" onclick="storeCaret(this);" onkeyup="storeCaret(this);" onchange="storeCaret(this);">$form_message</textarea>

~;
open(FILE, "$memberdir/adminim/admin.txt");
              file_lock(FILE);
              @entries = <FILE>;
              unfile_lock(FILE);
              close(FILE);
        foreach $curentry (@entries) {

        $curentry =~ s/[\n\r]//g; ($imxinbox, $imxsaved, $imxsent, $imxfolders, $numfolders, $radiogif, $themegif, $themecolor, $imximage, $contactnum) = split(/\|/, $curentry);}

if ($imximage eq "1") {
print qq~<br>
<a href="javascript:upload()"><img src="$imagesurl/im/foto.gif" alt="" border=0><b>$msg{'598'}</b></a>
<br>~;}
print qq~
</td>
</tr>
<tr class="boardtitle">
<td colspan="2"><input type="submit" value="$btn{'008'}">
<input type="reset" value="$btn{'009'}"></td>
</tr>
</table>
</form>
</td>
</tr>
</table>
</td></tr></table>
</td><td valign=top>
<table width=100% border="0" cellspacing="0" cellpadding="0"><Tr><Td valign=top>
<table width=100% cellspacing="0" cellpadding="0">
<tr class="menutable"><td align=center><b>$imx{'045'}</b></td></tr></table>~;

unless (-e("$memberdir/adminim/contact"))
{
   mkdir("$memberdir/adminim/contact",0777);
   chmod(0777,"$memberdir/adminim/contact");
}
open(FILE, "<$memberdir/adminim/contact/$username.lst");
file_lock(FILE);
chop(@mycontact = <FILE>);
unfile_lock(FILE);
close(FILE);
$countcontact = @mycontact;

if (@mycontact <= 5){
for ($a = 0; $a < @mycontact; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);

print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
else {
                for ($a = 0; $a < 5; $a++){
($name[$a], $value[$a]) = split(/\|/,$mycontact[$a]);
print qq~
<img src="$imagesurl/im/insert.gif">&nbsp;<a href="$pageurl/$cgi?action=imsend&to=$name[$a]">$name[$a]</a><br>~;}
}
print qq~<br>Total = $countcontact $imx{'045'}</td></tr>
<tr><td></td></tr>
<tr><td></td></tr>
</table>
<br><br>
<center>
<table width=100%><tr class=menutable><td colspan=5 align=center><B>$imx{'045'} $imx{'047'}</b></td></tr>
<tr><td colspan=5>&nbsp;</td></tr>~;
blist();

print qq~
<tr><td colspan=5></td></tr>
<tr><td colspan=5 class=forumwindow1 align=right><a href="$pageurl/$cgi?action=contacts">$btn{'030'}</a><br><a href="$pageurl/$cgi?action=memberlist">$nav{'019'}</a></td></tr>

</table></center>
~;
imxversion();
print qq~
</td></tr></table>

<br><center><a href=$pageurl/$cgi?action=im>$nav{'102'}</a></center>


~;
        print_bottom();
        exit;
}
############
sub modim2 {
############
                                open (FILE, "$memberdir/$username.dat");
                                file_lock(FILE);
                                @settings = <FILE>;
                                unfile_lock(FILE);
                                close(FILE);
                                for( $i = 0; $i < @settings; $i++ ) {
                                $settings[$i] =~ s~[\n\r]~~g;
                                }
        if ($username ne "admin" && $settings[7] ne "$root" && $settings[7] ne "$boardmoderator") { error("$err{'011'}"); }
        open(FILE, "$memberdir/$username.dat");
        file_lock(FILE);
        chomp(@memsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        error("$err{'014'}") unless($input{'subject'});
        error("$err{'015'}") unless($input{'message'});
        $imsubj = htmlescape($input{'subject'});
        $formatmsg = htmlescape($input{'message'});

        open (FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        @sendingto = <FILE>;
        unfile_lock(FILE);
        close (FILE);
        foreach $sitemember (@sendingto) {
                $sitemember =~ s/[\n\r]//g;

                                open (FILE, "$memberdir/$sitemember.dat");
                                file_lock(FILE);
                                @settings = <FILE>;
                                unfile_lock(FILE);
                                close(FILE);
                                for( $i = 0; $i < @settings; $i++ ) {
                                $settings[$i] =~ s~[\n\r]~~g;
                                }
                                if ($settings[7] eq "$boardmoderator") {
                                sendim($sitemember, $imsubj, $formatmsg, $username);
                                }

                }
        print "Location: $pageurl/$cgi\?action=im\n\n";
        exit;
}



################
# move subs    #
################

###############
sub moveim {
###############




        open (FILE, "$memberdir/$username.msg") || error("$err{'001'} $memberdir/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$username.msg") || error("$err{'016'} $memberdir/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @topics; $a++) {
                ($imuser, $subject, $postdate, $message, $imxid, $imxicon, $imvue) = split(/\|/,$topics[$a]);
                $message  =~ s~[\n\r]~~g;
                if ($imxid ne $input{'topic'}) {
                print FILE "$topics[$a]"; }
                else { $linetowrite = "$topics[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);


        if ($input{"tocat"} eq "saved"){

        open (FILE, "$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}else{
        open (FILE, "$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}
        print "Location: $pageurl/$cgi\?action=im\n\n";
        exit;

}

###############
sub moveim2 {
###############



        open (FILE, "$memberdir/backup/$username.msg") || error("$err{'001'} $memberdir/backup/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/backup/$username.msg") || error("$err{'016'} $memberdir/backup/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @topics; $a++) {
                ($imuser, $subject, $postdate, $message, $imxid, $imxicon, $imvue) = split(/\|/,$topics[$a]);
                $message  =~ s~[\n\r]~~g;
                if ($imxid ne $input{'topic'}) {
                print FILE "$topics[$a]"; }
                else { $linetowrite = "$topics[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);
        if ($input{"tocat"} eq "saved"){

        open (FILE, "$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}else{
        open (FILE, "$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}
        print "Location: $pageurl/$cgi\?action=imfolder\n\n";
        exit;

}

###############
sub moveim3 {
###############



        open (FILE, "$memberdir/saved/$username.msg") || error("$err{'001'} $memberdir/saved/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/saved/$username.msg") || error("$err{'016'} $memberdir/saved/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @topics; $a++) {
                ($imuser, $subject, $postdate, $message, $imxid, $imxicon, $imvue) = split(/\|/,$topics[$a]);
                $message  =~ s~[\n\r]~~g;
                if ($imxid ne $input{'topic'}) {
                print FILE "$topics[$a]"; }
                else { $linetowrite = "$topics[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);
        if ($input{"tocat"} eq "backup"){

        open (FILE, "$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}else{
        open (FILE, "$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}
        print "Location: $pageurl/$cgi\?action=saveim\n\n";
        exit;

}

###############
sub moveim4 {
###############


$whatfolder = $input{'whatfolder2'};

        open (FILE, "$memberdir/adminim/$username/$whatfolder/$username.msg") || error("$err{'001'} $memberdir/adminim/$username/$whatfolder/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/adminim/$username/$whatfolder/$username.msg") || error("$err{'016'} $memberdir/adminim/$username/$whatfolder/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @topics; $a++) {
                ($imuser, $subject, $postdate, $message, $imxid, $imxicon, $imvue) = split(/\|/,$topics[$a]);
                $message  =~ s~[\n\r]~~g;
                if ($imxid ne $input{'topic'}) {
                print FILE "$topics[$a]"; }
                else { $linetowrite = "$topics[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);
        if ($input{"tocat"} eq "saved"){

        open (FILE, "$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}else{
        open (FILE, "$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/adminim/$username/$input{'tocat'}/$username.msg");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $linetowrite (@topics) { print FILE "$linetowrite"; }
        unfile_lock(FILE);
        close(FILE);

}
        print "Location: $pageurl/$cgi\?action=messagefolder&folder=$whatfolder\n\n";
        exit;

}


##################
# remove subs    #
##################


##############
sub imremove {
##############
        if ($username eq "$anonuser") { error("noguests"); }


if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/$username.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);


open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "0\n";
unfile_lock(FILE);
close(FILE);


}

else {

        open(FILE, "$memberdir/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);


open(FILE, "$memberdir/$username.upder");
file_lock(FILE);
chomp(@pref = <FILE>);
unfile_lock(FILE);
close(FILE);

$prefmess = $pref[0] - 1;

open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "$prefmess\n";
unfile_lock(FILE);
close(FILE);


        open(FILE, ">$memberdir/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=im\n\n";
}


##############
sub myuserremove {
##############
        if ($username ne "admin") { error("noguests"); }

if ($info{'viewthisuser'} ne "") {
           $myuser = $info{'viewthisuser'}; }

if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/$myuser.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);

}

else {

        open(FILE, "$memberdir/$myuser.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$memberdir/$myuser.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=userimindex&viewthisuser=$myuser\n\n";
}

##############
sub imremove2 {
##############
        if ($username eq "$anonuser") { error("noguests"); }


if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/backup/$username.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);
               open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "0\n";
unfile_lock(FILE);
close(FILE);
}

else {

        open(FILE, "$memberdir/backup/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

       open(FILE, "$memberdir/$username.upder");
file_lock(FILE);
chomp(@pref = <FILE>);
unfile_lock(FILE);
close(FILE);

$prefmess = $pref[0] - 1;

open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "$prefmess\n";
unfile_lock(FILE);
close(FILE);


        open(FILE, ">$memberdir/backup/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=imfolder\n\n";
}

##############
sub myuserremove2 {
##############
        if ($username ne "admin") { error("noguests"); }

if ($info{'viewthisuser'} ne "") {
           $myuser = $info{'viewthisuser'}; }

if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/backup/$myuser.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);

}

else {

        open(FILE, "$memberdir/backup/$myuser.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$memberdir/backup/$myuser.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=userimindex2&viewthisuser=$myuser\n\n";
}

##############
sub imremove3 {
##############
        if ($username eq "$anonuser") { error("noguests"); }


if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/saved/$username.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);
               open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "0\n";
unfile_lock(FILE);
close(FILE);
}

else {

        open(FILE, "$memberdir/saved/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$memberdir/$username.upder");
file_lock(FILE);
chomp(@pref = <FILE>);
unfile_lock(FILE);
close(FILE);

$prefmess = $pref[0] - 1;

open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "$prefmess\n";
unfile_lock(FILE);
close(FILE);

        open(FILE, ">$memberdir/saved/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=saveim\n\n";
}


##############
sub imremove4 {
##############
        if ($username eq "$anonuser") { error("noguests"); }

$folder = $info{"folder"};
if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/adminim/$username/$folder/$username.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);
               open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "0\n";
unfile_lock(FILE);
close(FILE);
}

else {

        open(FILE, "$memberdir/adminim/$username/$folder/$username.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$memberdir/$username.upder");
file_lock(FILE);
chomp(@pref = <FILE>);
unfile_lock(FILE);
close(FILE);

$prefmess = $pref[0] - 1;

open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "$prefmess\n";
unfile_lock(FILE);
close(FILE);

        open(FILE, ">$memberdir/adminim/$username/$folder/$username.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=messagefolder&folder=$folder\n\n";
}


##############
sub imremove5 {
##############
        if ($username eq "$anonuser") { error("noguests"); }
$myuser = $info{"user"};
$folder = $info{"folder"};
if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/adminim/$myuser/$folder/$myuser.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);
       open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "0\n";
unfile_lock(FILE);
close(FILE);
}

else {

        open(FILE, "$memberdir/adminim/$myuser/$folder/$myuser.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$memberdir/$username.upder");
file_lock(FILE);
chomp(@pref = <FILE>);
unfile_lock(FILE);
close(FILE);

$prefmess = $pref[0] - 1;

open(FILE, ">$memberdir/$username.upder");
file_lock(FILE);
print FILE "$prefmess\n";
unfile_lock(FILE);
close(FILE);

        open(FILE, ">$memberdir/adminim/$myuser/$folder/$myuser.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=userimindex4&viewthisuser=$myuser&folder=$folder\n\n";
}


##############
sub myuserremove3 {
##############
        if ($username ne "admin") { error("noguests"); }

if ($info{'viewthisuser'} ne "") {
           $myuser = $info{'viewthisuser'}; }
if ($info{'id'} eq "all") {

        open(FILE, ">$memberdir/saved/$myuser.msg");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);

}

else {

        open(FILE, "$memberdir/saved/$myuser.msg");
        file_lock(FILE);
        @imessages = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$memberdir/saved/$myuser.msg");
        file_lock(FILE);
        for ($a = 0; $a < @imessages; $a++) {
                ($musername, $msub, $mdate, $mmessage, $messageid) = split(/\|/, $imessages[$a]);
                if ($messageid < 100 ) {
                        if($a ne $info{'id'}) { print FILE "$imessages[$a]"; }
                }
                else {
                        if(!($messageid =~ /$info{'id'}/)) { print FILE "$imessages[$a]"; }
                }
        }
        unfile_lock(FILE);
        close(FILE);
}

        print "Location: $pageurl/$cgi\?action=userimindex3&viewthisuser=$myuser\n\n";
}


############
sub imxundosmilies {
############

                $message =~ s~\[bones\]~ox~g;
                $message =~ s~\[bounce\]~I~g;
                $message =~ s~\:-\?~:-?~g;
                $message =~ s~\[confused\]~:-?~g;
                $message =~ s~\Q8\)~Q8~g;
                $message =~ s~\Q8-\)~Q8~g;
                $message =~ s~\[cool\]~Q8~g;
                $message =~ s~\[cry\]~:'-(~g;
                $message =~ s~\:o~:o~g;
                $message =~ s~\:\-o~:-o~g;
                $message =~ s~\[eek\]~:-o~g;
                $message =~ s~\[evil\]~>;->~g;
                $message =~ s~\:\(~:-(~g;
                $message =~ s~\:-\(~(:-(~g;
                $message =~ s~\[frown\]~(:-(~g;
                $message =~ s~\:D~:D~g;
                $message =~ s~\:-D~:-D~g;
                $message =~ s~\[grin\]~:-D~g;
                $message =~ s~\[lol\]~LoL~g;
                $message =~ s~\:x~:x~g;
                $message =~ s~\:-x~:-x~g;
                $message =~ s~\[mad\]~:-x~g;
                $message =~ s~\[ninja\]~(:)-)~g;
                $message =~ s~\[nonsense\]~:-?~g;
                $message =~ s~\[oops\]~8-)~g;
                $message =~ s~\[razz\]~:PP~g;
                $message =~ s~\[rolleyes\]~oo~g;
                $message =~ s~\:\)~:-)~g;
                $message =~ s~\:-\)~:-)~g;
                $message =~ s~\[smile\]~:-)~g;
                $message =~ s~\:P~:P~g;
                $message =~ s~\:-P~:-P~g;
                $message =~ s~\[tongue\]~:P~g;
                $message =~ s~\;-\)~;-)~g;
                $message =~ s~\[wink\]~;-)~g;
                $message =~ s~\[tarzan\]~Tz~g;

$message =~ s~\[imxconfused\]~:-?~g;
$message =~ s~\[imxcool\]~Q8~g;
$message =~ s~\[imxcry\]~:'-(~g;
$message =~ s~\[imxpray\]~\o/~g;
$message =~ s~\[imxhuh\]~:-o~g;
$message =~ s~\[imxgrin\]~:-D~g;
$message =~ s~\[imxlol\]~LoL~g;
$message =~ s~\[imxclap\]~0//~g;
$message =~ s~\[imxsmile\]~:)~g;
$message =~ s~\[imxlove\]~luv~g;
$message =~ s~\[imxwink\]~;-)~g;
$message =~ s~\[imxangel\]~[]:)~g;
$message =~ s~\[imxkiss\]~:*~g;
$message =~ s~\[imxsad\]~:(~g;
$message =~ s~\[imxzzz\]~zzz:|~g;
}

############
sub imxdosmilies {
############

                $message =~ s~\[bones\]~<img src="$imagesurl/forum/smilies/bones.gif" alt="">~g;
                $message =~ s~\[bounce\]~<img src="$imagesurl/forum/smilies/bounce.gif" alt="">~g;
                $message =~ s~\:-\?~<img src="$imagesurl/forum/smilies/confused.gif" alt="">~g;
                $message =~ s~\[confused\]~<img src="$imagesurl/forum/smilies/confused.gif" alt="">~g;
                $message =~ s~\Q8)\E~<img src="$imagesurl/forum/smilies/cool.gif" alt="">~g;
                $message =~ s~\Q8-)\E~<img src="$imagesurl/forum/smilies/cool.gif" alt="">~g;
                $message =~ s~\[cool\]~<img src="$imagesurl/forum/smilies/cool.gif" alt="">~g;
                $message =~ s~\[cry\]~<img src="$imagesurl/forum/smilies/cry.gif" alt="">~g;
                $message =~ s~\:o~<img src="$imagesurl/forum/smilies/eek.gif" alt="">~g;
                $message =~ s~\:\-o~<img src="$imagesurl/forum/smilies/eek.gif" alt="">~g;
                $message =~ s~\[eek\]~<img src="$imagesurl/forum/smilies/eek.gif" alt="">~g;
                $message =~ s~\[evil\]~<img src="$imagesurl/forum/smilies/evil.gif" alt="">~g;
                $message =~ s~\:\(~<img src="$imagesurl/forum/smilies/frown.gif" alt="">~g;
                $message =~ s~\:-\(~<img src="$imagesurl/forum/smilies/frown.gif" alt="">~g;
                $message =~ s~\[frown\]~<img src="$imagesurl/forum/smilies/frown.gif" alt="">~g;
                $message =~ s~\:D~<img src="$imagesurl/forum/smilies/grin.gif" alt="">~g;
                $message =~ s~\:-D~<img src="$imagesurl/forum/smilies/grin.gif" alt="">~g;
                $message =~ s~\[grin\]~<img src="$imagesurl/forum/smilies/grin.gif" alt="">~g;
                $message =~ s~\[lol\]~<img src="$imagesurl/forum/smilies/lol.gif" alt="">~g;
                $message =~ s~\:x~<img src="$imagesurl/forum/smilies/mad.gif" alt="">~g;
                $message =~ s~\:-x~<img src="$imagesurl/forum/smilies/mad.gif" alt="">~g;
                $message =~ s~\[mad\]~<img src="$imagesurl/forum/smilies/mad.gif" alt="">~g;
                $message =~ s~\[ninja\]~<img src="$imagesurl/forum/smilies/ninja.gif" alt="">~g;
                $message =~ s~\[nonsense\]~<img src="$imagesurl/forum/smilies/nonsense.gif" alt="">~g;
                $message =~ s~\[oops\]~<img src="$imagesurl/forum/smilies/oops.gif" alt="">~g;
                $message =~ s~\[razz\]~<img src="$imagesurl/forum/smilies/razz.gif" alt="">~g;
                $message =~ s~\[rolleyes\]~<img src="$imagesurl/forum/smilies/rolleyes.gif" alt="">~g;
                $message =~ s~\:\)~<img src="$imagesurl/forum/smilies/smile.gif" alt="">~g;
                $message =~ s~\:-\)~<img src="$imagesurl/forum/smilies/smile.gif" alt="">~g;
                $message =~ s~\[smile\]~<img src="$imagesurl/forum/smilies/smile.gif" alt="">~g;
                $message =~ s~\:P~<img src="$imagesurl/forum/smilies/tongue.gif" alt="">~g;
                $message =~ s~\:-P~<img src="$imagesurl/forum/smilies/tongue.gif" alt="">~g;
                $message =~ s~\[tongue\]~<img src="$imagesurl/forum/smilies/tongue.gif" alt="">~g;
                $message =~ s~\;-\)~<img src="$imagesurl/forum/smilies/wink.gif" alt="">~g;
                $message =~ s~\[wink\]~<img src="$imagesurl/forum/smilies/wink.gif" alt="">~g;
                $message =~ s~\[tarzan\]~<img src="$imagesurl/forum/smilies/tarzan.gif" alt="">~g;



$message =~ s~\[imxconfused\]~<img src="$imagesurl/im/smilies/confused.gif" alt="">~g;
$message =~ s~\[imxcool\]~<img src="$imagesurl/im/smilies/cool.gif" alt="">~g;
$message =~ s~\[imxcry\]~<img src="$imagesurl/im/smilies/cry.gif" alt="">~g;
$message =~ s~\[imxpray\]~<img src="$imagesurl/im/smilies/pray.gif" alt="">~g;
$message =~ s~\[imxhuh\]~<img src="$imagesurl/im/smilies/huh.gif" alt="">~g;
$message =~ s~\[imxgrin\]~<img src="$imagesurl/im/smilies/grin.gif" alt="">~g;
$message =~ s~\[imxlol\]~<img src="$imagesurl/im/smilies/haha.gif" alt="">~g;
$message =~ s~\[imxclap\]~<img src="$imagesurl/im/smilies/applaud.gif" alt="">~g;
$message =~ s~\[imxsmile\]~<img src="$imagesurl/im/smilies/smile.gif" alt="">~g;
$message =~ s~\[imxlove\]~<img src="$imagesurl/im/smilies/iheartu.gif" alt="">~g;
$message =~ s~\[imxwink\]~<img src="$imagesurl/im/smilies/wink.gif" alt="">~g;
$message =~ s~\[imxangel\]~<img src="$imagesurl/im/smilies/angel.gif" alt="">~g;
$message =~ s~\[imxkiss\]~<img src="$imagesurl/im/smilies/kiss.gif" alt="">~g;
$message =~ s~\[imxsad\]~<img src="$imagesurl/im/smilies/sad.gif" alt="">~g;
$message =~ s~\[imxzzz\]~<img src="$imagesurl/im/smilies/zzz.gif" alt="">~g;



}
############
sub imxdoubbc {
############

        $message =~ s~\[font=(.+?)\]~<font face="$1">~isg;
             $message =~ s~\[\/font\]~</font>~isg;

              $message =~ s~\[size=(.+?)\]~<font size="$1">~isg;
            $message =~ s~\[\/size\]~</font>~isg;

        $message =~ s~\[\[~\{\{~g;
        $message =~ s~\]\]~\}\}~g;
        $message =~ s~\n\[~\[~g;
        $message =~ s~\]\n~\]~g;

        $message =~ s~\<br\>~ <br>~g;
        $message =~ s~\<pipe\>~\|~g;
        $message =~ s~\[hr\]\n~<hr size="1">~g;
        $message =~ s~\[hr\]~<hr size="1">~g;

        $message =~ s~\[b\]~<b>~isg;
        $message =~ s~\[\/b\]~</b>~isg;

        $message =~ s~\[i\]~<i>~isg;
        $message =~ s~\[\/i\]~</i>~isg;

        $message =~ s~\[u\]~<u>~isg;
        $message =~ s~\[\/u\]~</u>~isg;

        if ($imageicons eq "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<a href="$1" target="_blank"><img src="$1" width="50" height="50" alt="" border="0"></a>~isg;
                }
        if ($imageicons ne "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<img src="$1" alt="" border="0">~isg;
                }

        $message =~ s~\[color=(\S+?)\]~<font color="$1">~isg;
        $message =~ s~\[\/color\]~</font>~isg;

        $message =~ s~\[quote\]<br>(.+?)<br>\[\/quote\]~<blockquote><hr align=left width=40%>$1<hr align=left width=40%></blockquote>~isg;
        $message =~ s~\[quote\](.+?)\[\/quote\]~<blockquote><hr align=left width=40%><b>$1</b><hr align=left width=40%></blockquote>~isg;

        $message =~ s~\[fixed\]~<font face="Courier New">~isg;
        $message =~ s~\[\/fixed\]~</font>~isg;

        $message =~ s~\[sup\]~<sup>~isg;
        $message =~ s~\[\/sup\]~</sup>~isg;

        $message =~ s~\[strike\]~<strike>~isg;
        $message =~ s~\[\/strike\]~</strike>~isg;

        $message =~ s~\[sub\]~<sub>~isg;
        $message =~ s~\[\/sub\]~</sub>~isg;

        $message =~ s~\[left\]~<div align="left">~isg;
        $message =~ s~\[\/left\]~</div>~isg;
        $message =~ s~\[center\]~<center>~isg;
        $message =~ s~\[\/center\]~</center>~isg;
        $message =~ s~\[right\]~<div align="right">~isg;
        $message =~ s~\[\/right\]~</div>~isg;

        $message =~ s~\[list\]~<ul>~isg;
        $message =~ s~\[\*\]~<li>~isg;
        $message =~ s~\[\/list\]~</ul>~isg;

        $message =~ s~\[pre\]~<pre>~isg;
        $message =~ s~\[\/pre\]~</pre>~isg;

        $message =~ s~\[code\](.+?)\[\/code\]~<blockquote><font face="Courier New">code:</font><hr align=left width=40%><font face="Courier New"><pre>$1</pre></font><hr align=left width=40%></blockquote>~isg;

        $message =~ s~\[email\](.+?)\[\/email\]~<a href="mailto:$1">$1</a>~isg;

        $message =~ s~\[url\]www\.\s*(.+?)\s*\[/url\]~<a href="http://www.$1" target="_blank">www.$1</a>~isg;
        $message =~ s~\[url=\s*(\w+\://.+?)\](.+?)\s*\[/url\]~<a href="$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url=\s*(.+?)\]\s*(.+?)\s*\[/url\]~<a href="http://$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url\]\s*(.+?)\s*\[/url\]~<a href="$1" target="_blank">$1</a>~isg;

        $message =~ s~([^\w\"\=\[\]]|[\n\b]|\A)\\*(\w+://[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="$2" target="_blank">$2</a>~isg;
        $message =~ s~([^\"\=\[\]/\:\.]|[\n\b]|\A)\\*(www\.[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="http://$2" target="_blank">$2</a>~isg;

        $message =~ s~\{\{~\[~g;
        $message =~ s~\}\}~\]~g;
}

############
sub imxundoubbc {
############

        $message =~ s~\[font=(.+?)\]~<font face="$1">~isg;
             $message =~ s~\[\/font\]~</font>~isg;

              $message =~ s~\[size=(.+?)\]~<font size="$1">~isg;
            $message =~ s~\[\/size\]~</font>~isg;

        $message =~ s~\[\[~\{\{~g;
        $message =~ s~\]\]~\}\}~g;
        $message =~ s~\n\[~\[~g;
        $message =~ s~\]\n~\]~g;

        $message =~ s~\<br\>~ <br>~g;
        $message =~ s~\<pipe\>~\|~g;
        $message =~ s~\[hr\]\n~<hr size="1">~g;
        $message =~ s~\[hr\]~<hr size="1">~g;

        $message =~ s~\[b\]~<b>~isg;
        $message =~ s~\[\/b\]~</b>~isg;

        $message =~ s~\[i\]~<i>~isg;
        $message =~ s~\[\/i\]~</i>~isg;

        $message =~ s~\[u\]~<u>~isg;
        $message =~ s~\[\/u\]~</u>~isg;

        if ($imageicons eq "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<a href="$1" target="_blank"><img src="$1" width="50" height="50" alt="" border="0"></a>~isg;
                }
        if ($imageicons ne "1") {
                $message =~ s~\[img\](.+?)\[\/img\]~<img src="$1" alt="" border="0">~isg;
                }

        $message =~ s~\[color=(\S+?)\]~<font color="$1">~isg;
        $message =~ s~\[\/color\]~</font>~isg;

        $message =~ s~\[quote\]<br>(.+?)<br>\[\/quote\]~<blockquote><hr align=left width=40%>$1<hr align=left width=40%></blockquote>~isg;
        $message =~ s~\[quote\](.+?)\[\/quote\]~<blockquote><hr align=left width=40%><b>$1</b><hr align=left width=40%></blockquote>~isg;

        $message =~ s~\[fixed\]~<font face="Courier New">~isg;
        $message =~ s~\[\/fixed\]~</font>~isg;

        $message =~ s~\[sup\]~<sup>~isg;
        $message =~ s~\[\/sup\]~</sup>~isg;

        $message =~ s~\[strike\]~<strike>~isg;
        $message =~ s~\[\/strike\]~</strike>~isg;

        $message =~ s~\[sub\]~<sub>~isg;
        $message =~ s~\[\/sub\]~</sub>~isg;

        $message =~ s~\[left\]~<div align="left">~isg;
        $message =~ s~\[\/left\]~</div>~isg;
        $message =~ s~\[center\]~<center>~isg;
        $message =~ s~\[\/center\]~</center>~isg;
        $message =~ s~\[right\]~<div align="right">~isg;
        $message =~ s~\[\/right\]~</div>~isg;

        $message =~ s~\[list\]~<ul>~isg;
        $message =~ s~\[\*\]~<li>~isg;
        $message =~ s~\[\/list\]~</ul>~isg;

        $message =~ s~\[pre\]~<pre>~isg;
        $message =~ s~\[\/pre\]~</pre>~isg;

        $message =~ s~\[code\](.+?)\[\/code\]~<blockquote><font face="Courier New">code:</font><hr align=left width=40%><font face="Courier New"><pre>$1</pre></font><hr align=left width=40%></blockquote>~isg;

        $message =~ s~\[email\](.+?)\[\/email\]~<a href="mailto:$1">$1</a>~isg;

        $message =~ s~\[url\]www\.\s*(.+?)\s*\[/url\]~<a href="http://www.$1" target="_blank">www.$1</a>~isg;
        $message =~ s~\[url=\s*(\w+\://.+?)\](.+?)\s*\[/url\]~<a href="$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url=\s*(.+?)\]\s*(.+?)\s*\[/url\]~<a href="http://$1" target="_blank">$2</a>~isg;
        $message =~ s~\[url\]\s*(.+?)\s*\[/url\]~<a href="$1" target="_blank">$1</a>~isg;

        $message =~ s~([^\w\"\=\[\]]|[\n\b]|\A)\\*(\w+://[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="$2" target="_blank">$2</a>~isg;
        $message =~ s~([^\"\=\[\]/\:\.]|[\n\b]|\A)\\*(www\.[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="http://$2" target="_blank">$2</a>~isg;

        $message =~ s~\{\{~\[~g;
        $message =~ s~\}\}~\]~g;
}


sub jumplist {

my ($page) = @_;

print qq~
<form name="jump">
$imx{'059'}<select name="menu" onChange="location=document.jump.menu.options[document.jump.menu.selectedIndex].value;" value="GO">
<option value="#">-- $imx{'051'} --</option>
~;


if ($page ne "inbox") { print qq~<option value="$pageurl/$cgi?action=im">My Inbox</option>~; }
if ($page ne "sent") { print qq~<option value="$pageurl/$cgi?action=imfolder">Sent Message's</option>~; }
if ($page ne "saved") { print qq~<option value="$pageurl/$cgi?action=saveim">Saved Message's</option>~; }


open(FILE, "<$memberdir/adminim/folder/$username.txt");
        file_lock(FILE);
        my @folder = <FILE>;
        unfile_lock(FILE);
        close(FILE);
        $imxmnum = @folder;
        @folder = (sort { lc($a) cmp lc($b) } @folder);
 foreach $line (@folder) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[0] eq "") { }
           else { print qq~<option value="$pageurl/$cgi?action=messagefolder&folder=$item[0]">$item[0]</option>\n~; }
}
print qq~
<option value="$pageurl/$cgi?action=folder">$btn{'015'} $imx{'051'}</option>~;


if($access[35] eq "on"){
print qq~<option value="$pageurl/$cgi?action=messageadmin">IM Admin</option>~;
}
print qq~
</select>
</form>
~;

}

1; # return true