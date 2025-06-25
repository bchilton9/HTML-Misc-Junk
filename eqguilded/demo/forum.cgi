#!/usr/bin/perl

require '../../cookie.lib';
require 'config.pl';
use DBI;

# $ENV{'REMOTE_ADDR'}

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

&get_html;
&get_guild;

if ($INPUT{'do'} eq "view_thread") { &view_thread; }
elsif ($INPUT{'do'} eq "view_topic") { &view_topic; }
elsif ($INPUT{'do'} eq "post_a") { &post_a; }
elsif ($INPUT{'do'} eq "post_b") { &post_b; }
elsif ($INPUT{'do'} eq "delete") { &delete; }
elsif ($INPUT{'do'} eq "stick") { &stick; }
elsif ($INPUT{'do'} eq "lock") { &lock; }
elsif ($INPUT{'do'} eq "edit") { &edit; }
elsif ($INPUT{'do'} eq "edit_b") { &edit_b; }
else { &main; }

##################################################################################

##################################################################################

sub edit {

&get_user;
$id = "$INPUT{'id'}";

$temp ="select * from $postsdb where id='$id' LIMIT 1";


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 


$sth=$dbh->prepare($temp);
$sth->execute;


 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

	$message = "$row[2]";
	$subject = "$row[3]";

}


$sth->finish; 
$dbh->disconnect; 



$tag = qq~
<FORM ACTION="forum.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name:</TD>
	<TD>$user</TD>
      </TR>
      <TR>
	<TD>Subject:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="subject" VALUE="$subject"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2>Message:</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><TEXTAREA NAME="message" ROWS="15" COLS="30">$message</TEXTAREA></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Post"> &nbsp;
	  <INPUT TYPE=reset VALUE="Start Over">
	  <INPUT TYPE="hidden" NAME="do" VALUE="edit_b">
	  <INPUT TYPE="hidden" NAME="id" VALUE="$id">
	</TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;




print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$tag/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";

}

##################################################################################

sub edit_b {

$id = "$INPUT{'id'}";
$message = "$INPUT{'message'}";
$subject = "$INPUT{'subject'}";


if ($subject eq "") {
$tag = qq~
Please Enter a subject!<BR>
Press your back button to try agine!
~;
}
else {

my $dbhb = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 
$temp="UPDATE $postsdb SET `message` = '$message', `subject` = '$subject' WHERE `id` = '$id' LIMIT 1 ;";
$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;

$tag = "Posted!<BR><A HREF=forum.cgi>Back to the Forum</A>";

}



print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$tag/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";

}

##################################################################################

sub lock {

$type = "$INPUT{'type'}";
$id = "$INPUT{'id'}";

if ($type eq "lock") {
$temp = "UPDATE $postsdb SET `locked` = 'true' WHERE `id` = '$id' LIMIT 1";
$tag = qq~
Topic Locked!
~;

}
elsif ($type eq "unlock") {
$temp = "UPDATE $postsdb SET `locked` = '' WHERE `id` = '$id' LIMIT 1";
$tag = qq~
Topic UnLocked!
~;

}

my $dbhb = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;


$tag = qq~ $tag
<BR>
<A HREF=forum.cgi class=menu>Back to the Forums</A>
~;


print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$tag/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";
}

##################################################################################

sub stick {

$type = "$INPUT{'type'}";
$id = "$INPUT{'id'}";

if ($type eq "stick") {
$temp = "UPDATE $postsdb SET `sticky` = 'true' WHERE `id` = '$id' LIMIT 1";
$tag = qq~
Topic Stuck!
~;

}
elsif ($type eq "unstick") {
$temp = "UPDATE $postsdb SET `sticky` = 'false' WHERE `id` = '$id' LIMIT 1";
$tag = qq~
Topic UnStuck!
~;

}

my $dbhb = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;


$tag = qq~ $tag
<BR>
<A HREF=forum.cgi class=menu>Back to the Forums</A>
~;


print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$tag/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";
}

##################################################################################

sub delete {

$topic = "$INPUT{'topic'}";
$forum = "$INPUT{'forum'}";
$type = "$INPUT{'type'}";
$id = "$INPUT{'id'}";


if ($type eq "post") {
$temp = "DELETE FROM $postsdb WHERE `id` ='$id' LIMIT 1";
$tag = qq~
Post Deleted!
~;

}
elsif ($type eq "topic") {
$temp = "DELETE FROM $postsdb WHERE `topic` ='$topic' AND `forum` ='$forum'";
$tag = qq~
Topic Deleted!
~;

}

my $dbhb = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;


$tag = qq~ $tag
<BR>
<A HREF=forum.cgi class=menu>Back to the Forums</A>
~;


print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$tag/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";
}

##################################################################################

sub post_a {

&get_user;
$topic = "$INPUT{'topic'}";
$thread = "$INPUT{'thread'}";
$forum = "$INPUT{'forum'}";



if ($user eq "") {
$tag = "You Must be loged in to post<BR><A HREF=http://www.eqguilded.com</A>Click here to log in</A>";
}
elsif ($thread eq "") {
$tag = "Please try posting from <A HREF=forum.cgi>Here</A>";
}
elsif ($forum eq "") {
$tag = "Please try posting from <A HREF=forum.cgi>Here</A>";
}
else {

$tag = qq~
<FORM ACTION="forum.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name:</TD>
	<TD>$user</TD>
      </TR>
      <TR>
	<TD>Subject:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="subject"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2>Message:</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><TEXTAREA NAME="message" ROWS="15" COLS="30"></TEXTAREA></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Post"> &nbsp;
	  <INPUT TYPE=reset VALUE="Start Over">
	  <INPUT TYPE="hidden" NAME="topic" VALUE="$topic">
	  <INPUT TYPE="hidden" NAME="thread" VALUE="$thread">
	  <INPUT TYPE="hidden" NAME="forum" VALUE="$forum">
	  <INPUT TYPE="hidden" NAME="name" VALUE="$user">
	  <INPUT TYPE="hidden" NAME="do" VALUE="post_b">
	</TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;

}


print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$tag/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";

}

##################################################################################

sub post_b {

$name = "$INPUT{'name'}";
$message = "$INPUT{'message'}";
$subject = "$INPUT{'subject'}";
$topic = "$INPUT{'topic'}";
$forum = "$INPUT{'forum'}";
$thread = "$INPUT{'thread'}";

if ($thread eq "1") {
if ($subject eq "") {
$tag = qq~
Please Enter a subject!<BR>
Press your back button to try agine!
~;
}
else {

$topic = "$INPUT{'subject'}";

my $dbhb = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 
$temp="insert into $postsdb (name,message,subject,date,topic,forum,thread,sticky) values('$name','$message','$subject',NOW( ),'$topic','$forum','$thread','false')";
$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;

$tag = "Posted!<BR><A HREF=forum.cgi>Back to the Forum</A>";

}
}
else {

if ($subject eq "") {
$subject = "Re: $topic";
}

my $dbhb = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 
$temp="insert into $postsdb (name,message,subject,date,topic,forum,thread,sticky) values('$name','$message','$subject',NOW( ),'$topic','$forum','$thread','false')";
$sthb=$dbhb->prepare($temp);
$sthb->execute;
$sthb->finish; 
$dbhb->disconnect;

$tag = "Posted!<BR><A HREF=forum.cgi>Back to the Forum</A>";
}

print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$tag/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";

}

##################################################################################

sub main {

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $formsdb";
$sth=$dbh->prepare($temp);
$sth->execute;


 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

	$id = "$row[0]";
        $forum = "$row[1]";
        $descript = "$row[2]";

	$temp = "select count(*) from $postsdb where forum='$forum' and thread='1'";

	$xboardvals=$dbh->prepare($temp);
	$xboardvals->execute();
	$topicnum=$xboardvals->fetchrow();
	$xboardvals->finish();

	$temp = "select * from $postsdb where forum='$forum' order by date desc limit 1";

        $lastpostvals=$dbh->prepare($temp);
        $lastpostvals->execute();

	$ref = $lastpostvals->fetchrow_hashref();

	$lpostname=$ref->{'name'};
	$lposttopic=$ref->{'topic'};
	$lpostsubject=$ref->{'subject'};
	$lpostdate=$ref->{'date'};

	if (!$topicnum){$topicnum="0";}

my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from user WHERE id='$lpostname'";

if($sthb=$dbhb->prepare($temp)) 
{ 
 $sthb->execute;  #Execute the query 

 while((@row=$sthb->fetchrow_array)!=NULL) { 
          $row_hit=1;
$username = "$row[1]";
$surname = "$row[2]";

$poster = "$username $surname";
 } 

}
$sthb->finish; 
$dbhb->disconnect; 



$temp = "$HTML{'forum_view_main_html'}";

$temp =~ s/!!forum!!/$forum/gi;
$temp =~ s/!!description!!/$descript/gi;
$temp =~ s/!!lastpostname!!/$poster/gi;
$temp =~ s/!!lastpostdate!!/$lpostdate/gi;
$temp =~ s/!!count!!/$topicnum/gi;

$posthtml = "$posthtml $temp";

}


$sth->finish; 
$dbh->disconnect; 

$HTML{'forum_main_html'} =~ s/!!threads!!/$posthtml/gi;

print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$HTML{'forum_main_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";

}

##################################################################################

sub view_thread {

$forum = "$INPUT{'forum'}";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $postsdb where forum='$forum' AND `sticky` ='true' order by date desc";
$sth=$dbh->prepare($temp);
$sth->execute;

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

        $id = "$row[0]";
        $name = "$row[1]";
        $message = "$row[2]";
        $subject = "$row[3]";
        $date = "$row[8]";
        $ip = "$row[4]";
        $topic = "$row[6]";
        $forum = "$row[7]";
        $thread = "$row[5]";

if ($row[10] eq "true") {
	$image = "http://www.eqguilded.com/images/forums/stickylocked.gif";
}
else {
	$image = "http://www.eqguilded.com/images/forums/sticky.gif";
}

        if ($thread eq "1")
        {

	$temp = "select count(*) from $postsdb where forum='$forum' and topic='$topic'";
	$numreply=$dbh->prepare($temp);
	$numreply->execute();

	$count=$numreply->fetchrow();
	if ($count eq "") {
	$count = "0";
	}

	$numreply->finish();


my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from user WHERE id='$name'";

if($sthb=$dbhb->prepare($temp)) 
{ 
 $sthb->execute;  #Execute the query 

 while((@row=$sthb->fetchrow_array)!=NULL) { 
          $row_hit=1;
$username = "$row[1]";
$surname = "$row[2]";
$rank = "$row[11]";

$poster = "$username $surname";
 } 

}
$sthb->finish; 
$dbhb->disconnect; 

$temp = "$HTML{'forum_thread_html'}";

$temp =~ s/!!image!!/$image/gi;
$temp =~ s/!!forum!!/$forum/gi;
$temp =~ s/!!topic!!/$topic/gi;
$temp =~ s/!!name!!/$poster/gi;
$temp =~ s/!!date!!/$date/gi;
$temp =~ s/!!count!!/$count/gi;

$posthtml = "$posthtml $temp";

        }
}


$sth->finish; 
$dbh->disconnect;

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $postsdb where forum='$forum' AND `sticky` ='false' order by date desc";
$sth=$dbh->prepare($temp);
$sth->execute;

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

        $id = "$row[0]";
        $name = "$row[1]";
        $message = "$row[2]";
        $subject = "$row[3]";
        $date = "$row[8]";
        $ip = "$row[4]";
        $topic = "$row[6]";
        $forum = "$row[7]";
        $thread = "$row[5]";

if ($row[10] eq "true") {
	$image = "http://www.eqguilded.com/images/forums/locked.gif";
}
else {
	$image = "http://www.eqguilded.com/images/forums/thread.gif";
}


        if ($thread eq "1")
        {

	$temp = "select count(*) from $postsdb where forum='$forum' and topic='$topic'";
	$numreply=$dbh->prepare($temp);
	$numreply->execute();

	$count=$numreply->fetchrow();
	if ($count eq "") {
	$count = "0";
	}

	$numreply->finish();


$temp = "$HTML{'forum_thread_html'}";

$temp =~ s/!!image!!/$image/gi;
$temp =~ s/!!forum!!/$forum/gi;
$temp =~ s/!!topic!!/$topic/gi;
$temp =~ s/!!name!!/$name/gi;
$temp =~ s/!!date!!/$date/gi;
$temp =~ s/!!count!!/$count/gi;

$posthtml = "$posthtml $temp";

        }
}


$sth->finish; 
$dbh->disconnect;

$HTML{'forum_view_thred_html'} =~ s/!!topics!!/$posthtml/gi;
$HTML{'forum_view_thred_html'} =~ s/!!topic!!//gi;
$HTML{'forum_view_thred_html'} =~ s/!!forum!!/$forum/gi;

print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$HTML{'forum_view_thred_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";


}

##################################################################################

sub view_topic {

&get_user;

$forum = "$INPUT{'forum'}";
$topic = "$INPUT{'topic'}";

$ida = "";

my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $postsdb where forum='$forum' and topic='$topic' order by date asc";
$sth=$dbh->prepare($temp);
$sth->execute;

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;
	
        $id = "$row[0]";
        $name = "$row[1]";
        $message = "$row[2]";
        $subject = "$row[3]";
        $date = "$row[8]";
	$ip = "$row[4]";
	$thread = "$row[5]";

if ($ida eq "") {
$ida = "$row[0]";
$sticky = "$row[9]";
$locked = "$row[10]";
}

if ($sticky eq "true") {

if ($locked eq "true") {
	$image = "http://www.eqguilded.com/images/forums/stickylocked.gif";
}
else {
	$image = "http://www.eqguilded.com/images/forums/sticky.gif";
}

}
else {

if ($locked eq "true") {
	$image = "http://www.eqguilded.com/images/forums/locked.gif";
}
else {
	$image = "http://www.eqguilded.com/images/forums/thread.gif";
}

}


my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from user WHERE id='$name'";

if($sthb=$dbhb->prepare($temp)) 
{ 
 $sthb->execute;  #Execute the query 

 while((@row=$sthb->fetchrow_array)!=NULL) { 
          $row_hit=1;
$username = "$row[1]";
$surname = "$row[2]";
$rank = "$row[11]";

$poster = "$username $surname";
 } 

}
$sthb->finish; 
$dbhb->disconnect; 

my $dbhc = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $userdb WHERE name='$user'";

if($sthc=$dbhc->prepare($temp)) 
{ 
 $sthc->execute;  #Execute the query 

 while((@row=$sthc->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($rank eq "") {
$rank = "$row[2]";
}


if ($row[1] eq "Master") {
&process_admin_b;
}
elsif ($row[1] eq "Modarator") {
&process_admin_b;
}
elsif ($row[1] eq "Administrator") {
&process_admin_b;
}

}
}

$sthc->finish; 
$dbhc->disconnect;

if ($rank eq "") {
$rank = "Guest";
}


$temp = "$HTML{'forum_post_html'}";

$temp =~ s/!!admin!!/$adminb/gi;
$temp =~ s/!!message!!/$message/gi;
$temp =~ s/!!date!!/$date/gi;
$temp =~ s/!!subject!!/$subject/gi;
$temp =~ s/!!name!!/$poster/gi;
$temp =~ s/!!rank!!/$rank/gi;

$posthtml = "$posthtml $temp";

}


my $dbhc = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $userdb WHERE name='$user'";

if($sthc=$dbhc->prepare($temp)) 
{ 
 $sthc->execute;  #Execute the query 

 while((@row=$sthc->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[1] eq "Master") {
&process_admin;
}
elsif ($row[1] eq "Modarator") {
&process_admin;
}
elsif ($row[1] eq "Administrator") {
&process_admin;
}

}
}

$sthc->finish; 
$dbhc->disconnect;



if ($locked eq "") {
$admin = qq~
<A HREF="forum.cgi?do=post_a&topic=$topic&forum=$forum&thread=2" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/replymsg.gif BORDER="0" ALT="Reply"></A>
$admin
~;
}


$sth->finish; 
$dbh->disconnect;

$HTML{'forum_topic_html'} =~ s/!!admin!!/$admin/gi;
$HTML{'forum_topic_html'} =~ s/!!image!!/$image/gi;
$HTML{'forum_topic_html'} =~ s/!!forum!!/$forum/gi;
$HTML{'forum_topic_html'} =~ s/!!topic!!/$topic/gi;
$HTML{'forum_topic_html'} =~ s/!!posts!!/$posthtml/gi;

print "Content-type: text/html\n\n";
 $HTML{'off_page_html'} =~ s/!!content!!/$HTML{'forum_topic_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!links!!/$HTML{'links_html'}/gi;
 $HTML{'off_page_html'} =~ s/!!guildname!!/$guildname/gi;
 $HTML{'off_page_html'} =~ s/!!headbanner!!/$headbanner/gi;
 $HTML{'off_page_html'} =~ s/!!footbanner!!/$footbanner/gi;
 print "$HTML{'off_page_html'}";

}

##################################################################################

sub process_admin_b {

$adminb = "";

if ($thread ne "1") {
$adminb = qq~
<A HREF="forum.cgi?do=delete&type=post&id=$id" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/delete.gif BORDER="0" ALT="Delete Post"></A>
~;
}

$adminb = qq~ $adminb
<A HREF="forum.cgi?do=edit&id=$id" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/modify.gif BORDER="0" ALT="Edit Post"></A>
~;
if ($ip ne "") {
$adminb = qq~ $adminb
<IMG SRC=http://www.eqguilded.com/images/forums/ip.gif BORDER="0" ALT="Ip Address Loged">
~;
}
else {
$adminb = qq~ $adminb
<IMG SRC=http://www.eqguilded.com/images/forums/ip.gif BORDER="0" ALT="Ip Address Not Loged">
~;
}


}

##################################################################################

sub process_admin {


$admin = "";

$admin = qq~ $admin
<A HREF="forum.cgi?do=delete&topic=$topic&forum=$forum&type=topic" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/delete.gif BORDER="0" ALT="Delete Topic"></A>
~;

if ($sticky eq "true") {

   if ($locked eq "true") {
      $admin = qq~ $admin
      <A HREF="forum.cgi?do=lock&type=unlock&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/locked.gif BORDER="0" ALT="UnLock Topic"></A>
      <A HREF="forum.cgi?do=stick&type=unstick&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/thread.gif BORDER="0" ALT="UnStick Topic"></A>
      ~;
   } # LOCKED EQ TRUE
   else {
      $admin = qq~ $admin
      <A HREF="forum.cgi?do=lock&type=lock&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/lock.gif BORDER="0" ALT="Lock Topic"></A>
      <A HREF="forum.cgi?do=stick&type=unstick&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/thread.gif BORDER="0" ALT="UnStick Topic"></A>
      ~;
   } #ELSE

} #IF STICKY
else {

if ($locked eq "true") {
   $admin = qq~ $admin
   <A HREF="forum.cgi?do=lock&type=unlock&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/locked.gif BORDER="0" ALT="UnLock Topic"></A>
   <A HREF="forum.cgi?do=stick&type=stick&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/sticky.gif BORDER="0" ALT="Make Sticky"></A>
   ~;
}
else {
   $admin = qq~ $admin
<A HREF="forum.cgi?do=lock&type=lock&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/lock.gif BORDER="0" ALT="Lock Topic"></A>
   <A HREF="forum.cgi?do=stick&type=stick&id=$ida" class=menu><IMG SRC=http://www.eqguilded.com/images/forums/sticky.gif BORDER="0" ALT="Make Sticky"></A>
   ~;
}

} # ELSE


} #close sub

##################################################################################

sub get_html {


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $htmldb";

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
$rank = "$row[11]";
 } 

}
$sth->finish; 
$dbh->disconnect; 


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from $userdb WHERE name='$user'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$user{'access'} = "$row[1]";
$user{'rank'} = "$row[2]";
$user{'type'} = "$row[3]";
$user{'points'} = "$row[4]";

 } 

}
$sth->finish; 
$dbh->disconnect;

}