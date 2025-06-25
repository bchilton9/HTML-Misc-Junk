#!/usr/bin/perl

############################################
##                                        ##
##           WebAdverts (Admin)           ##
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

# COPYRIGHT NOTICE:
#
# Copyright 1999 Darryl C. Burgdorf.  All Rights Reserved.
#
# This program is being distributed as shareware.  It may be used and
# modified by anyone, so long as this copyright notice and the header
# above remain intact, but any usage should be registered.  (See the
# program documentation for registration information.)  Selling the
# code for this program without prior written consent is expressly
# forbidden.  Obtain permission before redistributing this program
# over the Internet or in any other medium.  In all cases copyright
# and header must remain intact.
#
# This program is distributed "as is" and without warranty of any
# kind, either express or implied.  (Some states do not allow the
# limitation or exclusion of liability for incidental or consequential
# damages, so this notice may not apply to you.)  In no event shall
# the liability of Darryl C. Burgdorf and/or Affordable Web Space
# Design for any damages, losses and/or causes of action exceed the
# total amount paid by the user for this software.

# DEFINE THESE CONFIGURATION VARIABLES!

# The following variables should be set to define the locations
# and URLs of various files, as explained in the documentation,
# and to "tailer" the functioning of the script.

$adverts_dir = "/home/erenetw/public_html/furnet/be/ads";
$admin_cgi = "http://www.erenetwork.com/furnet/be/ads_admin.pl";
$nonssi_cgi = "http://www.erenetwork.com/furnet/be/ads.pl";

# %nonssi_cgis = (
#   'Zone1','http://foo.com/ads/ads_1.pl',
#   'Zone2','http://foo.com/ads/ads_2.pl',
#   'Zone3','http://foo.com/ads/ads_3.pl',
# );

$UseLocking = 1;
$LogIP = 1;

$AdminDisplaySetup = 0;

$AllowUserEdit = 1;
$RequireAdminApproval = 0;
$DefaultDisplayRatio = 2;
$DefaultWeight = 1;

$DefaultLinkAttribute = "TARGET=_blank";

$bodyspec = "BGCOLOR=\"#ffffff\" TEXT=\"#000000\"";
$header_file = "";
$footer_file = "footer.txt";

$ExchangeName = "Furcadian Banner Exchange";
$ExchangeURL = "http://www.furres.net";
$ExchangeLogo = "http://www.furres.net/be/el.gif";
$ExchangeLogoWidth = 60;
$ExchangeLogoHeight = 60;
$ExchangeBannerWidth = 468;
$ExchangeBannerHeight = 60;

$email_address = "webmaster\@furres.com";
$mailprog = '/usr/sbin/sendmail';
$WEB_SERVER = "";
$SMTP_SERVER = "";

# use Socket;

# NOTHING BELOW THIS LINE NEEDS TO BE ALTERED!

@months = (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec);
$version = "2.02";
$cryptword = 0;
$time = time;

print "Content-type: text/html\n\n";

unless ($UseLocking) { &MasterLockOpen; }

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	if ($INPUT{$name}) { $INPUT{$name} = $INPUT{$name}." ".$value; }
	else { $INPUT{$name} = $value; }
}

unless (-s "$adverts_dir/adcount.txt") {
	open (COUNT, ">$adverts_dir/adcount.txt");
	$lines[0] = 1;
	$lines[1] = "0";
	$lines[2] = time;
	seek(COUNT, 0, 0);
	foreach $line (@lines) { print COUNT "$line\n"; }
	truncate (COUNT, tell(COUNT));
	close (COUNT);
}

if (!(-e "$adverts_dir/adlist.txt")) { &UpdateAdList; }

if ($ENV{'QUERY_STRING'} =~ /reginfo/i) { &reginfo; }
elsif ($ENV{'QUERY_STRING'} =~ /admin/i) { &adminintro; }
elsif ($INPUT{'register'}) { &register; }
elsif ($INPUT{'edit'}) { &edit; }
elsif ($INPUT{'UserEdit'}) { &UserEdit; }
elsif ($INPUT{'groupedit'}) { &groupedit; }
elsif ($INPUT{'del'}) { &del; }
elsif ($INPUT{'delgroup'}) { &delgroup; }
elsif ($INPUT{'newpass'}) { &newpass; }
elsif ($INPUT{'resetcount'}) { &resetcount; }
elsif ($INPUT{'editfinal'}) { &editfinal; }
elsif ($INPUT{'editgroupfinal'}) { &editgroupfinal; }
elsif ($INPUT{'delfinal'}) { &delfinal; }
elsif ($INPUT{'delgroupfinal'}) { &delgroupfinal; }
elsif ($INPUT{'reviewone'} eq "Define View") {
	if ($AdminDisplaySetup) { &defineview; }
	else {
		$INPUT{'whichtype'} = "pending established groups";
		$INPUT{'whichtime'} = "active expired disabled";
		$INPUT{'whichzone'} = "";
		&reviewall;
	}
}
elsif ($INPUT{'reviewone'} eq "Review All Accounts") { &reviewall; }
elsif ($INPUT{'reviewone'}) { &reviewone; }
elsif ($INPUT{'dailystats'}) { &dailystats; }
elsif ($INPUT{'iplog'}) { &iplog; }
elsif ($INPUT{'listemail'}) { &ListEmail; }
else { &userintro; }

sub userintro {
	&Header("Furcadian Banner Exchange","Furcadian Banner Exchange");
	print "<P ALIGN=CENTER>To view the status of your account ",
	  "<BR>enter your name and password:</P>\n",
	  "<CENTER><FORM METHOD=POST ACTION=$admin_cgi>\n",
	  "<P><STRONG>Account or Group Name:</STRONG> ",
	  "<INPUT TYPE=TEXT NAME=reviewone SIZE=15>\n",
	  "<BR><STRONG>Password:</STRONG> ",
	  "<INPUT TYPE=PASSWORD NAME=password SIZE=15>\n",
	  "<P><INPUT TYPE=SUBMIT ",
	  "VALUE=\"Review Account\">\n",
	  "</P></FORM></CENTER>\n";
	if ($AllowUserEdit) {
		print "<HR><P ALIGN=CENTER>To add your site to the exchange,\n",
		  "<BR>enter the name and password you wish to use:</P>\n",
		  "<CENTER><FORM METHOD=POST ACTION=$admin_cgi>\n",
		  "<P><STRONG>Account Name:</STRONG> ",
		  "<INPUT TYPE=TEXT NAME=reviewone SIZE=15>\n",
		  "<BR><STRONG>Password:</STRONG> ",
		  "<INPUT TYPE=PASSWORD NAME=password SIZE=15>\n",
		  "<INPUT TYPE=HIDDEN NAME=newuser VALUE=yes>\n",
		  "<P><INPUT TYPE=SUBMIT ",
		  "VALUE=\"Create New Account\">\n",
		  "</P></FORM></CENTER>\n";
	}
	&Footer;
}

sub adminintro {
	open (PASSWORD, "<$adverts_dir/adpassword.txt");
	$password = <PASSWORD>;
	close (PASSWORD);
	chop ($password) if ($password =~ /\n$/);
	if (!$password) { &InitializePassword; }
	&Header("WebAdverts","WebAdverts Administrative Access");
	print "<P ALIGN=CENTER>To view the status of all accounts and ",
	  "access WebAdvert's main administrative functions,\n",
	  "<BR>input the administrative password:</P>\n",
	  "<CENTER><FORM METHOD=POST ACTION=$admin_cgi>\n",
	  "<P><STRONG>Password:</STRONG> ",
	  "<INPUT TYPE=PASSWORD NAME=password SIZE=15>\n",
	  "<INPUT TYPE=HIDDEN NAME=reviewone ",
	  "VALUE=\"Define View\">\n",
	  "<P><INPUT TYPE=SUBMIT VALUE=\"Review Accounts\"> ",
	  "</P></FORM></CENTER>\n";
	&Footer;
}

sub InitializePassword {
	&Header("WebAdverts","Enter an Administrative Password!");
	print "<P>Before you can do anything else, ",
	  "you'll need to set your administrative password. ",
	  "This will allow you to access the admin functions, ",
	  "create and edit accounts, review statistics, etc. ",
	  "Please enter your desired password below. ",
	  "(Enter it twice.)\n",
	  "<FORM METHOD=POST ACTION=$admin_cgi>\n",
	  "<INPUT TYPE=HIDDEN NAME=newpass VALUE=yes> ",
	  "<P><CENTER><INPUT TYPE=SUBMIT ",
	  "VALUE=\"Set Admin Password:\"> ",
	  "<INPUT TYPE=PASSWORD NAME=passad SIZE=10> ",
	  "<INPUT TYPE=PASSWORD NAME=passad2 SIZE=10>\n",
	  "</CENTER></P></FORM>\n";
	&Footer;
}

sub ConfirmAdminPassword {
	local($which_admin) = @_;
	if ($INPUT{'password'}) {
		$newpassword = crypt($INPUT{'password'}, "aa");
	}
	else {
		&Header("WebAdverts Error!","No Password!");
		print "<P ALIGN=CENTER>You must ";
		print "enter a password!</P>\n";
		&Footer;
	}
	open (PASSWORD, "<$adverts_dir/adpassword.txt");
	$password = <PASSWORD>;
	close (PASSWORD);
	chop ($password) if ($password =~ /\n$/);
	unless ($password && ($newpassword eq $password)) {
		if ($AllowUserEdit && $INPUT{'newuser'} && ($which_admin == 2)) {
			&Header("WebAdverts Error!","Name in Use!");
			print "<P ALIGN=CENTER>";
			print "The account name you entered ";
			print "is already in use!</P>\n";
			&Footer;
		}
		else {
			&Header("WebAdverts Error!","Invalid Password!");
			print "<P ALIGN=CENTER>";
			print "The password you entered is incorrect!</P>\n";
			&Footer;
		}
	}
	$cryptword = 1;
}

sub ConfirmUserPassword {
	unless ($INPUT{'password'}) {
		&Header("WebAdverts Error!","No Password!");
		print "<P ALIGN=CENTER>You must enter a password!</P>\n";
		&Footer;
	}
	$INPUT{'advert'} =~ s/[^\w_-]//g;
	$INPUT{'advert'} =~ tr/A-Z/a-z/;
	if ($INPUT{'admincheck'}) {
		&ConfirmAdminPassword(2);
	}
	open (DISPLAY, "<$adverts_dir/$INPUT{'advert'}.txt");
	@lines = <DISPLAY>;
	close (DISPLAY);
	foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
	$pass = $lines[8];
	unless ($INPUT{'password'} eq $pass) {
		if ($INPUT{'groupstatus'}) {
			open (DISPLAY, "<$adverts_dir/$INPUT{'groupstatus'}.grp");
			@grpck = <DISPLAY>;
			close (DISPLAY);
			foreach $grpln (@grpck) { chop ($grpln) if ($grpln =~ /\n$/); }
		}
		unless ($grpck[0] && ($INPUT{'password'} eq $grpck[0])) {
			&ConfirmAdminPassword(2);
		}
	}
}

sub defineview {
	&ConfirmAdminPassword(1);
	&Header("WebAdverts","WebAdverts Administrative Display");
	print "<P ALIGN=CENTER><BIG><BIG><STRONG>Select Which Accounts ",
	  "You Wish to View:</STRONG></BIG></BIG></P>\n",
	  "<CENTER><FORM METHOD=POST ACTION=$admin_cgi>\n",
	  "<INPUT TYPE=HIDDEN NAME=password ",
	  "VALUE=\"$INPUT{'password'}\">\n";
	if ((-s "$adverts_dir/adnew.txt") || (-s "$adverts_dir/groups.txt")) {
		print "<P><STRONG>Pending Accounts (those awaiting ";
		print "administrative approval), Established Accounts,\n";
		print "<BR>and/or Defined Groups (&quot;sets&quot; ";
		print "of accounts):</STRONG>\n<BR>";
		if (-s "$adverts_dir/adnew.txt") {
			print "<INPUT TYPE=CHECKBOX NAME=whichtype ";
			print "VALUE=pending>Pending Accounts ";
		}
		print "<INPUT TYPE=CHECKBOX NAME=whichtype ";
		print "VALUE=established CHECKED>Established Accounts";
		if (-s "$adverts_dir/groups.txt") {
			print " <INPUT TYPE=CHECKBOX NAME=whichtype ";
			print "VALUE=groups>Defined Groups";
		}
		print "\n";
		print "<BR><SMALL><EM>(If no selection is made, ";
		print "only Established Accounts will be displayed.)</EM></SMALL>\n";
		print "<P><STRONG><EM>(If including Established Accounts, ";
		print "select which ones below.)</EM></STRONG>\n";
	}
	else {
		print "<INPUT TYPE=HIDDEN NAME=whichtype ";
		print "VALUE=established>\n";
	}
	print "<P><STRONG>Active Accounts, Expired Accounts,\n",
	  "<BR>and/or Disabled Accounts (those with weights ",
	  "temporarily set to 0):</STRONG>\n",
	  "<BR><INPUT TYPE=CHECKBOX NAME=whichtime ",
	  "VALUE=active CHECKED>Active Accounts ",
	  "<INPUT TYPE=CHECKBOX NAME=whichtime ",
	  "VALUE=expired>Expired Accounts ",
	  "<INPUT TYPE=CHECKBOX NAME=whichtime ",
	  "VALUE=disabled>Disabled Accounts\n",
	  "<BR><SMALL><EM>(If no selection is made, ",
	  "only Active Accounts will be displayed.)</EM></SMALL>\n";
	if (%nonssi_cgis) {
		print "<P><STRONG>Accounts Displaying in Zone(s):</STRONG>\n<BR>";
		foreach $setzone (sort (keys %nonssi_cgis)) {
			print "<INPUT TYPE=CHECKBOX NAME=whichzone ";
			print "VALUE=\"$setzone\" CHECKED>$setzone ";
		}
		print "\n";
		print "<BR><SMALL><EM>(If no selection is made, ";
		print "accounts from all zones will be displayed.)</EM></SMALL>\n";
	}
	print "<INPUT TYPE=HIDDEN NAME=reviewone ";
	print "VALUE=\"Review All Accounts\">\n";
	print "<P><INPUT TYPE=SUBMIT VALUE=\"Review Accounts\"> ";
	print "</P></FORM></CENTER>\n";
	&Footer;
}

sub reviewall {
	&ConfirmAdminPassword(1);
	&Header("WebAdverts","WebAdverts Administrative Display");
	unless (-e "$adverts_dir/register.txt") {
		print "<P ALIGN=CENTER><STRONG>";
		print "Unregistered copy.</STRONG> ";
		print "<A HREF=\"$admin_cgi?reginfo\">Click here</A> ";
		print "for registration info.</P><HR>\n";
	}
	unless ($INPUT{'whichtype'}) { $INPUT{'whichtype'} = "established"; }
	unless ($INPUT{'whichtime'}) { $INPUT{'whichtime'} = "active"; }
	if ($INPUT{'whichtype'} =~ /established/) {
		print "<P ALIGN=CENTER><BIG><BIG><STRONG>";
		print "The Following Accounts ";
		print "Have Been Established:</STRONG></BIG></BIG>\n";
		if ($AdminDisplaySetup) {
			print "<P ALIGN=CENTER>";
			print "(Accounts Included: ";
			print "$INPUT{'whichtime'})\n";
			if ($INPUT{'whichzone'}) {
				@whichzones = split(/\s+/,$INPUT{'whichzone'});
				print "<BR>(Zones Included: ";
				print "$INPUT{'whichzone'})\n";
			}
		}
		print "<P><CENTER><TABLE CELLPADDING=3>\n",
		  "<TR ALIGN=CENTER VALIGN=BOTTOM>",
		  "<TD><EM>Account</EM><BR><HR></TD>",
		  "<TD><EM>Start</EM><BR><HR></TD>",
		  "<TD><EM>End</EM><BR><HR></TD>",
		  "<TD><EM>Zone(s)</EM><BR><HR></TD>",
		  "<TD><EM>Wt.</EM><BR><HR></TD>",
		  "<TD><EM>Exposures</EM><BR><HR></TD>",
		  "<TD><EM>Exp./Day</EM><BR><HR></TD>",
		  "<TD><EM>Clicks</EM><BR><HR></TD>",
		  "<TD><EM>%</EM><BR><HR></TD>",
		  "<TD><EM>Ratio</EM><BR><HR></TD></TR>\n";
		open (COUNT, "<$adverts_dir/adcount.txt");
		@lines = <COUNT>;
		close (COUNT);
		if (@lines < 2) {
			print "</TABLE></CENTER></P>\n";
			print "<P ALIGN=CENTER>[ File Error: ";
			print "adcount.txt ]";
			print "</P>\n";
			&Footer;
		}
		open (LIST, "<$adverts_dir/adlist.txt");
		while ($list = <LIST>) {
			push (@lines,$list);
		}
		close (LIST);
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		$max = @lines - 1;
		$exposures = $lines[1];
		($exposures,$other) = split (/\|/, $exposures);
		$starttime = $lines[2];
		@advertisements = @lines[3..$max];
		@sortedadverts = sort (@advertisements);
		foreach $advertiser (@sortedadverts) {
			$expired = 0;
			$name = $advertiser;
			next if (length($advertiser) < 1);
			open (DISPLAY, "<$adverts_dir/$advertiser.txt");
			@lines = <DISPLAY>;
			close (DISPLAY);
			foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
			($max,$shown,$visits,$url,$image,$height,$width,
			  $alt,$pass,$text,$start,$weight,$zone,
			  $border,$target,$raw,$displayratio,$username,$email,
			  $displayzone) = @lines;
			unless ($max || $displayratio) {
				print "<TR ALIGN=CENTER>";
				print "<TD COLSPAN=10>";
				print "[ File Error: ";
				print "$advertiser.txt ]</TD></TR>\n";
				next;
			}
			if ($INPUT{'whichzone'} && (length($zone)>2)) {
				$zoneok = 0;
				foreach $whichzones (@whichzones) {
					if ($zone =~ /$whichzones/) {
						$zoneok = 1;
					}
				}
				next unless ($zoneok);
			}
			($max,$maxtype) = split (/\|/, $max);
			unless ($maxtype) { $maxtype = "E"; }
			($text,$texttype) = split (/\|/, $text);
			unless ($texttype) { $texttype = "B"; }
			($displayratio,$displaycount) = split (/\|/, $displayratio);
			if (($maxtype eq "N") && ($displayratio > 0)) {
				$max = int($displaycount/$displayratio);
			}
			if (($maxtype eq "E") && ($displayratio > 0)) {
				$max = $max+int($displaycount/$displayratio);
			}
			if ($max < 1) { $max = "0"; }
			$runtime = 0;
			if ($start) {
				$runtime = $time - $start + 1;
			}
			$average = 0;
			if (($weight > 0) && ($runtime > 86400)) {
				&GetAverage;
			}
			$expirationstatus = "";
			if ($maxtype eq "D") {
				($sec,$min,$hour,$mday,$mon,$year,
				  $wday,$yday,$isdst) = localtime($max);
				$year += 1900;
				$expirationstatus .= "<TD NOWRAP>$mday $months[$mon] $year";
				unless ($max > $time) {
					$expired = 1 ;
					$expirationstatus .=
					  "<BR><EM>EXPIRED!</EM>";
				}
				$expirationstatus .= "</TD>";
			}
			elsif (($maxtype eq "N") && ($max < 1)) {
				if ($displayratio > 1) {
					$expirationstatus .= "<TD NOWRAP>0 exposures<BR><EM>(non-expiring!)</EM></TD>";
				}
				else {
					$expirationstatus .= "<TD NOWRAP><EM>(non-expiring!)</EM></TD>";
				}
			}
			else {
				$expirationstatus .= "<TD NOWRAP>".&commas($max);
				if ($maxtype eq "C") {
					$expirationstatus .= " clicks";
					if (($average == 0) || ($shown == 0) || ($visits == 0)) {
						$expirationstatus .= "<BR><EM>(date unknown)</EM>";
					}
					elsif ($max > $visits) {
						$daystogo = (($max-$visits)/($average*($visits/$shown)));
						$calculatedend = $time+($daystogo*86400);
						($sec,$min,$hour,$mday,$mon,$year,
						  $wday,$yday,$isdst) = localtime($calculatedend);
						$year += 1900;
						$expirationstatus .= "<BR><EM>(~ $mday $months[$mon] $year)</EM>";
					}
					else {
						$expired = 1;
						$expirationstatus .=
						  "<BR><EM>EXPIRED!</EM>";
					}
				}
				else {
					$expirationstatus .= " exposures";
					if ($displayratio > 0) {
						$expirationstatus .= "<BR><EM>(non-expiring!)</EM>";
					}
					elsif ($average == 0) {
						$expirationstatus .= "<BR><EM>(date unknown)</EM>";
					}
					elsif ($max > $shown) {
						$daystogo = (($max-$shown)/$average);
						$calculatedend = $time+($daystogo*86400);
						($sec,$min,$hour,$mday,$mon,$year,
						  $wday,$yday,$isdst) = localtime($calculatedend);
						$year += 1900;
						$expirationstatus .= "<BR><EM>(~ $mday $months[$mon] $year)</EM>";
					}
					else {
						$expired = 1;
						$expirationstatus .=
						  "<BR><EM>EXPIRED!</EM>";
					}
				}
				$expirationstatus .= "</TD>";
			}
			next if (($expired == 1) && ($INPUT{'whichtime'} !~ /expired/));
			next if (($expired == 0) && ($weight == 0)
			  && ($INPUT{'whichtime'} !~ /disabled/));
			next if (($expired == 0) && ($weight > 0)
			  && ($INPUT{'whichtime'} !~ /active/));
			if ($shown == 0) {
				$perc = "N/A";
				$ratio = "N/A";
			}
			elsif ($visits == 0) {
				$perc = "N/A";
				$ratio = "N/A";
			}
			else {
				$perc = ((100*($visits/$shown))+.05001);
				$ratio = (($shown/$visits)+.5001);
			}
			unless ($perc eq "N/A") {
				$perc =~ s/(\d+\.\d).*/$1/;
				$perc = $perc."%";
			}
			unless ($ratio eq "N/A") {
				$ratio =~ s/(\d+)\.\d.*/$1/;
				$ratio = $ratio.":1";
			}
			print "<TR ALIGN=CENTER>\n",
			  "<FORM METHOD=POST ACTION=$admin_cgi><TD>",
			  "<INPUT TYPE=HIDDEN NAME=password ",
			  "VALUE=\"$INPUT{'password'}\">",
			  "<INPUT TYPE=SUBMIT NAME=reviewone ",
			  "VALUE=\"$advertiser\">",
			  "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>",
			  "</TD></FORM>\n";
			$runtime = 0;
			if ($start) {
				($sec,$min,$hour,$mday,$mon,$year,
				  $wday,$yday,$isdst) = localtime($start);
				$year += 1900;
				print "<TD NOWRAP>$mday $months[$mon] $year</TD>";
			}
			else { print "<TD></TD>"; }
			print "$expirationstatus";
			print "<TD NOWRAP>$zone</TD>";
			print "<TD>$weight</TD>";
			print "<TD>",&commas($shown),"</TD>";
			if ($expired || ($weight < 1)) {
				print "<TD>--</TD>";
			}
			elsif ($average > 0) {
				print "<TD>",&commas($average),"</TD>";
			}
			else {
				print "<TD>N/A</TD>";
			}
			print "<TD>",&commas($visits),"</TD>";
			print "<TD>$perc</TD><TD>$ratio</TD></TR>\n";
		}
		print "</TABLE></CENTER></P>\n";
		print "<P ALIGN=CENTER>";
		($sec,$min,$hour,$mday,$mon,$year,
		  $wday,$yday,$isdst) = localtime($time);
		if ($hour < 10) { $hour = "0".$hour; }
		if ($min < 10) { $min = "0".$min; }
		$year += 1900;
		print "(These figures are accurate as of ";
		print "$hour:$min on $mday $months[$mon] $year.";
		($sec,$min,$hour,$mday,$mon,$year,
		  $wday,$yday,$isdst) = localtime($starttime);
		if ($hour < 10) { $hour = "0".$hour; }
		if ($min < 10) { $min = "0".$min; }
		$year += 1900;
		print "<BR>Since $hour:$min on $mday $months[$mon] $year, ";
		print "there have been a total of <STRONG>",&commas($exposures);
		print "</STRONG> advert exposures";
		$time = $time - $starttime + 1;
		if ($time > 86400) {
			$average = int(($exposures/($time/86400))+.5);
			print ",<BR>for an average of <STRONG>",&commas($average);
			print "</STRONG> exposures per day";
		}
		print ".)</P>\n<HR>";
	}
	if ((-s "$adverts_dir/adnew.txt") && ($INPUT{'whichtype'} =~ /pending/)) {
		undef @newlines;
		open (COUNT, "<$adverts_dir/adnew.txt");
		@newlines = <COUNT>;
		close (COUNT);
	}
	if (@newlines > 0) {
		print "<P ALIGN=CENTER><BIG><BIG><STRONG>";
		print "The Following Accounts Await ";
		print "Administrative Approval:";
		print "</STRONG></BIG></BIG><CENTER>\n";
		@sortednewlines = sort (@newlines);
		foreach $newad (@sortednewlines) {
			chop ($newad) if ($newad =~ /\n$/);
			next if (length($newad) < 1);
			open (DISPLAY, "<$adverts_dir/$newad.txt");
			@lines = <DISPLAY>;
			close (DISPLAY);
			foreach $line (@lines) {
				chop ($line) if ($line =~ /\n$/);
			}
			($max,$shown,$visits,$url,$image,$height,$width,
			  $alt,$pass,$text,$start,$weight,$zone,
			  $border,$target,$raw,$displayratio,$username,$email,
			  $displayzone) = @lines;
			print "<P><FORM METHOD=POST ACTION=$admin_cgi>",
			  "<INPUT TYPE=HIDDEN NAME=password ",
			  "VALUE=\"$INPUT{'password'}\">",
			  "<INPUT TYPE=SUBMIT NAME=reviewone ",
			  "VALUE=\"$newad\">",
			  "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>",
			  "</FORM></P>\n";
		}
		print "</CENTER>\n<HR>";
	}
	if ((-s "$adverts_dir/groups.txt") && ($INPUT{'whichtype'} =~ /groups/)) {
		undef @grouplines;
		open (COUNT, "<$adverts_dir/groups.txt");
		@grouplines = <COUNT>;
		close (COUNT);
	}
	if (@grouplines > 0) {
		print "<P ALIGN=CENTER><BIG><BIG><STRONG>";
		print "The Following Groups Have Been Defined:";
		print "</STRONG></BIG></BIG>\n";
		print "<P><CENTER><TABLE CELLPADDING=3>\n";
		@sortedgroups = sort (@grouplines);
		foreach $group (@sortedgroups) {
			chop ($group) if ($group =~ /\n$/);
			next if (length($group) < 1);
			open (DISPLAY, "<$adverts_dir/$group.grp");
			@members = <DISPLAY>;
			close (DISPLAY);
			$grppassword = $members[0];
			print "<TR ALIGN=CENTER>",
			  "<FORM METHOD=POST ",
			  "ACTION=$admin_cgi><TD>",
			  "<INPUT TYPE=HIDDEN NAME=password ",
			  "VALUE=$INPUT{'password'}>\n",
			  "<INPUT TYPE=HIDDEN NAME=editgroup ",
			  "VALUE=\"$group\">\n",
			  "<INPUT TYPE=SUBMIT NAME=groupedit ",
			  "VALUE=\"$group\">",
			  "</TD></FORM>\n",
			  "<TD>";
			foreach $member (@members) {
				unless ($member eq $grppassword) {
					chop ($member)
					  if ($member =~ /\n$/);
					print " $member";
				}
			}
			print "</TD></TR>\n";
		}
		print "</TABLE></CENTER></P>\n<HR>";
	}
	print "<FORM METHOD=POST ACTION=$admin_cgi>\n",
	  "<CENTER><P><BIG><BIG><STRONG>The Following Options ",
	  "Are Available:</STRONG></BIG></BIG>\n",
	  "<INPUT TYPE=HIDDEN NAME=password ",
	  "VALUE=$INPUT{'password'}>\n",
	  "<P><STRONG>Add/Edit/Delete Account:</STRONG> ",
	  "<INPUT TYPE=TEXT NAME=editad SIZE=25 ",
	  "VALUE=\"(enter account name)\"> ",
	  "<INPUT TYPE=SUBMIT NAME=edit ",
	  "VALUE=\"Edit Account\">\n",
	  "<P><STRONG>Add/Edit/Delete Group:</STRONG> ",
	  "<INPUT TYPE=TEXT NAME=editgroup SIZE=25 ",
	  "VALUE=\"(enter group name)\"> ",
	  "<INPUT TYPE=SUBMIT NAME=groupedit ",
	  "VALUE=\"Edit Group\">\n",
	  "<P><STRONG>Change Admin Password:</STRONG> ",
	  "<INPUT TYPE=PASSWORD NAME=passad SIZE=10> ",
	  "<INPUT TYPE=PASSWORD NAME=passad2 SIZE=10> ",
	  "<INPUT TYPE=SUBMIT NAME=newpass ",
	  "VALUE=\"Change Password\">\n",
	  "<P><INPUT TYPE=SUBMIT NAME=resetcount ",
	  "VALUE=\"Reset Overall Total Exposures Count\">\n",
	  "<P><INPUT TYPE=SUBMIT NAME=listemail ",
	  "VALUE=\"List All Account Holder E-Mails\">\n",
	  "</P></CENTER></FORM>\n";
	&LinkBack;
	&Footer;
}

sub ListEmail {
	&ConfirmAdminPassword(1);
	open (LIST, "<$adverts_dir/adlist.txt");
	@advertlist = <LIST>;
	close (LIST);
	foreach $advertiser (@advertlist) {
		chop ($advertiser) if ($advertiser =~ /\n$/);
		open (DISPLAY, "<$adverts_dir/$advertiser.txt");
		@lines = <DISPLAY>;
		close (DISPLAY);
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		unless ($lines[18]) { next; }
		push (@emails,"&quot;$lines[17]&quot; &lt;<A HREF=\"mailto:$lines[18]\">$lines[18]</A>&gt;");

	}
	@sortedemails = sort (@emails);
	&Header("WebAdverts","WebAdverts Account Holder E-Mails");
	print "<P ALIGN=CENTER><BIG><BIG><STRONG>";
	print "Account Holder E-Mail Addresses:";
	print "</STRONG></BIG></BIG>\n";
	print "<P>";
	foreach $email (@sortedemails) {
		if ($email eq $lastemail) { next; }
		if ($lastemail) { print ", "; }
		print "$email";
		$lastemail = $email;
	}
	print "</P>\n";
	&LinkBack;
	&Footer;
}

sub reviewgroup {
	$groupstatus = "$INPUT{'reviewone'}";
	unless (-s "$adverts_dir/$INPUT{'reviewone'}.grp") {
		if ($AllowUserEdit && $INPUT{'newuser'}) {
			&UserEdit;
		}
		&Header("WebAdverts Error!","Invalid Name!");
		print "<P ALIGN=CENTER>There is no ";
		print "account or group on the list with the name ";
		print "<STRONG>&quot;$INPUT{'reviewone'}&quot;</STRONG>!\n";
		print "<P ALIGN=CENTER>(Note that all names ";
		print "<EM>are</EM> case sensitive!)</P>\n";
		&Footer;
	}
	open (DISPLAY, "<$adverts_dir/$INPUT{'reviewone'}.grp");
	@adverts = <DISPLAY>;
	close (DISPLAY);
	foreach $line (@adverts) { chop ($line) if ($line =~ /\n$/); }
	unless ($cryptword) {
		unless ($INPUT{'password'} eq $adverts[0]) {
			&ConfirmAdminPassword(2);
		}
	}
	&Header("WebAdverts","WebAdverts Administrative Display");
	print "<P ALIGN=CENTER><BIG><STRONG>(Accounts in the ";
	print "<EM>$INPUT{'reviewone'}</EM> Group)</STRONG></BIG></P>\n";
	foreach $advert (@adverts) {
		$name = $advert;
		next unless (-s "$adverts_dir/$advert.txt");
		open (DISPLAY, "<$adverts_dir/$advert.txt");
		@lines = <DISPLAY>;
		close (DISPLAY);
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		($max,$shown,$visits,$url,$image,$height,$width,
		  $alt,$pass,$text,$start,$weight,$zone,
		  $border,$target,$raw,$displayratio,$username,$email,
		  $displayzone) = @lines;
		($max,$maxtype) = split (/\|/, $max);
		unless ($maxtype) { $maxtype = "E"; }
		($text,$texttype) = split (/\|/, $text);
		unless ($texttype) { $texttype = "B"; }
		($displayratio,$displaycount) = split (/\|/, $displayratio);
		if (($maxtype eq "E") && ($displayratio > 0)) {
			$max = $max+int($displaycount/$displayratio);
		}
		$TotalShown += $shown;
		$TotalVisits += $visits;
		print "<HR>\n";
		&reviewadvert;
	}
	print "<HR><P ALIGN=CENTER><BIG><BIG><STRONG>Master Overview:",
	  "</STRONG></BIG></BIG>\n",
	  "<P><CENTER><TABLE CELLPADDING=3>\n",
	  "<TR ALIGN=CENTER VALIGN=BOTTOM>",
	  "<TD><EM>Exposures</EM><BR><HR></TD>",
	  "<TD><EM>Clicks</EM><BR><HR></TD>",
	  "<TD><EM>%</EM><BR><HR></TD>",
	  "<TD><EM>Ratio</EM><BR><HR></TD></TR>\n";
	if ($TotalShown == 0) {
		$perc = "N/A";
		$ratio = "N/A";
	}
	elsif ($TotalVisits == 0) {
		$perc = "N/A";
		$ratio = "N/A";
	}
	else {
		$perc = ((100*($TotalVisits/$TotalShown))+.05001);
		$ratio = (($TotalShown/$TotalVisits)+.5001);
	}
	unless ($perc eq "N/A") {
		$perc =~ s/(\d+\.\d).*/$1/;
		$perc = $perc."%";
	}
	unless ($ratio eq "N/A") {
		$ratio =~ s/(\d+)\.\d.*/$1/;
		$ratio = $ratio.":1";
	}
	print "<TR ALIGN=CENTER>";
	print "<TD>",&commas($TotalShown),"</TD>";
	print "<TD>",&commas($TotalVisits),"</TD>";
	print "<TD>$perc</TD><TD>$ratio</TD></TR>\n";
	print "</TABLE></CENTER></P>\n";
	&Footer;
}

sub reviewone {
	unless ($INPUT{'password'}) {
		&Header("WebAdverts Error!","No Password!");
		print "<P ALIGN=CENTER>You must enter a password!</P>\n";
		&Footer;
	}
	$INPUT{'reviewone'} =~ s/[^\w_-]//g;
	$INPUT{'reviewone'} =~ tr/A-Z/a-z/;
	if ($INPUT{'admincheck'}) {
		&ConfirmAdminPassword(2);
	}
	unless (-s "$adverts_dir/$INPUT{'reviewone'}.txt") {
		&reviewgroup;
	}
	$name = $INPUT{'reviewone'};
	open (DISPLAY, "<$adverts_dir/$INPUT{'reviewone'}.txt");
	@lines = <DISPLAY>;
	close (DISPLAY);
	foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
	($max,$shown,$visits,$url,$image,$height,$width,
	  $alt,$pass,$text,$start,$weight,$zone,
	  $border,$target,$raw,$displayratio,$username,$email,
	  $displayzone) = @lines;
	($max,$maxtype) = split (/\|/, $max);
	unless ($maxtype) { $maxtype = "E"; }
	($text,$texttype) = split (/\|/, $text);
	unless ($texttype) { $texttype = "B"; }
	($displayratio,$displaycount) = split (/\|/, $displayratio);
	if (($maxtype eq "N") && ($displayratio > 0)) {
		$max = int($displaycount/$displayratio);
	}
	if (($maxtype eq "E") && ($displayratio > 0)) {
		$max = $max+int($displaycount/$displayratio);
	}
	if ($max < 1) { $max = "0"; }
	unless ($cryptword) {
		unless ($INPUT{'password'} eq $pass) {
			&ConfirmAdminPassword(2);
		}
	}
	&Header("WebAdverts","WebAdverts Administrative Display");
	&reviewadvert;
	if ($cryptword) {
		&LinkBack;
	}
	&Footer;
}

sub reviewadvert {
	$expired = 0;
	print "<P ALIGN=CENTER><BIG><BIG><STRONG>Current Status of the ";
	print "<EM>$name</EM> Account:</STRONG></BIG></BIG>\n";
	if ($image || $raw) {
		print "<P><CENTER><TABLE CELLPADDING=3>\n";
		print "<TR ALIGN=CENTER VALIGN=BOTTOM>";
		print "<TD><EM>Start</EM><BR><HR></TD>";
		print "<TD><EM>End</EM><BR><HR></TD>";
		if ($displaycount) {
			print "<TD NOWRAP><EM>Banners Shown<BR>";
			print "on Your Site</EM><BR><HR></TD>";
		}
		print "<TD NOWRAP><EM>Your Banner's<BR>";
		print "Exposures</EM><BR><HR></TD>";
		print "<TD><EM>Exp./Day</EM><BR><HR></TD>";
		print "<TD NOWRAP><EM>Clicks<BR>";
		print "on Your Banner</EM><BR><HR></TD>";
		print "<TD><EM>%</EM><BR><HR></TD>";
		print "<TD><EM>Ratio</EM><BR><HR></TD></TR>\n";
		if ($shown == 0) {
			$perc = "N/A";
			$ratio = "N/A";
		}
		elsif ($visits == 0) {
			$perc = "N/A";
			$ratio = "N/A";
		}
		else {
			$perc = ((100*($visits/$shown))+.05001);
			$ratio = (($shown/$visits)+.5001);
		}
		unless ($perc eq "N/A") {
			$perc =~ s/(\d+\.\d).*/$1/;
			$perc = $perc."%";
		}
		unless ($ratio eq "N/A") {
			$ratio =~ s/(\d+)\.\d.*/$1/;
			$ratio = $ratio.":1";
		}
		print "<TR ALIGN=CENTER>";
		$runtime = 0;
		if ($start) {
			($sec,$min,$hour,$mday,$mon,$year,
			  $wday,$yday,$isdst) = localtime($start);
			$year += 1900;
			print "<TD NOWRAP>$mday $months[$mon] $year</TD>";
			$runtime = $time - $start + 1;
		}
		else { print "<TD></TD>"; }
		$average = 0;
		if (($weight > 0) && ($runtime > 86400)) {
			&GetAverage;
		}
		if ($maxtype eq "D") {
			($sec,$min,$hour,$mday,$mon,$year,
			  $wday,$yday,$isdst) = localtime($max);
			$year += 1900;
			print "<TD NOWRAP>$mday $months[$mon] $year";
			unless ($max > $time) {
				$expired = 1;
				print "<BR><EM>EXPIRED!</EM>";
			}
			print "</TD>";
		}
		elsif (($maxtype eq "N") && ($max < 1)) {
			if ($displayratio > 1) {
				print "<TD NOWRAP>0 exposures<BR><EM>(non-expiring!)</EM></TD>";
			}
			else {
				print "<TD NOWRAP><EM>(non-expiring!)</EM></TD>";
			}
		}
		else {
			print "<TD NOWRAP>",&commas($max);
			if ($maxtype eq "C") {
				print " clicks";
				if (($average == 0) || ($shown == 0) || ($visits == 0)) {
					print "<BR><EM>(date unknown)</EM>";
				}
				elsif ($max > $visits) {
					$daystogo = (($max-$visits)/($average*($visits/$shown)));
					$calculatedend = $time+($daystogo*86400);
					($sec,$min,$hour,$mday,$mon,$year,
					  $wday,$yday,$isdst) = localtime($calculatedend);
					$year += 1900;
					print "<BR><EM>(~ $mday $months[$mon] $year)</EM>";
				}
				else {
					$expired = 1;
					print "<BR><EM>EXPIRED!</EM>";
				}
			}
			else {
				print " exposures";
				if ($displayratio > 0) {
					print "<BR><EM>(non-expiring!)</EM>";
				}
				elsif ($average == 0) {
					print "<BR><EM>(date unknown)</EM>";
				}
				elsif ($max > $shown) {
					$daystogo = (($max-$shown)/$average);
					$calculatedend = $time+($daystogo*86400);
					($sec,$min,$hour,$mday,$mon,$year,
					  $wday,$yday,$isdst) = localtime($calculatedend);
					$year += 1900;
					print "<BR><EM>(~ $mday $months[$mon] $year)</EM>";
				}
				else {
					$expired = 1;
					print "<BR><EM>EXPIRED!</EM>";
				}
			}
			print "</TD>";
		}
		if ($displaycount) {
			print "<TD>",&commas($displaycount),"</TD>";
		}
		print "<TD>",&commas($shown),"</TD>";
		if ($expired || ($weight < 1)) {
			print "<TD>--</TD>";
		}
		elsif ($average > 0) {
			print "<TD>",&commas($average),"</TD>";
		}
		else {
			print "<TD>N/A</TD>";
		}
		print "<TD>",&commas($visits),"</TD>";
		print "<TD>$perc</TD><TD>$ratio</TD></TR>\n";
		print "</TABLE></CENTER></P>\n";
	}
	else {
		print "<P>Your account currently has no assigned banner.\n";
	}
	if ($displayratio || $displaycount || !($image || $raw)) {
		if ($displaycount<1) { $displaycount = "0"; }
		print "<P>To date, you have displayed <STRONG>";
		print &commas($displaycount),"</STRONG> banners ";
		print "on your site";
		if ($displayratio > 0) {
			$earnings = int($displaycount/$displayratio);
			print ", earning <STRONG>";
			print &commas($earnings),"</STRONG> exposures ";
			print "for your own advert on other sites. ";
			print "(You earn an exposure for each ";
			print "<STRONG>$displayratio</STRONG> display";
			if ($displayratio > 1) { print "s"; }
			print ".)\n";
		}
		else {
			print ".\n";
		}
		print "<P>The HTML code below should be placed on your site ";
		print "where you want the banners to appear.\n";
		print "<P><BLOCKQUOTE><SMALL><STRONG>";
		$HTMLCode = "&lt;P ALIGN=CENTER&gt;";
		if ($ExchangeLogo) {
			if ($ExchangeURL) {
				$HTMLCode .= "&lt;A HREF=&quot;$ExchangeURL&quot;&gt;";
			}
			$HTMLCode .= "&lt;IMG SRC=&quot;$ExchangeLogo&quot;";
			if ($ExchangeLogoHeight && $ExchangeLogoWidth) {
				$HTMLCode .= " WIDTH=$ExchangeLogoWidth";
				$HTMLCode .= " HEIGHT=$ExchangeLogoHeight";
			}
			if ($ExchangeName) {
				$HTMLCode .= " ALT=&quot;$ExchangeName&quot;";
			}
			$HTMLCode .= " ISMAP&gt;";
			if ($ExchangeURL) {
				$HTMLCode .= "&lt;/A&gt;";
			}
		}
		if (%nonssi_cgis) {
			foreach $setzone (keys %nonssi_cgis) {
				if ($displayzone eq $setzone) {
					$nonssi_cgi = $nonssi_cgis{$setzone};
				}
			}
		}
		$HTMLCode .= "&lt;A HREF=&quot;$nonssi_cgi?";
		$HTMLCode .= "member=$name;banner=NonSSI;page=01&quot;&gt;";
		$HTMLCode .= "&lt;IMG SRC=&quot;$nonssi_cgi?";
		$HTMLCode .= "member=$name;page=01&quot;";
		if ($ExchangeBannerHeight && $ExchangeBannerWidth) {
			$HTMLCode .= " WIDTH=$ExchangeBannerWidth";
			$HTMLCode .= " HEIGHT=$ExchangeBannerHeight";
		}
		if ($ExchangeName) {
			$HTMLCode .= " ALT=&quot;$ExchangeName&quot;";
		}
		$HTMLCode .= " ISMAP&gt;&lt;/A&gt;";
		if ($ExchangeName) {
			$HTMLCode .= "&lt;BR&gt;&lt;SMALL&gt;";
			if ($ExchangeURL) {
				$HTMLCode .= "&lt;A HREF=&quot;$ExchangeURL&quot;&gt;";
			}
			$HTMLCode .= "$ExchangeName";
			if ($ExchangeURL) {
				$HTMLCode .= "&lt;/A&gt;";
			}
			$HTMLCode .= "&lt;/SMALL&gt;";
		}
		$HTMLCode .= "&lt;/P&gt;";
		print "$HTMLCode</STRONG></SMALL></BLOCKQUOTE>\n";
		print "<P>If you want banners to appear on more than one page, ",
		  "simply use a unique &quot;page=&quot; number for each banner ",
		  "call. This will ensure that new banners are loaded (and that new ",
		  "displays are credited to you) on each of your pages.  For ",
		  "example, a second banner call would look like the following. ",
		  "(Note that there are two &quot;page=&quot; designations in the ",
		  "call, and that they must match!)\n";
		$HTMLCode =~ s/page=01/page=02/g;
		print "<P><BLOCKQUOTE><SMALL>$HTMLCode</SMALL></BLOCKQUOTE>\n";
	}
	print "<P><CENTER><TABLE><TR ALIGN=CENTER>\n";
	print "<FORM METHOD=POST ACTION=$admin_cgi><TD>\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	if ($groupstatus) {
		print "<INPUT TYPE=HIDDEN NAME=groupstatus ";
		print "VALUE=\"$groupstatus\">\n";
	}
	print "<INPUT TYPE=HIDDEN NAME=advert VALUE=$name>\n";
	if ($cryptword) {
		print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
	}
	print "<INPUT TYPE=SUBMIT NAME=dailystats ";
	print "VALUE=\"View Daily Stats\">";
	print "</TD></FORM>\n";
	if ($LogIP) {
		print "<FORM METHOD=POST ";
		print "ACTION=$admin_cgi><TD>\n";
		print "<INPUT TYPE=HIDDEN NAME=password ";
		print "VALUE=$INPUT{'password'}>\n";
		if ($groupstatus) {
			print "<INPUT TYPE=HIDDEN NAME=groupstatus ";
			print "VALUE=\"$groupstatus\">\n";
		}
		print "<INPUT TYPE=HIDDEN NAME=advert VALUE=$name>\n";
		if ($cryptword) {
			print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
		}
		print "<INPUT TYPE=SUBMIT NAME=iplog ";
		print "VALUE=\"View IP Address Log\">";
		print "</TD></FORM>\n";
	}
	if (($AllowUserEdit || $cryptword) && !($groupstatus)) {
		print "<FORM METHOD=POST ";
		print "ACTION=$admin_cgi><TD>\n";
		print "<INPUT TYPE=HIDDEN NAME=password ";
		print "VALUE=$INPUT{'password'}>\n";
		print "<INPUT TYPE=HIDDEN NAME=reviewone ";
		print "VALUE=$name>\n";
		if ($cryptword) {
			print "<INPUT TYPE=SUBMIT NAME=edit ";
		}
		else {
			print "<INPUT TYPE=SUBMIT NAME=UserEdit ";
		}
		print "VALUE=\"Edit Account\">";
		print "</TD></FORM>\n";
	}
	print "</TR></TABLE></CENTER></P>\n";
	if ($email && $INPUT{'welcomeletter'}) {
		open (WELCOME, "<$adverts_dir/welcome.txt");
		$body = "";
		while ($line = <WELCOME>) {
			$body .= $line;
		}
		close (WELCOME);
		$HTMLCode =~ s/page=02/page=01/g;
		$HTMLCode =~ s/&lt;/</g;
		$HTMLCode =~ s/&gt;/>/g;
		$HTMLCode =~ s/&quot;/"/g;
		$body =~ s/<--UserID-->/$name/g;
		$body =~ s/<--Password-->/$pass/g;
		$body =~ s/<--HTMLCode-->/$HTMLCode/g;
		&SendMail($email);
	}
	&ShowAdvert;
}

sub GetAverage {
	open (DISPLAY, "<$adverts_dir/$name.log");
	@lines = <DISPLAY>;
	close (DISPLAY);
	@reverselines = reverse (@lines);
	$avexposures = 0;
	$linecount = 0;
	foreach $line (@reverselines) {
		next if (length($line)<10);
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

sub dailystats {
	&ConfirmUserPassword;
	open (DISPLAY, "<$adverts_dir/$INPUT{'advert'}.log") || &Error_NoStats;
	@lines = <DISPLAY>;
	close (DISPLAY);
	foreach $line (@lines) {
		next if (length($line) < 10);
		($acc,$logstring) = ($line =~
		  /^(\d\d\d\d\d\d\d\d\d\d) (\d\d \d\d \d\d\d\d \w)$/);
		$accesses{$logstring} = int($acc);
		($mday,$mon,$year,$type) = ($logstring =~
			  /^(\d+) (\d+) (\d+) (\w)/);
		if ($type eq "E") { $beingshown = 1; }
		if ($type eq "S") { $bannex = 1; }
		unless ($startday) {
			&date_to_count(int($mon),int($mday),($year-1900));
			$startday = $perp_days;
		}
	}
	&date_to_count(int($mon),int($mday),($year-1900));
	$endday = $perp_days;
	if ((($endday-$startday) > 30) && !($INPUT{'FullDailyList'})) {
		$startday = $endday-30;
		$ShortenedList = 1;
	}
	&Header("WebAdverts","WebAdverts Administrative Display");
	print "<P ALIGN=CENTER><BIG><BIG><STRONG>Daily Stats for the ";
	print "<EM>$INPUT{'advert'}</EM> Account";
	if ($ShortenedList) {
		print "<BR>(Last Month Only)";
	}
	elsif ($INPUT{'FullDailyList'}) {
		print "<BR>(Full List)";
	}
	print ":</STRONG></BIG></BIG>\n";
	print "<P><CENTER><TABLE CELLPADDING=3>\n";
	print "<TR ALIGN=CENTER VALIGN=BOTTOM>";
	print "<TD><EM>Date</EM><BR><HR></TD>";
	if ($bannex) {
		print "<TD NOWRAP><EM>Banners Shown<BR>";
		print "on Your Site</EM><BR><HR></TD>";
	}
	if ($beingshown) {
		print "<TD NOWRAP><EM>Your Banner's<BR>";
		print "Exposures</EM><BR><HR></TD>";
		print "<TD NOWRAP><EM>Clicks<BR>";
		print "on Your Banner</EM><BR><HR></TD>";
		print "<TD><EM>%</EM><BR><HR></TD>";
		print "<TD><EM>Ratio</EM><BR><HR></TD></TR>\n";
	}
	foreach $daycount ($startday..$endday) {
		print "<TR ALIGN=CENTER>";
		if (($daycount > $startday)
		  && ($daycount-(int($daycount/7)*7)==3)) {
			print "<TD COLSPAN=5><HR WIDTH=50%>";
			print "</TD></TR>\n";
			print "<TR ALIGN=CENTER>";
		}
		&count_to_date($daycount);
		if ($perp_mon < 10) { $perp_mon = "0$perp_mon"; }
		if ($perp_day < 10) { $perp_day = "0$perp_day"; }
		$perp_year = $perp_year + 1900;
		print "<TD NOWRAP>$perp_day $months[$perp_mon-1] $perp_year</TD>";
		$banners = "$perp_day $perp_mon $perp_year S";
		$exposures = "$perp_day $perp_mon $perp_year E";
		$clicks = "$perp_day $perp_mon $perp_year C";
		$banners = $accesses{$banners};
		$exposures = $accesses{$exposures};
		$clicks = $accesses{$clicks};
		if ($banners < 1) { $banners = "0"; }
		if ($exposures < 1) { $exposures = "0"; }
		if ($clicks < 1) { $clicks = "0"; }
		if ($bannex) {
			print "<TD>",&commas($banners),"</TD>";
		}
		if ($beingshown) {
			print "<TD>",&commas($exposures),"</TD>";
			print "<TD>",&commas($clicks),"</TD>";
			if ($exposures == 0) {
				$perc = "-";
				$ratio = "-";
			}
			elsif ($clicks == 0) {
				$perc = "-";
				$ratio = "-";
			}
			else {
				$perc = ((100*($clicks/$exposures))+.05001);
				$ratio = (($exposures/$clicks)+.5001);
			}
			unless ($perc eq "-") {
				$perc =~ s/(\d+\.\d).*/$1/;
				$perc = $perc."%";
			}
			unless ($ratio eq "-") {
				$ratio =~ s/(\d+)\.\d.*/$1/;
				$ratio = $ratio.":1";
			}
			print "<TD>$perc</TD><TD>$ratio</TD></TR>\n";
		}
	}
	print "</TABLE></CENTER></P>\n";
	if ($ShortenedList) {
		print "<P><CENTER><FORM METHOD=POST ";
		print "ACTION=$admin_cgi>\n";
		print "<INPUT TYPE=HIDDEN NAME=password ";
		print "VALUE=$INPUT{'password'}>\n";
		if ($INPUT{'groupstatus'}) {
			print "<INPUT TYPE=HIDDEN NAME=groupstatus ";
			print "VALUE=\"$INPUT{'groupstatus'}\">\n";
		}
		print "<INPUT TYPE=HIDDEN NAME=advert ";
		print "VALUE=$INPUT{'advert'}>\n";
		print "<INPUT TYPE=HIDDEN NAME=FullDailyList ";
		print "VALUE=Yes>\n";
		if ($cryptword) {
			print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
		}
		print "<INPUT TYPE=SUBMIT NAME=dailystats ";
		print "VALUE=\"View Full Daily Stats List\">";
		print "</FORM></CENTER></P>\n";
	}
	elsif ($INPUT{'FullDailyList'}) {
		print "<P><CENTER><FORM METHOD=POST ";
		print "ACTION=$admin_cgi>\n";
		print "<INPUT TYPE=HIDDEN NAME=password ";
		print "VALUE=$INPUT{'password'}>\n";
		if ($INPUT{'groupstatus'}) {
			print "<INPUT TYPE=HIDDEN NAME=groupstatus ";
			print "VALUE=\"$INPUT{'groupstatus'}\">\n";
		}
		print "<INPUT TYPE=HIDDEN NAME=advert ";
		print "VALUE=$INPUT{'advert'}>\n";
		if ($cryptword) {
			print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
		}
		print "<INPUT TYPE=SUBMIT NAME=dailystats ";
		print "VALUE=\"View Daily Stats for Last Month Only\">";
		print "</FORM></CENTER></P>\n";
	}
	print "<P><CENTER><TABLE><TR ALIGN=CENTER>\n";
	print "<FORM METHOD=POST ACTION=$admin_cgi><TD>\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	if ($cryptword) {
		print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
	}
	print "<INPUT TYPE=HIDDEN NAME=reviewone VALUE=";
	if ($INPUT{'groupstatus'}) {
		print "\"$INPUT{'groupstatus'}\"";
	}
	else {
		print "$INPUT{'advert'}";
	}
	print ">\n";
	print "<INPUT TYPE=SUBMIT ";
	print "VALUE=\"View Overall Stats\"> ";
	print "</TD></FORM>\n";
	if ($LogIP) {
		print "<FORM METHOD=POST ";
		print "ACTION=$admin_cgi><TD>\n";
		print "<INPUT TYPE=HIDDEN NAME=password ";
		print "VALUE=$INPUT{'password'}>\n";
		if ($INPUT{'groupstatus'}) {
			print "<INPUT TYPE=HIDDEN NAME=groupstatus ";
			print "VALUE=\"$INPUT{'groupstatus'}\">\n";
		}
		print "<INPUT TYPE=HIDDEN NAME=advert ";
		print "VALUE=$INPUT{'advert'}>\n";
		if ($cryptword) {
			print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
		}
		print "<INPUT TYPE=SUBMIT NAME=iplog ";
		print "VALUE=\"View IP Address Log\">";
		print "</TD></FORM>\n";
	}
	print "</TR></TABLE></CENTER></P>\n";
	&Footer;
}

sub iplog {
	&ConfirmUserPassword;
	open (DISPLAY, "<$adverts_dir/$INPUT{'advert'}.ips") || &Error_NoIPLog;
	@lines = <DISPLAY>;
	close (DISPLAY);
	&Header("WebAdverts","WebAdverts Administrative Display");
	print "<P ALIGN=CENTER><BIG><BIG><STRONG>IP Address Log for the ",
	  "<EM>$INPUT{'advert'}</EM> Account:</STRONG></BIG></BIG>\n",
	  "<P>The following log file lists ",
	  "the IP addresses of those individuals who ",
	  "have seen or clicked on this advert's banner ",
	  "in the past 12 hours. Each ",
	  "line displays the time of the exposure (E) ",
	  "or click-thru (C), and the IP ",
	  "address of the responsible party.\n",
	  "<P><PRE>";
	foreach $line (@lines) {
		$line =~ s/^(\d*) - //g;
		print $line;
	}
	print "</PRE></P>\n";
	print "<P><CENTER><TABLE><TR ALIGN=CENTER>\n";
	print "<FORM METHOD=POST ACTION=$admin_cgi><TD>\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	if ($cryptword) {
		print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
	}
	print "<INPUT TYPE=HIDDEN NAME=reviewone VALUE=";
	if ($INPUT{'groupstatus'}) {
		print "\"$INPUT{'groupstatus'}\"";
	}
	else {
		print "$INPUT{'advert'}";
	}
	print ">\n";
	print "<INPUT TYPE=SUBMIT ";
	print "VALUE=\"View Overall Stats\"> ";
	print "</TD></FORM>\n";
	print "<FORM METHOD=POST ";
	print "ACTION=$admin_cgi><TD>\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	if ($INPUT{'groupstatus'}) {
		print "<INPUT TYPE=HIDDEN NAME=groupstatus ";
		print "VALUE=\"$INPUT{'groupstatus'}\">\n";
	}
	print "<INPUT TYPE=HIDDEN NAME=advert ";
	print "VALUE=$INPUT{'advert'}>\n";
	if ($cryptword) {
		print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
	}
	print "<INPUT TYPE=SUBMIT NAME=dailystats ";
	print "VALUE=\"View Daily Stats\">";
	print "</TD></FORM>\n";
	print "</TR></TABLE></CENTER></P>\n";
	&Footer;
}

sub ShowAdvert {
	@image = split (/\|/,$image);
	foreach $image (@image) {
		print "<P ALIGN=CENTER><IMG SRC=\"$image\"></P>\n";
	}
	if ($url) {
		print "<P ALIGN=CENTER>Destination: ";
		print "<A HREF=\"$url\">$url</A></P>\n";
	}
	if ($username || $email) {
		print "<P ALIGN=CENTER>Account Holder: ";
		if ($email) {
			print "<A HREF=\"mailto:$email\">";
		}
		if ($username) { print "$username"; }
		else { print "$email"; }
		if ($email) {
			print "</A>";
		}
		print "</P>\n";
	}
}

sub edit {
	&ConfirmAdminPassword(1);
	if ($INPUT{'reviewone'} && !($INPUT{'editad'})) {
		$INPUT{'editad'} = $INPUT{'reviewone'};
	}
	$INPUT{'editad'} =~ s/[^\w_-]//g;
	$INPUT{'editad'} =~ tr/A-Z/a-z/;
	&CheckName($INPUT{'editad'});
	if (-s "$adverts_dir/$INPUT{'editad'}.txt") {
		open (DISPLAY, "<$adverts_dir/$INPUT{'editad'}.txt");
		@lines = <DISPLAY>;
		close (DISPLAY);
		foreach $line (@lines) {
			chop ($line) if ($line =~ /\n$/);
			$line =~ s/&/&amp;/g;
			$line =~ s/>/&gt;/g;
			$line =~ s/</&lt;/g;
			$line =~ s/"/&quot;/g;
		}
		($max,$shown,$visits,$url,$image,$height,$width,
		  $alt,$pass,$text,$start,$weight,$zone,
		  $border,$target,$raw,$displayratio,$username,$email,
		  $displayzone) = @lines;
		($max,$maxtype) = split (/\|/, $max);
		($text,$texttype) = split (/\|/, $text);
		($displayratio,$displaycount) = split (/\|/, $displayratio);
	}
	unless ($weight) {
		if ($maxtype || $displayratio) { $weight = "0"; }
		else { $weight = 1; }
	}
	unless ($border) {
		if ($maxtype || $displayratio) { $border = "0"; }
		else { $border = 2; }
	}
	unless ($maxtype) { $maxtype = "E"; }
	unless ($texttype) { $texttype = "B"; }
	unless ($url) { $url = "http://"; }
	$image =~ s/\|/\n/g;
	unless ($image) { $image = "http://"; }
	if ($target eq "_top") { $target = "TARGET=&quot;_top&quot;"; }
	if ($DefaultLinkAttribute && !($target)) {
		$target = $DefaultLinkAttribute;
	}
	&Header("WebAdverts","Add/Edit/Delete Account");
	print "<FORM METHOD=POST ACTION=$admin_cgi>\n";
	print "<P ALIGN=CENTER><BIG><STRONG>Info for the ",
	  "<EM>$INPUT{'editad'}</EM> Account:",
	  "</STRONG></BIG>\n",
	  "<P><CENTER><TABLE CELLPADDING=3>\n",
	  "<TR><TD COLSPAN=2><HR WIDTH=50%></TD></TR>\n",
	  "<TR><TD COLSPAN=2>",
	  "<STRONG>I. General Information</STRONG>: ",
	  "The following information is needed for each account, ",
	  "no matter <EM>how</EM> you're setting things up. Note ",
	  "that while <EM>either</EM> an expiration or a display ",
	  "ratio must be set, it is not necessary to set both. ",
	  "If you're running a &quot;banner exchange,&quot; ",
	  "the display ratio will define how many banner displays ",
	  "earn one exposure. If you're running straight adverts, ",
	  "leave it set to 0, and simply set the appropriate ",
	  "expiration criteria instead. (If you're running ",
	  "an exchange, but want a member to get extra ",
	  "&quot;bonus&quot; exposures, set that bonus number ",
	  "in the &quot;expiration&quot; slot.)</TD></TR>\n",
	  "<TR><TD>Name:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=username VALUE=\"$username\" SIZE=50></TD></TR>\n",
	  "<TR><TD>E-Mail:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=email VALUE=\"$email\" SIZE=50></TD></TR>\n";
	if ($start > $time) {
		$startday = int((($start-$time)/86400)+.5);
	}
	print "<TR><TD>Start Day:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=startday VALUE=\"$startday\" SIZE=5>",
	  "<BR><EM>(Input the number of days ",
	  "in which the advert should ",
	  "start running, or leave blank ",
	  "to start the run immediately.)</EM>",
	  "</TD></TR>\n";
	if ($maxtype eq "D") {
		$max = int((($max-$time)/86400)+.5);
		if ($max < 0) { $max = 0; }
	}
	print "<TR><TD>Expiration:";
	print "</TD><TD><INPUT TYPE=TEXT ";
	print "NAME=purch VALUE=\"$max\" SIZE=25>";
	print "<BR><INPUT TYPE=RADIO NAME=purchtype VALUE=N";
	if ($maxtype eq "N") { print " CHECKED"; }
	print "> Never Expires <INPUT TYPE=RADIO NAME=purchtype VALUE=E";
	if ($maxtype eq "E") { print " CHECKED"; }
	print "> Exposures <INPUT TYPE=RADIO NAME=purchtype VALUE=C";
	if ($maxtype eq "C") { print " CHECKED"; }
	print "> Clicks <INPUT TYPE=RADIO NAME=purchtype VALUE=D";
	if ($maxtype eq "D") { print " CHECKED"; }
	print "> Days\n";
	print "<BR><EM>(Input the maximum number of exposures, ",
	  "click-thrus or days to be allowed for the run.)</EM>",
	  "</TD></TR>\n",
	  "<TR><TD>Display Ratio:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=displayratio VALUE=\"$displayratio\" SIZE=5>",
	  "</TD></TR>\n",
	  "<TR><TD>Site URL:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=url VALUE=\"$url\" SIZE=50></TD></TR>\n",
	  "<TR><TD>Banner URL(s):</TD><TD>",
	  "<TEXTAREA COLS=50 ROWS=5 NAME=image WRAP=VIRTUAL>",
	  "$image</TEXTAREA></TD></TR>\n",
	  "<TR><TD>Weight (Wt.):</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=weight VALUE=\"$weight\" SIZE=5>",
	  "<BR><EM>(0 = never; 1 = always; ",
	  "higher numbers = less often)</EM>",
	  "</TD></TR>\n";
	if (%nonssi_cgis) {
		print "<TR><TD VALIGN=TOP>Zone(s):</TD><TD>";
		foreach $setzone (sort (keys %nonssi_cgis)) {
			print "<INPUT TYPE=CHECKBOX NAME=zone ";
			print "VALUE=\"$setzone\"";
			if ($zone =~ /$setzone/) {
				print " CHECKED";
			}
			print ">$setzone\n<BR>";
		}
		print "<EM>(Select target categories of pages ";
		print "on which this banner should be displayed.)</EM>";
		print "</TD></TR>\n";
		print "<TR><TD></TD><TD><SELECT NAME=displayzone>";
		foreach $setzone (sort (keys %nonssi_cgis)) {
			print "<OPTION";
			if ($displayzone eq $setzone) {
				print " SELECTED";
			}
			print ">$setzone";
		}
		print "</SELECT>";
		print "<BR><EM>(If this advertiser is an exchange member, ";
		print "select the category of banners to be displayed on ";
		print "his or her pages.)</EM>";
		print "</TD></TR>\n";
	}
	else {
		print "<TR><TD>Zone(s):</TD><TD><INPUT TYPE=TEXT ";
		print "NAME=zone VALUE=\"$zone\" SIZE=25></TD></TR>\n";
	}
	print "<TR><TD>Password:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=pass VALUE=\"$pass\" SIZE=50></TD></TR>\n",
	  "<TR><TD COLSPAN=2><HR WIDTH=50%></TD></TR>\n",
	  "<TR><TD COLSPAN=2>",
	  "<STRONG>II. SSI Advert Information</STRONG>: ",
	  "The following information is used to define or modify ",
	  "the &quot;appearance&quot; of an advert banner when ",
	  "called via an SSI tag. None of it is necessary ",
	  "(or even useful) if the advert is called only via IMG ",
	  "tags.</TD></TR>\n",
	  "<TR><TD>Link Attributes:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=target VALUE=\"$target\" SIZE=50></TD></TR>\n",
	  "<TR><TD>Banner Width:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=width VALUE=\"$width\" SIZE=5> pixels</TD></TR>\n",
	  "<TR><TD>Banner Height:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=height VALUE=\"$height\" SIZE=5> pixels</TD></TR>\n",
	  "<TR><TD>Border:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=border VALUE=\"$border\" SIZE=5></TD></TR>\n",
	  "<TR><TD>ALT Text:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=alt VALUE=\"$alt\" SIZE=50></TD></TR>\n",
	  "<TR><TD>Link Text:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=text VALUE=\"$text\" SIZE=50>",
	  "<BR><INPUT TYPE=RADIO NAME=texttype VALUE=T";
	if ($texttype eq "T") { print " CHECKED"; }
	print "> Above Banner <INPUT TYPE=RADIO NAME=texttype VALUE=B";
	if ($texttype eq "B") { print " CHECKED"; }
	print "> Below Banner</TD></TR>\n",
	  "<TR><TD COLSPAN=2><HR WIDTH=50%></TD></TR>\n",
	  "<TR><TD COLSPAN=2>",
	  "<STRONG>III. &quot;Raw Mode&quot; Information</STRONG>: ",
	  "If you so choose, you can specify below <EM>exactly</EM> ",
	  "how an advert is to appear on your pages. (Again, of ",
	  "course, this is only possible if you're using SSI tags; ",
	  "&quot;raw mode&quot; and non-SSI display are ",
	  "incompatible.) <EM>Only use this option if you're sure ",
	  "you know what you're doing; anything input here will ",
	  "override just about everything above!</EM></TD></TR>\n",
	  "<TR><TD>\"Raw\" HTML:</TD><TD>",
	  "<TEXTAREA COLS=50 ROWS=5 NAME=raw WRAP=VIRTUAL>";
	$raw =~ s/&lt;NLB&gt;/\n/g;
	print "$raw</TEXTAREA></TD></TR>\n",
	  "<TR><TD COLSPAN=2><HR WIDTH=50%></TD></TR>\n",
	  "</TABLE></P>\n",
	  "<P><INPUT TYPE=HIDDEN NAME=editad ",
	  "VALUE=\"$INPUT{'editad'}\">\n",
	  "<INPUT TYPE=HIDDEN NAME=start VALUE=\"$start\">\n",
	  "<INPUT TYPE=HIDDEN NAME=password ",
	  "VALUE=$INPUT{'password'}>\n",
	  "Check here to reset advert exposures &amp; clicks: ",
	  "<INPUT TYPE=CHECKBOX NAME=\"resetadvert\">";
	if (-s "$adverts_dir/welcome.txt") {
		print "<P>Check here to send a welcome letter: ",
		  "<INPUT TYPE=CHECKBOX NAME=\"welcomeletter\">";
	}
	if ($cryptword) {
		print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
	}
	print "<P><INPUT TYPE=SUBMIT NAME=editfinal ";
	print "VALUE=\"Add/Edit Account\">\n";
	if (-s "$adverts_dir/$INPUT{'editad'}.txt") {
		print "<P><INPUT TYPE=SUBMIT NAME=del ";
		print "VALUE=\"Delete Account\"> ";
		print "<INPUT TYPE=HIDDEN NAME=delad ";
		print "VALUE=\"$INPUT{'editad'}\">\n";
	}
	print "</P></CENTER></FORM>\n";
	&Footer;
}

sub UserEdit {
	$INPUT{'reviewone'} =~ s/[^\w_-]//g;
	$INPUT{'reviewone'} =~ tr/A-Z/a-z/;
	&CheckName($INPUT{'reviewone'});
	if (-s "$adverts_dir/$INPUT{'reviewone'}.txt") {
		open (DISPLAY, "<$adverts_dir/$INPUT{'reviewone'}.txt");
		@lines = <DISPLAY>;
		close (DISPLAY);
		foreach $line (@lines) {
			chop ($line) if ($line =~ /\n$/);
			$line =~ s/&/&amp;/g;
			$line =~ s/>/&gt;/g;
			$line =~ s/</&lt;/g;
			$line =~ s/"/&quot;/g;
		}
		($max,$shown,$visits,$url,$image,$height,$width,
		  $alt,$pass,$text,$start,$weight,$zone,
		  $border,$target,$raw,$displayratio,$username,$email,
		  $displayzone) = @lines;
		unless ($INPUT{'password'} eq $pass) {
			&ConfirmAdminPassword(2);
		}
	}
	else {
		$pass = $INPUT{'password'};
	}
	unless ($url) { $url = "http://"; }
	$image =~ s/\|/\n/g;
	unless ($image) { $image = "http://"; }
	&Header("WebAdverts","Add/Edit/Delete Account");
	print "<FORM METHOD=POST ACTION=$admin_cgi>\n",
	  "<P ALIGN=CENTER><BIG><STRONG>Info for the ",
	  "<EM>$INPUT{'reviewone'}</EM> Account:",
	  "</STRONG></BIG>\n",
	  "<P><CENTER><TABLE CELLPADDING=3>\n",
	  "<TR><TD COLSPAN=2><HR WIDTH=50%></TD></TR>\n",
	  "<TR><TD>Name:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=username VALUE=\"$username\" SIZE=50></TD></TR>\n",
	  "<TR><TD>E-Mail:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=email VALUE=\"$email\" SIZE=50></TD></TR>\n",
	  "<TR><TD>Site URL:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=url VALUE=\"$url\" SIZE=50></TD></TR>\n",
	  "<TR><TD>Banner URL(s):</TD><TD>",
	  "<TEXTAREA COLS=50 ROWS=5 NAME=image WRAP=VIRTUAL>",
	  "$image</TEXTAREA></TD></TR>\n";
	if (%nonssi_cgis) {
		print "<TR><TD VALIGN=TOP>Zone(s):</TD><TD>";
		foreach $setzone (sort (keys %nonssi_cgis)) {
			print "<INPUT TYPE=CHECKBOX NAME=zone ";
			print "VALUE=\"$setzone\"";
			if ($zone =~ /$setzone/) {
				print " CHECKED";
			}
			print ">$setzone\n<BR>";
		}
		print "<EM>(Select target categories of pages ";
		print "on which this banner should be displayed.)</EM>";
		print "</TD></TR>\n";
		print "<TR><TD></TD><TD><SELECT NAME=displayzone>";
		foreach $setzone (sort (keys %nonssi_cgis)) {
			print "<OPTION";
			if ($displayzone eq $setzone) {
				print " SELECTED";
			}
			print ">$setzone";
		}
		print "</SELECT>";
		print "<BR><EM>(Select the category of banners ";
		print "to be displayed on your own pages.)</EM>";
		print "</TD></TR>\n";
	}
	print "<TR><TD>Password:</TD><TD><INPUT TYPE=TEXT ",
	  "NAME=pass VALUE=\"$pass\" SIZE=50></TD></TR>\n",
	  "<TR><TD COLSPAN=2><HR WIDTH=50%></TD></TR>\n",
	  "</TABLE></P>\n",
	  "<P><INPUT TYPE=HIDDEN NAME=editad ",
	  "VALUE=\"$INPUT{'reviewone'}\">\n",
	  "<INPUT TYPE=HIDDEN NAME=password ",
	  "VALUE=$INPUT{'password'}>\n";
	if ($AllowUserEdit && $INPUT{'newuser'}) {
		print "<INPUT TYPE=HIDDEN NAME=newuser ";
		print "VALUE=$INPUT{'newuser'}>\n";
	}
	if ($cryptword) {
		print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
	}
	print "<P><INPUT TYPE=SUBMIT NAME=editfinal ";
	print "VALUE=\"Add/Edit Account\">\n";
	if (-s "$adverts_dir/$INPUT{'reviewone'}.txt") {
		print "<P><INPUT TYPE=SUBMIT NAME=del ";
		print "VALUE=\"Delete Account\"> ";
		print "<INPUT TYPE=HIDDEN NAME=delad ";
		print "VALUE=\"$INPUT{'reviewone'}\">\n";
	}
	print "</P></CENTER></FORM>\n";
	&Footer;
}

sub CheckName {
	local($namecheck) = @_;
	if (($namecheck eq "adcount") || ($namecheck eq "adlist")
	  || ($namecheck eq "adnew") || ($namecheck eq "adpassword")
	  || ($namecheck eq "groups") || ($namecheck eq "register")
	  || ($namecheck eq "welcome") || ($namecheck =~ /ads_/)) {
		&Header("WebAdverts Error!","Illegal Account Name!");
		print "<P>The account name you selected isn't allowed. ";
		print "Please go back and pick another one!</P>\n";
		&Footer;
	}
}

sub groupedit {
	&ConfirmAdminPassword(1);
	$INPUT{'editgroup'} =~ s/[^\w_-]//g;
	$INPUT{'editgroup'} =~ tr/A-Z/a-z/;
	&CheckName($INPUT{'editgroup'});
	if (-s "$adverts_dir/$INPUT{'editgroup'}.grp") {
		open (DISPLAY, "<$adverts_dir/$INPUT{'editgroup'}.grp");
		@lines = <DISPLAY>;
		close (DISPLAY);
		$grouppassword = $lines[0];
		$adverts = join(' ',@lines);
	}
	&Header("WebAdverts","Add/Edit/Delete Group");
	print "<FORM METHOD=POST ACTION=$admin_cgi>\n";
	print "<P><CENTER><BIG><STRONG>Info for the ";
	print "<EM>$INPUT{'editgroup'}</EM> Group:";
	print "</STRONG></BIG>\n";
	print "<P>Select the adverts to be included in this group:\n";
	open (COUNT, "<$adverts_dir/adlist.txt");
	@lines = <COUNT>;
	close (COUNT);
	foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
	@sortedlines = sort (@lines);
	$size = @lines;
	if ($size > 10) { $size = 10; }
	print "<P><SELECT NAME=groupadverts MULTIPLE ";
	print "SIZE=$size>\n";
	foreach $advertiser (@sortedlines) {
		next if (length($advertiser) < 1);
		print "<OPTION VALUE=\"$advertiser\"";
		if ($adverts && ($adverts =~ $advertiser)) {
			print " SELECTED";
		}
		print "> $advertiser ";
	}
	print "</SELECT>\n";
	print "<P>Password: <INPUT TYPE=TEXT ";
	print "NAME=pass VALUE=\"$grouppassword\" SIZE=25>\n";
	print "<P><INPUT TYPE=HIDDEN NAME=editgroup ";
	print "VALUE=\"$INPUT{'editgroup'}\">\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	print "<INPUT TYPE=SUBMIT NAME=editgroupfinal ";
	print "VALUE=\"Add/Edit Group\">\n";
	if (-s "$adverts_dir/$INPUT{'editgroup'}.grp") {
		print "<P><INPUT TYPE=SUBMIT NAME=delgroup ";
		print "VALUE=\"Delete Group\"> ";
		print "<INPUT TYPE=HIDDEN NAME=delgroupname ";
		print "VALUE=\"$INPUT{'editgroup'}\">\n";
	}
	print "</P></CENTER></FORM>\n";
	&Footer;
}

sub del {
	$INPUT{'delad'} =~ s/[^\w_-]//g;
	$INPUT{'delad'} =~ tr/A-Z/a-z/;
	&CheckName($INPUT{'delad'});
	unless (-s "$adverts_dir/$INPUT{'delad'}.txt") {
		&Header("WebAdverts Error!","Invalid Account Name!");
		print "<P ALIGN=CENTER>There is no account with the name ";
		print "<STRONG>&quot;$INPUT{'delad'}&quot;</STRONG> ";
		print "on the list!\n";
		print "<P ALIGN=CENTER>(Note that account names ";
		print "<EM>are</EM> case sensitive!)</P>\n";
		&Footer;
	}
	$INPUT{'advert'} = $INPUT{'delad'};
	&ConfirmUserPassword;
	&Header("WebAdverts","&quot;Delete&quot; Request Confirmation");
	print "<FORM METHOD=POST ACTION=$admin_cgi>\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	print "<P><CENTER>Are you <EM>sure</EM> you want to delete the ";
	print "<STRONG>$INPUT{'delad'}</STRONG> account?\n";
	print "<INPUT TYPE=HIDDEN NAME=delad VALUE=$INPUT{'delad'}>\n";
	if ($cryptword) {
		print "<INPUT TYPE=HIDDEN NAME=admincheck VALUE=1>\n";
	}
	print "<INPUT TYPE=SUBMIT NAME=delfinal VALUE=\"Yes\">\n";
	print "</CENTER></P></FORM>\n";
	&Footer;
}

sub delgroup {
	$INPUT{'delgroupname'} =~ s/[^\w_-]//g;
	$INPUT{'delgroupname'} =~ tr/A-Z/a-z/;
	&CheckName($INPUT{'delgroupname'});
	unless (-s "$adverts_dir/$INPUT{'delgroupname'}.grp") {
		&Header("WebAdverts Error!","Invalid Group Name!");
		print "<P ALIGN=CENTER>There is no group ";
		print "on the list defined with the name <STRONG>";
		print "&quot;$INPUT{'delgroupname'}&quot;</STRONG>!\n";
		print "<P ALIGN=CENTER>(Note that group names ";
		print "<EM>are</EM> case sensitive!)</P>\n";
		&Footer;
	}
	&ConfirmAdminPassword(1);
	&Header("WebAdverts","&quot;Delete&quot; Request Confirmation");
	print "<FORM METHOD=POST ACTION=$admin_cgi>\n";
	print "<P><CENTER>Are you <EM>sure</EM> you want to delete the ";
	print "<STRONG>$INPUT{'delgroupname'}</STRONG> group? ";
	print "<INPUT TYPE=HIDDEN NAME=delgroupname ";
	print "VALUE=$INPUT{'delgroupname'}>\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	print "<INPUT TYPE=SUBMIT NAME=delgroupfinal VALUE=\"Yes\">\n";
	print "</CENTER></FORM>\n";
	print "<P>(Please note that deleting the group will ";
	print "<EM>not</EM> delete or otherwise affect the adverts ";
	print "themselves. Only the ability to view all their stats ";
	print "on a single page will be gone!)</P>\n";
	&Footer;
}

sub newpass {
	unless ($INPUT{'passad'} && ($INPUT{'passad'} eq $INPUT{'passad2'})) {
		&Header("WebAdverts Error!","Password Mismatch!");
		print "<P ALIGN=CENTER>Your administrative password was ";
		print "not set, as the two entries were different!</P>\n";
		&Footer;
	}
	open (PASSWORD, "<$adverts_dir/adpassword.txt");
	$password = <PASSWORD>;
	close (PASSWORD);
	chop ($password) if ($password =~ /\n$/);
	if ($password) {
		if ($INPUT{'password'}) {
			$newpassword = crypt($INPUT{'password'}, "aa");
		}
		else {
			&Header("WebAdverts Error!","No Password!");
			print "<P ALIGN=CENTER>You must ";
			print "enter a password!</P>\n";
			&Footer;
		}
		unless ($newpassword eq $password) {
			&Header("WebAdverts Error!","Invalid Password!");
			print "<P ALIGN=CENTER>";
			print "The password you entered is incorrect!</P>\n";
			&Footer;
		}
	}
	$newpassword = crypt($INPUT{'passad'}, "aa");
	&LockOpen (PASSWORD, "adpassword.txt");
	seek (PASSWORD,0,0);
	print PASSWORD "$newpassword";
	truncate (PASSWORD,tell(PASSWORD));
	&LockClose (PASSWORD,"adpassword.txt");
	&Header("WebAdverts","Password Set");
	print "<P ALIGN=CENTER>Your administrative password ";
	print "has been set.</P>\n";
	$INPUT{'password'} = $INPUT{'passad'};
	&LinkBack;
	&Footer;
}

sub resetcount {
	&ConfirmAdminPassword(1);
	&LockOpen (COUNT, "adcount.txt");
	seek(COUNT, 0, 0);
	print COUNT "1\n";
	print COUNT "0\n";
	print COUNT "$time\n";
	truncate (COUNT, tell(COUNT));
	&LockClose (COUNT, "adcount.txt");
	if ($AdminDisplaySetup) { &defineview; }
	else {
		$INPUT{'whichtype'} = "pending established groups";
		$INPUT{'whichtime'} = "active expired disabled";
		$INPUT{'whichzone'} = "";
		&reviewall;
	}
}

sub editfinal {
	$INPUT{'editad'} =~ s/[^\w_-]//g;
	$INPUT{'editad'} =~ tr/A-Z/a-z/;
	$INPUT{'advert'} = $INPUT{'editad'};
	&CheckName($INPUT{'advert'});
	unless ($AllowUserEdit && $INPUT{'newuser'}) {
		&ConfirmUserPassword;
	}
	$editad = $INPUT{'editad'};
	if (-s "$adverts_dir/$editad.txt") {
		open (DISPLAY, "<$adverts_dir/$editad.txt");
		@lines = <DISPLAY>;
		close (DISPLAY);
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		if ($cryptword) {
			($shown,$visits,$start,$displaycount)
			  = @lines[1,2,10,16];
			($other,$displaycount) = split (/\|/, $displaycount);
		}
		else {
			($max,$shown,$visits,$dmy,$dmy,$height,$width,
			  $alt,$dmy,$text,$start,$weight,$zone,
			  $border,$target,$raw,$displayratio,
			  $dmy,$dmy,$displayzone) = @lines;
			($max,$maxtype) = split (/\|/, $max);
			($text,$texttype) = split (/\|/, $text);
			($displayratio,$displaycount)
			  = split (/\|/, $displayratio);
		}
	}
	elsif (!($cryptword)) {
		$maxtype = "E";
		$texttype = "B";
		$weight = 1;
		$border = 2;
	}
	$INPUT{'email'} =~ s/\s//g;
	unless ($INPUT{'email'} =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)|,|;/
	  || $INPUT{'email'} !~
	  /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/)
	  {
		$email = "$INPUT{'email'}";
	}
	$INPUT{'url'} =~ s/\s//g;
	unless ($INPUT{'url'} =~ /\*|(\.\.)|(^\.)|(\/\/\.)/ ||
	  $INPUT{'url'} !~ /(.*\:\/\/.*\..*|mailto:.*@.*)/) {
		$url = $INPUT{'url'};
	}
	@image = split (/\cM|\n/,$INPUT{'image'});
	foreach $fauximage (@image) {
		$fauximage =~ s/\s//g;
		unless ($fauximage =~ /\*|(\.\.)|(^\.)|(\/\/\.)/ ||
		  $fauximage !~ /.*\:\/\/.*\..*/) {
			$image = $image.$fauximage."|";
		}
	}
	chop $image;
	$pass = $INPUT{'pass'};
	if ($cryptword) {
		$displayratio = $INPUT{'displayratio'};
		$weight = int($INPUT{'weight'});
	}
	else {
		$displayratio = $DefaultDisplayRatio;
		$weight = $DefaultWeight;
	}
	if ($INPUT{'zone'}) {
		$zone = $INPUT{'zone'};
		$zone =~ s/^\s+//;
		$zone =~ s/\s+$//;
		$zone =~ s/\s+/ /g;
	}
	if ($INPUT{'displayzone'}) {
		$displayzone = $INPUT{'displayzone'};
	}
	if ($cryptword) {
		if ($INPUT{'purchtype'} eq "D") {
			$INPUT{'purch'} = $time + ($INPUT{'purch'}*86400);
		}
		$INPUT{'purch'} =~ s/[^\d]//g;
		$max = $INPUT{'purch'};
		$maxtype = $INPUT{'purchtype'};
		if ($INPUT{'startday'}) {
			$INPUT{'startday'}
			  = $time + ($INPUT{'startday'}*86400);
			$start = $INPUT{'startday'}
		}
		elsif ($start > $time) {
			$start = $time;
		}
		$height = int($INPUT{'height'});
		$width = int($INPUT{'width'});
		$alt = $INPUT{'alt'};
		$INPUT{'text'} =~ s/^\s+//;
		$INPUT{'text'} =~ s/\s+$//;
		$INPUT{'text'} =~ s/\s+/ /g;
		$text = $INPUT{'text'};
		$texttype = $INPUT{'texttype'};
		$border = int($INPUT{'border'});
		$target = $INPUT{'target'};
		$INPUT{'raw'} =~ s/(\cM|\n)+/<NLB>/g;
		$raw = $INPUT{'raw'};
	}
	unless ($pass) {
		&Header("WebAdverts Error!","Incomplete Entry!");
		print "<P>You didn't provide all of the necessary ";
		print "information! You must at <EM>least</EM> ";
		print "include a password!</P>\n";
		&Footer;
	}
	if ((($maxtype eq "C") || ($maxtype eq "D")) && ($displayratio)) {
		&Header("WebAdverts Error!","Invalid Entry!");
		print "<P>You've indicated that this account is to earn exposures by ";
		print "showing other banners, but have also indicated that it is to ";
		print "expire based on date or click-thrus.  These two designations are ";
		print "mutually incompatible!  Display ratios may only be set for ";
		print "accounts which are defined as non-expiring, or for which a set ";
		print "number of &quot;bonus&quot; exposures have been defined.</P>\n";
		&Footer;
	}
	$PresenceCheck = 0;
	if (-s "$adverts_dir/adnew.txt") {
		&LockOpen (COUNT, "adnew.txt");
		@lines = <COUNT>;
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		seek(COUNT, 0, 0);
		foreach $line (@lines) {
			if ($line eq $editad) { $PresenceCheck = 1; }
			unless (($line eq $editad) || (length($line) < 1)) {
				print COUNT "$line\n";
			}
		}
		truncate (COUNT, tell(COUNT));
		&LockClose (COUNT, "adnew.txt");
	}
	if (-s "$adverts_dir/adlist.txt") {
		&LockOpen (COUNT, "adlist.txt");
		@lines = <COUNT>;
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		seek(COUNT, 0, 0);
		foreach $line (@lines) {
			if ($line eq $editad) { $PresenceCheck = 1; }
			unless (($line eq $editad) || (length($line) < 1)) {
				print COUNT "$line\n";
			}
		}
		truncate (COUNT, tell(COUNT));
		&LockClose (COUNT, "adlist.txt");
	}
	if ($INPUT{'resetadvert'}
	  || (!$PresenceCheck && !$shown)) {
		$shown = 0;
		$visits = 0;
		unless ($start > $time) { $start = $time; }
		$displaycount = 0;
		unlink ("$adverts_dir/$editad.log");
		unlink ("$adverts_dir/$editad.log.bak");
		unlink ("$adverts_dir/$editad.ips");
	}
	if ($maxtype eq "N") { $max = 0; }
	&LockOpen (DISPLAY, "$editad.txt");
	seek (DISPLAY,0,0);
	print DISPLAY "$max|$maxtype\n";
	print DISPLAY "$shown\n";
	print DISPLAY "$visits\n";
	print DISPLAY "$url\n";
	print DISPLAY "$image\n";
	print DISPLAY "$height\n";
	print DISPLAY "$width\n";
	print DISPLAY "$alt\n";
	print DISPLAY "$pass\n";
	print DISPLAY "$text|$texttype\n";
	print DISPLAY "$start\n";
	print DISPLAY "$weight\n";
	print DISPLAY " $zone \n";
	print DISPLAY "$border\n";
	print DISPLAY "$target\n";
	print DISPLAY "$raw\n";
	print DISPLAY "$displayratio|$displaycount\n";
	print DISPLAY "$INPUT{'username'}\n";
	print DISPLAY "$email\n";
	print DISPLAY "$displayzone\n";
	truncate (DISPLAY,tell(DISPLAY));
	&LockClose (DISPLAY, "editad.txt");
	if ($cryptword || !($RequireAdminApproval)) {
		&LockOpen (COUNT, "adlist.txt");
		@adlist = <COUNT>;
		seek (COUNT,0,0);
		foreach $adlist (@adlist) {
			print COUNT "$adlist";
		}
		print COUNT "$editad\n";
		truncate (COUNT,tell(COUNT));
		&LockClose (COUNT, "adlist.txt");
	}
	else {
		&LockOpen (COUNT, "adnew.txt");
		@adnew = <COUNT>;
		seek (COUNT,0,0);
		foreach $adnew (@adnew) {
			print COUNT "$adnew";
		}
		print COUNT "$editad\n";
		truncate (COUNT,tell(COUNT));
		&LockClose (COUNT, "adnew.txt");
		&SendMail($email_address);
	}
	$INPUT{'reviewone'} = $editad;
	&reviewone;
}

sub editgroupfinal {
	&ConfirmAdminPassword(1);
	$INPUT{'editgroup'} =~ s/[^\w_-]//g;
	$INPUT{'editgroup'} =~ tr/A-Z/a-z/;
	&CheckName($INPUT{'editgroup'});
	$editgroup = $INPUT{'editgroup'};
	$pass = $INPUT{'pass'};
	@groupadverts = split(' ',$INPUT{'groupadverts'});
	unless ($pass && (@groupadverts > 0)) {
		&Header("WebAdverts Error!","Incomplete Form!");
		print "<P>You didn't provide all of the necessary ";
		print "information to allow creation ";
		print "of the <STRONG>$editgroup</STRONG> ";
		print "group!</P>\n";
		&Footer;
	}
	&LockOpen (GROUP, "$editgroup.grp");
	seek (GROUP,0,0);
	print GROUP "$pass\n";
	foreach $advert (@groupadverts) {
		print GROUP "$advert\n";
	}
	truncate (GROUP,tell(GROUP));
	&LockClose (GROUP,"$editgroup.grp");
	$PresenceCheck = 0;
	if (-s "$adverts_dir/groups.txt") {
		open (COUNT, "<$adverts_dir/groups.txt");
		@lines = <COUNT>;
		close (COUNT);
	}
	foreach $line (@lines) {
		chop ($line) if ($line =~ /\n$/);
		if ($line eq $editgroup) { $PresenceCheck = 1; }
	}
	unless ($PresenceCheck) {
		&LockOpen (COUNT, "groups.txt");
		@groups = <COUNT>;
		seek (COUNT,0,0);
		foreach $group (@groups) {
			print COUNT "$group";
		}
		print COUNT "$editgroup\n";
		truncate (COUNT,tell(COUNT));
		&LockClose (COUNT,"groups.txt");
	}
	&Header("WebAdverts","Group Updated!");
	print "<P ALIGN=CENTER>";
	print "The <STRONG>$editgroup</STRONG> group now includes ";
	print "the following adverts:\n";
	print "<P ALIGN=CENTER><STRONG>";
	foreach $advert (@groupadverts) {
		chop $advert if ($advert =~ /\n$/);
		print "$advert ";
	}
	print "</STRONG>\n";
	&LinkBack;
	&Footer;
}

sub delfinal {
	$INPUT{'delad'} =~ s/[^\w_-]//g;
	$INPUT{'delad'} =~ tr/A-Z/a-z/;
	$INPUT{'advert'} = $INPUT{'delad'};
	&CheckName($INPUT{'advert'});
	&ConfirmUserPassword;
	$delad = $INPUT{'delad'};
	unlink ("$adverts_dir/$delad.txt");
	unlink ("$adverts_dir/$delad.txt.bak");
	unlink ("$adverts_dir/$delad.log");
	unlink ("$adverts_dir/$delad.log.bak");
	unlink ("$adverts_dir/$delad.ips");
	if (-s "$adverts_dir/adlist.txt") {
		&LockOpen (COUNT, "adlist.txt");
		@lines = <COUNT>;
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		seek (COUNT,0,0);
		foreach $line (@lines) {
			unless (($line eq $delad) || (length($line) < 1)) {
				print COUNT "$line\n";
			}
		}
		truncate (COUNT, tell(COUNT));
		&LockClose (COUNT,"adlist.txt");
	}
	if (-s "$adverts_dir/adnew.txt") {
		&LockOpen (COUNT, "adnew.txt");
		@lines = <COUNT>;
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		seek (COUNT,0,0);
		foreach $line (@lines) {
			unless (($line eq $delad) || (length($line) < 1)) {
				print COUNT "$line\n";
			}
		}
		truncate (COUNT, tell(COUNT));
		&LockClose (COUNT,"adnew.txt");
	}
	if ($cryptword) {
		if ($AdminDisplaySetup) { &defineview; }
		else {
			$INPUT{'whichtype'} = "pending established groups";
			$INPUT{'whichtime'} = "active expired disabled";
			$INPUT{'whichzone'} = "";
			&reviewall;
		}
	}
	&userintro;
}

sub delgroupfinal {
	&ConfirmAdminPassword(1);
	$INPUT{'delgroupname'} =~ s/[^\w_-]//g;
	$INPUT{'delgroupname'} =~ tr/A-Z/a-z/;
	&CheckName($INPUT{'delgroupname'});
	$delgroup = $INPUT{'delgroupname'};
	unlink ("$adverts_dir/$delgroup.grp");
	if (-s "$adverts_dir/groups.txt") {
		&LockOpen (COUNT, "groups.txt");
		@lines = <COUNT>;
		foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
		seek (COUNT,0,0);
		foreach $line (@lines) {
			unless (($line eq $delgroup) || (length($line) < 1)) {
				print COUNT "$line\n";
			}
		}
		truncate (COUNT, tell(COUNT));
		&LockClose (COUNT,"groups.txt");
	}
	if ($AdminDisplaySetup) { &defineview; }
	else {
		$INPUT{'whichtype'} = "pending established groups";
		$INPUT{'whichtime'} = "active expired disabled";
		$INPUT{'whichzone'} = "";
		&reviewall;
	}
}

sub LinkBack {
	print "<P><CENTER>\n";
	print "<FORM METHOD=POST ACTION=$admin_cgi>\n";
	print "<INPUT TYPE=HIDDEN NAME=password ";
	print "VALUE=$INPUT{'password'}>\n";
	print "<INPUT TYPE=HIDDEN NAME=reviewone ";
	print "VALUE=\"Define View\">\n";
	print "<INPUT TYPE=SUBMIT ";
	print "VALUE=\"Reload Account Index\">\n";
	print "</FORM></CENTER></P>\n";
}

sub Header {
	($title,$header) = @_;
	if ($ExchangeName) {
		$title =~ s/WebAdverts/$ExchangeName/g;
		$header =~ s/WebAdverts/$ExchangeName/g;
	}
	print "<HTML><HEAD><TITLE>$title</TITLE></HEAD>\n";
	print "<BODY $bodyspec>\n";
	if ($header_file) {
		open (HEADER,"<$header_file");
		@header = <HEADER>;
		close (HEADER);
		foreach $line (@header) {
			print "$line";
		}
	}
	#print "<HR><H1 ALIGN=CENTER>$header</H1><HR>\n";
}

sub Footer {
	if ($footer_file) {
		print "<HR>\n";
		open (FOOTER,"<$footer_file");
		@footer = <FOOTER>;
		close (FOOTER);
		foreach $line (@footer) {
			print "$line";
		}
	}
	print "</BODY></HTML>\n";
	unless ($UseLocking) { &MasterLockClose; }
	reset 'A-Za-z';
	exit;
}

sub register {
	unless ($INPUT{'register'} eq "frtytw") {
		&Header("WebAdverts Error!","Incorrect Code!");
		print "<P ALIGN=CENTER>Sorry, but the registration code ";
		print "you entered is incorrect!</P>\n";
		&Footer;
	}
	open (REGISTER, ">$adverts_dir/register.txt");
	print REGISTER "frtytw";
	close (REGISTER);
	&Header("WebAdverts","Thanks For Registering!");
	print "<P ALIGN=CENTER>Your support is appreciated!</P>\n";
	&Footer;
}

sub reginfo {
	&Header("WebAdverts","Registration Information");
	print "<P>WebAdverts is distributed as shareware. While you ",
	  "are free to modify and use it as you see fit, any usage ",
	  "should be registered. The registration fee is just \$50 ",
	  "(US). Payment should be sent via check or money order ",
	  "to <STRONG>Darryl C. Burgdorf, Affordable Web Space ",
	  "Design, 3524 Pacific Street, Omaha NE 68105</STRONG>.\n",
	  "<P>(If you happen to live in a country other than the ",
	  "United States, you can write a check in your local ",
	  "currency for the equivalent of \$57.50. That will cover ",
	  "the \$50 registration fee and the \$7.50 ",
	  "service fee which my bank charges. Please do ",
	  "<STRONG><EM>not</EM></STRONG> write me a check ",
	  "in US funds drawn on a non-US bank; the service charge ",
	  "for those can be anywhere from \$10 to \$25!)\n",
	  "<P>Thank you for your support!\n",
	  "<P><CENTER>\n",
	  "<FORM METHOD=POST ACTION=$admin_cgi>\n",
	  "<INPUT TYPE=SUBMIT VALUE=\"Enter Registration Code:\">\n",
	  "<INPUT TYPE=TEXT NAME=register SIZE=10>\n",
	  "</FORM></CENTER></P>\n";
	&Footer;
}

sub date_to_count {
	($perp_mon,$perp_day,$perp_year) = @_;
	%day_counts =
	  (1,0,2,31,3,59,4,90,5,120,6,151,7,181,
	  8,212,9,243,10,273,11,304,12,334);
	$perp_days = (($perp_year-93)*365)+(int(($perp_year-93)/4));
	$perp_days = $perp_days + $day_counts{$perp_mon};
	if ((int(($perp_year-92)/4) eq (($perp_year-92)/4))
	  && ($perp_mon>2)) {
		$perp_days++;
	}
	$perp_days = $perp_days + $perp_day;
}

sub count_to_date {
	local($perp_days) = @_;
	%day_counts =
	  (1,0,2,31,3,59,4,90,5,120,6,151,
	  7,181,8,212,9,243,10,273,11,304,12,334);
	$perp_year = (int(($perp_days-1)/1461))*4;
	$perp_days = $perp_days-(int(($perp_days-1)/1461)*1461);
	if ($perp_days == 1461) {
		$perp_year = 93+$perp_year+3;
		$perp_days = $perp_days-1095;
	}
	else {
		$perp_year = 93+$perp_year+(int(($perp_days-1)/365));
		$perp_days = $perp_days-(int(($perp_days-1)/365)*365);
	}
	foreach $key (sort ({$a <=> $b} keys %day_counts)) {
		$perp_count = $day_counts{$key};
		if ((int(($perp_year-92)/4) eq (($perp_year-92)/4))
		  && ($key>2)) {
			$perp_count++;
		}
		if ($perp_days > $perp_count) {
			$perp_mon = $key;
			$perp_subtract = $perp_count;
		}
	}
	$perp_day = $perp_days-$perp_subtract;
}

sub LockOpen {
	local(*FILE,$lockfilename) = @_;
	unless (-e "$adverts_dir/$lockfilename") {
		open (FILE,">$adverts_dir/$lockfilename");
		print FILE "\n";
		close (FILE);
	}
	open (FILE,"+<$adverts_dir/$lockfilename") || &Error_File($lockfilename);
	if ($UseLocking) {
		local($TrysLeft) = 1500;
		while ($TrysLeft--) {
			select(undef,undef,undef,0.01);
			(flock(FILE,6)) || next;
			last;
		}
		unless ($TrysLeft >= 0) {
			&Error_File($lockfilename);
		}
	}
}

sub LockClose {
	local(*FILE,$lockfilename) = @_;
	close (FILE);
}

sub MasterLockOpen {
	local($TrysLeft) = 1500;
	if ((-e "$adverts_dir/masterlockfile.lok")
	  && ((stat("$adverts_dir/masterlockfile.lok"))[9]+15<$time)) {
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
		$UseLocking = 1;
		&Error_File(masterlockfile.lok);
	}
}

sub MasterLockClose {
	unlink ("$adverts_dir/masterlockfile.lok");
}

sub commas {
	local($_)=@_;
	1 while s/(.*\d)(\d\d\d)/$1,$2/;
	$_;
}

sub SendMail {
	local($To) = $_[0];
	return unless $To;
	if ($To eq $email_address) {
		$messagebody = "Subject: A New Account Awaits Approval!\n\n";
		$messagebody .= "A new account, $editad, awaits approval ";
		$messagebody .= "in the $ExchangeName exchange!\n";
	}
	else {
		$messagebody = "Subject: Welcome to the $ExchangeName Exchange!\n\n";
		$messagebody .= $body;
	}
	unless ($mailprog eq "SMTP") {
		open (MAIL, "|$mailprog -t") || &Error("9450","9451");
		print MAIL "To: $To\n";
		print MAIL "From: $email_address\n",
		  "$messagebody";
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
	print SMTP "$messagebody";
	print SMTP "\r\n\r\n.\r\n";
	sysread(SMTP, $_, 1024);
	shutdown(SMTP, 2);
}

sub Error_File {
	&Header("WebAdverts Error!","File Permission Error!");
	print "<P>The server encountered an error while trying ";
	print "to access <STRONG>$_[0]</STRONG>!\n";
	print "<P>The most likely cause of the problem is a permissions ";
	print "error in your adverts directory ($adverts_dir). Make ";
	print "sure that the directory exists and that it is set ";
	print "world-writable.</P>\n";
	&Footer;
}

sub Error_NoStats {
	&Header("WebAdverts Error!","No Daily Stats!");
	print "<P ALIGN=CENTER>";
	print "Sorry, but it seems ";
	print "there is no daily log file available ";
	print "for the $INPUT{'advert'} account!</P>\n";
	&Footer;
}

sub Error_NoIPLog {
	&Header("WebAdverts Error!","No IP Log!");
	print "<P ALIGN=CENTER>";
	print "Sorry, but it seems ";
	print "there is no IP address log file available ";
	print "for the $INPUT{'advert'} account!</P>\n";
	&Footer;
}

sub UpdateAdList {
	&LockOpen (COUNT, "adcount.txt");
	@lines = <COUNT>;
	foreach $line (@lines) { chop ($line) if ($line =~ /\n$/); }
	seek (COUNT,0,0);
	print COUNT "$lines[0]\n";
	print COUNT "$lines[1]\n";
	print COUNT "$lines[2]\n";
	$max = @lines - 1;
	@advertisements = @lines[3..$max];
	open (LIST, ">$adverts_dir/adlist.txt");
	foreach $advertiser (@advertisements) {
		next if (length($advertiser) < 1);
		print LIST "$advertiser\n";
	}
	truncate (COUNT, tell(COUNT));
	&LockClose (COUNT,"adcount.txt");
	truncate (LIST, tell(LIST));
	close (LIST);
}
