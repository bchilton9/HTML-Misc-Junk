#!/usr/bin/perl

###################################################
#                                                 #
# Virtual Visions Ad Banner Rotation Script v1.70 #
# Copyright 1999 by Barracuda                     #
# Email - baracuda@feartech.com                   #
#                                                 #
###################################################

# this is the directory where you want your ad banner
# logs to be stored... chmod 777 this directory!

$log_dir = '/home/ere/public_html/cgi-bin/ban/data';

###################################################

use CGI qw(:standard);
$ads = new CGI;

$idnum = $ads->param('id');
$redirect = $ads->param('url');

###################################################

&log;
&redirect;

################
# sub routines #
################

sub log
{
	open (LOG,">>$log_dir$idnum.txt") || &redirect;
	flock(LOG,2);

	print LOG "$ENV{'HTTP_REFERER'} $ENV{'REMOTE_ADDR'} $ENV{'REMOTE_HOST'}\n";

	flock(LOG,8);
	close(LOG);
}

sub redirect
{
	$redirect = "http://$redirect";

	print "Location: $redirect\n\n";
}