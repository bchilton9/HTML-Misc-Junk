###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# block.pl                                                   		      #
# v0.9.9 - Requin                                                             #
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
# File: Last modified: 10/31/02                                               #
###############################################################################
###############################################################################

################
sub block_left {
################

	open(FILE, "$datadir/blocks/blockleft.dat");
	file_lock(FILE);
	chomp(@blockl = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	foreach $line (@blockl) {
		@item = split(/\|/, $line);

		# 0 = Anyone ---- 1 = members only
		if ($item[4] eq "0" || $item[4] eq "") {

		if ($item[2] eq 1) { print qq~<bgcolor = "$boxbgcolor">~;
	    $cont = &showblockhtml($item[3]);
			boxheader("$item[1]");
			print qq~<tr><td>$cont</td></tr>~;
			boxfooter();
		}
	}

		if ($item[4] eq "1" && $username ne "$anonuser") {

		if ($item[2] eq 1) { print qq~<bgcolor = "$boxbgcolor">~;
	    $cont = &showblockhtml($item[3]);
			boxheader("$item[1]");
			print qq~<tr><td>$cont</td></tr>~;
			boxfooter();
		}
	}

		else	{
			print qq~ ~;
			}
	}
}

################
sub block_right {
################

	open(FILE, "$datadir/blocks/blockright.dat");
	file_lock(FILE);
	chomp(@blockr = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	foreach $line (@blockr) {
		@item = split(/\|/, $line);

		# 0 = Anyone ---- 1 = members only
		if ($item[4] eq "0" || $item[4] eq "") {

		if ($item[2] eq 1) { print qq~<bgcolor = "$boxbgcolor">~;
     	$cont = &showblockhtml($item[3]);
			boxheader("$item[1]");
			print qq~<tr><td>$cont</td></tr>~;
			boxfooter();
		}
}

		if ($item[4] eq "1" && $username ne "$anonuser") {

		if ($item[2] eq 1) { print qq~<bgcolor = "$boxbgcolor">~;
     	$cont = &showblockhtml($item[3]);
			boxheader("$item[1]");
			print qq~<tr><td>$cont</td></tr>~;
			boxfooter();
		}
}
		else	{
			print qq~ ~;
			}
	}
}


###################
sub showblockhtml {
###################
	
my $text = shift;

if ($allow_html == 1) {

	$text =~ s/&amp;/&/g;
	$text =~ s/&quot;/"/g;
	$text =~ s/ \&nbsp;/  /g;
	$text =~ s/&lt;/</g;
	$text =~ s/&gt;/>/g;
	$text =~ s/ \&nbsp; \&nbsp; \&nbsp;/\t/g;
	$text =~ s/\n/<br>/g;
	$text =~ s/<pipe>/\|/g;

		$text =~ s~(\<|&lt;?)(.*?)color=([\w#]+)(\>|&gt;?)(.*?)(\<|&lt;?)/color(\>|&gt;?)~<font color="$2">$3</font>~isg;

		$text =~ s~(\<|&lt;?)hr(\>|&gt;?)~<hr size="1">~g;	

	$text =~ s~([^\w\"\=\[\]]|[\A\n\b])\\*(\w+://[^<>\s\n\"\]\[]+)~$1<a href="$2" target="_blank">$2</a>~isg;
	$text =~ s~([^\"\=\[\]/\:]|[\A\n\b])\\*(www\.[^<>\s\n\]\[]+)~$1<a href="http://$2" target="_blank">$2</a>~isg;

	$text =~ s~([^\f\"\=\[\]]|[\A\n\b])\\*(\f+://[^<>\s\n\"\]\[]+)~$1<a href="$2" target="_blank">$2</a>~isg;
	$text =~ s~([^\"\=\[\]/\:]|[\A\n\b])\\*(ftp\.[^<>\s\n\]\[]+)~$1<a href="ftp://$2" target="_blank">$2</a>~isg;

	# $text =~ s~(\S+?)\@(\S+)~<a href="mailto:$1\@$2">$1\@$2</a>~gi;
	}

	return $text;
}


if (-e "$scriptdir/user-lib/block.pl") {require "$scriptdir/user-lib/block.pl"} 

1;

