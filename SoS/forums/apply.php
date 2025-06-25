<?php 

// standard hack prevent 
define('IN_PHPBB', true); 
$phpbb_root_path = './'; 
include($phpbb_root_path . 'extension.inc'); 
include($phpbb_root_path . 'common.'.$phpEx); 

// standard session management 
$userdata = session_pagestart($user_ip, PAGE_APPLICATION); 
init_userprefs($userdata); 

// set page title 
$page_title = 'Guild Application'; 

// standard page header 
include($phpbb_root_path . 'includes/page_header.'.$phpEx); 

// assign template 
include($phpbb_root_path . 'application.'.$phpEx);
// standard page footer 
include($phpbb_root_path . 'includes/page_tail.'.$phpEx); 

?>