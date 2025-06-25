#!/usr/bin/perl

use DBI;

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

if ($INPUT{'do'} eq "list") {

$count = 0;

$tag = qq~
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" class=cat>
    <TR>
      <TD>Server Name:</TD>
      <TD>Guild Count:</TD>
    </TR>
~;


my $dbh = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM server ORDER BY server";

if($sth=$dbh->prepare($temp)) 
{ 

 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
        $row_hit=1;



my $dbhb = DBI->connect("DBI:mysql:eqguild_user:localhost","eqguild_guild","eqg") 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp ="select * from guild WHERE server ='$row[1]'";


$sthb=$dbhb->prepare($temp);
$sthb->execute;

$count = 0;

while(@rowb = $sthb->fetchrow_array) { 

$count++;

} 

$sthb->finish; 
$dbhb->disconnect; 


if ($count eq "0") {
$count = "";
}

$tag = qq~ $tag
    <TR>
      <TD><A HREF=server.cgi?server=$row[1] class=menu>$row[0]</A></TD>
      <TD><CENTER>$count</CENTER></TD>
    </TR>
~;

 } 

}
$sth->finish; 
$dbh->disconnect; 

$tag = qq~ $tag
</TABLE>
</CENTER>
<BR><A HREF=index.cgi class=menu>Return to Main Page</A>
~;


print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}

##################################################################################

else {

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

$tag = "$tag <A HREF=/$server/$row[0] class=menu>$row[1]</A><BR>";

} 

$sth->finish; 
$dbh->disconnect; 

$tag = "$tag <BR><A HREF=index.cgi class=menu>Return to Main Page</A>";

print "Content-type: text/html\n\n";
$HTML{'off_page_html'} =~ s/!!tag!!/$tag/gi;
$HTML{'off_page_html'} =~ s/!!leftblocks!!/$HTML{'left_blocks_html'}/gi;
print "$HTML{'off_page_html'}";

}