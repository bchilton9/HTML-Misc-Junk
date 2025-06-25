#!/usr/bin/perl

$| = 1;
use CGI::Carp qw(fatalsToBrowser);
$scriptname = "Page";
$scriptver = "0.9.9";

BEGIN {

	require "../../config.pl";
	require "$lang";
	require "$sourcedir/subs.pl";


	push(@INC,$cm_scriptDir);
}

eval {
	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};

if ($@) {
	print "Content-type: text/html\n\n";
	print qq~<h1>Software Error:</h1>
		Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
		<pre>$@</pre>
		<p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
		~;
	exit;
}

&parse_form;


logips();
loadcookie();
loaduser();
logvisitors();


########################################

$navbar = "&nbsp;$btn{'014'}&nbsp; $input{'go'}";

print_top();

open (DATA, "./pages/$input{'go'}.dat");
@data = <DATA>;
close DATA;

print "@data";

print_bottom();

########################################

sub parse_form {

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
   @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $input{$name} = $value;
   }
}

1;