###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# emailer.pl                                           			      #
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

############
sub sendto {
############
$guestapproval = "0";
$approvedemail = "0";

if ($info{'sendto'} eq "CompanyEmail") {$guestapproval = "1"; $approvedemail = "1";}
if ($info{'sendto'} eq "WebmasterEmail") {$guestapproval = "1"; $approvedemail = "2";}

if ($username eq "$anonuser" && $guestapproval eq "0") { error("$err{'011'}"); }
if ($username ne "$anonuser") {$guestapproval = "0";}
if ($approvedemail eq "0") {$approvedemail = "$info{'sendto'}";}

	$navbar = "$btn{'014'} $msg{'394'}";
	print_top();
	print qq~
	<table border="0" width="100%" cellpading="1" cellspacing="3">
	<form action="$cgi?action=sendto2" method="post">
	<tr>
	<td>
	~;
	
	if ($guestapproval eq "1") {print qq~
	<b>$msg{'007'}</b><br>~;
	if ($approvedemail eq "1") {print qq~$compname~;}
	if ($approvedemail eq "2") {print qq~$pagename $root~;}
	print qq~<input type="hidden" name="recipemail" value="$approvedemail">~;
	} else {print qq~
	<b>$msg{'007'}</b><br>~;
	if ($approvedemail eq "0") {print qq~$info{'sendto'}~;}
	if ($approvedemail eq "1") {print qq~$compname~;}
	if ($approvedemail eq "2") {print qq~$pagename $root~;}
	print qq~
	<input type="hidden" name="recipemail" value="$approvedemail">~;}
	
	print qq~
	</td>
	</tr>
	<tr>
	<td>
	~;

	if ($guestapproval eq "1") {print qq~
	<b>$msg{'182'}</b><br><input type="text" name="senderemail" size="40">
	~;
	} else {print qq~
	<b>$msg{'182'}</b><br>$username<input type="hidden" name="senderemail" value="$username">
	~;}	

	print qq~
	</td>
	</tr>
	<tr>
	<td>
	<b>$msg{'395'}</b><br>
	<input type="text" name="subject" value="$subject" size="40">
	</td>
	</tr>
	<tr>
	<td>
	<b>$msg{'396'}</b><br>
	<textarea name="message" cols="40" rows="10">$message</textarea>
	</td>
	</tr>
	<tr>
	<td><input type="submit" class="button" value="$btn{'005'}">&nbsp;&nbsp;<input type="reset" class="button" value="$btn{'009'}"></td>
	</tr>
	</table>
	</form>
~;
	print_bottom();
	exit;
}

#############
sub sendto2 {
#############
	if ($username eq "$anonuser" && $guestapproval eq "0")  { error("$err{'011'}"); }
	error("$err{'014'}") unless ($input{'subject'});
	error("$err{'015'}") unless ($input{'message'});
	
	if ($guestapproval eq "1") {
	error("$err{'005'}") unless ($input{'senderemail'});
	}

		chomp($input{'subject'});
		chomp($input{'message'});

		$foot = "\n\nThis E-mail was sent via $baseurl";

		$mailsubject = convert_newsletter($input{'subject'});
		$mailmessage = convert_newsletter($input{'message'}).$foot;

			# Getting the Senders E-mail Address
			$emailersender = "";
			$emailerrecip = "";
			
 			if ($input{'recipemail'} eq "1") {
			$emailerrecip = $compemail; }
			
			if ($input{'recipemail'} eq "2") {
			$emailerrecip = $webmaster_email; }
			
			if ($emailerrecip eq "") {
			open(FILE, "$memberdir/$input{'recipemail'}.dat") || error("$err{'001'} $memberdir/$input{'recipemail'}.dat"); 
			file_lock(FILE); 
			chomp(@sendingto = <FILE>); 
			unfile_lock(FILE); 
			close(FILE);
			
			$emailerrecip = $sendingto[2];
			}						
			
			if ($input{'senderemail'} eq "$username") {
			open(FILE, "$memberdir/$username.dat") || error("$err{'001'} $memberdir/$username.dat"); 
			file_lock(FILE); 
			chomp(@usermail = <FILE>); 
			unfile_lock(FILE);
			close(FILE); 
			
			$emailersender = $usermail[2];
			} else {
			$emailersender = $input{'senderemail'};
			}
				
		sendemail($emailerrecip, $mailsubject, $mailmessage, $emailersender);

	$navbar = "$btn{'014'} $msg{'394'}";
	print_top();
	print qq~
	<br>$msg{'166'}. $msg{'398'}<br><br>
	<a href="$cgi?action=" class="link">$nav{'002'}</a><br><br>
~;
	print_bottom();
	exit;

}

if (-e "$scriptdir/user-lib/emailer.pl") {require "$scriptdir/user-lib/emailer.pl"} 

1;

