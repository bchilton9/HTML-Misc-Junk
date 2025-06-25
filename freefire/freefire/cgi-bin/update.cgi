#!/usr/bin/perl




	open(FILE, "./db/members/memberlist.dat");

	chomp(@memberlist = <FILE>);

	close(FILE);



print "Content-type: text/html\n\n";

foreach $member (@memberlist) {

print "$member Done!<BR>";

	open(FILE, ">./db/members/$member.inv");
	file_lock(FILE);
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	print FILE "Empty\n";
	unfile_lock(FILE);
	close(FILE);

}


print "done!";