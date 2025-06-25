#!/usr/bin/perl

####################################################################################
##  <FORM ACTION="http://www.erenetwork.com/eq/cgi-bin/members.cgi" METHOD="POST">
##  <CENTER><TABLE BORDER CELLPADDING="2" ALIGN="Center"><TR><TD>UserName:</TD><TD>
##  <INPUT TYPE="text" NAME="user"></TD></TR><TR><TD>Password:</TD><TD>
##  <INPUT TYPE="password" NAME="pass"></TD></TR><TR><TD>E-Mail:</TD><TD>
##  <INPUT TYPE="text" NAME="email"></TD></TR><TR><TD COLSPAN=2><P ALIGN=Center>
##  <INPUT TYPE="hidden" NAME="A" VALUE="signup"><INPUT TYPE=submit></TD></TR>
##  </TABLE></CENTER></FORM>
####################################################################################

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
    push(@values,$value); push(@names,$name);   
    $INPUT{$name} = $value;
  }

print "Content-type: text/html\n\n";

if ($INPUT{'A'} eq "login") { &login }
elsif ($INPUT{'A'} eq "signup") { &signup }
elsif ($INPUT{'A'} eq "admin") { &adminA }
elsif ($INPUT{'A'} eq "adminB") { &adminB }
elsif ($INPUT{'A'} eq "content") { &content }
elsif ($INPUT{'A'} eq "Update Content") { &upcontent }
elsif ($INPUT{'A'} eq "editpage") { &editpage }
elsif ($INPUT{'A'} eq "editpageB") { &editpageB }
elsif ($INPUT{'A'} eq "Update Page") { &uppage }
else {
print <<"HTML";
<FORM>
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>UserName:</TD>
	<TD>
	  <INPUT TYPE="text" NAME="user"></TD>
      </TR>
      <TR>
	<TD>Password:</TD>
	<TD>
	  <INPUT TYPE="password" NAME="pass"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE="hidden" NAME="A" VALUE="login">
	  <INPUT TYPE=Submit VALUE="Submit"></TD>
      </TR>
    </TABLE>
<SMALL><SMALL><FONT COLOR=red><B>USERNAME AND PASSWORD IS CASE SENSATIVE!!
  </CENTER>
</FORM>
HTML
}


sub login {
	open (DATA, "admin/mem.dat");
	@data = <DATA>;
	close DATA;
	foreach $line (@data) {
		chomp ($line);
		($Auser, $Apass, $Aemail) = split(/::/, $line);
		if ($Auser eq $INPUT{'user'}) {
			$user = $Auser;
			$pass = $Apass;
		}
	}

if ($user eq $INPUT{'user'}) {
	if ($pass eq $INPUT{'pass'}) {
		&main;
	}
	else {
		print "<CENTER>Invalid Password";
	}
}
else {
print "<CENTER>Invalid UserName";
}
}


sub signup {
	open (DATA, "admin/mem.dat");
	@data = <DATA>;
	close DATA;
	foreach $line (@data) {
		chomp ($line);
		($Auser, $Apass, $Aemail) = split(/::/, $line);
		if ($Auser eq $INPUT{'user'}) {
			$user = $Auser;
		}
	}

		if ( $user eq "" ) {
			open(data, ">>admin/mem.dat");
			@data=<data>;
			close(data);
			open(data, ">>admin/mem.dat");
			foreach $line (@data){
				print data "$line";
			}
			print data "$INPUT{'user'}::$INPUT{'pass'}::$INPUT{'email'}\n";
			close(data);

			print "<CENTER>Account Created!";
			&main;
		}
		else {
			print "<CENTER>Username Taken!";
		}

}

sub main {
open (HEAD, "admin/data.pl");
@DATA=<HEAD>;
close (HEAD);
foreach $line (@DATA){
print "$line";
}
}

sub adminA {
print <<"HTML";
<FORM ACTION="members.cgi" METHOD="POST">
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Password 1:</TD>
	<TD>
	  <INPUT TYPE="password" NAME="pass1"></TD>
      </TR>
      <TR>
	<TD>Password 2:</TD>
	<TD>
	  <INPUT TYPE="password" NAME="pass2"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE="hidden" NAME="A" VALUE="adminB">
	  <INPUT TYPE=submit></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}

sub adminB {
if ( $INPUT{'pass1'} eq "0519aa" ) {
	if ( $INPUT{'pass2'} eq "shellee" ) {
print <<"HTML";
<CENTER> Add Account<BR>
<FORM><CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center><TR><TD>UserName:</TD><TD>
<INPUT TYPE=text NAME=user></TD></TR><TR><TD>Password:</TD><TD>
<INPUT TYPE=password NAME=pass></TD></TR><TR><TD>E-Mail:</TD><TD>
<INPUT TYPE=text NAME=email></TD></TR><TR><TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE=hidden NAME=A VALUE=signup><INPUT TYPE=submit></TD></TR>
</TABLE></CENTER></FORM>
<P>
<A HREF="members.cgi?A=content">Update Content</A>
<P>
<A HREF="members.cgi?A=editpage">Update Page</A>
HTML

	}
	else {
		print "<CENTER>Invalid Password";
	}
}
else {
	print "<CENTER>Invalid Password";
}
}

sub content {
print <<"HTML";
<FORM METHOD="POST">
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  Content</TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <TEXTAREA NAME="content" ROWS="15" COLS="60">
HTML

open (DATA, "admin/data.pl");
@data = <DATA>;
close DATA;

print "@data";


print <<"HTML";
</textarea></TD>
      </TR>
      <TR>
	<TD COLSPAN=2><P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Update Content" NAME=A></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}

sub upcontent {
open (DATA, "admin/data.pl");
@data = <DATA>;
close DATA;
open(DATA, ">admin/data.pl");

print DATA "$INPUT{'content'}";

print <<"HTML";
<CENTER><B>Content has been Updated</B><BR>
HTML
}

sub editpage {
print "<CENTER>";
open (DATA, "admin/pages.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
print "<A HREF=members.cgi?A=editpageB&page=$line>Edit $line</A><BR>";
}
print <<"HTML";
<FORM METHOD="POST">
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD>Page Name</TD>
	<TD>
	  <INPUT TYPE="text" NAME="page"></TD>
      </TR>
      <TR>
	<TD COLSPAN=2>
	  <INPUT TYPE="hidden" NAME="new" VALUE="true">
	  <INPUT TYPE="hidden" NAME="A" VALUE="editpageB">
	  <P ALIGN=Center>
	  <INPUT TYPE=submit VALUE="Add Page"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}

sub editpageB {
if ($INPUT{'new'} eq "true") { 
open (DATA, "admin/pages.dat");
@data = <DATA>;
close DATA;
open(DATA, ">admin/pages.dat");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$INPUT{'page'}\n";
close DATA;
 }

print <<"HTML";
<FORM METHOD="POST">
  <CENTER>
    <TABLE BORDER CELLPADDING="2" ALIGN="Center">
      <TR>
	<TD><P ALIGN=Center>
	  $INPUT{'page'}<INPUT TYPE=hidden NAME="page" VALUE="$INPUT{'page'}"></TD>
      </TR>
      <TR>
	<TD><TEXTAREA NAME="content" ROWS="15" COLS="60">
HTML

open (DATA, "admin/$INPUT{'page'}.dat");
@data = <DATA>;
close DATA;

print "@data";

print <<"HTML";
</textarea></TD>
      </TR>
      <TR>
	<TD><P ALIGN=Center>
	  <INPUT TYPE=submit NAME="A" VALUE="Update Page"></TD>
      </TR>
    </TABLE>
  </CENTER>
</FORM>
HTML
}

sub uppage {
open (DATA, "admin/$INPUT{'page'}.dat");
@data = <DATA>;
close DATA;
open(DATA, ">admin/$INPUT{'page'}.dat");

print DATA "$INPUT{'content'}";

print <<"HTML";
<CENTER><B>Page has been Updated</B><BR>
URL to page is<BR>
http://www.erenetwork.com/eq/cgi/page.cgi?page=$INPUT{'page'}
HTML

}