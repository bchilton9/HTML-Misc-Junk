# header/footer display for the Office mod
# each section has it's own arrangement of top icons
# they all share the bottom text navigation

###########################
sub top_navbar_tasks {
###########################

my $headerColor = shift;

print qq~
<table cellspacing="0" cellpadding="0" border="0" width="100%">
	<tr>
	    <td align="left">
			<a href="$officeURL/tasks.cgi"><IMG alt="$office_task{'001'}" src="$imgURL/task_big.gif" border=0" align="absmiddle"></a>
			<font size="+1">$office_gen{'032'} $office_task{'001'}</font>
		</td>
		<td align="right">
			<table cellspacing="1" cellpadding="2" border="0">
				<tr>
					<td align="center" bgcolor="$headerColor">
					<a href="$officeURL/index.cgi"><IMG alt="$office_gen{'002'}" src="$imgURL/office_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/journal.cgi"><IMG alt="$office_journal{'001'}" src="$imgURL/journal_big.gif" border=0></A>	
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/calendar.cgi"><IMG alt="$office_cal{'001'}" src="$imgURL/calendar_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/contacts.cgi"><IMG alt="$office_con{'001'}" src="$imgURL/contact_big.gif" border=0></A>
					</td>
				</tr>
			</table>
		</td>
	</tr>
</table>
~;

}		

###########################
sub top_navbar_contacts {
###########################

my $headerColor = shift;

print qq~
<table cellspacing="0" cellpadding="0" border="0" width="100%">
	<tr>
	    <td align="left">
			<a href="$officeURL/contacts.cgi"><IMG alt="$office_con{'001'}" src="$imgURL/contact_big.gif" border=0 align="absmiddle"></a>
			<font size="+1">$office_gen{'032'} $office_con{'001'}</font>
		</td>
		<td align="right">
			<table cellspacing="1" cellpadding="2" border="0">
				<tr>
					<td align="center" bgcolor="$headerColor">
					<a href="$officeURL/index.cgi"><IMG alt="$office_gen{'002'}" src="$imgURL/office_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/journal.cgi"><IMG alt="$office_journal{'001'}" src="$imgURL/journal_big.gif" border=0></A>	
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/calendar.cgi"><IMG alt="$office_cal{'001'}" src="$imgURL/calendar_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/tasks.cgi"><IMG alt="$office_task{'001'}" src="$imgURL/task_big.gif" border=0"></A></td>
				</tr>
			</table>
		</td>
	</tr>
</table>
~;

}		

###########################
sub top_navbar_calendar {
###########################

my $headerColor = shift;

print qq~
<table cellspacing="0" cellpadding="0" border="0" width="100%">
	<tr>
	    <td align="left">
			<a href="$officeURL/calendar.cgi"><IMG alt="$office_cal{'001'}" src="$imgURL/calendar_big.gif" border=0 align="absmiddle"></a>
			<font size="+1">$office_gen{'032'} $office_cal{'001'}</font>
		</td>
		<td align="right">
			<table cellspacing="1" cellpadding="2" border="0">
				<tr>
					<td align="center" bgcolor="$headerColor">
					<a href="$officeURL/index.cgi"><IMG alt="$office_gen{'002'}" src="$imgURL/office_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/journal.cgi"><IMG alt="$office_journal{'001'}" src="$imgURL/journal_big.gif" border=0></A>	
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/contacts.cgi"><IMG alt="$office_con{'001'}" src="$imgURL/contact_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/tasks.cgi"><IMG alt="$office_task{'001'}" src="$imgURL/task_big.gif" border=0"></A></td>
				</tr>
			</table>
		</td>
	</tr>
</table>
~;

}		

###########################
sub top_navbar_journal {
###########################

my $headerColor = shift;

#print qq~
#<table cellspacing="0" cellpadding="0" border="0" width="100%">
#	<tr>
#	    <td align="left">
#			<a href="$officeURL/journal.cgi"><IMG alt="$office_journal{'001'}" src="$imgURL/journal_big.gif" border=0 align="absmiddle"></a>
#			<font size="+1">$office_gen{'032'} $office_journal{'001'}</font>
#		</td>
#		<td align="right">
#			<table cellspacing="1" cellpadding="2" border="0">
#				<tr>
#					<td align="center" bgcolor="$headerColor">
#					<a href="$officeURL/index.cgi"><IMG alt="$office_gen{'002'}" src="$imgURL/office_big.gif" border=0></A>
#					</td><td align="center" bgcolor="$headerColor">
#					<a href="$officeURL/calendar.cgi"><IMG alt="$office_cal{'001'}" src="$imgURL/calendar_big.gif" border=0></A>
#					</td><td align="center" bgcolor="$headerColor">
#					<a href="$officeURL/contacts.cgi"><IMG alt="$office_con{'001'}" src="$imgURL/contact_big.gif" border=0></A>
#					</td><td align="center" bgcolor="$headerColor">
#					<a href="$officeURL/tasks.cgi"><IMG alt="$office_task{'001'}" src="$imgURL/task_big.gif" border=0"></A></td>
#				</tr>
#			</table>
#		</td>
#	</tr>
#</table>
#~;

}		

###########################
sub top_navbar_office {
###########################

my $headerColor = shift;

print qq~
<table cellspacing="0" cellpadding="0" border="0" width="100%">
	<tr>
	    <td align="left">
			<a href="$officeURL/index.cgi"><IMG alt="$office_gen{'002'}" src="$imgURL/office_big.gif" border=0 align="absmiddle"></a>
			<font size="+1">$office_gen{'032'} $office_gen{'002'}</font>
		</td>
		<td align="right">
			<table cellspacing="1" cellpadding="2" border="0">
				<tr>
					<td align="center" bgcolor="$headerColor">
					<a href="$officeURL/journal.cgi"><IMG alt="$office_journal{'001'}" src="$imgURL/journal_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/calendar.cgi"><IMG alt="$office_cal{'001'}" src="$imgURL/calendar_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/contacts.cgi"><IMG alt="$office_con{'001'}" src="$imgURL/contact_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/tasks.cgi"><IMG alt="$office_task{'001'}" src="$imgURL/task_big.gif" border=0"></A></td>
				</tr>~;
				if ($username eq "admin") {
					print qq~
					<tr><td colspan="4" align="center"><font size="1">[ <a href="$officeURL/admin.cgi">$office_gen{'012'}</a> ]</font></td></tr>
					~;
				}
			print qq~
			</table>
		</td>
	</tr>
</table>
~;

}		

###########################
sub top_navbar_admin {
###########################

my $headerColor = shift;

print qq~
<table cellspacing="0" cellpadding="0" border="0" width="100%">
	<tr>
	    <td align="left">
			<font size="+1">$office_gen{'012'}</font>
		</td>
		<td align="right">
			<table cellspacing="1" cellpadding="2" border="0">
				<tr>
					<td align="center" bgcolor="$headerColor">
					<a href="$officeURL/index.cgi"><IMG alt="$office_gen{'002'}" src="$imgURL/office_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/journal.cgi"><IMG alt="$office_journal{'001'}" src="$imgURL/journal_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/calendar.cgi"><IMG alt="$office_cal{'001'}" src="$imgURL/calendar_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/contacts.cgi"><IMG alt="$office_con{'001'}" src="$imgURL/contact_big.gif" border=0></A>
					</td><td align="center" bgcolor="$headerColor">
					<a href="$officeURL/tasks.cgi"><IMG alt="$office_task{'001'}" src="$imgURL/task_big.gif" border=0"></A></td>
				</tr>
			</table>
		</td>
	</tr>
</table>
~;

}		

###########################
sub bottom_nav {
###########################

# it would be nice if you leave my website link :)
#$copyleft = qq~ ~;
			
# create a link if they implement the group calendar
#if (-e("$officeDIR/groupcal.cgi")) {
#	$grouplink = "<a href=\"$officeURL/groupcal.cgi\">$office_cal{'032'}</A> | ";
#}
#else {
#	$grouplink = "";
#}

#print qq~
#<table cellspacing="0" cellpadding="2" border="0" width="100%">
#	<tr>
#	    <td height="5" align="center"><font size="1">
#		<br><br>
#		$grouplink
#		<a href="$officeURL/index.cgi">$office_gen{'002'}</A> | 
#		<a href="$officeURL/journal.cgi">$office_journal{'001'}</A> | 
#		<a href="$officeURL/calendar.cgi">$office_cal{'001'}</A> | 
#		<a href="$officeURL/contacts.cgi">$office_con{'001'}</A> | 
#		<a href="$officeURL/tasks.cgi">$office_task{'001'}</A></font><BR>
#		$copyleft</td>
#	</tr>
#</table>
#~;

}

###########################
sub mod_langsupp {
###########################

$modlangfail = "0";

if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat");
		file_lock(FILE);
		@settings = <FILE>;
		unfile_lock(FILE);
		close(FILE);

		for( $i = 0; $i < @settings; $i++ ) {
			$settings[$i] =~ s~[\n\r]~~g;
		}
		
		if ($settings[0] ne $password && $action ne "logout") { error("$err{'002'}"); }
		else {
			$realname = $settings[1];
			$realemail = $settings[2];
			$userlang = $settings[15];
		}
		
}

		if ($userlang eq "") { $userlang = $language; }
						
			 if ($modlangfail ne "1") {
			 @modlanguage = $userlang;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
			 } else {
			 @modlanguage = $language;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
		}

eval {
	require "$officeDIR/language/$modlang.dat";
	
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};

if ($@) {$modlangfail = "1"; mod_langsuppfail();}

}

########################
sub mod_langsuppfail {
########################

eval {
	require "$officeDIR/language/$mod_lang";
	
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};
if ($@) {
print "Content-type: text/html\n\n";
print qq~<h1>Software Error:</h1>
Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
<pre>$@</pre>
<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
~;
	exit;
}

}


1;