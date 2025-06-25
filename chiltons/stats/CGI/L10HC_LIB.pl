# v3.16 1/1/04

$symlinkFlag = 1;
$dataDir = '';

@YDbMo = (0,31,59,90,120,151,181,212,243,273,304,334);
@DpMo = (0,31,28,31,30,31,30,31,31,30,31,30,31);

$aTime = time();

($curSec,$curMin,$curHr,$curDay,$curMo,$curYr,$curDoW,$curDoY) = localtime();
$curYr += 1900;
$curYr2 = substr($curYr,2);
$serYr = $curYr;
$curMo ++;
$serMo = $curMo;
$serDay = $curDay;
$serHr = $curHr;
$serMin = $curMin;
$serSec = $curSec;
$curHr += $timeAdj;

while($curHr >= 24) {
	$curHr -= 24;
	($curYr,$curMo,$curDay) = &AddDeltaDays($curYr,$curMo,$curDay,1);
}

while($curHr < 0) {
	$curHr += 24;
	($curYr,$curMo,$curDay) = &AddDeltaDays($curYr,$curMo,$curDay,-1);
}
$dateStamp = "$curYr/$curMo/$curDay";
$curHr2 = ($curHr < 10) ? "0$curHr" : $curHr;
$curMin2 = ($curMin < 10) ? "0$curMin" : $curMin;

sub gen_error {
	($msg) = @_;
	&log_error($msg);
	print header;
	print "res=Err&msg=$msg&msg2=<p>see <a href=http://hitcounter.leveltendesign.com/help_troubleshooting.html>L10HC Help</a> to troubleshoot";
	&unlock_stats();
	exit 0;
}

sub log_error {
	($msg) = @_;
	&setRepTime();
	open(ERROR_FH, ">>L10HC_Errors.log");
	print ERROR_FH "$repDate $repTime $acct - $msg\n";
	close(ERROR_FH);
}

sub log_event {
	my ($msg,$file) = @_;
	if(length($file) > 0) {
		$file = "_$file";
	} else {
		$file = "";
	}
	my ($eSec,$eMin,$eHr,$eDay,$eMo,$eYr,$eDoW,$eDoY) = localtime();
	my $t = 60*($eMin-$curMin)+($eSec-$curSec);
	&setRepTime();
	open(ERROR_FH, ">>L10HC_Events$file.log");
	print ERROR_FH "$repDate $repTime $acct - $msg\n";
	close(ERROR_FH);
}

$acctL = '';
sub setRepTime () {
	$hr = $curHr;
	$min = $curMin;
	$sec = $curSec;
	$repSecs = $curHr*3600+$curMin*60+$curSec;

	$timeMod = "AM";
	if($hr>=11) {
		$timeMod = "PM";
	}
	if($hr>11) {
		$hr = $hr - 12;
	}
	if($hr==0) {
		$hr=12;
	}
	if($min<10) {
		$min = "0$min";
	}
	if($sec<10) {
		$sec = "0$sec";
	}
	
	$repTime = "$hr:$min:$sec $timeMod";
	$repDate = "$curMo/$curDay/$curYr";
	if($acct ne '') {
		$acctL = " - $acct";
	}
}

sub writeParams () {
	open (PARAM_FH, ">L10HC_Params.pl") || &gen_error("Cannot open L10HC_Params.pl at writeParams()");
	print PARAM_FH "\$initDate = \'$initDate\'\;\n";
	print PARAM_FH "\$adminPassword = \"$adminPassword\"\;\n";
	print PARAM_FH "\$logLimit = $logLimit\;\n";
	print PARAM_FH "\$keyCode = \'$keyCode\'\;\n"; 
	print PARAM_FH "\$kcErr = $kcErr\;\n"; 
	print PARAM_FH "\$kcErrMsg = \'$kcErrMsg\'\;\n"; 
	print PARAM_FH "\$datVer = $datVer\;\n"; 
	print PARAM_FH "\$debugLog = $debugLog\;\n"; 
	print PARAM_FH "\$acctManager = $acctManager\;\n"; 
	print PARAM_FH '1;';
	close (PARAM_FH);
}

sub writeAcctParams () {
	$phr = "(\'".join("\',\'",@phrases)."\')";
	$ds = "(\'".join("\',\'",@validDoms)."\')";
	$bips = "(\'".join("\',\'",@blockIPs)."\')";
	$qsf = "(\'".join("\',\'",@queryStrFilters)."\')";
	open (PARAM_FH, ">$acct/L10HC_AcctParams.pl") || &gen_error("Cannot open $acct/L10HC_AcctParams.pl at writeAcctParams()");
	print PARAM_FH "\$startDate = \'$startDate\'\;\n";
	print PARAM_FH "\$startDateDisplay = \'$startDateDisplay\'\;\n";
	print PARAM_FH "\$siteTitle = \'$siteTitle\'\;\n";
	print PARAM_FH "\$timeAdj = $timeAdj\;\n"; 
	print PARAM_FH "\@phrases = $phr\;\n";
	print PARAM_FH "\$bTagClr = \"$bTagClr\"\;\n";
	print PARAM_FH "\$removeDisplay = $removeDisplay\;\n";
	print PARAM_FH "\$removeBranding = $removeBranding\;\n";  
	print PARAM_FH "\$password = \"$password\"\;\n";
	print PARAM_FH "\$allowLocalFiles = $allowLocalFiles\;\n";
	print PARAM_FH "\@validDoms = $ds\;\n";
	print PARAM_FH "\@blockIPs = $bips\;\n";
	print PARAM_FH "\$removePageWWW = $removePageWWW\;\n";
	print PARAM_FH "\$lowercasePage = $lowercasePage\;\n";
	print PARAM_FH "\$lowercaseRef = $lowercaseRef\;\n";
	print PARAM_FH "\$removeQueryStr = $removeQueryStr\;\n";
	print PARAM_FH "\@queryStrFilters = $qsf\;\n";
	print PARAM_FH "\$indexPage = \"$indexPage\"\;\n";
	print PARAM_FH "\$maxPgTime = $maxPgTime\;\n";
	print PARAM_FH "\$protectStats = $protectStats\;\n";
	print PARAM_FH "\$reporterURL = \'$reporterURL\'\;\n";
	print PARAM_FH "\$enableAdminLink = $enableAdminLink\;\n";
	print PARAM_FH "\$displaySize = \'$displaySize\'\;\n";
	print PARAM_FH "\$fileLockTO = $fileLockTO\;\n";
	print PARAM_FH "\$maxRepItems = $maxRepItems\;\n";
	print PARAM_FH "\$visitorLog = $visitorLog\;\n";	
	print PARAM_FH '1;';
	close (PARAM_FH);
}

sub moreThan24Hrs () {
	($y0,$m0,$d0,$h0,$y1,$m1,$d1,$h1) = @_;
	if($y1 > $y0) {return 1;}
	if($y1 < $y0) {return 0;}
	if($m1 > $m0) {return 1;}
	if($m1 < $m0) {return 0;}
	if($d1 <= $d0) {return 0;}
	if($d1 > ($d0 +1)) {return 1;}
	if($h1 > $hr0) {return 1;}
	return 0;
}



sub MondayOfWeek() {
	my ($y,$m,$d) = @_;
	$DoW = &DayOfWeek($y,$m,$d);
	unless($DoW == 0) {
		$d -= $DoW;
		if($d < 1) {
			$m --;
			if($m>0) {
				$d += $DpMo[$m];
				if(($m == 2) && &isLeapYr($y)) {
					$d++;
				}
			} else {
				$y--;
				$m = 12;
				$d += 31;
			}
		}
	}
	@r = ($y,$m,$d);
	return @r;
}

sub DayOfWeek () {
	my ($y,$m,$d) = @_;
	$ds01_01_01 = &DaysSince01_01_01($y,$m,$d);
	my @w = &intDiv($ds01_01_01,7);
	my $c = substr($w[1],0,1);
	if($c == 0) {
		return 6;
	} elsif($c == 1) {
		return 0;
	} elsif($c == 2) {
		return 1;
	} elsif($c == 4) {
		return 2;
	} elsif($c == 5) {
		return 3;
	} elsif($c == 7) {
		return 4;
	} else {
		return 5;
	}
	my $dow = ($w[1]); 
	return $dow;
}

sub DeltaDays() {
	my ($y0,$m0,$d0,$y1,$m1,$d1) = @_;
	$ds = &DaysSince01_01_01($y1,$m1,$d1) - &DaysSince01_01_01($y0,$m0,$d0);
	return $ds;
}

sub AddDeltaDays() {
	my ($y,$m,$d,$add) = @_;
	$d = &DaysSince01_01_01($y,$m,$d) + $add;
	my @r = &DateFromDay($d);
	return @r;
}

sub DaysSince01_01_01 () {
	my ($y,$m,$d) = @_;
	my $Ys01 = $y - 2001;
	my @val = &intDiv($Ys01,4);
	my $ds01_01_01 = $Ys01*365 + $val[0];
	$ds01_01_01 += $YDbMo[$m-1];
	if(&isLeapYr($y) && ($m > 2)) {
		$ds01_01_01 ++;
	}
	$ds01_01_01 += $d;
	return $ds01_01_01;
}

sub DateFromDay () {
	my ($d) = @_;
	my $y = 2001;
	my $m = 1;
	while($d > (365 + &isLeapYr($y))) {
		$d -= (365 + &isLeapYr($y));
		$y ++;
	}
	if(&isLeapYr($y)) {
		$DpMo[2] = 29;
	}
	while($d > ($DpMo[$m])) {
		$d -= $DpMo[$m];
		$m ++;
	}
	$DpMo[2] = 28;
	my @r = ($y,$m,$d);
	return @r;
	
}

sub intDiv () {	
	my ($n,$d) = @_;
	# print "n=$n,d=$d<br>";
	my $v = $n/$d;
	return  split(/\./,$v);	
}

sub isLeapYr () {
	($y) = @_;
	my $Ys01 = $y - 2001;
	my @val = &intDiv($Ys01,4);
	if($val[1] == 75) {
		return 1;
	} else {
		return 0;
	}
	
}

sub roundNum() {
	my ($val,$dec) = @_;
	if($dec > 0) {
		$val += (0.5 * (.1 ** $dec));
	} else {
		$val += 0.5;
	}
	my ($n,$d) = split(/\./,$val);
	if(($dec > 0) && (length($d) > 0)) {
		return $n.".".substr($d,0,$dec);
	} else {
		return $n;
	}
}

sub getFileDateStr() {
	my ($fc,$ft,$y,$m,$d) = @_;
	my $rStr = "L10HC_Archive/$fc/Y";
	if(length($y) == 4) { $rStr .= substr($y,2); } else {$rStr .= "$y"; }
	$rStr .= "\/$fc$ft\_";
	if(length($m) == 1) { $rStr .= "0$m"; } else {$rStr .= $m;}
	if(length($d) == 1) { $rStr .= "0$d"; } else {$rStr .= $d;}
	return "$acct/$rStr.dat";
}

sub lock_stats() {
# &log_event($ENV{'REMOTE_ADDR'}."-lck-vID=$visitID,pg=$url,ref=$ref,a=".param('action'));
	if(!$symlinkFlag) {
		return 1;
	}
	for($i=0; $i<=$fileLockTO; $i++) { 
		if(symlink( "$acct/L10HC_Hits.dat", "$acct/L10HC_Hits.dat.lck")) {
			return 1;
		}
($tSec,$tMin,$tHr,$curDay,$tMo,$tYr,$tDoW,$tDoY) = localtime();
# &log_event($ENV{'REMOTE_ADDR'}."-locked-$tHr:$tMin:$tSec");
		sleep 1;
	}
	my @t = 0;
	if(-e "$acct/L10HC_LockTO.dat") {
		open(FILE, "$acct/L10HC_LockTO.dat") || &gen_error("Cannot open $acct/L10HC_LockTO.dat at \"Write Today's Stats Data\"");
		@t = <FILE>;
		close(FILE);
		if(($t[0] ne '') && (($t[0]+4*$fileLockTO) < $aTime)) {
			&unlock_stats();
			unlink ("$acct/L10HC_LockTO.dat");
			&log_error("LockTO exceeded, Lock cleared.");
			return 1;
		} else {
			&log_error("LockTO exceeded.");
		}
		
	} else {
		open(FILE, ">$acct/L10HC_LockTO.dat") || &gen_error("Cannot open $acct/L10HC_LockTO.dat at \"Write Today's Stats Data\"");
		print FILE $aTime;
		close(FILE);
	}
	return 0;
}

sub unlock_stats() {
# &log_event($ENV{'REMOTE_ADDR'}."-ulk");
	if(!$symlinkFlag) {
		return 1;
	}
	unlink ("$acct/L10HC_Hits.dat.lck");
}


# init blank %
@nStats = ();
%hitsA = ();
%paths = ();
%pathsI = ();
%pathsD = ();
%paRefsIbPa = ();
%paRefsIabR = ();
%pgRefsIbPg = ();
%pgRefsIabR = ();
%sRefs = ();
$newPaths = 0;
sub readNav() {
	open(FILE, "$acct/L10HC_Nav.dat") || &gen_error("Cannot open $acct/L10HC_Nav.dat at LIB.readNav()1");
	@nStats = <FILE>;
	close(FILE);
}

############
# writeNav()

$pathID = -1;
# set $navIndex, -1 for check
sub writeNav() {
	open(NAVFILE, ">$acct/L10HC_Nav.dat")|| &gen_error("Cannot open $acct/L10HC_Nav.dat at LIB.writeNav()1");
	$endCheck = 0;
	$endLimit = $#nStats - 2;
	for($j=0;$j<=$endLimit;$j+=3) {	
		if($j == $navIndex) {

			if($reload) { #reload	
				print NAVFILE "$nStats[$j]\n";
				print NAVFILE "$nStats[$j+1]";
				print NAVFILE "$nStats[$j+2]";
			} else {
				chop($nStats[$j+1]);
				chop($nStats[$j+2]);

				print NAVFILE "$visitID\t$aTime\t$cPgID\t$fDateStr\n";
				
				if($success > 0) {
					print NAVFILE "$nStats[$j+1],$cPgID*\n";
					@t = split(/\t/,$nStats[$j+2]);
					$t[3] = $success;
					$nStats[$j+2] = join("\t",@t);
					
				} else {
					print NAVFILE "$nStats[$j+1],$cPgID\n";
				}
				print NAVFILE "$nStats[$j+2]\t$pgTm\n";
				$endCheck = 1;
			}
		} else {
			if(!$endCheck) {
				chop($nStats[$j]);
				chop($nStats[$j+1]);
				chop($nStats[$j+2]);
				@t1 = split(/\t/,$nStats[$j]);
				@t3 = split(/\t/,$nStats[$j+2]);
				$dt1 = $t1[3];
				$pYr1 = substr($dt1,0,2);
				$pMD1 = substr($dt1,2);
				$dt0 = $t3[0];
				$pYr = substr($dt0,0,2);
				$pMD = substr($dt0,2);
				$pgID1 = $t1[2];
				@ta = split(/\,/,$nStats[$j+1]);
				$ta[0] =~ s/\*//;
				$pgID0 = $ta[0]; 
				$refID = $t3[2];
				if(($aTime - $t1[1]) > $maxPgTime) {
					$pgHI1 = $pgID1*5+1;
					$pgRI = $t1[2]*3;
					if(!exists $hitsA{$dt0}) {
						if(-e "$acct/L10HC_Archive/Hits/Y$pYr/HitsD_$pMD.dat") {
							open(FILE, "$acct/L10HC_Archive/Hits/Y$pYr/HitsD_$pMD.dat")|| &gen_error("Cannot open $acct/L10HC_Archive/Hits/Y$pYr/HitsD_$pMD.dat at LIB.writeNav()2");
							@t = <FILE>;
							$hitsA{$dt0} = [ @t ];
							close(FILE);
						} else {
							$hitsA{$dt0} = [ () ];
						}
					}
					if(!exists $hitsA{$dt1}) {
						if(-e "$acct/L10HC_Archive/Hits/Y$pYr1/HitsD_$pMD1.dat") {
							open(FILE, "$acct/L10HC_Archive/Hits/Y$pYr1/HitsD_$pMD1.dat")|| &gen_error("Cannot open $acct/L10HC_Archive/Hits/Y$pYr1/HitsD_$pMD1.dat at LIB.writeNav()3");
							@t = <FILE>;
							$hitsA{$dt1} = [ @t ];
							close(FILE);
						} else {
							$hitsA{$dt1} = [ () ];
						}
					}
					if(!exists $sRefs{$dt0}) {
						if(-e "$acct/L10HC_Archive/sRefs/Y$pYr/sRefsD_$pMD.dat") {
							open(FILE, "$acct/L10HC_Archive/sRefs/Y$pYr/sRefsD_$pMD.dat")|| &gen_error("Cannot open $acct/L10HC_Archive/sRefs/Y$pYr/sRefsD_$pMD.dat at LIB.writeNav()4");
							@t = <FILE>;
							$sRefs{$dt0} = [ @t ];
							close(FILE);
						} else {
							$sRefs{$dt0} = [ () ];
						}
					}

					chop($hitsA{$dt1}[0]);
					@saStats = split(/\t/,$hitsA{$dt1}[0]);
					chop($hitsA{$dt1}[$pgHI1]);
					@paStats =  split(/\t/,$hitsA{$dt1}[$pgHI1]);

					$saStats[4] --;
					$paStats[4] --;
					$hitsA{$dt1}[0] = join("\t",@saStats)."\n";
					$hitsA{$dt1}[$pgHI1] = join("\t",@paStats)."\n";	
					
					chop($hitsA{$dt0}[0]);
					@saStats = split(/\t/,$hitsA{$dt0}[0]);
					chop($hitsA{$dt0}[$pgHI1]);
					@paStats =  split(/\t/,$hitsA{$dt0}[$pgHI1]);
					chop($sRefs{$dt0}[$refID]);
					@rStats = split(/\t/,$sRefs{$dt0}[$refID]);
					
					if($t3[4] <= 5) {
						$saStats[5] ++;
						$paStats[5] ++;
					}
					if($t3[4] <= 4) {
						$saStats[6] ++;
						$paStats[6] ++;
					}
					if($t3[4] == 0) {
						$saStats[7] ++;
						$paStats[7] ++;
					}
					$hitsA{$dt0}[$pgHI1] = join("\t",@paStats)."\n"; # 3.001 mod

					$pgHI0 = $pgID0*5+1; 
					chop($hitsA{$dt0}[$pgHI0]);
					@paStats =  split(/\t/,$hitsA{$dt0}[$pgHI0]);

					if(($nStats[$j+1] =~ m/\,/) || ($nStats[$j+1] =~ m/\*/)) {
						if($t3[4] <= 5) {
							$saStats[8] ++;
							$paStats[8] ++;
						}
						if($t3[4] <= 4) {
							$saStats[9] ++;
							$paStats[9] ++;
							$rStats[1] ++;
						}
						if($t3[4] == 0) {
							$saStats[10] ++;
							$paStats[10] ++;
						}
						if($refID >= 0) {
							if(! exists $pgRefsIbPg{$dt0}) {
								open (FILE, "$acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbPg_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbPg_$pMD.dat at LIB.writeNav()5");
								@t = <FILE>;
								$pgRefsIbPg{$dt0} = [ @t ];
								close (FILE);
								open (FILE, "$acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbR_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbR_$pMD.dat at LIB.writeNav()6");
								@t = <FILE>;
								$pgRefsIbR{$dt0} = [ @t ];
								close (FILE);
							}

							$iI = $pgID0*4;
							chop($pgRefsIbPg{$dt0}[$iI]);
							chop($pgRefsIbPg{$dt0}[$iI+2]);
							@ta = split(/\t/,$pgRefsIbPg{$dt0}[$iI]);
							@tb = split(/\t/,$pgRefsIbPg{$dt0}[$iI+2]);
							for($k=0;$k<=$#ta;$k++) {
								if($ta[$k] eq $refID) {
									$tb[$k] ++;
									last;
								}
							}
							$pgRefsIbPg{$dt0}[$iI] .= "\n";
							$pgRefsIbPg{$dt0}[$iI+2] = join("\t",@tb)."\n";

							$iI = $refID*4;
							chop($pgRefsIbR{$dt0}[$iI]);
							chop($pgRefsIbR{$dt0}[$iI+2]);
							@ta = split(/\t/,$pgRefsIbR{$dt0}[$iI]);
							@tb = split(/\t/,$pgRefsIbR{$dt0}[$iI+2]);
							for($k=0;$k<=$#ta;$k++) {
								if($ta[$k] eq $pgID0) {
									$tb[$k] ++;
									last;
								}
							}
							$pgRefsIbR{$dt0}[$iI] .= "\n";
							$pgRefsIbR{$dt0}[$iI+2] = join("\t",@tb)."\n";
					
						}
					}					

					
					if($nStats[$j+1] =~ m/\*/) {
						if($t3[4] <= 5) {
							$saStats[11] ++;
							$paStats[11] ++;
						}
						if($t3[4] <= 4) {
							$saStats[12] ++;
							$paStats[12] ++;
							$rStats[2] ++;
						}
						if($t3[4] == 0) {
							$saStats[13] ++;
							$paStats[13] ++;
						}
						
						if($refID >= 0) {

							if(! exists $pgRefsIbPg{$dt0}) {
								open (FILE, "$acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbPg_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbPg_$pMD.dat at LIB.writeNav()7");
								@t = <FILE>;
								$pgRefsIbPg{$dt0} = [ @t ];
								close (FILE);
								open (FILE, "$acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbR_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbR_$pMD.dat at LIB.writeNav()8");
								@t = <FILE>;
								$pgRefsIbR{$dt0} = [ @t ];
								close (FILE);
							}

							$iI = $pgID0*4;
							chop($pgRefsIbPg{$dt0}[$iI]);
							chop($pgRefsIbPg{$dt0}[$iI+3]);
							@ta = split(/\t/,$pgRefsIbPg{$dt0}[$iI]);
							@tb = split(/\t/,$pgRefsIbPg{$dt0}[$iI+3]);
							for($k=0;$k<=$#ta;$k++) {
								if($ta[$k] eq $refID) {
									$tb[$k] ++;
									last;
								}
							}
							$pgRefsIbPg{$dt0}[$iI] .= "\n";
							$pgRefsIbPg{$dt0}[$iI+3] = join("\t",@tb)."\n";

							$iI = $refID*4;
							chop($pgRefsIbR{$dt0}[$iI]);
							chop($pgRefsIbR{$dt0}[$iI+3]);
							@ta = split(/\t/,$pgRefsIbR{$dt0}[$iI]);
							@tb = split(/\t/,$pgRefsIbR{$dt0}[$iI+3]);
							for($k=0;$k<=$#ta;$k++) {
								if($ta[$k] eq $pgID0) {
									$tb[$k] ++;
									last;
								}
							}
							$pgRefsIbR{$dt0}[$iI] .= "\n";
							$pgRefsIbR{$dt0}[$iI+3] = join("\t",@tb)."\n";

						}
						
					}
					$hitsA{$dt0}[$pgHI0] = join("\t",@paStats)."\n";	
					$hitsA{$dt0}[0] = join("\t",@saStats)."\n";

					$sRefs{$dt0}[$refID] = join("\t",@rStats)."\n";
					
					if(! exists $paths{$dt0}) {
						@t = ();
						if(-e "$acct/L10HC_Archive/Paths/Y$pYr/PathsL_$pMD.dat") {
							open (FILE2, "$acct/L10HC_Archive/Paths/Y$pYr/PathsL_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Paths/Y$pYr/PathsL_$pMD.dat at LIB.writeNav()9");
							@t = <FILE2>;
							close (FILE2);							
						} else {
							@t = ();
						}
						$paths{$dt0} = [ @t ];
						
						if(-e "$acct/L10HC_Archive/Paths/Y$pYr/PathsI_$pMD.dat") {
							open (FILE2, "$acct/L10HC_Archive/Paths/Y$pYr/PathsI_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Paths/Y$pYr/PathsI_$pMD.dat at LIB.writeNav()10");
							@t = <FILE2>;
							close (FILE2);							
						} else {
							@t = ();
						}
						$pathsI{$dt0} = [ @t ];

						if(-e "$acct/L10HC_Archive/Paths/Y$pYr/PathsD_$pMD.dat") {
							open (FILE2, "$acct/L10HC_Archive/Paths/Y$pYr/PathsD_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Paths/Y$pYr/PathsD_$pMD.dat at LIB.writeNav()11");
							@t = <FILE2>;
							close (FILE2);							
						} else {
							@t = ();
						}
						$pathsD{$dt0} = [ @t ];
						
						if(-e "$acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbR_$pMD.dat") {
							open (FILE2, "$acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbR_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbR_$pMD.dat at LIB.writeNav()12");
							@t = <FILE2>;
							close (FILE2);							
						} else {
							@t = ();
						}
						$paRefsIbR{$dt0} = [ @t ];
						
						if(-e "$acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbPa_$pMD.dat") {
							open (FILE2, "$acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbPa_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbPa_$pMD.dat at LIB.writeNav()13");
							@t = <FILE2>;
							close (FILE2);							
						} else {
							@t = ();
						}
						$paRefsIbPa{$dt0} = [ @t ];
					} 
					@res = &bSearch($nStats[$j+1],\@{ $paths{$dt0} },1,\@{ $pathsI{$dt0} },1,1);
					if($res[0]) {
						$paID = $pathsI{$dt0}[$res[1]];
						chop($paID);
						chop($pathsD{$dt0}[$paID]);
						@ta = split(/\t/,$pathsD{$dt0}[$paID]);
						if($t3[4] <= 5) {
							$ta[0] ++;
						}
						if($t3[4] <= 4) {
							$ta[1] ++;
						}
						if($t3[4] == 0) {
							$ta[2] ++;
						}
						for($k=3;$k<=$#ta;$k++) {
							$ta[$k] += $t3[$k+2];
						}
						$pathsD{$dt0}[$paID] = join("\t",@ta)."\n";
						
						if($refID >= 0) {
							$iI = $paID*2;
							while(($iI+1)>$#{$paRefsIbPa{$dt0}}) {
								push(@{$paRefsIbPa{$dt0}},"\n","\n");
							}
						
							chop($paRefsIbPa{$dt0}[$iI]);
							chop($paRefsIbPa{$dt0}[$iI+1]);
							@ta = split(/\t/,$paRefsIbPa{$dt0}[$iI]);
							@tb = split(/\t/,$paRefsIbPa{$dt0}[$iI+1]);
							$found = 0;
							for($k=0;$k<=$#ta;$k++) {
								if($ta[$k] == $refID) {
									$tb[$k] ++;
									$found = 1;
									last;
								}
							}
							if(!$found) {
								push(@ta,$refID);
								push(@tb,1);	
							}
							$paRefsIbPa{$dt0}[$iI] = join("\t",@ta)."\n";
							$paRefsIbPa{$dt0}[$iI+1] = join("\t",@tb)."\n";

							$iI = $refID*2;
							while(($iI+1)>$#{$paRefsIbR{$dt0}}) {
								push(@{$paRefsIbR{$dt0}},"\n","\n");
							}
							chop($paRefsIbR{$dt0}[$iI]);
							chop($paRefsIbR{$dt0}[$iI+1]);
							@ta = split(/\t/,$paRefsIbR{$dt0}[$iI]);
							@tb = split(/\t/,$paRefsIbR{$dt0}[$iI+1]);
							$found = 0;
							for($k=0;$k<=$#ta;$k++) {
								if($ta[$k] == $paID) {
									$tb[$k] ++;
									$found = 1;
									last;
								}
							}
							if(!$found) {
								push(@ta,$paID);
								push(@tb,1);	
							}
							$paRefsIbR{$dt0}[$iI] = join("\t",@ta)."\n";
							$paRefsIbR{$dt0}[$iI+1] = join("\t",@tb)."\n";
						}
					} else {
						$newPaths = 1;
						push(@{ $paths{$dt0} },"$nStats[$j+1]\n");
						$paID = $#{ $paths{$dt0} };

						if(($paID == 0) || ($res[1] > $#{$pathsI{$dt0}})) {
							push(@{$pathsI{$dt0}},"$paID\n");
						} else {
							splice(@{$pathsI{$dt0}},$res[1],0,"$paID\n");
						}

						@ta = ();
						push(@ta,(($t3[4] <= 5) ? 1 : 0));
						push(@ta,(($t3[4] <= 4) ? 1 : 0));
						push(@ta,(($t3[4] == 0) ? 1 : 0));
						for($k=3;$k<=$#t3;$k++) {
							push(@ta,$t3[$k+2]);
						}
						push(@{ $pathsD{$dt0} },join("\t",@ta)."\n");
						
						if($refID >= 0) {
							$iI = $paID*2;
							while(($iI+1) > $#{$paRefsIbPa{$dt0}}) {
								push(@{$paRefsIbPa{$dt0}},"\n","\n");
							}
							$paRefsIbPa{$dt0}[$iI] = "$refID\n";
							$paRefsIbPa{$dt0}[$iI+1] = "1\n";

							$iI = $refID*2;
							while(($iI+1) > $#{$paRefsIbR{$dt0}}) {
								push(@{$paRefsIbR{$dt0}},"\n","\n");
							}
							chop($paRefsIbR{$dt0}[$iI]);
							chop($paRefsIbR{$dt0}[$iI+1]);
							@ta = split(/\t/,$paRefsIbR{$dt0}[$iI]);
							@tb = split(/\t/,$paRefsIbR{$dt0}[$iI+1]);
							$found = 0;
							for($k=0;$k<=$#ta;$k++) {
								if($ta[$k] == $paID) {
									$tb[$k] ++;
									$found = 1;
									last;
								}
							}
							if(!$found) {
								push(@ta,$paID);
								push(@tb,1);	
							}
							$paRefsIbR{$dt0}[$iI] = join("\t",@ta)."\n";
							$paRefsIbR{$dt0}[$iI+1] = join("\t",@tb)."\n";
						}

					}
					&writeVisitorLog($t1[0],"$t3[0]$t3[1]",$refID,$paID);
				} else {
					print NAVFILE "$nStats[$j]\n";
					print NAVFILE "$nStats[$j+1]\n";
					print NAVFILE "$nStats[$j+2]\n";
					$endCheck = 1;

					
				}
			} else {
				print NAVFILE "$nStats[$j]";
				print NAVFILE "$nStats[$j+1]";
				print NAVFILE "$nStats[$j+2]";
			}			
		}
	}
	close(NAVFILE);
	if($newPaths) {
		foreach $dt (keys %paths) {

			$pYr = substr($dt,0,2);
			$pMD = substr($dt,2);
			open (FILE2, ">$acct/L10HC_Archive/Paths/Y$pYr/PathsL_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Paths/Y$pYr/PathsL_$pMD.dat at LIB.writeNav()14");
			foreach $i (0 .. $#{$paths{$dt}}) {
				 print FILE2 $paths{$dt}[$i];
			}						
			close(FILE2);
		}
		foreach $dt (keys %pathsI) {
			$pYr = substr($dt,0,2);
			$pMD = substr($dt,2);
			open (FILE2, ">$acct/L10HC_Archive/Paths/Y$pYr/PathsI_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Paths/Y$pYr/PathsI_$pMD.dat at LIB.writeNav()15");
			foreach $i (0 .. $#{$pathsI{$dt}}) {
				 print FILE2 $pathsI{$dt}[$i];
			}						
			close(FILE2);
		}
	}
	foreach $dt (keys %pathsD) {
		$pYr = substr($dt,0,2);
		$pMD = substr($dt,2);
		open(FILE2, ">$acct/L10HC_Archive/Paths/Y$pYr/PathsD_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Paths/Y$pYr/PathsD_$pMD.dat at LIB.writeHitsArchive()16");
		foreach $i (0 .. $#{$pathsD{$dt}}) {
			 print FILE2 $pathsD{$dt}[$i];
		}
		close (FILE2);
	}					
	foreach $dt (keys %paRefsIbR) {
		$pYr = substr($dt,0,2);
		$pMD = substr($dt,2);
		open(FILE2, ">$acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbR_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbR_$pMD.dat at LIB.writeHitsArchive()17");
		foreach $i (0 .. $#{$paRefsIbR{$dt}}) {
			 print FILE2 $paRefsIbR{$dt}[$i];
		}
		close (FILE2);
	}					
	foreach $dt (keys %paRefsIbPa) {
		$pYr = substr($dt,0,2);
		$pMD = substr($dt,2);
		open(FILE2, ">$acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbPa_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/paRefs/Y$pYr/paRefsIbPa_$pMD.dat at LIB.writeHitsArchive()18");
		foreach $i (0 .. $#{$paRefsIbPa{$dt}}) {
			 print FILE2 $paRefsIbPa{$dt}[$i];
		}
		close (FILE2);
	}
	foreach $dt (keys %pgRefsIbR) {
		$pYr = substr($dt,0,2);
		$pMD = substr($dt,2);
		open(FILE2, ">$acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbR_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/pgRefs/Y$pYr/paRefsIbR_$pMD.dat at LIB.writeHitsArchive()19");
		foreach $i (0 .. $#{$pgRefsIbR{$dt}}) {
			 print FILE2 $pgRefsIbR{$dt}[$i];
		}
		close (FILE2);
	}
	foreach $dt (keys %pgRefsIbPg) {
		$pYr = substr($dt,0,2);
		$pMD = substr($dt,2);
		open(FILE2, ">$acct/L10HC_Archive/pgRefs/Y$pYr/pgRefsIbPg_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/pgRefs/Y$pYr/paRefsIbPg_$pMD.dat at LIB.writeHitsArchive()20");
		foreach $i (0 .. $#{$pgRefsIbPg{$dt}}) {
			 print FILE2 $pgRefsIbPg{$dt}[$i];
		}
		close (FILE2);
	}
	foreach $dt (keys %sRefs) {
		$pYr = substr($dt,0,2);
		$pMD = substr($dt,2);
		open(FILE2, ">$acct/L10HC_Archive/sRefs/Y$pYr/sRefsD_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/sRefs/Y$pYr/sRefsD_$pMD.dat at LIB.writeHitsArchive()21");
		foreach $i (0 .. $#{$sRefs{$dt}}) {
			 print FILE2 $sRefs{$dt}[$i];
		}
		close (FILE2);
	}
	
	
}

sub writeHitsArchive() {
	foreach $dt (keys %hitsA) {
		if(length($dt) == 6) {
			$pYr = substr($dt,0,2);
			$pMD = substr($dt,2);
			open(FILE, ">$acct/L10HC_Archive/Hits/Y$pYr/HitsD_$pMD.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Hits/Y$pYr/HitsD_$pMD.dat at LIB.writeHitsArchive()1");
			foreach $i (0 .. $#{$hitsA{$dt}}) {
				 print FILE $hitsA{$dt}[$i];
			}
			close (FILE);
		}
	}
}

sub writeVisitorLog() {
	my ($vID,$date,$rID,$pID) = @_;
	if(!$visitorLog) {
		return;
	}
	my $fID = '0';
	my $vI = $vID;
	$vLen = length($vID);
	
	if($vLen > 4) {
		$fID = substr($vID,$vLen-5,$vLen-4);
		$vI = substr($vID,$vLen-4);
	}
	my @t = ("\n");

	if(-e "$acct/L10HC_Archive/Visitor/Visitor_$fID.dat") {
		open (VLFILE, "$acct/L10HC_Archive/Visitor/Visitor_$fID.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Visitor/Visitor_$fID.dat at LIB.writeVisitorLog()");
		@t = <VLFILE>;
		close(VLFILE);
	}
	
	for(my $i=$#t;$i<$vI;$i++) {
		push(@t,"\n");
	}
	chop($t[$vI]);
	if(length($t[$vI]) > 0) {
		$t[$vI] .= "\t";
	}
	$t[$vI] .= "$date$rID,$pID\n";
	
	open (VLFILE, ">$acct/L10HC_Archive/Visitor/Visitor_$fID.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Visitor/Visitor_$fID.dat at archiveStats() 2");
	foreach(@t) {
		print VLFILE $_;
	}
	close(VLFILE);
}

sub bSearch() {
	my ($sItem, $items, $itemsChop, $iIndexes, $iIndexesChop, $retIndexIndex) = @_;
	my @res = (0,-1,-1);
	if(@$items == 0) {
		return (0,0,0);
	}
	my $sI0 = 0;
	my $sI1 = @$items -1;
	my $sIm = 0;
	my $sI = -1;
	my @sIe = ();
	my $sIn = $sI1/2;
	
	$sItem =~ s/\n\$//;
	my $done = 0;
	my $byIndex = 0;
	@sIe = split(/\./,$sIn);
	$sI = $sIe[0];
	if((@$iIndexes > 0) && (@$items == @$iIndexes)) { $byIndex = 1; }
	my $cItem = '';
	my $i = 0;
	while (!$done && ($i < 20)) {
		if($iIndexesChop) {
			chop($iIndexes->[$sI]);
		}
		$cItem = ($byIndex) ? $items->[$iIndexes->[$sI]] : $items->[$sI];
		if($itemsChop) {
			$iIndexes->[$sI] .= "\n";
			chop($cItem);
		}
		if($cItem eq $sItem) {
			$res[0] = 1;
			$done = 1;
		} else {
			if(($sI1 - $sI0) <= 0) {
				if($cItem lt $sItem) { $sI++; }
				$done = 1;
			} else {
				if($cItem lt $sItem) {
					if($sI == (@$items-1)) {
						$done = 1;
						$sI++;
					} else {
						$sI0 = $sI+1;
					}				

				} else { 
					if($sI == 0) {
						$done = 1;
					} else {
						$sI1 = $sI-1;
					}
					
				}
				if(!$done) {
					$sIn = (($sI1 - $sI0) / 2 ) + $sI0;
					@sIe = split(/\./,$sIn);
					$sI = $sIe[0];
				}
			}
		}

		$i ++;
	}
	if($i > 50) {
		&log_event("bSearch Steps exceeded sItem=$sItem ItemCount=$@items");
	}

	$res[1] = $sI;
	$res[2] = $sI;
	if($res[0] == 1) {		
		for($i=$sI;$i>=0;$i--) {
			$cItem = ($byIndex) ? $items->[$iIndexes->[$i]] : $items->[$i];
			if($itemsChop) {
				chop($cItem);
			}
			if($cItem eq $sItem) {
				$res[1] = $i;
			} else {
				last;
			}
		}
		for($i=$sI;$i<@$items;$i++) {
			$cItem = ($byIndex) ? $items->[$iIndexes->[$i]] : $items->[$i];
			if($itemsChop) {
				chop($cItem);
			}
			if($cItem eq $sItem) {
				$res[2] = $i;
			} else {
				last;
			}
		}

	}
	if($byIndex && !$retIndexIndex) {
		@res = ($res[0],$iIndexes->[$res[1]],$iIndexes->[$res[2]]);

	}
	$res[1] =~ s/\n$//;
	$res[2] =~ s/\n$//;
	return @res;	
}

sub filterPageURL() {
	my ($ret) = @_;
	$ret =~ s/http:\/\///i;
	$ret =~ s/https:\/\///i;
	$ret =~ s/\&/\%26/g;
	$ret =~ s/\/$indexPage/\//i;
	if($removePageWWW) {
		$ret =~ s/^www.//i;
	}
	return $ret;
}

1;