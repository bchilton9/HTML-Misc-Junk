#!/usr/local/bin/perl
# -------------------------------------------
$ENV{'REQUEST_METHOD'} and (print "Content-type: text/plain\n\n");
open (DB, "<links.db")     or print "Unable to open links database 'links.db'. Reason: $!" and exit;
open (DBOUT, ">links2.db") or print "Unable to open output database. Make sure hits dir is chmod 777 temporairly. Reason: $!" and exit;
while (<DB>) {
    chomp;
    s/NULL//g;
    print DBOUT "$_|Yes\n";
}
close DB;
close DBOUT;
print "Added two new fields onto the end. Saved it as links2.db. Change permissions back to 755 on the hits directory.";
# ---------------------------------------------