###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# about.pl 	      	                                                      #
# v0.9.9 - Requin                                                             #
#                                                                             #
# Copyright (C) 2002 by Carter (carter@mcarterbrown.com)                      #
# Added by Shawn Raloff                                                       #
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


############### 
sub about { 
############### 
$navbar = " $btn{'014'} $nav{'091'}"; 
print_top(); 
print qq~
<BR>
~;

	open(FILE, "$datadir/aboutinfo.txt");
	file_lock(FILE);
	chomp(@lines = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	$welcometitle = showhtml("$lines[0]");
	$welcomebody = showhtml("$lines[1]");

print qq~
<p class="texttitle">$welcometitle</p>
$welcomebody<br>
<br><br>

~; 
print_bottom(); 
exit; 
} 


if (-e "$scriptdir/user-lib/about.pl") {require "$scriptdir/user-lib/about.pl"} 

1; # return true 