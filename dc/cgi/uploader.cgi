#!/usr/local/bin/perl 

require 'cgi-lib2.pl';

# Indicate if your server O/S is Unix/Linux or Windows NT
# Set to "unix" if Unix or Linux; set to "nt" if Windows NT
$serverOS = "unix";

# This parameter defines what character set you want the Web
# browser to be set to when viewing your Html pages.
# Default is "". Chinese GB = "gb2312". Chinese Big5 = "Big5".
$charset = "";

# Supervisor Password.
$superpwd = "rose";

# Full pathname of directory (parent) which is 1 level higher than
# the "file upload" directory (directory storing the uploaded files).
# This directory must be resided in a Html directory
# Create this directory manually if it is not already existed.
# Use chmod command to set this directory to writable, i.e. 0777.
# The last "/" character is significant.
$parent_dir = "/home/erenetw/public_html/dc/";

# Maximum file size ( in bytes ) allowed to be uploaded to the server
# Note: This value will be superceded by the value defined in the (optional)
# form statement <input type=hidden name="maxfilesize" value="someValue">
# if it is present in your "uploader" html form.
$maxfilesize = "20480"; 

# Return URL link used by OK and error messages
$return_url = "http://www.erenetwork.com/dc";

# These are the urls that are allowed to execute this program
# eg. @valid = ('abc.com','def.com','xyz.net');
@valid = ('erenetwork.com');

####### End of field definitions ####

############# Must not change the codes after this line ###########
#############    if you don't know what you are doing   ###########

# Parse Form Contents
&ReadParse;

if ($ENV{'REQUEST_METHOD'} ne 'POST') {
   &error_not_a_command;
}

$| = 1;

# Validate & execute command according to Action Type
unless (
   ($in{'action'} eq "uploadfile") ||
   ($in{'action'} eq "listfilenames")) { 
   &error_not_a_command;
}

if ($in{'action'} eq "uploadfile") {&uploadfile}
if ($in{'action'} eq "listfilenames") {&listfilenames}
exit;


sub uploadfile {
   &check_url_referer;

   if ($in{'pwd'} ne $superpwd) {
      &error_password;
   }
   if (!$in{'sourcefile'}) {
      &error_uploadfile;
   }
   if (!$in{'filedirname'}) {
      &error_no_upload_directory;
   }
   if ($in{'filedirname'} =~ /[^a-z0-9A-Z]+/) {
      &error_invalid_directory_name;
   }
   if ($in{'maxfilesize'}) {
      $maxfilesize = $in{'maxfilesize'};
   }
   if ($ENV{'CONTENT_LENGTH'} > $maxfilesize) {
      &error_file_too_large;
   }
   $upload_dir = "$parent_dir$in{'filedirname'}";
   if (opendir(DIR,"$upload_dir") != 1) {
      if (mkdir($upload_dir,0777) == 0) {
         &cannot_create_directory;
      } 
      if ($serverOS =~ /^unix$/i) {
         `chmod 0777 $upload_dir`;
      }
   }

   $upload_dir = "$upload_dir/";
   open(REAL,">$upload_dir$in{'destn_filename'}") || &error_open_file;
   if ($serverOS =~ /^nt$/i) {   
      binmode(REAL);
   }
   print REAL $in{'sourcefile'};
   close(REAL);

   if ($serverOS eq "unix") {
      `chmod 0777 $upload_dir$in{'destn_filename'}`;
   }

   &upload_ok;
}


sub listfilenames {
   &check_url_referer;

   if ($in{'pwd'} ne $superpwd) {
      &error_password;
   }
   if (!$in{'filedirname'}) {
      &error_no_upload_directory;
   }
   $list_dir = "$parent_dir$in{'filedirname'}";
   if (opendir(DIR,"$list_dir") == 1) {
      @files = readdir(DIR);
      closedir(DIR);
   }
   else {
      &error_cannot_open_dir;
   }

   &set_content_type;
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>Listing of Filenames</b></font></center><p>\n";
   print "<b>The following filenames are found in directory \"$in{'filedirname'}\":<br>\n";
   $count = 0;
   foreach $fitem (@files) {
      $fitem_pathname = "$list_dir" . "/" . "$fitem";
      if (-e $fitem_pathname) {
         if (-d $fitem_pathname) {next;}
         $count++;
         print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$fitem<br>\n";
      }
   }
   if ($count == 0) {
      print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sorry, nothing found!!<br>\n";
   }
   print "</b><p>\n";

   &listfilenames_ok;
}


sub return {
   print "Location: $ENV{'DOCUMENT_URI'}\n\n";
}

sub check_url_referer {
   $referral_cnt = @valid;
   if ($referral_cnt > 0) {
      foreach $referer (@valid) {
	   if ($ENV{'HTTP_REFERER'} =~ /$referer/i) {
	      $good_ref = "yes";
            last;
	   }
      }
      if ($good_ref ne "yes") {
         &go_away; 
      }
   }
}

sub error_password {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Invalid password</b></font></center>";
   print "<p>You didn't supply a valid password. Please check and enter again.</p></body></html>\n";
   exit;
}

sub error_not_a_command {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Not a valid command</b></font></center>";
   print "<p>You did not select a valid command. Please check and try again.</p></body></html>\n";
   exit;
}

sub go_away {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Unauthorised Access</b></font></center>";
   print "<p>Request denied. You are attempting to access our server using an unauthorized form.</p></body></html>\n";
   exit;
}

sub cannot_create_directory {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Cannot create the upload directory</b></font></center>";
   print "<p>Please check your input and try again. If the problem repeats, please contact your Webmaster.</p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub error_invalid_directory_name {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Invalid upload directory name</b></font></center>";
   print "<p>Please check your input and try again. Directory name must contain alphanumeric characters only.</p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub set_content_type {
   if ($charset eq "") {
      print "content-type: text/html\n\n";
   } else {
      print "content-type: text/html\; charset=$charset\n\n";
   }
}

sub upload_ok {
   &set_content_type;
   print "<p><center><font size=+1 color=\"FF0000\"><b>File Upload Completed</b></font></center>";
   print "<p><center><b>URL for image: http://www.erenetwork.com/dc/photos/$in{'destn_filename'}</b></center></p></body></html>\n";
   exit;
}

sub listfilenames_ok {
   print "<p><center><b>Total files listed = $count</b></center></p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub error_no_source_file {
   &set_content_type;
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Source File Is Empty</b></font></center>";
   print "<p>You must select a source file to be uploaded. Please try again.</p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub error_no_upload_directory {
   &set_content_type;
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Upload directory name absent</b></font></center>";
   print "<p>You did not enter an upload directory name. Please try again. Directory name must contain alphanumeric characters only.</p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub error_cannot_open_dir {
   &set_content_type;
   print "<html><body><center><font size=+1 color=\"FF0000\"><b>ERROR: Cannot open the directory</b></font></center>";
   print "<p>Please supply a valid directory name and try again.</p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub error_file_too_large {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\">ERROR: Upload file too large.</font></center>";
   print "<p>Size of your upload file exceeds $maxfilesize bytes. Please try again.</p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub error_uploadfile {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\">ERROR: Upload file not specified or empty.</font></center>";
   print "<p>You did not provide a file to be uploaded or it is empty.  Please try again.</p>\n";
   print "<p><center><b><a href=\"$return_url\">Back Home</a></b></center></p></body></html>\n";
   exit;
}

sub error_open_file {
   &set_content_type; 
   print "<html><body><center><font size=+1 color=\"FF0000\">ERROR: Destination upload file cannot be opened.</font></center>";
   print "<p>Please contact Webmaster.</p></body></html>\n";
   exit;
}

