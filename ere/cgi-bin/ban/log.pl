#!/usr/bin/perl

###################################################
#                                                 #
# Virtual Visions Ad Banner Rotation Script v1.70 #
# Copyright 1999 by Barracuda                     #
# Email - baracuda@feartech.com                   #
#                                                 #
###################################################

# this is the url of this script

$script = 'http://www.erenetwork.com/cgi-bin/ban/log.pl';

# this is the url of admin.pl

$admin_script = 'http://www.erenetwork.com/cgi-bin/ban/admin.pl';

# this is the directory where you want your ad banner
# logs to be stored... chmod 777 this directory!

$log_dir = '/home/erenetw/public_html/ban/data';

# this is the url to the index.htm file which will be
# created in your $log_dir

$logfile_url = 'http://www.erenetwork.com/ban/data/index.htm';

# this is the path to banners.txt

$config = '/home/erenetw/public_html/cgi-bin/ban/banners.txt';

# this is the path to your access.log

$access_log = '/home/erenetw/public_html/cgi-bin/ban/access.log';

###################################################

&time;
&get_access_logs;
&get_ad_data;
&get_logs;
&build_index;

###################################################

print "Location: $logfile_url\n\n";

################
# sub routines #
################

sub get_ad_data
{
	open(CONFIG,"$config") || &cgiError ("Error Opening: $config", "$!");
	@banners=<CONFIG>;
	close(CONFIG);
}

sub get_access_logs
{
	open(ACCESSLOG,"$access_log") || &cgiError ("Error Opening: $access_log", "$!");
	@access=<ACCESSLOG>;
	close(ACCESSLOG);

	$exposure_log .= join('',@access);
}

sub get_logs
{
	$num = 0;

	foreach $line (@banners)
	{
		chomp($line);
		($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$line);
		$id = "$id";

		if (open(LOG,"$log_dir/$id.txt"))
		{
			@data = <LOG>;
			close(LOG);
		}

		else
		{
			@data=("");
		}

		&build_stats;
		&build_ad_log;

		$banners[$num] .= "||$exposures||$clicks||$ratio";

		$num++;
	}
}

sub get_exposures
{
	$exposures = $exposure_log =~ s/$img/$img/ig;	
}

sub build_stats
{
	undef %referrer;
	undef %ip;
	undef %host;

	undef $ref_printed;
	undef $ip_printed;
	undef $host_printed;

	undef $ref_check;
	undef $ip_check;
	undef $host_check;

	foreach $line (@data)
	{
		chomp($line);
		($referrer,$ip,$host) = split(/ /,$line);

		$ref_check = "$ref_check $referrer";
		$ip_check = "$ip_check $ip";
		$host_check = "$host_check $host";
	}
	
	foreach $line (@data)
	{
		chomp($line);
		($referrer,$ip,$host) = split(/ /,$line);

		$referrer{$referrer} = ($ref_check =~ s/$referrer/$referrer/g);

		$ip{$ip} = ($ip_check =~ s/$ip/$ip/g);	

		$host{$host} = ($host_check =~ s/$host/$host/g);	
	}
	
	$clicks = @data;

	&get_exposures;
	
	if ($exposures > 0)
	{
		$ratio = ($clicks / $exposures);
	}

	$ratio = sprintf "%.2f", ($ratio);
}

sub build_ad_log
{
	open(ADLOG,">$log_dir/$id.htm") || &cgiError ("Error Writing: $log_dir/$id.htm", "$!");
	flock(ADLOG,2);
	
	&print_header;
	
	print ADLOG qq~
	<center><table border="2" cellpadding="5" cellspacing="0" width="98%" bordercolor="#808080">
	<tr><td colspan="6" bgcolor="#000080"><font color="#FFFFFF"><b>Perl N' JavaScript Banners :: Banner Statistics :: Banner $id :: $time</b></font></td></tr>
	<tr><td width="25" bgcolor="#C0C0C0"><b><u>Banner</u></b></td><td width="15" bgcolor="#C0C0C0"><b><u>Weight</u></b></td><td width="15" bgcolor="#C0C0C0"><b><u>Views</u></b></td><td width="15" bgcolor="#C0C0C0"><b><u>Clicks</u></b></td><td width="15" bgcolor="#C0C0C0"><b><u>CTR</u></b></td><td width="10" bgcolor="#C0C0C0"><b><u>Options</u></b></td></tr>
	<tr><td>Banner $id ($img)</td><td>$weight</td><td>$exposures</td><td>$clicks</td><td>$ratio %</td><td><a href="$admin_script?action=view&amp;view=$id">View</a> <a href="$admin_script?action=modify&amp;modify=$id">Modify</a> <a href="$admin_script?action=delete&amp;delete=$id">Remove</a></td></tr>
	<tr><td colspan="6" bgcolor="#000080"><font color="#FFFFFF"><b>Referrer Log</b></font></td></tr>
	<tr><td colspan="5" bgcolor="#C0C0C0"><b><u>Referrer Url</u></b></td><td bgcolor="#C0C0C0"><b><u>Total Referrals</u></b></td></tr>
	~;
	
	foreach $key (keys %referrer)
	{
		if ($ref_printed =~ /$key/)
		{
			$print = "no";
		}
		
		else
		{
			print ADLOG qq|<tr><td colspan="5"><a href="$key">$key</a></td><td>$referrer{$key}</td></tr>\n|; 
		}
		
		$ref_printed .= " $key";
	}
	
	print ADLOG qq~
	<tr><td colspan="6" bgcolor="#000080"><font color="#FFFFFF"><b>VisitorLog</b></font></td></tr>
	<tr><td colspan="5" bgcolor="#C0C0C0"><b><u>Visitor IpAddress</u></b></td><td bgcolor="#C0C0C0"><b><u>Total Click-Throughs</u></b></td></tr>
	~;
	
	foreach $key (keys %ip)
	{
		if ($ip_printed =~ /$key/)
		{
			$print = "no";
		}
		
		else
		{
			print ADLOG qq|<tr><td colspan="5">$key</td><td>$ip{$key}</td></tr>\n|;
		}
		
		$ip_printed .= " $key";
	}
	
	print ADLOG qq~
	<tr><td colspan="6" bgcolor="#000080"><font color="#FFFFFF"><b>Host Log</b></font></td></tr>
	<tr><td colspan="5" bgcolor="#C0C0C0"><b><u>Host Ip Address</u></b></td><td bgcolor="#C0C0C0"><b><u>Total Click-Throughs</u></b></td></tr>
	~;
	
	foreach $key (keys %host)
	{
		if ($host_printed =~ /$key/)
		{
			$print = "no";
		}
		
		else
		{
			print ADLOG qq|<tr><td colspan="5">$key</td><td>$host{$key}</td></tr>\n|;
		}
		
		$host_printed .= " $key";
	}

	print ADLOG "</table></center>\n\n";

	&print_footer;

	flock(ADLOG,8);
	close(ADLOG);
}

sub build_index
{
	open(ADLOG,">$log_dir/index.htm") || &cgiError ("Error Writing: $log_dir/index.htm", "$!");
	flock(ADLOG,2);

	&print_header;
	
	print ADLOG qq~
	<center><table border="2" cellpadding="5" cellspacing="0" width="98%" bordercolor="#808080">
	<tr><td colspan="6" bgcolor="#000080"><font color="#FFFFFF"><strong>Perl N' JavaScript Banners :: Banner Statistics :: $time</strong></font></td></tr>
	<tr><td width="25" bgcolor="#C0C0C0"><strong><u>Banner</u></strong></td><td width="15" bgcolor="#C0C0C0"><strong><u>Weight</u></strong></td><td width="15" bgcolor="#C0C0C0"><strong><u>Views</u></strong></td><td width="15" bgcolor="#C0C0C0"><strong><u>Clicks</u></strong></td><td width="15" bgcolor="#C0C0C0"><strong><u>CTR</u></strong></td><td width="10" bgcolor="#C0C0C0"><strong><u>Options</u></strong></td></tr>
	~;
	
	foreach $line (@banners)
	{
		chomp($line);
		($id,$img,$border,$width,$height,$alt,$url,$weight,$exposures,$clicks,$ratio) = split(/\|\|/,$line);

		print ADLOG qq|<tr><td><a href="$id.htm">Banner $id</a> ($img)</td><td>$weight</td><td>$exposures</td><td>$clicks</td><td>$ratio %</td><td><a href="$admin_script?action=view&view=$id">View</a> <a href="$admin_script?action=modify&modify=$id">Modify</a> <a href="$admin_script?action=delete&delete=$id">Remove</a></td></tr>|;
	}
	
	print ADLOG "</table></center>\n\n";

	&print_footer;

	flock(ADLOG,8);
	close(ADLOG);
}

sub print_header
{
	print ADLOG qq|<html><head><title>Ad Log</title></head><body>|;
}

sub print_footer
{
	print ADLOG qq|<br><br><center><font size="-1">Powered by Virtual Visions Perl N' Javascript Banners. Copyright &copy; 1999 by <a href="http://www.feartech.com/vv">Virtual Visions</a>. All rights Reserved.</font></center><br><br></body></html>|;
}

sub time
{
	($sec, $min, $hr, $day, $mon, $yr, $weekday) = (localtime(time))[0,1,2,3,4,5,6];

	@months = ('January','February','March','April','May','June','July','August','September','October','November','December');
	@weekdays = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
	
	if ($sec < 10) { $sec = "0$sec"; }
	if ($min < 10) { $min = "0$min"; }
	if ($hr < 12) { $mn = "AM"; }
	if ($hr > 12) { $hr = ($hr - 12); $mn = "PM"; }
	if ($day < 10) { $day = "0$day"; }

	if ($yr > 99)
	{
		$yr-=100;

		if ($yr < 10) { $yr = "200$yr"; }
		elsif ($yr >= 10 && $yr < 100) { $yr = "20$yr"; }
		else { $yr = "2$yr"; }
	}

	else 
	{
		if ($yr < 10) { $yr = "190$yr"; }
		else { $yr = "19$yr"; }
	}

	$time = "$weekdays[$weekday] $months[$mon] $day $yr at $hr:$min:$sec $mn";
}

sub cgiError
{
	my ($error_cause,$error) = @_;

	if ($error_cause eq "") { $error_cause = "Error:"; }
	if ($error eq "") { $error = "The script encountered problems and terminated"; }

	print "Content-type: text/html\n\n";
	print "<h3>$error_cause</h3>$error";

	exit;
}