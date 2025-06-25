###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# contact.pl                                                       	      #
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
sub contact { 
############### 
$navbar = " $btn{'014'} $nav{'092'}"; 
print_top(); 
print qq~ 
<table border="0" width="100%" cellpading="1" cellspacing="3">
<tr>
<td><b>$compname</b></td>
</tr>
<tr>
<td>$compadd<BR>
$compcity, $compstate  $compzip
</td>
</tr>
~;
if ($compphone ne "") {print qq~
<tr><td><img src="$imagesurl/phone.gif" width="16" height="14" border="0" alt="">&nbsp;$compphone</td></tr>~;}
if ($compfax ne "") {print qq~
<tr><td><img src="$imagesurl/fax.gif" width="16" height="14" border="0" alt="">&nbsp;$compfax</td></tr>~;}
print qq~
<tr>
<td>&nbsp;</td>
</tr>~;

if ($compemail ne "") {print qq~
<tr><td>
~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~$msg{'394'}&nbsp;$msg{'320'}&nbsp;<a href="$cgi?action=anonemail&sendto=CompanyEmail" class="link">$compname</a></td></tr>~;
} else {
print qq~
$msg{'538'}&nbsp;<a href="mailto:$compemail">$compemail</a></td></tr>~;}
}

if ($webmaster_email ne "") {print qq~
<tr><td>
~;
if ($hidemail eq "1" || $hidemail eq "") {
print qq~$msg{'394'}&nbsp;$msg{'320'}&nbsp;<a href="$cgi?action=anonemail&sendto=WebmasterEmail" class="link">$pagename&nbsp;$root</a></td></tr>~;
} else {
print qq~
$msg{'539'}&nbsp;<a href="mailto:$webmaster_email">$webmaster_email</a></td></tr>~;}
}

print qq~
</table>
~; 
print_bottom(); 
exit; 
} 

if (-e "$scriptdir/user-lib/contact.pl") {require "$scriptdir/user-lib/contact.pl"} 

1; # return true 