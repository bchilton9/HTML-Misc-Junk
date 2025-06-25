#!/usr/bin/perl

###################################################
#                                                 #
# Virtual Visions Ad Banner Rotation Script v1.70 #
# Copyright 1999 by Barracuda                     #
# Email - baracuda@feartech.com                   #
#                                                 #
###################################################

# this is the url of the directory that holds your
# ad banner images, include a trailing "/" !!!

$ad_url = '';

# this is the path to the directory that holds your
# ad banner images, include a trailing "/" !!!

$ad_dir = '';

# this is the path to banners.txt

$config = '/home/erenetw/public_html/cgi-bin/ban/banners.txt';

# this is the url of this script

$admin_script = 'http://www.erenetwork.com/cgi-bin/ban/admin.pl';

# this is the url of banners.pl

$ads_script = 'http://www.erenetwork.com/cgi-bin/ban/banners.pl';

# this is the url of log.pl or logNT.pl

$log_script = 'http://www.erenetwork.com/cgi-bin/ban/log.pl';

# this is the url of your log directory

$log_url = 'http://www.erenetwork.com/ban/data/index.htm';

# this is the path to banners.js which will be created
# by this script, you just need to specify where you
# want it to be created below, the file does not need
# to exist. You will need to chmod 777 the directory
# where you want it to be created though.

$javascript = '/home/erenetw/public_html/ban/banners.js';

###################################################

use CGI qw(:standard);
$ads = new CGI;

$action = $ads->param('action');
$subaction = $ads->param('subaction');

&add unless $action ne "add";
&view unless $action ne "view";
&list_all unless $action ne "listall";
&modify unless $action ne "modify";
&delete unless $action ne "delete";
&search unless $action ne "search";
&build unless $action ne "build";

###################################################

if ($last_action eq "") { $last_action = "Admin Logon"; }

&read_db ("$config");
&lastmod ("$config");

&print_header;

print qq~
<b>Last Action: $last_action</b><br>
<i>$total Ads Currently in the Rotation</i><br><br>
<b>Ad Url:</b> $ad_url<br>
<b>Ad Dir:</b> $ad_dir<br>
<b>Last Modified:</b> $date<br><br>
~;

&print_footer;

################
# sub routines #
################

sub add
{
	$img = $ads->param('img');
	$border = $ads->param('border');
	$width = $ads->param('width');
	$height = $ads->param('height');
	$alt = $ads->param('alt');
	$url = $ads->param('url');
	$image = $ads->param('image');
	$weight = $ads->param('weight');

	if ($subaction eq "add")
	{
		&read_db ("$config");
		
		$last_entry = pop(@database);
		($id,$a,$b,$c,$d,$e,$f,$g) = split(/\|\|/,$last_entry);
		$id++;
		
		$url =~ s/http:\/\///g;

		open (DB,">>$config") || &cgiError ("Error Updating $config:", "$!");
		print DB "$id||$img||$border||$width||$height||$alt||$url||$weight\n";
		close(DB);

		$last_action = "Ad: $id Added Successfully";
	}

	else
	{
		&print_header;

		print qq~
		<b>Add Ad to Rotation</b><form action="$admin_script" method=POST>
		<table border="0" cellpadding="5" cellspacing="0">
		<tr valign="top"><td width="75">Modify<br></td><td width="90"><b>Image:</b></td><td><input type="text" name="img" size="50"></td></tr>
		<tr valign="top"><td rowspan="7">Delete</td><td><b>Border:</b></td><td><input type="text" name="border" size="50"></td></tr>
		<tr valign="top"><td><b>Width:</b></td><td><input type="text" name="width" size="50" value="468"></td></tr>
		<tr valign="top"><td><b>Height:</b></td><td><input type="text" name="height" size="50" value="60"></td></tr>
		<tr valign="top"><td><b>Alt Text:</b></td><td><input type="text" name="alt" size="50"></td></tr>
		<tr valign="top"><td><b>URL:</b></td><td><input type="text" name="url" size="50"></td></tr>
		<tr valign="top"><td><b>Weight:</b></td><td><input type="text" name="weight" size="50" value="1"></td></tr>
		<tr valign="top"><td colspan="2"><input type="hidden" name="subaction" value="add"><input type="hidden" name="action" value="add"><br><input type="submit" value="Add Ad"></td></tr>
		</table></form>
		~;

		&print_footer;
	
		exit;
	}
}

sub view
{
	$find = $ads->param('view');
	&search_db ("$config");
	&print_header;

	print qq~
	<b>View Ad: $img (id: $id)</b>
	<table border="0" cellpadding="0" cellspacing="5">
	<tr valign="top"><td width="50" rowspan="7"><a href="$admin_script?action=modify&modify=$id">Modify</a>&nbsp;&nbsp;&nbsp;&nbsp;<br><a href="javascript:killEntry('$id')">Delete</a><br></td><td><b>Image:</b></td><td><img src="$ad_url$img" alt="ID: $id ($img - $alt)" border="$border" width="$width" height="$height"><br><br></td></tr>
	<tr valign="top"><td><b>Url:</b></td><td><a href="http://$url">http://$url</a></td></tr>
	<tr valign="top"><td><b>Alt Text:</b></td><td>$alt</td></tr>
	<tr valign="top"><td><b>Border:</b></td><td>$border</td></tr>
	<tr valign="top"><td><b>Width:</b></td><td>$width</td></tr>
	<tr valign="top"><td><b>Height:</b></td><td>$height</td></tr>
	<tr valign="top"><td><b>Weight:</b></td><td>$weight</td></tr>
	</table>
	~;

	&print_footer;

	exit;
}

sub modify
{
	$find = $ads->param('modify');
	$id = $ads->param('id');
	$img = $ads->param('img');
	$border = $ads->param('border');
	$width = $ads->param('width');
	$height = $ads->param('height');
	$alt = $ads->param('alt');
	$url = $ads->param('url');
	$weight = $ads->param('weight');
	
	$url =~ s/http:\/\///g;

	if ($subaction eq "modify")
	{
		&read_db ("$config");

		open (DB,">$config") || &cgiError ("Error Updating $config:", "$!");
		
			foreach $line (@database) {
				($idnum,$m,$b,$w,$h,$a,$u,$wt) = split(/\|\|/,$line);
				if ($idnum == $id) { $found=1; print DB "$id||$img||$border||$width||$height||$alt||$url||$weight\n"; }
				else { print DB "$line"; }
			}
			
		close(DB);

		if ($found != 1) { &cgiError ("$find Does Not Exist:", "Unable to locate user in: $config"); }

		$last_action = "Ad: $id Modified Successfully";
	}

	else
	{
		&search_db ("$config");
		&print_header;

		print qq~
		<b>Modify Ad: $img (id: $id)</b><form action="$admin_script" method=POST>
		<table border="0" cellpadding="5" cellspacing="0">
		<tr valign="top"><td width="75">Modify<br></td><td width="90"><b>Image:</b></td><td><input type="text" name="img" size="50" value="$img"></td></tr>
		<tr valign="top"><td rowspan="7"><a href="javascript:killEntry('$find')">Delete</a></td><td><b>Border:</b></td><td><input type="text" name="border" size="50" value="$border"></td></tr>
		<tr valign="top"><td><b>Width:</b></td><td><input type="text" name="width" size="50" value="$width"></td></tr>
		<tr valign="top"><td><b>Height:</b></td><td><input type="text" name="height" size="50" value="$height"></td></tr>
		<tr valign="top"><td><b>Alt Text:</b></td><td><input type="text" name="alt" size="50" value="$alt"></td></tr>
		<tr valign="top"><td><b>URL:</b></td><td><input type="text" name="url" size="50" value="$url"></td></tr>
		<tr valign="top"><td><b>Weight:</b></td><td><input type="text" name="weight" size="50" value="$weight"></td></tr>
		<tr valign="top"><td colspan="2"><input type="hidden" name="subaction" value="modify"><input type="hidden" name="action" value="modify"><input type="hidden" name="id" value="$id"><br><input type="submit" value="Modify Ad"></td></tr>
		</table></form>
		~;

		&print_footer;

		exit;
	}
}

sub delete
{
	foreach $key ($ads->param)
	{
		$action = $ads->param($key);
		$find = $key;
	
		if ($key eq "delete") { $find = $ads->param($key); $action = "delete"; }
		
		if ($action eq "delete" && $find ne "action")
		{
			&read_db ("$config");

			open (DB,">$config") || &cgiError ("Error Updating $database:", "$!");
			
				foreach $line (@database)
				{
					($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$line);
					if ($find == $id) { $found=1; $image = "$ad_dir$img"; }
					else { print DB "$line"; }
				}

			close(DB);

			if ($found != 1) { &cgiError ("$find Does Not Exist:", "Unable to locate user in: $config"); }

			#if (-e $image) { unlink($image) || &cgiError ("Error Removing $image:", "$!"); }
			#else { &cgiError ("Error Removing $image:", "file does not exist"); }

			$entry = "$entry $id";

			$last_action = "Ad(s): $entry Removed Successfully";
		}
	}
}

sub list_all
{
	$page = $ads->param('page');
	$results=5;

	&read_db ("$config");
	
	if ($page > 0) { $first = ($page * $results); $last = (($first + $results) - 1); }
	else { $first = 0; $last = ($results - 1); }
	
	if ($page > 0) { $first = ($page * $results); $last = (($first + $results) - 1); }
	else { $first = 0; $last = ($results - 1); }
	
	$from = ($first + 1);
	$to = ($last + 1);

	if ($to > $total) { $to = $total; }
	
	# @database = sort(@database);
	$seek = int($total / $results);
	
	if ($total < $results) { $to = $total; }
	
	&print_header;
	print "<b>Entry Listing: Full Listing</b><br>\n<i>$total Ads in the Rotation ($from - $to shown)</i>\n\n";
	
	for ($x=$first; $x<=$last; $x++)
	{
		if ($database[$x])
		{
			($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$database[$x]);

			print qq~
			<table border="0" cellpadding="0" cellspacing="5">
			<tr valign="top">
			<td width="50" rowspan="7">
			<a href="$admin_script?action=modify&modify=$id">Modify</a>&nbsp;&nbsp;&nbsp;&nbsp;<br>
			<a href="javascript:killEntry('$id')">Delete</a><br>
			</td>
			<td><b>Image:</b></td><td><img src="$ad_url$img" alt="ID: $id ($img - $alt)" border="$border" width="$width" height="$height"><br><br></td>
			</tr>
			<tr valign="top"><td><b>Url:</b></td><td><a href="http://$url">http://$url</a></td></tr>
			<tr valign="top"><td><b>Alt Text:</b></td><td>$alt</td></tr>
			<tr valign="top"><td><b>Border:</b></td><td>$border</td></tr>
			<tr valign="top"><td><b>Width:</b></td><td>$width</td></tr>
			<tr valign="top"><td><b>Height:</b></td><td>$height</td></tr>
			<tr valign="top"><td><b>Weight:</b></td><td>$weight</td></tr>
			
			</table><br>
			~;
		}
	}

	if ($total > $results)
	{
		print "<b>Page:</b>";
		
		for ($x=0; $x<=$seek; $x++)
		{
			$num = ($x * $results);
			if ($database[$num])
			{
				print " <a href=\"$admin_script?action=listall&page=$x\">$x</a>\n";
			}
		}
		
		print "<br><br>\n";
	}
	
	&print_footer;

exit;
}

sub search
{
	$keyword = $ads->param('keyword');
	$page = $ads->param('page');

	&read_db ("$config");
	
	$results=5;

	if ($page > 0) { $first = ($page * $results); $last = (($first + $results) - 1); }
	else { $first = 0; $last = ($results - 1); }

	for ($i=0; $i<=$total; $i++)
	{
		if ($database[$i] =~ /$keyword/i)
		{
			push(@matches,$database[$i]);
		}
	}

	$totalnum=@matches;
	$seek = int($totalnum / $results);
	
	if ($page > 0) { $first = ($page * $results); $last = (($first + $results) - 1); }
	else { $first = 0; $last = ($results - 1); }
	
	$from = ($first + 1);
	$to = ($last + 1);

	if ($to > $totalnum) { $to = $totalnum; }
	
	@matches = sort(@matches);

	&print_header;
	print "<b>Search Results for: $keyword</b><br>\n";
	print "<i>$totalnum Matches Found ($from - $to shown)</i>\n\n";
	
	for ($x=$first; $x<=$last; $x++)
	{
		if ($matches[$x])
		{
			($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$matches[$x]);
			
			print qq~
			<table border="0" cellpadding="0" cellspacing="5">
			<tr valign="top">
			<td width="50" rowspan="7">
			<a href="$admin_script?action=modify&modify=$id">Modify</a>&nbsp;&nbsp;&nbsp;&nbsp;<br>
			<a href="javascript:killEntry('$id')">Delete</a><br>
			</td>
			<td><b>Image:</b></td><td><img src="$ad_url$img" alt="ID: $id ($img - $alt)" border="$border" width="$width" height="$height"><br><br></td>
			</tr>
			<tr valign="top"><td><b>Url:</b></td><td><a href="http://$url">http://$url</a></td></tr>
			<tr valign="top"><td><b>Alt Text:</b></td><td>$alt</td></tr>
			<tr valign="top"><td><b>Border:</b></td><td>$border</td></tr>
			<tr valign="top"><td><b>Width:</b></td><td>$width</td></tr>
			<tr valign="top"><td><b>Height:</b></td><td>$height</td></tr>
			<tr valign="top"><td><b>Weight:</b></td><td>$weight</td></tr>
			</table><br>
			~;
		}
	}

	if ($totalnum > $results)
	{
		print "<b>Page:</b>";
		
		for ($x=0; $x<=$seek; $x++)
		{
			$num = ($x * $results);
			
			if ($matches[$num])
			{
				print " <a href=\"$admin_script?action=search&keyword=$keyword&page=$x\">$x</a>\n";
			}
		}
		
		print "<br><br>\n";
	}
	
	&print_footer;

exit;
}

sub build
{
	&read_db("$config");
	
	$totalnum = $total;
	
	for ($x=0; $x<$totalnum; $x++)
	{
		($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$database[$x]);
		
		if ($weight > 1)
		{
			for ($i=1; $i<$weight; $i++)
			{
				$database[$total] = "$id||$img||$border||$width||$height||$alt||$url||$weight";
				
				$total++;
			}
		}
	}

	open(JAVA,">$javascript") || &cgiError ("Error Writing: $javascript", "$!");
	print JAVA "var how_many_ads = $total;\n";
	print JAVA "var now = new Date()\n";
	print JAVA "var sec = now.getSeconds()\n";
	print JAVA "var ad = sec % how_many_ads;\n";
	print JAVA "ad +=1;\n\n";
	
	$ad_counter=1;
	
	foreach $line (@database)
	{
		chomp($line);
		($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$line);
		$url =~ s/http\:\/\///g;
		$url =~ s/\r//g;
		$url =~ s/\n//g;
		
		print JAVA "if (ad==$ad_counter)\n{\n";
		print JAVA "	id=\"$id\";\n";
		print JAVA "	url=\"$url\";\n";
		print JAVA "	alt=\"$alt\";\n";
		print JAVA "	img=\"$img\";\n";
		print JAVA "	width=\"$width\";\n";
		print JAVA "	height=\"$height\";\n";
		print JAVA "	border=\"$border\";\n";
		print JAVA "}\n\n";
	
		$ad_counter++;
	}
	
$end_java = qq~	
document.write("<a href=$ads_script?a=url&id=" + id + " TARGET=NEW>");
document.write("<img src=" + img + " border=" + border + " width=" + width + " height=" + height + " alt='" + alt + "'>");
document.write("</a>");
~;
	
	print JAVA "$end_java";
	
	close(JAVA);
}

sub print_header {
print "Content-type: text/html\n\n";

print <<END_PRINT_HEADER;
<html><head><title>Perl N' JavaScript Banners v1.70</title>
<SCRIPT LANGUAGE="JavaScript">
function viewEntry () { var entry = window.prompt("Enter the ID# of the Entry to View:\\r",'enter id#'); if (entry != null) { window.location.href = "$admin_script?action=view&view=" + entry + "" } }
function modifyEntry () { var entry = window.prompt("Enter the ID# of the Entry to Modify:\\r",'enter id#'); if (entry != null) { window.location.href = "$admin_script?action=modify&modify=" + entry + "" } }
function deleteEntry () { var entry = window.prompt("Enter the ID# of the Entry to Delete:\\r",'enter id#'); if (entry != null) { window.location.href = "$admin_script?action=delete&delete=" + entry + "" } }
function killEntry(entry) { if (window.confirm("Are you sure you want to Remove this Entry?\\r\\r" + entry + "")) { window.location.href = "$admin_script?action=delete&delete=" + entry + "" } }
function search () { var entry = window.prompt("Enter Keyword to Search For:\\rThis can be ID#, Link Name, URL, Date",'enter keyword'); if (entry != null) { window.location.href = "$script_url?action=search&keyword=" + entry + "" } }
</SCRIPT></head><body bgcolor="#666666" text="#000000" link="blue" alink="red" vlink="blue">
<center><table border="2" cellpadding="4" cellspacing="0" width="95%"><tr valign="top"><td width="100%" bgcolor="#000080"><b><font color="white" face="arial">Perl N' JavaScript Banners :: Admin</font></b></td></tr><tr><td bgcolor="#999999">
<center><a href="$admin_script">Main</a> | <a href="$admin_script?action=add">Add Ad</a> | <a href="javascript:viewEntry()">View Ad</a> | <a href="javascript:modifyEntry()">Modify Ad</a> | <a href="javascript:deleteEntry()">Remove Ad</a> | 
<a href="javascript:search()">Search</a> | <a href="$admin_script?action=listall">List All</a> | <a href="$log_url">View Stats</a> | <a href="$log_script">Rebuild Stats</a> | <a href="$admin_script?action=build">Rebuild JavaScript</a></center></td></tr><tr><td bgcolor="#999999">
END_PRINT_HEADER
}

sub print_footer {
print <<END_PRINT_FOOTER;
</td></tr></table></center><br><center><font size="-1">Powered by Virtual Visions Perl N' Javascript Banners. Copyright &copy; 1999 by <a href="http://www.feartech.com/vv"><font color="#C0C0C0">Virtual Visions</font></a>. All rights Reserved.</font></center></body></html>
END_PRINT_FOOTER
}

sub search_db
{
	&read_db;

	foreach $line (@database)
	{
		chomp($line);
		($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$line);
		
		if ($find == $id)
		{
			$found=1; last;
		}
	}
	
	if ($found != 1) { &cgiError ("$find Does Not Exist:", "Unable to locate user in database"); }
}

sub read_db
{
	my ($database) = @_;

	open(DB,"$database") || &cgiError("Error Reading $database:", "$!");
	@database = <DB>;
	close(DB);
	
	$total=@database;
}

sub lastmod
{
	my ($checkdir) = @_;
	($filedate) = (stat($checkdir))[9];
	&getdate ("$filedate");
}

sub getdate
{
	my ($filedate) = @_;

	if ($filedate ne "") { ($day, $mon, $yr) = (localtime($filedate))[3,4,5]; }
	else { ($day, $mon, $yr) = (localtime(time))[3,4,5]; }

	@months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');

	if ($day < 10) { $day = "0$day"; }

	if ($yr > 99)
	{
		$yr-=100;

		if ($yr < 10) { $yr = "200$yr"; }
		elsif ($yr >= 10 && $yr < 100) { $yr = "20$yr"; }
		else { $yr = "2$yr"; }
	}

	else 
	{
		if ($yr < 10) { $yr = "190$yr"; }
		else { $yr = "19$yr"; }
	}

	$date = "$months[$mon] $day $yr";
}
sub cgiError
{
	my ($error_cause,$error) = @_;

	if ($error_cause eq "") { $error_cause = "Error:"; }
	if ($error eq "") { $error = "The script encountered problems and terminated"; }

	&print_header;
	print "<font color=\"black\"><h3>$error_cause</h3>$error</font><br><br><b>Environment:</b><br><br>";
	foreach $key ($ads->param) { $value = $ads->param($key); print "<b>$key:</b> $value<br>\n"; }
	&print_footer;

exit;
}