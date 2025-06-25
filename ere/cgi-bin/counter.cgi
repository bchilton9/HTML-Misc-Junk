#!/usr/bin/perl

## Dectory for counter images
$image_directory = "/home/erenetw/public_html/counter";

## HTML dectory for counter images
$html_image_directory = "http://www.erenetwork.com/counter";

## Path to fly program (Read the ReadMe.txt
$flyprog = "/home/erenetw/public_html/cgi-bin/fly-1.6.5/fly -q";

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
if ($INPUT{'u'}) {
open (FILE, "$data_path/$INPUT{'u'}.mem");
flock (FILE, 2);
$name = <FILE>;
chop ($name);
$cryptpass = <FILE>;
chop ($cryptpass);
$mail = <FILE>;
chop ($mail);
$url = <FILE>;
chop ($url);
$site_title = <FILE>;
chop ($site_title);
flock (FILE, 8);
close(FILE);

if ($INPUT{'u'} eq "webmaster") { 
$name = "webmaster";
}
if ($name eq "") { 
$alow = "no";
}
else {
if ($INPUT{'p'}) {
if ($INPUT{'h'} eq "") { $INPUT{'h'} = "15"; }
if ($INPUT{'w'} eq "") { $INPUT{'w'} = "15"; }
if ($INPUT{'r'} eq "") { $INPUT{'r'} = "1"; }
if ($INPUT{'z'} eq "") { $INPUT{'z'} = "auto"; }
if ($INPUT{'s'} eq "") { $INPUT{'s'} = "1"; }

open(COUNTERDB,"<$data_path\/$INPUT{'u'}.cnt");
@counterdb = <COUNTERDB>;
close(COUNTERDB);
$x = "0";
$found = "0";
foreach $counter (@counterdb) {
    ($countername,$value,$IPs,undef) = split(/\::/,$counter);
    if ($countername eq $INPUT{'p'}) { $dbnumber = $x; $found = "1"; }
    $x++;
}
if ($found eq "0") {
    $counter_value = "1";
    push(@counterdb,join("\::",$INPUT{'p'},"1",$ENV{'REMOTE_ADDR'},"\n"));
    $already_visited = "0";
}
if ($found eq "1") {
    @counter_profile = split(/\::/,$counterdb[$dbnumber]);
    $counter_profile[1]++;
    @IPs = split(/\,/,$counter_profile[2]);
    push(@IPs,$ENV{'REMOTE_ADDR'});
    if ($counter_profile[2] =~ $ENV{'REMOTE_ADDR'}) { $already_visited = "1"; } else { $already_visited = "0"; }
    $counter_profile[2] = join("\,",@IPs);
    $counter_value = $counter_profile[1];
    $counterdb[$dbnumber] = join("\::",@counter_profile);
}
if (($INPUT{'r'} eq "1" && $already_visited eq "0") || $INPUT{'r'} eq "0") {
    open(COUNTERDB,">$data_path\/$INPUT{'u'}.cnt");
    print COUNTERDB @counterdb;
    close(COUNTERDB);
} 
else { $counter_value = $counter_value - 1; }
if (length($counter_value) < $INPUT{'z'}) {
    while (length($counter_value) < $INPUT{'z'}) { $counter_value = "0" . $counter_value; }
}
@digits = split(//,$counter_value);
$total_width = $INPUT{'w'} * scalar(@digits);
open(FLY,">$data_path\/$INPUT{'u'}_temp.txt");
print FLY "new\n";
print FLY "size $total_width,$INPUT{'h'}\n";
$insert_width = "0";
foreach $digit (@digits) {
    print FLY "copy $insert_width,0,-1,-1,-1,-1,$image_directory/$INPUT{'s'}/$digit.gif\n";
    $insert_width = $insert_width + $INPUT{'w'};
}
close(FLY);
print "Content-type: image/gif\n\n";
print `$flyprog -i $data_path/$INPUT{'u'}_temp.txt`;
unlink("$data_path\/$INPUT{'u'}_temp.txt");
}
}
}