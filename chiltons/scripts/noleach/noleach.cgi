#!/usr/bin/perl

$domain = "www.d0tt.com";

	read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$INPUT{$name} = $value;
	}

	@pairs = split(/&/, $ENV{'QUERY_STRING'});
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$INPUT{$name} = $value;
	}


#$refer = "$ENV{'HTTP_REFERER'}";

#if ($refer eq "$domain") {
print "Content-Type: text/html\n\n";
print "Caller = $ENV{'HTTP_REFERER'}\n";
#}

#else {
#print "Content-Type: text/html\n\n";
#print "<center><h2>This file is being stolen</h2><HR>";
#print "$refer is steeling my files<BR>";
#print "For a good download site go to:";
#print "<A HREF=http://$domain>$domain</A><P>";
#print "NoLeach by <A HREF=http://www.d0tt.com>Byron</a>";
#}