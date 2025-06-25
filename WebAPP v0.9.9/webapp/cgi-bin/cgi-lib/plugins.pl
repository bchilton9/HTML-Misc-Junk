###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# plugins.pl 			                                                #
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

###############################################################################
###############################################################################
# About:                                                                      #
# The object of this file is to make the themes upwards compatible.           #
#                                                                             #
#                                                                             #
# There are Four sections:                                                    #
# left_top_plugins();                                                         #
# left_bottom_plugins();                                                      #
# right_top_plugins();                                                        #
# right_bottom_plugins();                                                     #
#                                                                             #
#                                                                             #
# This way the programmes can add code here, to add new sections to the themes#
# and not affect the themes themeselves.  Allowing users to keep customized   #
# themes, and keeping us from messing them up.                                #
#                                                                             #
#                                                                             #
# These are currently left blank intentionally...                             #
# Current Date: 07/24/02                                                      #
###############################################################################
###############################################################################


######################
sub left_top_plugins {
######################
# these blocks will be located below the main menu


}


#########################
sub left_bottom_plugins {
#########################
# These blocks will be located above the left blocks



}


#######################
sub right_top_plugins {
#######################
# These blocks are located below the poll

}


##########################
sub right_bottom_plugins {
##########################
# These blocks will be located above the info block

}

if (-e "$scriptdir/user-lib/plugins.pl") {require "$scriptdir/user-lib/plugins.pl"} 

1;

