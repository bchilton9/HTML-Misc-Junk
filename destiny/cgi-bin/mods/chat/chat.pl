############################################################################
#        Chat configuration for WebAPP - Adapted by Simon Jones http://www.simonj.co.uk      #
############################################################################
	require "../../config.pl";
	require "$lang";	
	require "$sourcedir/subs.pl";
	loadcookie();
	loaduser();	
	require "$themesdir/$usertheme/theme.pl"; getvars();
$pagetitle = "Sanctuary Online Chat";	
$chat_url = "$scripturl/mods/chat"; #Change this if you change the directory name
$chat_dir = "$scriptdir/mods/chat"; #Change this if you change the directory name
$url_of_chat_cgi = "$chat_url/chat.cgi";
$path_to_active_users = "$chat_dir/chatters.txt";
$url_of_chat_file = "$baseurl/chat.list.html";
$path_to_chat_file = "$basedir/chat.list.html";
$path_to_language_file = "$chat_dir/lang-en";
$chat_goodbye_url = "$chat_url/goodbye.cgi";
$registered_users = "$chat_dir/registered_users";
$smile_url ="$baseurl/images/forum/smilies";
$login="$username";

########################    End of WebAPP integration      #########################

$chatbg = "#ffffff"; # Main chat background colour - beware this is shared across all themes!
$new_chat_lines_on_top = 0;
$debugging = 0; # set to 1 to activate
$disable_html = 0; # set to 0 to turn off
$idle_timeout = "10"; # time out in minutes before the user is logged off - good if they crash 
$censor_chat = 1; # set to 0 if you don't want to censor - bad words are in badwords.txt
$censored_msg = '@#%$'; # This is printed instead of a bad word
$show_settings_to_user = 1; # shows users what the setup is
$show_user_address = "no"; # Shows IP or machine hostname when they log in
$number_of_chats_to_display = "20"; # number of chat lines displayed
$clear_chatroom_when_empty = 1; # resets the chat line list
$play_sound_when_entering = "no"; # erm, as it says
$url_of_sound_file = "$baseurl/ding.wav"; # this is where the sound is
$server_time_offset = 0; # time offset adjustment
$time_format = "HH:MN:SS "; # set to your time format
$refresh_time = 5; # number of seconds before the chat window is refreshed
$who_refresh = ( $refresh_time * 6 );
$chat_in_new_window = "yes"; # set to yes if you want a new window
$log_directory = "$chat_dir/logs";
$badwords_file = "$chat_dir/badwords.txt";
$path_to_banned_ip_file = "$chat_dir/banned-ip.txt";
# Change to "win" for windows systems.
$opsys = "unix";
$max_log_space = "500000"; # If you run the log this will override it
$log_all_chats = "no"; # set to yes to enable logging

# $type_of_log has four options, described below. You should **CHANGE** this
# to the type of log you want:
# daily:   Creates a new log every day containing chat records from that day.
# monthly: Creates a new log every month.
# big:     Creates one log that gets added to forever. 
$type_of_log = "big";

$disable_special_characters_in_login = 1;
$chat_window_width = 640;
$chat_window_height = 480;

############################    End of script variables      #########################

$chat_window_header = "
<title>Chat window</title>
<script language=Javascript>
function scrollChat () {
	var needtoscroll = $new_chat_lines_on_top;
        if(needtoscroll == 0){
		if(parent.listen != null){
          		parent.listen.scrollBy(0,5000);
			}
		}
	return true;
	
}
</script>
</head>
<body onLoad=\"scrollChat();\" bgcolor=$chatbg>
<strong><center>Sanctuary Chat room!</center></strong>
<font size=-1>Type /help for a list of options.
<hr>
"; #<-- This quote and semicolon are necessary. Don't backslash them!

$chat_window_footer = "</font>

</body></html>

"; #<-- This quote and semicolon are necessary. Don't backslash them!

$form_window_header = "
<html><head><title>Online Chat</title>
<link rel=stylesheet href=$themesurl/$usertheme/style.css type=text/css> 
<SCRIPT LANGUAGE=\"JavaScript\">
<!-- Begin
function validate(){

if (document.TalkForm.Sez2.value==\"\") {
return false
}
else {
document.TalkForm.Sez.value=document.TalkForm.Sez2.value;
document.TalkForm.Sez2.value='';
document.TalkForm.Sez2.focus();
return true
}
}
// End -->
</SCRIPT>
</head>
<body class=menutable topmargin=2 leftmargin=2 bottommargin=2 rightmargin=2>
<CENTER>
<TABLE WIDTH=100% class=menutable BORDER=0 CELLPADDING=0 CELLSPACEING=0>
<TR><TD>
"; #<-- This quote and semicolon are necessary. Don't backslash them!

$form_window_footer = "
</TD></TD></TABLE>
</body></html>

"; #<-- This quote and semicolon are necessary. Don't backslash them!


$banned_message = "
<!-- Banned message start -->

Sorry, but you may not participate in this chatroom.

<!-- Banned message end -->";