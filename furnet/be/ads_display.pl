############################################
##                                        ##
##          WebAdverts (Display)          ##
##           by Darryl Burgdorf           ##
##       (e-mail burgdorf@awsd.com)       ##
##                                        ##
##             version: 2.02              ##
##         last modified: 6/25/99         ##
##           copyright (c) 1999           ##
##                                        ##
##    latest version is available from    ##
##        http://awsd.com/scripts/        ##
##                                        ##
############################################

# NOTHING BELOW THIS LINE NEEDS TO BE ALTERED!

sub ADVsetup {
	$AdvertChosen = 0;
	$ADVtime = time;
	($ADVmin,$ADVhour,$ADVmday,$ADVmon,$ADVyear) =
	  (localtime($ADVtime))[1,2,3,4,5];
	if ($ADVmin < 10) { $ADVmin = "0$ADVmin"; }
	if ($ADVhour < 10) { $ADVhour = "0$ADVhour"; }
	if ($ADVmday < 10) { $ADVmday = "0$ADVmday"; }
	$ADVmon++;
	if ($ADVmon < 10) { $ADVmon = "0$ADVmon"; }
	$ADVyear = $ADVyear+1900;
	unless ($ADVUseLocking) {
		&ADVMasterLockOpen;
		if ($ADVlockerror) {
			return;
		}
	}
	$TrimmedIP = $ENV{'REMOTE_ADDR'};
	$TrimmedIP =~ s/(\d*\.\d*\.\d*)\.\d*/$1/;
	$ADVshown = 0;
	$ADVWrapCounter = 0;
	if ($ADVQuery =~ /page=([^\s&;\?]*)/i) {
		$displaypage = $1;
		$NonSSI = 1;
	}
	if ($ADVQuery =~ /zone=([^\s&;\?]*)/i) {
		$advertzone = $1;
	}
	unless ($advertzone) { $advertzone = "unzoned"; }
	if ($ADVQuery =~ /setdest=([^\s&;\?]*)/i) {
		$SetDest = $1;
		$SetDest =~ s/[^\w_-]//g;
		$SetDest =~ tr/A-Z/a-z/;
	}
	if (($ADVQuery =~ /advert=([^\s&;\?]*)/i)
	  || ($ADVQuery =~ /banner=([^\s&;\?]*)/i)) {
		$displayad = $1;
		$displayad =~ s/[^\w_-]//g;
		$displayad =~ tr/A-Z/a-z/;
		if ($ADVQuery =~ /url=(.*)/i) {
			$rawmodedest = $1;
		}
		&gotoad;
		return;
	}
	unless ($NonSSI || $ADVNoPrint) { print "Content-type: text/html\n\n"; }
	if (($ADVQuery =~ /ID=([^\s&;\?]*)/i)
	  || ($ADVQuery =~ /member=([^\s&;\?]*)/i)) {
		$ADVID = $1;
		$ADVID =~ s/[^\w_-]//g;
		$ADVID =~ tr/A-Z/a-z/;
	}
	&ADVLockOpen (ADVCOUNT, "adcount.txt");
	if ($ADVlockerror) {
		&ADVLockClose (ADVCOUNT, "adcount.txt");
		return;
	}
	@ADVcountlines = <ADVCOUNT>;
	if (($ADVtime - $ADVcountlines[2]) > 250000000) {
		$ADVcountlines[0] = 1;
		$ADVcountlines[1] = "0";
		$ADVcountlines[2] = time;
	}
	open (ADVLIST, "<$adverts_dir/adlist.txt");
	while ($ADVlist = <ADVLIST>) {
		push (@ADVcountlines,$ADVlist);
	}
	close (ADVLIST);
	foreach $ADVline (@ADVcountlines) {
		chop ($ADVline) if ($ADVline =~ /\n$/);
	}
	$ADVcount = $ADVcountlines[0];
	@ADVcount = split(/\|/,$ADVcount);
	foreach $ADVcount (@ADVcount) {
		($ADVone,$ADVtwo) = split(/=/,$ADVcount);
		unless ($ADVtwo) { $ADVtwo = "unzoned"; }
		$zonecount{$ADVtwo} = $ADVone;
	}
	unless ($zonecount{$advertzone}) { $zonecount{$advertzone} = 1; }
	$ADVexposures = $ADVcountlines[1];
	($ADVexposures,@ADVcycles) = split (/\|/, $ADVexposures);
	foreach $ADVcycles (@ADVcycles) {
		($ADVone,$ADVtwo) = split(/=/,$ADVcycles);
		unless ($ADVtwo) { $ADVtwo = "unzoned"; }
		$cyclecount{$ADVtwo} = $ADVone;
	}
	unless ($cyclecount{$advertzone}) { $cyclecount{$advertzone} = 1; }
	if ($advertzone eq "ShowAll") { &ADVshowall; }
	else { &ADVdisplayad; }
	if (($AdvertChosen < 1) && $DefaultBanner) {
		$ShowDefaultBanner = 1;
		&ADVdisplayad;
	}
	$ADVcountlines[0] = "";
	foreach $key (keys %zonecount) {
		$ADVcountlines[0] =
		  $ADVcountlines[0]."$zonecount{$key}=$key|";
	}
	$ADVcountlines[1] = "$ADVexposures|";
	foreach $key (keys %cyclecount) {
		$ADVcountlines[1] =
		  $ADVcountlines[1]."$cyclecount{$key}=$key|";
	}
	seek(ADVCOUNT, 0, 0);
	foreach $key (0..2) {
		print ADVCOUNT "$ADVcountlines[$key]\n";
	}
	truncate (ADVCOUNT, tell(ADVCOUNT));
	&ADVLockClose (ADVCOUNT, "adcount.txt");
	unless ($ADVUseLocking) {
		&ADVMasterLockClose;
	}
	if ($ADVLogIP) {
		unless ($DupViewTime) { $DupViewTime = 3600; }
		if ($DupViewTime > 43200) { $DupViewTime = 43200; }
	}
}

sub ADVdisplayad {
	if ($ShowDefaultBanner) {
		$ADVdisplayad = $DefaultBanner;
	}
	elsif ($SetDest) {
		$ADVdisplayad = $SetDest;
	}
	else {
		$ADVWrapCounter++;
		if ($ADVWrapCounter > @ADVcountlines-3) {
			return;
		}
		$ADVdisplayad = $ADVcountlines[$zonecount{$advertzone}+2];
		$ADVcycles = $cyclecount{$advertzone};
		$zonecount{$advertzone}++;
		if ($zonecount{$advertzone} > @ADVcountlines-3) {
			$zonecount{$advertzone} = 1;
			$cyclecount{$advertzone}++;
		}
		if ($ADVID eq $ADVdisplayad) {
			&ADVdisplayad;
			return;
		}
	}
	&ADVLockOpen (ADVDISPLAY, "$ADVdisplayad.txt");
	if ($ADVlockerror) {
		&ADVLockClose (ADVDISPLAY, "$ADVdisplayad.txt");
		$SetDest = "";
		unless ($ShowDefaultBanner) {
			&ADVdisplayad;
		}
		return;
	}
	@ADVdisplaylines = <ADVDISPLAY>;
	foreach $ADVline (@ADVdisplaylines) {
		chop ($ADVline) if ($ADVline =~ /\n$/);
	}
	($ADVmax,$ADVshown,$ADVvisits,
	  $ADVurl,$ADVimage,$ADVheight,$ADVwidth,
	  $ADValt,$ADVpass,$ADVtext,$ADVstart,
	  $ADVweight,$ADVzone,$ADVborder,$ADVtarget,
	  $ADVraw,$ADVratio,$ADVname,$ADVemail,
	  $ADVdisplayzone) = @ADVdisplaylines;
	($ADVmax,$ADVmaxtype) = split (/\|/, $ADVmax);
	unless ($ADVmaxtype) { $ADVmaxtype = "E"; }
	($ADVdisplayratio,$ADVdisplaycount) = split (/\|/, $ADVratio);
	$ADVrealmax = $ADVmax;
	if (($ADVmaxtype eq "E") && ($ADVdisplayratio > 0)) {
		$ADVrealmax += int($ADVdisplaycount/$ADVdisplayratio);
	}
	if ($ADVmaxtype eq "N") {
		if ($ADVdisplayratio > 0) {
			$ADVrealmax = int($ADVdisplaycount/$ADVdisplayratio);
		}
		else {
			$ADVrealmax = $ADVshown+1;
		}
	}
	($ADVtext,$ADVtexttype) = split (/\|/, $ADVtext);
	unless ($ADVtexttype) { $ADVtexttype = "B"; }
	if ($Ztext) { $ADVtext = $Ztext; }
	if ($Zalt) { $ADValt = $Zalt; }
	if ($Ztarget) { $ADVtarget = $Ztarget; }
	if ($Zheight) { $ADVheight = $Zheight; }
	if ($Zwidth) { $ADVwidth = $Zwidth; }
	if ($Zborder) { $ADVborder = $Zborder; }
	unless ($ShowDefaultBanner || $SetDest) {
		if ((($advertzone ne "unzoned") && ($advertzone ne "ShowAll")
		  && (length($ADVzone) > 2) && ($ADVzone !~ /\s$advertzone\s/))
		  || !($ADVimage || $ADVraw)
		  || ($ADVweight < 1)
		  || (((($ADVmaxtype eq "E") || ($ADVmaxtype eq "N"))
		  && ($ADVrealmax <= $ADVshown))
		  && (($ADVdisplayratio < 1) || ($advertzone ne "ShowAll")))
		  || (($ADVmaxtype eq "C") && ($ADVrealmax <= $ADVvisits))
		  || (($ADVmaxtype eq "D") && ($ADVrealmax <= $ADVtime))
		  || ($ADVstart > $ADVtime)
		  || ((($ADVcycles/$ADVweight) != int($ADVcycles/$ADVweight))
		  && ($advertzone ne "ShowAll"))) {
			&ADVLockClose (ADVDISPLAY, "$ADVdisplayad.txt");
			&ADVdisplayad;
			return;
		}
	}
	if ($SetDest) {
		if (!($ADVimage || $ADVraw)
		  || ($ADVweight < 1)
		  || (((($ADVmaxtype eq "E") || ($ADVmaxtype eq "N"))
		  && ($ADVrealmax <= $ADVshown))
		  && (($ADVdisplayratio < 1) || ($advertzone ne "ShowAll")))
		  || (($ADVmaxtype eq "C") && ($ADVrealmax <= $ADVvisits))
		  || (($ADVmaxtype eq "D") && ($ADVrealmax <= $ADVtime))
		  || ($ADVstart > $ADVtime)) {
			&ADVLockClose (ADVDISPLAY, "$ADVdisplayad.txt");
			$SetDest = "";
			&ADVdisplayad;
			return;
		}
	}
	$DuplicateView = 0;
	if ($ADVLogIP) {
		&ADVLockOpen (DAILYLOG,"$ADVdisplayad.ips");
		if ($ADVlockerror) {
			&ADVLockClose (DAILYLOG,"$ADVdisplayad.ips");
			return;
		}
		undef (@ADVips);
		while ($ADVline = <DAILYLOG>) {
			$ADVip = int($ADVline);
			unless (($ADVtime-$ADVip) > 43200) {
				push (@ADVips,$ADVline);
			}
			if ((($ADVtime-$ADVip) < $DupViewTime)
			  && ($ADVline =~ /$TrimmedIP\./)
			  && ($ADVline =~ /- E -/)) {
				$DuplicateView = 1;
			}
		}
		seek (DAILYLOG, 0, 0);
		foreach $ADVline (@ADVips) {
			print DAILYLOG "$ADVline";
		}
		unless ($DuplicateView) {
			print DAILYLOG "$ADVtime - $ADVhour:$ADVmin - E - ";
			print DAILYLOG "$ENV{'REMOTE_ADDR'}\n";
		}
		truncate (DAILYLOG, tell(DAILYLOG));
		&ADVLockClose (DAILYLOG, "$ADVdisplayad.ips");
	}
	unless ($DuplicateView) {
		$ADVexposures++;
	}
	@ADVimage = split (/\|/,$ADVimage);
	$imagecount = @ADVimage;
	srand();
	$ADVdisplayimage = @ADVimage[int(rand($imagecount))];
	if ($NonSSI) {
		&ADVLockOpen (NONSSILOG,"nonssi.log");
		if ($ADVlockerror) {
			&ADVLockClose (NONSSILOG,"nonssi.log");
			&ADVLockClose (ADVDISPLAY, "$ADVdisplayad.txt");
			return;
		}
		$NONSSIsize = int((stat("$adverts_dir/nonssi.log"))[7]);
		seek(NONSSILOG, $NONSSIsize, 0);
		print NONSSILOG "$ADVtime $TrimmedIP $displaypage ";
		print NONSSILOG "$advertzone | $ADVdisplayad\n";
		truncate (NONSSILOG, tell(NONSSILOG));
		&ADVLockClose (NONSSILOG, "nonssi.log");
		print "Status: 302 Found\n";
		print "Location: $ADVdisplayimage\n\n";
	}
	elsif ($ADVraw) {
		srand();
		$ADVrand = int(rand(100))+1;
		$ADVrealraw = $ADVraw;
		$ADVrealraw =~ s/<NLB>/\n/g;
		$ADVrealraw =~ s/<RAND>/$ADVrand/g;
		$ADVrealraw =~ s/<URL>/$display_cgi?banner=$ADVdisplayad&url=/g;
		print "$ADVrealraw\n";
	}
	else {
		if ($ADVtext && ($ADVtexttype eq "T")
		  && ($advertzone ne "ShowAll")) {
			print "<SMALL>";
			if ($ADVurl) {
				print "<A HREF=\"$display_cgi?";
				print "banner=$ADVdisplayad\"";
				if ($ADVtarget eq "_top") {
					print " TARGET=\"$ADVtarget\"";
				}
				elsif ($ADVtarget) {
					print " $ADVtarget";
				}
				print ">";
			}
			print "$ADVtext";
			if ($ADVurl) {
				print "</A>";
			}
			print "</SMALL><BR>";
		}
		if ($ExchangeLogo) {
			if ($ExchangeURL) {
				print "<A HREF=\"$ExchangeURL\"";
				if ($ADVtarget eq "_top") {
					print " TARGET=\"$ADVtarget\"";
				}
				elsif ($ADVtarget) {
					print " $ADVtarget";
				}
				print ">";
			}
			print "<IMG SRC=\"$ExchangeLogo\"";
			if ($ExchangeLogoHeight && $ExchangeLogoWidth) {
				print " HEIGHT=$ExchangeLogoHeight";
				print " WIDTH=$ExchangeLogoWidth";
			}
			if ($ExchangeName) {
				print " ALT=\"$ExchangeName\"";
			}
			print " ISMAP>";
			if ($ExchangeURL) {
				print "</A>";
			}
		}
		if ($ADVurl) {
			print "<A HREF=\"$display_cgi?banner=$ADVdisplayad\"";
			if ($ADVtarget eq "_top") {
				print " TARGET=\"$ADVtarget\"";
			}
			elsif ($ADVtarget) {
				print " $ADVtarget";
			}
			print ">";
		}
		print "<IMG SRC=\"$ADVdisplayimage\"";
		if ($ADVheight && $ADVwidth) {
			print " HEIGHT=$ADVheight WIDTH=$ADVwidth";
		}
		print " ALT=\"$ADValt\"";
		unless ($ADVborder) { $ADVborder="0"; }
		print " BORDER=$ADVborder";
		print " ISMAP>";
		if ($ADVurl) {
			print "</A>";
		}
		if ($ADVtext && ($ADVtexttype eq "B")
		  && ($advertzone ne "ShowAll")) {
			print "<BR><SMALL>";
			if ($ADVurl) {
				print "<A HREF=\"$display_cgi?";
				print "banner=$ADVdisplayad\"";
				if ($ADVtarget eq "_top") {
					print " TARGET=\"$ADVtarget\"";
				}
				elsif ($ADVtarget) {
					print " $ADVtarget";
				}
				print ">";
			}
			print "$ADVtext";
			if ($ADVurl) {
				print "</A>";
			}
			print "</SMALL>";
		}
		print "\n";
	}
	unless ($DuplicateView) {
		$ADVshown += 1;
	}
	if ($ADVmax || $ADVratio) {
		seek(ADVDISPLAY, 0, 0);
		print ADVDISPLAY "$ADVmax|$ADVmaxtype\n";
		print ADVDISPLAY "$ADVshown\n";
		print ADVDISPLAY "$ADVvisits\n";
		print ADVDISPLAY "$ADVurl\n";
		print ADVDISPLAY "$ADVimage\n";
		print ADVDISPLAY "$ADVheight\n";
		print ADVDISPLAY "$ADVwidth\n";
		print ADVDISPLAY "$ADValt\n";
		print ADVDISPLAY "$ADVpass\n";
		print ADVDISPLAY "$ADVtext|$ADVtexttype\n";
		print ADVDISPLAY "$ADVstart\n";
		print ADVDISPLAY "$ADVweight\n";
		print ADVDISPLAY "$ADVzone\n";
		print ADVDISPLAY "$ADVborder\n";
		print ADVDISPLAY "$ADVtarget\n";
		print ADVDISPLAY "$ADVraw\n";
		print ADVDISPLAY "$ADVratio\n";
		print ADVDISPLAY "$ADVname\n";
		print ADVDISPLAY "$ADVemail\n";
		print ADVDISPLAY "$ADVdisplayzone\n";
		truncate (ADVDISPLAY, tell(ADVDISPLAY));
	}
	&ADVLockClose (ADVDISPLAY, "$ADVdisplayad.txt");
	$AdvertChosen++;
	unless ($DuplicateView) {
		if ($ADVID) {
			&ADVLockOpen (ADVDISPLAY, "$ADVID.txt");
			unless ($ADVlockerror) {
				@ADVdisplaylines = <ADVDISPLAY>;
				($ADVratio,$ADVdisplaycount) = split (/\|/, $ADVdisplaylines[16]);
				$ADVdisplaycount++;
				unless (@ADVdisplaylines < 1) {
					seek(ADVDISPLAY, 0, 0);
					foreach $key (0..15) {
						print ADVDISPLAY "$ADVdisplaylines[$key]";
					}
					print ADVDISPLAY "$ADVratio|$ADVdisplaycount\n";
					foreach $key (17..19) {
						print ADVDISPLAY "$ADVdisplaylines[$key]";
					}
					truncate (ADVDISPLAY, tell(ADVDISPLAY));
				}
			}
			&ADVLockClose (ADVDISPLAY, "$ADVID.txt");
			$ADVacc = 0;
			&ADVLockOpen (DAILYLOG,"$ADVID.log");
			unless ($ADVlockerror) {
				$ADVaccess = "$ADVmday $ADVmon $ADVyear S";
				$ADVlocation = tell DAILYLOG;
				while ($ADVline = <DAILYLOG>) {
					if (($ADVacc,$ADVlogstring) = ($ADVline =~
					  /^(\d\d\d\d\d\d\d\d\d\d) (\d\d \d\d \d\d\d\d S)$/)) {
						if ($ADVaccess eq $ADVlogstring) {
							last;
						}
					}
					last if ($ADVaccess eq $ADVlogstring);
					$ADVlocation = tell DAILYLOG;
					$ADVacc = 0;
				}
				$ADVacc++;
				seek (DAILYLOG, $ADVlocation, 0);
				$ADVlongacc = sprintf("%010.10d",$ADVacc);
				print DAILYLOG "$ADVlongacc $ADVaccess\n";
			}
			&ADVLockClose (DAILYLOG, "$ADVID.log");
		}
		$ADVacc = 0;
		&ADVLockOpen (DAILYLOG,"$ADVdisplayad.log");
		if ($ADVlockerror) {
			&ADVLockClose (DAILYLOG,"$ADVdisplayad.log");
			return;
		}
		$ADVaccess = "$ADVmday $ADVmon $ADVyear E";
		$ADVlocation = tell DAILYLOG;
		while ($ADVline = <DAILYLOG>) {
			if (($ADVacc,$ADVlogstring) = ($ADVline =~
			  /^(\d\d\d\d\d\d\d\d\d\d) (\d\d \d\d \d\d\d\d E)$/)) {
				if ($ADVaccess eq $ADVlogstring) {
					last;
				}
			}
			last if ($ADVaccess eq $ADVlogstring);
			$ADVlocation = tell DAILYLOG;
			$ADVacc = 0;
		}
		$ADVacc++;
		seek (DAILYLOG, $ADVlocation, 0);
		$ADVlongacc = sprintf("%010.10d",$ADVacc);
		print DAILYLOG "$ADVlongacc $ADVaccess\n";
		&ADVLockClose (DAILYLOG, "$ADVdisplayad.log");
	}
}

sub ADVshowall {
	$ADVshown = 0;
	&ADVdisplayad;
	unless ((@ADVcountlines < 4)
	  || ($ADVWrapCounter > @ADVcountlines-3)) {
		&ADVshowall
	}
}

sub gotoad {
	if ($NonSSI) {
		$displayad = "";
		$logcheck = "$TrimmedIP $displaypage $advertzone";
		&ADVLockOpen (NONSSILOG,"nonssi.log");
		if ($ADVlockerror) {
			if ($SetDest) {
				$displayad = $SetDest;
			}
			else {
				&ADVLockClose (NONSSILOG,"nonssi.log");
				&BadRef;
				return;
			}
		}
		else {
			undef (@nonssi);
			while ($nonssiline = <NONSSILOG>) {
				$nonssitime = int($nonssiline);
				unless (($ADVtime-$nonssitime) > 3600) {
					push (@nonssi,$nonssiline);
				}
				if ($nonssiline =~ /^\d* $logcheck \| (.*)$/) {
					$displayad = $1;
				}
			}
			seek(NONSSILOG, 0, 0);
			foreach $nonssiline (@nonssi) {
				print NONSSILOG "$nonssiline";
			}
			truncate (NONSSILOG, tell(NONSSILOG));
			&ADVLockClose (NONSSILOG, "nonssi.log");
		}
		unless ($displayad) {
			if ($SetDest) {
				$displayad = $SetDest;
			}
			else {
				&BadRef;
				return;
			}
		}
	}
	$DuplicateView = 0;
	if ($ADVLogIP) {
		&ADVLockOpen (DAILYLOG,"$displayad.ips");
		unless ($ADVlockerror) {
			undef (@ADVips);
			while ($ADVline = <DAILYLOG>) {
				$ADVip = int($ADVline);
				unless (($ADVtime-$ADVip) > 43200) {
					push (@ADVips,$ADVline);
				}
				if ((($ADVtime-$ADVip) < $DupViewTime)
				  && ($ADVline =~ /$TrimmedIP\./)
				  && ($ADVline =~ /- C -/)) {
					$DuplicateView = 1;
				}
			}
			seek (DAILYLOG, 0, 0);
			foreach $ADVline (@ADVips) {
				print DAILYLOG "$ADVline";
			}
			unless ($DuplicateView) {
				print DAILYLOG "$ADVtime - $ADVhour:$ADVmin - C - ";
				print DAILYLOG "$ENV{'REMOTE_ADDR'}\n";
			}
			truncate (DAILYLOG, tell(DAILYLOG));
		}
		&ADVLockClose (DAILYLOG, "$displayad.ips");
	}
	&ADVLockOpen (ADVDISPLAY, "$displayad.txt");
	if ($ADVlockerror) {
		&ADVLockClose (ADVDISPLAY,"$displayad.txt");
		&BadRef;
		return;
	}
	@ADVdisplaylines = <ADVDISPLAY>;
	foreach $ADVline (@ADVdisplaylines) {
		chop ($ADVline) if ($ADVline =~ /\n$/);
	}
	unless ($DuplicateView) {
		$ADVdisplaylines[2] += 1;
	}
	unless (@ADVdisplaylines < 1) {
		seek(ADVDISPLAY, 0, 0);
		foreach $ADVline (@ADVdisplaylines) {
			print ADVDISPLAY ("$ADVline\n");
		}
		truncate (ADVDISPLAY, tell(ADVDISPLAY));
	}
	&ADVLockClose (ADVDISPLAY, "$displayad.txt");
	unless ($DuplicateView) {
		$ADVacc = 0;
		&ADVLockOpen (DAILYLOG,"$displayad.log");
		unless ($ADVlockerror) {
			$ADVaccess = "$ADVmday $ADVmon $ADVyear C";
			$ADVlocation = tell DAILYLOG;
			while ($ADVline = <DAILYLOG>) {
				if (($ADVacc,$ADVlogstring) = ($ADVline =~
				  /^(\d\d\d\d\d\d\d\d\d\d) (\d\d \d\d \d\d\d\d C)$/)) {
					if ($ADVaccess eq $ADVlogstring) {
						last;
					}
				}
				last if ($ADVaccess eq $ADVlogstring);
				$ADVlocation = tell DAILYLOG;
				$ADVacc = 0;
			}
			$ADVacc++;
			seek (DAILYLOG, $ADVlocation, 0);
			$ADVlongacc = sprintf("%010.10d",$ADVacc);
			print DAILYLOG "$ADVlongacc $ADVaccess\n";
		}
		&ADVLockClose (DAILYLOG, "$displayad.log");
	}
	print "Status: 302 Found\n";
	if ($rawmodedest) {
		print "Location: $rawmodedest\n\n";
	}
	else {
		print "Location: $ADVdisplaylines[3]\n\n";
	}
}

sub BadRef {
	print "Content-type: text/html\n\n";
	print "<HTML>";
	print "<HEAD><TITLE>WebAdverts Error!</TITLE></HEAD>\n";
	print "<BODY BGCOLOR=\"#ffffff\" TEXT=\"#000000\">\n";
	print "<HR><H1 ALIGN=CENTER>Invalid Destination</H1><HR>\n";
	print "<P>Sorry, but the server encountered an error ";
	print "while trying to redirect you to the destination ";
	print "of the banner on which you clicked! ";
	print "The most likely cause of the problem ";
	print "is that you attempted to click on a banner ";
	print "before the graphic image loaded. ";
	print "Another possibility is that you attempted to click ";
	print "on an old banner which was reloaded ";
	print "from your browser's cache.</P>\n";
	print "<HR></BODY></HTML>\n";
}

sub ADVLockOpen {
	$ADVlockerror = 0;
	local(*FILE,$lockfilename) = @_;
	unless (-e "$adverts_dir/$lockfilename") {
		open (FILE,">$adverts_dir/$lockfilename");
		print FILE "\n";
		close (FILE);
	}
	open (FILE,"+<$adverts_dir/$lockfilename") || &ADVError;
	if ($ADVUseLocking) {
		local($TrysLeft) = 1500;
		while ($TrysLeft--) {
			select(undef,undef,undef,0.01);
			(flock(FILE,6)) || next;
			last;
		}
		unless ($TrysLeft >= 0) {
			&ADVError;
		}
	}
}

sub ADVLockClose {
	local(*FILE,$lockfilename) = @_;
	close (FILE);
}

sub ADVMasterLockOpen {
	$ADVlockerror = 0;
	local($TrysLeft) = 1500;
	if ((-e "$adverts_dir/masterlockfile.lok")
	  && ((stat("$adverts_dir/masterlockfile.lok"))[9]+15<$ADVtime)) {
		unlink ("$adverts_dir/masterlockfile.lok");
	}
	while ($TrysLeft--) {
		if (-e "$adverts_dir/masterlockfile.lok") {
			select(undef,undef,undef,0.01);
		}
		else {
			open (MASTERLOCKFILE,">$adverts_dir/masterlockfile.lok");
			print MASTERLOCKFILE "\n";
			close (MASTERLOCKFILE);
			last;
		}
	}
	unless ($TrysLeft >= 0) {
		&ADVError;
	}
}

sub ADVMasterLockClose {
	unlink ("$adverts_dir/masterlockfile.lok");
}

sub ADVError {
	$ADVlockerror = 1;
}

1;

