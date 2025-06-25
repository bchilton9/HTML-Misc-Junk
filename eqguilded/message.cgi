#!/usr/bin/perl

require 'cookie.lib';
#require 'html.pl';
use DBI;
&get_html;

##################################################################################

  read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
  if (length($buffer) < 5) {
    $buffer = $ENV{QUERY_STRING};
  }
 
  @pairs = split(/&/, $buffer);
  foreach $pair (@pairs) {
    ($name, $value) = split(/=/, $pair);

    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $value =~ s/[\;\|\\ ]/ /ig;
if ($value eq "") { $value = "NULL"; }
    $INPUT{$name} = $value;
}


##################################################################################

if ($INPUT{'do'} eq "send_msg") { &send_msg; }
elsif ($INPUT{'do'} eq "send_form") { &send_form; }
elsif ($INPUT{'do'} eq "delete_message") { &delete_message; }
elsif ($INPUT{'do'} eq "view_message") { &view_message; }
elsif ($INPUT{'do'} eq "search_names") { &search_names; }
else { &messages; }

##################################################################################

sub send_msg {

&get_user;

$to = "$INPUT{'to'}";
$subject = "$INPUT{'subject'}";
$message = "$INPUT{'message'}";

$message =~ s/\n/<BR>/gi;

$from = "$user";


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="INSERT INTO `messages` ( `to` , `from` , `subject` , `message` , `date` ) 
VALUES (
'$to', '$from', '$subject', '$message', NOW())";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 


print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/Message Sent<BR><A HREF=message.cgi class=menu>Return to Message Center<\/A><BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub send_form {

print "Content-type: text/html\n\n";
$HTML{'send_form_html'} =~ s/!!to!!/$INPUT{'to'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'send_form_html'}/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub delete_message {

$from = "$INPUT{'from'}";
$subject = "$INPUT{'subject'}";
$date = "$INPUT{'date'}";

&get_user;

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$name = "$INPUT{'name'}";

$temp = "DELETE 
FROM messages
WHERE `to` = '$user' and `from` = '$from' and `subject` = '$subject' and `date` = '$date'";

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 


print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/Message Deleted<BR><A HREF=message.cgi class=menu>Return to Message Center<\/A><BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}

##################################################################################

sub view_message {

$from = "$INPUT{'from'}";
$subject = "$INPUT{'subject'}";
$date = "$INPUT{'date'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * 
FROM messages
HAVING `from` = '$from' and `subject` = '$subject' and `date` = '$date'";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 

          #$row_hit=1;

$tag = qq~
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" width=75%>
    <TR>
      <TD class=text>From:</TD>
      <TD class=cat>$row[1]</TD>
    </TR>
    <TR>
      <TD class=text>Subject:</TD>
      <TD class=cat>$row[2]</TD>
    </TR>
    <TR>
      <TD class=text COLSPAN=2>Message:</TD>
    </TR>
    <TR>
      <TD class=cat COLSPAN=2><CENTER>$row[3]</TD>
    </TR>
    <TR>
      <TD class=text>Sent:</TD>
      <TD class=cat>$row[4]</TD>
    </TR>
    <TR>
      <TD COLSPAN=2><CENTER>
<A HREF=message.cgi?do=send_form&to=$row[1] class=menu>Reply</A> <A HREF="message.cgi?do=delete_message&from=$row[1]&subject=$row[2]&date=$row[4]" class=menu>Delete</TD> 
</TD>
    </TR>
  </TABLE>
<A HREF=message.cgi class=menu>Return to Message Center</A><BR><A HREF=index.cgi class=menu>Return to Main Page</A>
</CENTER>
~;

 } 

}
$sth->finish; 
$dbh->disconnect; 


print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}

##################################################################################

sub messages {

print "Content-type: text/html\n\n";

&get_user;

$tag = qq~
<FONT class=text>Message's</FONT
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD class=textsmall>From</TD>
      <TD class=textsmall>Subject</TD>
      <TD class=textsmall>View</TD>
      <TD class=textsmall>Reply</TD>
      <TD class=textsmall>Delete</TD>
    </TR>
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * 
FROM messages
HAVING `to` = '$user'";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 

          #$row_hit=1;
$tag = "$tag <TR>";
$tag = "$tag<TD BGCOLOR=c0c0c0 class=cat>$row[1]</TD>";
$tag = "$tag<TD BGCOLOR=c0c0c0 class=cat>$row[2]</TD>";
$tag = "$tag<TD BGCOLOR=c0c0c0 class=cat><A HREF=\"message.cgi?do=view_message&from=$row[1]&subject=$row[2]&date=$row[4]\" class=menu>View</A></TD>";
$tag = "$tag<TD BGCOLOR=c0c0c0 class=cat><A HREF=message.cgi?do=send_form&to=$row[1] class=menu>Reply</A></TD>";
$tag = "$tag<TD BGCOLOR=c0c0c0 class=cat><A HREF=\"message.cgi?do=delete_message&from=$row[1]&subject=$row[2]&date=$row[4]\" class=menu>Delete</A></TD>";
$tag = "$tag</TR>";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag
</TABLE><BR>
<A HREF=index.cgi class=menu>Return to Main Page</A>

<FORM ACTION="message.cgi" METHOD="POST">
  <CENTER>
    <TABLE CELLPADDING="2" ALIGN="Center" CLASS=cat>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  Send a Message<BR>
	  <SMALL>To search enter a<BR>
	  User Name,<BR>
	  or Display Name.</SMALL></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Right>Search:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="search"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="do" VALUE="search_names">
	  <INPUT TYPE=submit VALUE="Search"> &nbsp; 
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
</CENTER>

~;

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub get_user {

&GetCookies('user');

$user = "$Cookies{'user'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from user WHERE id='$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$user{'id'} = "$user";
$user{'name'} = "$row[1]";
$user{'sur'} = "$row[2]";
$user{'pass'} = "$row[3]";
$user{'email'} = "$row[4]";
$user{'guild'} = "$row[5]";
$user{'class'} = "$row[6]";
$user{'race'} = "$row[7]";
$user{'level'} = "$row[8]";
$user{'datecreated'} = "$row[9]";
$user{'dateactave'} = "$row[10]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

}

##################################################################################

sub search_names {

$search = "$INPUT{'search'}";

$tag = "<TABLE BORDER=0 CELLPADDING=2>";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT  *
FROM  `user` 
WHERE  `id` LIKE  '$search' 
OR  `name` LIKE  '$search' 
order by `name`";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$tag = "$tag <TR class=cat><TD>$row[1] $row[2]</TD><TD><A HREF=message.cgi?do=send_form&to=$row[0] CLASS=menu>Send Message</A></TD></TR>";

 } 

}
$sth->finish; 
$dbh->disconnect;

$tag = "$tag </TABLE>";

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub get_html {


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from html";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$HTML{$row[0]} = $row[1];


 } 

}
$sth->finish; 
$dbh->disconnect; 


}