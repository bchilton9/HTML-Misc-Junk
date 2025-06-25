#!/usr/bin/perl

############################################
##                                        ##
##     WebAdverts Expire Date Checker     ##
##           by Darryl Burgdorf           ##
##       (e-mail burgdorf@awsd.com)       ##
##                                        ##
############################################

# This program can be run at set times via cron, in order to
# let the site administrator know whenever an account is about
# to expire.  Assign the variables as in your admin script,
# with the additional $DaysToNotify variable set to the number
# of days' notice you want.  (If you set it to 7, for example,
# you'll be notified at each run of any accounts due to expire
# within the next 7 days.)  If no accounts are due to expire,
# no e-mail will be sent.

$adverts_dir = "/home/erenetw/public_html/furnet/beads";

$DaysToNotify = 7;

$email_address = "webadverts\@furres.net";
$mailprog = '/usr/sbin/sendmail';
$WEB_SERVER = "";
$SMTP_SERVER = "";

# use Socket;

# NOTHING BELOW THIS LINE NEEDS TO BE ALTERED!

$time = time;
$body = "The following accounts are expiring:\n\n";

if (!(-e "$adverts_dir/adlist.txt")) { exit; }

open (LIST, "<$adverts_dir/adlist.txt");
@advertisers = <LIST>;
close (LIST);

foreach $advertiser (@advertisers) {
	chop ($advertiser) if ($advertiser =~ /\n$/);
	$expired = 0;
	next if (length($advertiser) < 1);
	open (DISPLAY, "<$adverts_dir/$advertiser.txt");
	@lines = <DISPLAY>;
	close (DISPLAY);
	foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
	($max,$shown,$visits,$url,$image,$height,$width,
	  $alt,$pass,$text,$start,$weight,$zone,
	  $border,$target,$raw,$displayratio,$username,$email,
	  $displayzone) = @lines;
	next if (int($displayratio) > 0);
	next unless $max;
	($max,$maxtype) = split (/\|/, $max);
	unless ($maxtype) { $maxtype = "E"; }
	next if ($maxtype eq "N");
	$runtime = 0;
	if ($start) { $runtime = $time - $start + 1; }
	$average = 0;
	if (($weight > 0) && ($runtime > 86400)) {
		&GetAverage;
	}
	if ($maxtype eq "D") {
		if ($time < $max ) {
			$body .= "$advertiser - EXPIRED!\n";
		}
		else {
			$daysleft = int((($max-$time)/86400)+.5);
			unless ($daysleft > $DaysToNotify) {
				$body .= "$advertiser - $daysleft day";
				if ($daysleft > 1) { $body .= "s"; }
				$body .= " left\n";
			}
		}
	}
	else {
		if ($maxtype eq "C") {
			next if (($average == 0) || ($shown == 0));
			if ($max > $visits) {
				$daysleft = int((($max-$visits)/($average*($visits/$shown)))+.5);
				unless ($daysleft > $DaysToNotify) {
					$body .= "$advertiser - $daysleft day";
					if ($daysleft > 1) { $body .= "s"; }
					$body .= " left\n";
				}
			}
			else {
				$body .= "$advertiser - EXPIRED!\n";
			}
		}
		else {
			next if ($average == 0);
			if ($max > $shown) {
				$daysleft = int((($max-$shown)/$average)+.5);
				unless ($daysleft > $DaysToNotify) {
					$body .= "$advertiser - $daysleft day";
					if ($daysleft > 1) { $body .= "s"; }
					$body .= " left\n";
				}
			}
			else {
				$body .= "$advertiser - EXPIRED!\n";
			}
		}
	}
}

if (length($body) > 40) {
	&SendMail($email_address);
}

exit;

sub GetAverage {
	open (DISPLAY, "<$adverts_dir/$advertiser.log");
	@lines = <DISPLAY>;
	close (DISPLAY);
	@reverselines = reverse (@lines);
	$avexposures = 0;
	$linecount = 0;
	foreach $line (@reverselines) {
		($acc,$type) = ($line =~
		  /^(\d\d\d\d\d\d\d\d\d\d) \d\d \d\d \d\d\d\d (\w)$/);
		next unless ($type eq "E");
		$linecount++;
		next if ($linecount < 2);
		last if ($linecount > 8);
		$avexposures += int($acc);
	}
	unless ($linecount > 8) {
		$avexposures -= int($acc);
	}
	if (($avexposures < 1) || ($linecount < 3)) {
		return;
	}
	$average = int(($avexposures/($linecount-2))+.5);
}

sub SendMail {
	local($To) = $_[0];
	return unless $To;
	unless ($mailprog eq "SMTP") {
		open (MAIL, "|$mailprog -t") || &Error("9450","9451");
		print MAIL "To: $To\n";
		print MAIL "From: $email_address\n",
		  "Subject: Expiring Accounts!\n\n",
		  "$body";
		close (MAIL);
		return;
	}
	unless ($WEB_SERVER) {
		$WEB_SERVER = $ENV{'SERVER_NAME'};
	}
	if (!$WEB_SERVER) {
		&Error("9450","9451");
	}
	unless ($SMTP_SERVER) {
		$SMTP_SERVER = "smtp.$WEB_SERVER";
		$SMTP_SERVER =~ s/^smtp\.[^.]+\.([^.]+\.)/smtp.$1/;
	}
	local($AF_INET) = ($] > 5 ? AF_INET : 2);
	local($SOCK_STREAM) = ($] > 5 ? SOCK_STREAM : 1);
	$, = ', ';
	$" = ', ';
	local($local_address) = (gethostbyname($WEB_SERVER))[4];
	local($local_socket_address) = pack('S n a4 x8', $AF_INET, 0, $local_address);
	local($server_address) = (gethostbyname($SMTP_SERVER))[4];
	local($server_socket_address) = pack('S n a4 x8', $AF_INET, '25', $server_address);
	local($protocol) = (getprotobyname('tcp'))[2];
	if (!socket(SMTP, $AF_INET, $SOCK_STREAM, $protocol)) {
		&Error("9450","9451");
	}
	bind(SMTP, $local_socket_address);
	if (!(connect(SMTP, $server_socket_address))) {
		&Error("9450","9451");
	}
	local($old_selected) = select(SMTP); 
	$| = 1; 
	select($old_selected);
	$* = 1;
	select(undef, undef, undef, .75);
	sysread(SMTP, $_, 1024);
	print SMTP "HELO $WEB_SERVER\r\n";
	sysread(SMTP, $_, 1024);
	while (/(^|(\r?\n))[^0-9]*((\d\d\d).*)$/g) {
		$status = $4;
		$message = $3;
	}
	if ($status != 250) {
		&Error("9450","9451");
	}
	print SMTP "MAIL FROM:<$from>\r\n";
	sysread(SMTP, $_, 1024);
	if (!/[^0-9]*250/) {
		&Error("9450","9451");
	}
	$To = "<$To>";
	print SMTP "RCPT TO:$To\r\n";
	sysread(SMTP, $_, 1024);
	/[^0-9]*(\d\d\d)/;
	unless ($1 eq '250') {
		&Error("9450","9451");
	}
	print SMTP "DATA\r\n";
	sysread(SMTP, $_, 1024);
	if (!/[^0-9]*354/) {
		&Error("9450","9451");
	}
	print SMTP "To: $To\r\n";
	print SMTP "From: $email_address\r\n";
	print SMTP "Subject: Expiring Accounts!\r\n\r\n";
	print SMTP "$body";
	print SMTP "\r\n\r\n.\r\n";
	sysread(SMTP, $_, 1024);
	shutdown(SMTP, 2);
}
