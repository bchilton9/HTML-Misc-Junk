<?php
/***************************************************************************
 *							profilcp_public_base.php
 *							------------------------
 *	begin				: 08/05/2003
 *	copyright			: Ptirhiik
 *	email				: admin@rpgnet-fr.com
 *
 *	version				: 1.0.8 - 24/10/2003
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
if ( !empty($setmodules) )
{
	// read maps
	@reset($user_maps);
	while ( list($map_name, $map_data) = @each($user_maps) )
	{
		$map_tree = explode('.', $map_name);
		if ( ($map_tree[0] = 'PCP') && ($map_data['custom'] == 2) )
		{
			// build 
			$map_root = '';
			for ( $i=0; $i < count($map_tree); $i++ )
			{
				$map_root .= ( empty($map_root) ? '' : '.' ) . $map_tree[$i];

				// ignore main level (PCP, phpBB)
				if ( $i == 1 )
				{
					// create it as main menu
					$pgm = '';
					if ( $i == (count($map_tree)-1) )
					{
						$pgm = __FILE__;
					}
					$order = $user_maps[$map_root]['order'];
					$shortcut = $user_maps[$map_root]['title'];
					$pagetitle = $user_maps[$map_root]['title'];
					pcp_set_menu( $map_tree[$i], $order, $pgm, $shortcut, $pagetitle );
				}
				if ( $i > 1 )
				{
					$pgm = '';
					if ( $i == (count($map_tree)-1) )
					{
						$pgm = __FILE__;
					}
					$order = $user_maps[$map_root]['order'];
					$shortcut = $user_maps[$map_root]['title'];
					$pagetitle = $user_maps[$map_root]['title'];
					pcp_set_sub_menu( $map_tree[$i-1], $map_tree[$i], $order, $pgm, $shortcut, $pagetitle );
				}
			}
		}
	}
	return;
}

//----------------------------------------
//
// inits
//
//----------------------------------------

// ids
$user_id = $userdata['user_id'];
$view_user_id = $view_userdata['user_id'];

// get buddy infos
$sql = "SELECT * FROM " . BUDDYS_TABLE . " 
		WHERE (user_id=$user_id AND buddy_id=$view_user_id) OR (user_id=$view_user_id AND buddy_id=$user_id)";
if ( !$result = $db->sql_query($sql) )
{
	message_die(GENERAL_ERROR, 'Could not get buddy information', '', __LINE__, __FILE__, $sql);	
}
while ( $row = $db->sql_fetchrow($result) )
{
	if ( $row['user_id'] = $user_id )
	{
		$view_userdata['user_my_friend'] = !$row['buddy_ignore'];
		$view_userdata['user_my_ignore'] = $row['buddy_ignore'];
		$view_userdata['user_my_visible'] = $row['buddy_visible'];
	}
	else
	{
		$view_userdata['user_friend'] = !$row['buddy_ignore'];
		$view_userdata['user_ignore'] = $row['buddy_ignore'];
		$view_userdata['user_visible'] = $row['buddy_visible'];
	}
}
$view_userdata['user_online'] = ( $view_userdata['user_session_time'] >= (time()-300) );
$view_userdata['user_pm'] = pcp_get_class_check('pm', $view_userdata);

//----------------------------------------
//
// process the maps
//
//----------------------------------------

// read all the maps involved
$maps = array();
$map_orders = array();
$map_base = 'PCP.viewprofile.';
$map_base = 'PCP.' . $mode . '.';
if ( !empty($sub) )
{
	$map_base .= $sub . '.';
}
@reset($user_maps);
while ( list($map_name, $map_data) = @each($user_maps) )
{
	if ( (substr($map_name, 0, strlen($map_base)) == $map_base) && ( !empty($map_data['title']) || !empty($map_data['fields']) ) )
	{
		$maps[] = $map_name;
		$map_orders[] = $user_maps[$map_name]['order'];
	}
}
array_multisort($map_orders, $maps);

// count cols
$col = 1;
for ($i=0; $i < count($maps); $i++)
{
	if ( ($i != 0) && $user_maps[ $maps[$i] ]['split'] )
	{
		$col++;
	}
}

// template file
$template->set_filenames(array(
	'body' => 'profilcp/public_base_body.tpl')
);

$template->assign_vars(array(
	'L_PUBLIC_TITLE'	=> sprintf($lang['Viewing_user_profile'], ( ($view_userdata['user_id'] != ANONYMOUS) ? $view_userdata['username'] : $lang['Guest'] ) ),
	'SPAN'				=> $col,
	)
);

// process the panels
for ($i = 0; $i < count($maps); $i++ )
{
	$split = false;
	if ( $user_maps[ $maps[$i] ]['split'] )
	{
		$split = true;
		$template->assign_block_vars('col', array());
	}

	// count how many cols in the panel
	$col = 1;
	@reset( $user_maps[ $maps[$i] ]['fields'] );
	while ( list($field_name, $field_data) = @each($user_maps[ $maps[$i] ]['fields']) )
	{
		if ( $field_data['leg'] && ($field_data['img'] || $field_data['txt']) )
		{
			$col++;
			$col++;
			break;
		}
	}

	// panel title
	$title = '';
	if ( is_string($user_maps[ $maps[$i] ]['title']) )
	{
		$title = mods_settings_get_lang( $user_maps[ $maps[$i] ]['title'] );
	}
	else
	{
		$user_maps['_temp'] = array();
		$user_maps['_temp']['fields'] = $user_maps[ $maps[$i] ]['title'];
		$title .= pcp_output_panel('_temp', $view_userdata);
	}
	$template->assign_block_vars('col.panel', array(
		'SPAN'	=> $col,
		'TITLE'	=> $title,
		)
	);
	if ( !$split )
	{
		$template->assign_block_vars('col.panel.linefeed', array());
	}

	// panel field
	@reset( $user_maps[ $maps[$i] ]['fields'] );
	while ( list($field_name, $field_data) = @each($user_maps[ $maps[$i] ]['fields']) )
	{
		if (substr($field_name, 0, 4) == '[lf]')
		{
			$template->assign_block_vars('col.panel.row', array());
			$template->assign_block_vars('col.panel.row.linefeed', array());
		}
		else
		{
			$is_leg = ($col > 1);
			$leg = pcp_output($field_name, $view_userdata, $maps[$i], true);

			// forget the legend
			$user_maps[ $maps[$i] ]['fields'][$field_name]['leg'] = false;
			$val = pcp_output($field_name, $view_userdata, $maps[$i]);

			// reset the legend
			$user_maps[ $maps[$i] ]['fields'][$field_name]['leg'] = $is_leg;

			// output
			$template->assign_block_vars('col.panel.row', array());
			if ($is_leg)
			{
				$template->assign_block_vars('col.panel.row.cell', array(
					'CLASS'	=> 'row2',
					'ALIGN'	=> 'right',
					'WIDTH'	=> '40%',
					'WRAP'	=> 'nowrap="nowrap"',
					'VALUE'	=> $is_leg ? $leg . ( !empty($leg) ? ':&nbsp;' : '') : '',
					)
				);
			}
			$template->assign_block_vars('col.panel.row.cell', array(
				'CLASS'	=> 'row1',
				'ALIGN'	=> $is_leg ? 'left' : 'center',
				'WIDTH'	=> $is_leg ? '100%' : '60%',
				'WRAP'	=> '',
				'VALUE'	=> $val,
				)
			);
			if ($is_leg)
			{
				$template->assign_block_vars('col.panel.row.cellfeed', array());
			}
		}
	}
}

// page
$template->pparse('body');

?>