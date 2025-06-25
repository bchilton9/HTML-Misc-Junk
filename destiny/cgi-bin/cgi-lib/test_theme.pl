
###############################################################################
# Sub-Routines                                                                #
# for the use with PerlPort and WebAPP (and maybe YaWPS ?)                    #
#                                                                             #
# Copyright (C) 2004 by ABYWN  webapp@abywn.de                                #
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
# Last modified: Dec 28 2004 by Jos - open new window, local image load,      #
# and line breaks                                                             #
###############################################################################
###############################################################################

###< (c) abwyn >####
sub test_theme {
####################

	if (!defined $info{'right'}) { $info{'right'} = ""; }

	$navbar = " $btn{'014'} $nav{'091'}";

    if ($info{'right'} ne "") {
        print_top();

            print qq~ 
                <p align=left>
                    <BR><BR><BR><BR>
                    <a href="http://validator.w3.org/check?uri=referer" target="_blank">
                    CHECK HTML <BR><BR>
                    <img border="0" src="$imagesurl/valid-html401.gif"
                    alt="Valid HTML 4.01!" height="31" width="88"></a>
                    <BR><BR>
                    <A HREF="$pageurl/$cgi?action=test_theme&amp;right=">TEST WITH FOOTER</A>
                    <BR><BR>
                </p>
            ~;

			newsheader(); # closes nav_bar
        print_poll();
    } else { 
        print_top();

            print qq~ 
                <p align=left>
                    <BR><BR><BR><BR>
                    <a href="http://validator.w3.org/check?uri=referer" target="_blank">
                    CHECK HTML <BR><BR>
                    <img border="0" src="$imagesurl/valid-html401.gif"
                    alt="Valid HTML 4.01!" height="31" width="88"></a>
                    <BR><BR>
                    <A HREF="$pageurl/$cgi?action=test_theme&amp;right=on">TEST WITH POLLFOOTER</A>
                    <BR><BR>
                </p>
            ~;

        print_bottom();
    }
}

if (-e "$scriptdir/user-lib/test_theme.pl") { require "$scriptdir/user-lib/test_theme.pl" }

1;
