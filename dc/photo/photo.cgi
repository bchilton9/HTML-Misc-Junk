#!/usr/local/bin/perl 

require 'cgi-lib2.pl';

&ReadParse;

print "Content-type: text/html\n\n";


if ($in{'a'} eq "uploadfile") { &uploadfile }
elsif ($in{'a'} eq "pform") { &pform; }


sub uploadfile {

   if (!$in{'sourcefile'}) {
   	print "<html><body><center><font size=+1 color=\"FF0000\">ERROR: Upload file not specified or empty.</font></center>";
   	print "<p>You did not provide a file to be uploaded or it is empty.  Please try again.</p>\n";
   	exit;
   }
   if ($ENV{'CONTENT_LENGTH'} > 50000) {
   	print "<html><body><center><font size=+1 color=\"FF0000\">ERROR: Upload file too large.</font></center>";
   	print "<p>Size of your upload file exceeds max file size. Please try again.</p>\n";
   	exit;
   }
   $upload_dir = "/home/erenetw/public_html/defender/photos/";
   if (opendir(DIR,"$upload_dir") != 1) {
         `chmod 0777 $upload_dir`;
   }

   $upload_dir = "$upload_dir/";
   open(REAL,">$upload_dir$in{'destn_filename'}");
   print REAL $in{'sourcefile'};
   close(REAL);
      `chmod 0777 $upload_dir$in{'destn_filename'}`;
   print "<p><center><font size=+1 color=\"FF0000\"><b>File Upload Completed</b></font></center>";
   exit;
}


sub pform {
print <<"HTML";
<CENTER>

<form ENCTYPE="multipart/form-data" method=post action="http://www.erenetwork.com/defender/cgi/photo.cgi">
<input type=hidden name="a" value="uploadfile">
Press the "Browse" button to<BR>
select the file to be uploaded.<br>
<input type=file name="sourcefile"><br>

<input type="submit" value="Upload File">

</form>
HTML
}