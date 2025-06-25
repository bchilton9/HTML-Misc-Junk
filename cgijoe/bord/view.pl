#!/usr/local/bin/perl
#################################################################
#             Message Board V4.5.1 (Freeware)
#
# This program is distributed as freeware. We are not            	
# responsible for any damages that the program causes	
# to your system. It may be used and modified free of 
# charge, as long as the copyright notice
# in the program that give me credit remain intact.
# If you find any bugs in this program. It would be thankful
# if you can report it to us at cgifactory@cgi-factory.com.  
# However, that email address above is only for bugs reporting. 
# We will not  respond to the messages that are sent to that 
# address. If you have any trouble installing this program. 
# Please feel free to post a message on our CGI Support Forum.
# Selling this script is absolutely forbidden and illegal.
##################################################################
#
#               COPYRIGHT NOTICE:
#
#         Copyright 1999-2001 CGI-Factory.com TM 
#		  A subsidiary of SiliconSoup.com LLC
#
#
#      Web site: http://www.cgi-factory.com
#      E-Mail: cgifactory@cgi-factory.com
#      Released Date: Junuary 13, 2001
#	
#   Message Board V4.5.1 is protected by the copyright 
#   laws and international copyright treaties, as well as other 
#   intellectual property laws and treaties.
###################################################################
$fullpath="./";

push(@INC, $fullpath);
##don't change this variable unless you know what you are doing
$bench="0";
###You may need to change following variables to full system path if you are using windows servers
$mcfg="mcfg.pl";
$vcfg="vcfg.pl";
#
$start=(times)[0];
if ($ENV{'REQUEST_METHOD'} eq 'GET') {
@pairs = split(/&/, $ENV{'QUERY_STRING'});
}
else {
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
}
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$name =~ tr/+/ /;
$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$value =~ s/\n/\s/g;
if ($name && $value) { $input{$name} = $value; }
if ($value=~ tr/;<>*|`&$!#()[]{}:'"//) {
print "Content-type: text/html\n\n";
&header;
print "<h2>Action canceled</h2>\n";
print "Please don't use weird symbols\n";
&footer;
exit;
}
}
@months = ('January','February','March','April','May','June','July','August','September','October','November','December');
@days = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
eval {
require "$mcfg";
require "$vcfg";
};
if ($@) {
print "Content-type: text/html\n\n";
&error("Unable to load $mcfg and $vcfg. Please check out the readme file.");
}
#cookie
if ($use_cookie eq "y" or $username_cookie) {
@nvpairs=split(/; /, $ENV{'HTTP_COOKIE'});
foreach $pair (@nvpairs) {
        ($name, $value) = split(/=/, $pair);
        $cookie{$name} = $value;
}
}
if ($cookie{'MBuser'}) {
($user_name, $user_email)=split(/\|/, $cookie{'MBuser'});
}
#

if ($use_cookie eq "y") {
$time=time;
$expires+=$time+2592000;
local($sec,$min,$hour,$mday,$mon,$year,$wday) = gmtime($expires);
$year+=1900;
$expires="$days[$wday], $mday-$months[$mon]-$year $hour:$min:$sec GMT";
if (!$cookie{board1}) {
print "Set-Cookie: board1=$time; path=/; expires= $expires;\n";
}
else {
print "Set-Cookie: board1=$time; path=/; expires= $expires;\n" if ($time-$cookie{board1}>=$reset_cookie);
}
}

print "Content-type: text/html\n\n";
open (board, "<$bdata/board1.bd") or &error("unable to open board1.bd");
if ($flock eq "y") {
flock board, 2;	
}	
@board=<board>;
close (board);
chomp(@board[0]);
chomp(@board[1]);
chomp(@board[2]);
chomp(@board[3]);
chomp(@board[4]);
$messages=@board[0];
$messages2=@board[1];
#starting to get the message array
opendir (DIR, "$messages") or &error("Unable to open the dir for reading");
@reading=readdir(DIR);
@reading=grep(/\.dat/, @reading);
close (DIR);
$total=0;
COUNTING:foreach $read(@reading) {
$read=~ s/\.dat//;
open (content, "<$messages/$read.dat") or next COUNTING;
@content=<content>;
close (content);
$order[$total]="@content[2]x$read";
$total++;
}
@order=sort(@order);
@order=reverse(@order);	
#start to create the message index page
if ($input{'next'} and $input{'next'}<$total and $input{'next'}>=0) {
@order=splice(@order, $input{'next'}); 
}
else {
$input{'next'}=0;	
}	

if (@board[4]==0) {
$closed="[forum closed] ";
}

&header;

print <<EOF;
<TABLE bgcolor="$table_background_color" border="0" cellpadding="0" cellspacing="1">
      <TR>
        <TD width="100%">
          <TABLE width="100%" bgcolor="$title_bar_color" cellpadding="0" cellspacing="0" border="0">
            <TR>
              <TD align="left">
                <FONT color="$title_bar_text_color" face="arial" size="2"><B>@board[2] $closed</B></FONT>
              </TD>
EOF

$num=0;
print "<td align=\"right\" valign=\"bottom\">&nbsp;</td></tr></table>";

print "<table border=\"0\" width=\"$table_width\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"$inner_table_background_color\"><tr><td><table border=\"0\" width=\"$table_width\" cellspacing=\"1\" cellpadding=\"1\">\n
<tr bgcolor=\"$column_title_color\" valign=\"top\"><td><font color=\"$column_title_text_color\" face=\"$font_face\" size=\"$font_size\">&nbsp;</font></td>
<td><font color=\"$column_title_text_color\" face=\"$font_face\" size=\"$font_size\">Subject&nbsp;</font></td>\n
<td width=\"5\"><font color=\"$column_title_text_color\" face=\"$font_face\" size=\"$font_size\">Replies&nbsp;</font></td>\n
<td width=\"$from_width\"><font color=\"$column_title_text_color\" face=\"$font_face\" size=\"$font_size\">From&nbsp;</font></td>\n
<td width=\"$post_width\"><font color=\"$column_title_text_color\" face=\"$font_face\" size=\"$font_size\">Last Post&nbsp;</font></td></tr>\n";
if ($total==0) {
print "<tr bgcolor=\"$color1\" valign=\"top\"><td>&nbsp;</td><td><img src=\"$default_icon\" border=\"0\"> <font color=\"$font_color\" face=\"$font_face\" size=\"$font_size\">No messages were posted.</font></td>";
print "<td align=\"center\"><font color=\"$font_color\" face=\"$font_face\" size=\"$font_size\">-</font></td>\n";
print "<td align=\"center\"><font color=\"$font_color\" face=\"$font_face\" size=\"$font_size\">-</font></td><td align=\"center\"><font color=\"$font_color\" face=\"$font_face\" size=\"$font_size\">-</font></td></tr></table>\n";
&skip;
}
Opening:foreach $order (@order) {
@xorder=split (/x/, "$order");
chomp(@xorder[1]);
open (data, "<$messages/@xorder[1].dat") or next Opening;
@data=<data>;
close (data);
#time
chomp(@data[2]);
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(@data[2]))[0,1,2,3,4,5,6];
$sec = sprintf("%.02d",$sec);
$min = sprintf("%.02d",$min);
$hour = sprintf("%.02d",$hour);
$mday = sprintf("%.02d",$mday);
$year += 1900;
#date format
if ($date_format==1) {
$date = "$days[$wday], $months[$mon] $mday, $year at $hour:$min:$sec";
}
elsif ($date_format==2) {
$mon++;
$date = "$mday/$mon/$year $hour:$min:$sec";	
}
else {
$mon++;
$date = "$mon/$mday/$year $hour:$min:$sec";	
}		
#
$num++;
if (!@data[4]) {
@data[4]=$default_icon;	
}	
$temp_color=$color1;
$color1=$color2;
$color2=$temp_color;
print "<tr valign=\"top\" bgcolor=\"$color2\"><td width=\"1%\">";
if ($use_cookie eq "y") {
if (@data[2]>$cookie{board1}) {
print "<img src=\"$new_icon\" alt=\"New Topic!\">";
}
else {
print "&nbsp;";
}
}
else {
print "&nbsp;";
}
@xorder[1]="@xorder[1]\-@data[5]" if (@data[5]>0);
print "</td><td>
<img src=\"@data[4]\" border=\"0\"> <font face=\"$font_face\" size=\"$font_size\"><a href=\"$messages2/@xorder[1].$file_ending\">
@data[0]</a></font></td>
<td><font color=\"$font_color\" face=\"$font_face\" size=\"$font_size\">@data[1]</font></td>
<td><font color=\"$font_color\" face=\"$font_face\" size=\"$font_size\">@data[3]</font></td>
<td><font color=\"$font_color\" face=\"$font_face\" size=\"$font_size\">$date</font></td></tr>\n";
if ($num==$max) {
print "</table></td></tr></table></td></tr></table>\n";
&copyright;

&links;
if (@board[4]==1) {
&post_box;
}
if ($bench==1) {
$end=(times)[0];
print "<br>It took ", ($end - $start) , " second to complete this job (start: $start end $end)";
}
&footer;
exit;	
}
}
sub skip {
print "</table></td></tr></table></td></tr></table>\n";
&copyright;

&links;
if (@board[4]==1) {
&post_box;
}
if ($bench==1) {
$end=(times)[0];
print "<br>It took ", ($end - $start) , " second to complete this job (start: $start end $end)";
}
&footer;
exit;	
}
print "</table></td></tr></table></td></tr></table>\n";
&copyright;

&links;
if (@board[4]==1) {
&post_box;
}
if ($bench==1) {
$end=(times)[0];
print "<br>It took ", ($end - $start) , " second to complete this job (start: $start end $end)";
}
&footer;
exit;
#post box
sub post_box {
print "<br><br><br>\n";

# Print the posting form ##############################################

print qq|
<table border="0">\n
<tr>\n
<td>\n
<table border="0" width="100%">\n
  <tr bgcolor="$title_bar_color">\n
    <td>\n
      <font color="$title_bar_text_color" face="$font_face" size="2">\n
        <b>Post a new message:</b>\n
	  </font>\n
	</td>\n
  </tr>\n
|;
		

print qq|
</table>\n
</td>\n
</tr>\n

<br>\n
\n
<tr>\n
<td>\n
<table border="0" cellspacing="0">\n
<form action="$cgi" method="post">\n
  <tr>\n
    <td>\n
	  <font color="$other_color" face="$font_face" size="$font_size">\n
	    Name:\n
	  </font>\n
	</td>\n
	<td>\n
	  <input type="text" name="name" maxlength="20" value="$user_name">\n
	</td>\n
  </tr>\n
  <tr>\n
    <td>\n
	  <font color="$other_color" face="$font_face" size="$font_size">\n
	    Email:\n
	  </font>\n
	</td>\n
	<td>\n
	  <input type="text" name="email" maxlength="50" value="$user_email">\n
	</td>\n
  </tr>\n
|;

if ($username_cookie eq "y") {
print qq|
  <tr>\n
    <td>\n
	</td>\n
	<td>\n
	  <font color="$other_color" face="$font_face" size="$font_size">\n
	    Store my name and email<input type="checkbox" name="store_user" value="1">\n
	  </font>\n
	  <br>\n
	  <br>\n
	</td>\n
  </tr>\n
|;
}

if ($replymail eq "y") {
print qq|
  <tr>\n
    <td>\n
	</td>\n
	<td>\n
	  <font color="$other_color" face="$font_face" size="$font_size">\n
	    Notify me when I get a reply to my message:\n
		<input type="radio" name="ereply" value="yes">Yes &nbsp;\n
		<input type="radio" name="ereply" value="no" checked>No\n
	  </font>\n
	  <br>\n
	  <br>\n
	</td>\n
  </tr>\n
|;
}

print qq|
  <tr>\n
    <td>\n
	  <font color="$other_color" face="$font_face" size="$font_size">\n
	    Subject:
	  </font>\n
	</td>\n
	<td>\n
	  <input type="text" name="subject" maxlength="50">\n
	</td>\n
  </tr>\n
  <tr>\n
    <td valign="top">\n
	  <font color="$other_color" face="$font_face" size="$font_size">\n
	    Message:\n
	  </font>\n
	</td>\n
	<td valign="top">
	  <textarea name="message" cols="50" rows="10" wrap="physical"></textarea>\n
      <input type="hidden" name="action" value="preview">\n
	  <input type="hidden" name="board" value="board1">\n
	</td>\n
  </tr>\n
  <tr>\n
    <td>\n
	</td>\n
	<td>\n
	  <font face="$font_face">\n
	    <input type="submit" value="Preview - Post">\n
	  </font>\n
	</td>\n
  </tr>\n
</form>\n
</table>
</td>
</tr>
</table>
|;
}

#####quick search
sub copyright {
print "<table border=\"0\"><tr><td><font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">Powered by Message Board V4 - © <a href=\"http://www.cgi-factory.com\">CGI-Factory.com</a></font></td></tr></table>"; 
}
#####################links
sub links {
print "<font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">";
print "&nbsp;Pages: ";
$link=int($total/$max);
$link2=$total%$max;	
unless ($link2==0) {
$link++;	
}
$next=0;	
$count=1;
for ($count; $count<=$link; $count++) {
if ($input{'next'}==$next) {
print "<b>$count</b> ";
$next=$next+$max;
}
else {
print "<a href=\"$cgi2?board=board1&next=$next\&ptime=$input{'ptime'}\">$count</a> ";
$next=$next+$max;	
}
}
print "</font>";
}
######################header input
sub header {
$vheader_file="$fullpath/vheader.txt";

open (header, "<$vheader_file") or &error("Unable to open the vheader file");
@header=<header>;
close(header);
print @header;
}
####################footer input
sub footer {
$vfooter_file="$fullpath/vfooter.txt";

open (footer, "<$vfooter_file") or &error("Unable to open the vfooter file");
@footer=<footer>;
close(footer);
print @footer;
}
#####error
sub error {
print "<h2>An error has occured</h2> The error is $_[0]<br>\n";	
print "Reason: $!\n<br><br>";
print "Please contact the webmaster of this web site if you keep getting this message.";	
exit;	
}

