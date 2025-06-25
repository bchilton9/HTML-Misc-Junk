#!/usr/bin/perl
#
# CalendarScript
# Version: 3.2
#
# Copyright 2001,2002 Matt Kruse
# http://www.CalendarScript.com/
#

BEGIN {
	# CHANGE THE LINE BELOW IF NECESSARY
	# Be sure to remove the # before $BASE_DIR, and change the path between the quotes
	#$BASE_DIR = "/...change.to.full.file.path.of.dir.../calendarscript/";
	
	# DO NOT CHANGE ANYTHING BELOW HERE!
	
	if ($BASE_DIR ne "") { $BASE_DIR =~ s|([^/])$|$1/|; }
	else {
		my ($path) =  $ENV{'PATH_TRANSLATED'} || $ENV{'SCRIPT_FILENAME'};
		unless ($path) {
			print "Content-type:text/html\n\n<B>ERROR:</B><BR>Your server does not provide the PATH_TRANSLATED or SCRIPT_FILENAME environment variables.<br><br>Please see the installation documentation for how to set the \$BASE_DIR variable manually.";
			exit(0);
			}
		$path =~ s|[^/\\]*$||;
		$path =~ s|([^/])$|$1/|;
		$BASE_DIR = $path . "calendarscript/";
		}
	unshift(@INC,$BASE_DIR."lib");
	require "asp.inc";
	require "DBFile.pm";
	require "DBFileUtil.inc";
	require "TimeLocal.inc";
	require "Date.inc";
	require "ConfigFile.pm";
	require "Event.inc";
	require "HTML.pm";
	require "CGISession.inc";
	require "User.pm";
	require "SimpleDateFormat.pm";
	require "calendars.inc";
	}
	
sub ERROR {
	my($msg,$severity) = @_;
	&addUserMessage($msg);
	&showScreen();
	}
sub FATALERROR {
	my ($msg) = @_;
	&addErrorMessage($msg);
	if ($in{template} eq "error.html") { print "FATAL ERROR: COULD NOT LOAD error.html"; exit(0); }
	$in{template} = "error.html";
	&showScreen();
	}
	
# Load the required template and execute it
# -----------------------------------------
sub showScreen {
	&populateTemplateVariables();
	$template_dir = $BASE_DIR . "templates/calendars/" . $Config->get("template_dir") . "/";
	$template_file = $template_dir . $in{'template'};
	$template = &ASPLoadTemplate($template_file);
	&ASPEval($template,$template_dir);
	&ASPError($tmp_parsed_template) if $@;
	exit(0);
	}
sub showSameScreen() {
	&populateTemplateVariables();
	$in{'template'} = $in{'fromTemplate'} || "error.html";
	&showScreen();
	}

# Handle error messages
# ---------------------
sub addUserMessage {
	my($msg) = shift;
	if ($msg ne "") {
		$Template::userMessage .= $msg . "<BR>";
		}
	}
sub addErrorMessage {
	my($msg) = shift;
	if ($msg ne "") {
		$Template::errorMessage .= $msg . "<BR>";
		}
	}

# Get message text to support language translation
# ------------------------------------------------
sub getMessage() {
	my ($name,$p1,$p2,$p3,$p4) = @_;
	# Only read in the file if there is a message to be retrieved
	unless ($MESSAGES) {
		$msgfile = $BASE_DIR . "templates/admin/$admin_template_dir/messages.txt";
		open(MESSAGES,$msgfile) || &FATALERROR("Error opening messages file [$msgfile]: $!");
		while(<MESSAGES>) {
			next if /^#/;
			next unless /\S/;
			chomp;
			my($name,$value) = split(/=/,$_,2);
			$MESSAGES->{$name} = $value;
			}
		close(MESSAGES);
		}
	my ($message) = $MESSAGES->{$name};
	if ($message eq "") { return "MESSAGE TEXT MISSING FOR: $name"; }
	if ($p1) { $message =~ s/\%s/$p1/; }
	if ($p2) { $message =~ s/\%s/$p2/; }
	if ($p3) { $message =~ s/\%s/$p3/; }
	if ($p4) { $message =~ s/\%s/$p4/; }
	return $message;
	}

# Get a list of plugin files
# --------------------------
sub getPluginFileList {
	my ($file,$plugin);
	my ($pluginfiles,$pluginsfilesfile);
	$pluginsfilesfile = $plugins_dir."plugin_files.txt";
	if (-e $pluginsfilesfile) {
		open(PLUGINFILES,$pluginsfilesfile) || &FATALERROR(&getMessage("ERROR_OPENING_PLUGIN_FILES_LIST",$!));
		while (<PLUGINFILES>) {
			next if /^\s*(#|$)/;
			chomp;
			($file,$plugin) = split(/\t/);
			unless (exists $pluginfiles->{$file}) {
				$pluginfiles->{$file} = "plugins/$plugin/$file";
				}
			}
		close(PLUGINFILES);
		}
	return $pluginfiles;
	}

# Handle custom-defined functionality
# -----------------------------------
sub handleCustomFunction() {
	my ($funcName,@args) = @_;
	my ($result) = 0;
	my ($filename) = $funcName . ".pl";
	if ($PluginFiles->{$filename}) {
		$filename = $BASE_DIR . $PluginFiles->{$filename};
		eval("require \"$filename\";");
		if ($@) {
			# Error including file - return error msg and continue running normal functions
			&addUserMessage(&getMessage("ERROR_REQUIRING_CUSTOM_FUNCTION",$filename,$@));
			return 0;
			}
		# Try to call custom function
		eval("\$result = \&${funcName}(\@args);");
		if ($@) {
			# Error calling function - return error msg and continue running normal functions
			&addUserMessage(&getMessage("ERROR_RUNNING_CUSTOM_FUNCTION",$funcName,$@));
			return 0;
			}
		# Custom function was executed. Return whatever it returned.
		return $result;
		}
	return 0;
	}

# Get a Template Preference value, either from the config file or the default
# ---------------------------------------------------------------------------
sub getTemplatePreference {
	my ($name) = @_;
	my ($key) = "template_preference_".$Config->get("template_dir")."_".$name;
	if ($Config->contains($key)) { 
		return $Config->get($key);
		}
	return $main::TemplateDefaults->{$name};
	}
	
sub LZ { my($x)=shift;if(length($x)==1){return "0$x";}return $x; }

sub URLEncode {
	my($url)=@_;
	my(@characters)=split(/(\%[0-9a-fA-F]{2})/,$url);
	foreach(@characters) {
		if ( /\%[0-9a-fA-F]{2}/ ) {
			unless ( /(20|7f|[0189a-fA-F][0-9a-fA-F])/i || /2[2356fF]|3[a-fA-F]|40/i ) {
				s/\%([2-7][0-9a-fA-F])/sprintf "%c",hex($1)/e;
				}
			}
		else {
			s/([\000-\040\177-\377\074\076\042])/sprintf "%%%02x",unpack("C",$1)/egx;
			}
		}
	return join("",@characters);
	}

# Get input Data
# --------------
sub getInput {
	my ($in,@in,$key,$val);
	my (@keys,%formvars);
	if ($ENV{'REQUEST_METHOD'}) {
		if ($ENV{'REQUEST_METHOD'} eq "GET") { $in = $ENV{'QUERY_STRING'}; }
		elsif ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN,$in,$ENV{'CONTENT_LENGTH'}); }
		@in = split(/&/,$in);
		# First get all the raw form vars
		foreach $i (0 .. $#in) {
			$in[$i] =~ s/\+/ /g;    ($key, $val) = split(/=/,$in[$i],2);
			$key =~ s/%(..)/pack("c",hex($1))/ge;
			$val =~ s/%(..)/pack("c",hex($1))/ge;
			# Keep a record of their order, because later values take precendent
			push(@keys,$key);
			$formvars{$key} = $val;
			}
		# Process the special QUERY_STRING field, if it exists
		# These values come first and then might be over-written
		if ($formvars{'QUERY_STRING'}) {
			@in = split(/&/,$formvars{'QUERY_STRING'});
			foreach $i (0 .. $#in) {
				$in[$i] =~ s/\+/ /g;    ($key, $val) = split(/=/,$in[$i],2);
				if ($val ne "") {
					$in{$key} = $val;
					if ($in{'datestring'} && (($key eq 'year') || ($key eq 'month') || ($key eq 'date'))) {
						delete $in{'datestring'};
						}
					if ($key eq "datestring") {
						delete $in{'year'};
						delete $in{'month'};
						delete $in{'date'};
						}
					}
				}
			delete $formvars{'QUERY_STRING'};
			}
		# Process all the new field values, over-writing the old ones
		foreach $key (@keys) {
			next if ($key eq "QUERY_STRING");
			$in{$key} = $formvars{$key};
			if ($in{'datestring'} && (($key eq 'year') || ($key eq 'month') || ($key eq 'date'))) {
				delete $in{'datestring'};
				}
			if ($key eq "datestring") {
				delete $in{'year'};
				delete $in{'month'};
				delete $in{'date'};
				}
			}
		# Form the query string from form input
		foreach $key (keys %in) {
			if (($key eq "command") || ($key eq "username") || ($key eq "password") || ($key =~/^FIELD_/)) {
				delete $formvars{$key};
				next;
				}
			if ($QUERY_STRING ne "") { $QUERY_STRING .= "&"; }
			$QUERY_STRING .= &URLEncode($key) . "=" . &URLEncode($in{$key});
			}
		$FORM_QUERY = join('&', map {"$_=$formvars{$_}"} keys %formvars);
		}
	elsif ($ENV{'DOCUMENT_URI'}) {
		open(SSI,$BASE_DIR."ssi.txt");
		while(<SSI>) {
			chomp;
			($key,$val) = ( /^\s*([^=]+)\s*=\s*"?(.*?)"?$/o );
			$key =~ s|\s*$||;
			$val =~ s|\s*$||;
			next unless ($key);
			$in{$key} = $val;
			}
		close(SSI);
		$no_session = 1;
		}
	elsif ($#ARGV >= 0) {
		while ($in = shift(@ARGV)) {
			($key,$val) = split(/=/,$in);
			$in{$key} = $val;
			}
		$no_session = 1;
		$no_header=1;
		}
	}

#################################
# Here is all the dirty work... #
#################################
$|=1;

# Read the main admin config file
$admin_config    = $BASE_DIR . "config.txt";
$AdminConfig = new ConfigFile($admin_config);
$Template::AdminConfig = $AdminConfig;
$admin_template_dir = $AdminConfig->get("admin_template_dir") || "English";
$plugins_dir     = $BASE_DIR . "plugins/";

$PluginFiles = &getPluginFileList();

# Get input
unless(&handleCustomFunction("display_before_getInput")) {
	&getInput();
	}
&handleCustomFunction("display_after_getInput");

# Start output
# ------------
if (($ENV{'HTTP_COOKIE'} =~ /CGISessionID/) || ($in{'command'} eq "login")) {
	$Session = new CGISession($BASE_DIR . "session/");
	unless ($no_session) {
		my ($id) = ($ENV{'HTTP_COOKIE'} =~ /CGISessionID\s*=\s*([^;]*)/);
		$Session->getSession($id);
		if (($Session->isValid()) && ($in{'command'} ne "logout")) { 
			print "Set-cookie: CGISessionID=",$Session->getValue("_id"),";path=/\n"; 
			}
		else { print "Set-cookie: CGISessionID=;path=/;expires=Thu, 01-Jan-1970 00:00:00 GMT\n"; }
		}
	# Make session available in template files
	$Template::Session = $Session;
	}
unless ($no_header) {
	print "Content-type: text/html\n\n";
	}

$in{'calendar'} ||= $AdminConfig->get("default_calendar");
$in{'calendar'} =~ s|[^\w\d\._]||g;
$calendar = $in{'calendar'};
$in{'template'} ||= "default.html";
$in{'template'} =~ s|[^\w\d\._]||g;

$db_dir          = $BASE_DIR . "calendars/" . $in{'calendar'} . "/";
$config_file     = $db_dir . "config.txt";
$schedule_db     = $db_dir . "schedule";
$events_db       = $db_dir . "events";
$calendars_db    = $BASE_DIR . "calendars";
$users_db        = $BASE_DIR . "users";
$permissions_db  = $BASE_DIR . "permissions";

# Read the config file for the calendar
$Config = new ConfigFile($config_file);
$Template::Config = $Config;

# Get calendar name, description
$Calendar = &getCalendarInfo($calendar);

# Get display options for the template set to be used
$TemplateFields = &GetFieldProperties($BASE_DIR."templates/calendars/".$Config->get("template_dir")."/preferences.txt");
foreach $field (@$TemplateFields) {
	$TemplateDefaults->{$field->{'field_name'}} = $field->{'defaultvalue'};
	}

# The CGI URL for call-back
$Template::CGI_URL = $AdminConfig->get("calendar_url") || $ENV{'SCRIPT_NAME'} || $ENV{'REQUEST_URI'};
$Template::CGI_URL_QUERYSTRING = $Template::CGI_URL . "?".$QUERY_STRING;
if ($QUERY_STRING ne "") { $Template::CGI_URL_QUERYSTRING .= "&"; }
$Template::QUERY_STRING = $QUERY_STRING;
$Template::CGI_HIDDEN_FIELDS .= "<INPUT TYPE=\"hidden\" NAME=\"QUERY_STRING\" VALUE=\"$FORM_QUERY\">";
$Template::ADMIN_CGI_URL = $AdminConfig->get("calendar_admin_url");

# Attempt to Login?
# -----------------
if ($in{'command'} eq "login") {
	unless(&handleCustomFunction("display_before_login")) {
		$User = new User($in{username}, $users_db, $permissions_db);
		my ($result) = $User->login($in{password});
		if ($result == 1) {
			# User logged in
			$Session->{'username'} = $User->{'username'};
			$Session->{'name'} = $User->{'name'};
			$Session->{'calendar'} = $calendar;
			&addUserMessage(($User->{'name'} || $User->{'username'}) . $User::MSG_LOGGED_IN_SUCCESSFULLY);
			}
		elsif ($result == 2) {
			undef $Session;
			&addUserMessage(&getMessage("CALENDAR_PASSWORD_MUST_BE_CHANGED"));
			&showSameScreen();
			}
		else {
			&addUserMessage($User->getErrorMessage());
			&showSameScreen();
			}
		}
	&handleCustomFunction("display_after_login");
	}

# Handle Logout
# -------------
if ($in{'command'} eq "logout") {
	unless(&handleCustomFunction("display_before_logout")) {
		$Session->ExpireNow();
		$Session->cleanupExpiredSessions();
		undef $Session;
		undef $Template::Session;
		undef $User;
		}
	&handleCustomFunction("display_after_logout");
	}	

# Create a global "User" object if it doesn't already exist
# ---------------------------------------------------------
unless(&handleCustomFunction("display_before_create_user")) {
	unless ($User) {
		if ($Session && ($Session->{'username'} ne "")) {
			$User = new User($Session->{'username'}, $users_db, $permissions_db);
			$User->{'logged_in'} = 1;
			$Session->{'calendar'} = $calendar;
			}
		else {
			$User = new User('anonymous', $users_db, $permissions_db);
			$User->{'logged_in'} = 0;
			}
		}
	$Template::User = $User;
	}
&handleCustomFunction("display_after_create_user");

# Require Login?
# --------------
if ($Config->get("require_login")) {
	unless(&handleCustomFunction("display_before_require_login")) {
		if ($Session->{'username'}) {
			unless ($User->hasPermission($calendar,"VIEW")) {
				$Template::userMessage = &getMessage("CALENDAR_NO_VIEW_PERMISSION");
				&FATALERROR("");
				}
			}
		else {
			$in{'template'} = "login.html";
			&showScreen();
			}
		}
	}
&handleCustomFunction("display_after_require_login");

# Create the event and schedule database objects
$DBEvents = new DBFile($events_db);
$DBSchedule = new DBFile($schedule_db);

# Handle any commands here
# ------------------------

# SEARCH
# ------
if ($in{'command'} eq "search") {
	unless(&handleCustomFunction("display_before_search")) {
		my ($properties,$name,$field);
		foreach $name (keys %in) {
			$field = $name;
			if (($in{$name} ne "") && ($field =~ s/^FIELD_//)) {
				$properties->{$field} = $in{$name};
				}
			}
		if (scalar keys %$properties <= 0) {
			&addUserMessage("Search query must not be blank!");
			}
		else {
			$start = Time::Local::timegm(0,0,0,$in{start_date},$in{start_month}-1,$in{start_year});
			$end   = Time::Local::timegm(0,0,0,$in{end_date},$in{end_month}-1,$in{end_year});
			$Template::SEARCH_RESULTS = &Event::search($DBEvents, $DBSchedule, "", $properties, $start, $end);
			}
		}
	&handleCustomFunction("display_after_search");
	}

# Load the required template and execute it
# -----------------------------------------
&showScreen();

END {	
	if (defined $main::Session && ref($main::Session) eq "CGISession") {
		$main::Session->saveSession();
		}
	}

##################################################
# Populate variables and references for templates
##################################################
sub populateTemplateVariables {
	$localtime_offset = 3600*$Config->get("time_zone_offset");
	($now_ss,$now_mi,$now_hh,$now_dd,$now_mm,$now_yy,$now_wd,$now_yd,$now_dst) = localtime(time+$localtime_offset);
	$now_mm++;
	$now_yy += 1900;

	# Get the displayed dates, etc
	$year = substr($in{'datestring'},0,4) || $in{'year'} || substr($in{'selected_datestring'},0,4) || $now_yy;
	$month = substr($in{'datestring'},4,2) || $in{'month'} || substr($in{'selected_datestring'},4,2) || $now_mm;
	$date = substr($in{'datestring'},6,2) || $in{'date'} || substr($in{'selected_datestring'},6,2) || $now_dd;

	# Get selected date
	$selected_datestring = $in{'selected_datestring'} || $year.&LZ($now_mm).&LZ($now_dd);

	# Date-related fields and HTML elements
	$Template::YEAR_SELECT = "<SELECT NAME=\"year\">" . &HTML::yearOptions($year) ."</SELECT>";
	$Template::MONTH_SELECT = "<SELECT NAME=\"month\">" . &HTML::monthNameOptions($month) . "</SELECT>";
	$Template::MONTH_ABBREVIATION_SELECT = "<SELECT NAME=\"month\">" . &HTML::monthAbbreviationOptions($month) . "</SELECT>";
	$Template::DAY_NAMES = $Config->get("day_names");
	$Template::DAY_ABBREVIATIONS = $Config->get("day_abbreviations");
	$Template::MONTH_NAMES = $Config->get("month_names");
	$Template::MONTH_ABBREVIATIONS = $Config->get("month_abbreviations");
	for ($i=0; $i<7; $i++) { ${"Template::DAY_NAME_".$i} = $Template::DAY_NAMES->[$i]; }
	for ($i=0; $i<12; $i++) { ${"Template::MONTH_NAME_".$i} = $Template::MONTH_NAMES->[$i]; }
	for ($i=0; $i<7; $i++) { ${"Template::DAY_ABBREVIATION_".$i} = $Template::DAY_ABBREVIATIONS->[$i]; }
	for ($i=0; $i<12; $i++) { ${"Template::MONTH_ABBREVIATION_".$i} = $Template::MONTH_ABBREVIATIONS->[$i]; }
	$Template::MONTH_NAME = $Template::MONTH_NAMES->[$month-1];
	$Template::YEAR = $year;
	$Template::MONTH = $month;
	$Template::DATE = $date;
	$Template::DATESTRING = $year . &LZ($month) . &LZ($date);
	$Template::NEXT_YEAR = $year+1;
	$Template::LAST_YEAR = $year-1;
	($Template::NEXT_MONTH_YEAR,$Template::NEXT_MONTH) = &Date::getNextMonthYear($year,$month);
	$Template::NEXT_MONTH_NAME = $Template::MONTH_NAMES->[$Template::NEXT_MONTH-1];
	($Template::LAST_MONTH_YEAR,$Template::LAST_MONTH) = &Date::getLastMonthYear($year,$month);
	$Template::LAST_MONTH_NAME = $Template::MONTH_NAMES->[$Template::LAST_MONTH-1];
	($Template::LAST_WEEK_YEAR,$Template::LAST_WEEK_MONTH,$Template::LAST_WEEK_DATE) = &Date::getLastWeek($year,$month,$date);
	($Template::NEXT_WEEK_YEAR,$Template::NEXT_WEEK_MONTH,$Template::NEXT_WEEK_DATE) = &Date::getNextWeek($year,$month,$date);
	($Template::NEXT_DAY_YEAR,$Template::NEXT_DAY_MONTH,$Template::NEXT_DAY_DATE) = &Date::getTomorrow($year,$month,$date);
	$Template::NEXT_DAY_DATESTRING = $Template::NEXT_DAY_YEAR . &LZ($Template::NEXT_DAY_MONTH) . &LZ($Template::NEXT_DAY_DATE);
	($Template::PREVIOUS_DAY_YEAR,$Template::PREVIOUS_DAY_MONTH,$Template::PREVIOUS_DAY_DATE) = &Date::getYesterday($year,$month,$date);
	$Template::PREVIOUS_DAY_DATESTRING = $Template::PREVIOUS_DAY_YEAR . &LZ($Template::PREVIOUS_DAY_MONTH) . &LZ($Template::PREVIOUS_DAY_DATE);
	($Template::TODAY_YEAR,$Template::TODAY_MONTH,$Template::TODAY_DATE) = ($now_yy,$now_mm,$now_dd);
	$Template::TODAY_DATESTRING = $Template::TODAY_YEAR . &LZ($Template::TODAY_MONTH) . &LZ($Template::TODAY_DATE);

	# Other
	$Template::CALENDAR = $Calendar;
	$Template::CALENDAR_KEY = $Calendar->{'key'};

	# Call-back method to get events
	*Template::getEvents = \&getEvents;
	*Template::getEvent = \&getEvent;

	# Method to get template preferences
	*Template::getPreference = \&getTemplatePreference;

	# Form input
	%Template::in = %in;

	# Looping and conditional special tags
	&ASPCustomTag('\s*FOREACH\s*GRID\s*ROW\s*','foreach $ROW (0 .. $Grid->{rowcount}-1) {');
	&ASPCustomTag('\s*FOREACH\s*GRID\s*COLUMN\s*','foreach $COL (0 .. $Grid->{colcount}-1) { $DAY = $Grid->{grid}->[$ROW]->[$COL]; my ($EVENTS) = $Grid->{grid}->[$ROW]->[$COL]->{events};');
	&ASPCustomTag('\s*FOREACH\s*DAY\s*OF\s*WEEK\s*','foreach $COL (0 .. $Grid->{colcount}-1) { $DAY = $Grid->{grid}->[0]->[$COL]; my ($EVENTS) = $Grid->{grid}->[0]->[$COL]->{events};');
	&ASPCustomTag('\s*FOREACH\s*HOUR\s*OF\s*DAY\s*','foreach $HOUR ( 99, $Config->{days_hours_display_start} .. $Config->{days_hours_display_end} ) { my ($EVENTS) = $DAY->{hours}->[$HOUR]->{events};');
	&ASPCustomTag('\s*FOREACH\s*EVENTLIST','foreach $datestring (sort keys %$EventList) { $DAY = $EventList->{$datestring}; my ($EVENTS) = $DAY->{events};');
	&ASPCustomTag('\s*FOREACH\s*EVENT\s*','foreach $EVENT (@$EVENTS) { ');
	&ASPCustomTag('\s*FOREACH\s*SEARCH\s*RESULT\s*','foreach $i (0 .. $#$SEARCH_RESULTS) { $EVENT = $SEARCH_RESULTS->[$i]; ');
	&ASPCustomTag('\s*IF\s*SEARCH\s*RESULT\s*','if ($in{command} eq "search") {');
	&ASPCustomTag('\s*IF\s*SEARCH\s*RESULTS\s*EXIST\s*','if ($#$SEARCH_RESULTS < 0) {');
	&ASPCustomTag('\s*IF\s*EVENTS\s*EXIST\s*','if ($#{$EVENTS} >= 0) {');
	&ASPCustomTag('\s*IF\s*NEXT\s*OCCURRENCE\s*EXISTS\s*','if ($EVENT->{schedule}->{nextoccurrence}) {');
	&ASPCustomTag('\s*IF\s*NO\s*EVENTS\s*EXIST\s*','if (!($#{$EVENTS} >= 0)) {');
	&ASPCustomTag('\s*IF\s*DISPLAY\s*','if ($DAY->{\'display\'}) {');
	&ASPCustomTag('\s*IF\s*SELECTED\s*','if ($DAY->{\'selected\'}) {');
	&ASPCustomTag('\s*IF\s*USER\s*LOGGED\s*IN\s*','if ($User->{username} ne "anonymous") {');
	&ASPCustomTag('\s*/FOREACH\s*','}');
	&ASPCustomTag('\s*ELSE\s*','}else{');
	&ASPCustomTag('\s*/IF\s*','}');

	# Other special tags
	&ASPCustomTag('=?\s*EVENT\s*FIELD\s*\((\w+)\)\s*','= $EVENT->{details}->{$1} ');
	&ASPCustomTag('=?\s*SCHEDULE\s*FIELD\s*\((\w+)\)\s*','= $EVENT->{schedule}->{$1} ');
	&ASPCustomTag('=?\s*PREFERENCE\s*\((\w+)\)\s*','= &getPreference(\'$1\') ');
	&ASPCustomTag('\s*LAST\s*YEAR\s*LINK\s*','= $CGI_URL_QUERYSTRING."year=".$LAST_YEAR');
	&ASPCustomTag('\s*NEXT\s*YEAR\s*LINK\s*','= $CGI_URL_QUERYSTRING."year=".$NEXT_YEAR');
	&ASPCustomTag('\s*LAST\s*MONTH\s*LINK\s*','= $CGI_URL_QUERYSTRING."year=".$LAST_MONTH_YEAR."&month=".$LAST_MONTH');
	&ASPCustomTag('\s*NEXT\s*MONTH\s*LINK\s*','= $CGI_URL_QUERYSTRING."year=".$NEXT_MONTH_YEAR."&month=".$NEXT_MONTH');
	&ASPCustomTag('\s*LAST\s*WEEK\s*LINK\s*','= $CGI_URL_QUERYSTRING."year=".$LAST_WEEK_YEAR."&month=".$LAST_WEEK_MONTH."&date=".$LAST_WEEK_DATE');
	&ASPCustomTag('\s*NEXT\s*WEEK\s*LINK\s*','= $CGI_URL_QUERYSTRING."year=".$NEXT_WEEK_YEAR."&month=".$NEXT_WEEK_MONTH."&date=".$NEXT_WEEK_DATE');

	&ASPCustomTag('\s*PREVIOUS\s*DAY\s*LINK\s*','= $CGI_URL_QUERYSTRING."datestring=".$PREVIOUS_DAY_DATESTRING."&selected_datestring=".$PREVIOUS_DAY_DATESTRING');
	&ASPCustomTag('\s*NEXT\s*DAY\s*LINK\s*','= $CGI_URL_QUERYSTRING."datestring=".$NEXT_DAY_DATESTRING."&selected_datestring=".$NEXT_DAY_DATESTRING');

	&ASPCustomTag('\s*CALENDAR\s*NAME\s*','= ($CALENDAR->{name})');
	&ASPCustomTag('\s*CALENDAR\s*DESCRIPTION\s*','= ($CALENDAR->{description})');
	&ASPCustomTag('\s*CALENDAR\s*KEY\s*','= ($CALENDAR->{key})');
	}

##################################################
# Subroutine called by Template to get an event
##################################################
sub getEvent {
	my ($id) = @_;
	unless(&handleCustomFunction("display_before_getEvent",$id)) {
		my ($db) = new DBFile($events_db);
		my ($event) = $db->getRecord( {'id'=>$id } );
		if ($event == 0) { return {}; }
		# Add the auto-links if necessary
		if ($Config->get("auto_link")) {
			foreach $key (keys %$event) {
				$event->{$key} = &HTML::autoLink($event->{$key},$Config->get("auto_link_target"));
				}
			}
		&handleCustomFunction("display_after_getEvent");
		return $event;
		}
	}

##################################################
# Subroutine called by Template to populate events
##################################################
sub getEvents {
	my ($properties) = @_;
	unless(&handleCustomFunction("display_before_getEvents",$properties)) {
		my ($event_ids,$events,$event_details,$s);
		my ($month,$year,$date,$datestring,$start,$end);

		$month = &LZ($properties->{'month'}) || &LZ($Template::MONTH);
		$year = $properties->{'year'} || ($Template::YEAR);
		$date = &LZ($properties->{'date'}) || &LZ($Template::DATE);

		if ($properties->{'range'} eq "month") {
			$datestring = $year . $month . "01";
			$properties->{'startdate'} = $datestring;
			}
		else {
			$datestring = $year . $month . $date;
			$properties->{'startdate'} ||= $datestring;
			}

		($start,$end) = &Date::getTimeSpan( $properties );	
		$Template::RANGE_START = &SimpleDateFormat::formatDate($start,$Config->get("date_format"));
		($Template::RANGE_START_DATE,$Template::RANGE_START_MONTH,$Template::RANGE_START_YEAR) = (gmtime($start))[3,4,5];
		$Template::RANGE_START_MONTH++;
		$Template::RANGE_START_YEAR+=1900;
		$Template::RANGE_END = &SimpleDateFormat::formatDate($end,$Config->get("date_format"));
		($Template::RANGE_END_DATE,$Template::RANGE_END_MONTH,$Template::RANGE_END_YEAR) = (gmtime($end))[3,4,5];
		$Template::RANGE_END_MONTH++;
		$Template::RANGE_END_YEAR+=1900;

		$schedule = &Event::getEventsInRange($DBSchedule,$start,$end);
		foreach $s (@$schedule) {
			$event_ids->{$s->{'event_id'}}=1;
			}
		$event_details = &Event::getEventDetails($DBEvents,$event_ids);

		foreach $s (@$schedule) {
			# Skip the event unless it's approved
			next unless ($event_details->{$s->{'event_id'}}->{'approved'});
			# Skip if it's private
			next if ($event_details->{$s->{'event_id'}}->{'private'});

			push(@$events, { 'schedule'=>$s, 'details'=>$event_details->{$s->{'event_id'}} } );
			}

		# Put the raw events into the template
		# ------------------------------------
		$Template::EVENTS = $events;

		my ($Grid);
		my ($start_ss,$start_mi,$start_hh,$start_dd,$start_mm,$start_yy,$start_wd,$start_yd,$start_dst) = gmtime($start);
		$week_start_day = $Config->get("week_start_day");
		if ($start_wd >= $week_start_day) {
			$offset_days = $start_wd - $week_start_day;
			}
		elsif ($start_wd < $week_start_day) {
			$offset_days = 7-$week_start_day+$start_wd;
			}
		$i = $start;
		my $x = 0;
		my $y = 0;
		# Place pre-empty grid cells if more than one row
		if ((($end - $start)/86400) > 7) {
			foreach (0 .. ($offset_days-1)) {
				$Grid->{'grid'}->[$y]->[$x]->{'display'} = 0;
				$x++;
				}
			}
		while ($i < $end) {
			my ($ss,$mi,$hh,$dd,$mm,$yy,$wd,$yd,$dst) = gmtime($i);
			my ($datestring) = (1900+$yy) . &LZ($mm+1) . &LZ($dd);
			$gridMappings->{$datestring} = [$y,$x];
			$Grid->{'grid'}->[$y]->[$x]->{'dd'} = $dd;
			$Grid->{'grid'}->[$y]->[$x]->{'mm'} = $mm+1;
			$Grid->{'grid'}->[$y]->[$x]->{'yyyy'} = 1900+$yy;
			$Grid->{'grid'}->[$y]->[$x]->{'wd'} = $wd;
			$Grid->{'grid'}->[$y]->[$x]->{'yd'} = $yd;
			$Grid->{'daynames'}->[$x] = $Template::DAY_NAMES->[$wd];
			$Grid->{'grid'}->[$y]->[$x]->{'dayname'} = $Template::DAY_NAMES->[$wd];
			$Grid->{'grid'}->[$y]->[$x]->{'dayabbreviation'} = $Template::DAY_ABBREVIATIONS->[$wd];
			$Grid->{'grid'}->[$y]->[$x]->{'monthname'} = $Template::MONTH_NAMES->[$mm];
			$Grid->{'grid'}->[$y]->[$x]->{'monthabbreviation'} = $Template::MONTH_ABBREVIATIONS->[$mm];
			$Grid->{'grid'}->[$y]->[$x]->{'datestring'} = $datestring;
			$Grid->{'grid'}->[$y]->[$x]->{'display'} = 1;
			if ($datestring eq $selected_datestring) {
				$Grid->{'grid'}->[$y]->[$x]->{'selected'} = 1;
				}
			$x++;
			$Grid->{'rowcount'} = $y+1;
			if ($x > $Grid->{'colcount'}) { $Grid->{'colcount'} = $x; }
			if ($x > 6) { $x=0; $y++; }
			$i+=86400;
			}
		# Place post-empty grid cells if more than one row
		if ((($end - $start)/86400) > 7) {
			while($wd < 6) {
				$Grid->{'grid'}->[$y]->[$x]->{'display'} = 0;
				$x++;
				$wd++;
				}
			}
		$Template::Grid = $Grid;
		$Template::GRID_ROW_COUNT = $Grid->{'rowcount'};
		$Template::GRID_COLUMN_COUNT = $Grid->{'colcount'};

		# Map events on to Grid and dates/hours/etc
		# -----------------------------------------
		foreach $event (sort {$a->{'schedule'}->{'start'} <=> $b->{'schedule'}->{'start'} } @$events) {
			# Time of event
			if ($event->{'schedule'}->{'start_time'} == $event->{'schedule'}->{'end_time'}) {
				$event->{'schedule'}->{'end_time'} = "";
				}
			if ($event->{'schedule'}->{'all_day'}) {
				$event->{'schedule'}->{'start_time'} = "";
				$event->{'schedule'}->{'end_time'} = "";
				$event->{'schedule'}->{'start_hh'}=99;
				$event->{'schedule'}->{'start_mm'}=0;
				$event->{'schedule'}->{'end_hh'}=99;
				$event->{'schedule'}->{'end_mm'}=0;
				
				}
			else {
				($hh,$mm) = ($event->{'schedule'}->{'start_time'} =~ /^(\d\d)(\d\d)/);
				$event->{'schedule'}->{'start_hh'} = $hh;
				$event->{'schedule'}->{'start_mm'} = $mm;
				($hh,$mm) = ($event->{'schedule'}->{'end_time'} =~ /^(\d\d)(\d\d)/);
				$event->{'schedule'}->{'end_hh'} = $hh;
				$event->{'schedule'}->{'end_mm'} = $mm;
				$event->{'schedule'}->{'start_time'} = &Date::formatTime($event->{'schedule'}->{'start_time'}, $Config->get("time_format"));
				$event->{'schedule'}->{'end_time'} = &Date::formatTime($event->{'schedule'}->{'end_time'} , $Config->get("time_format"));
				}

			# Date, month, day name, month name, etc
			my ($event_start) = $event->{'schedule'}->{'start'};
			my ($event_end) = $event->{'schedule'}->{'end'};
			my ($continued) = 0;
			# If event spans multiple days, keep track of it
			$event->{'schedule'}->{'span'} = (($event_end - $event_start) > 86400)?1:0;
			
			while ($event_start <= $event_end) {
				if (($event_start >= $start) && ($event_start <= $end)) {
					my ($ss,$mi,$hh,$dd,$mm,$yy,$wd,$yd,$dst) = gmtime($event_start);
					$event->{'schedule'}->{'year'} = (1900+$yy);
					$event->{'schedule'}->{'month'} = $mm+1;
					$event->{'schedule'}->{'date'} = $dd;
					$event->{'schedule'}->{'day'} = $wd;
					my ($datestring) = (1900+$yy) . &LZ($mm+1) . &LZ($dd);
					$event->{'schedule'}->{'datestring'} = $datestring;
					if ($event->{'schedule'}->{'all_day'}) {
						$hh = 99;
						}
					else {
						$hh = &LZ($hh);
						}
					push(@{$Grid->{'grid'}->[$gridMappings->{$datestring}->[0]]->[$gridMappings->{$datestring}->[1]]->{'events'}} , $event);
					push(@{$Grid->{'grid'}->[$gridMappings->{$datestring}->[0]]->[$gridMappings->{$datestring}->[1]]->{'hours'}->[$hh]->{'events'}} , $event);

					$continued=1;
					}
				$event_start = $event_start+86400;
				}
			}
		# Sort the events on each day into chronological order
		for ($y=0; $y<$Grid->{'rowcount'}; $y++) {
			for ($x=0; $x<$Grid->{'colcount'}; $x++) {
				if ($Grid->{'grid'}->[$y]->[$x]->{'display'}) {
					@{$Grid->{'grid'}->[$y]->[$x]->{'events'}} = sort { ($a->{'schedule'}->{'start'} <=> $b->{'schedule'}->{'start'}) || ($a->{'details'}->{'id'} <=> $b->{'details'}->{'id'}) } @{$Grid->{'grid'}->[$y]->[$x]->{'events'}};
					$EventList->{$Grid->{'grid'}->[$y]->[$x]->{'datestring'}} = $Grid->{'grid'}->[$y]->[$x];
					}
				}
			}
		$Template::EventList = $EventList;

		if ($properties->{'range'} eq "day") {
			$Template::DAY = $Grid->{'grid'}->[0]->[0];
			$Template::EVENTS = $Grid->{'grid'}->[0]->[0]->{'events'};
			}
		}
		&handleCustomFunction("display_after_getEvents",$properties);
	}
