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

print "Content-type: text/html\n\n";

if ($INPUT{'id'} eq "") {
print "Error No id entered";
}
else {
open (FILE, "data/$INPUT{'id'}");
flock (FILE, 2);
$name = <FILE>;
chop ($name);
$zone = <FILE>;
chop ($zone);
$prop = <FILE>;
chop ($prop);
$type = <FILE>;
chop ($type);
$slot = <FILE>;
chop ($slot);
$ac = <FILE>;
chop ($ac);
$dmg = <FILE>;
chop ($dmg);
$boost = <FILE>;
chop ($boost);
$effect = <FILE>;
chop ($effect);
$weight = <FILE>;
chop ($weight);
$size = <FILE>;
chop ($size);
$class = <FILE>;
chop ($class);
$race = <FILE>;
chop ($race);
$drop = <FILE>;
chop ($drop);
$desc = <FILE>;
chop ($desc);
$form = <FILE>;
chop ($form);
$zonea = <FILE>;
chop ($zonea);
$zoneb = <FILE>;
chop ($zoneb);
$zonec = <FILE>;
chop ($zonec);
$zoned = <FILE>;
chop ($zoned);
$zonee = <FILE>;
chop ($zonee);
$zonef = <FILE>;
chop ($zonef);
$zoneg = <FILE>;
chop ($zoneg);
$mapa = <FILE>;
chop ($mapa);
$mapb = <FILE>;
chop ($mapb);
$mapc = <FILE>;
chop ($mapc);
$mapd = <FILE>;
chop ($mapd);
$mape = <FILE>;
chop ($mape);
$mapf = <FILE>;
chop ($mapf);
$mapg = <FILE>;
chop ($mapg);
flock (FILE, 8);
close(FILE);

if ($name eq "") {
print "Error Id not found";
}
else {
print "$name<BR>\n";
print "$zone<BR>\n";
print "$prop<BR>\n";
print "$type<BR>\n";
print "$slot<BR>\n";
print "$ac<BR>\n";
print "$dmg<BR>\n";
print "$boost<BR>\n";
print "$effect<BR>\n";
print "$weight<BR>\n";
print "$size<BR>\n";
print "$class<BR>\n";
print "$race<BR>\n";
print "$drop<BR>\n";
print "$desc<BR>\n";
print "$form<BR>\n";
print "$zonea<BR>\n";
print "$zoneb<BR>\n";
print "$zonec<BR>\n";
print "$zoned<BR>\n";
print "$zonee<BR>\n";
print "$zonef<BR>\n";
print "$zoneg<BR>\n";
print "$mapa<BR>\n";
print "$mapb<BR>\n";
print "$mapc<BR>\n";
print "$mapd<BR>\n";
print "$mape<BR>\n";
print "$mapf<BR>\n";
print "$mapg<BR>\n";
}
}