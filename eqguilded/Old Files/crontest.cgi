#!/usr/bin/perl

open (FILE, "cron.cnt");
flock (FILE, 2);
$cnt = <FILE>;
chop ($abcdefg);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$cnt++;

open(DATA, ">cron.cnt");
print DATA "$cnt\n";
print DATA "junk\n";
close DATA;


print "Content-type: text/html\n\n";

print "done this $cnt times";