#!/usr/bin/perl 
use DBI; 
$hostname="localhost"; 
$ms="eqguild_guild"; 
$username ="eqguild_guild"; 
$password ="eqg"; 
$data_source = "DBI:mysql:$ms"; 

print "Content-type:text/html \n\n"; 
print "<html>\n";  # HTML Tag starts 
print "<head><title> </title></head>\n"; 
print "<body>"; # Body Starts 
# Reading the query string if the method is post in $query_string scalar variable 
read(STDIN,$query_string,$ENV{'CONTENT_LENGTH'}); 
$i=0; 

#The codes below are used to separate the Name and Value Pairs 
foreach((split('&',$query_string))) 
  { 
    s/\+/ /g; 
    ($fname[$i],$fvalue[$i]) = split('=',$_); 
    $fname[$i] =~ s/%(..)/chr(hex($1))/ge; 
    $fvalue[$i] =~ s/%(..)/chr(hex($1))/ge; 
    $i++; 
  } 

#Now fvalue array contains all the string entered throgh HTML form 

my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

if(($fvalue[0] ne "") and ($fvalue[1] ne "") and ($fvalue[2] ne "") and ($fvalue[3] ne "") and ($fvalue[4] ne "") and ($fvalue[5] ne "")) 
#It checks all the fields, if any field is empty then it will not proceed 
{ 
# Query for inserting  the values (Data) read from HTML form into table  book 
$temp="insert into book values ('$fvalue[0]','$fvalue[1]','$fvalue[2]','$fvalue[3]',$fvalue[4],'$fvalue[5]')"; 

} 
else {  # If any field in the HTML form is empty it comes out giving error message to the OS 
 print "<h1>Fill all the froms and press SUBMIT button</h1>"; 
 exit(1); 
} 
if($sth=$dbh->prepare($temp)) 
{ 
 if($sth->execute) 
 { 
 print "<center><h1> Data Accepted</h1></center>"; 
 } 
 else 
 { 
   print "Can't execute query"; 
 } 

} 
else 
 { 
  print "Query failed";  # In case Query is not correct 
 } 
$sth->finish; 
$dbh->disconnect; 
print "</body>\n"; # End the body of HTML  
print "</html>\n"; # End the HTML Page 
exit(0); 

