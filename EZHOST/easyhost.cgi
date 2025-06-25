#!/usr/bin/perl

use strict;

### Configure

my %objects = ();
my %config = ();

open(CONFIG,($0 =~ /(.+)\./)[0].'.conf');
while (<CONFIG>)
{
	chop if (/\n/);
	my @line = split(/=/,$_,2);
	$config{$line[0]} = $line[1];
}
close(CONFIG);

use CGI qw/:cgi/;
my $cgi = new CGI;

if ($config{'setup'})
{
	push (@INC,($0 =~ /(.+)[\\\/]/)[0]);
	require 'easyhost.setup';
}
else
{
	my $interface = $ARGV[0] || 'go';

	push (@INC,$config{'system_dir'}.'lib');
	require $interface.'.pl';
}

&go($cgi,%config);