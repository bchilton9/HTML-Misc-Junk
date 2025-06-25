#!/usr/bin/perl

use DBI;

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

##########################################

if ($INPUT{'id'} eq "") { &error("No counter ID number provided"); }
if ($INPUT{'username'} eq "") { &error("No Username provided"); }

##########################################

$id = "$INPUT{'id'}";

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from counter";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] eq "$id") {

$username =  "$row[1]";
$invisible = "$row[2]";
$noreload = "$row[3]";
$style = "$row[4]";
$width = "$row[5]";
$height = "$row[6]";
$bgcolor = "$row[7]";
$free = "$row[8]";
$fontcolor = "$row[11]";

}


 } 

}

if ($username eq "") {
&error("Counter ID number not valid");

}

$sth->finish; 
$dbh->disconnect;

if ($INPUT{'username'} ne "$username") { &error("Invalid Username or counter ID number provided"); }

##########################################


if (!$ENV{'REMOTE_HOST'}) {
$host=$ENV{'REMOTE_ADDR'};
}
else {
$host=$ENV{'REMOTE_HOST'};
}



open (count, "<./data/$INPUT{'id'}.cnt") || &error("Unable to open the data for reading");
$count = <count>;
close (count);


if ($noreload ==1) {
	
	open (record, "<./data/$INPUT{'id'}.rec") || &error("Unable to open the data file for reading");
	$pvisitor = <record>;
	close (record);
    

        open (wrecord, ">./data/$INPUT{'id'}.rec") || &error("Unable to open the data file for writing");
	print wrecord "$host";
	close (wrecord);

if ($host==$pvisitor) {
if ($invisible==1) {

print "Content-type: text/html\n\n";
exit;
}

print "Content-type: text/html\n\n";

print qq~
<HTML>
<HEAD>
<TITLE>Chiltons.us Flash Counter</TITLE>
</HEAD>
<BODY bgcolor="$bgcolor" topmargin="0" leftmargin="0">
<CENTER>
<OBJECT WIDTH="$width" HEIGHT="$height" id="counter">

<PARAM NAME=movie VALUE="$style.swf"> 
<PARAM NAME=quality VALUE=high> 
<PARAM NAME=bgcolor VALUE=$bgcolor> 
<PARAM NAME=FlashVars VALUE="textcolor=$fontcolor&id=$INPUT{'id'}">

<EMBED src="$style.swf" quality=high bgcolor=$bgcolor FlashVars="textcolor=$fontcolor&id=$INPUT{'id'}" WIDTH="$width" HEIGHT="$height" NAME="counter"></EMBED>

</OBJECT>
</CENTER>
</BODY>
</HTML>
~;

 
}

}


$count++;


if ($count == 100000000) {
$longcount = "00000001";
$count = 1;
}

if ($count <= 99999999) {
$longcount = "$count";
}

if ($count <= 9999999) {
$longcount = "0$count";
}

if ($count <= 999999) {
$longcount = "00$count";
}

if ($count <= 99999) {
$longcount = "000$count";
}

if ($count <= 9999) {
$longcount = "0000$count";
}

if ($count <= 999) {
$longcount = "00000$count";
}

if ($count <= 99) {
$longcount = "000000$count";
}

if ($count <= 9) {
$longcount = "0000000$count";
}

open (wcount, ">./data/$INPUT{'id'}.cnt") || &error("Unalbe to open the data for writing");
print wcount "$count";
close (wcount);

open (wdat, ">./data/$INPUT{'id'}.dat") || &error("Unalbe to open the data for writing");
print wdat "Count=$longcount";
close (wdat);

if ($invisible==1) {
print "Content-type: text/html\n\n";
exit;
}

print "Content-type: text/html\n\n";

print qq~
<HTML>
<HEAD>
<TITLE>Chiltons.us Flash Counter</TITLE>
</HEAD>
<BODY bgcolor="$bgcolor" topmargin="0" leftmargin="0">
<CENTER>
<OBJECT WIDTH="$width" HEIGHT="$height" id="counter">

<PARAM NAME=movie VALUE="$style.swf"> 
<PARAM NAME=quality VALUE=high> 
<PARAM NAME=bgcolor VALUE=$bgcolor> 
<PARAM NAME=FlashVars VALUE="textcolor=$fontcolor&id=$INPUT{'id'}">

<EMBED src="$style.swf" quality=high bgcolor=$bgcolor FlashVars="textcolor=$fontcolor&id=$INPUT{'id'}" WIDTH="$width" HEIGHT="$height" NAME="counter"></EMBED>

</OBJECT>
</CENTER>
</BODY>
</HTML>
~;

exit;


sub error{
print "Content-type: text/html\n\n";
print qq~
<HTML>
<HEAD>
<TITLE>Chiltons.us Flash Counter: Error</TITLE>
</HEAD>
<BODY bgcolor="#FFFFFF" topmargin="0" leftmargin="0">
<OBJECT WIDTH="300" HEIGHT="40" id="error" ALIGN="">
 <PARAM NAME=movie VALUE="error.swf"> 
<PARAM NAME=quality VALUE=high> 
<PARAM NAME=bgcolor VALUE=#FFFFFF> 
<PARAM NAME=FlashVars VALUE="error=Counter Error: $_[0]. Please recreate your counter code at http://www.chiltons.us!">
<EMBED src="error.swf" FlashVars="error=Counter Error: $_[0]. Please recreate your counter code at http://www.chiltons.us!" quality=high bgcolor=#FFFFFF  WIDTH="300" HEIGHT="40" NAME="error"></EMBED>
</OBJECT>
</BODY>
</HTML>
~;
exit;
}






