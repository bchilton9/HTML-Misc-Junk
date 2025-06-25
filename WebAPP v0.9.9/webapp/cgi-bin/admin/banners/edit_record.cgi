#!/usr/bin/perl 
############################################################################### 
############################################################################### 
# WebAPP - Automated Perl Portal                                              # 
#-----------------------------------------------------------------------------# 
# edit_record.cgi for admin/banners                                           #
# v0.9.9 - Requin                                                             #
# Javascript banner rotation removed by Carter v0.9.4                         # 
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
# File: Last modified: 10/30/02                                               # 
############################################################################### 
############################################################################### 
 
$| = 1; 
 
use CGI::Carp qw(fatalsToBrowser); 
 
$scriptname = "WebAPP";
$scriptver = "0.9.9"; 
 
 
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
 
check_access(editbanner); if ($access_granted ne "1") { error("$err{'011'}"); }

$navbar = "$btn{'014'} $mnu{'040'} $btn{'014'} $banner{'010'}"; 
print_top(); 

 
print qq~ 
<font face='Arial'> 
<b><i>$banner{'010'}</i></b> 
<form action='edit.cgi' method='GET'> 
<input type='hidden' name='banurl' value='$input{'banurl'}'> 
<input type='hidden' name='iban' value='$input{'iban'}'> 
<input type='hidden' name='iw' value='$input{'iw'}'> 
<input type='hidden' name='ih' value='$input{'ih'}'> 
<input type='hidden' name='alt' value='$input{'alt'}'>
<input type='hidden' name='hit' value='$input{'hit'}'> 
<table border='1'> ~;

	$input{'banurl'} =~ s/EQSIGN/\=/g;
	$input{'banurl'} =~ s/QMSIGN/\?/g;
	$input{'banurl'} =~ s/DQUOTE/\"/g;
	$input{'banurl'} =~ s/SQUOTE/\'/g;
	$input{'banurl'} =~ s/AMPSIGN/\&/g;

print qq~
<tr><td><font size='2'>$banner{'003'}</font></td><td><input type='text' name='nbanurl' value="$input{'banurl'}"></td></tr> 
<tr><td><font size='2'>$banner{'004'}</font></td><td><input type="text" name="niban" value="$input{'iban'}"></td></tr> 
<tr><td><font size='2'>$banner{'005'}</font></td><td><input type='text' name='niw' value="$input{'iw'}"></td></tr> 
<tr><td><font size='2'>$banner{'006'}</font></td><td><input type='text' name='nih' value="$input{'ih'}"></td></tr> 
<tr><td><font size='2'>$banner{'007'}</font></td><td><input type='text' name='nalt' value="$input{'alt'}"></td></tr>
<tr><td><font size='2'>$banner{'017'}</font></td><td><input type='hidden' name='nhit' value="$input{'hit'}">$input{'hit'}</td></tr> 
</table> 
<input type='Submit' value='$banner{'010'}'> 
</form> 
</font> 
</font> 
~; 
 
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
 
