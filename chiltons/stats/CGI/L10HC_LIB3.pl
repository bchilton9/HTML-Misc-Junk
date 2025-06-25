# v3.16 1/1/04

$filePermissions = "755";

sub initForm() {
	my ($errMsg) = @_;
	
	open (FILE, ">L10HC_writetest.dat") || &gen_error_int("Script cannot write to files. See <a href=http://www.leveltendesign.com/L10Apps/HC/help_troubleshooting.html#directory_permissions target=_blank>troublshooting</a> to resolve this issue.");
	close (FILE);
	unlink ("L10HC_writetest.dat");
	
	@script = split(/\//,$ENV{'SCRIPT_NAME'});
	print header;
	print "<html>\n<header>\n<title>Script Initialization</title>\n<style>body {font-family : Arial, Helvetica, sans-serif;}</style>\n";
	print '<script language=JavaScript> function initForm() { ref=window.location.href; document.theForm.cgi.value = ref; re = /^http:\/\//; ref = ref.replace(re,""); re = /^https:\/\//; ref = ref.replace(re,""); re = /^www./; ref = ref.replace(re,""); refs = ref.split("/"); document.theForm.validDoms.value = refs[0];}'."\n</script>\n";
	print "</header>\n<body onLoad=initForm()>\n";
	print "<form name=theForm action=\"$script[$#script]\" method=POST>\n";
	print "<input type=hidden name=action value=init>\n";
	print "<input type=hidden name=aPw value=$adminPassword>\n";
	
	print "<table align=center width=400>";
	print "<tr><td><b>Install Form</b></td></tr>\n";
	print "<tr><td><font color=#FF0000><b>$errMsg</b></font></td></tr>\n";
	
	print "<tr><td><br><b>A. URL for L10HC_Admin.cgi:</b> (this script)<br>\n<input name=cgi type=text size=80 value='http://'></td></tr>\n";
	print "<tr><td><br><b>B. URL address to L10HC_Reporter.html:</b><br>\n<input name=url type=text size=80 value='http://'></td></tr>\n";
	print "<tr><td><br><b>C. Authorized Domains:</b><br>\n<input name=validDoms type=text size=80><br>\n(Provide domain(s) that will be authorized to report hits. For multiple domains separate by commas. Don't use \"http://\" or \"www\")</td></tr>\n";
	print "<tr><td><br><b>D. Index Page:</b><br>\n<input name=indexPage type=text size=80 value=index.html><br>\n</td></tr>\n";
	if($acctManager) {
		print "<tr><td><br><b>E. Account Directory:</b><br>\n<input name=acct type=text size=80 value=''><br>\nOnly use letters, number and underscores</td></tr>\n";
		print "<tr><td><br><b>F. Account Name:</b><br>\n<input name=acctName type=text size=80 value=''><br></td></tr>\n";
	}
	print "<tr><td align=center><br><input type=submit name='init' value='Initialize'>\n</td></tr></table></form>";

	print "</body></html>";
	exit 0;	
}

sub initAcct() {
	my ($errMsg) = @_;
	@script = split(/\//,$ENV{'SCRIPT_NAME'});
	print header;
	print "<html>\n<header>\n<title>Account Initialization</title>\n<style>body {font-family : Arial, Helvetica, sans-serif;}</style>\n";
	print '<script language=JavaScript> function initForm() { ref=window.location.href; document.theForm.cgi.value = ref; re = /^http:\/\//; ref = ref.replace(re,""); re = /^https:\/\//; ref = ref.replace(re,""); re = /^www./; ref = ref.replace(re,""); refs = ref.split("/"); document.theForm.validDoms.value = refs[0]; document.theForm.rTitle.value = refs[0];}'."\n</script>\n";
	print "</header>\n<body onLoad=initForm()>\n";
	print "<form name=theForm action=\"$script[$#script]\" method=POST>\n";
	print "<input type=hidden name=action value=init>\n";
	print "<input type=hidden name=aPw value=$adminPassword>\n";
	
	print "<table align=center width=400>";
	print "<tr><td><b>Install Form</b></td></tr>\n";
	print "<tr><td><font color=#FF0000><b>$errMsg</b></font></td></tr>\n";
	
	print "<tr><td><br><b>A. URL for L10HC_Admin.cgi:</b> (this script)<br>\n<input name=cgi type=text size=80 value='http://'></td></tr>\n";
	print "<tr><td><br><b>B. URL address to L10HC_Reporter.html:</b><br>\n<input name=url type=text size=80 value='http://'></td></tr>\n";
	print "<tr><td><br><b>C. Authorized Domains:</b><br>\n<input name=validDoms type=text size=80><br>\n(Provide domain(s) that will be authorized to report hits. For multiple domains separate by commas. Don't use \"http://\" or \"www\")</td></tr>\n";
	print "<tr><td><br><b>D. Index Page:</b><br>\n<input name=indexPage type=text size=80 value=index.html><br>\n</td></tr>\n";
	if($acctManager) {
		print "<tr><td><br><b>E. Account Directory:</b><br>\n<input name=acct type=text size=80 value=''><br>\nOnly use letters, number and underscores</td></tr>\n";
		print "<tr><td><br><b>F. Account Name:</b><br>\n<input name=acctName type=text size=80 value=''><br></td></tr>\n";
	}
	print "<tr><td align=center><br><input type=submit name='init' value='Initialize'>\n</td></tr></table></form>";

	print "</body></html>";
	exit 0;	
}

sub initScript() {	
	$initDate = $dateStamp;
	$adminPassword = 'password';
	$logLimit = 100;
	$keyCode = '';
	$kcErr = 0;
	$kcErrMsg = '';
	$datVer = 0;
	$debugLog = 0;
	$acctManager = 0;
	
	&writeParams();
	
	&initAcct();	
}

sub initAcct() {	
	$startDate = $dateStamp;
	$startDateDisplay = "$curMo/$curDay/$curYr";
	$acct = '.';
	$siteTitle = '';
	if(param('acct') ne '') {
		$acct = param('acct');
		$siteTitle = " - ".param('acct');
	}
	$timeAdj = 0; #new
	@phrases = ('<P ALIGN="CENTER"><FONT FACE="_sans" SIZE="14" COLOR="#000000">--SV0-- visitors since --TD0--</FONT></P>','<P ALIGN="CENTER"><FONT FACE="_sans" SIZE="14" COLOR="#000000">--PH0-- page views since --TD0--</FONT></P>');
	$removeDisplay = 1;
	$removeBranding = 0; #new
	$password = "password";
	$allowLocalFiles = 0;
	$t = param('validDoms');
	@validDoms = split(/,/,$t);
	$removePageWWW = 1;
	$lowercasePage = 1;
	$lowercaseRef = 1;
	$removeQueryStr = 0;
	@queryStrFilters = ('');
	$indexPage = param('indexPage');
	$maxPgTime = 900;
	$protectStats = 1;
	$reporterURL = param('url');
	$enableAdminLink = 1;
	$displaySize = "250X22";
	$fileLockTO = 30;
	$maxRepItems = 200;
	$visitorLog  = 0;
	
	
	if($acct ne '.') {
		unless (-e "$acct") {mkdir "$acct", $filePermissions;}
	}
	$acct = $dataDir.$acct;
	
	&writeAcctParams();
	
	%t = ("[Unknown]" => 0);
	unless (-e "$acct/L10HC_Hits.dat") {
		open (DSTAT_FH, ">$acct/L10HC_Hits.dat") || &gen_error("Cannot create $acct/L10HC_Hits.dat at DoInit");
		print DSTAT_FH "$dateStamp\n";
		print DSTAT_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print DSTAT_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print DSTAT_FH "\n";
		print DSTAT_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print DSTAT_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print DSTAT_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		$i = 1;
		foreach (@validDoms) {
			$t{$_} = $i;
			print DSTAT_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
			$i++;
		}
		close (DSTAT_FH);
	}
	
	open (FILE, ">$acct/L10HC_Nav.dat") || &gen_error("Cannot create $acct/L10HC_Nav.dat at DoInit");
	close (FILE);
	
	open (FILE, ">$acct/L10HC_Extended.dat") || &gen_error("Cannot create $acct/L10HC_Extended.dat at DoInit");
	close (FILE);
	
	open (FILE, ">$acct/L10HC_IPL.dat") || &gen_error("Cannot create $acct/L10HC_IPL.dat at DoInit");
	close (FILE);
	open (FILE, ">$acct/L10HC_IPL2.dat") || &gen_error("Cannot create $acct/L10HC_IPL2.dat at DoInit");
	close (FILE);
	open (FILE, ">$acct/L10HC_IPI.dat") || &gen_error("Cannot create $acct/L10HC_IPI.dat at DoInit");
	close (FILE);
	open (FILE, ">$acct/L10HC_IPI2.dat") || &gen_error("Cannot create $acct/L10HC_IPI2.dat at DoInit");
	close (FILE);
	open (FILE, ">$acct/L10HC_IPD.dat") || &gen_error("Cannot create $acct/L10HC_IPD.dat at DoInit");
	close (FILE);
	open (FILE, ">$acct/L10HC_IPD2.dat") || &gen_error("Cannot create $acct/L10HC_IPD2.dat at DoInit");
	close (FILE);
	
	open (FILE, ">$acct/L10HC_Security.log") || &gen_error("Cannot create $acct/L10HC_Security.log at DoInit");
	close (FILE);
	open (FILE, ">$acct/L10HC_Security2.log") || &gen_error("Cannot create $acct/L10HC_Security2.log at DoInit");
	close (FILE);
	
	
	unless(-e "$acct/L10HC_PageL.dat") {
		open (FILE, ">$acct/L10HC_PageL.dat") || &gen_error("Cannot create $acct/L10HC_PageL.dat at DoInit");
		print FILE "[unknown]\n";
		foreach (@validDoms) {
			print FILE "$_/\n";
		}
		close (FILE);

		open (FILE, ">$acct/L10HC_PageI.dat") || &gen_error("Cannot create $acct/L10HC_PageI.dat at DoInit");
		foreach (sort keys %t) {
			print FILE "$t{$_}\n";
		}
		close (FILE);
	}
	
	unless(-e "$acct/L10HC_HotLists.dat") {
		open (FILE, ">$acct/L10HC_HotLists.dat") || &gen_error("Cannot create $acct/L10HC_HotLists.dat at DoInit");
		close (FILE);
	}

	unless (-e "$acct/L10HC_Archive") {mkdir "$acct/L10HC_Archive", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Doms") {mkdir "$acct/L10HC_Archive/Doms", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Doms/Y$curYr2") {mkdir "$acct/L10HC_Archive/Doms/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Refs") {mkdir "$acct/L10HC_Archive/Refs", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Refs/Y$curYr2") {mkdir "$acct/L10HC_Archive/Refs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEs") {mkdir "$acct/L10HC_Archive/SEs", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEs/Y$curYr2") {mkdir "$acct/L10HC_Archive/SEs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/KWs") {mkdir "$acct/L10HC_Archive/KWs", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/KWs/Y$curYr2") {mkdir "$acct/L10HC_Archive/KWs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEKWs") {mkdir "$acct/L10HC_Archive/SEKWs", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEKWs/Y$curYr2") {mkdir "$acct/L10HC_Archive/SEKWs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/rTypes") {mkdir "$acct/L10HC_Archive/rTypes", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/rTypes/Y$curYr2") {mkdir "$acct/L10HC_Archive/rTypes/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/sRefs") {mkdir "$acct/L10HC_Archive/sRefs", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/sRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/sRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/pgRefs") {mkdir "$acct/L10HC_Archive/pgRefs", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/pgRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/pgRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/paRefs") {mkdir "$acct/L10HC_Archive/paRefs", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/paRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/paRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Hits") {mkdir "$acct/L10HC_Archive/Hits", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Hits/Y$curYr2") {mkdir "$acct/L10HC_Archive/Hits/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Paths") {mkdir "$acct/L10HC_Archive/Paths", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Paths/Y$curYr2") {mkdir "$acct/L10HC_Archive/Paths/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Visitor") {mkdir "$acct/L10HC_Archive/Visitor", $filePermissions;}
	
	unless (-e "$acct/L10HC_Archive/SiteHistory_Hits.dat") {
		open (SITE_FH, ">$acct/L10HC_Archive/SiteHistory_Hits.dat") || &gen_error("Cannot create $acct/SiteHistory_Hits.dat at DoInit");
		close (SITE_FH);
	}
	
	unless (-e "$acct/L10HC_Archive/rTypes/rTypeL.dat") {
		open (FILE, ">$acct/L10HC_Archive/rTypes/rTypeL.dat") || &gen_error("Cannot create $acct/L10HC_Archive/rTypes/rTypeL.dat at DoInit");
		print FILE "[Unknown]\n";
		print FILE "[Major SE]\n";
		print FILE "[Site Link]\n";
		close (FILE);
		
		open (FILE, ">$acct/L10HC_Archive/rTypes/rTypeI.dat") || &gen_error("Cannot create $acct/L10HC_Archive/rTypes/rTypeI.dat at DoInit");
		print FILE "1\n";
		print FILE "2\n";
		print FILE "0\n";
		close (FILE);
	}
	
	unless(-e "$acct/L10HC_Archive/Hits_byPeriod.dat") {
		open (SITE_FH, ">$acct/L10HC_Archive/Hits_byPeriod.dat") || &gen_error("Cannot create $acct/Hits_byPeriod.dat at DoInit");
		print SITE_FH "0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		print SITE_FH "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n";
		close (SITE_FH);
	}
	
	open (PLIST_FH, ">$acct/L10HC_FlashParams.txt") || &gen_error("Cannot create pagelist at $acct/L10HC_AdminParams.txt");
	$cgi = param('cgi');
	$cgi =~ s/L10HC_AcctManager/L10HC_Admin/;
	print PLIST_FH "res=OK&cgiPath=$cgi&acct=".(($acct eq '.') ? '' : $acct)."&";
	close (PLIST_FH);
	
	print header;
	if($acctManager) {
		&initAcct2();
		print "<html><header><title>New Account Initialized</title><style>body {font-family : Arial, Helvetica, sans-serif;}</style></header><body>\n";
		print "<table align=center>";
		print "<tr><td nowrap><b>Initialization Succesful!</b><br>\n<br></td></tr>\n";
		print "<tr><td>&nbsp;</td></tr>\n";
		print "<tr><td align=center><form action=L10HC_AcctManager.cgi method=POST><input type=hidden name=aPw value=$aPw><input type=submit value='Return to Accounts'></form></td></tr>\n";
	} else {
		print "<html><header><title>L10 Hit Counter script init</title><style>body {font-family : Arial, Helvetica, sans-serif;}</style></header><body>\n";
		print "<table align=center>";
		print "<tr><td nowrap><b>Initialization Succesful!</b><br>\n<br></td></tr>\n";	
	}
	print "</table></body></html>";
	exit 0;	

}

sub initAcct2 () {
	$acctActive  = 1;
	@contactInfo = ('','','','');
	@userPasswords = ('password');
	@userEmails= ('');
	@userSesIDs = (0);
	&writeAMAcctParams();
}

sub genPageCode () {
	$scriptURL = $ENV{'SERVER_NAME'}.$ENV{'SCRIPT_NAME'};
	$scriptURL =~ s/L10HC_Admin\./L10HC_Counter\./i;
	$displayURL = $reporterURL;
	$displayURL =~ s/L10HC_Reporter.html/L10HC_Display.swf/i;
	if($acct eq '.') {
		$acctStr = '';
	} else {
		$acctStr = "acct=$acct&";
	}
	print header;
	print '<HTML><head><title>L10 Hit Counter HTML page tag</title></head><body>'."\n";
	print '<table width=550 align=center><tr><td style="font-family: arial,helvetica,sans-serif">';
	print 'Copy the tag below and paste into all pages you want to track on your website.';
	print '</tr></td><tr><td>';
	print '<form action=""><textarea cols=80 rows=20>'."\n";
	print '<!-- L10 Hit Counter page code -->'."\n";
	print '<table border=0 cellspacing=0 cellpadding=0 align=center>'."\n";	
	if(!$removeDisplay) {
		print '<tr><td><OBJECT classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" ID="L10HC_Display" WIDTH="250" HEIGHT="22" ALIGN=""><PARAM NAME=movie VALUE="'.$displayURL.'"> <PARAM NAME=quality VALUE=high> <PARAM NAME=wmode VALUE=transparent> <PARAM NAME=bgcolor VALUE=#FFFFFF> <EMBED src="'.$displayURL.'" quality=high wmode=transparent bgcolor=#FFFFFF  WIDTH="250" HEIGHT="22" swLiveConnect=true ID="L10HC_Display" NAME="L10HC_Display" ALIGN="" TYPE="application/x-shockwave-flash" PLUGINSPAGE="http://www.macromedia.com/go/getflashplayer"></EMBED></OBJECT></td></tr>'."\n";
		print '<tr><td><table border=0 cellspacing=0 cellpadding=0 align=center>'."\n";
	}	
	print '<script language="javascript">'."\n";
	print 'var success=0; cRef=""; cRefType=""; cPage="";'."\n";
	if(!$removeDisplay) {
		print 'var InternetExplorer = navigator.appName.indexOf("Microsoft") != -1;'."\n";
		print 'function L10HC_Display_DoFSCommand(command, args) {'."\n";
		print 'var L10HC_DisplayObj = InternetExplorer ? L10HC_Display : window.document.L10HC_Display;'."\n";
		print 'if(command == "init") { L10HC_DisplayObj.SetVariable("page",document.URL.toString()); L10HC_DisplayObj.GotoFrame(3); } }'."\n";
		print 'if (navigator.appName && navigator.appName.indexOf("Microsoft") != -1 && navigator.userAgent.indexOf("Windows") != -1 && navigator.userAgent.indexOf("Windows 3.1") == -1) {'."\n";
		print "document.write(\'<SCRIPT LANGUAGE=VBScript\\> \\n on error resume next \\nSub L10HC_Display_FSCommand(ByVal command, ByVal args)\\n  call L10HC_Display_DoFSCommand(command, args)\\nend sub\\n </SCRIPT\\> \\n\'); }"."\n";
	}
	print 'var L10qstr,L10pc,L10ref,L10a,L10pg; L10pg=document.URL.toString(); L10ref=document.referrer;'."\n";
	print 'if(top.document.location==document.referrer || (document.referrer == "" && top.document.location != "")) {L10ref=top.document.referrer;}'."\n";
	print 'L10qStr = "'.$acctStr.'pg="+escape(L10pg)+"&ref="+escape(L10ref)+"&os="+escape(navigator.userAgent)+"&nn="+escape(navigator.appName)+"&nv="+escape(navigator.appVersion)+"&nl="+escape(navigator.language)+"&sl="+escape(navigator.systemLanguage)+"&sa="+success+"&cR="+escape(cRef)+"&cRT="+escape(cRefType)+"&cPg="+escape(cPage);'."\n";
	print 'if(navigator.appVersion.substring(0,1) > "3") { L10d = new Date(); L10qStr = L10qStr+"&cd="+screen.colorDepth+"&sx="+screen.width+"&sy="+screen.height+"&tz="+L10d.getTimezoneOffset();}'."\n";
	print '<!-- The L10 Hit Counter logo and links must not be removed or altered -->'."\n";
	print 'if((location.href.substr(0,6)=="https:") || (location.href.substr(0,6)=="HTTPS:")) { L10pc="https"; } else { L10pc="http"; }'."\n";
	print 'document.write('."\'".'<tr><td><a href="'.$reporterURL.'" target=_blank><img border=0 hspace=0 vspace=0 width=25 height=25 src="'."\'".'+L10pc+'."\'".'://'.$scriptURL.'?'."\'".'+L10qStr+'."\'".'" alt="L10 Web Stats Reporter 3.15"></a></td>'."\'".');'."\n";
	# print 'document.write('."\'".'<tr><td><a href="'.$reporterURL.'" target=_blank><img border=0 hspace=0 vspace=0 width=25 height=25 src="'."\'".'+L10pc+'."\'".'://'.$scriptURL.'?'."\'".'+L10qStr+'."\'".'" alt="L10 Web Stats Reporter 3.15"></a></td>'."\'".');'."\n";
	print '</script><noscript><tr><td><a href="'.$reporterURL.'"><img border=0 hspace=0 vspace=0 width=25 height=25 src="http://'."$scriptURL?acct=$acct".'" alt="L10 Web Stats Reporter 3.15"></a></td></noscript>'."\n";
	if(!$removeBranding) {
		print '<td><a href="http://www.leveltendesign.com/L10Apps/HC" target="_blank"><img border=0 src="http://'.$scriptURL.'?i=R" width=70 height=25 alt="L10 Hit Counter - Free Web Counters"></a></td></tr><tr><td colspan=2><a href="http://www.leveltendesign.com" target="_blank"><img border=0 src="http://'.$scriptURL.'?i=B" width=95 height=9 alt="LevelTen Web Design Company - Professional Flash &amp; Website Designers"></a></td>'."\n";
	}
	print '</tr></table>';
	if(!$removeDisplay) {
		print '</td></tr></table>';
	}
	print "\n<!-- end: L10 Hit Counter page code -->";
	print '</textarea></tr></td></table></body></html>';

}

sub genEventCode () {
	$scriptURL = $ENV{'SERVER_NAME'}.$ENV{'SCRIPT_NAME'};
	$scriptURL =~ s/L10HC_Admin\./L10HC_Counter\./i;
	$displayURL = $reporterURL;
	$displayURL =~ s/L10HC_Reporter.html/L10HC_Display.swf/i;
	if($acct eq '.') {
		$acctStr = '';
	} else {
		$acctStr = "acct=$acct&";
	}
	print header;
	print '<HTML><head><title>L10 Hit Counter HTML page tag</title></head><body>'."\n";
	print '<table width=550 align=center><tr><td style="font-family: arial,helvetica,sans-serif">';
	print '<form action="">'."\n";
	print 'HTML JavaScript Header Function:<br>'."\n";
	print '<textarea cols=80 rows=7>'."\n";
	print '<script language=JavaScript>'."\n";
	print 'HCImg = new Image();'."\n";
	print 'function HCEvent(event,success) { '."\n\t".'HCImg.src = "http://'.$scriptURL.'?'.$acctStr.'cPg="+event+"&sa="+success;'."\n".'}'."\n";
	print '</script>'."\n";
	print '</textarea><br><br>'."\n";
	print 'Flash ActionScript Event Call:<br>'."\n";
	print '<textarea cols=80 rows=2>'."\n";
	print 'getURL("javascript:HCEvent('."'".'EventName'."'".',successFlag)","_self");';
	print '</textarea><br><br>'."\n";
	print 'HTML JavaScript Event Call:<br>'."\n";
	print '<textarea cols=80 rows=2>'."\n";
	print 'HCEvent('."'".'EventName'."'".',successFlag);';
	print '</textarea>'."\n";
	print '</tr></td></table></body></html>';
}

sub writeAMAcctParams() {
	open (PARAM_FH, ">$acct/L10HC_AMAcctParams.pl") || &gen_error("Cannot open $acct/L10HC_AMAcctParams.pl at writeAcctParams()");
	print PARAM_FH "\$acctActive  = $acctActive \;\n";
	$t = "(\'".join("\',\'",@contactInfo)."\')";
	print PARAM_FH "\@contactInfo = $t\;\n";
	$t = "(\'".join("\',\'",@userPasswords)."\')";
	print PARAM_FH "\@userPasswords = $t\;\n";
	$t = "(\'".join("\',\'",@userEmails)."\')";
	print PARAM_FH "\@userEmails = $t\;\n";
	$t = "(\'".join("\',\'",@userSesIDs)."\')";
	print PARAM_FH "\@userSesIDs = $t\;\n";
	$t = "(\'".join("\',\'",@userSesIDErrs)."\')";
	print PARAM_FH "\@userSesIDErrs = $t\;\n";
	print PARAM_FH '1;';
	close (PARAM_FH);
}

sub gen_error_int {
	($msg) = @_;
	print header;
	print "$msg";
	exit 0;
}

1;