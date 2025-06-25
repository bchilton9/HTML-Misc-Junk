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

$log_dir = "/home/erenetw/public_html/ban/data";
$config = "/home/erenetw/public_html/cgi-bin/ban/banners.txt";
$database = "/home/erenetw/public_html/cgi-bin/ban/banners.txt";

###################################################

use CGI qw(:standard);
$ads = new CGI;

$idnum = $ads->param('id');
$redirect = $ads->param('url');

###################################################

if ($INPUT{'a'} eq "url") {
&redirect;
}
elsif ($INPUT{'a'} eq "pic") {
&pic;
}

################
# sub routines #
################


sub redirect
{
	open (LOG,">>$log_dir/$idnum.txt") || &redirect;
	flock(LOG,2);

	print LOG "$ENV{'HTTP_REFERER'} $ENV{'REMOTE_ADDR'} $ENV{'REMOTE_HOST'}\n";

	flock(LOG,8);
	close(LOG);

	open(DB,"$database") || &cgiError("Error Reading $database:", "$!");
	@database = <DB>;
	close(DB);
	
	foreach $line (@database)
	{
		chomp($line);
		($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$line);
		
		if ($id eq "$INPUT{'id'}")
		{
$mainurl = "$url";
		}
	}


$redirect = "http://$mainurl";
print "Location: $redirect\n\n";
}


sub pic
{
	$z = "0";

	open(DB,"$log_dir/exp.txt") || &cgiError("Error Reading $database:", "$!");
	@database = <DB>;
	close(DB);

open(DATA, ">$log_dir/exp.txt");

   foreach $line (@database)
   {
		chomp($line);
		($aid, $view) = split(/::/, $line);
        if ($aid eq "$INPUT{'id'}") {
            $view++;
            print DATA "$INPUT{'id'}::$view\n";
            $z = "1";
        }
        else {
            print DATA "$line\n";
        }
   }

if ($z eq "0") {
print DATA "$INPUT{'id'}::1\n";
}

close DATA;

	open(DB,"$database") || &cgiError("Error Reading $database:", "$!");
	@database = <DB>;
	close(DB);
	
	foreach $line (@database)
	{
		chomp($line);
		($id,$img,$border,$width,$height,$alt,$url,$weight) = split(/\|\|/,$line);
		
		if ($id eq "$INPUT{'id'}")
		{
$mainimg = "$img";
		}
	}

print "Location: $mainimg\n\n";
}
