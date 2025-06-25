#!/usr/bin/perl 
###################Database connectivity###############3 
use DBI; 
$hostname="localhost"; #Host name 
$ms="ncsi"; 
$username ="ncsi"; 
$password ="ncsidb"; 
$data_source = "DBI:mysql:$ms"; 

read(STDIN,$query_string,$ENV{'CONTENT_LENGTH'}); 
$i=0; # used for array index 
$flag=0; # If both the search form field is empty the flag = 0 otherwise if any field is not empty flag =1 
$row_hit=0; # Used 
####################### 
foreach((split('&',$query_string))) 
  { 
    s/\+/ /g; 
    ($fname[$i],$fvalue[$i]) = split('=',$_); 
    $fname[$i] =~ s/%(..)/chr(hex($1))/ge; 
    $fvalue[$i] =~ s/%(..)/chr(hex($1))/ge; 
    $i++; 
  } 
my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 
print "Content-type:text/html \n\n"; 
print "<html>"; 
print "<head><title> </title></head>"; 

print "<body>"; 
print "<center><h1> The result of the query</h1></center>"; 
if(($fvalue[0] ne "") or ($fvalue[2] ne ""))  # If any of the two search form fields is not empty 
{ 
 $flag=1; 
 if(($fvalue[0] ne "") and ($fvalue[2] ne "")) 
 { 
    # If both form fields are not empty then the Query for selecting rows of table book 
 $temp ="select * from book where Title like '%$fvalue[0]%' $fvalue[1] Author like '%$fvalue[2]%'"; 
 } 
 elsif(($fvalue[0] eq "") and ($fvalue[2] ne "")) 
 { 
       #If Second form field is not empty 
      $temp ="select * from book where  Author like '%$fvalue[2]%'"; 
 } 
 elsif(($fvalue[0] ne "") and ($fvalue[2] eq "")) 
 { 
     #If first field is not empty then the query 
     $temp ="select * from book where Title like '%$fvalue[0]%'"; 
 } 
} 
else {  # If both fields are empty 
 print "Enter the search word in any of the froms"; 
 print "<br>"; 
 print "<h2>Press back button to renter the words</h2>"; 
} 
if($flag==1)  
{ 
print "<center>"; 

#Codes below are for creating table in the Browser 
     print "<table border cellpadding=4>"; 
     print"<tr>"; 
     print"<th colspan=95 align=center>Title</th>"; 
     print"<th colspan=25 align=center>Author</th>"; 
     print"<th colspan=20 align=center>Publication Year</th>"; 
     print"<th colspan=20 align=center>Publisher</th>"; 
     print"<th colspan=10 align=center>Accession No.</th>"; 
     print"<th colspan=10 align=center>Language</th>"; 
     print"</tr>"; 
if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) 
        # Fetch one row at a time from table book and store into array @row 
          { 
          $row_hit=1; #If the row is not empty 
       # Print then rows in the table format 
       print "<tr>"; 
       print"<td colspan=95  align=center>$row[0]</th>"; 
       print"<td colspan=25 align=center>$row[1]</td>"; 
       print"<td colspan=20 align=center>$row[2]</td>"; 
       print"<td colspan=20 align=center>$row[3]</td>"; 
       print"<td colspan=10 align=center>$row[4]</td>"; 
       print"<td colspan=10 align=center>$row[5]</td>"; 
       print "</tr>"; 
 } 
 if((!$sth->fetchrow_array) and ($row_hit==0)) 
  #If nothing there in the table 
 { 
  print "<h1>No suitable match is found</h1>"; 
  exit(1); 
 } 
} 
else 
 { 
  print "Query failed"; 
 } 
 print "</center>"; 
 print "</table>"; 
} 
$sth->finish; 
$dbh->disconnect; 
print "</body>\n"; 
print "</html>\n"; 
exit(0); 

