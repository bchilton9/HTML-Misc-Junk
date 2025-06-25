#!/usr/bin/perl 

use DBI;   # DBI  is perl module used to connect to the database 
$hostname="localhost"; #Host name on which MySQL server is running 
$ms="eqguild_guild";                     # Name of the database to connect 
$username ="eqguild_guild";         # Database user who wants to connect to the Server 
$password ="eqg";      # Password for the database user 
$data_source = "DBI:mysql:$ms:$hostname";  # MySQL driver 

my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 
# Connects to the MySQL  server 

# Query for Creating table 
 $stmt="create table book ( 
Title char(255), 
Author char(100), 
Pub_year char(4), 
Publisher char(100), 
acc_no int(11) not null, 
language char(20))"; 

print "Content-type :text/html\n\n";  # Content Type is needed for displying messages in the browser 

$sth=$dbh->prepare($stmt); # Necessary for execution 

if($sth->execute)                    # Executes the Query prepared 
{ 
 print "Table book is Successfully created";  # Prints Messages in the browser is successfull 
} 
else { 
  print "Can't execute the query"; # In case some errors  
       exit(1); 
     } 

$sth->finish;    #Finish execution No needed 
$dbh->disconnect;  # Disconnect to the database server 
exit(0);  # Tells OS that operation was successful 
