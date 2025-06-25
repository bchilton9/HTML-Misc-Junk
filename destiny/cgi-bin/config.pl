############################################################################### 
############################################################################### 
# WebAPP - Automated Perl Portal                                              # 
#-----------------------------------------------------------------------------# 
# config.pl                                                                   #
# Version 0.9.8                                                               #
# v0.9.8 (Upgrade Patch v1.9)                                                 # 
# Copyright (C) 2002 by WebAPP                                                #
#                                                                             # 
# Security Patch by Big R                                                     #
# Patching System by Floyd                                                    #
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
# File: Modified: 12/27/02 by Big R                                           #
# Patching Routines: 02/18/03 by Floyd                                        #
############################################################################### 
############################################################################### 

$config_dir='/hsphere/local/home/destiny/chilsoft.com/cgi-bin/conf';

&loadConfig("$config_dir/config.dat");
&exportConfig(\%waconf);

#################################################
sub loadConfig {
#################################################

 my $conf_file="$config_dir/config.dat";
 open INCFG,"<$conf_file" or die ("Could not open $conf_file\n");
 %waconf=();
 my $next='';
 my $key='';
 my $val='';
 while ($next=<INCFG>)
 {
  chomp $next;
  ($key,$val)=split(/\|/,$next);
  $waconf{$key}=$val;
  }
 close INCFG;
 }
 
#################
sub exportConfig {
#################

 $cref=shift;
################## 
# General Settings 
##################
 $pagename = $$cref{'page_name'}; 
 $pageurl = $$cref{'page_url'};
 $pagetitle = $$cref{'page_title'};
 
 $cgi=$$cref{'cgi'}; 

 $cookieusername = $$cref{'cookieusername'};
 $cookiepassword = $$cref{'cookiepassword'};
 $cookieusertheme = $$cref{'cookieusertheme'};
 $cookieuserlang = $$cref{'cookieuserlang'};
 
 $mailtype = $$cref{'mailtype'};
 $mailprogram = $$cref{'mailprog'};
 $smtp_server =  $$cref{'smtp_server'};
 
 $basedir   = $$cref{'base_dir'};
 $baseurl   = $$cref{'base_url'};
 $scriptdir = $$cref{'script_dir'};
 $scripturl = $$cref{'script_url'};
 $sourcedir = $$cref{'lib_dir'};
 $datadir   = $$cref{'data_dir'};
 $memberdir = $$cref{'member_dir'};
 
 $imagesdir = $$cref{'images_dir'};
 $themesdir = $$cref{'themes_dir'};
 $imagesurl = $$cref{'images_url'};
 $themesurl = $$cref{'themes_url'};
 
 $language = $$cref{'default_lang'};
 $langdir = $$cref{'lang_dir'};
 $lang = $$cref{'backup_lang'};
 
######################## 
# Contact Settings 
########################  
 $compname = $$cref{'compname'};
 $compadd = $$cref{'compadd'};
 $compcity = $$cref{'compcity'};
 $compstate = $$cref{'compstate'};
 $compzip = $$cref{'compzip'};
 $compphone = $$cref{'compphone'};
 $compfax = $$cref{'compfax'};
 $compemail = $$cref{'compemail'};
 $webmaster_email = $$cref{'webmaster_email'};
 
######################## 
# IM Settings 
########################  
 $bmheadercolor = $$cref{'bmheadercolor'}; 
 $bmbgcolor = $$cref{'bmbgcolor'}; 
 $welcome_im = $$cref{'welcome_im'};
 $newuser_im = $$cref{'newuser_im'};
 $article_im = $$cref{'article_im'};
 
######################## 
# Information Settings 
########################  
 $image1 = $$cref{'image1'}; 
 $link1 = $$cref{'link1'};
 $image2 = $$cref{'image2'};
 $link2 = $$cref{'link2'};
 $image3 = $$cref{'image3'};
 $link3 = $$cref{'link3'};
 
######################## 
# News Specific Settings 
######################## 
 $topicsdir = $$cref{'topic_dir'};
 $maxnews = $$cref{'maxnews'};
 $maxtopics = $$cref{'maxtopics'};
 $enable_userarticles = $$cref{'enable_userarticles'};
 $allow_html = $$cref{'allow_html'};
 $enable_topicguestposting = $$cref{'enable_topicguestposting'};
 $enable_autopublish = $$cref{'enable_autopublish'};
 $article_imrecip = $$cref{'article_imrecip'};
 $topicimgupld = $$cref{'topicimgupld'};
 
########################## 
# Forums Specific Settings 
########################## 
 $boardsdir = $$cref{'forum_dir'};
 $messagedir = $$cref{'message_dir'};
 $enable_guestposting = $$cref{'enable_guestposting'};
 $enable_notification = $$cref{'enable_notification'};
 $maxdisplay = $$cref{'maxdisplay'};
 $maxmessagedisplay = $$cref{'maxmessagedisplay'};
 $insert_original = $$cref{'insert_original'};
 $max_log_days_old = $$cref{'max_log_days_old'};
 $forumimgupld = $$cref{'forumimgupld'};
 
#########################
# Smilies/UBBC Settings
######################### 
 $enable_ubbc = $$cref{'enable_ubbc'};
 $enable_smile = $$cref{'enable_smile'};
 $imageicons = $$cref{'imageicons'}; 

######################### 
# Stats Specific Settings 
######################### 
 $logdir = $$cref{'log_dir'};
 $ip_time = $$cref{'ip_time'};
 $top_browsers = $$cref{'top_browsers'};
 $top_os = $$cref{'top_os'};
 
######################### 
# Links Specific Settings 
######################### 
 $linksdir = $$cref{'links_dir'};
 $maxlinks = $$cref{'maxlinks'};
 $adminonlyl = $$cref{'adminonlyl'};
 $showlatestlinks = $$cref{'showlatestlinks'};
 
######################### 
# Downloads Specific Settings 
######################### 
 $downloadsdir = $$cref{'download_dir'};
 $maxdownloads = $$cref{'maxdownloads'};
 $antileech = $$cref{'antileech'};
 $adminonlyd = $$cref{'adminonlyd'};
 $showlatestdownloads = $$cref{'showlatestdownloads'};
 
############################
# Admin Assistant Settings
############################
 $dispmost = $$cref{'dispmost'};
 $dispstat = $$cref{'dispstat'};
 $infoblockmod = $$cref{'infoblockmod'};
 $dispfrad = $$cref{'dispfrad'};
 $showcon = $$cref{'showcon'};
 $showcon2 = $$cref{'showcon2'};
 $hidemail = $$cref{'hidemail'};
 $letmemdel = $$cref{'letmemdel'};
 $letmemlng = $$cref{'letmemlng'};
 $letmemthm = $$cref{'letmemthm'};
 $searchmod = $$cref{'searchmod'};
 $hidememlist = $$cref{'hidememlist'};
 $modulecal = $$cref{'modulecal'};
 $modulenl = $$cref{'modulenl'};
 $pollmod = $$cref{'pollmod'};
 $multiplevoting = $$cref{'multiplevoting'};
 $modulenlmem = $$cref{'modulenlmem'};
 $botkiller = $$cref{'botkiller'};
 $signupmethod = $$cref{'signupmethod'};
 $timezone = $$cref{'timezone'};
 $defaulttheme = $$cref{'defaulttheme'};
 $check_date = $$cref{'check_date'};

################
# Admin Access
################
 $editwelc = $$cref{'editwelc'}; 
 $editabout = $$cref{'editabout'}; 
 $editim = $$cref{'editim'}; 
 $editbanner = $$cref{'editbanner'}; 
 $editfaq = $$cref{'editfaq'}; 
 $editdown = $$cref{'editdown'}; 
 $editlink = $$cref{'editlink'}; 
 $modadmin = $$cref{'modadmin'}; 
 $editcats = $$cref{'editcats'}; 
 $editboards = $$cref{'editboards'}; 
 $editcensor = $$cref{'editcensor'}; 
 $editpoll = $$cref{'editpoll'}; 
 $pubnews = $$cref{'pubnews'}; 
 $editnews = $$cref{'editnews'}; 
 $edittops = $$cref{'edittops'}; 
 $editlblk = $$cref{'editlblk'}; 
 $editrblk = $$cref{'editrblk'}; 
 $editnl = $$cref{'editnl'}; 
 $editip = $$cref{'editip'}; 

################ 
# Other Settings 
################ 
 $timeoffset = $$cref{'timeoffset'};
 $memberpic_height = $$cref{'memberpic_height'};
 $memberpic_width = $$cref{'memberpic_width'};
 $maxuploadsize = $$cref{'maxuploadsize'};
 $uploaddir = $$cref{'upload_dir'};
 $uploadurl = $$cref{'upload_url'};
 $use_flock = $$cref{'use_flock'};
 $LOCK_EX = $$cref{'LOCK_EX'};
 $LOCK_UN = $$cref{'LOCK_UN'};
 $IIS =  $$cref{'IIS'};
 $server_os =  $$cref{'server_os'};
 
################
# Module Paths
################
 $poll_dir = $$cref{'poll_dir'};
 $newsletter_dir =  $$cref{'newsletter_dir'};

################
# Mods Paths
################
 $mods_dir = $$cref{'mods_dir'};
 $mods_url =  $$cref{'mods_url'};
 
################
# Misc Paths
################
 $user_lib = $$cref{'user_lib'};
 $upgrade_lib =  $$cref{'upgrade_lib'};
 
################
# WebAPP Settings
################
 $scriptname = $$cref{'scriptname'};
 $scriptver =  $$cref{'scriptver'};
 $updatever = $$cref{'updatever'};
 $scriptbuildnumber = $$cref{'scriptbuildnumber'};
 $web_dir = $$cref{'web_dir'};

}

1; #return true
	