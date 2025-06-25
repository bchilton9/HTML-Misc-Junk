###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# whosonline.pl         			                                    #
# v0.9.9 - Requin                                                             #
# Copyright (C) 2002 by WebAPP (webapp@attbi.com)                             #
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
# File: Last modified: 08/01/02                                               #
###############################################################################
###############################################################################


############# 
sub readwho {
#############

	if ($username eq "$anonuser") {error('noguests');}

	$navbar = "$btn{'014'} $msg{'255'}";	
	print_top();
	print qq~<table width="100%" bgcolor="$titlebg" border="0" cellspacing="0" cellpadding="0">
<tr>
<td>
<table width="100%" border="0" cellspacing="1" cellpadding="2">
<tr>
<td bgcolor="$windowbg"><b>$msg{'263'}</b></td>

</tr>
~;

	if (@entries == 0) {
		print qq~<tr>
<td colspan="1" bgcolor="$windowbg2">$msg{'268'}</td>
</tr>
~;
		
	}

	elsif (@entries != 0) {
		print qq~<tr>
<td colspan="1" bgcolor="$windowbg2">
~;

	$guests = 0;	

	open(LOG, "$datadir/log.dat");
	file_lock(LOG);
	chomp(@entries = <LOG>);
	unfile_lock(LOG);
	close(LOG);

	$howmany = 0;

	foreach $curentry (@entries) {

		($name, $value) = split(/\|/, $curentry);

if ($name ne "admin2") {
		if($name =~ /\./) { ++$guests } 
		else {

		$howmany++;
		if ($howmany > 1) { print ", "; }

			open(FILE, "$memberdir/$name.dat");
			file_lock(FILE);
			chomp(@msettings = <FILE>);
			unfile_lock(FILE);
			close(FILE);


		$whoonline = qq~<a href="$pageurl/$cgi?action=viewprofile&amp;username=$name" class="menu">$msettings[1]</a>~; 	
		print "$whoonline";

		}

}
			
		}	

print qq~
<br>$msg{'344'} $guests $msg{'276'}.</td></tr>
~;
}
	print qq~</table>
</td>
</tr>
</table>
<br>

~;

	print_bottom();
	exit;

}

if (-e "$scriptdir/user-lib/whosonline.pl") {require "$scriptdir/user-lib/whosonline.pl"} 

1; # return true
