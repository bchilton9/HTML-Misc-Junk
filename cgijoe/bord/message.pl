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
#show bench mark?
$bench="0";
$require_referer_check="1";
#you may need to change the following vairables to the full system path if you are using windows servers.
$mcfg="mcfg.pl";
$mgcfg="mgcfg.pl";
$vcfg="vcfg.pl";
$enotify="enotify.pl";
$smtp_mail="smtp_mail.lib";
$superuser="superuser.db";
##############################
$start=(times)[0];
#import variables. However, use eval to avoid 500 error message 
#when something goes wrong
eval {
require "$mcfg";
require "$mgcfg";
};
if ($@) {
print "Content-type: text/html\n\n";
&error("Unable to load $mcfg and $mgcfg. Please check out the readme file.");
}
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$input{$name} = $value;
}
if ($require_referer_check ==1) {
unless ($ENV{'HTTP_REFERER'} =~ /$domain/i) {
print "Content-type: text/html\n\n";
print "<h2>Bad Referer</h2>\n";
print "You can only post a message from $domain.";
exit;
}
}
if (!$input{'action'}) {
print "Content-type: text/html\n\n";
print "<h2>Error 403 Access Forbidden</h2>\n";
exit;
}
@months = ('January','February','March','April','May','June','July','August','September','October','November','December');
@days = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');

if ($flood_control eq "y" and $input{'action'} eq "postnow") {
@nvpairs=split(/; /, $ENV{'HTTP_COOKIE'});
foreach $pair (@nvpairs) {
        ($name, $value) = split(/=/, $pair);
        $cookie{$name} = $value;
}
if ((time - $cookie{'MBflood'})<=$flood_time) {
$flood_error=1;
}
else {
&setCookie('MBflood',time);
}
}
sub setCookie {
local($cookie_name,$cookie_value) = @_;
$time=time;
$expires+=$time+2592000;
local($sec,$min,$hour,$mday,$mon,$year,$wday) = gmtime($expires);
$year+=1900;
$expires="$days[$wday], $mday-$months[$mon]-$year $hour:$min:$sec GMT";
print "Set-Cookie: $cookie_name=$cookie_value; path=/; expires= $expires;\n";
}


if ($input{'store_user'}) {
&setCookie('MBuser',"$input{'name'}|$input{'email'}");
}
print "Content-type: text/html\n\n";
open (board, "<$bdata/board1.bd") or &jump("2");	
@board=<board>;
close (board);
chomp(@board[0]);
chomp(@board[1]);
chomp(@board[2]);
$messages=@board[0];
$messages2=@board[1];
$boardname=@board[2];

if (@board[4]==0) { #check if the board is closed
&vheader;
print "<h2>Unable to post the message</h2>
This board is closed.<br><br>
<font size=\"-1\" face=\"$font_face\" color=\"$other_color\">If you believe this to be an error, please contact us at <a href=\"mailto:$yourmail\">$yourmail</a></font><br><br>";
&vfooter;
exit;
}

if (!$ENV{'REMOTE_HOST'}) {
$IP=$ENV{'REMOTE_ADDR'};
}
else {
$IP=$ENV{'REMOTE_HOST'};
}
$ctime=time();
if ($time_differ !=0) {
$ctime+= $time_differ * 3600;
}	
($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime($ctime))[0,1,2,3,4,5,6];
$sec = sprintf("%.02d",$sec);
$min = sprintf("%.02d",$min);
$hour = sprintf("%.02d",$hour);
$mday = sprintf("%.02d",$mday);
$year += 1900;
#time format
if ($date_format==1) {
$date = "$days[$wday], $months[$mon] $mday, $year<br>$hour:$min:$sec";
}
elsif ($date_format==2) {
$mon++;
$date = "$mday/$mon/$year<br>$hour:$min:$sec";	
}
else {
$mon++;
$date = "$mon/$mday/$year<br>$hour:$min:$sec";	
}
if ($input{'count'}=~ tr/;<>*|`&$!#()[]{}:'"//) {
&header;
print "<h2>Weird Symbol</h2>\n";
print "Please don't use weird symbols.<br>\n";
&footer;
exit;
}        	
$input{'email'}=lc($input{'email'});
if ($input{'action'} eq "preview") {
&preview;
}
elsif ($input{'action'} eq "postnow") {
&postnow;
}
else {
print "<h2>Error 403 Access Forbidden</h2>\n";
exit;
}
##########################preview the message first
sub preview {
&ckfields;
&vheader;

#check reserved username
open (pass, "<$fullpath/$superuser") or &error("Unable to open the superuser data.");
$pass=<pass>;
close(pass);
$compare=$input{'name'};
$compare=lc($compare);
$compare=~ s/\s//g;

chomp($pass);
@check=split(/\|/, $pass);
@check[0]=lc(@check[0]);
@check[0]=~ s/\s//g;
if ($compare eq "@check[0]" and $compare == "@check[0]") {
$admin_user=1;
$member_title="Administrator";
}
#

if ($html eq "n") {
&tran1;
}
$input{'message'}=~ s/\n/<br><!---\|abreak\|--->/g;
print "<font color=\"$other_color\" face=\"$font_face\" size=\"2\"><b>Preview Post:</b></font>\n
<table border=\"0\" width=\"$message_width\"><tr bgcolor=\"$mbar\"><td bgcolor=\"$mbar\" width=\"15%\"><font color=\"$mbar_text\" face=\"$font_face\" size=\"$font_size\">From</font></td><td bgcolor=\"$mbar\">
<font color=\"$mbar_text\" face=\"$font_face\" size=\"$font_size\">Message</font></td></tr>
<tr bgcolor=\"$mcolor2\"><td valign=\"top\"><font color=\"$mfont_color\" face=\"$font_face\" size=\"$font_size\">$input{'name'}<br>$member_title<br>";
print "&nbsp;<a href=\"mailto:$input{'email'}\"><img src=\"$email_icon\" border=\"0\" alt=\"Email\"></a>" if ($input{'email'});
print "<br><br>$date</font></td><td valign=\"top\">\n
<font color=\"$mfont_color\" face=\"$font_face\" size=\"$font_size\">
<img src=\"$default_icon\" border=\"0\"> <u>Subject: $input{'subject'}</u><br><font size=\"1\">IP: Logged</font><br><br>\n
Message:<br>$input{'message'}<br><br>$signature</font><br></td></tr></table>\n";
&tran1;
print "<form action=\"$cgi\" method=\"post\">\n";
if ($admin_user==1) {
print "<font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">The name <b>$input{'name'}</b> is currently used by the owner of this web site. 
Please enter the admin password in the box below in order to use this name.<br><br>\n
<b>Password:</b><input type=\"password\" name=\"password\"><br><br></font>\n";
}
print "<input type=\"hidden\" name=\"subject\" value=\"$input{'subject'}\">\n
<input type=\"hidden\" name=\"name\" value=\"$input{'name'}\">\n
<input type=\"hidden\" name=\"email\" value=\"$input{'email'}\">\n
<input type=\"hidden\" name=\"message\" value=\"$input{'message'}\">\n
<input type=\"hidden\" name=\"icon\" value=\"$input{'icon'}\">\n
<input type=\"hidden\" name=\"count\" value=\"$input{'count'}\">\n
<input type=\"hidden\" name=\"ereply\" value=\"$input{'ereply'}\">\n
<input type=\"hidden\" name=\"board\" value=\"board1\">\n
<input type=\"hidden\" name=\"action\" value=\"postnow\">\n
<input type=\"submit\" value=\"Post Now!\"></form>\n";
if ($bench==1) {
$end=(times)[0];
print "It took ", ($end - $start) , " second to complete this job (start: $start end $end)";
}
&vfooter;
exit;
}
###post now
sub postnow {
&ckfields;
#check reserved username
open (pass, "<$fullpath/$superuser") or &error("Unable to open the superuser data.");
if ($flock eq "y") {
flock pass, 2; 
}
$pass=<pass>;
close(pass);
chomp($pass);
$compare=$input{'name'};
$compare=lc($compare);
$compare=~ s/\s//g;
@check=split(/\|/, $pass);
@check[0]=lc(@check[0]);
@check[0]=~ s/\s//g;
if ($compare eq "@check[0]" and $compare == "@check[0]") {
$member_title="Administrator";
$input{'password'}=lc($input{'password'});  
$password=crypt("$input{'password'}", YL);
unless ($password eq "@check[1]") {
&vheader;
print "<font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\"><h2>Unable to post the message</h2>\n";
print "Incorrect Admin Password<br></font>\n";
&vfooter;
exit;
}
}
if ($html eq "n") {
&tran1;
}
$input{'message'}=~ s/&lt;br&gt;&lt;!---\|abreak\|---&gt;/<br>/g;
if (!$input{'count'}) {
&flock("$bdata/board1"."t.lock");
open (count, "<$bdata/board1.txt") or &error("Unable to open the counting file");
$count=<count>;
close (count);
&post_message("$count","$count");
open (dat, ">$messages/$count.dat") or &error("Unable to write to the data file");
print dat "$input{'subject'}\n";
print dat "0\n";
print dat "$ctime\n";
print dat "$input{'name'} \n";
print dat "$default_icon\n";
close (dat);
$count++;
&ltime;
&flock("$bdata/board1"."t.lock");
open (count, ">$bdata/board1.txt") or &error("Unable to write to the counting file");
print count "$count";
close (count);
&unflock("$bdata/board1"."t.lock");
$count--;
&vheader;
print "<font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\"><h2>Thank You!</h2> Your message has been posted.<br>\n
You can find your message <a href=\"$messages2/$count.$file_ending\">here</a>.<br>\n
Please click <a href=\"$cgi2\">here</a>, if you want to return to the message index page.<br>";
print "</font>\n";
if ($bench==1) {
$end=(times)[0];
print "It took ", ($end - $start) , " second to complete this job (start: $start end $end)";
}
&vfooter;
exit;
}
#reply
else{


&flock("$messages/$input{'count'}"."d.lock");
open (dat, "<$messages/$input{'count'}.dat") or &error("Unable to open the data file - $input{'count'}.dat");
@dat=<dat>;
close (dat);
&unflock("$messages/$input{'count'}"."d.lock");
$reply=@dat[1];
$reply++;
$display="$input{'count'}";
$hfile=$input{'count'};
$hfile="$input{'count'}\-@dat[5]" if (@dat[5]>0);
$display="$input{'count'}\-@dat[5]" if (@dat[5]>0);

#choose the color of the field
if ((@dat[1]%2)==1) {
$color=$mcolor1;
}
else {
$color=$mcolor2;
}
&flock("$messages/$input{'count'}"."h.lock");
open (html, "<$messages/$hfile.$file_ending") or &error("Unable to open the html document.");
@html=<html>;
close (html);
&unflock("$messages/$input{'count'}"."h.lock");
$line=0;
##################
foreach $html (@html) {
if ($html=~ /<!---$input{'count'}.*--->/i) {
if (!$input{'email'}) {
&flock("$messages/$input{'count'}"."e.lock");
open (email, "<$messages/$input{'count'}.email") or &create;
@notify=<email>;
close (email);
&unflock("$messages/$input{'count'}"."e.lock");
}
else {
$insert="&nbsp;<a href=\"mailto:$input{'email'}\"><img src=\"$email_icon\" border=\"0\" alt=\"Email\"></a>";
&flock("$messages/$input{'count'}"."e.lock");
open (email, "<$messages/$input{'count'}.email") or &create;
@notify=<email>;
close (email);
&unflock("$messages/$input{'count'}"."e.lock");
if ($input{'ereply'} eq "yes") {
$check=0;
foreach $notify (@notify) {
chomp($notify);
if ($input{'email'} eq "$notify") {
$check++;
}
$notify="$notify\n";
}	
if ($check==0) {
&flock("$messages/$input{'count'}"."e.lock");
open (email, ">>$messages/$input{'count'}.email") or &error("Unable to write to the data file");
print email "$input{'email'}\n";
close (email);
&unflock("$messages/$input{'count'}"."e.lock");
}
}
}
@reply="<!---reply|start:$ctime---><tr><td bgcolor=\"$color\" valign=\"top\"><font color=\"$mfont_color\" face=\"$font_face\" size=\"$font_size\">$input{'name'}<br>$member_title<br>$insert<br><br>$date<br></font></td><td valign=\"top\" bgcolor=\"$color\"><img src=\"$default_icon\" border=\"0\"> <font color=\"$mfont_color\" face=\"$font_face\" size=\"$font_size\"><u>$input{'subject'}</u><br><font size=\"1\">IP: Logged</font><br><br>\nMessage:<br>$input{'message'}<br><br>$signature<br></font></td></tr>\n<!---reply|end:$ctime--->\n<!---$input{'count'}.$file_ending--->\n";
$max_reply+=@dat[5]*$max_reply;
if ($reply>$max_reply and $max_reply !=0) {
@dat[5]+=1;
open (footer, "<$fullpath/footer.txt") or &error("Unable to open the header file");
@footer=<footer>;
close(footer);
splice (@html, $line);
if (@dat[5]>1) {
if (@dat[5]==2) {
$space="<font color=\"$mbar_text\" face=\"$font_face\" size=\"$font_size\"><a href=\"$messages2/$input{'count'}.$file_ending\">\&lt\;\&lt\;</a>Previous Page";
}
else { 
$space="<font color=\"$mbar_text\" face=\"$font_face\" size=\"$font_size\"><a href=\"$messages2/$input{'count'}\-".(@dat[5]-2).".$file_ending\">\&lt\;\&lt\;</a>Previous Page";
}
}
$pn="P ". (@dat[5]);
@html=(@html, "</td></tr></table></td></tr></table></td></tr>
<tr><td valign=\"top\" align=\"right\">","<font face=\"$font_face\" size=\"$font_size\" color=\"$mbar_text\">$space $pn Next Page<a href=\"$messages2/$input{'count'}\-@dat[5].$file_ending\">\&gt\;\&gt\;</a></font>",
"</td></tr></table></td></tr></table><br><br>", 
@footer);
&post_message("$input{'count'}\-@dat[5]","$input{'count'}");
$display="$input{'count'}\-@dat[5]";
#########
}
else {
splice (@html, $line, 1, @reply);
}
&flock("$messages/$input{'count'}"."h.lock");
open (whtml, ">$messages/$hfile.$file_ending") or &error("Unable to write to the html document.");
print whtml @html;
close (whtml);
open (IP, ">$misc/$input{'count'}_$reply.board1") or &error("Unable to write to the ip record file");
print IP "$IP";
close (IP);
&unflock("$messages/$input{'count'}"."h.lock");
&flock("$messages/$input{'count'}"."d.lock");
open (data, ">$messages/$input{'count'}.dat") or &error("Unable to write to the data file");
print data @dat[0];
print data "$reply\n";
print data "$ctime\n";
print data @dat[3];
print data @dat[4];
print data @dat[5];
close (data);
&unflock("$messages/$input{'count'}"."d.lock");
&ltime;
&vheader;
print "<font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\"><h2>Thank You!</h2> Your message has been posted.<br>\n
You can find your message <a href=\"$messages2/$display.$file_ending\">here</a>.<br>\n
Please click <a href=\"$cgi2?board=board1\">here</a>, if you want to return to the message index page.<br></font>\n";
if ($bench==1) {
$end=(times)[0];
print "It took ", ($end - $start) , " second to complete this job (start: $start end $end)";
}
&vfooter;
if ($replymail eq "y") {
&notifymail;
}	
exit;
}
$line++;
}
}
###########
&vheader;
print "<font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\"><h2>Unable to post the message</h2>\n
The following line could not be found in the page that you were trying to post a reply message<br>\n
&lt;!---$input{'count'}.$file_ending---&gt;<br>
Please report this problem to the webmaster of the web site.</font>";
&vfooter;
exit;
}
sub post_message {
local($file,$count)=@_;
$re="RE: " if ($file eq $count);
if (@dat[5] > 1) {
$tlink="$input{'count'}\-".(@dat[5]-1);
}
else {
$tlink="$input{'count'}";
}
if ($input{'count'}) {
if ((@dat[1]%2)==1) {
$color=$mcolor1;
}
else {
$color=$mcolor2;
}
}
else {
$color=$mcolor1;
}
&unflock("$bdata/board1"."t.lock");
chomp ($count);

open (html, ">$messages/$file.$file_ending") or &error("Unable to create the html document.");
&header;
print html"<table bgcolor=\"$mtable_background_color\" border=\"0\" cellpadding=\"0\" cellspacing=\"1\" width=\"$message_width\">
      <tr width=\"100%\">
        <td>
          <table width=\"100%\" bgcolor=\"$mtitle_bar_color\" cellpadding=\"0\" cellspacing=\"0\" border=\"0\">
            <tr>
              <td align=\"left\">
			    <font face=\"$font_face\" size=\"2\" color=\"$mtitle_bar_text_color\"><b>$boardname [ </b></font>
                <a href=\"$cgi2\"><b>return</b></a>
				<font face=\"$font_face\" size=\"2\" color=\"$mtitle_bar_text_color\"><b>]</b></font>
              </td></tr>";
print html "<tr width=\"100%\"><td><table bgcolor=\"$minner_table_background_color\" border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\"><tr><td><table border=\"0\" width=\"100%\" cellspacing=\"1\" cellpadding=\"0\"><tr bgcolor=\"$mbar\"><td width=\"15%\"><font color=\"$mbar_text\" face=\"$font_face\" size=\"$font_size\">From</font></td><td><font color=\"$mbar_text\" face=\"$font_face\" size=\"$font_size\">Message</font></td></tr>
<tr><td valign=\"top\" bgcolor=\"$color\"><font color=\"$mfont_color\" face=\"$font_face\" size=\"$font_size\">";
if (!$input{'email'}) {
open (email, ">$messages/$count.email") or &error("Unable to write to the data file");
close (email);
}
else {
if ($input{'ereply'} eq "yes") {
open (email, ">$messages/$count.email") or &error("Unable to write to the data file");
print email "$input{'email'}\n";
close (email);
}
}
print html "$input{'name'}<br>$member_title<br>";
print html "&nbsp;<a href=\"mailto:$input{'email'}\"><img src=\"$email_icon\" border=\"0\" alt=\"Email\"></a>" if ($input{'email'});
print html "<br><br>$date<br></font></td><td bgcolor=\"$color\" valign=\"top\">\n
<font color=\"$mfont_color\" face=\"$font_face\" size=\"$font_size\">
<img src=\"$default_icon\" border=\"0\"> <u>Subject: $input{'subject'}</u><br><font size=\"1\">IP: Logged</font><br><br>\n
Message:<br>$input{'message'}<br><br>$signature<br></font></td></tr>\n
<!---$count.$file_ending--->\n
</td></tr></table></td></tr></table></td></tr>
<tr><td valign=\"top\" align=\"right\"><font color=\"$mbar_text\" face=\"$font_face\" size=\"$font_size\">";
print html "<a href=\"$messages2/$input{'count'}.$file_ending\">\&lt\;\&lt\;</a>Original Post <a href=\"$messages2/$tlink.$file_ending\">\&lt\;\&lt\;</a>Previous Page" if (@dat[5]);
print html "<font color=\"$mtitle_bar_text_color\" face=\"$font_face\" size=\"$font_size\"> P ".(@dat[5]+1)."</b></font></td></tr></table></td></tr></table>
<br>
<br>
<table border=\"0\" cellspacing=\"0\">
  <tr bgcolor=\"$mtitle_bar_color\">
    <td>
      <font color=\"$mtitle_bar_text_color\" face=\"$font_face\" size=\"2\">
        <b>Post a reply to this message:</b>
	  </font>
	</td>
	<td>
	</td>
  </tr>
  <tr>
    <td>";

print html "<table border=\"0\">\n
<form action=\"$cgi\" name=\"REPLYFORM\" method=\"post\">\n
<tr><td><font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">Name:</font></td><td><input type=\"text\" name=\"name\" maxlength=\"20\"></td></tr>\n
<tr><td><font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">Email:</font></td><td><input type=\"text\" name=\"email\" maxlength=\"50\"></td></tr>\n";
if ($replymail eq "y") {
print html "<tr><td></td><td><font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">Notify me when I get a reply to my message:<input type=\"radio\" name=\"ereply\" value=\"yes\">Yes &nbsp;<input type=\"radio\" name=\"ereply\" value=\"no\" checked>No</font><br><br></td></tr>\n";
}
print html "<tr><td><font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">Subject:</font></td><td><input type=\"text\" name=\"subject\" value=\"$re$input{'subject'}\" size=\"30\" maxlength=\"50\"></td></tr>\n
<tr><td valign=\"top\"><font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\">Message:</font></td><td><textarea name=\"message\" cols=\"50\" rows=\"10\" wrap=\"physical\"></textarea></td></tr>\n
<input type=\"hidden\" name=\"count\" value=\"$count\">\n
<input type=\"hidden\" name=\"board\" value=\"board1\"><input type=\"hidden\" name=\"action\" value=\"preview\">\n
<tr><td></td><td><font face=\"$font_face\"><input type=\"submit\" value=\"Preview / Post\"></font></form></td></tr></table></td></tr></table>\n";
print html "<script language = \"JavaScript\" src =\"$cookie_js\"></script>" if ($username_cookie eq "y");
&footer;
close (html);
open (IP, ">$misc/$count"."_0.board1") or &error("Unable to write to the ip record file");
print IP "$IP";
close (IP);
##############################3
}
sub create {
open (create, ">$messages/$input{'count'}.email") or &error("Unable to create the data file");
close (create);	
}
##################sub check fields
sub ckfields {
if ($input{'icon'}) {
$default_icon=$input{'icon'};
}
$e_count="0";
if ($input{'name'}=~ tr/;<>*|`&$!#()[]{}:'"//) {
$e_count++;
&cerror("Weird symbols or HTML tags are not allowed in the name field.<br>\n");
}   
if ($input{'email'}=~ tr/;<>*|`&$!#()[]{}:'"//) {
$e_count++;
&cerror("Weird symbols or HTML tags are not allowed in the name field.<br>\n");
}
if (!$input{'subject'}) {
if ($require_subject eq "y") {
$e_count++;
&cerror("The subject field is missing.<br>\n");
}
$input{'subject'}= "No Subject";
}
if (!$input{'name'}) {
if ($require_name eq "y") {
$e_count++;
&cerror("The name field is missing.<br>\n");
}
$input{'name'}= "Anonymous";
}
if ($require_email eq "y") {
if (!$input{'email'}) {
$e_count++;
&cerror("The email field is missing.<br>\n");
}
}
if ($input{'email'}) {
unless ($input{'email'}=~/.*\@.*/)   { 
$e_count++;
&cerror("You have entered an invalid email address.<br>\n");
}
}
if (!$input{'message'}) {
$e_count++;
&cerror("The message field is missing<br>\n");
}
sub cerror {
if ($e_count==1) {
&vheader;
print "<font color=\"$other_color\" face=\"$font_face\" size=\"$font_size\"><h2>Unable to post the message</h2>\n";
}
print "$_[0]";
}
if ($e_count>0) {
print "<font>";
&vfooter;
exit;
}
}
###tag handling.
sub tran1 {
$input{'subject'}=~ s/</&lt;/g;
$input{'subject'}=~ s/>/&gt;/g;
$input{'message'}=~ s/</&lt;/g;
$input{'message'}=~ s/>/&gt;/g;
$input{'subject'}=~ s/"/&quot;/g;
$input{'message'}=~ s/"/&quot;/g;
}
sub tran2 {
$input{'subject'}=~ s/&lt;/</g;
$input{'subject'}=~ s/&gt;/>/g;
$input{'message'}=~ s/&lt;/</g;
$input{'message'}=~ s/&gt;/>/g;
$input{'subject'}=~ s/&quot;/"/g;
$input{'message'}=~ s/&quot;/"/g;
}

##record time
sub ltime {
&flock("$bdata/board1"."l.lock");
open (ltime, ">$bdata/board1.ltime") or &error("Unable to write to board1.ltime");
print ltime $ctime;
close(ltime);
&unflock("$bdata/board1"."l.lock");
}
######################header input
sub header {
$header_file="$fullpath/header.txt";

open (header, "<$header_file") or &error("Unable to open the header file");
@header=<header>;
close(header);
foreach $header(@header) {
$header=~ s/<subject>/$input{'subject'}/;
print html "$header";
}
}
####################footer input
sub footer {

$footer_file="$fullpath/footer.txt";

open (footer, "<$footer_file") or &error("Unable to open the footer file");
@footer=<footer>;
close(footer);
print html @footer;
}
######################vheader input
sub vheader {

$vheader_file="$fullpath/vheader.txt";

open (vheader, "<$vheader_file") or &error("Unable to open the vheader file");
@vheader=<vheader>;
close(vheader);
print @vheader;
}
####################footer input
sub vfooter {
$vfooter_file="$fullpath/vfooter.txt";
open (vfooter, "<$vfooter_file") or &error("Unable to open the vfooter file");
@vfooter=<vfooter>;
close(vfooter);
print @vfooter;
}
#notify mail
sub notifymail {
eval {
require "$enotify";
};
if ($@) {
&error("Unable to load $enotify. Please check out the readme file.");
}

if (@notify) {
$date=~ s/<br>/ /;
$date=~ s/<b>//;
$date=~ s/<\/b>//;

if ($mail_option==1) {
foreach $notify (@notify) {
$notify=~s /$input{'email'}//i;	
}
@notify=join(",", @notify);
eval {
require "$smtp_mail";
};
if ($@) {
&error("Unable to load $smtp_mail. Please check out the readme file.");
}
&smtp_mail(@notify,$yourmail,$esub,$mailprog,$econtent);
}
else {
foreach $notify (@notify) {
chomp ($notify);
if ($notify ne "$input{'email'}") {
open (MAIL, "|$mailprog") or &error("Can't open the mail program!");
print MAIL "To: $notify\n";
print MAIL "From: $yourmail\n";
print MAIL "Subject: $esub\n\n";
print MAIL "$econtent"; 
close(MAIL);
}
}
}  
}
}
#filelock
sub flock
  {
  local ($lock_file) = @_;
  local ($timeout);

  $timeout=20;
  while (-e $lock_file && 
        (stat($lock_file))[9]+$timeout>time)
  { sleep(1);}
 
  open LOCK_FILE, ">$lock_file" 
    or &error("Unable to create $lock_file");
}

sub unflock
  {
  local ($lock_file) = @_;

  close(LOCK_FILE);
  unlink($lock_file);
  }
#####error
sub error {
print "<h2>An error has occured</h2> The error is $_[0]<br>\n";	
print "$!\n<br><br>";
print "Please contact the webmaster of this web site if you keep getting this message.";	
exit;	
}



