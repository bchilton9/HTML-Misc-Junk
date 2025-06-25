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
    push(@values,$value); push(@names,$name);   
    $INPUT{$name} = $value;
  }

print "Content-type: text/html\n\n";

open (DATA, "admin/$INPUT{'page'}.dat");
@data = <DATA>;
close DATA;

print "@data";