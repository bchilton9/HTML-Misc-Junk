#!/usr/bin/perl

## use this script to see your server's information

$master_cfg_dir="/somewhere/abmasterd"; # change this to the master cfg dir you created

server_info();
test_modules();

print "<h1>INC</h1>";
print join("\n", @INC);
print "<h1>PROGRAM: $0</h1>";
print "<h1>PERL: $^X</h1>";

print_file("/etc/fstab");
win32_tests();

sub print_file {
    my $f = shift;
print "<h1>$f on cgi server: ", `hostname`, "</h1>";
open F, "<$f";
print "<pre>";
print join ("<br>", <F>);
print "</pre>";
close F;
}


sub s_2col_tb{
    my $tstr = qq(<table border=0 cellpadding=3 cellspacing=3 bgcolor="#eeeecc" width=95%><tr bgcolor="#99cccc">);
    for (@_) {
       $tstr .= qq(<th> <font face="Verdana">$_\&nbsp;</font></th>);
    } 
    return $tstr."</tr>";
}

sub s_2col_tr{
    my $color = shift;
    $color = qq(bgcolor="$color") if $color;
    my $tstr = qq(<tr $color>);
    for (@_) {
       $tstr .= qq(<td> $_\&nbsp;</td>);
    } 
    return $tstr."</tr>";
}
sub server_info {
   my $i=0;
   print "Content-type: text/html\n\n";
   print qq(<html><body>);
   print &s_2col_tb("Attribute", "Value", "Comments");
   print &s_2col_tr($bgs[$i++%2], "WEB site", $ENV{SERVER_NAME}, "");
   print &s_2col_tr($bgs[$i++%2], "Server", $ENV{SERVER_SOFTWARE}, "");
   print &s_2col_tr($bgs[$i++%2], "OS", $^O, "");
   print &s_2col_tr($bgs[$i++%2], "DOCROOT", $ENV{DOCUMENT_ROOT}, "");
   print &s_2col_tr($bgs[$i++%2], "SERVER ROOT", $ENV{SEVER_ROOT}, "");
   print &s_2col_tr($bgs[$i++%2], "PERL VERSION", $], ($]< 5.004)?"Needs upgrade":"");
   print &s_2col_tr($bgs[$i++%2], "CGI User", eval('(getpwuid($<))[0] || "unknown"'), "");
   print &s_2col_tr($bgs[$i++%2], "PATH_INFO", $ENV{PATH_INFO}, "");
   my $test="";                  
   my $path = $ENV{PATH_TRANSLATED};
   $test = "Not exist or not a dir!\n" if(not -d $path);
   $test .= "Not writable!\n" if(not -w $path);
   $test .= "Not owned by CGI user!\n" if(not -O $path);
   print &s_2col_tr($bgs[$i++%2], "PATH", $ENV{PATH_TRANSLATED}, $test);
   print &s_2col_tr($bgs[$i++%2], "Working directory", $ENV{PWD}||`pwd`, "");
   $path = $master_cfg_dir;
   $test = "";
   $test = "Not exist or not a dir!\n" if(not -d $path);
   $test .= "Not writable!\n" if(not -w $path);
   $test .= "Not owned by CGI user!\n" if(not -O $path);
   print &s_2col_tr($bgs[$i++%2], "Master CFG", $path,  $test);
   print &s_2col_tr($bgs[$i++%2], "Script Name", $ENV{SCRIPT_NAME}, "");
   print &s_2col_tr($bgs[$i++%2], "Script File", $ENV{SCRIPT_FILENAME}, "prog=$0");
   print "</table></body></html>";
}

sub test_modules {
    @mods = qw(Socket integer vars POSIX Fcntl);
    for(@mods) {
      eval "use $_";
      print "Test $_: ";
      print "OK" if not $@;
      print $@ if $@;
      print "<p>";
    }
}

sub win32_tests{
    print "test functions\n";
    @funcs = qw(alarm crypt flock);
    for(@funcs) {
	eval "$_(0,0)";
        print "$_:", $@? $@:"OK<br>";
     }
}
   

