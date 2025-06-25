#!/usr/bin/perl

use CGI::Carp qw(fatalsToBrowser);
#
#
# Spam Bot Killer --> Written for WebAPP
#
#
print "Content-type: text/html\n\n";

&getcgi();

require "./../cgi-bin/config.pl";
if ($botkiller eq "" || $botkiller eq "1") {

&banip();

&ban();

}

############
sub getcgi {
############

	read(STDIN, $input, $ENV{'CONTENT_LENGTH'});
	@pairs = split(/&/, $input);
	foreach $pair(@pairs) {

	        ($name, $value) = split(/=/, $pair);
	        $name =~ tr/+/ /;
	        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $value =~ tr/+/ /;
	        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $input{$name} = $value;
	}
	@vars = split(/&/, $ENV{QUERY_STRING});
	foreach $var(@vars) {
	        ($v,$i) = split(/=/, $var);
	        $v =~ tr/+/ /;
	        $v =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $i =~ tr/+/ /;
	        $i =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $i =~ s/<!--(.|\n)*-->//g;
	        $input{$v} = $i;
	}

}

#################
sub banip {
#################

    require "./../cgi-bin/config.pl";
    open (FILE , ">>$datadir/banned/banned_ip.txt") || error("$err{'001'} $datadir/banned/banned_ip.txt");
    hold(FILE);
    print FILE "$ENV{'REMOTE_ADDR'}\n";
    close (FILE);


}

################
sub ban {
################
	
	require "./../cgi-bin/config.pl";
	open (BANNED , "$datadir/banned/banned_ip.txt");
	hold(BANNED);
	while (<BANNED>) {
			
			 chomp;
			 if ($_ eq  $ENV{'REMOTE_ADDR'}) {
				 print "Content-type: text/html\n\n";
				 print "You're IP is: $ENV{'REMOTE_ADDR'}<br>";
				 print FILE "[BANNED_IP] $_ at attemp to connect. Rejecting";
				 print "<b>You are banned from this site..... Rejecting connection<\b>"; exit;

				 
				
				}	
		}
	
	close BANNED;

}

1;
