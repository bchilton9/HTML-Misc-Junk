#!/usr/bin/perl

require 'cookie.lib';
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
    $INPUT{$name} = $value;
}

##################################################################################

if ($INPUT{'do'} eq "useredit_b") { &useredit_b; }
elsif ($INPUT{'do'} eq "edit_form") { &edit_form; }
elsif ($INPUT{'do'} eq "edit_guild") { &edit_guild; }
elsif ($INPUT{'do'} eq "save_guild") { &save_guild; }
elsif ($INPUT{'do'} eq "set_guild_b") { &set_guild_b; }
elsif ($INPUT{'do'} eq "set_guild_c") { &set_guild_c; }
elsif ($INPUT{'do'} eq "guild_remove") { &guild_remove; }
elsif ($INPUT{'do'} eq "guild_edit_html") { &guild_edit_html; }
elsif ($INPUT{'do'} eq "guild_edit_html_b") { &guild_edit_html_b; }
elsif ($INPUT{'do'} eq "guild_edit_html_c") { &guild_edit_html_c; }
elsif ($INPUT{'do'} eq "guild_edit_page") { &guild_edit_page; }
elsif ($INPUT{'do'} eq "guild_edit_page_b") { &guild_edit_page_b; }
elsif ($INPUT{'do'} eq "guild_edit_page_c") { &guild_edit_page_c; }
elsif ($INPUT{'do'} eq "guild_edit_page_d") { &guild_edit_page_d; }
elsif ($INPUT{'do'} eq "guild_aprove_member") { &guild_aprove_member; }
elsif ($INPUT{'do'} eq "guild_aprove_member_b") { &guild_aprove_member_b; }
elsif ($INPUT{'do'} eq "guild_edit_member") { &guild_edit_member; }
elsif ($INPUT{'do'} eq "guild_edit_member_b") { &guild_edit_member_b; }
elsif ($INPUT{'do'} eq "guild_edit_member_c") { &guild_edit_member_c; }
elsif ($INPUT{'do'} eq "guild_add_news") { &guild_add_news; }
elsif ($INPUT{'do'} eq "guild_add_news_b") { &guild_add_news_b; }
elsif ($INPUT{'do'} eq "guild_delete_news") { &guild_delete_news; }
elsif ($INPUT{'do'} eq "guild_delete_news_b") { &guild_delete_news_b; }
elsif ($INPUT{'do'} eq "guild_message_member") { &guild_message_member; }
elsif ($INPUT{'do'} eq "guild_message_member_b") { &guild_message_member_b; }
elsif ($INPUT{'do'} eq "guild_edit_info") { &guild_edit_info; }
elsif ($INPUT{'do'} eq "guild_edit_info_b") { &guild_edit_info_b; }
elsif ($INPUT{'do'} eq "guild_edit_counter") { &guild_edit_counter; }
elsif ($INPUT{'do'} eq "guild_edit_counter_b") { &guild_edit_counter_b; }
elsif ($INPUT{'do'} eq "guild_delete_forum") { &guild_delete_forum; }
elsif ($INPUT{'do'} eq "guild_delete_forum_b") { &guild_delete_forum_b; }
elsif ($INPUT{'do'} eq "guild_add_forum") { &guild_add_forum; }
elsif ($INPUT{'do'} eq "guild_add_forum_b") { &guild_add_forum_b; }

else { &options; }

##################################################################################

sub guild_add_forum {
print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'add_forum_html'}/gi;
print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_add_forum_b {

$desc = "$INPUT{'desc'}";
$forum = "$INPUT{'forum'}";

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild forums";
$database =~ s/ /_/gi;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp = "INSERT INTO `$database` ( `id` , `forum` , `description` ) VALUES ('', '$forum', '$desc')"; 
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_save_forum_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_delete_forum {
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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild forums";
$database =~ s/ /_/gi;

$tag = qq~
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Name</TD>
      <TD>Description</TD>
      <TD></TD>
    </TR>
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$tag = qq~ $tag
    <TR>
      <TD>$row[1]</TD>
      <TD>$row[2]</TD>
      <TD><A HREF="useredit.cgi?do=guild_delete_forum_b&forum=$row[1]&database=$database">Delete</A></TD>
    </TR>
~;

 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag
  </TABLE>
</CENTER>
~;


print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_delete_forum_b {

$database = "$INPUT{'database'}";
$forum = "$INPUT{'forum'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp = "DELETE FROM `$database` WHERE `forum` = '$forum' LIMIT 1"; 
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_delete_forum_b_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_counter {
print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_edit_counter_html'}/gi;
print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_edit_counter_b {

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$counter = "$INPUT{'counter'}";

my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 
$temp="UPDATE `guild` SET `counterimage` = '$counter' WHERE `shortname` = '$guild' LIMIT 1 ;";
$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_save_counter_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_info {
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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild WHERE `shortname` = '$guild'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$longname = "$row[1]";
$password = "$row[2]";
$email = "$row[3]";

 } 

}
$sth->finish; 
$dbh->disconnect; 

$HTML{'guild_edit_info_html'} =~ s/!!longname!!/$longname/gi;
$HTML{'guild_edit_info_html'} =~ s/!!password!!/$password/gi;
$HTML{'guild_edit_info_html'} =~ s/!!email!!/$email/gi;
$HTML{'guild_edit_info_html'} =~ s/!!guild!!/$guild/gi;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_edit_info_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_info_b {

$longname = "$INPUT{'longname'}";
$password = "$INPUT{'password'}";
$email = "$INPUT{'email'}";
$guild = "$INPUT{'guild'}";

my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 
$temp="UPDATE `guild` SET `longname` = '$longname', `password` = '$password', `email` = '$email' WHERE `shortname` = '$guild' LIMIT 1 ;";
$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_info_saved_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_message_member {

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_message_member_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_message_member_b {

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild user";
$database =~ s/ /_/gi;
$message = "$INPUT{'message'}";
$subject = "$INPUT{'subject'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

if ($INPUT{'sendto'} eq "All") {
$temp ="select * from `$database`";
}
else {
$temp ="select * from `$database` WHERE `type` = 'Officer'";
}

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1; 


my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 
$temp="INSERT INTO `messages` ( `to` , `from` , `subject` , `message` , `date` ) 
VALUES (
'$row[0]', '$user', '$subject', '$message', NOW())";
$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;



 } 

}
$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_messages_sent_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_delete_news {
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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild news";
$database =~ s/ /_/gi;


$tag = qq~ $tag
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class=cat>
    <TR>
      <TD>Date</TD>
      <TD>News</TD>
      <TD></TD>
    </TR>
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT  * 
FROM  `$database` 
ORDER BY `date` DESC";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$tag = qq~ $tag
    <TR>
      <TD>$row[0]</TD>
      <TD>$row[1]</TD>
      <TD><A HREF="JavaScript:if (window.confirm('Are you sure you want to delete this news?')) { window.location.href = '?do=guild_delete_news_b&date=$row[0]&news=$row[1]&database=$database' }" CLASS=menu>Delete</A></TD>
    </TR>
~;

 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag

  </TABLE>
</CENTER>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_delete_news_b {

$database = "$INPUT{'database'}";
$date = "$INPUT{'date'}";
$news = "$INPUT{'news'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="DELETE FROM `$database` WHERE `date` = '$date' AND `news` = '$news' LIMIT 1"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_delere_news_html'}/gi;

print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_add_news {

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_add_news_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_add_news_b {
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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild news";
$database =~ s/ /_/gi;

$news = "$INPUT{'news'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="INSERT INTO $database ( `date` , `news` ) VALUES (NOW( ) , '$news')"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_add_news_b_html'}/gi;

print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_edit_member {
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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild user";
$database =~ s/ /_/gi;

$rankdatabase = "$guild ranks";
$rankdatabase =~ s/ /_/gi;

$tag = qq~
<CENTER>
  <TABLE BORDER="0" CELLSPACING="3" CELLPADDING="3" ALIGN="Center" class=cat>
<TR>
<TD>Name</TD>
<TD>Access</TD>
<TD>Rank</TD>
<TD>Type</TD>
<TD>Points</TD>
<TD></TD>
<TD></TD>
</TR>
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from `$database` WHERE `aproved` = 'true' ORDER BY name";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1; 

$tag = qq~ $tag
<TR><TD>$row[0]</TD>
<TD>$row[1]</TD>
<TD>$row[2]</TD>
<TD>$row[3]</TD>
<TD>$row[4]</TD>
<TD><A HREF="?do=guild_edit_member_b&name=$row[0]&action=edit&database=$database&rankdatabase=$rankdatabase" class=menu>Edit</A></TD><TD>
~;

if ($row[1] eq "Master") {
$tag = qq~ $tag
Master
~;
}
else {
$tag = qq~ $tag
<A HREF="?do=guild_edit_member_c&name=$row[0]&action=delete&database=$database" class=menu>Delete</A></TD></TR>
~;
}

 } 

}
$sth->finish; 
$dbh->disconnect; 




$tag = qq~ $tag

    </TABLE>
</CENTER>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_edit_member_b {

$rankdatabase = "$INPUT{'rankdatabase'}";
$database = "$INPUT{'database'}";
$name = "$INPUT{'name'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database WHERE name='$name'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$access = "$row[1]";
$rank = "$row[2]";
$type = "$row[3]";

 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~
<FORM ACTION="useredit.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name:</TD>
	<TD>$name
	  <INPUT TYPE="hidden" NAME="name" VALUE="$name"></TD>
      </TR>
      <TR>
	<TD>Access:</TD>
	<TD>
	  
~;

if ($access eq "Master") {
$tag = qq~ $tag
Master<INPUT TYPE="hidden" NAME="access" VALUE="Master">
~;
}
elsif ($access eq "Administrator") {
$tag = qq~ $tag
<SELECT NAME="access">
<OPTION SELECTED>Administrator
<OPTION>Modarator
<OPTION>Member
</SELECT>
~;
}
elsif ($access eq "Modarator") {
$tag = qq~ $tag
<SELECT NAME="access">
<OPTION>Administrator
<OPTION SELECTED>Modarator
<OPTION>Member
</SELECT>
~;
}
else {
$tag = qq~ $tag
<SELECT NAME="access">
<OPTION>Administrator
<OPTION>Modarator
<OPTION SELECTED>Member
</SELECT>
~;
}

$tag = qq~ $tag
</TD>
      </TR>
      <TR>
	<TD>Rank:</TD>
	<TD>
	  <SELECT NAME="rank">
~;


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $rankdatabase";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] eq "$rank") {
$tag = qq~ $tag <OPTION SELECTED>$row[0]
~;
}
else {
$tag = qq~ $tag <OPTION>$row[0]
~;
}

 } 

}
$sth->finish; 
$dbh->disconnect; 


$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD>Type:</TD>
	<TD>
	  <SELECT NAME="type">
~;

if ($type eq "Officer") {
$tag = qq~ $tag <OPTION SELECTED>Officer
<OPTION>Member
~;
}
else {
$tag = qq~ $tag <OPTION>Officer
<OPTION SELECTED>Member
~;
}

$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden name=do value=guild_edit_member_c>
<INPUT TYPE=hidden name=database value=$INPUT{'database'}>
	  <INPUT TYPE=submit VALUE="Save"> &nbsp; 
	  <INPUT TYPE=reset VALUE="Start Over"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_member_c {

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($guild eq "$row[0]") {
$guildname = "$row[1]";
}


 } 

}
$sth->finish; 
$dbh->disconnect;

$database = "$INPUT{'database'}";
$name = "$INPUT{'name'}";
$acc = "$INPUT{'access'}";
$rank = "$INPUT{'rank'}";
$type = "$INPUT{'type'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

if ($INPUT{'action'} eq "delete") {
$temp="DELETE FROM `$database` WHERE `name` = '$name' LIMIT 1";
}
else {
$temp="UPDATE `$database` SET `access` = '$acc', `rank` = '$rank', `type` = '$type' WHERE `name` = '$name' LIMIT 1";  
}

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 


if ($INPUT{'action'} eq "delete") {

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="UPDATE `user` SET `guild` = '' WHERE `id` = '$name' LIMIT 1"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 


$message = qq~
The officers of $guildname have decided to remove you from $guildname!
<P>
EQ Guilded has no choice over this decishion. If you feal it is in error please contact your guilds Leader/Officers.
~;

$subject = "Removel from $guildname";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="INSERT INTO `messages` ( `to` , `from` , `subject` , `message` , `date` ) 
VALUES (
'$name', '$user', '$subject', '$message', NOW())";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;

}

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_edit_member_c_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_aprove_member {
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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild user";
$database =~ s/ /_/gi;

$tag = qq~
<CENTER>
  <TABLE BORDER="0" CELLSPACING="3" CELLPADDING="3" ALIGN="Center" class=cat>
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from `$database` WHERE `aproved` = 'false'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1; 

$tag = qq~ $tag
<TR><TD>$row[0]</TD><TD>
<A HREF="?do=guild_aprove_member_b&name=$row[0]&action=aprove&database=$database" class=menu>APROVE</A></TD><TD>
<A HREF="?do=guild_aprove_member_b&name=$row[0]&action=decline&database=$database" class=menu>DECLINE</A></TD></TR>
~;

 } 

}
$sth->finish; 
$dbh->disconnect; 




$tag = qq~ $tag

    </TABLE>
</CENTER>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";
}

##################################################################################

sub guild_aprove_member_b {

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($guild eq "$row[0]") {
$guildname = "$row[1]";
}


 } 

}
$sth->finish; 
$dbh->disconnect;


$database = "$INPUT{'database'}";
$name = "$INPUT{'name'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

if ($INPUT{'action'} eq "aprove") {
$temp="UPDATE `$database` SET `aproved` = 'true' WHERE `name` = '$name' LIMIT 1 "; 
}
else {
$temp="DELETE FROM `$database` WHERE `name` = '$name' LIMIT 1"; 
}

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 


if ($INPUT{'action'} eq "decline") {

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="UPDATE `user` SET `guild` = '' WHERE `id` = '$name' LIMIT 1"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

}

$message = qq~
The officers of $guildname have decided to $INPUT{'action'} your request to join $guildname!
<P>
~;
if ($INPUT{'action'} eq "aprove") {
$message = qq~ $message
You may now go to there website <A HREF=http://www.eqguilded.com/$guild>http://www.eqguilded.com/$guild</A>
~;
}
else {
$message = qq~ $message
EQ Guilded has no choice over this decishion. If you feal it is in error please contact the guild for witch you aplyed for.
~;
}

$subject = "Aproval status for $guildname";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="INSERT INTO `messages` ( `to` , `from` , `subject` , `message` , `date` ) 
VALUES (
'$name', '$user', '$subject', '$message', NOW())";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect;


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'guild_aproved_member_b_html'}/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################
####### STOPED HTML TEMPLETS HERE
##################################################################################

sub guild_edit_page {

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild pages";
$database =~ s/ /_/gi;

$tag = qq~
Please chose a page to edit!<BR>
<A HREF=commands.html onclick="NewWindow(this.href,'name','410','300','yes');return false;" class=menu>View a list of commands you can use!</A>
<FORM ACTION="useredit.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Page:</TD>
	<TD>
	  <SELECT NAME="templet">
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$tag = "$tag <OPTION>$row[0]\n";
 } 

}
$sth->finish; 
$dbh->disconnect; 




$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME="new" VALUE="false">
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_page_b">
<INPUT TYPE=hidden NAME="database" VALUE="$database">
	  <INPUT TYPE=submit VALUE="Edit Page"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
Add a new page<BR>
<FORM ACTION="useredit.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Page name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="templet"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_page_b">
<INPUT TYPE=hidden NAME="database" VALUE="$database">
<INPUT TYPE=hidden NAME="new" VALUE="true">
	  <INPUT TYPE=submit VALUE="Add Page">
	  &nbsp;
	  <INPUT TYPE=reset VALUE="Start Over"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>

Delete a page!<BR>
<FORM ACTION="useredit.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Page:</TD>
	<TD>
	  <SELECT NAME="templet">
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$tag = "$tag <OPTION>$row[0]\n";
 } 

}
$sth->finish; 
$dbh->disconnect; 




$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_page_d">
<INPUT TYPE=hidden NAME="database" VALUE="$database">
	  <INPUT TYPE=submit VALUE="Delete Page" onclick="return confirm('Are you sure you want to delete this page? Files are NOT abel to be recovered!');"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_page_b {

$database = "$INPUT{'database'}";
$templet = "$INPUT{'templet'}";

$tag = qq~
<FORM ACTION="useredit.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class=cat>
      <TR>
	<TD><P ALIGN=Center>
	  Editing Page "$templet"</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
	  <TEXTAREA NAME="content" ROWS="30" COLS="60" onFocus="replaceCharsB(document.subform.content.value);">
~;

if ($INPUT{'new'} eq "false") {

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] eq "$templet") {
$row[1] =~ s/TEXTAREA/TXTXTXT/gi;
$tag = "$tag $row[1]\n";
}

 } 

}
$sth->finish; 
$dbh->disconnect; 

}

$tag = qq~ $tag
</TEXTAREA></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT TYPE=hidden NAME="new" VALUE="$INPUT{'new'}">
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_page_c">
<INPUT TYPE=hidden NAME="database" VALUE="$database">
<INPUT TYPE=hidden NAME="templet" VALUE="$templet">
<input type="button" value="Preview" onclick="displayHTML(this.form)"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=submit VALUE="Save Templet" onClick="replaceChars(document.subform.content.value);"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=reset VALUE="Start Over"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_page_c {

$database = "$INPUT{'database'}";
$templet = "$INPUT{'templet'}";
$content = "$INPUT{'content'}";
$content =~ s/'/\\'/gi;
$content =~ s/XZXZXZX/\\;/gi;
($guild, $junk) = split(/_/, $database);

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($guild eq "$row[0]") {
$server = "$row[8]";
}
 } 
}
$sth->finish; 
$dbh->disconnect; 

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

if ($INPUT{'new'} eq "false") {
$temp="UPDATE `$database` SET `content` = '$content' WHERE `name` = '$templet' LIMIT 1 "; 
}
else {
$temp="INSERT INTO `$database` ( `name` , `content` ) VALUES ('$templet', '$content')"; 
}

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

$tag = qq~
Page Saved!<BR>
URL to your page is:<BR>
<A HREF=http://www.eqguilded.com/$server/$guild/page.cgi?view=$templet class=menu>http://www.eqguilded.com/$server/$guild/page.cgi?view=$templet</A>
<P>
<A HREF=?do=guild_edit_page class=menu>Edit Another Page</A><BR>
<A HREF=?do=edit_guild class=menu>Return to edit guild</A><BR>
<A HREF=index.cgi class=menu>Return to EQ Guilded</A>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_page_d {

$database = "$INPUT{'database'}";
$templet = "$INPUT{'templet'}";



my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 


$temp="DELETE FROM `$database` WHERE `name` = '$templet' LIMIT 1"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

$tag = qq~
Page Deleted!
<P>
<A HREF=?do=guild_edit_page class=menu>Edit Another Page</A><BR>
<A HREF=?do=edit_guild class=menu>Return to edit guild</A><BR>
<A HREF=index.cgi class=menu>Return to EQ Guilded</A>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_html {

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
$guild = "$row[5]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

$database = "$guild html";
$database =~ s/ /_/gi;

$tag = qq~
Please chose a templet to edit!<BR>
<FORM ACTION="useredit.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Templet:</TD>
	<TD>
	  <SELECT NAME="templet">
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database order by `name`";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$tag = "$tag <OPTION>$row[0]\n";
 } 

}
$sth->finish; 
$dbh->disconnect; 




$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_html_b">
<INPUT TYPE=hidden NAME="database" VALUE="$database">
	  <INPUT TYPE=submit VALUE="Edit HTML"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>

~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}
##################################################################################

sub guild_edit_html_b {

$database = "$INPUT{'database'}";
$templet = "$INPUT{'templet'}";

$tag = qq~
<A HREF=commands.html onclick="NewWindow(this.href,'name','410','300','yes');return false;" class=menu>View a list of commands you can use!</A>
<FORM ACTION="useredit.cgi" METHOD="POST" name="subform">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class=cat>
      <TR>
	<TD><P ALIGN=Center>
	  Editing Templet "$templet"</TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
	  <TEXTAREA NAME="content" ROWS="30" COLS="60" onFocus="replaceCharsB(document.subform.content.value);">
~;


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] eq "$templet") {
$row[1] =~ s/TEXTAREA/TXTXTXT/gi;
$tag = "$tag $row[1]\n";
$useheader = "$row[2]";
}

 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag
</TEXTAREA></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
<INPUT TYPE=hidden NAME="do" VALUE="guild_edit_html_c">
<INPUT TYPE=hidden NAME="useheader" VALUE="$useheader">
<INPUT TYPE=hidden NAME="database" VALUE="$database">
<INPUT TYPE=hidden NAME="templet" VALUE="$templet">
<input type="button" value="Preview" onclick="displayHTML(this.form)"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=submit VALUE="Save Templet" onClick="replaceChars(document.subform.content.value);"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=reset VALUE="Start Over"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;

$tag =~ s/!!HEADBANNER!!//s;
$tag =~ s/!!FOOTBANNER!!//s;
$tag =~ s/!!headbanner!!//s;
$tag =~ s/!!footbanner!!//s;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub guild_edit_html_c {

$database = "$INPUT{'database'}";
$templet = "$INPUT{'templet'}";
$content = "$INPUT{'content'}";
$content =~ s/'/\\'/gi;
$content =~ s/XZXZXZX/\\;/gi;

if ($INPUT{'useheader'} eq "true") {

if ($content =~ /<body([^>]*)>/i) { 
$content =~ s/<body([^>]*)>/<body$1>!!HEADBANNER!!/i;
}
else {
$content = "!!HEADBANNER!! $content";
}
if ($content =~ /<\/body>/i) { 
$content =~ s/<\/body>/!!FOOTBANNER!!<\/body>/i;
}
else {
$content = "$content !!FOOTBANNER!!";
}

}

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="UPDATE `$database` SET `content` = '$content' WHERE `name` = '$templet' LIMIT 1 "; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

$tag = qq~
Templet Saved!
<P>
<A HREF=?do=guild_edit_html class=menu>Edit Another Templet</A><BR>
<A HREF=?do=edit_guild class=menu>Return to edit guild</A><BR>
<A HREF=index.cgi class=menu>Return to EQ Guilded</A>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################
sub useredit_b {

if ($INPUT{'sur'} eq "NULL") {
$INPUT{'sur'} = "";
}
if ($INPUT{'level'} eq "NULL") {
$INPUT{'level'} = "";
}

$user = "$INPUT{'user'}";
$name = "$INPUT{'name'}";
$sur = "$INPUT{'sur'}";
$pass = "$INPUT{'pass'}";
$email = "$INPUT{'email'}";
$class = "$INPUT{'class'}";
$race = "$INPUT{'race'}";
$level = "$INPUT{'level'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="UPDATE `user` SET `name` = '$name',
`sur` = '$sur',
`password` = '$pass',
`email` = '$email',
`class` = '$class',
`race` = '$race',
`level` = '$level' WHERE `id` = '$user' LIMIT 1
"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/Changes Saved<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################

sub edit_form {

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
$user = "$row[0]";
$name = "$row[1]";
$sur = "$row[2]";
$pass = "$row[3]";
$email = "$row[4]";
$class = "$row[6]";
$race = "$row[7]";
$level = "$row[8]";
 } 

}
$sth->finish; 
$dbh->disconnect; 


print "Content-type: text/html\n\n";

$HTML{'edit_form_html'} =~ s/!!user!!/$user/gi;
$HTML{'edit_form_html'} =~ s/!!name!!/$name/gi;
$HTML{'edit_form_html'} =~ s/!!email!!/$email/gi;
$HTML{'edit_form_html'} =~ s/!!pass!!/$pass/gi;
$HTML{'edit_form_html'} =~ s/!!level!!/$level/gi;
$HTML{'edit_form_html'} =~ s/!!race!!/$race/gi;
$HTML{'edit_form_html'} =~ s/!!class!!/$class/gi;
$HTML{'edit_form_html'} =~ s/!!sur!!/$sur/gi;

$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'edit_form_html'}/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub edit_guild {

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
$user = "$row[0]";
$name = "$row[1]";
$sur = "$row[2]";
$pass = "$row[3]";
$email = "$row[4]";
$guild = "$row[5]";
$class = "$row[6]";
$race = "$row[7]";
$level = "$row[8]";
 } 

}
$sth->finish; 
$dbh->disconnect; 

if ($guild eq "") {

$tag = "$tag Please Chose Your Server.<BR><FORM ACTION=useredit.cgi METHOD=POST>";
$tag = "$tag <P ALIGN=Center>";
$tag = "$tag <SMALL>Server: </SMALL><SELECT NAME=server>";



my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM server ORDER BY server";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
        $row_hit=1;
$tag = "$tag <OPTION>$row[0]\n";
 } 

}
$sth->finish; 
$dbh->disconnect; 



$tag = "$tag </SELECT>";
$tag = "$tag <INPUT TYPE=submit VALUE=Go>";
$tag = "$tag <INPUT TYPE=hidden NAME=do VALUE=set_guild_b></FORM>";
$tag = "$tag <P><BR><A HREF=createguild.cgi class=menu>Add a new Guild</A>";

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";


}
else {

&get_user;

$database = "$user{'guild'}_user";


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $database WHERE name='$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
$guild{'name'} = "$user";
$guild{'access'} = "$row[1]";
$guild{'rank'} = "$row[2]";
$guild{'type'} = "$row[3]";
$guild{'points'} = "$row[4]";
$guild{'aproved'} = "$row[5]";

 } 

}
$sth->finish; 
$dbh->disconnect; 

&get_guild;

if ($guild{'access'} eq "Master") {

$tag = qq~
<CENTER><TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class="cat">

<TR><TD COLSPAN=2>Edit Website</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_edit_html class=menu>Edit HTML</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=template.cgi class=menu>Change Template</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_edit_page class=menu>Edit Pages</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_edit_counter class=menu>Change Counter Image</A></TD></TR>

<TR><TD COLSPAN=2>Edit Members</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_aprove_member class=menu>Aprove Members</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_edit_member class=menu>Edit Members</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_message_member class=menu>Message Members</A></TD></TR>

<TR><TD COLSPAN=2>Edit News</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_add_news class=menu>Add News</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_delete_news class=menu>Delete News</A></TD></TR>

<TR><TD COLSPAN=2>Edit Forums</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_add_forum class=menu>Add Forum</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_delete_forum class=menu>Delete Forum</A></TD></TR>

<TR><TD COLSPAN=2>Change Guild Settings</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_edit_info class=menu>Edit Info</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2>
<A href="JavaScript:if (window.confirm('Are you sure you want to delete your guild website? Files are NOT abel to be recovered!')) { window.location.href = 'deleteguild.cgi' }" class=menu>Delete Guild Website</A>
</TD></TR>

</TABLE>
</CENTER>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}

elsif ($guild{'access'} eq "Administrator") {


$tag = qq~
<CENTER><TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class="cat">

<TR><TD COLSPAN=2>Edit Members</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_aprove_member class=menu>Aprove Members</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_edit_member class=menu>Edit Members</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_message_member class=menu>Message Members</A></TD></TR>

<TR><TD COLSPAN=2>Edit News</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_add_news class=menu>Add News</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_delete_news class=menu>Delete News</A></TD></TR>

<TR><TD COLSPAN=3><CENTER><A href="JavaScript:if (window.confirm('Are you sure you want to be removed from your guild?')) { window.location.href = 'useredit.cgi?do=guild_remove' }" class=menu>Remove me from $user{'guild'}</A></TD></TR>

</TABLE>
</CENTER>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}

elsif ($guild{'access'} eq "Modarator") {

$tag = qq~
<CENTER><TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class="cat">

<TR><TD COLSPAN=2>Edit Members</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_message_member class=menu>Message Members</A></TD></TR>

<TR><TD COLSPAN=2>Edit News</TD><TD></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_add_news class=menu>Add News</A></TD></TR>
<TR><TD></TD><TD COLSPAN=2><A HREF=?do=guild_delete_news class=menu>Delete News</A></TD></TR>

<TR><TD COLSPAN=3><CENTER><A href="JavaScript:if (window.confirm('Are you sure you want to be removed from your guild?')) { window.location.href = 'useredit.cgi?do=guild_remove' }" class=menu>Remove me from $user{'guild'}</A></TD></TR>

</TABLE>
</CENTER>
~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}
else {

$tag = qq~

<A href="JavaScript:if (window.confirm('Are you sure you want to be removed from your guild?')) { window.location.href = 'useredit.cgi?do=guild_remove' }" class=menu>Remove me from $user{'guild'}</A>

~;

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";
}


}


}


##################################################################################

sub guild_remove {

&get_user;

$database = "$user{'guild'}_user";


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$name = "$INPUT{'name'}";

$temp = "DELETE FROM $database WHERE name = '$user'"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="UPDATE `user` SET `guild` = '' WHERE `id` = '$user' LIMIT 1"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/You have been removed from your guild!<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub set_guild_b {

$server = "$INPUT{'server'}";


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM server HAVING `server` = '$server'";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
        $row_hit=1;
$server = "$row[1]";
 } 

}
$sth->finish; 
$dbh->disconnect; 


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp ="select * from guild WHERE server ='$server' ORDER BY longname";

$sth=$dbh->prepare($temp);
$sth->execute;

while(@row = $sth->fetchrow_array) { 

$tag = "$tag <A HREF=/$row[0] class=menu TARGET=_new>$row[1]</A> | <A HREF=useredit.cgi?do=set_guild_c&guild=$row[0] class=menu>Add me to $row[1]</A><BR>";

} 

$sth->finish; 
$dbh->disconnect;


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}
##################################################################################

sub set_guild_c {

&get_user;

$guild = "$INPUT{'guild'}";
$database = "$INPUT{'guild'}_user";


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp="UPDATE `user` SET `guild` = '$guild' WHERE `id` = '$user' LIMIT 1"; 

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish; 
$dbh->disconnect; 

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 
$temp="INSERT INTO `$database` ( `name` , `access` , `rank` , `type` , `points` , `aproved`) 
VALUES ('$user', 'Member', 'Member', 'Member', '0', 'False')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 


print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
$HTML{'off_page_html'} =~ s/!!tag!!/Guild Set<BR><A HREF=index.cgi class=menu>Return to Main Page<\/A>/gi;

print "$HTML{'off_page_html'}";

}

##################################################################################
sub options {

print "Content-type: text/html\n\n";

$HTML{'off_page_html'} =~ s/!!tag!!/$HTML{'edit_options_html'}/gi;
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

##################################################################################

sub get_guild {


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from guild";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($guild eq "$row[0]") {
$guildname = "$row[1]";
$goldexp = "$row[4]";
$server = "$row[8]";
$counterimg = "$row[9]";
}


 } 

}
$sth->finish; 
$dbh->disconnect; 

($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

$mon = $mon + 1;
$year = $year + 1900;

($eyear, $emon, $emday) = split(/-/, $goldexp);

if ($eyear eq $year) {

if ($emon < $mon) { $stats = "Silver"; }

elsif ($emon eq $mon) {
    if ($emday < $mday) { $stats = "Silver"; }
    else { $stats = "Gold"; }
} # END MONTH

elsif ($mon < $emon) { $stats = "Gold"; }

} # END YEAR

elsif ($eyear > $year) { $stats = "Gold"; }
else { $stats = "Silver"; }


if ($stats eq "Gold") {

$headbanner = "";
$footbanner = "";

}

else {

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from html";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$MAINHTML{$row[0]} = $row[1];

 } 

}
$sth->finish; 
$dbh->disconnect; 

$headbanner = "$MAINHTML{'header_banner_html'}";
$footbanner = "$MAINHTML{'footer_banner_html'}";
}


}

##################################################################################
