#!/usr/bin/perl

$| = 1;
use CGI::Carp qw(fatalsToBrowser);
$scriptname = "Gallery";
$scriptver = "0.9.9";

BEGIN {

	require "../../../config.pl";
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



# ----------- print everything to the browser ---
$navbar = "&nbsp;$btn{'014'}&nbsp; $cm_title";
print_top();

&PrintDefault;

print_bottom();



# _____________________________________________________________________________
sub PrintDefault {

open (DATA, "db.dat");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($name, $path) = split(/::/, $line);

if ($input{'view'} eq "$path") {
$usename = "$name";
}

}


$count = 0;

print qq~
<CENTER>
<B>$usename</B><BR>
<SMALL>Click to enlarge</SMALL>
<P>
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
    <TR>
~;

open (DATA, "./$input{'view'}/db.dat");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($img, $desc) = split(/::/, $line);

$count = $count + 1;
 
print qq~
<TD>
<A HREF=http://www.eqguilded.com/freefire/gallery/$input{'view'}/$img onclick="NewWindow(this.href,'name','800','600','yes');return false;"><IMG SRC=http://www.eqguilded.com/freefire/gallery/$input{'view'}/$img WIDTH=150 HEIGHT=150 BORDER="0"></A><BR>
$desc
</TD>
~;

if ($count eq 4) {
$count = 0;
print qq~
    </TR>
    <TR>
~;
}

}

print qq~
    </TR>
  </TABLE>
<P>
~;

}



########################################
# Code to get the data from GET & POST #
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