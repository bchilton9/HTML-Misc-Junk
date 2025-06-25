#!/usr/bin/perl

require 'cookie.lib';
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

if ($INPUT{'do'} eq "signup") { &signup; }
elsif ($INPUT{'do'} eq "cp") { &cp; }
elsif ($INPUT{'do'} eq "page") { &page; }
elsif ($INPUT{'do'} eq "addnew") { &addnew; }
elsif ($INPUT{'do'} eq "edit") { &edit; }
elsif ($INPUT{'do'} eq "save") { &save; }
elsif ($INPUT{'do'} eq "delete") { &delete; }

else { 
$INPUT{'page'} = "main";
&page;
 }

##########################################

sub page {
&header;
open (page, "<./pages/$INPUT{'page'}.dat");
@page = <page>;
close (page);
print "@page";
&footer;
}

##########################################

sub signup {

$username = "$INPUT{'username'}";
$name = "$INPUT{'name'}";
$password = "$INPUT{'password'}";
$email = "$INPUT{'email'}";
$url = "$INPUT{'url'}";
$news = "$INPUT{'news'}";


my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="INSERT INTO `user` ( `id` , `username` , `realname` , `password` , `email` , `url` , `news` ) VALUES ( '', '$username', '$name', '$password', '$email', '$url', '$news')";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 


$INPUT{'page'} = "signupdone";
&page;

}

##########################################

sub cp {
&GetCookies('user');

$username = "$Cookies{'user'}";
$password = "$Cookies{'pass'}";

if ($username eq "") {
$INPUT{'page'} = "notlogedin";
&page;
}
else {
&header;


my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM `counter` WHERE `owner` = '$username'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[8] eq "no") {
open (cprow, "<./pages/cprowpay.dat");
@cprow = <cprow>;
close (cprow);
$cprow = "@cprow";
}
else {
open (cprow, "<./pages/cprowfree.dat");
@cprow = <cprow>;
close (cprow);
$cprow = "@cprow";
}

open (count, "<./data/$row[0].cnt");
$count = <count>;
close (count);

if ($count eq "") {

$count = "0";

open (wcount, ">./data/$row[0].cnt");
print wcount "0";
close (wcount);

open (wdat, ">./data/$row[0].dat");
print wdat "Count=00000000";
close (wdat);

open (wrecord, ">./data/$row[0].rec");
print wrecord "$host";
close (wrecord);

}

$cprow =~ s/!!id!!/$row[0]/gi;
$cprow =~ s/!!username!!/$row[1]/gi;
$cprow =~ s/!!invisible!!/$row[2]/gi;
$cprow =~ s/!!noreload!!/$row[3]/gi;
$cprow =~ s/!!style!!/$row[4]/gi;
$cprow =~ s/!!width!!/$row[5]/gi;
$cprow =~ s/!!height!!/$row[6]/gi;
$cprow =~ s/!!bgcolor!!/$row[7]/gi;
$cprow =~ s/!!free!!/$row[8]/gi;
$cprow =~ s/!!name!!/$row[9]/gi;
$cprow =~ s/!!expire!!/$row[10]/gi;
$cprow =~ s/!!count!!/$count/gi;
$cprow =~ s/!!fontcolor!!/$row[11]/gi;

$myrow = "$myrow\n$cprow";

 } 

}

$sth->finish; 
$dbh->disconnect;
 
open (cp, "<./pages/cp.dat");
@cp = <cp>;
close (cp);
$cp = "@cp";

$cp =~ s/!!counters!!/$myrow/gi;

print "$cp";

&footer;
}

}

##########################################

sub addnew {

&GetCookies('user');

$username = "$Cookies{'user'}";
$password = "$Cookies{'pass'}";


if ($username eq "") {
$INPUT{'page'} = "notlogedin";
&page;
}
else {


$style = "$INPUT{'style'}";
$width = "$INPUT{'width'}";
$height = "$INPUT{'height'}";
$invisible = "$INPUT{'invisible'}";
$noreload = "$INPUT{'noreload'}";
$bgcolor = "$INPUT{'bgcolor'}";
$name = "$INPUT{'name'}";
$fontcolor = "$INPUT{'fontcolor'}";

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="INSERT INTO `counter` ( `id` , `owner` , `invisible` , `noreload` , `style` , `width` , `height` , `bgcolor` , `free` , `name` , `expire` , `fontcolor` ) VALUES ( '', '$username', '$invisible', '$noreload', '$style', '$width', '$height', '$bgcolor', 'yes', '$name', '', '$fontcolor')";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 

$INPUT{'page'} = "adddone";
&page;

}
}

##########################################

sub edit {
&GetCookies('user');

$username = "$Cookies{'user'}";
$password = "$Cookies{'pass'}";

if ($username eq "") {
$INPUT{'page'} = "notlogedin";
&page;
}
else {

&header;


$id = "$INPUT{'id'}";

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM `counter` WHERE `owner` = '$username' AND `id` = '$id'";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

$invisible = "$row[2]";
$noreload = "$row[3]";
$style = "$row[4]";
$width = "$row[5]";
$height = "$row[6]";
$bgcolor = "$row[7]";
$name = "$row[9]";
$fontcolor = "$row[11]";

 } 

}

$sth->finish; 
$dbh->disconnect;


$hexfontcolor = "$fontcolor";
$hexfontcolor =~ s/0x/\#/gi;

open (count, "<./data/$id.cnt");
$count = <count>;
close (count);

open (edit, "<./pages/edit.dat");
@edit = <edit>;
close (edit);
$edit = "@edit";

if ($invisible eq "1") {
$edit =~ s/!!invisible!!/CHECKED/gi;
}

if ($noreload eq "1") {
$edit =~ s/!!noreload!!/CHECKED/gi;
}

$edit =~ s/!!id!!/$id/gi;
$edit =~ s/!!width!!/$width/gi;
$edit =~ s/!!height!!/$height/gi;
$edit =~ s/!!bgcolor!!/$bgcolor/gi;
$edit =~ s/!!name!!/$name/gi;
$edit =~ s/!!count!!/$count/gi;
$edit =~ s/!!fontcolor!!/$fontcolor/gi;
$edit =~ s/!!hexfontcolor!!/$hexfontcolor/gi;

if ($style eq "1") {
$edit =~ s/!!style1!!/CHECKED/gi;
}
if ($style eq "2") {
$edit =~ s/!!style2!!/CHECKED/gi;
}
if ($style eq "3") {
$edit =~ s/!!style3!!/CHECKED/gi;
}
if ($style eq "4") {
$edit =~ s/!!style4!!/CHECKED/gi;
}
if ($style eq "5") {
$edit =~ s/!!style5!!/CHECKED/gi;
}
if ($style eq "6") {
$edit =~ s/!!style6!!/CHECKED/gi;
}
if ($style eq "7") {
$edit =~ s/!!style7!!/CHECKED/gi;
}
if ($style eq "8") {
$edit =~ s/!!style8!!/CHECKED/gi;
}
if ($style eq "9") {
$edit =~ s/!!style9!!/CHECKED/gi;
}
if ($style eq "10") {
$edit =~ s/!!style10!!/CHECKED/gi;
}



print "$edit";

&footer;
}
}

##########################################

sub save {

&GetCookies('user');

$username = "$Cookies{'user'}";
$password = "$Cookies{'pass'}";

if ($username eq "") {
$INPUT{'page'} = "notlogedin";
&page;
}
else {

$id = "$INPUT{'id'}";
$style = "$INPUT{'style'}";
$width = "$INPUT{'width'}";
$height = "$INPUT{'height'}";
$invisible = "$INPUT{'invisible'}";
$noreload = "$INPUT{'noreload'}";
$bgcolor = "$INPUT{'bgcolor'}";
$fontcolor = "$INPUT{'fontcolor'}";

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="UPDATE `counter` SET `invisible` = '$invisible',
`noreload` = '$noreload',
`style` = '$style',
`width` = '$width',
`height` = '$height', 
`fontcolor` = '$fontcolor', 
`bgcolor` = '$bgcolor' WHERE `owner` = '$username' AND `id` = '$id' LIMIT 1";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 

if ($INPUT{'count'} eq "") {
$INPUT{'count'} = "0";
}

open (wcount, ">./data/$id.cnt");
print wcount "$INPUT{'count'}";
close (wcount);



if ($INPUT{'count'} >= 100000000) {
$longcount = "00000000";

}

if ($INPUT{'count'} <= 99999999) {
$longcount = "$INPUT{'count'}";
}

if ($INPUT{'count'} <= 9999999) {
$longcount = "0$INPUT{'count'}";
}

if ($INPUT{'count'} <= 999999) {
$longcount = "00$INPUT{'count'}";
}

if ($INPUT{'count'} <= 99999) {
$longcount = "000$INPUT{'count'}";
}

if ($INPUT{'count'} <= 9999) {
$longcount = "0000$INPUT{'count'}";
}

if ($INPUT{'count'} <= 999) {
$longcount = "00000$INPUT{'count'}";
}

if ($INPUT{'count'} <= 99) {
$longcount = "000000$INPUT{'count'}";
}

if ($INPUT{'count'} <= 9) {
$longcount = "0000000$INPUT{'count'}";
}


open (wdat, ">./data/$id.dat");
print wdat "Count=$longcount";
close (wdat);


$INPUT{'page'} = "editdone";
&page;
}
}

##########################################

sub delete {

&GetCookies('user');

$username = "$Cookies{'user'}";
$password = "$Cookies{'pass'}";

if ($username eq "") {
$INPUT{'page'} = "notlogedin";
&page;
}
else {

$id = "$INPUT{'id'}";

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="DELETE FROM `counter` WHERE `owner` = '$username' AND `id` = '$id' LIMIT 1";

$sth=$dbh->prepare($temp);
$sth->execute;
$sth->finish; 
$dbh->disconnect; 

unlink ("./data/$id.dat");
unlink ("./data/$id.cnt");
unlink ("./data/$id.rec");

$INPUT{'page'} = "delete";
&page;
}
}

##########################################

sub header {

&GetCookies('user');

$username = "$Cookies{'user'}";
$password = "$Cookies{'pass'}";

print "Content-type: text/html\n\n";

open (header, "<./pages/header.dat");
@head = <header>;
close (header);
$header = "@head";


if ($username ne "") {

open (loged, "<./pages/logedin.dat");
@log = <loged>;
close (loged);
$loged = "@log";
}
else {

open (loged, "<./pages/logedout.dat");
@log = <loged>;
close (loged);
$loged = "@log";
}

$header =~ s/!!loged!!/$loged/gi;

$header =~ s/!!username!!/$username/gi;

print "$header";
}

##########################################

sub footer {
open (footer, "<./pages/footer.dat");
@footer = <footer>;
close (footer);
print "@footer";
}