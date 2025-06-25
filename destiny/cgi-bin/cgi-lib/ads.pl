###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# ads.pl 									                  #
# v0.9.9 - Requin   										#
#                                                                             #
# Copyright (C) 2002 by Carter (carter@mcarterbrown.com)                      #
#                                                                             #
# This program is free software; you can redistribute it and/or               #
# modify it under the terms of the GNU General Public License                 #
# as published by the Free Software Foundation; either version 2              #
# of the License, or (at your option) any later version.                      #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program; if not, write to the Free Software                 #
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA. #
#                                                                             #
#                                                                             #
# File: Last modified: 03/26/03                                               #
###############################################################################
###############################################################################


$adfile = "$datadir/banners/data.txt";	  

#################
sub OutputJava {
#################

	open(FILE, $adfile) || die "Can't open $adfile";
	@rotation_info = <FILE>;
	close(FILE);
	
	srand(time|$$);

	$banner_info = $rotation_info[int(rand(@rotation_info))];
	chomp($banner_info); 

	
	($banurl,$iban,$iw,$ih,$alt,$hits) = split(/\|/, $banner_info);

	$banurl =~ s/\=/EQSIGN/g;
	$banurl =~ s/\?/QMSIGN/g;
	$banurl =~ s/\"/DQUOTE/g;
	$banurl =~ s/\'/SQUOTE/g;
	$banurl =~ s/\&/AMPSIGN/g;


	print qq~<center>$banner{'001'}<br><a href="$pageurl/$cgi?action=bannerredirect&banurl=$banurl&iban=$iban" target="_blank" class="bannerlink"><img src="$iban" width="$iw" height="$ih" alt="$alt" border="0"><br>$alt</a></center>~;

}

####################
sub bannerredirect {
####################
$adfile = "$datadir/banners/data.txt";	

	getcgi();

	$info{'banurl'} =~ s/EQSIGN/\=/g;
	$info{'banurl'} =~ s/QMSIGN/\?/g;
	$info{'banurl'} =~ s/DQUOTE/\"/g;
	$info{'banurl'} =~ s/SQUOTE/\'/g;
	$info{'banurl'} =~ s/AMPSIGN/\&/g;

	open(FILE, $adfile) || die "Can't open $adfile";
	file_lock(FILE);
	chomp(@datas = <FILE>);
	unfile_lock(FILE);
	close(FILE);
	

	
	open(FILE, ">$adfile");
	file_lock(FILE);



	foreach $data (@datas) {
	($banurl,$iban,$iw,$ih,$alt,$hits)=split(/\|/, $data);

		if ($info{'banurl'} eq $banurl && $info{'iban'} eq $iban) {
			$myurl = $banurl;	
			$hits_temp = $hits + 1;
			print FILE "$banurl|$iban|$iw|$ih|$alt|$hits_temp\n";
			}

	else {
		print FILE "$data\n";
		}
	

	}

	unfile_lock(FILE);
	close(FILE);

	


print "Location: $myurl\n\n";

}


if (-e "$scriptdir/user-lib/ads.pl") {require "$scriptdir/user-lib/ads.pl"} 

1;

