#!/usr/bin/perl

# <!--#exec cgi="/cgi-bin/plugit.cgi" --> 

{
&PlugIt;
}

sub PlugIt
{
$plugit="links.txt";

open (PLUG,$plugit) || die "can't open $plugout";
$plugit="";
while (<PLUG>){$plugit .=$_;}
close(PLUG);

print "Content-type: text/html\n\n";
print "$plugit";

}
1;