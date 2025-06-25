###############################################################################

###############
sub siteadmin {
###############
        #check_access(siteadmin);
        #$access_granted = 0;

         $navbar = "$btn{'014'} $nav{'042'}";
         print_top();

print qq~
<TABLE BORDER="0" CELLPADDING="2" WIDTH="100%">
  <TR>
    <TD><HR COLOR=blue><B>Site Admin</B><BR>
        <HR COLOR=blue>
    </TD>
    <TD><HR COLOR=blue><B>Security Admin</B><BR>
        <HR COLOR=blue>
    </TD>
    <TD><HR COLOR=blue><B>User Admin</B><BR>
        <HR COLOR=blue>
    </TD>
  </TR>
  <TR>
    <TD ROWSPAN="3" VALIGN="Top">

~;

if ($access[35] eq "on") { print qq~<a href="$pageurl/$admin&op=siteconfig">$mnu{'001'}</a><br>~; }

if ($access[0] eq "on") { print qq~<a href="$pageurl/$admin&op=welcomemsg">$mnu{'002'}</a><br>~; }

if ($access[2] eq "on") { print qq~<a href="$pageurl/$admin&op=guestwelcomemsg">Edit Guest Welcome message</a><br>~; }

if ($welcome_im eq "0") { print qq~$mnu{'003'}<br>~; }
else { #check_access(editim);
if ($access[6] eq "on") { print qq~<a href="$pageurl/$admin&amp;op=welcomeim">$mnu{'003'}</a><br>~; }
}
if ($access[27] eq "on") { print qq~<a href="$scripturl/admin/links/linksadmin.cgi">$mnu{'007'}</a><br>~; }

if ($access[35] eq "on") { print qq~<a href="$scripturl/mods/modmanager.cgi">$mnu{'042'}</a><br>~; }

if ($access[4] eq "on") { print qq~<A HREF="$pageurl/mods/menuman/admin/admin.cgi">Edit Menus</A><BR>~; }

if ($access[7] eq "on") { print qq~<A HREF="$pageurl/mods/apage/apage.cgi">Page Admin</A><BR>~; }

if ($access[8] eq "on") { print qq~<a href="$scripturl/admin/blocks/left/view.cgi">$mnu{'021'}</a><br>
<a href="$scripturl/admin/blocks/right/view.cgi">$mnu{'022'}</a><br>~; }

if ($access[34] eq "on") { print qq~<a href="$pageurl/$admin&op=broadcast">Broadcast Message</a><br>~; }

print qq~</TD><TD VALIGN="Top">~;

if ($access[9] eq "on") { print qq~<a href="$pageurl/$admin&amp;op=editbanip">$mnu{'025'}</a><br>~; }

print qq~</TD><TD VALIGN="Top">~;


if ($access[35] eq "on") { print qq~<a href="$admin&amp;op=userstate">$mnu{'013'}</a><br>~; }
#<a href="$admin&amp;op=userranks">$mnu{'012'}</a><br>

if ($access[26] eq "on") { print qq~<a href="index.cgi?action=viewmasterlog">Site User Access Log's</A><br>~; }

print qq~

<a href="index.cgi?action=memberlist">Member List</A>

</TD>
  </TR>
  <TR>
    <TD><HR COLOR=blue><B>Forum Admin</B><BR>
        <HR COLOR=blue>
    </TD>
    <TD><HR COLOR=blue><B>Poll Admin</B><BR>
        <HR COLOR=blue>
    </TD>
  </TR>
  <TR>
    <TD VALIGN="Top">

~;

if ($access[10] eq "on") { print qq~<a href="$pageurl/$admin&amp;op=managecats">$mnu{'014'}</a><br>~; }

if ($access[12] eq "on") { print qq~<a href="$pageurl/$admin&amp;op=manageboards">$mnu{'015'}</a><br>~; }

if ($access[11] eq "on") { print qq~<a href="$pageurl/$admin&amp;op=setcensor">$mnu{'016'}</a><br>~; }



print qq~

</TD>
    <TD VALIGN="Top">

~;

if ($access[14] eq "on") { print qq~<a href="$pageurl/$admin&amp;op=polladmin">$mnu{'017'}</a>~; }


print qq~

</TD>
  </TR>
  <TR>
    <TD><HR COLOR=blue><B>News Admin</B><BR>
        <HR COLOR=blue>
    </TD>
    <TD></TD>
    <TD></TD>
  </TR>
  <TR>
    <TD VALIGN="Top">

~;

if ($access[1] eq "on") { print qq~<a href="$pageurl/index.cgi?action=postnews">Add News</A><BR>~; }

if ($access[3] eq "on") { print qq~<a href="$pageurl/$admin&amp;op=modifynews">$mnu{'019'}</a><br>
<a href="$pageurl/$admin&amp;op=topicadmin">$mnu{'020'}</a><br>~; }


print qq~

</TD>
    <TD VALIGN="Top"></TD>
    <TD VALIGN="Top"></TD>
</TR>

</TABLE>
~;


        print_bottom();
        exit;
}


################
sub siteconfig {
################
if ($access[35] ne "on") { error("$err{'011'}"); }


$navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $mnu{'001'}";
print_top();

if ($mailtype eq 1) {$mailtype = "on"; $mailchecked = "checked" } else {$mailtype = "off"; $mailchecked = "unchecked"}
if ($showban eq 1) {$showban = "on"; $showbanchecked = "checked" } else {$showban = "off"; $showbanchecked = "unchecked"}
if ($showcon eq 1) {$showcon = "on"; $showconchecked = "checked" } else {$showcon = "off"; $showconchecked = "unchecked"}
if ($showcon2 eq 1) {$showcon2 = "on"; $showcon2checked = "checked" } else {$showcon2 = "off"; $showcon2checked = "unchecked"}
if ($welcome_im eq 1) {$welcome_im = "on"; $welcome_imchecked = "checked" } else {$welcome_im = "off"; $welcome_imchecked = "unchecked"}
if ($newuser_im eq 1) {$newuser_im = "on"; $newuser_imchecked = "checked" } else {$newuser_im = "off"; $newuser_imchecked = "unchecked"}
if ($article_im eq 1) {$article_im = "on"; $article_imchecked = "checked" } else {$article_im = "off"; $article_imchecked = "unchecked"}
if ($enable_userarticles eq 1) {$enable_userarticles = "on"; $enable_userarticleschecked = "checked" } else {$enable_userarticles = "off"; $enable_userarticleschecked = "unchecked"}
if ($allow_html eq 1) {$allow_html = "on"; $allow_htmlchecked = "checked" } else {$allow_html = "off"; $allow_htmlchecked = "unchecked"}
if ($enable_guestposting eq 1) {$enable_guestposting = "on"; $enable_guestpostingchecked = "checked" } else {$enable_guestposting = "off"; $enable_guestpostingchecked = "unchecked"}
if ($enable_notification eq 1) {$enable_notification = "on"; $enable_notificationchecked = "checked" } else {$enable_notification = "off"; $enable_notificationchecked = "unchecked"}
if ($insert_original eq 1) {$insert_original = "on"; $insert_originalchecked = "checked" } else {$insert_original = "off"; $insert_originalchecked = "unchecked"}
if ($enable_ubbc eq 1) {$enable_ubbc = "on"; $enable_ubbcchecked = "checked" } else {$enable_ubbc = "off"; $enable_ubbcchecked = "unchecked"}
if ($enable_smile eq 1) {$enable_smile = "on"; $enable_smilechecked = "checked" } else {$enable_smile = "off"; $enable_smilechecked = "unchecked"}
if ($top_browsers eq 1) {$top_browsers = "on"; $top_browserschecked = "checked" } else {$top_browsers = "off"; $top_browserschecked = "unchecked"}
if ($top_os eq 1) {$top_os = "on"; $top_oschecked = "checked" } else {$top_os = "off"; $top_oschecked = "unchecked"}
if ($adminonlyl eq 1) {$adminonlyl = "on"; $adminonlylchecked = "checked" } else {$adminonlyl = "off"; $adminonlylchecked = "unchecked"}
if ($antileech eq 1) {$antileech = "on"; $antileechchecked = "checked" } else {$antileech = "off"; $antileechchecked = "unchecked"}
if ($adminonlyd eq 1) {$adminonlyd = "on"; $adminonlydchecked = "checked" } else {$adminonlyd = "off"; $adminonlydchecked = "unchecked"}
if ($modulecal eq 1) {$modulecal = "on"; $modulecalchecked = "checked" } else {$modulecal = "off"; $modulecalchecked = "unchecked"}
if ($modulenl eq 1) {$modulenl = "on"; $modulenlchecked = "checked" } else {$modulenl = "off"; $modulenlchecked = "unchecked"}
if ($modulenlmem eq 1) {$modulenlmem = "on"; $modulenlmemchecked = "checked" } else {$modulenlmem = "off"; $modulenlmemchecked = "unchecked"}
if ($botkiller eq 1) {$botkiller = "on"; $botkillerchecked = "checked" } else {$botkiller = "off"; $botkillerchecked = "unchecked"}
if ($multiplevoting eq 1) {$multiplevoting = "on"; $multiplevotingchecked = "checked" } else {$multiplevoting = "off"; $multiplevotingchecked = "unchecked"}
if ($pollmod eq 1) {$pollmod = "on"; $pollmodchecked = "checked" } else {$pollmod = "off"; $pollmodchecked = "unchecked"}
if ($use_flock eq 1) {$use_flock = "on"; $use_flockchecked = "checked" } else {$use_flock = "off"; $use_flockedchecked = "unchecked"}
if ($hidemail eq 1) { $hidemail = "on"; $hidemailchecked = "checked" } else {$hidemail = "off"; $hidemailchecked = "unchecked"}
if ($enable_topicguestposting eq 1) { $enable_topicguestposting = "on"; $enable_topicguestpostingchecked = "checked" } else {$enable_topicguestposting = "off"; $enable_topicguestpostingchecked = "unchecked"}
if ($enable_autopublish eq 1) { $enable_autopublish = "on"; $enable_autopublishchecked = "checked" } else {$enable_autopublish = "off"; $enable_autopublishchecked = "unchecked"}
if ($dispmost eq 1) { $dispmost = "on"; $dispmostchecked = "checked" } else {$dispmost = "off"; $dispmostchecked = "unchecked"}
if ($letmemdel eq 1) { $letmemdel = "on"; $letmemdelchecked = "checked" } else {$letmemdel = "off"; $letmemdelchecked = "unchecked"}
if ($letmemlng eq 1) { $letmemlng = "on"; $letmemlngchecked = "checked" } else {$letmemlng = "off"; $letmemlngchecked = "unchecked"}
if ($letmemthm eq 1) { $letmemthm = "on"; $letmemthmchecked = "checked" } else {$letmemthm = "off"; $letmemthmchecked = "unchecked"}
if ($hidememlist eq 1) { $hidememlist = "on"; $hidememlistchecked = "checked" } else {$hidememlist = "off"; $hidememlistchecked = "unchecked"}
if ($imageicons eq 1) {$imageicons = "on"; $imageiconschecked = "checked" } else {$imageicons = "off"; $imageiconschecked = "unchecked"}
if ($editwelc eq 1) {$editwelc = "on"; $editwelcchecked = "checked" } else {$editwelc = "off"; $editwelcchecked = "unchecked"}
if ($editabout eq 1) {$editabout = "on"; $editaboutchecked = "checked" } else {$editabout = "off"; $editaboutchecked = "unchecked"}
if ($editim eq 1) {$editim = "on"; $editimchecked = "checked" } else {$editim = "off"; $editimchecked = "unchecked"}
if ($editbanner eq 1) {$editbanner = "on"; $editbannerchecked = "checked" } else {$editbanner = "off"; $editbannerchecked = "unchecked"}
if ($editfaq eq 1) {$editfaq = "on"; $editfaqchecked = "checked" } else {$editfaq = "off"; $editfaqchecked = "unchecked"}
if ($editdown eq 1) {$editdown = "on"; $editdownchecked = "checked" } else {$editdown = "off"; $editdownchecked = "unchecked"}
if ($editlink eq 1) {$editlink = "on"; $editlinkchecked = "checked" } else {$editlink = "off"; $editlinkchecked = "unchecked"}
if ($modadmin eq 1) {$modadmin = "on"; $modadminchecked = "checked" } else {$modadmin = "off"; $modadminchecked = "unchecked"}
if ($editcats eq 1) {$editcats = "on"; $editcatschecked = "checked" } else {$editcats = "off"; $editcatschecked = "unchecked"}
if ($editboards eq 1) {$editboards = "on"; $editboardschecked = "checked" } else {$editboards = "off"; $editboardschecked = "unchecked"}
if ($editcensor eq 1) {$editcensor = "on"; $editcensorchecked = "checked" } else {$editcensor = "off"; $editcensorchecked = "unchecked"}
if ($editpoll eq 1) {$editpoll = "on"; $editpollchecked = "checked" } else {$editpoll = "off"; $editpollchecked = "unchecked"}
if ($pubnews eq 1) {$pubnews = "on"; $pubnewschecked = "checked" } else {$pubnews = "off"; $pubnewschecked = "unchecked"}
if ($editnews eq 1) {$editnews = "on"; $editnewschecked = "checked" } else {$editnews = "off"; $editnewschecked = "unchecked"}
if ($edittops eq 1) {$edittops = "on"; $edittopschecked = "checked" } else {$edittops = "off"; $edittopschecked = "unchecked"}
if ($editlblk eq 1) {$editlblk = "on"; $editlblkchecked = "checked" } else {$editlblk = "off"; $editlblkchecked = "unchecked"}
if ($editrblk eq 1) {$editrblk = "on"; $editrblkchecked = "checked" } else {$editrblk = "off"; $editrblkchecked = "unchecked"}
if ($editcal eq 1) {$editcal = "on"; $editcalchecked = "checked" } else {$editcal = "off"; $editcalchecked = "unchecked"}
if ($editnl eq 1) {$editnl = "on"; $editnlchecked = "checked" } else {$editnl = "off"; $editnlchecked = "unchecked"}
if ($editip eq 1) {$editip = "on"; $editipchecked = "checked" } else {$editip = "off"; $editipchecked = "unchecked"}
if ($instantsignup eq 1) {$instantsignup = "on"; $instantsignupchecked = "checked" } else {$instantsignup = "off"; $instantsignupchecked = "unchecked"}
if ($topicimgupld eq 1) {$topicimgupld = "on"; $topicimgupldchecked = "checked" } else {$topicimgupld = "off"; $topicimgupldchecked = "unchecked"}
if ($forumimgupld eq 1) {$forumimgupld = "on"; $forumimgupldchecked = "checked" } else {$forumimgupld = "off"; $forumimgupldchecked = "unchecked"}
if ($showlatestlinks eq 1) {$showlatestlinks = "on"; $showlatestlinkschecked = "checked" } else {$showlatestlinks = "off"; $showlatestlinkschecked = "unchecked"}
if ($showlatestdownloads eq 1) {$showlatestdownloads = "on"; $showlatestdownloadschecked = "checked" } else {$showlatestdownloads = "off"; $showlatestdownloadschecked = "unchecked"}
if ($config_dir eq "") {$config_dir = "$scriptdir/conf";}

        print qq~<table border="0" width="100%">
        <form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$admin&amp;op=siteconfig2" method="post">~;
if ( $info{'area'} ne "general" && $info{'area'} ne "") { print qq~
        <input type="hidden" name="page_name" value="$pagename">
        <input type="hidden" name="page_url" value="$pageurl">
        <input type="hidden" name="page_title" value="$pagetitle">
        <input type="hidden" name="cgi" value="$cgi">
        <input type="hidden" name="cookieusername" value="$cookieusername">
        <input type="hidden" name="cookiepassword" value="$cookiepassword">
        <input type="hidden" name="cookieusertheme" value="$cookieusertheme">
        <input type="hidden" name="cookieuserlang" value="$cookieuserlang">
        <input type="hidden" name="mailtype" value="$mailtype">
        <input type="hidden" name="mailprog" value="$mailprogram">
        <input type="hidden" name="smtp_server" value="$smtp_server">
        <input type="hidden" name="base_dir" value="$basedir">
        <input type="hidden" name="base_url" value="$baseurl">
        <input type="hidden" name="script_url" value="$scripturl">
        <input type="hidden" name="script_dir" value="$scriptdir">
        <input type="hidden" name="lib_dir" value="$sourcedir">
        <input type="hidden" name="data_dir" value="$datadir">
        <input type="hidden" name="member_dir" value="$memberdir">
        <input type="hidden" name="images_dir" value="$imagesdir">
        <input type="hidden" name="themes_dir" value="$themesdir">
        <input type="hidden" name="images_url" value="$imagesurl">
        <input type="hidden" name="themes_url" value="$themesurl">
        <input type="hidden" name="default_lang" value="$language">
        <input type="hidden" name="lang_dir" value="$langdir">
        <input type="hidden" name="backup_lang" value="$lang">~;}
if ( $info{'area'} ne "contact") { print qq~
        <input type="hidden" name="compname" value="$compname">
        <input type="hidden" name="compadd" value="$compadd">
        <input type="hidden" name="compcity" value="$compcity">
        <input type="hidden" name="compstate" value="$compstate">
        <input type="hidden" name="compzip" value="$compzip">
        <input type="hidden" name="compphone" value="$compphone">
        <input type="hidden" name="compfax" value="$compfax">
        <input type="hidden" name="compemail" value="$compemail">
        <input type="hidden" name="webmaster_email" value="$webmaster_email">~;}
if ( $info{'area'} ne "im") { print qq~
        <input type="hidden" name="welcome_im" value="$welcome_im">
        <input type="hidden" name="newuser_im" value="$newuser_im">
        <input type="hidden" name="article_im" value="$article_im">
                <input type="hidden" name="bmheadercolor" value="$bmheadercolor">
        <input type="hidden" name="bmbgcolor" value="$bmbgcolor">~;}
if ( $info{'area'} ne "information") { print qq~
        <input type="hidden" name="image1" value="$image1">
        <input type="hidden" name="link1" value="$link1">
        <input type="hidden" name="image2" value="$image2">
        <input type="hidden" name="link2" value="$link2">
        <input type="hidden" name="image3" value="$image3">
        <input type="hidden" name="link3" value="$link3">~;}
if ( $info{'area'} ne "editorsdesk") { print qq~
        <input type="hidden" name="topic_dir" value="$topicsdir">
        <input type="hidden" name="maxnews" value="$maxnews">
        <input type="hidden" name="forumimgupld" value="$forumimgupld">
        <input type="hidden" name="topicimgupld" value="$topicimgupld">
        <input type="hidden" name="maxtopics" value="$maxtopics">
        <input type="hidden" name="enable_userarticles" value="$enable_userarticles">
        <input type="hidden" name="allow_html" value="$allow_html">
        <input type="hidden" name="enable_topicguestposting" value="$enable_topicguestposting">
        <input type="hidden" name="enable_autopublish" value="$enable_autopublish">
        <input type="hidden" name="article_imrecip" value="$article_imrecip">
        <input type="hidden" name="forum_dir" value="$boardsdir">
        <input type="hidden" name="message_dir" value="$messagedir">
        <input type="hidden" name="enable_guestposting" value="$enable_guestposting">
        <input type="hidden" name="enable_notification" value="$enable_notification">
        <input type="hidden" name="maxdisplay" value="$maxdisplay">
        <input type="hidden" name="maxmessagedisplay" value="$maxmessagedisplay">
        <input type="hidden" name="enable_ubbc" value="$enable_ubbc">
        <input type="hidden" name="enable_smile" value="$enable_smile">
        <input type="hidden" name="upload_dir" value="$uploaddir">
        <input type="hidden" name="upload_url" value="$uploadurl">
        <input type="hidden" name="maxuploadsize" value="$maxuploadsize">
        <input type="hidden" name="imageicons" value="$imageicons">
        <input type="hidden" name="insert_original" value="$insert_original">~;}
if ( $info{'area'} ne "stats") { print qq~
        <input type="hidden" name="max_log_days_old" value="$max_log_days_old">
        <input type="hidden" name="log_dir" value="$logdir">
        <input type="hidden" name="ip_time" value="$ip_time">
        <input type="hidden" name="top_browsers" value="$top_browsers">
        <input type="hidden" name="top_os" value="$top_os">~;}
if ( $info{'area'} ne "links") { print qq~
        <input type="hidden" name="links_dir" value="$linksdir">
        <input type="hidden" name="maxlinks" value="$maxlinks">
        <input type="hidden" name="adminonlyl" value="$adminonlyl">
        <input type="hidden" name="download_dir" value="$downloadsdir">
        <input type="hidden" name="maxdownloads" value="$maxdownloads">
        <input type="hidden" name="antileech" value="$antileech">
        <input type="hidden" name="adminonlyd" value="$adminonlyd">
        <input type="hidden" name="showlatestlinks" value="$showlatestlinks">
        <input type="hidden" name="showlatestdownloads" value="$showlatestdownloads">~;}
if ( $info{'area'} ne "others") { print qq~
        <input type="hidden" name="timeoffset" value="$timeoffset">
        <input type="hidden" name="memberpic_height" value="$memberpic_height">
        <input type="hidden" name="memberpic_width" value="$memberpic_width">
        <input type="hidden" name="use_flock" value="$use_flock">
        <input type="hidden" name="LOCK_EX" value="$LOCK_EX">
        <input type="hidden" name="LOCK_UN" value="$LOCK_UN">
        <input type="hidden" name="server_os" value="$server_os">
        <input type="hidden" name="IIS" value="$IIS">~;}
if ( $info{'area'} ne "access") { print qq~
        <input type="hidden" name="editwelc" value="$editwelc">
        <input type="hidden" name="editabout" value="$editabout">
        <input type="hidden" name="editim" value="$editim">
        <input type="hidden" name="editbanner" value="$editbanner">
        <input type="hidden" name="editfaq" value="$editfaq">
        <input type="hidden" name="editdown" value="$editdown">
        <input type="hidden" name="editlink" value="$editlink">
        <input type="hidden" name="modadmin" value="$modadmin">
        <input type="hidden" name="editcats" value="$editcats">
        <input type="hidden" name="editboards" value="$editboards">
        <input type="hidden" name="editcensor" value="$editcensor">
        <input type="hidden" name="editpoll" value="$editpoll">
        <input type="hidden" name="pubnews" value="$pubnews">
        <input type="hidden" name="editnews" value="$editnews">
        <input type="hidden" name="edittops" value="$edittops">
        <input type="hidden" name="editlblk" value="$editlblk">
        <input type="hidden" name="editrblk" value="$editrblk">
        <input type="hidden" name="editcal" value="$editcal">
        <input type="hidden" name="editnl" value="$editnl">
        <input type="hidden" name="editip" value="$editip">~;}
if ( $info{'area'} ne "assistant") { print qq~
        <input type="hidden" name="timezone" value="$timezone">
        <input type="hidden" name="showcon" value="$showcon">
        <input type="hidden" name="showcon2" value="$showcon2">
        <input type="hidden" name="dispmost" value="$dispmost">
        <input type="hidden" name="dispstat" value="$dispstat">
        <input type="hidden" name="dispinfo" value="$dispinfo">
        <input type="hidden" name="hidemail" value="$hidemail">
        <input type="hidden" name="letmemlng" value="$letmemlng">
        <input type="hidden" name="letmemdel" value="$letmemdel">
        <input type="hidden" name="letmemthm" value="$letmemthm">
        <input type="hidden" name="infoblockmod" value="$infoblockmod">
        <input type="hidden" name="searchmod" value="$searchmod">
        <input type="hidden" name="hidememlist" value="$hidememlist">
        <input type="hidden" name="dispfrad" value="$dispfrad">
        <input type="hidden" name="modulecal" value="$modulecal">
        <input type="hidden" name="modulenl" value="$modulenl">
        <input type="hidden" name="pollmod" value="$pollmod">
        <input type="hidden" name="multiplevoting" value="$multiplevoting">
        <input type="hidden" name="modulenlmem" value="$modulenlmem">
        <input type="hidden" name="botkiller" value="$botkiller">
        <input type="hidden" name="check_date" value="$check_date">
        <input type="hidden" name="signupmethod" value="$signupmethod">
        <input type="hidden" name="defaulttheme" value="$defaulttheme">~;}
print qq~

<caption class="texttitle">$msg{'223'}</caption>
  <tr>
    <td colspan="2">
                        <table border="0" cellpadding="1" cellspacing="0" width="100%" class="menubordercolor">
                                <tr align="center">
                                <td width="100%">
                                        <table border="0" width="100%" cellpadding="3" cellspacing="5" class="menubackcolor">
                                                <tr align="center">
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=general">$nav{'099'}</a></td>
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=im">$nav{'102'}</a></td>
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=contact">$nav{'100'}</a></td>
                                                </tr>
                                                <tr align="center">
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=editorsdesk">$nav{'004'}&nbsp;&amp;&nbsp;$nav{'003'}</a></td>
                                                          <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=stats">$nav{'106'}</a></td>~;
                                                        if ($infoblockmod eq "0") {print qq~
                                                        <td>$nav{'103'} ($msg{'426'})</td>~;}
                                                        else
                                                        {print qq~
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=information">$nav{'103'}</a></td>~;
                                                        }
                                                print qq~
                                                </tr>
                                                <tr align="center">
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=links">$nav{'107'}&nbsp;&amp;&nbsp;$nav{'108'}</a></td>
                                                        <td><a href="$scripturl/$cgi?action=backup">$nav{'111'}</a></td>
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=others">$nav{'113'}</a></td>
                                                </tr>
                                                <tr align="center">
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=assistant">$nav{'112'}</a></td>
                                                          <td>&nbsp;</td>
                                                        <td><a href="$scripturl/$cgi?action=admin&amp;op=siteconfig&amp;area=access">$nav{'162'}</a></td>
                                                </tr>
                                        </table>
                                        <table width="100%" cellpadding="0" cellspacing="0" class="menubackcolor">
                                                <tr><td><br><hr><input type="hidden" name="config_dir" value="$config_dir"></td></tr>
                                                <tr>
                                                        <td align="center"><input type="submit" value="$btn{'021'}"></td>
                                                </tr>
                                                <tr><td colspan="2" class="textsmall" valign="bottom" align="center">$msg{'197'}</td><tr>
                                        </table>
                                </td>
                                </tr>
                        </table>
                </td>
  </tr>

~;


if ( $info{'area'} eq "general" || $info{'area'} eq "") { general_options();}
elsif ( $info{'area'} eq "contact") { contact_options();}
elsif ( $info{'area'} eq "im") { im_options();}
elsif ( $info{'area'} eq "information") { information_options();}
elsif ( $info{'area'} eq "editorsdesk") { editorsdesk_options();}
elsif ( $info{'area'} eq "stats") { stats_options();}
elsif ( $info{'area'} eq "links") { links_options();}
elsif ( $info{'area'} eq "assistant") { admin_assistant();}
elsif ( $info{'area'} eq "backup") { backup();}
elsif ( $info{'area'} eq "others") { others_options();}
elsif ( $info{'area'} eq "access") { admin_access();}
else { print "$err{'006'}";}

        print_bottom();
        exit;
}

#################
sub siteconfig2 {
#################
if ($access[35] ne "on") { error("$err{'011'}"); }

$config_dir = $input{'config_dir'};

@list_of_checkboxes=(
        'mailtype',
        'showban',
        'showcon',
        'showcon2',
        'welcome_im',
        'newuser_im',
        'article_im',
        'enable_userarticles',
        'allow_html',
        'enable_guestposting',
        'enable_notification',
        'insert_original',
        'enable_ubbc',
        'enable_smile',
        'top_browsers',
        'top_os',
        'adminonlyl',
        'antileech',
        'adminonlyd',
        'modulecal',
        'modulenl',
        'modulenlmem',
        'botkiller',
        'multiplevoting',
        'pollmod',
        'use_flock',
        'hidemail',
        'enable_topicguestposting',
        'enable_autopublish',
        'dispmost',
        'letmemdel',
        'letmemlng',
        'letmemthm',
        'hidememlist',
        'imageicons',
        'editwelc',
        'editabout',
        'editim',
        'editbanner',
        'editfaq',
        'editdown',
        'editlink',
        'modadmin',
        'editcats',
        'editboards',
        'editcensor',
        'editpoll',
        'pubnews',
        'editnews',
        'edittops',
        'editlblk',
        'editrblk',
        'editcal',
        'editnl',
        'editip',
        'topicimgupld',
        'forumimgupld',
        'showlatestdownloads',
        'showlatestlinks');

foreach $thing (@list_of_checkboxes) {
$input{$thing}=$input{$thing} eq 'on'?1:0;
}

&saveConfig(\%input);
print "Location: $pageurl/$admin\&op=siteconfig\n\n";
exit;

}

################
sub broadcast {
################

if ($access[34] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/broadcast.txt") || error("$err{'001'} $datadir/broadcast.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $nav{'042'} $btn{'014'} Edit Broadcast Message";

$message = htmltotext($lines[1]);

        print_top();

        print qq~<form onSubmit="submitonce(this)"  action="$pageurl/$admin&op=broadcast2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
<INPUT TYPE="checkbox" NAME="broadcastcheck" VALUE="on"
~;
if ($lines[0] eq "on") { print "   CHECKED"; }
print qq~
>Broadcast Message On
</td>
</tr>
<tr>
<td>
Broadcast Message:<br>
<textarea name="message" cols="40" rows="10">$message</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}"><input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
        print_bottom();
        exit;
}

#################
sub broadcast2 {
#################
if ($access[34] ne "on") { error("$err{'011'}"); }

        chomp($input{'message'});
        $message = htmlescape($input{'message'});

        open(FILE, ">$datadir/broadcast.txt") || error("$err{'016'} $datadir/broadcast.txt");
        file_lock(FILE);
        print FILE "$input{'broadcastcheck'}\n";
        print FILE "$message\n";
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=broadcast\n\n";
}

################
sub welcomemsg {
################

if ($access[0] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/welcomemsg.txt") || error("$err{'001'} $datadir/welcomemsg.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $subject = htmltotext($lines[0]);
        $message = htmltotext($lines[1]);

        $navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $mnu{'002'}";
        print_top();
        print qq~<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=welcomemsg2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
$nav{'071'}:<br>
<input type="text" name="subject" value="$subject" size="40">
</td>
</tr>
<tr>
<td>
$nav{'072'}:<br>
<textarea name="message" cols="40" rows="10">$message</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}"><input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
        print_bottom();
        exit;
}

#################
sub welcomemsg2 {
#################
if ($access[0] ne "on") { error("$err{'011'}"); }
        error("$err{'014'}") unless ($input{'subject'});
        error("$err{'015'}") unless ($input{'message'});

        chomp($input{'subject'});
        chomp($input{'message'});

        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});

        open(FILE, ">$datadir/welcomemsg.txt") || error("$err{'016'} $datadir/welcomemsg.txt");
        file_lock(FILE);
        print FILE "$subject\n";
        print FILE "$message\n";
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=welcomemsg\n\n";
}

################
sub guestwelcomemsg {
################
if ($access[2] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/welcomemsg2.txt") || error("$err{'001'} $datadir/welcomemsg2.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $subject = htmltotext($lines[0]);
        $message = htmltotext($lines[1]);

        $navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $mnu{'002'}";
        print_top();
        print qq~<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=guestwelcomemsg2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
$nav{'071'}:<br>
<input type="text" name="subject" value="$subject" size="40">
</td>
</tr>
<tr>
<td>
$nav{'072'}:<br>
<textarea name="message" cols="40" rows="10">$message</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}"><input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
        print_bottom();
        exit;
}



#################
sub guestwelcomemsg2 {
#################
if ($access[2] ne "on") { error("$err{'011'}"); }

        error("$err{'014'}") unless ($input{'subject'});
        error("$err{'015'}") unless ($input{'message'});

        chomp($input{'subject'});
        chomp($input{'message'});

        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});

        open(FILE, ">$datadir/welcomemsg2.txt") || error("$err{'016'} $datadir/welcomemsg2.txt");
        file_lock(FILE);
        print FILE "$subject\n";
        print FILE "$message\n";
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=guestwelcomemsg\n\n";
}

################
sub viewlog {
################

if ($access[0] ne "on") { error("$err{'011'}"); }


open(FILE, "$memberdir/$info{'username'}.log") || error("$err{'001'} $memberdir/$info{'username'}.log");
        file_lock(FILE);
        @data = <FILE>;
        unfile_lock(FILE);
        close(FILE);
$log = "@data";

$log =~ s/\n/<BR>/gi;


        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

$navbar = "$btn{'014'} View $mymemsettings[1]'s Log File.";

        print_top();
print qq~

<table border="0">
<tr>
<td class="formstexttitle" colspan="2">$mymemsettings[1]'s Log File</td>
</TR>
</TABLE>
<TABLE BORDER=0 CELLPADDING="2">
  <TR>
    <TD>$log</TD>
  </TR>
</TABLE>

~;
        print_bottom();

        exit;
}

################
sub viewmasterlog {
################
$navbar = "$btn{'014'} View Log File's.";
$files_found = "FALSE";
        print_top();
print qq~

<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Log File's</td>
</TR>
</TABLE>
<TABLE BORDER=0 CELLPADDING="2">
  <TR>
    <TD>~;



       opendir(DIR,"$datadir/logs");
        @dir=readdir(DIR);
        @dir = sort {uc($a) cmp uc($b)} @dir;
        closedir(DIR);
        foreach $line (@dir) {
                if (-f "$datadir/logs/$line" && $line ne "." && $line ne "..") {
                        $files_found = "TRUE";
                }
        }


        if ($files_found) {
                #@dir = sort {lc($a) cmp lc($b)} @dir;
                @dir = sort { $b <=> $a } @dir;
                foreach $line (@dir) {


                        if (-f "$datadir/logs/$line") {
                                #@stat=stat("$config{'root_dir'}/$current_dir/$line");
                                $file_name=$line;
                                ($name,$ext)=split(/\./,$file_name);
                                $ext=lc($ext);
                                if ($name ne "") {
                                if ($ext eq "dat") {
                                ($lmonth,$lday,$lyear)=split(/\-/,$name);
                                print qq~ <A HREF="index.cgi?action=viewmasterlogb&visitdate=$name">View Log from $lmonth/$lday/$lyear</A><BR> ~;
                                }
                                }
                        }
                 }


}

print qq~
    </TD>
  </TR>
</TABLE>

~;
        print_bottom();

        exit;
}

################
sub viewmasterlogb {
################

if ($access[0] ne "on") { error("$err{'011'}"); }


open(FILE, "$datadir/logs/$info{'visitdate'}.dat") || error("$err{'001'} $datadir/logs/$info{'visitdate'}.dat");
        file_lock(FILE);
        @data = <FILE>;
        unfile_lock(FILE);
        close(FILE);
$log = "@data";

$log =~ s/\|/<\/TD><TD>/gi;
$log =~ s/\n/<\/TD><\/TR><TR><TD>/gi;

$log = "<TR><TD>$log";

$navbar = "$btn{'014'} View Log File from $info{'visitdate'}.";

        print_top();
print qq~

<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Log File from $info{'visitdate'}</td>
</TR>
</TABLE>
<TABLE BORDER BGCOLOR="#FFFFFF" CELLSPACING="0" CELLPADDING="2" WIDTH='70%"'>
  <TR>
    <TD BGCOLOR="#C0C0C0"><P ALIGN=Center>
      <B>Username</B></TD>
    <TD BGCOLOR="#C0C0C0"><P ALIGN=Center>
      <B>Ip Address</B></TD>
    <TD BGCOLOR="#C0C0C0"><P ALIGN=Center>
      <B>Date and Time</B></TD>
    <TD BGCOLOR="#C0C0C0"><P ALIGN=Center>
      <B>Hits</B></TD>
  </TR>

    $log


</TABLE>
<P>
<BR>
~;
        print_bottom();

        exit;
}



################
sub agreement {
################
if ($access[35] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/agreement.txt") || error("$err{'001'} $datadir/agreement.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        $agreement = htmltotext($lines[0]);

        $navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $mnu{'044'}";
        print_top();
        print qq~<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=agreement2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
$msg{'665'}:<br>
<textarea name="agreement" cols="40" rows="10">$agreement</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}"><input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
        print_bottom();
        exit;
}

#################
sub agreement2 {
#################
if ($access[35] ne "on") { error("$err{'011'}"); }
        error("$err{'015'}") unless ($input{'agreement'});

        chomp($input{'agreement'});


        $agreement = htmlescape($input{'agreement'});

        open(FILE, ">$datadir/agreement.txt") || error("$err{'016'} $datadir/agreement.txt");
        file_lock(FILE);
        print FILE "$agreement\n";
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=agreement\n\n";
}

########## Shawn Raloff 3/29/02 Edited and Fixed by Carter #######
################
sub aboutinfo {
################
if ($access[35] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/aboutinfo.txt") || error("$err{'001'} $datadir/aboutinfo.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $subject = htmltotext($lines[0]);
        $message = htmltotext($lines[1]);

        $navbar = "$btn{'014'} $mnu{'039'}";
        print_top();
        print qq~<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=aboutinfo2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
$nav{'157'}<br>
<input type="text" name="subject" value="$subject" size="40">
</td>
</tr>
<tr>
<td>
$nav{'158'}<br>
<textarea name="message" cols="40" rows="10">$message</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}">&nbsp;<input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
        print_bottom();
        exit;
}


#################
sub aboutinfo2 {
#################
if ($access[35] ne "on") { error("$err{'011'}"); }

        error("$err{'014'}") unless ($input{'subject'});
        error("$err{'015'}") unless ($input{'message'});

        chomp($input{'subject'});
        chomp($input{'message'});

        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});

        open(FILE, ">$datadir/aboutinfo.txt") || error("$err{'016'} $datadir/aboutinfo.txt");
        file_lock(FILE);
        print FILE "$subject\n";
        print FILE "$message\n";
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=aboutinfo\n\n";
}


############# End Carter Fix ######
################
sub welcomeim {
################
if ($access[6] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/welcomeim.txt") || error("$err{'001'} $datadir/welcomeim.txt");
        file_lock(FILE);
        chomp(@lines = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $subject = htmltotext($lines[0]);
        $message = htmltotext($lines[1]);

        $navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $mnu{'003'}";
        print_top();
        print qq~<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=welcomeim2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
$msg{'329'}<br>
<input type="text" name="subject" value="$subject" size="40">
</td>
</tr>
<tr>
<td>
$msg{'330'}<br>
<textarea name="message" cols="40" rows="10">$message</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}">&nbsp;<input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
        print_bottom();
        exit;
}

#################
sub welcomeim2 {
#################
if ($access[6] ne "on") { error("$err{'011'}"); }
        error("$err{'014'}") unless ($input{'subject'});
        error("$err{'015'}") unless ($input{'message'});

        chomp($input{'subject'});
        chomp($input{'message'});

        $subject = htmlescape($input{'subject'});
        $message = htmlescape($input{'message'});

        open(FILE, ">$datadir/welcomeim.txt") || error("$err{'016'} $datadir/welcomemsg.txt");
        file_lock(FILE);
        print FILE "$subject\n";
        print FILE "$message\n";
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=welcomeim\n\n";
}


################
sub managecats {
################
if ($access[10] ne "on") { error("$err{'011'}"); }

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        chomp(@categories = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $catsdropdown = "";
        $catlist = "";
        foreach $curcat (@categories) {
                $catsdropdown = "$catsdropdown<option>$curcat</option>";
                $catlist = "$catlist\n$curcat";
        }

        $navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $mnu{'014'}";

        print_top();
        print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top">
<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$admin&amp;op=reordercats" method="post">
<b>$msg{'198'}</b><br>
<textarea name="cats" cols="40" rows="4">$catlist</textarea><br>
<input type="submit" value="$btn{'024'}">
</form>
<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=removecat" method="post">
<b>$msg{'199'}</b><br>
<select name="cat">
$catsdropdown
</select>
<input type=submit value="$btn{'011'}">
</form>
<form  onSubmit="submitonce(this)"   onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=createcat" method="post">
<b>$msg{'200'}</b><br>
ID:<br>
<input type="text" size="15" name="catid"><br>
$msg{'201'}<br>
<input type="text" size="40" name="catname"><br>
$msg{'202'}<br>
<input type="text" size="40" name="memgroup"><br>
$msg{'203'}<br>
<input type="submit" value="$btn{'025'}">
</form>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}

#################
sub reordercats {
#################
if ($access[10] ne "on") { error("$err{'011'}"); }

        $input{'cats'} =~ s/\r//g;
        open(FILE, ">$boardsdir/cats.txt") || error("$err{'016'} $boardsdir/cats.txt");
        file_lock(FILE);
        print FILE "$input{'cats'}";
        unfile_lock(FILE);
        close(FILE);
        print "Location: $pageurl/$admin\&op=managecats\n\n";
        exit;
}

###############
sub removecat {
###############
if ($access[10] ne "on") { error("$err{'011'}"); }

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        chomp(@categories = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $newcatlist = "";
        foreach $curcat (@categories) {
                if ($curcat ne "$input{'cat'}") { $newcatlist = "$newcatlist$curcat\n"; }
        }

        open(FILE, ">$boardsdir/cats.txt") || error("$err{'016'} $boardsdir/cats.txt");
        file_lock(FILE);
        print FILE "$newcatlist";
        unfile_lock(FILE);
        close(FILE);

        $curcat = "$input{'cat'}";

        open(CAT, "$boardsdir/$curcat.cat") || error("$err{'001'} $boardsdir/$curcat.cat");
        file_lock(CAT);
        chomp(@catinfo = <CAT>);
        unfile_lock(CAT);
        close(CAT);

        $curcatname = "$catinfo[0]";

        $navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $btn{'039'}";
        print_top();

        foreach $curboard (@catinfo) {
                if ($curboard ne "$catinfo[0]") {
                        open(BOARDDATA, "$boardsdir/$curboard.txt");
                        file_lock(BOARDDATA);
                        @messages = <BOARDDATA>;
                        unfile_lock(BOARDDATA);
                        close(BOARDDATA);

                        foreach $curmessage (@messages) {
                                ($id, $dummy) = split(/\|/, $curmessage);
                                unlink("$messagedir/$id.txt");
                                unlink("$messagedir/$id.mail");
                                print qq~Removing message $id...<br>~;
                        }
                }
                unlink("$boardsdir/$curboard.txt");
                unlink("$boardsdir/$curboard.mail");
                unlink("$boardsdir/$curboard.dat");
                unlink("$boardsdir/$curboard.sticky");
                print qq~Removing board datafiles...<br>~;
        }
        print qq~$inf{'024'}<br>~;
        unlink("$boardsdir/$curcat.cat");
        print qq~$inf{'025'}~;
        print_bottom();
        exit;
}

###############
sub createcat {
###############
if ($access[10] ne "on") { error("$err{'011'}"); }

        $catid = "$input{'catid'}";
        $catid =~ s/^\s+//;
        $catid =~ s/\s+$//;
        $catid =~ tr/ /_/;
        $catid = lc($catid);

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        chomp(@categories = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$boardsdir/cats.txt") || error("$err{'016'} $boardsdir/cats.txt");
        file_lock(FILE);
        foreach $curcat (@categories) {
                print FILE "$curcat\n";
        }
        print FILE "$catid";
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$boardsdir/$catid.cat");
        print FILE "$input{'catname'}\n";
        print FILE "$input{'memgroup'}\n";
        close(FILE);
        print "Location: $pageurl/$admin\&op=managecats\n\n";
        exit;
}

##################
sub manageboards {
##################
if ($access[12] ne "on") { error("$err{'011'}"); }

        open(FILE, "$boardsdir/cats.txt") || error("$err{'001'} $boardsdir/cats.txt");
        file_lock(FILE);
        chomp(@categories = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $mnu{'015'}";
        print_top();

        print qq~<table border="0" cellspacing="1">
<tr>
<td><b>$nav{'073'}</b></td>
<!-- td><b>$nav{'074'}</b></td -->
<td><b>$nav{'075'}</b></td>
</tr>
~;
        foreach $curcat (@categories) {
                open(CAT, "$boardsdir/$curcat.cat");
                file_lock(CAT);
                chomp(@catinfo = <CAT>);
                unfile_lock(CAT);
                close(CAT);

                $curcatname = "$catinfo[0]";

                print qq~<tr>
<td colspan="3"><HR COLOR=BLue><a href="$pageurl/$admin&amp;op=reorderboards&cat=$curcat"><b>$curcatname</b></a><HR COLOR=BLue></td>
</tr>
~;
                foreach $curboard (@catinfo) {
                        if ($curboard ne "$catinfo[0]" && $curboard ne "$catinfo[1]") {
                                open(BOARD, "$boardsdir/$curboard.dat");
                                file_lock(BOARD);
                                @boardinfo = <BOARD>;
                                unfile_lock(BOARD);
                                close(BOARD);

                                $curboardname = "$boardinfo[0]";
                                $descr = "$boardinfo[1]";

                                open(BOARDDATA, "$boardsdir/$curboard.txt");
                                file_lock(BOARDDATA);
                                @messages = <BOARDDATA>;
                                unfile_lock(BOARDDATA);
                                close(BOARDDATA);

                                $moderator = "$modprop[1]";

                                print qq~<tr>
<td valign="top"><form  onSubmit="submitonce(this)" action="$pageurl/$admin&op=modifyboard" method="post">
<input type="hidden" name="id" value="$curboard">
<input type="hidden" name="cat" value="$curcat">
<input type="text" name="boardname" value="$curboardname" size="20"><br>
<textarea name="descr" cols="30" rows="3">$descr</textarea>
</td>
<!-- td valign="top"><input type=text name="moderator" value="$boardinfo[2]" size="10"></td -->
<td valign="top">
<input type=hidden name="moderator" value="$boardinfo[2]" size="10">
<input type="submit" name="moda" value="$btn{'015'}">
<!-- input type="submit" name="moda" value="$btn{'026'}" DISABLED -->
</form>
<form onSubmit="submitonce(this)" action="$pageurl/$admin&op=deleteboard" method="post">
<input type="hidden" name="id" value="$curboard">
<input type="hidden" name="cat" value="$curcat">
<input type="hidden" name="boardname" value="$curboardname">
<input type="hidden" name="descr" value="$descr">
<input type="hidden" name="moderator" value="$boardinfo[2]">
<input type="submit" name="moda" value="$btn{'026'}">
</form>
</td>
</tr>
~;
                        }
                }
                print qq~<tr>
<td colspan="3"><hr size="1"></td>
</tr>
<tr>
<td valign="top"><form  onSubmit="submitonce(this)" action="$pageurl/$admin&op=createboard" method="post">
<table>
<tr>
<td>$msg{'204'}</td>
<td><input type="text" name="id" value="" size="15"></td>
</tr>
<tr>
<td>$msg{'201'}</td>
<td><input type="text" name="boardname" size="20"></td>
</tr>
<tr>
<td colspan="2">$msg{'205'}<br>
<textarea name="descr" cols="30" rows="3"></textarea></td>
</tr>
</table>
</td>
<td valign="top"><input type="text" name="moderator" value="" size="10"><input type="hidden" name="cat" value="$curcat"></td>
<td valign="top"><input type="submit" value="$btn{'027'}">
</form>
</td>
</tr>
~;
        }
        print "</table>";
        print_bottom();
        exit;
}

###################
sub reorderboards {
###################
if ($access[12] ne "on") { error("$err{'011'}"); }

        open(FILE, "$boardsdir/$info{'cat'}.cat") || error("$err{'001'} $boardsdir/$info{'cat'}.cat");
        file_lock(FILE);
        chomp(@allboards = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $boardlist = "";
        foreach $cboard (@allboards) {
                if ($cboard ne "$allboards[0]" && $cboard ne "$allboards[1]") { $boardlist = "$boardlist\n$cboard"; }
        }

        $navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $nav{'114'} $btn{'014'} $nav{'115'}";

        print_top();
        print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td valign="top"><form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=reorderboards2" method="post">
<b>$msg{'382'}</b><br>
<textarea name="boards" cols="30" rows="4">$boardlist</textarea><br>
<input type="hidden" name="firstline" value="$allboards[0]">
<input type="hidden" name="secondline" value="$allboards[1]">
<input type="hidden" name="cat" value="$info{'cat'}">
<input type="submit" value="$btn{'028'}">
</form>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}

####################
sub reorderboards2 {
####################
if ($access[12] ne "on") { error("$err{'011'}"); }

        $input{'boards'} =~ s/\r//g;
        $input{'firstline'} =~ s/\n//g;
        $input{'secondline'} =~ s/\n//g;

        open(FILE, ">$boardsdir/$input{'cat'}.cat") || error("$err{'016'} $boardsdir/$input{'cat'}.cat");
        file_lock(FILE);
        print FILE "$input{'firstline'}\n";
        print FILE "$input{'secondline'}\n";
        print FILE "$input{'boards'}";
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=reorderboards\&cat=$input{'cat'}\n\n";
        exit;
}

#################
sub modifyboard {
#################
if ($access[12] ne "on") { error("$err{'011'}"); }
                $input{'descr'} =~ s/\n/ /g;
                $input{'descr'} =~ s/\r//g;

                open(FILE, ">$boardsdir/$input{'id'}.dat");
                file_lock(FILE);
                print FILE "$input{'boardname'}\n";
                print FILE "$input{'descr'}\n";
                print FILE "$input{'moderator'}\n";
                unfile_lock(FILE);
                close(FILE);

                print "Location: $pageurl/$admin\&op=manageboards\n\n";

        exit;
}

#################
sub deleteboard {
#################

if ($access[12] ne "on") { error("$err{'011'}"); }

                open(FILE, "$boardsdir/$input{'cat'}.cat");
                file_lock(FILE);
                @categories = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                $newcatlist="";
                foreach $curboard (@categories) {
                        $curboard =~ s/\n//g;
                        if($curboard ne "$input{'id'}") { $newcatlist="$newcatlist$curboard\n"; }
                }
                open(FILE, ">$boardsdir/$input{'cat'}.cat");
                file_lock(FILE);
                print FILE "$newcatlist";
                unfile_lock(FILE);
                close(FILE);

                $curboard="$input{'id'}";
                open(BOARDDATA, "$boardsdir/$curboard.txt");
                file_lock(BOARDDATA);
                chomp(@messages = <BOARDDATA>);
                unfile_lock(BOARDDATA);
                close(BOARDDATA);

                $navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $nav{'116'}";
                print_top();

                foreach $curmessage (@messages) {
                        ($id, $dummy) = split(/\|/, $curmessage);
                        unlink("$messagedir/$id\.txt");
                        unlink("$messagedir/$id\.mail");
                        print "Removing message $id...<br>";
                }
                print "Removing board datafiles...<br>";
                unlink("$boardsdir/$curboard.dat");
                unlink("$boardsdir/$curboard.txt");
                unlink("$boardsdir/$curboard.sticky");
                print "Done!";
                print_bottom();

}

#################
sub createboard {
#################
if ($access[12] ne "on") { error("$err{'011'}"); }

        $id = "$input{'id'}";
        $id =~ s/^\s+//;
        $id =~ s/\s+$//;
        $id =~ tr/ /_/;
        $id = lc($id);
        $input{'descr'} =~ s/\n/ /g;
        $input{'descr'} =~ s/\r//g;
        if ($input{'moderator'} eq "") { $input{'moderator'} = "admin"; }

        open(FILE, "$boardsdir/$input{'cat'}.cat");
        file_lock(FILE);
        chomp(@categories = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$boardsdir/$input{'cat'}.cat");
        file_lock(FILE);
        foreach $curboard (@categories) {
                print FILE "$curboard\n";
        }
        print FILE "$id";
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$boardsdir/$id.sticky");
        close(FILE);

        open(FILE, ">$boardsdir/$id.dat");
        print FILE "$input{'boardname'}\n";
        print FILE "$input{'descr'}\n";
        print FILE "$input{'moderator'}\n";
        close(FILE);

        open(FILE, ">$boardsdir/$id.txt");
        print FILE "";
        close(FILE);

        print "Location: $pageurl/$admin\&op=manageboards\n\n";
        exit;
}

###############
sub setcensor {
###############
if ($access[11] ne "on") { error("$err{'011'}"); }

        open(FILE, "$boardsdir/censor.txt") || error("$err{'001'} $boardsdir/censor.txt");
        file_lock(FILE);
        @censored = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $nav{'043'} $btn{'014'} $mnu{'016'}";

        print_top();

        print qq~<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td><form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=setcensor2" method="post">
$msg{'206'}<br>
<textarea cols="30" rows="6" name="censored">
~;
        foreach $cur (@censored) {
                print "$cur";
        }

        print qq~</textarea><br>
<input type="submit" value="$btn{'022'}">
</form>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}

################
sub setcensor2 {
################
if ($access[11] ne "on") { error("$err{'011'}"); }

        open(FILE, ">$boardsdir/censor.txt") || error("$err{'016'} $boardsdir/censor.txt");
        file_lock(FILE);
        print FILE "$input{'censored'}";
        unfile_lock(FILE);
        close(FILE);
        print "Location: $admin\&op=setcensor\n\n";
        exit;
}

###############
sub polladmin {
###############
if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
        file_lock(FILE);
        @data = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $mnu{'017'}";
        print_top();

        if (@data == 0) { }
        else {
                print qq~
When createing a new poll dont edit the old one create a new one.<BR>
The system logs whos already voted and theay will not be allowed to vote on the new one.<BR>
<P>
<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor="$windowbg"><b>$msg{'207'}</b></td>
<td bgcolor="$windowbg"><b>$msg{'208'}</b></td>
~;
                foreach $line (@data) {
                        @item = split(/\|/, $line);
                        print qq~<tr>
<td bgcolor="$windowbg2"><a href="$pageurl/$cgi?action=pollit2&amp;id=$item[$0]">$item[1]</a></td>
<td bgcolor="$windowbg2">[<a href="$pageurl/$admin&amp;op=editpoll&amp;id=$item[$0]">$nav{'096'}</a>] <!-- [<a href="$admin&amp;op=deletepoll&amp;id=$item[$0]">$nav{'097'}</a>] [<a href="$admin&amp;op=resetpoll&amp;id=$item[$0]">$nav{'117'}</a>]--></td>
</tr>
~;
                }
                print qq~</table>
</td>
</tr>
</table>
<br><br>
~;
        }
        ($num, $name) = split(/\|/, $data[0]);
        $num++;

        print qq~<a href="$pageurl/$admin&amp;op=createpoll&amp;newid=$num"><b>$nav{'118'}</b></a>~;
        print_bottom();
        exit;

}

################
sub createpoll {
################
if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
        file_lock(FILE);
        @polls = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$datadir/polls/polls.txt") || error("$err{'016'} $datadir/polls/polls.txt");
        file_lock(FILE);
        print FILE "$info{'newid'}|Welcome to the Pollbooth\n";
        print FILE @polls;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$datadir/polls/$info{'newid'}_q.dat") || error("$err{'016'} $datadir/polls/$info{'newid'}_q.dat");
        file_lock(FILE);
        print FILE "Option 1\n";
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$datadir/polls/$info{'newid'}_a.dat") || error("$err{'016'} $datadir/polls/$info{'newid'}_a.dat");
        file_lock(FILE);
        print FILE "0\n";
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$datadir/polls/$info{'newid'}_ip.dat") || error("$err{'016'} $datadir/polls/$info{'newid'}_ip.dat");
        file_lock(FILE);
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=editpoll\&id=$info{'newid'}\n\n";
}

##############
sub editpoll {
##############

if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
        file_lock(FILE);
        chomp(@polls = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        for ($x = 0; $x < @polls; $x++) {
                ($id, $name) = split(/\|/, $polls[$x]);
                if ($info{'id'} == $id) { $question = $name; }
        }

        open(FILE, "$datadir/polls/$info{'id'}_q.dat") || error("$err{'001'} $datadir/polls/$info{'id'}_q.dat! This is a problem!");
        file_lock(FILE);
        @data = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $mnu{'031'} $btn{'014'} $mnu{'032'}";
        print_top();
        print qq~<table>
<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=editpoll2" method="post">
<tr>
<td>$msg{'209'}</td>
<td><input type="text" name="question" size="40" value="$question"></td>
<td><input type="hidden" name="id" value="$info{'id'}">
<input type="submit" name="moda" value="$btn{'015'}"></td>
</tr>
</form>
~;
        for ($i = 0; $i < @data; $i++) {
                print qq~<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=editpoll2a" method="post">
<tr>
<td>$msg{'210'} $i:</td>
<td><input type="text" name="answer" size="40" value="$data[$i]"></td>
<td><input type="hidden" name="id" value="$info{'id'}">
<input type="hidden" name="num" value="$i">
<input type="submit" name="moda" value="$btn{'015'}"><input type="submit" name="moda" value="$btn{'011'}"></td>
</tr>
</form>
~;
        }
        print qq~</table>
</form>
<hr size="1">
<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=editpoll3" method="post">
<table>
<tr>
<td>$msg{'383'}<input type="text" name="newanswer" size="40">
<input type="hidden" name="id" value="$info{'id'}">
<input type="submit" name="moda" value="$btn{'027'}"></td>
</tr>
</table>
~;
        print_bottom();
        exit;
}

###############
sub editpoll2 {
###############

if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
        file_lock(FILE);
        @polls = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$datadir/polls/polls.txt") || error("$err{'016'} $datadir/polls/polls.txt!");
        file_lock(FILE);
        for ($i = 0; $i < @polls; $i++) {
                ($id, $name) = split(/\|/, $polls[$i]);
                if ($input{'id'} eq $id) { print FILE "$id|$input{'question'}\n"; }
                else { print FILE "$polls[$i]"; }
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=editpoll\&id=$input{'id'}\n\n";
}

################
sub editpoll2a {
################

if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/$input{'id'}_q.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_q.dat!");
        file_lock(FILE);
        @questions = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$datadir/polls/$input{'id'}_a.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_a.dat!");
        file_lock(FILE);
        @answers = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        if ($input{'moda'} eq $btn{'011'}) {
                open(FILE, ">$datadir/polls/$input{'id'}_q.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_q.dat!");
                file_lock(FILE);
                for ($i = 0; $i < @questions; $i++) {
                        if ($input{'num'} eq $i) { }
                        else { print FILE "$questions[$i]"; }
                }
                unfile_lock(FILE);
                close(FILE);

                open(FILE, ">$datadir/polls/$input{'id'}_a.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_a.dat!");
                file_lock(FILE);
                for ($i = 0; $i < @answers; $i++) {
                        if ($input{'num'} eq $i) { }
                        else { print FILE "$answers[$i]"; }
                }
                unfile_lock(FILE);
                close(FILE);
        }
        else {
                open(FILE, ">$datadir/polls/$input{'id'}_q.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_q.dat!");
                file_lock(FILE);
                for ($i = 0; $i < @questions; $i++) {
                        if ($input{'num'} eq $i) { print FILE "$input{'answer'}\n"; }
                        else { print FILE "$questions[$i]"; }
                }
                unfile_lock(FILE);
                close(FILE);
        }

        print "Location: $pageurl/$admin\&op=editpoll\&id=$input{'id'}\n\n";
}

###############
sub editpoll3 {
###############

if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/$input{'id'}_q.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_q.dat!");
        file_lock(FILE);
        @questions = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open (FILE, ">$datadir/polls/$input{'id'}_q.dat") || error("$err{'016'} $datadir/polls/$input{'id'}_q.dat!");
        file_lock(FILE);
        print FILE @questions;
        print FILE "$input{'newanswer'}\n";
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$datadir/polls/$input{'id'}_a.dat") || error("$err{'001'} $datadir/polls/$input{'id'}_a.dat!");
        file_lock(FILE);
        @answers = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open (FILE, ">$datadir/polls/$input{'id'}_a.dat") || error("$err{'016'} $datadir/polls/$input{'id'}_a.dat!");
        file_lock(FILE);
        print FILE @answers;
        print FILE "0\n";
        unfile_lock(FILE);
        close(FILE);


        print "Location: $pageurl/$admin\&op=editpoll\&id=$input{'id'}\n\n";
}

###############
sub resetpoll {
###############

if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/$info{'id'}_a.dat") || error("$err{'001'} $datadir/polls/$info{'id'}_a.dat!");
        file_lock(FILE);
        chomp(@answers = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        open (FILE, ">$datadir/polls/$info{'id'}_a.dat") || error("$err{'016'} $datadir/polls/$info{'id'}_a.dat!");
        file_lock(FILE);
        foreach $line (@answers) { print FILE "0\n"; }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin\&op=polladmin\n\n";
}

################
sub deletepoll {
################

if ($access[14] ne "on") { error("$err{'011'}"); }

        open(FILE, "$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
        file_lock(FILE);
        chomp(@polls = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$datadir/polls/polls.txt") || error("$err{'001'} $datadir/polls/polls.txt");
        file_lock(FILE);
        for ($x = 0; $x < @polls; $x++) {
                ($id, $name) = split(/\|/, $polls[$x]);
                if ($info{'id'} == $id) { }
                else { print FILE "$polls[$x]\n"; }
        }
        unfile_lock(FILE);
        close(FILE);

        unlink("$datadir/polls/$info{'id'}_q.dat");
        unlink("$datadir/polls/$info{'id'}_a.dat");
        unlink("$datadir/polls/$info{'id'}_ip.dat");

        print "Location: $pageurl/$admin\&op=polladmin\n\n";
}

################
sub verifynews {
################
        check_access(pubnews); if ($access_granted ne "1") { error("$err{'011'}"); }

        xml();

        open(TMPDATA, "<$topicsdir/newarticles.dat");
        file_lock(TMPDATA);
        chomp(@tmpdatas = <TMPDATA>);
        unfile_lock(TMPDATA);
        close(TMPDATA);

        open(FILE, "$topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);
        unfile_lock(FILE);
        close(FILE);


        for ($a = 0; $a < @tmpdatas; $a++) {
                ($id[$a], $cat[$a], $subject[$a], $nick[$a], $postername[$a], $email[$a], $postdate[$a], $message[$a]) = split(/\|/, $tmpdatas[$a]);
        }


        $navbar = "$btn{'014'} $nav{'024'} $btn{'014'} $mnu{'033'}";
        print_top();

        if (@tmpdatas == 0) { print "$msg{'036'}"; }
        else {
                print qq~<table border="0" cellpadding="5" cellspacing="0" width="100%">
<tr>
<td align="center"><b>$msg{'035'}</b></td>
</tr>
</table>
~;
                if ($info{'start'} eq "") { $start = 0; }
                else { $start = "$info{'start'}"; }

                $numshown = 0;
                for ($b = 0; $b < @tmpdatas; $b++) {
                        $numshown++;
                        $catsdropdown[$b] = "";
                        foreach $catslist (@cats) {
                                chomp($catslist);
                                ($name, $link) = split(/\|/, $catslist);
                                if ($cat[$b] eq $link) { $sel[$b] = " selected"; }
                                else { $sel[$b] = ""; }
                                $catsdropdown[$b] = qq~$catsdropdown[$b]\n<option value="$link" $sel[$b]>$name~;
                        }

                        $message[$b] = htmltotext($message[$b]);

                        my $tmp_sub=$subject[$b];
                        $tmp_sub =~ s/\s/%20/g;

                        print qq~<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=verifynews2&amp;mysubject=$tmp_sub" method="post">
<hr noshade="noshade" size="1">
<table>
<tr>
<td colspan="2"><b>$msg{'384'}$postdate[$b]:</b><input type="hidden" name="postdate" value="$postdate[$b]"></td>
</tr>
<tr>
<td>$msg{'013'}</td>
<td>$nick[$b]<input type="hidden" name="posternick" value="$nick[$b]"></td>
</tr>
<tr>
<td>$msg{'007'}</td>
<td>$email[$b]<input type="hidden" name="posteremail" value="$email[$b]"></td>
</tr>
<tr>
<td>$msg{'034'}</td>
<td>
<select name="cat">$catsdropdown[$b]
</select>
</td>
</tr>
<td>$msg{'037'}</td>
<td><input type="text" name="subject" size="40" maxlength="50" value="$subject[$b]"></td>
</tr>
<tr>
<td valign="top">$msg{'038'}</td>
<td>
<textarea name="message" rows="10" cols="40">$message[$b]</textarea><br>
</td>
</tr>
<td colspan="2" align="center">
<input type="hidden" value="$id[$b]" name="id">
<input type="hidden" name="postername" value="$postername[$b]">
<input type="submit" name="moda" value="$btn{'010'}"><input type="submit" name="moda" value="$btn{'011'}">
</td>
</tr>
</table>
</form>
~;
                        if ($numshown >= $maxtopics) { $b = @tmpdatas; }
                }
                if ($numshown >= $maxtopics) {
                        print qq~<hr noshade="noshade" size="1">
$msg{'039'}
~;
                        $numcontribs = @tmpdatas;
                        $c = 0;
                        while (($c*$maxtopics) < $numcontribs) {
                                $viewc = $c+1;
                                $strt = ($c*$maxtopics);
                                if ($start == $strt) { print "$viewc "; }
                                elsif ($strt == 0) { print qq~<a href="$pageurl/$admin&amp;op=verifynews">$viewc</a> ~; }
                                else { print qq~<a href="$pageurl/$admin&amp;op=verifynews&amp;start=$strt">$viewc</a> ~; }
                                $c++;
                        }
                }
        }
        print_bottom();
        exit;
}

#################
sub verifynews2 {
#################
        check_access(pubnews); if ($access_granted ne "1") { error("$err{'011'}"); }
        error("$err{'014'}") unless ($input{'subject'});
        error("$err{'015'}") unless ($input{'message'});

$subj = htmlescape($input{'subject'});
$mesg = htmlescape($input{'message'});

open(FILE, "<$topicsdir/newarticles.dat") || error("$err{'010'} $topicsdir/newarticles.dat");
@data = <FILE>;
close(FILE);

# if the admin chooses to pubish the article....

if ($input{'moda'} eq "$btn{'010'}") {
        opendir (DIR, "$topicsdir/articles");
        @files = readdir(DIR);
        closedir (DIR);

        @files = grep(/txt/, @files);
        @files = reverse(sort { $a <=> $b } @files);
        $postnum = @files[0];
        $postnum =~ s/.txt//;
        $postnum++;

        for ($a = 0; $a < @data; $a++) {
        ($id, $cat, $subject, $posternick, $postername, $posteremail, $postdate, $message) = split(/\|/, $data[$a]);

if ($subject eq "$info{'mysubject'}") {

        open(SETS, "$memberdir/$postername.dat") || error("$err{'010'}");
        file_lock(SETS);
        chomp(@msets = <SETS>);
        unfile_lock(SETS);
        close(SETS);

        $msets[11]++;

        open(SETS2, ">$memberdir/$postername.dat");
        file_lock(SETS2);
        for ($i = 0; $i < @msets; $i++) {
                print SETS2 "$msets[$i]\n";
                }
        unfile_lock(SETS2);
        close(SETS2);

        open(FILE2, "<$topicsdir/$input{'cat'}.cat");
        @data2 = <FILE2>;
        close(FILE2);

        open(FILE2,">$topicsdir/$input{'cat'}.cat");
        file_lock(FILE2); print FILE2 "$postnum|$subj|$input{'posternick'}|$input{'postername'}|$input{'posteremail'}|$date|0|0\n";
        print FILE2 @data2;
        close(FILE2);

        open(FILE, ">$topicsdir/articles/$postnum.txt");
        file_lock(FILE);
        print FILE "$subj|$input{'posternick'}|$input{'postername'}|$input{'posteremail'}|$date|$mesg\n"; close(FILE); } }


        open (FILE, "$topicsdir/newarticles.dat") || error("$err{'001'} $topicssdir/newarticles.dat");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$topicsdir/newarticles.dat") || error("$err{'016'} $boardsdir/newarticles.dat");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($id, $cat, $subject, $posternick, $postername, $postermail, $posterdate, $message) = split(/\|/,$threads[$a]);
                $message =~ s~[\n\r]~~g;
                if ($subject eq $info{'mysubject'}) { print FILE ""; }
                        else { print FILE "$threads[$a]"; }

        }
        unfile_lock(FILE);
        close(FILE);


}

else {
        open (FILE, "$topicsdir/newarticles.dat") || error("$err{'001'} $topicssdir/newarticles.dat");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$topicsdir/newarticles.dat") || error("$err{'016'} $topicsdirsdir/newarticles.dat");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($id, $cat, $subject, $posternick, $postername, $postermail, $posterdate, $message) = split(/\|/,$threads[$a]);
                $message =~ s~[\n\r]~~g;
                if ($subject eq $info{'mysubject'}) { print FILE ""; }
                        else { print FILE "$threads[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);


}

print "Location: $pageurl/$admin&op=verifynews\n\n";

}

################
sub modifynews {
################
if ($access[3] ne "on") { error("$err{'011'}"); }

        xml();

        undef @catnames;
        undef @catlinks;

        open(FILE, "$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $nav{'024'} $btn{'014'} $mnu{'034'}";
        print_top();
        print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor="$windowbg"><b>$msg{'211'}</b></td>
<td bgcolor="$windowbg"><b>$msg{'212'}</b></td>
<td bgcolor="$windowbg"><b>$msg{'213'}</b></td>
<td bgcolor="$windowbg"><b>$msg{'214'}</b></td>
<td bgcolor="$windowbg"><b>$msg{'215'}</b></td>
~;
        foreach (@cats) {
                @item = split(/\|/, $_);
                push(@catnames, $item[0]);
                push(@catlinks, $item[1]);
        }

        foreach $curcat (@catlinks) {
                if (-e("$topicsdir/$curcat.cat")) {
                        foreach (@cats) {
                                @item = split(/\|/, $_);
                                if ($curcat eq "$item[1]") { $curcatname = "$item[0]"; }
                        }

                        open(FILE, "$topicsdir/$curcat.cat");
                        file_lock(FILE);
                        chomp(@articles = <FILE>);
                        unfile_lock(FILE);
                        close(FILE);

                        for ($a = 0; $a < @articles; $a++) {
                                ($id, $subject, $nick, $poster, $email, $postdate, $comments) = split(/\|/, $articles[$a]);
                                if ($second eq "$windowbg3") { $second="$windowbg2"; }
                                else { $second="$windowbg3"; }

                                print qq~<tr>
<td bgcolor="$second">$id</td>
<td bgcolor="$second"><a href="$pageurl/$admin&amp;op=modifynews2&amp;cat=$curcat&amp;id=$id">$subject</a></td>
<td bgcolor="$second">$curcatname</td>
<td bgcolor="$second">$postdate</td>
<td bgcolor="$second"><a href="mailto:$email">$nick</a></td>
</tr>
~;
                        }
                }
        }
                        print qq~</table>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}

#################
sub modifynews2 {
#################
if ($access[3] ne "on") { error("$err{'011'}"); }

        open(FILE, "$topicsdir/articles/$info{'id'}.txt") || error("$err{'001'} $topicsdir/articles/$info{'id'}.txt");
        file_lock(FILE);
        chomp(@articles = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $nav{'024'} $btn{'014'} $mnu{'034'}";
        print_top();
        print qq~<table width="100%">
~;

        for ($a = 0; $a < @articles; $a++) {
                ($msub, $mname, $musername, $memail, $mdate, $mmessage) = split(/\|/, $articles[$a]);

                $mmessage = htmltotext($mmessage);

                print qq~<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=modifynews3" method="post">
<input type="hidden" name="cat" value="$info{'cat'}">
<input type="hidden" name="id" value="$info{'id'}">
<input type="hidden" name="viewnum" value="$a">
<tr>
<td valign="top">
~;
if ($mname eq "") { print qq~$msg{'183'}~; }
if ($mname ne "") { print qq~
<a href="mailto:$memail">$mname</a>~;
}
print qq~<br>
$mdate</td>
<td><input type="text" name="subject" value="$msub" size="30"><br>
<textarea name="message" rows="50" cols="50">$mmessage</textarea></td>
<td><input type="submit" name="moda" value="$btn{'015'}"><br>~;
if ($a eq 0) { print qq~<input type="submit" name="moda" value="$btn{'011'}"></td>~;
} else {print qq~<input type="submit" name="delt" value="$btn{'011'}"></td>~;
}
print qq~</tr>
<tr>
<td colspan="3"><hr size="1"></td>
</tr>
</form>
~;
        }
        open(FILE, "$topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        foreach $catslist (@cats) {
                chomp($catslist);
                ($name, $link) = split(/\|/, $catslist);
                if ($info{'cat'} eq $link) { $sel = "selected"; }
                else { $sel = ""; }
                $catsdropdown = qq~$catsdropdown\n<option value="$link" $sel>$name~;
        }
        print qq~<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=movetopic" method="post">
<tr>
<td colspan="3">$msg{'216'}<select name="tocat">$catsdropdown
</select>
<input type="hidden" name="topic" value="$info{'id'}">
<input type="hidden" name="oldcat" value="$info{'cat'}"><input type="submit" value="$btn{'029'}"></td>
</tr>
</form>
</table>
~;


        print_bottom();
        exit;
}

#################
sub modifynews3 {
#################
if ($access[3] ne "on") { error("$err{'011'}"); }

        open(FILE, "$topicsdir/articles/$input{'id'}.txt") || error("$err{'001'} $topicsdir/articles/$input{'id'}.txt");
        file_lock(FILE);
        @data = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        for ($a = 0; $a < @data; $a++) {
                ($msub[$a], $mname[$a], $musername[$a], $museremail[$a], $mdate[$a], $mmessage[$a]) = split(/\|/, $data[$a]);
        }

        $count = $a;
        if ($input{'viewnum'} == 0 && $count > 1 && $input{'moda'} eq $btn{'011'}) { error("$err{'025'}"); }

        open(FILE, ">$topicsdir/articles/$input{'id'}.txt") || error("$err{'016'} $topicsdir/articles/$input{'id'}.txt");
        file_lock(FILE);
        for ($b = 0; $b < @data; $b++) {
                if ($input{'viewnum'} eq $b) {
                        if ($input{'moda'} eq $btn{'015'}) {
                                chomp($input{'subject'});
                                chomp($input{'message'});

                                $subj = htmlescape($input{'subject'});
                                $mesg = htmlescape($input{'message'});

                                if ($input{'viewnum'} == 0) {
                                        open(FILE2, "$topicsdir/$input{'cat'}.cat") || error("$err{'001'} $topicsdir/$input{'cat'}.cat");
                                        file_lock(FILE2);
                                        @data2 = <FILE2>;
                                        unfile_lock(FILE2);
                                        close(FILE2);

                                        open(FILE2, ">$topicsdir/$input{'cat'}.cat") || error("$err{'016'} $topicsdir/$input{'cat'}.cat");
                                        file_lock(FILE2);
                                        for ($a = 0; $a < @data2; $a++) {
                                                ($oldnum, $subject, $posternick, $postername, $posteremail, $postdate, $comments) = split(/\|/, $data2[$a]);
                                                $comments =~ s/[\n\r]//g;
                                                if ($oldnum eq $input{'id'}) {
                                                        print FILE2 "$oldnum|$subj|$posternick|$postername|$posteremail|$postdate|$comments\n";
                                                }
                                                else { print FILE2 "$data2[$a]"; }
                                        }
                                        unfile_lock(FILE2);
                                        close(FILE2);
                                }
                                print FILE "$subj|$mname[$b]|$musername[$b]|$museremail[$b]|$mdate[$b]|$mesg\n";
                        }
                        else {
                                open (FILE2, "$topicsdir/$input{'cat'}.cat") || error("$err{'001'} $topicsdir/$input{'cat'}.cat");
                                file_lock(FILE2);
                                @data2 = <FILE2>;
                                unfile_lock(FILE2);
                                close (FILE2);

                                open (FILE2, ">$topicsdir/$input{'cat'}.cat") || error("$err{'016'} $topicsdir/$input{'cat'}.cat");
                                file_lock(FILE2);
                                for ($a = 0; $a < @data2; $a++) {
                                        ($oldnum, $subject, $posternick, $postername, $posteremail, $postdate, $comments) = split(/\|/, $data2[$a]);
                                        $comments =~ s/[\n\r]//g;
                                        $comments--;
                                        if ($comments < 0) {$comments = 0;}

                                        if ($oldnum == $input{'id'}) {
                                                print FILE2 "$oldnum|$subject|$posternick|$postername|$posteremail|$postdate|$comments\n";
                                        }
                                        else { print FILE2 "$data2[$a]"; }
                                }
                                unfile_lock(FILE2);
                                close(FILE2);

                                if ($input{'moda'} eq $btn{'011'}) {
                                unlink("$topicsdir/articles/$input{'id'}.txt");
                                unlink("$topicsdir/articles/$input{'id'}.cnt");
                                }

                                open(MEMBERFILE, "$memberdir/$musername[$b].dat");
                                file_lock(MEMBERFILE);
                                chomp(@memsett = <MEMBERFILE>);
                                unfile_lock(MEMBERFILE);
                                close(MEMBERFILE);

                                if ($input{'viewnum'} == 0) {
                                        open(FILE2, "$topicsdir/$input{'cat'}.cat") || error("$err{'001'} $topicsdir/$input{'cat'}.cat");
                                        file_lock(FILE2);
                                        @data2 = <FILE2>;
                                        unfile_lock(FILE2);
                                        close(FILE2);

                                        open(FILE2, ">$topicsdir/$input{'cat'}.cat") || error("$err{'016'} $topicsdir/$input{'cat'}.cat");
                                        file_lock(FILE2);
                                        for ($a = 0; $a < @data2; $a++) {
                                                ($oldnum, $subject, $posternick, $postername, $posteremail, $postdate, $comments) = split(/\|/, $data2[$a]);
                                                $comments =~ s/[\n\r]//g;
                                                if ($oldnum eq $input{'id'}) {        }
                                                else { print FILE2 "$data2[$a]"; }
                                        }
                                        unfile_lock(FILE2);
                                        close(FILE2);

                                        $memsett[11]--;
                                        open(MEMBERFILE, ">$memberdir/$musername[$b].dat") || error("$err{'016'} $memberdir/$musername[$b].dat");
                                        file_lock(MEMBERFILE);
                                        for ($i = 0; $i < @memsett; $i++) {
                                                print MEMBERFILE "$memsett[$i]\n";
                                        }
                                        unfile_lock(MEMBERFILE);
                                        close(MEMBERFILE);
                                }
                                else {
                                        $memsett[12]--;
                                        open(MEMBERFILE, ">$memberdir/$musername[$b].dat") || error("$err{'016'} $memberdir/$musername[$b].dat");
                                        file_lock(MEMBERFILE);
                                        for ($i = 0; $i < @memsett; $i++) {
                                                print MEMBERFILE "$memsett[$i]\n";
                                        }
                                        unfile_lock(MEMBERFILE);
                                        close(MEMBERFILE);
                                }
                        }
                }
                else { print FILE "$data[$b]"; }
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin&op=modifynews\n\n";
        exit;
}

###############
sub movetopic {
###############
if ($access[3] ne "on") { error("$err{'011'}"); }

        open (FILE, "$topicsdir/$input{'oldcat'}.cat") || error("$err{'001'} $topicsdir/$input{'cat'}.cat");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$topicsdir/$input{'oldcat'}.cat") || error("$err{'016'} $topicsdir/$input{'cat'}.cat");
        file_lock(FILE);
        for ($a = 0; $a < @topics; $a++) {
                ($num, $subject, $posternick, $postername, $posteremail, $postdate, $comments) = split(/\|/,$topics[$a]);
                $comments  =~ s~[\n\r]~~g;
                if ($num ne $input{'topic'}) { print FILE "$topics[$a]"; }
                else { $linetowrite = "$topics[$a]"; }
        }
        unfile_lock(FILE);
        close(FILE);

        open (FILE, "$topicsdir/$input{'tocat'}.cat");
        file_lock(FILE);
        @topics = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$topicsdir/$input{'tocat'}.cat");
        file_lock(FILE);
        print FILE "$linetowrite";
        foreach $line (@topics) {
                print FILE "$line";
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin&op=modifynews\n\n";
        exit;
}

################
sub topicadmin {
################
if ($access[5] ne "on") { error("$err{'011'}"); }

        open(FILE, "$topicsdir/cats.dat");
        file_lock(FILE);
        chomp(@cats = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $nav{'024'} $btn{'014'} $mnu{'035'}";
        print_top();
        print qq~<table>~;

        foreach $line (@cats) {
                @item = split(/\|/, $line);
                print qq~<form  onSubmit="submitonce(this)"  action="$admin&op=topicadmin2" method="post">
<tr>
<td><img src="$imagesurl/topics/$item[1].gif" alt="$imagesurl/topics/$item[1].gif"></td>
<td valign="top">
<table>
<tr>
<td>$msg{'205'}</td>
<td><input type="text" name="desc" value="$item[0]"></td>
</tr>
<tr>
<td>$msg{'092'}</td>
<td><input type="text" name="cat" value="$item[1]"></td>
</tr>
</table>
</td>
<td valign="top"><input type="hidden" name="oldcat" value="$item[1]"><input type="submit" name="moda" value="$btn{'015'}"><br>
<input type="submit" name="moda" value="$btn{'011'}"></td>
</tr>
</form>
~;
        }
        print qq~<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&op=topicadmin3" method="post">
<tr>
<td colspan="2"><hr size="1">
<b>$msg{'217'}</b></td>
</tr>
<tr>
<td>$msg{'205'}</td>
<td><input type="text" name="desc"></td>
</tr>
<tr>
<td>$msg{'218'}</td>
<td><input type="text" name="cat"></td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$btn{'025'}"></td>
</tr>
</form>
</table>
~;
        print_bottom();
        exit;
}

#################
sub topicadmin2 {
#################
if ($access[5] ne "on") { error("$err{'011'}"); }

        open(FILE, "$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
        file_lock(FILE);
        @cats = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        if ($input{'moda'} eq $btn{'015'}) {
                chomp($input{'oldcat'});

                open(FILE, ">$topicsdir/cats.dat") || error("$err{'016'} $topicsdir/cats.dat");
                file_lock(FILE);
                foreach $line (@cats) {
                        chomp($line);
                        ($name, $link) = split(/\|/, $line);
                        if ($input{'oldcat'} eq $link) { print FILE "$input{'desc'}|$input{'cat'}\n"; }
                        else { print FILE "$line\n"; }
                }
                unfile_lock(FILE);
                close(FILE);

                open(FILE, "$topicsdir/$input{'oldcat'}.cat");
                file_lock(FILE);
                chomp(@topics = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                open(FILE, ">$topicsdir/$input{'cat'}.cat");
                file_lock(FILE);
                foreach $line (@topics) {
                        print FILE "$line\n";
                }
                unfile_lock(FILE);
                close(FILE);

                if ($input{'oldcat'}.cat ne $input{'cat'}.cat) {
                unlink("$topicsdir/$input{'oldcat'}.cat");
                }
                else { };

        }
        if ($input{'moda'} eq $btn{'011'}) {
                open(FILE, "$topicsdir/$input{'cat'}.cat");
                file_lock(FILE);
                @data = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                if (@data != 0) { error("$err{'025'}"); }
                chomp($input{'cat'});

                open(FILE, ">$topicsdir/cats.dat") || error("$err{'016'} $topicsdir/cats.dat");
                file_lock(FILE);
                foreach $line (@cats) {
                        chomp($line);
                        ($name, $link) = split(/\|/, $line);
                        if ($input{'cat'} eq $link) { }
                        else { print FILE "$line\n"; }
                }
                unfile_lock(FILE);
                close(FILE);

                unlink("$topicsdir/$input{'cat'}.cat");
        }

        print "Location: $pageurl/$admin&op=topicadmin\n\n";
        exit;
}

#################
sub topicadmin3 {
#################
if ($access[5] ne "on") { error("$err{'011'}"); }

        open(FILE, "$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
        file_lock(FILE);
        @cats = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$topicsdir/cats.dat") || error("$err{'016'} $topicsdir/cats.dat");
        file_lock(FILE);
        print FILE "$input{'desc'}|$input{'cat'}\n";
        print FILE @cats;
        unfile_lock(FILE);
        close(FILE);

        open(FILE, ">$topicsdir/$input{'cat'}.cat") || error("$err{'016'} $topicsdir/$input{'cat'}.cat");
        file_lock(FILE);
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin&op=topicadmin\n\n";
        exit;
}

###############
sub userapproval {
###############
        check_access(); if ($settings[7] ne "Administrator") { error("$err{'011'}"); }

        open(TMPDATA, "<$memberdir/forapproval.dat");
        file_lock(TMPDATA);
        chomp(@tmpdatas = <TMPDATA>);
        unfile_lock(TMPDATA);
        close(TMPDATA);

        for ($a = 0; $a < @tmpdatas; $a++) {
                ($actualpass[$a], $cryptedpass[$a], $appusername[$a], $appemail[$a], $appnewletter[$a], $applang[$a]) = split(/\|/, $tmpdatas[$a]);
        }


        $navbar = "$btn{'014'} $nav{'062'} $btn{'014'} $msg{'644'}";
        print_top();
        print qq~<table border="0" cellpadding="5" cellspacing="0" width="100%">
        <tr>
        <td><b>$msg{'648'}</b></td>
        </tr>
        </table>
        <table border="1" cellpadding="3" cellspacing="1" width="100%">
        <tr>
        <td class="imtitle" width="10%">$msg{'006'}</td>
        <td class="imtitle" width="70%">$msg{'007'}</td>
        <td class="imtitle" width="20%">$msg{'208'}:</td>
        </tr>
        ~;

        if (@tmpdatas == 0) { print qq~<tr><td colspan="3">$msg{'649'}</td></tr>~; }
        else {

                if ($info{'start'} eq "") { $start = 0; }
                else { $start = "$info{'start'}"; }

                $numshown = 0;
                for ($b = 0; $b < @tmpdatas; $b++) {
                        $numshown++;

                        print qq~<form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=userapproval2&amp;myappusername=$appusername[$b]" method="post">
<tr>
<td width="10%">$appusername[$b]<input type="hidden" name="appusername" value="$appusername[$b]"></td>
<td width="70%">$appemail[$b]<input type="hidden" size="40" name="appemail" value="$appemail[$b]"></td>
<td width="20%" align="center"><input type="hidden" value="$actualpass[$b]" name="actualpass">
<input type="hidden" value="$cryptedpass[$b]" name="cryptedpass">
<input type="hidden" value="$appnewletter[$b]" name="appnewletter">
<input type="hidden" value="$applang[$b]" name="applang">
<input type="submit" name="moda" value="$btn{'027'}"><input type="submit" name="moda" value="Delete">
</td>
</tr>
</form>
~;
                if ($numshown >= 20) { $b = @tmpdatas; }
                }
                if ($numshown >= 20) {
                        print qq~<tr><td colspan="3" class="imtitle"><b>$msg{'039'} </b>~;
                        $numcontribs = @tmpdatas;
                        $c = 0;
                        while (($c*20) < $numcontribs) {
                                $viewc = $c+1;
                                $strt = ($c*20);
                                if ($start == $strt) { print "$viewc "; }
                                elsif ($strt == 0) { print qq~<a href="$pageurl/$admin&amp;op=userapproval">$viewc</a> ~; }
                                else { print qq~<a href="$pageurl/$admin&amp;op=userapproval&amp;start=$strt">$viewc</a> ~; }
                                $c++;
                        }
                        print qq~</td></tr>~;
                }
        }
        print qq~</table><br>~;
        print_bottom();
        exit;
}

###############
sub userapproval2 {
###############

use DBI;

        check_access(); if ($settings[7] ne "Administrator") { error("$err{'011'}"); }

open(FILE, "<$memberdir/forapproval.dat") || error("$err{'010'} $memberdir/forapproval.dat");
@data = <FILE>;
close(FILE);

# if the admin chooses to authorise the user....

if ($input{'moda'} ne "Delete") {

        for ($a = 0; $a < @data; $a++) {
        ($actualpass, $cryptedpass, $appusername, $appemail, $appnewletter, $applang) = split(/\|/, $data[$a]);

                                                                if ($appusername eq $info{'myappusername'}) {

                                                                open(FILE, ">$memberdir/$appusername.dat");
                                                                file_lock(FILE);
                                                                print FILE "$cryptedpass\n";
                                                                print FILE "$appusername\n";
                                                                print FILE "$appemail\n";
                                                                print FILE "\n";
                                                                print FILE "\n";
                                                                print FILE "$msg{'026'}\n";
                                                                print FILE "0\n";
                                                                print FILE "Member\n";
                                                                print FILE "\n";
                                                                print FILE "\n";
                                                                print FILE "$date\n";
                                                                print FILE "0\n";
                                                                print FILE "0\n";
                                                                print FILE "$defaulttheme\n";
                                                                print FILE "Member\n";
                                                                print FILE "$applang\n";
                                                                print FILE "\n";
                                                                print FILE "\n";
                                                                print FILE "\n";
                                                                print FILE "\n";
                                                                print FILE "\n";
                                                                print FILE "\n";
                                                                unfile_lock(FILE);
                                                                close(FILE);




                                                                open(FILE, ">$memberdir/$appusername.pref");
                                                                file_lock(FILE);
                                                                print FILE "1\n";
                                                                print FILE "1\n";
                                                                print FILE "1\n";
                                                                print FILE "1\n";
                                                                print FILE "0\n";
                                                                print FILE "\n";
                                                                print FILE "0\n";
                                                                print FILE "1\n";
                                                                unfile_lock(FILE);
                                                                close(FILE);

                                                                 if ($welcome_im == 1) {
                                                                  open(FILE, "$datadir/welcomeim.txt");
                                                                  file_lock(FILE);
                                                                  chomp(@lines = <FILE>);
                                                                  unfile_lock(FILE);
                                                                  close(FILE);

                                                                  open(FILE, ">$memberdir/$appusername.msg");
                                                                  file_lock(FILE);
                                                                  print FILE "admin|$lines[0]|$date|$lines[1]|\n";
                                                                  unfile_lock(FILE);
                                                                  close(FILE);
                                                                 }

                                                                open(FILE, "$memberdir/memberlist.dat");
                                                                file_lock(FILE);
                                                                @members = <FILE>;
                                                                unfile_lock(FILE);
                                                                close(FILE);

                                                                open(FILE, ">$memberdir/memberlist.dat");
                                                                file_lock(FILE);
                                                                foreach $curmem (@members) { print FILE "$curmem"; }
                                                                print FILE "$appusername\n";
                                                                unfile_lock(FILE);
                                                                close(FILE);

                                                                if ($appnewletter eq "on") {
                                                                open(FILE,"$datadir/newsletter/emails.txt");
                                                                @subscribers = <FILE>;
                                                                close(FILE);
                                                                $x=0;
                                                                                 foreach $subscriber(@subscribers) {chomp($subscriber); if ($appemail eq $subscriber){  $x=1;}}
                                                                                                                  if ($x eq 0) {
                                                                                                                  open(FILE, ">>$datadir/newsletter/emails.txt") || (print "Error");
                                                                                                                  file_lock(FILE);
                                                                                                                  print FILE "$appemail\n";
                                                                                                                  unfile_lock(FILE);
                                                                                                                  close(FILE);
                                                                                 }
                                                                }

                                                                $subject = "$msg{'008'} $pagename";
                                                                $message = qq~$inf{'023'}        $inf{'008'}
                                                                $msg{'006'} $appusername
                                                                $msg{'009'} $actualpass~;
                                                                sendemail($appemail, $subject, $message, $webmaster_email);

                                                                open (FILE, "$memberdir/forapproval.dat") || error("$err{'001'} $memberdir/forapproval.dat");
                                                                file_lock(FILE);
                                                                @threads = <FILE>;
                                                                unfile_lock(FILE);
                                                                close (FILE);

                                                                open (FILE, ">$memberdir/forapproval.dat") || error("$err{'016'} $memberdir/forapproval.dat");
                                                                file_lock(FILE);
                                                                for ($a = 0; $a < @threads; $a++) {
                                                                ($actualpass, $cryptedpass, $appusername, $appemail, $appnewletter, $applang) = split(/\|/,$threads[$a]);

                                                                if ($appusername eq $info{'myappusername'}) { print FILE ""; }
                                                                else { print FILE "$threads[$a]"; }

                                                                }
                                                                unfile_lock(FILE);
                                                                close(FILE);

                                                                open(FILE, "$memberdir/forapprovallist.dat");
                                                                file_lock(FILE);
                                                                chomp(@members = <FILE>);
                                                                unfile_lock(FILE);
                                                                close(FILE);

                                                                open(FILE, ">$memberdir/forapprovallist.dat");
                                                                file_lock(FILE);
                                                                foreach $curmem (@members) {
                                                                                                if ($curmem ne $info{'myappusername'}) { print FILE "$curmem\n"; }
                                                                }
                                                                unfile_lock(FILE);
                                                                close(FILE);
                                                                }
        }

}

else {

        open (FILE, "$memberdir/forapproval.dat") || error("$err{'001'} $memberdir/forapproval.dat");
        file_lock(FILE);
        @threads = <FILE>;
        unfile_lock(FILE);
        close (FILE);

        open (FILE, ">$memberdir/forapproval.dat") || error("$err{'016'} $memberdir/forapproval.dat");
        file_lock(FILE);
        for ($a = 0; $a < @threads; $a++) {
                ($actualpass, $cryptedpass, $appusername, $appemail, $appnewletter, $applang) = split(/\|/,$threads[$a]);
                                                                        if ($appusername eq $info{'myappusername'}) { print FILE "";
                                                                        }        else { print FILE "$threads[$a]";
                                                                        }
        }
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$memberdir/forapprovallist.dat");
        file_lock(FILE);
        chomp(@members = <FILE>);
        unfile_lock(FILE);
        close(FILE);

         open(FILE, ">$memberdir/forapprovallist.dat");
        file_lock(FILE);
        foreach $curmem (@members) {
        if ($curmem ne $info{'myappusername'}) { print FILE "$curmem\n"; }
        }
        unfile_lock(FILE);
        close(FILE);

}

print "Location: $pageurl/$admin&op=userapproval\n\n";

}

# userranks implementation from YaWPs and writer Demigod

###############
sub userranks {
###############
if ($access[35] ne "on") { error("$err{'011'}"); }


        open(FILE, "$memberdir/membergroups.dat") || error("$err{'001'} $topicsdir/cats.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        @req_posts = qw(0 25 50 75 100 250 500);

        $navbar = "$btn{'014'} $nav{'062'} $btn{'014'} $mnu{'012'}";

        print_top();
        print "<table>";

        $num = 0;
        foreach $line (@membergroups) {
                chomp($line);
                print qq~<form  onSubmit="submitonce(this)"  action="$admin&amp;op=userranks2" method="post">
<tr>
<td>$msg{'219'}</td>
<td><input type="text" name="lvl" value="$line">&nbsp;<input type="submit" value="$btn{'030'}"><input type="hidden" name="line" value="$num"></td>
</tr>
</form>
~;
                $num++;
        }
        print "</table>\n";
        print_bottom();
        exit;
}

################
sub userranks2 {
################
if ($access[35] ne "on") { error("$err{'011'}"); }

        open(FILE, "$memberdir/membergroups.dat") || error("$err{'001'} $memberdir/membergroups.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $num = 0;
        open(FILE, ">$memberdir/membergroups.dat") || error("$err{'001'} $memberdir/membergroups.dat");
        file_lock(FILE);
        foreach $line (@membergroups) {
                $line =~ s/\n//g;
                if ($num eq $input{'line'}) { print FILE "$input{'lvl'}\n"; }
                else { print FILE "$line\n"; }
                $num++;
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin&op=userranks\n\n";
        exit;
}

##ADDED KLAUS 3/18
###############
sub userstate {
###############
if ($access[35] ne "on") { error("$err{'011'}"); }


        open(FILE, "$memberdir/memberstatus.dat") || error("$err{'001'} $topicsdir/memberstatus.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $navbar = "$btn{'014'} $nav{'062'} $btn{'014'} $mnu{'013'}";

        print_top();
        print "<table>";

        $num = 0;
        foreach $line (@membergroups) {
                chomp($line);
                print qq~<form  onSubmit="submitonce(this)"  action="$admin&amp;op=userstate2" method="post">
<tr>
<td>$msg{'220'}</td>
<td><input type="text" name="lvl" value="$line"> <input type="submit" value="$btn{'030'}"><input type="hidden" name="line" value="$num"></td>
</tr>
</form>
~;
                $num++;
        }
        print "</table>\n";
        print_bottom();
        exit;
}

################
sub userstate2 {
################
if ($access[35] ne "on") { error("$err{'011'}"); }


        open(FILE, "$memberdir/memberstatus.dat") || error("$err{'001'} $memberdir/memberstatus.dat");
        file_lock(FILE);
        @membergroups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        $num = 0;
        open(FILE, ">$memberdir/memberstatus.dat") || error("$err{'001'} $memberdir/memberstatus.dat");
        file_lock(FILE);
        foreach $line (@membergroups) {
                $line =~ s/\n//g;
                if ($num eq $input{'line'}) { print FILE "$input{'lvl'}\n"; }
                else { print FILE "$line\n"; }
                $num++;
        }
        unfile_lock(FILE);
        close(FILE);

        print "Location: $pageurl/$admin&op=userstate\n\n";
        exit;
}


#################
sub admineditmember {
#################
        if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }

print_top();

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

print qq~


<table cellpadding="3" cellspacing="3" width="100%" border="0"><tr>
<td colspan="2" class="texttitle">Editing $mymemsettings[1]</td>
</tr>
</table>


<table cellpadding="3" cellspacing="3" width="100%" border="0">
<TR><TD VALIGN="Top">

<TABLE cellpadding="2" cellspacing="2" border="0" WIDTH="50%">
  <TR>
    <TD class="forumwindow3">&nbsp; &nbsp;Pick a Task:</TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=viewprofile&username=$info{'username'}">View $mymemsettings[1]'s Profile</A></TD>
  </TR>
~;
if ($access[19] eq "on") {
print qq~
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=admineditprofile&username=$info{'username'}">Edit $mymemsettings[1]'s Profile</A></TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=admineditemail&username=$info{'username'}">Edit $mymemsettings[1]'s E-Mail Address</A></TD>
  </TR>
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=admineditpassword&username=$info{'username'}">Change $mymemsettings[1]'s Password</A></TD>
  </TR>
~;
}
if ($access[25] eq "on") {
print qq~
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=admineditrankstatus&username=$info{'username'}">Change $mymemsettings[1]'s Rank</A></TD>
  </TR>
~;
}
if ($access[23] eq "on") {
print qq~
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=admineditaccess&username=$info{'username'}">Change $mymemsettings[1]'s Access</A></TD>
  </TR>
~;
}

if ($access[26] eq "on") {
print qq~
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="http://www.sanctuaryeq2.com/cgi-bin/index.cgi?action=viewlog&username=$info{'username'}">View $mymemsettings[1]'s Log File</A></TD>
  </TR>
~;
}

if ($access[21] eq "on") {
print qq~
  <TR>
    <TD class="forumwindow1"><img src="http://www.sanctuaryeq2.com/themes/standard/images/dot.gif">&nbsp; &nbsp;<A HREF="javascript:killEntry('index.cgi?action=admindeleteprofile&deleteduser=$info{'username'}')">Delete $mymemsettings[1]</A></TD>
  </TR>
~;
}
print qq~
</TABLE>

~;

print_bottom();
        exit;

}

#################
sub admineditemail {
#################

        if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }

if ($access[19] ne "on") { error("$err{'011'}"); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$mymemsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$mymemsettings[16]";
        $about =~ s/\&\&/\n/g;

        #if ($settings[0] ne "$mymemsettings[0]" && $settings[7] ne "$root") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'161'} $btn{'014'} $mymemsettings[1]";
        print_top();
        print qq~<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=admineditprofile2" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Edit $mymemsettings[1]'s E-Mail Address</td>
</TR>
<tr>
<td><b>$msg{'007'}</b></td>
<td><input type="text" name="email" size="40" value="$mymemsettings[2]"></td>
</tr>
<TR>
<td colspan="2">

<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="passwrd1" size="20" value="$mymemsettings[0]">
<input type="hidden" name="passwrd2" size="20" value="$mymemsettings[0]">
<input type="hidden" name="name" size="40" value="$mymemsettings[1]">
<input type="hidden" name="websitetitle" value="$mymemsettings[3]">
<input type="hidden" name="websiteurl" value="$mymemsettings[4]">
<input type="hidden" name="icq" value="$mymemsettings[8]">
<input type="hidden" name="aim" value="$mymemsettings[23]">
<input type="hidden" name="yahoo" value="$mymemsettings[24]">
<input type="hidden" name="gen" value="$mymemsettings[22]">
<input type="hidden" name="ages" value="$mymemsettings[17]">
<input type="hidden" name="marstat" value="$mymemsettings[20]">
<input type="hidden" name="state" value="$mymemsettings[19]">
<input type="hidden" name="profession" value="$mymemsettings[21]">
<input type="hidden" name="fav" size="40" maxlength="200" value="$mymemsettings[18]">
<input type="hidden" name="about" value="$about">
<input type="hidden" name="signature" value="$signature">
<input type="hidden" name="theme" value="$mymemsettings[13]">
<input type="hidden" name="memberpic" value="$mymemsettings[9]">
<input type="hidden" name="settings6" size="4" value="$mymemsettings[6]">
<input type="hidden" name="settings11" size="4" value="$mymemsettings[11]">
<input type="hidden" name="settings12" size="4" value="$mymemsettings[12]">
<input type="hidden" name="settings14" value="$mymemsettings[14]">
<input type="hidden" name="settings7" value="$mymemsettings[7]">
<input type="hidden" name="settings8" value="$mymemsettings[8]">
<input type="hidden" name="settings10" value="$mymemsettings[10]">
<input type="hidden" name="settings15" value="$mymemsettings[15]">
<input type="hidden" name="settings25" value="$mymemsettings[25]">
<input type="hidden" name="settings26" value="$mymemsettings[26]">


<input type="submit" name="moda" value="$btn{'006'}">

</td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;

}

#################
sub admineditpassword {
#################

        if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }

if ($access[19] ne "on") { error("$err{'011'}"); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$mymemsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$mymemsettings[16]";
        $about =~ s/\&\&/\n/g;

        #if ($settings[0] ne "$mymemsettings[0]" && $settings[7] ne "$root") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'161'} $btn{'014'} $mymemsettings[1]";
        print_top();
        print qq~<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=admineditprofile2" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Change $mymemsettings[1]'s E-Mail Password</td>
</TR>
<tr>
<td><b>$msg{'009'}</b></td>
<td><input type="password" name="passwrd1" size="20" value="$mymemsettings[0]"></td>
</tr>
<tr>
<td><b>$msg{'009'}</b></td>
<td><input type="password" name="passwrd2" size="20" value="$mymemsettings[0]"></td>
</tr>
<TR>
<td colspan="2">
<input type="submit" name="moda" value="$btn{'006'}">


<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="email" size="40" value="$mymemsettings[2]">
<input type="hidden" name="name" size="40" value="$mymemsettings[1]">
<input type="hidden" name="websitetitle" value="$mymemsettings[3]">
<input type="hidden" name="websiteurl" value="$mymemsettings[4]">
<input type="hidden" name="icq" value="$mymemsettings[8]">
<input type="hidden" name="aim" value="$mymemsettings[23]">
<input type="hidden" name="yahoo" value="$mymemsettings[24]">
<input type="hidden" name="gen" value="$mymemsettings[22]">
<input type="hidden" name="ages" value="$mymemsettings[17]">
<input type="hidden" name="marstat" value="$mymemsettings[20]">
<input type="hidden" name="state" value="$mymemsettings[19]">
<input type="hidden" name="profession" value="$mymemsettings[21]">
<input type="hidden" name="fav" size="40" maxlength="200" value="$mymemsettings[18]">
<input type="hidden" name="about" value="$about">
<input type="hidden" name="signature" value="$signature">
<input type="hidden" name="theme" value="$mymemsettings[13]">
<input type="hidden" name="memberpic" value="$mymemsettings[9]">
<input type="hidden" name="settings6" size="4" value="$mymemsettings[6]">
<input type="hidden" name="settings11" size="4" value="$mymemsettings[11]">
<input type="hidden" name="settings12" size="4" value="$mymemsettings[12]">
<input type="hidden" name="settings14" value="$mymemsettings[14]">
<input type="hidden" name="settings7" value="$mymemsettings[7]">
<input type="hidden" name="settings8" value="$mymemsettings[8]">
<input type="hidden" name="settings10" value="$mymemsettings[10]">
<input type="hidden" name="settings15" value="$mymemsettings[15]">
<input type="hidden" name="settings25" value="$mymemsettings[25]">
<input type="hidden" name="settings26" value="$mymemsettings[26]">




</td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}

#################
sub admineditrankstatus {
#################



        if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }

if ($access[25] ne "on") { error("$err{'011'}"); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$mymemsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$mymemsettings[16]";
        $about =~ s/\&\&/\n/g;

        #if ($settings[0] ne "$mymemsettings[0]" && $settings[7] ne "$root") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'161'} $btn{'014'} $mymemsettings[1]";
        print_top();
        print qq~<table border="0" cellspacing="1">
<tr>
<td>

<form action="$pageurl/$cgi?action=admineditprofile2" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Change $mymemsettings[1]'s Rank</td>
</TR>
~;
        open(FILE, "$memberdir/membergroups.dat");
        file_lock(FILE);
        @groups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        my @superusers = @groups[0..3];

        if ($settings[7] eq $root) {
                $position = "";
                if ($mymemsettings[7] eq "") { $position = qq~$position<option value="$line" selected>$line</option>\n~; }
                foreach $line (@superusers) {
                        $line =~ s/[\n\r]//g;
                        if ($mymemsettings[7] eq $line) { $position = qq~$position<option value="$line" selected>$line</option>\n~; }
                else { $position = qq~$position<option value="$line">$line</option>\n~; }
                }

        open(FILE, "$memberdir/memberstatus.dat");
        file_lock(FILE);
        @groups = <FILE>;
        unfile_lock(FILE);
        close(FILE);

        my @superusers = @groups[0..4];

                $position1 = "";
                if ($mymemsettings[14] eq "") { $position1 = qq~$position1<option value="$line" selected>$line</option>\n~; }
                foreach $line (@superusers) {
                        $line =~ s/[\n\r]//g;
                        if ($mymemsettings[14] eq $line) { $position1 = qq~$position1<option value="$line" selected>$line</option>\n~; }
                else { $position1 = qq~$position1<option value="$line">$line</option>\n~; }
                }


print qq~

<tr>
<td><b>$msg{'024'}</b></td>
<td><select name="settings14">
$position1</select>
    <input type="Hidden" name="settings7" value="Member">
</td>
</tr>
<tr>
<td><!-- <b>$msg{'011'}</b> --></td>
<td><!-- <select name="settings7">
$position</select> --></td>
</tr>

<TR>
<td colspan="2">


<input type="hidden" name="passwrd1" size="20" value="$mymemsettings[0]">
<input type="hidden" name="passwrd2" size="20" value="$mymemsettings[0]">
<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="email" size="40" value="$mymemsettings[2]">
<input type="hidden" name="name" size="40" value="$mymemsettings[1]">
<input type="hidden" name="websitetitle" value="$mymemsettings[3]">
<input type="hidden" name="websiteurl" value="$mymemsettings[4]">
<input type="hidden" name="icq" value="$mymemsettings[8]">
<input type="hidden" name="aim" value="$mymemsettings[23]">
<input type="hidden" name="yahoo" value="$mymemsettings[24]">
<input type="hidden" name="gen" value="$mymemsettings[22]">
<input type="hidden" name="ages" value="$mymemsettings[17]">
<input type="hidden" name="marstat" value="$mymemsettings[20]">
<input type="hidden" name="state" value="$mymemsettings[19]">
<input type="hidden" name="profession" value="$mymemsettings[21]">
<input type="hidden" name="fav" size="40" maxlength="200" value="$mymemsettings[18]">
<input type="hidden" name="about" value="$about">
<input type="hidden" name="signature" value="$signature">
<input type="hidden" name="theme" value="$mymemsettings[13]">
<input type="hidden" name="memberpic" value="$mymemsettings[9]">
<input type="hidden" name="settings6" size="4" value="$mymemsettings[6]">
<input type="hidden" name="settings11" size="4" value="$mymemsettings[11]">
<input type="hidden" name="settings12" size="4" value="$mymemsettings[12]">
<input type="hidden" name="settings8" value="$mymemsettings[8]">
<input type="hidden" name="settings10" value="$mymemsettings[10]">
<input type="hidden" name="settings15" value="$mymemsettings[15]">
<input type="hidden" name="settings25" value="$mymemsettings[25]">
<input type="hidden" name="settings26" value="$mymemsettings[26]">


<input type="submit" name="moda" value="$btn{'006'}">

</td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;

}

#################
sub admineditaccess {
#################
        if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }

if ($access[23] ne "on") { error("$err{'011'}"); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        open(FILE, "$memberdir/$info{'username'}.acc");
        file_lock(FILE);
        chomp(@mymemaccess = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        #if ($settings[0] ne "$mymemsettings[0]" && $settings[7] ne "$root") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'161'} $btn{'014'} $mymemsettings[1]";
        print_top();
print qq~
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">Edit $mymemsettings[1]'s Access</td>
</TR>
</TABLE>

<FORM action="$pageurl/$cgi?action=admineditaccess2" method="post" name="creator">

    <TABLE BORDER="0" CELLPADDING="2" WIDTH=75%>
      <TR>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>Site Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
        <TD></TD>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>News Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editwelcomemessage" VALUE="on"~;
if ($mymemaccess[0] eq "on") { print "   CHECKED" }
if ($access[0] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Welcome Message</TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="addnews" VALUE="on"~;
if ($mymemaccess[1] eq "on") { print "   CHECKED" }
if ($access[1] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Add News</TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editguestwelcomemessage" VALUE="on"~;
if ($mymemaccess[2] eq "on") { print "   CHECKED" }
if ($access[2] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Guest Welcome Message</TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="editnews" VALUE="on"~;
if ($mymemaccess[3] eq "on") { print "   CHECKED" }
if ($access[3] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit News/Comments</TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editmenus" VALUE="on"~;
if ($mymemaccess[4] eq "on") { print "   CHECKED" }
if ($access[4] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Menus</TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="edittopicsnews" VALUE="on"~;
if ($mymemaccess[5] eq "on") { print "   CHECKED" }
if ($access[5] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Topic Categories</TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editwelcomeim" VALUE="on"~;
if ($mymemaccess[6] eq "on") { print "   CHECKED" }
if ($access[6] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Welcome Instant Message</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="pageadmin" VALUE="on"~;
if ($mymemaccess[7] eq "on") { print "   CHECKED" }
if ($access[7] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Page Admin</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="blockadmin" VALUE="on"~;
if ($mymemaccess[8] eq "on") { print "   CHECKED" }
if ($access[8] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Block Admin</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="broadcast" VALUE="on"~;
if ($mymemaccess[34] eq "on") { print "   CHECKED" }
if ($access[34] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Broadcast Message</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="serverconfig" VALUE="on"~;
if ($mymemaccess[35] eq "on") { print "   CHECKED" }
if ($access[35] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Server Configuration</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>Security Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
        <TD></TD>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>Forum Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="iplistadmin" VALUE="on"~;
if ($mymemaccess[9] eq "on") { print "   CHECKED" }
if ($access[9] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>IP Access List Admin</TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="editfourmcats" VALUE="on"~;
if ($mymemaccess[10] eq "on") { print "   CHECKED" }
if ($access[10] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Categories (reorder/create/remove)</TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="editfourmwords" VALUE="on"~;
if ($mymemaccess[11] eq "on") { print "   CHECKED" }
if ($access[11] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Set censored words</TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="editfourmboards" VALUE="on"~;
if ($mymemaccess[12] eq "on") { print "   CHECKED" }
if ($access[12] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Boards (reorder/create/remove)</TD>
      </TR>

  <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="poststicky" VALUE="on"~;
if ($mymemaccess[28] eq "on") { print "   CHECKED" }
if ($access[28] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Post Stickey</TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="editposts" VALUE="on"~;
if ($mymemaccess[30] eq "on") { print "   CHECKED" }
if ($access[30] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Posts</TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="deleteposts" VALUE="on"~;
if ($mymemaccess[31] eq "on") { print "   CHECKED" }
if ($access[31] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Delete Posts</TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="moveposts" VALUE="on"~;
if ($mymemaccess[32] eq "on") { print "   CHECKED" }
if ($access[32] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Move Posts</TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="showip" VALUE="on"~;
if ($mymemaccess[33] eq "on") { print "   CHECKED" }
if ($access[33] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Show Ip Address</TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>

      <TR>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>Gallery Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
        <TD></TD>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>Poll Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="galleryadmin" VALUE="on"~;
if ($mymemaccess[13] eq "on") { print "   CHECKED" }
if ($access[13] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~ DISABLED></TD>
        <TD><FONT COLOR=gray>Gallery Admin Tools</TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="polladmin" VALUE="on"~;
if ($mymemaccess[14] eq "on") { print "   CHECKED" }
if ($access[14] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Poll Admin (edit/create)</TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="createalbum" VALUE="on"~;
if ($mymemaccess[15] eq "on") { print "   CHECKED" }
if ($access[15] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~ DISABLED></TD>
        <TD><FONT COLOR=gray>Create an Album</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="addpictures" VALUE="on"~;
if ($mymemaccess[16] eq "on") { print "   CHECKED" }
if ($access[16] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~ DISABLED></TD>
        <TD><FONT COLOR=gray>Add Pictures</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editalbum" VALUE="on"~;
if ($mymemaccess[17] eq "on") { print "   CHECKED" }
if ($access[17] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~ DISABLED></TD>
        <TD><FONT COLOR=gray>Edit an Album</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="deletealbum" VALUE="on"~;
if ($mymemaccess[18] eq "on") { print "   CHECKED" }
if ($access[18] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~ DISABLED></TD>
        <TD><FONT COLOR=gray>Delete Album</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>User Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
        <TD></TD>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>Calendar Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editmembers" VALUE="on"~;
if ($mymemaccess[19] eq "on") { print "   CHECKED" }
if ($access[19] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Members Profiles</TD>
        <TD></TD>
        <TD>
          <INPUT TYPE="checkbox" NAME="addevents" VALUE="on"~;
if ($mymemaccess[20] eq "on") { print "   CHECKED" }
if ($access[20] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~>
<INPUT TYPE="hidden" NAME="deleteevents" VALUE="off">
<INPUT TYPE="hidden" NAME="editevents" VALUE="off">
</TD>
        <TD>Add/Edit/Delete Events</TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="deletemembers" VALUE="on"~;
if ($mymemaccess[21] eq "on") { print "   CHECKED" }
if ($access[21] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Delete Members</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editmemberaccess" VALUE="on"~;
if ($mymemaccess[23] eq "on") { print "   CHECKED" }
if ($access[23] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Members Access</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editmemberrank" VALUE="on"~;
if ($mymemaccess[25] eq "on") { print "   CHECKED" }
if ($access[25] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Members Ranks</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="viewmemberlog" VALUE="on"~;
if ($mymemaccess[26] eq "on") { print "   CHECKED" }
if ($access[26] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>View Member Log</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD COLSPAN=2><CENTER>
              <HR COLOR=blue>
            <B>Link Administration</B><BR>
              <HR COLOR=blue>
          </CENTER>
        </TD>
        <TD></TD>
        <TD COLSPAN=2>        </TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editlinkcats" VALUE="on"~;
if ($mymemaccess[27] eq "on") { print "   CHECKED" }
if ($access[27] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Edit Link Categorys</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD>
          <INPUT TYPE="checkbox" NAME="editlinks" VALUE="on"~;
if ($mymemaccess[29] eq "on") { print "   CHECKED" }
if ($access[29] ne "on") { print "   DISABLED" }
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~></TD>
        <TD>Add/Move/Delete Links</TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>
      <TR>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
        <TD></TD>
      </TR>

      <TR>
        <TD COLSPAN=5>
<input type="hidden" name="username" value="$info{'username'}">
<input type="submit" name="moda" value="Edit Access"~;
if ($info{'username'} eq "admin") { print "   DISABLED" }
print qq~>

        </TD>
      </TR>
    </TABLE>




</FORM>

~;
        print_bottom();
        exit;
}

#################
sub admineditaccess2 {
#################

                open(FILE, ">$memberdir/$input{'username'}.acc") || error("$err{'016'} $input{'username'}.acc");
                file_lock(FILE);
print FILE "$input{'editwelcomemessage'}\n";
print FILE "$input{'addnews'}\n";
print FILE "$input{'editguestwelcomemessage'}\n";
print FILE "$input{'editnews'}\n";
print FILE "$input{'editmenus'}\n";
print FILE "$input{'edittopicsnews'}\n";
print FILE "$input{'editwelcomeim'}\n";
print FILE "$input{'pageadmin'}\n";
print FILE "$input{'blockadmin'}\n";
print FILE "$input{'iplistadmin'}\n";
print FILE "$input{'editfourmcats'}\n";
print FILE "$input{'editfourmwords'}\n";
print FILE "$input{'editfourmboards'}\n";
print FILE "$input{'galleryadmin'}\n";
print FILE "$input{'polladmin'}\n";
print FILE "$input{'createalbum'}\n";
print FILE "$input{'addpictures'}\n";
print FILE "$input{'editalbum'}\n";
print FILE "$input{'deletealbum'}\n";
print FILE "$input{'editmembers'}\n";
print FILE "$input{'addevents'}\n";
print FILE "$input{'deletemembers'}\n";
print FILE "$input{'deleteevents'}\n";
print FILE "$input{'editmemberaccess'}\n";
print FILE "$input{'editevents'}\n";
print FILE "$input{'editmemberrank'}\n";
print FILE "$input{'viewmemberlog'}\n";
print FILE "$input{'editlinkcats'}\n";
print FILE "$input{'poststicky'}\n";
print FILE "$input{'editlinks'}\n";
print FILE "$input{'editposts'}\n";
print FILE "$input{'deleteposts'}\n";
print FILE "$input{'moveposts'}\n";
print FILE "$input{'showip'}\n";
print FILE "$input{'broadcast'}\n";
print FILE "$input{'serverconfig'}\n";
                unfile_lock(FILE);
                close(FILE);

done();

}

#################
sub admineditprofile {
#################
        if ($info{'username'} =~ /\//){ error("$err{'004'}" ); }
        if ($info{'username'} =~ /\\/){ error("$err{'004'}" ); }

if ($access[19] ne "on") { error("$err{'011'}"); }

        open(FILE, "$memberdir/$info{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        $signature = "$mymemsettings[5]";
        $signature =~ s/\&\&/\n/g;

        $about = "$mymemsettings[16]";
        $about =~ s/\&\&/\n/g;

        #if ($settings[0] ne "$mymemsettings[0]" && $settings[7] ne "$root") { error("$err{'011'}"); }

        $navbar = "$btn{'014'} $nav{'161'} $btn{'014'} $mymemsettings[1]";
        print_top();
        print qq~<table border="0" cellspacing="1">
<tr>
<td><form action="$pageurl/$cgi?action=admineditprofile2" method="post" name="creator">
<table border="0">
<tr>
<td class="formstexttitle" colspan="2">$mymemsettings[1]'s Profile</td>
</TR>
<tr>
<td><b>$msg{'013'}</b></td>
<td><input type="text" name="name" size="40" value="$mymemsettings[1]">*</td>
</tr>


<tr>
<td><b>$msg{'014'}</b></td>
<td><input type="hidden" name="websitetitle" value="$mymemsettings[3]">~; if ($mymemsettings[3] ne "") {print qq~$mymemsettings[3]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<td><b>$msg{'015'}</b></td>
<td><input type="hidden" name="websiteurl" value="$mymemsettings[4]">~; if ($mymemsettings[4] ne "") {print qq~$mymemsettings[4]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<td><b>$msg{'016'}</b></td>
<td><input type="hidden" name="icq" value="$mymemsettings[8]">~; if ($mymemsettings[8] ne "") {print qq~$mymemsettings[8]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'661'}</td>
<td width="70%"><input type="hidden" name="aim" value="$mymemsettings[23]">~; if ($mymemsettings[23] ne "") {print qq~$mymemsettings[23]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'662'}</td>
<td width="70%"><input type="hidden" name="yahoo" value="$mymemsettings[24]">~; if ($mymemsettings[24] ne "") {print qq~$mymemsettings[24]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'650'}</td>
<td width="70%"><input type="hidden" name="gen" value="$mymemsettings[22]">~; if ($mymemsettings[22] ne "") {print qq~$mymemsettings[22]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'651'}</td>
<td width="70%"><input type="hidden" name="ages" value="$mymemsettings[17]">~; if ($mymemsettings[17] ne "") {print qq~$mymemsettings[17]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'654'}</td>
<td width="70%"><input type="hidden" name="marstat" value="$mymemsettings[20]">~; if ($mymemsettings[20] ne "") {print qq~$mymemsettings[20]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<td><b>$msg{'655'}</b></td>
<td width="70%"><textarea name="about" rows="4" cols="35" maxlength="50" wrap="virtual">$about</textarea></td>
</tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'652'}</td>
<td width="70%"><input type="hidden" name="state" value="$mymemsettings[19]">~; if ($mymemsettings[19] ne "") {print qq~$mymemsettings[19]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<tr>
<td class="formstextnormal" width="30%">$msg{'653'}</td>
<td width="70%"><input type="hidden" name="profession" value="$mymemsettings[21]">~; if ($mymemsettings[21] ne "") {print qq~$mymemsettings[21]~;} else {print qq~$msg{'666'}~;} print qq~</td>
</tr>
<tr>
<td><b>$msg{'656'}</b></td>
<td><input type="text" name="fav" size="40" maxlength="200" value="$mymemsettings[18]"></td>
</tr>

<tr>
<td class="formstexttitle" colspan="2">$mymemsettings[1]'s Signature</td>
</TR>

</tr>
<td valign="top" class="formstextnormal" width="30%">$msg{'017'}</td>
<td width="70%"><textarea name="signature" rows="4" cols="35" wrap="virtual">$signature</textarea></td>
</tr>
<tr>
<td class="formstexttitle" colspan="2">$mymemsettings[1]'s Theme Settings</td>
</TR>
<tr>
<td valign="top"><b>$msg{'161'}</b></td>
<td><select name="theme"> ~;

     open(FILE, "$themesdir/themes.dat");
     file_lock(FILE);
     @themes = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@themes) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);

        if ($mymemsettings[13] eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option><br>~; }
        else { print qq~<option value="$item[1]">$item[0]</option><br>~; }

     }
     print qq~</select> </td>
</tr>
<tr>
<td class="formstexttitle" colspan="2">$mymemsettings[1]'s Member Pic</td>
</TR>
~;
        opendir(DIR, "$imagesdir/avatars");
        @contents = readdir(DIR);
        closedir(DIR);

        $images = "";
        if ($mymemsettings[9] eq "") { $mymemsettings[9] = "_nopic.gif"; }
        foreach $line (sort @contents) {
                ($name, $extension) = split (/\./, $line);
                $checked = "";
                if ($line eq $mymemsettings[9]) { $checked = " selected"; }
                if ($mymemsettings[9] =~ m~\Ahttp://~ && $line eq "") { $checked = " selected"; }
                if ($extension =~ /gif/i || $extension =~ /jpg/i || $extension =~ /jpeg/i || $extension =~ /png/i ) {
                        if ($line eq "_nopic.gif") {
                                $name = "";
                                $pic = "_nopic.gif";
                        }
                        $images .= qq~<option value="$line"$checked>$name</option>\n~;
                }
        }
        if ($mymemsettings[9] =~ m~\Ahttp://~) {
                $pic = "$mymemsettings[9]";
                $checked = " checked";
                $tmp = $mymemsettings[9];
        }
        else {
                $pic = "$imagesurl/avatars/$mymemsettings[9]";
                $tmp = "http://";
        }
        print qq~<tr>
<td valign="top"><b>$msg{'018'}</b></td>
<td valign="top">
<table>
<tr>
<td>$msg{'012'}</td>
</tr>
<tr>
<td>

<script language="javascript" type="text/javascript">
<!--
function showImage() {
document.images.avatars.src="$imagesurl/avatars/"+document.creator.memberpic.options[document.creator.memberpic.selectedIndex].value;
}
// -->
</script>


<select name="memberpic" onChange="showImage()" size="6">
$images</select>
<img src="$pic" name="avatars" border="0" hspace="15"></td>
</tr>
<tr>
<td>$msg{'020'}</td>
</tr>
<tr>
<td><input type="checkbox" name="memberpicpersonalcheck"$checked>
<input type="text" name="memberpicpersonal" size="40" value="$tmp"><br>
$msg{'019'}</td>
</tr>
</table>
</td>
</tr>

<tr>
<td colspan="2">* $msg{'025'}</td>
</tr>
<tr>
<td colspan="2">
<input type="hidden" name="username" value="$info{'username'}">
<input type="hidden" name="passwrd1" size="20" value="$mymemsettings[0]">
<input type="hidden" name="passwrd2" size="20" value="$mymemsettings[0]">
<input type="hidden" name="email" size="40" value="$mymemsettings[2]">

<input type="hidden" name="settings6" size="4" value="$mymemsettings[6]">
<input type="hidden" name="settings11" size="4" value="$mymemsettings[11]">
<input type="hidden" name="settings12" size="4" value="$mymemsettings[12]">
<input type="hidden" name="settings14" value="$mymemsettings[14]">
<input type="hidden" name="settings7" value="$mymemsettings[7]">

<input type="hidden" name="settings8" value="$mymemsettings[8]">
<input type="hidden" name="settings10" value="$mymemsettings[10]">
<input type="hidden" name="settings15" value="$mymemsettings[15]">
<input type="hidden" name="settings25" value="$mymemsettings[25]">
<input type="hidden" name="settings26" value="$mymemsettings[26]">
~;
        #}


print qq~
<input type="submit" name="moda" value="$btn{'006'}">
</td>
</tr>
</table>
</form>
</td>
</tr>
</table>
~;
        print_bottom();
        exit;
}
}

##################
sub admineditprofile2 {
##################

        if ($info{'username'} =~ /\//) { error("$err{'004'}" ); }
        if ($input{'passwrd1'} ne "$input{'passwrd2'}") { error("$err{'012'}"); }
        if ($input{'passwrd1'} eq "") { error("$err{'009'}"); }
        if ($input{'name'} eq "") { error("$err{'013'}"); }
        #if ($input{'name'} !~ /^[0-9A-Za-z#%+,-\.:=?@^_ ]+$/) { error("$err{'006'}"); }
        #if ($input{'name'} eq "|") { error("$err{'006'}"); }
        #if ($input{'name'} =~ /$anonuser/i) { error("$err{'006'}"); }

        if ($input{'email'} eq "") { error("$err{'005'}"); }

        if ($input{'memberpicpersonalcheck'} && ( $input{'memberpicpersonal'} =~ m/\.gif\Z/i || $input{'memberpicpersonal'} =~ m/\.jpg\Z/i || $input{'memberpicpersonal'} =~ m/\.jpeg\Z/i || $input{'memberpicpersonal'} =~ m/\.png\Z/i ) ) {
                $input{'memberpic'} = $input{'memberpicpersonal'};
        }
        #if ($input{'memberpic'} !~ m^\A[0-9a-zA-Z_\.\#\%\-\:\+\?\$\&\~\.\,\@/]+\Z^) { error("$err{'006'}"); }
    if ($input{'ages'} eq "") {$ages = "";
        } else {$ages = "$input{'ages'}";}
        if ($input{'marstat'} eq "") {$marstat = "";
        } else {$marstat = "$input{'marstat'}";}
        if ($input{'aim'} eq "") {$aim = "";
        } else {$aim = "$input{'aim'}";}
        if ($input{'state'} eq "") {$state = "";
        } else {$state = "$input{'state'}";}
        if ($input{'gen'} eq "") {$gen = "";
        } else {$gen = "$input{'gen'}";}
        if ($input{'profession'} eq "") {$profession = "";
        } else {$profession = "$input{'profession'}";}
        open(FILE, "$memberdir/$input{'username'}.dat") || error("$err{'010'}");
        file_lock(FILE);
        chomp(@mymemsettings = <FILE>);
        unfile_lock(FILE);
        close(FILE);

        if ($input{'passwrd1'} eq $mymemsettings[0]) { $passwrd = $input{'passwrd1'}; }
        else { $passwrd = crypt($input{'passwrd1'}, substr($input{'username'}, 0, 2)); }

        if ($input{'moda'} eq "$btn{'006'}") {
                open(FILE, ">$memberdir/$input{'username'}.dat") || error("$err{'016'} $input{'username'}.dat");
                file_lock(FILE);
                print FILE "$passwrd\n";
                print FILE "$input{'name'}\n";
                print FILE "$input{'email'}\n";
                print FILE "$input{'websitetitle'}\n";
                print FILE "$input{'websiteurl'}\n";
                if ($input{'signature'} eq "") { $input{'signature'} = "$msg{'026'}"; }
                $input{'signature'} =~ s/\n/\&\&/g;
                $input{'signature'} =~ s/\r//g;
                print FILE "$input{'signature'}\n";
                print FILE "$input{'settings6'}\n";
                print FILE "$input{'settings7'}\n";
                print FILE "$input{'icq'}\n";
                print FILE "$input{'memberpic'}\n";
                print FILE "$input{'settings10'}\n";
                print FILE "$input{'settings11'}\n";
                print FILE "$input{'settings12'}\n";
                print FILE "$input{'theme'}\n";
                print FILE "$input{'settings14'}\n";
                print FILE "$input{'settings15'}\n";
                if ($input{'about'} eq "") { $input{'about'} = "Me"; }
                $input{'about'} =~ s/\n/\&\&/g;
                $input{'about'} =~ s/\r//g;
                print FILE "$input{'about'}\n";
                print FILE "$input{'ages'}\n";
                print FILE "$input{'fav'}\n";
                print FILE "$input{'state'}\n";
                print FILE "$input{'marstat'}\n";
                print FILE "$input{'profession'}\n";
                print FILE "$input{'gen'}\n";
                print FILE "$input{'aim'}\n";
                print FILE "$input{'yahoo'}\n";
                print FILE "$input{'settings25'}\n";
                print FILE "$input{'settings26'}\n";
                unfile_lock(FILE);
                close(FILE);

                open(FILE, "$memberdir/$input{'username'}.dat");
                file_lock(FILE);
                @settings = <FILE>;
                unfile_lock(FILE);
                close(FILE);

                for( $i = 0; $i < @settings; $i++ ) {
                        $settings[$i] =~ s~[\n\r]~~g;
                }
                done();

        }
        if ($input{'delt'} eq "$btn{'007'}") {areyou_sureadmin();
                }
}

############
sub done {
############
        $navbar = " $btn{'014'} $nav{'027'}";
        print_top();
        print qq~
<a href="$pageurl/$cgi?action=memberlist">$nav{'019'}</a><BR>
<a href="$pageurl/$cgi">$nav{'052'}</a>~;
        print_bottom();
        exit;
}


###############
sub editbanip {
###############

if ($access[9] ne "on") { error("$err{'011'}"); }

  open (FILE , "$datadir/banned/banned_ip.txt") || error("$err{'001'} $datadir/banned/banned_ip.txt");
  file_lock(FILE);
  my @data = <FILE>;
  unfile_lock (FILE);
  close (FILE);
#  print $ban_dir;
#  print $test[0];

        $navbar = "$btn{'014'} $mnu{'025'}";
        print_top();
        print qq ~
 <center><b>$msg{'224'}</b></center><p>
  <table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
  <tr>
  <td>
  <table width="100%" border="0" cellspacing="1" cellpadding="2">
  <tr>
  <td bgcolor="$windowbg"><b>$msg{'225'}</b></td>
  <td bgcolor="$windowbg"><b>$msg{'226'}</b></td>
  ~;
  foreach (@data) {
     chomp;
     print qq~<tr>
     <td bgcolor="$windowbg">$_</td>
     <td bgcolor="$windowbg">[<a href="$admin&amp;op=deletebannedip&amp;$ip=$_">$nav{'097'}</a>]</td>
      ~;
    }
        print qq ~
  <form  onSubmit="submitonce(this)"  action="$pageurl/$admin&amp;op=addbannedip" method="post">
  <tr>
    <td bgcolor="$windowbg">$msg{'227'}</td>
    <td bgcolor="$windowbg">
      <input type="text" name="ipaddress">
      <input type="submit" name="moda" value="$btn{'031'}"></td>
    </td>
  </tr>
  </form>
  </table>
  </table>
  ~;
  print_bottom();
}

####################
sub deletebannedip {
####################

if ($access[9] ne "on") { error("$err{'011'}"); }

                my %linea;
    $navbar ="$btn{'014'} $mnu{'036'}";
    print_top();
    open (FILE , "$datadir/banned/banned_ip.txt") || error("$err{'001'} $datadir/banned/banned_ip.txt");
    file_lock(FILE);
    while (<FILE>) {
    $li = $_;
        chomp;
        $linea{$_} = '1';
    }
    unfile_lock (FILE);
    close (FILE);
    open (FILE2 , "+>$datadir/banned/banned_ip.txt") || error("$err{'001'} $datadir/banned/banned_ip.txt");
    foreach $clave (keys %linea) {
            if ($clave eq $info{$ip}) {
                $linea{$info{$ip}} = 0;
                print "$msg{'225'} $info{$ip} $msg{'228'}";
            }
            else {
              print FILE2 "$clave\n";
            }

    }
    close (FILE2);
    unfile_lock (FILE2);
    print qq ~
    <p><b>$msg{'229'} $msg{'224'}</b>
    ~;
    print_bottom();
}

#################
sub addbannedip {
#################

if ($access[9] ne "on") { error("$err{'011'}"); }
                $navbar ="$btn{'014'} $mnu{'037'}";
    print_top();
    open (FILE , ">>$datadir/banned/banned_ip.txt") || error("$err{'001'} $datadir/banned/banned_ip.txt");
    file_lock(FILE);
    print FILE "$input{'ipaddress'}\n";
    unfile_lock (FILE);
    close (FILE);
    print "$input{'ipaddress'} $msg{'230'}";
    print qq ~
    <p><b>$msg{'229'} $msg{'224'}</b>
    ~;
    print_bottom();
}

############
sub backup {
############
if ($access[35] ne "on") { error("$err{'011'}"); }

                                $navbar = "$btn{'014'} $nav{'042'} $btn{'014'} Tar.gz";
                                print_top();
                                print qq~<form  onSubmit="submitonce(this)"  action="$scripturl/$cgi?action=backup2" method="post">
                                <table border="0" width="100%" cellpading="0" cellspacing="0">
                                <tr>
                                <td colspan="2" align="center"><b><u>$nav{'111'}</u></b></td>
                                </tr>
                                <tr>
                                <td>$msg{'479'}<br>
                                <input type="text" name="outfile" value="$outfile" size="40"></td>
                                </tr>
                                <tr>
                                <td><input type="submit" value="$btn{'042'}">
                                <input type="reset" value="$btn{'009'}"></td>
                                </tr>
                                </table>
                                </form>
                                ~;
                                print_bottom(); exit;  }


###########
sub backup2 {
###########

if ($access[35] ne "on") { error("$err{'011'}"); }

# location of tar
$tar_loc = '/bin/tar';

# location of gzip
$gzip_loc = '/bin/gzip';

# the output gzip filename - admin names to anything he wants..
# This makes it basically unhackable and unable for a regular user to download
$output= "$basedir/$input{'outfile'}.tar.gz";

# the  output file
$htmlout = "$baseurl/$input{'outfile'}.tar.gz";

# the temporary tar file (this will be deleted)
$tar_temp = "$datadir/bk.tar";

$navbar = "$btn{'014'} $nav{'042'} $btn{'014'} Tar.gz";
print_top();
print qq~
<html>

<font size="2" face="arial"><b>$nav{'111'}</b></font><br><br>
~;

open(TAR, "$tar_loc cf $tar_temp $datadir/* |");
print qq~<font size="2 face="arial"><b>1.</b> $msg{'480'} [ </font>
<font size="1" face="arial">$tar_temp</font>
<font size="2" face="arial"> ]</font>
~;

close(TAR);

print qq~<form  onSubmit="submitonce(this)" >
<font size="2" face="arial"><b>2.</b> $msg{'481'} [ </font>
<font size="1" face="arial">$tar_temp</font>
<font size="2" face="arial"> ] : </font>
<br>&nbsp;&nbsp;&nbsp;&nbsp;<select name="">
~;

open (EXE, "$tar_loc tf $tar_temp |");
@data=<EXE>;
close(EXE);

foreach $file (@data)
                                {
                                print "<option value=\"\">$file<option>\n";
                                }

open(GZ, "$gzip_loc -c $tar_temp > $output |");
print qq~ </select><br><br>
<font size="2" face="arial"><b>3.</b> $msg{'482'} [ </font>
<font size="1" face="arial">$output</font>
<font size="2" face="arial"> ]</font><br><br>~;
close(GZ);

unlink("$tar_temp");
print qq~<font size="2" face="arial"><b>4.</b> $msg{'483'} [ </font>
<font size="1" face="arial">$tar_temp</font>
<font size="2" face="arial"> ]</font><br><br>~;

print qq~<font size="2" face="arial"><b>5.</b> $msg{'484'} [ </font>
<font size="1" face="arial"><a href="$htmlout">$htmlout</a></font>
<font size="2 face="arial"> ]</font><br>~;

print qq~

<br><br>
</body>
</html>
~;

print_bottom();
exit;
}

#################################################################################
# Subs for site config
#################################################################################

###########
sub general_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~<tr align="center">
        <td colspan="2"><b><u>$nav{'099'}</u></b></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'333'}</u></b></td>
</tr>
<tr>
<td>$msg{'232'}<br>
<input type="text" name="page_name" value="$pagename" size="30"></td>
<td>$msg{'234'}<br>
<input type="text" name="page_title" value="$pagetitle" size="30"></td>
</tr>
<tr>
<td>$msg{'233'}<br>
<input type="text" name="page_url" value="$pageurl" size="30"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'334'}</u></b></td>
</tr>
<tr>
<td>$msg{'236'}<br>
<input type="text" name="cookieusername" value="$cookieusername" size="30"></td>
<td>$msg{'237'}<br>
<input type="text" name="cookiepassword" value="$cookiepassword" size="30"></td>
</tr>
<tr>
<td>$msg{'238'}<br>
<input type="text" name="cookieusertheme" value="$cookieusertheme" size="30"></td>
<td>$msg{'239'}<br>
<input type="text" name="cookieuserlang" value="$cookieuserlang" size="30"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'335'}</u></b></td>
</tr>
<tr>
<td>$msg{'331'}<br>
<input type="text" name="lang_dir" value="$langdir" size="30"></td>
<td>$msg{'332'}<br>
<input type="text" name="default_lang" value="$language" size="30"></td>
</tr>
<tr>
<td>$msg{'254'}<br>
<input type="text" name="backup_lang" value="$lang" size="30"><BR></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'336'}</u></b></td>
</tr>
<tr>
<td>$msg{'240'}<br>
<input type="checkbox" name="mailtype"   $mailchecked><small> ($msg{'328'})</small></td>
<td>$msg{'241'}<br>
<input type="text" name="mailprog" value="$mailprogram" size="30"></td>
</tr>
<tr>
<td>$msg{'242'}<br>
<input type="text" name="smtp_server" value="$smtp_server" size="30"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'337'}</u></b></td>
</tr>
<tr>
<td>$msg{'244'}<br>
<input type="text" name="base_url" value="$baseurl" size="30"></td>
<td>$msg{'245'}<br>
<input type="text" name="script_url" value="$scripturl" size="30"></td>
<tr>
<td>$msg{'246'}<br>
<input type="text" name="script_dir" value="$scriptdir" size="30"></td>
<td>$msg{'247'}<br>
<input type="text" name="lib_dir" value="$sourcedir" size="30"></td>
</tr>
<tr>
<td>$msg{'243'}<br>
<input type="text" name="base_dir" value="$basedir" size="30"></td>
<td>$msg{'235'}<br>
<input type="text" name="cgi" value="$cgi" size="30"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'338'}</u></b></td>
</tr>
<tr>
<td>$msg{'248'}<br>
<input type="text" name="data_dir" value="$datadir" size="30"></td>
<td>$msg{'249'}<br>
<input type="text" name="member_dir" value="$memberdir" size="30"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'339'}</u></b></td>
</tr>
<tr>
<td>$msg{'250'}<br>
<input type="text" name="images_dir" value="$imagesdir" size="30"></td>
<td>$msg{'251'}<br>
<input type="text" name="themes_dir" value="$themesdir" size="30"></td>
</tr>
<tr>
<td>$msg{'252'}<br>
<input type="text" name="images_url" value="$imagesurl" size="30"></td>
<td>$msg{'253'}<br>
<input type="text" name="themes_url" value="$themesurl" size="30"></td>
</tr>
</table>~
}

###########
sub contact_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~
<tr align="center">
<td colspan="2"><b><u>$nav{'100'}</u></b></td>
</tr>
<tr>
<td>$msg{'256'}<br>
<input type="text" name="compname" value="$compname" size="30"></td>
<td>$msg{'257'}<br>
<input type="text" name="compadd" value="$compadd" size="30"></td>
</tr>
<tr>
<td>$msg{'258'}<br>
<input type="text" name="compcity" value="$compcity" size="30"></td>
<td>$msg{'259'}<br>
<input type="text" name="compstate" value="$compstate" size="30"></td>
</tr>
<tr>
<td>$msg{'260'}<br>
<input type="text" name="compzip" value="$compzip" size="30"></td>
<td>$msg{'261'}<br>
<input type="text" name="compphone" value="$compphone" size="30"></td>
</tr>
<tr>
<td>$msg{'262'}<br>
<input type="text" name="compfax" value="$compfax" size="30"></td>
<td>$msg{'538'}<br>
<input type="text" name="compemail" value="$compemail" size="30"></td>
</tr>
<tr>
<td>$msg{'539'}<br>
<input type="text" name="webmaster_email" value="$webmaster_email" size="30"></td>
</tr>
</table>
~
}

###########
sub im_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~
<tr>
<td colspan="2" align="center"><b><u>$nav{'102'}</u></b></td>
</tr>
<tr>
<td>$msg{'269'}<br>
<input type="checkbox" name="welcome_im"  $welcome_imchecked><small>($msg{'312'})</small></td>
<td>$msg{'469'}<br>
<input type="checkbox" name="newuser_im"  $newuser_imchecked><small>($msg{'312'})</small></td>
</tr>
<tr>
<td>$msg{'470'}<br>
<input type="checkbox" name="article_im"  $article_imchecked><small>($msg{'312'})</small></td>
</tr>
<tr>
<td>$msg{'271'}<br>
<input type="text" name="bmbgcolor" value="$bmbgcolor" size="12"><BR></td>
<td>$msg{'270'}<br>
<input type="text" name="bmheadercolor" value="$bmheadercolor" size="12"></td>
</tr>
</table>
~
}

###########
sub information_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~
<tr>
<td colspan="2" align="center"><b><u>$msg{'272'}</u></b></td>
</tr>
<tr>
<td>$msg{'274'} 1<br>
<input type="text" name="image1" value="$image1" size="30"></td>
<td>$msg{'275'} 1<br>
<input type="text" name="link1" value="$link1" size="30"></td>
</tr>
<tr>
<td>$msg{'274'} 2<br>
<input type="text" name="image2" value="$image2" size="30"></td>
<td>$msg{'275'} 2<br>
<input type="text" name="link2" value="$link2" size="30"></td>
</tr>
<tr>
<td>$msg{'274'} 3<br>
<input type="text" name="image3" value="$image3" size="30"></td>
<td>$msg{'275'} 3<br>
<input type="text" name="link3" value="$link3" size="30"></td>
</tr>
</table>
~
}

###########
sub editorsdesk_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~
<tr>
<td colspan="2" align="center"><b><u>$nav{'004'}&nbsp;&amp;&nbsp;$nav{'003'}</u></b></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'104'}</u></b></td>
</tr>
<tr>
<td>$msg{'277'}<br>
<input type="text" name="topic_dir" value="$topicsdir" size="30"></td>
<td>$msg{'278'}<br>
<input type="text" maxlength="2" name="maxnews" value="$maxnews" size="1"></td>
</tr>
<tr>
<td>$msg{'279'}<br>
<input type="text" maxlength="2" name="maxtopics" value="$maxtopics" size="1"></td>
<td>$msg{'280'}<br>
<input type="checkbox" name="enable_userarticles" $enable_userarticleschecked> <small>($msg{'282'})</small></td>
</tr>
<tr>
<td>$msg{'281'}<br>
<input type="checkbox" name="allow_html" $allow_htmlchecked> <small>($msg{'282'})</small></td>
<td>$msg{'283'}<br>
<input type="checkbox" name="enable_topicguestposting" $enable_topicguestpostingchecked><small>($msg{'282'})</small></td>
</tr>
<tr>
<td>$msg{'542'}<br>
<input type="checkbox" name="enable_autopublish" $enable_autopublishchecked> <small>($msg{'282'})</small></td>
<td>$msg{'485'}<br>
<input type="text" name="article_imrecip" value="$article_imrecip" size="12"><small>($msg{'471'})</small></td>
</tr>
<tr>
<td>$msg{'606'}<br>
<input type="checkbox" name="topicimgupld" $topicimgupldchecked> <small>$msg{'607'}</small></td>
<td>&nbsp;</td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'105'}</u></b></td>
</tr>
<tr>
<td>$msg{'285'}<br>
<input type="text" name="forum_dir" value="$boardsdir" size="30"></td>
<td>$msg{'286'}<br>
<input type="text" name="message_dir" value="$messagedir" size="30"></td>
</tr>
<tr>
<td>$msg{'287'}<br>
<input type="checkbox" name="enable_guestposting" $enable_guestpostingchecked> <small>($msg{'282'})</small></td>
<td>$msg{'288'}<br>
<input type="checkbox"  name="enable_notification"  $enable_notificationchecked> <small>($msg{'282'})</small></td>
</tr>
<tr>
<td>$msg{'289'}<br>
<input type="text" maxlength="2" name="maxdisplay" value="$maxdisplay" size="1"></td>
<td>$msg{'290'}<br>
<input type="text" maxlength="2" name="maxmessagedisplay" value="$maxmessagedisplay" size="1"></td>
</tr>
<tr>
<td>$msg{'291'}<br>
<input type="text" maxlength="3" name="max_log_days_old" value="$max_log_days_old" size="1"></td>
<td>$msg{'292'}<br>
<input type="checkbox" name="insert_original" $insert_originalchecked> <small>($msg{'293'})</small></td>
</tr>
<tr>
<td>$msg{'571'}<br>
<input type="checkbox" name="imageicons" $imageiconschecked> <small>($msg{'572'})</small></td>
<td>$msg{'606'}<br>
<input type="checkbox" name="forumimgupld" $forumimgupldchecked> <small>$msg{'607'}</small></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'541'}</u></b></td>
</tr>
<tr>
<td>$msg{'294'}<br>
<input type="checkbox"name="enable_ubbc" $enable_ubbcchecked> <small>($msg{'282'})</small></td>
<td>$msg{'540'}<br>
<input type="checkbox"name="enable_smile" $enable_smilechecked> <small>($msg{'282'})</small></td>
</tr>
<tr>
<td>$msg{'608'}<br>
<input type="text" name="upload_dir" value="$uploaddir" size="30"></td>
<td>$msg{'610'}<br>
<input type="text" name="upload_url" value="$uploadurl" size="30"></td>
</tr>
<tr>
<td>$msg{'609'}<br>
<input type="text" name="maxuploadsize" value="$maxuploadsize" size="5"></td>
<td>&nbsp;</td>
</tr>
</table>
~
}

###########
sub stats_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~
<tr>
<td colspan="2" align="center"><b><u>$nav{'106'}</u></b></td>
</tr>
<tr>
<td>$msg{'296'}<br>
<input type="text" name="log_dir" value="$logdir" size="30"></td>
<td>$msg{'297'}<br>
<input type="text" maxlength="3" name="ip_time" value="$ip_time" size="1"></td>
</tr>
<tr>
<td>$msg{'298'}<br>
<input type="checkbox" name="top_browsers" $top_browserschecked> <small>($msg{'299'})</small></td>
<td>$msg{'300'}<br>
<input type="checkbox" name="top_os" $top_oschecked> <small>($msg{'299'})</small></td>
</tr>
</table>
~
}

###########
sub links_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~
<tr>
<td colspan="2" align="center"><b><u>$nav{'107'}&nbsp;&amp;&nbsp;$nav{'108'}</u></b></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'107'}</u></b></td>
</tr>
<tr>
<td>$msg{'302'}<br>
<input type="text" name="links_dir" value="$linksdir" size="30"></td>
<td>$msg{'303'}<br>
<input type="text"  name="maxlinks" value="$maxlinks" ></td>
</tr>
<tr>
<td>$msg{'304'}<br>
<input type="checkbox" name="adminonlyl" $adminonlylchecked><small>($msg{'299'})</small></td>
<td>$msg{'675'}<br>
<input type="checkbox" name="showlatestlinks" $showlatestlinkschecked><small>($msg{'299'})</small></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'108'}</u></b></td>
</tr>
<tr>
<td>$msg{'306'}<br>
<input type="text" name="download_dir" value="$downloadsdir" size="30"></td>
<td>$msg{'307'}<br>
<input type="text"  name="maxdownloads" value="$maxdownloads" ></td>
</tr>
<tr>
<td>$msg{'308'}<br>
<input type="checkbox" name="antileech" $antileechchecked><small>($msg{'299'})</small></td>
<td>$msg{'309'}<br>
<input type="checkbox" name="adminonlyd" $adminonlydchecked><small>($msg{'299'})</small></td>
</tr>
<tr>
<td>$msg{'676'}<br>
<input type="checkbox" name="showlatestdownloads" $showlatestdownloadschecked><small>($msg{'299'})</small></td>
</tr>
</table>
~
}

###########
sub others_options {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

($dummy, $ntime) = split(/ - /, $date);
print qq~
<tr>
<td colspan="2" align="center"><b><u>$nav{'113'}</u></b></td>
</tr>
<tr>
<td>$msg{'322'}<br>
<input type="text" maxlength="3" name="memberpic_height" value="$memberpic_height" size="3"></td>
<td>$msg{'323'}<br>
<input type="text" maxlength="3" name="memberpic_width" value="$memberpic_width" size="3"></td>
</tr>
<tr>
<td>$msg{'321'} ($msg{'564'} $ntime)<br>
<select name="timeoffset">~;

                        open (ZONES,"<$datadir/timezones.dat") || error("$err{'016'} $datadir/timezones.dat");
      @timezones=<ZONES>;
      close (ZONES);

                        foreach $zone (@timezones) {
                                                $zone =~ s/[\n\r]//g;
                                                @zitem = split(/\|/, $zone);

                                                if ($zitem[1] ne "") {
                                                         if ($zitem[0] eq $timeoffset) {print qq~<option value="$zitem[0]" selected>$zitem[1]</option>~;} else {print qq~<option value="$zitem[0]">$zitem[1]</option>~;}
                                                }
                        }

print qq~</select></td>
<td>$msg{'324'}<br>
<input type="checkbox" name="use_flock" $use_flockchecked> <small>($msg{'299'})</small></td>
</tr>
<tr>
<td>$msg{'325'}<br>
<input type="text" maxlength="2" name="LOCK_EX" value="$LOCK_EX" size="1"></td>
<td>$msg{'326'}<br>
<input type="text" maxlength="2" name="LOCK_UN" value="$LOCK_UN" size="1"></td>
</tr>
<tr>
<td>$msg{'327'}<br>
<select name="IIS">
~;
if ($IIS eq 0) {print qq~<option value="0" selected>Auto</option>~;} else {print qq~<option value="0">auto</option>~;}
if ($IIS eq 1) {print qq~<option value="1" selected>IIS</option>~;} else {print qq~<option value="1">IIS</option>~;}
if ($IIS eq 2) {print qq~<option value="2" selected>Apache</option>~;} else {print qq~<option value="2">Apache</option>~;}
print qq~</select></td>
<td>Server OS<br>
<select name="server_os">
~;
if ($server_os eq "linux") {print qq~<option value="linux" selected>Linux</option>~;} else {print qq~<option value="linux">Linux</option>~;}
if ($server_os eq "windows") {print qq~<option value="windows" selected>Windows</option>~;} else {print qq~<option value="windows">Windows</option>~;}
print qq~</select></td>
</tr>
</table>
~
}

###########
sub admin_assistant {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

print qq~
<tr>
<td colspan="2" align="center"><b><u>$nav{'112'}</u></b></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'423'}</u></b></td>
</tr>
<tr>
<td>$msg{'265'}<br>
<input type="checkbox" name="showcon"  $showconchecked><small> ($msg{'312'})</small></td>
<td>$msg{'267'}<br>
<input type="checkbox" name="showcon2" $showcon2checked><small>($msg{'312'})</small></td>
</tr>
<tr>
<td>$msg{'372'}<br>
<input type="checkbox" name="dispmost" $dispmostchecked><small>($msg{'312'})</small></td>
<td>$msg{'474'}<br>
<input type="checkbox" name="hidememlist" $hidememlistchecked><small>($msg{'299'})</small></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'424'}</u></b></td>
</tr>
<tr>
<td>$msg{'374'}<br>
<input type="checkbox" name="letmemdel" $letmemdelchecked><small>($msg{'282'})</small></td>
<td>$msg{'375'}<br>
<input type="checkbox" name="letmemlng" $letmemlngchecked><small>($msg{'282'})</small></td>
</tr>
<tr>
<td>$msg{'376'}<br>
<input type="checkbox" name="letmemthm" $letmemthmchecked><small>($msg{'282'})</small></td>
<td>$msg{'266'}<br>
<input type="checkbox" name="hidemail" $hidemailchecked><small> ($msg{'312'})</small></td>
</tr>
<tr>
<td>$msg{'553'}<br>
<select name="defaulttheme">
~;
     open(FILE, "$themesdir/themes.dat" );
     file_lock(FILE);
     @themes = <FILE>;
     unfile_lock(FILE);
     close(FILE);

     foreach $line (@themes) {
           $line =~ s/[\n\r]//g;
           @item = split(/\|/, $line);
           if ($item[2] ne "0") {
                                         if ($defaulttheme eq $item[1]) { print qq~<option selected value="$item[1]">$item[0]</option>\n~; }
                                         else { print qq~<option value="$item[1]">$item[0]</option>\n~; }
                                         }
                                         }
     print qq~</select>
</td>
<td>$msg{'597'}<br>
<select name="signupmethod">
~;
if ($signupmethod eq 0) {print qq~<option value="0" selected>$msg{'669'}</option>~;} else {print qq~<option value="0">$msg{'669'}</option>~;}
if ($signupmethod eq 1) {print qq~<option value="1" selected>$msg{'670'}</option>~;} else {print qq~<option value="1">$msg{'670'}</option>~;}
if ($signupmethod eq 2) {print qq~<option value="2" selected>$msg{'671'}</option>~;} else {print qq~<option value="2">$msg{'671'}</option>~;}
print qq~</select></tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'581'}</u></b></td>
</tr>
<tr>
<td colspan="2">$msg{'582'}<br>
<select name="timezone">
~;

                        open (ZONES,"<$datadir/timezones.dat") || error("$err{'016'} $datadir/timezones.dat");
      @timezones=<ZONES>;
      close (ZONES);

                        foreach $zone (@timezones) {
                                                $zone =~ s/[\n\r]//g;
                                                @zitem = split(/\|/, $zone);

                                                if ($zitem[0] eq $timezone) {print qq~<option value="$zitem[0]" selected>$zitem[2] $zitem[3]: $zitem[5]</option>~;} else {print qq~<option value="$zitem[0]">$zitem[2] $zitem[3]: $zitem[5]</option>~;}
                        }

print qq~</select>
</td>
<tr>
<td>$msg{'554'}<br>
~;

# For backwards compatability
if ($check_date eq "") { print qq~
<select name="check_date">
<option selected value="american">$msg{'555'}</option>
<option value="european">$msg{'556'}</option>~;
}
if ($check_date eq "american") { print qq~
<select name="check_date">
<option selected value="american">$msg{'555'}</option>
<option value="european">$msg{'556'}</option>~;
}
if ($check_date eq "european") { print qq~
<select name="check_date">
<option selected value="european">$msg{'556'}</option>
<option value="american">$msg{'555'}</option>~;
}

print qq~
</select>
</td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$msg{'425'}</u></b></td>
</tr>
<tr>
<td>$msg{'377'}<br>
<select name="infoblockmod">
~;
if ($infoblockmod eq 0) {print qq~<option value="0" selected>0</option>~;} else {print qq~<option value="0">0</option>~;}
if ($infoblockmod eq 1) {print qq~<option value="1" selected>1</option>~;} else {print qq~<option value="1">1</option>~;}
if ($infoblockmod eq 2) {print qq~<option value="2" selected>2</option>~;} else {print qq~<option value="2">2</option>~;}
print qq~</select> <small>($msg{'379'})</small></td>
<td>$msg{'416'}<br>
<select name="dispfrad">
~;
if ($dispfrad eq 0) {print qq~<option value="0" selected>0</option>~;} else {print qq~<option value="0">0</option>~;}
if ($dispfrad eq 1) {print qq~<option value="1" selected>1</option>~;} else {print qq~<option value="1">1</option>~;}
if ($dispfrad eq 2) {print qq~<option value="2" selected>2</option>~;} else {print qq~<option value="2">2</option>~;}
print qq~</select> <small>($msg{'379'})</small></td>
</tr>
<tr>
<td>$msg{'315'}<br>
<select name="searchmod">
~;
if ($searchmod eq 0) {print qq~<option value="0" selected>$msg{'426'}</option>~;} else {print qq~<option value="0">$msg{'426'}</option>~;}
if ($searchmod eq 1) {print qq~<option value="1" selected>$msg{'427'}</option>~;} else {print qq~<option value="1">$msg{'427'}</option>~;}
if ($searchmod eq 2) {print qq~<option value="2" selected>$msg{'428'}</option>~;} else {print qq~<option value="2">$msg{'428'}</option>~;}
print qq~</select> <small>($msg{'429'})</small></td>
<td>$msg{'373'}<br>
<select name="dispstat">
~;
if ($dispstat eq 0) {print qq~<option value="0" selected>$msg{'430'}</option>~;} else {print qq~<option value="0">$msg{'430'}</option>~;}
if ($dispstat eq 1) {print qq~<option value="1" selected>$msg{'431'}</option>~;} else {print qq~<option value="1">$msg{'431'}</option>~;}
if ($dispstat eq 2) {print qq~<option value="2" selected>$msg{'432'}</option>~;} else {print qq~<option value="2">$msg{'432'}</option>~;}
print qq~</select> <small>($msg{'433'})</small></td>
</tr>
<tr>
<td>$msg{'313'}<br>
<input type="checkbox" name="modulenl" $modulenlchecked><small>($msg{'312'})</small></td>
<td>$msg{'314'}<br>
<input type="checkbox"name="modulenlmem" $modulenlmemchecked><small>($msg{'312'})</small></td>
</tr>
<tr>
<td>$msg{'318'}<br>
<input type="checkbox" name="pollmod" $pollmodchecked><small>($msg{'299'})</small></td>
<td>$msg{'319'}<br>
<input type="checkbox" name="multiplevoting" $multiplevotingchecked><small>($msg{'299'})</small></td>
</tr>
<tr>
<td>$msg{'311'}<br>
<input type="checkbox" name="modulecal" $modulecalchecked><small>($msg{'312'})</small></td>
<td>$msg{'316'}<br>
<input type="checkbox" name="botkiller" $botkillerchecked><small>($msg{'312'})</small></td>
</tr>

</table>
~
}

###########
sub admin_access {
###########
if ($access[35] ne "on") { error("$err{'011'}"); }

($dummy, $ntime) = split(/ - /, $date);
print qq~
<tr>
<td colspan="2" align="center"><b><u>$nav{'162'}</u></b></td>
</tr>
<tr>
<td colspan="2" align="center"><b>$msg{'579'}</b></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'042'}</u></b></td>
</tr>
<tr>
<td>$msg{'417'}<br>
<input type="checkbox" name="editwelc" $editwelcchecked></td>
<td>$mnu{'039'}<br>
<input type="checkbox" name="editabout" $editaboutchecked></td>
</tr>
<tr>
<td>$msg{'269'}<br>
<input type="checkbox" name="editim" $editimchecked></td>
<td>$nav{'061'}<br>
<input type="checkbox" name="editbanner" $editbannerchecked></td>
</tr>
<tr>
<td>$mnu{'040'}<br>
<input type="checkbox" name="editfaq" $editfaqchecked></td>
<td>$mnu{'006'}<br>
<input type="checkbox" name="editdown" $editdownchecked></td>
</tr>
<tr>
<td>$mnu{'007'}<br>
<input type="checkbox" name="editlink" $editlinkchecked></td>
<td>$mnu{'042'}<br>
<input type="checkbox" name="modadmin" $modadminchecked></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'043'}</u></b></td>
</tr>
<tr>
<td>$mnu{'014'}<br>
<input type="checkbox" name="editcats" $editcatschecked></td>
<td>$mnu{'015'}<br>
<input type="checkbox" name="editboards" $editboardschecked></td>
</tr>
<tr>
<td>$mnu{'016'}<br>
<input type="checkbox" name="editcensor" $editcensorchecked></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'044'}</u></b></td>
</tr>
<tr><td>$mnu{'031'}<br>
<input type="checkbox" name="editpoll" $editpollchecked></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'024'}</u></b></td>
</tr>
<tr>
<td>$mnu{'018'}<br>
<input type="checkbox" name="pubnews" $pubnewschecked></td>
<td>$mnu{'019'}<br>
<input type="checkbox" name="editnews" $editnewschecked></td>
</tr>
<tr>
<td>$mnu{'020'}<br>
<input type="checkbox" name="edittops" $edittopschecked></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'063'}</u></b></td>
</tr>
<tr>
<td>$mnu{'021'}<br>
<input type="checkbox" name="editlblk" $editlblkchecked></td>
<td>$mnu{'022'}<br>
<input type="checkbox" name="editrblk" $editrblkchecked></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'064'}</u></b></td>
</tr>
<tr>
<td>$mnu{'023'}<br>
<input type="checkbox" name="editcal" $editcalchecked></td>
<td>$mnu{'024'}<br>
<input type="checkbox" name="editnl" $editnlchecked></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>$nav{'070'}</u></b></td>
</tr>
<tr>
<td>$mnu{'025'}<br>
<input type="checkbox" name="editip" $editipchecked></td>
</tr>
</table>
~
}

#######################
sub areyou_sureadmin {
#######################
if ($access[21] ne "on") { error("$err{'011'}"); }
  $deletepositive = "0";
        $navbar = "$btn{'014'} $btn{'007'}";
        print_top();
        print qq~<b>$btn{'007'}?</b><br>
<a href="$cgi\?action=admindeleteprofile&deleteduser=$input{'username'}">$nav{'047'}</a> - <a href="$cgi\?action=editprofile&username=$input{'username'}">$nav{'048'}</a>
~;
        print_bottom();
        exit;

}

#########################
sub admindeleteprofile {
#########################
if ($access[21] ne "on") { error("$err{'011'}"); }
                $deleteduser = $info{'deleteduser'};

                if ($deleteduser ne "admin") {
                unlink("$memberdir/$deleteduser.dat");
                unlink("$memberdir/$deleteduser.msg");
                unlink("$memberdir/$deleteduser.log");
                unlink("$memberdir/$deleteduser.pref");


                open(FILE, "$memberdir/memberlist.dat");
                file_lock(FILE);
                chomp(@members = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                open(FILE, ">$memberdir/memberlist.dat");
                file_lock(FILE);
                foreach $curmem (@members) {
                        if ($curmem ne $deleteduser) { print FILE "$curmem\n"; }
                }
                unfile_lock(FILE);
                close(FILE);

                        print qq~Set-Cookie: $cookieusername=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookiepassword=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookieusertheme=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookieuserlang=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;

                        $username = $anonuser;
                        $password = "";
                        $usertheme = "$defaulttheme";
                        $userlang = $language;
                        @settings = ();
                        $realname = "";
                        $realemail = "";
                        $ENV{'HTTP_COOKIE'} = "";

                        logvisitors();
                        byebye();
                        } else {
                                                print qq~Set-Cookie: $cookieusername=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookiepassword=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookieusertheme=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;
                        print qq~Set-Cookie: $cookieuserlang=; path=/; expires=Tue, 01-Jan-1980 00:00:00 GMT;\n~;

                        $username = $anonuser;
                        $password = "";
                        $usertheme = "$defaulttheme";
                        $userlang = $language;
                        @settings = ();
                        $realname = "";
                        $realemail = "";
                        $ENV{'HTTP_COOKIE'} = "";

                        logvisitors();
                        byebye();
                        }
}

#####################
sub installupgrade {
#####################
check_access(); if ($access_granted ne "1") { error("$err{'011'}"); }

        @upgradefiles = ();
        @upgradescripts = ();
        @allupgrades = ();

        $navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $nav{'164'}";
        print_top();

        print qq~<br><b><u>$msg{'679'}</u></b><p>~;

        opendir (DIR, "$scriptdir/upgrade-lib");
        @upgradefiles = readdir(DIR);
        closedir (DIR);
        @upgradescripts = sort @upgradefiles;

     FILE: foreach (@upgradescripts) {
                        next FILE if($_ eq '.');
                        next FILE if($_ eq '..');
                        next FILE if($_ eq 'index.html');
                        next FILE if($_ eq '.htaccess');
                        next FILE if($_ eq 'upgrades.dat');
                        $foundupgradescript = $_;
                        $testinstallscript = $foundupgradescript;
                        $testinstallscript =~ s/.pl//;
                        $upgradefound = "0";
                                open (UPGRADES,"$scriptdir/upgrade-lib/upgrades.dat");
                                while(<UPGRADES>) {
                                chop;
                                @allupgrades = split(/\n/);
                                        if (grep (/\b^$testinstallscript\b/i, @allupgrades) ne "0" ) { $upgradefound = "1"; }
                                }
                                close(UPGRADES);

                        if ($upgradefound eq "0") {print qq~<a href="$pageurl/$admin&amp;op=installupgrade2&amp;upgrade=$testinstallscript"><b>$testinstallscript</b></a><br>~; } else {print qq~<i>$testinstallscript</i><br>~;}

                }

        print qq~<br><b>$msg{'680'}</b><p>~;
        print_bottom();
        exit;

}

####################
sub installupgrade2 {
####################
check_access(); if ($access_granted ne "1") { error("$err{'011'}"); }

        $upgradetoinstall = "$info{'upgrade'}.pl";

        require "$scriptdir/upgrade-lib/$upgradetoinstall"; install_upgrade();

        print "Location: $pageurl/$admin\&op=installupgrade\n\n";
        exit;
}

if (-e "$scriptdir/user-lib/admin.pl") {require "$scriptdir/user-lib/admin.pl"}

1; # return true