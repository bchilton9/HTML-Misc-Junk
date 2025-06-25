#!/usr/bin/perl

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

use DBI;

$hostname="localhost";
$ms="eqguild_guild";
$username ="eqguild_guild";
$password ="eqg";
$data_source = "DBI:mysql:$ms:$hostname";


if ($INPUT{'do'} eq "create_table") { &create_table; }
elsif ($INPUT{'do'} eq "enter_into_table") { &enter_into_table; }
elsif ($INPUT{'do'} eq "enter_into_table_b") { &enter_into_table_b; }
elsif ($INPUT{'do'} eq "view_table") { &view_table; }
elsif ($INPUT{'do'} eq "delete_entry") { &delete_entry; }
elsif ($INPUT{'do'} eq "edit_entry") { &edit_entry; }
elsif ($INPUT{'do'} eq "edit_entry_b") { &edit_entry_b; }
else { &link; }

######################################################################
sub edit_entry {
print "Content-type: text/html\n\n";
print <<"HTML";
<FORM METHOD="POST">
  <TABLE BORDER CELLPADDING="2">
    <TR>
      <TD>Name:</TD>
      <TD>
	<INPUT TYPE="hidden" NAME="name" VALUE=$INPUT{'name'}>$INPUT{'name'}</TD>
    </TR>
    <TR>
      <TD>E-Mail:</TD>
      <TD>
	<INPUT TYPE="text" NAME="email" VALUE=$INPUT{'email'}></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<INPUT TYPE="hidden" VALUE="edit_entry_b" NAME="do">
	<INPUT TYPE=submit></TD>
    </TR>
  </TABLE>
</FORM>
HTML
}

######################################################################

sub edit_entry_b {

my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$email = "$INPUT{'email'}";
$name = "$INPUT{'name'}";

$temp="UPDATE user SET email = '$email' WHERE name = '$name'"; 

$sth=$dbh->prepare($temp);

$sth->execute;

print "Content-type: text/html\n\n";
 print "Entry edited"; 

$sth->finish; 
$dbh->disconnect; 

}

######################################################################

sub delete_entry {

my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$name = "$INPUT{'name'}";

$temp = "DELETE FROM user WHERE name = '$name'"; 

$sth=$dbh->prepare($temp);

$sth->execute;

print "Content-type: text/html\n\n";
print "Entry Deleted"; 

$sth->finish; 
$dbh->disconnect; 

}

######################################################################

sub view_table {

my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

print "Content-type: text/html\n\n";

print "table<BR>";

$temp ="select * from user ORDER BY name";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) { 

          #$row_hit=1;

       print"$row[0] "; 
       print"$row[1] "; 
       print"<A HREF=?do=edit_entry&name=$row[0]&email=$row[1]>EDIT</A> <A HREF=?do=delete_entry&name=$row[0]>DELETE</A><BR>"; 
 } 


$sth->finish; 
$dbh->disconnect; 

}

######################################################################

sub enter_into_table {
print "Content-type: text/html\n\n";
print <<"HTML";
<FORM METHOD="POST">
  <TABLE BORDER CELLPADDING="2">
    <TR>
      <TD>Name:</TD>
      <TD>
	<INPUT TYPE="text" NAME="name"></TD>
    </TR>
    <TR>
      <TD>E-Mail:</TD>
      <TD>
	<INPUT TYPE="text" NAME="email"></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<INPUT TYPE="hidden" VALUE="enter_into_table_b" NAME="do">
	<INPUT TYPE=submit></TD>
    </TR>
  </TABLE>
</FORM>
HTML
}

######################################################################

sub enter_into_table_b {

my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$temp="insert into user values ('$INPUT{'name'}','$INPUT{'email'}')"; 

$sth=$dbh->prepare($temp);

$sth->execute;

print "Content-type: text/html\n\n";
 print "Entry Added"; 

$sth->finish; 
$dbh->disconnect; 

}

######################################################################

sub create_table {

my $dbh = DBI->connect($data_source,$username,$password) 
or die "Can't connect to $data_source: $dbh->errstr\n"; 

$stmt = "create table user (name char(15), email char(100))"; 

$sth = $dbh->prepare($stmt);

$sth->execute;

print "Content-type: text/html\n\n";
 print "Table created"; 

$sth->finish;
$dbh->disconnect;

}

######################################################################

sub link {

print "Content-type: text/html\n\n";
print <<"HTML";

<A HREF=?do=create _table>Create Table</A><BR>
<A HREF=?do=enter_into_table>Add User</A><BR>
<A HREF=?do=view_table>View Table</A><BR>
HTML
}