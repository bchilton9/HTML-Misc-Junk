#!/usr/bin/perl


require "/hsphere/local/home/destiny/destinyeq2.com/cgi-lib.pl";

&ReadParse;

print "Content-type: text/html\n\n<html>\n<body>\n";

$USER = "webmaster\@sanctuaryeq2.com";
$PASSWORD = "dragon45";
$HOST = "mail.sanctuaryeq2.com";
$DOMAIN = "sanctuaryeq2.com";
$username = "linkk";

if ($in{'action'} eq "view") { &view; }
elsif ($in{'action'} eq "delete") { &delete; }
elsif ($in{'action'} eq "deleteall") { &deleteall; }
else { &list; }

##################
sub list {
##################
$shown = 0;

use Mail::POP3Client;
$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $in{'DEBUG'});
  for( $i = 1; $i <= $pop->Count(); $i++ ) {
    $_ = $pop->List($i);
    ($no, $size) = split(/ /);
    $size[$no] = $size;

    foreach( $pop->Head( $i ) ) {
      $to[$no] = $_ if (/To:/);
      $date[$no] = $_ if (/Date:/);
      $from[$no] = $_ if (/From:/);
      $subject[$no] = $_ if (/Subject:/);
    }

  }
$popstate = $pop->State();
$pop->Close();

if (($popstate eq "TRANSACTION") && (@size)) {

print "<center><h3>Showing mailbox for $username</h3></center>\n";
print "<table border=1 align=center width=\"70%\">\n";

for ($i=1;$i<=(scalar @size)-1;$i++) {

if ($to[$i] eq "To: $username\@$DOMAIN") {

    print qq~<tr><td align=center>$i<br>($size[$i])</td><td>

$to[$i]<BR>
$date[$i]<BR>
$from[$i]<br>
$subject[$i]

</td><td align=right>
<FORM action="email.cgi" method=\"get\">
<INPUT TYPE=hidden NAME="action" value="view">
<INPUT TYPE=hidden NAME="message" value="$i">
<input type=submit name="view" value="View">
</FORM>
<FORM action="email.cgi" method=\"get\">
<INPUT TYPE=hidden NAME="action" value="delete">
<INPUT TYPE=hidden NAME="message" value="$i">
<input type=submit name="delete" value="Delete">
</FORM>
</td></tr>\n~;
    $shown++;
}
}

print qq~ </table><br>
<center>$shown messages.<br>

<FORM action="email.cgi" method=\"get\">
<INPUT TYPE=hidden NAME="action" value="deleteall">
<input type=submit name="deleteall" value="Delete All">
</FORM>
</center>

~;

} elsif ($popstate ne "TRANSACTION") {

print "<center>The password you supplied for ".$in{'USER'} ."@". $in{'HOST'} . " is invalid.</center><br>\n";

} elsif (!@size) {

print "<center>The mailbox is empty.</center><br>\n";

}

}

##################
sub view {
##################
$i = $in{'message'};

use Mail::POP3Client;
$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $in{'DEBUG'});

    $_ = $pop->List($i);
    ($no, $size) = split(/ /);
    $size[$no] = $size;

    foreach( $pop->Head( $i ) ) {
      $to[$no] = $_ if (/To:/);
      $date[$no] = $_ if (/Date:/);
      $from[$no] = $_ if (/From:/);
      $subject[$no] = $_ if (/Subject:/);
    }

    foreach( $pop->Body( $i ) ) {
      $body.="$_ <BR>\n";
    }

$popstate = $pop->State();
$pop->Close();

print qq~
$to[$i]<BR>
$date[$i]<BR>
$from[$i]<br>
$subject[$i]<br>
<HR>
$body
<HR>
~;

}

##################
sub delete {
##################
$i = $in{'message'};

$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $in{'DEBUG'});
    $pop->Delete($i);
    $popstate = $pop->State();
  $pop->Close();

open(FILE, "$memberdir/$username.ema");
file_lock(FILE);
chomp(@prefemal = <FILE>);
unfile_lock(FILE);
close(FILE);

$newemal = $prefemal[0] - 1;

open(FILE, ">$memberdir/$username.ema");
file_lock(FILE);
print FILE "$newemal\n";
unfile_lock(FILE);
close(FILE);

print "Location: http://www.destinyeq2.com/email.cgi\n\n";
}

##################
sub deleteall {
##################

$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $in{'DEBUG'});
    for( $i = 1; $i <= $pop->Count(); $i++ ) {
      $pop->Delete($i);
    }
    $popstate = $pop->State();
  $pop->Close();

  open(FILE, ">$memberdir/$username.ema");
file_lock(FILE);
print FILE "0\n";
unfile_lock(FILE);
close(FILE);

print "Location: http://www.destinyeq2.com/email.cgi\n\n";

}