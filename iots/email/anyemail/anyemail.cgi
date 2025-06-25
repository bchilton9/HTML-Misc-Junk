#!/usr/bin/perl


$perlapp = 0;

if($perlapp) {
	my $f = PerlApp::exe();
	my $fi = $f;
	$fi =~ s/anyemail.exe/anyemail_cfg.pl/i;
	$f =~ s/anyemail.exe/anyemail_lib.pl/i;
	eval {
		do $f;
		do $fi ;
	};
	error($@) if $@;
}

eval "use Mail::SpamAssassin;";
if(!$@) {
	$main::use_spamkiller=1;	
}
$main::spamtest = undef;

eval "use Date::Parse;";

if(!$@) {
	$main::use_date_parse=1;	
}

eval {
	anyemail_run();
};

if($@) {
	error($@, join("<br>", $@, caller(5) ) );	

}


#use strict;
#no strict 'vars';

BEGIN {
use vars qw(@bT);

$anyemaildir = "/hsphere/local/home/destiny/destinyeq2.com/aedata"; ## the top level directory that contains custom configurations and data
			    ## you must make it writable (chmod 0777 if needed)

$icon_location="/aeicons"; ## URL of the directory under which the fA are stored

$fix_cgi_url="";     ## for IIS users, you must set this to the full url of the anyemail script, others may leave this unchanged 

$smtp_server="localhost"; ## change this to your smtp server

$use_sendmail = 0; ## set to 1 if using dM command

$sendmail_cmd = '/usr/lib/dM -t'; ## notice the -t flag

$mOz = 1; #set this to 1 to disable WYSIWYG HTML editing

$use_long_form = 1; ## set 1 if want to show the long login form with POP3 server

$left_panel = 0;

$no_cmd_bar = 1;

$pop_attachment=0;

$default_charset ="iso-8859-1"; 


$use_fixed_popserver_only = 0;  ## set this to only allow checking email on a single server
$fixed_pop_server="your-domain";    
$fixed_return_domain="your-domain";    ## if this is set and no domain provided, then return address is user@domain 
$non_changeable_from_address = 0; ## don't allow user to change the from address
$broke_pathinfo = 1; ## set this to 1 if script not found error when retrieve attachments


##for these pop3 servers using email as pop id

%use_email_as_id_for_pops =('gctea.org'=>1
);

$broke_uidl_command = 0; ## set this to 1 if UIDL command is broken

%email_to_pop3_map = (
"mydomain.com" => "pop3.mydomain.com",   ##for address me@mydomain.com go to pop3.mydomain.com to fetech email
"herdomain.com" => "pop3.herdomain.com"
);

@bT = qw(Subject From Date size Status);
@bT = qw(Subject From Date size) if $no_status;

$VERSION = 6.25; 

$default_smtp_port = 25;

$use_smtp_auth = 0;
$fix_smtp_user ="";
$fix_smtp_passwd ="";

$debug_log = "/tmp/ae.debug";
$log_send = 0;  ## log sending activity  
$log_read = 0;  ## log reading activity  
$no_pop_win = 1;
$debug = 1;
$onlinedemo = 0;
$gimgidx = 0;
$pop_msg = 0;
$no_frames = 0;
$no_headers= 0; ## does not show header
$no_junk = 0; ## set to 1 to not enable bulk mail and junk mail features
$no_status =0; ## set to 1 to remove the status column
$mkcmd = "/users.exe";
$rm_html_in_reply =1;

$comp_name ="netbula.com";


  #################### COLORS ##################################

@bgcols =("#ffffff", "#fefefa"); #backgrounds of  message list line
$hi_bg ="#dfdfdf"; ##background color of selected messages

$form_color= qq("#93bee2");      #background of the compose form
$form_body_bg= qq("#336699"); #background of the send message window

$label_bg_color=qq(#5588bb);    #background of the label columns

$bar_bg_color=qq(#336699);    #background of the table columns
$bar_txt_color=qq(#ffffee);    #text of the table columns

$cmd_bar_bg=qq(#c0c0c0);    #background of the command bar

$body_bg_color=qq(#77aadd);    #background of the mail listings display
$cmd_panel_bg =qq(#93bee2);    #background of the command panel 

$pglist_bg_color=qq(#4477aa);    #background of the page list area
$pglist_txt_color=qq(#ffffff);    #text color of the page list area

$mpage_tit_bg = qq(#bbbbbb);

$login_form_field_bg =qq(#93bee2);
$login_form_field_font =qq(color=#002200);
$login_form_tit_bg =qq(#336699);

$box_label_bg =qq(#6699cc);


  #################### COLORS ##################################

  ##set the fonts for mail fields

$subject_font ="";
$from_font = "";
$size_font = qq(size="1");

$inbox_label =qq(<b><font color="white">Inbox mail</font></b>);
$bulk_label =qq(<b><font color="white">Bulk mail?</font></b>  );
$sent_label =qq(<b>Sent mail</b>  );
$kept_label =qq(<b>Good mail</b>  );
$junk_label =qq(<b>Junk mail</b>  );
$trash_label =qq(<b>Trash</b>  );
$draft_label =qq(<b><font color="white">Draft mail</font></b>  );

%type_labels=(
'recv'=>[0, $inbox_label], 
'bulk'=>[1, $bulk_label], 
'sent'=>[2, $sent_label],
'junk'=>[3, $junk_label],
'draft'=>[4, $draft_label],
'trash'=>[5, $trash_label],
'kept'=>[6, $kept_label],
);

%type_folders=(
'recv'=>"Inbox folder", 
'bulk'=>"Inbox folder", 
'kept'=>"Good mail",
'sent'=>"Sent mail",
'junk'=>"Junk mail",
'trash'=>"Trash bin",
);

$reply_label = qq(\&nbsp;<img src="$icon_location/replybt2.gif" border="0" alt="Reply message">);
$replyall_label = qq(\&nbsp;<img src="$icon_location/reply_all.gif" border="0" alt="Reply to all">);
$forward_label = qq(\&nbsp;<img src="$icon_location/forwardbt2.gif" border="0" alt="Forward message">);
$back_label = qq(<img src="$icon_location/back.gif" border="0" alt="Close message">);
$check_btn = qq(<img src="$icon_location/check2.gif" width="66" height="39" border="0" alt="Check For New Mail">);
$compose_btn = qq(<img src="$icon_location/compose2.gif" width="75" height="39" border="0" alt="Compose a new Message">);
$logout_btn = qq(<img src="$icon_location/logout2.gif" width="59" height="39" border="0" alt="Log out">);
$newusr_btn = qq(<img src="$icon_location/newuser2.gif" width="59" height="39" border="0" alt="Check another account">);
$address_btn =qq(<img src="$icon_location/address.gif" width="59" height="39" border="0" alt="Address book and personal settings">);
$help_btn = qq(<img src="$icon_location/help2.gif" width="29" height="39" border="0" alt="Help With">);
$important_label =qq(<b><font color=red face="impact">!</font></b>);
$attachment_label =qq(<img src="$icon_location/clip.gif">);

$fN = qq($icon_location/qon.gif);
$fQ =  qq($icon_location/qoff.gif);
$fS = qq($icon_location/hon.gif);
$fR = qq($icon_location/hoff.gif);
$del_src = qq($icon_location/delete.gif);

$icon_attr = qq(width="16" height="15");

$charset_str = "; charset=$default_charset" if $default_charset;


$td_bg= qq($icon_location/bg.gif);

$linetl = qq(<img src="$icon_location/linetl.gif" width="13" height="12" border="0" alt="">);
$linetr = qq(<img border="0" src="$icon_location/linetr.gif" width="11" height="12">);
$spline_gif = qq(<img src="$icon_location/spline.gif" width="7" height="39" border="0">);

 ##spell checker configure this
    $main::enable_speller=0; #set it to 1 to enable
    $main::spellcgi ="/cgi-bin/sproxy.cgi";

 ## no need to change what's below, unless you put spch.js out of the www/ root 
    $main::fBz = "/spch.js";    #URI of the spch.js script
    $main::spell_js=qq(<script type="text/javascript" language="javascript" src="$main::fBz"></script>); 

$max_content_length=1024*1024*24; ## 24 Meg, maximum message size

$pop_logon_retry_time = 15;

#map domain in email address to pop3 server name, in case they are different


%fix_port_cgi_url=(); #use this to map eE to cgi url

$anyemail_msg_tag = "Email sent using AnyEmail (http://netbula.com/anyemail/)";

binmode STDOUT;

$msg_per_page=40;                 ## display this many message per page
$no_attachment_sending = 0; ## set this to 1 will disable attachment sending
$show_reply_form_on_msg = 0; ## put reply form on the message page
$dont_show_title = 0;     ##don't show email address in title
$short_mail_list = 1;     ## set this to 1 to narrow the mail list window
$SUB_TRUNCATE_LIM = 64; ## truncate subject display on message list to 64
$NAME_TRUNCATE_LIM = 24; ## truncate from address display on message list to 64

%mail_stats=(
RO=>"Read",
R=>"Read",
O=>"Old",
N=>"New",
U=>"Unread",
);


$style_text =<<"EOF_STYLE";
<style type="text/css">
<!--
A {FONT-FAMILY: Verdana, Helvetica, Arial; FONT-STYLE: normal; FONT-VARIANT: normal; TEXT-DECORATION: none;  font-weight: bold}
HTML  { font-size: 9pt; COLOR: #000000; FONT-FAMILY: Verdana, Helvetica, Arial; FONT-STYLE: normal; FONT-VARIANT: normal; TEXT-DECORATION: none  }
a:hover 	{ text-decoration: underline;}
.inputfields { COLOR: #666666; FONT-WEIGHT: bold; BACKGROUND-COLOR: #ffffff; FONT-FAMILY: Verdana, Helvetica, Arial; BORDER-BOTTOM: #666666 thin solid; BORDER-LEFT: #666666 thin solid; BORDER-RIGHT: #666666 thin solid; BORDER-TOP: #666666 thin solid  }
.topnav { FONT-SIZE: 10pt; font-weight: bold}
.topnav:hover { BACKGROUND-COLOR: #6699cc; BORDER-BOTTOM: #666666 thin solid ; BORDER-LEFT: #666666 thin solid ; BORDER-RIGHT: #888888 thin solid ; BORDER-TOP: #777777 thin solid; COLOR: #ffcc00;  FONT-SIZE: 10pt; font-weight: bold}
TD { font-size: 9pt; }
BODY {margin-top: 0px; margin-left:1px}
.buttonstyle  { BACKGROUND-COLOR: #5a5a5a; BORDER-BOTTOM: #666666 thin solid ; BORDER-LEFT: #666666 thin solid ; BORDER-RIGHT: #888888 thin solid ; BORDER-TOP: #777777 thin solid; COLOR: #cccccc;  FONT-SIZE: 9pt; font-weight: bold}
.buttonstyle_n  { BACKGROUND-COLOR: #610000; BORDER-BOTTOM: #666666 thin solid ; BORDER-LEFT: #666666 thin solid ; BORDER-RIGHT: #888888 thin solid ; BORDER-TOP: #777777 thin solid; COLOR: #ffffff;  FONT-SIZE: 9pt; font-weight: bold}
DIV.aemsgbody { font-size: 9pt; font-family: "Arial, Helvetica, sans-serif"; margin-right:80px;}
small { font-size: 9pt; font-family: "Arial, Helvetica, sans-serif"}

-->
</style>
EOF_STYLE


$exit_msg =<<"END_OF_EXITMSG";  ## html code to send when user logout
<html><head><META HTTP-EQUIV="refresh" CONTENT="5; URL=http://netbula.com">
<title>Logout</title>
</head><body bgcolor="$body_bg_color">
<table align=center width=300><tr><td height=150>&nbsp;</td></tr><tr><td>
<h1>Thank you for using AnyEMail. Bye bye!</h1>
<h1>LOGOUT_ALL_LNK</h1>
</td></tr></table></body></html>

END_OF_EXITMSG


$top_win_layout_top_down =<<"EOF_OF_LAYOUT"; #see online user guide 
<frameset cols="160,*" border="1" marginwidth=0>
          <frame name="aM" src="COMMAND_SRC_URL" border=1>
<frameset rows="40%,*" border="1" marginwidth=0>
          <frame name="list" src="LIST_SRC_URL" border=1>
          <frame name="msg" src="HELP_SRC_URL" border=1>
       </frameset>
</frameset>
</frameset>
EOF_OF_LAYOUT


$top_win_layout_left_cmd =<<"EOF_OF_LAYOUT"; #see online user guide 
<frameset cols="160,*" border="1" marginwidth=0>
          <frame name="aM" src="COMMAND_SRC_URL" border=1>
          <frame name="msg" src="LIST_SRC_URL" border=1>
       </frameset>
</frameset>
EOF_OF_LAYOUT

$cmd_panel_footer=<<"EOF_CMD_FOOT";
<p>Powered by <a href="http://netbula.com/anyemail" target=_top>AnyEmail</a>
EOF_CMD_FOOT

$list_win_header=<<"EOF_LIST_HEAD";
<!-- Put ad 1 here</small> -->
EOF_LIST_HEAD

$list_win_footer=<<"EOF_LIST_FOOT";
<!-- <small>Put ad 2 here</small><p> -->
EOF_LIST_FOOT

$msg_body_header=<<"EOF_MSG_HEAD";
<!--<small>Put ad 3 here</small><p> -->
EOF_MSG_HEAD

$msg_body_footer=<<"EOF_MSG_FOOT";
<!--
<small>Put ad 4 here</small><p>
<small>Put ad 5 here</small><p>
-->
EOF_MSG_FOOT


$addusercmd="/usr/sbin/adduser";

}

###############CUT THE LINES ABOVE AND SAVE IT AS YOUR CONFIGURATION###

############# do not edit aCz below  #################################

$DO_NOT_EDIT_STARTING_HERE =<<'COPY_RIGHT_TEXT';
/################################################################
/# Copyright (C) Netbula LLC, 1998-2000, All rights reserved.
/# Use of this software without a license is prohibited.
/# Unauthorized modification of the code below is also prohibited.
/# For more information visit http://netbula.com/anyemail/
/################################################################
COPY_RIGHT_TEXT


#IF_AUTO use lib ABMODDIR;
#IF_AUTO use hSz;
#IF_AUTO use main;
#IF_AUTO use aVz;
#IF_AUTO use dH;
#IF_AUTO use kGz;
#IF_AUTO use jZz;
#IF_AUTO use kWz;
#IF_AUTO use dF;
#IF_AUTO use gOz;
#IF_AUTO use hVz;
#IF_AUTO use CSVText;



BEGIN{

$eO=0;
$fFz="";
$bOz="";

$cHz =<<'XYZK7';

XYZK7

$pop_win_str= qq@
<script language=javascript>
<!--
function set_check(f, val) {
  for(var i=0; i< f.elements.length; i++) {
    var e = f.elements[i];
    if(e.type=="checkbox") e.checked = val; 
  }
}
function get_chk_cnt(f) {
  var l=0;
  for(var i=0; i< f.elements.length; i++) {
    var e = f.elements[i];
    if(e.type=="checkbox" && e.checked && e.name != "") l++; 
  }
  return l;
}
//-->
</script>
@;

$eAz= $pop_msg? qq! onclick="dGz(this.href, 'popwin', 0.7,0.7,'yes');return false;"!:"";

@mfs = qw(From To Cc Subject Date size Status Received Importance xMbox Content-type ret_time);

@gE=();
%g_mhlist_by_type = ();
@aP = qw(From To);

%dZz=(Subject=>"Subject", From=>"Sender", Date=>"Date", size=>"Size", Status=>"Status", To=>'Recipient');

%ecodes = (
miss=>[	"Missing required field",
	"You did not fill in one or more required fields in the form submission.", 
	"Go back and complete the information and then resubmit."],

too_long=>["Field too long",
	"One of the fields exceeded limit.",
	"Go back, reduce the field length and then resubmit."],

violate=>["Rule violation",
	"You violated the rules imposed by this forum!",
	"Please read the rules again and cooperate. Thank you!"],

inval =>["Input rejection", "The information or command you sent was rejected",
         "Go back to the previous page and make corrections. Please see the detailed error message for explanation."],    
deny    => ["Access denied!", "Sorry!", "Sorry!"],

fail_auth => ["Fail to authenticate!", 
	"Missing or invalid authentication information.", 
	"Provide the correct authentication info and retry."],

aE=> ["No cookie!", 
	"Your browser did not send the expected cookie!", 
	"Use a browser that supports cookie and enable cookie. This error could also be due to the expiration of the trial license (see http://netbula.com/sales/ ) " ],

'sys'=>	["System error", 
	"Error caused by invalid URL, incorrect setup, incorrect permission setting, etc.", 
	"Notify webmaster with the detailed error message."
	],
);

@jTz= (
[display_info=>"head", "Enter or modify license key"],
[k=>"text", "size=48", "License key", ""],
[s=>"text", "size=32", "Password for modifying license key", ""],
[aM=>"command", "", "", "jUz"],
);

@addressbook= (
[display_info=>"head", "Add or modify address book entry"],
[name=>"text", "size=32", "Name", ""],
[email=>"text", "size=32", "E-Mail", ""],
[url=>"text", "size=60", "Home page URL", ""],
[phone=>"text", "size=20", "Phone number", ""],
[mphone=>"text", "size=20", "Mobile phone", ""],
[company=>"text", "size=48", "Company", ""],
[address=>"textarea", "rows=4 cols=60", "Address", ""],
[desc=>"textarea", "rows=2 cols=60", "Comments", ""],
[fO=>"checkbox", "", "In group", ""],
[id=>"hidden", "", "Address entry id"],
[aM=>"command", "", "", "gKz"],
);

@nDz=(
[display_info=>"head", "Import addresses"],
[addlistfile=>"file", "size=32", "File", ""],
[aM=>"command", "", "", "nEz"],
);


@add_user_form=(
[display_info=>"head", "New user information"],
[userid=>"text", "size=20", "User ID", ""], 
[realname=>"text", "size=20", "Real name", ""], 
[password=>"password", "size=20", "Password", ""], 
[password2=>"password", "size=20", "Re-type password", ""], 
[secret_key=>"hidden", "", "key"],
[aM=>"command", "", "", "kDz"],
);

@mod_user_form=(
[display_info=>"head", "Moidfy user information"],
[userid=>"text", "size=20", "User ID", ""], 
[realname=>"text", "size=20", "Real name", ""], 
[old_password=>"password", "size=20", "Old password", ""], 
[password=>"password", "size=20", "Password", ""], 
[password2=>"password", "size=20", "Re-type password", ""], 
[secret_key=>"hidden", "", "key"],
);

@personsettings= (
[display_info=>"head", "Personal settings"],
[name=>"text", "size=32", "Real name", ""],
[replyaddr=>"text", "size=32", "Reply-to address"],
[phone=>"text", "size=20", "Phone number", ""],
[mphone=>"text", "size=20", "Mobile phone", ""],
[signat=>"textarea", "rows=4 cols=30", "Email signature", ""],
[url=>"text", "size=60", "Home page URL", ""],
[dspinf=>"head", "Address group settings"],
[mlist_set=>"textarea", "rows=5 cols=30", "Address groups. One per line, in the format, id=description, where id must not contain spaces", "personal=Personal contacts\nbiz=Business contacts"],
[dspinf2=>"head", "Filter settings"],
[good_pat=>"text", "size=50", "Accept From address which match this pattern as good mail (separate entries by |)", ""],
[good_sub_pat=>"text", "size=50", "Accept subjects which match this pattern as good mail (separate entries by |)", ""],
[junk_pat=>"text", "size=50", "Mark email which match this pattern as junk mail (separate entries by |)", "junkmail.com|spam.com"],
[block_pat=>"textarea", "rows=4 cols=40", "Mark the following SMTP servers as junk mailer (separate entries by space)", "junkmail.com spam.com"],
[markbulk=>"checkbox", "1=Yes", "Automark bulk mail for deletion", 0],
[mv_on_del=>"checkbox", "1=Yes", "Move messages to trash folder when delete", 1],
[dspinf3=>"head", "Interface settings"],
[fancyhtml=>"checkbox", "1=Yes", "Use WYSIWYG HTML editing for IE", 1],
[rm_html_in_reply =>"checkbox", "1=Yes", "Remove HTML tags when reply", 1],
[default_charset =>"text", "size=16", "Default charset (Examples: iso-8859-1, gb2312, big5, latin2, iso-8859-5, euc-kr, euc-jp )", "$default_charset"],
[displayhdrs=>"text", qq(size=60), "Displayed mail fields and order.<br>Available fields: ".join(" ", @bT), "Subject From Date size Status"],
[ae_config=>'select', ""],
[aM=>"command", "", "", "kEz"],
);

}


package main;


sub anyemail_run {

$ae_cfg_dir = eCz($anyemaildir, "config"); #path to config dir
$mailing_list_dir= eCz($anyemaildir, "mailinglist");
$alias_map_dir= eCz($anyemaildir, "aliases"); 
$abook_dir= eCz($anyemaildir, "addresses"); 
$ae_licfile= eCz($anyemaildir, "addresses", ".z"); 
$ae_logfile = eCz($anyemaildir, "anyemail.log"); #path to log file  


$cJ=undef;
$dD=undef;
$g_popuser=undef;
$g_use_email_as_id = undef;
$cJz=undef;
$aN=undef;
$cKz=undef;
$bC=undef;
$cU=undef;
$cJz=undef;
$dPz=undef;
$g_cook_val=undef;
$eO=undef;
$cPz=undef;
$cLz=undef;
$bSz=undef;
$g_perseronal = undef;

undef @cWz;
undef %bYz;
undef %dJz;
undef %eFz ;
undef %eVz;

bD();
cT();
bQz();


&bS;

$xfile = eCz($abook_dir, "._"); #path to log file  

$fixed_pop_server=$serv if $fixed_pop_server eq "your-domain";    
$fixed_return_domain= $serv if $fixed_return_domain eq "your-domain";   

$aM = $bYz{aM};
dIz();
if($aM eq 'log') {
	aU(1);
	main::cXz();
}

if(!$aM) {
      if($no_pop_win) {
	&aU();
	main::cXz();
      }else {
	eOz();
	main::cXz();
      }
}

%aNz = (
   login => ['BOTH', \&aC, 'ADM'],
   sinfo => ['BOTH', \&kSz, 'ADM'],
   plog => ['BOTH', \&aU, 'ADM'],
   logout => ['BOTH', \&cP, 'ADM'],
   reply =>["BOTH", \&aD, 'ADM'],
   recompose=>["BOTH", \&nSz, 'ADM'],
   dM=>["BOTH", \&bJ, 'ADM'],
   dRz=>["BOTH", \&bI, 'ADM'],
   bP=>["BOTH", \&bV, 'ADM'],
   cUz =>["BOTH", \&eEz, 'ADM'],
   dLz =>["BOTH", \&dYz, 'ADM'],
   cZz=>["BOTH", \&eRz, 'ADM'],
   list =>["BOTH", \&cQ, 'ADM'],
   nMz =>["BOTH", \&nNz, 'ADM'],
   hXz =>["BOTH", \&hXz, 'ADM'],
   choose_addr =>["BOTH", \&choose_addr, 'ADM'],
   nCz =>["BOTH", \&nCz, 'ADM'],
   nEz =>["BOTH", \&nEz, 'ADM'],
   nDz =>["BOTH", \&nDz, 'ADM'],
   mYz =>["BOTH", \&mYz, 'ADM'],
   fYz=>["BOTH", \&fYz, 'ADM'],
   add_user_form=>["BOTH", \&add_user_form, 'ADM'],
   kDz=>["BOTH", \&kDz, 'ADM'],
   gKz=>["BOTH", \&gKz, 'ADM'],
   kLz=>["BOTH", \&kLz, 'ADM'],
   kEz=>["BOTH", \&kEz, 'ADM'],
   kJz=>["BOTH", \&kJz, 'ADM'],
   hGz=>["BOTH", \&hGz, 'ADM'],
   del =>["BOTH", \&aB, 'ADM'],
   deltrash =>["BOTH", \&handle_empty_trash, 'ADM'],
   mdel =>["BOTH", \&aB, 'ADM'],
   forward=>["BOTH", \&cC, 'ADM'],
   panel=>["BOTH", \&aQ, 'ADM'],
   bBz=>["BOTH", \&aXz, 'ADM'],
   compose=>["BOTH", \&cO, 'ADM'],
   hdr=>["BOTH", \&eI, 'ADM'],
   lSz=>['GET', \&lFz], 
   lico=>["BOTH", \&gNz, "ADM"],
   lic=>["BOTH", \&jEz, "ADM"],
   jUz=>["BOTH", \&jCz, "ADM"],
   split=>['BOTH', \&hEz]
);

my $aOz = $aNz{$main::bYz{aM}};


if($aOz) {
    my $eBz = $aOz->[1];
    &$eBz;
    main::cXz();
}elsif($cN ne 'POST') {
   error('What?', "Unknown or disabled command");
   main::cXz();
}else {
   error('What?', "Unknown or disabled command");
   main::cXz();
}

}


sub rm_htmltag{
   my $nref = shift;
   #$$nref =~ s{<!(.*?)(--.*--\s*)+.(.*?)>}{if($1||$3) {"<!$1 $3>";}}ges;
   $$nref =~ s/<!--.*?-->//gs;
   $$nref =~ s#<(!|[a-zA-Z]|/)[^>]*>##gs;
}

sub cXz {
    my $code = shift;
   if($ENV{GATEWAY_INTERFACE} =~ /^CGI-Perl/ || exists $ENV{MOD_PERL}) {
      undef %bYz;
      undef %dJz;
      undef %eFz;
      if($pop) {
		$pop->Close();
		$pop = undef;
     }
      Apache::exit($code);
   }else {
      exit;
   }
}

sub dIz{
	if($no_frames) {
		$list_tgt = "_self"; 
		$msg_tgt = "list";  
	        $pop_msg = 1; #set to 1  pop window when viewing message
	}elsif(not $left_panel){
		$list_tgt = "msg"; 
		$msg_tgt = "msg";  
	        $pop_msg = 0; #set to 0 to disable pop window when viewing message
		$top_win_layout = $top_win_layout_left_cmd;
	}else {
		$list_tgt = "list"; 
		$msg_tgt = "msg";  
	        $pop_msg = 0; #set to 0 to disable pop window when viewing message
		$top_win_layout = $top_win_layout_top_down;

        }
	$eAz= $pop_msg? qq! onclick="dGz(this.href, 'popwin', 0.7,0.7,'yes');return false;"!:"";

}

sub set_font{
    my ($str, $font)=@_;
    return $str if not $font;
    return qq(<font $font>$str</font>);
}
	
sub spell_btn {
    my %langs=( "en" , "English", "uk" , "British", "fr" , "French", "ge" , "German", "it" , "Italian",
     "sp" , "Spanish", "dk" , "Danish", "br" , "Brazilian", "nl" , "Dutch", "no" , "Norwegian",
     "pt" , "Portuguese", "se" , "Swedish", "fi" , "Finnish");
    my ($f, $msg) = @_;
    return qq!<INPUT TYPE="BUTTON" VALUE= "SpellCheck" onclick= "doSpell($f.spelllang.options[$f.spelllang.selectedIndex].value, $f.$msg, document.location.protocol+'//'+document.location.host+'$main::spellcgi', true);"> 
              <select name=spelllang>!. join ("", map { qq(<option value="$_" @{[$_ eq 'en'? 'SELECTED':""]}>$langs{$_}) } sort keys %langs )."</select>";
}

sub eTz {   
    my $str = shift;
    return "" if not $str;
    $str =~ s/([" %&+<=>'\r\n])/sprintf '%%%.2X' => ord $1/eg;
    return $str;
}

sub ePz{
     my $v = shift;
     $v =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/chr(hex($1))/ge;
     return $v;
}

sub encode_fn{   
    my $str = shift;
    return "" if not $str;
    $str =~ s/(\W)/sprintf '%%%.2X' => ord $1/eg;
    return $str;
}

sub eZz{
    my $str = shift;
    my $maxlen = shift;
    my $len = length($str);
    return $str if $len <= $maxlen;
    return substr($str, 0, $maxlen -3)."...";
}

sub eCz{
    my ($root, @dSz)= @_;
    for(@dSz) {
        $_ =~ s#^/*##;
        $root =~ s#/*$#/#;
        $root .= $_; 
    }
    return $root;
}

sub bNz{
    my @eSz = @_;
    for (@eSz) {
      s/\n/ /g;
      s/\t//g;
    }
    open F, ">>$ae_logfile"; 
    print F join ("\t",time(), $ENV{REMOTE_ADDR}, @eSz), "\n";
    close F;
}

sub log_debug{
     my @eSz = @_;
    open F, ">>$debug_log"; 
    print F join ("\t",time(), $ENV{REMOTE_ADDR}, @eSz), "\n";
    close F;
}

###################FUNCTIONS ########################


sub cT {
    my($in) ;
    my ($name, $value) ;
    my @dQz;
                     log_debug("Enter get cgivars\n") if $debug;

    if ( ($ENV{'REQUEST_METHOD'} eq 'GET') || ($ENV{'REQUEST_METHOD'} eq 'HEAD') ) {
        $in= $ENV{'QUERY_STRING'} ;
        $cN="GET";
    } elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
           length($ENV{'CONTENT_LENGTH'})
                || &error('sys', "No Content-Length sent with the POST request.") ;
            my $len = $ENV{'CONTENT_LENGTH'};
            my $cnt=0;
            $cN="POST";
            my $buf;
            &error('inval', "Content-Length exceeded limit.") if $len > $max_content_length;
            if ($ENV{'CONTENT_TYPE'}=~ m#^application/x-www-form-urlencoded$#i) {
                while($len > 0) {
                     log_debug("$len bytes left\n") if $debug;
                     $cnt = read(STDIN, $buf, $len);
                     last if $cnt<=0 || not $cnt;
                     push @dQz, $buf;
                     $len -= $cnt;
                }
                log_debug("got all bytes \n") if $debug;
                $in = join('', @dQz);
            }elsif($ENV{'CONTENT_TYPE'}=~ m#^multipart/form-data#i) {
                binmode STDIN;
                while($len >0 ) {
                     log_debug("$len bytes left\n") if $debug;
                     $cnt = read(STDIN, $buf, $len);
                     last if $cnt <=0 || not $cnt;
                     push @dQz, $buf;
                     $len -= $cnt;
                }
                log_debug("got all bytes, $len \n") if $debug;
                $in = join('', @dQz);
                my @plines = split /^/m, $in;

                my $mime = new aVz(\@plines);
                $mime->{head}->{'content-type'} = $ENV{'CONTENT_TYPE'}; 
                $mime->aYz();
                $mime->aZz();
		my $aJz;
                for $aJz(@{$mime->{aFz}}) {
                    my $name= $aJz->{bHz};
                    my $val = $aJz->aWz();
                    if (length($aJz->{bFz})>0) {
                      $main::dJz{$name} = [$aJz->{bFz}, $val, $aJz->{head}->{'content-type'}];
                    } else {
    	              $main::bYz{$name} .= "\0" if defined($main::bYz{$name}); 
    	              $main::bYz{$name} .=  $val;
                    }
                }
                    
            }
    } else {
        &error('sys',"Script was called with unsupported REQUEST_METHOD $ENV{REQUEST_METHOD} $ENV{CONTENT_TYPE}.") ;
    }
    if ($cN eq 'GET'  || $ENV{'CONTENT_TYPE'}=~ m#^application/x-www-form-urlencoded$#i) {
    	foreach (split('&', $in)) {
    	    s/\+/ /g ;
    	    ($name, $value)= split('=', $_, 2) ;
    	    $name=~ s/%(..)/chr(hex($1))/ge ;
    	    $value=~ s/%(..)/chr(hex($1))/ge ;
    	    $main::bYz{$name}.= "\0" if defined($main::bYz{$name}) ; 
    	    $main::bYz{$name}.= $value ;
    	}
    }
}

sub bS {
    my $eE = $ENV{SERVER_PORT};
    $serv = $ENV{SERVER_NAME};
    $bL = $ENV{PATH_INFO};
    $bL =~ s#^/?#/#;
    $bL =~ s#/?$#/#;
    my $proto = lc((split /\//, $ENV{SERVER_PROTOCOL})[0]);
    my $aIz = $proto."://$serv";
    if($eE != 80) {
          $aIz .= ":$eE";
    }
    $xad =  unpack("u*", $cHz) unless 1==bTz($bOz);
    $aIz = $aLz if $aLz;
    if($proto eq 'http' && $fix_cgi_url) {
        $cgi_url_full = $bA = $fix_cgi_url;
    }elsif ($eE != 80 && $fix_port_cgi_url{$eE}){
        $bA = $fix_port_cgi_url{$eE};
    } else{
        $bA = $ENV{SCRIPT_NAME};
        $cgi_url_full = $aIz. $ENV{SCRIPT_NAME};
	if($^O =~ /win/i) {
        	$bA = $cgi_url_full;
	}
    }
    $cgi_url_full = $bA if not defined($cgi_url_full);
    error() if not $bA =~ /anyemail/i;
    $agent = $ENV{'HTTP_USER_AGENT'}.$ENV{'HTTP_USERAGENT'};

}

sub gQ {
   my ($url, $str, $tgt) = @_;
   $str = $url if !$str;
   my $cls = qq( class="$link_class") if $main::link_class;
   return qq(<a href="$url" target="$tgt" $action$cls>$str</a>) if $tgt;
   return qq(<a href="$url" $action$cls>$str</a>);
}

sub jQz{
   my ($p, $s) = @_;
   return "" if not $p;
   $s = "ne";
   return crypt($p, $s);
}




#IF_AUTO BEG_AUTO_FUNC
sub AUTOLOAD {
    my($func) = $AUTOLOAD;
    my($pack,$func_name) = $func=~/(.+)::([^:]+)$/;

    my($sub) = \%{"$pack\:\:bZz"};
    unless (%$sub) {
        my($auto) = \${"$pack\:\:AUTOLOADED_ROUTINES"};
        eval "package $pack; $$auto";
        main::error('sys', "$AUTOLOAD: $@") if $@;
    }
    my($code) = $sub->{$func_name};

    $code = "sub $AUTOLOAD { }" if (!$code and $func_name eq 'DESTROY');
    main::error('sys', "Undefined subroutine $AUTOLOAD\n") unless $code;
    eval "package $pack; $code";
    if ($@) {
        $@ =~ s/ at .*\n//;
        main::error('sys', "$AUTOLOAD: $@");
    }
    $main::func_cnt++;
    goto &{"$pack\:\:$func_name"};
}
#IF_AUTO BEG_AUTO_FUNC

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__

sub eR {

   return  $eR=<<JS_CODE_END;
<SCRIPT language="JavaScript">
<!--//
var hon_pos=-1;
var qon_pos=-1;
if (document.images) {
    fM = new Image();     fM.src = "$fN";
    fL = new Image(); fL.src = "$fQ";
    fB = new Image();  fB.src = "$fS";
    eS = new Image(); eS.src = "$fR";
    del = new Image(); del.src = "$del_src";
}

function offdel(img) {
    img.src = del.src;
}
function qon(index) {
        if (document.images) {
                if(hon_pos != index) {
                	code = 'document.image_'+index+'.src = fM.src';
			eval(code);
                	qon_pos = index;
                }
        }
}
function qoff(index) {
       if(index == hon_pos) return;
       code= 'document.image_'+index+'.src = fL.src';
       eval(code);
       qon_pos = -1;
}
       

function hon(index) {
        if (document.images) {
                if(hon_pos >=0){
                	code = 'document.image_'+hon_pos+'.src = fL.src';
                        eval(code);
                }
                hon_pos=index;
               	code = 'document.image_'+hon_pos+'.src = fB.src';
                eval(code);
        }
}
var ab_newin=null;
function dGz(myurl, myname, w, h, scroll) {
w=(screen.width)?screen.width*w: 620;
h=(screen.height)?screen.height*h:420;
LeftPos=(screen.height)?screen.width/2-w/2+50:0;
TopPos=(screen.height)?200:0;
settings='height='+h+',width='+w+',top='+TopPos+',left='+LeftPos+',scrollbars='+scroll+',resizable';
if(ab_newin==null || ab_newin.closed) {
	ab_newin=window.open(myurl, myname, settings);
}else {
	ab_newin.location=myurl;
}
ab_newin.focus();
}
// -->
</SCRIPT>
JS_CODE_END

}

sub test_pattern{
	my $pat = shift;
	return 1 if $pat eq "";
	my $ok1 = eval { "" =~ /$pat/; 1};
	return if not $ok1;
	return ('a' =~ /$pat/)? 0: 1;
}

sub hEz {
    my $ofile1 = eCz($main::anyemaildir, "anyemail_auto.cgi");
    my $ofile2;
    if (-w $0) {
       $ofile2 = $0."_split";
    }
    gMz($0, eCz($main::anyemaildir, "aelib"), $ofile2, $ofile1);
}

sub lFz{
    print "Content-type: application/x-javascript\n\n";
    $main::agent = $ENV{'HTTP_USER_AGENT'};
    my $mMz = ($main::agent =~ /MSIE\s*(5\.5|6)/i);
    print hSz::lJz($main::bYz{mHz}) if ($mMz && $ENV{HTTP_REFERER}=~/any/);
}

sub gMz {
 eval 'use AutoSplit';
 my ($gK, $modd, $outfile, $altf) = @_;

open F, "<$gK" or error("Can't open script $gK: $!");
my @jPz = <F>;
close F;

if (not -d $modd) {
  	mkdir $modd, 0755 or error("Can't make dir $modd: $!");
}
my $modauto = eCz($modd, "auto");
if (not -d $modauto) {
	mkdir $modauto, 0755 or error("Can't make dir $modauto: $!");
}

my $all= join("", @jPz);

error('inval', "Can't split the code") if not $all =~ /#IF_AUTO/; 

study $all;

print "Content-type: text/html$charset_str\n\n";
print "<html><body><h1>To complete, you must replace the original script with the generated short script after a successful split!!</h1><pre>";

$all =~ s/^.*##SUB_LIST.*$//gm;
$all =~ s/^bLz$//gm;
$all =~ s/^.*'bLz'.*$//gm;
$all =~ s/^END_OF_AUTOLOAD$//gm;
$all =~ s/^.*'END_OF_AUTOLOAD'.*$//gm;

$all =~ s/^#IF_AUTO\s+//gm;

$all =~ s/ABMODDIR/"$modd"/g;

my @mods = split /(^package\s+.*;$)/m, $all;
my $main = shift @mods;
while(@mods) {
       my $mSz = shift @mods;
       my $code = shift @mods;
       $code =~ s/^BEG_AUTO_FUNC.*?^BEG_AUTO_FUNC//sm;
       $mSz =~ /package\s+(.*);/;
       my $pkn = $1;
       my $pk = eCz($modd, "$pkn.pm");
       open F, ">$pk";
       print F $mSz, "\n", $code;
       close F;
       print "Saving modules $pkn.pm\n";
       AutoSplit::autosplit("$pk", "$modauto");
       print "Split modules $pkn.pm\n";
   
       open F, ">$pk";
       print F $mSz, "\n", $code;
       close F;
} 

my $use_alt=0;
if($outfile && open (F, ">$outfile")) {
}else {
    $outfile = $altf;
    open F, ">$outfile" or error("On open $outfile: $!");
    $use_alt = 1;
}
print F $main;
close F;
chmod 0755, $outfile;
print "</pre>";
print "The has been split into smaller files.<br/>";
print "But, you are not done yet, the split command does not change the original script ($0)<br/>";
print "the new main script was written to<br/>   <b>$outfile</b><br/>you need to rename it to $0 manually\n";
print qq(<hr/><a href="javascript:history.go(-1)">Go back</a></body></html>);

}


BEGIN{ ##SUB_LIST

$AUTOLOADED_ROUTINES = '';     
$AUTOLOADED_ROUTINES=<<'END_OF_AUTOLOAD';

%bZz = ( ##SUB_LIST

bUz =><<'bLz',
sub bUz{
    my ($aGz, $cA, $curlev, $gK, $no_table, $disp_attach, $shownref) = @_;
    my @str;

    my $look_for_best=0;
    
    if($aGz->{head}->{'content-type'} =~ m!multipart/alternative!i) {
    	$look_for_best=1;
    }
	
    if (@{$aGz->{aFz}}) {     
        my $i=0;
	my @aFz;
	if($look_for_best) {
          for(@{$aGz->{aFz}}) {     
	    if($_->{head}->{'content-type'} =~ m!text/html!i) {
		unshift @aFz, $_;
	    }else {
		push @aFz, $_;
	    }
	  }
	}else {
           @aFz = @{$aGz->{aFz}};  
	}
        for(@aFz) {
	    push @str, bUz($_, $cA, "${curlev}_$i", $gK, $no_table, $disp_attach, $shownref);
            $i++;
	}
    	return join ('', @str);
    }
    my ($type, $bGz) = split('/', $aGz->{head}->{'content-type'});
    my $inline = $aGz->{head}->{'content-disposition'} =~ /inline;/i || 0;

    if( (not $aGz->{head}->{'content-disposition'}) && $type eq 'image') {
	$inline =1;
    }
    
    $bGz = (split(';', $bGz))[0];
    my $bFz = $aGz->{bFz} || $aGz->{bHz};
    return if $gK && $gK ne $curlev;

    if ($gK) {
	        my $attach = $disp_attach;
	
              	push @str, "Content-Type: ". $aGz->{head}->{'content-type'}. qq(; filename="$bFz"\n);
		if($bGz eq 'msword' || $type eq 'application' ){
			$attach =1;
                }
		if($attach) {
			push @str, qq(Content-Disposition: attachment; filename=$bFz\n);
		}
		push @str, "\n";
            	push @str, $aGz->aWz();
    		return join ('', @str);
    }

    my $shown_body=0;
    if(not $$shownref) {
      if (($type=~ /^text$/i && ($bGz =~ /^plain/i || $bGz =~/html/i || $inline) ) || (lc($type) eq  'message') ) {  
    	    my $d = $aGz->aWz();
	    if(length($d) < 400*1024) {
		if($bGz !~ /html/i) {
			$d = qq(<pre WRAP="soft" style="pre-wrap:break-word">\n$d\n</pre>);
		}
            	push @str, $d;
            	$shown_body=1;
		$$shownref=1;
	    }
      }
    }

    if($bFz || not $shown_body){
           
         if($cA >=0) {
    	    	my $d = $aGz->aWz();
		my $kb = length($d)/1024;
                
		$inline = 0 if $kb > 200;
		my $kbstr= sprintf ("%.2fk", $kb);

    	        push @str, qq(<br><br><table border=1 cellpadding=5 bgcolor="#efefff"><tr><td align=center>);
                $bFz =~ s/\s/_/g;
		$bFz =~ s#^.*/##g;
		$bFz =~ s#^.*\\##g;
                $bFz =~ s/\?|\&//g;

		my $fn = $bFz;
                $bFz = encode_fn($bFz);
             if($broke_pathinfo) {
               if($inline && $type eq 'image' ) {
    	         push @str, '', qq(<img src="$bA?aM=cUz\&gK=$curlev\&cA=$cA\&cKz=$cKz\&type=$type\&bGz=$bGz\&file=$bFz" alt="$bFz">); 
               }else{
    	         push @str, gQ(qq($bA?aM=dLz\&gK=$curlev\&cA=$cA\&cKz=$cKz\&type=$type\&bGz=$bGz\&file=$bFz), "View", ""); 
    	         push @str, '&nbsp;&nbsp;&nbsp;', gQ(qq($bA?aM=cUz\&gK=$curlev\&cA=$cA\&cKz=$cKz\&type=$type\&bGz=$bGz\&file=$bFz\&issave=1), "Save", ""); 
               }
             }else {
               if($inline && $type eq 'image' ) {
    	         push @str, qq(<img src="$bA/$bFz?aM=cUz\&gK=$curlev\&cA=$cA\&cKz=$cKz\&type=$type\&bGz=$bGz\&file=$bFz"); 
               }else {
		if($pop_attachment) {
    	         push @str, gQ(qq($bA/$bFz?aM=cUz\&gK=$curlev\&cA=$cA\&cKz=$cKz\&type=$type\&bGz=$bGz\&file=$bFz), "View", ""); 
		}else {
    	         push @str, gQ(qq($bA/$bFz?aM=dLz\&gK=$curlev\&cA=$cA\&cKz=$cKz\&type=$type\&bGz=$bGz\&file=$bFz), "View", ""); 
		}
    	         push @str, '&nbsp;&nbsp;&nbsp;', gQ(qq($bA/$bFz?aM=cUz\&gK=$curlev\&cA=$cA\&cKz=$cKz\&type=$type\&bGz=$bGz\&file=$bFz\&issave=1), "Save", ""); 
               }
             }
    	        push @str, "<br><b>". $fn." [ $kbstr ] </b><br>"; 
    	        push @str, "( $type/$bGz )", "<br>"; 
    	        push @str, "</td></tr></table>";
          } else {
                 push @str, "\n\n", "Attachment: ", $aGz->{bHz}, 
                            $aGz->{bFz},"\n", $aGz->bEz(), "\n";
          }
    }

    return join ('', @str);
}

bLz

cW =><<'bLz',
sub cW {
   my( $format, $li, $op) = @_;
   my $t;
   if($op eq "CONV") {
          $t = $li;
   } else {
          $t = time() + $li;
   }

   my($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($t);
   my $mon_num = $mon+1;

   my @dT = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
   my @wdays  = qw(Sun Mon Tue Wed Thu Fri Sat);

   $mon = $dT[$mon];
   $wday = $wdays[$wday];

   $sec = "0$sec" if $sec<10;
   $hour = "0$hour" if $hour<10;
   $min = "0$min" if $min<10;
   $mday = "0$mday" if $mday<10;
   $mon_num  = "0$mon_num" if $mon_num<10;
   $year+=1900;
   my $dstr= "$wday, $mday-$mon-$year $hour:$min:$sec";

   if($format eq 'COOK') {
           return "$dstr GMT";
   }
   if($format eq 'LONG') {
           return "$wday, $mon $mday, $year, $hour:$min:$sec";
   }

   if($format eq 'DAY') {
           return "$mday-$mon-$year";
   }

   if($format eq 'DAY2') {
           return "$year/$mon_num/$mday";
   }

   if($format eq 'DAY3') {
           return "$year-$mon_num-$mday, $hour:$min:$sec, $wday";
   }

   return "$mon $mday,$year,$hour\:$min";

}


bLz

aW =><<'bLz',
sub aW {
    my($name, $val, $path, $exp) = @_;
    if($exp) {
    	return "Set-Cookie: $name=$val; expires=$exp; path=$path\n";
    }else {
    	return "Set-Cookie: $name=$val; path=$path\n";
    }
}

bLz

bD =><<'bLz',
sub bD {
   my($name, $val);
   foreach (split (/; /, $ENV{'HTTP_COOKIE'})) {
       ($name, $val) = split /=/;
       $eFz{$name}=$val;
   }
}

bLz

eM =><<'bLz',
sub eM {
    my @dBz = split (':', $eFz{xinxiang});
    #bNz('cook=', $eFz{xinxiang});
    for(@dBz) {
      next if not /\w+/;
      push @cWz,[(split /\&/, $_)] ;
    }
    return @cWz;
}

bLz

eL =><<'bLz',
sub eL{
    my ($ne, $cfg) = @_;
    my @mZz;
    push @mZz, [$ne, $cfg];
    foreach (@cWz) {
          next if lc($ne) eq $_->[0];
          push @mZz, $_;
    }
    $#cWz=0;
    @cWz = @mZz;
}

bLz

eN =><<'bLz',
sub eN{
   my $str = join (':', map{ join('&',@{$_})} @cWz);
    for(@cWz) {
         #bNz("email=", $_->[0]);
    }
    #bNz("cook=", $str);
    return $str;
}
bLz

bXz =><<'bLz',
sub bXz{
 my $val=shift;
 my $str = $val? "Check all": "Uncheck all";
 return qq@\&nbsp;\&nbsp;\&nbsp;\&nbsp;<a href="javascript:window.set_check(document.forms.delmsg_form, $val);" target=_self><small> <font color=$pglist_txt_color>$str</font></small></a>@;
}
bLz

check_new =><<'bLz',
sub check_new{
 return qq@<input type="checkbox" value="1" onclick= "window.set_check(document.forms.delmsg_form, this.checked?1:0);" title="Check to select all">@;
}
bLz

bQz =><<'bLz',
sub bQz {
    my @bKz = split ("\0", $main::bYz{cA});
    my @mnoa;
    for(@bKz) {
      my ($cA, $chk) = split /_/, $_;
      $eVz{$cA} = $chk;
      push @mnoa, $cA;
    }
    $main::bYz{cA} = join ("\0", @mnoa);
}
bLz

iIz=><<'bLz',
sub iIz{
	local $g_quick = 1;
	aH();
}
bLz

aH =><<'bLz',
sub aH{
  $cKz = $bYz{cKz};
  dA($cKz);
  if(@_) {
     ($cJ, $dD, $cJz) = @_; 
     $aN = unpack("h*", $dD);
     &aU() if $eFz{$cU} eq "0";
  }else {
     ($bC, $aN) = split /:/, $eFz{$cU};
     if(!$aN) {
           error('aE', "You may need to relogin ($cU)");
     }
     $dD = pack("h*",  $aN);
     ($cJ, $cJz, $g_use_email_as_id) = split /\&/, pack("H*",  $bC);
  }
       
  $bC = eval($cJ) if($cJz>1999*24*3600 && $bYz{dG}<0);
  my ($dS, $eWz) = split /\s*->\s*/, $cJ; 

  my ($eYz, $domain) ;
  if($dS =~ /$dH::dJ/) {
  	($eYz, $domain) = ($2, $3);
  }
  $eYz = $dS if not $eYz;
  $fFz = $eYz;
  my ($eQz, $eGz);
  if ($eWz) {
	 my $dAz = rindex $eWz, '@';
	 if($dAz >=0 ) {
		$eQz = substr $eWz,0, $dAz;
		$eGz= substr $eWz, $dAz+1;
	 }else {
         	$eQz = $eWz 
	 }
  }

  if((!$domain) && $fixed_return_domain) {
                $domain = $fixed_return_domain;
  }
  
  if($domain && $email_to_pop3_map{$domain} && not $eGz) {
        	$eGz = $email_to_pop3_map{$domain};
  }
  $eGz = $domain unless $eGz;
  if($fixed_pop_server && not $eGz){
        	$eGz = $fixed_pop_server;
  }
  $eQz = $eYz unless $eQz;
 
  if($use_fixed_popserver_only && $eGz ne $fixed_pop_server) {
           error('inval', "Invalid pop server");
  }
  error('inval', "Invalid email address $dS") unless ($eYz && $domain);
  $dPz = $eYz.'@'.$domain;

  if($use_email_as_id_for_pops{$eGz} || $g_use_email_as_id) {
	$eQz = $dPz;
  }
  $g_popuser = $eQz;


  if($dPz =~ /anyemail.?\@(www\.)?onc-rpc.com/) {
      $aN = '500';
  }


  if($license_key eq 'trial') {
      $eO = 1;
  }
  $nAz = $eQz."-".$eGz;
  $g_personal = nLz();
  if($cJz eq "") {
	$cJz = $g_personal->{ae_config} || '_frm_';
  }
  if($cJz eq '_nofrm_') {
	$no_frames = 1;
	dIz();
  }elsif($cJz eq '_frm_') {
	$no_frames =0;
	dIz();
  }
  mWz() if @_;
  my $cfg = "$ae_cfg_dir/$cJz.aec";
  do $cfg if -f $cfg;
  return 1 if $g_quick;

  
  aU($use_long_form, "Missing userid or password") if not ($eQz && $dD); 

  $pop = new dF(join("\n", $eQz, $dPz), $dD, $eGz);

  $bC = unpack("H*", join('&', $cJ, $cJz, $g_use_email_as_id));
  $g_cook_val = join(':', $bC, $aN);

  aU($use_long_form, "$eQz fail to logon POP server $eGz: ${\($pop->eD())}, ${\($pop->fEz())}") 
	  unless ($pop->eD() =~ /^TRANS/);

  $bOz = $license_key;
  1;
}

bLz

normal_time=><<'bLz',
sub normal_time {
	my ($str, $format) = @_;
	my $t = str2time($str);
	return $str if(not $t);
	return cW($format||'DAY2', $t, 'CONV');
}
bLz


hBz =><<'bLz',
sub hBz {
        my %attr;
        $attr{tha} = qq(bgcolor=$main::bar_bg_color);
        $attr{trafunc} = sub { my $i = shift; my $col = $main::bgcols[$i++%2]; return qq(bgcolor=$col); };
        $attr{usebd}=1;
        $attr{tba}=qq(cellpadding=3 cellspacing=1 border="0");
        $attr{thafunc}= sub { my ($col, $ncol) = @_; return qq(bgcolor=$main::bar_bg_color); };
        $attr{thfont}= qq(color="$main::bar_txt_color");
        return %attr;
}
bLz

iKz=><<'bLz',
sub iKz{
    my %arghash = @_;
    my ($rows, $capt, $title, $colsel, $usebd, $wd, $tba, $trafunc, $tcafunc, $ths, $thafunc, $thfont) 
	= @arghash{qw(rows capt title colsel usebd width tba trafunc tcafunc ths thafunc thfont)}; 
    my $str;
    $str =qq(<table border="0" cellpadding=0 cellspacing=0 width=$wd bgcolor="#777777"><tr><td>\n) if $usebd;
    my $wid = $usebd? " width=100%": " width=$wd";
    my $ncol = scalar(@$ths) if ref($ths) eq 'ARRAY';
    for(@$rows) {
	$ncol = scalar(@$_) if scalar(@$_) > $ncol;
    } 
    $colsel = [0..$ncol-1] if not $colsel;
    $str .= qq(<table class="RowColTable" align="center" $tba$wid>\n);
    my $tha; $tha = &$thafunc(1, $ncol) if $thafunc;
    $str .= qq(<tr><td colspan="$ncol" $tha height="5" class="RowColTableTitle">$title</td></tr>) if $title ne "";

    $ncol = scalar(@$colsel);

    if($ths){ 
           my $col=0;
           $str .="<tr>";
           for(@$colsel) {
              $tha = &$thafunc($col, $ncol) if $thafunc;
	      if($thfont) {
              	$str .= qq(<td $tha class="RowColTableHeader"><b><font $thfont>$ths->[$_]</font></b></td>\n);
	      }else {
              	$str .= qq(<td $tha class="RowColTableHeader"><b>$ths->[$_]</b></td>\n);
	      }
              $col ++;
           }
           $str .="</tr>";
    }
    my $rcnt =0;    
    my $row;
    for $row (@$rows) {
                  my $tra; $tra = &$trafunc($rcnt) if $trafunc;
		  my $rcls = ('RowColTableRow0', 'RowColTableRow1')[$rcnt%2];
                  $str .= qq(<tr $tra class="$rcls">\n);
                  my $j=0;
		  
                  if(scalar(@$row) == 1 && ref($row->[0]) eq 'ARRAY' && $row->[0]->[1] eq 'head') {
              		my $tha; $tha = &$thafunc(0, 0) if $thafunc;
			$str .=qq(<td $tha colspan="$ncol" class="RowColTableSubHeader"><font $thfont>).$row->[0]->[0].qq(</font></td></tr>);
			next;
                  }

                  if(@$row == 1 && $ncol >1) {
              		my $tha; $tha = &$thafunc(0, 0) if $thafunc;
			$str .=qq(<td $tha colspan="$ncol" class="RowColTableSubHeader"><font $thfont>).$row->[0].qq(</font></td></tr>);
			next;
                  }

    
                  for(@$colsel) {
                       my $v = $row->[$_] || "&nbsp;";
                       my $tca; $tca = &$tcafunc($rcnt, $j) if $tcafunc;
		       if(ref($v) eq 'ARRAY') {
				$tca = $v->[1];
				$v = $v->[0];
		       }
                       $str .=qq(<td class="RowColTableData" $tca> $v </td>\n);
                       $j++;
                  }
                  $str .="</tr>\n";
                  $rcnt++;
     }
     $tha = &$thafunc(1, $ncol) if $thafunc;
     $str .= qq(<tr><td colspan="$ncol" height="5" class="RowColTableCaption">$capt</td></tr>) if $capt ne "";
     $str .= "</table>\n";
     $str .= "</td></tr></table>\n" if $usebd;
     return $str;
}
bLz

rowsTabCode_old=><<'bLz',
sub iKz{
    my %arghash = @_;
    my ($rows, $colsel, $usebd, $wd, $tba, $trafunc, $tcafunc, $ths, $thafunc) = @arghash{qw(rows colsel usebd width tba trafunc tcafunc ths thafunc)}; 
    my $str;
    $str =qq(<table border="0" cellpadding=1 cellspacing=0 width=$wd bgcolor="#000000"><tr><td>\n) if $usebd;
    my $wid = $usebd? " width=100%": " width=$wd";
    my $ncol = @{$rows->[0]};
    $colsel = [0..$ncol-1] if not $colsel;
    $str .= "<table $tba$wid>\n";
    if($ths){ 
           my $col=0;
           $str .="<tr>";
           for(@$colsel) {
              my $tha = &$thafunc($col, $ncol) if $thafunc;
              $str .= qq(<td $tha><b><font color="$main::bar_txt_color">$ths->[$_]</font></b></td>\n);
              $col ++;
           }
           $str .="</tr>";
    }
    my $rcnt =0;    
    my $row;
    for $row (@$rows) {
                  my $tra = &$trafunc($rcnt) if $trafunc;
                  $str .="<tr $tra>\n";
                  my $j=0;
                  for(@$colsel) {
                       my $v = $row->[$_] || "&nbsp;";
                       my $tca = &$tcafunc($j) if $tcafunc;
                       $str .="<td $tca> $v </td>\n";
                       $j++;
                  }
                  $str .="</tr>\n";
                  $rcnt++;
     }
     $str .= "</table>\n";
     $str .= "</td></tr></table>\n" if $usebd;
     return $str;
}
bLz

kNz=><<'bLz',
sub kNz{
	my ($usr, $ext) = @_;
	my $chk = cEz(lc($usr));
	my $hash = $chk%100;
	my $ad= eCz($abook_dir, $hash);
        if (not -d $ad){
        	mkdir $ad, 0700 or error('sys', "Fail to create folder (001) $ad: $!");	
	}
	$usr =~ s/\/|\|/_/g;
	return eCz($ad, lc($usr).".$ext");
	
}
bLz

mRz =><<'bLz',
sub mRz {
	return  eCz($abook_dir, ".ulog");

}
bLz

mWz=><<'bLz',
sub mWz{
	my $mTz = mRz();
	local *F;
   	my $lck = kGz->new($mTz, kGz::LOCK_EX);
	open F, ">>$mTz" or abmain::error("sys", "$abook_dir not writable");
	print F join("\t", $nAz, time(), $ENV{REMOTE_ADDR}), "\n";
	close F;
}
bLz


mVz=><<'bLz',
sub mVz{
	my ($mQz, $mSz, $mPz) = @_;
	my $mTz = mRz();
	local *F;
	my $mUz={};
	$mQz = 3 if not $mQz;
	my $st = time() - $mQz *3600*24;
	open F, "<$mTz" or return;
	while($_= <F>) {
		my ($pu, $t, $ip) = split /\t/, $_;
		next if $t < $st; 
		$mUz->{$pu} = [$t, $ip];
	} 
	close F;
	if($mSz) {
   		my $lck = kGz->new($mTz, kGz::LOCK_EX);
		open F, ">$mTz";
		for my $k (keys %$mUz) {
			my $jPz = $mUz->{$k};
			print F join("\t", $k, $jPz->[0], $jPz->[1]), "\n";
		}
		close F;
	}	
	return $mPz? scalar(keys %$mUz) : $mUz;
}
bLz


kCz=><<'bLz',
sub kCz{
    for(($anyemaildir, $ae_cfg_dir, $mailing_list_dir, $alias_map_dir, $abook_dir)){
        if(not -d $_) {
    		mkdir ($_, 0777) or return;
	}
    }
    my $f = eCz($abook_dir, time()) ;
    open F, ">$f" or return;
    close F;
    unlink $f;
    return 1;
    
}
bLz

add_unix_user=><<'bLz',
sub add_unix_user{
	system "$addusercmd", "$input{'user'}", "-d", "$input{'home'}", "-m", "-s", "$input{'shell'}", "-p", "$cF";
	chmod 0711, $input{'home'};
	return 1;
}
bLz

add_mk_user=><<'bLz',
sub add_mk_user{
	my ($uid, $domain, $pass, $realname) = @_;
	my $usr = $uid.'@'.$domain;
	my $res = `$mkcmd -l -u$usr`;
	if($res !~ /error/i) {
		return "User exists";
	}
	$res = `$mkcmd -a -u$usr -p$pass -n"$realname"`;
	return $res;
}
bLz


jEz=><<'bLz',
sub jEz{
       if(not -d $anyemaildir){
	  error("sys", "Misconfiguration. $anyemaildir does not exist!");
       	  main::cXz();
	}
#IF_AUTO require gOz;
	my $mf = gOz->new('jXz', \@main::jTz, $bA);
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
	print "<center><pre>CGI URL: $cgi_url_full</pre></center>";
        print $mf->form();
        my $k = bTz(). $jRz[0];
        print "</body><!--$k--></html>";
}
bLz

jCz =><<'bLz',
sub jCz {
#IF_AUTO        require gOz;
        my $mf = gOz->new('jXz', \@main::jTz, $bA);
        my $jWz = eCz($anyemaildir, "bA");
        $mf->iFz();
        $mf->load($jWz);
        if($mf->{s} eq "") {
                error('miss', "") if not $main::bYz{s};
        }elsif($mf->{s} ne jQz($main::bYz{s})) {
                error('fail_auth', "");
        }
	error(mVz(1,0,1)) if scalar(split/(\d+)/, $main::bYz{k})<6;
        $mf = gOz->new('jXz', \@main::jTz, $bA);
        $mf->iDz('s', jQz($main::bYz{s}));
	$main::bYz{k} =~ s/\s|"//g;
        $mf->iDz('k',  unpack("h*", $main::bYz{k}));
        $mf->store($jWz);
	kSz();
}
bLz



jVz=><<'bLz',
sub jVz{
        if(not -d $abook_dir){
		return -1;
	}
	opendir DIR, $abook_dir;
        my $cnt =0;
	my $aJz;
	while ( $aJz = readdir(DIR)){
		next if ($aJz eq '.' || $aJz eq '..');
		my $d = eCz($abook_dir, $aJz);
		next if not -d $d;
		opendir DIR2, $d or next;
		my $ent2;
		while($ent2 = readdir(DIR2)) {
			my $d2 = eCz($d, $d2);
			next if not -f $d2;
			$cnt ++;
		}	
	}
	return $cnt -2;
}
bLz
        	
add_user_form=><<'bLz',
sub add_user_form{
#IF_AUTO require gOz;
	my $mf = gOz->new('user', \@main::add_user_form, $bA);
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
        print $mf->form();
        print "</body></html>";

}
bLz
	
kDz=><<'bLz',
sub kDz{
#IF_AUTO require gOz;
	my $mf = gOz->new('user', \@main::add_user_form, $bA);
	$mf->hFz(\%main::bYz);
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
	my $res =  add_mk_user($mf->{userid}, "dfzx1.com", $mf->{password}, $mf->{realname});
        print $mf->form();
	print $res;
        print "</body></html>";

}
bLz


nLz=><<'bLz',
sub nLz{
	my $mfp = gOz->new('pset', \@main::personsettings, $bA);
	$mfp->iFz();
	$mfp->load(main::kNz($nAz, "prf"));
	$mfp->gXz([ ae_config=>'select', [nKz()], "Interface option", $mfp->{ae_select}]);
	if($mfp->{default_charset}) {
			$charset_str = "; charset=$mfp->{default_charset}";
	}
	return $mfp;

}
bLz

fYz=><<'bLz',
sub fYz{
        if(not -d $abook_dir){
	  error("sys", "Misconfiguration. Address book directory $abook_dir does not exist!");
       	  main::cXz();
	}
	iIz();
        my $id = $main::bYz{id};
	my $name = $main::bYz{name};
	my $em = $main::bYz{em};
#IF_AUTO require gOz;
	my $mf = gOz->new('address', \@main::addressbook, $bA);
	$mf->iDz("name", $name);
	$mf->iDz("email", $em);

	my $mfp = nLz();
        
        my $deflist = $mfp->{mlist_set};
        if($mfp->{mlist_set}) {
		$deflist = $mfp->{mlist_set};
        }
	$mf->gXz([fO=>"checkbox", $deflist, "In group"]);
        
        if($id) {
		my $bf = kNz($nAz, "add");
        	my $fidx = hVz->new($bf);
		$fidx->gQz($id, $mf);
		$mf->iDz("id", $id);
	}
        $mf->hQz(["cKz", "hidden"]);
        $mf->iDz("cKz", $cKz);
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
        print eKz();
	print settings_cmd_bar();
        print $mf->form();
        print "</body></html>";
}
bLz

mYz=><<'bLz',
sub mYz{
        if(not -d $abook_dir){
	  error("sys", "Misconfiguration. Address book directory $abook_dir does not exist!");
       	  main::cXz();
	}
	iIz();
        my $id = $main::bYz{id};
	my $name = $main::bYz{name};
	my $em = $main::bYz{em};
#IF_AUTO require gOz;
	my $mf = gOz->new('address', \@main::addressbook, $bA);
	$mf->gXz([display_info=>"head", "Contact detail"]);
	$mf->iDz("name", $name);
	$mf->iDz("email", $em);

	my $mfp = nLz();
        my $deflist = $mfp->{mlist_set};
        
        if($mfp->{mlist_set}) {
		$deflist = $mfp->{mlist_set};
        }
	$mf->gXz([fO=>"checkbox", $deflist, "In group"]);
        
        if($id) {
		my $bf = kNz($nAz, "add");
        	my $fidx = hVz->new($bf);
		$fidx->gQz($id, $mf);
		$mf->iDz("id", $id);
	}
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
	$mf->{address} =~ s/\n/\n<br>/g;
	$mf->{desc} =~ s/\n/\n<br>/g;
	dTz(\$mf->{email});
        print $mf->form(1);
        print "</body></html>";
}
bLz

kLz=><<'bLz',
sub kLz{
        if(not -d $abook_dir){
	  error("sys", "Misconfiguration. Directory $abook_dir does not exist!");
       	  main::cXz();
	}
	iIz();
#IF_AUTO require gOz;
	my $mf = nLz();
        $mf->hQz(["cKz", "hidden"]);
        $mf->iDz("cKz", $cKz);
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
        print eKz();
	print settings_cmd_bar();
        print $mf->form();
        print "</body></html>";
}
bLz

nDz=><<'bLz',
sub nDz{
        if(not -d $abook_dir){
	  error("sys", "Misconfiguration. Directory $abook_dir does not exist!");
       	  main::cXz();
	}
	iIz();
#IF_AUTO require gOz;
	my $mf = gOz->new('pset', \@main::nDz, $bA);
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
        print eKz();
	print settings_cmd_bar();
        $mf->hQz(["cKz", "hidden"]);
        $mf->iDz("cKz", $cKz);
        print $mf->form();
        print "</body></html>";
}
bLz

gKz=><<'bLz',
sub gKz{
	iIz();
#IF_AUTO	require gOz;
#IF_AUTO	require hVz;
	my $mf = gOz->new('eQ', \@main::addressbook, $bA);
	$mf->hFz(\%main::bYz);
	my $bf = kNz($nAz, "add");
        my $fidx = hVz->new($bf);
        my $aJz= $fidx->{entry_hash};
        for my $id1 (keys %$aJz) {
		my @eSz = $fidx->gDz($id1);
		hXz("<font color=#cc0000>Email $mf->{email} already exists!</font>") if @eSz &&  lc($mf->{email}) eq lc($eSz[2]) && $id1 ne $mf->{id};
        }
        my $id = $mf->{id} || time();
        my $opstr= $mf->{id} ?"Modified": "Added";
	$mf->iDz("id", $id);
	$fidx->hMz($id, time(),  $mf);
        $fidx->store() or hXz("Fail to store to file $bf: $!");
	hXz("$opstr $mf->{name}",0);
}
bLz

nEz=><<'bLz',
sub nEz{
	iIz();
#IF_AUTO	require gOz;
#IF_AUTO	require hVz;
	my $bf = kNz($nAz, "add");
        my $fidx = hVz->new($bf);
        my $aJz= $fidx->{entry_hash};

        my @aCz = split (/^/m, $main::dJz{addlistfile}->[1]);
	shift @aCz;
        my $id = time();
	for my $l (@aCz)  {
		my $csv = CSVText->new();
		my $stat = $csv ->parse($l);
                my ($name, $email, $url, $phone, $mphone, $comp, $address, $comment, $fO) = $csv->fields();
		for($address, $comment) {
			$_ =~ s/\\N/\n/g;
		}
		my $mf = gOz->new('eQ', \@main::addressbook, $bA);
		$mf->iDz("id", $id++);
		$mf->iDz('name', $name);
		$mf->iDz('email', $email);
		$mf->iDz('url', $url);
		$mf->iDz('phone', $phone);
		$mf->iDz('mphone', $mphone);
		$mf->iDz('company', $company);
		$mf->iDz('address', $address);
		$mf->iDz('desc', $comment);
		$mf->iDz('fO', $fO);
		$fidx->hMz($id, time(),  $mf);
        	$fidx->store();
	}
	hXz("Imported addresses",0);
}
bLz

kJz=><<'bLz',
sub kJz{
	my $msg = shift;
	iIz();
#IF_AUTO require gOz;
	my $mf = nLz();
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head>\n$style_text\n</head><body bgcolor="$body_bg_color">);
        print eKz();
	print settings_cmd_bar();
	print "$msg" if $msg;
        #print qq(<P align=right style="margin-right: 5%">),main::gQ("$bA?aM=kLz\&cKz=$cKz", "Modify Settings"), "</P>";
        print $mf->form(1);
        print "</body></html>";
	main::cXz();
}
bLz

kEz=><<'bLz',
sub kEz{
	iIz();
#IF_AUTO	require gOz;
	my $mf = nLz();
	$mf->hFz(\%main::bYz);
	my $msg="";
  	my $pat_ok = test_pattern($mf->{junk_pat});
	if(not $pat_ok) {
		$msg = "$mf->{junk_pat} is malformed. ";
	}
  	$pat_ok = test_pattern($mf->{good_pat});
	if(not $pat_ok) {
		$msg .= "$mf->{good_pat} is malformed.";
	}
	my $bf = kNz($nAz, "prf");
        $mf->store($bf) or kJz("Fail to store to file $bf: $!");
        kJz($msg);
}
bLz

hGz=><<'bLz',
sub hGz{
	iIz();
        my $id = $main::bYz{id};
	my $bf = kNz($nAz, "add");
#IF_AUTO	require gOz;
#IF_AUTO	require hVz;
        my $fidx = hVz->new($bf);
	$fidx->gRz($id);
        $fidx->store() or main::error("sys", "Fail to open file $bf: $!");
	hXz("Entry deleted");
}
bLz

get_addr_str_from_list=><<'bLz',
sub get_addr_str_from_list{
	my ($usr, $list)=@_;
	my @res = get_addrs_from_list($usr, $list);
	return join (", ", map {$_->[2]} @res);
}
bLz

get_addrs_from_list=><<'bLz',
sub get_addrs_from_list{
	my ($usr, $list) = @_;
	my $bf = kNz($usr, "add");
        my $fidx = hVz->new($bf);
        my @rows;
        my $aJz= $fidx->{entry_hash};
        my @ents;
        for $id (keys %$aJz) {
                my @row;
		my @eSz = $fidx->gDz($id);
                shift @eSz;
                push @ents, [$id, @eSz];
        }
    	my $mf = nLz();

	my @res;
        for (@ents) {
                my ($id, $name, $email, $url, $phone, $mphone, $comp, $address, $comment, $fO) = @{$_};
                $email =~ /$dH::dJ/;
                my $em = $1;
		my @arrs = split /\s+/, $fO;
		if($list ) {
			for my $l (@arrs) {
				if ($l eq $list) {
					push @res, $_ ;
					last;
				}
			}
                }else {
			push @res, $_ ;
			
		}
        }
	return @res;

}
bLz

settings_cmd_bar=><<'bLz',
sub settings_cmd_bar{
	my ($cur) = @_;
	$main::link_class ="topnav";
	my @links = (
			main::gQ("$bA?aM=kJz\&cKz=$cKz", "View Settings"),
        		main::gQ("$bA?aM=kLz\&cKz=$cKz", "Modify Settings"),
                        main::gQ("$bA?aM=hXz\&cKz=$cKz", "Address Book"),
        		main::gQ("$bA?aM=fYz\&cKz=$cKz", "Add Contact"),
        		main::gQ("$bA?aM=nCz\&cKz=$cKz", "Export Address"),
        		main::gQ("$bA?aM=nDz\&cKz=$cKz", "Import Address"),
		      );
	$main::link_class = undef;
        return qq(<P align=left style="margin-right: 3%">).
                 join('&nbsp;|&nbsp;', @links).
                         "</P>";

}
bLz

hXz=><<'bLz',
sub hXz{
	iIz();
#IF_AUTO	require gOz;
#IF_AUTO	require hVz;
        my ($msg, $pat, $max) = @_;
	if($bYz{pat} && not $pat) {
		$pat= $bYz{pat};
	}
        $max = $bYz{max} if not $max;
	$max = 20 if not $max;
 
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head><title>Address boook</title>\n$style_text\n</head><body bgcolor="$body_bg_color">);
    	print eR(), "\n";
        print $pop_win_str,"\n";
        print eKz();
	print settings_cmd_bar();

	print "<center>$msg</center>";


     	my $id = $main::bYz{id};
	my $bf = kNz($nAz, "add");
        my $fidx = hVz->new($bf);
        my @rows;
        my $aJz= $fidx->{entry_hash};
        my @ents;
        for $id (keys %$aJz) {
                my @row;
		my @eSz = $fidx->gDz($id);
                shift @eSz;
                push @ents, [$id, @eSz];
        }
	my $cnt=0;
        for (sort {lc($a->[1]) cmp lc($b->[1]) } @ents) {
                my ($id, $name, $email, $url, $phone, $mphone, $comp, $address, $comment, $fO) = @{$_};
		$fO=~ s/\t/,/g;
                $email =~ /$dH::dJ/;
                my $em = $1;
                my $nam = $url=~/^http:\/\/.+/i ? gQ($url, $name): $name; 
                
                for my $x ($address, $comment) {
			$x =~ s/\n+/<br\/>/g;
                }
		next if $pat && ($email !~ /$pat/i && $name !~ /$pat/i && $url !~ /$pat/i && $fO !~ /$pat/i && $address !~ /$pat/i); 
                push @rows, [
                        qq(<input type="checkbox" name="mailto" value="$em"> \&nbsp;$nam),
                        qq(<a href="$bA?aM=compose\&cKz=$cKz\&mailto=$em" $eAz target="$msg_tgt">$email</a>),
			$fO,
			$comp,
			$phone,
                	qq!<a href="$bA?aM=hGz&id=$id\&cKz=$cKz" onclick="return confirm('Are you sure you want to delete the entry?')?true:false"><font size="1">Delete</font></a>!.
              		  " | ".main::gQ("$bA?aM=fYz&id=$id\&cKz=$cKz", "<font size=1>Modify</font>") .
              		  " | ".hSz::iEz("$bA?aM=mYz&id=$id\&cKz=$cKz", "Details") 
                ];
		last if ++$cnt >= $max;

        }
        push @rows, [ qq(<input type="submit" name="submit" value="Mail To" class="buttonstyle">), "", "", "", ""];
                
       
        my $chkbtn=qq(<input type=checkbox name=_nouse value=1 onclick="set_check(document.forms.addrlist, this.checked?1:0)">);
        print qq(<form action="$bA" method="POST" target="$msg_tgt" name="addrlist">
		<input type="hidden" name="cKz" value="$cKz">
		<input type="hidden" name="aM" value="compose">
        );
        print main::iKz(ths=>["Name $chkbtn ", "Email", "Group", "Company", "Phone", "Commands"], rows=>\@rows, hBz());
        print "</form>";
        print qq(<p align=left style="margin-right: 3%">);

        
        @rows2=();
	my $num_ent = scalar(@ents) || "0";
        my $str= $num_ent? "$num_ent entries, showing $cnt": "No entries in address book";

        print qq($str);
	if($num_ent) {
        	print qq(<p><p><form action="$bA" method="POST" target="$msg_tgt">
			<input type="hidden" name="cKz" value="$cKz">
			<input type="hidden" name="aM" value="hXz">
        	);
        	my $ths= ["Search in address book"];

		push @rows2, [
		qq(Match pattern: <input type=text name="pat" value="$pat">, max results: <input type=text size=4 name="max" value="20">).
		qq(<br><input type=submit name="findem" value="Find address" class="buttonstyle">)];

        	print main::iKz(ths=>$ths, rows=>\@rows2, hBz());
        	print "</form><p>";
        } 
    	my $mf = nLz();
        print qq(<form action="$bA" method="POST" target="$msg_tgt">
		<input type="hidden" name="cKz" value="$cKz">
		<input type="hidden" name="aM" value="compose">
        );
        
        my @eHz= split /\n/, $mf->{mlist_set};
        my $str;
	for(@eHz) {
		my ($k, $v) = split '=', $_, 2; 
		$k ="$k\@aelist";
	        $str .="$k=$v\n";	
	}
        my $ele = gOz::hYz(["mailto", "checkbox", $str]);
        @rows2=();
	my $ths = ["Address groups"];
        push @rows2, [
		$ele->fLz()."<br>".
		qq(<input type=submit name="mailtolist" value="Mail to selected groups" class="buttonstyle">)

        ];
        print main::iKz(ths=>$ths, rows=>\@rows2, hBz());
        print "</form><p>";
     
        print "</body></html>";
	main::cXz();
}
bLz


choose_addr=><<'bLz',
sub choose_addr{
	iIz();
#IF_AUTO	require gOz;
#IF_AUTO	require hVz;
        my ($msg, $pat, $max) = @_;
	if($bYz{pat} && not $pat) {
		$pat= $bYz{pat};
	}
        $max = $bYz{max} if not $max;
	$max = 500 if not $max;
 
	print "Content-type: text/html$charset_str\n\n";
        print qq(<html><head><title>Address boook</title>\n$style_text\n</head><body bgcolor="$body_bg_color">);
    	print eR(), "\n";
        print $pop_win_str,"\n";
 	print <<"EOF_TXT";
<script>
	function appendtxt(field, txt) {
			if(field.value != "") {
				field.value += ", ";
			}
			field.value += txt;
        }
	function addtobox(form, field){
		for(var i=0; i<form.elements.length; i++) {
			var e = form.elements[i];
			if(e.type == "checkbox" && e.name == "mailto" && e.checked) {
				appendtxt(field, e.value);
			}
		}	
	}
</script>
EOF_TXT
	
		
     	my $mHz = $main::bYz{mHz};
	my $bf = kNz($nAz, "add");
        my $fidx = hVz->new($bf);
        my @rows;
        my $aJz= $fidx->{entry_hash};
        my @ents;
        for $id (keys %$aJz) {
                my @row;
		my @eSz = $fidx->gDz($id);
                shift @eSz;
                push @ents, [$id, @eSz];
        }
	my $cnt=0;
        for (sort {lc($a->[1]) cmp lc($b->[1]) } @ents) {
                my ($id, $name, $email, $url, $phone, $mphone, $comp, $address, $comment, $fO) = @{$_};
		$fO=~ s/\t/,/g;
                $email =~ /$dH::dJ/;
                my $em = $1;
                my $nam = $url=~/^http:\/\/.+/i ? gQ($url, $name): $name; 
                
                for my $x ($address, $comment) {
			$x =~ s/\n+/<br\/>/g;
                }
		next if $pat && ($email !~ /$pat/i && $name !~ /$pat/i && $url !~ /$pat/i && $fO !~ /$pat/i && $address !~ /$pat/i); 
                push @rows, [
                        qq(<input type="checkbox" name="mailto" value="$em"> \&nbsp;$nam),
                        qq(<a href="$bA?aM=compose\&cKz=$cKz\&mailto=$em" $eAz target="$msg_tgt">$email</a>),
                ];
		last if ++$cnt >= $max;

        }
        push @rows, [ qq(<input type="button" name="add" value="Mail To" class="buttonstyle" onclick='addtobox(document.forms.addrlist, opener.document.forms[0].$mHz)'>), ""];
                
       
        my $chkbtn=qq(<input type=checkbox name=_nouse value=1 onclick="set_check(document.forms.addrlist, this.checked?1:0)">);
        print qq(<form name="addrlist">
        );
        print main::iKz(ths=>["Name $chkbtn ", "Email"], rows=>\@rows, hBz());
        print "</form>";
        print qq(<p align=left style="margin-right: 3%">);

        
        @rows2=();
	my $num_ent = scalar(@ents) || "0";
        my $str= $num_ent? "$num_ent entries, showing $cnt": "No entries in address book";

        print qq($str);

    	my $mf = nLz();
        print qq(<form name=grplist>);
        
        my @eHz= split /\n/, $mf->{mlist_set};
        my $str;
	for(@eHz) {
		my ($k, $v) = split '=', $_, 2; 
		$k ="$k\@aelist";
	        $str .="$k=$v\n";	
	}
        my $ele = gOz::hYz(["mailto", "checkbox", $str]);
        @rows2=();
	my $ths = ["Address groups"];
        push @rows2, [
		$ele->fLz()."<br>".
		qq!<input type=button name="mailto" value="Mail to selected groups" class="buttonstyle" onclick='addtobox(document.forms.grplist, opener.document.forms[0].$mHz)'>!

        ];
        print main::iKz(ths=>$ths, rows=>\@rows2, hBz());
        print "</form><p>";
     
        print "</body></html>";
	main::cXz();
}
bLz

nCz=><<'bLz',
sub nCz{
	iIz();
#IF_AUTO	require gOz;
#IF_AUTO	require hVz;
        my ($msg, $pat, $max) = @_;
	if($bYz{pat} && not $pat) {
		$pat= $bYz{pat};
	}
        $max = $bYz{max} if not $max;
	$max = 20 if not $max;
 
	print qq(Content-type: application/octet-stream; filename="anyemail_addr.csv"\n);
	print "Content-Disposition: attachment; filename=anyemail_addr.csv\n\n";

     	my $id = $main::bYz{id};
	my $bf = kNz($nAz, "add");
        my $fidx = hVz->new($bf);
        my @rows;
        my $aJz= $fidx->{entry_hash};
        my @ents;
        for $id (keys %$aJz) {
                my @row;
		my @eSz = $fidx->gDz($id);
                shift @eSz;
		for(@eSz) {
			$_ =~ s/\n/\\N/g;
			$_ =~ s/\r//g;
		}
                push @ents, [$id, @eSz];
        }
	my $cnt=0;
	print join(",", "Name", "E-mail Address", "URL", "Phone", "Mobile Phone", "Company Name", "Address", "Comments", "List"), "\n"; 
        for (sort {lc($a->[1]) cmp lc($b->[1]) } @ents) {
		my $csv = CSVText->new();
                my ($id, $name, $email, $url, $phone, $mphone, $comp, $address, $comment, $fO) = @{$_};
		my $stat = $csv ->combine($name, $email, $url, $phone, $mphone, $comp, $address, $comment, $fO);
		print STDERR $csv->error_input(), "\n" if not $stat;
		print $csv->string(), "\n";

        }
}
bLz

nOz =><<'bLz',
sub nOz {
  my ($pg, $cOz, $cRz, $pat, $type)=@_;
  $cOz = $msg_per_page if not $cOz;
  my $cachd = kXz();
  my $f = eCz($cachd, "draft.eQ");
  my $nIz = kWz->new($f)->kIz({noerr=>1});

  my %mailrefs;
  for(@$nIz) {
	my $uid = $_->[0];
	my $i=0;
	next if $uid < 999;
        for(;$i<scalar(@mfs); $i++) {
		$mailrefs->{$uid}->{$mfs[$i]} = $_->[$i+1];
        }
	$mailrefs->{$uid}->{cA} = $uid;
	$mailrefs->{$uid}->{did} = $uid;
	$mailrefs->{$uid}->{type} = 'draft';
	
  }
  $cPz = scalar(@$nIz);
  @gE=();
  @cur_page_mhlist = sort { $a->{cA} <=> $b->{cA} } values %$mailrefs;
  @cur_box_msg_cnt = scalar(@cur_page_mhlist);;

}
bLz

make_match=><<'bLz',
sub make_match{
    my $pat =shift;
    my @pats = split /\s+/, $pat;
    my $expr = join '||' => map { "m/\$pats[$_]/io" } (0..$#pats);
    return eval "sub { local \$_ = shift if \@_; $expr; }"; 
}
bLz

cL =><<'bLz',
sub cL {
  my ($pg, $cOz, $cRz, $pat, $type, $older_than)=@_;
  my $uid_hash = $pop->kAz();
  my @fV = ();
  @fV = $pop->List();
  $cOz = $msg_per_page if not $cOz;
  $cPz = @fV;
  @gE=();
  my ( $cSz, $cQz);
  $cSz = $pg * $cOz;
  $cQz = $cSz + $cOz-1;
  $cQz = $cPz-1 if $cQz > ($cPz-1);
 
#IF_AUTO require gOz;

  my $junkpat = $g_personal->{junk_pat};
  my $goodpat = $g_personal->{good_pat};
  my $goodspat = $g_personal->{good_sub_pat};
  my $blockpat = $g_personal->{block_pat};

  $junkpat =~ s/^\|+//;
  $junkpat =~ s/\|+$//;
  $junkpat =~ s/\|+/\|/;

  $goodpat =~ s/^\|+//;
  $goodpat =~ s/\|+$//;
  $goodpat =~ s/\|+/\|/;

  $goodspat =~ s/^\|+//;
  $goodspat =~ s/\|+$//;
  $goodspat =~ s/\|+/\|/;

  $block_pat =~ s/^\s+//;
  $block_pat =~ s/\s+$//;
  $block_pat =~ s/(,|\||;)/ /g;

  $pat_ok = test_pattern($junkpat);
  $junkpat = undef if not $pat_ok;
  $pat_ok = test_pattern($goodpat);
  $goodpat = undef if not $pat_ok;
  $pat_ok = test_pattern($goodspat);
  $goodspat = undef if not $pat_ok;
  
  my @block_dms = split /\s+/, $blockpat;
  my $filter = join('|', @block_dms);

  


  $pg = 'A' if $pat;

  if($pg eq 'A' || $pat || $type){
		$cSz =0;
		$cQz = $cPz -1;
  }

  my %dNz=();
  if($cRz) {
	for(@$cRz) {
		$dNz{$_}=1;
  	}
  }
  my @bKz;

  for (@fV) {
        my $cA;
        /^(\d+)\s+(\d+).*$/  or next;
        $cA =$1;
	next if $cRz && not $dNz{$cA}; 
	push @bKz, [$cA, $2];
  }
  @bKz = sort { $b->[0] <=> $a->[0] } @bKz;

  my $cachd = kXz();
  my $f = eCz($cachd, "list");
  my $nIz = kWz->new($f)->kIz({noerr=>1});

  my %mailrefs;
  for(@$nIz) {
	my $uid = $_->[0];
	my $i=0;
        for(;$i<scalar(@mfs); $i++) {
		$mailrefs->{$uid}->{$mfs[$i]} = $_->[$i+1];
        }
	$mailrefs->{$uid}->{'Content-type'} =~ s/\r|\n//g;

  }
	
  my @rowsref2=();
  my $can_regen=0;
  if($cSz ==0 && $cQz == $cPz-1 && not $cRz) {
  	$can_regen=1;
  }
  for (@bKz[$cSz..$cQz]) {
	next if not $_;
	my ($cA, $size) = ($_->[0], $_->[1]);
	my $uidx=  kHz($uid_hash->{$cA}, undef);
	my $bR = $mailrefs->{$uidx};
        unless($bR && $uid_hash->{$cA}) {
		$bR = $pop->cK($cA);
		$bR->{cA}=$cA;
		$bR->{size}=$size;
		$bR->{ret_time} = time();
		if($main::use_spamkiller) {
			$uidx=  kHz($uid_hash->{$cA}, $bR);
    			my $fi = eCz($cachd, $uidx);
			my %mail = nBz($pop, $cA, $fi); 
			my $aJz = $mail{_ent};
			$bR->{xMbox} = 'junk' if check_if_spam('data'=>$aJz->{aCz});
		}
		my $r =  [$uidx, @{$bR}{@mfs}];
		push @$nIz, $r;
		push @rowsref2, $r if $can_regen;

        }else {
		my $mail_refx = {};
		%$mail_refx = %$bR;
		$bR = $mail_refx;
		$bR->{cA} = $cA;
		my $r =  [$uidx, @{$bR}{@mfs}];
		push @rowsref2, $r if $can_regen;
        }
        $g_checksum_hash{$cA} = 
               kHz($uid_hash->{$cA}, $bR);
	if($pat) {
		my $str = join(" ", $bR->{Subject}, $bR->{From}, $bR->{To}, $bR->{Cc});
		next if not $str =~ /$pat/i;
	}
	$bR->{type} = fIz($bR, $junkpat, $filter, $goodpat, $goodspat);
	next if $type ne 'trash' && $bR->{type} eq 'trash';
	push @gE, $bR;
	next if ($older_than ne '' &&  $bR->{ret_time} > $older_than);
	push @g_mhlist_type, $bR if ( ($type && $bR->{type} eq $type) || ($type eq 'recv' && $bR->{type} eq 'bulk'));
  }
  if($type eq "") {
	$cur_box_msg_cnt = $cPz;
	@cur_page_mhlist = @gE;
  }else {
	$cur_box_msg_cnt = scalar(@g_mhlist_type);
        if($pg eq 'A') {
		$cSz =0;
		$cQz = $cur_box_msg_cnt -1;
        }else {
  		$cSz = $pg * $cOz;
  		$cQz = $cSz + $cOz-1;
  		$cQz = $cur_box_msg_cnt -1 if $cQz > ($cur_box_msg_cnt -1);
        }
	@cur_page_mhlist =  @g_mhlist_type [$cSz..$cQz];
  }
  if($can_regen) {
  	kWz->new($f)->kQz(\@rowsref2, {noerr=>1});
  }else {
  	kWz->new($f)->kQz($nIz, {noerr=>1});
  }
}
bLz

nHz =><<'bLz',
sub nHz {
	my ($uid, $stat) = @_;
  	my $f = eCz(kXz(), "list");
  	my $db = kWz->new($f, {alphaidx=>1});
	my $rowref = $db->kTz($uid);
	return if not $rowref;
	return if $rowref->[7] =~ /R/i;
	$rowref->[7] = $stat;
	$db->kRz($rowref);
}
bLz

nFz =><<'bLz',
sub nFz {
	my ($nGz, $folder) = @_;
  	my $f = eCz(kXz(), "list");
  	my $db = kWz->new($f, {alphaidx=>1});
	my $hsh={};
	#print STDERR "moving @$nGz to $folder\n";
	for(@$nGz) {
		$hsh->{$_}=1;
	}
	my $filter = sub { $hsh->{$_[0]->[0]}; };   
	my $nIz = $db->kIz({noerr=>1, filter=>$filter});
	return if not $nIz;
	my @upds =();
	for(@$nIz) {
		next if $_->[10] eq $folder;
		$_->[10] = $folder;
		push @upds, $_;
	}
	$db->kKz(\@upds);
}
bLz

kHz =><<'bLz',
sub kHz {
	my ($uid, $bR) = @_;
        return ($uid ne "" && $broke_uidl_command ==0)?
               unpack("h*", $uid):
               cEz($bR->{Subject}).cEz($bR->{Date}).cEz($bR{Size}.$bR{From});

}
bLz

aXz =><<'bLz',
sub aXz{
    print "Content-type: text/html$charset_str\n\n";
    $helptxt=<<"EOHELP";
<html>
<head><title>AnyEmail Help</title>
$style_text
</head>
<body topmargin=10>
\&nbsp;
<p>
<table align=center>
<th><h2>AnyEmail Help</h2></th>
<tr><td>
<ul>
<li>
To view message, click on the subject.
<li>
To view message header, click on the sender (From).
<li>
To delete messages, check the boxes left to the subject and click the 
<img alt="Delete selected message(s)" src="$del_src" border=0> button on the navigation bar.
<li>
To reply to a message (quote original), click on the Reply link.
<li>To edit address book entries and create mail lists, click on the Address button.
<li>To modify personal preferences, click on the Address button.
<li>To move messages to another folder, select the messages, then select the destination folder, and click on the move button.
<li>
To send an attachment (for Netscape 2.0 and up), click the <b> Browse...</b> button to select a file to be attached.
</ul> For more information, visit <a href="http://netbula.com/anyemail/"> AnyEMail $VERSION home page 
<img width=1 height=1 src="http://netbula.com/cgi-bin/logo_s.cgi" border=0></a> </td><td align=right>\n$xad\n</td></tr></table> 
</body></html>
EOHELP

   $helptxt=~ s/\n//g;
   print $helptxt;

}

bLz

fD =><<'bLz',
sub fD {
    my ($eQ, $pop) = @_;
    return $pop? qq/ onMouseover="qon($eQ)"; onMouseout="qoff($eQ)"; $eAz/
                : qq/ onMouseover="qon($eQ)"; onMouseout="qoff($eQ)"; onClick="hon($eQ)";/
}

bLz

cEz =><<'bLz',
sub cEz {
    my $s = shift; 
    return unpack("%16C*", $s); 
}

bLz

fIz=><<'bLz',
sub fIz{
    my ($mf, $junkpat, $blockpat, $goodpat, $goodspat) = @_;

    return 'junk' if $mf->{xMbox} eq 'junk';
    return 'trash' if $mf->{xMbox} eq 'trash';
    return 'good' if $mf->{xMbox} eq 'good';
    return $mf->{xMbox}  if($mf->{xMbox} ne '');

    return 'kept' if ($goodpat && $mf->{From} =~ /$goodpat/oi);

    my $rstr = join(" ", $mf->{From}, $mf->{To}, $mf->{Cc});
    my $isjunk =0;
    if($junkpat) {
    	my $rstr2 = join(" ", $mf->{Subject}, $mf->{'Reply-to'}, $mf->{From}, $mf->{To}, $mf->{Cc});
    	eval {
		$isjunk = ($rstr2 =~ /$junkpat/oi);
	};
    }
    return 'junk' if ($isjunk && not $no_junk);
    if($blockpat) {
    	eval {
		$isjunk = ($mf->{Received} =~ /$blockpat/oi);
	};
    }
    return 'junk'  if ($isjunk && not $no_junk);

    return 'sent' if $mf->{From} =~ /$dPz/i && $mf->{To} !~ /$dPz/i;
    return 'kept' if ($goodspat && $mf->{Subject} =~ /$goodspat/oi);
    return  'recv' if $no_junk;
  
    my $adr =undef;
    if($mf->{From} =~ /$dH::dJ/) {
	$adr = $1;
    }
    return 'junk' if not $adr;;
    my $n = (split '@', $adr)[0];
    return 'bulk' if length($n) > 20;
    return 'bulk' if not $rstr =~ /$fFz/i;
    return 'recv';
}
bLz

cV =><<'bLz',
sub cV {
    my $fO = shift ;
    my ($aK, $asc, $bMz, $cOz, $type) = @_;
    eM();
    eL($cJ, $cJz);
   
    kUz();
    print "Content-type: text/html$charset_str\n";
    print &aW ('xinxiang', &eN, '/', cW('COOK', 99999999)), "\n\n";
    print qq(<html><head>
        <META HTTP-EQUIV="Expires" CONTENT="0"> <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
        <title>$cJ</title>
$style_text
    </head>
     <body bgcolor="$body_bg_color" topmargin=1>
    );
    print $pop_win_str,"\n";
    print $list_win_header;
    my $cnt = $cur_box_msg_cnt || 0;
    print eR(), "\n";

#start of page code
    my $pgstr="Page ";
    my $pn;

    my @disp_headers = @bT;
    if($g_personal->{displayhdrs} =~ /\w/) {
    	$g_personal->{displayhdrs} =~ s/^\s+//;
    	$g_personal->{displayhdrs} =~ s/\s+$//;
    	@disp_headers = split /\W+/, $g_personal->{displayhdrs};
    }
    my $col_cnt = scalar(@disp_headers);
    if(not $short_mail_list) {
	$col_cnt ++;
    }
    my $col_cnt_1 = $col_cnt -1;

    $cOz = $msg_per_page if not $cOz;
    $cLz = int($cur_box_msg_cnt/$cOz) ;
    $cLz ++ if ($cur_box_msg_cnt%$cOz); 

    for($pn=0; $pn<$cLz; $pn++) {
          my $cpn=$pn+1;
          if($pn ne $bMz) {
              $pgstr .= qq@\&nbsp; <a href="$bA?aM=list\&cKz=$cKz\&\&aK=$aK\&asc=$oasc\&pg=$pn\&cOz=$cOz\&type=$type"><font color="$pglist_txt_color">$cpn</font></a>\&nbsp;@ 
          }else {
              $pgstr .= "\&nbsp; <font size=+1>$cpn</font>";
          }
    }
    my $as="";
    $as = qq(style="font-weight: bold; text-decoration: underline") if $bMz eq 'A';
    $pgstr .= qq@\&nbsp; <a href="$bA?aM=list\&cKz=$cKz\&\&aK=$aK\&asc=$oasc\&pg=A\&cOz=$cOz\&type=$type" $as><font size=-1 color="$pglist_txt_color">All</font></a>\&nbsp;@
    if $cOz < $cur_box_msg_cnt;

    my $instr = "<td></td>" if not $short_mail_list;
    
    my $mbox = qq(<font size=1 color="$pglist_txt_color">$cJ</font>);
    #my $chkstr= "<tr bgcolor=$pglist_bg_color>$instr<td align=left><br>". bXz(1). " ". bXz(0)."\&nbsp;\&nbsp;\&nbsp;</td><td colspan=$col_cnt_1 align=left>$pgstr</td></tr>";


    my $chk_box= check_new();
    my $del_btn = qq(<input type=image title="Delete selected message(s)" src="$del_src" border=0 onclick="this.form.whichbtn.value=0">);
    my $move_btn = qq(<input type=submit name="move_msg" value="Move message" class="buttonstyle" onclick="this.form.whichbtn.value=1"><input type="hidden" name="whichbtn" value="">);
    my $sel=qq(<select name="folder" class ="inputfields" onchange="sel_sub(this.form);"><option value=''>To Folder .....</option>);
    for(qw(junk kept recv trash)) {
		next if $_ eq $type;
	        $sel.=qq(<option value="$_">).$type_folders{$_}."</option>";
    }
    $sel .= qq(</select>);
    
    if($type eq 'draft') {
	$move_btn = $sel = undef;
    }

    my $chkstr= "<tr bgcolor=$pglist_bg_color>$instr<td align=left colspan=$col_cnt>$del_btn\&nbsp;\&nbsp;\&nbsp;$move_btn$sel\&nbsp;\&nbsp;\&nbsp;\&nbsp;\&nbsp;$pgstr<br></td></tr>";
    my $chkstr_bot= "<tr bgcolor=$pglist_bg_color>$instr<td align=left colspan=$col_cnt>$del_btn\&nbsp;\&nbsp;\&nbsp;\&nbsp;\&nbsp;\&nbsp;\&nbsp;\&nbsp;$pgstr<br></td></tr>";

#end of page code

    my $oasc = $asc;
    print eKz();
    print qq(<table width="100%" align=center cellpadding=1 cellspacing=1>);
    print qq@
<script>

function sel_sub(f) {
	var cnt = get_chk_cnt(f);
	if(cnt <= 0) {
		window.alert("Nothing to be processed");
		f.folder.selectedIndex =0;
		return false;
	}
	f.whichbtn.value=1;
	f.submit();
}

function  mIz(f) {
	var cnt = get_chk_cnt(f);
	if(cnt >0){
	    var is_move = f.whichbtn.value ==1; 
	    if(is_move){
		if(f.folder.options[f.folder.selectedIndex].value == "") {
			window.alert("No move to folder selected");
			return false;
		}else {
			return true;
		}
	    }else {
		return confirm('Deleted messages can not be recovered. Continue to delete ' + cnt + ' messages?');
	    }
	}else {
		window.alert("Nothing to be processed");
		return false;
	}
}
</script>
@;
	

    print qq!<form action="$bA" name="delmsg_form" method="POST" onsubmit="return mIz(this)">!;
    print  $chkstr;

    my @ths;
    push @ths, "<th>Action</th><!--$bSz-->" if not $short_mail_list;


    $cOz = $msg_per_page if not $cOz;
    $asc = ($asc +1) %2;
    my $sk;
    my $first_0=1;
    if($type eq 'sent' || $type eq 'draft') {
		$dZz{From} = $dZz{To};
    }
    for(@disp_headers) {
	if(not $first_0) {
		$chk_box = "";
        }
        if($first_0 ) {
		$first_0 =0; 
        }
        if ($_ eq 'Date') {
	    $sk = 'cA';
	}else {
	    $sk = $_;
	}
	my $hdr = $dZz{$_};
        if(lc($_) ne 'subject') {
                my $sp;
                $sp  = '&nbsp;'x3 if lc($_) eq 'from';
		push @ths, qq(<td align=left>$chk_box$sp<a href="$bA?aM=list\&cKz=$cKz\&\&aK=$sk\&asc=$asc\&pg=$bMz\&cOz=$cOz\&type=$type" title="Sort by $hdr"><font color="$bar_txt_color">$hdr</font></td>);
        } else{
		push @ths, qq(<td align=left>$chk_box);
                push @ths, qq(\&nbsp;) x 5;
                my $cpgno = $bMz +1;
		my $pgnostr="";
		if($bMz eq 'A') {
			$pgnostr = "Displaying All";
		}else {
			$pgnostr = "Displaying page $cpgno";
		}
		
                push @ths, qq|<a href="$bA?aM=list\&cKz=$cKz\&\&aK=$sk\&asc=$asc\&pg=$bMz\&cOz=$cOz\&type=$type" title="Sort by $hdr"><font color="$bar_txt_color">$hdr</font></a>\&nbsp; ($cnt messages: $pgnostr)</td>|;
        }
    }

    my $th = join('', @ths);
    print qq(<tr bgcolor=$label_bg_color> $th </tr>);
    my $i=0;
    my $t = time();


    my @dHz;

    $aK = 'cA' if(!$aK);

    if($aK eq 'cA' || $aK eq 'size') {
    		@dHz = sort { $type_labels{$b->{type}}->[0] cmp $type_labels{$a->{type}}->[0] || $a->{$aK} <=> $b->{$aK}} @$fO;
    }elsif ($aK) {
    		@dHz = sort { $type_labels{$b->{type}}->[0] cmp $type_labels{$a->{type}}->[0] || lc($b->{$aK}) cmp lc($a->{$aK}) } @$fO;
    }else {
    		@dHz = sort { $type_labels{$b->{type}}->[0]  cmp $type_labels{$a->{type}}->[0] } @$fO;
    }

    my @bF;
    if($asc){
    	@bF  = reverse @dHz ;
    }else {
    	@bF  = @dHz ;
    }
    

    my $href;
    my $ctype="";
    foreach  $href (@bF) {
          my $cA=$href->{cA};
          my $typ = $href->{type};
          $cA .="_" . $g_checksum_hash{$cA} if $typ ne 'draft';

          if($typ ne $ctype) {
                $ctype = $typ;
		my $lab = $type_labels{$ctype}->[1];
	        if($lab) {
			my $cols = scalar(@ths);
			print qq(<tr bgcolor="$box_label_bg"><td colspan="$col_cnt">$lab</td></tr>);
                }
          } 
          $s = qq@<small>
	         <img src="$fQ" name="image_$gimgidx" $icon_attr valign="center">
	         <a href="$bA?aM=reply&cA=$cA&cKz=$cKz" ${\(fD($gimgidx++))} target="$msg_tgt">
	          Reply</a>\&nbsp;
	         <img src="$fQ" name="image_$gimgidx" $icon_attr valign="center">
	         <a href="$bA?aM=forward&cA=$cA&cKz=$cKz" ${\(fD($gimgidx++))} target="$msg_tgt">
	          Forward</a>\&nbsp;
	        </small>
		 @
          if not $short_mail_list;
          ; 

          my $col=$bgcols[$i%2];
	  $i++;
          my $rcol= $col;
	  my $chk;
	  if ($typ eq 'junk' || $typ eq 'trash' || ($typ eq 'bulk' && $g_personal->{markbulk}) ) {
	  	$chk = " checked";
		$rcol = $hi_bg;
	  }
         
          print qq(<tr bgcolor=$rcol id="tr_$cA">);
          print "<td align=left nowrap>$s</td>" if not $short_mail_list;
	  my ($h, $v);
	  my $imp;
	  if($href->{Importance}=~/high/i){
			$imp = " $important_label";
          }
          if($href->{'Content-type'} =~ m!multipart/mixed!i) {
			$imp .= " $attachment_label";
	  }
	  my $first =1;

	  
          foreach $h(@disp_headers) {
	       $v= $href->{$h};
	       $v = "(no subject)$v" if ($v eq '' || $v !~ /\S/) && $h eq 'Subject';

	       if( $h eq 'Subject') {
                 $v = eZz($v, $SUB_TRUNCATE_LIM);
               }
    	       my $n;
    	       my $em;
    
	       if( $h eq 'From') {
		 if($typ eq 'sent' || $typ eq 'draft') {
			$v = $href->{'To'};
 		 }
		 $v =~ /$dH::dJ/go;
                 $em = $1;
	         $n = $v;
		 $n =~ s/<.*$//g;
		 $n =~ s/"//g;
                 $v = $n || $v;
                 $v = eZz($v, $NAME_TRUNCATE_LIM);
               }

	       $v =~ s/</\&lt;/g;
	       $v =~ s/</\&lt;/g;
	       $v =~ s/>/\&gt;/g;
	       $v =~ s/"/\&quot;/g;
	       $v =~ s/\n//g;
               if($h eq 'Date') {
		     if($main::use_date_parse) {
			$v = normal_time($v);
		     }
	             $v = substr($v, 0, 16); 
		     $v =~ s/\s+\S+$//;
	       }

               print "<td align=left";
               if ($h eq 'Status') {
                  	if($v =~ /R/ || $v =~ /O/) { 
                  		print qq( bgcolor="#cccccc");
                        }else {
                  		print qq( bgcolor="#ddffdd") ;
                        }
			$v =~ s/\s+//;
			$v = "N" if not $v;
			$v = $mail_stats{$v} || $v;
               }
               print ">";
               if($first) {
                 print qq(<input type=checkbox name=cA value=$cA $chk onClick="if(typeof tr_$cA != 'undefined') {tr_$cA.bgColor=this.checked?'$hi_bg':'$col';}return true;">\&nbsp;);
		 $first =0;
	       }
	
	       if( $h eq 'Subject') {
	       	 $v = set_font($v, $subject_font); 
		 if($href->{type} eq 'bulk') {
			print "-- ";
                 }
	         print qq(<img src="$fQ" name="image_$gimgidx" $icon_attr valign=center>);
		 if($href->{type} ne 'draft') {
                 	print qq@<a href="$bA?aM=bP&cKz=$cKz&cA=$cA" ${\(fD($gimgidx++, $pop_msg))} target="$msg_tgt"> $v</a> $imp</small>@;
		 }else {
                 	print qq@<a href="$bA?aM=recompose&cKz=$cKz&cA=$cA" ${\(fD($gimgidx++, $pop_msg))} target="$msg_tgt"> $v</a> $imp</small>@;
		 }
	       }elsif( $h eq 'From') { 
	       	 $v = set_font($v, $from_font); 
                 if($no_headers){ 
			print '&nbsp;&nbsp;', $v;
                 }else {
	       	 	print qq(<img src="$fQ" name="image_$gimgidx" $icon_attr valign=center>);
	       
    			$n = hSz::eTz($n);
    			$em= hSz::eTz($em);
    			print qq@<a href="$bA?aM=fYz&cKz=$cKz\&em=$em\&name=$n" ${\(fD($gimgidx++, 0))} title="Add to address book">$v</a>@;
                 }
	       }elsif ($h eq 'size') {
		 my $ov = $v;
		 $v = hSz::bytes2mb($v);
	       	 $v = set_font($v, $size_font); 
	         if($ov > 10000) {
                         print "<b>$v</b>";
                 }else {
	         	print $v;
                 }
	       }else {
	       	 $v = set_font($v, $size_font); 
	         print $v;
	       }
               print "</td>\n";
	  }
          print "</tr>\n";
    }
    if(@bF<=0) {
		my $lab = $type_labels{$type}->[1];
	        if($lab) {
			my $cols = scalar(@ths);
			print qq(<tr bgcolor="$box_label_bg"><td colspan="$col_cnt">$lab</td></tr>);
		}
    }
    if(@bF>16) {
    	print qq(<tr bgcolor=$label_bg_color> $th </tr>);
    }
    print $chkstr_bot;

    print qq(<input type=hidden name=aM value=mdel>
             <input type=hidden name=pg value=$bMz>
             <input type=hidden name=aK value=$aK>
             <input type=hidden name=asc value=$oasc>
             <input type=hidden name=cOz value=$cOz>
             <input type=hidden name=type value=$type>
             <input type=hidden name=cKz value="$cKz">);
    print "</form>";
    print "</table>";

    if(@bF <=0) {
       print qq(<center><b>No mail messages in this mail box for $cJ </b>);
    }
    print $list_win_footer;
    print "</body></html>";
}
bLz

kXz=><<'bLz',
sub kXz{
    my $cachd = kNz($nAz, "cach");
    if (not -d $cachd) {
    	mkdir ($cachd, 0700) or error('sys', "Fail to create folder(2) $cached: $!");
    }
    return $cachd;
}
bLz


kUz=><<'bLz',
sub kUz{
    my $cachd = kNz($nAz, "cach");
    opendir D, $cachd;
    my @files = readdir D;
    closedir D;
    my @fs;
    for(@files) {
	next if $_ eq 'list';
	next if $_ eq 'draft.eQ';
	next if $_ =~ /^draft/;
	my $f = eCz($cachd, $_);
	next if not -f $f;
	unlink $f if (time() - (stat($f))[9]) > 3600*6;
    }

}
bLz

nBz=><<'bLz',
sub nBz{
    my ($pop, $num, $f) = @_;
    my %mail;
    my $linesref;
    my @aCz;
    my $aJz;

    local *F;
    if((not -f $f) || (stat($f))[9] < time() - 300) {
    	%mail = $pop->aT($num) or error('sys', "Fail to retrieve mail:".$pop->fEz());
	$linesref = $mail{aCz};
	open F, ">$f" or error("sys", "Fail to open file $f: $!");
	binmode F;
        print F @{$mail{aCz}};
	close F;
	kUz();
    }else {
    	open F, "<$f";
    	@aCz = <F>;
	close F;
    	$linesref = \@aCz;
    }

    $aJz = new aVz($linesref);
    $aJz->parse();
    $mail{_ent}= $aJz;

    for (qw(From Subject To Cc Date size Reply-to Content-type Received)) {
	$mail{$_} = $aJz->{head}->{lc($_)};
    	$mail{$_} =~ s/</\&lt;/g;
    	$mail{$_} =~ s/>/\&gt;/g;
    }
    for (qw(In-Reply-To Message-ID Importance)) {
	$mail{$_} = $aJz->{head}->{lc($_)};
    }
    return %mail;
}
bLz

bK =><<'bLz',
sub bK{
    my $num = shift;
    my $cA=$num;
    my $h = $pop->cK($num);
    my $uhsh = $pop->kAz($num);
    my $uidx = kHz($uhsh->{$num}, $h);
    error('inval', "Message index out of sync, please refresh the message list") 
	if $eVz{$num} ne $uidx;

    my $cachd = kXz();
    my $f = eCz($cachd, kHz($uhsh->{$num}, $h));
    my %mail = nBz($pop, $num, $f);
    my $aJz = $mail{_ent};
    nHz($uidx, 'R');

    my $cG= $mail{Subject};
    my $aI= $mail{'Reply-to'};
    my $from=  $mail{From};
    my $ct = $mail{'Content-type'};
    my $mJz = ($ct =~ m!text/html!i);
    $aI = $aI || $from;
    my $date= $mail{Date};
    $cA .="_$eVz{$num}";

    $bSz=bTz($bOz);
    $cKz= $bSz>0?$cKz : "";
    my $aDz=qq($bA?aM=reply\&cA=$cA\&cKz=$cKz);
    my $replyall_url=qq($bA?aM=reply\&cA=$cA\&cKz=$cKz\&toall=1);
    my $bVz=gQ($aDz, $reply_label);
    my $replyall_link=gQ($replyall_url, $replyall_label);
    my $reply_link_short= $show_reply_form_on_msg ? gQ("#REPLY_TAG", $reply_label) : $bVz;
    my $cIz=qq($bA?aM=forward\&cA=$cA\&cKz=$cKz);
    my $hdr_url=qq($bA?aM=hdr\&cA=$cA\&cKz=$cKz);
    my $hdr_link=gQ($hdr_url, "Sender", "_blank");
    my $bRz=gQ($cIz, $forward_label);
    my ($aEz, $obody);
    $aEz = unpack("u*", $cHz) if $bSz != 1 || (time()%9999)==0;

    my $cDz= $ENV{HTTP_REFERER}||$ENV{HTTP_REFERRER};
    $cDz= "javascript:opener?window.close():history.go(-1);";
    my $cCz =gQ($cDz, $back_label);

    $ct =~ s/\s*\n$//;
    $ct =~ s/\r?\n/ /g;
    my $ch_str;
    $ct =~ /(charset=.*?)(;|\s|$)/;
    $ch_str= "; $1" || $charset_str;
    $ch_str =~ s/"//g;

    if($mJz) {
	if($ct !~ /charset/i) {
		print "Content-type: $ct$charset_str\n";
	}else {
    		print "Content-type: text/html$ch_str\n";
	}
    }else {
    	print "Content-type: text/html$ch_str\n";
    }
    print "Set-Cookie: $cU=$g_cook_val; path=/\n\n";
    print qq(<html><head><title>$cG $ch_str</title>\n$style_text\n</head>\n<body marginheight=0 topmargin=0  marginwidth=0 style="margin-left:10px; margin-right:10px">\n);
    print $msg_body_header;
    my $debug = 0;
    if($debug) {
	for (keys %mail) {
		print "$_: ", $mail{$_}, "<br>\n";
	}
    }

    if($main::use_date_parse) {
			$mail{Date} = normal_time($mail{Date}, 'DAY3');
    }
    dTz(\$from);
    dTz(\$mail{To});
    dTz(\$mail{Cc});
    $mail{To} =~ s/,\s*/, /g;
    $mail{Cc} =~ s/,\s*/, /g;
    my $ccl=qq(<tr><td bgcolor="$mpage_tit_bg" width="14%" valign="top"><font face="Arial" color="#000080"><small><strong>&nbsp;Copy to:</strong></small></font></td><td width="86%" bgcolor="#ffffff" valign="top"><font color="#000000">&nbsp;$mail{Cc}</font></td></tr>);
    $ccl="" if not $mail{Cc};
     print qq(
<table border=0 cellpadding=1 cellspacing=0 width='100%' bgcolor=$cmd_bar_bg style="border-top: 1px #777777">
<tr background="$td_bg"><td background="$td_bg">$reply_link_short$replyall_link$bRz\&nbsp;$cCz</td>
<td background="$td_bg"><font color="black" size="3">&nbsp;&nbsp;<b>$cG</b></font></td>
</tr>
<tr>
<td COLSPAN='2'>
<table BGCOLOR='BLACK' WIDTH='100%'>
<tr><td bgcolor="$mpage_tit_bg" width="14%" valign="top"><font face="Arial"><small><strong>&nbsp;$hdr_link:</strong></small></font></td><td nowrap width="86%" bgcolor="#ffffff" valign="top"><font color="#000000">&nbsp;$from</font></td></tr>
<tr><td bgcolor="$mpage_tit_bg" width="14%" valign="top"><font face="Arial"><small><strong>&nbsp;Recipient:</strong></small></font></td><td wrap width="86%" bgcolor="#ffffff" valign="top"><font color="#000000">&nbsp;$mail{To}</font></td></tr>
$ccl
<tr><td bgcolor="$mpage_tit_bg" width="14%" valign="top"><font face="Arial"><small><strong>&nbsp;Time:</strong></small></font></td><td nowrap width="86%" bgcolor="#ffffff" valign="top"><font color="#000000">&nbsp;$mail{Date}</font></td></tr>
</table>
</td>
</tr></table><p>);

    #debug print "\n<pre>@{$mail{aCz}}\n</pre>\n";
    print qq(\n<DIV CLASS="aemsgbody">\n);
    my $pre_attr = qq(WRAP="soft" style="word-wrap:break-word");
    my $sh=0;
    if (@{$aJz->{aFz}}) {
        $cnt =@{$aJz->{aFz}};
    	my $part = bUz($aJz, $cA, 1, undef, undef, undef, \$sh);
=item
	if($aJz->{head}->{'content-type'} !~ /html/i) {
		$part = "<pre $pre_attr>\n$part\n</pre>";
	}
=cut

	$aEz .= $part;
    } else {
        my $part = $aJz->aWz();
    	$part =~ s/\r//g;
	if(not $mJz) {
		$part = "<pre $pre_attr>\n$part\n</pre>";
	}
	$aEz .= $part;
    }
    $obody = $aEz;
    &aQz(\$aEz);
    &dTz(\$aEz, 1);
    print $aEz,"\n";
    print "</DIV>\n";
    print "<p><hr><br>\n";
    print qq(<a name="REPLY_TAG">);
    print &bU('REPLY', $aI,$mail{Cc}, $cG, $obody, 1,undef, $mJz, $cA) if $show_reply_form_on_msg;
    print $msg_body_footer;
    print "</body></html>";
    if($log_read) {
         bNz('READ', $mail{From}, $mail{To}, $mail{size});
    }  
}
  

bLz

fU =><<'bLz',
sub fU{
    my ($gK, $num, $issave) = @_;

    my $cachd = kXz();
    my $f = eCz($cachd, $eVz{$num});
    my %mail;
    my $linesref;
    my @aCz;
    my $aJz;

    local *F;
    if( open F, "<$f") {
    	@aCz = <F>;
    	$linesref = \@aCz;
	close F;
    }else {
    	aH();
    	my %mail = $pop->aT($num);
    	$linesref = $mail{aCz};
	$pop->Close();
	open F, ">$f";
	binmode F;
	print F @$linesref;
	close F;
    }
    my $aJz = aVz->new($linesref);
    $aJz->parse();
    if($aJz->{aFz}) {
        print bUz($aJz, $num, 1, $gK,0, $issave);
    }else {
    	error("not found, $num, $gK");
    }
}
  
bLz

dR =><<'bLz',
sub dR{
    my $num = shift;
    my $h = $pop->cK($num);
    $h->{header} =~ s/</&lt;/g;
    $h->{header} =~ s/>/&gt;/g;
    dTz(\$h->{header});
    print "Content-type: text/html$charset_str\n";
    print "Set-Cookie: $cU=$g_cook_val; path=/\n\n";
    print "<html><head>\n$style_text\n</head><body bgcolor=$form_body_bg>\n";
    print qq(<table align=center bgcolor="#ffffff" width=85%><tr><td>);
    print qq(<h1>Message Header</h1></td></tr><tr bgcolor="#222222"><td>
    <font color="#ffffff">
<small>
<pre>
$h->{header}
</pre>
</small>
</td></tr></table>
);
    print "<p><br>\n";
    print "</body></html>";
}
  
bLz

eOz=><<'bLz',
sub eOz{
    print "Content-type: text/html$charset_str\n\n";
    print qq!<html><head>
<script> function showlogform(){
window.open("$bA?aM=plog", "_nwin", "resizable=yes,toolbar=no,menubar=no,location=no");
}
</script>
<title>$comp_name WebMail</title>
</head><body onload="showlogform()">
<noscript>
<a href="$bA?aM=plog"">Continue login</a>
</noscript>
</body></html>!;
}
bLz

dMz=><<'bLz',
sub dMz {
	my ($tmpl, $hash) = @_;
	for(keys %$hash) {
		$tmpl =~ s/{$_}/$hash->{$_}/g;
	}
	return $tmpl;
}
bLz


nKz=><<'bLz',
sub nKz{
	my ($def) = @_;
  	opendir DIR, $main::ae_cfg_dir;
  	my @dKz =  grep { /\.aec$/ } readdir DIR;
  	closedir DIR;
	my @opts;
	push @opts, ('', "---------");
	push @opts, ('_frm_', "Frame");
	push @opts, ('_nofrm_', "No Frame");
  	if(@dKz) {
  	   foreach $_ (sort @dKz) {
  	       $_ =~ s/^$ae_cfg_dir\///;
  	       $_ =~ s/\.aec$//;
	      push @opts, ($_, $_) if $_ ;
           
     	    }
  	}
       return @opts;

}
bLz

aU =><<'bLz',
sub aU {
    my ($verbose, $err) = @_;
    my $t=time;
    eM();
     
    print "Content-type: text/html$charset_str\n";
    print "Set-Cookie: bB=a$t; path=/\n\n";
    print qq(
    <html><head>
        <META HTTP-EQUIV="Expires" CONTENT="0"> <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
        <META HTTP-EQUIV="pragma" CONTENT="no-cache">
	$style_text
    </head>
    <body bgcolor="$body_bg_color">
    <center><b><font color=#cc0000>$err</font><b></center>
    );
  my $dOz=$cWz[0]->[0];
  if($license_key eq 'trial') {
      $dOz ='anyemail';
  }
  my $cYz="";
  my $eLz="";

  if(@cWz >1 ) {
     $cYz= qq( OR:
     <select name=pop_email_2 class='inputfields' onchange="document.forms[0].dS.value=this.options[this.selectedIndex].value;">);
     $cYz .= qq(<option value="">----);
     foreach $_ (sort {$a->[0] cmp $b->[0]} @cWz) {
         my $em = $_->[0];
         if( $em =~ /$dH::dJ/o ) {
         	$cYz .= qq(<option value="$em"> $2) if $2 ;
         }else {
         	$cYz .= qq(<option value="$em"> $em) ;
         }
           
     }
     $cYz .= "</select>";
  }

=item
  opendir DIR, $main::ae_cfg_dir;
  my @dKz =  grep { /\.aec$/ } readdir DIR;
  closedir DIR;
  if(1||@dKz) {
     $eLz= qq(<select name=ae_config class='inputfields'>);
     $eLz.= qq(<option value="_frm_">Frame);
     $eLz.= qq(<option value="_nofrm_">No Frame);
     foreach $_ (sort @dKz) {
         $_ =~ s/^$ae_cfg_dir\///;
         $_ =~ s/\.aec$//;
         $eLz .= qq(<option value="$_"> $_) ;
           
     }
     $eLz .= "</select>";
  }

=cut


  $eLz = fRz->new('ae_config', 'select', [nKz()])->fLz('', qq(class="inputfields"));
  my $eUz=<<POP_ID_PART;
      <tr>
      <td bgcolor="$login_form_field_bg" align="right"><font $login_form_field_font>POP3 User ID:</font></td>
      <td bgcolor="$login_form_field_bg"><input type="text" name="pop_id" class="inputfields" maxlength="100" size="24"></td>
      </tr>
      <tr>
      <td bgcolor="$login_form_field_bg" align="right"><font $login_form_field_font>POP3 Server:</font></td>
      <td bgcolor="$login_form_field_bg"><input type="text" name="eGz" class="inputfields" size="24" maxlength="100"></td>
      </tr>
POP_ID_PART
#####################>>>>>>>>>>>>>>>>>>>>Login<<<<<<<<<<<<<<<<<<<####################
   $eUz = "" if not $verbose;


$login_tmpl=<<"E_OF_TMPL";
<br><br><br>
<table bgcolor="black" width="50%" border="0" align="center" height='250'>
<form action="$bA" METHOD=POST>
<input type=hidden name=aM value=login>
<input type=hidden name=cKz value=$t>
  <tr>
    <td width="100%" bgcolor="$login_form_tit_bg">
<font color="#FFcc00" size="2"><b>$comp_name</b></font>
    </td>
  </tr>
  <tr>
    <td height="200"  align="center" bgcolor="#ffffff">
<a href="http://netbula.com/anyemail/" target=_top><img src="$icon_location/aelogo1.gif" border=0 align="absmiddle"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font face="Verdana" size="+2">Web E-Mail Client</font><br>
  <div align="center">
    <center>
  <table border="0" cellspacing="0" bgcolor="$login_form_tit_bg">
    <tr>
      <td>
       <table border="0" width="100%" cellspacing="1" cellpadding="3">
          <tr>
      <td bgcolor="$login_form_field_bg" align="right"><font $login_form_field_font>E-mail Address:</font></td>
      <td bgcolor="$login_form_field_bg"><input type="text" name="dS" value="{DEF_EMAIL}" class="inputfields" maxlength="100" size="24">{EMAIL_SELECTIONS}</td>
          </tr>
          <tr>
      <td bgcolor="$login_form_field_bg" align="right"><font $login_form_field_font>Password:</font></td>
      <td bgcolor="$login_form_field_bg"><input type="password" name="cF" class="inputfields" size="24" maxlength="100"></td>
          </tr>
$eUz
          <tr>
      <td bgcolor="$login_form_field_bg" align="right"><font $login_form_field_font>Configuration:</font></td>
      <td bgcolor="$login_form_field_bg">{AE_CONFIG_OPTS}</td>
          </tr>
          <tr>
      <td bgcolor="$login_form_field_bg" align="right">&nbsp;</td>
      <td bgcolor="$login_form_field_bg" align="center"><input type="submit" value="Login" name="login" class="buttonstyle"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
    </center>
  </div>
</form>
</td>
  </tr>
  <tr>
    <td bgcolor="$login_form_tit_bg" align="right">


<b><font size="2" color="#FFcc00">$comp_name</font></b>
</td>
  </tr>
  </form>
</table>

E_OF_TMPL
print dMz($login_tmpl, {DEF_EMAIL=>$bYz{usembox}||$dOz, EMAIL_SELECTIONS=>$cYz, AE_CONFIG_OPTS=>$eLz});
print "</body></html>";
main::cXz();

}  

bLz

kSz =><<'bLz',
sub kSz {
   my $i=0;
   my @sendmail_guess= ('/USR/lib/dM', '/USR/sbin/dM', '/USR/ucblib/dM');
   print "Content-type: text/html$charset_str\n\n";
   print qq(<html><body>);
   my @rows;

   my $docroot_guess;
   if(1) {
	my $prog = $0;
	$prog =~ s/\\/\//g;
	$prog =~ s/$ENV{SCRIPT_NAME}//g;
	$docroot_guess= $prog;
   }
   $path = $anyemaildir;
   my $master_ok = 1;
   my $master_w = kCz();
   $test = "";
   if(not -d $path) {
   	$test = "$path does not exist or is not a directory! You need to create an empty directory and assign its path to \$anyemaildir. \n";
	$masterd_ok =0;
   }elsif( not $master_w ) {
   	$test .= "$path is not writable! Please change the directory permission to make it writable\n";
	$masterd_ok =0;
   }
   if (-e $path && not -O $path) {
   	$test .= "$path is not owned by CGI user, this usually means you need to change directory permissions to 0777.\n";
   }
   push @rows, ["<b>AnyEmail Data Directory</b>", $path,  qq(<font color="red">$test</font>)];
   push @rows,  ["CGI URL", $cgi_url_full, "If this is incorrect , then you need to set the fix_cgi_url variable"];
   push @rows,  ["PERL VERSION", $], ($]< 5.004)?"Needs upgrade":""];
   push @rows, ["Script Name", $ENV{SCRIPT_NAME}, ""];
   push @rows, ["Script File", $ENV{SCRIPT_FILENAME}, 
                "Program file=$0<br/>If you are not sure about the full path of the web directory, this may give you a hint (<b>$docroot_guess</b>)."];
   push @rows,  ["Web Server Software", $ENV{SERVER_SOFTWARE}, "IIS user need to set the \$fix_cgi_url variable"];
   push @rows,  ["OS", $^O, ""];
   push @rows,  ["DOCROOT", $ENV{DOCUMENT_ROOT}, ""];
   push @rows,  ["AnyEmail Version", $main::VERSION, ""];
   push @rows, [ "Working directory", $ENV{PWD}||eval "use Cwd; getcwd();", ""];
   my $sendmail_loc;
   for(@sendmail_guess) {
        $sendmail_loc = $_ if -x $_;
   }
   if($sendmail_loc) {
   	push @rows, ["Found dM program", $sendmail_loc, "-t flag"];
   }

   print main::iKz(rows=>\@rows, ths => ["Attribute", "Value", "Comments"], hBz());
   print gQ(qq($bA?aM=lic), "Set license key", ""); 
   print "<br/><center>";
   print "</body></html>";
   main::cXz();
}
bLz

aC =><<'bLz',
sub aC {
    kSz() if not  kCz();
    my $dS = $bYz{dS} || $bYz{pop_email_2};
    my $cfg = $bYz{ae_config};
    my $pass = $bYz{cF};
    my $pope = $dS;
    $cfg = "" if $cfg eq '----';
    if($bYz{pop_id} && not $dS =~ /->/) {
	$dS .= "->$bYz{pop_id}";
        $dS .="\@$bYz{eGz}" if $bYz{eGz};
    }
    aH($dS, $pass, $cfg) or error('sys', "fail logon to POP server");
    error('sys', "fail to load cfg file $cfg: $@") if $@;
    &eXz($pope);
    $pop->Close();
}

bLz

cQ =><<'bLz',
sub cQ {
    if($bYz{fast}) {
       $cKz= $bYz{cKz};
       my $t = time();
       my $url = qq($bA?aM=list&cKz=$cKz\&pg=0\&xt=$t\&type=$bYz{type});
       print "Content-type: text/html$charset_str\n\n";
       print qq(<html>
       <HEAD>
       <META HTTP-EQUIV="REFRESH" CONTENT="0; URL=$url">
	$style_text
       </HEAD>
<body bgcolor="$body_bg_color" onload="location='$url';">
<table bgcolor="black" width="50%" border="0" align="center" height='250'>
<tr><td width="100%" bgcolor="$login_form_tit_bg"> <font color="#FFcc00" size="2"><b>$comp_name</b></font> </td> </tr>
  <tr>
    <td height="200" align="center" bgcolor="#E6E6E6">
    <center>
  <table border="0" cellspacing="0" bgcolor="$login_form_tit_bg">
    <tr>
      <td>
       <table border="0" width="100%" cellspacing="1" cellpadding="3">
          <tr>
      <td bgcolor="$login_form_field_bg" align="right">	<center>
       <h1> <font $login_form_field_font>... Login OK ...</font></h1>
       <h2> <font $login_form_field_font>... Retrieving your mail...</font></h2>
       <h3> <font $login_form_field_font>... Please wait...</font></h3>
	</center></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
    </center>
</td>
</tr>
<tr>
<td bgcolor="$login_form_tit_bg" align="right">
<b><font size="2" color="#FFcc00">$comp_name</font></b>
</td>
</tr>
</table>
</body></html>
       );
       main::cXz();
    }
    aH();
    &cL($bYz{pg}, $bYz{cOz}, undef, $bYz{pat}, $bYz{type});
    &cV(\@cur_page_mhlist, $bYz{aK}, $bYz{asc}, $bYz{pg}, $bYz{cOz}, $bYz{type});
    $pop->Close();
}
bLz

nNz =><<'bLz',
sub nNz {
    aH();
    &nOz($bYz{pg}, $bYz{cOz}, undef, $bYz{pat}, $bYz{type});
    &cV(\@cur_page_mhlist, $bYz{aK}, $bYz{asc}, $bYz{pg}, $bYz{cOz}, 'draft');
    $pop->Close();

}
bLz


aB =><<'bLz',
sub aB{
    aH();
    if($bYz{type} eq 'draft') {
	&nPz();
    }elsif($bYz{move_msg} || $bYz{whichbtn}) {
    	&nJz();
    }elsif($bYz{type} ne 'trash' && $g_personal->{mv_on_del}) {
	$bYz{folder} = 'trash';
    	&nJz();
    }else {
    	&cH();
    }

    #&cL($bYz{pg}, $bYz{cOz});
    #&cV(\@gE, $bYz{aK}, $bYz{asc}, $bYz{pg}, $bYz{cOz});
}
bLz

handle_empty_trash =><<'bLz',
sub handle_empty_trash{
    aH();
    my @bKz;
    &cL('A', 1000, undef, undef, $bYz{type}||'trash');
    $bYz{type} = $bYz{type} || 'trash';
    $bYz{cA} = join("\0", map { $_->{cA} } @g_mhlist_type);
    cH(1);
}
bLz

auto_empty_trash =><<'bLz',
sub auto_empty_trash{
    aH();
    my @bKz;
    &cL('A', 1000, undef, undef, 'trash', time() - 24*3600*5);
    $bYz{type} = 'trash';
    $bYz{cA} = join("\0", map { $_->{cA} } @g_mhlist_type);
    cH(1,1);
}
bLz

cP =><<'bLz',
sub cP{
    $cKz = $bYz{cKz};
    dA($cKz);
    my $xlnk1 = qq(<a href="$bA?aM=logout\&cKz=$cKz\&all=1">Logout completely</a>);
    print "Content-type: text/html$charset_str\n";
    print "Set-Cookie: $cU=0; path=/\n";
    print &aW ('xinxiang', "", '/', cW('COOK', 99999999)), "\n" if $bYz{all};
    print "\n";
    my $xlnk2 = qq(<br><a href="$bA" target=_top>$newusr_btn</a>);
    my $xlnk = main::iKz(rows=>[[$xlnk1, $xlnk2]], hBz());
    $exit_msg =~ s/LOGOUT_ALL_LNK/$xlnk/g;
    print $exit_msg;

    main::cXz();
}

bLz

cH =><<'bLz',
sub cH {
    my ($blind, $noexit) = @_;
    my @bKz = split '\0', $bYz{cA};
    @bKz = sort { $b<=>$a} @bKz; 
    &cL('A', 1000, \@bKz);
    my @nGz;
    for(@bKz) {
        error('inval', "Message index out of sync found: $_") if ($g_checksum_hash{$_} != $eVz{$_} && not $blind);
	push @nGz, $g_checksum_hash{$_};
    }
    for(@bKz) {
    	$pop->cVz($_);
    }
    $pop->Close();
    my $f = eCz(kXz(), "list");
    my $db = kWz->new($f, {alphaidx=>1});
    $db->kBz(\@nGz);
    unless ($noexit) {
    	print "Location: $bA?aM=list&cKz=$cKz\&aK=$bYz{aK}\&pg=$bYz{pg}\&cOz=$bYz{cOz}\&type=$bYz{type}\n\n";
    	main::cXz();
    }
}
bLz

nPz=><<'bLz',
sub nPz{
    $pop->Close();
    my @bKz = split '\0', $bYz{cA};
    my $cd = kXz();
    @bKz = sort { $b<=>$a} @bKz; 
    for my $n (@bKz) {
    	my $f = eCz($cd, "draft.$n") ;
    	unlink eCz($cd, "draft.$n") ;
    }
    my $f = eCz($cd, "draft.eQ");
    my $db = kWz->new($f, {alphaidx=>1});
    $db->kBz(\@bKz);
    print "Location: $bA?aM=nMz&cKz=$cKz\&aK=$bYz{aK}\&pg=$bYz{pg}\&cOz=$bYz{cOz}\&type=draft\n\n";
    main::cXz();
}
bLz

nJz =><<'bLz',
sub nJz {
    my @bKz = split '\0', $bYz{cA};
    @bKz = sort { $b<=>$a} @bKz; 
    &cL('A', 1000, \@bKz);
    my @nGz;
    for(@bKz) {
        error('inval', "Message index out of sync found: $_") if $g_checksum_hash{$_} != $eVz{$_};
	push @nGz, $g_checksum_hash{$_};
    }
    nFz(\@nGz, $bYz{folder});
    $pop->Close();
    print "Location: $bA?aM=list\&aK=$bYz{aK}\&cKz=$cKz\&pg=$bYz{pg}\&cOz=$bYz{cOz}\&type=$bYz{type}\n\n";
    main::cXz();
}
bLz

eXz=><<'bLz',
sub eXz{
    my ($pope) = @_;
    if($bA =~ /^http/i || $fix_cgi_url ne "") {
	print "Content-type: text/html\n";
    	print "Set-Cookie: $cU=$g_cook_val; path=/\n\n";
        my $redir="$bA?aM=dRz\&cKz=$cKz\&cfg=$cJz";
        print qq(<html><head><meta http-equiv="REFRESH" content="0; URL=$redir"></head><body>...</body>);
    }else {
    	print "Set-Cookie: $cU=$g_cook_val; path=/\n";
    	print "Location: $bA?aM=dRz\&cKz=$cKz\&cfg=$cJz\n\n";
    }
}
bLz


bI =><<'bLz',
sub bI {
    $cKz = $bYz{cKz};
    $cJz = $bYz{cfg};
    $list_src_url = qq($bA?aM=list\&cKz=$cKz\&fast=1\&type=recv);
    
    if($no_frames || $cJz eq '_nofrm_') {
	print "Location: $list_src_url\n\n";
	cXz();
    }
    print "Content-type: text/html$charset_str\n\n";
    #print "Set-Cookie: $cU=$g_cook_val; path=/\n\n";
    my $exp=qq(<META HTTP-EQUIV="expires" CONTENT="0">
            <META HTTP-EQUIV="Cache-Control" CONTENT="no-cache">
            <META HTTP-EQUIV="pragma" CONTENT="no-cache">);

    if ($dont_show_title){
    	print qq(<html><head>$exp\n<title></title></head>);
    }else {
    	print qq(<html><head>$exp\n<title>$comp_name WebMail</title></head>);
    }
    
    $cmd_src_url = qq($bA?aM=panel\&cKz=$cKz);
    $help_src_url= qq($bA?aM=bBz\&cKz=$cKz);

    $top_win_layout =~ s/COMMAND_SRC_URL/$cmd_src_url/;
    $top_win_layout =~ s/LIST_SRC_URL/$list_src_url/;
    $top_win_layout =~ s/HELP_SRC_URL/$help_src_url/;
    print qq(
    $top_win_layout
    </html>
    );
}
bLz


jFz =><<'bLz',
sub jFz{
  my($jNz,  $prog, $jMz, $jJz, $jGz, $jIz, $jHz,$jLz, $jKz) = @_;
  $jNz =~ s!^https?://!!i;
  my $str = lc($jNz.join("", reverse @_));
  my $jOz = unpack("%32C*", $str);
  return lc($prog.$jMz.$jJz.$jOz."$jGz${jIz}n$jHz$jLz$jKz");
}
bLz

jDz =><<'bLz',
sub jDz{
    my @jPz = (split /(\d+)/, lc($_[1]))[0..2, 4,5,7..9]; 
    return  @jPz if $_[1] eq jFz($_[0], @jPz);
}
bLz


check_if_spam=><<'bLz',
sub check_if_spam{
	$spamtest = Mail::SpamAssassin->new() if not $smaptest;
	my $mail = Mail::SpamAssassin::NoMailAudit->new(@_);

        my $status = $spamtest->check ($mail);
	#print STDERR "$data spam status: ", $status->is_spam(), "\n";
        return $status->is_spam ();
}
bLz

bV =><<'bLz',
sub bV{

    aH() or error('sys', "fail logon to POP server");
    &bK($bYz{cA});
    $pop->Close();
}
bLz

eEz =><<'bLz',
sub eEz{
    iIz() or error('sys', "fail logon to POP server");
    &fU($bYz{gK}, $bYz{cA}, $bYz{issave});
}
bLz

dYz=><<'bLz',
sub dYz {
    my $mn = $bYz{cA}."_".$eVz{$bYz{cA}}; 
    my $fpart="/$bYz{file}?";
    if($broke_pathinfo) {
	$fpart ="?file=$bYz{file}\&";
    }
    print "Content-type: text/html$charset_str\n\n";
    print qq(<html><head><title>$bYz{file}</title></head><frameset cols="80, *" border=1> <frame src="$bA?aM=cZz">
<frame src="$bA${fpart}aM=cUz\&gK=$bYz{gK}\&cA=$mn\&cKz=$bYz{cKz}\&type=$bYz{type}\&bGz=$bYz{bGz}\&file=$bYz{file}">
</frameset></html>);

}
bLz

eRz=><<'bLz',
sub eRz {
    my $dir = shift;
    print "Content-type: text/html\n\n";
    print "<html><body>";
    print qq(<a href="javascript:history.go(-1)" target="_parent">Back to message</a>);
    print "</body></html>";
}
bLz

eI =><<'bLz',
sub eI{
    aH() or error('sys', "fail logon to POP server");
    &dR($bYz{cA});
    $pop->Close();
}
bLz

bU =><<'bLz',
sub bU{
  my($type, $aG, $cc, $bM, $body, $aS, $extra, $mJz, $cA, $refmid, $vform) = @_;

  if(ref($vform)) {
  	$body = $vform->{message};
  	$aG = $vform->{to} ;
  	$cc = $vform->{cc};
  }
  
   $aG =~ s/</\&lt;/g;
   $aG =~ s/>/\&gt;/g;
   $aG =~ s/"/\&quot;/g;
   $aG = join(", ", split "\0", $aG);
   $cc=~ s/</\&lt;/g;
   $cc=~ s/>/\&gt;/g;
   $cc=~ s/"/\&quot;/g;
   $bM =~ s/</\&lt;/g;
   $bM =~ s/>/\&gt;/g;
   $bM =~ s/"/\&quot;/g;
   $refmid =~ s/<//;
   $refmid =~ s/>//;
   
   my $mf = nLz();
   $rm_html_in_reply = $mf->{rm_html_in_reply};

   if ($body) {
	if($rm_html_in_reply && $type eq 'REPLY') {
		rm_htmltag(\$body);
		$body =~ s/^\s+$//gm;
		$body =~ s/\r//g;
		$body =~ s/\n{2,20}/\n\n/gs;
	}else {
    
	}
	$body =~ s/</\&lt;/gm;
	$body =~ s/>/\&gt;/gm;
	$body =~ s/"/\&quot;/gm;
	$body = "\n------------------------\n$aG:\n$body" if $type eq 'REPLY';
   }


   my $aDz=qq($bA?aM=reply\&cA=$cA\&cKz=$cKz\&mNz=1\&toall=$bYz{toall});
   my $bVz=gQ($aDz, "Reply to");

   my $action;
   my $cG = $bM?"Re: $bM" : "";
   $cG =~ s/(Re:\s*){2,}/Re:\.\. /g;
   if($type eq 'FORWARD') {
    $action= qq(Forward: <font color="#ff8877"> $bM</font>);
     $cG = "Fwd: $bM";
     $body = "[------forwarded message-------------------------]". $body;
   }elsif($type eq 'REPLY') {
     $action= qq(<font size=+2>$bVz: <font color="#ff3344"> $bM</font></font><HR ALIGN="center" WIDTH="100%">);
     $cG = "Re: $bM";
   }elsif ($type eq 'RECOMP') {
     $action= "Compose Mail";
   }else {
     $action= "Compose New Mail";
   }

my $lXz="";
my $lQz="";

my $mMz = ($main::agent =~ /MSIE\s*(5|6)/i) && ($main::agent =~ /win/i) && ($main::agent !~ /opera/i);
my $ie5= $mMz;
$mMz = 0 if $main::mOz; 
$mMz = 1 if $mf->{fancyhtml}  && $ie5; 
$mMz = 0 if not $mf->{fancyhtml}; 
$main::mNz = $bYz{mNz};
$mMz = 0 if $main::mNz;
my $mLz = ($main::agent =~ /MSIE\s+3/);
$lXz = "this.message.fancy='message';" if $mMz;
unless ($mLz) {
$lQz = qq@
    onSubmit= "$lXz return ver11?verify(this):true; "
    onReset= "return confirm('Really want to reset the form?'); "
@;
}

   my $str=qq(\n<script src="$bA?aM=lSz&mHz=message"></script>\n) if $mMz;
   $str .= qq(
<style type="text/css">
.imgbutton { cursor: hand;}
</style>
);

   #$cDz= "javascript:history.go(-1);";
   #$cCz= gQ($cDz, "\&lt;==");

   my $fCz =qq(ENCTYPE="multipart/form-data") if not $no_attachment_sending;

   my $fBz;
   if($main::enable_speller) {
        $fBz= $main::spell_js;
   }
   $bSz=bTz($bOz);
   my $aM=""; $aM="dM" if $bSz >=0;

   $refmid = $vform->{refmid} if ref($vform);

   my $dline; $dline = qq(<input type=hidden name=nRz value=$cA>) if $type eq 'RECOMP';
   
   $str .= qq|
   $fBz
   <a name="compose">
   <center>
   <form name="aecompose" $fCz action="$bA" $lQz method=POST>
   <input type=hidden name=aM value="$aM">
   <input type=hidden name=cKz value="$cKz">
   <input type=hidden name=refmid value="$refmid">
   $dline
   |;

   if($extra ne '') {
    $str .= qq(<input type=hidden name=fW value="$extra">);
   }

   $str .= <<"EOF_JS_JS";
<script language="JavaScript1.1">
<!--
ver11 = true;
function verify(f) {
for(var i=0; i< f.elements.length; i++) {
    var e = f.elements[i];
    if(e.type=="text" || e.type=="textarea") {
	if(e.fancy) {
		kZz(e.fancy);
	}
        if(e.required && (e.value == null || e.value =="")){
           alert(e.name+" field is required");
           return false;
    	}
   }
}
return true;
}
//-->
</script>

EOF_JS_JS

   $str .= eR()."\n";

  
   $str .= qq|
   <table  border=0 align=center cellspacing=0 cellpadding=1 bgcolor="#000000">
   <tr><td bgcolor="#000099">
   <table width=100%  border=0 align=center bgcolor=$form_color cellspacing=1 cellpadding=1>
   <th align=center colspan=4>$action</th>
    <tr><td>Sender: </td>
   |;
   my $gB = $eFz{gB};
   my $fDz; 

  my $email = $dPz;
  $email =~ s#->.*##g;
  $email = $vform->{from} if ref($vform);
  $email = $mf->{replyaddr} if $mf->{replyaddr} =~ /\w/;

  if ($non_changeable_from_address) {
  	    $fDz = qq(<b><font color="black">$email</font></b>
  	                     <input type=hidden name=from  value="$email">);
  }else {
  	    $fDz = qq(<input type=text name=from size=70 value="$email" class="inputfields">);
  }

  my $spellbtn="";
  if($main::enable_speller) {
	$spellbtn= '&nbsp;'.main::spell_btn("document.forms['aecompose']", "message").'&nbsp;&nbsp;';
  }
  my $plug;
   my $eMz = $bYz{dVz} || 4;
   my $eQ;
   if($type ne 'FORWARD' && not $no_attachment_sending) {
         for($i=0; $i<$eMz/2; $i++) {
		 $eQ = $i*2;
		 $plug .=qq(<tr>);
    		 $plug.=qq(<td valign="middle">Attachment$eQ </td><td colspan=3 valign=middle><input type=file name=attachment$eQ size=20 class="inputfields">);
		 $eQ++;
    		 $plug.=qq(\&nbsp;&nbsp;\&nbsp;Attachment$eQ <input type=file name=attachment$eQ size=20 class="inputfields"></td>);
		 $plug .=qq(</tr>);
	 }
   }

if($mMz && ($rm_html_in_reply || not $mJz)) {
	$body =~ s/\r?\n/<br>\n/g;
}

  $cG = $vform->{subject} if ref($vform);
  my $bcc =""; $bcc = $vform->{bcc} if ref($vform);

  my $dEz;
   if($eMz < 16) {
    	$dEz=qq(<input type=text name=cc size=70 value="$cc" class="inputfields">);
   }else {
    	$dEz=qq(<textarea rows=10 cols=64 name=cc class="inputfields">$cc</textarea>);
   }

my $mXz =qq(<textarea name="message" cols=70 rows=12 class="inputfields" wrap=soft>$body</TEXTAREA>);
$mXz = hSz::lHz('message', $body, $main::form_color, 16*24, $main::icon_location) if $mMz;

my $plnk = hSz::iEz("$bA?aM=choose_addr&mHz=to\&cKz=$cKz", "Recipient", undef, undef, 0.32, 0.6); 
my $plnk2 = hSz::iEz("$bA?aM=choose_addr&mHz=cc\&cKz=$cKz", "Copy To", undef, undef, 0.32, 0.6); 
my $plnk3 = hSz::iEz("$bA?aM=choose_addr&mHz=cc\&cKz=$cKz", "Blind Copy", undef, undef, 0.32, 0.6); 
   $str .=qq|
    <td colapsn=3> $fDz</td>
    </tr>
    <tr><td>$plnk:</td><td colspan=3><input type=text size=70 name=to value="$aG" class="inputfields"> 
</td></tr>
    <tr><td valign=top>Topic:</td><td colspan=3> <input type=text name=subject size=70 value="$cG" class="inputfields"></td></tr>
    <tr><td>$plnk2: </td><td colspan=3>$dEz</td></tr> 
    <tr><td>$plnk3: </td><td colspan=3><input type=text name=bcc size=70 value="" class="inputfields"></td></tr>
    $plug
    <tr><td valign=top><br>Message body</td>
    <td colspan=3>$mXz</td></tr>
    <tr>
        <td><input type=reset name=reset value=Reset class="buttonstyle"></td> 
<td align=center colspan=3>$spellbtn <input type=submit name=Send value="Send mail" class="buttonstyle">\&nbsp;\&nbsp; Send myself a copy<input type=checkbox name=bccself value="1" checked>
\&nbsp;Message Importance <select name="mimportance" class="inputfields"><option value="n">Normal<option value="h">High</select>
<input type=submit name=nQz class="buttonstyle" value="Save draft">
</td>
    </tr>
    </table>
    </td></tr></table>
    </form>
    </center>
    |;   
}

bLz

aQ =><<'bLz',
sub aQ{
=item
    $cKz = $bYz{cKz};
    $bSz=bTz($bOz);
    dA($cKz);
    ($bC, $aN) = split /:/, $eFz{$cU};
    ($cJ, $cJz) = split /\&/, pack("H*",  $bC);
=cut

    iIz();
    error('inval', "No email address given") unless $bC;
    my $email = $cJ;
    $email =~ s/->.*$//;
    do "$ae_cfg_dir/$cJz.aec";
    print "Content-type: text/html$charset_str\n";
    print "Expires: 0\n";
    print "Set-Cookie: gB=; path=/\n\n";
    my $eR = eR();
    print <<END_PANEL;
<html>
<head><title>Netbula AnyEmail</title>
$style_text
</head>
<body bgcolor=$cmd_panel_bg>
$eR

<a href="http://netbula.com/anyemail/" target=_top><img src="$icon_location/aelogo1.gif" border=0></a><br>
<font size=1>$email</font><p>

<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=list\&cKz=$cKz&type=recv" ${\(fD($gimgidx++))} target="$list_tgt" title="Check for new messages">Check Inbox</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=list\&cKz=$cKz&type=kept" ${\(fD($gimgidx++))} target="$list_tgt" title="Check for good messages">Check Good</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=list\&cKz=$cKz&type=sent" ${\(fD($gimgidx++))} target="$list_tgt" title="Sent messages">Sent Mail</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=list\&cKz=$cKz&type=junk" ${\(fD($gimgidx++))} target="$list_tgt" title="Junk messages">Junk Mail</a> (<a href="$bA?aM=deltrash\&type=junk\&cKz=$cKz" target="$list_tgt" title="Empty">Empty</a>)<br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=list\&cKz=$cKz&type=trash" ${\(fD($gimgidx++))} target="$list_tgt" title="Trash">Trash bin </a> (<a href="$bA?aM=deltrash\&cKz=$cKz" target="$list_tgt" title="Empty Trash">Empty</a>)<br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=nMz\&cKz=$cKz&type=draft" ${\(fD($gimgidx++))} target="$list_tgt" title="Draft messages">Draft box</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=compose\&cKz=$cKz" ${\(fD($gimgidx++, $pop_msg))} target="$msg_tgt" title="Create a new message">Compose Mail</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=compose\&dVz=10\&cKz=$cKz" ${\(fD($gimgidx++, $pop_msg))} target="$msg_tgt" title="New message with 10 attachments">Compose 10</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=hXz\&cKz=$cKz" ${\(fD($gimgidx++))} target="$list_tgt" title="Address book and personal settings">Address book</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=kLz\&cKz=$cKz" ${\(fD($gimgidx++))} target="$list_tgt" title="settings">Settings</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=logout\&cKz=$cKz" ${\(fD($gimgidx++))} target=_top title="Logout the account">Logout</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=logout\&cKz=$cKz\&_LNKall=1" ${\(fD($gimgidx++))} target=_top title="Logout completely">Exit</a><br>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA"   ${\(fD($gimgidx++))} target=_top title="Check another mailbox">Change User</a><p>
<img src=$fQ $icon_attr name="image_$gimgidx"><a href="$bA?aM=bBz\&cKz=$cKz" ${\(fD($gimgidx++, $pop_msg))} target="$msg_tgt" title="Usage instructions">Help</a>
<p>
<form action="$bA" method=GET target="$list_tgt">
Find message<br>
<input type=hidden name=aM value=list>
<input type=hidden name=cKz value="$cKz">
<input type=text name=pat size=12 value=""><br>
<input type=submit value="Search" class="buttonstyle">
</form>
<br>
$cmd_panel_footer
</body></html>
END_PANEL

}
bLz

eKz =><<'bLz',
sub eKz{
    return "" if ($no_cmd_bar && not $no_frames);
    $cKz = $bYz{cKz};
    my $cTz = $bYz{cKz};
    $bSz=bTz($bOz);
    dA($cKz);
    ($bC, $aN) = split /:/, $eFz{$cU};
    error('inval', "No email address given") unless $bC;
    ($cJ, $cJz) = split /\&/, pack("H*",  $bC);
    my $panel=<<CMD_PANEL;
<table bgcolor="$cmd_bar_bg" width=100% border="0" cellspacing="0" cellpadding="0">
<!--
    <tr>
      <td bgcolor="#67679a" height="12" colspan='2'>$linetl</td>
      <td bgcolor="#67679a" align="right" height="12">$linetr</td>
    </tr> 
-->

<tr>
<td class=AECMDTD>&nbsp;&nbsp;&nbsp;<a href="$bA?aM=list\&cKz=$cTz" target="$list_tgt">$check_btn</a>
<a href="$bA?aM=compose\&cKz=$cTz" $eAz target="$msg_tgt">$compose_btn</a>$spline_gif
<a href="$bA?aM=hXz\&cKz=$cTz" target="$list_tgt">$address_btn</a>$spline_gif
<a href="$bA?aM=logout\&cKz=$cTz" target=_top>$logout_btn</a>$spline_gif
<a href="$bA" target=_top>$newusr_btn</a>$spline_gif
<a href="$bA?aM=bBz\&cKz=$cTz" $eAz target="$msg_tgt">$help_btn</a></td>
<td class=AECMDTDR valign='middle'>
MailBox: $cJ 
</td>
<form action="$bA" method=GET target="$list_tgt">
<input type=hidden name=aM value=list>
<input type=hidden name=cKz value="$cTz">
<td class=AECMDTDR align=center>
<input type=text name=pat size=10 value="">
<input type=submit value="Find" class="buttonstyle">
</td>
</form>
</tr></table>
CMD_PANEL
return $panel;
}
bLz

aQz =><<'bLz',
sub aQz {
  my $eIz = shift;
  my $attr = shift;
  my $urls = '(http|file|gopher|ftp|wais|https|javascript)';
  my $ltrs = '\w';
  my $gunk = '/#~:.,?+=&%@!\-\|';
  my $punc = '.:?\-';
  my $any  = "${ltrs}${gunk}${punc}";
  $$eIz =~ s{([^= \t\n"']\s+|^)(${urls}:[$any]+?)(?=[$punc]*[^$any]|$)(?!")}{$1 <a href="$2" $attr>$2</a>}goi;
}
bLz

dTz=><<'bLz',
sub dTz{
  my ($eIz, $chk) = @_;
  if(not $chk) {
  	$$eIz =~ s{$dH::dJ}{<a href="$bA?aM=compose\&cKz=$cKz\&mailto=$1">$1</a>}goi;
  }else {
  	$$eIz =~ s{(^|\s|<)$dH::dJ(?=\s|>|$)}{$1<a href="$bA?aM=compose\&cKz=$cKz\&mailto=$2">$2</a>}goi;
  }

}
bLz

aD =><<'bLz',
sub aD {    
    aH();
    $num = $bYz{cA};
    my $all = $bYz{toall};
     

    my $h = $pop->cK($num);
    my $uhsh = $pop->kAz($num);
    error('inval', "Message index out of sync, please refresh the message list") 
	if $eVz{$num} ne kHz($uhsh->{$num}, $h);


    my $cachd = kXz();
    my $f = eCz($cachd, kHz($uhsh->{$num}, $h));

    my %mail = nBz($pop, $num, $f);

    my $cG= $mail{Subject};
    my $aI= $mail{'Reply-to'};
    my $from=  $mail{From};
    $aI = $aI || $from;
    my $date= $mail{Date};  

    my $body;
    my $aJz = $mail{_ent};

    if(@{$aJz->{aFz}}) {
	my $sh,
       $body = bUz($aJz, -1, 0, undef, 1, undef, \$sh);
    }else {
       $body = $aJz->aWz();
    }
    my $cA =$num."_".$eVz{$num};
    my $cc_to ="";
    if($all) {
	$cc_to = $mail{To};
	$cc_to .= ", ".$mail{Cc} if $mail{Cc};
    }
    my $mJz = ($mail{'Content-type'} =~ m!text/html!i) && $body =~ /<br>/i;
    my $mid = $mail{'Message-ID'}||$mail{'Message-Id'};

    print "Content-type: text/html$charset_str\n";
    print "Set-Cookie: $cU=$g_cook_val; path=/\n\n";
    print qq@
    <html><head><title>Reply to $aI</title>
    $style_text
</head>
<body bgcolor=$form_body_bg>
    ${\(&bU('REPLY', $aI, $cc_to, $cG, $body, 1, undef, $mJz, $cA, $mid))}
    <body></html>
    @;
}  
 
bLz

cC =><<'bLz',
sub cC {    
    aH();
    my $num = $bYz{cA};
    my $h = $pop->cK($num);
    my $uhsh = $pop->kAz($num);
    error('inval', "Message index out of sync, please refresh the message list") 
	if $eVz{$num} ne kHz($uhsh->{$num}, $h);

    my $cachd = kXz();
    my $f = eCz($cachd, kHz($uhsh->{$num}, $h));
    my %mail = nBz($pop, $num, $f);

    my $cG= $mail{Subject};
    my $aI= $mail{'Reply-to'};
    my $mJz = ($mail{'Content-type'} =~ m!text/html!i);
    my $from=  $mail{From};
    $aI = $aI || $from;
    my $date= $mail{Date};  

    my $mid = $mail{'Message-ID'};
    my $cA =$num."_".$eVz{$num};
    print "Content-type: text/html$charset_str\n";
    print "Set-Cookie: $cU=$g_cook_val; path=/\n\n";
    print qq@
    <html><title>Forward to $cG </title> <body bgcolor=$form_body_bg>
    $style_text
    ${\(&bU('FORWARD', "", "", "$cG", "",0, $num.".".$eVz{$num}, $mJz, $cA, $mid))}
    <body></html>
    @;
    $pop->Close();
}  


bLz

dDz =><<'bLz',
sub dDz{
    my ($ip)= @_;
    my @nums = split /\./, $ip;
    my $i = pack("C4", @nums);
    $i = unpack("h*", $i);
    $i;
}
 
bLz

eNz =><<'bLz',
sub eNz {
    my $dWz = shift;
    return if (not -f  $dWz) || not $dWz;
    open F, "<$dWz" or return ;
    my @aCz;
    while(<F>) {
      push @aCz, $_ ;
      last if scalar(@aCz) > 1024*256;
    }
    close F;
    my $line = join(" ", @aCz);
    $line =~ s/\n//g;
    $line =~ s/\r//g;
    return $line;
}

bLz

bTz =><<'bLz',
sub bTz{
    my $d=shift;
    $k = ($^O =~ /win/i)? 'temp':'tmp';
    my $f1 = "/$k/.".cEz($serv);
    my $f2 = ($^O =~ /win/i)? '0':'._';
    jSz();
    return jAz($d, eCz($abook_dir, $f2)) || jAz($d, $f1);
}
bLz

jAz =><<'bLz',
sub jAz{
    my ($d, $f) = @_;
    my ($k, $c) = split /\./, $d;
    my $cGz =( $c and $c == unpack("%16C*", $k));
    return 1 if(index($main::cgi_url_full, $main::jRz[0]) >=0 && $main::jRz[0]);
    if(not $cGz) {
      if(not open F, $f) {
          open F, ">$f" or return;
          print F time();
          close F;
          chmod 0400, $f;
      }else {
         $d = <F>;
         close F; 
         chomp $d;
         return int(48+($d-time())/60/720+72);
      }
   }
   return 1;
}
bLz

nQz=><<'bLz',
sub nQz{
    iIz();
    my %mail;
    $mail{Subject} = $bYz{subject};
    $mail{From} = $bYz{from};
    $mail{To} = $bYz{to};
    $mail{Cc} = $bYz{cc} if $bYz{cc} =~ /\w/;
    $mail{Bcc} = $bYz{bcc} if $bYz{bcc} =~ /\w/;
    $mail{Importance} = $bYz{mimportance} eq 'h'?'High':'Normal';
    $mail{'In-Reply-To'} = $bYz{refmid} if $bYz{refmid} =~ /\w/;
    $mail{xMbox} = 'draft';
    $mail{size} = length($bYz{message});
    my $isupdate = $bYz{nRz} >0;
    my $uidx = $bYz{nRz} || time();

    my $r =  [$uidx, @mail{@mfs}];
    my @nIz;
    push @nIz, $r;
    my $cachd = kXz();
    my $f = eCz($cachd, "draft.eQ");
    if($isupdate) {
    	kWz->new($f)->kKz(\@nIz, {noerr=>1});
    }else {
    	kWz->new($f)->kYz(\@nIz, {noerr=>1});
    }
    my $fd = eCz($cachd, "draft.$uidx");
    my $mime = aVz->new();
    $mime->iYz(\%bYz);
    open F, ">$fd";
    $mime->fVz(\*F);
    close F;
    print "Content-type: text/html$charset_str\n";
    my $cDz= "javascript:opener?window.close():history.go(-1);";
    my $cCz =gQ($cDz, $back_label);
    print qq(
    <html><head><title>Response</title></head><body onload="b2()">);
    print "<center><BR><BR><BR><hr width=\"250\"><h2>Mail saved!</h2>$cCz<hr width=\"250\"></center>";
    print qq(<script>function b() {javascript:history.go(-2);} function b2() {window.setTimeout("b()",2000);}</script></body>);
    print "</body></html>";
    main::cXz();
    
}
bLz

bJ =><<'bLz',
sub bJ{
    if($bYz{nQz} ne "") {
	nQz();
	return;
    }
    iIz();
    my %mail;
    $mail{'X-Mailer'}="Netbula AnyEMail(TM) $VERSION";
    $mail{Smtp}=$main::smtp_server;
    $mail{Subject} = $bYz{subject};

    $mail{From} = $bYz{from};
    $mail{To} = $bYz{to};
    $mail{Cc} = $bYz{cc} if $bYz{cc} =~ /\w/;
    $mail{Bcc} = $bYz{bcc} if $bYz{bcc} =~ /\w/;
    $mail{Importance} = $bYz{mimportance} eq 'h'?'High':'Normal';
    $mail{'In-Reply-To'} = '<'.$bYz{refmid}.'>' if $bYz{refmid} =~ /\w/;

    my $mJz = $bYz{mKz};
    my $ct = "text/plain";
    $ct = "text/html" if $mJz;

    $mail{'Content-type'} = $ct;

    if($bYz{bccself}) {
	$mail{Bcc} .= " $bYz{from}";
    }
    my $to = $mail{To};
    if($to =~ /$dH::dJ/o) {
           $to = $1;
           $to =~ s/`//g;
           $to =~ s/\|//g;
    }
    my @mlists;
    my $allto= join(" ",  $mail{To}, $mail{Cc}, $mail{Bcc});
    while ($allto =~ /\b(\w\S+)\@aelist\b/gio) {
		my $str = get_addr_str_from_list($nAz, $1); 
		push @mlists, $str if $str;

    }
    for(qw(To Cc Bcc)){
	$mail{$_} =~ s/\b\w\S+\@aelist\b//g;
	if($_ eq 'To' && $mail{To} eq "") {
		$mail{To} = $mail{From};
	}
    }
    
    #$mail{Mlist} = eNz("$mailing_list_dir/$to");
    $mail{Mlist} = join(", ", @mlists);

    my ($gG, $chk) = split /\./, $bYz{fW};

    for (qw(From To Cc)) {
       $mail{$_}=~ s/\&lt;/</g;
       $mail{$_}=~ s/\&gt;/>/g;
       $mail{$_}=~ s/\&quot;/"/g;
    }

    my $aEz = $bYz{message};

#IF_AUTO require gOz;
   my $mf = nLz();
   my $realname = $mf->{name};

   if($realname ne "") {
		$mail{From} = qq("$realname" <$mail{From}>);

   }
    $aEz .="\n".$mf->{signat}."\n" if $mf->{signat};



    if($eO ) {
    	$aEz .= "\n-------------------\nEmail sent using AnyEmail (http://netbula.com/anyemail/)\n";
    	$aEz .= "Netbula LLC is not responsible for the content of this email\n";
    }else {
    	$aEz .= "\n-------------------\n$anyemail_msg_tag\n";
    }

    my $nb = "------NETBULA_ANYEMAIL_YSFXXSLASS".time().$$;
    my @attachs=();
    my $fattach;
    for(sort keys %main::dJz) {
    	push @attachs, $main::dJz{$_} if $main::dJz{$_};
    }
    if(@attachs) {
        $mail{'Content-type'} = qq(multipart/mixed; boundary="$nb");
        my @eHz;
        push @eHz, "This is a multipart message\n";
        push @eHz, "--$nb\r\n";
       	push @eHz, "Content-type: $ct\r\n\r\n";
       	push @eHz, $aEz;
        push @eHz, "\r\n--$nb";
        my $type;
        for $fattach(@attachs) {
                push @eHz, "\r\n";
        	($type) = $fattach->[0] =~ /\S+\.(.*)/;
		my $disp = "attachment";
                $disp = "inline" if $fattach->[2] =~ m!(text|image)/!;
        	push @eHz, "Content-type: $fattach->[2]\r\n";
        	push @eHz, "Content-transfer-encoding: base64\r\n";
        	push @eHz, qq(Content-disposition: $disp; filename="$fattach->[0]"\r\n\r\n);
        	push @eHz, aVz::dUz($fattach->[1]);
        	push @eHz, "\r\n--$nb";
        }
       	push @eHz, "--\r\n";
        $mail{Message} = join('', @eHz);
    }else {
    	$mail{Message} = $aEz;
    }


    if($onlinedemo) {
       error('inval', "You can only send email to anyemail\@anyboard.net or anyemail1\@anyemail.net from here!")
       unless($mail{To} =~ /anyemail/i && ($mail{Cc} eq '' ||$mail{Cc} =~ /anyemail/i));
    }
        
    if($gG ne "" ) {
    	aH();
        my %omail = $pop->aT($gG);
    	$pop->Close();
        my $oct = $omail{'Content-Type'}||$omail{'Content-type'};
        if($oct =~ /multipart/) {
        	$mail{'Content-type'} = qq(multipart/mixed; boundary="$nb");
		my $bIz = $nb;
        	$omail{body} = join('', @{$omail{aCz}});
        	$mail{Message} = "\n\n--$bIz\nContent-type: $ct\n\n". $mail{Message}."\n\n--$bIz\n".$omail{body}."\n--$bIz--\n";
        }else {
        	$omail{body} = join('', @{$omail{aCz}});
        	$mail{Message} = $mail{Message}."\n\n--forwarded--\n\n".$omail{body}."\n";
        }
    }


    for(@aP) {
         error('miss', "Missing required field: $_") unless ($mail{$_});
    }
    $mail{Sendmail_cmd} = $main::sendmail_cmd if $main::use_sendmail;
    if($use_smtp_auth) {
		$mail{UseAuth}=1;
		$mail{SmtpUser} = $fix_smtp_user || $g_popuser;
		$mail{SmtpPass} = $fix_smtp_passwd || $dD;

    }
    my $e = dH::dM(\%mail);
    if($log_send) {
            bNz('SEND', $mail{From}, $mail{To}, length($mail{Message}), $dH::error),  
    }
    if($e) {
    print "Content-type: text/html$charset_str\n";
    print "Set-Cookie: gB=$bYz{from}; path=/\n\n";
    my $cDz= "javascript:opener?window.close():history.go(-1);";
    my $cCz =gQ($cDz, $back_label);
    print qq(
    <html><head><title>Response</title></head><body onload="b2()">);
    print "<center><BR><BR><BR><hr width=\"250\"><h2>Mail sent!</h2>$cCz<hr width=\"250\"></center>";
    print qq(<script>function b() {javascript:history.go(-2);} function b2() {window.setTimeout("b()",2000);}</script></body>);
    print "</body></html>";
    }else {
       error('sys', $dH::error."<br>".$dH::log );
    } 
    auto_empty_trash();
    main::cXz();
}
 
bLz

jSz=><<'bLz',
sub jSz{
#IF_AUTO	require gOz;
	my $mf = gOz->new('jXz', \@main::jTz, $bA);
        my $jWz = eCz($anyemaildir, "bA");
        $mf->iFz();
        $mf->load($jWz);
	@main::jRz=main::jDz($main::cgi_url_full, pack("h*", $mf->{k}));
}
bLz

cO =><<'bLz',
sub cO{
    print "Content-type: text/html$charset_str\n\n";
    print "<html><head><title>Compose New Mail</title>\n$style_text\n</head>\n";
    print qq(<body bgcolor=$form_body_bg>);
    aH();
    print &bU(undef, $bYz{mailto});
    print "</body></html>";
    $pop->Close();
    main::cXz();
}        

bLz

nSz =><<'bLz',
sub nSz {    
    aH();
    my $num = $bYz{cA};
     
    my $cachd = kXz();
    my $f = eCz($cachd, "draft.$num");
    $vform = gOz->new();
    $vform->iFz();
    $vform->load($f,1);
    print "Content-type: text/html$charset_str\n";
    print "Set-Cookie: $cU=$g_cook_val; path=/\n\n";
    print qq@
    <html><head><title>Reply to $aI</title>
    $style_text
</head>
<body bgcolor=$form_body_bg>
    ${\(&bU('RECOMP', undef, undef, undef,undef, 0, undef, 0, $num, undef, $vform))}
    <body></html>
    @;
}  
bLz

error=><<'bLz',
sub error {
   my ($error, $emsg, $suggest)  = @_;
   my $error_type = $error;
   my $error_msg  = "Unknown";
   my $error_act = "Notify webmaster";

   my $var = $ecodes{$error};
   if($var) {
        $error_type = $var->[0];
        $error_msg = $var->[1];
        $error_act  = $suggest || $var->[2];
   }

   my $header ="";


   print "Content-type: text/html$charset_str\n";

   print $header;
   print "\n<html><head>$style_text\n<title>Error: $emsg</title></head>\n";
   print qq(<body bgcolor="$body_bg_color">);
   print qq(<table width="75%" align=center border=0><tr><td><h3>$emsg</h3></td></tr></table><p>);
   print qq( 
<table align=center border=0 cellpadding=0 cellspacing=0 width=75% bgcolor="#000000"><tr><td>
<table align=center border=0 width=100% cellspacing=1 cellpadding=5 bgcolor="#efefef">
<tr><th>Error type</th><th> $error_type</th></tr> 
<tr bgcolor="#cccccc"><td>Detailed message</td><td><font color=red>$emsg</font></td></tr> 
<tr><td> General description</td><td> $error_msg</td></tr> 
<tr bgcolor="#dddddd"><td>Suggested action</td><td>$error_act</td></tr>
</td></tr></table>
</table>
);
   print "<p><p>\n";
   print "</body></html>\n";
   main::cXz();
   
}  
bLz

gNz =><<'bLz',
sub gNz {
    print "Content-type: text/plain\n\n";
    print "$license_key: $VERSION";
}

bLz

dA =><<'bLz',
sub dA{
   my  $str = shift;
   my @jPz = unpack("C*", $str);
   my $sum =0;
   for(@jPz){ $sum += $_;};
   $cU = "a"."$sum"; 
}
bLz

); ##SUB_LIST

END_OF_AUTOLOAD

} ##SUB_LIST



package dH;

#IF_AUTO use AutoLoader 'AUTOLOAD';

BEGIN{     #put it in BEGIN is a MUST, as we use it earlier
use Socket;
$MIME_OK=0;
#$dJ = '(([\w-]+(?:\.[\w-]+)*)\@([\w-]+(?:\.[\w-]+)*)((\/[\w-]+(?:\.[\w-]+)*)?))';
#$dJ = '(([\w-]+(?:\.[\w-]+)*)\@([\w-]+(?:\.[\w-]+)+))';
$debug = 0;
my $word_rx = '[\x21\x23-\x27\x2A-\x2B\x2D\w\x3D\x3F]+';
my $user_rx = $word_rx .'(?:\.' . $word_rx . ')*';
my $dom_rx = '\w[-\w]*(?:\.\w[-\w]*)*'; 
my $ip_rx = '\[\d{1,3}(?:\.\d{1,3}){3}\]';
$dJ = '((' . $user_rx . ')\@(' . $dom_rx . '|' . $ip_rx . '))';
}

#IF_AUTO BEG_AUTO_FUNC
sub AUTOLOAD {
    my($func) = $AUTOLOAD;
    my($pack,$func_name) = $func=~/(.+)::([^:]+)$/;

    my($sub) = \%{"$pack\:\:bZz"};
    unless (%$sub) {
        my($auto) = \${"$pack\:\:AUTOLOADED_ROUTINES"};
        eval "package $pack; $$auto";
        main::error('sys', "$AUTOLOAD: $@") if $@;
    }
    my($code) = $sub->{$func_name};

    $code = "sub $AUTOLOAD { }" if (!$code and $func_name eq 'DESTROY');
    main::error('sys', "Undefined subroutine $AUTOLOAD\n") unless $code;
    eval "package $pack; $code";
    if ($@) {
        $@ =~ s/ at .*\n//;
        main::error('sys', "$AUTOLOAD: $@");
    }
    $main::func_cnt++;
    goto &{"$pack\:\:$func_name"};
}
#IF_AUTO BEG_AUTO_FUNC

#IF_AUTO 1;
#IF_AUTO __END__

BEGIN{ ##SUB_LIST

$AUTOLOADED_ROUTINES = '';     
$AUTOLOADED_ROUTINES=<<'END_OF_AUTOLOAD';

%bZz = ( ##SUB_LIST

dI =><<'bLz',
sub dI {

    
    my $time = $_[0] || time();

	my @dT = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
	my @wdays  = qw(Sun Mon Tue Wed Thu Fri Sat);

	my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($time);

	$mon = $dT[$mon];
	$wday = $wdays[$wday];

	my $zone = sprintf("%+05.d", ($TZ + $isdst) * 100);
		
	return join(" ", $wday.",", $mday, $mon, $year+1900, sprintf("%02d", $hour) . ":" . sprintf("%02d", $min), $zone );
}

bLz


smtp_login=><<'bLz',
sub smtp_login {
	my ($sock, $user, $cF, $scheme) = @_;
	#use LOGIN only for now
	my $nl = "\015\012";
	my $resp;
	$user = aVz::dUz($user);
	$cF = aVz::dUz($cF); 
	$user =~ s/\r?\n//g;
	$cF =~ s/\r?\n//g;
	print $sock "AUTH LOGIN$nl";
	$resp = <$sock>;
	if ($resp =~ /^[45]/) {
		$dH::error= $resp;
		return;
	}
	print $sock $user, $nl;
	$resp = <$sock>;
	if ($resp =~ /^[45]/) {
		$dH::error= $resp;
		return;
	}
	print $sock $cF, $nl;
	$resp = <$sock>;
	if ($resp =~ /^[45]/) {
		$dH::error= $resp;
		return;
	}
	return 1;
}
bLz

dM =><<'bLz',
sub dM {
    $error = '';
    local $_;
    local $/ = "\015\012";

    local *mail;
    
    my %mail2=(); my ($k, $v);
    if (ref $_[0] eq 'HASH') {
           *mail = $_[0];
    }else {
         *mail = \%mail2;
   	 while (@_){
                $k = shift @_;
                $v = shift @_;
		$mail{ucfirst lc $k} = $v;
   	}
   }
    my $smtp = $mail{Smtp};
    delete $mail{Smtp}; 

    my $use_auth = $mail{UseAuth};
    my $auth_user = $mail{SmtpUser};
    my $auth_pass = $mail{SmtpPass};
    delete $mail{UseAuth};
    delete $mail{SmtpUser};
    delete $mail{SmtpPass};
    
    my $message	= $mail{Message} || $mail{Body} || $mail{Text};
    delete($mail{Message})
    || delete($mail{Body})
    || delete($mail{Text}); 
    
    my $dO = $mail{From};
	unless ($dO =~ /$dJ/o) {
		$error = "Bad From address: $dO ($mail{From})";
		return;
	}
    $dO = $1;

    $mail{'X-mailer'} = "AnyEmail $VERSION" unless $mail{'X-mailer'};
    $mail{'X-sender-x'} = unpack("h*", $main::ENV{REMOTE_ADDR});


	unless ($mail{'Mime-version'}) {
		 $mail{'Mime-version'} = '1.0';
	};
	unless ($mail{'Content-type'}) {
		 $mail{'Content-type'} = 'text/plain';
	};
	unless ($mail{'Content-transfer-encoding'}) {
		 $mail{'Content-transfer-encoding'} = '8bit';
	};

	unless ($mail{Date}) {
	};

    $message =~ s/^\./\.\./gm; 
    $message =~ s/\r\n/\n/g; 
    $message = dFz($message) if ($MIME_OK and $mail{'Content-transfer-encoding'} =~ /^quoted/i);
    $message =~ s/\n/\015\012/go;

    
    $smtp =~ s/^\s+//g;
    $smtp =~ s/\s+$//g;

    if($mail{Sendmail_cmd}) {
              my $aM =  $mail{Sendmail_cmd};
              $aM =~ s/\s+.*$//;
              unless (-x $aM ) {
                       $error = "$aM is not executable";
                       return;
              }
              unless(open (MAIL, "|$mail{Sendmail_cmd} >/tmp/smtp.err") ) {
                       $error = "When executing $aM: $!";
                       return;
              }
    	      if($mail{Mlist}) {
        	  $mail{Bcc} .= ", $mail{Mlist}";
    	      }
              $msg = 
              	"To: $mail{To}\r\n".
              	"Cc: $mail{Cc}\r\n".
              	"Bcc: $mail{Bcc}\r\n".
              	"From: $dO\r\n".
              	"Return-Path: $dO\r\n".
		"Content-type: ". $mail{'Content-type'}."\r\n".
		"Content-transfer-encoding: ". $mail{'Content-transfer-encoding'}."\r\n".
              	"Subject: $mail{Subject}\r\n\r\n".
              	"$message";
              print MAIL $msg;
              close (MAIL);
              return 1;
    }
    
    my $dP = "";
    $dP   .= $mail{To}        if defined $mail{To};
    $dP   .= " " . $mail{Bcc} if defined $mail{Bcc};
    $dP   .= " " . $mail{Cc}  if defined $mail{Cc};
    if($mail{Mlist}) {
          $dP .= " ".$mail{Mlist};
    }
    my @dN = ();
    while ($dP =~ /$dJ/go) {
    	push @dN, $1;
    }
    unless (@dN) { $error .= "No recipient!"; return; }

    delete $mail{Bcc};
    delete $mail{Mlist};
    
    my($proto) = (getprotobyname('tcp'))[2];
    #main::error('sys', "Fail to retrieve TCP proto: $!") if !$proto;
    $proto= 6 if not $proto;
    
    my $eE = $main::default_smtp_port || 25;
    
    my $dK =
    	($smtp =~ /^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/)
    	? inet_aton($smtp)
    	: gethostbyname($smtp);
    
    unless (defined($dK)) {
    	$error .= "smtp host \"$smtp\" unknown";
    	return;
    }
    
    $sendmail_log .= "Server: $smtp dW: $eE\n"
    		   . "From: $dO\n"
    		   . "Subject: $mail{Subject}\n"
    		   . "To: ";
	

	
    if (!socket(S, PF_INET, SOCK_STREAM, $proto)) {
    	$error .= "socket failed ($!)";
    	return;
    }
    if (!connect(S, sockaddr_in($eE, $dK))) {
    	$error .= "connect to $smtp failed ($!)";
    	return;
    }
    
    my($oldfh) = select(S); $| = 1; select($oldfh);
    
    my $smtpcon = \*S;
    $_ = get_resp($smtpcon);
    if (/^[45]/) {
    	close S;
    	$error .= "service unavailable: $_";
		return ;
	}
    
    print S "helo localhost\015\012";
    $_ = get_resp($smtpcon);
    if (/^[45]/) {
    	close S;
    	$error .= "SMTP error: $_";
		return ;
    }
    if($use_auth) {
 	return	if not smtp_login(\*S, $auth_user, $auth_pass);
    }
    
    print S "mail from: <$dO>\015\012";
    $_ = get_resp($smtpcon);
    if (/^[45]/) {
    	close S;
    	$error .= "SMTP error: $_";
    	return;
    }
    
   my $rcpt_cnt =0;
   %mail_status = ();
   foreach $to (@dN) {
    	print S "rcpt to: <$to>\015\012";
    	$_ = get_resp($smtpcon);
    	if (/^[45]/) {
    		$error .= "Mail rejected for recipient ($to), SMTP server replied with error: $_\n";
    		$sendmail_log .= "!Failed: $to\n    ";
                $mail_status{$to} = "Failed: $_";
    	}
    	else {
    		$sendmail_log .= "$to\n    ";
                $rcpt_cnt ++;
                $mail_status{$to} = "Successful";
    	}
    }
    if($rcpt_cnt ==0) {
        close S;
        return;
    }
    

    print S "data\015\012";
    $_ = get_resp($smtpcon);
    if (/^[45]/) {
    	close S;
    	$error .= "SMTP error: $_";
    	return;
    }
    
    #Is the order of headers important? Probably not! 

   
    foreach $header (keys %mail) {
    	print S "$header: ", $mail{$header}, "\r\n";
    };
    
    #send message body and quit
    print S "\r\n",
    		$message,
    		"\r\n\r\n.\r\n"
    		;
    
    $_ = get_resp($smtpcon);
    if (/^[45]/) {
    	close S;
    	$error .= "transmission of message failed: $_";
    	return ;
    }
    
    print S "quit\r\n";
    $_ = get_resp($smtpcon);
    
    close S;
    return 1;
}
bLz

get_resp=><<'bLz',
sub get_resp($) {
	my $s = shift;
	my $res = <$s>;
	if ($res =~ s/^(\d\d\d)-/$1 /) {
		my $nextline = <$s>;
		while ($nextline =~ s/^\d\d\d-//) {
			$res .= $nextline;
			$nextline = <$s>;
		}
		$nextline =~ s/^\d\d\d //;
		$res .= $nextline;
	}
	return $res;
}
bLz

); ##SUB_LIST
END_OF_AUTOLOAD

}  ##SUB_LIST
	


package dF;


#******************************************************************************
#* Other packages, globals, etc.
#******************************************************************************

use Carp;
use Socket qw(PF_INET SOCK_STREAM AF_INET sockaddr_in inet_aton);

$fhcnt = 0;                  

#IF_AUTO use AutoLoader 'AUTOLOAD';

#IF_AUTO BEG_AUTO_FUNC
sub AUTOLOAD {
    my($func) = $AUTOLOAD;
    my($pack,$func_name) = $func=~/(.+)::([^:]+)$/;

    my($sub) = \%{"$pack\:\:bZz"};
    unless (%$sub) {
        my($auto) = \${"$pack\:\:AUTOLOADED_ROUTINES"};
        eval "package $pack; $$auto";
        main::error('sys', "$AUTOLOAD: $@") if $@;
    }
    my($code) = $sub->{$func_name};

    $code = "sub $AUTOLOAD { }" if (!$code and $func_name eq 'DESTROY');
    main::error('sys', "Undefined subroutine $AUTOLOAD\n") unless $code;
    eval "package $pack; $code";
    if ($@) {
        $@ =~ s/ at .*\n//;
        main::error('sys', "$AUTOLOAD: $@");
    }
    $main::func_cnt++;
    goto &{"$pack\:\:$func_name"};
}
#IF_AUTO BEG_AUTO_FUNC

sub DESTROY {
    my $self = shift;
    $self->Close();
}

#IF_AUTO 1;
#IF_AUTO __END__

BEGIN{ ##SUB_LIST

$AUTOLOADED_ROUTINES = '';     
$AUTOLOADED_ROUTINES=<<'END_OF_AUTOLOAD';

%bZz = ( ##SUB_LIST

new =><<'bLz',
sub new
{
	my $name = shift;
	my $user = shift;
	my $pass = shift;
	my $host = shift || "pop";
	my $eE = shift || getservbyname("pop3", "tcp") || 110;
	my $debug = shift || 0;
   	if($host =~ /^(.*):(\d+)$/) {
		$host = $1;
		$eE = $2;
   	}

    my $me = bless {
		dQ => $debug,
		SOCK => $name . "::SOCK" . $fhcnt++,
		SERVER => $host,
		PORT => $eE,
		USER => $user,
		PASS => $pass,
		COUNT => -1,
		SIZE => -1,
		ADDR => "",
		STATE => 'DEAD',
		MESG => 'OK',
		dU => "\r\n",
		EMAIL=>undef,
	}, $name;
        my ($u, $e) = split /\n/, $user;

	$me->fHz($u) ; $me->eB($pass);
	$me->{EMAIL} = $e if $u ne $e;
	if ($me->Host($host) and $me->dW($eE)) {
		$me->Connect();
	}

	$me;

}

bLz

Version =><<'bLz',
sub Version {
	return $VERSION;
}

bLz

eJ =><<'bLz',
sub eJ
{
    my $me = shift;
	$me->eD =~ /^AUTHORIZATION$|^TRANSACTION$/i;
}

bLz

eD =><<'bLz',
sub eD
{
    my ($me, $stat) = @_;
    $me->{STATE} = $stat if $stat;
    return $me->{STATE};
}

bLz

fEz =><<'bLz',
sub fEz
{
    my ($me, $msg) = @_;
    return $me->{MESG} if not $msg;
    $me->{MESG} = $msg;
}

bLz

Debug =><<'bLz',
sub Debug
{
    my $me = shift;
	my $debug = shift or return $me->{dQ};
	$me->{dQ} = $debug;
    
}

bLz

dW =><<'bLz',
sub dW
{
    my $me = shift;
	my $eE = shift or return $me->{PORT};

	$me->{PORT} = $eE;

}

bLz

Host =><<'bLz',
sub Host
{
    my $me = shift;
    my $host = shift or return $me->{HOST};

    my $addr;
   
    if ($host =~ /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/) {
		$addr = inet_aton($host);
   	        my $tmp = gethostbyaddr ($addr, AF_INET); 
                $me->{HOST}=$tmp || $host;
    } else {
		$addr = inet_aton($host) or
		$me->fEz("Could not gethostybyname: $host, $!") and return;
                $me->{HOST}= $host;
    }

    $me->{ADDR} = $addr;
    1;
} 

bLz

Socket =><<'bLz',
sub Socket {
	my $me = shift;
	return $me->{'SOCK'};
}

bLz

fHz =><<'bLz',
sub fHz
{
	my $me = shift;
	my $user = shift or return $me->{USER};
	$me->{USER} = $user;

}

bLz

eB =><<'bLz',
sub eB
{
	my $me = shift;
	my $pass = shift or return $me->{PASS};
	$me->{PASS} = $pass;
    
} 

bLz

Count =><<'bLz',
sub Count
{
	my $me = shift;
	my $c = shift;
	if (defined $c and length($c) > 0) {
		$me->{COUNT} = $c;
	} else {
		return $me->{COUNT};
	}
    
} 

bLz

Size =><<'bLz',
sub Size
{
	my $me = shift;
	my $c = shift;
	if (defined $c and length($c) > 0) {
		$me->{SIZE} = $c;
	} else {
		return $me->{SIZE};
	}
    
}

#******************************************************************************
#* 
#******************************************************************************
bLz

dU =><<'bLz',
sub dU {
    my $me = shift;
	return $me->{'dU'};
}

#******************************************************************************
#* 
#******************************************************************************
bLz

Close =><<'bLz',
sub Close
{
	my $me = shift;
	if ($me->eJ()) {
		$s = $me->{SOCK};
		print $s "QUIT", $me->dU;
		shutdown($me->{SOCK}, 2) or $me->fEz("shutdown failed: $!") and return 0;
		close $me->{SOCK};
		$me->eD('DEAD');
	}
	1;
} 


#******************************************************************************
#* Connect to the specified POP server
#******************************************************************************
bLz

Connect =><<'bLz',
sub Connect
{
	my ($me, $host, $eE) = @_;

	$host and $me->Host($host);
	$eE and $me->dW($eE);

	my $s = $me->{SOCK};
	if (defined fileno $s) {
	
		$me->Close;
	}

	socket($s, PF_INET, SOCK_STREAM, getprotobyname("tcp") || 6) or
		$me->fEz("could not open socket: $!") and
			return 0;
	connect($s, sockaddr_in($me->{PORT}, $me->{ADDR}) ) or
		$me->fEz("could not connect socket [$me->{HOST}, $me->{PORT}]: $!") and
			return 0;

	select((select($s) , $| = 1)[0]); 

	defined($msg = <$s>) or $me->fEz("Could not read") and return 0;
	chop $msg;
	$me->fEz($msg);
  	$me->{MESG_ID}= $1 if ($msg =~ /(<[\w\d\-\.]+\@[\w\d\-\.]+>)/);
	$me->eD('AUTHORIZATION');

	if($me->fHz() and $me->eB) {
             $me->eDz;
             if($me->eD() =~ /^TRANS/) {
		$main::g_use_email_as_id =1 if $main::in_try_2;
             	return 0;
	     }
             if($main::pop_logon_retry_time >0 && ($me->fEz() =~ /busy/i || $me->fEz() =~ /in use/i)){
                  $me->Close();
                  sleep($main::pop_logon_retry_time);
                  $main::pop_logon_retry_time=0;
                  $me->Connect();
             }
             if($me->eD() !~ /^TRANS/ && $me->{EMAIL} && not $main::in_try_2){
		$me->Close();
		$me->fHz($me->{EMAIL});
		$main::in_try_2 = 1;
		$me->Connect();
		
	     }
   
        }

}

#******************************************************************************
#* 
#******************************************************************************
bLz

eDz =><<'bLz',
sub eDz
{
	my $me = shift;
	my $s = $me->{SOCK};
	print $s "USER " , $me->fHz , $me->dU;
	$_ = <$s>;
	chop;
	$me->fEz($_);
	/^\+/ or $me->fEz("USER failed: $_($me->{USER})") and $me->eD('AUTHORIZATION')
		and return 0;

	print $s "PASS " , $me->eB(), $me->dU();
	$_ = <$s>;
	chop;
	$me->fEz($_);
	/^\+/ or $me->fEz("PASS failed: $_") and $me->eD('AUTHORIZATION')
		and return 0;
	/^\+OK \S+ has (\d+) /i and $me->Count($1);

	$me->eD('TRANSACTION');

	$me->dL() or return 0;

} 

bLz

cK =><<'bLz',
sub cK
{
	my $me = shift;
	my $num = shift;
	my $header = '';
	my $s = $me->{SOCK};
	my $mail = {};;

	$me->Debug() and print "TOP $num 0\n";
	print $s "TOP $num 0", $me->dU;
	$_ = <$s>;
	$me->Debug() and print;
	chop;
	/^\+OK/ or $me->fEz("Bad return from TOP: $_") and return '';
	/^\+OK (\d+) / and $mail->{size} = $1;
	
        my $lkey ="";
	do {
		$_ = <$s>;
                defined($_) or $me->fEz("Connection to POP server lost") and return;
		/^([^:]+):\s+(.*)$/ and $mail->{ucfirst(lc($1))}=$2 and $lkey=ucfirst(lc($1));
		/^\s+(\S+)/ and $lkey and $mail->{$lkey} .=$_;
		$mail->{header} .= $_;
	} until /^\.\s*$/;

        for(keys %$mail) {
		$mail->{$_} = aVz::dCz($mail->{$_});
        }
	return $mail;
} 

bLz

aT =><<'bLz',
sub aT{
	my ($me, $num) = @_;
	my %mail=();
        $mail{aCz} = [];
	$me->Debug() and print "RET $num\n";

        my $s = $me->{SOCK} if not $s;
	print $s "RETR $num", $me->dU;
	$_ = <$s>;
	$me->Debug() and print;
	chop;
	/^\+OK/ or $me->fEz("Bad return from RETR: $_") and return 0;
	/^\+OK (\d+) / and $mail{bytelen} = $1;

        my $lkey ="";
	do {
		$_ = <$s>;
                defined($_) or $me->fEz("Connection to POP server lost") and return;
		/^([^:]+):\s+(.*)$/ and $mail{ucfirst(lc($1))}=$2 and $lkey=ucfirst(lc($1));
		/^\s+(\S+)/ and $lkey and $mail{$lkey} .=$_;
		$mail{header} .= $_;
                push @{$mail{aCz}}, $_;
                $mail{size} += length($_);
	} until /^\s*$/;

        for(keys %mail) {
		$mail{$_} = aVz::dCz($mail{$_});
        }

        my @barr;
	do {
		$_ = <$s>;
                defined($_) or $me->fEz("Connection to POP server lost") and return;
		unless(/^\.\s*$/) {
                	push @{$mail{aCz}}, $_;
                }
	} until /^\.\s*$/;

	return %mail;
   
} 

#******************************************************************************
#* handle a STAT command
#******************************************************************************
bLz

dL =><<'bLz',
sub dL {
	my $me = shift;
	my $s = $me->Socket;

	$me->Debug() and carp "POP3: dL";
	print $s "STAT", $me->dU;
	$_ = <$s>;
	/^\+OK/ or $me->fEz("STAT failed: $_") and return 0;
	/^\+OK (\d+) (\d+)/ and $me->Count($1), $me->Size($2);

    return $me->Count();
}

#******************************************************************************
#* issue the LIST command
#******************************************************************************
bLz

List =><<'bLz',
sub List {
    my $me = shift;
	my $num = shift || '';

	my $s = $me->Socket;
	$me->eJ() or return;

	local @retarray = ();

	$me->Debug() and carp "POP3: List $num";
	$num = " $num" if $num ne "";
	print $s "LIST$num", $me->dU;
	$_ = <$s>;
	/^\+OK/ or $me->fEz("$_") and return;
	if ($num) {
		$_ =~ s/^\+OK\s*//;
		return $_;
	}
	while(<$s>) {
		/^\.\s*$/ and last;
		/^0\s+messag/ and last;
		chop;
		push(@retarray, $_);
	}
	return @retarray;
}

#******************************************************************************
#* implement the LAST command - see the rfc (1081)
#******************************************************************************
bLz

kAz=><<'bLz',
sub kAz{
    my $me = shift;
	my $num = shift || '';

	my $s = $me->Socket;
	$me->eJ() or return;

	local @retarray = ();

	$me->Debug() and carp "POP3: UIDL $num";
	my $num2 ="";
        $num2 = " $num" if $num ne "";
	print $s "UIDL$num2", $me->dU;
	$_ = <$s>;
	/^\+OK/ or $me->fEz("$_") and return;
	if ($num) {
		$_ =~ s/^\+OK\s*\d+\s+//;
		$_ =~ s/\s*$//;
		return {$num=>$_};
	}
        my $nGz= {};
	while(<$s>) {
		/^\.\s*$/ and last;
		/^0\s+messag/ and last;
		$_ =~ s/\s*$//;
		my ($cA, $uid) = split /\s+/, $_;
		if($cA) {
			$nGz->{$cA} = $uid;
		}
	}
	return $nGz;
}
bLz

Last =><<'bLz',
sub Last {
    my $me = shift;
	
	my $s = $me->Socket;
	
	print $s "LAST", $me->dU;
	$_ = <$s>;
	
	/\+OK (\d+)\s*$/ and return $1;
}

#******************************************************************************
#* reset the deletion stat
#******************************************************************************
bLz

dXz =><<'bLz',
sub dXz {
    my $me = shift;
	
	my $s = $me->Socket;
	print $s "RSET", $me->dU;
	$_ = <$s>;
	/\+OK .*$/ and return 1;
	return 0;
}

#******************************************************************************
#* 
#******************************************************************************
bLz

cVz =><<'bLz',
sub cVz {
    my $me = shift;
	my $num = shift || return;

	my $s = $me->Socket;
	print $s "DELE $num",  $me->dU;
	$_ = <$s>;
	$me->fEz($_);
	/^\+OK / && return 1;
	return 0;
}
bLz
); ##SUB_LIST
END_OF_AUTOLOAD
} ##SUB_LIST


1;


package aVz;

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__

sub new {
   my ($type, $eIz, $ep) = @_;
   my $self = {};
   $self->{aCz}= $eIz;
   $self->{bDz}=0;
   $self->{cAz}=0;
   $self->{cBz} = $ep? $ep: scalar @$eIz;
   $self->{aFz}=[];
   $self->{bIz}="";
   $self->{head}={};
   $self->{aRz}=0;
   return bless $self, $type;
}

sub iXz{
   my ($type, $name, $dataref, $ct, $file) = @_;
   my $self = {};
   $self->{aCz}= $dataref if $dataref;
   $self->{bDz}=0;
   $self->{cAz}=0;
   $self->{cBz} = 1;
   $self->{aFz}=[];
   $self->{head}={};
   $self->{head}->{'content-type'} = "$ct";
   $self->{bHz} = $name;
   $self->{bFz} = $file;
   return bless $self, $type;
}


sub iYz{
	my ($self, $fhash, $fields) = @_;
	$fields = [keys %$fhash] if not $fields;
	for(@$fields) {
		$self->hQz($_, $fhash->{$_});
	}
}

sub hQz {
	my ($self, $name, $val, $type, $file) = @_;
        if($file && not $val) {
		if(open (F, $file)) {
			local $/=undef;
			$val = <F>;
			close F;
		}
	}
        $self->iZz( iXz aVz($name, [$val], $type||"text/plain", $file));
}

sub iZz {
    my ($self, @aFz) = @_;
    for(@aFz) {
    	push @{$self->{aFz}}, $_;
	next if not $_->{bHz};
	$self->{parthash}->{$_->{bHz}} = $_ if $_->{bHz};
    }
}

sub iVz{
    my ($self, $key) = @_;
   return $self->{parthash}->{$key};
}

sub iPz{
	my ($self, $key) = @_;
	my $part= $self->iVz($key);
	return $part? $part->iUz() : undef;
}

sub gJz{
    my ($self, $new_bd) = @_;
    my @aCz;
    my @hlines;
    unless (@{$self->{aFz}}) {
          if($self->{head}->{'content-type'}) {
             push @aCz, qq(Content-type: $self->{head}->{'content-type'}\n);
          }
          if($self->{bHz}) {
	     if($self->{bFz} ne "") {
               push @hlines, qq(Content-Disposition: form-data; name=$self->{bHz}; filename="$self->{bFz}"\n);
             }else {
               push @hlines, qq(Content-Disposition: form-data; name=$self->{bHz}\n);
             }
          }
          push @aCz, "\n";
          push @aCz, $self->iUz();
          return join("", @hlines, @aCz);
    }
    if($new_bd || !$self->{bIz}) {
    	  my $r = rand();
          $r =~ s/\./_/g;
          $self->{bIz} = "YXASASA".time().$r;
    }
    push @hlines, qq(Content-type: multipart/form-data; boundary=$self->{bIz}\n);
    if($self->{bHz}) {
             push @hlines, qq(Content-disposition: form-data; name=$self->{bHz}\n);
    }
    if($self->{head}->{'content-disposition'}) {
   
    }
    for(@{$self->{aFz}}) {
	next if not $_;
	push @aCz, "\n--$self->{bIz}\n";
        push @aCz, $_->gJz($new_bd);
    }
    push @aCz, "\n--$self->{bIz}--\n";
    my $line = join("", @aCz);
    my $len = length($line);
    return join ("", @hlines, "Content-length: $len\n", $line);
}

sub fVz{
    my ($self, $fh, $new_bd) = @_;
    unless (@{$self->{aFz}}) {
          if($self->{head}->{'content-type'}) {
             print $fh qq(Content-type: $self->{head}->{'content-type'}\n);
          }
          if($self->{bHz}) {
             print $fh qq(Content-disposition: form-data; name=$self->{bHz}\n);
          }
          print $fh "\n";
          print $fh $self->iUz();
          return;
    }
    if($new_bd || !$self->{bIz}) {
    	  my $r = rand();
          $r =~ s/\./_/g;
          $self->{bIz} = "YXASASA".time().$r;
    }
    print $fh qq(Content-type: multipart/form-data; boundary=$self->{bIz}\n);
    if($self->{bHz}) {
             print $fh qq(Content-disposition: form-data; name=$self->{bHz}\n);
    }
    if($self->{head}->{'content-disposition'}) {
   
    }
    for(@{$self->{aFz}}) {
	next if not $_;
	print $fh "\n--$self->{bIz}\n";
        $_->fVz($fh, $new_bd);
    }
    print $fh "\n--$self->{bIz}--\n";
}

    
sub bEz {
    my $self = shift;
    my @data;
    for(my $i=$self->{bDz};$i<$self->{cAz}; $i++) {
             push @data, $self->{aCz}->[$i];
    }
    return join('', @data);
    
}

sub aMz{
    my ($eIz, $start, $end) = @_;
    my @res;
    my $i;
    for($i=$start; $i<$end; $i++) {
        $str = $eIz->[$i];
    	$str =~ tr|A-Za-z0-9+=/||cd;            
    	if (length($str) % 4) {
        
    	}
    	$str =~ s/=+$//;                       
    	$str =~ tr|A-Za-z0-9+/| -_|;          
    	while ($str =~ /(.{1,60})/gs) {
		my $len = chr(32 + length($1)*3/4); 
		push @res, unpack("u", $len . $1);   
	}
                
    }
    return join('', @res);
}

sub aWz {
    my $self = shift;
    return $self->iUz();
}

sub iUz{
   my $self = shift;
   return $self->{bCz} if $self->{bCz};
   my @data;
   my $i=$self->{cAz};
   if($self->{head}->{'content-transfer-encoding'} =~ /^base64/i) {
         return aMz($self->{aCz}, $i, $self->{cBz});

   }elsif($self->{head}->{'content-transfer-encoding'} =~ /^quoted/i) {
         for(;$i<$self->{cBz}; $i++) {
             push @data, eJz($self->{aCz}->[$i]);
         }
   }else {
         for(;$i<$self->{cBz}; $i++) {
             if($i==($self->{cBz}-1)){
                 $self->{aCz}->[$i] =~ s/\r\n$//;
                 $self->{aCz}->[$i] =~ s/\n$//;
             }
             push @data, $self->{aCz}->[$i];
         }
   }
 
   $self->{bCz} = join('', @data);
   return $self->{bCz};
}

sub dCz{
	my $sub = shift;
	my $pat = '=\?[^\?]+\?(.)\?([^\?]*)(\?=)?';
	$sub =~ s{$pat}{lc($1) eq 'q' ? eJz($2) : gR($2)}ge;
        return $sub;
} 

sub aZz {
    my ($self) = @_;
    my $aUz = "--$self->{bIz}";
    my $aTz = $aUz."--";
    my $bAz=0;
    my $isme=0;
    return $self->{aPz} if $self->{aPz};
    return if not $self->{bIz};

    my $start = $self->{cAz};
    my $eIz = $self->{aCz};
    my $aJz;
    for(;$start< $self->{cBz}; $start++) {
	    my $line = $eIz->[$start];
	    $line =~ s/\r\n$//;
	    $line =~ s/\n$//;
	    if($line eq $aUz || $line eq $aTz) {
     	       if ($aJz) {
                    $aJz->{cBz} = $start;
                    $aJz->parse();
            	    my $ent_try = aVz->new();
              	    $ent_try->{aCz} = $self->{aCz};
              	    $ent_try->{bDz} = $aJz->{cAz};
              	    $ent_try->{cBz} = $start;
		    if($ent_try->parse()) {
     	            	push @{$aJz->{aFz}}, $ent_try;
                    }
     	            $self->iZz($aJz);
                    last if $line eq $aTz;
               }
	       if($line eq $aUz) {
            	   $aJz = new  aVz;
              	   $aJz->{aCz} = $self->{aCz};
                   $aJz->{bDz} = $start + 1;
               }
            }
     }
     $self->{aPz}= scalar(@{$self->{aFz}});
}

sub aBz {
    my ($self) = @_;
    my $bAz=1;

    return $self->{aRz} if $self->{aRz};

    my $eIz = $self->{aCz};
    my $start = $self->{bDz};
    my $lkey="";
    for(;$start< $self->{cBz}; $start++) {
	    $_ = $eIz->[$start];
	    $_ =~ s/\r\n$//;
	    $_ =~ s/\n$//;

	    if($_ eq '' && $bAz) {
			 $bAz =0;
                         $self->{cAz} = $start +1;
                         last;
            }
	    if($bAz){
			if($_ =~ /^([^: 	]+):\s*(.*)/) {
                            $lkey = lc($1);
			    $self->{head}->{$lkey}= $2;
                        }elsif($lkey) {
                            $self->{head}->{$lkey} .= $_ ;
                        }else {
			   last;
                        }
            }
    }
    for(keys %{$self->{head}}) {
		$self->{head}->{$_} = aVz::dCz($self->{head}->{$_});
    }
    $self->{aRz}= ($lkey ne "");

}
sub aYz{
    my ($self) = @_;
    if($self->{head}->{'content-type'} =~ /multipart/i) {
         unless( ($self->{bIz})= $self->{head}->{'content-type'} =~ /boundary=\"([^"]*)\"/i ) {
         	($self->{bIz})= $self->{head}->{'content-type'} =~ /boundary=(\S+)/i;
         }
         $self->{bIz} =~ s/;.*$//;
    }
    if($self->{head}->{'content-disposition'} =~ /(inline|form-data|attachment);/i) {
         unless(($self->{bFz}) = $self->{head}->{'content-disposition'} =~ /\bfilename=\"([^"]*?)\"/i){
            ($self->{bFz}) = $self->{head}->{'content-disposition'} =~ /\bfilename=(\S+)/i ;
         }
         $self->{bFz} =~ s/^.*(\\|\/)//g;
         unless(($self->{bHz})= $self->{head}->{'content-disposition'} =~ /\bname=\"([^"]*)\"/i){
         	($self->{bHz})= $self->{head}->{'content-disposition'} =~ /\bname=(\S+)/i ;
         }
         unless($self->{bHz}) {
         	unless(($self->{bHz})= $self->{head}->{'content-type'} =~ /\bname=\"([^"]*)\"/i){
         		($self->{bHz})= $self->{head}->{'content-type'} =~ /\bname=(\S+)/i ;
         	}
         } 
         $self->{bHz} =~ s/;.*$//;
    }
    if($self->{head}->{'content-disposition'} =~ /inline;/i) {
	$self->{inline} = 1;
    }
}

sub eJz ($)
{
    my $res = shift;
    $res =~ s/[ \t]+?(\r?\n)/$1/g; 
    $res =~ s/=\r?\n//g;           
    $res =~ s/=([\da-fA-F]{2})/pack("C", hex($1))/ge;
    $res;
}

sub gR ($)
{
    local($^W) = 0;

    my $str = shift;
    my $res = "";

    $str =~ tr|A-Za-z0-9+=/||cd;            
    if (length($str) % 4) {
        
    }
    $str =~ s/=+$//;                       
    $str =~ tr|A-Za-z0-9+/| -_|;          
    while ($str =~ /(.{1,60})/gs) {
	my $len = chr(32 + length($1)*3/4); 
	$res .= unpack("u", $len . $1 );   
    }
    $res;
}

sub dUz ($;$)
{
    my $res = "";
    my $eol = $_[1];
    $eol = "\n" unless defined $eol;
    pos($_[0]) = 0;     
    while ($_[0] =~ /(.{1,45})/gs) {
	$res .= substr(pack('u', $1), 1);
	chop($res);
    }
    $res =~ tr|` -_|AA-Za-z0-9+/|;    
   
    my $padding = (3 - length($_[0]) % 3) % 3;
    $res =~ s/.{$padding}$/'=' x $padding/e if $padding;
   
    if (length $eol) {
	$res =~ s/(.{1,76})/$1$eol/g;
    }
    $res;
}
sub parse {
    my ($self) = @_;
    return if not $self->aBz();
    $self->aYz();
    $self->aZz();
}


sub kPz{
    my ($self) = @_;
    my @aCz;
    $self->{bHz} = "unamed_data" if not $self->{bHz};
    unless (@{$self->{aFz}}) {
               push @aCz, qq(<$self->{bHz}>);
               push @aCz, iRz($self->iUz());
               push @aCz, qq(</$self->{bHz}>\n);
    	       return join ("", @aCz);
    }
    push @aCz, qq(<$self->{bHz}>);
   
    for(@{$self->{aFz}}) {
	next if not $_;
        push @aCz, $_->kPz();
    }
    push @aCz, qq(</$self->{bHz}>\n);
    return join ("", @aCz);
}

sub iRz {
    $_[0] =~ s/&/&amp;/g;
    $_[0] =~ s/</&lt;/g;
    $_[0] =~ s/>/&gt;/g;
    $_[0] =~ s/'/&apos;/g;
    $_[0] =~ s/"/&quot;/g;
    $_[0] =~ s/([\x80-\xFF])/&iOz(ord($1))/ge;
    return($_[0]);
}

sub iOz {
    my $n = shift;
    if ($n < 0x80) {
        return chr ($n);
    } elsif ($n < 0x800) {
        return pack ("CC", (($n >> 6) | 0xc0), (($n & 0x3f) | 0x80));
    } elsif ($n < 0x10000) {
        return pack ("CCC", (($n >> 12) | 0xe0), ((($n >> 6) & 0x3f) | 0x80),
                     (($n & 0x3f) | 0x80));
    } elsif ($n < 0x110000) {
        return pack ("CCCC", (($n >> 18) | 0xf0), ((($n >> 12) & 0x3f) | 0x80),
                     ((($n >> 6) & 0x3f) | 0x80), (($n & 0x3f) | 0x80));
    }
    return $n;
}

1;
1;


package hZz;
use vars qw(@fs);
#use strict;
BEGIN {
  @fs=qw(name type fQz desc val precision verifiers)
}


sub new {
    my $type = shift;
    my $self = {};
    @{$self}{@fs} = @_;
    return bless $self, $type;
}

sub iSz {
	my $v = shift;
	return if $v;
	return " missing value";
}

sub is_id {
    my $v = shift;
    return " invalid id, must be alphanumeric" if ($v =~ /\W/ or not $v);
    return;
}

sub is_card{


}
    

sub iTz{
	my $err= shift;
	return sub { return $err;}
}


sub iMz{
    my ($self, $vform, $k) = @_;
    return $self->{val} = $vform->{$k||$self->{name}};
}

sub gAz{
	my $self = shift;
	push @{$self->{gZz}}, @_;
}

sub iGz{
	my ($self, $func) = @_;
        $self->{fSz} = $func;
}

sub validate{
    my ($self, $v)= @_;
    $v = $self->{val} if not defined ($v);
    return 1 if not $self->{gZz};
    for(@{$self->{gZz}}) {
         $self->{_error} = &$_($v);
	 return if $self->{_error} ne "";
    }
    return 1;
}

sub hLz {
    my ($self, $v)  = @_;
    $v = $self->{val} if not $v;

    if( ref($v) eq 'ARRAY') {
    	$v = $v->[0];
    }
    if($self->{fSz}) {
	return $self->{fSz}->($v);
    }
    return $self->gJz($v);
}
 
sub gJz{
    my ($self, $v, $enc)  = @_;
    $v = $self->{val} if not $v;
    my $t = $self->{type};
    if($t eq 'file' && ref($v) eq 'ARRAY') {
    	$v = $v->[0];
    }elsif($t eq 'mselect' || $t eq 'checkbox') {
    	my @vs = split "\0", $v;
    	$v = join("\t", @vs);
    }
    $v = hSz::eTz($v) if $enc;
    return $v;
}   

sub fLz{
    my  ($self) = @_;
    my ($k, $v, $a, $t) = ($self->{name}, $self->{val}, $self->{fQz}, $self->{type});
    my $subs;
    if($t eq 'const' || $t eq 'fixed') {
	return $v;
    }
    if($t eq 'textarea') {
		$subs =  qq(<textarea $a name="$k">$v</textarea>);
		return $subs;
    }
    my $sq = '&#39;';
    $subs=   qq(<input type="$t" $a name="$k");
    if( $t eq "checkbox" ) {
 			$subs .= " checked" if $v;
    } else{
           		$v =~ s/'/$sq/ge;
      			$subs .= qq( value='$v');
    }
    $subs .=  ">";
    return $subs;
}

sub iQz{
    my ($v) = @_;
    return unpack("h*", $v);
}
     
sub iNz{
    my ($v) = @_;
    return pack("h*", $v);
}

sub iLz{
	my $str = shift;
	my @aCz= split "\n", $str;
	my @a;
	for(@aCz) {
		my @pair= hSz::split_str($_);
		push @a, @pair if @pair;
	}
	return @a;
}

1;

package fMz;
use vars qw(@ISA);

#IF_AUTO use hZz;

BEGIN {
@ISA = qw(hZz);
}

sub new {
	my $type = shift;
	my ($k, $t, $a, $v, $r) = @_;
 	my $self = new hZz(@_);
	my @a=();
	if(ref $a eq 'ARRAY') {
		@a = @$a;
	}else {
		@a = hZz::iLz($a);
	}
        my ($opt, $lab);
	my $cnt = @a;
	my $i;
	for($i=0; $i<$cnt; $i+=2) {
		$opt = $a[$i];
		next if not defined($opt);
		$lab = $a[$i+1];
		$self->{vhash}->{$opt} = $lab;
		push @{$self->{karr}}, $opt;

	}
	return bless $self, $type;
}

sub hLz{
	my ($self, $v) = @_;
	$v = $self->{val} if not defined $v;
	return $self->{vhash}->{$v} || $v;
}

sub iWz{
	my ($self, $v, $lnkfunc)  = @_;
        my %links;
	for(@{$self->{karr}}) {
		my $lab = $self->{vhash}->{$_};
                if ($v ne $_) {
                	$links{$_} = hSz::gQ($lab, &$lnkfunc($_));
		}else {
                	$links{$_} =  "<b>$lab</b>";
		}
	}
	return \%links; 
}

1;

package hCz;
use vars qw(@ISA);

#IF_AUTO use fMz;

BEGIN{
	@ISA=qw(fMz);
}

sub new {
	my $type = shift;
	my $self = new fMz(@_);
	return bless $self, $type;
}

sub fLz{
	my ($self, $v) = @_;
	$v = $self->{val} if not defined $v;
        my $sel;
	my ($subs, $lab);
        $subs = '&nbsp;&nbsp; ';
	for(@{$self->{karr}}) {
		$sel="";
		$lab = $self->{vhash}->{$_};
		$sel =' CHECKED' if $_ eq $v;
		$subs .= qq(<input type="radio" name="$self->{name}" value="$_"$sel>$lab\&nbsp;\&nbsp; );
	}
	return $subs;
}

1;

package gFz;
use vars qw(@ISA);

#IF_AUTO use fMz;
BEGIN{
@ISA=qw(fMz);
}

sub new {
	my $type = shift;
	my $self = new fMz(@_);
	return bless $self, $type;
}

sub fLz{
	my ($self, $v) = @_;
	$v = $self->{val} if not defined $v;
        my $sel;
	my ($opt, $lab);
	my %vhas;
	my $subs;
	for(split ("\t|\0", $v)) {
			$vhas{$_}=1;
	}
	for(@{$self->{karr}}) {
		$sel="";
		$lab = $self->{vhash}->{$_};
		$sel =' CHECKED' if $vhas{$_};
		$subs .= qq(<input type="checkbox" name="$self->{name}" value="$_"$sel>$lab<br>\n);
	}
	return $subs;
}

sub hLz{
	my ($self, $v) = @_;
	$v = $self->{val} if not defined $v;
	my @vs = split ("\t|\0", $v);
	if(not $self->{vhash}) {
		return join("; ", @vs);
	}
	return join(";", @{$self->{vhash}}{@vs});
}

1;

package fRz;
use vars qw(@ISA);

#IF_AUTO use fMz;
BEGIN{
@ISA=qw(fMz);
}

sub new {
	my $type = shift;
	my $self = new fMz(@_);
	return bless $self, $type;
}

sub fLz{
	my ($self, $v, $extra) = @_;
	$v = $self->{val} if not defined $v;
        my $sel;
	my $mult = ' MULTIPLE' if $self->{type} eq 'mselect';
        $mult .=" $extra" if $extra;
	my $subs = qq(<select name="$self->{name}"$mult>);
	my ($opt, $lab);
	my %vhas;
	for(split ("\t|\0", $v)) {
			$vhas{$_}=1;
	}
	for(@{$self->{karr}}) {
		$sel="";
		$lab = $self->{vhash}->{$_} ||'-----';
		$sel =' SELECTED' if $vhas{$_};
		$subs .= qq(<option value="$_"$sel>$lab);
	}
	$subs .=qq(</select>\n);
	return $subs;
}

sub hLz{
	my ($self, $v) = @_;
	$v = $self->{val} if not defined $v;
	my @vs = split ("\t|\0", $v);
	if(not $self->{vhash}) {
		return join("; ", @vs);
	}
	return join(";", @{$self->{vhash}}{@vs});
}

1;
		


package gOz;
#IF_AUTO use hZz;
#IF_AUTO use fMz;
#IF_AUTO use hCz;
#IF_AUTO use fRz;
#IF_AUTO use gFz;

use vars qw(@cfgfs);
#use strict;

BEGIN {
@cfgfs=qw(name gSz cgi method temp tgt filedir);
}

#for radio button the  cfg look like
#['key', 'radio', [option1=>"Label 1", option2=>"Label 2"], "Description for this key", "default"]
#or
#['key', 'radio', "option1=Label 1\noption2=Label 2", "Description for this key", "default"]

#for single selection the cfg looks like
#['key', 'select', [option1=>"Label 1", option2=>"Label 2"], "Description for this key", "default"]
#['key', 'select', "option1=Label 1\noption2=Label 2", "Description for this key", "default"]

#for multi selection the cfg looks like
#['key', 'mselect', [option1=>"Label 1", option2=>"Label 2"], "Description for this key", "option1"]

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__

sub new {
    my $type = shift;
    my $self = {};
    $self->{fXz} = {};
    my $fQz = $self->{fXz};
    @{$fQz}{@cfgfs} = @_;
    if($fQz->{gSz}) {
 	foreach my $p (@{$fQz->{gSz}}) {
                next if not $p;
                next if $p->[1] eq 'head';
                $self->{$p->[0]} = $p->[4];
                $fQz->{ftmap}->{$p->[0]} = $p->[1];
		$fQz->{fobj}->{$p->[0]} = hYz($p);
        }
    }
    return bless $self, $type;
}

sub hYz{
	my ($refa) =@_;
        my $t = $refa->[1];
	if($t eq 'select' || $t eq 'mselect') {
		return new fRz(@$refa);
	}
	if($t eq 'radio') {
		return new hCz(@$refa);
	}
	if($t eq 'checkbox') {
		return new gFz(@$refa);
	}
	if($t eq 'textarea' || $t eq 'hidden'|| $t eq 'text' || $t eq 'file' || $t eq 'password' || $t eq 'const' || $t eq 'fixed'){
		return new hZz(@$refa);
	}
	return new hZz(@$refa);
}

sub gXz{
    my ($self, $f) = @_;
    my $fQz = $self->{fXz};
    for(my $i=0; $i< @{$fQz->{gSz}}; $i++) {
                my $p =${$fQz->{gSz}}[$i];
                next if not $p; 
                if($p->[0] eq $f->[0]) {
                	${$fQz->{gSz}}[$i] = $f;
			$fQz->{fobj}->{$p->[0]} = hYz($f);
		}
   }
}

sub gBz{
    my ($self, $gK) = @_;
    my $fQz = $self->{fXz};
    return if not $fQz->{gSz};
    for(my $i=0; $i< @{$fQz->{gSz}}; $i++) {
                my $p =${$fQz->{gSz}}[$i];
                next if not $p; 
                if($p->[0] eq $gK) {
                	return ${$fQz->{gSz}}[$i];
		}
   }
}

sub gIz{
    my ($self, $fn) = @_;
    my $fQz = $self->{fXz};
    for(my $i=0; $i< @{$fQz->{gSz}}; $i++) {
                my $p =${$fQz->{gSz}}[$i];
                next if not $p;
                if($p->[0] eq $fn) {
                	${$fQz->{gSz}}[$i] = undef;
			delete $fQz->{fobj}->{$p->[0]};
		}
   }
}

sub iDz{
    my ($self, $f, $v) = @_;
    my $fQz = $self->{fXz};
    $fQz->{fobj}->{$f}->{val} = $v;
    $self->{$f} = $v;
}

sub fTz{
	my ($self, $fsref, $req) = @_;
	my $fQz = $self->{fXz};
        for(@$fsref) {
                my $ele= $fQz->{fobj}->{$_};
		next if not $ele;
		$ele->gAz(\&hZz::iSz) if $req;
	}
}

sub gAz{
	my ($self, $key, @verfs) = @_;
	my $fQz = $self->{fXz};
	$fQz->{fobj}->{$key}->gAz(@verfs);

}

sub iGz{
	my ($self, $key, $sfunc) = @_;
	my $fQz = $self->{fXz};
	$fQz->{fobj}->{$key}->iGz($sfunc);
}
 
sub iAz{
	my ($self, $type, $sfunc) = @_;
	my $fQz = $self->{fXz};
	foreach my $p (@{$fQz->{gSz}}) {
                next if not $p;
                my $ele= $fQz->{fobj}->{$p->[0]};
		next if not $ele;
		next if($ele->{type} ne $type); 
		$ele->iGz($sfunc);
	}
}
sub hOz{
	my ($self, $type, @verfs) = @_;
	my $fQz = $self->{fXz};
	foreach my $p (@{$fQz->{gSz}}) {
                next if not $p;
                my $ele= $fQz->{fobj}->{$p->[0]};
		next if not $ele;
		next if($ele->{type} ne $type); 
		$ele->gAz(@verfs);
	}
}

sub gWz {
	my ($self, $tag)= @_;
	$self->{fXz}->{_req_tag}= $tag;
}

sub iFz{
	my ($self)=@_;
	$self->{fXz}->{_no_abort}=1;
}

sub hAz {
	my ($self, $errt, $err) = @_;
	if($self->{fXz}->{_no_abort} ) {
		return @{$self->{fXz}->{_last_error}} if not $err;
		$self->{fXz}->{_last_error} = [$errt, $err];
		return;
	}
        main::error($errt, $err);
}
        

sub hTz {
    my ($self, $cgi)=@_;
    $self->{fXz}->{cgi} = $cgi;
}

sub fUz{
    my ($self, $tmp)=@_;
    $self->{fXz}->{temp} = $tmp;
}

sub iCz{
	my ($self, $tmfile)=@_;
	open F, "<$tmfile" or return;
	$self->fUz(join("", <F>));
	close F;
}

   
sub hQz {
    my ($self, $f)=@_;
    return if not $f;
    push @{$self->{fXz}->{gSz}}, $f;
    $self->{fXz}->{fobj}->{$f->[0]} = hYz($f);
}

sub iJz {
	my ($self, $colorh, $coloro, $colore) = @_;
	$self->{fXz}->{_colors}= [$colorh, $coloro, $colore];
}

sub hDz {
        my ($self, $skips)=@_;
        $self->{fXz}->{def_temp} = $self->fPz(0, $skips);
}
 

sub fPz {
        my ($self, $viewonly, $skips)=@_;
	my $fQz = $self->{fXz};
	my @aCz;

        $self->iJz($main::bar_bg_color, @main::bgcols) if not $fQz->{_colors};
        my ($bgh, $bgo, $bge) = @{$fQz->{_colors}};
        $bgh = qq(bgcolor="$bgh") if $bgh;
        $bgo = qq(bgcolor="$bgo") if $bgo;
        $bge = qq(bgcolor="$bge") if $bge;
	push @aCz, qq(<table cellspacing="0" border="0" cellpadding="0" align="center" width="100%" bgcolor="#000000">\n<tr><td>\n);
	push @aCz, qq(<table border="0" cellspacing="1" cellpadding="3" align="center" width="100%">\n);

	my ($p, $k, $i);
        my $hidden_str;
	my $plc=qq(CLASS="PFTDL");
	my $prc=qq(CLASS="PFTDR");

        $i =1;
	foreach $p (@{$fQz->{gSz}}) {
                next if not $p;
                next if $p->[1] eq 'skip';
		if($p->[1] eq 'head') {
    			my $h = $p->[2];
    			push @aCz, qq(<tr $bgh align=left><td colspan=2>\&nbsp;<br><font color="$main::bar_txt_color" face="Verdana"><b>$h</b></font></td></tr>\n);
    			next;
		}
                my $ele= $fQz->{fobj}->{$p->[0]};
		next if not $ele;
		my ($k, $t, $d) =  @{$ele}{qw(name type desc)};
                if ($t eq 'hidden' || $t eq 'command') {
                    next;
                }
		next if $skips->{$k};
		my $col = $i++%2 ? $bgo : $bge;
                if (not $d) {
                      $d = $k;
                      $d =~ s/_/ /g;
                      $d = ucfirst($d);
                }
	        push @aCz, qq(<tr $col>\n<td valign="top">$d</td>\n<td>\{$k\}</td>\n</tr>\n);
	}
	push @aCz, "\{_COMMAND_\}\n" if not $viewonly;
        push @aCz, "</table>\n</td></tr></table>";
        return join "", @aCz;
}
 
sub hWz{
	my $self = shift;
	my $fQz = $self->{fXz};
        my @miss;
	foreach my $p (@{$fQz->{gSz}}) {
                next if not $p;
                my $ele= $fQz->{fobj}->{$p->[0]};
		next if not $ele;
		next if($ele->{type} eq 'head'); 
		push @miss, $ele->{desc}. ":".$ele->{_error} if not $ele->validate();
	}
	return @miss;
}

sub fJz {
	my $self = shift;
	my $fQz = $self->{fXz};
        my @miss;
	foreach my $p (@{$fQz->{gSz}}) {
                next if not $p;
                my $ele= $fQz->{fobj}->{$p->[0]};
		next if not $ele;
		next if($ele->{type} eq 'head'); 
		next if($ele->{type} eq 'const'); 
		push @miss, $p->[0];
	}
	return @miss;
}

     
#Third a argument is a reference to an array of skipped fields, such as [ 'field1', 'field2']

sub form{
	my ($self, $view_only, $hIz, $mark_inval) = @_; 
	my $fQz = $self->{fXz};
	my $name = $fQz->{name};
	my $cgi  = $fQz->{cgi}; 
	my $method = $fQz->{method} || 'POST';
        my %skips=();
	my @aCz;
	if($hIz) {
		for(@$hIz) {
			$skips{$_} =1;
		}
	}


        my $cmdstr=qq(<tr bgcolor="#eeeeee">\n<td><input type="reset" value="Reset"></td>\n<td><input type="submit"  value="Submit"></td>\n</tr>\n) if not $view_only;

	if (not $self->{fXz}->{temp}) {
	       	 $self->hDz(\%skips);
	       	 $self->{fXz}->{temp} = $self->{fXz}->{def_temp};
	}
 
	my $subs;
	my $ftemp = $self->{fXz}->{temp};
        my $enc ="";
        my $has_file;
        my @fields;
        my @types;
        my $hidden_str;
	my $reqtag= $fQz->{_req_tag} || "<font color=red size=1>(required)</font>";
	foreach my $p (@{$fQz->{gSz}}) {
                next if not $p;
                my $ele= $fQz->{fobj}->{$p->[0]};
		next if not $ele;
		next if($ele->{type} eq 'head'); 
		my $v;
		my ($k, $t, $a,  $d) = @{$ele}{qw(name type fQz desc)};
                push @fields, $k;
                push @types, $t;

		if ($self->{$k}) {
		     $v = $self->{$k};
		}else {
                     $v = $ele->{val};
                }
     
		$v="" if $t eq 'password';
                if($t eq 'hidden' || $t eq 'command') {
			next if $view_only;
  			$hidden_str .=qq(<input type="hidden" name="$k" value="$v">\n);
  		}

                if (not $view_only) {
                     $subs = $ele->fLz($v);
		     $subs .= " $reqtag" if not $ele->validate("");
		     $subs .= qq( Error: <font color="red">$ele->{_error}</font>) if $mark_inval && not $ele->validate(); 
                     $has_file = 1 if $t eq 'file';
                }else {
                     $subs = $ele->hLz($v);
                }
                $subs = '&nbsp;' if not $subs;
                $ftemp =~ s/\{$k\}/$subs/g;
	}
        my $fs = join('#', @fields);
        my $ts = join('#', @types);
        $ftemp =~ s/\{_COMMAND_\}/$cmdstr/g;
	return $ftemp if $view_only;
	$method=$fQz->{method} || 'POST';
        $enc= qq(ENCTYPE="multipart/form-data") if $has_file;
	my $tgt=""; $tgt= qq( target="$fQz->{tgt}" ) if $fQz->{tgt};
	return qq(<form name="$name" action="$fQz->{cgi}" $enc method=$method $tgt>\n$ftemp\n
$hidden_str
<input type="hidden" name="_af_xlist_" value="$fs">
<input type="hidden" name="_af_tlist_" value="$ts">
</form>);
}

sub fOz {
    my($self, $field, $form) = @_;
    my $ele = $self->{fXz}->{fobj}->{$field};
    return if not $ele;
    my $type = $ele->{type};
    return if ($type eq 'head' || $type eq 'const' || $type eq 'fixed');
    $self->{$field}=$ele->iMz($form);
}

sub hFz {
  my($self, $other, $def) = @_;
  my $cfgsref;
  my $fQz = $self->{fXz};
  foreach (@{$fQz->{gSz}}) {
        next if not $_;
	next if $def && not exists $other->{$_->[0]};
	$self->fOz($_->[0], $other);
   }
}

sub fZz {
  my($self, $form, $fields) = @_;
  my $fQz = $self->{fXz};

  my (@fs, @ts);
  my %ftmap;
  if($fields) {
       @fs = @$fields;
  }elsif($form->{_af_xlist_}) {
       @fs = split ('#', $form->{_af_xlist_});
       @ts = split ('#', $form->{_af_tlist_});
       map { $ftmap{$fs[$_]} = $ts[$_] } 0 .. $#fs;
  }else {
       @fs = sort keys %$form;
  }
  delete $form->{_af_xlist_};
  delete $form->{_af_tlist_};
  foreach (@fs){
           my $t =  $ftmap{$_};
           if (ref($form->{$_}) eq 'ARRAY') {
              $t = 'file';
           }
           if (not $t) {
		if(index("\0", $form->{$_}) < length($form->{$_}) ) {
		   $t = 'checkbox';
                }else {
	           $t = 'textarea' ;
		}
	   }

	   
           $self->hQz([$_, $t, "", $_]) unless $fQz->{ftmap}->{$_};
	   $self->fOz($_, $form);
   }
}

sub iHz{
   my($self, $adb) = @_;
   $adb->jYz([$self->pkey(), $self->gTz()]);

}

sub fKz{
   my($self, $adb) = @_;
   $adb->kRz([$self->pkey(), $self->gTz()]);

}

sub iBz{
   my($self, $pkey, $adb) = @_;
   $adb->kBz([$self->pkey()]);
}

sub gLz{
   my($self, $pkey, $adb) = @_;
   my $row = $adb->get_rows_by_id($self->pkey());
   return if not $row;
   $self->gGz(@$row);
}

sub store {
   my($self, $datafile, $datad) = @_;
   open CFGFILE, ">$datafile" or return $self->hAz('sys', "On writing $datafile: $!") ;
   my $formdata= $self->gYz($datad||$self->{filedir}, 1);
   $formdata->fVz(\*CFGFILE);
   close CFGFILE;
   chmod 0600, $datafile;
}

sub gYz{
   my($self, $datad, $store_data) = @_;
   my $fQz = $self->{fXz};
   my @fs =();
   my @ts =();
   my $formdata= aVz->iXz("anyform_$self->{name}");
  
   foreach (@{$fQz->{gSz}}) {
            next if not $_;
            my $ele= $fQz->{fobj}->{$_->[0]};
	    next if not $ele;
            my $fn = $ele->{name};
            my $ft = $ele->{type};
            next if ($ft eq 'head' || $ft eq 'command');
            push @fs, $fn;
            push @ts, $ft;
            my $v = $self->{$fn};
            my $sv;
            if($ft eq 'file' and $v ne "") {
                my $path;
                if( $datad && $store_data) {
                	$path = hSz::eCz($datad, $v->[0]);
                	open DF, ">$path" or next;
                	binmode DF;
                	print DF $v->[1];
                	close DF;
                }else {
                        $path = $v->[0];
                }
		$sv = $path;
           
            }else {
		  $sv = $ele->gJz($v);
	    }
            $formdata->iZz(aVz->iXz($fn, [$sv], "text/plain"));
    }
    $formdata->iZz(aVz->iXz("_af_xlist_", [join ("#", @fs)], "text/plain"));
    $formdata->iZz(aVz->iXz("_af_tlist_", [join ("#", @ts)], "text/plain"));
    return $formdata;
}

sub gTz{
   my($self) = @_;
   my $fQz = $self->{fXz};
   my @fs =();
   foreach (@{$fQz->{gSz}}) {
            next if not $_;
            my $ele= $fQz->{fobj}->{$_->[0]};
	    next if not $ele;
            my $fn = $ele->{name};
            my $ft = $_->[1];
            next if ($ft eq 'head' || $ft eq 'command');
            my $v = $self->{$fn};
            my $sv;
            if($ft eq 'file' and $v ne "") {
                my $path = $v->[0];
		$sv = $path;
           
            }else {
		  $sv = $ele->gJz($v);
	    }
	    push @fs, hSz::eTz($sv);
    }
    return @fs;
}

sub gGz{
   my($self, @fs) = @_;
   return if not @fs;
   my $fQz = $self->{fXz};
   foreach (@{$fQz->{gSz}}) {
            next if not $_;
            my $fn = $_->[0];
            my $ft = $_->[1];
            next if ($ft eq 'head' || $ft eq 'command');
	    $self->iDz($fn, hSz::ePz(shift @fs));
    }
}

sub load{
   my($self, $cfgfile, $init) = @_;

   open CFGFILE, "<$cfgfile" or 
   return $self->hAz('sys', "$self->{name}: on reading file $cfgfile: $!") ;
   my @plines = <CFGFILE>;
   close CFGFILE;

   my $mime = aVz->new(\@plines);
   $mime->parse();
   $self->gVz($mime, $init);
           
}

sub gVz{
   my($self, $mime, $init) = @_;
   my %mycfgs;

   for my $aJz(@{$mime->{aFz}}) {
                    my $name= $aJz->{bHz};
                    my $val = $aJz->aWz();
                    if (length($aJz->{bFz})>0) {
                      $aJz->{bFz} =~ s/\s+/_/g;
                      $mycfgs{$name} = [$aJz->{bFz}, $val, $aJz->{head}->{'content-type'}];
                    } else {
    	              if (defined($mycfgs{$name})){
    	              	$mycfgs{$name} .= "\0" if defined($mycfgs{$name}); 
                      }
    	              $mycfgs{$name} .=  $val;
                    }
   }
          
   if($init) {
            $self->fZz(\%mycfgs,undef, 1);
             return;
   }
   delete $mycfgs{_af_tlist};
   delete $mycfgs{_af_xlist};

   my $cfgsref;
   my $fQz = $self->{fXz};
   foreach  (@{$fQz->{gSz}}) {
           next if not $_;
   	   my $cfg = $_->[0];
   	   my $t = $_->[1];
	   my $v;
   	   next if not exists $mycfgs{$cfg}; 
           next if ($t eq 'head' || $t eq 'const' || $t eq 'fixed' || $t eq 'command');
   	   $v = $mycfgs{$cfg} if exists $mycfgs{$cfg}; 
	   $self->iDz($cfg, $v);
   }
}

sub gCz {
   my($self, $cfgfile) = @_;
   open CFGFILE, ">$cfgfile" or return $self->hAz('sys', "On writing $cfgfile: $!") ;
   my $fQz = $self->{fXz};
   my @fs =();
   my $formdata= aVz->iXz("def");
  
   my $dlen = @hZz::fs;
   foreach my $p (@{$fQz->{gSz}}) {
            next if not $p;
            my $fn = $p->[0];
	    for (my $i=0; $i<$dlen; $i++){ 
            	$formdata->iZz(aVz->iXz("$fn.".$hZz::fs[$i], [$p->[$i]], "text/plain"));
	    }
	    push @fs, $fn;
    }
    $formdata->iZz(aVz->iXz("_af_xlist_", [join ("#", @fs)], "text/plain"));
    $formdata->iZz(aVz->iXz("_af_temp_", [$self->{temp}], "text/plain"));
    $formdata->fVz(\*CFGFILE);
    close CFGFILE;
    chmod 0600, $cfgfile;
}

sub gPz{
   my($self, $cfgfile) = @_;
   my %mycfgs;

   open CFGFILE, "<$cfgfile" or 
   return $self->hAz('sys', "$self->{name}: on reading file $cfgfile: $!") ;
   my @plines = <CFGFILE>;
   close CFGFILE;

   my $mime = aVz->new(\@plines);
   $mime->parse();
   for my $aJz(@{$mime->{aFz}}) {
                    my $name= $aJz->{bHz};
                    my $val = $aJz->aWz();
                    $mycfgs{$name} =  $val;
   }
   my @fs = split ('#', $mycfgs{_af_xlist_});
   for my $fn(@fs) {
		my @fdefs=();
   		for my $ff (@hZz::fs) {
			push @fdefs, $mycfgs{"$fn.$ff"};
		}
		$self->hQz([@fdefs]);
   }
}

sub fWz{
    my ($t) = @_;
    $t = time() if not $t;
     my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst)=localtime($t);
     my $aorp;
    	$aorp = $hour>12 ? "PM": "AM";
    	$hour -= 12 if $hour > 12;;
    	$hour = "0$hour" if $hour<10;
    	$min = "0$min" if $min<10;
    	$mon = "0$mon" if $mon<10;
    	$mday = "0$mday" if $mday<10;
    	$year+=1900;
    return  join(':', $year, $mon, $mday, sprintf("%02d",$hour), sprintf("%02d", $min), $aorp, $wday);
}

sub gUz{
    my ($id, $ts) = @_;
    $ts = fWz() if not $ts;

    my($min,$hour,$mday,$mon,$year, $aorp, $wday);
    ($year, $mon, $mday, $hour, $min, $aorp, $wday) = split /:/, $ts;
    my ($y, $m, $d, $h, $mn, $ap);
       
    my @dT = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
    $y = make_select($id."_year", [$year-1, $year, $year+1, $year+2, $year+3, $year+4], $year);
    $m = make_select($id."_month", [map {sprintf("%02d", $_)}(0..11)], $mon, \@dT);
    $d = make_select($id."_day", [map {sprintf("%02d", $_)}(1..31)], $mday);
    $h = qq(<input type=text name="${id}_hour" value="$hour" size=2 maxlength=2>);
    $mn = qq(<input type=text name="${id}_minute" value="$min" size=2 maxlength=2>);
    $ap = make_select($id."_apm",  [qw(AM PM)], $aorp);
    return "$d - $m - $y, $h:$mn $ap";

}

sub hHz{
    my ($ts) = @_;
    $ts = fWz() if not $ts;

    my($min,$hour,$mday,$mon,$year, $aorp, $wday);
    ($year, $mon, $mday, $hour, $min, $aorp) = split /:/, $ts;
       
    my @dT = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
    my	@wdays  = qw(Sun Mon Tue Wed Thu Fri Sat);
    my $m = $dT[$mon];
    my $w = $wdays[$wday],
    return "$m $mday, $year, $hour:$min $aorp";

}

sub hKz {
    my ($vfref, $id) = @_;
    my ($y, $m, $d, $h, $mn, $ap)=
    ($vfref->{$id."_year"}, $vfref->{$id."_month"}, $vfref->{$id."_day"},
     $vfref->{$id."_hour"}, $vfref->{$id."_minute"}, $vfref->{$id."_apm"});
    return wantarray? ($y, $m, $d, $h, $mn, $ap) : join(":", $y,$m,$d,sprintf("%02d",$h),sprintf("%02d", $mn), $ap);
}


1;

package hNz;

BEGIN{
 use vars qw(@card_specs);
 @card_specs = (
   [MC=> '5[1-5]', 16, 10, "Master Card"],
   [VISA=>'4', 16, 10, "Visa"],
   [VISA=>'4', 13, 10, "Visa"],
   [DISC=>'6011', 16, 10, "Discover"],
   [AMEX=>'34|37', 15, 10, "American Express"],
   [DCCB=>'30[0-5]|36|38', 14, 10, "Dinners Club/Carte Blanche"],
   [JCB=>'3', 16, 10, "JCB"],
   [ENR=>'2014|2149', 15, 1, "enRoute"],
   [JCB=>'2131|1800', 15, 10, "JCB"]
 );
}

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__

sub hRz{
   my $pure_cn = shift;
   $pure_cn =~ s/\D//g;
   my @digits = reverse split //, $pure_cn;
   my $len = length($pure_cn);
   return undef if($len < 13);
   my $sum =0;
   for(my $i=0; $i<$len; $i++) {
        my $tmp = $digits[$i]*(1+ ($i%2));
	$sum += int $tmp/10 + $tmp%10;

   }

   for (@card_specs) {
         next if $len != $_->[2];
         next if not $pure_cn =~ /^($_->[1])/;
         next if ($sum % $_->[3]);
         return $_->[0];
  }
  return undef;
}

1;


package hVz;
#IF_AUTO use gOz;

BEGIN {
  @hVz::fs=qw(file form);
}

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__

sub new {
	my $type = shift;
	my $self = {};
	@{$self}{@hVz::fs} = @_;
	$self->{entry_hash} = {}; 
	$self->{max_idx} = 0;
	bless $self, $type;
	if($self->{file} && -r $self->{file}) {
		$self->load();
	}
	return $self;
}

sub hMz {
	my ($self, $eQ,  $tm,  $aJz) = @_;
	return if not $aJz;
	$self->{entry_hash}->{$eQ} = [$tm, $aJz->gTz()];
	if($eQ > $self->{max_idx}) {
		$self->{max_idx} = $eQ;
	}
}

sub gEz {
	my ($self, $eQ,  $tm,  $aJz) = @_;
	return if not $aJz;
	$self->{entry_hash}->{$eQ} = [$tm, $aJz->gTz()];
}

sub fNz{
	my ($self, $line) = @_;
	return if not $line;
	my @fs = split /\t/, $line;
	my $eQ = shift @fs;
	$self->{entry_hash}->{$eQ} = [@fs];
	if($eQ > $self->{max_idx}) {
		$self->{max_idx} = $eQ;
	}
}

sub gRz{
	my ($self, $eQ, $sync) = @_;
	delete $self->{entry_hash}->{$eQ};
	$self->store() if $sync;
}

sub hPz {
	my ($self)=@_;
        return keys %{$self->{entry_hash}};
}

sub gDz{
	my ($self, $eQ)=@_;
        return if not ref($self->{entry_hash}->{$eQ});
        my @eSz = @{$self->{entry_hash}->{$eQ}};
        for(@eSz) {
		$_ = hSz::ePz($_);
        }
	return @eSz;
}

sub gQz{
	my ($self, $eQ, $aJz)=@_;
	my @eSz = $self->gDz($eQ);
	my $len = @eSz;
        $aJz->gGz(@eSz[1..$len-1]);
	return $aJz;
}

sub fVz{
	my ($self, $fh) = @_;
	my ($k, $v);
	for $k (sort keys %{$self->{entry_hash}}) {
		$v = $self->{entry_hash}->{$k};
		print $fh join("\t", $k, @$v), "\n";
	}
} 

sub store{
	my ($self, $file) = @_;
	$file = $self->{file} if not $file;
	local *F;
	open F, ">$file";
	$self->fVz(\*F);
	close F;

} 
sub hUz{
	my ($self, $fh) = @_;
	while(<$fh>) {
		chomp;
		$self->fNz($_);
	}
} 

sub load{
	my ($self, $file) = @_;
	$file = $self->{file} if not $file;
        local *F;
	open F, "<$file" or return;
	$self->hUz(\*F);
	close F;
} 

1;


package hSz;

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__

sub eCz{
    my ($root, @dSz)= @_;
    for(@dSz) {
        $_ =~ s#^/?##;
        $root =~ s#/?$#/#;
        $root .= $_; 
    }
    return $root;
}

sub split_str {
    my ($str, $sep) = @_;
    $sep = "=" if not $sep;
    my ($k, $v, $pos);
    $pos = index $_, $sep;
    return if $pos <0;
    $k = substr $_, 0, $pos;
    $v = substr $_, $pos+1;
    return ($k, $v);
}
sub eTz {   
    my $str = shift;
    return "" if not $str;
    $str =~ s/([" %&+<=>'\r\n\t])/sprintf '%%%.2X' => ord $1/eg;
    return $str;
}

sub ePz{
     my $v = shift;
     $v =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/chr(hex($1))/ge;
     return $v;
}
	
sub bytes2mb {
	my ($fsize) = @_;
	if($fsize < 10* 1024) {
		return "$fsize b";
	}elsif($fsize < 10* 1024* 1024) {
    		return sprintf ("%.1f KB",$fsize/1024);
	}else{
    		return sprintf ("%.1f MB", $fsize/1024/1024);
	}
}

sub error {
   my ($error, $emsg, $suggest)  = @_;
   my $error_type = $error;
   my $error_msg  = "Unknown";
   my $error_act = "Notify webmaster";

   my $var = $ecodes{$error};
   if($var) {
        $error_type = $var->[0];
        $error_msg = $var->[1];
        $error_act  = $suggest || $var->[2];
   }

   my $header ="";
   $error =~ s#$err_filter#X#g if $err_filter;
   $emsg =~ s#$err_filter#X#g if $err_filter;


   print "Content-type: text/html$charset_str\n";

   print $header;
   print "\n<html><head><title>Error: $emsg</title>\n";
   if($abmain::bd) {
	print $abmain::bd->{other_header};
   }else {
   	print qq(<body bgcolor="$body_bg_color">);
   }
   print qq(<table width="75%" align="center" border="0"><tr><td><h3>$emsg</h3></td></tr></table><br/>);
   print qq( 
<table align="center" border="0" cellpadding=0 cellspacing=0 width=75% bgcolor="#000000"><tr><td>
<table align="center" border="0" width=100% cellspacing=1 cellpadding=5>
<tr bgcolor="#cc0000"><th colspan=2> <font color="#ffffff">$emsg</font></th></tr> 
<tr bgcolor="#d3e3f8"><th>Error type</th><th> $error_type</th></tr> 
<tr bgcolor="#ffffff"><td> General description</td><td> $error_msg</td></tr> 
<tr bgcolor="#d3e3f8"><td>Suggested action</td><td>$error_act</td></tr>
</td></tr></table>
</table>
);
   print "<p><p>\n";
   if($abmain::bd) {
	print $abmain::bd->{other_footer};
   }else {
   	print "</body></html>\n";
   }
  
   main::cXz(); 
   
}  

sub iEz{
   my ($url, $str, $popwin, $attr, $w, $h) = @_;
   return '' if !$url;
   return '' if !$str;
   $popwin="netbula_new" if $popwin eq "";
   $w = 0.6 if not $w;
   $h = 0.6 if not $h;
   return qq(<a href="javascript:dGz('$url', '$popwin', $w, $h,'yes')">$str</a>);
}

sub link_str_pop_o{
   my ($url, $str, $popwin, $attr, $w, $h) = @_;
   return '' if !$url;
   return '' if !$str;
   $popwin="netbula_new" if not $popwin;
   return qq(<a href="$url" $attr onclick="dGz(this.href, '$popwin', $w||0.6, $h||0.6,'yes');return false;false;">$str</a>);
}


sub gQ {
   my ($url, $str, $tgt, $action) = @_;
   return '' if !$url;
   return '' if !$str;
   my $cls = qq( class="$link_class") if $main::link_class;
   return qq(<a href="$url" target="$tgt" $action$cls>$str</a>) if $tgt;
   return qq(<a href="$url" $action$cls>$str</a>);
}

sub lHz{
	my ($lVz, $txt, $bgcolor, $lGz, $lEz) = @_;
	$lEz = "/abicons/formicons" if not $lEz;
	$bgcolor = "#e4e4be" if not $bgcolor;
	my $mAz = $txt;
	$mAz =~ s/'/\\'/g;
	$mAz =~ s/\n/\\n/g;
	$mAz =~ s/\r//g;

my $str = <<"END_OF_FANCY_FORM";
<table border="0" cellspacing="0" cellpadding="0" bgcolor="$bgcolor" width="100%" bordercolor="#f2f2df">
<tr valign="top"> 
 <td> 
       <table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%">
                 <tr valign="baseline"> 
                   <td nowrap> <img class='imgbutton' src="$lEz/new.gif" width="16" height="16" border="0" alt="New File" onClick="lRz('$lVz');"> 
                         <img class='imgbutton' src="$lEz/cut.gif" width="16" height="16" border="0" alt="Cut " onClick="lUz('$lVz', 'Cut')">&nbsp 
                                                                <img class='imgbutton' src="$lEz/copy.gif" width="16" height="16" border="0" alt="Copy" onClick="lUz('$lVz', 'Copy')">&nbsp 
                                                                <img class='imgbutton' src="$lEz/paste.gif" border="0" alt="Paste" onClick="lUz('$lVz', 'Paste')" width="16" height="16">&nbsp 
                                                              </td>
                                                      
                                                              <td nowrap> <img class='imgbutton' src="$lEz/ul.gif" width="16" height="16" border="0" alt="Bullet List" onClick="lUz('$lVz', 'InsertUnorderedList');" >&nbsp 
                                                                <img class='imgbutton' src="$lEz/ol.gif" width="16" height="16" border="0" alt="Numbered List" onClick="lUz('$lVz', 'InsertOrderedList');" >&nbsp 
                                                                <img class='imgbutton' src="$lEz/indent.gif" width="20" height="16" alt="Indent" onClick="lUz('$lVz', 'Indent')">&nbsp 
                                                                <img class='imgbutton' src="$lEz/outdent.gif" width="20" height="16" alt="Outdent" onClick="lUz('$lVz', 'Outdent')">&nbsp 
                                                                <img class='imgbutton' src="$lEz/hr.gif" width="16" height="18" alt="HR" onClick="lUz('$lVz', 'InsertHorizontalRule')">&nbsp 
                                                              </td>
                                                         
                                    <td> 
                                  <script>
                                      lPz("$lVz", new Array("Arial", "Times New Roman", "Verdana", "Courier New", "Georgia"));
				  </script>
                                    </td>
                                  
                              <td vlaign=baseline>
                                 <script>
                                      lLz("$lVz", new Array("1", "2", "3", "4", "5", "6", "7", "+1", "+2", "+3", "+4", "+5", "+6"));
				 </script>
                              </td><td vlaign=baseline>
							  <select name="mode" onChange="lCz('$lVz', this.value)" style="font: 9pt verdana;">
							  <option value="HTML" selected">HTML</option>
							  <option value="Text">Text</option>
							  </select>
							  </td>
                                                      </tr>
                                                    </table>
                                                  </td>
                                                </tr>
                                                <tr> 
                                                  <td height="41"> 
                                                    
                          <table border="0" width="100%">
                            <tr> 
                              <td nowrap valign="baseline" width=50%> 
                                <div align="left">
				  <img class='imgbutton' src="$lEz/bold.gif" width="16" height="16" border="0" align="absmiddle" alt="Bold text" onClick="lUz('$lVz', 'Bold')">&nbsp 
                                  <img class='imgbutton' src="$lEz/italics.gif" width="16" height="16" border="0" align="absmiddle" alt="Italic text" onClick="lUz('$lVz', 'Italic')">&nbsp 
                                  <img class='imgbutton' src="$lEz/underline.gif" width="16" height="16" border="0" align="absmiddle" alt="Underline text" onClick="lUz('$lVz', 'Underline')" >&nbsp 
                                  <img class='imgbutton' src="$lEz/left.gif" width="16" height="25" border="0" alt="Align Left" align="absmiddle"  onClick="lUz('$lVz', 'JustifyLeft')"> 
                                  <img class='imgbutton' src="$lEz/center.gif" width="16" height="16" border="0" alt="Align Center" align="absmiddle" onClick="lUz('$lVz', 'JustifyCenter')">&nbsp 
                                  <img class='imgbutton' src="$lEz/right.gif" width="16" height="16" border="0" alt="Align Right" align="absmiddle"  onClick="lUz('$lVz', 'JustifyRight')">&nbsp
				  <img class='imgbutton' src="$lEz/link.gif" border="0" alt="Add Link" onClick="lIz('$lVz');" width="20" height="16" > 
                                  <img class='imgbutton' src="$lEz/insertimg.gif" width="16" height="16" alt="Insert Image" onClick="lUz('$lVz', 'InsertImage')"> 
                                </div>
                               </td>
                               <td align="right" nowrap valign="baseline">
				<script>lNz("$lVz");</script>
                                                        </td>
                                                      </tr>
                                                    </table>
                                                    
                          
                                                  </td>
                                
                                        </tr>
                                        <tr valign="top" align="left"> 
                                          <td valign="top" height=$lGz> 
<script>
document.write('<iframe id=lZz$lVz width=100% height=100%></iframe>');
document.write('<textarea name="$lVz" style="display: none;" rows="1" cols="70">$mAz</textarea>');
document.write('<input type=hidden name="mKz" value="1">');
</script>
<noscript>
<textarea name="$lVz" rows="8" cols="70">$txt</textarea>
</noscript>


</td>
                          </tr>
                        </table>
<SCRIPT>
window.onload = new Function( "lDz('$lVz')" );
window.onunload = new Function( "kZz('$lVz')" );
</SCRIPT>
END_OF_FANCY_FORM

return $str;

};


sub lJz{

my $str = <<'END_OF_FANCY_JS';
//**************COPYRIGHT(2002) NETBULA LLC, COPYING OF THIS CODE STRICTLY PROHIBITED
//VIOLATORS WILL BE PROSECUTED

function lNz(mHz) {
var lAz = mHz +'lYz';
var txtid = mHz +'txt';
document.write('<table border=0 bgcolor="#eeeeff" cellpadding="0" cellspacing="0">'+
'<tr><td colspan=18 align=center id="' + txtid+ '"><font size=1 face=Verdana>Choose color</font></td>'+
'<td colspan=18 id="'+lAz+'" align=center bgcolor="#888888"><font size=1>&nbsp;</font></td></tr>');

clr = new Array('FF','CC','99','66','33','00');

for(k=0;k<6;++k){
  document.write('<tr>\n');
 for(j=0;j<6;j++){
         for(i=0;i<6;++i){
		    var bg = '#'+clr[k]+clr[j]+clr[i];
           document.write('<td width=8 height=5 bgcolor='+bg +'>');   
	   document.write('<img src=blank.gif width=8 height=5' + 
                               '     onClick="lBz(\'' + mHz + "', '" + bg + '\'); return true;" ' + 
                               ' onmouseover="lMz(\'' + mHz + "', '" + bg + '\'); return true;" ' + 
			'>');   
           document.write('</td>\n');
         }   
 }
 document.write('</tr>\n');
}

document.write('</table>');

}

function lLz(mHz, mGz) {
         document.write('<select name="size" onChange="lUz(\'' + mHz + '\', \'FontSize\',this);" style="font: 9pt verdana;">');
         document.write('<option value="None" selected>Size</option>');
	 var len = mGz.length;
	 for(i=0; i<len; i++) {
	    	document.write('<option value="' + mGz[i] + 
		 '" style="font-size: ' + mGz[i] +';">'+ mGz[i] + '</option>\n');
	 }
	 document.write("</select>");
}

function lPz(mHz, mDz) {
  document.write('<select name="font" onChange="lUz(\'' + mHz + '\', \'FontName\', this);" style="font: 9pt verdana;">');
  document.write('<option value="">Font Name</option>\n');
  var len = mDz.length;
  for(i=0; i<len; i++) {
    	document.write('<option value="' + mDz[i] + 
		 '" style="font: 9pt ', + mDz[i] +';"><font face=' + mDz[i]+'>'+ mDz[i] +'</font></option>\n');
  }
  document.write("</select>");
}


function lBz(mHz, lWz){
	lMz(mHz, lWz);
	lUz(mHz, 'ForeColor',lWz);
}

function lMz(mHz, lWz){
	var lYz = document.all[mHz+"txt"];
	lYz.firstChild.style.color=lWz;
	lYz = document.all[mHz+"lYz"];
	lYz.bgColor=lWz;	
	var fr =  lWz.substring(1,3);
	var fg = lWz.substring(3,5);
	var fb = lWz.substring(5,7);
	
	lYz.firstChild.firstChild.nodeValue= lWz;

	var col= (fr < "AA" && fg<"AA" && fb<"AA")? "#ffffff":"#000000";
	lYz.firstChild.style.color=col;
}

function lUz(mHz, what) {
		
	if(what == "FontName" || what == "FontSize"){
		if(arguments[2].selectedIndex != 0){
			lTz(mHz, what, arguments[2].value);
			arguments[2].selectedIndex = 0;
		} 
	}else {
	   lTz(mHz, what, arguments[2]);
	 
	}
}



function lIz(mHz){
	lUz(mHz, 'CreateLink');
}

function kZz(mHz) {
	var lZz = window.frames["lZz"+mHz];
	var theHtml = lZz.document.body.innerHTML;
	document.all[mHz].value = theHtml;
}

var lOz="HTML"

function lTz(mHz, command) {
var lZz = window.frames["lZz"+mHz];
lZz.focus();
 if (lOz=="HTML") {
  var lKz = lZz.document.selection.createRange()
  if (arguments[2]==null)
   lKz.execCommand(command, true)
  else
   lKz.execCommand(command,false, arguments[2])
  lKz.select()
  lZz.focus()
 }
}

function mEz(mHz){
var lZz = window.frames["lZz"+mHz];
var lKz = lZz.document;

lKz.execCommand('SelectAll');
lZz.focus();

}

function lRz(mHz) {
	var lZz = window.frames["lZz"+mHz];
	lZz.document.open()
	lZz.document.write("")
	lZz.document.close()
	lZz.focus()
}

function mCz(mHz, mBz) {
	var lZz = window.frames["lZz"+mHz];
	lZz.document.open()
	lZz.document.write(mBz)
	lZz.document.close()
}

function lDz(mHz) {
	var lZz = window.frames["lZz"+mHz];
	var mBz = document.all[mHz].value;
	lZz.document.designMode="On";
	lZz.document.execCommand("2D-Position", true, true);
	lZz.document.execCommand("MultipleSelection", true, true);
	lZz.document.execCommand("LiveResize", true, true);
	lZz.document.open()
	lZz.document.write(mBz)
	lZz.document.close()
}

function lCz(mHz, lOz) {
	var lZz = window.frames["lZz"+mHz];
	if (lOz=="Text") {
		lZz.document.body.innerText = lZz.document.body.innerHTML
		lZz.document.body.style.fontFamily = "monospace"
		lZz.document.body.style.fontSize = "9pt"
		lOz="Text"
 	}
	else {
   		lZz.document.body.innerHTML = lZz.document.body.innerText
   		lZz.document.body.style.fontFamily = ""
   		lZz.document.body.style.fontSize =""
   		lOz="HTML"
 	}
	var s = lZz.document.body.createTextRange()
	s.collapse(false)
	s.select()
}

END_OF_FANCY_JS

return $str;

};

1;

package kGz;
sub LOCK_SH {1}; sub LOCK_EX {2}; sub LOCK_UN {8};

sub new {
    my ($type, $file, $mode) = @_;
    my $lf = $file."_lck";
    $mode = LOCK_EX if ((!$mode) || not -f $lf);
    my $lock_fh="LOCKFILE$file";
    $lock_fh =~ s#\W#_#g;
    if($mode == LOCK_EX) {
    	open ($lock_fh, ">>$lf") or hSz::error('sys', "Fail to open file $lf: $!");
    }else {
    	open ($lock_fh, "$lf") or hSz::error('sys', "Fail to open file $lf: $!");
    }
    eval {
         my $rem=0;
	 local $SIG{ALRM} = sub { die "lock_operation_timeout ($lf)" };
         $rem = eval 'alarm 20' if $hSz::use_alarm;
         flock ($lock_fh, $mode) or hSz::error('sys', "Fail to lock $lf: $!");
         eval "alarm $rem" if $abmain::use_alarm;
    };
    if ($@ =~ /operation_timeout/) { hSz::error('sys', "Lock operation timed out. Go back and retry.<!--$@-->");  }
    my $self = bless {}, $type;
    $self->{lock_fh} = $lock_fh;
    return $self;
    
}

sub DESTROY{
    my ($self) = @_;
    my $lock_fh=$self->{lock_fh};
    return if not $lock_fh;
    flock ($lock_fh, LOCK_UN);
    close $lock_fh;
}



1;

package jZz;

sub new {
    my ($type, $tb, $opts) = @_;
    my $self = bless {}, $type;
    $self->{tb} = $tb;
    $self->{index} = $opts->{index} || 0;
    $self->{alphaidx} = $opts->{alphaidx};
    $self->{cmp} = $self->{alphaidx}? undef: sub {return $_[0] <=> $_[1];} ;
    return $self;
}


#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__

sub jYz{
    my ($self, $rowref, $opts) =@_;
    return $self->kYz([$rowref], $opts);
}

sub kQz{
    my ($self, $nIz, $opts) =@_;
    return $self->kYz($nIz, $opts, 1);
}

sub kRz{
   my ($self, $rowref, $opts) =@_;
   return $self->kKz([$rowref], $opts);
}

sub kFz{
   my ($self, $rowrefs, $opts, $clear) =@_;
   my @ids;
   my $index = $self->{index} ;
   for(@$rowrefs) {
    		push @ids, $_->[$index];
   }
   return $self->kBz(\@ids, $opts, $clear);
}

sub kTz {
    my ($self, $id) = @_;
    my $nIz = $self->kIz(
                 {noerr=>1, 
                  filter=>
                     $self->{alphaidx}? sub { $_[0]->[$self->{index}] eq $id; }
                                      : sub { $_[0]->[$self->{index}] == $id; }
                 });
    return if not ($nIz && scalar(@$nIz));
    return $nIz->[0];
}

sub kIz{
    my ($self, $opts) =@_;
    return;
}

sub kYz{
   my ($self, $rowrefs, $opts, $clear) =@_;
}

sub kBz{
   my ($self, $ids, $opts, $clear) =@_;
}
 

sub kKz{
   my ($self, $rowrefs, $opts) =@_;
}


sub kVz{
}

1;

package kWz;
#IF_AUTO use jZz;
#IF_AUTO use kGz;

BEGIN{
	@kWz::ISA= qw(jZz);
};

sub LOCK_SH {1}; sub LOCK_EX {2}; sub LOCK_UN {8};

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__


sub kVz{
	my ($self) = @_;
        my $f = $self->{tb};
        my $cnt =0; 
	my $buf;
        my $lck = kGz->new($self->{tb}, kGz::LOCK_SH);
        local *F;
	open F, "<$f";
        while(sysread F, $buf, 4096*4) { $cnt += ($buf =~ tr/\n//);}
        close F;
	my $hsh = kWz::get_deleted_ids($f."_del");
        my $dcnt =0;
	if($hsh) {
		$dcnt = scalar(keys %$hsh);
	}
	return wantarray?($cnt-$dcnt, $dcnt): $cnt-$dcnt;
}

sub kKz{
   my ($self, $rowrefs, $opts) =@_;
   my $lck = kGz->new($self->{tb}, kGz::LOCK_EX());
   return kMz($self->{tb}."_upd", $rowrefs, $opts);
}

sub kIz{
   my ($self, $opts) =@_;
   my $dbfile = $self->{tb};
   my $lck = kGz->new($self->{tb}, kGz::LOCK_SH);
   $opts->{index} = $self->{index};
   return kWz::kOz($dbfile, $opts);
} 

sub kYz{
   my ($self, $rowrefs, $opts, $clear) =@_;
   my $lck = kGz->new($self->{tb}, kGz::LOCK_EX());
   $self->compact_txt_db();
   return kWz::kMz($self->{tb}, $rowrefs, $opts, $clear);
}
 
sub kMz{
   my ($dbfile, $rowrefs, $opts, $clear) =@_;
   local *TBF;
   my $res;
   if($clear) {
	$res = open TBF, ">$dbfile";
   	unlink $dbfile."_upd";       
   	unlink $dbfile."_del";       
   }else {
	$res = open TBF, ">>$dbfile";
   }
   if(not $res) {
		unless($opts && $opts->{noerr}) {
			hSz::error("sys", $opts->{emsg}. "($!: $dbfile)");
	        }
		return;
   }
   for(@$rowrefs) {
	next if not ref($_) eq 'ARRAY';
	for my $str (@$_) {
		next if not $str;
		$str =~ tr/\t/ /;
		$str =~ tr/\r?\n/ /;
	}
    	print TBF join("\t", @$_), "\n";
   }
   close TBF;
   1;
}
  

sub kOz{
    my ($dbfile, $opts, $no_upd) =@_;
    local *TBF;
    my %upd_hash=();
    my $index = $opts->{index} ||0;
    my $dhash=undef;
    if(not $no_upd) {
	my $nIz= kWz::kOz($opts->{modfile} || "${dbfile}_upd", {index=>$index, noerr=>1}, 1);
	$dhash = kWz::get_deleted_ids(${dbfile}."_del");
        for(@$nIz) {
		$upd_hash{$_->[$index]} = $_;
        }
    }
        
    if(not open TBF, "<$dbfile") {
	unless($opts && $opts->{noerr} ) {
			print caller, "\n";
			hSz::error("sys", $opts->{emsg}. "($!: $dbfile)");
        }
	return;
    }
    my $rows=[];
    my $filter = $opts->{filter};
    my $row;
    my $cnt=0;
    my $filtcnt=0;
    my $max = $opts->{maxret}||0;
    my $sidx = $opts->{sidx};
    my $eidx = $opts->{eidx};
    my $eQ=0;
    my ( @aCz);
    my $wantstr = $opts->{getstr};
    local $_;
    while(<TBF>){
        $_ =~ s/\r*\n$//;
	next if not $_;
	$row = [split /\t/, $_];
        next if($dhash && $dhash->{$row->[$index]});
        $eQ ++;
	next if ($sidx && $eQ <$sidx+1);
	last if ($eidx && $eQ >$eidx);
        if((not $no_upd) && exists $upd_hash{$row->[$index]}) {
		$row = $upd_hash{$row->[$index]};
        }

	if ($filter && not &$filter($row, $eQ)) {
             $filtcnt ++;
	     next;
        }
        if($wantstr) {
		push @$rows, $_;
        }else {
		push @$rows, $row;
        }
	$cnt ++;
        last if $max >0 && $cnt > $max;
    }
    close TBF;
    return wantarray? ($rows, $cnt, $filtcnt) : $rows;
}

sub mark_deleted_ids{
   my ($delf, $ids, $opts) =@_;
   return if not @$ids;
   local *TBF;
   open TBF, ">>$delf" or hSz::error("sys", $opts->{emsg}. "($!: $delf)");
   print TBF join ("\n", @$ids), "\n";
   close TBF;
}

sub get_deleted_ids{
   my ($delf, $ids, $opts) =@_;
   local *TBF;
   open TBF, "<$delf" or return;
   local $/=undef;
   my $l = <TBF>;
   $l =~ s/\s+$//g;
   my @ids = split /\r?\n/, $l;
   my $idhsh = {};
   for(@ids) {
	$idhsh->{$_} =1 if $_ ne "";
   }
   close TBF;
   return $idhsh; 
}

sub kBz{
   my ($self, $ids, $opts, $clear) =@_;
   my $lck = kGz->new($self->{tb}, kGz::LOCK_EX);

   my $dbfile = $self->{tb};

   if($clear) {
	unlink $dbfile;
   	unlink $dbfile."_upd";
	return;
   }
   my $delf = $dbfile."_del";
   kWz::mark_deleted_ids($delf, $ids);
   my $dhash = kWz::get_deleted_ids($delf);

   if($dhash && scalar(keys %$dhash) > 3) {
	$self->compact_txt_db($opts);
   }
   return scalar(@$ids);
   
}

sub compact_txt_db{
   my ($self, $opts) =@_;
   local *TBF;
   my %upd_hash=();
   my $index = $self->{index};
   my $dbfile = $self->{tb};


   my $nIz= kWz::kOz($opts->{modfile} ||"${dbfile}_upd", {index=>$index, noerr=>1}, 1);
   for(@$nIz) {
		$upd_hash{$_->[$index]} = $_;
   }
   my $del_hash = kWz::get_deleted_ids("${dbfile}_del");
   return if (scalar(keys %upd_hash) ==0  && scalar(keys %$del_hash) ==0 );

   if(not open TBF, "<$dbfile") {
	return;
   }
   my $row;
   my $cnt=0;
   my $filtcnt=0;
   my $filter = $opts->{filter};
   my $eQ=0;


   open TBF2, ">$dbfile.tmp";
   while(<TBF>){
        $_ =~ s/\r*\n$//;
	next if not $_;
        $eQ ++;
	$row = [split /\t/, $_];
        if(exists $upd_hash{$row->[$index]}) {
		$row = $upd_hash{$row->[$index]};
        }
        if($del_hash->{$row->[$index]}) {
	      $filtcnt ++;
	      next;
        }
	if ($filter && &$filter($row, $eQ)) {
             $filtcnt ++;
	     next;
        }
        print TBF2 join("\t", @$row), "\n";
	$cnt ++;
   }
   close TBF;
   close TBF2;
   
   open TBF2, ">$dbfile";
   open TBF, "<$dbfile.tmp";
   binmode TBF2;
   my $buf;
   while(sysread TBF, $buf, 4096*4) { syswrite (TBF2, $buf, length($buf), 0); }
   close TBF;
   close TBF2;
   unlink $dbfile."_upd";       
   unlink $dbfile."_del";       
   unlink "$dbfile.tmp";       
   return $filtcnt;
}
1;


1;


package CSVText;


################################################################################
################################################################################

require 5.002;

use strict;

BEGIN {
  use Exporter   ();
  use AutoLoader qw(AUTOLOAD);
  use vars       qw($VERSION @ISA @EXPORT @EXPORT_OK %EXPORT_TAGS);
  $VERSION =     '0.01';
  @ISA =         qw(Exporter AutoLoader);
  @EXPORT =      qw();
  @EXPORT_OK =   qw();
  %EXPORT_TAGS = qw();
}

1;

#IF_AUTO use AutoLoader 'AUTOLOAD';
#IF_AUTO 1;
#IF_AUTO __END__


################################################################################
################################################################################
sub version {
  return $VERSION;
}

################################################################################
################################################################################
sub new {
  my $proto = shift;
  my $class = ref($proto) || $proto;
  my $self = {};
  $self->{'_STATUS'} = undef;
  $self->{'_ERROR_INPUT'} = undef;
  $self->{'_STRING'} = undef;
  $self->{'_FIELDS'} = undef;
  bless $self, $class;
  return $self;
}

sub status {
  my $self = shift;
  return $self->{'_STATUS'};
}

sub error_input {
  my $self = shift;
  return $self->{'_ERROR_INPUT'};
}

sub string {
  my $self = shift;
  return $self->{'_STRING'};
}

sub fields {
  my $self = shift;
  if (ref($self->{'_FIELDS'})) {
    return @{$self->{'_FIELDS'}};
  }
  return undef;
}

sub combine {
  my $self = shift;
  my @part = @_;
  $self->{'_FIELDS'} = \@part;
  $self->{'_ERROR_INPUT'} = undef;
  $self->{'_STATUS'} = 0;
  $self->{'_STRING'} = '';
  my $column = '';
  my $combination = '';
  my $skip_comma = 1;
  if ($#part >= 0) {

   
    for $column (@part) {
      if ($column =~ /[^\t\040-\176]/) {


	$self->{'_ERROR_INPUT'} = $column;
	return $self->{'_STATUS'};
      }
      if ($skip_comma) {


	$skip_comma = 0;
      } else {


	$combination .= ',';
      }
      $column =~ s/\042/\042\042/go;
      $combination .= "\042";
      $combination .= $column;
      $combination .= "\042";
    }
    $self->{'_STRING'} = $combination;
    $self->{'_STATUS'} = 1;
  }
  return $self->{'_STATUS'};
}

sub parse {
  my $self = shift;
  $self->{'_STRING'} = shift;
  $self->{'_FIELDS'} = undef;
  $self->{'_ERROR_INPUT'} = $self->{'_STRING'};
  $self->{'_STATUS'} = 0;
  if (!defined($self->{'_STRING'})) {
    return $self->{'_STATUS'};
  }
  my $keep_biting = 1;
  my $palatable = 0;
  my $line = $self->{'_STRING'};
  if ($line =~ /\n$/) {
    chop($line);
    if ($line =~ /\r$/) {
      chop($line);
    }
  }
  my $mouthful = '';
  my @part = ();
  while ($keep_biting and ($palatable = $self->_bite(\$line, \$mouthful, \$keep_biting))) {
    push(@part, $mouthful);
  }
  if ($palatable) {
    $self->{'_ERROR_INPUT'} = undef;
    $self->{'_FIELDS'} = \@part;
  }
  return $self->{'_STATUS'} = $palatable;
}

sub _bite {
  my ($self, $line_ref, $piece_ref, $bite_again_ref) = @_;
  my $in_quotes = 0;
  my $ok = 0;
  $$piece_ref = '';
  $$bite_again_ref = 0;
  while (1) {
    if (length($$line_ref) < 1) {

     
      if ($in_quotes) {


	last;
      } else {


	$ok = 1;
	last;
      }
    } elsif ($$line_ref =~ /^\042/) {

     
      if ($in_quotes) {
	if (length($$line_ref) == 1) {

	 
	  substr($$line_ref, 0, 1) = '';
	  $ok = 1;
	  last;
	} elsif ($$line_ref =~ /^\042\042/) {

	 
	  $$piece_ref .= "\042";
	  substr($$line_ref, 0, 2) = '';
	} elsif ($$line_ref =~ /^\042,/) {

	 
	  substr($$line_ref, 0, 2) = '';
	  $$bite_again_ref = 1;
	  $ok = 1;
	  last;
	} else {

	 
	  last;
	}
      } else {
	if (length($$piece_ref) < 1) {

	 
	  $in_quotes = 1;
	  substr($$line_ref, 0, 1) = '';
	} else {

	 
	  last;
	}
      }
    } elsif ($$line_ref =~ /^,/) {

     
      if ($in_quotes) {


	$$piece_ref .= substr($$line_ref, 0 ,1);
	substr($$line_ref, 0, 1) = '';
      } else {


	substr($$line_ref, 0, 1) = '';
	$$bite_again_ref = 1;
	$ok = 1;
	last;
      }
    } elsif ($$line_ref =~ /^[\t\040-\176]/) {

     
      $$piece_ref .= substr($$line_ref, 0 ,1);
      substr($$line_ref, 0, 1) = '';
    } else {

     
      last;
    }
  }
  return $ok;
}
1;

__END__

package LocalPOP3Client;


#******************************************************************************
#* Other packages, globals, etc.
#******************************************************************************

use Carp;

sub new
{
	my $name = shift;
	my ($dir, $box) = @_;

    my $me = bless {
	dir=>$dir
	}, $name;

	$me;

}

sub cK
{
	my $me = shift;
	my $num = shift;
	my $header = '';
	my $s = $me->{SOCK};
	my $mail = {};;

	$me->Debug() and print "TOP $num 0\n";
	print $s "TOP $num 0", $me->dU;
	$_ = <$s>;
	$me->Debug() and print;
	chop;
	/^\+OK/ or $me->fEz("Bad return from TOP: $_") and return '';
	/^\+OK (\d+) / and $mail->{size} = $1;
	
        my $lkey ="";
	do {
		$_ = <$s>;
                defined($_) or $me->fEz("Connection to POP server lost") and return;
		/^([^:]+):\s+(.*)$/ and $mail->{ucfirst(lc($1))}=$2 and $lkey=ucfirst(lc($1));
		/^\s+(\S+)/ and $lkey and $mail->{$lkey} .=$_;
		$mail->{header} .= $_;
	} until /^\.\s*$/;

        for(keys %$mail) {
		$mail->{$_} = aVz::dCz($mail->{$_});
        }
	return $mail;
} 

sub aT{
	my ($me, $num) = @_;
	my %mail=();
        $mail{aCz} = [];
	$me->Debug() and print "RET $num\n";

        my $s = $me->{SOCK} if not $s;
	print $s "RETR $num", $me->dU;
	$_ = <$s>;
	$me->Debug() and print;
	chop;
	/^\+OK/ or $me->fEz("Bad return from RETR: $_") and return 0;
	/^\+OK (\d+) / and $mail{bytelen} = $1;

        my $lkey ="";
	do {
		$_ = <$s>;
                defined($_) or $me->fEz("Connection to POP server lost") and return;
		/^([^:]+):\s+(.*)$/ and $mail{ucfirst(lc($1))}=$2 and $lkey=ucfirst(lc($1));
		/^\s+(\S+)/ and $lkey and $mail{$lkey} .=$_;
		$mail{header} .= $_;
                push @{$mail{aCz}}, $_;
                $mail{size} += length($_);
	} until /^\s*$/;

        for(keys %mail) {
		$mail{$_} = aVz::dCz($mail{$_});
        }

        my @barr;
	do {
		$_ = <$s>;
                defined($_) or $me->fEz("Connection to POP server lost") and return;
		unless(/^\.\s*$/) {
                	push @{$mail{aCz}}, $_;
                }
	} until /^\.\s*$/;

	return %mail;
   
} 

sub List {
    my $me = shift;
	my $num = shift || '';

	my $s = $me->Socket;
	$me->eJ() or return;

	my @retarray = ();

	$me->Debug() and carp "POP3: List $num";
	$num = " $num" if $num ne "";
	print $s "LIST$num", $me->dU;
	$_ = <$s>;
	/^\+OK/ or $me->fEz("$_") and return;
	if ($num) {
		$_ =~ s/^\+OK\s*//;
		return $_;
	}
	while(<$s>) {
		/^\.\s*$/ and last;
		/^0\s+messag/ and last;
		chop;
		push(@retarray, $_);
	}
	return @retarray;
}

sub kAz{
    my $me = shift;
	my $num = shift || '';

	my $s = $me->Socket;
	$me->eJ() or return;

	local @retarray = ();

	$me->Debug() and carp "POP3: UIDL $num";
	my $num2 ="";
        $num2 = " $num" if $num ne "";
	print $s "UIDL$num2", $me->dU;
	$_ = <$s>;
	/^\+OK/ or $me->fEz("$_") and return;
	if ($num) {
		$_ =~ s/^\+OK\s*\d+\s+//;
		$_ =~ s/\s*$//;
		return {$num=>$_};
	}
        my $nGz= {};
	while(<$s>) {
		/^\.\s*$/ and last;
		/^0\s+messag/ and last;
		$_ =~ s/\s*$//;
		my ($cA, $uid) = split /\s+/, $_;
		if($cA) {
			$nGz->{$cA} = $uid;
		}
	}
	return $nGz;
}

sub cVz {
    my $me = shift;
	my $num = shift || return;

	my $s = $me->Socket;
	print $s "DELE $num",  $me->dU;
	$_ = <$s>;
	$me->fEz($_);
	/^\+OK / && return 1;
	return 0;
}
1;