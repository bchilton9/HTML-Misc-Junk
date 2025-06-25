<?php

/***************************************************************************
 *							def_userfuncs_std.php
 *							---------------------
 *	begin				: 04/10/2003
 *	copyright			: Ptirhiik
 *	email				: Ptirhiik@rpgnet.clanmckeen.com
 *
 *	version				: 1.0.1 - 30/10/2003
 *
 ***************************************************************************/

/***************************************************************************
 *
 *   This program is free software; you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation; either version 2 of the License, or
 *   (at your option) any later version.
 *
 *
 ***************************************************************************/

if ( !defined('IN_PHPBB') )
{
	die('Hacking attempt');
	exit;
}

//-----------------------------------
//
// user_online output function
//
//-----------------------------------
function pcp_output_user_online($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if  ( $view_userdata['user_id'] != ANONYMOUS )
	{
		// offline
		$txt = $lang['Offline'];
		$img = '<img src="' . $images['icon_offline'] . '" border="0" align="absbottom" alt="' . $lang['Offline'] . '" title="' . $lang['Offline'] . '" />';
		if ( !empty($view_userdata[$field_name]) )
		{
			// hidden
			$txt = $lang['Hidden'];
			$img = '<img src="' . $images['icon_hidden'] . '" border="0" align="absbottom" alt="' . $lang['Hidden'] . '" title="' . $lang['Hidden'] . '" />';

			// not hidden set : online
			if ($view_userdata['user_allow_viewonline'] == YES)
			{
				$txt = $lang['Online'];
				$img = '<img src="' . $images['icon_online'] . '" border="0" align="absbottom" alt="' . $lang['Online'] . '" title="' . $lang['Online'] . '" />';
			}
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_my_friend output function
//
//-----------------------------------
function pcp_output_my_friend($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;
	global $mode, $sub;

	// use user_my_ignore

	$txt = '';
	$img = '';
	$res = '';
	if ( ($userdata['user_id'] != $view_userdata['user_id']) && ($view_userdata['user_id'] != ANONYMOUS) && $userdata['session_logged_in'] && ($userdata['user_id'] != ANONYMOUS) )
	{
		$from = '&from=profil';
		$maps = explode('.', $map_name);
		if ( empty($maps) )
		{
			$from = '&from=profil';
		}
		if ( in_array('viewprofile', $maps) )
		{
			$from = '&from=profil';
		}
		else if ( in_array('viewtopic', $maps) )
		{
			$from = '&from=topic&' . POST_POST_URL . '=' . $view_userdata['post_id'];
		}
		else if ( in_array('privmsgs', $maps) )
		{
			$from = '&from=privmsg&' . POST_POST_URL . '=' . $view_userdata['privmsgs_id'];
		}
		if ( $view_userdata['user_my_friend'] )
		{
			$temp_url = append_sid("./profile.$phpEx?mode=buddy&sub=friend&b=" . $view_userdata['user_id'] . "&set=remove" . $from);
			$title = $lang['Remove_from_friend_list'];
			$icon = $images['icon_friend_remove'];
			$txt = '<a href="' . $temp_url . '">' . $title . '</a>';
			$img = '<a href="' . $temp_url . '"><img src="' . $icon . '" alt="' . $title . '" title="' . $title . '" border="0" /></a>';
		}
		else if ( !$view_userdata['user_my_ignore'] )
		{
			$temp_url = append_sid("./profile.$phpEx?mode=buddy&sub=friend&b=" . $view_userdata['user_id'] . "&set=add" . $from);
			$title = $lang['Add_to_friend_list'];
			$icon = $images['icon_friend_add'];
			$txt = '<a href="' . $temp_url . '">' . $title . '</a>';
			$img = '<a href="' . $temp_url . '"><img src="' . $icon . '" alt="' . $title . '" title="' . $title . '" border="0" /></a>';
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_my_friend output function for buddy list
//
//-----------------------------------
function pcp_output_my_friend_buddy($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;
	global $mode, $sub;

	// use user_my_visible

	$txt = '';
	$img = '';
	$res = '';
	if ( ($userdata['user_id'] != $view_userdata['user_id']) && ($view_userdata['user_id'] != ANONYMOUS) && $userdata['session_logged_in'] && ($userdata['user_id'] != ANONYMOUS) )
	{
		if ( $view_userdata['user_my_friend'] )
		{
			$temp_url = append_sid( "./profile.$phpEx?mode=" . $mode . "&sub=$sub&b=" . $view_userdata['user_id'] . "&set=" . ( $view_userdata['user_my_visible'] ? 'inv' : 'vis') );
			$title = $view_userdata['user_my_visible'] ? $lang['Always_visible'] : $lang['Not_always_visible'];
			$icon = $view_userdata['user_my_visible'] ? $images['icon_visible'] : $images['icon_not_visible'];
			$txt = '<a href="' . $temp_url . '">' . $title . '</a>';
			$img = '<a href="' . $temp_url . '"><img src="' . $icon . '" border="0" alt="' . $title . '" /></a>';
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_my_ignore output function
//
//-----------------------------------
function pcp_output_my_ignore($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	// uses user_my_friend

	$txt = '';
	$img = '';
	if ( ($view_userdata['user_id'] != $userdata['user_id']) && ($view_userdata['user_id'] != ANONYMOUS) && $userdata['session_logged_in'] && ($userdata['user_id'] != ANONYMOUS) )
	{
		$from = '&from=profil';
		$maps = explode('.', $map_name);
		if ( empty($maps) )
		{
			$from = '&from=profil';
		}
		if ( in_array('viewprofile', $maps) )
		{
			$from = '&from=profil';
		}
		else if ( in_array('viewtopic', $maps) )
		{
			$from = '&from=topic&' . POST_POST_URL . '=' . $view_userdata['post_id'];
		}
		else if ( in_array('privmsgs', $maps) )
		{
			$from = '&from=privmsg&' . POST_POST_URL . '=' . $view_userdata['privmsgs_id'];
		}
		if ( $view_userdata['user_my_ignore'] )
		{
			$temp_url = append_sid("./profile.$phpEx?mode=buddy&sub=ignore&b=" . $view_userdata['user_id'] . "&set=remove" . $from);
			$title = $lang['Remove_from_ignore_list'];
			$icon = $images['icon_ignore_remove'];
			$txt = '<a href="' . $temp_url . '">' . $title . '</a>';
			$img = '<a href="' . $temp_url . '"><img src="' . $icon . '" alt="' . $title . '" title="' . $title . '" border="0" /></a>';
		}
		else if (!is_admin($userdata) && !is_admin($view_userdata) && (get_user_level($userdata) != MOD) && (get_user_level($view_userdata) != MOD) && !$view_userdata['user_my_friend'])
		{
			$temp_url = append_sid("./profile.$phpEx?mode=buddy&sub=ignore&b=" . $view_userdata['user_id'] . "&set=add" . $from);
			$title = $lang['Add_to_ignore_list'];
			$icon = $images['icon_ignore_add'];
			$txt = '<a href="' . $temp_url . '">' . $title . '</a>';
			$img = '<a href="' . $temp_url . '"><img src="' . $icon . '" alt="' . $title . '" title="' . $title . '" border="0" /></a>';
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// username output function
//
//-----------------------------------
function pcp_output_username($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$username = ($view_userdata['user_id'] != ANONYMOUS) ? $view_userdata[$field_name] : ( (isset($view_userdata['post_username']) && ($view_userdata['post_username'] !='') ) ? $view_userdata['post_username'] : $lang['Guest'] );

	// txt
	$txt = '<span class="' . get_user_level_class($view_userdata['user_level'], 'gen', $view_userdata) . '">' . $username . '</span>';

	// img
	if ( $view_userdata['user_id'] != ANONYMOUS )
	{
		$temp_url = append_sid("./profile.$phpEx?mode=viewprofile&amp;" . POST_USERS_URL . '=' . $view_userdata['user_id']);
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_profile'] . '" border="0" alt="' . $lang['Read_profile'] . '" title="' . $lang['Read_profile'] . '" /></a>';
	}

	// result
	$res = pcp_output_format($field_name, $txt, $img, $map_name);
	return $res;
}

//-----------------------------------
//
// username output function with link on txt
//
//-----------------------------------
function pcp_output_username_linked($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$username = ($view_userdata['user_id'] != ANONYMOUS) ? $view_userdata[$field_name] : ( (isset($view_userdata['post_username']) && ($view_userdata['post_username'] !='') ) ? $view_userdata['post_username'] : $lang['Guest'] );

	// txt
	if ( $view_userdata['user_id'] != ANONYMOUS )
	{
		$temp_url = append_sid("./profile.$phpEx?mode=viewprofile&amp;" . POST_USERS_URL . '=' . $view_userdata['user_id']);
		$txt = '<a href="' . $temp_url . '" title="' . $lang['Read_profile'] . '" class="' . get_user_level_class($view_userdata['user_level'], 'gen', $view_userdata) . '">' . $username . '</a>';
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_profile'] . '" border="0" alt="' . $lang['Read_profile'] . '" title="' . $lang['Read_profile'] . '" /></a>';
	}
	else
	{
		$txt = '<span class="' . get_user_level_class($view_userdata['user_level'], 'gen', $view_userdata) . '">' . $username . '</span>';
	}

	// result
	$res = pcp_output_format($field_name, $txt, $img, $map_name);
	return $res;
}

//-----------------------------------
//
// user_pm output function
//
//-----------------------------------
function pcp_output_user_pm($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) && ($userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url = append_sid("./privmsg.$phpEx?mode=post&" . POST_USERS_URL . '=' . $view_userdata['user_id']);
		$txt = '<a href="' . $temp_url . '" title="' . $lang['Send_private_message'] . '">' . $lang['Send_private_message'] . '</a>';
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_pm'] . '" alt="' . $lang['Send_private_message'] . '" title="' . $lang['Send_private_message'] . '" border="0" /></a>';

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_email output function
//
//-----------------------------------
function pcp_output_user_email($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	// add text for admin view in buddy/memberlist
	if ( in_array($map_name, array('PCP.buddy')) && is_admin($userdata))
	{
		$user_maps[$map_name]['fields'][$field_name]['txt'] = true;
		$user_maps[$map_name]['fields'][$field_name]['crlf'] = true;
	}

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url = ( $board_config['board_email_form'] ) ? append_sid("./profile.$phpEx?mode=email&amp;" . POST_USERS_URL . '=' . $view_userdata['user_id']) : 'mailto:' . $view_userdata[$field_name];

		$txt_title = ( is_admin($userdata) || $user_maps[$map_name]['fields'][$field_name]['img'] || $board_config['board_email_form'] ) ? $lang['Send_email'] : $view_userdata[$field_name];
		$txt_link = ( is_admin($userdata) || ($user_maps[$map_name]['fields'][$field_name]['img'] && !$board_config['board_email_form'] ))? $view_userdata[$field_name] : $lang['Send_email'];
		$txt = '<a href="' . $temp_url . '" title="' . $txt_title . '">' . $txt_link . '</a>';
		$txt_title = (is_admin($userdata) || !$board_config['board_email_form']) ? $view_userdata[$field_name] : $lang['Send_email'];
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_email'] . '" alt="' . $lang['Send_email'] . '" title="' . $txt_title . '" border="0" /></a>';

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_icq output function
//
//-----------------------------------
function pcp_output_icq($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url = 'http://wwp.icq.com/' . $view_userdata[$field_name] . '#pager';
		$icq_status_img = '<a href="' . $temp_url . '"><img src="http://web.icq.com/whitepages/online?icq=' . $view_userdata[$field_name] . '&img=5" width="18" height="18" border="0" /></a>';
		$icq_img = '<a href="http://wwp.icq.com/scripts/search.dll?to=' . $view_userdata[$field_name] . '"><img src="' . $images['icon_icq'] . '" alt="' . $lang['ICQ'] . '" title="' . $view_userdata[$field_name] . '" border="0" /></a>';
		$txt = '<a href="' . $temp_url . '" title="' . $view_userdata[$field_name] . '" title="' . $view_userdata[$field_name] . '">' . $lang['ICQ'] . '</a>';
		$img = '<table cellspacing="0" cellpadding="0" border="0"><tr><td><script language="JavaScript" type="text/javascript"><!-- 
				if ( navigator.userAgent.toLowerCase().indexOf(\'mozilla\') != -1 && navigator.userAgent.indexOf(\'5.\') == -1 && navigator.userAgent.indexOf(\'6.\') == -1 )
					document.write(\'' . $icq_img . '\');
				else
					document.write(\'</td><td nowrap="nowrap"><div style="position:relative" valign="top"><div style="position:absolute">' . $icq_img . '</div><div style="position:absolute;left:3px;top:-1px">' . $icq_status_img . '</div></div>\');
			//--></script><noscript>' . $icq_img . '</noscript>&nbsp;</span></td></tr></table>';

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}
//-----------------------------------
//
// user_aim output function
//
//-----------------------------------
function pcp_output_aim($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url = 'aim:goim?screenname=' . $view_userdata[$field_name] . '&amp;message=Hello+Are+you+there?';
		$txt = '<a href="' . $temp_url . '" title="' . $view_userdata[$field_name] . '">' . $lang['AIM'] . '</a>';
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_aim'] . '" alt="' . $lang['AIM'] . '" title="' . $view_userdata[$field_name] . '" border="0" /></a>';

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_yim output function
//
//-----------------------------------
function pcp_output_yim($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url = 'http://edit.yahoo.com/config/send_webmesg?.target=' . $view_userdata[$field_name] . '&amp;.src=pg';
		$txt = '<a href="' . $temp_url . '" title="' . $view_userdata[$field_name] . '">' . $lang['YIM'] . '</a>';
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_yim'] . '" alt="' . $lang['YIM'] . '" title="' . $view_userdata[$field_name] . '" border="0" /></a>';

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_msnm output function
//
//-----------------------------------
function pcp_output_msnm($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url = (substr($map_name, 0, 6) == 'PHPBB.') ? append_sid("./profile.$phpEx?mode=viewprofile&amp;" . POST_USERS_URL . '=' . $view_userdata['user_id']) : 'mailto:' . $view_userdata[$field_name];
		$txt = '<a href="' . $temp_url . '" title="' . $view_userdata[$field_name] . '">' . $lang['MSNM'] . '</a>';
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_msnm'] . '" alt="' . $lang['MSNM'] . '" title="' . $view_userdata[$field_name] . '" border="0" /></a>';

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_timezone output function
//
//-----------------------------------
function pcp_output_timezone($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( $view_userdata['user_id'] != ANONYMOUS )
	{
		@reset($lang['tz']);
		while ( list($offset, $value) = @each($lang['tz']) )
		{
			if ( $view_userdata[$field_name] == $offset )
			{
				$txt = $value . '&nbsp;(' . create_date($userdata['user_dateformat'], time(), $view_userdata['user_timezone']) . ')';
				$img = '<img src="' . $images['tz_' . $offset] . '" border="0" alt="' . $value . '" title="' . $txt .'" />';
				break;
			}
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_website output function
//
//-----------------------------------
function pcp_output_website($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		if ( substr($map_name, 0, 4) == 'PCP.' )
		{
			$link = $view_userdata[$field_name];
			$title = $lang['Visit_website'];
		}
		else
		{
			$link = $lang['Visit_website'];
			$title = $view_userdata[$field_name];
		}
		$txt = '<a href="' . $view_userdata[$field_name] . '" target="_userwww" title="' . $title . '">' . $link . '</a>';
		$img = '<a href="' . $view_userdata[$field_name] . '" target="_userwww"><img src="' . $images['icon_www'] . '" alt="' . $lang['Visit_website'] . '" title="' . $view_userdata[$field_name] . '" border="0" /></a>';

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_gender output function
//
//-----------------------------------
function pcp_output_gender($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( $view_userdata['user_id'] != ANONYMOUS )
	{
		switch ($view_userdata[$field_name])
		{
			case 0:
				$txt = $lang['No_gender_specify'];
				$img = '<img src="' . $images['No_gender_specify'] . '" border="0" alt="' . $lang['No_gender_specify'] . '" title="' . $lang['No_gender_specify'] . '" />';
				break;
			case 1:
				$txt = $lang['Male'];
				$img = '<img src="' . $images['Male'] . '" border="0" alt="' . $lang['Male'] . '" title="' . $lang['Male'] . '" />';
				break;
			case 2:
				$txt = $lang['Female'];
				$res = '<img src="' . $images['Female'] . '" border="0" alt="' . $lang['Female'] . '" title="' . $lang['Female'] . '" />';
				break;
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_age output function
//
//-----------------------------------
function pcp_output_age($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	// use user_birthday
	$pm_display = pcp_get_class_check('pm', $view_userdata);

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata['user_birthday']) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url = $pm_display ? append_sid("./privmsg.$phpEx?mode=post&amp;" . POST_USERS_URL . '=' . $view_userdata['user_id']) : '';
		$img = ( intval(substr($view_userdata['user_birthday'], 4, 4)) == date('md', time()) ) ? ( $pm_display ? '<a href="' . $temp_url . '"><img src="' . $images['icon_birthday'] . '" border="0" alt="' . $lang['Happy_birthday'] . '" title="' . $lang['Happy_birthday'] . '" /></a>' : '<img src="' . $images['icon_birthday'] . '" border="0" alt="' . $lang['Happy_birthday'] . '" title="' . $lang['Happy_birthday'] . '" />') : '';
		$txt = date('Y', time()) - intval(substr($view_userdata['user_birthday'], 0, 4));
		if ( intval(substr($view_userdata['user_birthday'], 4, 4)) > date('md', time()) )
		{
			$txt--;
		}
		if ($txt < 0)
		{
			$txt = '';
			$img = '';
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_rank_title output function
//
//-----------------------------------
function pcp_output_rank_title($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	if ( $view_userdata['user_id'] != ANONYMOUS )
	{
		$rank = get_user_rank($view_userdata);
		$txt = $rank['rank_title'];
		$img = $rank['rank_image'];

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_avatar output function
//
//-----------------------------------
function pcp_output_avatar($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && $userdata['user_viewavatar'] && $view_userdata['user_allowavatar'] && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		switch ($view_userdata[$field_name . '_type'] )
		{
			case USER_AVATAR_UPLOAD:
				$img = ( $board_config['allow_avatar_upload'] ) ? '<img src="' . $board_config['avatar_path'] . '/' . $view_userdata[$field_name] . '" alt="' . $lang['Avatar'] . '" border="0" />' : '';
				break;
			case USER_AVATAR_REMOTE:
				$img = ( $board_config['allow_avatar_remote'] ) ? '<img src="' . $view_userdata[$field_name] . '" alt="' . $lang['Avatar'] . '" border="0" />' : '';
				break;
			case USER_AVATAR_GALLERY:
				$img = ( $board_config['allow_avatar_local'] ) ? '<img src="' . $board_config['avatar_gallery_path'] . '/' . $view_userdata[$field_name] . '" alt="' . $lang['Avatar'] . '" border="0" />' : '';
				break;
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_sig output function
//
//-----------------------------------
function pcp_output_sig($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) && $view_userdata['user_allow_sig'] && $userdata['user_viewsig'] )
	{
		$user_sig = $view_userdata[$field_name];
		$user_sig_bbcode_uid = $view_userdata[$field_name . '_bbcode_uid'];			
		if ( !$board_config['allow_html'] && $userdata['user_allowhtml'])
		{
			$user_sig = preg_replace('#(<)([\/]?.*?)(>)#is', "&lt;\\2&gt;", $user_sig);
		}
		if ($board_config['allow_bbcode'] && ($user_sig_bbcode_uid != ''))
		{
			$user_sig = ( $board_config['allow_bbcode'] ) ? bbencode_second_pass($user_sig, $user_sig_bbcode_uid) : preg_replace('/\:[0-9a-z\:]+\]/si', ']', $user_sig);
		}
		$user_sig = make_clickable($user_sig);
		if ( $board_config['allow_smilies'] && $view_userdata['user_allowsmile'])
		{
			$user_sig = smilies_pass($user_sig);
		}
		if (count($orig_word) > 0)
		{
			$user_sig = str_replace('\"', '"', substr(preg_replace('#(\>(((?>([^><]+|(?R)))*)\<))#se', "preg_replace(\$orig_word, \$replacement_word, '\\0')", '>' . $user_sig . '<'), 1, -1));
		}
		$txt = str_replace("\n", "\n<br />\n", $user_sig);

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_regdate output function
//
//-----------------------------------
function pcp_output_regdate($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata[$field_name]) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$txt = create_date($lang['DATE_FORMAT'], $view_userdata[$field_name], $userdata['user_timezone']);
		if ( substr($map_name, 0, 4) == 'PCP.' )
		{
			$txt .= '&nbsp;(' . max(1, round( ( time() - $view_userdata['user_regdate'] ) / 86400 )) . '&nbsp;' . $lang['Days']. ')';
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_posts_stat output function
//
//-----------------------------------
function pcp_output_posts_stat($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata['user_posts']) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$temp_url	= append_sid("./search.$phpEx?search_author=" . urlencode($view_userdata['username']) . "&amp;showresults=posts");
		$img = '<a href="' . $temp_url . '"><img src="' . $images['icon_search'] . '" alt="' . sprintf($lang['Search_user_posts'], $view_userdata['username']) . '" title="' . sprintf($lang['Search_user_posts'], $view_userdata['username']) . '" border="0" /></a>';
		if ( !$user_maps[$map_name]['fields'][$field_name]['img'] )
		{
			$txt .= '<a href="' . $temp_url . '" title="' . sprintf($lang['Search_user_posts'], $view_userdata['username']) . '" class="topictitle"><b>' . sprintf($lang['Search_user_posts'], $view_userdata['username']) . '</b></a>';
		}

		$posts_per_day = $view_userdata['user_posts'] / max(1, round( (time() - $view_userdata['user_regdate']) / 86400 ));
		$total_posts = get_db_stat('postcount');
		$percentage = ( $total_posts ) ? ( ($view_userdata['user_posts'] * 100) / $total_posts ) : 0;
		$txt .= ( empty($txt) ? '' : '<br />' ) . sprintf('[' . $lang['User_post_stats'] . ']', $view_userdata['user_posts'], $percentage, $posts_per_day);

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_topics_stat output function
//
//-----------------------------------
function pcp_output_topics_stat($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;
	global $db;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata['user_posts']) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$most_active_topic = -1;
		$most_active_topic_title = '';
		$most_active_topic_posts = 0;
		$most_active_topic_posts_total = 0;
		$most_active_topic_posts_total_forum = 0;

		// get the value
		$is_auth = auth(AUTH_VIEW, AUTH_LIST_ALL, $userdata);
		$forum_ids = array();
		while (list($forum_id, $auth) = @each($is_auth) )
		{
			if ($auth['auth_view']) $forum_ids[] = $forum_id;
		}
		if ( !empty($forum_ids) )
		{
			$s_forum_ids = implode(', ', $forum_ids);

			// most active topic
			$sql = "SELECT p.topic_id, f.forum_posts, t.topic_title, t.topic_replies+1 AS topic_posts, count(p.post_id) AS posts_count
					FROM " . POSTS_TABLE . " p, " . TOPICS_TABLE . " t, " . FORUMS_TABLE . " f
					WHERE p.poster_id = " . $view_userdata['user_id'] . "
						AND t.topic_id = p.topic_id
						AND t.forum_id IN ($s_forum_ids)
						AND f.forum_id = t.forum_id
					GROUP BY p.topic_id
					ORDER BY posts_count DESC
					LIMIT 0,1";
			if ( !$result = $db->sql_query($sql) )
			{
				message_die(GENERAL_ERROR, 'Could not get most active topic informations', '', __LINE__, __FILE__, $sql);
			}
			if ( $row = $db->sql_fetchrow($result) )
			{
				// Define censored word matches
				$orig_word = array();
				$replacement_word = array();
				obtain_word_list($orig_word, $replacement_word);

				// get the info
				$most_active_topic_id = $row['topic_id'];
				$most_active_topic_title = ( count($orig_word) ) ? preg_replace($orig_word, $replacement_word, $row['topic_title']) : $row['topic_title'];
				$most_active_topic_posts = $row['posts_count'];
				$most_active_topic_posts_total = $row['topic_posts'];
				$most_active_topic_posts_total_forum = $row['forum_posts'];
			}

			// display
			if ( $most_active_topic_id > -1 )
			{
				// topic
				$temp_url = append_sid("./viewtopic.$phpEx?" . POST_TOPIC_URL . "=$most_active_topic_id");
				$txt = '<a href="' . $temp_url . '" class="topictitle">' . $most_active_topic_title . '</a>';
				$txt .= '<br /><span class="genmed">' . sprintf( '[' . $lang['Most_active_topic_stat'] . ']', $most_active_topic_posts, ( ($most_active_topic_posts*100) / $most_active_topic_posts_total ), ( ($most_active_topic_posts*100) / $most_active_topic_posts_total_forum ) ) . '</span>';
			}
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_forums_stat output function
//
//-----------------------------------
function pcp_output_forums_stat($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;
	global $db;

	$txt = '';
	$img = '';
	$res = '';
	if ( !empty($view_userdata['user_posts']) && ($view_userdata['user_id'] != ANONYMOUS) )
	{
		$most_active_forum_id = -1;
		$most_active_forum_name = '';
		$most_active_forum_posts = 0;
		$most_active_forum_posts_total = 0;
		$total_posts = get_db_stat('postcount');

		$is_auth = auth(AUTH_VIEW, AUTH_LIST_ALL, $userdata);
		$forum_ids = array();
		while (list($forum_id, $auth) = @each($is_auth) )
		{
			if ($auth['auth_view']) $forum_ids[] = $forum_id;
		}
		if ( !empty($forum_ids) )
		{
			$s_forum_ids = implode(', ', $forum_ids);

			// most active forum
			$sql = "SELECT t.forum_id, f.forum_name, f.forum_posts, count(p.post_id) AS posts_count
					FROM " . POSTS_TABLE . " p, " . TOPICS_TABLE . " t, " . FORUMS_TABLE . " f
					WHERE p.poster_id = " . $view_userdata['user_id'] . "
						AND t.topic_id = p.topic_id
						AND t.forum_id IN ($s_forum_ids)
						AND f.forum_id = t.forum_id
					GROUP BY t.forum_id
					ORDER BY posts_count DESC
					LIMIT 0, 1";
			if ( !$result = $db->sql_query($sql) )
			{
				message_die(GENERAL_ERROR, 'Could not get most active forum informations', '', __LINE__, __FILE__, $sql);
			}
			if ( $row = $db->sql_fetchrow($result) )
			{
				$most_active_forum_id = $row['forum_id'];
				$most_active_forum_name = isset($lang[ $row['forum_name'] ]) ? $lang[ $row['forum_name'] ] : $row['forum_name'];
				$most_active_forum_posts = $row['posts_count'];
				$most_active_forum_posts_total = $row['forum_posts'];
			}

			// display
			if ( $most_active_forum_id > -1 )
			{
				// forum
				$temp_url = append_sid("./viewforum.$phpEx?" . POST_FORUM_URL . "=$most_active_forum_id");
				$txt = '<a href="' . $temp_url . '" class="topictitle">' . $most_active_forum_name . '</a>';
				$txt .= '<br /><span class="genmed">' . sprintf( '[' . $lang['Most_active_forum_stat'] . ']', $most_active_forum_posts, ( ($most_active_forum_posts*100) / $most_active_forum_posts_total ), ( ($most_active_forum_posts*100) / $total_posts ) ) . '</span>';
			}
		}

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

//-----------------------------------
//
// user_groups output function
//
//-----------------------------------
function pcp_output_usergroups($field_name, $view_userdata, $map_name='')
{
	global $board_config, $phpbb_root_path, $phpEx, $lang, $images, $userdata;
	global $values_list, $tables_linked, $classes_fields, $user_maps, $user_fields;
	global $db, $template;

	$txt = '';
	$img = '';
	$res = '';
	if ( $view_userdata['user_id'] != ANONYMOUS )
	{
		// save template state
		$sav_tpl = $template->_tpldata;

		// template file
		$template->set_filenames(array(
			'_box_groups' => 'profilcp/public_groups_body.tpl')
		);

		$template->assign_block_vars('tiny_panel', array());

		// groupes
		$sql = "SELECT 
					g.group_id, 
					g.group_name, 
					g.group_description, 
					g.group_type 
				FROM 
					" . USER_GROUP_TABLE . " l, 
					" . GROUPS_TABLE . " g 
				WHERE l.user_pending = 0 
					AND g.group_single_user = 0 
					AND l.user_id = " . $view_userdata['user_id'] . "
					AND g.group_id = l.group_id 
				ORDER BY 
					g.group_name, 
					g.group_id";
		if ( !$result = $db->sql_query($sql) ) 
		{
			message_die(GENERAL_ERROR, 'Could not read groups', '', __LINE__, __FILE__, $sql);	
		}
		$groups = array();
		while ($row = $db->sql_fetchrow($result))
		{
			$groups[] = $row;
		}

		$template->assign_vars(array(
			'L_USERGROUPS'	=> $lang['Usergroups'],
			'L_NO_GROUPS'	=> $lang['None'],
			'TXTCLASS'		=> 'gensmall',
			)
		);
		$nb = 0;
		if (count($groups) > 0)
		{
			$class = false;
			for ($i=0; $i < count($groups); $i++)
			{
				$is_ok = false;

				// group hidden ?
				if ( ($groups[$i]['group_type'] != GROUP_HIDDEN) || is_admin($userdata) )
				{
					$is_ok=true;
				}
				else
				{
					$group_id = $groups[$i]['group_id'];
					$sql = "SELECT * FROM " . USER_GROUP_TABLE . " 
							WHERE group_id = $group_id 
								AND user_id = " . $userdata['user_id'] . "
								AND user_pending=0";
					if ( !$result = $db->sql_query($sql) )
					{
						message_die(GENERAL_ERROR, 'Couldn\'t obtain viewer group list', '', __LINE__, __FILE__, $sql);
					}
					$is_ok = ( $row = $db->sql_fetchrow($result) );
				}

				// group allowed : display
				if ($is_ok)
				{
					$nb++;
					$class = !$class;
					$u_group_name = append_sid("groupcp.$phpEx?" . POST_GROUPS_URL . '=' . $groups[$i]['group_id']);
					$l_group_name = $groups[$i]['group_name'];
					$l_group_desc = $groups[$i]['group_description'];
					$template->assign_block_vars('groups',array(
						'CLASS'			=> ($class) ? "row1" : "row2",
						'U_GROUP_NAME'	=> $u_group_name,
						'L_GROUP_NAME'	=> $l_group_name,
						'L_GROUP_DESC'	=> $l_group_desc,
						)
					);
				}  // end if ($is_ok)
			}  // end for ($i=0; $i < count($groups); $i++)
		}  // end if (count($groups) > 0)

		if ($nb == 0)
		{
			$template->assign_block_vars('no_groups', array('SPAN' => 1));
		}

		// transfert to a var
		$template->assign_var_from_handle('_box', '_box_groups');
		$txt = $template->_tpldata['.'][0]['_box'];

		// result
		$res = pcp_output_format($field_name, $txt, $img, $map_name);
	}
	return $res;
}

?>