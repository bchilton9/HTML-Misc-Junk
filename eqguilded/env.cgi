#!/usr/bin/perl

print "Content-Type: text/html\n\n";

my $i;
foreach $i (keys %ENV){
	print "$i: $ENV{$i}<br>";
}
