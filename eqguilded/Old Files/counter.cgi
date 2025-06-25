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
    if ($value eq "") { $value = "NULL"; }
    $INPUT{$name} = $value;
}


$image_directory = "/home/eqguild/public_html/images/$INPUT{'i'}";

if ($INPUT{'i'} eq "1") {
$img_width = "13";
$img_height = "17";
}
if ($INPUT{'i'} eq "2") {
$img_width = "13";
$img_height = "17";
}
if ($INPUT{'i'} eq "3") {
$img_width = "23";
$img_height = "24";
}
if ($INPUT{'i'} eq "4") {
$img_width = "18";
$img_height = "24";
}
if ($INPUT{'i'} eq "5") {
$img_width = "25";
$img_height = "25";
}
if ($INPUT{'i'} eq "6") {
$img_width = "25";
$img_height = "30";
}
if ($INPUT{'i'} eq "7") {
$img_width = "24";
$img_height = "30";
}
if ($INPUT{'i'} eq "8") {
$img_width = "24";
$img_height = "24";
}
if ($INPUT{'i'} eq "9") {
$img_width = "9";
$img_height = "46";
}
if ($INPUT{'i'} eq "10") {
$img_width = "15";
$img_height = "20";
}
if ($INPUT{'i'} eq "11") {
$img_width = "15";
$img_height = "20";
}
if ($INPUT{'i'} eq "12") {
$img_width = "16";
$img_height = "24";
}

$reload_protection = "1";
$counter_size = "auto";
$flyprog = "/home/eqguild/public_html/fly-1.6.5/fly -q";
$script_directory = "/home/eqguild/public_html";

# open the counter database
open(COUNTERDB,"<$script_directory/counters.db");
@counterdb = <COUNTERDB>;
close(COUNTERDB);

# see if this page already has an entry in the database
$x = "0";
$found = "0";
foreach $counter (@counterdb) {
    ($countername,$value,$IPs,undef) = split(/\|/,$counter);
    if ($countername eq $INPUT{'guild'}) { $dbnumber = $x; $found = "1"; }
    $x++;
}

# create new entry if this is the page's first hit
if ($found eq "0") {
    $counter_value = "1";
    push(@counterdb,join("\|",$INPUT{'guild'},"1",$ENV{'REMOTE_ADDR'},"\n"));
    $already_visited = "0";
}

# increase the count if this is an already existing counter
if ($found eq "1") {
    @counter_profile = split(/\|/,$counterdb[$dbnumber]);
    $counter_profile[1]++;
    @IPs = split(/\,/,$counter_profile[2]);
    push(@IPs,$ENV{'REMOTE_ADDR'});
    if ($counter_profile[2] =~ $ENV{'REMOTE_ADDR'}) { $already_visited = "1"; } else { $already_visited = "0"; }
    $counter_profile[2] = join("\,",@IPs);
    $counter_value = $counter_profile[1];
    $counterdb[$dbnumber] = join("\|",@counter_profile);
}

# update the counter database, if everything is ok
if (($reload_protection eq "1" && $already_visited eq "0") || $reload_protection eq "0") {
    open(COUNTERDB,">$script_directory/counters.db");
    print COUNTERDB @counterdb;
    close(COUNTERDB);
} else { $counter_value = $counter_value - 1; }

# create the number that will be shown
if (length($counter_value) < $counter_size) {
    while (length($counter_value) < $counter_size) { $counter_value = "0" . $counter_value; }
}
@digits = split(//,$counter_value);

# open fly
$total_width = $img_width * scalar(@digits);
open(FLY,">$script_directory/fly_temp.txt");
print FLY "new\n";
print FLY "size $total_width,$img_height\n";

# add all the digits
$insert_width = "0";
foreach $digit (@digits) {
    print FLY "copy $insert_width,0,-1,-1,-1,-1,$image_directory/$digit.gif\n";
    $insert_width = $insert_width + $img_width;
}

# close fly
close(FLY);

# send output to user
print "Content-type: image/gif\n\n";
print `$flyprog -i $script_directory/fly_temp.txt`;

# delete temporary file
unlink("$script_directory/fly_temp.txt");
