#!/usr/bin/perl

############################################
##                                        ##
##        WebAdverts L-C Converter        ##
##           by Darryl Burgdorf           ##
##       (e-mail burgdorf@awsd.com)       ##
##                                        ##
############################################

# Unlike earlier versions of WebAdverts, version 1.60 expects
# (and requires) that account names consist of lower-case
# characters.  This script will convert your existing accounts
# and data files to conform to the new requirement.  Simply
# assign the $adverts_dir variable as in your configuration
# scripts and run the program.  (To ensure there are no file
# conflicts, disable your banner rotation before running the
# name converter.)

$adverts_dir = "/home/erenetw/public_html/furnet/be/ads";

# NOTHING BELOW THIS LINE NEEDS TO BE ALTERED!

open (ADVLIST, "+<$adverts_dir/adlist.txt");
@adverts = <ADVLIST>;
seek (ADVLIST,0,0);
foreach $advert (@adverts) {
	chop ($advert) if ($advert =~ /\n$/);
	$newadvert = $advert;
	$newadvert =~ s/[^\w_-]//g;
	$newadvert =~ tr/A-Z/a-z/;
	unless ($newadvert eq $advert) {
		if (-e "$adverts_dir/$advert.txt") {
			rename ("$adverts_dir/$advert.txt",
			  "$adverts_dir/$newadvert.txt");
		}
		if (-e "$adverts_dir/$advert.log") {
			rename ("$adverts_dir/$advert.log",
			  "$adverts_dir/$newadvert.log");
		}
		if (-e "$adverts_dir/$advert.ips") {
			rename ("$adverts_dir/$advert.ips",
			  "$adverts_dir/$newadvert.ips");
		}
	}
	print ADVLIST "$newadvert\n";
}
truncate (ADVLIST, tell(ADVLIST));
close (ADVLIST);

open (GRPLIST, "+<$adverts_dir/groups.txt");
@groups = <GRPLIST>;
seek (GRPLIST,0,0);
foreach $group (@groups) {
	chop ($group) if ($group =~ /\n$/);
	$newgroup = $group;
	$newgroup =~ s/[^\w_-]//g;
	$newgroup =~ tr/A-Z/a-z/;
	unless ($newgroup eq $group) {
		if (-e "$adverts_dir/$group.grp") {
			rename ("$adverts_dir/$group.grp",
			  "$adverts_dir/$newgroup.grp");
		}
	}
	print GRPLIST "$newgroup\n";
}
truncate (GRPLIST, tell(GRPLIST));
close (GRPLIST);
