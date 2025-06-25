#!/usr/bin/perl 
require "admin.pl";
$| = 1;
my $length = $ENV{CONTENT_LENGTH};
my $query = $ENV{QUERY_STRING};
my (@assign);
if ($query){
@assign = split(/&/,$query);
$formlength = @assign;
}
elsif ($length) {
sysread(STDIN, $_, $length);
chomp;
@assign = split('&');
$formlength = @assign;
}
else {
$formlength = 0;
}
for (my $i=0; $i<$formlength; $i++) {
my ($name,$value) = split('=',$assign[$i]);
$value =~ tr/+/ /;
$value =~ s/%([a-fFA-F0-9][a-fFA-F0-9])/pack("C", hex($1))/eg;
$value =~ s/~!/ ~!/g;
$in{$name} = $value;
}
$prog = $0;
$prog =~ m|admin\.(\w+)|; $prog = "admin.$1";
$cgi_extension = $1;
$root_path = $ENV{DOCUMENT_ROOT};
$root_url = $ENV{HTTP_HOST};
open (PROG, $prog);
@prog = <PROG>;
close (PROG);
$perl = $prog[0];
$perl =~ s/^#!//;
$mailer  = '/var/qmail/bin/qmail-inject';
$mailer1  = '/bin/sendmail';
$mailer2 = '/usr/lib/sendmail';
$mailer3 = '/usr/bin/sendmail';
$mailer4 = '/usr/sbin/sendmail';
if ( -e $mailer) {
    $mail_program=$mailer;
} elsif( -e $mailer1){
    $mail_program=$mailer1;
} elsif( -e $mailer2){
    $mail_program=$mailer2;
} elsif( -e $mailer3){
    $mail_program=$mailer3;
} elsif( -e $mailer4){
    $mail_program=$mailer4;
} else {
    $mail_program="<font color=red>Mail Program Not Detected</font>";
}
if ($] < 5) {
	$perl4warn = "<FONT COLOR=#ff0000><B>Perl Version Warning</B>:  The Perl path that\n";
	$perl4warn .= "you selected, <B>$perl</B>, is running Perl version $].\n";
	$perl4warn .= "List Site PRO requires Perl 5.  In most cases,\n";
	$perl4warn .= "there will not be any difficulties, but it is <U>strongly</U>\n";
	$perl4warn .= "recommended that you consult your ISP's documents and determine\n";
	$perl4warn .= "if you can select a different Perl path for Perl version 5.</FONT>\n";
}
&clean_data;
&update_data;

if ($in{'step'} eq "1") {
print "Content-type: text/html\n\n";
print <<EOF;
<html>
<head>
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>List Site PRO - Set Up Server</title>
</head>
<body>
<form method="POST" action="admin.cgi">
  <p><font size="4">List Site PRO Setup</font></p>
  <p>#!$perl<br> version $]</p>
  <p>$perl4warn</p>
<p>Step 1. The default path for Perl is #!/usr/local/bin/perl for this
  program. If your path is different you need to open the following files and
  change them to the correct path. Always use a text editor like Notepad or Wordpad and save the 
  file in standard text format. Do not use a program 
  like Microsoft Word or you will have problems. The path for Perl is the very first line in each
  of the files.</p>
  <p>lspro.cgi<br>
  lspromember.pl<br>
  lspro_account_manager.pl<br>
  </p>
  <p>Step 2. Complete the following information for your server. The examples
  shown are suggested and may not be the exact settings for your server. You may
  have to adjust them. Consult with your host administrator if you are having
  difficulties.</p>
  <p>What is your cgi URL? (http://$root_url/cgi-bin/lspro)</p>
  <p><input type="text" name="lspro_cgi_url" size="40" value="$lspro_cgi_url"></p>
  <p>What is your path to your top site? ($root_path/topsites)</p>
  <p><input type="text" name="lspro_root_path" size="40" value="$lspro_root_path"></p>
  <p>What is you URL to your top site? (http://$root_url/topsites)</p>
  <p><input type="text" name="lspro_base_url" size="40" value="$lspro_base_url"></p>
  <p>What is your top site file name? (index.html)</p>
  <p><input type="text" name="lspro_file_name" size="25" value="$lspro_file_name"></p>
  <p>What is your mail program name? ($mail_program)</p>
  <p><input type="text" name="mailprog" size="25" value="$mailprog"></p>
  <p><input type="submit" value="Submit" name="B1"></p>
</form>
</body>
</html>
EOF
exit;
}
elsif ($in{'step'} eq "2") {
print "Content-type: text/html\n\n";
print <<EOF;
<html>
<head>
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>List Site PRO - Configure Top Site Options</title>
</head>
<body>
<form method="POST" action="admin.cgi">
  <p><font size="4">List Site PRO Setup</font></p>
  <p>Complete the following information for your top site.</p>
  <p>What is the email address for your members to contact you? ($ENV{SERVER_ADMIN})</p>
  <p><input type="text" name="lspro_email_address" size="30" value="$lspro_email_address"></p>
  <p>What is the name of your top site? (Top 100 Sites)</p>
  <p><input type="text" name="lspro_site_name" size="30" value="$lspro_site_name"></p>
  <p>Do you want to display the name of your top site at the top of the ranking page? (Y/N)</p>
  <p><input type="text" name="display_site_name" size="5" value="$display_site_name"></p>
  <p>What is the maximum number of members you want to list? (15, 50, 100)</p>
  <p><input type="text" name="max_record" size="5" value="$max_record"></p>
  <p>What is the minimum number of hits your member must have to get on the
  list? (0, 1, 2)</p>
  <p><input type="text" name="min_record_to_list" size="5" value="$min_record_to_list"></p>
  <p>What is the maximum number of members banners you want to show? (5, 10)</p>
  <p><input type="text" name="max_banner" size="5" value="$max_banner"></p>
  <p>What is the maximum width of a members banner they can use? (468)</p>
  <p><input type="text" name="max_banner_width" size="5" value="$max_banner_width"></p>
  <p>What is the maximum height of a members banner they can use? (60)</p>
  <p><input type="text" name="max_banner_height" size="5" value="$max_banner_height"></p>
  <p>What is the number of minutes you want your top site to update? (30, 60)</p>
  <p><input type="text" name="set_update" size="5" value="$set_update"> </p>
  <p>What is the number of days you want your top site to reset? (1, 7)</p>
  <p><input type="text" name="set_reset" size="5" value="$set_reset"></p>
  <p><input type="submit" value="Submit" name="B2"></p>
</form>
</body>
</html>
EOF
exit;
}
elsif ($in{'step'} eq "3") {
print "Content-type: text/html\n\n";
print <<EOF;
<html>
<head>
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>List Site PRO - Configure Linking Options</title>
</head>
<body>
<form method="POST" action="admin.cgi">
  <p><font size="4">List Site PRO Setup</font></p>
  <p>Complete the following information for your top site.</p>
  <p>What is file name of your vote button image? (image.gif)</p>
  <p><input type="text" name="image_filename" size="20" value="$image_filename"></p>
  <p>What is the URL of the vote button image? (http://$root_url/images)</p>
  <p><input type="text" name="image_url" size="40" value="$image_url"></p>
  <p>What is the width of your vote button image? (468)</p>
  <p><input type="text" name="image_width" size="5" value="$image_width"></p>
  <p>What is the height of your vote button image? (60)</p>
  <p><input type="text" name="image_height" size="5" value="$image_height"></p>
  <p>What text do you want to use for a text link? (Vote for Top 100 Sites)</p>
  <p><input type="text" name="image_text" size="30" value="$image_text"></p>
  <p><input type="submit" value="Submit" name="B2"></p>
</form>
</body>
</html>
EOF
exit;
}
elsif ($in{'step'} eq "4") {
print "Content-type: text/html\n\n";
print <<EOF;
<html>
<head>
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>List Site PRO - Configure Tables and Colors</title>
</head>
<body>
<form method="POST" action="admin.cgi">
  <p><font size="4">List Site PRO Setup</font></p>
  <p>Complete the following information for your top site.</p>
  <p>What text font do you want your top site title? (Arial, Comic Sans MS, Courier, Helvetica, Tahoma, Times New Roman, Verdana)</p>
  <p><input type="text" name="lspro_site_name_font" size="15" value="$lspro_site_name_font"></p>
  <p>What text font do you want the rest of your top site? (Arial, Comic Sans MS, Courier, Helvetica, Tahoma, Times New Roman, Verdana)</p>
  <p><input type="text" name="lspro_table_font" size="15" value="$lspro_table_font"></p>
  <p>What is the URL of your top site background image? (http://$root_url/images/background.gif)</p>
  <p><input type="text" name="lspro_background_image" size="45" value="$lspro_background_image"></p>
  <p>What is the color of your top site background? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_background_color" size="10" value="$lspro_background_color"></p>
  <p>What font color is your top site link? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_link_color" size="10" value="$lspro_link_color"></p>
  <p>What font color is your top site visited link? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_visited_link_color" size="10" value="$lspro_visited_link_color"></p>
  <p>What font color is your top site active link? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_active_link_color" size="10" value="$lspro_active_link_color"></p>
  <p>What is the size of your top top site table border? (0=no border, 1, 2, 3)</p>
  <p><input type="text" name="lspro_table_border_siz" size="5" value="$lspro_table_border_size"></p>
  <p>What color do you want the top site table header? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_table_heading_color" size="10" value="$lspro_table_heading_color"></p>
  <p>What color do you want the top site table header text? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_table_text_color" size="10" value="$lspro_table_text_color"></p>
  <p>What color do you want the top site table cells? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_cell_background_color" size="10" value="$lspro_cell_background_color"></p>
  <p>What color do you want the top site table cell text? (#000000=black, #FFFFFF=white, #FF0000=red, #008000=green, #0000FF=blue)</p>
  <p><input type="text" name="lspro_cell_text_color" size="10" value="$lspro_cell_text_color"></p>
  <p><input type="submit" value="Submit" name="B2"></p>
</form>
</body>
</html>
EOF
exit;
}
elsif ($in{'step'} eq "5") {
$create = "0";
open(NEWUSER,">update_time.txt");
print NEWUSER $create;
close(NEWUSER);
print "Location: $lspro_cgi_url/lspro.cgi?click=setup\n\n";
exit;
}
elsif ($in{'step'} eq "6") {
print "Content-type: text/html\n\n";
print <<EOF;
<html>
<head>
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>List Site PRO - Create Password Files</title>
</head>
<body>
<p>Create Password Files</p>
<form method="POST" action="admin.cgi">
  <p>Step 1. Enter your user name: <input type="text" name="username" size="20"></p>
  <p>Step 2. Enter your password: <input type="text" name="password" size="20"></p>
  <p>Step 3. Write down your user name and password.</p>
  <p>Note: You will only be prompted for your user name and password once per
  session. Do not be alarmed if you are not required to login each time you
  access the admin file. The password protection is most likely working and if a
  new user tries to gain access they will be prompted for a user name and
  password.</p>
  <p><input type="submit" value="Submit" name="B1"></p>
  <input type="hidden" value="encrypt" name="action">
</form>
<p>&nbsp;</p>
</body>
</html>
EOF
exit;
}

if ($in{'action'} eq "encrypt") {
$htpasswd = $ENV{SCRIPT_FILENAME};
for ($htpasswd) {
s/admin.cgi/.htpasswd/g;
}
$password = crypt($in{'password'}, "Cd");
open (PASS, ">$htpasswd");
print PASS "$in{'username'}:$password\n";
close (PASS);

$htaccess = $ENV{SCRIPT_FILENAME};
for ($htaccess) {
s/admin.cgi/.htaccess/g;
}
$filetext = "AuthName \"List Site PRO Admin Access\"\n";
$filetext .= "AuthType Basic\n";
$filetext .= "AuthUserFile $htpasswd\n";
$filetext .= "<Limit GET>\n";
$filetext .= "require valid-user\n";
$filetext .= "</Limit>\n"; 

open (ACCESS, ">$htaccess");
print ACCESS "$filetext\n";
close (ACCESS);



print "Location: #\n\n";

}
else {
print "Content-type: text/html\n\n";
print <<EOF;
<html>
<head>
<meta http-equiv="Content-Language" content="en-us">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>List Site PRO - Main Admin</title>
</head>
<body link="#0000FF" vlink="#0000FF" alink="#0000FF">
<div align="center">
  <center>
  <table border="0" cellpadding="0" cellspacing="0" width="500">
    <tr>
      <td><p><font face="Arial Rounded MT Bold" size="7"><font color="#000080">List Site</font>
<i><font color="#800000">PRO</font></i></font></p>
</td>
    </tr>
  </table>
  </center>
</div>
<p><br>
</p>
<div align="center">
  <center>
  <table border="0" cellpadding="0" cellspacing="0" width="300">
    <tr>
      <td>
        <p><font face="Verdana" size="2">&nbsp;1. <a href="admin.cgi?step=1">Set Up Server</a></font></p>
        <p><font face="Verdana" size="2">&nbsp;2. <a href="admin.cgi?step=2">Configure Top Site Options</a></font></p>
        <p><font face="Verdana" size="2">&nbsp;3. <a href="admin.cgi?step=3">Configure Linking Options</a></font></p>
        <p><font face="Verdana" size="2">&nbsp;4. <a href="admin.cgi?step=4">Configure Tables and Colors</a></font></p>
        <p><font face="Verdana" size="2">&nbsp;5. <a href="admin.cgi?step=5">Create New Top Site</a></font></p>
        <p><font face="Verdana" size="2">&nbsp;6. <a href="admin.cgi?step=6">Create Password Files</a></font></p>

      </td>  
    </tr>
  </table>
  </center>
</div>
<p align="center"><font
                color="#C0C0C0" size="1" face="Arial">Copyright
                © 1999 List Site PRO, All Rights Reserved</font> </p>
<p align="center">&nbsp;</p>

</body>

</html>
EOF
exit;
}
sub clean_data {
if ($in{'lspro_site_name'} eq "") {
$in{'lspro_site_name'} = $lspro_site_name;
}
if ($in{'display_site_name'} eq "") {
$in{'display_site_name'} = $display_site_name;
}
if ($in{'lspro_site_name_font'} eq "") {
$in{'lspro_site_name_font'} = $lspro_site_name_font;
}
if ($in{'lspro_root_path'} eq "") {
$in{'lspro_root_path'} = $lspro_root_path;
}
if ($in{'lspro_file_name'} eq "") {
$in{'lspro_file_name'} = $lspro_file_name;
}
if ($in{'lspro_base_url'} eq "") {
$in{'lspro_base_url'} = $lspro_base_url;
}
if ($in{'lspro_cgi_url'} eq "") {
$in{'lspro_cgi_url'} = $lspro_cgi_url;
}
if ($in{'max_banner'} eq "") {
$in{'max_banner'} = $max_banner;
}
if ($in{'max_banner_height'} eq "") {
$in{'max_banner_height'} = $max_banner_height;
}
if ($in{'max_banner_width'} eq "") {
$in{'max_banner_width'} = $max_banner_width;
}
if ($in{'max_record'} eq "") {
$in{'max_record'} = $max_record;
}
if ($in{'min_record_to_list'} eq "") {
$in{'min_record_to_list'} = $min_record_to_list;
}
if ($in{'set_update'} eq "") {
$in{'set_update'} = $set_update;
}
if ($in{'set_reset'} eq "") {
$in{'set_reset'} = $set_reset;
}
if ($in{'lspro_background_image'} eq "") {
$in{'lspro_background_image'} = $lspro_background_image;
}
if ($in{'lspro_background_color'} eq "") {
$in{'lspro_background_color'} = $lspro_background_color;
}
if ($in{'lspro_text_color'} eq "") {
$in{'lspro_text_color'} = $lspro_text_color;
}
if ($in{'lspro_link_color'} eq "") {
$in{'lspro_link_color'} = $lspro_link_color;
}
if ($in{'lspro_visited_link_color'} eq "") {
$in{'lspro_visited_link_color'} = $lspro_visited_link_color;
}
if ($in{'lspro_active_link_color'} eq "") {
$in{'lspro_active_link_color'} = $lspro_active_link_color;
}
if ($in{'lspro_table_font'} eq "") {
$in{'lspro_table_font'} = $lspro_table_font;
}
if ($in{'lspro_table_border_size'} eq "") {
$in{'lspro_table_border_size'} = $lspro_table_border_size;
}
if ($in{'lspro_table_heading_color'} eq "") {
$in{'lspro_table_heading_color'} = $lspro_table_heading_color;
}
if ($in{'lspro_table_text_color'} eq "") {
$in{'lspro_table_text_color'} = $lspro_table_text_color;
}
if ($in{'lspro_cell_background_color'} eq "") {
$in{'lspro_cell_background_color'} = $lspro_cell_background_color;
}
if ($in{'lspro_cell_text_color'} eq "") {
$in{'lspro_cell_text_color'} = $lspro_cell_text_color;
}
if ($in{'image_filename'} eq "") {
$in{'image_filename'} = $image_filename;
}
if ($in{'image_url'} eq "") {
$in{'image_url'} = $image_url;
}
if ($in{'image_width'} eq "") {
$in{'image_width'} = $image_width;
}
if ($in{'image_height'} eq "") {
$in{'image_height'} = $image_height;
}
if ($in{'image_text'} eq "") {
$in{'image_text'} = $image_text;
}
if ($in{'mailprog'} eq "") {
$in{'mailprog'} = $mailprog;
}
if ($in{'lspro_email_address'} eq "") {
$in{'lspro_email_address'} = $lspro_email_address;
}
}
sub update_data {
if ($in{'lspro_site_name'} =~ /\@/) {
for ($in{'lspro_site_name'})
{
(@site_name) = split(/\@/);
$in{'lspro_site_name'} = join '\\@',@site_name;
}
}
if ($in{'text_link'} =~ /\@/) {
for ($in{'text_link'})
{
(@text_link) = split(/\@/);
$in{'text_link'} = join '\\@',@text_link;
}
}
my ($xuser,$yhost) = split '@', $in{'lspro_email_address'};
$newuser .= "\#WARNING - DO NOT HAND EDIT THIS FILE\n";
$newuser .= "\$lspro_site_name=\"$in{'lspro_site_name'}\";\n";
$newuser .= "\$display_site_name=\"$in{'display_site_name'}\";\n";
$newuser .= "\$lspro_site_name_font=\"$in{'lspro_site_name_font'}\";\n";
$newuser .= "\$lspro_root_path=\"$in{'lspro_root_path'}\";\n";
$newuser .= "\$lspro_file_name=\"$in{'lspro_file_name'}\";\n";
$newuser .= "\$lspro_base_url=\"$in{'lspro_base_url'}\";\n";
$newuser .= "\$lspro_cgi_url=\"$in{'lspro_cgi_url'}\";\n";
$newuser .= "\$max_banner=\"$in{'max_banner'}\";\n";
$newuser .= "\$max_banner_height=\"$in{'max_banner_height'}\";\n";
$newuser .= "\$max_banner_width=\"$in{'max_banner_width'}\";\n";
$newuser .= "\$max_record=\"$in{'max_record'}\";\n";
$newuser .= "\$min_record_to_list=\"$in{'min_record_to_list'}\";\n";
$newuser .= "\$set_update=\"$in{'set_update'}\";\n";
$newuser .= "\$set_reset=\"$in{'set_reset'}\";\n";
$newuser .= "\$lspro_background_image=\"$in{'lspro_background_image'}\";\n";
$newuser .= "\$lspro_background_color=\"$in{'lspro_background_color'}\";\n";
$newuser .= "\$lspro_text_color=\"$in{'lspro_text_color'}\";\n";
$newuser .= "\$lspro_link_color=\"$in{'lspro_link_color'}\";\n";
$newuser .= "\$lspro_visited_link_color=\"$in{'lspro_visited_link_color'}\";\n";
$newuser .= "\$lspro_active_link_color=\"$in{'lspro_active_link_color'}\";\n";
$newuser .= "\$lspro_table_font=\"$in{'lspro_table_font'}\";\n";
$newuser .= "\$lspro_table_border_size=\"$in{'lspro_table_border_size'}\";\n";
$newuser .= "\$lspro_table_heading_color=\"$in{'lspro_table_heading_color'}\";\n";
$newuser .= "\$lspro_table_text_color=\"$in{'lspro_table_text_color'}\";\n";
$newuser .= "\$lspro_cell_background_color=\"$in{'lspro_cell_background_color'}\";\n";
$newuser .= "\$lspro_cell_text_color=\"$in{'lspro_cell_text_color'}\";\n";
$newuser .= "\$image_filename=\"$in{'image_filename'}\";\n";
$newuser .= "\$image_url=\"$in{'image_url'}\";\n";
$newuser .= "\$image_width=\"$in{'image_width'}\";\n";
$newuser .= "\$image_height=\"$in{'image_height'}\";\n";
$newuser .= "\$image_text=\"$in{'image_text'}\";\n";
$newuser .= "\$mailprog=\"$in{'mailprog'}\";\n";
$newuser .= "\$lspro_email_address=\"$xuser\\\@$yhost\"\;\n";
$newuser .= "1\;";
open(NEWUSER,">admin.pl");
print NEWUSER $newuser;
close(NEWUSER);
}
