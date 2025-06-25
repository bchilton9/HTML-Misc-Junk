## easymod compliant
############################################################## 
## MOD Title:   Multi BBCode update 1.2.1 to 1.4.0
## MOD Author:  Nuttzy99 < nospam@blizzhackers.com > (n/a) http://www.blizzhackers.com
## MOD Author, Secondary: wGEric < eric@best-dev.com > (Eric Faerber) http://mods.best-dev.com/
##
## MOD Description:  upgrades a previous installed Multi BBCode MOD
##    from version 1.2.1 to 1.4.0c
## MOD Version: 1.4.0c
## 
## Installation Level: Easy
## Installation Time:  1 Minutes 
## Files To Edit:      posting.php
##		       templates/subSilver/posting_body.tpl
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
##	Version 1.4.0 makes it so MOD Authors don't have to set a hotkey for their BBCodes.
##
##	I have added instructions to the MOD that tell MOD Authors what to do in the language files
##	This isn't required but I heavily recommend that you do it anyways just in case the MOD Authors
##	use something in what I have added as their FIND.
##
############################################################## 
##
## MOD History:
##
##    2004-09-26 - Version 1.4.0
##	   + Sets hot key automatically
##	   + Adds it to Private Messages (version b)
##	   + Fixes a help line bug (version c)
##
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
#-----[ OPEN ]---------------------------------
# 
posting.php

# 
#-----[ FIND ]---------------------------------
#
// MULTI BBCODE-begin
//NOTE: the first element of each array must be ''   Add new elements AFTER the ''
$EMBB_keys = array('') ;
$EMBB_widths = array('') ;
$EMBB_values = array('') ;

for ($i=1; $i<count($EMBB_values); $i++)
{
	// load BBcode MODs info
	$val = ($i*2)+16 ;
	$template->assign_block_vars('MultiBB', array(
		'KEY' => $EMBB_keys[$i],
		'NAME' => "addbbcode$val",
		'WIDTH' => $EMBB_widths[$i],
		'VALUE' => $EMBB_values[$i],
		'STYLE' => "bbstyle($val)")
	);
}
// MULTI BBCODE-end
# 
#-----[ REPLACE WITH ]------------------------------------------ 
#
Multi_BBCode();
# 
#-----[ OPEN ]---------------------------------
# 
privmsg.php


# 
#-----[ FIND ]---------------------------------
#
	generate_smilies('inline', PAGE_PRIVMSGS);


# 
#-----[ AFTER, ADD ]---------------------------------
#
Multi_BBCode();

# 
#-----[ OPEN ]---------------------------------
#
includes/bbcode.php
# 
#-----[ FIND ]---------------------------------
#
$bbcode_tpl = null;
# 
#-----[ AFTER, ADD ]---------------------------------
#

// MULTI BBCODE-begin
function Multi_BBCode()
{
	global $template, $lang;

	// DO NOT CHANGE THIS ARRAY
	$hotkeys = array('', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'r', 't', 'v', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0');

	//NOTE: the first element of each array must be ''   Add new elements AFTER the ''
	$EMBB_widths = array('') ;
	$EMBB_values = array('') ;
	for ($i=1; $i<count($EMBB_values); $i++)
	{
		// load BBcode MODs info
		$val = ($i*2)+16 ;
		$help_lang = ( !empty($lang['bbcode_help'][(strtolower($EMBB_values[$i]))]) ) ? $lang['bbcode_help'][(strtolower($EMBB_values[$i]))] : $lang['bbcode_help'][$EMBB_values[$i]];
		$template->assign_block_vars('MultiBB', array(
			'KEY' => $hotkeys[$i],
			'NAME' => "addbbcode$val",
			'HELP' => sprintf($help_lang, $hotkeys[$i]),
			'WIDTH' => $EMBB_widths[$i],
			'VALUE' => $EMBB_values[$i],
			'STYLE' => "bbstyle($val)")
		);
	}
}
// MULTI BBCODE-end

# 
#-----[ OPEN ]---------------------------------
# 
templates/subSilver/posting_body.tpl

#
#-----[ FIND ]---------------------------------
#
f_help = "{L_BBCODE_F_HELP}";

# 
#-----[ AFTER, ADD ]---------------------------------
#
<!-- BEGIN MultiBB -->
{MultiBB.VALUE}_help = "{MultiBB.HELP}";
<!-- END MultiBB -->
#
#-----[ FIND ]---------------------------------
#
// MULTI BBCODE-start
	// put an "n" in front of the value to make it an acceptable variable name
	if ((help == '1') || (help == '2') || (help == '3') || (help == '4') || (help == '5') || (help == '6') || (help == '7') || (help == '8') || (help == '9') || (help == '0'))
	{
		help = 'n' + help ;
	}
// MULTI BBCODE-end
# 
#-----[ REPLACE WITH ]------------------------------------------ 
#
// DELETED
#
#-----[ FIND ]---------------------------------
#
			<!-- BEGIN MultiBB -->
			<td><span class="genmed">
			  <input type="button" class="button" accesskey="{MultiBB.KEY}" name="{MultiBB.NAME}" value="{MultiBB.VALUE}" style="width: {MultiBB.WIDTH}px" onClick="{MultiBB.STYLE}" onMouseOver="helpline('{MultiBB.KEY}')" />
			  </span></td>
			<!-- END MultiBB -->
# 
#-----[ REPLACE WITH ]------------------------------------------ 
#
			<!-- BEGIN MultiBB -->
			<td><span class="genmed">
			  <input type="button" class="button" accesskey="{MultiBB.KEY}" name="{MultiBB.NAME}" value="{MultiBB.VALUE}" style="width: {MultiBB.WIDTH}px" onClick="{MultiBB.STYLE}" onMouseOver="helpline('{MultiBB.VALUE}')" />
			  </span></td>
			<!-- END MultiBB -->
# 
#-----[ OPEN ]---------------------------------
#
language/lang_english/lang_main.php

# 
#-----[ FIND ]---------------------------------
#
#  NOTE - the full line to look for is:
#	$lang['bbcode_f_help'] = 'Font size: [size=x-small]small text[/size]';
#
$lang['bbcode_f_help']

# 
#-----[ AFTER, ADD ]---------------------------------
#

//
// bbcode help format goes like this
// $lang['bbcode_help']['value'] = 'BBCode Name: Info (Alt+%s)';
//
// value is what you put in $EMBB_values in posting.php
// %s gets replaced with the automatic hotkey that the bbcode gets assigned
//
$lang['bbcode_help']['value'] = 'BBCode Name: Info (Alt+%s)';

# 
#-----[ SAVE/CLOSE ALL FILES ]------------------------------------------ 
# 
# EoM 