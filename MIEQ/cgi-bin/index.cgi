#!/usr/bin/perl

###############################################################################



open (DATA, "./lock/lock.dat");
@data = <DATA>;
close DATA;
chop(@data);

$locked = "@data";

if ($locked eq "LOCKED") {

print "Content-type: text/html\n\n";
print qq~
<CENTER>
<h1>FreeFire Web Site Down for Matanence!</h1>
Please Check back later!
~;

}

else {


$| = 1;

use CGI::Carp qw(fatalsToBrowser);

eval {
        require "config.pl";
        require "$sourcedir/subs.pl";
        require "$sourcedir/forum_display.pl";
        require "$sourcedir/notify.pl";

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
SD: $scriptdir~;
        exit;
}

require "config.pl";
if ($usertheme eq "") { $usertheme eq "$defaulttheme"; }

getlanguage();
ban();
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if ($action eq "register") { require "$sourcedir/user.pl"; register(); }
elsif ($action eq "register2") { require "$sourcedir/user.pl"; register2(); }
elsif ($action eq "help") { require "$sourcedir/help.pl"; help(); }
elsif ($action eq "bannerredirect") { require "$sourcedir/ads.pl"; bannerredirect(); }
elsif ($action eq "about") { require "$sourcedir/about.pl"; about(); }
elsif ($action eq "contact") { require "$sourcedir/contact.pl"; contact(); }
elsif ($action eq "login") { require "$sourcedir/user.pl"; login(); }
elsif ($action eq "login2") { require "$sourcedir/user.pl"; login2(); }
elsif ($action eq "logout") { require "$sourcedir/user.pl"; logout(); }
elsif ($action eq "reminder") { require "$sourcedir/user.pl"; reminder(); }
elsif ($action eq "reminder2") { require "$sourcedir/user.pl"; reminder2(); }
elsif ($action eq "editprofile") { require "$sourcedir/user.pl"; editprofile(); }

elsif ($action eq "editemail") { require "$sourcedir/user.pl"; editemail(); }

elsif ($action eq "editpassword") { require "$sourcedir/user.pl"; editpassword(); }
elsif ($action eq "editoptions") { require "$sourcedir/user.pl"; editoptions(); }
elsif ($action eq "editsig") { require "$sourcedir/user.pl"; editsig(); }
elsif ($action eq "editmagelo") { require "$sourcedir/user.pl"; editmagelo(); }

elsif ($action eq "editprofile2") { require "$sourcedir/user.pl"; editprofile2(); }
elsif ($action eq "editprofile3") { require "$sourcedir/user.pl"; editprofile3(); }
elsif ($action eq "deleteprofile") { require "$sourcedir/user.pl"; deleteprofile(); }
elsif ($action eq "admindeleteprofile") { require "$sourcedir/user.pl"; admindeleteprofile(); }
elsif ($action eq "editpb") { require "$sourcedir/user.pl"; editpb(); }
elsif ($action eq "editpb2") { require "$sourcedir/user.pl"; editpb2(); }
elsif ($action eq "ver") { require "$sourcedir/subs.pl"; ver(); }
elsif ($action eq "viewprofile") { require "$sourcedir/user.pl"; viewprofile(); }
elsif ($action eq "memberlist") { require "$sourcedir/memberlist.pl"; mlist(); }
elsif ($action eq "memberlist2") { require "$sourcedir/memberlist2.pl"; mlist(); }
elsif ($action eq "postnews") { require "$sourcedir/topics.pl"; postnews(); }
elsif ($action eq "postnews2") { require "$sourcedir/topics.pl"; postnews2(); }
elsif ($action eq "viewnews") { require "$sourcedir/topics.pl"; viewnews(); }
elsif ($action eq "commentnews") { require "$sourcedir/topics.pl"; commentnews(); }
elsif ($action eq "otherarticles") {require "$sourcedir/topics.pl"; other_articles(); }
elsif ($action eq "printtopic") {require "$sourcedir/topics.pl"; printtopic(); }
elsif ($action eq "emailtopic") {require "$sourcedir/topics.pl"; emailtopic(); }
elsif ($action eq "emailtopic2") {require "$sourcedir/topics.pl"; emailtopic2(); }
elsif ($action eq "who") { require "$sourcedir/whosonline.pl"; readwho(); }
elsif ($action eq "topics") { require "$sourcedir/topics.pl"; topics(); }
elsif ($action eq "recommend") { require "$sourcedir/recommend.pl"; recommend(); }
elsif ($action eq "recommend2") { require "$sourcedir/recommend.pl"; recommend2(); }
elsif ($action eq "pollit") { require "$sourcedir/poll.pl"; pollit(); }
elsif ($action eq "pollit2") { require "$sourcedir/poll.pl"; pollit2(); }
elsif ($action eq "commentpoll") { require "$sourcedir/poll.pl"; commentpoll(); }
elsif ($action eq "removepollcomment") { require "$sourcedir/poll.pl"; removepollcomment(); }
elsif ($action eq "editpollcomment") { require "$sourcedir/poll.pl"; editpollcomment(); }
elsif ($action eq "editpollcomment2") { require "$sourcedir/poll.pl"; editpollcomment2(); }
elsif ($action eq "stats") { require "$sourcedir/stats.pl"; stats(); }
elsif ($action eq "links") { require "$sourcedir/links.pl"; links(); }
elsif ($action eq "palm") { require "$scriptdir/palm.cgi"; palm(); }
elsif ($action eq "addlink") { require "$sourcedir/links.pl"; addlink(); }
elsif ($action eq "addlink2") { require "$sourcedir/links.pl"; addlink2(); }
elsif ($action eq "editlinks") { require "$sourcedir/links.pl"; editlinks(); }
elsif ($action eq "editlinks2") { require "$sourcedir/links.pl"; editlinks2(); }
elsif ($action eq "deletelinks") { require "$sourcedir/links.pl"; deletelinks(); }
elsif ($action eq "deletelinks2") { require "$sourcedir/links.pl"; deletelinks2(); }
elsif ($action eq "movelinks") { require "$sourcedir/links.pl"; movelinks(); }
elsif ($action eq "movelinks2") { require "$sourcedir/links.pl"; movelinks2(); }
elsif ($action eq "ratelinks") { require "$sourcedir/links.pl"; ratelinks(); }
elsif ($action eq "ratelinks2") { require "$sourcedir/links.pl"; ratelinks2(); }
elsif ($action eq "linkinfo") { require "$sourcedir/links.pl"; link_info(); }
elsif ($action eq "top10") { require "$sourcedir/top10.pl"; show_top10(); }
elsif ($action eq "downloads") { require "$sourcedir/downloads.pl"; downloads(); }
elsif ($action eq "adddownload") { require "$sourcedir/downloads.pl"; adddownload(); }
elsif ($action eq "adddownload2") { require "$sourcedir/downloads.pl"; adddownload2(); }
elsif ($action eq "editdownloads") { require "$sourcedir/downloads.pl"; editdownloads(); }
elsif ($action eq "editdownloads2") { require "$sourcedir/downloads.pl"; editdownloads2(); }
elsif ($action eq "deletedownload") { require "$sourcedir/downloads.pl"; deletedownload(); }
elsif ($action eq "deletedownload2") { require "$sourcedir/downloads.pl"; deletedownload2(); }
elsif ($action eq "movedownload") { require "$sourcedir/downloads.pl"; movedownload(); }
elsif ($action eq "movedownload2") { require "$sourcedir/downloads.pl"; movedownload2(); }
elsif ($action eq "redirect") { require "$sourcedir/links.pl"; redirect(); }
elsif ($action eq "redirectd") { require "$sourcedir/downloads.pl"; redirect(); }
elsif ($action eq "downloadinfo") { require "$sourcedir/downloads.pl"; download_info(); }
elsif ($action eq "ratedownloads") { require "$sourcedir/downloads.pl"; ratedownloads(); }
elsif ($action eq "ratedownloads2") { require "$sourcedir/downloads.pl"; ratedownloads2(); }
elsif ($action eq "search") { require "$sourcedir/search.pl"; find(); }
elsif ($action eq "subscribe") { require "$sourcedir/newsletter.pl"; subscribe(); }
elsif ($action eq "searchuser") { require "$sourcedir/memberlist.pl"; searchuser(); }
elsif ($action eq "anonemail") { require "$sourcedir/emailer.pl";
sendto(); }
elsif ($action eq "sendto2") { require "$sourcedir/emailer.pl";
sendto2(); }
elsif ($action eq "backup") { require "$sourcedir/admin.pl";  backup(); }
elsif ($action eq "backup2") { require "$sourcedir/admin.pl";  backup2(); }
elsif ($action eq "markasread") { require "$sourcedir/forum_mark.pl"; mark_as_read(); }
elsif ($action eq "markpostsread") { require "$sourcedir/forum_mark.pl"; mark_posts_read(); }
elsif ($action eq "uploadpicture") { require "$sourcedir/upload.pl";  uploadpicture(); }
elsif ($action eq "uploadsuccess") { require "$sourcedir/upload.pl";  success(); }
elsif ($action eq "uploadfail") { require "$sourcedir/upload.pl";  failure(); }

elsif ($action eq "im") { require "$sourcedir/instantmessage.pl"; imindex(); }
elsif ($action eq "imremove") { require "$sourcedir/instantmessage.pl"; imremove(); }
elsif ($action eq "imsend") { require "$sourcedir/instantmessage.pl"; impost(); }
elsif ($action eq "imsend2") { require "$sourcedir/instantmessage.pl"; impost2(); }
elsif ($action eq "siteim") { require "$sourcedir/instantmessage.pl"; siteim(); }
elsif ($action eq "siteim2") { require "$sourcedir/instantmessage.pl"; siteim2(); }
elsif ($action eq "adminim") { require "$sourcedir/instantmessage.pl"; adminim(); }
elsif ($action eq "adminim2") { require "$sourcedir/instantmessage.pl"; adminim2(); }
elsif ($action eq "modim") { require "$sourcedir/instantmessage.pl"; modim(); }
elsif ($action eq "modim2") { require "$sourcedir/instantmessage.pl"; modim2(); }

elsif ($action eq "addfolder") {require "$scriptdir/user-lib/instantmessage.pl"; addfolder();}
elsif ($action eq "deletefolder") {require "$scriptdir/user-lib/instantmessage.pl"; deletefolder();}
elsif ($action eq "folder") {require "$scriptdir/user-lib/instantmessage.pl"; folder();}
elsif ($action eq "messagefolder") { require "$scriptdir/user-lib/instantmessage.pl"; foldermessages();}
elsif ($action eq "im4") { require "$scriptdir/user-lib/instantmessage.pl"; foldermessages();}

elsif ($action eq "contacts") { require "$scriptdir/user-lib/instantmessage.pl"; contact();}
elsif ($action eq "addcontact") { require "$scriptdir/user-lib/instantmessage.pl"; addcontact();}
elsif ($action eq "addcontact2") { require "$scriptdir/user-lib/instantmessage.pl"; addcontact2();}
elsif ($action eq "editcontact") { require "$scriptdir/user-lib/instantmessage.pl"; editcontact();}
elsif ($action eq "deletecontact") { require "$scriptdir/user-lib/instantmessage.pl"; deletecontact();}

elsif ($action eq "im") { require "$sourcedir/instantmessage.pl"; imindex(); }
elsif ($action eq "deletefromylog") { require "$scriptdir/user-lib/instantmessage.pl"; deletefromylog(); }
elsif ($action eq "userimindex") { require "$scriptdir/user-lib/instantmessage.pl"; userimindex(); }
elsif ($action eq "userimindex2") { require "$scriptdir/user-lib/instantmessage.pl"; userimindex2(); }
elsif ($action eq "userimindex3") { require "$scriptdir/user-lib/instantmessage.pl"; userimindex3(); }
elsif ($action eq "userimindex4") { require "$scriptdir/user-lib/instantmessage.pl"; userimindex4(); }
elsif ($action eq "messageadmin") { require "$scriptdir/user-lib/instantmessage.pl"; messageadmin(); }
elsif ($action eq "messageadmin2") { require "$scriptdir/user-lib/instantmessage.pl"; messageadmin2();}
elsif ($action eq "messageadmin3") { require "$scriptdir/user-lib/instantmessage.pl"; messageadmin3();}
elsif ($action eq "messageadmin4") { require "$scriptdir/user-lib/instantmessage.pl"; messageadmin4();}
elsif ($action eq "im2") { require "$scriptdir/user-lib/instantmessage.pl"; imfolder(); }
elsif ($action eq "im3") { require "$scriptdir/user-lib/instantmessage.pl"; imsaved();}
elsif ($action eq "imfolder") { require "$scriptdir/user-lib/instantmessage.pl"; imfolder(); }
elsif ($action eq "saveim") { require "$scriptdir/user-lib/instantmessage.pl"; imsaved(); }
elsif ($action eq "moveim") { require "$scriptdir/user-lib/instantmessage.pl"; moveim(); }
elsif ($action eq "moveim2") { require "$scriptdir/user-lib/instantmessage.pl"; moveim2(); }
elsif ($action eq "moveim3") { require "$scriptdir/user-lib/instantmessage.pl"; moveim3(); }
elsif ($action eq "moveim4") { require "$scriptdir/user-lib/instantmessage.pl"; moveim4(); }
elsif ($action eq "imremove") { require "$sourcedir/instantmessage.pl"; imremove(); }
elsif ($action eq "myuserremove") { require "$scriptdir/user-lib/instantmessage.pl"; myuserremove(); }
elsif ($action eq "myuserremove2") { require "$scriptdir/user-lib/instantmessage.pl"; myuserremove2(); }
elsif ($action eq "myuserremove3") { require "$scriptdir/user-lib/instantmessage.pl"; myuserremove3(); }
elsif ($action eq "imremove2") { require "$scriptdir/user-lib/instantmessage.pl"; imremove2(); }
elsif ($action eq "imremove3") { require "$scriptdir/user-lib/instantmessage.pl"; imremove3(); }
elsif ($action eq "imremove4") { require "$scriptdir/user-lib/instantmessage.pl"; imremove4(); }
elsif ($action eq "imremove5") { require "$scriptdir/user-lib/instantmessage.pl"; imremove5(); }
elsif ($action eq "imsend") { require "$sourcedir/instantmessage.pl"; impost(); }
elsif ($action eq "imsend2") { require "$sourcedir/instantmessage.pl"; impost2(); }
elsif ($action eq "siteim") { require "$sourcedir/instantmessage.pl"; siteim(); }
elsif ($action eq "siteim2") { require "$sourcedir/instantmessage.pl"; siteim2(); }
elsif ($action eq "adminim") { require "$sourcedir/instantmessage.pl"; adminim(); }
elsif ($action eq "adminim2") { require "$sourcedir/instantmessage.pl"; adminim2(); }
elsif ($action eq "modim") { require "$sourcedir/instantmessage.pl"; modim(); }
elsif ($action eq "modim2") { require "$sourcedir/instantmessage.pl"; modim2(); }

elsif ($action eq "blistedit") {require "$scriptdir/user-lib/buddylist.pl"; blistedit();}
elsif ($action eq "addbuddy") {require "$scriptdir/user-lib/buddylist.pl"; addbuddy();}
elsif ($action eq "deletebuddy") {require "$scriptdir/user-lib/buddylist.pl"; deletebuddy();}

#######################
# Edit user profile fix
#######################
elsif ($action eq "admineditmember" ) { require "$sourcedir/admin.pl";         admineditmember(); }
elsif ($action eq "admineditemail" ) { require "$sourcedir/admin.pl";         admineditemail(); }
elsif ($action eq "admineditpassword" ) { require "$sourcedir/admin.pl";         admineditpassword(); }
elsif ($action eq "admineditrankstatus" ) { require "$sourcedir/admin.pl";         admineditrankstatus(); }
elsif ($action eq "admineditaccess" ) { require "$sourcedir/admin.pl";         admineditaccess(); }
elsif ($action eq "admineditaccess2" ) { require "$sourcedir/admin.pl";         admineditaccess2(); }
elsif ($action eq "viewlog" ) { require "$sourcedir/admin.pl";         viewlog(); }
elsif ($action eq "viewmasterlog" ) { require "$sourcedir/admin.pl";         viewmasterlog(); }
elsif ($action eq "viewmasterlogb" ) { require "$sourcedir/admin.pl";         viewmasterlogb(); }
elsif ($action eq "admineditprofile" ) { require "$sourcedir/admin.pl";         admineditprofile(); }
        elsif ($action eq "admineditprofile2" ) { require "$sourcedir/admin.pl";         admineditprofile2(); }
        elsif ($action eq "done" ) { require "$sourcedir/admin.pl"; done(); }

#######################
# The Assistant Admin Stuff
#######################

elsif ($action eq "adminlite") {
        $mod68 = qq~$cgi?action=adminlite~;
        $admin = qq~$cgi?action=admin~;
        if ($op eq "") { require "$sourcedir/admin.pl"; siteadmin(); }
        elsif ($op eq "siteadmin") { require "$sourcedir/admin.pl"; siteadmin(); }
        else { require "$sourcedir/admin.pl"; siteadmin(); }
}

#######################
# The Real Admin Stuff
#######################

elsif ($action eq "admin") {
        $admin = qq~$cgi?action=admin~;
        if ($op eq "") { require "$sourcedir/admin.pl"; siteadmin(); }
        elsif ($op eq "siteadmin") { require "$sourcedir/admin.pl"; siteadmin(); }
        elsif ($op eq "siteconfig") { require "$sourcedir/admin.pl"; siteconfig(); }
        elsif ($op eq "siteconfig2") { require "$sourcedir/admin.pl"; siteconfig2(); }
        elsif ($op eq "adminsetup") { require "$sourcedir/admin.pl"; adminsetup(); }
        elsif ($op eq "adminsetup2") { require "$sourcedir/admin.pl"; adminsetup2(); }
        elsif ($op eq "welcomemsg") { require "$sourcedir/admin.pl"; welcomemsg(); }
        elsif ($op eq "welcomemsg2") { require "$sourcedir/admin.pl"; welcomemsg2(); }

elsif ($op eq "broadcast") { require "$sourcedir/admin.pl"; broadcast(); }
elsif ($op eq "broadcast2") { require "$sourcedir/admin.pl"; broadcast2(); }

        elsif ($op eq "guestwelcomemsg") { require "$sourcedir/admin.pl"; guestwelcomemsg(); }
        elsif ($op eq "guestwelcomemsg2") { require "$sourcedir/admin.pl"; guestwelcomemsg2(); }

        elsif ($op eq "aboutinfo") { require "$sourcedir/admin.pl"; aboutinfo(); }
        elsif ($op eq "aboutinfo2") { require "$sourcedir/admin.pl"; aboutinfo2(); }
        elsif ($op eq "agreement") { require "$sourcedir/admin.pl"; agreement(); }
        elsif ($op eq "agreement2") { require "$sourcedir/admin.pl"; agreement2(); }
        elsif ($op eq "welcomeim") { require "$sourcedir/admin.pl"; welcomeim(); }
        elsif ($op eq "welcomeim2") { require "$sourcedir/admin.pl"; welcomeim2(); }
        elsif ($op eq "userapproval") { require "$sourcedir/admin.pl"; userapproval(); }
        elsif ($op eq "userapproval2") { require "$sourcedir/admin.pl"; userapproval2(); }
        elsif ($op eq "userranks") { require "$sourcedir/admin.pl"; userranks(); }
        elsif ($op eq "userranks2") { require "$sourcedir/admin.pl"; userranks2(); }
        elsif ($op eq "userstate") { require "$sourcedir/admin.pl"; userstate(); }
        elsif ($op eq "userstate2") { require "$sourcedir/admin.pl"; userstate2(); }
        elsif ($op eq "managecats") { require "$sourcedir/admin.pl"; managecats(); }
        elsif ($op eq "reordercats") { require "$sourcedir/admin.pl"; reordercats(); }
        elsif ($op eq "removecat") { require "$sourcedir/admin.pl"; removecat(); }
        elsif ($op eq "createcat") { require "$sourcedir/admin.pl"; createcat(); }
        elsif ($op eq "manageboards") { require "$sourcedir/admin.pl"; manageboards(); }
        elsif ($op eq "reorderboards") { require "$sourcedir/admin.pl"; reorderboards(); }
        elsif ($op eq "reorderboards2") { require "$sourcedir/admin.pl"; reorderboards2(); }
        elsif ($op eq "modifyboard") { require "$sourcedir/admin.pl"; modifyboard(); }
        elsif ($op eq "deleteboard") { require "$sourcedir/admin.pl"; deleteboard(); }
        elsif ($op eq "createboard") { require "$sourcedir/admin.pl"; createboard(); }
        elsif ($op eq "reindexlinksadmin") { require "$sourcedir/admin.pl";         reindexlinksadmin(); }
        elsif ($op eq "setcensor") { require "$sourcedir/admin.pl"; setcensor(); }
        elsif ($op eq "setcensor2") { require "$sourcedir/admin.pl"; setcensor2(); }
        elsif ($op eq "polladmin") { require "$sourcedir/admin.pl"; polladmin(); }
        elsif ($op eq "createpoll") { require "$sourcedir/admin.pl"; createpoll(); }
        elsif ($op eq "editpoll") { require "$sourcedir/admin.pl"; editpoll(); }
        elsif ($op eq "editpoll2") { require "$sourcedir/admin.pl"; editpoll2(); }
        elsif ($op eq "editpoll2a") { require "$sourcedir/admin.pl"; editpoll2a(); }
        elsif ($op eq "editpoll3") { require "$sourcedir/admin.pl"; editpoll3(); }
        elsif ($op eq "resetpoll") { require "$sourcedir/admin.pl"; resetpoll(); }
        elsif ($op eq "deletepoll") { require "$sourcedir/admin.pl"; deletepoll(); }
        elsif ($op eq "verifynews") { require "$sourcedir/admin.pl"; verifynews(); }
        elsif ($op eq "verifynews2") { require "$sourcedir/admin.pl"; verifynews2(); }
        elsif ($op eq "modifynews") { require "$sourcedir/admin.pl"; modifynews(); }
        elsif ($op eq "modifynews2") { require "$sourcedir/admin.pl"; modifynews2(); }
        elsif ($op eq "modifynews3") { require "$sourcedir/admin.pl"; modifynews3(); }
        elsif ($op eq "movetopic") { require "$sourcedir/admin.pl"; movetopic(); }
        elsif ($op eq "topicadmin") { require "$sourcedir/admin.pl"; topicadmin(); }
        elsif ($op eq "topicadmin2") { require "$sourcedir/admin.pl"; topicadmin2(); }
        elsif ($op eq "topicadmin3") { require "$sourcedir/admin.pl"; topicadmin3(); }
        elsif ($op eq "newsletter") { require "$sourcedir/newsletter.pl"; newsletter(); }
        elsif ($op eq "sendnewsletter") { require "$sourcedir/newsletter.pl";         sendnewsletter(); }
        elsif ($op eq "sendnewsletter2") { require "$sourcedir/newsletter.pl";         sendnewsletter2(); }
        elsif ($op eq "newslettermsg") { require "$sourcedir/newsletter.pl"; newslettermsg();         }
        elsif ($op eq "newslettermsg2") { require "$sourcedir/newsletter.pl";         newslettermsg2(); }
        elsif ($op eq "editemails") { require "$sourcedir/newsletter.pl"; editemails();         }
        elsif ($op eq "editemails2") { require "$sourcedir/newsletter.pl";         editemails2(); }
        elsif ($op eq "editbanip") { require "$sourcedir/admin.pl";         editbanip(); }
  elsif ($op eq "deletebannedip") { require "$sourcedir/admin.pl";         deletebannedip(); }
  elsif ($op eq "addbannedip") { require "$sourcedir/admin.pl";         addbannedip(); }
        elsif ($op eq "installupgrade") { require "$sourcedir/admin.pl";         installupgrade(); }
        elsif ($op eq "installupgrade2") { require "$sourcedir/admin.pl";         installupgrade2(); }
        else { require "$sourcedir/admin.pl"; siteadmin(); }
}

elsif ($action eq "forum") {
        $forum = qq~$cgi?action=forum&board=$currentboard~;
                if ($currentboard ne "" and $op eq "") {
                open(FILE, "$boardsdir/$currentboard.dat") || error("$err{'001'} $boardsdir/$currentboard.dat");
                file_lock(FILE);
                chomp(@boardinfo=<FILE>);
                unfile_lock(FILE);
                close(FILE);

                $boardname = "$boardinfo[0]";
                $boardmoderator = "$boardinfo[2]";

                open(MODERATOR, "$memberdir/$boardmoderator.dat");
                file_lock(MODERATOR);
                chomp(@modprop = <MODERATOR>);
                unfile_lock(MODERATOR);
                close(MODERATOR);

                $moderatorname = "$modprop[1]";

                require "$sourcedir/forum.pl";
                messageindex();
        }
        # forum_display.pl
        elsif ($currentboard ne "" and $op eq "display") { require "$sourcedir/forum_display.pl"; display(); }
        elsif ($currentboard ne "" and $op eq "displaysticky") { require "$sourcedir/forum_display.pl"; displaysticky(); }
        elsif ($currentboard ne "" and $op eq "printpage" and $action ne "index") { require "$sourcedir/forum_display.pl"; printpage(); }
        # forum_post.pl
        elsif ($currentboard ne "" and $op eq "poststicky" and $action ne "index") { require "$sourcedir/forum_post.pl"; poststicky(); }
        elsif ($currentboard ne "" and $op eq "poststicky2" and $action ne "index") { require "$sourcedir/forum_post.pl"; poststicky2(); }
        elsif ($currentboard ne "" and $op eq "post" and $action ne "index") { require "$sourcedir/forum_post.pl"; post(); }
        elsif ($currentboard ne "" and $op eq "post2" and $action ne "index") { require "$sourcedir/forum_post.pl"; post2(); }
        # forum_admin.pl
        elsif ($currentboard ne "" and $op eq "makesticky" and $action ne "index") { require "$sourcedir/forum_admin.pl"; makestickymessage(); }
        elsif ($currentboard ne "" and $op eq "unstick" and $action ne "index") { require "$sourcedir/forum_admin.pl"; unstickmessage(); }

        elsif ($currentboard ne "" and $op eq "modifysticky" and $action ne "index") { require "$sourcedir/forum_admin.pl"; modifystickymessage(); }
        elsif ($currentboard ne "" and $op eq "modifysticky2" and $action ne "index") { require "$sourcedir/forum_admin.pl"; modifystickymessage2(); }
        elsif ($currentboard ne "" and $op eq "modify" and $action ne "index") { require "$sourcedir/forum_admin.pl"; modifymessage(); }
        elsif ($currentboard ne "" and $op eq "modifystickymessage2" and $action ne "index") { require "$sourcedir/forum_admin.pl"; modifystickymessage2(); }
        elsif ($currentboard ne "" and $op eq "movestickythread" and $action ne "index") { require "$sourcedir/forum_admin.pl"; movestickythread(); }
        elsif ($currentboard ne "" and $op eq "movestickythread2" and $action ne "index") { require "$sourcedir/forum_admin.pl"; movestickythread2(); }
        elsif ($currentboard ne "" and $op eq "removestickythread" and $action ne "index") { require "$sourcedir/forum_admin.pl"; removestickythread(); }
        elsif ($currentboard ne "" and $op eq "removestickythread2" and $action ne "index") { require "$sourcedir/forum_admin.pl"; removestickythread2(); }
        elsif ($currentboard ne "" and $op eq "lockstickythread" and $action ne "index") { require "$sourcedir/forum_admin.pl"; lockstickythread(); }
        elsif ($currentboard ne "" and $op eq "modify" and $action ne "index") { require "$sourcedir/forum_admin.pl"; modifymessage(); }
        elsif ($currentboard ne "" and $op eq "modify2" and $action ne "index") { require "$sourcedir/forum_admin.pl"; modifymessage2(); }
        elsif ($currentboard ne "" and $op eq "movethread" and $action ne "index") { require "$sourcedir/forum_admin.pl"; movethread(); }
        elsif ($currentboard ne "" and $op eq "movethread2" and $action ne "index") { require "$sourcedir/forum_admin.pl"; movethread2(); }
        elsif ($currentboard ne "" and $op eq "removethread" and $action ne "index") { require "$sourcedir/forum_admin.pl"; removethread(); }
        elsif ($currentboard ne "" and $op eq "removethread2" and $action ne "index") { require "$sourcedir/forum_admin.pl"; removethread2(); }
        elsif ($currentboard ne "" and $op eq "lockthread" and $action ne "index") { require "$sourcedir/forum_admin.pl"; lockthread(); }
        # notify.pl
        elsif ($currentboard ne "" and $op eq "notifysticky" and $action ne "index") { require "$sourcedir/notify.pl"; notifysticky(); }
        elsif ($currentboard ne "" and $op eq "notifysticky2" and $action ne "index") { require "$sourcedir/notify.pl"; notifysticky2(); }
        elsif ($currentboard ne "" and $op eq "notify" and $action ne "index") { require "$sourcedir/notify.pl"; notify(); }
        elsif ($currentboard ne "" and $op eq "notify2" and $action ne "index") { require "$sourcedir/notify.pl"; notify2(); }
        elsif ($currentboard ne "" and $op eq "notify_remove" and $action ne "index") { require "$sourcedir/notify.pl"; notify_remove(); }
        elsif ($currentboard ne "" and $op eq "notify_remove_success" and $action ne "index") { require "$sourcedir/notify.pl"; notify_remove_success(); }
        elsif ($currentboard eq "") { require "$sourcedir/forum.pl"; boardindex(); }

}
else { print_main(); }

exit; # all done

}



1;