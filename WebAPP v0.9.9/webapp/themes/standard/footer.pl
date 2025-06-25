###############################################################################
###############################################################################
# footer.pl - prints the middle/bottom of each page                           #
# v0.9.7                                                                      #
# Copyright (C) 2001 by WebAPP ( webapp@attbi.com )                		#
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
# Last modified: 07/24/02                                                     #
###############################################################################
###############################################################################


	print qq~
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>

<!--

<td valign="top" width="150">
<table width="150">
<tr>
<td>

-->

<tr>
<td>
~;
	

	print qq~</td>
</tr>
<tr>
<td>

~;

	print qq~</td>
</tr>
</table>
</td>
</tr>
</table>
</div>
~;

mycontent_block2(); 

print qq~

<div align="center">
<table class="pagetable">
    <tr> 
      <td height="21">~;
menu_bar();
      print qq~</td>
    </tr>
    <tr> 
     <td>~;
about_bar();
print qq~</div>
<div align="center">~;
wepapp_bar();
print qq~</div>

</html>
~;


1; # return true


