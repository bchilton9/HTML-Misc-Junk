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

###########################################################################

if ($INPUT{'i'} ne "") { &item; }
elsif ($INPUT{'f'} ne "") { &faq; }
elsif ($INPUT{'c'} eq "1") { &contact; }
elsif ($INPUT{'c'} eq "2") { &contactb; }
elsif ($INPUT{'l'} ne "") { &list; }
elsif ($INPUT{'d'} eq "1") { &dl; }
elsif ($INPUT{'d'} eq "2") { &dlb; }
else { &main; }

###########################################################################

sub main {

$title = "Chilton's Script Archive!";

print "Content-type: text/html\n\n";
&head;

print qq~
<P><BR>
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" WIDTH="75%">
    <TR>
      <TD><CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Welcome</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER></TD>
    </TR>
    <TR>
      <TD>
Welcome to Chilton's Script Archive! I am runing this site for my easy to install,<BR>
Free to low cost, web based programs. Fell free to use them on your webpages<BR>
all I ask for with the free programs is to leave a link to my page.<BR>
The pay for programs you do not need to link to me.
<P><BR>
</TD>
    </TR>
    <TR>
      <TD><CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Featured Script</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER></TD>
    </TR>
    <TR>
      <TD>
Coming Soon!
</TD>
    </TR>
  </TABLE>
</CENTER>
~;

&foot;

}

###########################################################################

sub item {

$item = "$INPUT{'i'}";


my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from item";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] eq "$item") {

$title = "$row[1]";
$depth = "$row[2]";
$description = "$row[3]";
$notes = "$row[4]";
$download = "$row[5]";
$name = "$row[6]";
$other = "$row[7]";
$demo = "$row[8]";
$ver = "$row[9]";
$link = "$row[10]";
}


 } 

}

if ($name eq "") {
$title = "Chilton's Script Archive! > Program not found!";
$depth = "<A HREF=http://www.chiltons.us>Home</A> / Program not found!";

print "Content-type: text/html\n\n";
&head;

print "<CENTER>Where sorry the program you have selected could not be found.<BR>Please Return to the home page and try agine.";
&foot;
end;
}

$sth->finish; 
$dbh->disconnect;


print "Content-type: text/html\n\n";
&head;

print "<SMALL>$depth</SMALL><BR><P>";

print qq~

<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" width=75%>
    <TR>
      <TD>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Name</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER>
</TD>
    </TR>
    <TR>
      <TD>$name ($ver)</TD>
    </TR>
~;
if ($description ne "") {
print qq~
    <TR>
      <TD>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Description</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER>
</TD>
    </TR>
    <TR>
      <TD>$description
~;
if ($other ne "") {
print qq~
<BR>$other
~;
}
print qq~
</TD>
    </TR>

~;
}
if ($demo ne "") {
print qq~
    <TR>
      <TD>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Demo</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER>
</TD>
    </TR>
    <TR>
      <TD>$demo</TD>
    </TR>

~;
}

if ($notes ne "") {
print qq~
    <TR>
      <TD>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Note's</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER>
</TD>
    </TR>
    <TR>
      <TD>$notes</TD>
    </TR>
~;
}

if ($download ne "") {
print qq~

    <TR>
      <TD>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Download</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER>
</TD>
    </TR>
    <TR>
      <TD>$download</TD>
    </TR>

~;
}

print qq~

  </TABLE>
</CENTER>

~;

&foot;

}
###########################################################################

sub faq {

$title = "Chilton's Script Archive! > Help/FAQ";

print "Content-type: text/html\n\n";
&head;

print qq~
<SMALL><A HREF=http://www.chiltons.us>Home</A> / Help/FAQ</SMALL><BR><P>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="75%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Help/FAQ</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER>
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" WIDTH=75%>
~;

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM `faq`";


$sth=$dbh->prepare($temp);
$sth->execute;


while(@row = $sth->fetchrow_array) { 

print qq~
<TR><TD><B>Q: $row[1]</B></TD></TR>
<TR><TD>A: $row[2]</TD></TR>
<TR><TD><HR></TD></TR>
~;

} 

$sth->finish; 
$dbh->disconnect; 

print "</TABLE></CENTER>";
&foot;

}
###########################################################################

sub contact {

$title = "Chilton's Script Archive! > Contact!";

print "Content-type: text/html\n\n";
&head;

print "<SMALL><A HREF=http://www.chiltons.us>Home</A> / Contact</SMALL><BR><P>";

print qq~
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="75%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Contact</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
$tag
<B>Please fill out the Form to contact us!</B><BR>
<FORM onSubmit="return checkEmail(this)">
  <CENTER>
    <TABLE CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Name:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="name" SIZE="40" VALUE="$INPUT{'name'}"></TD>
      </TR>
      <TR>
	<TD>E-Mail:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="email" SIZE="40" VALUE="$INPUT{'email'}"></TD>
      </TR>
      <TR>
	<TD>Problem:</TD>
	<TD>
	  <SELECT NAME="problem">
	  <OPTION SELECTED>Billing
	  <OPTION>Other</SELECT></TD>
      </TR>
      <TR>
	<TD></TD>
	<TD><SMALL>If Other:</SMALL> 
	  <INPUT TYPE="text" NAME="other" SIZE="30" VALUE="$INPUT{'other'}"></TD>
      </TR>
      <TR>
	<TD>Content:</TD>
	<TD><TEXTAREA NAME="content" ROWS="10" COLS="30">$INPUT{'content'}</TEXTAREA></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=hidden NAME=c VALUE=2>
	  <INPUT TYPE=submit VALUE="Submit"> &nbsp;
	  <INPUT TYPE=reset></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
  </CENTER>
~;

&foot;

}

###########################################################################

sub contactb {

if ($INPUT{'name'} eq "") { 
$tag = "Please enter a name!<BR>";
&contact;
end;
 }
elsif ($INPUT{'email'} eq "") { 
$tag = "Please enter a E-Mail address!<BR>";
&contact;
end;
 }
elsif ($INPUT{'content'} eq "") { 
$tag = "Please enter content!<BR>";
&contact;
end;
 }
else {

$mailprog = '/usr/lib/sendmail -i -t';


open(MAIL,"|$mailprog");
    print MAIL "To: $INPUT{'email'}\n";
    print MAIL "From: Byron\@chiltons.us\n";
    print MAIL "Reply-to: Byron\@chiltons.us\n";
    print MAIL "X-Mailer: Chilton's Script Archive\n";
    print MAIL "Subject: Chilton's Script Archive Auto Reply\n\n";
    print MAIL "We have recived the following\n\n";
    print MAIL "Name: $INPUT{'name'}\n";
    print MAIL "E-Mail: $INPUT{'email'}\n";
    print MAIL "Problem: $INPUT{'problem'}\n";
    print MAIL "Other: $INPUT{'other'}\n";
    print MAIL "Content:\n";
    print MAIL "$INPUT{'content'}\n";
    print MAIL "We will respond as soon as posable!";
    print MAIL "\n.\n";
close (MAIL);

open(MAIL,"|$mailprog");
    print MAIL "To: Byron\@chiltons.us\n";
    print MAIL "From: $INPUT{'email'}\n";
    print MAIL "Reply-to: $INPUT{'email'}\n";
    print MAIL "X-Mailer: Chilton's Script Archive\n";
    print MAIL "Subject: Chilton's Script Archive contact form!\n\n";
    print MAIL "Name: $INPUT{'name'}\n";
    print MAIL "E-Mail: $INPUT{'email'}\n";
    print MAIL "Problem: $INPUT{'problem'}\n";
    print MAIL "Other: $INPUT{'other'}\n";
    print MAIL "Content:\n";
    print MAIL "$INPUT{'content'}\n";
    print MAIL "\n.\n";
close (MAIL);

$title = "Chilton's Script Archive! > Contact!";

print "Content-type: text/html\n\n";
&head;

print "<SMALL><A HREF=http://www.chiltons.us>Home</A> / Contact</SMALL><BR><P>";

print qq~
<CENTER>
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="75%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Contact</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>

Thank you! We will respond to your request as soon as posable!<BR><P><A HREF=?>Return to the home page!</A>
~;

&foot;
}
}

###########################################################################
sub list {

$title = "Chilton's Script Archive! > Program's!";

print "Content-type: text/html\n\n";
&head;

print qq~
<SMALL><A HREF=http://www.chiltons.us>Home</A> / Program's</SMALL><BR><P>
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" WIDTH=75%>
~;

my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="SELECT * FROM `item` ORDER BY `name`";


$sth=$dbh->prepare($temp);
$sth->execute;


while(@row = $sth->fetchrow_array) { 

print qq~
<TR><TD>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><A HREF=?i=$row[0]><FONT COLOR=white>$row[6]</FONT></A></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1>~;

if ($row[11] eq "yes") {
print qq~<IMG SRC="http://www.chiltons.us/6.jpg">~;
}
else {
print qq~<IMG SRC="http://www.chiltons.us/5.jpg">~;
}
print qq~</TD>
    </TR>
  </TABLE>
</CENTER>
</TD></TR>
<TR><TD>$row[3]</TD></TR>
~;

} 

$sth->finish; 
$dbh->disconnect; 

print "</TABLE></CENTER>";
&foot;

}
###########################################################################

sub dl {
print "Content-type: text/html\n\n";
&head;
print qq~
<SMALL><A HREF=http://www.chiltons.us>Home</A> / Download</SMALL><BR><P>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="75%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Download</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>
</CENTER>
<FORM onSubmit="return checkEmail(this)">
  <CENTER>
Please enter your E-Mail address to download this program.<BR>
Your address will not be used for naything other then product updates.
    <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>E-Mail:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="email"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=d VALUE=2>
<INPUT TYPE=hidden NAME=in VALUE=$INPUT{'in'}>
	  <INPUT TYPE=submit VALUE="Download"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
~;
&foot;
}

###########################################################################

sub dlb {

$item = "$INPUT{'in'}";


my $dbh = DBI->connect("DBI:mysql:bchilton9_item:freeprohost.com","bchilton9_item","dragon") 
or die "Can't connect to DBI: $dbh->errstr\n"; 

$temp ="select * from item";

if($sth=$dbh->prepare($temp)) 
{ 
 $sth->execute;  #Execute the query 

 while((@row=$sth->fetchrow_array)!=NULL) { 
          $row_hit=1;

if ($row[0] eq "$item") {

$title = "$row[1]";
$depth = "$row[2]";
$description = "$row[3]";
$notes = "$row[4]";
$download = "$row[5]";
$name = "$row[6]";
$other = "$row[7]";
$demo = "$row[8]";
$ver = "$row[9]";
$link = "$row[10]";
}


 } 

}

if ($name eq "") {
$title = "Chilton's Script Archive! > Program not found!";
$depth = "<A HREF=http://www.chiltons.us>Home</A> / Program not found!";

print "Content-type: text/html\n\n";
&head;

print "<CENTER>Where sorry the program you have selected could not be found.<BR>Please Return to the home page and try agine.";
&foot;
end;
}

$sth->finish; 
$dbh->disconnect;


print "Content-type: text/html\n\n";
&head;
print qq~
<SMALL><A HREF=http://www.chiltons.us>Home</A> / Download</SMALL><BR><P>
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center" WIDTH="75%">
    <TR>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/1.jpg"></TD>
      <TD width=25% BACKGROUND="http://www.chiltons.us/2.jpg"><CENTER><FONT COLOR=white>Download</FONT></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/3.jpg"></TD>
      <TD BACKGROUND="http://www.chiltons.us/4.jpg"><IMG SRC="http://www.chiltons.us/4.jpg"></TD>
      <TD WIDTH=1><IMG SRC="http://www.chiltons.us/5.jpg"></TD>
    </TR>
  </TABLE>

<A HREF=$link>Click here to download this program.</A>
</CENTER>
~;
&foot;
}

###########################################################################

sub head {
open (HEAD, "header.txt");
@DATA=<HEAD>;
close (HEAD);
foreach $line (@DATA){
$line =~ s/!!title!!/$title/gi;
print "$line";
}
}

sub foot {
open (FOOT, "footer.txt");
@DATA=<FOOT>;
close (FOOT);
print "@DATA";

}