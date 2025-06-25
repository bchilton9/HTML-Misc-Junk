###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# my_XXXXX.lng - the language file for your own additions                     #
# for the use with WebAPP and YaWPS and PerlPort                              #
#                                                                             #
# Copyright (C) 2002 by ABYWN  webapp@abywn.de                                #
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
# File: english.lng, Last modified: 07/23/02	                              #
###############################################################################
###############################################################################
#_<abwyn>______________________________________________________________________
#
# first of all you need to add the following 3 lines (without the #-sign of course)
# into all of your regular languagefiles.
# Add it in the very end right before the line with the 1;
#_______________________________________________________________________</abwyn>
#
#if (-e "$langdir/my_${langgfx}.pl") {require "$langdir/my_${langgfx}.pl"}
#elsif (-e "$langdir/my_${langgfx}.pl") {require "$langdir/my_${langgfx}.pl"}
#elsif (-e "$langdir/my_english.pl") {require "$langdir/my_english.pl"}

#_____________________________________________________________________________
@GENDER = qw(Female Male);
@MARSTAT= qw(Single Married Divorced none_of_your_business);
@PROFESSION = qw(Executive Admin Financial Artistic Managerial Clerical Secretarial Science Engineering Technical Teaching Law Medical Athletic Entrep Retired Student Other);
# ____________________________________________________________________________
# if you need entries including blankspaces you would have to
# use the explicit quoting like for example
# @GENDER = ("Female", "Male");
# @MARSTAT= ("Married", "Single", "Single and Looking",  "Divorced");
# ____________________________________________________________________________

# ____________________________________________________________________________
# this is very useful for a lot of stuff
$words{'000'} = "Add";
$words{'001'} = "Edit";
$words{'002'} = "Copy";
$words{'003'} = "Paste";
$words{'004'} = "Move";
$words{'005'} = "Cut";
$words{'006'} = "Delete";
$words{'007'} = "Modify";
$words{'008'} = "View";
$words{'009'} = "Choose";
$words{'010'} = "aktive";
$words{'011'} = "Check";
$words{'012'} = "Uncheck";
$words{'013'} = "Change";
$words{'014'} = "Lock";
$words{'015'} = "Unlock";
$words{'016'} = "Open";
$words{'017'} = "Close";
$words{'018'} = "Newest"; 
$words{'019'} = "Oldest";
$words{'020'} = "Reset";
$words{'021'} = "Userdata";
$words{'022'} = "Disclaimer";
$words{'023'} = "User Agreement";
$words{'024'} = "Other";
$words{'025'} = "Groups ";
$words{'026'} = "Profile";
$words{'027'} = "All";
$words{'028'} = "None";
$words{'029'} = "Some";
$words{'030'} = "Extended";
$words{'031'} = "Always";
$words{'032'} = "Never";
$words{'033'} = "User Choice";
$words{'034'} = "Top";
$words{'035'} = "Bottom";
$words{'036'} = "Block";
$words{'037'} = "On";
$words{'038'} = "Off";
$words{'039'} = "Toggle";
$words{'040'} = "Left";
$words{'041'} = "Right";
$words{'042'} = "Center";
$words{'043'} = "Read";
$words{'044'} = "Write";
$words{'045'} = "";
$words{'046'} = "Most read";
$words{'047'} = "Most commented";
$words{'048'} = "Most used";
$words{'049'} = "Stick"; # to stick
$words{'050'} = "Unstick"; # to unstick
$words{'060'} = "User";
$words{'061'} = "Netiquette";
$words{'062'} = "Recycled";
$words{'063'} = "just for";
$words{'064'} = "How to get here";

$words{'069'} = "Cite:";
$words{'070'} = "";
$words{'071'} = "IMPRESSUM";
$words{'072'} = "Link";
$words{'073'} = "Download";
$words{'074'} = "Board";
$words{'075'} = "Category";
$words{'076'} = "Order/Rank";
$words{'077'} = "Goto";
$words{'078'} = "";
$words{'079'} = "";
$words{'080'} = "Right";
$words{'081'} = "Left";
$words{'082'} = "Top";
$words{'083'} = "Bottom";
$words{'084'} = "Front";
$words{'085'} = "Back";
$words{'086'} = "";
$words{'087'} = "";
$words{'088'} = "";
$words{'089'} = "";
$words{'090'} = "";
$words{'091'} = "seconds";
$words{'092'} = "minutes";
$words{'093'} = "hours";
$words{'094'} = "days";
$words{'095'} = "weeks";
$words{'096'} = "months";
$words{'097'} = "years";
$words{'098'} = "";
$words{'099'} = "";
$words{'100'} = "";
$words{'111'} = "updated";
$words{'112'} = "edited";
$words{'113'} = "deleted";
$words{'114'} = "created";
$words{'115'} = "read";
$words{'116'} = "";
$words{'117'} = "";

$text{'045'} = "Read Instant-Message";

$text{'062'} = "Code was copied to the clipboard";
$text{'063'} = "Last entry posted by:";
$text{'064'} = "Sort:";
$text{'065'} = "up (A-Z)";
$text{'066'} = "down (Z-A)";
$text{'067'} = "Newest first";
$text{'068'} = "oldest first";
$text{'069'} = "days old";
$text{'070'} = "Please click here To read the full Article!";
$text{'071'} = "Refresh database. (Warning: This might take a little longer)";
$text{'072'} = "About this Web";
$text{'073'} = "Sorry to say but there is no description available for this entry. Please contact the sender of this entry and kindly ask him to edit this entry.";
$text{'074'} = "(Access restricted: <b>NO</b> access for you: $username)";
$text{'075'} = "(Access restricted: access for you: $username <b>approved</b> )";

$err{'070'} = "Sorry but you are looking in the wrong board. Maybe the thread has been moved. You can either use the search or contact one of the Admins for Information about this thread.";

$msg{'lock'} = "Lock Thread";
$msg{'unlock'} = "Unlock Thread";
# ____________________________________________________________________________

$im{'001'} = qq~This Message will be received, as soon as the recipient will
                come to this site again.
                ~; #
#_____________________________________________________________________________
# Site specific changes:
# if you are making any sitespecific changes, 
# it will be better to put them right here, so in case you need to update, 
# you will still keep your changes
#_____________________________________________________________________________




1; # return true

