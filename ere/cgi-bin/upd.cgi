#!/usr/bin/perl

require "config.pl";

open (DATA, "mem.data");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);

open (FILE, "$data_path/$line.mem");
$name = <FILE>;
chop ($name);
$cryptpassaaa = <FILE>;
chop ($cryptpass);
$mail = <FILE>;
chop ($mail);
$url = <FILE>;
chop ($url);
$site_title = <FILE>;
chop ($site_title);
close(FILE);

$cryptpass = crypt(16598, "aa");

open(cnt, ">$data_path/$line.mem");
print cnt "$name\n";
print cnt "$cryptpass\n";
print cnt "$mail\n";
print cnt "$url\n";
print cnt "$site_title\n";
close(cnt);

open (MAIL, "| $mailprog -t -oi") || die "Can't open $mailprog";
print MAIL "To: $mail\n";
print MAIL "Reply-to: $email\n";
print MAIL "From: $email\n";
print MAIL "Subject: ERE Network! Has changed servers\n";
print MAIL "ERE Network! Has changed servers\n";
print MAIL "The new server will be faster have more space\n";
print MAIL "and the counters and clocks will now work.\n";
print MAIL "The DNS will take maby a few days to transfer\n";
print MAIL "wach at www.erenetwork.com for it to be updated.\n";
print MAIL "There are no codeings that have to be replaced.\n";
print MAIL "Eavrything will be transfered to the newserver.\n";
print MAIL "The onely drawback is that the encryptshen on the passwords is\n";
print MAIL "diffrent on the new server.\n";
print MAIL "YOUR PASSWORD HAVE BEEN SET TO \"16598\"!\n";
print MAIL "PLEASE GO TO www.erenetwork.com\n";
print MAIL "AND CHANGE YOUR PASSWORD once the DNS is updated!\n";

print "Content-type: text/html\n\n";
print "<CENTER><B>done $mail $line</B></CENTER>";
}

##