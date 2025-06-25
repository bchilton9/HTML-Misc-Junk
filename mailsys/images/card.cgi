#!/usr/bin/perl

######################################################################################
##  http://www.erenetwork.com/mailsys/images/card.cgi?mode=1&from=&image=&mess=%20  ##
######################################################################################

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
print "Content-type: text/html\n\n";


if ($INPUT{'mode'} eq "1") {

print "<HEAD>\n";
print "<SCRIPT LANGUAGE=\"JavaScript\"><!-- Begin\n";
print "theUrl=\"card.cgi?mode=2&from=$INPUT{'from'}&image=$INPUT{'image'}&mess=$INPUT{'mess'}\";\n";
print "function doThePopUp() {\n";
print "reWin = window.open(theUrl,'determined','toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=350,height=350,top=100,left=100');\n";
print "}\n";
print "//  End --></script>\n";
print "</HEAD><BODY onLoad=\"doThePopUp();self.close()\"></BODY>\n";

}

if ($INPUT{'mode'} eq "2") {
print "<HTML><HEAD><TITLE>MailSys Furry Card</TITLE>\n";
print "</HEAD><BODY BGCOLOR=ffffff><CENTER>\n";
print "<TABLE BORDER=0 CELLPADDING=2 ALIGN=Center><TR><TD><P ALIGN=Center>\n";
print "$INPUT{'from'} Sent you this card.</TD>\n";
print "</TR><TR><TD><P ALIGN=Center>\n";
print "<IMG SRC=$INPUT{'image'}.gif></TD>\n";
print "</TR><TR><TD><P ALIGN=Center>\n";
print "$INPUT{'mess'}</TD>\n";
print "</TR><TR><TD></TD></TR><TR><TD><P ALIGN=Center>\n";
print "<A HREF=http://www.erenetwork.com/mailsys>MailSys</A></TD>\n";
print "</TR></TABLE></CENTER><P>\n";
print "<CENTER><IMG SRC=http://66.33.1.160/count/mailsys/1.gif WIDTH=114 HEIGHT=35> \n";
print "</BODY></HTML>\n";
}