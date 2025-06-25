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

############################################################

if ($INPUT{'do'} eq "lock") { &lock; }
elsif ($INPUT{'do'} eq "unlock") { &unlock; }
else { &main; }

############################################################

sub main {

open (DATA, "lock.dat");
@data = <DATA>;
close DATA;
chop(@data);

$locked = "@data";


print "Content-type: text/html\n\n";

print qq~

<CENTER>
<H2>Freefire Website is curently $locked</H2>

~;

if ($locked eq "LOCKED") {

print "<A HREF=?do=unlock>UnLock The Web Site!</A>";

}
else {

print "<A HREF=?do=lock>Lock The Web Site!</A>";

}

}

############################################################

sub lock {

open(DATA, ">lock.dat");
print DATA "LOCKED\n";
close DATA;

print "Content-type: text/html\n\n";

print qq~
<CENTER><H2>Freefire Web site Now Locked</H2>
~;

}

############################################################

sub unlock {

open(DATA, ">lock.dat");
print DATA "UNLOCKED\n";
close DATA;

print "Content-type: text/html\n\n";

print qq~
<CENTER><H2>Freefire Web site Now UnLocked</H2>
~;


}