# v3.16 1/1/04

sub archiveStats () {
	unless (-e "$acct/L10HC_Archive/Doms/Y$curYr2") {mkdir "$acct/L10HC_Archive/Doms/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Refs/Y$curYr2") {mkdir "$acct/L10HC_Archive/Refs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEs/Y$curYr2") {mkdir "$acct/L10HC_Archive/SEs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/KWs/Y$curYr2") {mkdir "$acct/L10HC_Archive/KWs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/SEKWs/Y$curYr2") {mkdir "$acct/L10HC_Archive/SEKWs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/rTypes/Y$curYr2") {mkdir "$acct/L10HC_Archive/rTypes/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/sRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/sRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/pgRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/pgRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/paRefs/Y$curYr2") {mkdir "$acct/L10HC_Archive/paRefs/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Hits/Y$curYr2") {mkdir "$acct/L10HC_Archive/Hits/Y$curYr2", $filePermissions;}
	unless (-e "$acct/L10HC_Archive/Paths/Y$curYr2") {mkdir "$acct/L10HC_Archive/Paths/Y$curYr2", $filePermissions;}

	open (FILE, "$acct/L10HC_Archive/SiteHistory_Hits.dat") || &gen_error("Cannot read $acct/L10HC_Archive/SiteHistory_Hits.dat at archiveStats()");
	@hist = <FILE>;
	close(FILE);
	($aYr,$aMo,$aDay) = split(/\//,$dStat[0]);
	chomp($aDay);
	$yrSearchStr = "Y$aYr";
	$moSearchStr = "M$aYr/$aMo";
	($mYr,$mMo,$mDay) = &MondayOfWeek($aYr,$aMo,$aDay);
	$wkSearchStr = "W$mYr/$mMo/$mDay";
	$daySearchStr = "D$aYr/$aMo/$aDay";
	
	@dStatNew = ("$dateStamp\n");
	$keepY = 1;
	$keepM = 1;
	$keepW = 1;
	$keepD = 1;
	if($curYr ne $aYr) {
		$keepY = 0;
	}
	if(!$keepY || ($curMo ne $aMo)) {
		$keepM = 0;
	}
	($amYr,$amMo,$amDay) = &MondayOfWeek($curYr,$curMo,$curDay);
	if(!$keepY || ($amMo ne $mMo) || ($amDay ne $mDay)) {
		$keepW = 0;
	}
	if(!$keepY || !$keepM || $curDay ne $aDay) {
		$keepD = 0;
	}
	
	chomp($dStat[1]);	
	@pStats = split(/\t/,$dStat[1]);
	chop($dStat[4]);
	chop($dStat[5]);
	
	
	# Save hitory
	open(FILE, ">$acct/L10HC_Archive/SiteHistory_Hits.dat")|| &gen_error("Cannot open $acct/L10HC_Archive/SiteHistory_Hits.dat at archiveStats() 2");	
	&parseArchive();	
	close(FILE);
	
	# Save by Period
	$DoW = &DayOfWeek($aYr,$aMo,$aDay);
	open (FILE, "$acct/L10HC_Archive/Hits_byPeriod.dat") || &gen_error("Cannot read $acct/L10HC_Archive/Hits_byPeriod.dat at archiveStats()");
	@byPeriod = <FILE>;
	close(FILE);
	for($i=0;$i<=$#byPeriod;$i++) {
		chop($byPeriod[$i]);
	}
	$byPeriod[0] ++;

	if($byPeriod[0] == 1) {
		$byPeriod[1] = $dStat[4];
		$byPeriod[2] = $dStat[5];
		$byPeriod[3] = $dStat[4];
		$byPeriod[4] = $dStat[5];
	} else {
		@VbHr0 = split(/\t/,$byPeriod[1]);
		@HbHr0 = split(/\t/,$byPeriod[2]);
		@VbHr1 = split(/\t/,$byPeriod[3]);
		@HbHr1 = split(/\t/,$byPeriod[4]);
		@VbHr = split(/\t/,$dStat[4]);
		@HbHr = split(/\t/,$dStat[5]);
		for($i=0;$i<24;$i++) {
			$VbHr0[$i] += $VbHr[$i];
			$HbHr0[$i] += $HbHr[$i];
			$VbHr1[$i] = &roundNum(((13 * $VbHr1[$i]) + $VbHr[$i]) / 14,2);
			$HbHr1[$i] = &roundNum(((13 * $HbHr1[$i]) + $HbHr[$i]) / 14,2);
		} 
		$byPeriod[1] = join("\t",@VbHr0);
		$byPeriod[2] = join("\t",@HbHr0);
		$byPeriod[3] = join("\t",@VbHr1);
		$byPeriod[4] = join("\t",@HbHr1);
	}

	$byPeriod[5] = $dStat[4];
	$byPeriod[6] = $dStat[5];
	@DbDoW = split(/\t/,$byPeriod[7]);
	@VbDoW0 = split(/\t/,$byPeriod[8]);  # Total
	@HbDoW0 = split(/\t/,$byPeriod[9]); 
	@VbDoW1 = split(/\t/,$byPeriod[10]); # W Ave
	@HbDoW1 = split(/\t/,$byPeriod[11]);
	@VbDoW2 = split(/\t/,$byPeriod[12]); # Today
	@HbDoW2 = split(/\t/,$byPeriod[13]);
	$DbDoW[$DoW] ++;
	if($DbDoW[$DoW] == 1) {
		$VbDoW1[$DoW] = $pStats[4];
		$HbDoW1[$DoW] = $pStats[9];
	} else {
		$VbDoW1[$DoW] = &roundNum(((3 * $VbDoW1[$DoW]) + $pStats[4]) / 4,2);
		$HbDoW1[$DoW] = &roundNum(((3 * $HbDoW1[$DoW]) + $pStats[9]) / 4,2);
	}	
	$VbDoW0[$DoW] += $pStats[4];
	$HbDoW0[$DoW] += $pStats[9];
	$VbDoW2[$DoW] = $pStats[4];
	$HbDoW2[$DoW] = $pStats[9];
	$byPeriod[7] = join("\t",@DbDoW);
	$byPeriod[8] = join("\t",@VbDoW0);
	$byPeriod[9] = join("\t",@HbDoW0);
	$byPeriod[10] = join("\t",@VbDoW1);
	$byPeriod[11] = join("\t",@HbDoW1);
	$byPeriod[12] = join("\t",@VbDoW2);
	$byPeriod[13] = join("\t",@HbDoW2);
	if(!$keepW) {
		$byPeriod[14] = $byPeriod[12];
		$byPeriod[15] = $byPeriod[13];
		$byPeriod[12] = "0\t0\t0\t0\t0\t0\t0";
		$byPeriod[13] = "0\t0\t0\t0\t0\t0\t0";
	}
	@DbDoM = split(/\t/,$byPeriod[16]);
	@VbDoM0 = split(/\t/,$byPeriod[17]);
	@HbDoM0 = split(/\t/,$byPeriod[18]);
	@VbDoM1 = split(/\t/,$byPeriod[19]);
	@HbDoM1 = split(/\t/,$byPeriod[20]);
	@VbDoM2 = split(/\t/,$byPeriod[21]);
	@HbDoM2 = split(/\t/,$byPeriod[22]);
	$DbDoM[$aDay-1] ++;
	if($DbDoM[$aDay-1] == 1) {
		$VbDoM1[$aDay-1] = $pStats[4];
		$HbDoM1[$aDay-1] = $pStats[9];
	} else {
		$VbDoM1[$aDay-1] = &roundNum(((3 * $VbDoM1[$aDay-1]) + $pStats[4]) / 4,2);
		$HbDoM1[$aDay-1] = &roundNum(((3 * $HbDoM1[$aDay-1]) + $pStats[9]) / 4,2);
	}	
	$VbDoM0[$aDay-1] += $pStats[4];
	$HbDoM0[$aDay-1] += $pStats[9];
	$VbDoM2[$aDay-1] = $pStats[4];
	$HbDoM2[$aDay-1] = $pStats[9];
	$byPeriod[16] = join("\t",@DbDoM);
	$byPeriod[17] = join("\t",@VbDoM0);
	$byPeriod[18] = join("\t",@HbDoM0);
	$byPeriod[19] = join("\t",@VbDoM1);
	$byPeriod[20] = join("\t",@HbDoM1);
	$byPeriod[21] = join("\t",@VbDoM2);
	$byPeriod[22] = join("\t",@HbDoM2);
	if(!$keepM) {
		$byPeriod[23] = $byPeriod[21];
		$byPeriod[24] = $byPeriod[22];
		$byPeriod[21] = "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0";
		$byPeriod[22] = "0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0";
	}
	
	
	push(@dStatNew,"$pStats[0]\t".($pStats[1]*$keepY)."\t".($pStats[2]*$keepM)."\t".($pStats[3]*$keepW)."\t".($pStats[4]*$keepD)."\t$pStats[5]\t".($pStats[6]*$keepY)."\t".($pStats[7]*$keepM)."\t".($pStats[8]*$keepW)."\t".($pStats[9]*$keepD)."\n");
	push(@dStatNew,"$dStat[2]");
	push(@dStatNew,"$dStat[3]");
	push(@dStatNew,"0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n");
	push(@dStatNew,"0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\n");
	
	open (FILE, ">$acct/L10HC_Archive/Hits_byPeriod.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Hits_byPeriod.dat at archiveStats() 2");
	foreach (@byPeriod) { print FILE "$_\n"; }
	close (FILE);
	
	
	for($j=6;$j<=$#dStat;$j++) {
		push(@dStatNew,"$dStat[$j]");
		$j++;
		@pStats = split(/\t/,$dStat[$j]);
		push(@dStatNew,"$pStats[0]\t".($pStats[1]*$keepY)."\t".($pStats[2]*$keepM)."\t".($pStats[3]*$keepW)."\t".($pStats[4]*$keepD)."\t$pStats[5]\t".($pStats[6]*$keepY)."\t".($pStats[7]*$keepM)."\t".($pStats[8]*$keepW)."\t".($pStats[9]*$keepD)."\n");
	}
	open (DSTAT_FH, ">$acct/L10HC_Hits.dat") || &gen_error("Cannot open $acct/L10HC_Hits.dat at archiveStats() 2");
	foreach (@dStatNew) { print DSTAT_FH $_; }
	close (DSTAT_FH);
	

	if(!$keepD) {
		if(-e "$acct/L10HC_IPL2.dat") { unlink("$acct/L10HC_IPL2.dat"); }
		rename("$acct/L10HC_IPL.dat","$acct/L10HC_IPL2.dat"); 
		open(FILE, ">$acct/L10HC_IPL.dat")|| &gen_error("Cannot open $acct/L10HC_IPL.dat at archiveStats() 2");	
		close(FILE);
		if(-e "$acct/L10HC_IPI2.dat") { unlink("$acct/L10HC_IPI2.dat"); }
		rename("$acct/L10HC_IPI.dat","$acct/L10HC_IPI2.dat"); 
		open(FILE, ">$acct/L10HC_IPI.dat")|| &gen_error("Cannot open $acct/L10HC_IPI.dat at archiveStats() 2");	
		close(FILE);
		if(-e "$acct/L10HC_IPD2.dat") { unlink("$acct/L10HC_IPD2.dat"); }
		rename("$acct/L10HC_IPD.dat","$acct/L10HC_IPD2.dat"); 
		open(FILE, ">$acct/L10HC_IPD.dat")|| &gen_error("Cannot open $acct/L10HC_IPD.dat at archiveStats() 2");	
		close(FILE);

		if(-e "$acct/L10HC_Security2.log") { unlink("$acct/L10HC_Security2.log"); } 
		rename("$acct/L10HC_Security.log","$acct/L10HC_Security2.log");
		open(FILE, ">$acct/L10HC_Security.log")|| &gen_error("Cannot open $acct/L10HC_Security.log at archiveStats() 2");	
		close(FILE);

		$size = (-s "L10HC_Error.log")/1024;
		if($size > $logLimit) {
			&log_event("Error log reset size=$size");
			if(-e "L10HC_Errors2.log") { unlink("L10HC_Errors2.log"); } 
			rename("L10HC_Errors.log","L10HC_Errors2.log");
			open(FILE, ">L10HC_Errors.log")|| &gen_error("Cannot open L10HC_Errors.log at archiveStats() 2");	
			close(FILE);
		}


		$size = (-s "L10HC_Events.log")/1024;
		if($size > $logLimit) {
			&log_event("Event log reset size=$size");
			if(-e "L10HC_Events2.log") { unlink("L10HC_Events2.log"); } 
			rename("L10HC_Events.log","L10HC_Events2.log");
			open(FILE, ">L10HC_Events.log")|| &gen_error("Cannot open L10HC_Events.log at archiveStats() 2");	
			close(FILE);
		}


	}
	
	&log_event("Stats Archived!");
	
	&archiveExtended();
	open (FILE, ">$acct/L10HC_Extended.dat") || &gen_error("Cannot open $acct/L10HC_Extended.dat at archiveRefs() 2");
	close(FILE);
	
	@dStat = @dStatNew;
	
}

sub parseArchive() {
	print FILE "1\n"; # version number (for binary search indexes in v2)
	print FILE "$pStats[0]\t$pStats[5]\n";
	
	$updateY = 0;
	$updateM = 0;
	$updateW = 0;
	$updateD = 0;
	$updating = 0;
	for($i=2;$i<=$#hist;$i++) {
		if(!$updateY) {
			if(substr($hist[$i],0,1) eq "Y") {
				if($hist[$i] =~ m/$yrSearchStr/) {
					print FILE "$yrSearchStr\t$pStats[1]\t$pStats[6]\n";	
					$updateY = 1;
				} else {
					print FILE "$hist[$i]";
				}
			} else {
				print FILE "$yrSearchStr\t$pStats[1]\t$pStats[6]\n";	
				$updateY = 1;
				$i--;
			}	
		} elsif(!$updateM) {
			if(substr($hist[$i],0,1) eq "M") {
				if($hist[$i] =~ m/$moSearchStr/) {
					print FILE "$moSearchStr\t$pStats[2]\t$pStats[7]\n";	
					$updateM = 1;
				} else {
					print FILE "$hist[$i]";
				}
			} else {
				print FILE "$moSearchStr\t$pStats[2]\t$pStats[7]\n";	
				$updateM = 1;
				$i--;
			}
		} elsif(!$updateW) {
			if(substr($hist[$i],0,1) eq "W") {
				if($hist[$i] =~ m/$wkSearchStr/) {
					print FILE "$wkSearchStr\t$pStats[3]\t$pStats[8]\n";	
					$updateW = 1;
				} else {
					print FILE "$hist[$i]";
				}
			} else {
				print FILE "$wkSearchStr\t$pStats[3]\t$pStats[8]\n";	
				$updateW = 1;
				$i--;
			}
		} elsif(!$updateD) {
			if(substr($hist[$i],0,1) eq "D") {
				if($hist[$i] =~ m/$daySearchStr/) {
					print FILE "$daySearchStr\t$pStats[4]\t$pStats[9]\n";	
					$updateD = 1;
				} else {
					print FILE "$hist[$i]";
				}
			} else {
				print FILE "$daySearchStr\t$pStats[4]\t$pStats[9]\n";	
				$updateD = 1;
				$i--;
			}		
		} else {
			if(length($hist[$i]) > 3) {
				print FILE "$hist[$i]";
			}
		}
	}
	
	if(!$updateY) {
		print FILE "$yrSearchStr\t$pStats[1]\t$pStats[6]\n";	
	}
	if(!$updateM) {
		print FILE "$moSearchStr\t$pStats[2]\t$pStats[7]\n";	
	}
	if(!$updateW) {
		print FILE "$wkSearchStr\t$pStats[3]\t$pStats[8]\n";	
	}
	if(!$updateD) {
		print FILE "$daySearchStr\t$pStats[4]\t$pStats[9]\n";	
	}
}

sub archiveExtended() {
	open (FILE, "$acct/L10HC_Extended.dat");
	@data = <FILE>;
	close(FILE);

	open (FILE, "L10HC_Languages.txt");
	@Lang = <FILE>;
	close(FILE);
	%LangTran = ();

	for($i=0;$i<=$#Lang;$i++) {
		chop($Lang[$i]);
		my @l = split(/\t/,$Lang[$i]);
		$LangTran{$l[0]} = $l[1];
	}

	open (FILE, "L10HC_OSs.txt");
	@OSList = <FILE>;
	close(FILE);
	@OS_Keys = ('');
	@OS_Vals = ('[unknown]');
	%OS_Cnts = ('0' => 0);

	for($i=0;$i<=$#OSList;$i++) {
		chop($OSList[$i]);
		my @l = split(/\t/,$OSList[$i]);
		push(@OS_Vals,$l[0]);
		push(@OS_Keys,$l[1]);
		$OS_Cnts{"".($i+1)} = 0;
	}

	print "OS_Keys=$OS_Keys[1]<br>";

	%Browser = ();
	%BrowserVer = ();
	%Language = ();
	%CookieSup = ();
	%JSSup = ();
	%ScreenClr = ();
	%ScreenRes = ();
	%unkown = ();
	%anal = ();

	for($i=0;$i<=$#data;$i++) {
		@dE = split(/\t/,$data[$i]);
		if($dE[1] eq "Microsoft Internet Explorer") {
			@dE2 = split(/;/,$dE[0]);
			$dE2[1] =~ s/^ //;
			$BrowserVer{$dE2[1]} ++;
			$Browser{"MSIE"}++;
			if(substr($dE2[2],length($dE2[2])-1,1) eq ')') {
				chop($dE2[2]);
			}
			$known = 0;
			for($j=1;$j<=$#OS_Keys;$j++) {
				if($dE[0] =~ m/$OS_Keys[$j]/i) {
					$OS_Cnts{"$j"} ++;
					$known = 1;
					last;
				}
			}
			if(!$known) {
				$OS_Cnts{'0'} ++;
			}
		} elsif(($dE[1] eq "Netscape") || ($dE[1] eq "Konqueror") || ($dE[1] eq "Opera")) {
			@dE2 = split(/ /,$dE[2]);
			if(($dE[1] eq "Netscape") && ($dE2[0] >= 5)) {
				$si = index($dE[0],"Netscape6/");
				if(($si = index($dE[0],"Netscape6/"))  >= 0) {
					$BrowserVer{"$dE[1] ".substr($dE[0],$si+10)} ++;	
				} elsif(($si = index($dE[0],"Netscape/"))  >= 0) {
					$BrowserVer{"$dE[1] ".substr($dE[0],$si+9)} ++;	
				} else {
					$BrowserVer{"Netscape [version unkown]"}++;
				}
			} else {
				$BrowserVer{"$dE[1] $dE2[0]"} ++;
			}
			$Browser{$dE[1]} ++;
			$known = 0;
			for($j=1;$j<=$#OS_Keys;$j++) {
				if($dE[0] =~ m/$OS_Keys[$j]/i) {
					$OS_Cnts{"$j"} ++;
					$known = 1;
					last;
				}
			}
			if(!$known) {
				$OS_Cnts{'0'} ++;
			}
		} else {
			$Browser{'[unknown]'} ++;
			$OS{'[unknown]'} ++;
		}
		@dE2 = split(/-/,$dE[3]);
		if(exists $LangTran{$dE2[0]}) {
			$Language{$LangTran{$dE2[0]}} ++;
		} else {
			$Language{'[unknown]'} ++;
		}
		$CookieSup{$dE[4]} ++;
		$JSSup{$dE[5]} ++;
		$ScreenClr{"$dE[6] bit"} ++;
		$ScreenRes{$dE[7]} ++;


	}
	
	if(exists $browserVer{''}) {
		$browserVer{'[unknown]'} += $browserVer{''};
		delete $browserVer{''};
	}	
	if(exists $browserVer{' '}) {
		$browserVer{'[unknown]'} += $browserVer{''};
		delete $browserVer{''};
	}
	
	%OS_Tran = ();
	foreach (keys %OS_Cnts) {
		$OS_Tran{$OS_Vals[$_]} += $OS_Cnts{$_}
	}
	
	if(-e "$acct/L10HC_Archive/OSs.dat") {
		open (FILE, "$acct/L10HC_Archive/OSs.dat") || &gen_error("Cannot open $acct/L10HC_Archive/OSs.dat at archiveStats() 2");
		foreach (<FILE>) {
			chop($_);
			@l = split(/\t/,$_);
			$OS_Tran{$l[0]} += (9 * $l[1]);
			$OS_Tran{$l[0]} = &roundNum($OS_Tran{$l[0]} / 10,3);
			if($OS_Tran{$l[0]} < 0.01) {
				delete $OS_Tran{$l[0]};
			}
		}
		close (FILE);
	}
	open (FILE, ">$acct/L10HC_Archive/OSs.dat") || &gen_error("Cannot open $acct/L10HC_Archive/OSs.dat at archiveStats() 2");
	foreach (sort {$OS_Tran{$b} <=> $OS_Tran{$a}} (keys %OS_Tran)) { 
		print FILE "$_\t$OS_Tran{$_}\n"; 
	}
	close (FILE);
	
	if(-e "$acct/L10HC_Archive/Browsers.dat") {
		open (FILE, "$acct/L10HC_Archive/Browsers.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Browsers.dat at archiveStats() 2");
		foreach (<FILE>) {
			chop($_);
			@l = split(/\t/,$_);
			$Browser{$l[0]} += (9 * $l[1]);
			$Browser{$l[0]} = &roundNum(($Browser{$l[0]} / 10),3);
			if($Browser{$l[0]} < 0.01) {
				delete $Browser{$l[0]};
			}
		}
		close (FILE);
	}
	open (FILE, ">$acct/L10HC_Archive/Browsers.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Browsers.dat at archiveStats() 2");
	foreach (sort {$Browser{$b} <=> $Browser{$a}} (keys %Browser)) { 
		print FILE "$_\t$Browser{$_}\n"; 
	}
	close (FILE);
	
	if(-e "$acct/L10HC_Archive/BrowserVers.dat") {
		open (FILE, "$acct/L10HC_Archive/BrowserVers.dat") || &gen_error("Cannot open $acct/L10HC_Archive/BrowserVers.dat at archiveStats() 2");
		foreach (<FILE>) {
			chop($_);
			@l = split(/\t/,$_);
			$BrowserVer{$l[0]} += (9 * $l[1]);
			$BrowserVer{$l[0]} = &roundNum($BrowserVer{$l[0]} / 10,3);
			if($BrowserVer{$l[0]} < 0.01) {
				delete $BrowserVer{$l[0]};
			}
		}
		close (FILE);
	}
	open (FILE, ">$acct/L10HC_Archive/BrowserVers.dat") || &gen_error("Cannot open $acct/L10HC_Archive/BrowserVers.dat at archiveStats() 2");
	foreach (sort {$BrowserVer{$b} <=> $BrowserVer{$a}} (keys %BrowserVer)) { 
		print FILE "$_\t$BrowserVer{$_}\n"; 
	}
	close (FILE);
	
	if(-e "$acct/L10HC_Archive/Languages.dat") {
		open (FILE, "$acct/L10HC_Archive/Languages.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Languages.dat at archiveStats() 2");
		foreach (<FILE>) {
			chop($_);
			@l = split(/\t/,$_);
			$Language{$l[0]} += (9 * $l[1]);
			$Language{$l[0]} = &roundNum($Language{$l[0]} / 10,3);
			if($Language{$l[0]} < 0.01) {
				delete $Language{$l[0]};
			}
		}
		close (FILE);
	}
	open (FILE, ">$acct/L10HC_Archive/Languages.dat") || &gen_error("Cannot open $acct/L10HC_Archive/Languages.dat at archiveStats() 2");
	foreach (sort {$Language{$b} <=> $Language{$a}} (keys %Language)) { 
		print FILE "$_\t$Language{$_}\n"; 
	}
	close (FILE);
	
	if(-e "$acct/L10HC_Archive/ScreenClrs.dat") {
		open (FILE, "$acct/L10HC_Archive/ScreenClrs.dat") || &gen_error("Cannot open $acct/L10HC_Archive/ScreenClrs.dat at archiveStats() 2");
		foreach (<FILE>) {
			chop($_);
			@l = split(/\t/,$_);
			$ScreenClr{$l[0]} += (9 * $l[1]);
			$ScreenClr{$l[0]} = &roundNum($ScreenClr{$l[0]} / 10,3);
			if($ScreenClr{$l[0]} < 0.01) {
				delete $ScreenClr{$l[0]};
			}
		}
		close (FILE);
	}
	open (FILE, ">$acct/L10HC_Archive/ScreenClrs.dat") || &gen_error("Cannot open $acct/L10HC_Archive/ScreenClrs.dat at archiveStats() 2");
	foreach (sort {$ScreenClr{$b} <=> $ScreenClr{$a}} (keys %ScreenClr)) { 
		print FILE "$_\t$ScreenClr{$_}\n"; 
	}
	close (FILE);
	
	if(-e "$acct/L10HC_Archive/ScreenRes.dat") {
		open (FILE, "$acct/L10HC_Archive/ScreenRes.dat") || &gen_error("Cannot open $acct/L10HC_Archive/ScreenRes.dat at archiveStats() 2");
		foreach (<FILE>) {
			chop($_);
			@l = split(/\t/,$_);
			$ScreenRes{$l[0]} += (9 * $l[1]);
			$ScreenRes{$l[0]} = &roundNum($ScreenRes{$l[0]} / 10,3);
			if($ScreenRes{$l[0]} < 0.01) {
				delete $ScreenRes{$l[0]};
			}
		}
		close (FILE);
	}
	open (FILE, ">$acct/L10HC_Archive/ScreenRes.dat") || &gen_error("Cannot open $acct/L10HC_Archive/ScreenRes.dat at archiveStats() 2");
	foreach (sort {$ScreenRes{$b} <=> $ScreenRes{$a}} (keys %ScreenRes)) { 
		print FILE "$_\t$ScreenRes{$_}\n"; 
	}
	close (FILE);
	

}

1;