#!/usr/bin/perl -i

# v3.16 1/1/04

use CGI ':standard';

if(param('i') ne '') {
	&retImg();
}

$removeQueryStr = 0; #temp
@queryStrFilters = (); #temp

if(param('acct') eq '') {
	$acct = '.';
	$acct2 = '';
} else {
	$acct = param('acct');
	$acct2 = $acct;
}
$acct = $dataDir.$acct;

if(-e "$acct/L10HC_AcctParams.pl") {
	require "$acct/L10HC_AcctParams.pl";
} elsif(param('action') ne 'init') {
	print header;
	print "res=Err&msg=Invalid Account - ".param('acct');
	exit 0;
}



require "L10HC_Params.pl";
require "L10HC_LIB.pl";

$fDateStr = "$curYr2";
if($curMo < 10) { $fDateStr .= "0$curMo"; } else {$fDateStr .= $curMo;}
if($curDay < 10) { $fDateStr .= "0$curDay"; } else {$fDateStr .= $curDay;}

@cookies = split(/;/,$ENV{'HTTP_COOKIE'});
$visitorLevel = 0;
$cookiesEnabled = 0;
$jSEnabled = 0;
$blockBrowser = 0;
$visitID = 0;
$cPgID = -1;
$cPgDt = '';
$lPgID = -1;
$lPgDt = '';
$pgTm = 0;
$newPage = 0;
@IPlog = (0,0);
@exits = ();
$reload = 0;
$success = 0;
$customURL = 0;
$IP = $ENV{'REMOTE_ADDR'};


foreach (@cookies) {
	($cKey,$cValue) = split(/=/,$_);
	if($cKey =~ m/L10HC_LV_$acct2/) {
		@vDate = split(/\//,$cValue);
# &log_event($ENV{'REMOTE_ADDR'}.",cookie-$cKey=$cValue"); # debug
		$visitID = @vDate[6];
		if(&moreThan24Hrs($vDate[2],$vDate[0],$vDate[1],$vDate[3],$curYr,$curMo,$curDay,$curHr)) {
			$visitorLevel = 4;
		} else {
			$visitorLevel = 6;
		}
		$cookiesEnabled = 1;
		if((@vDate[7] <= 5) && ($vDate[3] == $curDay)) {
			open(FILE, "$acct/L10HC_IPL.dat") || &gen_error("Cannot open $acct/L10HC_IPL.dat at \"Read Today's Stats Data\"");
			@t = <FILE>;
			close(FILE);	
			chop($t[$vDate[8]]);
			$t[$vDate[8]] .= "-\n";
			open(FILE, ">$acct/L10HC_IPL.dat") || &gen_error("Cannot open $acct/L10HC_IPL.dat at \"Read Today's Stats Data\"");
			foreach(@t) { print FILE $_; }
			close(FILE);
			open(FILE, "$acct/L10HC_IPD.dat") || &gen_error("Cannot open $acct/L10HC_IPL.dat at \"Read Today's Stats Data\"");
			@t = <FILE>;
			close(FILE);			
			$t[$vDate[8]] = "\n";
			open(FILE, ">$acct/L10HC_IPD.dat") || &gen_error("Cannot open $acct/L10HC_IPL.dat at \"Read Today's Stats Data\"");
			foreach(@t) { print FILE $_; }
			close(FILE);
		}
	} elsif($cKey =~ m/L10HC_CC/) {
		$cookiesEnabled = 1;
		$jSEnabled = 1;
	} elsif($cKey =~ m/L10HC_BB/) {
		if($cValue eq "1") {
			$blockBrowser = 1;
		}
	}
}

@IPL1 = ();
@IPD1 = ();
@IPI1 = ();
@IPL2 = ();
@IPD2 = ();
@IPI2 = ();
if(!$cookiesEnabled || ($visitorLevel == 0)) {
	open (FILE, "$acct/L10HC_IPL.dat") || &gen_error("Cannot open $acct/L10HC_IPL.dat at \"Read Today's Stats Data\"");
	@IPL1 = <FILE>;
	close(FILE);
	open (FILE, "$acct/L10HC_IPI.dat") || &gen_error("Cannot open $acct/L10HC_IPI.dat at \"Read Today's Stats Data\"");
	@IPI1 = <FILE>;
	close(FILE);
	

	@res = &bSearch($IP,\@IPL1,1,\@IPI1,1,1);
	$IPlog[1] = $res[1];
	if($res[0]) {
		$IPlog[0] = 1;
		open (FILE, "$acct/L10HC_IPD.dat") || &gen_error("Cannot open $acct/L10HC_IP.dat at \"Read Today's Stats Data\"");
		@IPD1 = <FILE>;
		close(FILE);
		@ipInfo = split(/\t/,$IPD1[$IPlog[1]]);
		@cDate = split(/\//,$ipInfo[0]);
		$visitID = @ipInfo[1];
		chop($visitID);
		if(($cDate[0] == $curDay) or ($cData[1] < $curHr)) {
			$visitorLevel = 6;
		}		
	} else {
		$IPlog[0] = 0;		
		open (FILE, "$acct/L10HC_IPL2.dat") || &gen_error("Cannot open $acct/L10HC_IPL2.dat at \"Read Today's Stats Data\"");
		@IPL2 = <FILE>;
		close(FILE);
		open (FILE, "$acct/L10HC_IPI2.dat") || &gen_error("Cannot open $acct/L10HC_IPI2.dat at \"Read Today's Stats Data\"");
		@IPI2 = <FILE>;
		close(FILE);

		@res = &bSearch($IP,\@IPL2,1,\@IPI1,1,1);

		if($res[0]) {
			open (FILE, "$acct/L10HC_IPD2.dat") || &gen_error("Cannot open $acct/L10HC_IPD2.dat at \"Read Today's Stats Data\"");
			@IPD2 = <FILE>;
			close(FILE);
			@ipInfo = split(/\t/,$IPD2[$res[0]]);
			@cDate = split(/\//,$ipInfo[0]);
			$visitID = @ipInfo[1];
			chop($visitID);
			if(($cDate[0] == $curDay) or ($cData[1] < $curHr)) {
				$visitorLevel = 6;			
			}
		}
		@IPL2 = undef;
		@IPD2 = undef;
		@IPI2 = undef;
	}
# &log_event("From IP log vID=$visitID");
} else {
# &log_event("From cookie vID=$visitID");
}


if(!($visitID > 0)) {
	$visitID = 0;
}

if(length(param('cPg')) > 0) {
	$url = '`'.param('cPg').'`';
	$customURL = 1;
} elsif(param('pg') ne "") {
	$url = param('pg');
} else {				 
	$url = $ENV{'HTTP_REFERER'};
}


if($url eq "") {
	$url = '[Unknown]';
} else {
	if(!$allowLocalFiles && (param('lfor') ne '1') && ($ENV{'HTTP_REFERER'} !~ m/^https?:\/\//i)) {
		&log_event("Blocked local file. Request from: ".$ENV{'HTTP_REFERER'}."-$url");
		&returnHitImage();
		exit 0;
	}

	if(($#validDoms >= 0) && (param('dvor') ne '1')) {
		$t = $ENV{'HTTP_REFERER'};
		$t =~ s/^https?:\/\///i;
		@t1 = split(/\//,$t);
		$t = 0;
		for($i=0;$i<=$#validDoms;$i++) {
			if($t1[0] =~ m/$validDoms[$i]$/i) {
				$t = 1;
				last;
			}
		}
		if(!$t) {
			&log_event("Blocked invalid domain. Request from: ".$ENV{'HTTP_REFERER'}."-$url-$t1[0]");
			&returnHitImage();
			exit 0;
		}
	}
	$url =~ s/http:\/\///i;
	$url =~ s/https:\/\///i;
	$url =~ s/\&/\%26/g;
	$url =~ s/\/$indexPage/\//i;
	if($removePageWWW) {
		$url =~ s/^www.//i;
	}

}


# &log_event($url);
$ref = '';
$refType = '';
@t = split(/\?/,$url);
$t[1] =~ s/\%26/\&/g;
$t[1] =~ s/\%20/ /g;

@ta = split(/\&/,$t[1]);

for($i=0;$i <= $#ta;$i++) {
	if($ta[$i] =~ m/hcr/i) {
		$ref = '`'.substr($ta[$i],4).'`';
		splice(@ta,$i,1);
		$i--;
	} elsif($ta[$i] =~ m/hct/i) {
		$refType = '`'.substr($ta[$i],4).'`';
		splice(@ta,$i,1);
		$i--;
	} else {
		$match = 0;
		foreach (@queryStrFilters) {			
			if($ta[$i] =~ m/^$_=/i) {
				$match = 1;
				last;
			}
		}
		if(($match && !$removeQueryStr) || (!$match && $removeQueryStr)) {
			splice(@ta,$i,1);
			$i--;
		}
	}
}

if($ref eq '') {
	$ref = param('ref');
	$ref =~ s/http:\/\///i;
	$ref =~ s/https:\/\///i;
	$ref =~ s/\&/\%26/g;
}

if($#ta >= 0) {
	$url = $t[0] . '?' . join("%26",@ta);
} else {
	$url = $t[0];
}

if(param('cR') ne '') {
	$ref = '`'.param('cR').'`';
}

if(param('cRT') ne '') {
	$refType = '`'.param('cRT').'`';
}

# if($lowercaseRef && (substr($ref,0,1) ne '[') && (substr($ref,0,1) ne '`')) {
#	$ref = lc($ref);
# }

if($lowercasePage && (substr($url,0,1) ne '[') && (substr($url,0,1) ne '`')) {
	$url = lc($url);
}

if(param('sa') > 0) {
	$success = param('sa');
}

# &log_event("$IP-vID=$visitID,vL=$visitLevel,pg=$url,ref=$ref");

# read today's stats data
unless(&lock_stats()) {
	&returnHitImage();
	exit 0;
}

############
# Open_Stats

open (DSTAT_FH, "$acct/L10HC_Hits.dat") || &gen_error("Cannot open $acct/L10HC_Hits.dat at Counter.Open_Stats1");
@dStat = <DSTAT_FH>;
close(DSTAT_FH);

if($dStat[0] ne "$dateStamp\n") {
	&log_event("Stats archived by time.");
	require "L10HC_LIB2.pl";
	&archiveStats();
}
 
if(param('action') eq "check") {
	&unlock_stats();
	print header;
	print "res=OK";	
	exit 0;
}

if($blockBrowser) {
	&unlock_stats();
	&returnHitImage();
	&log_event("Blocked by Browser, pg=$url");
	exit 0;
}
for($i=0;$i<=$#blockIPs;$i++) {
	if($IP eq $blockIPs[$i]) {
		&unlock_stats();
		&returnHitImage();
		&log_event("Blocked by IP, pg=$url");
		exit 0;
	}
}

chop($dStat[1]);
@sStats = split(/\t/,$dStat[1]);
$VbyHr=$dStat[4];
$HbyHr=$dStat[5];
chop($VbyHr);
chop($HbyHr);
chop($dStat[2]);
@t = split(/\t/,$dStat[2]);
$t[0] ++;
$t[$curMo] ++;
$dStat[2] = join("\t",@t)."\n";

if($visitID > $sStats[0]) {
	$visitID = 0;
	$visitorLevel = 0;
}

$navIndex = -1;
@psFile = ();

open(FILE, "$acct/L10HC_PageL.dat")|| &gen_error("Cannot open $acct/L10HC_Hits.dat at Counter.Open_Stats2");
@pageList = <FILE>;
close(FILE);

open(FILE, "$acct/L10HC_PageI.dat")|| &gen_error("Cannot open $acct/L10HC_Hits.dat at Counter.Open_Stats3");
@pageIndexes = <FILE>;
close(FILE);

@res = &bSearch($url,\@pageList,1,\@pageIndexes,1,1);

################
# New_Page_Write

if(!$res[0]) {
# &log_event("new page res=@res - $url");
	$newPage = 1;
	$cPgID = $#pageList + 1;
	open (FILE, ">>$acct/L10HC_PageL.dat") || &gen_error("Cannot open >>$acct/L10HC_PageL.dat at Counter.New_Page_Write1");
	print FILE "$url\n";
	close(FILE);
	
	open (FILE, ">$acct/L10HC_PageI.dat") || &gen_error("Cannot open >$acct/L10HC_PageI.dat at Counter.New_Page_Write2");

	$inserted = 0;
	for($i=0;$i<=$#pageIndexes;$i++) {
		if(!$inserted && ($i == $res[1])) {
			print FILE "$cPgID\n";
			$inserted = 1;
			$i--;
		} else {
			print FILE $pageIndexes[$i];
		}
	}
	if(!$inserted) {
		print FILE "$cPgID\n";
	}
	close(FILE);
	
	if($visitorLevel <= 4) {
		push(@dStat,"1\t1\t1\t1\t1\t1\t1\t1\t1\t1\n");
	} else {
		push(@dStat,"0\t0\t0\t0\t0\t1\t1\t1\t1\t1\n");
	}
	$pgCnt = $#pageList+2;
	
} else {
# &log_event("ext page res=@res - $url");
	$cPgID = @pageIndexes[$res[1]];
	chop($cPgID);
	$pgCnt = $#pageList+1;
}

###########
# Init_Hits

$cPgDt = $fDateStr;
$fName = &getFileDateStr('Hits','D',$curYr,$curMo,$curDay);
if(-e $fName) {
	open(FILE, $fName)|| &gen_error("Cannot open $fName at Counter.Init_Hits1");
	@t = <FILE>;
	$hitsA{$fDateStr} = [ @t ];
	close(FILE);
	if($newPage) {
		push(@{$hitsA{$fDateStr}},"0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n");
		push(@{$hitsA{$fDateStr}},"\n");
		push(@{$hitsA{$fDateStr}},"\n");
		push(@{$hitsA{$fDateStr}},"\n");
		push(@{$hitsA{$fDateStr}},"\n");
	}	
} else {
	$hitsA{$fDateStr} = ();
	push(@{$hitsA{$fDateStr}},"0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n");
	for($i=0;$i<$pgCnt;$i++) {
		push(@{$hitsA{$fDateStr}},"0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n");
		push(@{$hitsA{$fDateStr}},"\n");
		push(@{$hitsA{$fDateStr}},"\n");
		push(@{$hitsA{$fDateStr}},"\n");
		push(@{$hitsA{$fDateStr}},"\n");
	}
}

#############
# Visit_Stats

if($visitorLevel <= 4) {
	open(FILE, ">>$acct/L10HC_Extended.dat")|| &gen_error("Cannot open >>$acct/L10HC_Extended.dat at Counter.Visit_Stats1");
	if(param('sl') eq "undefined") {
		$lang = param('nl');
	} else {
		$lang = param('sl');
	}
	print FILE "".param('os')."\t".param('nn')."\t".param('nv')."\t$lang\t$cookiesEnabled\t$jSEnabled\t".param('cd')."\t".param('sx')."x".param('sy')."\t".param('tz')."\t".$ENV{'REMOTE_HOST'}."\n";
	close(FILE);

	$sStats[0] ++; # All Time Entry 
	$sStats[1] ++; # Year Entry
	$sStats[2] ++; # Month Entry
	$sStats[3] ++; # Week Entry
	$sStats[4] ++; # Day Entry

	@VbyHrArr = split(/\t/,$VbyHr);
	$VbyHrArr[$curHr] ++;
	$VbyHr = join("\t",@VbyHrArr);
	$visitID = $sStats[0];
# &log_event("new visitor = $visitID");
# &log_event("".$ENV{'REMOTE_ADDR'}." Unique1: vl=$visitorLevel,vID=$visitID,ref=$ref","visitors"); # debug
} else {

	&readNav();
	for($j=0;$j<=$#nStats;$j+=3) {			
		if($nStats[$j] =~ m/^$visitID\t/) {
			chop($nStats[$j]);
			@t = split(/\t/,$nStats[$j]);
			$pgTm = ($aTime - $t[1]);
			if($pgTm > $maxPgTime) {
				$navIndex = -1;
				$nStats[$j] .= "\n";
				&writeNav();
			} else {
				$visitID = $t[0];
				$lPgID = $t[2];
				$lPgDt = $t[3];
				if($pageList[$lPgID] eq "$url\n") {
					$reload = 1;
				}
				$navIndex = $j;
			}
			last;
		}
	}
	if($navIndex == -1) {
		$visitorLevel = 5;
	}
# &log_event($ENV{'REMOTE_ADDR'}." NonUnique1: vl=$visitorLevel,vID=$visitID,r=$reload","visitors"); # debug
}

&returnHitImage();

chop($dStat[$cPgID+6]);
@pStats = split(/\t/,$dStat[$cPgID+6]);	

if(!$reload) {
	$sStats[5] ++; # All Time Visit
	$sStats[6] ++; # Year Visit
	$sStats[7] ++; # Month Visit
	$sStats[8] ++; # Week Visit
	$sStats[9] ++; # Day Visit
	if($visitorLevel <= 4) {
		$pStats[0] ++; # All Time Entry
		$pStats[1] ++; # Year Entry
		$pStats[2] ++; # Month Entry
		$pStats[3] ++; # Week Entry
		$pStats[4] ++; # Day Entry
	}
	$pStats[5] ++; # All Time Visit
	$pStats[6] ++; # Year Visit
	$pStats[7] ++; # Month Visit
	$pStats[8] ++; # Week Visit
	$pStats[9] ++; # Day Visit

	@HbyHrArr = split(/\t/,$HbyHr);
	$HbyHrArr[$curHr] ++;
	$HbyHr = join("\t",@HbyHrArr);
}

$dStat[$cPgID+6] = join("\t",@pStats)."\n";

open(DSTAT_FH, ">$acct/L10HC_Hits.dat")|| &gen_error("Cannot open $acct/L10HC_Hits.dat at Counter.Visit_Stats2");

print DSTAT_FH "$dStat[0]";
print DSTAT_FH "$sStats[0]\t$sStats[1]\t$sStats[2]\t$sStats[3]\t$sStats[4]\t$sStats[5]\t$sStats[6]\t$sStats[7]\t$sStats[8]\t$sStats[9]\n";
print DSTAT_FH "$dStat[2]";
print DSTAT_FH "$dStat[3]";
print DSTAT_FH "$VbyHr\n";
print DSTAT_FH "$HbyHr\n";

for($i=6; $i<=$#dStat; $i++) {
	print DSTAT_FH "$dStat[$i]";
}
close(DSTAT_FH);

@dStat = undef; # de-alc mem

#########
# Ref_Log

$refID = -1;
$newRef = 0;
if($visitorLevel <= 4) { # refs log
	
	%refsH = ();
	@refsA = ();
	$refCnt = 0;

	$fName = &getFileDateStr('Refs','L',$curYr,$curMo,$curDay);
	if(-e $fName) {
		open (FILE, $fName) || &gen_error("Cannot open $fName at Counter.Ref_Log1");
		$i=0;
		foreach (<FILE>) {
			chop($_);
			$refsH{$_} = $i;
			push(@refsA,$_);
			$i++;
		}
		$refCnt = $i;
		$refID = $i+1;
		close (FILE);
	}

	if(exists($refsH{$ref})) {
		$refID = $refsH{$ref};
		$fName = &getFileDateStr('sRefs','D',$curYr,$curMo,$curDay);
		open (FILE, $fName) || &gen_error("Cannot open $fName at Counter.Ref_Log2");
		@t = <FILE>;
		close (FILE);
		$fName = &getFileDateStr('sRefs','D',$curYr,$curMo,$curDay);
		open (FILE, ">$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log3");
		for($i=0;$i<=$#t;$i++) { 
			if($i == $refID) {
				chop($t[$i]);
				@t1 = split(/\t/,$t[$i]);
				$t1[0] ++;
				
				print FILE "".join("\t",@t1)."\n";
			} else {
				print FILE $t[$i];
			}
		}
		close (FILE);
	} else {
		$newRef = 1;
	
		$rDomain = "";
		$rSE = "";
		$rKW = "";
		
		%SEIndexes = {};
		@SEName = ();
		@SESearch = ();
		%SDs = {};
		
		open (FILE, "L10HC_SE.txt") || &gen_error("Cannot open L10HC_SE.txt at Counter.Ref_Log4");
		$i = 0;
		foreach (<FILE>) {
			chop($_);
			if(length($_) > 1) {
				my @t = split(/\t/,$_);
				$SEIndexes{$t[0]} = $i;
				push(@SEName,$t[1]);
				push(@SESearch,$t[2]);
				$i++;
			}
		}
		close(FILE);

		open (FILE, "L10HC_SD.txt") || &gen_error("Cannot open L10HC_SD.txt at Counter.Ref_Log5");
		$i=0;
		foreach (<FILE>) {
			if($i) {
				chop($_);
				if(length($_) > 1) {
					my @t = split(/\t/,$_);
					$SDs{$t[0]} = $t[1];
				}
			} else {
				$i = 1;
			}
		}
		close(FILE);
	
		$refID = $#refsA+1;
		
		$fName = &getFileDateStr('Refs','I',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log6");
			@t = <FILE>;
			close (FILE);

			@t1 = &bSearch($ref,\@refsA,1,\@t,1,1);

			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log7");
			$inserted = 0;
			for($i=0;$i<=$#t;$i++) {
				if(!$inserted && ($i == $t1[1])) {
					print FILE "$refID\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $t[$i];
				}
			}
			if(!$inserted) {
				print FILE "$refID\n";
			}
			close (FILE);
		} else {
			open (FILE, ">>$fName") || &gen_error("Cannot open >>$fName at Counter.Ref_Log8");
			print FILE "$refID\n";
			close (FILE);
		}	
	
		$refsH{$ref} = $refCnt;
		push(@refsA,$ref);
		
		@refSegs = split(/\//,$ref); 
		$refSegs[0] =~ s/www\.//i;
		$rDomain = $refSegs[0];			
		if(exists $SEIndexes{$refSegs[0]}) {
			$SEI = $SEIndexes{$refSegs[0]};
			@query = split(/\?/,$refSegs[$#refSegs]);
			@query = split(/\%26/,$query[1]);
			foreach (@query) {
				if(substr($_,0,length($SESearch[$SEI]) + 1) eq "$SESearch[$SEI]=") {
					$srcStr = substr($_,length($SESearch[$SEI]) + 1);
					$last;
				}
			}
			$rSE = $SEName[$SEI];
			$rKW = $srcStr;
		} elsif(exists $SDs{$refSegs[0]}) {
			$dStr = "$refSegs[1]";
			for($i=2;$i<=$#refSegs;$i++) {
				$dStr = "$dStr/$refSegs[$i]";
			}
			$rSE = $SDs{$refSegs[0]};
			$rKW = $dStr;
		} else {
			$rKW = "";
		}
		if($rSE != '' && $rKW == '') {
			$rKW = '[No Term Entered]';
		}

		$fName = &getFileDateStr('Refs','L',$curYr,$curMo,$curDay);
		$fName = (-e "$fName") ? ">>$fName" : ">$fName"; 
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log9");
		print FILE "$ref\n";
		close (FILE);
		
		$fName = &getFileDateStr('Doms','L',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log10");
			@refsA = <FILE>;
			close (FILE);
		} else {
			@refsA = ();
		}
		
		$fName = (-e "$fName") ? ">>$fName" : ">$fName"; 
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log11");
		print FILE "$rDomain\n";
		close (FILE);
		
		$fName = &getFileDateStr('Doms','I',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log12");
			@t = <FILE>;
			close (FILE);

			@t1 = &bSearch($rDomain,\@refsA,1,\@t,1,1);

			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log13");
			$inserted = 0;
			for($i=0;$i<=$#t;$i++) {
				if(!$inserted && ($i == $t1[1])) {
					print FILE "$refID\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $t[$i];
				}
			}
			if(!$inserted) {
				print FILE "$refID\n";
			}
			close (FILE);
		} else {
			open (FILE, ">>$fName") || &gen_error("Cannot open >>$fName at Counter.Ref_Log14");
			print FILE "$refID\n";
			close (FILE);
		}
		

		$fName = &getFileDateStr('SEs','L',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log15");
			@refsA = <FILE>;
			close (FILE);
		} else {
			@refsA = ();
		}		
		$fName = (-e "$fName") ? ">>$fName" : ">$fName"; 
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log16");
		print FILE "$rSE\n";
		close (FILE);
		
		$fName = &getFileDateStr('SEs','I',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log17");
			@t = <FILE>;
			close (FILE);

			@t1 = &bSearch($rSE,\@refsA,1,\@t,1,1);

			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log18");
			$inserted = 0;
			for($i=0;$i<=$#t;$i++) {
				if(!$inserted && ($i == $t1[1])) {
					print FILE "$refID\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $t[$i];
				}
			}
			if(!$inserted) {
				print FILE "$refID\n";
			}
			close (FILE);
		} else {
			open (FILE, ">$fName") || &gen_error("Cannot open >>$fName at Counter.Ref_Log19");
			print FILE "$refID\n";
			close (FILE);
		}


		$fName = &getFileDateStr('KWs','L',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log20");
			@refsA = <FILE>;
			close (FILE);
		} else {
			@refsA = ();
		}		
		$fName = (-e "$fName") ? ">>$fName" : ">$fName"; 
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log21");
		print FILE "$rKW\n";
		close (FILE);
		
		$fName = &getFileDateStr('KWs','I',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log22");
			@t = <FILE>;
			close (FILE);

			@t1 = &bSearch($rKW,\@refsA,1,\@t,1,1);

			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log23");
			$inserted = 0;
			for($i=0;$i<=$#t;$i++) {
				if(!$inserted && ($i == $t1[1])) {
					print FILE "$refID\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $t[$i];
				}
			}
			if(!$inserted) {
				print FILE "$refID\n";
			}
			close (FILE);
		} else {
			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log24");
			print FILE "$refID\n";
			close (FILE);
		}
		
		$fName = &getFileDateStr('SEKWs','L',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log15");
			@refsA = <FILE>;
			close (FILE);
		} else {
			@refsA = ();
		}		
		$fName = (-e "$fName") ? ">>$fName" : ">$fName"; 
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log26");
		print FILE "$rSE - $rKW\n";
		close (FILE);

		$fName = &getFileDateStr('SEKWs','I',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log27");
			@t = <FILE>;
			close (FILE);

			@t1 = &bSearch("$rSE - $rKW",\@refsA,1,\@t,1,1);

			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log28");
			$inserted = 0;
			for($i=0;$i<=$#t;$i++) {
				if(!$inserted && ($i == $t1[1])) {
					print FILE "$refID\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $t[$i];
				}
			}
			if(!$inserted) {
				print FILE "$refID\n";
			}
			close (FILE);
		} else {
			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log29");
			print FILE "$refID\n";
			close (FILE);
		}

		if($refType eq '') {
			if($ref eq '') { $refType = '[Unknown]';}
			elsif($rSE eq '') { $refType = '[Site Link]';}
			else { $refType = '[Major SE]';}
		}
		$fName = "$acct/L10HC_Archive/rTypes/rTypeL.dat";
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log30");
		@refsA = <FILE>;
		close (FILE);
		
		$fName2 = "$acct/L10HC_Archive/rTypes/rTypeI.dat";
		open (FILE, "$fName2") || &gen_error("Cannot open $fName2 at Counter.Ref_Log30");
		@t = <FILE>;
		close (FILE);
		
		@res = &bSearch($refType,\@refsA,1,\@t,1,1);

		if(!$res[0]) {
			open (FILE, ">>$fName") || &gen_error("Cannot open >>$fName at Counter.New_Page_Write1");
			print FILE "$refType\n";
			close(FILE);
			$rTypeID = $#refsA+1;
			
			open (FILE, ">$fName2") || &gen_error("Cannot open >$fName2 at Counter.New_Page_Write2");
		
			$inserted = 0;
			for($i=0;$i<=$#t;$i++) {
				if(!$inserted && ($i == $res[1])) {
					print FILE "$rTypeID\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $t[$i];
				}
			}
			if(!$inserted) {
				print FILE "$rTypeID\n";
			}
			close(FILE);
			
		} else {
			$rTypeID = $t[$res[1]];
			chop($rTypeID);
		}
		$fName = &getFileDateStr('rTypes','L',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log15");
			@refsA = <FILE>;
			close (FILE);
		} else {
			@refsA = ();
		}	
		
		$fName = (-e "$fName") ? ">>$fName" : ">$fName"; 
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log35");
		print FILE "$rTypeID\n";
		close (FILE);
		
		$rTypeI = $#refsA + 1;
		
		$fName = &getFileDateStr('rTypes','I',$curYr,$curMo,$curDay);
		if(-e $fName) {
			open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log27");
			@t = <FILE>;
			close (FILE);

			@t1 = &bSearch($rTypeID,\@refsA,1,\@t,1,1);

			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log28");
			$inserted = 0;
			for($i=0;$i<=$#t;$i++) {
				if(!$inserted && ($i == $t1[1])) {
					print FILE "$rTypeI\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $t[$i];
				}
			}
			if(!$inserted) {
				print FILE "$rTypeI\n";
			}
			close (FILE);
		} else {
			open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log29");
			print FILE "$rTypeI\n";
			close (FILE);
		}
		

		$fName = &getFileDateStr('sRefs','D',$curYr,$curMo,$curDay);
		$fName = (-e "$fName") ? ">>$fName" : ">$fName"; 
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log35");
		print FILE "1\t0\t0\n";
		close (FILE);
		
	}
	
# pRefsIbPg
	$fName = &getFileDateStr('pgRefs','IbPg',$curYr,$curMo,$curDay);		
	if(-e $fName) {
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log37");
		@t = <FILE>;
		close (FILE);
	} else {
		@t = ("\n","\n","\n","\n");
	}
	$iI = $cPgID*4;
	while(($iI+3)>$#t) {
		push(@t,"\n","\n","\n","\n");
	}	
	chop($t[$iI]);
	chop($t[$iI+1]);
	@t1 = split(/\t/,$t[$iI]);
	@t2 = split(/\t/,$t[$iI+1]);
	$found = 0;
	for($i=0;$i<=$#t1;$i++) {
		if($t1[$i] eq $refID) {
			$t2[$i] ++;
			$found = 1;
			last;
		}
	} 
	if($found) {
		$t[$iI] = '';
		$t[$iI+1] = '';
		for($i=0;$i<=$#t1;$i++) {
			$t[$iI] .= "$t1[$i]\t";
			$t[$iI+1] .= "$t2[$i]\t";
		}
		chop($t[$iI]);
		chop($t[$iI+1]);
		$t[$iI] .= "\n";
		$t[$iI+1] .= "\n";		
	} elsif($t[$iI] eq '') {
		$t[$iI] = "$refID\n";
		$t[$iI+1] = "1\n";
		$t[$iI+2] = "0\n";
		$t[$iI+3] = "0\n";
	} else {
		chop($t[$iI+2]);
		chop($t[$iI+3]);
		$t[$iI] .= "\t$refID\n";
		$t[$iI+1] .= "\t1\n";
		$t[$iI+2] .= "\t0\n";
		$t[$iI+3] .= "\t0\n";
	}

	open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log38");
	foreach (@t) {
		print FILE $_;
	}
	close (FILE);

# pgRefsIbR
	$fName = &getFileDateStr('pgRefs','IbR',$curYr,$curMo,$curDay);		
	if(-e $fName) {
		open (FILE, "$fName") || &gen_error("Cannot open $fName at Counter.Ref_Log39");
		@t = <FILE>;
		close (FILE);
	} else {
		@t = ();
	}
	if($newRef) {
		push(@t,"$cPgID\n");
		push(@t,"1\n");
		push(@t,"0\n");
		push(@t,"0\n");
	} else {
		$iI = $refID*4;
		chop($t[$iI]);
		chop($t[$iI+1]);
		@t1 = split(/\t/,$t[$iI]);
		@t2 = split(/\t/,$t[$iI+1]);
		$found = 0;
		for($i=0;$i<=$#t1;$i++) {
			if($t1[$i] eq $cPgID) {
				$t2[$i] ++;
				$found = 1;
				last;
			}
		} 
		if($found) {
			$t[$iI] = '';
			$t[$iI+1] = '';
			for($i=0;$i<=$#t1;$i++) {
				$t[$iI] .= "$t1[$i]\t";
				$t[$iI+1] .= "$t2[$i]\t";
			}
			chop($t[$iI]);
			chop($t[$iI+1]);
			$t[$iI] .= "\n";
			$t[$iI+1] .= "\n";
		} else {
			chop($t[$iI+2]);
			chop($t[$iI+3]);
			$t[$iI] .= "\t$cPgID\n";
			$t[$iI+1] .= "\t1\n";
			$t[$iI+2] .= "\t0\n";
			$t[$iI+3] .= "\t0\n";
		}

	}

	open (FILE, ">$fName") || &gen_error("Cannot open >$fName at Counter.Ref_Log40");
	foreach (@t) {
		print FILE $_;
	}
	close (FILE);
	
	@t1 = ();
	@t2 = ();
	%t2a = ();
}

#################
# Hits_Processing

if($lPgID >= 0) {
	if(!exists $hitsA{$lPgDt}) {
		$pYr = substr($lPgDt,0,2);
		$pMD = substr($lPgDt,2);
		open(FILE, "$acct/L10HC_Archive/Hits/Y$pYr/HitsD_$pMD.dat")|| &gen_error("Cannot open $acct/L10HC_Archive/Hits/Y$pYr/HitsD_$pMD.dat at Counter.Hits_Processing1");
		@t = <FILE>;
		$hitsA{$lPgDt} = [ @t ];
		close(FILE);
# &log_event("Opening yesterday hits len=$#t, file=L10HC_Archive/Hits/Y$pYr/Hits_$pMD.dat");
	}
	$pgI = $lPgID*5+1;
	chop($hitsA{$lPgDt}[0]);
	@sStats = split(/\t/,$hitsA{$lPgDt}[0]);
	chop($hitsA{$lPgDt}[$pgI]);
	@pStats =  split(/\t/,$hitsA{$lPgDt}[$pgI]);
	if($reload) { #reload
		$sStats[14] ++;
		$hitsA{$lPgDt}[0] = join("\t",@sStats)."\n";
		$pStats[14] ++;
		$hitsA{$lPgDt}[$pgI] = join("\t",@pStats)."\n";	
	} else {
		$sStats[15] += $pgTm;
		$sStats[4] --;
		$hitsA{$lPgDt}[0] = join("\t",@sStats)."\n";
		$pStats[15] += $pgTm;
		$pStats[4] --;
		$hitsA{$lPgDt}[$pgI] = join("\t",@pStats)."\n";
		chop($hitsA{$lPgDt}[$pgI+3]); # link to page
		chop($hitsA{$lPgDt}[$pgI+4]); 
		@t1 =  split(/\t/,$hitsA{$lPgDt}[$pgI+3]);
		@t2 =  split(/\t/,$hitsA{$lPgDt}[$pgI+4]);
		$found = 0;
		for($i=0;$i<=$#t1;$i++) {
			if($t1[$i] eq $cPgID) {
				$t2[$i] ++;
				$found = 1;
				last;
			}
		}
		if(!$found) {
			push(@t1,$cPgID);
			push(@t2,1);
		}
		$hitsA{$lPgDt}[$pgI+3] = join("\t",@t1)."\n";
		$hitsA{$lPgDt}[$pgI+4] = join("\t",@t2)."\n";
		$pgI = $cPgID*5+1;
		chop($hitsA{$cPgDt}[$pgI+1]); # link from page
		chop($hitsA{$cPgDt}[$pgI+2]); 
		@t1 =  split(/\t/,$hitsA{$cPgDt}[$pgI+1]);
		@t2 =  split(/\t/,$hitsA{$cPgDt}[$pgI+2]);
		$found = 0;
		for($i=0;$i<=$#t1;$i++) {
			if($t1[$i] eq $lPgID) {
				$t2[$i] ++;
				$found = 1;
				last;
			}
		}
		if(!$found) {
			push(@t1,$lPgID);
			push(@t2,1);
		}
		$hitsA{$cPgDt}[$pgI+1] = join("\t",@t1)."\n";
		$hitsA{$cPgDt}[$pgI+2] = join("\t",@t2)."\n";

	}
}

if(!$reload) {
	$pgI = $cPgID*5+1;
	$t = $hitsA{$fDateStr}[0];
	chop($t);
	@sStats = split(/\t/,$t);
	$t = $hitsA{$fDateStr}[$pgI];
	chop($t);
	@pStats = split(/\t/,$t);

	if($visitorLevel <= 5) {
		$sStats[0] ++;
		$pStats[0] ++;
	}
	if($visitorLevel <= 4) {
		$sStats[1] ++;
		$pStats[1] ++;
	}
	if($visitorLevel == 0) {
		$sStats[2] ++;
		$pStats[2] ++;
	}

	$sStats[3] ++;
	$pStats[3] ++;
	$sStats[4] ++;
	$pStats[4] ++;
	
	$hitsA{$fDateStr}[0] = join("\t",@sStats)."\n";
	$hitsA{$fDateStr}[$pgI] = join("\t",@pStats)."\n";
}

###########
# Write_Nav

# &log_event("vL=$visitorLevel,vID=$visitID,reload=$reload");
if($visitorLevel <= 5) { # Nav log
# &log_event("Nav-Append New: $visitID\t$aTime\t$cPgID\t$fDateStr");
# for($i=0;$i<=$#nStats;$i+=3) {
#	chop($nStats[$i]);
# &log_event("Nav-Cur Nav File[".($i/3)."]: $nStats[$i]$nStats[$i+1]$nStats[$i+2]");
# }
	open(FILE, ">>$acct/L10HC_Nav.dat")|| &gen_error("Cannot open $acct/L10HC_Nav.dat at Counter.Write_Nav1");
	print FILE "$visitID\t$aTime\t$cPgID\t$fDateStr\n";
	if($success) {
		print FILE "$cPgID*\n";
	} else {
		print FILE "$cPgID\n";
	}
	
	print FILE "$fDateStr\t$curHr2$curMin2\t$refID\t$success\t$visitorLevel\n";
	close(FILE);	
} elsif(($visitID > 0) && !$reload) {
# &log_event("ext nav vID=$visitID,vL=$visitorLevel,nI=$navIndex");
	&writeNav();
}

# foreach (keys %hitsA) {
#	@t =  split(/\t/,$hitsA{$_}[0]);
#	&log_event("Hits File $_: Dif=".($t[0]-$t[5]-$t[4]).", Entries=$t[0], Exits=$t[5], Active=$t[4], Conv=$t[8], Succ=$t[11]");
# }


&writeHitsArchive();

&unlock_stats();

exit 0;

#####################################################
# Subroutine start
#####################################################

##################
# returnHitImage()
sub returnHitImage() {
# &log_event("L10HC_LV_$acct2=$curMo\/$curDay\/$curYr\/$curHr\/$curMin\/$curSec\/$visitID\/$visitorLevel\/$IPlog[1];");
	 if($visitorLevel <= 5) { 
	 	if($cookiesEnabled && ($visitorLevel > 0)) {
	 		open (FILE, "$acct/L10HC_IPL.dat") || &gen_error("Cannot open $acct/L10HC_IPL.dat at Counter.returnHitImage()1");
			@IPL1 = <FILE>;
			close(FILE);
			open (FILE, "$acct/L10HC_IPI.dat") || &gen_error("Cannot open $acct/L10HC_IPI.dat at Counter.returnHitImage()2");
			@IPI1 = <FILE>;
			close(FILE);
			
		
			@res = &bSearch($IP,\@IPL1,1,\@IPI1,1,1,1);
			$IPlog[0] = $res[0];
			$IPlog[1] = $res[1];
	 	}
	
	 	if($IPlog[0]) {
			splice(@IPD1,$IPlog[1],1,"$curDay/$curHr\t$visitID\n");
		} elsif(1==1) {
			open(FILE, ">>$acct/L10HC_IPL.dat") || &gen_error("Cannot open $acct/L10HC_IPL.dat at Counter.returnHitImage()3");
			print FILE "$IP\n";
			close(FILE);
			open(FILE, ">>$acct/L10HC_IPD.dat") || &gen_error("Cannot open $acct/L10HC_IPD.dat at Counter.returnHitImage()4");
			print FILE "$curDay/$curHr\t$visitID\n";
			close(FILE);
			
			open (FILE, ">$acct/L10HC_IPI.dat") || &gen_error("Cannot open $acct/L10HC_IPI.dat at Counter.returnHitImage()5");
			$inserted = 0;
			for($i=0;$i<=$#IPI1;$i++) {
				if(!$inserted && ($i == $IPlog[1])) {
					print FILE "".($#IPL1+1)."\n";
					$inserted = 1;
					$i--;
				} else {
					print FILE $IPI1[$i];
				}
			}
			if(!$inserted) {
				print FILE "".($#IPL1+1)."\n";
			}
			close(FILE);
		}
	}
# &log_event("L10HC_LV_$acct2=$curMo\/$curDay\/$curYr\/$curHr\/$curMin\/$curSec\/$visitID\/$visitorLevel\/$IPlog[1];src=".param('src'));
	if(param('src') eq 'swf') {
		open (IMG, "L10HC_SWF.swf") || &gen_error("Cannot open L10HC_SWF.swf at Counter.returnHitImage()6");
		@imgd = <IMG>;
		print "Content-type:  application/x-shockwave-flash\n\n";
	} else {
		open (IMG, "L10HC_Img_L.gif") || &gen_error("Cannot open L10HC_Img_L.gif at Counter.returnHitImage()7");
		@imgd = <IMG>;
		print "Content-type:  image/gif\n";
		print "Set-Cookie: L10HC_LV_$acct2=$curMo\/$curDay\/$curYr\/$curHr\/$curMin\/$curSec\/$visitID\/$visitorLevel\/$IPlog[1];";		
		print " expires=Fri, 31-Dec-10 00:00:01 GMT; \n\n";
	}
	

	foreach (@imgd) {
		print $_;
	}
	close(IMG);
}

sub retImg() {
	open (IMG, "L10HC_Img_".param('i').".gif") || &gen_error("Cannot open L10HC_Img_".param('i').".gif at Counter.returnHitImage()8");
	@imgd = <IMG>;
	print "Content-type:  image/gif\n\n";
	foreach (@imgd) {
		print $_;
	}
	close(IMG);
	exit 0;
}