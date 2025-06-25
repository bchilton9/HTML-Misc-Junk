<?php
/***************************************************************************
 *                            groules_buddy_list_to_PCP.php
 *                            -----------------------------
 *	begin				: 29/05/2003
 *	copyright			: Ptirhiik
 *	email				: admin@rpgnet-fr.com
 *	
 *	version				: 1.0.1
 ***************************************************************************/
define('IN_PHPBB', true);
$phpbb_root_path = './';
include($phpbb_root_path . 'extension.inc');
include($phpbb_root_path . 'common.'.$phpEx);

//
// Start session management
//
$userdata = session_pagestart($user_ip, PAGE_INDEX);
init_userprefs($userdata);
//
// end session management
//
if ($userdata['user_level'] != ADMIN) die('Admin only func');

// read old buddies
$olds = array();
$sql = "SELECT * FROM " . $table_prefix . "buddies ORDER BY user_id, buddy_id";
if (!$result = $db->sql_query ($sql)) message_die (GENERAL_ERROR, 'Could not read old buddy list', __LINE__, __FILE__, $sql);
while ($row = $db->sql_fetchrow($result) ) $olds[] = $row;

for ($i=0; $i < count($olds); $i++)
{
	$user_id = $olds[$i]['user_id'];
	$buddy_id = $olds[$i]['buddy_id'];

	// check if exist
	$sql= "SELECT * FROM " . BUDDYS_TABLE . " WHERE user_id=$user_id and buddy_id=$buddy_id";
	if (!$result = $db->sql_query ($sql)) message_die (GENERAL_ERROR, 'Could not read new buddy list', __LINE__, __FILE__, $sql);
	if ( !($row = $db->sql_fetchrow($result)) )
	{
		$sql = "INSERT INTO " . BUDDYS_TABLE . " 
					(
						user_id, 
						buddy_id, 
						buddy_ignore, 
						buddy_visible
					) VALUES (
						$user_id,
						$buddy_id,
						0,
						0
					)";
		if (!$result = $db->sql_query ($sql)) message_die (GENERAL_ERROR, 'Could not insert a guy in new buddy list', __LINE__, __FILE__, $sql);
	}
}

$msg = 'All done : you can now remove ' . $table_prefix . 'buddies and this prog<br /><br />' . sprintf ($lang['Click_return_index'], '<a href="' . append_sid ('index.'.$phpEx) . '">', '</a>');
message_die (GENERAL_MESSAGE, $msg);

?>