#---------------------------------------------------------
#  Subroutine:   print_top
#  Written By:   Ted Loomos
#  Description:  Modified for Menu Manager Mod
#                Get the latest updates from www.devdesk.com
#
#  Revision History:
#  2002-08-31  Script Created
#---------------------------------------------------------
sub print_top {
###############
	require "$scriptdir/config.pl";
	require "$sourcedir/plugins.pl";
	require "$themesdir/$usertheme/theme.pl";
	require "$scriptdir/user-lib/themes/theme.pl"; getvars();
	require "$themesdir/$usertheme/header.pl";
}

1;