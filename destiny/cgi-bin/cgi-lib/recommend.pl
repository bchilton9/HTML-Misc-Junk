###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# recommend.pl                                               		      #
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


###############
sub recommend {
###############
#KLAUS
	if ($username ne $anonuser && $username){ 
	open(FILE, "$memberdir/$username.dat") || error("$err{'010'}");
	file_lock(FILE);
	chomp(@member = <FILE>);
	unfile_lock(FILE);
	close(FILE);
	$membername = "$member[1]";
	$email = "$member[2]";
	} else { $membername = ""; $email = "";}
	$navbar = "$btn{'014'} $nav{'008'}";
	print_top();
	print qq~<form method="post" action="$cgi?action=recommend2">
<table border="0" cellspacing="1">
<tr>
<td><b>$msg{'060'}</b></td>
<td><input type="text" name="sender_name" size="25" value="$membername"></td>
</tr>
<tr>
<td><b>$msg{'061'}</b></td>
<td><input type="text" name="sender_email" size="25" value="$email"></td>
</tr>
<tr>
<td><b>$msg{'062'}</b></td>
<td><input type="text" name="recip_name" size="25" value=""></td>
</tr>
<tr>
<td><b>$msg{'063'}</b></td>
<td><input type="text" name="recip" size="25" value=""></td>
</tr>
<tr>
<td><b>$nav{'036'}</b></td>
<td> <textarea name="my_message" wrap=virtual rows=5 cols=35></TEXTAREA>
<BR><B>$msg{'175'}</B>
<BR>$msg{'062'}<BR>$username $inf{'012'}</td>
</tr>
<tr>
<td colspan="2"><input type="submit" value="$btn{'005'}"></td>
</tr>
</table>
</form>
~;
#KLAUS
	print_bottom();
	exit;
}

################
sub recommend2 {
################
	$sender_name = $input{'sender_name'};
	if ($input{'sender_name'} eq "") { $sender_name = "$anonuser"; }
	$sender_email  = $input{'sender_email'};
	$recip_name  = $input{'recip_name'};
	$recip_email = $input{'recip'};

	if ($sender_email eq "") { error ("$err{'005'}"); }
	if ($recip_name eq "") { error ("$err{'017'}"); }
	if ($recip_email eq "") { error ("$err{'018'}"); }

	$subject = "$inf{'010'}: $pagename";
	$message = qq~$recip_name,
	$input{'my_message'}
	$sender_name 
	$inf{'012'}
	~;

	sendemail($recip_email, $subject, $message, $sender_email);

	open (LOG,">>$datadir/recommend.log");
  	print LOG"$date|$ENV{'REMOTE_ADDR'}|$sender_name|$sender_email|$recip_name|$recip_email\n";
 	close(LOG);

	$navbar = "$btn{'014'} $nav{'008'}";
	print_top();
	print qq~$inf{'013'} <b>$recip_name ($recip_email)</b><br>
$inf{'014'}
~;
	print_bottom();
	exit;
}

if (-e "$scriptdir/user-lib/recommend.pl") {require "$scriptdir/user-lib/recommend.pl"} 

1; # return true

