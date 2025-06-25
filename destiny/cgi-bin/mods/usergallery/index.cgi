#!/usr/bin/perl
# CollapsedSubs: createalbum
###############################################################################

$| = 1;

use CGI::Carp qw(fatalsToBrowser);
use File::Copy;

### the following must be correct or else this script won't work ###
require "../../config.pl"; # WebAPP config
require "./usergallery.cfg"; # User Gallery config
require "$usergalleryadmindir/ugsetup.dat"; # User Gallery settings
######

# do not modify anything below this line unless you know what you are doing!

eval {
        require "$sourcedir/subs.pl";
        require "$usergallerydir/language/english.dat";
        require "$usergallerydir/ugplugin.pl";

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

getlanguage();
ban();
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

# Compatability Checks #
if ($shownewalbum eq "") {$shownewalbum = "0";}
if ($shownewpicture eq "") {$shownewpicture = "0";}
if ($showhotpicture eq "") {$showhotpicture = "0";}
if ($approvalaccess eq "") {$approvalaccess = "0";}
########################

# User Gallery Mod by Floyd #

ugplugin1();
exit;

######################
sub doorway {
######################

  $navbar = "$btn{'014'} $ug{'001'}";
                print_top();

print qq~
The Gallery has been disabeled.<BR>
It will be opened agine at a later time.
~;

                 print_bottom();
                exit;

}

######################
sub doorwayB {
######################

checkaccess(view);

if ($info{'page'} eq "") { $pagenum = 1; }  else { $pagenum = $info{'page'}; }

        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $counter = @cats;

                $navbar = "$btn{'014'} $ug{'001'}";
                print_top();
                print qq~<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
<td align="center" class="articlecattitle">~;

if (@cats ne "0") { print qq~$ug{'002'}~; }
else { print qq~$ug{'003'}~; }

print qq~
</td>
</tr>
<tr>
<td class="newstextsmall" align="center">~;

$numofpages = $counter / $maxperpage;
if ($numofpages > int ($numofpages)) { $numofpages = int ($numofpages) +1; } else { $numofpages = int ($numofpages); }
if ($numofpages > 1) {
        print qq~<br>$msg{'039'}&nbsp;~;
        for ( $i = 1 ; $i <= $numofpages ; $i++) {
                if ( $i == $pagenum ) { print qq~<b>$i</b>&nbsp;~ ; }
                else { print qq~<a href="$usergalleryurl/index.cgi?page=$i" class="smallnewslink">$i</a>&nbsp~; }
        }
}

print qq~</td></tr></table>
<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
~;

                for ($i = (($pagenum * $maxperpage) - ($maxperpage - 1)) - 1; $i <= (($pagenum * $maxperpage)) - 1; $i++) {
                        if ($i <= $counter) {
                        @item = split (/\|/, $cats[$i]);
                        if ($item[0] ne "") {
                        open(FILE, "$usergallerydb/$item[0].cat");
                        file_lock(FILE);
                        chomp(@albums = <FILE>);
                        unfile_lock(FILE);
                        close(FILE);
                        $albumnumber = 0;
                        foreach $aline (@albums) {
                              $aline =~ s/[\n\r]//g;
                                                $albumnumber++;
                                                }
                        $newalbummarker = "";
                        $date2 = $date; $date1 = $item[3];        calcdifference();
                        if ($result < $shownewalbum) { $newalbummarker = "<br><img src=\"$imagesurl/forum/new.gif\" border=\"0\">"; }

                        if ($albumnumber eq "0") {
print qq~
<td align="center" class="newstextsmall" valign="top">
<img src="$usergallerygfxurl/albumempty.gif" border="0" width="38" height="40" alt="$item[1]"><br>
<b>$item[1]</b> ($albumnumber)<br>
~;

if ($username eq $item[2]) {$allowpicpost = "1";}
else {$allowpicpost = $item[4];}


#if ($allowpicpost eq "1" && $allowaction > 1 && $username ne $anonuser && $username ne "admin") {
#print qq~<a href="$usergalleryurl/index.cgi?action=addpicture&amp;album=$item[0]">
#<img src="$usergallerygfxurl/photo.gif" border="0" width="16" height="13" alt="$ug{'004'}"></a>~;}
# if ($username eq $item[2] && $username ne "admin") {
#print qq~&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=editalbum&album=$item[0]">
#<img src="$usergallerygfxurl/editalbum.gif" border="0" width="16" height="13" alt="$ug{'005'}">
#</a>&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=removealbum&album=$item[0]">
#<img src="$usergallerygfxurl/deletealbum.gif" border="0" width="16" height="13" alt="$ug{'006'}"></a>~;
#}

if ($settings[7] eq "Administrator") {
print qq~<a href="$usergalleryurl/index.cgi?action=addpicture&amp;album=$item[0]">
<img src="$usergallerygfxurl/photo.gif" border="0" width="16" height="13" alt="$ug{'004'}">
</a>&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=editalbum&album=$item[0]">
<img src="$usergallerygfxurl/editalbum.gif" border="0" width="16" height="13" alt="$ug{'005'}">
</a>&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=removealbum&album=$item[0]">
<img src="$usergallerygfxurl/deletealbum.gif" border="0" width="16" height="13" alt="$ug{'006'}"></a>~;
}

print qq~$newalbummarker</td>~;


}
else {

print qq~
<td align="center" class="newstextsmall" valign="top">
<a href="$usergalleryurl/index.cgi?action=openalbum&amp;album=$item[0]&amp;albumname=$item[1]">
<img src="$usergallerygfxurl/album.gif" border="0" width="38" height="40" alt="$item[1]"></a>
<br><b>$item[1]</b> ($albumnumber)<br>
~;


#if ($username eq $item[2]) {$allowpicpost = "1";}
#else {$allowpicpost = $item[4];}
#if ($allowpicpost eq "1" && $allowaction > 1 && $username ne $anonuser && $username ne "admin") {
#print qq~<a href="$usergalleryurl/index.cgi?action=addpicture&amp;album=$item[0]">
#<img src="$usergallerygfxurl/photo.gif" border="0" width="16" height="13" alt="$ug{'004'}"></a>~;
#}
#if ($username eq $item[2] && $username ne "admin") {
#print qq~&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=editalbum&album=$item[0]">
#<img src="$usergallerygfxurl/editalbum.gif" border="0" width="16" height="13" alt="$ug{'005'}"></a>
#&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=removealbum2&album=$item[0]">
#<img src="$usergallerygfxurl/deletealbum.gif" border="0" width="16" height="13" alt="$ug{'006'}"></a>
#~;
#}


if ($settings[7] eq "Administrator") {

print qq~
<a href="$usergalleryurl/index.cgi?action=addpicture&amp;album=$item[0]">
<img src="$usergallerygfxurl/photo.gif" border="0" width="16" height="13" alt="$ug{'004'}"></a>
&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=editalbum&album=$item[0]">
<img src="$usergallerygfxurl/editalbum.gif" border="0" width="16" height="13" alt="$ug{'005'}"></a>
&nbsp;&nbsp;<a href="$usergalleryurl/index.cgi?action=removealbum&album=$item[0]">
<img src="$usergallerygfxurl/deletealbum.gif" border="0" width="16" height="13" alt="$ug{'006'}"></a>~;

}

print qq~$newalbummarker</td>~;
                        }

                        $count++;
                        if ($count == 4) {
                                print qq~</tr><br><tr>~;
                                $count = 0;
                                }
                        }
                        }
                }

print qq~
</table>~;

#if ($allowaction > 3 && $username ne $anonuser) {
#print qq~<br>
#<table align="center" border="0" cellpadding="3" cellspacing="0">
#<tr>
#<td><hr width="200"></td>
#</tr>
#<tr>
#<td align="center"><a href="$usergalleryurl/index.cgi?action=createalbum" class="smallnewslink">$ug{'007'}</a></td>
#</tr>
#</table>~; }

if ($settings[7] eq "Administrator") { #$allowaction < 4 &&
print qq~<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">
<tr>
<td><hr width="200"></td>
</tr>
<tr>
<td align="center"><a href="$usergalleryurl/index.cgi?action=createalbum" class="smallnewslink">$ug{'007'}</a></td>
</tr>
~;
 }

if ($settings[7] eq "Administrator") {
print qq~<tr><td align="center"><a href="$usergalleryurl/admin/admin.cgi" class="smallnewslink">$ug{'008'}</a></td></tr>~;
}

print qq~</table>~;

                print_bottom();
                exit;

}

########################
sub createalbum {
########################

checkaccess(create);

        $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $ug{'007'}";
        print_top();
        print qq~<table>
<form onSubmit="submitonce(this)" action="$usergalleryurl/index.cgi?action=createalbum2" method="post">
<tr>
<td>$ug{'009'}&nbsp;</td>
<td><input type="text" name="desc" size="20" maxlength="20"></td>
</tr>
<!--
<tr>
<td>$ug{'010'}&nbsp;</td>
<td><input type="checkbox" name="access">&nbsp;<small>$ug{'011'}</small></td>
</tr>
-->
<tr>
<td>&nbsp;</td>
<td><input class='button' type="submit" value="$ug{'012'}"></td>
</tr>
</form>
</table>
~;
        print_bottom();
        exit;

}

########################
sub createalbum2 {
########################

checkaccess(create);

if ($input{'desc'} ne "") {

                opendir (DIR, "$usergallerydb");
                @files = readdir(DIR);
                closedir (DIR);
                @files = grep(/cat/,@files);
                @files = reverse(sort { $a <=> $b } @files);
                $newalbumnumber = @files[0];
                $newalbumnumber =~ s/.cat//;
                $newalbumnumber++;

        if ($input{'access'} eq "on") {$accesstype = 1;} else {$accesstype = "0";}

        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        @cats = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$usergallerydb/cats.dat") || error("$err{'016'} $usergallerydb/cats.dat");
        file_lock(FILE);
        print FILE "$newalbumnumber|$input{'desc'}|$username|$date|$accesstype\n";
        print FILE @cats;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$usergallerydb/$newalbumnumber.cat");
        file_lock(FILE);
        print FILE "";
        unfile_lock(FILE);
        close(FILE);

}

        print "Location: $usergalleryurl/index.cgi\n\n";
        exit;

}

########################
sub openalbum {
########################

checkaccess(view);

if ($info{'page'} eq "") { $pagenum = 1; }  else { $pagenum = $info{'page'}; }
if ($info{'albumname'} eq "" && $info{'msg'} eq "0") {$info{'albumname'} = "$ug{'013'}";}
if ($info{'albumname'} eq "" && $info{'msg'} eq "1") {$info{'albumname'} = "$ug{'013'}";}
if ($info{'albumname'} eq "" && $info{'msg'} eq "2") {$info{'albumname'} = "$ug{'014'}";}
if ($info{'albumname'} eq "" && $info{'msg'} eq "3") {$info{'albumname'} = "$ug{'015'}";}

        open(FILE, "$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        chomp(@pics = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $counter = @pics;
        $counter = $counter-1;
        if ($counter < 1) {$counter = 1;}

                $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $info{'albumname'}";
                print_top();
                print qq~<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
<td align="center" class="articlecattitle">~;

if (@pics ne "0") { print qq~$ug{'016'}~; }
else { print qq~$ug{'017'}~; }

print qq~</td>
</tr>
<tr>
<td class="newstextsmall" align="center"><a href="$usergalleryurl/index.cgi" class="smallnewslink">$ug{'018'}</a>~;

$numofpages = $counter / $maxperpage;
if ($numofpages > int ($numofpages)) { $numofpages = int ($numofpages) +1; } else { $numofpages = int ($numofpages); }
if ($numofpages > 1) {
        print qq~<br>$msg{'039'}&nbsp;~;
        for ( $i = 1 ; $i <= $numofpages ; $i++) {
                if ( $i == $pagenum ) { print qq~<b>$i</b>&nbsp;~ ; }
                else { print qq~<a href="$usergalleryurl/index.cgi?action=openalbum&amp;album=$info{'album'}&amp;page=$i&amp;albumname=$info{'albumname'}" class="smallnewslink">$i</a>&nbsp~; }
        }
}

print qq~</td></tr>~;

if ($info{'msg'} eq 1) {print qq~<tr><td align="center"><font color="#ff0000"><b>$ug{'019'}</b></font></td></tr>~;}
if ($info{'msg'} eq 2) {print qq~<tr><td align="center"><font color="#ff0000"><b>$ug{'020'}</b></font></td></tr>~;}

print qq~</table>
<table border="0" cellpadding="3" cellspacing="0" width="100%">
<tr>
~;
                for ($i = (($pagenum * $maxperpage) - ($maxperpage - 1)) - 1; $i < ($pagenum * $maxperpage); $i++) {
                        if ($i <= $counter) {
                        @item = split (/\|/, $pics[$i]);
                        if ($item[0] ne "") {
                        $pictureowner = $item[1];
                        if ($item[5] eq "") {$item[5] = "0";}
                        $picmarker = "";
                        if ($showhotpicture ne "0") {
                                 if ($item[5] > $showhotpicture) {$picmarker = "<img src=\"$usergallerygfxurl/hotpic.gif\" border=\"0\" width=\"28\" height=\"11\" alt=\"$item[5] $ug{'047'}\">";}
                        }
                        $date2 = $date; $date1 = $item[4];        calcdifference();
                        if ($result < $shownewpicture) { $picmarker = "<img src=\"$usergallerygfxurl/newpic.gif\" border=\"0\" width=\"28\" height=\"11\" alt=\"$ug{'046'}\">"; }

print qq~
<td align="center" class="newstextsmall" valign="top">
<a href="$usergalleryurl/index.cgi?action=showpicture&album=$info{'album'}&id=$item[0]&picturename=$item[2]&albumname=$info{'albumname'}">
<img src="$usergalleryimagesurl/$item[3]" border="0" width="100" height="100" alt="$item[2]"></a><br>
$picmarker $item[2] ($item[5])<br>~;


 if ($settings[7] eq "Administrator") {
print qq~<a href="$usergalleryurl/index.cgi?action=editpicture&album=$info{'album'}&id=$item[0]">
<img src="$usergallerygfxurl/editphoto.gif" border="0" width="16" height="13" alt="$ug{'021'}"></a>
&nbsp;<a href="$usergalleryurl/index.cgi?action=movepicture&album=$info{'album'}&id=$item[0]">
<img src="$usergallerygfxurl/movephoto.gif" border="0" width="16" height="13" alt="$ug{'022'}">&nbsp;
<a href="$usergalleryurl/index.cgi?action=removepicture&album=$info{'album'}&id=$item[0]">
<img src="$usergallerygfxurl/deletephoto.gif" border="0" width="16" height="13" alt="$ug{'023'}"></a>~;
 }

#if ($pictureowner eq $username && $username ne "admin") {
#print qq~
#<a href="$usergalleryurl/index.cgi?action=editpicture&album=$info{'album'}&id=$item[0]">
#<img src="$usergallerygfxurl/editphoto.gif" border="0" width="16" height="13" alt="$ug{'021'}"></a>
#&nbsp;<a href="$usergalleryurl/index.cgi?action=movepicture&album=$info{'album'}&id=$item[0]">
#<img src="$usergallerygfxurl/movephoto.gif" border="0" width="16" height="13" alt="$ug{'022'}">&nbsp;
#<a href="$usergalleryurl/index.cgi?action=removepicture&album=$info{'album'}&id=$item[0]">
#<img src="$usergallerygfxurl/deletephoto.gif" border="0" width="16" height="13" alt="$ug{'023'}"></a>~;
# }


print qq~</td>~;




                        $count++;
                        if ($count == 4) {
                                print qq~</tr><br><tr>~;
                                $count = 0;
                        }
                        }
                        }
                }

print qq~
</table>
<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">~;

        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        @categories = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        foreach $curcat (@categories) {
                $curcat =~ s/[\n\r]//g;
                @curitem = split (/\|/, $curcat);

                                                 if ($curitem[0] ne $info{'album'}) { next; }
                                                 else {$albumowner = $curitem[2]; $allowpicpost = $curitem[4];}
        }

#if ($albumowner eq $username && $username ne "admin") {print qq~<tr><td><hr width="200"></td></tr><tr><td align="center"><a href="$usergalleryurl/index.cgi?action=addpicture&amp;album=$info{'album'}" class="smallnewslink">$ug{'004'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=editpicture&album=$info{'album'}&id=$info{'id'}" class="smallnewslink">$ug{'021'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=editalbum&album=$info{'album'}" class="smallnewslink">$ug{'005'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=removealbum&album=$info{'album'}" class="smallnewslink">$ug{'006'}</a>~;
#}

#if ($allowpicpost eq "1" && $albumowner ne $username && $username ne "admin" && $username ne $anonuser) {print qq~<tr><td><hr width="200"></td></tr><tr><td align="center"><a href="$usergalleryurl/index.cgi?action=addpicture&amp;album=$info{'album'}" class="smallnewslink">$ug{'004'}</a>~;
#}

if ($settings[7] eq "Administrator") {
print qq~<tr><td><hr width="200"></td></tr><tr><td align="center"><a href="$usergalleryurl/index.cgi?action=addpicture&amp;album=$info{'album'}" class="smallnewslink">$ug{'004'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=editalbum&album=$info{'album'}" class="smallnewslink">$ug{'005'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=removealbum&album=$info{'album'}" class="smallnewslink">$ug{'006'}</a>~;
print qq~&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=createalbum" class="smallnewslink">$ug{'007'}</a>~;
}

#if ($allowaction > 3 && $username ne $anonuser) {
#print qq~&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=createalbum" class="smallnewslink">$ug{'007'}</a>~;
#}

#if ($allowaction < 4 && $settings[7] eq "Administrator") {
#print qq~&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=createalbum" class="smallnewslink">$ug{'007'}</a>~;
#}

print qq~</td>
</tr></table>
~;

                print_bottom();
                exit;

}

########################
sub showpicture {
########################

checkaccess(view);

        open(FILE, "$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        @pics = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $piccount = @pics;
        $piccount = $piccount+1;

        foreach $curpic (@pics) {
                $curpic =~ s/[\n\r]//g;
                @pitem = split (/\|/, $curpic);

        if ($pitem[0] ne $info{'id'}) { next; }
        else {

        $pictureowner = $pitem[1];
        $prevpic = $pitem[0]-1;
        $nextpic = $pitem[0]+1;
        if ($prevpic < 1) {$prevpic = "none";}
        if ($nextpic > ($piccount-1)) {$nextpic = "none";}
        if ($nextpic ne "none") {$prevlink = "<a href=\"$usergalleryurl/index.cgi?action=showpicture&amp;album=$info{'album'}&amp;id=$nextpic&amp;albumname=$info{'albumname'}\">$ug{'024'}</a>";} else {$prevlink = "";}
        if ($prevpic ne "none") {$nextlink = "&nbsp;|&nbsp;<a href=\"$usergalleryurl/index.cgi?action=showpicture&amp;album=$info{'album'}&amp;id=$prevpic&amp;albumname=$info{'albumname'}\">$ug{'025'}</a>";} else {$nextlink = "";}
        if ($prevlink eq "" && $prevpic ne "none") {$nextlink = "<a href=\"$usergalleryurl/index.cgi?action=showpicture&amp;album=$info{'album'}&amp;id=$prevpic&amp;albumname=$info{'albumname'}\">$ug{'025'}</a>";}

        open(FILE, "$memberdir/$pitem[1].dat");
        file_lock(FILE);
        @usgalsettings = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $info{'albumname'} $btn{'014'} $pitem[2]";
        print_top();

        print qq~
        <table align="center" border="0" cellpadding="3" cellspacing="0">
        <tr>
        <td align="center" class="newstextsmall">
        <a href="$usergalleryurl/index.cgi" class="smallnewslink">$ug{'018'}</a>
        &nbsp;-&nbsp;
        <a href="$usergalleryurl/index.cgi?action=openalbum&amp;album=$info{'album'}&amp;albumname=$info{'albumname'}" class="smallnewslink">$info{'albumname'} $ug{'026'}</a>~;
        if ($nextlink ne "") { print qq~&nbsp;&gt;&nbsp;$prevlink$nextlink~;}
        print qq~
        </td>
        </tr>~;

        open(FILE, "$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        @countpics = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$usergallerydb/$info{'album'}.cat") || error("$err{'016'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        foreach $curcountpic (@countpics) {
                $curcountpic =~ s/[\n\r]//g;
        ($cnum, $cpicturesender, $cpicturename, $cpicturefile, $cpicturedate, $cpicturecount) = split(/\|/, $curcountpic);
        if ($cnum eq $info{'id'}) {
        if ($cpicturecount eq "") {$cpicturecount = 0;}
        $newpicturecount = $cpicturecount+1;
        print FILE "$cnum|$cpicturesender|$cpicturename|$cpicturefile|$cpicturedate|$newpicturecount\n";
        } else {print FILE "$cnum|$cpicturesender|$cpicturename|$cpicturefile|$cpicturedate|$cpicturecount\n";}
        }
        unfile_lock(FILE);
        close(FILE);

        $pitem[5] = $newpicturecount;

        $picmarker = "";
        if ($showhotpicture ne "0") {
                if ($pitem[5] > $showhotpicture) {$picmarker = "<img src=\"$usergallerygfxurl/hotpic.gif\" border=\"0\" width=\"28\" height=\"11\" alt=\"$pitem[5] $ug{'047'}\">";}
        }
        $date2 = $date; $date1 = $pitem[4];        calcdifference();
        if ($result < $shownewpicture) { $picmarker = "<img src=\"$usergallerygfxurl/newpic.gif\" border=\"0\" width=\"28\" height=\"11\" alt=\"$ug{'046'}\">"; }

        display_date($pitem[4]); $pitem[4] = $user_display_date;

        print qq~<tr>
        <td align="center" class="newstextsmall"><img src="$usergalleryimagesurl/$pitem[3]" border="0" alt="$pitem[2]"></td></tr><tr><td align="center" class="newstextsmall">$pitem[2] $picmarker</td></tr><tr><td align="center" class="newstextsmall">$ug{'027'}~; if ($username ne $anonuser) {print qq~<a href="$pageurl/$cgi?action=viewprofile&amp;username=$pitem[1]" class="smallnewslink">$usgalsettings[1]</a>~; } else {print qq~<b>$usgalsettings[1]</b>~; } print qq~$ug{'028'}$pitem[4]<br>$ug{'044'} $pitem[5]~;
        }

        }

        print qq~
        </td>
        </tr>
        </table>~;

#if ($pictureowner eq $username && $username ne "admin") {print qq~
#<br>
#<table align="center" border="0" cellpadding="3" cellspacing="0">
#<tr>
#<td><hr width="200"></td>
#</tr>
#<tr>
#<td align="center"><a href="$usergalleryurl/index.cgi?action=editpicture&album=$info{'album'}&id=$info{'id'}" class="smallnewslink">$ug{'021'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=movepicture&album=$info{'album'}&id=$info{'id'}" class="smallnewslink">$ug{'022'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=removepicture&album=$info{'album'}&id=$info{'id'}" class="smallnewslink">$ug{'023'}</a></td>
#</tr>
#</table>
#~;
#}

if ($settings[7] eq "Administrator") {print qq~
<br>
<table align="center" border="0" cellpadding="3" cellspacing="0">
<tr>
<td><hr width="200"></td>
</tr>
<tr>
<td align="center"><a href="$usergalleryurl/index.cgi?action=editpicture&album=$info{'album'}&id=$info{'id'}" class="smallnewslink">$ug{'021'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=movepicture&album=$info{'album'}&id=$info{'id'}" class="smallnewslink">$ug{'022'}</a>&nbsp;-&nbsp;<a href="$usergalleryurl/index.cgi?action=removepicture&album=$info{'album'}&id=$info{'id'}" class="smallnewslink">$ug{'023'}</a></td>
</tr>
</table>
~;
}

        print_bottom();
        exit;

}

########################
sub addpicture {
########################

checkaccess(post);

        if ($info{'album'} eq "") {
        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        @thecategories = <FILE>;
        unfile_lock(FILE);
        close(FILE);

                foreach $curcat (@thecategories) {
                        $curcat =~ s/[\n\r]//g;
                        @catitem = split(/\|/, $curcat);
                        if ($catitem[4] eq "1") {
                                $boardlist="$boardlist<option value=\"$catitem[0]\">$catitem[1]</option>";
                        }
                }
        }

        $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $ug{'004'}";
        print_top();
        print qq~
        <table cellpadding="3" cellspacing="1" border="0" align="center" width="100%">
        <tr>
        <td colspan="2" align="center" class="articlecattitle">$ugrule{'001'}<br>$ugrule{'002'}<br>$ugrule{'003'}<br>$ugrule{'004'}~; if ($allowaction < 6) {print qq~<br>$ugrule{'005'}~;}
        print qq~</td>
        <tr>
        <td align="center">&nbsp;</td>
        </tr>
        <form onSubmit="submitonce(this)" METHOD="POST" ACTION="$usergalleryurl/ugupload.cgi" ENCTYPE="multipart/form-data">
        <INPUT TYPE="HIDDEN" NAME="USERID" value="$username">
        <INPUT TYPE="HIDDEN" NAME="DATEID" value="$date">
        <TR>
        <TD align="left" width="20%" class="articlecattitle">$ug{'029'}</TD><TD align="left" width="80%"><INPUT TYPE="FILE" NAME="FILE1" size="40"></TD>
        </TR>
        <TR>
        <TD align="left" width="20%" class="articlecattitle">$ug{'032'}</TD><TD align="left" width="80%"><INPUT TYPE="TEXT" NAME="PICTURENAME" size="40" maxlength="30"></TD>
        </TR>~;
        if ($info{'album'} eq "") {
        print qq~<TR>
        <TD align="left" width="20%" class="articlecattitle">Album:</TD><TD><select name="ALBUMID">$boardlist</select></TD>
        </TR>~;
        } else {
        print qq~<INPUT TYPE="HIDDEN" NAME="ALBUMID" value="$info{'album'}">~;
        }
        print qq~<tr>
        <td align="center">&nbsp;</td>
        </tr>
        <TR>
        <TD colspan="2" align="center" class="articlecattitle"><INPUT class='button' TYPE="SUBMIT" VALUE="$ug{'030'}"></TD>
        </TR>
        </FORM>
        </table>~;

print_bottom();
exit;

}

########################
sub addpicture2 {
########################

checkaccess(post);

if ($info{'description'} eq "") {$info{'description'} = "$ug{'034'}";}

        $allowactionold = $allowaction;

        if ($settings[7] eq "Administrator") {

        $imgtoget = "";

        open(FILE, "$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        @pics = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        @picsgetnum = reverse(sort { $a <=> $b } @pics);
        $num = @picsgetnum[0];
        $num =~ s/\.//;
        $num++;;

                opendir (DIR, "$usergalleryimagesdir");
                @files = readdir(DIR);
                closedir (DIR);
                @files = reverse(sort { $a <=> $b } @files);
                $newpostnum = @files[0];
                $newpostnum =~ s/\.//;
                $newpostnum++;

        $newfilename = $info{'filename'};
        ($dummy, $ext) = split(/\./, $newfilename);
        $newfilename = "$newpostnum.$ext";

        open(FILE, ">$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        print FILE "$num|$info{'sendername'}|$info{'description'}|$newfilename|$date|0\n";
        print FILE @pics;
        unfile_lock(FILE);
        close(FILE);

                         $dirtoget = "$usergalleryimagesdir";
                         $dirtoget = "$usergalleryimagesdir/pending";
                         $dirtogo = "$usergalleryimagesdir";
                         $imgtoget = "$info{'filename'}";

                        copy("$dirtoget/$imgtoget", "$dirtogo/$newfilename");
                        unlink("$dirtoget/$imgtoget");

        open (FILE, "$usergallerydb/newugs.dat");
                file_lock(FILE);
                @threads = <FILE>;
                unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$usergallerydb/newugs.dat");
                file_lock(FILE);
                for ($a = 0; $a < @threads; $a++) {
                        ($nnum, $nalbumtogo, $nsendername, $ndescription, $nfilename, $ndate) = split(/\|/,$threads[$a]);
                        if ($nnum eq $info{'picid'}) { print FILE ""; }
                        else { print FILE "$threads[$a]"; }
                }
                unfile_lock(FILE);
        close(FILE);

        $info{'msg'} = "0";
        }

        $allowaction = $allowactionold;

        print "Location: $usergalleryurl/index.cgi?action=openalbum&album=$info{'album'}&msg=$info{'msg'}\n\n";
        exit;

}

########################
sub editpicture {
########################

checkaccess(post);

        open(FILE, "$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        @pics = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        foreach $curpic (@pics) {
                        $curpic =~ s/[\n\r]//g;
                        @item = split(/\|/, $curpic);
                        if ($item[0] eq $info{'id'}) {$thispictureowner = $item[1]; $thispicturename = $item[2]; }
        }

        #if ($username ne "admin") {
        #         if ($thispictureowner ne $username) {error("$err{'011'}");}
        #}

        $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $ug{'035'}";
        print_top();
        print qq~<table>
<form onSubmit="submitonce(this)" action="$usergalleryurl/index.cgi?action=editpicture2" method="post">
<tr>
<td>$ug{'032'}&nbsp;</td>
<td><input type="text" name="desc" size="30" maxlength="30" value="$thispicturename"></td>
</tr>
<tr>
<td><input type="hidden" name="editedpicture" value="$info{'id'}"><input type="hidden" name="editedpicturealbum" value="$info{'album'}">&nbsp;</td>
<td><input class='button' type="submit" value="$ug{'035'}"></td>
</tr>
</form>
</table>
~;
        print_bottom();
        exit;

}

########################
sub editpicture2 {
########################

checkaccess(create);

        open(FILE, "$usergallerydb/$input{'editedpicturealbum'}.cat") || error("$err{'001'} $usergallerydb/$input{'editedpicturealbum'}.cat");
        file_lock(FILE);
        @pics = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$usergallerydb/$input{'editedpicturealbum'}.cat") || error("$err{'016'} $usergallerydb/$input{'editedpicturealbum'}.cat");
        file_lock(FILE);
        foreach $curpic (@pics) {
                $curpic =~ s/[\n\r]//g;
        ($num, $picturesender, $picturename, $picturefile, $picturedate, $picturescore) = split(/\|/, $curpic);
        if ($num eq $input{'editedpicture'}) {
        print FILE "$num|$picturesender|$input{'desc'}|$picturefile|$picturedate|$picturescore\n";
        } else {print FILE "$num|$picturesender|$picturename|$picturefile|$picturedate|$picturescore\n";}
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $usergalleryurl/index.cgi?action=showpicture&album=$input{'editedpicturealbum'}&id=$input{'editedpicture'}\n\n";
        exit;

}

########################
sub movepicture {
########################

checkaccess(post);

        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        @categories = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $curcatid="$info{'album'}";
                foreach $curcat (@categories) {
                        $curcat =~ s/[\n\r]//g;
                        @item = split(/\|/, $curcat);
                        if ($item[2] eq $username) {
                        if($item[0] ne "$curcatid") {
                                $boardlist="$boardlist<option value=\"$item[0]\">$item[1]</option>";
                        }
                        }
                }

        if ($boardlist eq "") {
        $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $ug{'036'}";
        print_top();
        print qq~<table>
        <tr><td><b>$ug{'037'}</b></td></tr>
        </table>
        ~;
        } else {
        $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $ug{'036'}";
        print_top();
        print qq~<table>
        <form onSubmit="submitonce(this)" action="$usergalleryurl/index.cgi?action=movepicture2" method="post">
        <tr><td><b>$ug{'038'}</b> <select name="toalbum">$boardlist</select>
        <input type="hidden" name="picid" value="$info{'id'}">
        <input type="hidden" name="oldalbum" value="$info{'album'}">
        &nbsp;&nbsp;<input class='button' type="submit" value="$ug{'036'}">
        </td></tr>
        </form></table>
        ~;
        }

        print_bottom();
        exit;

}

########################
sub movepicture2 {
########################

checkaccess(post);

        $picfound = 0;
        open (FILE, "$usergallerydb/$input{'oldalbum'}.cat") || error("$err{'001'} $usergallerydb/$input{'oldalbum'}.cat");
        file_lock(FILE);
        @oldpics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$usergallerydb/$input{'oldalbum'}.cat") || error("$err{'016'} $usergallerydb/$input{'oldalbum'}.cat");
        file_lock(FILE);
        foreach $curpic (@oldpics) {
                $curpic =~ s/[\n\r]//g;
                ($num, $mpicturesender, $mpicturename, $mpicturefile, $mpicturedate, $mpicturescore) = split(/\|/,$curpic);
                if ($num ne $input{'picid'}) {if ($picfound eq 0) {$nnum = $num-1;} else {$nnum = $num;} print FILE "$nnum|$mpicturesender|$mpicturename|$mpicturefile|$mpicturedate|$mpicturescore\n"; }
                if ($num eq $input{'picid'}) {
                         $picfound = 1;
                         $linetowrite = "$num|$mpicturesender|$mpicturename|$mpicturefile|$mpicturedate|$mpicturescore";
                         print FILE "";
                }
        }
        unfile_lock(FILE);
        close(FILE);

        open (FILE, "$usergallerydb/$input{'toalbum'}.cat") || error("$err{'001'} $usergallerydb/$input{'toalbum'}.cat");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        ($newnum, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $threads[0]);
        $newnum++;

        ($dummy, $mpicturesender, $mpicturename, $mpicturefile, $mpicturedate, $mpicturescore) = split(/\|/, $linetowrite);

        open (FILE, ">$usergallerydb/$input{'toalbum'}.cat") || error("$err{'016'} $usergallerydb/$input{'toalbum'}.cat");
        file_lock(FILE);
        print FILE "$newnum|$mpicturesender|$mpicturename|$mpicturefile|$mpicturedate|$mpicturescore\n";
        print FILE @threads;
        unfile_lock(FILE);
        close(FILE);

        print "Location: $usergalleryurl/index.cgi?action=openalbum&album=$input{'toalbum'}&msg=3\n\n";
        exit;

}

########################
sub removepicture {
########################

checkaccess(post);

print_top();
        print qq~$ug{'039'}<br>
<a href="$usergalleryurl/index.cgi?action=removepicture2&album=$info{'album'}&id=$info{'id'}">$nav{'047'}</a> - <a href="$usergalleryurl/index.cgi">$nav{'048'}</a>
~;
        print_bottom();
        exit;

}

########################
sub removepicture2 {
########################

checkaccess(post);

        $imgtoget = "";
        $picfound = 0;

        open(FILE, "$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        @pics = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        foreach $curpic (@pics) {
                $curpic =~ s/[\n\r]//g;

                ($num, $sendername, $picturename, $filename, $adddate, $rpicturescore) = split(/\|/, $curpic);

        if ($num ne $info{'id'}) { if ($picfound eq 0) {$nnum = $num-1;} else {$nnum = $num;} print FILE "$nnum|$sendername|$picturename|$filename|$adddate|$rpicturescore\n"; }
        if ($num eq $info{'id'}) {
                         $picfound = 1;
                         print FILE "";
                         $dirtoget = "$usergalleryimagesdir";
                         $imgtoget = "$item[3]";
                         unlink("$dirtoget/$imgtoget");
        }
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $usergalleryurl/index.cgi?action=openalbum&album=$info{'album'}\n\n";
        exit;

}

########################
sub editalbum {
########################

checkaccess(create);

        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        @cats = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        foreach $curcat (@cats) {
        $curcat =~ s/[\n\r]//g;
        ($num, $albumname, $albumcreator, $dummy, $albumaccess) = split(/\|/, $curcat);
        if ($num eq $info{'album'}) { $thisalbumname = $albumname; $thisalbumcreator = $albumcreator; $thisalbumaccess = $albumaccess; }
        }

        #if ($username ne "admin") {
        #         if ($username ne $thisalbumcreator) {error("$err{'011'}");}
        #}

        if ($thisalbumaccess eq "1") {$accesschecked = " checked";
        } else {$accesschecked = "";}

        $navbar = "$btn{'014'} $ug{'001'} $btn{'014'} $ug{'040'} $btn{'014'} $thisalbumname";
        print_top();
        print qq~<table>
<form onSubmit="submitonce(this)" action="$usergalleryurl/index.cgi?action=editalbum2" method="post">
<tr>
<td>$ug{'009'}&nbsp;</td>
<td><input type="text" name="desc" size="20" maxlength="20" value="$thisalbumname"></td>
</tr>
<tr>
<td>$ug{'010'}&nbsp;</td>
<td><input type="checkbox" name="access"$accesschecked>&nbsp;<small>$ug{'011'}</small></td>
</tr>
<tr>
<td><input type="hidden" name="editedalbum" value="$info{'album'}">&nbsp;</td>
<td><input class='button' type="submit" value="$ug{'040'}"></td>
</tr>
</form>
</table>
~;
        print_bottom();
        exit;

}

########################
sub editalbum2 {
########################

checkaccess(create);

        if ($input{'access'} eq "on") {$accesstype = 1;} else {$accesstype = "0";}

        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        @cats = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$usergallerydb/cats.dat") || error("$err{'016'} $usergallerydb/cats.dat");
        file_lock(FILE);
        foreach $curcat (@cats) {
                $curcat =~ s/[\n\r]//g;
        ($num, $albumname, $albumcreator, $albumdate, $albumaccess) = split(/\|/, $curcat);
        if ($num eq $input{'editedalbum'}) {
        print FILE "$num|$input{'desc'}|$albumcreator|$albumdate|$accesstype\n";
        } else {print FILE "$num|$albumname|$albumcreator|$albumdate|$albumaccess\n";}
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $usergalleryurl/index.cgi\n\n";
        exit;

}

########################
sub removealbum {
########################

checkaccess(create);

print_top();
        print qq~$ug{'041'}<br>
<a href="$usergalleryurl/index.cgi?action=removealbum2&album=$info{'album'}">$nav{'047'}</a> - <a href="$usergalleryurl/index.cgi">$nav{'048'}</a>
~;
        print_bottom();
        exit;

}

########################
sub removealbum2 {
########################

checkaccess(create);

        $imgtoget = "";

        open(FILE, "$usergallerydb/$info{'album'}.cat") || error("$err{'001'} $usergallerydb/$info{'album'}.cat");
        file_lock(FILE);
        @pics = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        foreach $curpic (@pics) {
                $curpic =~ s/[\n\r]//g;
                @item = split (/\|/, $curpic);

                         $dirtoget = "$usergalleryimagesdir";
                         $imgtoget = "$item[3]";
                         unlink("$dirtoget/$imgtoget");
        }

        unlink("$usergallerydb/$info{'album'}.cat");

        open(FILE, "$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        @albums = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$usergallerydb/cats.dat") || error("$err{'001'} $usergallerydb/cats.dat");
        file_lock(FILE);
        foreach $curalbum (@albums) {
                $curalbum =~ s/[\n\r]//g;
                @item = split (/\|/, $curalbum);

        if ($item[0] ne $info{'album'}) { print FILE "$curalbum\n"; }

        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $usergalleryurl/index.cgi\n\n";
        exit;

}

########################
sub checkaccess {
########################

my ($actrequest) = @_;

#if ($allowaction eq 0) {
#                                                                  if ($username ne "admin" && $actrequest eq "create") { error("$err{'011'}"); }
#                                                                 if ($username ne "admin" && $actrequest eq "post") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "view") { error("noguests"); }
#}

#if ($allowaction eq 1) {

if ($settings[7] ne "Administrator" && $actrequest eq "create") { error("$err{'011'}"); }
if ($settings[7] ne "Administrator" && $actrequest eq "post") { error("$err{'011'}"); }

#if ($username ne "admin" && $actrequest eq "create") { error("$err{'011'}"); }
#if ($username ne "admin" && $actrequest eq "post") { error("$err{'011'}"); }
#}

#if ($allowaction eq 2) {
#                                                                  if ($username ne "admin" && $actrequest eq "create") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "post") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "view") { error("noguests"); }
#}

#if ($allowaction eq 3) {
#                                                                  if ($username ne "admin" && $actrequest eq "create") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "post") { error("$err{'011'}"); }
#}

#if ($allowaction eq 4) {
#                                                                  if ($username eq $anonuser && $actrequest eq "create") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "post") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "view") { error("noguests"); }
#}

#if ($allowaction eq 5) {
#                                                                  if ($username eq $anonuser && $actrequest eq "create") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "post") { error("noguests"); }
#}

#if ($allowaction eq 6) {
#                                                                  if ($username eq $anonuser && $actrequest eq "create") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "post") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "view") { error("noguests"); }
#}

#if ($allowaction eq 7) {
#                                                                  if ($username eq $anonuser && $actrequest eq "create") { error("$err{'011'}"); }
#                                                                 if ($username eq $anonuser && $actrequest eq "post") { error("$err{'011'}"); }
#}

}

1;