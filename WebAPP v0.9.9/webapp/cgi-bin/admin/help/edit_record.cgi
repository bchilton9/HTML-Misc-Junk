#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# edit_record.cgi for admin/help                                              #
# v0.9.9 - Requin                                                             #
#                                                                             #
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
# File: Last modified: 05/09/02 by Floyd                                      #
###############################################################################
###############################################################################

$| = 1;

use CGI::Carp qw(fatalsToBrowser);

$scriptname = "WebAPP";
$scriptver = "0.9.8";

eval {
	require "../../config.pl";
	require "$sourcedir/subs.pl";

	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};
if ($@) {
	print "Content-type: text/html\n\n";
	print qq~<h1>Software Error:</h1>
Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
<pre>$@</pre>
<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
~;
	exit;
}

getlanguage();
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

############################
# Get data from GET & POST #
############################
&parse_form;

##################################
# Print out the page for editing #
##################################

$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $help{'010'}";
print_top();

check_access(editfaq); if ($access_granted ne "1") { error("$err{'011'}"); }

open(FILE, "<$datadir/help/data.txt");
lock(FILE);
chomp(@datas = <FILE>);
unlock(FILE);
close(FILE);

foreach $rec (@datas){
	chomp($rec);
	($helpq,$helpa)=split(/\|/,$rec);

$question = &removehtml("$helpq");

if ($input{'helpq'} eq "$question") {
$helpa =~ s~<BR>~\n~g;
print qq~
<font face='Arial'>
<b><i>$help{'010'}</i></b>
<form action='edit.cgi' method='GET'>
<input type='hidden' name='helpq' value='$question'>
<table border='1'>
<tr><td><font size='2'>$help{'003'}</font></td><td><textarea name="nhelpq" cols="40" rows="2">$helpq</textarea></td></tr>
<tr><td><font size='2'>$help{'004'}</font></td><td><textarea name="nhelpa" cols="40" rows="10">$helpa</textarea></td></tr>
</table>
<input type='Submit' value='$help{'010'}'>
</form>
</font>
</font>
~;
}

else {}

}

print_bottom();

########################################
# Code to get the data from GET & POST #
########################################
sub parse_form {

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
   @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $input{$name} = $value;
   }
}

##############
sub revealhtml {
##############
	
my $text = shift;

	$text =~ s/1quote1/'/g;
	$text =~ s/2quote2/"/g;
	$text =~ s/&amp;/&/g;
	$text =~ s/&quot;/"/g;
	$text =~ s/ \&nbsp;/  /g;
	$text =~ s/&lt;script&gt;/<skript>/g;
	$text =~ s/&lt;\\script&gt;/<\\skript>/g;
	$text =~ s/&lt;javascript&gt;/<javaskript>/g;
	$text =~ s/&lt;\\javascript&gt;/<\\javaskript>/g;
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

	return $text;
}

################
sub removehtml {
################
	my $text = shift;
	
	$text =~ s/'/1quote1/g;
	$text =~ s/"/2quote2/g;
	$text =~ s/&/&amp;/g;
	$text =~ s/"/&quot;/g;
	$text =~ s/  / \&nbsp;/g;
	$text =~ s/</&lt;/g;
	$text =~ s/>/&gt;/g;
	$text =~ s/\t/ \&nbsp; \&nbsp; \&nbsp;/g;
	$text =~ s/\cM//g;
	$text =~ s/\n/<br>/g;
	$text =~ s/\|/<pipe>/g;	

	return $text;
}

1;

