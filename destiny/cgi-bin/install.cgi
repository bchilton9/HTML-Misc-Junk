#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# install.cgi	                                                            #
# v0.9.9 - Requin                              						#
# Copyright (C) 2002 by WebAPP (webapp@attbi.com)                             #
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
# Last modified: 03/26/03                                                     #
###############################################################################
###############################################################################
use CGI::Carp qw(fatalsToBrowser);

$scriptname = "WebAPP Installer";
$installscriptname = "WebAPP";

# Version Specific Settings ####################################################
$installversion = "0.9.9";
$installupdatename = "Requin";
$installbuildnumber = "020";
################################################################################

print "Content-type: text/html\n\n";

&getcgi();

if ($input{'action'} eq "config2") {
&setup_config2;
}

if ($input{'action'} eq "config3") {
&setup_config3;
}

&getinfo();
&setup_config();

############
sub getcgi {
############
	read(STDIN, $input, $ENV{'CONTENT_LENGTH'});
	@pairs = split(/&/, $input);
	foreach $pair(@pairs) {

	        ($name, $value) = split(/=/, $pair);
	        $name =~ tr/+/ /;
	        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $value =~ tr/+/ /;
	        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $input{$name} = $value;
	}
	@vars = split(/&/, $ENV{QUERY_STRING});
	foreach $var(@vars) {
	        ($v,$i) = split(/=/, $var);
	        $v =~ tr/+/ /;
	        $v =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $i =~ tr/+/ /;
	        $i =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $i =~ s/<!--(.|\n)*-->//g;
	        $input{$v} = $i;
	}
}

################
sub chmod_file {
################
  $chmodfailed = "0";
    my ($destination, $permissions) = @_;
    unless(chmod(oct($permissions), $destination))
      {$chmodfailed = "1";
	print qq~<font color="red" size="4"><b>>>> Cannot set permissions on $destination file!</b></font><br>~;
      }
  }

##################
sub setup_config {
##################

print qq~<html>
<head>
<title>WebAPP $installversion - Automated Perl Portal Installer</title>
</head>
<body>
<center><h2><font color="#000070">WebAPP v$installversion ($installupdatename) Build:$installbuildnumber<br>Automated Perl Portal Installer</font></h2></center>
<p>
<h3><center>Welcome to the WebAPP v$installversion Installer. This program will ease the Perl installation process and config.pl setup.<br>On most linux servers this information should be <i>almost</i> correct.</center></h3><hr>
<br>
<center><h2><font color=red><b>If you do not know your correct path information, please check with your web hosting provider first!</b></h2></font></center>
<hr>
<center><h3>The correct paths should have been generated <b>automatically</b> for you, but please check to see if they are correct!</h3>
<h3>If your images and themes directories are not found at...<br><font color="green">http://$hosturl/images/</font><br>...these will have to be changed!</h3></center>
<hr>
<b><center><h3><u>Site Setup</u></h3></center></b>
<form action="install.cgi" method="POST">
<input type="hidden" name="action" value="config2">
<form action="$admin&amp;op=siteconfig2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td colspan="2"><b><u>General Settings</u></b></td>
</tr>
<tr>
<td>Pagename</td>
<td><input type="text" name="pagename" value="$hosturl" size="30"></td>
</tr>
<tr>
<td>Pageurl (<b>Change the cgi-bin if you have a different directory</b>)</td>
<td><input type="text" name="pageurl" value="http://$hosturl/cgi-bin" size="80"></td>
</tr>
<tr>
<td>Pagetitle</td>
<td><input type="text" name="pagetitle" value="$hosturl" size="30"></td>
</tr>
<tr>
<td>Script Filename</td>
<td><input type="text" name="cgi" value="index.cgi" size="30"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Cookies</u></b>&nbsp;&nbsp;&nbsp;&nbsp;<b>(<u>Note:</u></b> If your Pagename is <b>My Site</b> you should name your Cookies - mysiteuid, mysitepwd, mysitethm & mysitelng.<b>)</b></td>
</tr>
<tr>
<td>Username Cookie</td>
<td><input type="text" name="cookieusername" value="mysiteuid" size="30"></td>
</tr>
<tr>
<td>Password Cookie</td>
<td><input type="text" name="cookiepassword" value="mysitepwd" size="30"></td>
</tr>
<tr>
<td>Theme Cookie</td>
<td><input type="text" name="cookieusertheme" value="mysitethm" size="30"></td>
</tr>
<tr>
<td>Language Cookie</td>
<td><input type="text" name="cookieuserlang" value="mysitelng" size="30"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>E-Mail Settings</u></b></td>
</tr>
<tr>
<td>Mailertype</td>
<td><select name="mailtype">
<option selected value="0">sendmail</option>
<option value="1">SMTP</option>
</select></td>
</tr>
<tr>
<td>Path to mailprogram</td>
<td><input type="text" name="mailprogram" value="/usr/sbin/sendmail -t" size="80"></td>
</tr>
<tr>
<td>SMTP-Server</td>
<td><input type="text" name="smtp_server" value="smtp.$smtpfun" size="80"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Paths</u></b></td>
</tr>
<tr>
<td>Path to website rootdirectory</td>
<td><input type="text" name="basedir" value="$rootpath" size="80"></td>
</tr>
<tr>
<td>Main URL to website</td>
<td><input type="text" name="baseurl" value="http://$hosturl" size="80"></td>
</tr>
<tr>
<td>Main script URL to website (<b>Change the cgi-bin if you have a different directory</b>)</td>
<td><input type="text" name="scripturl" value="http://$hosturl/cgi-bin" size="80"></td>
</tr>
<tr>
<td>Path to script maindirectory</td>
<td><input type="text" name="scriptdir" value="$scriptpath" size="80"></td>
</tr>
<tr>
<td>Path to script sources</td>
<td><input type="text" name="sourcedir" value="$scriptpath/cgi-lib" size="80"></td>
</tr>
<tr>
<td>Path to data directory</td>
<td><input type="text" name="datadir" value="$scriptpath/db" size="80"></td>
</tr>
<tr>
<td>Path to members directory</td>
<td><input type="text" name="memberdir" value="$scriptpath/db/members" size="80"></td>
</tr>
<tr>
<td>Path to images directory</td>
<td><input type="text" name="imagesdir" value="$rootpath/images" size="80"></td>
</tr>
<tr>
<td>Path to themes directory</td>
<td><input type="text" name="themesdir" value="$rootpath/themes" size="80"></td>
</tr>
<tr>
<td>Path/URL to images directory</td>
<td><input type="text" name="imagesurl" value="http://$hosturl/images" size="80"></td>
</tr>
<tr>
<td>Path/URL to themes directory</td>
<td><input type="text" name="themesurl" value="http://$hosturl/themes" size="80"></td>
</tr>
<tr>
<td>Path to Uploaded Images Directory</td>
<td><input type="text" name="uploaddir" value="$rootpath/images/uploads" size="80"></td>
</tr>
<tr>
<td>URL to Uploaded Images Directory</td>
<td><input type="text" name="uploadurl" value="http://$hosturl/images/uploads" size="80"></td>
</tr>
<tr>
<td>Max Uploaded Image Size (KB)</td>
<td><input type="text" name="maxuploadsize" value="150" size="5"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Language Support</u></b></td>
</tr>
<tr>
<td>Language Directory</td>
<td><input type="text" name="lang_dir" value="$scriptpath/lang" size="80"><BR></td>
</tr>
<tr>
<td>Site Language</td>
<td><input type="text" name="backup_lang" value="$scriptpath/lang/english.lng" size="80"><BR></td>
</tr>
<tr>
<td>Default Language</td>
<td><input type="text" name="default_lang" value="english.lng" size="30"><BR></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Contact Info</u></b></td>
</tr>
<tr>
<td>Company Name</td>
<td><input type="text" name="compname" value="$hosturl" size="80"></td>
</tr>
<tr>
<td>Company Address</td>
<td><input type="text" name="compadd" value="5555 Lane" size="80"></td>
</tr>
<tr>
<td>Company City</td>
<td><input type="text" name="compcity" value="Some Town" size="80"></td>
</tr>
<tr>
<td>Company State</td>
<td><input type="text" name="compstate" value="State" size="80"></td>
</tr>
<tr>
<td>Company Zip</td>
<td><input type="text" name="compzip" value="Zip" size="80"></td>
</tr>
<tr>
<td>Company Phone</td>
<td><input type="text" name="compphone" value="Phone" size="80"></td>
</tr>
<tr>
<td>Company Fax</td>
<td><input type="text" name="compfax" value="Fax" size="80"></td>
</tr>
<tr>
<td>Company E-Mail</td>
<td><input type="text" name="compemail" value="Company E-Mail" size="80"></td>
</tr>
<tr>
<td>Webmaster E-Mail</td>
<td><input type="text" name="webmaster_email" value="Webmaster E-Mail" size="80"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Articles</u></b></td>
</tr>
<tr>
<td>Path to topics directory</td>
<td><input type="text" name="topicsdir" value="$scriptpath/db/topics" size="80"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Forums</u></b></td>
</tr>
<tr>
<td>Path to forums directory</td>
<td><input type="text" name="boardsdir" value="$scriptpath/db/forum" size="80"></td>
</tr>
<tr>
<td>Path to messages directory</td>
<td><input type="text" name="messagedir" value="$scriptpath/db/forum/messages" size="80"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Statistics</u></b></td>
</tr>
<tr>
<td>Path to stats directory</td>
<td><input type="text" name="logdir" value="$scriptpath/db/stats" size="80"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Links</u></b></td>
</tr>
<tr>
<td>Path to links directory</td>
<td><input type="text" name="linksdir" value="$scriptpath/db/links" size="80"></td>
</tr>
<tr>
<td colspan="2"><hr><b><u>Downloads</u></b></td>
</tr>
<tr>
<td>Path to downloads directory</td>
<td><input type="text" name="downloadsdir" value="$scriptpath/db/downloads" size="80"></td>
</tr>
<tr>
<tr>
<td colspan="2"><hr><b><u>Other Settings</u></b></td>
</tr>
<tr>
<td>Time Difference</td>
<td><select name="timeoffset">~;

			open (ZONES,"./db/timezones.dat") || error("$err{'016'} ./db/timezones.dat"); 
      @timezones=<ZONES>; 
      close (ZONES);
			
			foreach $zone (@timezones) {
						$zone =~ s/[\n\r]//g;
						@zitem = split(/\|/, $zone);
						
						if ($zitem[1] ne "") {
							 if ($zitem[0] eq 0) {print qq~<option value="$zitem[0]" selected>$zitem[1]</option>~;} else {print qq~<option value="$zitem[0]">$zitem[1]</option>~;}
						}
			}
			
print qq~</select></td>
</tr>
<tr>
<td>Time Zone</td>
<td><select name="timezone">
~;

			open (ZONES,"./db/timezones.dat") || error("$err{'016'} ./db/timezones.dat"); 
      @timezones=<ZONES>; 
      close (ZONES);
			
			foreach $zone (@timezones) {
						$zone =~ s/[\n\r]//g;
						@zitem = split(/\|/, $zone);
						
						if ($zitem[0] eq 0) {print qq~<option value="$zitem[0]" selected>$zitem[2] $zitem[3]: $zitem[5]</option>~;} else {print qq~<option value="$zitem[0]">$zitem[2] $zitem[3]: $zitem[5]</option>~;}
			}
			
print qq~</select>
</td>
</tr>
<tr>
<td>Date Format</td>
<td><select name="check_date">
<option selected value="american">American (mm/dd/yy)</option>
<option value="european">European (dd/mm/yy)</option>
</select>
</td>
</tr>
<tr>
<td>File Locking</td>
<td><select name="use_flock">
<option selected value="1">On</option>
<option value="0">Off</option>
</select></td>
</tr>
<tr>
<td>LOCK_EX</td>
<td><input type="text" maxlength="2" name="LOCK_EX" value="2" size="1"></td>
</tr>
<tr>
<td>LOCK_UN</td>
<td><input type="text" maxlength="2" name="LOCK_UN" value="8" size="1"></td>
</tr>
<tr>
<td>IIS</td>
<td><select name="IIS">
<option selected value="0">Auto</option>
<option value="1">IIS</option>
<option value="2">Apache</option>
</select></td>
</tr>
<tr>
<td>Server OS</td>
<td><select name="server_os">
<option selected value="linux">Linux</option>
<option value="windows">Windows</option>
</select></td>
</tr>
<tr>
<td colspan="2"><hr></td>
</tr>
<tr>
<td align="center" colspan="2"><input type="submit" value="Save"></td>
</tr>
</table>
</form>
</body>
</html>
~;
	
	exit;
}

###################
sub setup_config2 {
###################

if ($input{'timeoffset'} eq "") {$input{'timeoffset'} = "0";}
if ($input{'timezone'} eq "") {$input{'timezone'} = "0";}

%conf=();
################## 
# General Settings 
##################
$conf{'page_name'}=$input{'pagename'};
$conf{'page_url'}=$input{'pageurl'};
$conf{'page_title'}=$input{'pagetitle'};
$conf{'cgi'}=$input{'cgi'};
$conf{'cookieusername'}=$input{'cookieusername'};
$conf{'cookiepassword'}=$input{'cookiepassword'};
$conf{'cookieusertheme'}=$input{'cookieusertheme'};
$conf{'cookieuserlang'}=$input{'cookieuserlang'};
$conf{'mailtype'}=$input{'mailtype'};
$conf{'mailprog'}=$input{'mailprogram'};
$conf{'smtp_server'}=$input{'smtp_server'};
$conf{'base_dir'}=$input{'basedir'};
$conf{'base_url'}=$input{'baseurl'};
$conf{'script_url'}=$input{'scripturl'};
$conf{'script_dir'}=$input{'scriptdir'};
$conf{'lib_dir'}=$input{'sourcedir'};
$conf{'data_dir'}=$input{'datadir'};
$conf{'member_dir'}=$input{'memberdir'};
$conf{'images_dir'}=$input{'imagesdir'};
$conf{'themes_dir'}=$input{'themesdir'};
$conf{'images_url'}=$input{'imagesurl'};
$conf{'themes_url'}=$input{'themesurl'};
$conf{'lang_dir'}=$input{'lang_dir'};
$conf{'default_lang'}=$input{'default_lang'};
$conf{'backup_lang'}=$input{'backup_lang'};
######################## 
# Contact Settings 
########################
$conf{'compname'}=$input{'compname'};
$conf{'compadd'}=$input{'compadd'};
$conf{'compcity'}=$input{'compcity'};
$conf{'compstate'}=$input{'compstate'};
$conf{'compzip'}=$input{'compzip'};
$conf{'compphone'}=$input{'compphone'};
$conf{'compfax'}=$input{'compfax'};
$conf{'compemail'}=$input{'compemail'};
$conf{'webmaster_email'}=$input{'webmaster_email'};
######################## 
# IM Settings 
########################
$conf{'bmheadercolor'}="#000070";
$conf{'bmbgcolor'}="#FFFFFF";
$conf{'welcome_im'}="1";
$conf{'newuser_im'}="1";
$conf{'article_im'}="1";
######################## 
# Information Settings 
########################
$conf{'image1'}="$input{'imagesurl'}/pb_perl.gif";
$conf{'link1'}="http://www.perl.com/";
$conf{'image2'}="$input{'imagesurl'}/pb_gimp.gif";
$conf{'link2'}="http://www.gimp.org/";
$conf{'image3'}="$input{'imagesurl'}/pb_webapp.gif";
$conf{'link3'}="http://www.web-app.org/";
######################## 
# News Specific Settings 
########################
$conf{'topic_dir'}=$input{'topicsdir'};
$conf{'maxnews'}="5";
$conf{'maxtopics'}="25";
$conf{'enable_userarticles'}="1";
$conf{'allow_html'}="1"; 
$conf{'enable_topicguestposting'}="1";
$conf{'enable_autopublish'}="1";
$conf{'article_imrecip'}="admin";
$conf{'topicimgupld'}="1";
########################## 
# Forums Specific Settings 
##########################
$conf{'forum_dir'}=$input{'boardsdir'};
$conf{'message_dir'}=$input{'messagedir'};
$conf{'enable_guestposting'}="1";
$conf{'enable_notification'}="1";
$conf{'maxdisplay'}="25";
$conf{'maxmessagedisplay'}="15";
$conf{'insert_original'}="1";
$conf{'max_log_days_old'}="21";
$conf{'forumimgupld'}="1";
#########################
# Smilies/UBBC Settings
#########################
$conf{'enable_ubbc'}="1";
$conf{'enable_smile'}="1";
$conf{'imageicons'}="0";
######################### 
# Stats Specific Settings 
#########################
$conf{'log_dir'}=$input{'logdir'};
$conf{'ip_time'}="5";
$conf{'top_browsers'}="1";
$conf{'top_os'}="1";
######################### 
# Links Specific Settings 
#########################
$conf{'links_dir'}=$input{'linksdir'};
$conf{'maxlinks'}="30";
$conf{'adminonlyl'}="1";
$conf{'showlatestlinks'}="1";
######################### 
# Downloads Specific Settings 
#########################
$conf{'download_dir'}=$input{'downloadsdir'};
$conf{'maxdownloads'}="30";
$conf{'antileech'}="1";
$conf{'adminonlyd'}="1";
$conf{'showlatestdownloads'}="1";
############################
# Admin Assistant Settings
############################
$conf{'dispmost'}="1";
$conf{'dispstat'}="0";
$conf{'infoblockmod'}="1";
$conf{'dispfrad'}="1";
$conf{'showcon'}="1";
$conf{'showcon2'}="0";
$conf{'hidemail'}="1";
$conf{'letmemdel'}="0";
$conf{'letmemlng'}="0";
$conf{'letmemthm'}="0";
$conf{'searchmod'}="1";
$conf{'hidememlist'}="0";
$conf{'modulecal'}="0";
$conf{'modulenl'}="1";
$conf{'pollmod'}="1";
$conf{'multiplevoting'}="1";
$conf{'modulenlmem'}="0";
$conf{'botkiller'}="0";
$conf{'signupmethod'}="0";
$conf{'timezone'}=$input{'timezone'};
$conf{'defaulttheme'}="standard";
$conf{'check_date'}=$input{'check_date'};
################
# Admin Access
################
$conf{'editwelc'}="0";
$conf{'editabout'}="0";
$conf{'editim'}="0";
$conf{'editbanner'}="0";
$conf{'editfaq'}="0";
$conf{'editdown'}="0";
$conf{'editlink'}="0";
$conf{'modadmin'}="0";
$conf{'editcats'}="1";
$conf{'editboards'}="1";
$conf{'editcensor'}="1";
$conf{'editpoll'}="1";
$conf{'pubnews'}="1";
$conf{'editnews'}="1";
$conf{'edittops'}="0";
$conf{'editlblk'}="0";
$conf{'editrblk'}="0";
$conf{'editnl'}="0";
$conf{'editip'}="1";
################ 
# Other Settings 
################
$conf{'timeoffset'}=$input{'timeoffset'};
$conf{'memberpic_height'}="100";
$conf{'memberpic_width'}="60";
$conf{'maxuploadsize'}=$input{'maxuploadsize'};
$conf{'upload_url'}=$input{'uploadurl'};
$conf{'upload_dir'}=$input{'uploaddir'};
$conf{'use_flock'}=$input{'use_flock'};
$conf{'LOCK_EX'}=$input{'LOCK_EX'};
$conf{'LOCK_UN'}=$input{'LOCK_UN'};
$conf{'IIS'}=$input{'IIS'};
$conf{'server_os'}=$input{'server_os'};
################
# Module Paths
################
$conf{'poll_dir'}="$input{'datadir'}/polls";
$conf{'newsletter_dir'}="$input{'datadir'}/newsletter";
################
# Mods Paths
################
$conf{'mods_dir'}="$input{'scriptdir'}/mods";
$conf{'mods_url'}="$input{'scripturl'}/mods";
################
# Misc Paths
################
$conf{'user_lib'}="$input{'scriptdir'}/user-lib";
$conf{'upgrade_lib'}="$input{'scriptdir'}/upgrade-lib";
################
# WebAPP Settings
################
$conf{'scriptname'}=$installscriptname;
$conf{'scriptver'}=$installversion;
$conf{'updatever'}=$installupdatename;
$conf{'scriptbuildnumber'}=$installbuildnumber;
$conf{'web_dir'}=$input{'basedir'};

# Define the Location of the config.dat File ###################################
$filename="$input{'scriptdir'}/conf/config.dat";
$config_dir = "$input{'scriptdir'}/conf";
$config_script = "$input{'scriptdir'}/config.pl";

# Write the config.dat File ####################################################
open OTF,">$filename" or die ("Could not open $filename!");
foreach $thing (keys %conf)
  { print OTF "$thing|$conf{$thing}\n"; }
close OTF;

# Write config.pl ############################################################

 	open FILE,">$config_script" or die ("Could not open $config_script!"); 
	print FILE qq~############################################################################### 
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

\$config_dir='$config_dir';

&loadConfig("\$config_dir/config.dat");
&exportConfig(\\%waconf);

#################################################
sub loadConfig {
#################################################

 my \$conf_file="\$config_dir/config.dat";
 open INCFG,"<\$conf_file" or die ("Could not open \$conf_file\\n");
 %waconf=();
 my \$next='';
 my \$key='';
 my \$val='';
 while (\$next=<INCFG>)
 {
  chomp \$next;
  (\$key,\$val)=split(/\\|/,\$next);
  \$waconf{\$key}=\$val;
  }
 close INCFG;
 }
 
#################
sub exportConfig {
#################

 \$cref=shift;
################## 
# General Settings 
##################
 \$pagename = \$\$cref{'page_name'}; 
 \$pageurl = \$\$cref{'page_url'};
 \$pagetitle = \$\$cref{'page_title'};
 
 \$cgi=\$\$cref{'cgi'}; 

 \$cookieusername = \$\$cref{'cookieusername'};
 \$cookiepassword = \$\$cref{'cookiepassword'};
 \$cookieusertheme = \$\$cref{'cookieusertheme'};
 \$cookieuserlang = \$\$cref{'cookieuserlang'};
 
 \$mailtype = \$\$cref{'mailtype'};
 \$mailprogram = \$\$cref{'mailprog'};
 \$smtp_server =  \$\$cref{'smtp_server'};
 
 \$basedir   = \$\$cref{'base_dir'};
 \$baseurl   = \$\$cref{'base_url'};
 \$scriptdir = \$\$cref{'script_dir'};
 \$scripturl = \$\$cref{'script_url'};
 \$sourcedir = \$\$cref{'lib_dir'};
 \$datadir   = \$\$cref{'data_dir'};
 \$memberdir = \$\$cref{'member_dir'};
 
 \$imagesdir = \$\$cref{'images_dir'};
 \$themesdir = \$\$cref{'themes_dir'};
 \$imagesurl = \$\$cref{'images_url'};
 \$themesurl = \$\$cref{'themes_url'};
 
 \$language = \$\$cref{'default_lang'};
 \$langdir = \$\$cref{'lang_dir'};
 \$lang = \$\$cref{'backup_lang'};
 
######################## 
# Contact Settings 
########################  
 \$compname = \$\$cref{'compname'};
 \$compadd = \$\$cref{'compadd'};
 \$compcity = \$\$cref{'compcity'};
 \$compstate = \$\$cref{'compstate'};
 \$compzip = \$\$cref{'compzip'};
 \$compphone = \$\$cref{'compphone'};
 \$compfax = \$\$cref{'compfax'};
 \$compemail = \$\$cref{'compemail'};
 \$webmaster_email = \$\$cref{'webmaster_email'};
 
######################## 
# IM Settings 
########################  
 \$bmheadercolor = \$\$cref{'bmheadercolor'}; 
 \$bmbgcolor = \$\$cref{'bmbgcolor'}; 
 \$welcome_im = \$\$cref{'welcome_im'};
 \$newuser_im = \$\$cref{'newuser_im'};
 \$article_im = \$\$cref{'article_im'};
 
######################## 
# Information Settings 
########################  
 \$image1 = \$\$cref{'image1'}; 
 \$link1 = \$\$cref{'link1'};
 \$image2 = \$\$cref{'image2'};
 \$link2 = \$\$cref{'link2'};
 \$image3 = \$\$cref{'image3'};
 \$link3 = \$\$cref{'link3'};
 
######################## 
# News Specific Settings 
######################## 
 \$topicsdir = \$\$cref{'topic_dir'};
 \$maxnews = \$\$cref{'maxnews'};
 \$maxtopics = \$\$cref{'maxtopics'};
 \$enable_userarticles = \$\$cref{'enable_userarticles'};
 \$allow_html = \$\$cref{'allow_html'};
 \$enable_topicguestposting = \$\$cref{'enable_topicguestposting'};
 \$enable_autopublish = \$\$cref{'enable_autopublish'};
 \$article_imrecip = \$\$cref{'article_imrecip'};
 \$topicimgupld = \$\$cref{'topicimgupld'};
 
########################## 
# Forums Specific Settings 
########################## 
 \$boardsdir = \$\$cref{'forum_dir'};
 \$messagedir = \$\$cref{'message_dir'};
 \$enable_guestposting = \$\$cref{'enable_guestposting'};
 \$enable_notification = \$\$cref{'enable_notification'};
 \$maxdisplay = \$\$cref{'maxdisplay'};
 \$maxmessagedisplay = \$\$cref{'maxmessagedisplay'};
 \$insert_original = \$\$cref{'insert_original'};
 \$max_log_days_old = \$\$cref{'max_log_days_old'};
 \$forumimgupld = \$\$cref{'forumimgupld'};
 
#########################
# Smilies/UBBC Settings
######################### 
 \$enable_ubbc = \$\$cref{'enable_ubbc'};
 \$enable_smile = \$\$cref{'enable_smile'};
 \$imageicons = \$\$cref{'imageicons'}; 

######################### 
# Stats Specific Settings 
######################### 
 \$logdir = \$\$cref{'log_dir'};
 \$ip_time = \$\$cref{'ip_time'};
 \$top_browsers = \$\$cref{'top_browsers'};
 \$top_os = \$\$cref{'top_os'};
 
######################### 
# Links Specific Settings 
######################### 
 \$linksdir = \$\$cref{'links_dir'};
 \$maxlinks = \$\$cref{'maxlinks'};
 \$adminonlyl = \$\$cref{'adminonlyl'};
 \$showlatestlinks = \$\$cref{'showlatestlinks'};
 
######################### 
# Downloads Specific Settings 
######################### 
 \$downloadsdir = \$\$cref{'download_dir'};
 \$maxdownloads = \$\$cref{'maxdownloads'};
 \$antileech = \$\$cref{'antileech'};
 \$adminonlyd = \$\$cref{'adminonlyd'};
 \$showlatestdownloads = \$\$cref{'showlatestdownloads'};
 
############################
# Admin Assistant Settings
############################
 \$dispmost = \$\$cref{'dispmost'};
 \$dispstat = \$\$cref{'dispstat'};
 \$infoblockmod = \$\$cref{'infoblockmod'};
 \$dispfrad = \$\$cref{'dispfrad'};
 \$showcon = \$\$cref{'showcon'};
 \$showcon2 = \$\$cref{'showcon2'};
 \$hidemail = \$\$cref{'hidemail'};
 \$letmemdel = \$\$cref{'letmemdel'};
 \$letmemlng = \$\$cref{'letmemlng'};
 \$letmemthm = \$\$cref{'letmemthm'};
 \$searchmod = \$\$cref{'searchmod'};
 \$hidememlist = \$\$cref{'hidememlist'};
 \$modulecal = \$\$cref{'modulecal'};
 \$modulenl = \$\$cref{'modulenl'};
 \$pollmod = \$\$cref{'pollmod'};
 \$multiplevoting = \$\$cref{'multiplevoting'};
 \$modulenlmem = \$\$cref{'modulenlmem'};
 \$botkiller = \$\$cref{'botkiller'};
 \$signupmethod = \$\$cref{'signupmethod'};
 \$timezone = \$\$cref{'timezone'};
 \$defaulttheme = \$\$cref{'defaulttheme'};
 \$check_date = \$\$cref{'check_date'};

################
# Admin Access
################
 \$editwelc = \$\$cref{'editwelc'}; 
 \$editabout = \$\$cref{'editabout'}; 
 \$editim = \$\$cref{'editim'}; 
 \$editbanner = \$\$cref{'editbanner'}; 
 \$editfaq = \$\$cref{'editfaq'}; 
 \$editdown = \$\$cref{'editdown'}; 
 \$editlink = \$\$cref{'editlink'}; 
 \$modadmin = \$\$cref{'modadmin'}; 
 \$editcats = \$\$cref{'editcats'}; 
 \$editboards = \$\$cref{'editboards'}; 
 \$editcensor = \$\$cref{'editcensor'}; 
 \$editpoll = \$\$cref{'editpoll'}; 
 \$pubnews = \$\$cref{'pubnews'}; 
 \$editnews = \$\$cref{'editnews'}; 
 \$edittops = \$\$cref{'edittops'}; 
 \$editlblk = \$\$cref{'editlblk'}; 
 \$editrblk = \$\$cref{'editrblk'}; 
 \$editnl = \$\$cref{'editnl'}; 
 \$editip = \$\$cref{'editip'}; 

################ 
# Other Settings 
################ 
 \$timeoffset = \$\$cref{'timeoffset'};
 \$memberpic_height = \$\$cref{'memberpic_height'};
 \$memberpic_width = \$\$cref{'memberpic_width'};
 \$maxuploadsize = \$\$cref{'maxuploadsize'};
 \$uploaddir = \$\$cref{'upload_dir'};
 \$uploadurl = \$\$cref{'upload_url'};
 \$use_flock = \$\$cref{'use_flock'};
 \$LOCK_EX = \$\$cref{'LOCK_EX'};
 \$LOCK_UN = \$\$cref{'LOCK_UN'};
 \$IIS =  \$\$cref{'IIS'};
 \$server_os =  \$\$cref{'server_os'};
 
################
# Module Paths
################
 \$poll_dir = \$\$cref{'poll_dir'};
 \$newsletter_dir =  \$\$cref{'newsletter_dir'};

################
# Mods Paths
################
 \$mods_dir = \$\$cref{'mods_dir'};
 \$mods_url =  \$\$cref{'mods_url'};
 
################
# Misc Paths
################
 \$user_lib = \$\$cref{'user_lib'};
 \$upgrade_lib =  \$\$cref{'upgrade_lib'};
 
################
# WebAPP Settings
################
 \$scriptname = \$\$cref{'scriptname'};
 \$scriptver =  \$\$cref{'scriptver'};
 \$updatever = \$\$cref{'updatever'};
 \$scriptbuildnumber = \$\$cref{'scriptbuildnumber'};
 \$web_dir = \$\$cref{'web_dir'};

}

1; #return true
	~; 
	close(FILE);

open(DATA, ">./mods/calendar/data/calendar.cfg");

print DATA qq~



	#---------------------------------
	# General Settings
	#---------------------------------
	\$cm_title                    = "Calendar";
	\$cm_requireAdminApproval     =  1;
	\$cm_emailAdminNewEventNotice =  0;
	\$cm_eventAdminEmailAddress   = "$input{'webmaster_email'}";

	#---------------------------------
	# Paths & Files
	#---------------------------------
	\$cm_scriptDir           = "$input{'scriptdir'}/mods/calendar";
	\$cm_dataDir             = "$input{'scriptdir'}/mods/calendar/data";
	\$cm_langDir             = "$input{'scriptdir'}/mods/calendar/lang";
	\$cm_scriptUrl           = "$input{'scripturl'}/mods/calendar/index.cgi";
	\$cm_adminScriptUrl      = "$input{'scripturl'}/mods/calendar/admin/admin.cgi";
	\$cm_eventsFileName      = "calendar.dat";
	\$cm_langFileName        = "english.lng";
	\$cm_detailIconUrl       = "$input{'imagesurl'}/calendar/calendar.gif";

	#---------------------------------
	# Database Settings
	#---------------------------------
	\$cm_delimiter           = "	";
	\$cm_useFileLocking      =  1;

	#---------------------------------
	# Style Elements
	#---------------------------------
	# Sidebar Calendar
	#---------------------------------
	\$cmsb_cellSize          = "20";
	\$cmsb_borderWidth       = "0";
	\$cmsb_borderStyle       = "padding:2";
	\$cmsb_headFontStyle     = "";
	\$cmsb_dayHeadFontStyle  = "";
	\$cmsb_dayHeadCellStyle  = "";
	\$cmsb_selFontStyle      = "";
	\$cmsb_selCellStyle      = "background-color:#336699";
	\$cmsb_stdFontStyle      = "";
	\$cmsb_stdCellStyle      = "";
	\$cmsb_emptyCellStyle    = "";

	#---------------------------------
	# Large Calendar (show detail)
	#---------------------------------
	\$cml_cellSize           = "60";
	\$cml_borderWidth        = "1";
	\$cml_borderStyle        = "padding:2";

	#---------------------------------
	# Small Calendar (hide detail)
	#---------------------------------
	\$cms_cellSize           = "30";
	\$cms_borderWidth        = "1";
	\$cms_borderStyle        = "padding:2";

	#---------------------------------
	# Large & Small Calendars
	#---------------------------------
	\$cm_headFontStyle       = "";
	\$cm_dayHeadFontStyle    = "";
	\$cm_dayHeadCellStyle    = "";
	\$cm_selFontStyle        = "";
	\$cm_selCellStyle        = "background-color:#336699";
	\$cm_stdFontStyle        = "";
	\$cm_stdCellStyle        = "";
	\$cm_todayFontStyle      = "color:#00ff00";
	\$cm_emptyCellStyle      = "";

	1; #return true

~;

close(DATA);


print qq~
<html>
<title>WebAPP v$installversion - Automated Perl Portal Installer</title>
<body>
<form action="install.cgi">
<input type="hidden" name="action" value="config3">
<p><font color="green" size="4"><b>>>> Configuration Updated!!!</font></p>
~;
chmod_file("index.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> index.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/banners/add.cgi", "0755");
chmod_file("./admin/banners/edit.cgi", "0755");
chmod_file("./admin/banners/edit_record.cgi", "0755");
chmod_file("./admin/banners/view.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/banners/*.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/blocks/left/add.cgi", "0755");
chmod_file("./admin/blocks/left/edit.cgi", "0755");
chmod_file("./admin/blocks/left/edit_record.cgi", "0755");
chmod_file("./admin/blocks/left/view.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/blocks/left/*.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/blocks/right/add.cgi", "0755");
chmod_file("./admin/blocks/right/edit.cgi", "0755");
chmod_file("./admin/blocks/right/edit_record.cgi", "0755");
chmod_file("./admin/blocks/right/view.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/blcoks/right/*.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/downloads/downloadadmin.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/downloads/downloadadmin.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/help/add.cgi", "0755");
chmod_file("./admin/help/edit.cgi", "0755");
chmod_file("./admin/help/edit_record.cgi", "0755");
chmod_file("./admin/help/view.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/help/*.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/language/add.cgi", "0755");
chmod_file("./admin/language/edit.cgi", "0755");
chmod_file("./admin/language/edit_record.cgi", "0755");
chmod_file("./admin/language/view.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/language/*.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/links/linksadmin.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/links/linksadmin.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/logs/view.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/logs/*.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/themes/add.cgi", "0755");
chmod_file("./admin/themes/edit.cgi", "0755");
chmod_file("./admin/themes/edit_record.cgi", "0755");
chmod_file("./admin/themes/view.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/themes/*.cgi permissions set</b><br></font> ~;}
chmod_file("./mods/modmanager.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /mods/modmanager.cgi permissions set</b><br></font> ~;}
chmod_file("./mods/calendar/index.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /mods/calendar/index.cgi permissions set</b><br></font> ~;}
chmod_file("./mods/calendar/sidebar.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /mods/calendar/sidebar.cgi permissions set</b><br></font> ~;}
chmod_file("./mods/calendar/admin/admin.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /mods/calendar/admin/admin.cgi permissions set</b><br></font> ~;}
chmod_file("palm.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> palm.cgi permissions set</b><br></font> ~;}
chmod_file("./admin/uploader/upload.cgi", "0755");
if ($chmodfailed ne "1") {
print qq~<font color="green" size="4"><b>>>> /admin/uploader/upload.cgi permissions set</b><br></font> ~;}


print qq~
<hr>
<br>
First, was the installation successful?  <a href="./index.cgi" target="_blank">Click Here to See</a>.<br>
<br>
<b>If everything is correct:<br> <font color="red"> Remove the "install.cgi" file</font> from your /cgi-bin/ folder by clicking the submit button below!</b><br><br>
Make sure that the attributes (chmod) is set correctly:<br>
>>> index.cgi >>> chmod 755<br>
Also, make sure that you have the correct path information from your web hosting provider!<br><br>
<hr>
<br>
<b>click the button below to edit your "index.html" file </b>to reflect your new site.  Install.cgi will automatically be deleted after hitting "submit".<br><br>
<br><center>
<table>
<tr>
<td align="center" colspan="2">~;

$hosturl = $ENV{HTTP_HOST};
$rootpath = $ENV{DOCUMENT_ROOT};

print qq~
<input type="hidden" name="baseurl" value="http://$hosturl">
<input type="hidden" name="basedir" value="$rootpath">
<input type="hidden" name="pagetitle" value="$hosturl">
<input type="hidden" name="pageurl" value="$input{'pageurl'}">
<input type="submit" value="Submit"></td>
</tr>
</table>
</form></center>
</body>
</html>
~;

exit;
}


###################
sub setup_config3 {
###################


	open(FILE, ">$input{'basedir'}/index.html");
	print FILE 
qq~<html><head><title>$input{'pagetitle'}</title>
<META NAME="revisit" CONTENT="12 days">
<meta NAME="Robot" CONTENT="allow">
</head>
<body>
<script language="javascript">window.location="$input{'pageurl'}/index.cgi";</script>
Click <a href="$input{'pageurl'}/index.cgi">here</a> to enter site<br>
</body>
</html>
~;
	close(FILE);

print qq~
<html>
<title>Finished WebAPP Installation!
</title>
<body>
<br>
>>> index.html edited<br><br>
>>> Finished Installation!<br><br>
Follow the link <a href="./index.cgi">here</a> to go to your main page.<br>
</body>
</html>
~;

unlink("./install.cgi");

exit;
}

#############################
sub getinfo {
#############################

$scriptpath = $ENV{SCRIPT_FILENAME};
$hosturl = $ENV{HTTP_HOST};
$rootpath = $ENV{DOCUMENT_ROOT};
$givemail =  $ENV{SERVER_ADMIN};
$smtpfun = $ENV{SERVER_NAME};



for (1 .. 12) {
chop $scriptpath;
}
}

1;



