## easymod compliant
############################################################## 
## MOD Title:   Multi BBCode update to 1.2.1
## MOD Author:  Nuttzy99 < nospam@blizzhackers.com > (n/a) http://www.blizzhackers.com
##
## MOD Description:  upgrades a previous installed Multi BBCode MOD
##    from version 1.0.1 to 1.2.1
## MOD Version: 1.2.1
## 
## Installation Level: Easy
## Installation Time:  1 Minutes 
## Files To Edit:      templates/subSilver/posting_body.tpl
## Included Files:     n/a
############################################################## 
## For Security Purposes, Please Check: http://www.phpbb.com/mods/ for the 
## latest version of this MOD. Downloading this MOD from other sites could cause malicious code 
## to enter into your phpBB Forum. As such, phpBB will not offer support for MOD's not offered 
## in our MOD-Database, located at: http://www.phpbb.com/mods/
############################################################## 
## 
## Author Notes:
##     + DO NOT INSTALL IF: you have already installed Multi BBCode MOD v1.2.0
##     + Works with phpBB 2.0.2 thru 2.0.6
##     + installable with EasyMOD
##
############################################################## 
##
## MOD History:
##    2003-09-25 - Version 1.2.1
##         + improved MOD Template compliance
##
##    2003-08-15 - Version 1.2.0
##         + initial release
##         + keeping version number compatiable with main MOD version
##
##############################################################
## Before Adding This MOD To Your Forum, You Should Back Up All Files Related To This MOD 
##############################################################


# 
#-----[ OPEN ]------------------------------------------ 
# 
templates/subSilver/posting_body.tpl


#
#-----[ FIND ]---------------------------------
#
#   NOTE - the complete line to find is:
# function helpline(help) {
#
function helpline(

# 
#-----[ AFTER, ADD ]------------------------------------------ 
#
// MULTI BBCODE-start
	// put an "n" in front of the value to make it an acceptable variable name
	if ((help == '1') || (help == '2') || (help == '3') || (help == '4') || (help == '5') || (help == '6') || (help == '7') || (help == '8') || (help == '9') || (help == '0'))
	{
		help = 'n' + help ;
	}
// MULTI BBCODE-end

# 
#-----[ SAVE/CLOSE ALL FILES ]------------------------------------------ 
# 
# EoM 
