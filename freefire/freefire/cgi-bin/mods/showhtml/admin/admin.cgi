#!/usr/bin/perl -w
$| = 1;

use CGI::Carp qw(fatalsToBrowser);

###############################################################################
# WebApp ShowHTML Mod                                                         #
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
#-----------------------------------------------------------------------------#
#
#  Written by Ted Loomos
#  Get the latest updates from the CMS Project Area on www.web-app.org
#
#  Revision History:
#  2002-12-30  Script Created
#  0.0.6 - 01/06/2003 - Bug fixes - static files not working and prevent directory traversals
#
###############################################################################

eval {
	require "../../../config.pl";
##--------------------------------------------------------------
## If you are not using standard folder locations, the following
## lines may need to be changed to match your installation
##--------------------------------------------------------------
	$modDir           = "$scriptdir/mods/showhtml";
	$showHTMLDatafile = "$modDir/data/links.dat";
	$cssFile          = "$modDir/iframe.css";
	$defaultHTMLDir   = "$modDir/html";
	$defaultProtocol  = "http";

##--------------------------------------------------------------
## Nothing below this point should require modification
##--------------------------------------------------------------
	require "$sourcedir/subs.pl";
	require "../config.dat";

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
ban();

#getcgi();
&parse_form;

getdate();
logips();
loadcookie();
loaduser();
logvisitors();

####################################
# A Wonderful Mod by Me!
####################################

if ($lang_support eq "1") { mod_langsupp(); }

# Start making your changes here! #

if ($username ne "admin") { error("$err{'011'}"); }

$action = $info{action};
$op 	= $info{op};
$id		= $info{id};

if ($action eq "View") {
	viewLinks();
} elsif ($action eq "Add" || $action eq "Edit") {
	editLinkItem();
} elsif ($action eq "Save") {
	saveLinkItem();
}

print_top();
viewLinks();
print_bottom();

exit;

sub viewLinks {

	print_top();

	open (LINKFILE,"<$showHTMLDatafile") || error("$err{'016'} $showHTMLDatafile");
	@links=<LINKFILE>;
	close (LINKFILE);

	print qq~
	<font face='Arial' size='2'>
	<i>ShowHTML Links</i>
	<table width='100%' border='1'>
	<tr>
	  <td bgcolor='#F2C973'><font size='2'>Action</font></td>
	  <td bgcolor='#F2C973'><font size='2'>ID</font></td>
	  <td bgcolor='#F2C973'><font size='2'>Type</font></td>
	  <td bgcolor='#F2C973'><font size='2'>Protocol</font></td>
	  <td bgcolor='#F2C973'><font size='2'>Source</font></td>
	</tr>
	~;

	foreach $rec (@links){
		chomp($rec);
		($lid,$type,$source,$protocol,$height,$width,$scrolling,$path)=split(/\|/,$rec);

		print qq~
			<tr>
			  <td>
			      <font size="2">
			      <a href="admin.cgi?id=$lid&action=Edit">$nav{'096'}</a> -
			      <a href="admin.cgi?id=$lid&action=Save&op=Delete">$nav{'097'}</a>
			      </font></td>
			  <td><font size="2">$lid</font></td>
			  <td><font size="2">$type</font></td>
			  <td><font size="2">$protocol</font></td>
			  <td><font size="2">$source</font></td>
			</tr>
		~;
	}

	print qq~
		</table>
		<p><a href="admin.cgi\?action=Add">Add Link</a></p>
		</font>
	~;

	print_bottom();
	exit;
}

sub	editLinkItem {

	print_top();

	if ($action eq "Edit") {
		open (LINKFILE,"<$showHTMLDatafile") || error("$err{'016'} $showHTMLDatafile");
		@links = <LINKFILE>;
		close (LINKFILE);

		LINKITEM: foreach $rec (@links){
			chomp($rec);
			($lid,$type,$source,$protocol,$height,$width,$scrolling,$path)=split(/\|/,$rec);
			if ($lid eq $info{id}) {
				last LINKITEM;
			}
		}
	} else {
		$lid       = "";
		$type      = "";
		$source    = "";
		$protocol  = "";
		$height    = "";
		$width     = "";
		$scrolling = "";
		$path      = "";
	}

	%typehash = (
		filename => "Static HTML File",
		url      => "URL"
	);
	%protocolhash = (
		http	=> "http://",
		https	=> "https://"
	);
	%scrollinghash = (
		auto	=> "Automatic",
		yes		=> "Yes",
		no		=> "No"
	);

	$typesel = "";
	while(($key,$value) = each(%typehash)) {
		if ($key eq $type) {$sel="selected"} else {$sel=""}
		$typesel .= "<option value=\"$key\" $sel>$value</option>";
	}

	$protocolsel = "";
	while(($key,$value) = each(%protocolhash)) {
		if ($key eq $protocol) {$sel="selected"} else {$sel=""}
		$protocolsel .= "<option value=\"$key\" $sel>$value</option>";
	}
	if (!$protocol) {$protocolsel .= "<option value=\"\" selected>Default</option>";}

	$scrollingsel = "";
	while(($key,$value) = each(%scrollinghash)) {
		if ($key eq $scrolling) {$sel="selected"} else {$sel=""}
		$scrollingsel .= "<option value=\"$key\" $sel>$value</option>";
	}
	if (!$scrolling) {$scrollingsel .= "<option value=\"\" selected>Default</option>";}


	print qq~
	<TABLE class=menubackcolor cellSpacing=0 cellPadding=3 width="100%" border=0>
	  <TR>
	   <TD vAlign=top width="100%"><FONT face=Arial><I>$action Link</I><BR>
	    <form onSubmit="submitonce(this)" action=admin.cgi method=post>
	    <input type="hidden" name="action" value="Save">
	    <input type="hidden" name="op" value="$action">
	    <input type="hidden" name="id" value="$id">
	     <TABLE border=1>
	       <TR>
				<TD><font size="2">ID</font></TD>
				<TD><INPUT name=id value="$lid" size="30" style="width:200"></TD>
				<TD><font size="2">Enter an identifier to use in the url when displaying this link.  For example, if ID=google then you would use $scripturl/mods/showhtml/showhtml.pl?id=google</font></TD></TR>
			<TR>
				<TD><font size="2">Type</font></TD>
				<TD><SELECT name=type style="width:200">$typesel</select></TD>
				<TD><font size="2"></font></TD></TR>
			<TR>
				<TD><font size="2">Protocol</font></TD>
				<TD><SELECT name=protocol style="width:200">$protocolsel</select></TD>
				<TD><font size="2">Leave blank for $defaultProtocol</font></TD></TR>
			<TR>
				<TD><font size="2">Source</font></TD>
				<TD><INPUT name=source value="$source" size=50 style="width:400"></TD>
				<TD><font size="2">Enter the url w/parameters or the filename.  DO NOT include the protocol (http://) for urls.</font></TD></TR>
			<TR>
				<TD><font size="2">Height</font></TD>
				<TD><INPUT name=height value="$height" size=50 style="width:50"></TD>
				<TD><font size="2">Only for Type = URL.  Leave blank to use CSS setting.</font></TD></TR>
			<TR>
				<TD><font size="2">Width</font></TD>
				<TD><INPUT name=width value="$width" size=50 style="width:50"></TD>
				<TD><font size="2">Only for Type = URL.  Leave blank to use CSS setting.</font></TD></TR>
			<TR>
				<TD><font size="2">Scrollbars</font></TD>
				<TD><SELECT name=scrolling style="width:200">$scrollingsel</select></TD>
				<TD><font size="2">Only for Type = URL.  Leave blank to use CSS setting.</font></TD></TR>
			<TR>
				<TD><font size="2">Path</font></TD>
				<TD><INPUT name=path value="$path" size=50 style="width:400"></TD>
				<TD><font size="2">Only for Type = Static File.  Leave blank to use $defaultHTMLDir.</font></TD></TR>
		  </TABLE>
		  <INPUT type=submit value="$action Link">
		 </FORM></FONT>
		</TD>
	   </TR>
	</TABLE>
	~;

	print_bottom();
	exit;

}

sub	saveLinkItem {

	open (LINKFILE,"<$showHTMLDatafile") || error("$err{'016'} $showHTMLDatafile");
	@links = <LINKFILE>;
	close (LINKFILE);

	open (LINKFILE,">$showHTMLDatafile") || error("$err{'016'} $showHTMLDatafile");
	foreach $rec (@links){
		chomp($rec);
		($lid,$type,$source,$protocol,$height,$width,$scrolling,$path)=split(/\|/,$rec);
		if ($op eq "Edit" || $op eq "Delete") {
			if ($lid eq $id) {
				if ($op eq "Edit") {
					print LINKFILE "$id|$info{type}|$info{source}|$info{protocol}|$info{height}|$info{width}|$info{scrolling}|$info{path}\n";
				}
			} else {
				print LINKFILE "$rec\n";
			}
		} else {
			print LINKFILE "$rec\n";
		}
	}
	if ($op eq "Add") {
		print LINKFILE "$id|$info{type}|$info{source}|$info{protocol}|$info{height}|$info{width}|$info{scrolling}|$info{path}\n";
	}
	close (LINKFILE);
}



# Finish making your changes here! #

###########################
sub mod_langsupp {
###########################

$modlangfail = "0";

if ($username ne $anonuser) {
		open(FILE, "$memberdir/$username.dat");
		lock(FILE);
		@settings = <FILE>;
		unlock(FILE);
		close(FILE);

		for( $i = 0; $i < @settings; $i++ ) {
			$settings[$i] =~ s~[\n\r]~~g;
		}

		if ($settings[0] ne $password && $action ne "logout") { error("$err{'002'}"); }
		else {
			$realname = $settings[1];
			$realemail = $settings[2];
			$userlang = $settings[15];
		}

}

		if ($userlang eq "") { $userlang = $language; }

			 if ($modlangfail ne "1") {
			 @modlanguage = $userlang;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
			 } else {
			 @modlanguage = $language;
			 foreach $rec (@modlanguage){
			 chomp($rec);
			 ($modlang,$dummy)=split(/\./,$rec);
			 }
		}

eval {
	require "../language/$modlang.dat";

	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};

if ($@) {$modlangfail = "1"; mod_langsuppfail();}

}

########################
sub mod_langsuppfail {
########################

eval {
	require "../language/$mod_lang";

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

}
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
		if ($name =~ /^multiple-/) {
			$name =~ s/multiple-//;
			push (@{$info{$name}}, $value);
		} else {
			$info{$name} = $value;
		}
	}
}

1;

