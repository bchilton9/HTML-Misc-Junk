#!/usr/bin/perl


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

require 'cookie.lib';
use DBI;


if ($INPUT{'do'} eq "View") { &view; }
elsif ($INPUT{'do'} eq "Set Template") { &set_template; }
else { &main; }

##################################################################################

sub set_template {

&get_html;
&get_user;


open (DATA, "./cgis/temp/$INPUT{'template'}/main_page_html.txt");
@data = <DATA>;
close DATA;
$main_page_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/log_box_html_in.txt");
@data = <DATA>;
close DATA;
$log_box_html_in = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/log_box_html_out.txt");
@data = <DATA>;
close DATA;
$log_box_html_out = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/news_box_html.txt");
@data = <DATA>;
close DATA;
$news_box_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/off_page_html.txt");
@data = <DATA>;
close DATA;
$off_page_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/roster_line_html.txt");
@data = <DATA>;
close DATA;
$roster_line_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/roster_head_html.txt");
@data = <DATA>;
close DATA;
$roster_head_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/roster_foot_html.txt");
@data = <DATA>;
close DATA;
$roster_foot_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/links_html.txt");
@data = <DATA>;
close DATA;
$links_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/forum_main_html.txt");
@data = <DATA>;
close DATA;
$forum_main_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/forum_post_html.txt");
@data = <DATA>;
close DATA;
$forum_post_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/forum_thread_html.txt");
@data = <DATA>;
close DATA;
$forum_thread_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/forum_topic_html.txt");
@data = <DATA>;
close DATA;
$forum_topic_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/forum_view_main_html.txt");
@data = <DATA>;
close DATA;
$forum_view_main_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/forum_view_thred_html.txt");
@data = <DATA>;
close DATA;
$forum_view_thred_html = "@data";

$guild = "$user{'guild'}";

$htmldb = "$guild html";
$htmldb =~ s/ /_/gi;


my $dbh = DBI->connect("DBI:mysql:eqguild_guild:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbhb->errstr\n"; 

## HTML TABLE
$temp = "INSERT INTO `$htmldb` VALUES ('main_page_html', '$main_page_html', 'true')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('log_box_html_in', '$log_box_html_in', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('log_box_html_out', '$log_box_html_out', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('news_box_html', '$news_box_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('off_page_html', '$off_page_html', 'true')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('roster_line_html', '$roster_line_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('roster_head_html', '$roster_head_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('roster_foot_html', '$roster_foot_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('links_html', '$links_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_main_html', '$forum_main_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_post_html', '$forum_post_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_thread_html', '$forum_thread_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_topic_html', '$forum_topic_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_view_main_html', '$forum_view_main_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$temp = "INSERT INTO `$htmldb` VALUES ('forum_view_thred_html', '$forum_view_thred_html', '')";
$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 

$dbh->disconnect;

$tag = qq~
Template Updated!
<P>
<A HREF=useredit.cgi?do=edit_guild class=menu>Return to edit guild</A><BR>
<A HREF=index.cgi class=menu>Return to EQ Guilded</A>
~;

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

sub view {

&get_html;
&get_user;

$tag = qq~
<FORM ACTION="template.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Template:</TD>
	<TD>
	  <SELECT NAME="template">
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp ="select * from templates ORDER BY display";

$sth=$dbh->prepare($temp);
$sth->execute;

while(@row = $sth->fetchrow_array) { 

$tag = "$tag <OPTION value=\"$row[0]\">$row[1]";

} 

$sth->finish; 
$dbh->disconnect;

$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="View" NAME="do"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=submit VALUE="Set Template" NAME="do"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;


open (DATA, "./cgis/temp/$INPUT{'template'}/main_page_html.txt");
@data = <DATA>;
close DATA;
$main_page_html = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/log_box_html_in.txt");
@data = <DATA>;
close DATA;
$log_box_html_in = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/log_box_html_out.txt");
@data = <DATA>;
close DATA;
$log_box_html_out = "@data";

open (DATA, "./cgis/temp/$INPUT{'template'}/news_box_html.txt");
@data = <DATA>;
close DATA;
$news_box_html = "@data";


open (DATA, "./cgis/temp/$INPUT{'template'}/links_html.txt");
@data = <DATA>;
close DATA;
$links_html = "@data";




$news_box_html =~ s/!!date!!/DATE/gi;
$news_box_html =~ s/!!news!!/NEWS/gi;

print "Content-type: text/html\n\n";


$log_box_html_in =~ s/!!name!!/Username/gi;
$log_box_html_in =~ s/!!sur!!/Surname/gi;
$log_box_html_in =~ s/!!messages!!/0/gi;
$log_box_html_in =~ s/!!points!!/0/gi;
$main_page_html =~ s/!!logbox!!/$log_box_html_in/gi;

$main_page_html =~ s/!!links!!/$links_html/gi;
$main_page_html =~ s/!!news!!/$news_box_html/gi;
$main_page_html =~ s/!!guildname!!/Guild Name/gi;
$main_page_html =~ s/!!counter!!/Counter/gi;

$main_page_html =~ s/!!headbanner!!//gi;
$main_page_html =~ s/!!footbanner!!/$tag/gi;

print "$main_page_html";

}

##################################################################################

sub main {

&get_html;
&get_user;

$tag = qq~
<FORM ACTION="template.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Template:</TD>
	<TD>
	  <SELECT NAME="template">
~;

my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp ="select * from templates ORDER BY display";

$sth=$dbh->prepare($temp);
$sth->execute;

while(@row = $sth->fetchrow_array) { 

$tag = "$tag <OPTION value=\"$row[0]\">$row[1]";

} 

$sth->finish; 
$dbh->disconnect;

$tag = qq~ $tag
</SELECT></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="View" NAME="do"> &nbsp;
	  &nbsp;
	  <INPUT TYPE=submit VALUE="Set Template" NAME="do"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;


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