#!/usr/bin/perl -i

# v3.16 1/1/04

use CGI ':standard';

if(-e "L10HC_Params.pl") {	
	require "L10HC_Params.pl";
	@t = split(/\//,$startDate);
	$startYr = @t[0];
	$startMo = @t[1];
	$startDay = @t[2];
} else { 
	$timeAdj = 0;
	require "L10HC_LIB.pl";
	require "L10HC_LIB3.pl";
	if(param('action') eq "init") {
		&initScript();
	} else {
		&initForm(); 
	}
	exit 0;
}

if(param('action') eq "updateKC") {
	require "L10HC_LIB.pl";
	&updateKC();
	exit 0;
}

if(param('acct') eq '') {
	$acct = '.';
} else {
	$acct = param('acct');
}
$acct = $dataDir.$acct;

if(-e "$acct/L10HC_AcctParams.pl") {
	require "$acct/L10HC_AcctParams.pl";
} elsif(param('action') ne 'init') {
	print header;
	print "res=Err&msg=Invalid Account - ".param('acct');
	exit 0;
}

require "L10HC_LIB.pl";

$repSecs=0;
$repTime="";
$repDate="";

($curMonYr,$curMonMo,$curMonDay) = MondayOfWeek($curWk,$curWkYr);

@MoAbv = ("","Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec");
@MoName = ("","January","Febuary","March","April","May","June","July","August","September","October","November","December");
@DoWAbv = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun");
@DoWName = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday");

if(param('action') eq "getMsgs") {
	&getMsgs();
	exit 0;
}

if(param('action') eq "tempext") {
	require "L10HC_LIB2.pl";
	&archiveExtended();
	print header;
	print "Extended Archived";
	exit 0;
}

if(param('action') eq "initAdmin") {
	&initAdmin();
	exit 0;
} elsif(param('action') eq "auth") {
	print header;
	&authPassword();
	exit 0;
} elsif(param('action') eq "sTD") {
	print header;
	print "sDate=$serMo/$serDay/$serYr&";
	if($serMin<10) {
		$serMin = "0$serMin";
	}
	if($serSec<10) {
		$serSec = "0$serSec";
	}
	print "sTime=$serHr:$serMin:$serSec&";
	exit 0;
} elsif(param('action') eq "pageList") {
	&pageList();
	exit 0;
} elsif(param('action') eq "rTypeList") {
	&rTypeList();
	exit 0;
} elsif(param('action') eq "hotLists") {
	&getHotLists();
	exit 0;
}

if(!$protectStats || &verifyAuth()) {
	if(param('action') eq "summary") {
		&summaryReport();
		exit 0;
	} elsif(param('action') eq "pgsRep") {
		&pagesReport();
		exit 0;
	} elsif(param('action') eq "pgDRep") {
		&pageDetailReport();
		exit 0;
	} elsif(param('action') eq "pasRep") {
		&pathReport();
		exit 0;
	} elsif(param('action') eq "paDRep") {
		&pathReport();
		exit 0;
	} elsif(param('action') eq "period") {
		&periodReport();
		exit 0;
	} elsif(param('action') eq "histRep") {
		&historyReport();
		exit 0;
	} elsif(param('action') eq "refsRep") {
		&referrerReport();
		exit 0;
	} elsif(param('action') eq "ext") {
		&extendedReport();
		exit 0;
	} elsif(param('action') eq "refLinks") {
		&getRefLinks();
		exit 0;
	}
}

if(&verifyAuth()) {
	if(param('action') eq "changeParams") {
		&changeParams();
		exit 0;
	}  elsif(param('action') eq "genPageCode") {
		require "L10HC_LIB3.pl";
		&genPageCode();
		exit 0;		
	}  elsif(param('action') eq "genEventCode") {
		require "L10HC_LIB3.pl";
		&genEventCode();
		exit 0;
	}  elsif(param('action') eq "saveHotLists") {
		&saveHotLists();
		exit 0;
	} elsif(param('action') eq "setCookie") {
		&setCookie();
		exit 0;
	}  elsif(param('action') eq "removeCookie") {
		&removeCookie();
		exit 0;
	}
	
	
}
	print header;
	print '<html><head><title>L10 Hit Counter</title></head><body style="font-family : Arial, Helvetica, sans-serif;">';
	print '<center><b>L10 Hit Counter successfuly installed!</b><br><br><span style="font-size:x-small">Script Sponsors<br><a href="http://www.leveltendesign.com">LevelTen Web Design</a> | <a href="http://www.websitedesignpromotion.org">Website Design &amp; Promotion</a> | <a href="http://www.10minuteflash.com">10Minute Flash</a><br>';
	print '&copy; 2002 <a href="http://www.lorentzconsulting.com">Lorentz Consulting Group, LLC</a> - All Rights Reserved</span>'."\n";
	print "<!-- action=".param('action')." -->\n";
	print '</body></html>';


exit 0;

#####################################################
# Subroutine start
#####################################################

sub getMsgs() {
	print header;
	open (DSTAT_FH, "$acct/L10HC_Hits.dat") || &gen_error("Cannot open $acct/L10HC_Hits.dat at \"Read Today's Stats Data\"");
	@dStat = <DSTAT_FH>;
	close(DSTAT_FH);
	
	open (FILE, "$acct/L10HC_PageL.dat") || &gen_error("Cannot open $acct/L10HC_PageL.dat at \"Read Today's Stats Data\"");
	@pgLFile = <FILE>;
	close(FILE);
	open (FILE, "$acct/L10HC_PageI.dat") || &gen_error("Cannot open $acct/L10HC_PageI.dat at \"Read Today's Stats Data\"");
	@pgIFile = <FILE>;
	close(FILE);

	@sStats = split(/\t/,$dStat[1]);
	@hvStats = split(/\t/,$dStat[4]);
	@hhStats = split(/\t/,$dStat[5]);
	@pStats = (0,0,0,0,0,0,0,0,0);

	$url = &filterPageURL(param('page'));
	if($url eq "") {
		$url = '[Unknown]';
	}
	@res = &bSearch($url,\@pgLFile,1,\@pgIFile,1);
	if($res[0]) {
		$pgID = $res[1]+6;
		chop($dStat[$pgID]);
		@pStats = split(/\t/,$dStat[$pgID]);
	}
	for($i=0;$i<=4;$i++) {
		print "SV$i=$sStats[$i]\&";
		print "SH$i=$sStats[$i+5]\&";
		print "PV$i=$pStats[$i]\&";
		print "PH$i=$pStats[$i+5]\&"; 
	}

	
	if($enableAdminLink) {
		print "adminPath=$reporterURL\&";
	} else {
		print "adminPath=\&";
	}


	($sYr,$sMo,$sDay) = split(/\//,$startDate);
	($curMonYr,$curMonMo,$curMonDay) = &MondayOfWeek($curYr,$curMo,$curDay);
	$DoW = &DayOfWeek($curYr,$curMo,$curDay);
	&setRepTime();
	($rHr,$rMin,$rSec) = split(/:/,$repTime);
	($rSec,$rMod) = split(/ /,$rSec);
	print "SV5=$hvStats[$curHr]\&";
	print "SH5=$hhStats[$curHr]\&";
	print "TD0=$sMo/$sDay\&";
	print "TD1=$sMo/$sDay/".substr($curMonYr,2)."\&";
	print "TD2=$sMo/$sDay/$sYr\&";
	print "TD3=".substr($curYr,2)."\&";
	print "TD4=$curYr\&";
	print "TD5=$curMo\&";
	print "TD6=$MoAbv[$curMo]\&";
	print "TD7=$MoName[$curMo]\&";
	print "TD8=$curMonMo/$curMonDay\&";
	print "TD9=$curMonMo/$curMonDay/".substr($curMonYr,2)."\&";
	print "TD10=$curMonMo/$curMonDay/$curMonYr\&";
	print "TD11=$curMo/$curDay\&";
	print "TD12=$curMo/$curDay/".substr($curYr,2)."\&";
	print "TD13=$curMo/$curDay/$curYr\&";
	print "TD14=$curDay\&";
	print "TD15=$DoWAbv[$DoW]\&";
	print "TD16=$DoWName[$DoW]\&";
	print "TD17=$rHr:$rMin $rMod\&";
	print "TD18=$repTime\&";
	print "TD19=$curHr\&";
	print "TD20=$rHr\&";
	print "TD21=$rMin\&";
	print "TD22=$rSec\&";
	print "TD23=$rMod\&";
	
	
	$i=0;
	foreach (@phrases) {
		print "p$i=$_\&";
		$i++;
	}
	exit 0;
}

sub initAdmin() {
	print header;
	print "res=OK&";
	@cookies = split(/;/,$ENV{'HTTP_COOKIE'});
	$blockBrowser = 0;
	$cookiePW = "";
	foreach (@cookies) {
		($cKey,$cValue) = split(/=/,$_);
# print "$cKey=$cValue&";
		if(($cKey =~ m/L10HC_BB/) && ($cValue eq "1")) {
			$blockBrowser = 1;
		} elsif(($cKey =~ m/L10HC_PW/) && ($cValue ne "")) {
			$cookiePW = $cValue;
			if(! &verifyAuth(1)) {
				$cookiePW = '';
			}
		}
	}

	&authPassword();
	
	print "cDate=$curMo/$curDay/$curYr&";
	print "cTime=$curHr:$curMin:$curSec&";
	@t = split(/\//,$initDate);
	# print "iDate=02/01/2001&";
	print "iDate=$t[1]/$t[2]/$t[0]&";
	if($curMin<10) {
		$curMin = "0$curMin";
	}
	if($curSec<10) {
		$curSec = "0$curSec";
	}	
	print "sDate=$serMo/$serDay/$serYr&";
	if($serMin<10) {
		$serMin = "0$serMin";
	}
	if($serSec<10) {
		$serSec = "0$serSec";
	}
	print "sTime=$serHr:$serMin:$serSec&";
	
	print "timeAdj=$timeAdj&";
	print "kc=$keyCode&";
	print "kcErr=$kcErr&";
	print "kcErrMsg=$kcErrMsg&";
	print "datVer=$datVer&";
	print "rb=$removeBranding&";
	print "blockBrowser=$blockBrowser\&";
	print "PW=$cookiePW\&";
	print "protectStats=$protectStats\&";
	print "adminPath=$reporterURL&";
	print "enableAdminLink=$enableAdminLink\&";
	print "removeHCDisplay=$removeDisplay\&";
	print "reporterURL=$reporterURL\&";
	print "maxRepItems=$maxRepItems&";
	print "siteTitle=$siteTitle&";
	print "indexPage=$indexPage&";
	print "blockIPs=".join(',',@blockIPs)."&";
	foreach $phrase (@phrases) {
		$i++;
		print "p$i=$phrase\&";
	}
	$i=0;
	foreach $phrase (@validDoms) {
		$i++;
		print "vd$i=$phrase\&";
	}
	open (FILE, "L10HC_SE.txt");
	%SEName = ();
	%SEGroups = ();
	$SEMain = '';
	$i = 0;
	foreach (<FILE>) {
		chop($_);
		@t = split(/\t/,$_);
		if($i) {
			$SEName{$t[1]} = '';	
		} else {
			for(;$i<=$#t;$i++) {
				$SEGroups{$t[$i]} = '';
			}
			$i=1;
		}		
	}
	close(FILE);
	foreach $SEN (sort (keys %SEName)) {
		$mf = 0;
		foreach (keys %SEGroups) {			
			if($SEN =~ m/$_/i) {
				if($SEGroups{$_} eq '') {
					$SEMain = "$SEMain$_>,";
				}
				$SEN =~ s/$_//i;
				if($SEN eq '') {
					$SEGroups{$_} = "$SEGroups{$_}Main,";	
				} else {
					$SEN =~ s/^ //;
					$SEGroups{$_} = "$SEGroups{$_}$SEN,";
				}				
				$mf = 1;				
				last;
			}
		}
		if(!$mf && $SEN ne '') {
			$SEMain = "$SEMain$SEN,";
		}			
	}	
	chop($SEMain);
	print "SEM=$SEMain&";
	$i=0;
	foreach (keys %SEGroups) {
		$l = $_;
		$l =~ s/ /_/g;
		chop($SEGroups{$_});
		print "SEM$l=$SEGroups{$_}&";
		print "SEM_$i=$l&";
		print "SEMV_$i=$_&";
		$i++;
	}


}

sub getHotLists () {
	open (FILE, "$acct/L10HC_HotLists.dat") || &gen_error("Cannot open $acct/L10HC_HotLists.dat at \"Read Today's Stats Data\"");
	@t = <FILE>;
	close(FILE);
	$domI = 0;
	$urlI = 0;
	$kwI = 0;
	$sekwI = 0;
	$rtI = 0;
	$pgI = 0;
	$paI = 0;
	print header;
	foreach(@t) {
		chop($_);
		@s = split(/\t/,$_);
		if($s[0] eq 'D') {
			print "DC$domI=$s[1]&DL$domI=$s[2]&";
			$domI++;
		} elsif($s[0] eq 'U') {
			print "UC$urlI=$s[1]&UL$urlI=$s[2]&";
			$urlI++;
		} elsif($s[0] eq 'K') {
			print "KC$kwI=$s[1]&KL$kwI=$s[2]&";
			$kwI++;
		} elsif($s[0] eq 'SK') {
			print "SKC$sekwI=$s[1]&SKL$sekwI=$s[2]&";
			$sekwI++;
		} elsif($s[0] eq 'T') {
			print "TC$rtI=$s[1]&TL$rtI=$s[2]&";
			$rtI++;
		} elsif($s[0] eq 'Pg') {
			print "PgC$pgI=$s[1]&PgL$pgI=$s[2]&";
			$pgI++;
		} elsif($s[0] eq 'Pa') {
			print "PaC$paI=$s[1]&PaL$paI=$s[2]&";
			$paI++;
		}
		
	}
	print "D=$domI&U=$urlI&K=$kwI&SK=$sekwI&T=$rtI&Pg=$pgI&Pa=$paI";
}

sub saveHotLists() {
	@types = ('D','U','K','SK','T','Pg','Pa');
	open (FILE, ">$acct/L10HC_HotLists.dat") || &gen_error("Cannot open >$acct/L10HC_HotLists.dat at \"saveHotLists()\"");
	foreach $type (@types) {
		for($i=0;$i<20;$i++) {
			if(param($type.'C'.$i) ne '') {
				print FILE "$type\t".param($type.'C'.$i)."\t".param($type.'L'.$i)."\n";
			}
		}
	}
	close(FILE);
	&getHotLists();
}

sub authPassword() {
	if($acctManager) {
		require "$acct/L10HC_AMAcctParams.pl";
		$auth=0;
		if(!$acctActive) {
			print "res=Err&code=IA&msg=This account is currently inactive.&";
		}		
		for($i=0;$i<=$#userPasswords;$i++) {	
			if(($userPasswords[$i] eq param('pw')) || ($userPasswords[$i] eq $cookiePW)) {
				$userSesIDs[$i] ++;
				print "sesID=$userSesIDs[$i]&";
				require "L10HC_LIB3.pl";
				&writeAMAcctParams();
				$auth=1;
				last;
			}
		}
		print "auth=$auth&"; 
	} elsif ((param('pw') eq $password) || ($cookiePW eq $password)) {
		print "auth=1&";
	} else {
		print "auth=0&"; 
	}

}

sub verifyAuth() {
	($ignoreSesID) = @_;
	if($acctManager) {
		require "$acct/L10HC_AMAcctParams.pl";
		$found = 0;
		for($i=0;$i<=$#userPasswords;$i++) {
			if(($userPasswords[$i] eq param('pw')) || ($userPasswords[$i] eq $cookiePW)) {
				if(($ignoreSesID) || ($userSesIDs[$i] == param('sesID'))) {
					return 1;	
				} else {
					print header;
					print "res=Err&code=IS&msg=The session ID is no longer valid.";
					$userSesIDErrs[$i] ++;
					require "L10HC_LIB3.pl";
					&writeAMAcctParams();
					exit 0;
				}
			}
		}
		return 0;
	} elsif ((param('pw') eq $password) || ($cookiePW eq $password)) {
		return 1;
	} else {
		return 0;
	}
}

sub pageList() {
	open (DSTAT_FH, "$acct/L10HC_PageL.dat") || &gen_error("Cannot open $acct/L10HC_PageL.dat at \"Read Today's Stats Data\"");
	@dStat = <DSTAT_FH>;
	close(DSTAT_FH);
	print header;
	$j = 0;
	foreach (@dStat) {
		chop($_);
		print "p$j=$_&";
		$j++;
	}
	print "Count=$j";
}

sub rTypeList() {
	open (DSTAT_FH, "$acct/L10HC_Archive/rTypes/rTypeL.dat") || &gen_error("Cannot open $acct/L10HC_Archive/rTypes/rTypeL.dat at \"Read Today's Stats Data\"");
	@dStat = <DSTAT_FH>;
	close(DSTAT_FH);
	print header;
	$j = 0;
	foreach (@dStat) {
		chop($_);
		print "r$j=$_&";
		$j++;
	}
	print "Count=$j";
}

sub summaryReport() {
	unless(&lock_stats()) {
		print header;
		print "res=Err&msg=File lock timeout exceeded";
		exit 0;
	}
	open (DSTAT_FH, "$acct/L10HC_Hits.dat") || &gen_error("Cannot open $acct/L10HC_Hits.dat at \"Read Today's Stats Data\"");
	@dStat = <DSTAT_FH>;
	close(DSTAT_FH);
	
	if($dStat[0] ne "$dateStamp\n") {
		&log_event("Stats archived by time.");
		require "L10HC_LIB2.pl";
		&archiveStats();
	}
	&unlock_stats();

	open (DSTAT_FH, "$acct/L10HC_Archive/Hits_byPeriod.dat") || &gen_error("$acct/L10HC_Archive/Hits_byPeriod.dat at \"Read Today's Stats Data\"");
	@bStat = <DSTAT_FH>;
	close(DSTAT_FH);
	
	print header;

	($sYr,$sMo,$sDay) = split(/\//,$startDate);
	$AD = &DeltaDays($sYr,$sMo,$sDay,$curYr,$curMo,$curDay);
	if($sYr < $curYr) {
		$YD = &DeltaDays($curYr,1,1,$curYr,$curMo,$curDay);
	} else {
		$YD = &DeltaDays($sYr,$sMo,$sDay,$curYr,$curMo,$curDay);
	}
	if($sMo < $curMo) {
		$MD = &DeltaDays($curYr,$curMo,1,$curYr,$curMo,$curDay);
	} else {
		$MD = &DeltaDays($sYr,$sMo,$sDay,$curYr,$curMo,$curDay);
	}
	($curMonYr,$curMonMo,$curMonDay) = &MondayOfWeek($curYr,$curMo,$curDay);
	($sMonYr,$sMonMo,$sMonDay) = &MondayOfWeek($sYr,$sMo,$sDay);
	if($sWk < $curWk) {
		$WD = DeltaDays($curMonYr,$curMonMo,$curMonDay,$curYr,$curMo,$curDay);
	} else {
		$WD = DeltaDays($sYr,$sMo,$sDay,$curYr,$curMo,$curDay);
	}
	
	@pStats = split(/\t/,$dStat[1]);
	
	&setRepTime();
	print "Run=$repDate $repTime$siteTitle&";
	print "SD=$startDate\&";
	print "Date=$repDate\&";
	print "Time=$repTime\&";
	print "Secs=$repSecs\&";
	print "DoW=".&DayOfWeek($curYr,$curMo,$curDay)."&";
	print "AV=$pStats[0]\&";
	print "AH=$pStats[5]\&";
	print "AD=$AD\&";
	print "YV=$pStats[1]\&";
	print "YH=$pStats[6]\&";
	print "YD=$YD\&";
	print "MV=$pStats[2]\&";
	print "MH=$pStats[7]\&";
	print "MD=$MD\&";
	print "WV=$pStats[3]\&";
	print "WH=$pStats[8]\&";
	print "WD=$WD\&";
	print "DV=$pStats[4]\&";
	print "DH=$pStats[9]\&";
	
	@pStats = split(/\t/,$bStat[3]);
	@pStats2 = split(/\t/,$bStat[4]);
	@pStats3 = split(/\t/,$dStat[4]);
	@pStats4 = split(/\t/,$dStat[5]);
	for($i=0;$i<24;$i++) {
		print "HVA$i=$pStats[$i]\&";
		print "HHA$i=$pStats2[$i]\&";
		print "HV$i=$pStats3[$i]\&";
		print "HH$i=$pStats4[$i]\&";
	}
	print "THV=$pStats3[$curHr]\&";
	print "THH=$pStats4[$curHr]\&";
	@pStats = split(/\t/,$bStat[10]);
	@pStats2 = split(/\t/,$bStat[11]);
	@pStats3 = split(/\t/,$bStat[12]);
	@pStats4 = split(/\t/,$bStat[13]);
	for($i=0;$i<7;$i++) {
		print "DVA$i=$pStats[$i]\&";
		print "DHA$i=$pStats2[$i]\&";
		print "DV$i=$pStats3[$i]\&";
		print "DH$i=$pStats4[$i]\&";
	}
	print "Run=$repDate $repTime$siteTitle&";
	
	
	
}



sub pagesReport() {
	if(param('fft') ne '') {
		&pagesReportF();
		return;
	}
	&updateNav();
	my ($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();
	
	$startDate = "$sMo/$sDay/$sYr";
	$pCount = 0;
	
	@sStats = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
	@pStats = ();
	
	($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
	$daysFound = 0;
	for($i=0;$i<$dayCnt;$i++) {
		($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,1);
		@file = ();
		
		if(-e &getFileDateStr('Hits','D',$sYr,$sMo,$sDay)) {
			open (FILE, &getFileDateStr('Hits','D',$sYr,$sMo,$sDay)) || &retNoData();
			@file = <FILE>;
			close(FILE);
			$daysFound ++;
		} else {
			next;
		}
		@t = split(/\t/,$file[0]);
		for($j=0;$j<16;$j++) {
			$sStats[$j] += $t[$j];
		}
		$l = 0;
		for($j=1;$j<=$#file;$j+=5) {
			@t = split(/\t/,$file[$j]);
			if($l > $#pStats) {
				push(@pStats,[ (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ]);
				$pCount ++;
			}
			for($k=0;$k<16;$k++) {
				$pStats[$l][$k] += $t[$k];
			}
			$l++;
		}
		
	}
	
	$endDate="$sMo/$sDay/$sYr";
	if(param('format') > 0) {
		if($daysFound == 0) {
			&retNoData()
		} else {
			open (FILE, "$acct/L10HC_PageL.dat") || &retNoData();
			@pageList = <FILE>;
			close(FILE);
			&setRepTime();
			$iD = "\t";
			$sD = "";
			$eD = "\n";
			$lb = "";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>Page Report</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 8pt;}</style></header><body><table border=1 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td> ';
				$eD = ' </td></tr>'."\n";
				$lb = '<br>';
			}
			print $sD."Page Report".$eD;
			print $sD."Run Time: $repDate $repTime$siteTitle".$eD;
			print $sD."Date Range: $startDate-$endDate".$eD;
			print $sD.&getFromFilterStr().$eD;
			print $sD.$eD;
			print $sD."Page".$iD."Page Hits".$iD."Entries$lb All".$iD."Entries$lb Uniques".$iD."Entries$lb New".$iD."Exits$lb All".$iD."Exits$lb Uniques".$iD."Exits$lb New".$iD."Conv.$lb All".$iD."Conv.$lb Uniques".$iD."Conv.$lb New".$iD."Success$lb All".$iD."Success$lb Uniques".$iD."Success$lb New".$iD."Active Sessions".$iD."Reloads".$iD."Total Time".$iD."Average Time".$eD;
			print $sD."All Pages".$iD.$sStats[3].$iD.$sStats[0].$iD.$sStats[1].$iD.$sStats[2].$iD.$sStats[5].$iD.$sStats[6].$iD.$sStats[7].$iD.$sStats[8].$iD.$sStats[9].$iD.$sStats[10].$iD.$sStats[11].$iD.$sStats[12].$iD.$sStats[13].$iD.$sStats[4].$iD.$sStats[14].$iD.$sStats[15].$iD.( (($sStats[3]-$sStats[4]-$sStats[5]) > 0) ? &roundNum($sStats[15]/($sStats[3]-$sStats[4]-$sStats[5]),1) : 0).$eD;
			for($i=0;$i<=$#pStats;$i++) {
				if($pStats[$i][3] > 0) {
					chop($pageList[$i]);
			 		print $sD.$pageList[$i].$iD.$pStats[$i][3].$iD.$pStats[$i][0].$iD.$pStats[$i][1].$iD.$pStats[$i][2].$iD.$pStats[$i][5].$iD.$pStats[$i][6].$iD.$pStats[$i][7].$iD.$pStats[$i][8].$iD.$pStats[$i][9].$iD.$pStats[$i][10].$iD.$pStats[$i][11].$iD.$pStats[$i][12].$iD.$pStats[$i][13].$iD.$pStats[$i][4].$iD.$pStats[$i][14].$iD.$pStats[$i][15].$iD.( (($pStats[$i][3]-$pStats[$i][4]-$pStats[$i][5]) > 0) ? &roundNum($pStats[$i][15]/($pStats[$i][3]-$pStats[$i][4]-$pStats[$i][5]),1) : 0).$eD;
				}
			}
			print $sD.$eD;
			if(param('format') ne '1') {
				print '</table></body></html>';
			}
		}
	} else {
		if($daysFound == 0) {
			&retNoData()
		} else {
			&setRepTime();
			print header;
			print "res=OK&TR=$total&";
			print "Date=$startDate - $endDate&";
			print "Run=$repDate $repTime$siteTitle&";
			print "AS=$sStats[0]&BS=$sStats[1]&CS=$sStats[2]&DS=$sStats[3]&ES=$sStats[4]&FS=$sStats[5]&GS=$sStats[6]&HS=$sStats[7]&IS=$sStats[8]&JS=$sStats[9]&KS=$sStats[10]&LS=$sStats[11]&MS=$sStats[12]&NS=$sStats[13]&OS=$sStats[14]&PS=$sStats[15]&";
			
			@pStats = sort { $a[3] <=> $b[3] } @pStats;
			$iMax = ($#pStats < $maxRepItems) ? $#pStats : $maxRepItems;
			
			for($i=0;$i<=$iMax;$i++) {
				if($pStats[$i][3] > 0) {
					print "X$i=$i&A$i=$pStats[$i][0]&B$i=$pStats[$i][1]&C$i=$pStats[$i][2]&D$i=$pStats[$i][3]&E$i=$pStats[$i][4]&F$i=$pStats[$i][5]&G$i=$pStats[$i][6]&H$i=$pStats[$i][7]&I$i=$pStats[$i][8]&J$i=$pStats[$i][9]&K$i=$pStats[$i][10]&L$i=$pStats[$i][11]&M$i=$pStats[$i][12]&N$i=$pStats[$i][13]&O$i=$pStats[$i][14]&P$i=$pStats[$i][15]&";				
				}
			}
			print "pCount=$pCount";
		}
	}

}

sub pagesReportF() {
	&updateNav();
	
	my ($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();
	
	$startDate = "$sMo/$sDay/$sYr";
	$pCount = 0;
	
	@totals = (0,0,0);
	@totals2 = (0,0,0);
	%pStats = ();
	%pRStats = ();
	$rFileName = 'Doms';
	$qRef = param('ff');
	if($qRef eq '[No Referrer]') {
		$qRef = '';
	}
	if(param('fft') eq 'URL') {
		$rFileName = 'Refs';
	} elsif(param('fft') eq 'SE') {
		$rFileName = 'SEs';
	} elsif(param('fft') eq 'SEKW') {
		$rFileName = 'SEKWs';
	} elsif(param('fft') eq 'KW') {
		$rFileName = 'KWs';
	} elsif(param('fft') eq 'RT') {
		$rFileName = 'rTypes';
		$qRef = &getRTypeID(param('ff'));
	}
	
	($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
	$daysFound = 0;
	for($i=0;$i<$dayCnt;$i++) {
		($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,1);
		@dFile = ();
		@refLFile = ();
		@refIFile = ();
		@refIDs = ();
		if(-e &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) {
			open (FILE, &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) || &retNoData();
			@refLFile = <FILE>;
			close(FILE);
			
		} else {
			next;
		}
		if($qRef eq '_') {
			if(-e &getFileDateStr('pgRefs','IbPg',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr('pgRefs','IbPg',$sYr,$sMo,$sDay)) || &retNoData();
				@dFile = <FILE>;
				close(FILE);
				$daysFound ++;
			} else {
				next;
			}

		} else {
			if(-e &getFileDateStr($rFileName,'I',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr($rFileName,'I',$sYr,$sMo,$sDay)) || &retNoData();
				@refIFile = <FILE>;
				close(FILE);
				$daysFound ++;
			} else {
				next;
			}
			
			@res = &bSearch($qRef,\@refLFile,1,\@refIFile,1,1);

			if($res[0]) {
				for($j=$res[1];$j<=$res[2];$j++) {
					push(@refIDs,$refIFile[$j]);
				}
				if(-e &getFileDateStr('pgRefs','IbR',$sYr,$sMo,$sDay)) {
					open (FILE, &getFileDateStr('pgRefs','IbR',$sYr,$sMo,$sDay)) || &retNoData();
					@dFile = <FILE>;
					close(FILE);

				} else {
					next;
				}
			} else {
				next;
			}
		}

		if($qRef eq '_') {
			$pgID = 0;
			if((param('fft') eq 'SE') || (param('fft') eq 'KW') || (param('fft') eq 'SEKW')) {
				$removeStr = '';
				if(param('fft') eq 'SEKW') {
					$removeStr = ' - ';
				}
				for($j=0;$j<=$#dFile;$j+=4) {
					chop($dFile[$j]);
					chop($dFile[$j+1]);
					chop($dFile[$j+2]);
					chop($dFile[$j+3]);
					@ta = split(/\t/,$dFile[$j]);
					@tb = split(/\t/,$dFile[$j+1]);
					@tc = split(/\t/,$dFile[$j+2]);
					@td = split(/\t/,$dFile[$j+3]);
					for($k=0;$k<=$#ta;$k++) {
						$r = $refLFile[$ta[$k]];
						chop($r);
						if($r eq $removeStr) {
							$totals2[0] += $tb[$k];
							$totals2[1] += $tc[$k];
							$totals2[2] += $td[$k];
							next;
						}
						if(exists $pStats{$pgID}) {
							$pStats{$pgID}[0] += $tb[$k];
							$pStats{$pgID}[1] += $tc[$k];
							$pStats{$pgID}[2] += $td[$k];
							if(exists $pRStats{$pgID}{$r}) {
								$pRStats{$pgID}{$r}[0] += $tb[$k];
								$pRStats{$pgID}{$r}[1] += $tc[$k];
								$pRStats{$pgID}{$r}[2] += $td[$k];
							} else {
								$pRStats{$pgID}{$r} = [ ($tb[$k],$tc[$k],$td[$k]) ]
							}
						} else {
							$pStats{$pgID} = [ ($tb[$k],$tc[$k],$td[$k]) ];
							$pRStats{$pgID}{$r} = [ ($tb[$k],$tc[$k],$td[$k]) ]
						} 
						$totals[0] += $tb[$k];
						$totals[1] += $tc[$k];
						$totals[2] += $td[$k];
					}	

					$pgID ++;

				}
				$totals2[0] += $totals[0];
				$totals2[1] += $totals[1];
				$totals2[2] += $totals[2];
			} else {
				for($j=0;$j<=$#dFile;$j+=4) {
					chop($dFile[$j]);
					chop($dFile[$j+1]);
					chop($dFile[$j+2]);
					chop($dFile[$j+3]);
					@ta = split(/\t/,$dFile[$j]);
					@tb = split(/\t/,$dFile[$j+1]);
					@tc = split(/\t/,$dFile[$j+2]);
					@td = split(/\t/,$dFile[$j+3]);
					for($k=0;$k<=$#ta;$k++) {
						$r = $refLFile[$ta[$k]];
						chop($r);
						if(exists $pStats{$pgID}) {
							$pStats{$pgID}[0] += $tb[$k];
							$pStats{$pgID}[1] += $tc[$k];
							$pStats{$pgID}[2] += $td[$k];
							if(exists $pRStats{$pgID}{$r}) {
								$pRStats{$pgID}{$r}[0] += $tb[$k];
								$pRStats{$pgID}{$r}[1] += $tc[$k];
								$pRStats{$pgID}{$r}[2] += $td[$k];
							} else {
								$pRStats{$pgID}{$r} = [ ($tb[$k],$tc[$k],$td[$k]) ]
							}
						} else {
							$pStats{$pgID} = [ ($tb[$k],$tc[$k],$td[$k]) ];
							$pRStats{$pgID}{$r} = [ ($tb[$k],$tc[$k],$td[$k]) ]
						} 
						$totals[0] += $tb[$k];
						$totals[1] += $tc[$k];
						$totals[2] += $td[$k];
					}				

					$pgID ++;
				}
			}
		} else {
			for($j=0;$j<=$#refIDs;$j++) {
				$rI = $refIDs[$j] * 4;
				chop($dFile[$rI]);
				chop($dFile[$rI+1]);
				chop($dFile[$rI+2]);
				chop($dFile[$rI+3]);
				@ta = split(/\t/,$dFile[$rI]);
				@tb = split(/\t/,$dFile[$rI+1]);
				@tc = split(/\t/,$dFile[$rI+2]);
				@td = split(/\t/,$dFile[$rI+3]);
				for($k=0;$k<=$#ta;$k++) {
					if(exists $pStats{$ta[$k]}) {
						$pStats{$ta[$k]}[0] += $tb[$k];
						$pStats{$ta[$k]}[1] += $tc[$k];
						$pStats{$ta[$k]}[2] += $td[$k];
					} else {
						$pStats{$ta[$k]} = [ ($tb[$k],$tc[$k],$td[$k]) ];
					} 
					$totals[0] += $tb[$k];
					$totals[1] += $tc[$k];
					$totals[2] += $td[$k];
				}
			}
		}

		
	}
	
	$endDate="$sMo/$sDay/$sYr";
	
	if((param('fft') eq 'Dom') || (param('fft') eq 'URL') || (param('fft') eq 'RT')) {
		$rStr = '[No Referrer]';
		if((param('fft') eq 'RT')) {
			$rStr = "[Default]";
		}
		foreach $p (keys %pRStats) {
			if(exists $pRStats{$p}{''}) {
				$pRStats{$p}{$rStr} = [ ($pRStats{$p}{''}[0],$pRStats{$p}{''}[1],$pRStats{$p}{''}[2]) ];
				delete $pRStats{$p}{''};
			}
		}
	}
	
	if(param('format') > 0) {
		if($daysFound == 0) {
			&retNoData()
		} else {
			open (FILE, "$acct/L10HC_PageL.dat") || &retNoData();
			@pageList = <FILE>;
			close(FILE);
			&setRepTime();
			$iD = "\t";
			$sD = "";
			$sD2 = "";
			$eD = "\n";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>Page Report</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 8pt;}</style></header><body><table border=1 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td>';
				$sD2 = ' <tr bgcolor=#E8E8FF><td> ';
				$eD = ' </td></tr>'."\n";
			}
			print $sD."Page Report".$eD;
			print $sD."Run Time: $repDate $repTime$siteTitle".$eD;
			print $sD."Date Range: $startDate-$endDate".$eD;
			print $sD.&getFromFilterStr().$eD;
			print $sD.$eD;			
			print $sD."Page".$iD."Count".$iD."Conv.".$iD."Succ.".$eD;
			foreach $p (sort {$pStats{$b}[0] <=> $pStats{$a}[0]} (keys %pStats)) {
				print $sD.$pageList[$p].$iD.$pStats{$p}[0].$iD.$pStats{$p}[1].$iD.$pStats{$p}[2].$eD;
				foreach $r (sort {$pRStats{$p}{$b}[0] <=> $pRStats{$p}{$a}[0]} (keys %{$pRStats{$p}})) {
					$rl = $r;
					$rl =~ s/%([a-fA-F0-9]{2})/chr(hex($1))/ge;
					print $sD2."> $rl".$iD.$pRStats{$p}{$r}[0].$iD.$pRStats{$p}{$r}[1].$iD.$pRStats{$p}{$r}[2].$eD;
				}
			}
			print $sD.$eD;
			print $sD."".$iD.$totals[0].$iD.$totals[1].$iD.$totals[2].$eD; 
			if($totals2[0] > 0) {
				print $sD."".$iD.$totals2[0].$iD.$totals2[1].$iD.$totals2[2].$eD
			}
		}
	} else {
		if($daysFound == 0) {
			&retNoData()
		} else {
			&setRepTime();
			print header;
			print "res=OK&";
			print "Date=$startDate - $endDate&";
			print "Run=$repDate $repTime$siteTitle&";
			print "BS=$totals[0]&JS=$totals[1]&MS=$totals[2]&";
			print "BT=$totals2[0]&JT=$totals2[1]&MT=$totals2[2]&";
			$i = 0;
			if(param('ff') eq '_') {
				foreach $p (sort {$pStats{$b}[0] <=> $pStats{$a}[0]} (keys %pStats)) {
					foreach $r (keys %{$pRStats{$p}}) {
						print "X$i=$p&Y$i=$r&B$i=$pRStats{$p}{$r}[0]&J$i=$pRStats{$p}{$r}[1]&M$i=$pRStats{$p}{$r}[2]&";
						$i++;
						if($i>=$maxRepItems) { last; }
					}
				}
			} else {
				foreach $p (sort {$pStats{$b}[0] <=> $pStats{$a}[0]} (keys %pStats)) {
					print "X$i=$p&B$i=$pStats{$p}[0]&J$i=$pStats{$p}[1]&M$i=$pStats{$p}[2]&";
					$i++;
					if($i>=$maxRepItems) { last; }
				}
			}
			print "pCount=$i";
		}
	}

}

sub pageDetailReport() {
	&updateNav();
	my ($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();
	
	$startDate = "$sMo/$sDay/$sYr";
	$pgIndex = -1;

	
	$url = &filterPageURL(param('pg'));
	
	open (FILE, "$acct/L10HC_PageL.dat") || &gen_error("Cannot open $acct/L10HC_PageL.dat at \"Read Today's Stats Data\"");
	@pageList = <FILE>;
	close(FILE);
	
	open (FILE, "$acct/L10HC_PageI.dat") || &gen_error("Cannot open $acct/L10HC_PageI.dat at \"Read Today's Stats Data\"");
	@pageIndexes = <FILE>;
	close(FILE);
	
	if(length($url) == 0) {
		@res = (1,1,1);
	} else {
		@res = &bSearch($url,\@pageList,1,\@pageIndexes,1);
	}
	

	
	
	if(!$res[0]) {
		print header;
		print "res=Err&msg=Page not found: $url";
		exit 0;
	}
	$pgIndex = $res[1]*5+1;
	$pgID = $res[1];
	
	$pCount = $#pageList+1;
	
	@sStats = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
	@pStats = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
	%outLinks = ();
	%inLinks = ();
	
	($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
	$daysFound = 0;
	for($i=0;$i<$dayCnt;$i++) {
		($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,1);
		@file = ();
		
		if(-e &getFileDateStr('Hits','D',$sYr,$sMo,$sDay)) {
			open (FILE, &getFileDateStr('Hits','D',$sYr,$sMo,$sDay)) || &retNoData();
			@file = <FILE>;
			close(FILE);
			$daysFound ++;
		} else {
			next;
		}

		@t = split(/\t/,$file[0]);
		for($j=0;$j<=15;$j++) {
			$sStats[$j] += $t[$j];
		}
		if($#file >= $pgIndex) {
			@t = split(/\t/,$file[$pgIndex]);
			for($j=0;$j<=15;$j++) {
				$pStats[$j] += $t[$j];
			}
			chop($file[$pgIndex+1]);
			chop($file[$pgIndex+2]);
			@t1 = split(/\t/,$file[$pgIndex+1]);
			@t2 = split(/\t/,$file[$pgIndex+2]);
			for($j=0;$j<=$#t1;$j++) {
				$inLinks{$t1[$j]} += $t2[$j];
			}
			chop($file[$pgIndex+3]);
			chop($file[$pgIndex+4]);
			@t1 = split(/\t/,$file[$pgIndex+3]);
			@t2 = split(/\t/,$file[$pgIndex+4]);
			for($j=0;$j<=$#t1;$j++) {
				$outLinks{$t1[$j]} += $t2[$j];
			}
			
		}
		
		
	}
	
	$endDate="$sMo/$sDay/$sYr";
	if(param('format') > 0) {
		if($daysFound == 0) {
			&retNoData()
		} else {
			&setRepTime();
			foreach(@pageList) {
				chop($_);
			}
			
			$iD = "\t";
			$sD = "";
			$eD = "\n";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>Page Details</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 8pt;}</style></header><body><table border=1 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td> ';
				$eD = ' </td></tr>'."\n";
			}
			print $sD."Page Details".$eD;
			print $sD."Run Time: $repDate $repTime$siteTitle".$eD;
			print $sD."Date Range: $startDate-$endDate".$eD;
			print $sD."Page: ".$url.$eD;
			print $sD.$eD;
			print $sD."".$iD."This Page".$iD."All Pages".$eD;
			print $sD."Page Hits".$iD.$pStats[3].$iD.$sStats[3].$eD;
			print $sD."Entries - All Sessions".$iD.$pStats[0].$iD.$sStats[0].$eD;
			print $sD."Entries - All Uniques".$iD.$pStats[1].$iD.$sStats[1].$eD;
			print $sD."Entries - New Visitors".$iD.$pStats[2].$iD.$sStats[2].$eD;
			print $sD."Conversions - All Sessions".$iD.($pStats[0]-$pStats[8]).$iD.($sStats[0]-$sStats[8]).$eD;
			print $sD."Conversions - All Uniques".$iD.($pStats[1]-$pStats[9]).$iD.($sStats[1]-$sStats[9]).$eD;
			print $sD."Conversions - New Visitors".$iD.($pStats[2]-$pStats[10]).$iD.($sStats[2]-$sStats[10]).$eD;
			print $sD."Successes - All Sessions".$iD.$pStats[11].$iD.$sStats[11].$eD;
			print $sD."Successes - All Uniques".$iD.$pStats[12].$iD.$sStats[12].$eD;
			print $sD."Successes - New Visitors".$iD.$pStats[13].$iD.$sStats[13].$eD;
			print $sD."Exits - All Sessions".$iD.$pStats[5].$iD.$sStats[5].$eD;
			print $sD."Exits - All Uniques".$iD.$pStats[6].$iD.$sStats[6].$eD;
			print $sD."Exits - New Visitors".$iD.$pStats[7].$iD.$sStats[7].$eD;
			print $sD."Bounces - All Sessions".$iD.$pStats[8].$iD.$sStats[8].$eD;
			print $sD."Bounces - All Uniques".$iD.$pStats[9].$iD.$sStats[9].$eD;
			print $sD."Bounces - New Visitors".$iD.$pStats[10].$iD.$sStats[10].$eD;
			print $sD."Active Sessions".$iD.$pStats[4].$iD.$sStats[4].$eD;
			print $sD."Reloads".$iD.$pStats[14].$iD.$sStats[14].$eD;
			print $sD."Total Time".$iD.$pStats[15].$iD.$sStats[15].$eD;
			print $sD."Average Time".$iD.( (($pStats[3]-$pStats[4]-$pStats[5]) > 0) ? &roundNum($pStats[15]/($pStats[3]-$pStats[4]-$pStats[5]),1) : 0).$iD.( (($sStats[3]-$sStats[4]-$sStats[5]) > 0) ? &roundNum($sStats[15]/($sStats[3]-$sStats[4]-$sStats[5]),1) : 0).$eD;
			
			print $sD."<b>Inbound Links</b>".$eD;			
			foreach (sort {$inLinks{$b} <=> $inLinks{$a}} (keys %inLinks)) {
				print $sD.$pageList[$_].$iD.$inLinks{$_}.$eD;
			}
			print $sD."<b>Outbound Links</b>".$eD;	
			foreach (sort {$outLinks{$b} <=> $outLinks{$a}} (keys %outLinks)) {
				print $sD.$pageList[$_].$iD.$outLinks{$_}.$eD;
			}
			print $sD.$eD;
			if(param('format') ne '1') {
				print '</table></body></html>';
			}			
		}
	} else {
		if($daysFound == 0) {
			&retNoData()
		} else {
			&setRepTime();
			print header;
			print "res=OK&TR=$total&";
			print "Date=$startDate - $endDate&";
			print "Run=$repDate $repTime$siteTitle&";
			print "AS=$sStats[0]&BS=$sStats[1]&CS=$sStats[2]&DS=$sStats[3]&ES=$sStats[4]&FS=$sStats[5]&GS=$sStats[6]&HS=$sStats[7]&IS=$sStats[8]&JS=$sStats[9]&KS=$sStats[10]&LS=$sStats[11]&MS=$sStats[12]&NS=$sStats[13]&OS=$sStats[14]&PS=$sStats[15]&";
			print "AP=$pStats[0]&BP=$pStats[1]&CP=$pStats[2]&DP=$pStats[3]&EP=$pStats[4]&FP=$pStats[5]&GP=$pStats[6]&HP=$pStats[7]&IP=$pStats[8]&JP=$pStats[9]&KP=$pStats[10]&LP=$pStats[11]&MP=$pStats[12]&NP=$pStats[13]&OP=$pStats[14]&PP=$pStats[15]&";
			$i = 0;
			foreach (sort {$outLinks{$b} <=> $outLinks{$a}} (keys %outLinks)) {
				print "OI$i=$_&OC$i=$outLinks{$_}&";
				$i++;
			}
			$i = 0;
			foreach (sort {$inLinks{$b} <=> $inLinks{$a}} (keys %inLinks)) {
				print "II$i=$_&IC$i=$inLinks{$_}&";
				$i++;
			}
			print "pCount=$pCount&pgID=$pgID&pg=$pageList[$pgID]";
		}
	}

}

sub pathReport() {
	if(param('fft') ne '') {
		&pathReportF();
		return;
	}

	&updateNav();
	my ($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();
	
	$startDate = "$sMo/$sDay/$sYr";
	$pCount = 0;
	
	@totals = (0,0,0);
	%pCnt = ();
	%pTime = ();
	%pTypes = ();
	
	@pathList = ();
	@pathData = ();
	@pathIndexes = ();
	
	($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
	$daysFound = 0;
	for($i=0;$i<$dayCnt;$i++) {
		($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,1);
		@file = ();
		
		if(-e &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) {
			open (FILE, &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) || &retNoData();
			@pathList = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr('Paths','D',$sYr,$sMo,$sDay)) || &retNoData();
			@pathData = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr('Paths','I',$sYr,$sMo,$sDay)) || &retNoData();
			@pathIndexes = <FILE>;
			close(FILE);
			$daysFound ++;
		} else {
			next;
		}
		
		if(param('Pa') ne '') {
			$pa = param('Pa');
			@res = &bSearch(param('Pa'),\@pathList,1,\@pathIndexes,1);
			if($res[0]) {
				$j = $res[1];
				chop($pathData[$j]);
				@t = split(/\t/,$pathData[$j]);
				if(exists $pCnt{$pa}) {
					$pCnt{$pa}[0] += $t[0];
					$pCnt{$pa}[1] += $t[1];
					$pCnt{$pa}[2] += $t[2];
				} else {
					$pCnt{$pa} = [ ($t[0],$t[1],$t[2]) ];
					$pTypes{$pa} = "".(($pa =~ m/\,/) ? C : B).(($pa =~ m/\*/) ? S : N);
				}
				if(($t[3] > 0) && (exists $pTime{$pa})) {
					for($k=0;$k<=$#t;$k++) {
						$pTime{$pa}[$k] += $t[$k+3];
					}
				} elsif($t[1] > 0) {
					shift(@t);
					shift(@t);
					shift(@t);
					$pTime{$pa} = [ @t ];
				} else {
					$pTime{$pa} = [ (0) ];
				}
				$totals[0] += $t[0];
				$totals[1] += $t[1];
				$totals[2] += $t[2];
			}
			
			
		} else {
		
			for($j=0;$j<=$#pathList;$j++) {
				chop($pathList[$j]);
				chop($pathData[$j]);
				@t = split(/\t/,$pathData[$j]);
				if(exists $pCnt{$pathList[$j]}) {
					$pCnt{$pathList[$j]}[0] += $t[0];
					$pCnt{$pathList[$j]}[1] += $t[1];
					$pCnt{$pathList[$j]}[2] += $t[2];
				} else {
					$pCnt{$pathList[$j]} = [ ($t[0],$t[1],$t[2]) ];
					$pTypes{$pathList[$j]} = "".(($pathList[$j] =~ m/\,/) ? C : B).(($pathList[$j] =~ m/\*/) ? S : N);
				}
				$totals[0] += $t[0];
				$totals[1] += $t[1];
				$totals[2] += $t[2];
				if(($t[3] > 0) && (exists $pTime{$pathList[$j]})) {
					for($k=0;$k<=$#t;$k++) {
						$pTime{$p}[$k] += $t[$k+3];
					}
				} elsif($t[1] > 0) {
					shift(@t);
					shift(@t);
					shift(@t);
					$pTime{$pathList[$j]} = [ @t ];
				} else {
					$pTime{$pathList[$j]} = [ (0) ];
				}
			}
		}
		
	}
	
	$endDate="$sMo/$sDay/$sYr";
	if(param('format') > 0) {
		if($daysFound == 0) {
			&retNoData()
		} else {
			open (FILE, "$acct/L10HC_PageL.dat") || &retNoData();
			@pageList = <FILE>;
			close(FILE);
			foreach(@pageList) {
				chop($_);
			}
			&setRepTime();
			$iD = "\t";
			$sD = "";
			$eD = "\n";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>Paths</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 8pt;}</style></header><body><table border=1 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td> ';
				$eD = ' </td></tr>'."\n";
			}
			print $sD."Path Report".$eD;
			print $sD."Run Time: $repDate $repTime$siteTitle".$eD;
			print $sD."Date Range: $startDate-$endDate".$eD;
			print $sD.&getFromFilterStr().$eD;
			print $sD.$eD;
			print $sD."".$iD."All Sessions".$iD."All Uniques".$iD."New Visitors".$eD;
			foreach (sort {$pCnt{$b}[0] <=> $pCnt{$a}[0]} (keys %pCnt)) {
				print $sD."$_".$iD."$pCnt{$_}[0]".$iD."$pCnt{$_}[1]".$iD."$pCnt{$_}[2]".$iD."$pTypes{$_}".$eD;
				$t2 = $_;
				$t2 =~ s/\*//;
				@t = split(/,/,$t2);
				for($k=0;$k<=$#t;$k++) {					
					$t1 = &roundNum($pTime{$_}[$k]/$pCnt{$_}[0],1);
					$t1 = ($t1 eq "0.0") ? "" : $t1;
					print $sD.$pageList[$t[$k]].$iD.$t1.$eD;	
				}
			}
			print $sD.$eD;
			print $sD."Totals".$iD."$totals[0]".$iD."$totals[1]".$iD."$totals[2]".$iD."".$eD;
		}	
	
	} else {
		if($daysFound == 0) {
			&retNoData();
		} else {
			&setRepTime();
			print header;
			print "res=OK&TR=$total&";
			print "Date=$startDate - $endDate&";
			print "Run=$repDate $repTime$siteTitle&";
			if(param('Pa') eq '') {
				$i = 0;
				foreach (sort {$pCnt{$b}[0] <=> $pCnt{$a}[0]} (keys %pCnt)) {
					print "X$i=$_&A$i=$pCnt{$_}[0]&B$i=$pCnt{$_}[1]&C$i=$pCnt{$_}[2]&D$i=".join(",",@{ $pTime{$_} })."&E$i=$pTypes{$_}&";
					$i++;
					if($i>=$maxRepItems) { last; }
				}
				print "pCount=$i";
			} else {
				$pa = param('Pa');
				print "XP=$pa&AP=$pCnt{$pa}[0]&BP=$pCnt{$pa}[1]&CP=$pCnt{$pa}[2]&DP=".join(",",@{ $pTime{$pa} })."&EP=$pTypes{$pa}&";

			}
		}
	}
}

sub pathReportF() {
	&updateNav();
	my ($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();
	
	$startDate = "$sMo/$sDay/$sYr";
	$pCount = 0;
	
	$total = 0;
	$total2 = 0;
	%paCnt = ();
	%paTime = ();
	%paTypes = ();

	%paList = ();	
	@paListI = ();
	%refList = ();
	@refListI = ();
	
	%prCnt = ();
	
	@paLFile= ();
	@paIFile = ();
	@paDFile = ();
	@refLFile = ();
	
	
	$qRef = param('ff');
	if($qRef eq '[No Referrer]') {
		$qRef = '';
	}
	
	if(param('fft') eq 'Dom') {
		$rFileName = 'Doms';
	} elsif(param('fft') eq 'URL') {
		$rFileName = 'Refs';
	} elsif(param('fft') eq 'SE') {
		$rFileName = 'SEs';
	} elsif(param('fft') eq 'SEKW') {
		$rFileName = 'SEKWs';
	} elsif(param('fft') eq 'KW') {
		$rFileName = 'KWs';
	} elsif(param('fft') eq 'RT') {
		$rFileName = 'rTypes';
		$qRef = &getRTypeID(param('ff'));
	}
	
	($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);	
	$daysFound = 0;
	for($i=0;$i<$dayCnt;$i++) {
		($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,1);

		@file = ();
		
		if(-e &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) {
			open (FILE, &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) || &retNoData();
			@paLFile = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr('Paths','D',$sYr,$sMo,$sDay)) || &retNoData();
			@paDFile = <FILE>;
			close(FILE);
			$daysFound ++;
		} else {
			next;
		}
		
		open (FILE, &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) || &retNoData();
		@refLFile = <FILE>;
		close(FILE);
		
		if(param('ff') ne '_') {
			open (FILE, &getFileDateStr('paRefs','IbR',$sYr,$sMo,$sDay)) || &retNoData();
			@paIbRFile = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr($rFileName,'I',$sYr,$sMo,$sDay)) || &retNoData();
			@refIFile = <FILE>;
			close(FILE);
			
			@res = &bSearch($qRef,\@refLFile,1,\@refIFile,1,1);	
			
			for($j=$res[1];$j<=$res[2];$j++) {
				
				$IbRFID = $refIFile[$j]*2;
				chop($paIbRFile[$IbRFID]);
				chop($paIbRFile[$IbRFID+1]);
				@ta = split(/\t/,$paIbRFile[$IbRFID]);
				@tb = split(/\t/,$paIbRFile[$IbRFID+1]);
				for($k=0;$k<=$#ta;$k++) {
					$pa = $paLFile[$ta[$k]];
					chop($pa);
					$paD = $paDFile[$ta[$k]];
					chop($paD);
					@t = split(/\t/,$paD);
					if(!exists $paList{$pa} ) {
						push(@paListI,$pa);
						$paID = $#paListI;
						$paList{$pa} = $paID;
						$paCnt{$paID} = $tb[$k];
						$paTypes{$paID} = "".(($pa =~ m/\,/) ? C : B).(($pa =~ m/\*/) ? S : N);	
						$paTime{$paID} = [ splice(@t,3) ];
						
					} else {
						$paID = $paList{$pa};
						$paCnt{$paID} += $tb[$k];
						for($k=3;$k<=$#t;$k++) {
							$paTime{$paID}[$k-3] = $t[$k]; 
						}
					}
				}
			}
			
			
		} else {
			open (FILE, &getFileDateStr('paRefs','IbPa',$sYr,$sMo,$sDay)) || &retNoData();
			@paIbPaFile = <FILE>;
			close(FILE);
			
			$paFID = 0;
			for($j=0;$j<=$#paDFile;$j+=2) {
				chop($paLFile[$paFID]);
				$pa = $paLFile[$paFID];
				chop($paIbPaFile[$j]);
				chop($paIbPaFile[$j+1]);
				@ta = split(/\t/,$paIbPaFile[$j]);
				@tb = split(/\t/,$paIbPaFile[$j+1]);
				chop($paDFile[$paFID]);
				@t = split(/\t/,$paDFile[$paFID]);
				if(!exists $paList{$pa}) {

					push(@paListI,$pa);
					$paID = $#paListI;
					$paList{$pa} = $paID;
					$paCnt{$paID} = $t[1];
					$paTypes{$paID} = "".(($pa =~ m/\,/) ? C : B).(($pa =~ m/\*/) ? S : N);					
					$paTime{$paID} = [ splice(@t,3) ];
				} else {
					$paID = $paList{$pa};
					$paCnt{$paID} += $t[1];
					for($k=3;$k<=$#t;$k++) {
						$paTime{$paID}[$k-3] = $t[$k]; 
					}
				}
				for($k=0;$k<=$#ta;$k++) {
					$ref = $refLFile[$ta[$k]];
					chop($ref);
					if(!exists $refList{$ref}) {
						push(@refListI,$ref);
						$refID = $#refListI;
						$refList{$ref} = $refID;
						$paRefCnt{$paID}{$refID} = 0;
					} else {
						$refID = $refList{$ref};
					}
					$paRefCnt{$paID}{$refID} += $tb[$k];
					
				}
				
				$paFID ++;
				$total += $t[1];
			
			}
			
		}
		$total2 = $total;
		if(param('fft') eq 'SE' || param('fft') eq 'KW') {
			if(exists $refList{''}) {
				$refID = $refList{''};
				foreach $paID (keys %paCnt) {
					if(exists $paRefCnt{$paID}{$refID}) {
						$paCnt{$paID} -= $paRefCnt{$paID}{$refID};
						$total2 -= $paRefCnt{$paID}{$refID};
						delete $paRefCnt{$paID}{$refID};
						if($paCnt{$paID} == 0) {
							delete $paCnt{$paID};
						}
						
					}
				}
			}

		} elsif(param('fft') eq 'SEKW') {
			if(exists $refList{' - '}) {
				$refID = $refList{' - '};
				foreach $paID (keys %paCnt) {
					if(exists $paRefCnt{$paID}{$refID}) {
						$paCnt{$paID} -= $paRefCnt{$paID}{$refID};
						$total2 -= $paRefCnt{$paID}{$refID};
						delete $paRefCnt{$paID}{$refID};
						if($paCnt{$paID} == 0) {
							delete $paCnt{$paID};
						}

					}
				}
			}
		} else {
			if(exists $refList{''}) {
				$refID = $refList{''};
				$refListI[$refID] = '[No Referrer]';
			}
		}
		
	}

	$endDate="$sMo/$sDay/$sYr";
	if(param('format') > 0) {
		if($daysFound == 0) {
			&retNoData()
		} else {
			open (FILE, "$acct/L10HC_PageL.dat") || &retNoData();
			@pageList = <FILE>;
			close(FILE);
			&setRepTime();
			$iD = "\t";
			$sD = "";
			$eD = "\n";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>Paths</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 8pt;}</style></header><body><table border=1 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td> ';
				$sD2 = ' <tr bgcolor=#E8E8FF><td> ';
				$eD = ' </td></tr>'."\n";
			}
			print $sD."Path Report".$eD;
			print $sD."Run Time: $repDate $repTime$siteTitle".$eD;
			print $sD."Date Range: $startDate-$endDate".$eD;
			print $sD.&getFromFilterStr().$eD;
			print $sD.$eD;
			print $sD."".$iD."All Uniques".$eD;
			foreach $pa (sort {$paCnt{$b} <=> $paCnt{$a}} (keys %paCnt)) {
				print $sD.$paListI[$pa].$iD.$paCnt{$pa}.$iD.$paTypes{$pa}.$eD;
				$t2 = $paListI[$pa];
				$t2 =~ s/\*//;
				@t = split(/\,/,$t2);
				for($k=0;$k<=$#t;$k++) {
					$t1 = &roundNum($paTime{$pa}[$k]/$paCnt{$pa},1);
					$t1 = ($t1 eq "0.0") ? "" : $t1;
					print $sD.$pageList[$t[$k]].$iD.$t1.$eD;	
				}
				
				foreach $r (sort {$paRefCnt{$pa}{$b} <=> $paRefCnt{$pa}{$a}} (keys %{$paRefCnt{$pa}})) {
					$ref = $refListI[$r];
					$ref =~ s/%([a-fA-F0-9]{2})/chr(hex($1))/ge;
					print $sD2."> $ref".$iD.$paRefCnt{$pa}{$r}.$eD;
				}

				
			}
			if($total2 != $total) {
				print $sD."Total".$iD."$total2".$eD;
			}
			print $sD."Total".$iD."$total".$eD;
		}	
	
	} else {
		if($daysFound == 0) {
			&retNoData();
		} else {
			&setRepTime();
			print header;
			print "res=OK&TR=$total&";
			print "Date=$startDate - $endDate&";
			print "Run=$repDate $repTime$siteTitle&";
			if(param('Pa') eq '') {
				$i = 0;
				if(param('ff') eq '_') {
					foreach $pa (sort {$paCnt{$b} <=> $paCnt{$a}} keys %paCnt) {
						foreach $r (keys %{$paRefCnt{$pa}}) {	
							print "X$i=$paListI[$pa]&Y$i=$r&B$i=$paRefCnt{$pa}{$r}&D$i=".join(",",@{ $paTime{$pa} })."&E$i=$paTypes{$pa}&";
							$i++;
							if($i>=$maxRepItems) { last; }
						}
						if($i>=$maxRepItems) { last; }
					}
				
					for($j=0;$j<=$#refListI;$j++) {
						print "YL$j=$refListI[$j]&";
					}
				} else {
					foreach $pa (sort {$paCnt{$b} <=> $paCnt{$a}} keys %paCnt) {
						print "X$i=$paListI[$pa]&B$i=$paCnt{$pa}&D$i=".join(",",@{ $paTime{$pa} })."&E$i=$paTypes{$pa}&";
						$i++;
						if($i>=$maxRepItems) { last; }
					}
				}
				print "pCount=$i";
			} else {
				print "XP=".param('Pa')."&BP=$pCnt{$_}&DP=".join(",",@{ $pTime{$_} })."&EP=$pTypes{$_}&";

			}
		}
	}
}

sub referrerReport() {
	my ($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();
	$startDate = "$sMo/$sDay/$sYr";
	
	$SE = '';
	%rRefs = ();
	%rRefsTypes = ();
	# $rRefs{'[No Referrer]'} = [ (0,0,0) ];
	%rPgRefs = ();
	@pgFile = ();
	$tFilter = '';
	$tFilterT = '';
	$tFilterI = 0;
	@totals = (0,0,0);
	@totals2 = (0,0,0);
	@totals3 = (0,0,0);
	%paList = ();
	@paDat = ();
	@paDat2 = ();
	@paLFile = ();
	@paListI = ();
	@paDFile = ();
	@rTypeL = ();
	$rTypeID = -1;
	if((param('b') eq 'RT') || (param('b2') ne '')) {
		open (FILE, "$acct/L10HC_Archive/rTypes/rTypeL.dat") || &gen_error("Cannot open $acct/L10HC_Archive/rTypes/rTypeL.dat at \"Read Today's Stats Data\"");
		@rTypeL = <FILE>;
		close(FILE);
		
		if(length(param('b2')) > 1) {
			open (FILE, "$acct/L10HC_Archive/rTypes/rTypeI.dat") || &gen_error("Cannot open $acct/L10HC_Archive/rTypes/rTypeI.dat at \"Read Today's Stats Data\"");
			@t = <FILE>;
			close(FILE);
			
			@res = &bSearch(param('b2'),\@rTypeL,1,\@t,1);
			if(!$res[0]) {
				print header;
				print "res=Err&msg=Referrer type not found! rType=".param('b2');
				exit 0;
			} else {
				$rTypeID = $res[1];
			}
		}
	}
	if(param('tft') eq 'Pg') {
		$tFilterT = 'Pg';
		open (FILE, "$acct/L10HC_PageL.dat") || &gen_error("Cannot open $acct/L10HC_PageL.dat at \"Read Today's Stats Data\"");
		@pgLFile = <FILE>;
		close(FILE);
		open (FILE, "$acct/L10HC_PageI.dat") || &gen_error("Cannot open $acct/L10HC_PageI.dat at \"Read Today's Stats Data\"");
		@pgIFile = <FILE>;
		close(FILE);
		
		if(param('tf') ne '_') {
			$pg = &filterPageURL(param('tf'));
			@res = &bSearch($pg,\@pgLFile,1,\@pgIFile,1);
			if(!$res[0]) {
				print header;
				print "res=Err&msg=To page not found! pg=$pg";
				exit 0;
			} else {
				$tFilterI = $res[1];
			}
		}
	} elsif(param('tft') eq 'Pa') {
		$tFilter = param('tf');
		$tFilterT = 'Pa';
	}
	
	$refDes = '';
	if(param('b') eq "Dom") {
		$file = "Doms";
		$refDes = 'Domains';
	} elsif(param('b') eq "URL") {
		$file = "Refs";
		$refDes = 'URLs';
	} elsif(param('b') eq "SE") {
		$file = "SEs";
		$refDes = 'Search Engines';
	} elsif(param('b') eq "KW") {
		$file = "KWs";
		$refDes = 'Keywords';
	} elsif(param('b') eq "SEKW") {
		$file = "SEKWs";
		$refDes = 'SE Keywords';
	} elsif(param('b') eq "RT") {
		$file = 'rTypes';
		$refDes = 'Types';
	} else {
		$file = "KWs";
		$SE = param('b');
		$refDes = "$SE Keywords";
	}

	my $total = 0;
	($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
	my $daysFound = 0;
	for($i=0;$i<$dayCnt;$i++) {
	
		($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,1);
		@refLFile = ();
		@refIFile = ();
		@refCnt = ();
		%refCntF = ();
		if($tFilterT eq 'Pg') {
			if(-e &getFileDateStr('pgRefs','IbPg',$sYr,$sMo,$sDay)) {
				
				if(param('tf') ne '_') {

					open (FILE, &getFileDateStr('pgRefs','IbPg',$sYr,$sMo,$sDay)) || &retNoData();
					@t = <FILE>;
					close(FILE);
		
					chop($t[$tFilterI*4]);
					chop($t[$tFilterI*4+1]);
					chop($t[$tFilterI*4+2]);
					chop($t[$tFilterI*4+3]);
					@ta = split(/\t/,$t[$tFilterI*4]);
					@tb = split(/\t/,$t[$tFilterI*4+1]);
					@tc = split(/\t/,$t[$tFilterI*4+2]);
					@td = split(/\t/,$t[$tFilterI*4+3]);
					for($j=0;$j<=$#ta;$j++) {
						$refCntF{$ta[$j]} = [($tb[$j],$tc[$j],$td[$j])];
					}
				} else {
					open (FILE, &getFileDateStr('pgRefs','IbR',$sYr,$sMo,$sDay)) || &retNoData();
					@pgFile = <FILE>;
					close(FILE);
				}
			} else {
				next;
			}
		} elsif($tFilterT eq 'Pa') {
			if(param('tf') ne '_') {
				if(-e &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) {
					open (FILE, &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) || &gen_error("Cannot open ".&getFileDateStr('Paths','L',$sYr,$sMo,$sDay)." at \"Read Today's Stats Data\"");
					@paLFile = <FILE>;
					close(FILE);
					open (FILE, &getFileDateStr('Paths','I',$sYr,$sMo,$sDay)) || &gen_error("Cannot open ".&getFileDateStr('Paths','I',$sYr,$sMo,$sDay)." at \"Read Today's Stats Data\"");
					@paIFile = <FILE>;
					close(FILE);
				} else {
					next;
				}

				@res = &bSearch($tFilter,\@paLFile,1,\@paIFile,1);

				if(!$res[0]) {
					next;
				} else {
					$tFilterI = $res[1];
				}
				if(-e &getFileDateStr('paRefs','IbPa',$sYr,$sMo,$sDay)) {
					open (FILE, &getFileDateStr('paRefs','IbPa',$sYr,$sMo,$sDay)) || &retNoData();
					@t = <FILE>;
					close(FILE);
					chop($t[$tFilterI*2]);
					chop($t[$tFilterI*2+1]);
					@ta = split(/\t/,$t[$tFilterI*2]);
					@tb = split(/\t/,$t[$tFilterI*2+1]);
					for($j=0;$j<=$#ta;$j++) {
						$refCntF{$ta[$j]} = $tb[$j];
					}
				} else {
					next;
				}
			} else {
				if(-e &getFileDateStr('paRefs','IbR',$sYr,$sMo,$sDay)) {
					open (FILE, &getFileDateStr('paRefs','IbR',$sYr,$sMo,$sDay)) || &retNoData();
					@paDFile = <FILE>;
					close(FILE);
					open (FILE, &getFileDateStr('Paths','D',$sYr,$sMo,$sDay)) || &retNoData();
					@paDMFile = <FILE>;
					close(FILE);
					open (FILE, &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) || &retNoData();
					@paLFile = <FILE>;
					close(FILE);
				} else {
					next;
				}	
			}
		} else {
			if(-e &getFileDateStr('sRefs','D',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr('sRefs','D',$sYr,$sMo,$sDay)) || &retNoData();
				@refCnt = <FILE>;
				close(FILE);
			} else {
				next;
			}
		}

		if(-e &getFileDateStr($file,'L',$sYr,$sMo,$sDay)) {
			open (FILE, &getFileDateStr($file,'L',$sYr,$sMo,$sDay)) || &retNoData();
			@refLFile = <FILE>;
			close(FILE);
		#	open (FILE, &getFileDateStr($file,'I',$sYr,$sMo,$sDay)) || &retNoData();
		#	@refIFile = <FILE>;
		#	close(FILE);
			$daysFound ++;
		} else {
			next;
		}
		
		if($SE ne '') { # KW for one SE
			open (FILE, &getFileDateStr('SEs','L',$sYr,$sMo,$sDay)) || &retNoData();
			@seLFile = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr('SEs','I',$sYr,$sMo,$sDay)) || &retNoData();
			@seIFile = <FILE>;
			close(FILE);
		}
		if(param('b2') ne '') {
			open (FILE, &getFileDateStr('rTypes','L',$sYr,$sMo,$sDay)) || &retNoData();
			@rTypeLFile = <FILE>;
			close(FILE);
		} else {
			@rTypeLFile = ();
		}
		
		if($tFilterT eq '') { # no to filter
			if($SE ne '') { # KW for one SE
				
				@res = &bSearch($SE,\@seLFile,1,\@seIFile,1,1);	
				
				if($res[0]) {
					for($j=$res[1];$j<=$res[2];$j++) {
						$ji = $seIFile[$j];
						chop($ji);
						chop($refCnt[$ji]);
						chop($refLFile[$ji]);
						if(param('b2') eq '_') {
							chop($rTypeLFile[$ji]);
							$t = $rTypeL[$rTypeLFile[$ji]]; 
							chop($t);
							$ref = "$t - $refLFile[$j]";
						} elsif(param('b2') ne '') {
							if("$rTypeLFile[$ji]" ne "$rTypeID\n") {
								next;
							}
							$ref = $refLFile[$ji];
						} else {
							$ref = $refLFile[$ji];
						}
						@t = split(/\t/,$refCnt[$ji]);
						if(exists $rRefs{$ref}) {
							$rRefs{$ref}[0] += $t[0];
							$rRefs{$ref}[1] += $t[1];
							$rRefs{$ref}[2] += $t[2];
						} else {
							$rRefs{$ref} = [ @t ];
						}
						$totals[0] += $t[0];
						$totals[1] += $t[1];
						$totals[2] += $t[2];
					}
				} else {
					next;
				}
			} else { # regular refs
				for($j=0;$j<=$#refLFile;$j++) {
					chop($refCnt[$j]);					
					chop($refLFile[$j]);
					if(param('b2') eq '_') {
						chop($rTypeLFile[$j]);
						$t = $rTypeL[$rTypeLFile[$j]]; 
						chop($t);
						$ref = "$t - $refLFile[$j]";
					} elsif(param('b2') ne '') {
						if("$rTypeLFile[$j]" ne "$rTypeID\n") {
							next;
						}
						$ref = $refLFile[$j];
					} else {
						$ref = $refLFile[$j];
					}
					@t = split(/\t/,$refCnt[$j]);
					if(exists $rRefs{$ref}) {
						$rRefs{$ref}[0] += $t[0];
						$rRefs{$ref}[1] += $t[1];
						$rRefs{$ref}[2] += $t[2];
					} else {
						$rRefs{$ref} = [ @t ];
					}
					$totals[0] += $t[0];
					$totals[1] += $t[1];
					$totals[2] += $t[2];
				}
			}
		} elsif($tFilterT eq 'Pg') {
			if(param('tf') ne '_') {
				foreach $refID (keys %refCntF) {
					if(($SE eq '') || ("$SE\n" eq $seLFile[$refID])) {
						chop($refLFile[$refID]);
						if(param('b2') eq '_') {
							chop($rTypeLFile[$refID]);
							$t = $rTypeL[$rTypeLFile[$refID]]; 
							chop($t);
							$ref = "$t - $refLFile[$refID]";
						} elsif(param('b2') ne '') {
							if("$rTypeLFile[$refID]" ne "$rTypeID\n") {
								next;
							}
							$ref = $refLFile[$refID];
						} else {
							$ref = $refLFile[$refID];
						}
						
						if(exists $rRefs{$ref}) {
							$rRefs{$ref}[0] += $refCntF{$refID}[0];
							$rRefs{$ref}[1] += $refCntF{$refID}[1];
							$rRefs{$ref}[2] += $refCntF{$refID}[2];
						} else {
							$rRefs{$ref} = [($refCntF{$refID}[0],$refCntF{$refID}[1],$refCntF{$refID}[2])];
						}
						$totals[0] += $refCntF{$refID}[0];
						$totals[1] += $refCntF{$refID}[1];
						$totals[2] += $refCntF{$refID}[2];
					}
				}
			} else {
				$refID = 0;
				for($k=0;$k<=$#pgFile;$k+=4) {
					if(($SE eq '') || ("$SE\n" eq $seLFile[$refID])) {
						chop($refLFile[$refID]);
						if(param('b2') eq '_') {
							chop($rTypeLFile[$refID]);
							$t = $rTypeL[$rTypeLFile[$refID]]; 
							chop($t);
							$ref = "$t - $refLFile[$refID]";
						} elsif(param('b2') ne '') {
							if("$rTypeLFile[$refID]" ne "$rTypeID\n") {
								next;
							}
							$ref = $refLFile[$refID];
						} else {
							$ref = $refLFile[$refID];
						}
						chop($pgFile[$k]);
						chop($pgFile[$k+1]);
						chop($pgFile[$k+2]);
						chop($pgFile[$k+3]);
						@ta = split(/\t/,$pgFile[$k]);
						@tb = split(/\t/,$pgFile[$k+1]);
						@tc = split(/\t/,$pgFile[$k+2]);
						@td = split(/\t/,$pgFile[$k+3]);
						for($j=0;$j<=$#ta;$j++) {
							if(exists $rRefs{$ref}) {
								$rRefs{$ref}[0] += $tb[$j];
								$rRefs{$ref}[1] += $tc[$j];
								$rRefs{$ref}[2] += $td[$j];
							} else {
								$rRefs{$ref} = [ ($tb[$j],$tc[$j],$td[$j]) ];
							}
							if(exists $rPgRefs{$ref}{$ta[$j]}) {
								$rPgRefs{$ref}{$ta[$j]}[0] += $tb[$j];
								$rPgRefs{$ref}{$ta[$j]}[1] += $tc[$j];
								$rPgRefs{$ref}{$ta[$j]}[2] += $td[$j];
							} else {
								$rPgRefs{$ref}{$ta[$j]} = [ ($tb[$j],$tc[$j],$td[$j]) ];
							}
							$totals[0] += $tb[$j];
							$totals[1] += $tc[$j];
							$totals[2] += $td[$j];
						}
					}
					$refID ++;
				}				
			}
		} else { # Pa
			if(param('tf') ne '_') {
				$pa = param('tf');
				$c1 = (($pa =~ m/\*/) || ($pa =~ m/\,/)) ? 1 : 0;
				$c2 = ($pa =~ m/\*/) ? 1 : 0; 
				foreach $refID (keys %refCntF) {
					if(($SE eq '') || ("$SE\n" eq $seLFile[$refID])) {
						chop($refLFile[$refID]);
						if(param('b2') eq '_') {
							chop($rTypeLFile[$refID]);
							$t = $rTypeL[$rTypeLFile[$refID]]; 
							chop($t);
							$ref = "$t - $refLFile[$refID]";
						} elsif(param('b2') ne '') {
							if("$rTypeLFile[$refID]" ne "$rTypeID\n") {
								next;
							}
							$ref = $refLFile[$refID];
						} else {
							$ref = $refLFile[$refID];
						}
						
						if(exists $rRefs{$ref}) {
							$rRefs{$ref}[0] += $refCntF{$refID};
							if($c1) { $rRefs{$ref}[1] += $refCntF{$refID}; }
							if($c2) { $rRefs{$ref}[2] += $refCntF{$refID}; }
						} else {
							$rRefs{$ref} = [ ($refCntF{$refID},$c1*$refCntF{$refID},$c2*$refCntF{$refID}) ];
						}
						$totals[0] += $refCntF{$refID};
						if($c1) {$totals[1] += $refCntF{$refID};}
						if($c2) {$totals[2] += $refCntF{$refID};}
					}
				}
			} else {
				$refFileID = 0;
				for($k=0;$k<=$#paDFile;$k+=2) {
					if(($SE eq '') || ("$SE\n" eq $seLFile[$refFileID])) {
						
						chop($paDFile[$k]);
						chop($paDFile[$k+1]);
						@ta = split(/\t/,$paDFile[$k]);
						@tb = split(/\t/,$paDFile[$k+1]);
						chop($refLFile[$refFileID]);
						if(param('b2') eq '_') {
							chop($rTypeLFile[$refFileID]);
							$t = $rTypeL[$rTypeLFile[$refFileID]]; 
							chop($t);
							$ref = "$t - $refLFile[$refFileID]";
						} elsif(param('b2') ne '') {
							if("$rTypeLFile[$refFileID]" ne "$rTypeID\n") {
								next;
							}
							$ref = $refLFile[$refFileID];
						} else {
							$ref = $refLFile[$refFileID];
						}
						for($j=0;$j<=$#ta;$j++) {
							$pa = $paLFile[$ta[$j]];
							chop($pa);
							chop($paDMFile[$ta[$j]]);
							@t = split(/\t/,$paDMFile[$ta[$j]]);
							
							if(exists $paList{$pa}) {
								$paID = $paList{$pa};
								$paDat[$paID][0] += $t[0];
								for($m=1;$m<$#[$paDat[$paID]];$m++) {
									$paDat[$paID][$m] += $t[$m+2];
								}						
							} else {
								$c1 = (($pa =~ m/\*/) || ($pa =~ m/\,/)) ? 1 : 0;
								$c2 = ($pa =~ m/\*/) ? 1 : 0; 
								push(@paDat,[ ($t[0],splice(@t,3)) ]);
								push(@paDat2,[ ($c1,$c2) ]);
								push(@paListI,$pa);
								$paList{$pa} = $#paListI;								
								$paID = $#paListI;
							}
							
							$tc = ($paDat2[$paID][0]) ? $tb[$j] : 0;
							$td = ($paDat2[$paID][1]) ? $tb[$j] : 0;
							if(exists $rRefs{$ref}) {
								$rRefs{$ref}[0] += $tb[$j];
								$rRefs{$ref}[1] += $tc;
								$rRefs{$ref}[2] += $td;
							} else {
								$rRefs{$ref} = [ ($tb[$j],$tc,$td) ];
							}
							if(exists $rPgRefs{$ref}{$paID}) {
								$rPgRefs{$ref}{$paID}[0] += $tb[$j];
								$rPgRefs{$ref}{$paID}[1] += $tc;
								$rPgRefs{$ref}{$paID}[2] += $td;
							} else {
								$rPgRefs{$ref}{$paID} = [ ($tb[$j],$tc,$td) ];
							}
							$totals[0] += $tb[$j];
							$totals[1] += $tc;
							$totals[2] += $td;
						}

					}
					$refFileID ++;
				}				
			}
		}
	}

	$endDate="$sMo/$sDay/$sYr";
	if((param('b') eq 'Dom') || (param('b') eq 'URL') || (param('b') eq 'RT')) {
 		if(param('b2') eq '_') {
 			$k = '[Unknown] - [No Referrer]';
 			$l = '[Unknown] - ';
 		} else {
			$k = (param('b') eq 'RT') ? '[Unknown]' : '[No Referrer]';
			$l = '';
		}
		if(exists $rRefs{$l}) {
			$rRefs{$k}[0] += $rRefs{$l}[0];
			$rRefs{$k}[1] += $rRefs{$l}[1];
			$rRefs{$k}[2] += $rRefs{$l}[2];
			
			delete($rRefs{$l});
			foreach (keys %{$rPgRefs{$l}}) {
				$rPgRefs{$k}{$_} = $rPgRefs{$l}{$_};
				delete $rPgRefs{$l}{$_};
			}

		}
	} else {
		if(param('b2') eq '_') {
			$totals2[0] = $totals[0];
			$totals2[1] = $totals[1];
			$totals2[2] = $totals[2];
			foreach $k (keys %rRefs) {
				if(index($k,"-  - ") >= 0) {

					$totals[0] -= $rRefs{$k}[0];
					$totals[1] -= $rRefs{$k}[1];
					$totals[2] -= $rRefs{$k}[2];
					delete($rRefs{$k});					
					foreach (keys %{$rPgRefs{$k}}) {
						delete $rPgRefs{$k}{$_};
					}		
				}
			}
			delete($rRefs{'[No Referrer]'});
		} else {
			$k = (param('b') eq 'SEKW') ? ' - ' : '';
			if(exists $rRefs{$k}) {
				$totals2[0] = $totals[0];
				$totals2[1] = $totals[1];
				$totals2[2] = $totals[2];
				$totals[0] = $totals2[0] - $rRefs{$k}[0];
				$totals[1] = $totals2[1] - $rRefs{$k}[1];
				$totals[2] = $totals2[2] - $rRefs{$k}[2];
				delete($rRefs{$k});
				delete($rRefs{'[No Referrer]'});
				foreach (keys %{$rPgRefs{$k}}) {
					delete $rPgRefs{$k}{$_};
				}
			}
		}
	}
	
	$KWI = '';
	if(param('KWI') ne '') {
		$KWI = param('KWI');
		$totals3[0] = $totals[0];
		$totals3[1] = $totals[1];
		$totals3[2] = $totals[2];
	}
	$threshold = 0;
	if(param('TH') ne '') {
		$threshold = param('TH') - 1;
	}
	if(param('format') > 0) {
		if($daysFound == 0) {
			&retNoData()
		} else {
			&setRepTime();
			$iD = "\t";
			$sD = "";
			$sD2 = "";
			$eD = "\n";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>Referrers</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 8pt;}</style></header><body><table border=1 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td>';
				$sD2 = ' <tr bgcolor=#E8E8FF><td> ';
				$eD = ' </td></tr>'."\n";
			}
			if($KWI eq '') {
				print $sD."Referrers".$eD;
			} else {
				print $sD."Referrers - including: \"$KWI\"".$eD;
			}
			print $sD."Run Time: $repDate $repTime$siteTitle".$eD;
			print $sD."Date Range: $startDate-$endDate".$eD;
			print $sD.&getToFilterStr.$eD;
			print $sD.$eD;
			print $sD."Referrer".$iD."Count".$iD."Conv.".$iD."Succ.".$iD."Conv%".$iD."Succ%".$eD;
			if($tFilterT eq 'Pa') {
				foreach $r (sort {$rRefs{$b}[0] <=> $rRefs{$a}[0]} (keys %rRefs)) {
					if(param('b') eq 'RT') {
						$rl = $rTypeL[$r];
						chop($rl);
					} else {
						$rl = $r;
						$rl =~ s/%([a-fA-F0-9]{2})/chr(hex($1))/ge;
					}
					print $sD.$rl.$iD.$rRefs{$r}[0].$iD.$rRefs{$r}[1].$iD.$rRefs{$r}[2].$eD;
					foreach $p (sort {$rPgRefs{$r}{$b}[0] <=> $rPgRefs{$r}{$a}[0]} (keys %{$rPgRefs{$r}})) {
						$pa = $paListI[$p];
						print $sD2."> $pa".$iD.$rPgRefs{$r}{$p}[0].$iD.$rPgRefs{$r}{$p}[1].$iD.$rPgRefs{$r}{$p}[2].$iD.&roundNum(100*$rPgRefs{$r}{$p}[1]/$rPgRefs{$r}{$p}[0],1).$iD.&roundNum(100*$rPgRefs{$r}{$p}[2]/$rPgRefs{$r}{$p}[0],1).$eD;
					}	

				}
			
			} else {
				foreach $r (sort {$rRefs{$b}[0] <=> $rRefs{$a}[0]} (keys %rRefs)) {
					if(param('b') eq 'RT') {
						$rl = $rTypeL[$r];
						chop($rl);
					} else {
						$rl = $r;
						$rl =~ s/%([a-fA-F0-9]{2})/chr(hex($1))/ge;
					}
					if(($KWI eq '') || ($rl =~ m/$KWI/i)) {
						if($rRefs{$r}[0] > $threshold) {
							print $sD.$rl.$iD.$rRefs{$r}[0].$iD.$rRefs{$r}[1].$iD.$rRefs{$r}[2].$iD.&roundNum(100*$rRefs{$r}[1]/$rRefs{$r}[0],1).$iD.&roundNum(100*$rRefs{$r}[2]/$rRefs{$r}[0],1).$eD;
							foreach $p (sort {$rPgRefs{$r}{$b}[0] <=> $rPgRefs{$r}{$a}[0]} (keys %{$rPgRefs{$r}})) {
								print $sD2."> $pgLFile[$p]".$iD.$rPgRefs{$r}{$p}[0].$iD.$rPgRefs{$r}{$p}[1].$iD.$rPgRefs{$r}{$p}[2].$iD.&roundNum(100*$rPgRefs{$r}{$p}[1]/$rPgRefs{$r}{$p}[0],1).$iD.&roundNum(100*$rPgRefs{$r}{$p}[2]/$rPgRefs{$r}{$p}[0],1).$eD;
							}
						}
					} else {
						$totals3[0] -= $rRefs{$r}[0];
						$totals3[1] -= $rRefs{$r}[1];
						$totals3[2] -= $rRefs{$r}[2];
					}
				}
			}
			print $sD.$eD;
			if($totals3[0] > 0) {
				print $sD."Totals".$iD.$totals3[0].$iD.$totals3[1].$iD.$totals3[2].$iD.&roundNum(100*$totals3[1]/$totals3[0],1).$iD.&roundNum(100*$totals3[2]/$totals3[0],1).$eD;
			}
			print $sD."Totals".$iD.$totals[0].$iD.$totals[1].$iD.$totals[2].$iD.&roundNum(100*$totals[1]/$totals[0],1).$iD.&roundNum(100*$totals[2]/$totals[0],1).$eD;
			if($totals2[0] > 0) {
				print $sD."Totals".$iD.$totals2[0].$iD.$totals2[1].$iD.$totals2[2].$iD.&roundNum(100*$totals2[1]/$totals2[0],1).$iD.&roundNum(100*$totals2[2]/$totals2[0],1).$eD;
			}
		}
	} else {
		if($daysFound == 0) {
			&retNoData()
		} else {
			&setRepTime();
			print header;
			print "res=OK&";
			print "title=Referring $refDes&";
			print "Date=$startDate - $endDate&";
			print "Run=$repDate $repTime$siteTitle&";
			print "BS=$totals[0]&JS=$totals[1]&MS=$totals[2]&";
			print "BT=$totals2[0]&JT=$totals2[1]&MT=$totals2[2]&";
			$i = 0;
			if(param('tf') eq '_') {
				if(param('tft') eq 'Pg') {
					foreach $r (sort {$rRefs{$b}[0] <=> $rRefs{$a}[0]} (keys %rRefs)) {
						$rl = (param('b') eq 'RT') ? $rTypeL[$r] : $r;
						foreach $p (keys %{$rPgRefs{$r}}) {
							print "X$i=$rl&Y$i=$p&B$i=$rRefs$rPgRefs{$r}{$p}[0]&J$i=$rRefs$rPgRefs{$r}{$p}[1]&M$i=$rRefs$rPgRefs{$r}{$p}[2]&";
							$i++;
							if($i>=$maxRepItems) { last; }
						}
						if($i>=$maxRepItems) { last; }
					}
				} else {
					foreach $r (sort {$rRefs{$b}[0] <=> $rRefs{$a}[0]} (keys %rRefs)) {
						if(param('b') eq 'RT') { $rl = $rTypeL[$r]; chop($rl); } else { $rl=$r; }
						foreach $p (keys %{$rPgRefs{$r}}) {
							print "X$i=$rl&Y$i=$p&B$i=$rRefs$rPgRefs{$r}{$p}[0]&J$i=$rRefs$rPgRefs{$r}{$p}[1]&M$i=$rRefs$rPgRefs{$r}{$p}[2]&";
							$i++;
							if($i>=$maxRepItems) { last; }
						}
						if($i>=$maxRepItems) { last; }
					}
					for($j=0;$j<=$#paListI;$j++) {
						print "YL$j=$paListI[$j]&YD$j=$paDat[$j][0]&YE$j=".join(',',splice(@{$paDat[$j]},1))."&";
					}
				}
			} else {
				foreach $r (sort {$rRefs{$b}[0] <=> $rRefs{$a}[0]} (keys %rRefs)) {
					if(param('b') eq 'RT') { $rl = $rTypeL[$r]; chop($rl); } else { $rl=$r; }
					print "X$i=$rl&B$i=$rRefs{$r}[0]&J$i=$rRefs{$r}[1]&M$i=$rRefs{$r}[2]&";
					$i++;
					if($i>=$maxRepItems) { last; }
				}
			}
			print "iCnt=$i&"
		}
	}	
}

sub getRefLinks() {
	my ($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();
	
	$startDate = "$sMo/$sDay/$sYr";
	
	%URLs = ();
	$file = 'Doms';
	$desStr = 'Domain';
	$ref = param('ref');
	if(param('b') eq "URL") {
		$file = "Refs";
	} elsif(param('b') eq "SE") {
		$file = "SEs";
		$desStr = 'Search Engine';
	} elsif(param('b') eq "KW") {
		$file = "KWs";
		$desStr = 'Keyword';
	} elsif(param('b') eq "SEKW") {
		$file = "SEKWs";
		$desStr = 'Search Engine keyword';
	} elsif(param('b') eq 'RT') {
		$file = "rTypes";
		$desStr = 'Referrer Types';
		open (FILE, "$acct/L10HC_Archive/rTypes/rTypeL.dat") || &retNoData();
		@refL = <FILE>;
		close(FILE);
		open (FILE, "$acct/L10HC_Archive/rTypes/rTypeI.dat") || &retNoData();
		@refI = <FILE>;
		close(FILE);
		
		@res = &bSearch($ref,\@refL,1,\@refI,1);

		if($res[0]) {
			$ref = $res[1];
		} else {
			&retNoData();
		}
		
	}
	($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
	for($i=0;$i<$dayCnt;$i++) {
		($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,1);	
		if(-e &getFileDateStr($file,'L',$sYr,$sMo,$sDay)) {
			open (FILE, &getFileDateStr($file,'L',$sYr,$sMo,$sDay)) || &retNoData();
			@refL = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr($file,'I',$sYr,$sMo,$sDay)) || &retNoData();
			@refI = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr('Refs','L',$sYr,$sMo,$sDay)) || &retNoData();
			@refURLs = <FILE>;
			close(FILE);
			open (FILE, &getFileDateStr('sRefs','D',$sYr,$sMo,$sDay)) || &retNoData();
			@refD = <FILE>;
			close(FILE);
		} else {
			next;
		}

		@res = &bSearch($ref,\@refL,1,\@refI,1,1);
		if($res[0]) {
			for($j=$res[1];$j<=$res[2];$j++) {
				$URLs{$refURLs[$refI[$j]]} += $refD[$refI[$j]];
			}
			$daysFound ++;
		} else {
			next;
		}
		
			
	}
	
	$endDate="$sMo/$sDay/$sYr";
	
	if($daysFound == 0) {
		print header;
		print "No results found!";
	} else {
		if(keys %URLs == 0) {
			print header;
			print "No results found!";
			
		} elsif(keys %URLs == 1) {
			foreach (keys %URLs) {
				$_ =~ s/%26/&/g;
				print "Location: http://$_\n\n";
				last;
			}
		} else {
			&setRepTime();
			$iD = "\t";
			$sD = "";
			$sD2 = "";
			$eD = "\n";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>Referrers</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 9pt;}</style></header><body>';
				
				print '<table border=0 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td>';
				$sD2 = ' <tr bgcolor=#E8E8FF><td> ';
				$eD = ' </td></tr>'."\n";
			}
			print $sD."<b>Multiple referrer links were found for the $desStr: ".param('ref')."</b>".$eD;;
			print $sD."Date Range: $startDate-$endDate".$eD;
			print $sD.$eD;

			print $sD."Referrer".$iD."Count".$eD;
			foreach $r (sort {$URLs{$b}[0] <=> $URLs{$a}[0]} (keys %URLs)) {
				$rl = $r;
				$rl =~ s/%26/&/g;
				# $rl =~ s/%([a-fA-F0-9]{2})/chr(hex($1))/ge;
				$rt = $rl;
				if(length($rt) > 80) {
					$rt = substr($rt,0,80).'...';
				}
				print $sD."<a href=\"http://$rl\" target=\"_blank\">$rt</a>".$iD.$URLs{$r}.$eD;
			}
			print $sD.$eD;
			if($totals2[0] > 0) {
				print $sD."".$iD.$totals2[0].$iD.$totals2[1].$iD.$totals2[2].$eD
			}
			print $sD."".$iD.$totals[0].$iD.$totals[1].$iD.$totals[2].$eD; 
		}
	}
}


sub historyReport () {
	&updateNav();
		
	($sYr,$sMo,$sDay,$dayCnt) = &getReportDateRange();

	&setRepTime();
	$per = '';
	$dataCnt = 0;
	@data = ();
	@xLables = ();
	$per = '';
	$period = "";
	if($dayCnt == 365) {
		$per = 'Y';
		if(param('p') == -6) { # this year
			$sYr = $curYr;
			$sMo = $curMo;
			$sDay = $curDay;
		} elsif(param('p') == -7) { # last year
			$sYr = $curYr-1;
			$sMo = 12;
			$sDay = 31;
		} else {
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,$dayCnt-1);
			if($sYr == $curYr) {
				$sMo = $curMo;
				$sDay = $curDay;				
			} else {
				$sMo = 12;
				$sDay = 31;
			}
		}
		$dataCnt = 10;
		$xL = $sYr - $dataCnt;
		$xL++;
		$period = "$xL - $sYr";
		for($i=0;$i<$dataCnt;$i++) {			
			push(@xLables,"$xL");
			push(@data, [ (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ]);
			$xL++;
		}
	} elsif($dayCnt >= 28) {
		$per = 'M';
		if(param('p') == -4) { # this mo
			$sYr = $curYr;
			$sMo = $curMo;
			$sDay = $curDay;
		} elsif(param('p') == -5) { # last mo
			$sYr = $curYr;
			$sMo = $curMo - 1;
			if($sMo < 1) {
				$sYr --;
				$sMo += 12;
			}
			$sDay = $DpMo[$sMo];
		} else {
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,$dayCnt-1);
			if(($sYr == $curYr) && ($sMo == $curMo)) {
				$sDay = $curDay;				
			} else {
				$sDay = $DpMo[$sMo];
			}
		}
		$dataCnt = 12;
		$xLYr = $sYr - 1;
		$xLMo = $sMo;
		$xLMo ++;
		if($xLMo > 12) {
			$xLMo = $xLMo-12;
			$xLYr ++;
		}
		$period = "$xLMo/$xLYr - $sMo/$sYr";
		for($i=0;$i<$dataCnt;$i++) {
			push(@xLables,"$xLMo/$xLYr");
			push(@data, [ (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ]);
			$xLMo ++;
			if($xLMo > 12) {
				$xLMo = $xLMo-12;
				$xLYr ++;
			}
		}
	} elsif($dayCnt == 7) {
		$per = 'W';
		if(param('p') == -2) { # this week
			$sYr = $curYr;
			$sMo = $curMo;
			$sDay = $curDay;
		} elsif(param('p') == -3) { # last week
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,6);
		} else {
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,$dayCnt-1);
			if(&DeltaDays($sYr,$sMo,$sDay,$curYr,$curMo,$curDay) < 7) {
				$sYr = $curYr;
				$sMo = $curMo;
				$sDay = $curDay;				
			} else {
				($mYr,$mMo,$mDay) = &MondayOfWeek($sYr,$sMo,$sDay);
				($sYr,$sMo,$sDay) = &AddDeltaDays($mYr,$mMo,$mDay,6);
			}
		}
		($mYr,$mMo,$mDay) = &MondayOfWeek($sYr,$sMo,$sDay);
		$period = "$mMo/$mDay/$mYr";
		$dataCnt = 26;
		($xYr,$xMo,$xDay) = &AddDeltaDays($sYr,$sMo,$sDay,-7*$dataCnt); 
		($xYr,$xMo,$xDay) = &AddDeltaDays($xYr,$xMo,$xDay,7); 
		($mYr,$mMo,$mDay) = &MondayOfWeek($xYr,$xMo,$xDay);
		$period = "$mMo/$mDay/$mYr - $period";
		for($i=0;$i<$dataCnt;$i++) {
			push(@xLables,"$mMo/$mDay/$mYr");
			push(@data, [ (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ]);
			($xYr,$xMo,$xDay) = &AddDeltaDays($xYr,$xMo,$xDay,7); 
			($mYr,$mMo,$mDay) = &MondayOfWeek($xYr,$xMo,$xDay);
		}
	} else {
		$per = 'D';
		$endDate = "D$sYr/$sMo/$sDay";
		$dataCnt = 30;
		($xYr,$xMo,$xDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1 * $dataCnt); 
		($xYr,$xMo,$xDay) = &AddDeltaDays($xYr,$xMo,$xDay,1);
		$period = "$xMo/$xDay/$xYr - $sMo/$sDay/$sYr";
		for($i=0;$i<$dataCnt;$i++) {			 
			push(@xLables,"$xMo/$xDay/$xYr");
			push(@data, [ (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ]);
			($xYr,$xMo,$xDay) = &AddDeltaDays($xYr,$xMo,$xDay,1);
		}
	}
	$endDate = "$sMo/$sDay/$sYr";
	
	$daysFound = 0;
	if((param('tft') eq 'Pa') && (param('fft') eq '')) {
		&genHistData2();
	} elsif((param('fft') ne '') && (param('tft') eq '')) {
		&genHistData3();
	} elsif((param('fft') ne '') && (param('tft') eq 'Pg')) {
		&genHistData4();
	} elsif((param('fft') ne '') && (param('tft') eq 'Pa')) {
		&genHistData5();
	} else {
		&genHistData();
	}
	
	$startDate="$sMo/$sDay/$sYr";
	if(param('format') > 0) {
		if($daysFound == 0) {
			&retNoData()
		} else {
			open (FILE, "$acct/L10HC_PageL.dat") || &retNoData();
			@pageList = <FILE>;
			close(FILE);
			&setRepTime();
			$iD = "\t";
			$sD = "";
			$eD = "\n";
			$lb = "";
			if(param('format') eq '1') {
				print "Content-type:  text/plain\n\n";
			} else {
				print header;
				print '<html><header><title>History Report</title><style>td  {font-family : Arial, Helvetica, sans-serif; font-size : 8pt;}</style></header><body><table border=1 cellspacing=0 cellspacing=1>';
				$iD = '</td><td align=right> ';
				$sD = ' <tr><td> ';
				$eD = ' </td></tr>'."\n";
				$lb = '<br>';
			}
			print $sD."History".$eD;
			print $sD."Run Time: $repDate $repTime$siteTitle".$eD;
			print $sD."Date Range: $startDate-$endDate ($daysFound/$dayCnt found)".$eD;
			print $sD.&getToFilterStr().$eD;
			print $sD.&getFromFilterStr().$eD;
			print $sD.$eD;
			print $sD."Page".$iD."Page Hits".$iD."Entries$lb All".$iD."Entries$lb Uniques".$iD."Entries$lb New".$iD."Exits$lb All".$iD."Exits$lb Uniques".$iD."Exits$lb New".$iD."Conv.$lb All".$iD."Conv.$lb Uniques".$iD."Conv.$lb New".$iD."Success$lb All".$iD."Success$lb Uniques".$iD."Success$lb New".$iD."Active Sessions".$iD."Reloads".$iD."Total Time".$iD."Average Time".$eD;
			for($i=0;$i<=$#data;$i++) {
				print $sD.$xLables[$i].$iD.$data[$i][3].$iD.$data[$i][0].$iD.$data[$i][1].$iD.$data[$i][2].$iD.$data[$i][5].$iD.$data[$i][6].$iD.$data[$i][7].$iD.$data[$i][8].$iD.$data[$i][9].$iD.$data[$i][10].$iD.$data[$i][11].$iD.$data[$i][12].$iD.$data[$i][13].$iD.$data[$i][4].$iD.$data[$i][14].$iD.$data[$i][15].$iD.( (($data[$i][3]-$data[$i][4]-$data[$i][5]) > 0) ? &roundNum($data[$i][15]/($data[$i][3]-$data[$i][4]-$data[$i][5]),1) : 0).$eD;
			}
			print $sD.$eD;
			if(param('format') ne '1') {
				print '</table></body></html>';
			}
		}
	} else {
		if($daysFound == 0) {
			&retNoData()
		} else {
			&setRepTime();
			print header;
			print "res=OK&TR=$total&";
			print "Date=$startDate - $endDate&";
			print "Run=$repDate $repTime$siteTitle&";
			print "ffs=".&getFromFilterStr()."&tfs=".&getToFilterStr()."&";
			@totals = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
			for($i=0;$i<=$#data;$i++) {
				print "X$i=$xLables[$i]&A$i=$data[$i][0]&B$i=$data[$i][1]&C$i=$data[$i][2]&D$i=$data[$i][3]&E$i=$data[$i][4]&F$i=$data[$i][5]&G$i=$data[$i][6]&H$i=$data[$i][7]&I$i=$data[$i][8]&J$i=$data[$i][9]&K$i=$data[$i][10]&L$i=$data[$i][11]&M$i=$data[$i][12]&N$i=$data[$i][13]&O$i=$data[$i][14]&P$i=$data[$i][15]&";				
				for($j=0;$j<=15;$j++) {
					$totals[$j] += $data[$i][$j];
				}
			}
			print "AS=$totals[0]&BS=$totals[1]&CS=$totals[2]&DS=$totals[3]&ES=$totals[4]&FS=$totals[5]&GS=$totals[6]&HS=$totals[7]&IS=$totals[8]&JS=$totals[9]&KS=$totals[10]&LS=$totals[11]&MS=$totals[12]&NS=$totals[13]&OS=$totals[14]&PS=$totals[15]&";				
			print "iCount=$dataCnt&perCode=$per";
		}
	}	
}

sub genHistData() {
	if(param('tft') eq 'Pg') {
		open (FILE, "$acct/L10HC_PageL.dat") || &gen_error("Cannot open $acct/L10HC_PageL.dat at \"Read Today's Stats Data\"");
		@pgLFile = <FILE>;
		close(FILE);
		open (FILE, "$acct/L10HC_PageI.dat") || &gen_error("Cannot open $acct/L10HC_PageI.dat at \"Read Today's Stats Data\"");
		@pgIFile = <FILE>;
		close(FILE);

		$pg = &filterPageURL(param('tf'));
		@res = &bSearch($pg,\@pgLFile,1,\@pgIFile,1);
		if(!$res[0]) {
			print header;
			print "res=Err&msg=To page not found! pg=$pg";
			exit 0;
		} else {
			$pgI = $res[1]*5+1;
		}
	} else {
		$pgID = 0;
	}
	for($i=$dataCnt-1;$i>=0;$i--) {
		if($per eq 'Y') {
			$nYr = $sYr-1;
			$nextDate = "12/31/$nYr";
		} elsif($per eq 'M') {
			$nYr = $sYr;
			$nMo = $sMo - 1;
			if($nMo < 1) {
				$nYr --;
				$nMo += 12;
			}
			$nDay = $DpMo[$nMo];
			$nextDate = "$nMo/$nDay/$nYr";
		} elsif($per eq 'W') {
			($mYr,$mMo,$mDay) = &MondayOfWeek($sYr,$sMo,$sDay);
			($nYr,$nMo,$nDay) = &AddDeltaDays($mYr,$mMo,$mDay,-1);			
			$nextDate = "$nMo/$nDay/$nYr";
		} else {
			($nYr,$nMo,$nDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
			$nextDate = "$nMo/$nDay/$nYr";
		}

		$j = 0;
# print "set-$nextDate = $sMo/$sDay/$sYr<br>";
		while ($nextDate ne "$sMo/$sDay/$sYr") {			
# print "lop-$nextDate = $sMo/$sDay/$sYr<br>";
			if(-e &getFileDateStr('Hits','D',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr('Hits','D',$sYr,$sMo,$sDay)) || &retNoData();
				@dFile = <FILE>;
				close(FILE);
				$daysFound ++;
				
				if($#dFile >= $pgI) {
					chop($dFile[$pgID]);

					@t = split(/\t/,$dFile[$pgI]);
					for($k=0;$k<=15;$k++) {
						$data[$i][$k] += $t[$k];
					}
				}
				
			} elsif(&beforeInit($sYr,$sMo,$sDay)) {
				$i = -1;
				last;
			}			
			
			if($j > $dayCnt) {
				print "loop cnt exceeded ($j)<br>";
				$i = -1;
				last;
			}
			$j++;
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);

		}	
	
	}
	
}

# Hist by Path, No From Filter

sub genHistData2() { 
	$pa = param('tf');
	$c1 = (($pa =~ m/\*/) || ($pa =~ m/\,/)) ? 1 : 0;
	$c2 = ($pa =~ m/\*/) ? 1 : 0; 
	for($i=$dataCnt-1;$i>=0;$i--) {
		if($per eq 'Y') {
			$nYr = $sYr-1;
			$nextDate = "12/31/$nYr";
		} elsif($per eq 'M') {
			$nYr = $sYr;
			$nMo = $sMo - 1;
			if($nMo < 1) {
				$nYr --;
				$nMo += 12;
			}
			$nDay = $DpMo[$nMo];
			$nextDate = "$nMo/$nDay/$nYr";
		} elsif($per eq 'W') {
			($mYr,$mMo,$mDay) = &MondayOfWeek($sYr,$sMo,$sDay);
			($nYr,$nMo,$nDay) = &AddDeltaDays($mYr,$mMo,$mDay,-1);			
			$nextDate = "$nMo/$nDay/$nYr";
		} else {
			($nYr,$nMo,$nDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
			$nextDate = "$nMo/$nDay/$nYr";
		}

		$j = 0;
		while ($nextDate ne "$sMo/$sDay/$sYr") {			
			if(-e &getFileDateStr('Paths','D',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr('Paths','D',$sYr,$sMo,$sDay)) || &retNoData();
				@dFile = <FILE>;
				close(FILE);
				open (FILE, &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) || &retNoData();
				@paLFile = <FILE>;
				close(FILE);
				open (FILE, &getFileDateStr('Paths','I',$sYr,$sMo,$sDay)) || &retNoData();
				@paIFile = <FILE>;
				close(FILE);
				$daysFound ++;	
				
				@res = &bSearch($pa,\@paLFile,1,\@paIFile,1);
				if(!$res[0]) {
					($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
					next;
				} else {
					$paI = $res[1];
				}
				
				if($#dFile >= $paI) {
					chop($dFile[$paI]);
					@t = split(/\t/,$dFile[$paI]);
					$data[$i][0] += $t[0];
					$data[$i][1] += $t[1];
					$data[$i][2] += $t[2];
				}
			} elsif(&beforeInit($sYr,$sMo,$sDay)) {
				$i = -1;
				last;
			}
			

			
			
			if($j > $dayCnt) {
				print "loop cnt exceeded ($j)<br>";
				$i = -1;
				last;
			}
			$j++;
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);

		}	

		if($c1) {
			$data[$i][8] = $data[$i][0];
			$data[$i][9] = $data[$i][1];
			$data[$i][10] = $data[$i][2];
		}
		if($c2) {
			$data[$i][11] = $data[$i][0];
			$data[$i][12] = $data[$i][1];
			$data[$i][13] = $data[$i][2];		
		}
	
	}	
}

# Hist From Filter, no To Filter

sub genHistData3() { 
	$rFileName = 'Doms';
	$ref = param('ff');
	if($ref eq '[No Referrer]') {
		$ref = '';
	}
	if(param('fft') eq 'URL') {
		$rFileName = 'Refs';
	} elsif(param('fft') eq 'SE') {
		$rFileName = 'SEs';
	} elsif(param('fft') eq 'SEKW') {
		$rFileName = 'SEKWs';
	} elsif(param('fft') eq 'KW') {
		$rFileName = 'KWs';
	} elsif(param('fft') eq 'RT') {
		$rFileName = 'rTypes';
		$ref = &getRTypeID(param('ff'));
	}
	for($i=$dataCnt-1;$i>=0;$i--) {
		if($per eq 'Y') {
			$nYr = $sYr-1;
			$nextDate = "12/31/$nYr";
		} elsif($per eq 'M') {
			$nYr = $sYr;
			$nMo = $sMo - 1;
			if($nMo < 1) {
				$nYr --;
				$nMo += 12;
			}
			$nDay = $DpMo[$nMo];
			$nextDate = "$nMo/$nDay/$nYr";
		} elsif($per eq 'W') {
			($mYr,$mMo,$mDay) = &MondayOfWeek($sYr,$sMo,$sDay);
			($nYr,$nMo,$nDay) = &AddDeltaDays($mYr,$mMo,$mDay,-1);			
			$nextDate = "$nMo/$nDay/$nYr";
		} else {
			($nYr,$nMo,$nDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
			$nextDate = "$nMo/$nDay/$nYr";
		}

		$j = 0;
		while ($nextDate ne "$sMo/$sDay/$sYr") {	

			if(-e &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr('sRefs','D',$sYr,$sMo,$sDay)) || &retNoData();
				@dFile = <FILE>;
				close(FILE);
				open (FILE, &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) || &retNoData();
				@refLFile = <FILE>;
				close(FILE);
				open (FILE, &getFileDateStr($rFileName,'I',$sYr,$sMo,$sDay)) || &retNoData();
				@refIFile = <FILE>;
				close(FILE);
				$daysFound ++;	
				
				@res = &bSearch($ref,\@refLFile,1,\@refIFile,1,1);
				if(!$res[0]) {
					($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
					next;
				}
				
				for($k=$res[1];$k<=$res[2];$k++) {
					$refI = $refIFile[$k];
					if($#dFile >= $refI) {
						chop($dFile[$refI]);
						@t = split(/\t/,$dFile[$refI]);
						$data[$i][1] += $t[0];
						$data[$i][9] += $t[1];
						$data[$i][12] += $t[2];
					}
				}
			} elsif(&beforeInit($sYr,$sMo,$sDay)) {
				$i = -1;
				last;
			}
			

			
			
			if($j > $dayCnt) {
				print "loop cnt exceeded ($j)<br>";
				$i = -1;
				last;
			}
			$j++;
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);

		}	

	}	
}

# Hist From Filter, Page To Filter

sub genHistData4() { 
	open (FILE, "$acct/L10HC_PageL.dat") || &gen_error("Cannot open $acct/L10HC_PageL.dat at \"Read Today's Stats Data\"");
	@pgLFile = <FILE>;
	close(FILE);
	open (FILE, "$acct/L10HC_PageI.dat") || &gen_error("Cannot open $acct/L10HC_PageI.dat at \"Read Today's Stats Data\"");
	@pgIFile = <FILE>;
	close(FILE);

	$pg = &filterPageURL(param('tf'));
	@res = &bSearch($pg,\@pgLFile,1,\@pgIFile,1);
	if(!$res[0]) {
		print header;
		print "res=Err&msg=To page not found! pg=$pg";
		exit 0;
	} else {
		$pgI = $res[1]*4;
	}
	
	%refIndexes = ();
	$rFileName = 'Doms';
	$ref = param('ff');
	if($ref eq '[No Referrer]') {
		$ref = '';
	}
	if(param('fft') eq 'URL') {
		$rFileName = 'Refs';
	} elsif(param('fft') eq 'SE') {
		$rFileName = 'SEs';
	} elsif(param('fft') eq 'SEKW') {
		$rFileName = 'SEKWs';
	} elsif(param('fft') eq 'KW') {
		$rFileName = 'KWs';
	} elsif(param('fft') eq 'RT') {
		$rFileName = 'rTypes';
		$ref = &getRTypeID(param('ff'));
	}
	for($i=$dataCnt-1;$i>=0;$i--) {
		if($per eq 'Y') {
			$nYr = $sYr-1;
			$nextDate = "12/31/$nYr";
		} elsif($per eq 'M') {
			$nYr = $sYr;
			$nMo = $sMo - 1;
			if($nMo < 1) {
				$nYr --;
				$nMo += 12;
			}
			$nDay = $DpMo[$nMo];
			$nextDate = "$nMo/$nDay/$nYr";
		} elsif($per eq 'W') {
			($mYr,$mMo,$mDay) = &MondayOfWeek($sYr,$sMo,$sDay);
			($nYr,$nMo,$nDay) = &AddDeltaDays($mYr,$mMo,$mDay,-1);			
			$nextDate = "$nMo/$nDay/$nYr";
		} else {
			($nYr,$nMo,$nDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
			$nextDate = "$nMo/$nDay/$nYr";
		}

		$j = 0;
		while ($nextDate ne "$sMo/$sDay/$sYr") {			
			if(-e &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr('pgRefs','IbPg',$sYr,$sMo,$sDay)) || &retNoData();
				@dFile = <FILE>;
				close(FILE);
				open (FILE, &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) || &retNoData();
				@refLFile = <FILE>;
				close(FILE);
				open (FILE, &getFileDateStr($rFileName,'I',$sYr,$sMo,$sDay)) || &retNoData();
				@refIFile = <FILE>;
				close(FILE);
				$daysFound ++;	
				
				@res = &bSearch($ref,\@refLFile,1,\@refIFile,1,1);
				if(!$res[0]) {
					($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
					next;
				} else {
					%refIndexes = ();
					for($k=$res[1];$k<=$res[2];$k++) {
						$refIndexes{$refIFile[$k]} = 1;
					}
				}
				chop($dFile[$pgI]);
				chop($dFile[$pgI+1]);
				chop($dFile[$pgI+2]);
				chop($dFile[$pgI+3]);
				@ta = split(/\t/,$dFile[$pgI]);
				@tb = split(/\t/,$dFile[$pgI+1]);
				@tc = split(/\t/,$dFile[$pgI+2]);
				@td = split(/\t/,$dFile[$pgI+3]);
				for($k=0;$k<=$#ta;$k++) {
					if(exists $refIndexes{"$ta[$k]\n"}) {
						$data[$i][1] += $tb[$k];
						$data[$i][9] += $tc[$k];
						$data[$i][12] += $td[$k];
					}

				}
			} elsif(&beforeInit($sYr,$sMo,$sDay)) {
				$i = -1;
				last;
			}			
			
			if($j > $dayCnt) {
				print "loop cnt exceeded ($j)<br>";
				$i = -1;
				last;
			}
			$j++;
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);

		}	

	}	
}

# Hist From Filter, Path To Filter

sub genHistData5() { 
	$pa = param('tf');
	$c1 = (($pa =~ m/\*/) || ($pa =~ m/\,/)) ? 1 : 0;
	$c2 = ($pa =~ m/\*/) ? 1 : 0; 
	
	%refIndexes = ();
	$rFileName = 'Doms';
	$ref = param('ff');
	if($ref eq '[No Referrer]') {
		$ref = '';
	}
	if(param('fft') eq 'URL') {
		$rFileName = 'Refs';
	} elsif(param('fft') eq 'SE') {
		$rFileName = 'SEs';
	} elsif(param('fft') eq 'SEKW') {
		$rFileName = 'SEKWs';
	} elsif(param('fft') eq 'KW') {
		$rFileName = 'KWs';
	} elsif(param('fft') eq 'RT') {
		$rFileName = 'rTypes';
		$ref = &getRTypeID(param('ff'));
	}
	for($i=$dataCnt-1;$i>=0;$i--) {
		if($per eq 'Y') {
			$nYr = $sYr-1;
			$nextDate = "12/31/$nYr";
		} elsif($per eq 'M') {
			$nYr = $sYr;
			$nMo = $sMo - 1;
			if($nMo < 1) {
				$nYr --;
				$nMo += 12;
			}
			$nDay = $DpMo[$nMo];
			$nextDate = "$nMo/$nDay/$nYr";
		} elsif($per eq 'W') {
			($mYr,$mMo,$mDay) = &MondayOfWeek($sYr,$sMo,$sDay);
			($nYr,$nMo,$nDay) = &AddDeltaDays($mYr,$mMo,$mDay,-1);			
			$nextDate = "$nMo/$nDay/$nYr";
		} else {
			($nYr,$nMo,$nDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
			$nextDate = "$nMo/$nDay/$nYr";
		}

		$j = 0;
		while ($nextDate ne "$sMo/$sDay/$sYr") {			
			if(-e &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) {
				open (FILE, &getFileDateStr('Paths','L',$sYr,$sMo,$sDay)) || &retNoData();
				@paLFile = <FILE>;
				close(FILE);
				open (FILE, &getFileDateStr('Paths','I',$sYr,$sMo,$sDay)) || &retNoData();
				@paIFile = <FILE>;
				close(FILE);
				$daysFound ++;	
				
				@res = &bSearch($pa,\@paLFile,1,\@paIFile,1);
				if(!$res[0]) {
					($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
					next;
				} else {
					$paI = $res[1]*2;
				}
				
				if(-e &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) {
					open (FILE, &getFileDateStr('paRefs','IbPa',$sYr,$sMo,$sDay)) || &retNoData();
					@dFile = <FILE>;
					close(FILE);
					open (FILE, &getFileDateStr($rFileName,'L',$sYr,$sMo,$sDay)) || &retNoData();
					@refLFile = <FILE>;
					close(FILE);
					open (FILE, &getFileDateStr($rFileName,'I',$sYr,$sMo,$sDay)) || &retNoData();
					@refIFile = <FILE>;
					close(FILE);

					@res = &bSearch($ref,\@refLFile,1,\@refIFile,1,1);
					if(!$res[0]) {
						($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);
						next;
					} else {
						%refIndexes = ();
						for($k=$res[1];$k<=$res[2];$k++) {
							$refIndexes{$refIFile[$k]} = 1;
						}
					}
					chop($dFile[$paI]);
					chop($dFile[$paI+1]);
					@ta = split(/\t/,$dFile[$paI]);
					@tb = split(/\t/,$dFile[$paI+1]);
					for($k=0;$k<=$#ta;$k++) {
						if(exists $refIndexes{"$ta[$k]\n"}) {
							$data[$i][1] += $tb[$k];
							$data[$i][9] += $tc[$k];
							$data[$i][12] += $td[$k];
						}

					}
				} elsif(&beforeInit($sYr,$sMo,$sDay)) {
					$i = -1;
					last;
				}				
				
			} elsif(&beforeInit($sYr,$sMo,$sDay)) {
				$i = -1;
				last;
			}			
			
			if($j > $dayCnt) {
				print "loop cnt exceeded ($j)<br>";
				$i = -1;
				last;
			}
			$j++;
			($sYr,$sMo,$sDay) = &AddDeltaDays($sYr,$sMo,$sDay,-1);

		}
		if($c1) {
			$data[$i][8] = $data[$i][0];
			$data[$i][9] = $data[$i][1];
			$data[$i][10] = $data[$i][2];
		}
		if($c2) {
			$data[$i][11] = $data[$i][0];
			$data[$i][12] = $data[$i][1];
			$data[$i][13] = $data[$i][2];		
		}

	}	
}


sub periodReport() {
	&setRepTime();
	print header;
	print "Run=$repDate $repTime$siteTitle&";
	print "Date=$repDate\&";
	print "Time=$repTime\&";
	open (FILE, "$acct/L10HC_Archive/Hits_byPeriod.dat") || &gen_error("$acct/L10HC_Archive/Hits_byPeriod.dat at \"Read Today's Stats Data\"");
	@bStat = <FILE>;
	close(FILE);
	
	@d = ();
	@s1 = ();
	@s2 = ();
	@ave = ();
	@wave = ();
	
	$iMod = 0;
	if(param('c') eq '1') {
		$iMod = 1;
	}
	if(param('p') eq "2") {
		@d = split(/\t/,$bStat[16]);
		@ave = split(/\t/,$bStat[17+$iMod]);
		@wave = split(/\t/,$bStat[19+$iMod]);
		@s1 = split(/\t/,$bStat[21+$iMod]);
		@s2 = split(/\t/,$bStat[23+$iMod]);
	} elsif(param('p') eq "1") {
		@d = split(/\t/,$bStat[7]);
		@ave = split(/\t/,$bStat[8+$iMod]);
		@wave = split(/\t/,$bStat[10+$iMod]);
		@s1 = split(/\t/,$bStat[12+$iMod]);
		@s2 = split(/\t/,$bStat[14+$iMod]);
	} else {
		chop($bStat[0]);
		for($i=0;$i<24;$i++) {
			push(@d,$bStat[0]);	
		}
		@ave = split(/\t/,$bStat[1+$iMod]);
		@wave = split(/\t/,$bStat[3+$iMod]);
		@s2 = split(/\t/,$bStat[5+$iMod]);
		open (DSTAT_FH, "$acct/L10HC_Hits.dat") || &gen_error("Cannot open $acct/L10HC_Hits.dat at \"Read Today's Stats Data\"");
		@dStat = <DSTAT_FH>;
		close(DSTAT_FH);
		@s1 = split(/\t/,$dStat[4+$iMod]);
	}
	for($i=0;$i<=$#d;$i++) {
		print "d$i=$d[$i]&";
		print "s1$i=$s1[$i]&";
		print "s2$i=$s2[$i]&";
		print "ave$i=$ave[$i]&";
		print "wave$i=$wave[$i]&";	
	}
	
}



sub extendedReport() {
	$theFile = "";
	&setRepTime();
	print header;
	print "Run=$repDate $repTime$siteTitle&";
	print "res=OK&TR=$total&DF=$daysFound&DS=$dayCnt&";
	print "Date=$repDate&Time=$repTime&";
	print "SD=$startDate&ED=$endDate&";
	if(param('b') eq "OS") {
		$theFile = "OSs";			
	} elsif(param('b') eq "Browser") {
		$theFile = "Browsers";
	} elsif(param('b') eq "BrowserVer") {
		$theFile = "BrowserVers";
	} elsif(param('b') eq "Language") {
		$theFile = "Languages";
	} elsif(param('b') eq "ScreenRes") {
		$theFile = "ScreenRes";
	} elsif(param('b') eq "ScreenClr") {
		$theFile = "ScreenClrs";
	}
	if(-e "$acct/L10HC_Archive/$theFile.dat") {
		open (FILE, "$acct/L10HC_Archive/$theFile.dat") || &gen_error("Cannot open $acct/L10HC_Archive/$theFile.dat at archiveStats() 2");
		$i=0;
		$total = 0;
		foreach (<FILE>) {
			chop($_);
			@l = split(/\t/,$_);
			print "k$i=$l[0]&v$i=$l[1]&";
			$total += $l[1];
			$i++;
		}
		close (FILE);
		print "total=$total";
	} else {
		&retNoData();
	}
}

sub getReportDateRange() {
	my $dayCnt = 0;
	if(param('p') == 0) { # Today
		$sYr = $curYr;
		$sMo = $curMo;
		$sDay = $curDay;
		$dayCnt = 1;
	} elsif(param('p') == -1) { # Yesterday
		($sYr,$sMo,$sDay) = &AddDeltaDays($curYr,$curMo,$curDay,-1);
		$dayCnt = 1;
	} elsif(param('p') == -2) { # This Week
		($sYr,$sMo,$sDay) = &MondayOfWeek($curYr,$curMo,$curDay);
		$dayCnt = 7;
	} elsif(param('p') == -3) { # Last Week
		($sYr,$sMo,$sDay) = &AddDeltaDays($curYr,$curMo,$curDay,-7);
		($sYr,$sMo,$sDay) = &MondayOfWeek($sYr,$sMo,$sDay);
		$dayCnt = 7;
	} elsif(param('p') == -4) { # This Month
		$sYr = $curYr;
		$sMo = $curMo;
		$sDay = 1;
		$dayCnt = $DpMo[$sMo];
	} elsif(param('p') == -5) { # Last Month
		($sYr,$sMo,$sDay) = &AddDeltaDays($curYr,$curMo,$curDay,-$DpMo[$curMo]);
		$sDay = 1;
		$dayCnt = $DpMo[$sMo];
	} elsif(param('p') == -6) {
		$sYr = $curYr;
		$sMo = 1;
		$sDay = 1;
		$dayCnt = 365 + &isLeapYr($sYr);
	} elsif(param('p') == -7) {
		$sYr = $curYr-1;
		$sMo = 1;
		$sDay = 1;
		$dayCnt = 365 + &isLeapYr($sYr);
	} else {
		($sYr,$sMo,$sDay) = &AddDeltaDays(param('bY'),param('bM'),param('bD'),1-param('p'));	
		$dayCnt = param('p');
	}
	my @t = ($sYr,$sMo,$sDay,$dayCnt);
	return @t;
}

sub retNoData() {
	print header;
	print "res=Err&msg=No data was found for the given time period.";
	exit 0;
}

sub changeParams() {
	if(param('param') eq "msgs") {
		@phrases = ();
		for($i=0;param("m$i") ne "";$i++) {
			$str = param("m$i");
			$str =~ s/\%/\%25/g;
			$str =~ s/\&amp;/\%26/g;
			$str =~ s/\+/\%2B/g;			
			push(@phrases,$str);
		}
	} elsif(param('param') eq "displayOptions") {
		$bTagClr = param('bTagClr');
		$removeDisplay = param('removeDisplay');
		$enableAdminLink = param('enableAdminLink');
	} elsif(param('param') eq "browserTracking") {
		@blockIPs = split(/\,/,param('blockIPs'));
	} elsif(param('param') eq "password") {
		if(param('newPW') ne "") {
			$password = param('newPW');
		}
		$protectStats = param('protectStats');
	} elsif(param('param') eq "timeAdj") {
		$timeAdj = param('timeAdj');
	} elsif(param('param') eq "reports") {
		$siteTitle = param('siteTitle');
		$maxRepItems = param('maxRepItems');
	} elsif(param('param') eq "filters") {
		$indexPage= param('indexPg');
		@validDoms = ();
		for($i=0;param("vd$i") ne "";$i++) {
			$str = param("vd$i");
			push(@validDoms,$str);
		}
	}

	&writeAcctParams();
	
	print header;
	print "res=OK";
}

sub setCookie() {
	open (IMG, "L10HC_Img_L.gif") || &gen_error("Cannot open L10HC_Img_L.gif at Admin.setCookie()");
	@imgd = <IMG>;
	print "Content-type:  image/gif\n";
	print "Set-Cookie: ".param(k)."=".param(v).";";		
	print " expires=Fri, 31-Dec-10 00:00:01 GMT; \n\n";
	foreach (@imgd) {
		print $_;
	}
	close(IMG);
}

sub removeCookie() {
	open (IMG, "L10HC_Img_L.gif") || &gen_error("Cannot open L10HC_Img_L.gif at Admin.setCookie()");
	@imgd = <IMG>;
	print "Content-type:  image/gif\n";
	print "Set-Cookie: ".param(k)."=".param(v).";";		
	print " expires=Thu, 01-Jan-70 00:00:01 GMT; \n\n";
	foreach (@imgd) {
		print $_;
	}
	close(IMG);
}

sub updateKC() {
	print header;
	unless($ENV{'HTTP_REFERER'} =~ m/^http:\/\/www.leveltendesign.com\//) {
		print "invalid ref!";
		exit 0;
	}

	$keyCode = param('kc');
	$kcErr = param('kce');
	$removeBranding = param('rb');
	$datVer = param('datVer');
	
	&writeParams();
	
	if(param('SE') ne "") {
		$newFile = param('SE');
		$newFile =~ s/\=/\t/g;
		$newFile =~ s/\&/\n/g;
		open (FILE, ">L10HC_SE.txt") || &gen_error("Cannot open L10HC_SE.txt at updateLC");
		print FILE $newFile;
		close(FILE);
		
	}
	if(param('SD') ne "") {
		$newFile = param('SD');
		$newFile =~ s/\=/\t/g;
		$newFile =~ s/\&/\n/g;
		open (FILE, ">L10HC_SD.txt") || &gen_error("Cannot open L10HC_SD.txt at updateLC");
		print FILE $newFile;
		close(FILE);
	}
	if(param('OS') ne "") {
		$newFile = param('OS');
		$newFile =~ s/\=/\t/g;
		$newFile =~ s/\&/\n/g;
		open (FILE, ">L10HC_OSs.txt") || &gen_error("Cannot open L10HC_OSs.txt at updateLC");
		print FILE $newFile;
		close(FILE);
	}
	if(param('SE') ne "") {
		$newFile = param('Lang');
		$newFile =~ s/\=/\t/g;
		$newFile =~ s/\&/\n/g;
		open (FILE, ">L10HC_Languages.txt") || &gen_error("Cannot open L10HC_SE.txt at updateLC");
		print FILE $newFile;
		close(FILE);
	}

	
	
	print "<html><head><title>L10 Hit Counter Update</title></head><body style={font-family : arial, helvetica, sans-serif}><table width=500 align=center><tr><td>\n";
	print param('msg');
	print "\n</td></tr></table></body></html>";

	exit 0;	
}

sub updateNav() {
# &log_event("admin updateNav()");
	unless(&lock_stats()) {
		print header;
		print "res=Err&msg=File lock timeout exceeded. Try again after a few minutes.";
		exit 0;
	}
	&readNav();
	$navIndex = -1;
	&writeNav();
	&writeHitsArchive();
	&unlock_stats();
}

sub getToFilterStr() {
	$str = '';
	if(param('tft') eq 'Pg') {
		$str = 'To Page: '.&filterPageURL(param('tf'));
	} elsif(param('tft') eq 'Pa') {
		$str = 'To Path: '.param('tf');
	} else {
		$str = 'To: All Pages';	
	}
	if(length(param('b2')) > 1) {
		$str .= "\nFrom Type: ".param('b2');
	}
	return $str;
}

sub getFromFilterStr() {
	if(param('fft') eq 'Dom') {
		return 'From Domain: '.param('ff');
	} elsif(param('fft') eq 'URL') {
		return 'From URL: '.param('ff');
	} elsif(param('fft') eq 'SE') {
		return 'From Search Engine: '.param('ff');
	} elsif(param('fft') eq 'KW') {
		return 'From Keyword: '.param('ff');
	} elsif(param('fft') eq 'SEKW') {
		return 'From SE Keyword: '.param('ff');
	} elsif(param('fft') eq 'RT') {
		return 'From Referrer Type: '.param('ff');
	}
	return "From: All Referrers";
}

sub beforeInit() {
	my ($y,$m,$d) = @_;
	if($startYr > $y) {
		return 1;
	} elsif($startYr == $y) {
		if($startMo > $m) {
			return 1;
		} elsif($startMo == $m) {
			if($startDay > $d) {
				return 1;
			} else {
				return 0;
			}
		} else {
			return 0;
		}
	} else {
		return 0;
	}
		

}

sub getRTypeID() {
	my ($item) = @_;
	
	open (FILE, "$acct/L10HC_Archive/rTypes/rTypeL.dat") || &gen_error("Cannot open $acct/L10HC_Archive/rTypes/rTypeL.dat at \"Read Today's Stats Data\"");
	@t = <FILE>;
	close(FILE);

	open (FILE, "$acct/L10HC_Archive/rTypes/rTypeI.dat") || &gen_error("Cannot open $acct/L10HC_Archive/rTypes/rTypeI.dat at \"Read Today's Stats Data\"");
	@t1 = <FILE>;
	close(FILE);

	@res = &bSearch($item,\@t,1,\@t1,1);
	if(!$res[0]) {
		print header;
		print "res=Err&msg=Referrer type not found! rType=".param('b2');
		exit 0;
	} else {
		return $res[1];
	}
	
}

