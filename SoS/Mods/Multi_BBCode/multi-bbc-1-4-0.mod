## easymod compliant
############################################################## 
## MOD Title:    Multiple BBCode MOD
## MOD Author:   Nuttzy99 < nospam@blizzhackers.com > (n/a) http://www.blizzhackers.com
## MOD Author, Secondary: wGEric < eric@best-dev.com > (Eric Faerber) http://mods.best-dev.com/
##
## MOD Description:  Allows you to install BBCode MODs that
##    add quick BBCode buttons in post edits.  Without this
##    MOD, there is no standard way of installing BBCode MODs.
## MOD Version:  1.4.0c
## 
## Installation Level:  EASY
## Installation Time:   2 minutes
## Files To Edit:       posting.php
##                      templates/subSilver/posting_body.tpl
## Included Files:      n/a
############################################################## 
## For Security Purposes, Please Check: http://www.phpbb.com/mods/ for the 
## latest version of this MOD. Downloading this MOD from other sites could cause malicious code 
## to enter into your phpBB Forum. As such, phpBB will not offer support for MOD's not offered 
## in our MOD-Database, located at: http://www.phpbb.com/mods/
############################################################## 
##
## Author Notes:
##     + if Multi BBCode MOD v1.0.1 is already installed, use the update to 1.2.0 MOD
##          and do NOT install this MOD script
##     + Works with phpBB 2.0.2 thru 2.0.10
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
##         + updated for 2.0.6
##         + allows additional hotkeys - Xore did most of the work ;-)
##         + made EasyMOD compatiable
##
##    2003-02-03 - Version 1.0.1
##         + updated for 2.0.4
##         + no code changes required, just updated the header info
##
##    2002-08-31 - Version 1.0.0
##         + initial release
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
#  NOTE - the full line to look for is:
# make_jumpbox('viewforum.'.$phpEx);
#
make_jumpbox(


# 
#-----[ AFTER, ADD ]---------------------------------
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
#  NOTE - the full line to look for is:
#			  <input type="button" class="button" accesskey="w" name="addbbcode16" value="URL" style="text-decoration: underline; width: 40px" onClick="bbstyle(16)" onMouseOver="helpline('w')" />
#			  </span></td>
#
	name="addbbcode16"
	</td>

# 
#-----[ AFTER, ADD ]---------------------------------
#

			<!-- BEGIN MultiBB -->
			<td><span class="genmed">
			  <input type="button" class="button" accesskey="{MultiBB.KEY}" name="{MultiBB.NAME}" value="{MultiBB.VALUE}" style="width: {MultiBB.WIDTH}px" onClick="{MultiBB.STYLE}" onMouseOver="helpline('{MultiBB.VALUE}')" />
			  </span></td>
			<!-- END MultiBB -->
# 
#-----[ FIND ]---------------------------------
#
#  NOTE - the full line to look for is:
#					<select name="addbbcodefontcolor" onChange="bbfontstyle('[color=' + this.form.addbbcodefontcolor.options[this.form.addbbcodefontcolor.selectedIndex].value + ']', '[/color]')" onMouseOver="helpline('s')">
#
	name="addbbcode18"


# 
#-----[ IN-LINE FIND ]---------------------------------
#
name="addbbcode18"


# 
#-----[ IN-LINE REPLACE WITH ]---------------------------------
#
name="addbbcodefontcolor"


# 
#-----[ IN-LINE FIND ]---------------------------------
#
this.form.addbbcode18.options


# 
#-----[ IN-LINE REPLACE WITH ]---------------------------------
#
this.form.addbbcodefontcolor.options


# 
#-----[ IN-LINE FIND ]---------------------------------
#
this.form.addbbcode18.selectedIndex


# 
#-----[ IN-LINE REPLACE WITH ]---------------------------------
#
this.form.addbbcodefontcolor.selectedIndex


# 
#-----[ FIND ]---------------------------------
#
#  NOTE - the full line to look for is:
#					</select> &nbsp;{L_FONT_SIZE}:<select name="addbbcodefontsize" onChange="bbfontstyle('[size=' + this.form.addbbcodefontsize.options[this.form.addbbcodefontsize.selectedIndex].value + ']', '[/size]')" onMouseOver="helpline('f')">
#
	name="addbbcode20"

# 
#-----[ IN-LINE FIND ]---------------------------------
#
name="addbbcode20"


# 
#-----[ IN-LINE REPLACE WITH ]---------------------------------
#
name="addbbcodefontsize"


# 
#-----[ IN-LINE FIND ]---------------------------------
#
this.form.addbbcode20.options


# 
#-----[ IN-LINE REPLACE WITH ]---------------------------------
#
this.form.addbbcodefontsize.options


# 
#-----[ IN-LINE FIND ]---------------------------------
#
this.form.addbbcode20.selectedIndex


# 
#-----[ IN-LINE REPLACE WITH ]---------------------------------
#
this.form.addbbcodefontsize.selectedIndex

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
#-----[ SAVE/CLOSE ALL FILES ]---------------------------------
#
# EoM
