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
    $INPUT{$name} = $value;
}

if ($INPUT{"cbreceipt"} eq "") {
print "Content-type: text/html\n\n";
print <<"HTML";
There has been an error<BR>
If you have ordered remote please<BR>
Email the webmaster at webmaster\@erenetwork.com<BR>
<A HREF=http://www.clickbank.com>www.ClickBank.com</A>
HTML
}

elsif ($INPUT{"cbreceipt"} eq "val") {
$a = "0";

open (DATA, "/home/erenetw/public_html/cgi-bin/sell.txt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($user, $passA, $emailA, $urlA) = split(/::/, $line);
if ($INPUT{'user'} eq "$user") { $a="1"; }
}

if ($a eq "0") { 
$cyppass = crypt($INPUT{'pass'}, "YL");
open (DATA, "/home/erenetw/public_html/cgi-bin/sell.txt");
@data = <DATA>;
close DATA;
open(DATA, ">/home/erenetw/public_html/cgi-bin/sell.txt");
print DATA "$INPUT{'user'}::$cyppass::$INPUT{'email'}::$INPUT{'url'}\n";
foreach $line (@data) {
chomp ($line);
print DATA "$line\n";
}
close DATA;

open (DATA, "/home/erenetw/public_html/remote/members/.htpasswd");
@data = <DATA>;
close DATA;
open(DATA, ">/home/erenetw/public_html/remote/members/.htpasswd");
print DATA "$INPUT{'user'}:$cyppass\n";
foreach $line (@data) {
chomp ($line);
print DATA "$line\n";
}
close DATA;

print "Content-type: text/html\n\n";
print <<"HTML";
<CENTER>
Thank you<BR>
Your username and password will now work at the members page at<BR>
<A HREF=http://www.erenetwork.com/remote/members>http://www.erenetwork.com/remote/members</a><BR>
Username: $INPUT{'user'}<BR>
Password: $INPUT{'pass'}<BR>
Thank you<BR>
<A HREF=http://www.clickbank.com>www.ClickBank.com</A>
HTML
 }
else { 
print "Content-type: text/html\n\n";
print <<"HTML";
<CENTER>
Sorry that user name is taken<BR>
please hit your back butten<BR>
and chose anoputher one
HTML
 }
}

elsif ($INPUT{"cbreceipt"} ne "") {

print "Content-type: text/html\n\n";

print <<"HTML";
<FORM ACTION="sell.cgi" METHOD="POST">
<CENTER>
This is the last step<BR>
Please Enter a username and password<BR>
If you dont you will not be abel to downlaod the script<BR>
Or recive updates<BR>
Fields in <FONT color=red>Red</FOnt> are required
<TABLE BORDER CELLPADDING="2" ALIGN="Center">
<TR><TD><FONT color=red>Username</FOnt></TD><TD>
<INPUT TYPE="text" NAME="user"></TD>
</TR><TR>
<TD><FONT color=red>Password</FOnt></TD><TD>
<INPUT TYPE="text" NAME="pass"></TD>
</TR><TR>
<TD>E-Mail</TD><TD><INPUT TYPE="text" NAME="email"></TD>
</TR><TR><TD>URL</TD>
<TD><INPUT TYPE="text" NAME="url" VALUE="http://"></TD></TR><TR>
<TD COLSPAN=2><P ALIGN=Center>
<INPUT NAME="cbreceipt" VALUE=val TYPE=hidden>
<INPUT TYPE=submit VALUE="Finish"></TD>
 </TR></TABLE></CENTER></FORM><BR>
<CENTER>
<A HREF=http://www.clickbank.com>www.ClickBank.com</A>
HTML
}