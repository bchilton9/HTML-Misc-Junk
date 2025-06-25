#!/usr/bin/perl


require 'cookie.lib';

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


if ($INPUT{'a'} eq "login") { &login; }
elsif ($INPUT{'a'} eq "logout") { &logout; }
else { &main; }


sub login {


## ADD IN VALADATE MEMBERS CODE

$user = "$INPUT{'username'}";
$pass = "$INPUT{'password'}";

 &SetCookiesSave('user',"$user");
 &SetCookiesSave('pass',"$pass");


           print "Content-type: text/html\n\n";
print qq~
<HTML>
<HEAD>
<META HTTP-EQUIV="Refresh" CONTENT="2;URL=index.cgi">
<TITLE>Loging in</TITLE>
</HEAD>
<BODY>
<CENTER>Please wate whale we log you in.
</BODY>
</HTML>
~;
   exit;

}

sub logout {

   &SetCookies('user',"");
   &SetCookies('pass',"");

print "Content-type: text/html\n\n";
print qq~
<HTML>
<HEAD>
<META HTTP-EQUIV="Refresh" CONTENT="2;URL=index.cgi">
<TITLE>Loging out</TITLE>
</HEAD>
<BODY>
<CENTER>Please wate whale we log you out.
</BODY>
</HTML>
~;
  exit;

}

sub main {

&GetCookies('user');

$username = "$Cookies{'user'}";
$password = "$Cookies{'pass'}";

print "Content-type: text/html\n\n";

print qq~
<HTML>
<HEAD>
<TITLE>Index</TITLE>
</HEAD>
<BODY bgcolor="#000000">
<CENTER>
  <TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" ALIGN="Center">
    <TR>
      <TD>

<OBJECT WIDTH="100%" HEIGHT="100%" id="Index" ALIGN="">
 <PARAM NAME=movie VALUE="Index.swf">
<PARAM NAME=quality VALUE=high>
<PARAM NAME=bgcolor VALUE=#ffffff>
<PARAM NAME=FlashVars VALUE="cookie=$username&mylogo=logo.jpg">


<EMBED src="Index.swf"
 quality=high
 bgcolor=#ffffff
 WIDTH="900"
 HEIGHT="500"
 NAME="Index"
 ALIGN=""
 FlashVars="cookie=$username&mylogo=logo.jpg"></EMBED>

</OBJECT>
</TD>
    </TR>
  </TABLE>
</CENTER>
</BODY>
</HTML>
~;
}