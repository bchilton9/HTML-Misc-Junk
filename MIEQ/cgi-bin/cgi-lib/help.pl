###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# help.pl                                         		                  #
# v0.9.9 - Requin                                                             #
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
# File: Last modified: 08/01/02                                               #
###############################################################################
###############################################################################

#
#
#  		Code Shell Written by:  Vladimir Babynin <bob@mail.ru>
#
#

############### 
sub help { 
############### 
$database="$datadir/help/data.txt";
open (ORGDB,"<$database");
@ODB=<ORGDB>;
close (ORGDB);

$navbar = " $btn{'014'} $nav{'090'}"; 
print_top();
print "
<table width='100%' border='0'>
<tr><td class='texttitle'>$help{'011'}</td></tr>
<tr><td><hr noshade='noshade' size='1' width='100%'></td></tr>
";
foreach $rec (@ODB){
	chomp($rec);
	($helpq,$helpa)=split(/\|/,$rec);
		$message=$helpa;
		if ($enable_ubbc) { doubbc(); }
		if ($enable_smile) { dosmilies(); }
print qq~
<tr><td><b>$helpq<b></td></tr>
<td>$message</td></tr>
<tr><td>&nbsp;</td></tr>\n
~;
}
print qq~
</table>
~;

print_bottom();
exit; 
} 

if (-e "$scriptdir/user-lib/help.pl") {require "$scriptdir/user-lib/help.pl"} 

1; # return true 



