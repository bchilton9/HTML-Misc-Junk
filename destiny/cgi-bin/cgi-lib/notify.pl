###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# notify.pl 						                              #
# v0.9.9 - Requin       									#
#                                                                             #
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
# File: Last modified: 10/30/02                                               #
###############################################################################
###############################################################################


##################
sub notify_users {
##################
	open(FILE, "$messagedir/$thread.mail");
	file_lock(FILE);
	@mails = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	foreach $curmail (@mails) {
		$curmail =~ s/[\n\r]//g;
		$notifysubject = "$msg{'683'} $subject";
		$notifymessage = qq~$inf{'016'} $pageurl/$forum$curboard&op=display&num=$thread   To be removed: $pageurl/$forum$curboard&op=notify_remove&num=$thread&email=$curmail ~;
		sendemail($curmail, $notifysubject, $notifymessage);
	}
}

############
sub notify {
############
	if ($username eq "$anonuser") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $nav{'003'} $btn{'014'} $boardname";
	print_top();
	print qq~$msg{'155'}<br>
<b><a href="$cgi?action=forum&amp;board=$currentboard&amp;op=notify2&amp;thread=$info{'thread'}">$nav{'047'}</a> - <a href="$cgi?action=forum&amp;board=$currentboard&amp;op=display&num=$info{'thread'}">$nav{'048'}</a></b>
~;
	print_bottom();
	exit;
}

#############
sub notify2 {
#############
	if ($username eq "$anonuser") { error("$err{'011'}"); }
	
	if ($info{'thread'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	open (FILE, "$messagedir/$info{'thread'}.mail");
	file_lock(FILE);
	chomp(@mails = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	open (FILE, ">$messagedir/$info{'thread'}.mail") || error("$err{'016'} $thread.mail");
	file_lock(FILE);
	print FILE "$settings[2]\n";
	foreach $curmail (@mails) {
		if($settings[2] ne "$curmail") { print FILE "$curmail\n"; }
	}
	unfile_lock(FILE);
	close(FILE);

print "Location: $cgi?action=forum\&board=$currentboard\&op=display\&num=$info{'thread'}\n\n";
	exit;
}

###################
sub notify_remove {
###################	
	if ($info{'num'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	open (FILE, "$messagedir/$info{'num'}.mail");
	file_lock(FILE);
	chomp(@mails = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	open (FILE, ">$messagedir/$info{'num'}.mail") || error("$err{'016'} $info{'num'}.mail");
	file_lock(FILE);

	foreach $curmail (@mails) {
		if($info{'email'} eq "$curmail") { print FILE ""; }
		else { print FILE "$curmail\n"; }
	}
	unfile_lock(FILE);
	close(FILE);

print "Location: $cgi?action=forum\&board=$currentboard\&op=notify_remove_success\n\n";
	exit;
}

###########################
sub notify_remove_success {
###########################

print_top();

print qq~<br><br>
<center><b>You have successfully been removed from this thread!</b></center>
<br><br>
~;
print_bottom();


exit;
}

#########################
sub notify_sticky_users {
#########################
	open(FILE, "$messagedir/$thread.mail");
	file_lock(FILE);
	@mails = <FILE>;
	unfile_lock(FILE);
	close(FILE);

	foreach $curmail (@mails) {
		$curmail =~ s/[\n\r]//g;
		$notifysubject = "$msg{'683'} $subject";
		$notifymessage = qq~$inf{'016'} $pageurl/$forum$curboard&op=display&num=$thread  To be removed: $pageurl/$forum$curboard&op=notify_remove&num=$thread&email=$curmail ~;
		sendemail($curmail, $notifysubject, $notifymessage);
	}
}

##################
sub notifysticky {
##################
	if ($username eq "$anonuser") { error("$err{'011'}"); }

	$navbar = "$btn{'014'} $nav{'003'} $btn{'014'} $boardname";
	print_top();
	print qq~$msg{'155'}<br>
<b><a href="$cgi?action=forum&amp;board=$currentboard&amp;op=notifysticky2&amp;thread=$info{'thread'}">$nav{'047'}</a> - <a href="$cgi?action=forum&amp;board=$currentboard&amp;op=display&num=$info{'thread'}">$nav{'048'}</a></b>
~;
	print_bottom();
	exit;
}

###################
sub notifysticky2 {
###################
	
	if ($username eq "$anonuser") { error("$err{'011'}"); }
	
	if ($info{'thread'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	if ($currentboard =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { print_top();  print "What are you doing Stan?"; print_bottom(); exit; }

	open (FILE, "$messagedir/$info{'thread'}.mail");
	file_lock(FILE);
	chomp(@mails = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	open (FILE, ">$messagedir/$info{'thread'}.mail") || error("$err{'016'} $thread.mail");
	file_lock(FILE);
	print FILE "$settings[2]\n";
	foreach $curmail (@mails) {
		if($settings[2] ne "$curmail") { print FILE "$curmail\n"; }
	}
	unfile_lock(FILE);
	close(FILE);

print "Location: $cgi?action=forum\&board=$currentboard\&op=displaysticky\&num=$info{'thread'}\n\n";
	exit;
}




if (-e "$scriptdir/user-lib/notify.pl") {require "$scriptdir/user-lib/notify.pl"} 

1; # return true

