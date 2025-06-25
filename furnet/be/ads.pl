#!/usr/bin/perl

############################################
##                                        ##
##       WebAdverts (Configuration)       ##
##           by Darryl Burgdorf           ##
##       (e-mail burgdorf@awsd.com)       ##
##                                        ##
##             version:  2.02             ##
##         last modified: 6/25/99         ##
##           copyright (c) 1999           ##
##                                        ##
##    latest version is available from    ##
##        http://awsd.com/scripts/        ##
##                                        ##
############################################

# The following variables should be set to define the locations
# and URLs of various files, as explained in the documentation.

require "/home/erenetw/public_html/furnet/be/ads_display.pl";

$adverts_dir = "/home/erenetw/public_html/furnet/be/ads";
$display_cgi = "http://www.erenetwork.com/furnet/be/ads.pl";

$advertzone = "";

$ADVUseLocking = 1;
$ADVLogIP = 1;
$DupViewTime = 3600;

$DefaultBanner = "";

# $Ztext = "";
# $Zalt = "";
# $Ztarget = "";
# $Zwidth = "";
# $Zheight = "";
# $Zborder = "";

$ExchangeName = "";
$ExchangeURL = "";
$ExchangeLogo = "";
$ExchangeLogoWidth = 40;
$ExchangeLogoHeight = 40;

# NOTHING BELOW THIS LINE NEEDS TO BE ALTERED!

$ADVQuery = $ENV{'QUERY_STRING'};
&ADVsetup;

reset 'A-Za-z';
exit;

