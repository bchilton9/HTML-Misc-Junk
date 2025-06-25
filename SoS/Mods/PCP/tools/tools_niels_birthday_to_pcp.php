<?php
/***************************************************************************
 *                            niels_birthday_to_pcp.php
 *                            -------------------------
 *	begin				: 09/05/2003
 *	copyright			: Ptirhiik
 *	email				: admin@rpgnet-fr.com
 *	
 *	version				: 1.0.0
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
//
// check if the save part has been already done
$sql = "SELECT user_birthday_sav FROM " . USERS_TABLE;
$sav_done = ($db->sql_query($sql));

if ($sav_done) echo "<hr />Save birthday date already done";

// perform the save part
if (!$sav_done)
{
	$sql = "ALTER TABLE " . USERS_TABLE . " CHANGE user_birthday user_birthday_sav INT(11) DEFAULT '999999' NOT NULL";
	$sav_done = ($db->sql_query($sql));
	if (!$sav_done) 
	{
		echo "<hr />An error has occured while trying to save the old user birthday field in " . USERS_TABLE . " table. Check your database, and do it manually.";
		echo "<br />the request to perform is :";
		die( "<br />	" . $sql . "<hr />");
	}
	else echo "<hr>Save old birthday date done successfully";
}

$add_done = false;
if ($sav_done)
{
	$sql = "SELECT user_birthday FROM " . USERS_TABLE;
	$add_done = ($db->sql_query($sql));
	if ($add_done) echo "<br />New user_birthday field already added";
}

// perform the add of the new field
if ($sav_done && !$add_done)
{
	$sql = "ALTER TABLE " . USERS_TABLE .  " ADD user_birthday VARCHAR(8) DEFAULT '0' NOT NULL";
	$add_done = ($db->sql_query($sql));
	if (!$add_done) 
	{
		echo "<br />An error has occured while trying to add the new field to " . USERS_TABLE . " table. Check your database, and do it manually.";
		echo "<br />the request to perform is :";
		die( "<br />	" . $sql . "<hr />");
	}
	else echo "<br />New birthday date field added successfully";
}
echo "<hr />";

// preform the migration
$count = 0;
$count_upd = 0;
if ($sav_done && $add_done)
{
	$sql = "SELECT user_id, user_birthday_sav, user_birthday FROM " . USERS_TABLE . " ORDER BY user_id";
	if ( !( $result = $db->sql_query($sql) ) ) message_die(GENERAL_ERROR, 'Wasn\'t able to read users table', '', __LINE__, __FILE__, $sql);
	while ($row = $db->sql_fetchrow($result))
	{
		$count++;
		$user_birthday_sav = $row['user_birthday_sav'];
		$user_birthday = ($user_birthday_sav == '999999') ? '' : realdate("Ymd", $row['user_birthday_sav']);
		$updated = false;
		if ( (intval($row['user_birthday']) == 0) && (intval($user_birthday) != 0) && (intval($user_birthday) != intval($row['user_birthday'])) )
		{
			$sql = "UPDATE " . USERS_TABLE . " set user_birthday = '" . $user_birthday . "' WHERE user_id = " . $row['user_id'];
			if ( !($db->sql_query($sql)) ) message_die(GENERAL_ERROR, 'Wasn\'t able to update users table', '', __LINE__, __FILE__, $sql);
			$updated = true;
			$count_upd++;
		}
		echo "<br />user_id=" . $row['user_id'] . ", username=" . $row['username'] . ", user_birthday=$user_birthday, user_birthday_sav=" . $row['user_birthday_sav'] . ( ($updated) ? " updated !" : "");
	}
}
echo "<hr />$count users readed, $count_upd users updated<br />";
echo "<br />You can now remove field user_birthday_sav and user_next_birthday_greeting from " . USERS_TABLE . " and uninstall old mod";
echo "<br />Don\'t forget to remove also keys birthday_required, birthday_greeting, max_user_age, min_user_age and birthday_check_day from " . CONFIG_TABLE;
echo "<hr />";

flush();

?>