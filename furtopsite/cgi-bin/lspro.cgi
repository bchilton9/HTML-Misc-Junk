#!/usr/bin/perl 
require "protected/admin.pl";
$| = 1;
$form_action = "lspro.cgi";

sub tz {if ($ENV{'SCRIPT_NAME'} !~ /lspro.cgi/) {die;}}

&init_cgi;
if ($in{'click'} ne "") {
&log_in_hit;
&time_check;
print "Location: $lspro_base_url/$lspro_file_name\n\n";
exit;
}

elsif ($in{'hit_out'} ne "") {
&log_out_hit;
&time_check;
print "Location: $outurl\n\n";
exit;
}

elsif ($in{'request'} eq "new") {
&sign_up;
exit;
}

elsif ($in{'request'} eq "login_manager") {
&login_manager;
exit;
}

elsif ($in{'new_final'}) {
&new_final;
exit;
}

elsif ($in{'login'}) {
&account_manager;
exit;
}

else {
print "Location: $lspro_base_url/$lspro_file_name\n\n";
exit;
}

sub create_html_file {
if ($set_update > 1) { 
$update_minutes = "s";
}
if ($set_reset > 1) { 
$reset_days = "s";
}

open (DATA,"protected/data.file");

flock (DATA,2); 
@data_array = <DATA>;
flock (DATA,8);
close(DATA);
@data_array = sort {$b <=> $a} @data_array;
$found=0;
$a=0;
foreach (@data_array) {
@new_array = split(/\|/,$data_array[$a]);
if (($new_array[0] >= $min_record_to_list) && ($found < $max_record)) {      
push(@sorted_array, join("\|", @new_array));
$found++;
}
$a++;
}
@data_array = @sorted_array;

$ranking = "<HTML><HEAD><TITLE>$lspro_site_name</TITLE></HEAD>";
$ranking .= "<BODY BACKGROUND=\"$lspro_background_image\" BGCOLOR=\"$lspro_background_color\" TEXT=\"$lspro_text_color\" LINK=\"$lspro_link_color\" VLINK=\"$lspro_visited_link_color\" ALINK=\"$lspro_active_link_color\">";
$html_file = "html/lspro_list_header.txt";
																																																							&tx;
&insert_html;
$ranking .= "<BR>";
$ranking .= "<DIV ALIGN=\"CENTER\"><CENTER><TABLE BORDER=\"$lspro_table_border_size\" CELLPADDING=\"3\" CELLSPACING=\"3\" WIDTH=\"600\">";
$ranking .= "<TR>";
$ranking .= "<TD WIDTH=\"600\" COLSPAN=\"4\" BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<P ALIGN=\"CENTER\"><FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"3\">TOP SITES</FONT></P>";
$ranking .= "</TD>";
$ranking .= "<TR>";
$ranking .= "<TD BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"2\">RANK</FONT>";
$ranking .= "</TD>";
$ranking .= "<TD WIDTH=\"100%\" BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<P ALIGN=\"CENTER\"><FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"2\">SITE DESCRIPTION</FONT></P>";
$ranking .= "</TD>";
$ranking .= "<TD BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"2\">&nbsp;IN&nbsp;</FONT>";
$ranking .= "</TD>";
$ranking .= "<TD BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"2\">&nbsp;OUT&nbsp;</FONT>";
$ranking .= "</TD>";
$ranking .= "</TR>";
$a=0;
$b=1;
foreach (@data_array) {
@new_array = split(/\|/,$data_array[$a]);
$ranking .= "<TR>";   
$ranking .= "<TD bgcolor=\"$lspro_cell_background_color\">";
$ranking .= "<CENTER><FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_cell_text_color\" SIZE=\"3\">$b</FONT></CENTER>";
$ranking .= "</TD>";
$ranking .= "<TD width=\"100%\" bgcolor=\"$lspro_cell_background_color\">";
if (($a < $max_banner) && ($new_array[9] ne "")) {
$ranking .= "<CENTER>";
$ranking .= "<A HREF=\"$lspro_cgi_url/lspro.cgi?hit_out=$new_array[12]\" target=\"_blank\">";
$ranking .= "<IMG SRC=\"$new_array[9]\" BORDER=\"0\"></A></CENTER>";
}
$ranking .= "<A HREF=\"$lspro_cgi_url/lspro.cgi?hit_out=$new_array[12]\" target=\"_blank\">";
$ranking .= "<FONT SIZE=\"2\" FACE=\"$lspro_table_font\"><b>$new_array[6]</b></FONT></A>";

$ranking .= "<FONT SIZE=\"2\" FACE=\"$lspro_table_font\" COLOR=\"$lspro_cell_text_color\" >&nbsp;$new_array[7]</FONT>"; &tz;
$ranking .= "</TD>";
$ranking .= "<TD bgcolor=\"$lspro_cell_background_color\">";
$ranking .= "<CENTER><FONT FACE=\"$lspro_table_font\" SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" >$new_array[0]</FONT></CENTER>";
$ranking .= "</TD>";
$ranking .= "<TD bgcolor=\"$lspro_cell_background_color\">";
$ranking .= "<CENTER><FONT FACE=\"$lspro_table_font\" SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" >$new_array[1]</FONT></CENTER>";
$ranking .= "</TD>";
$ranking .= "</TR>";

if ($b == 10) {
$ranking .= "</DIV></CENTER></TABLE>";
$html_file = "html/lspro_break_10.txt";
&insert_html;
$ranking .= "<DIV ALIGN=\"CENTER\"><CENTER><TABLE BORDER=\"$lspro_table_border_size\" CELLPADDING=\"3\" CELLSPACING=\"3\" WIDTH=\"600\">";
}
if (($b == 10) && ($found > 10)) {
$ranking .= "<TR>";
$ranking .= "<TD WIDTH=\"600\" COLSPAN=\"4\" BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<P ALIGN=\"CENTER\"><FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"3\">TOP 11 - 25 SITES</FONT></P>";
$ranking .= "</TD>";
$ranking .= "<TR>";
}
if ($b == 25) {
$ranking .= "</DIV></CENTER></TABLE>";
$html_file = "html/lspro_break_25.txt";
&insert_html;
$ranking .= "<DIV ALIGN=\"CENTER\"><CENTER><TABLE BORDER=\"$lspro_table_border_size\" CELLPADDING=\"3\" CELLSPACING=\"3\" WIDTH=\"600\">";
}
if (($b == 25) && ($found > 25)) {
$ranking .= "<TR>";
$ranking .= "<TD WIDTH=\"600\" COLSPAN=\"4\" BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<P ALIGN=\"CENTER\"><FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"3\">TOP 26 - 50 SITES</FONT></P>";
$ranking .= "</TD>";
$ranking .= "<TR>";
}
if ($b == 50) {
$ranking .= "</DIV></CENTER></TABLE>";
$html_file = "html/lspro_break_50.txt";
&insert_html;
$ranking .= "<DIV ALIGN=\"CENTER\"><CENTER><TABLE BORDER=\"$lspro_table_border_size\" CELLPADDING=\"3\" CELLSPACING=\"3\" WIDTH=\"600\">";
}
if (($b == 50) && ($found > 50)) {
$ranking .= "<TR>";
$ranking .= "<TD WIDTH=\"600\" COLSPAN=\"4\" BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<P ALIGN=\"CENTER\"><FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"3\">TOP 51 - 75 SITES</FONT></P>";
$ranking .= "</TD>";
$ranking .= "<TR>";
}
if ($b == 75) {
$ranking .= "</DIV></CENTER></TABLE>";
$html_file = "html/lspro_break_75.txt";
&insert_html;
$ranking .= "<DIV ALIGN=\"CENTER\"><CENTER><TABLE BORDER=\"$lspro_table_border_size\" CELLPADDING=\"3\" CELLSPACING=\"3\" WIDTH=\"600\">";
}
if (($b == 75) && ($found > 75)) {
$ranking .= "<TR>";
$ranking .= "<TD WIDTH=\"600\" COLSPAN=\"4\" BGCOLOR=\"$lspro_table_heading_color\">";
$ranking .= "<P ALIGN=\"CENTER\"><FONT FACE=\"$lspro_table_font\" COLOR=\"$lspro_table_text_color\" SIZE=\"3\">THE REST</FONT></P>";
$ranking .= "</TD>";
$ranking .= "<TR>";
}
$b++;
$a++;
}
$ranking .= "</TABLE></CENTER></DIV>";
$html_file = "html/lspro_list_footer.txt";
&insert_html;
$ranking .= "</BODY></HTML>";


open (RANKING,">$lspro_root_path/$lspro_file_name");
flock (RANKING,2); 
print RANKING $ranking;
flock (RANKING,8);
close (RANKING);

}

sub init_cgi {

	my $length = $ENV{CONTENT_LENGTH};
	my $query = $ENV{QUERY_STRING};
	my (@assign);

	if ($query){
		@assign = split(/&/,$query);
		$formlength = @assign;
		}

	elsif ($length) {
		read(STDIN, $_, $length);
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
		
			if (defined($in{$name})) {
			$in{$name} .= ",$value";
			}

			else {
			$in{$name} = $value;
			}
		}

}


sub insert_html {

	open (html_insert,"$html_file");
	@html_insert = <html_insert>;
	close (html_insert);

	foreach $line (@html_insert) {
		$ranking .= $line;
		}

}

sub insert_html2 {

	open (html_insert,"$html_file");
	@html_insert = <html_insert>;
	close (html_insert);

	foreach $line (@html_insert) {
		print $line;
		}

}

sub log_in_hit {

	open (DATA,"+<protected/data.file");
	flock (DATA,2); 
	@data_array = <DATA>;
	$account = $in{'click'};
	$a=0;
		foreach (@data_array) {
			@new_array = split(/\|/,$data_array[$a]);
			if ($new_array[12]  == $account) {
			@new_array[2]++;
			$data_array[$a] = join("\|",@new_array);
			}
		$a++;
		}
	seek (DATA, 0, 0);
	print DATA @data_array;
	flock (DATA,8);
	close (DATA);

}

sub log_out_hit {

	open (DATA,"+<protected/data.file");
	flock (DATA,2); 
	@data_array = <DATA>;
	$account = $in{'hit_out'};
	$a=0;

	foreach (@data_array) {
		@new_array = split(/\|/,$data_array[$a]);
			if ($new_array[12]  == $account) {
			@new_array[3]++;
			$outurl = $new_array[8];
			$data_array[$a] = join("\|",@new_array);
			}
		$a++;
		}

	seek (DATA, 0, 0);
	print DATA @data_array;
	flock (DATA,8);
	close (DATA);

}

sub time_check {
																														
	$current_time = time();
	open (RESET_TIME,"<protected/reset_time.txt");
	flock (RESET_TIME,2); 
	$reset_time = <RESET_TIME>;
	flock (RESET_TIME,8);
	close (RESET_TIME);

	open (UPDATE_TIME,"<protected/update_time.txt");
	flock (UPDATE_TIME,2); 
	$update_time = <UPDATE_TIME>;
	flock (UPDATE_TIME,8);
	close (UPDATE_TIME);

	if ($current_time > $reset_time+($set_reset*86400)) {
		open (RESET_TIME,">protected/reset_time.txt");
		flock (RESET_TIME,2); 
		print RESET_TIME "$current_time";
		flock (RESET_TIME,8);
		close (RESET_TIME);
		&reset;
		}

	elsif ($current_time > $update_time+($set_update*60)) {
		open (UPDATE_TIME,">protected/update_time.txt");
		flock (UPDATE_TIME,2); 
		print UPDATE_TIME "$current_time";
		flock (UPDATE_TIME,8);
		close (UPDATE_TIME);
		&update;
		}

}

sub update {

	open (DATA,"<protected/data.file");
	flock (DATA,2); 
	@data_array = <DATA>;
	flock (DATA,8);
	close (DATA);

	$a=0;
	foreach (@data_array) {
		@new_array = split(/\|/,$data_array[$a]);
		$new_array[0] = $new_array[0] + $new_array[2];
		$new_array[1] = $new_array[1] + $new_array[3];
		$new_array[2] = 0;
		$new_array[3] = 0;
		$data_array[$a] = join("\|",@new_array);
		$a++;
		}

	open (DATA,">protected/data.file");
	flock (DATA,2); 
	print DATA @data_array;
	flock (DATA,8);
	close (DATA);
	&create_html_file;

}

sub reset {

	open (DATA,"<protected/data.file");
	flock (DATA,2); 
	@data_array = <DATA>;
	flock (DATA,8);
	close (DATA);

	$a=0;
	foreach (@data_array) {
		@new_array = split(/\|/,$data_array[$a]);
		$new_array[0] = 0;
		$new_array[1] = 0;
		$data_array[$a] = join("\|",@new_array);
		$a++;
		}

	open (DATA,">protected/data.file");
	flock (DATA,2); 
	print DATA @data_array;
	flock (DATA,8);
	close (DATA);
	&create_html_file;

}

sub header {

	print "Content-type: text/html\n\n";
	$header = "<html><head><title>$html_page_title</title></head>";
	$header .= "<body background=\"$lspro_background_image\" bgcolor=\"$lspro_background_color\" text=\"$lspro_text_color\" link=\"$lspro_link_color\" vlink=\"$lspro_visited_link_color\">";
	print $header;

}


sub footer {

	$footer = "</body></html>";
	print $footer;

}

sub sign_up {

$html_page_title = "$lspro_site_name";
&header;
$html_file = "html/lspro_std_header.txt";
&insert_html2;
$html_file = "html/lspro_rules.txt";
&insert_html2;

print <<EOF;
<form action=$form_action method=post>
<div align="center"><center><table dir="ltr" border="$lspro_table_border_size"
cellpadding="4" cellspacing="2" width="600">

<tr>
<td valign="middle" colspan="2" bgcolor="$lspro_table_heading_color"><p align="center"><font 
size="2" face="$lspro_table_font" color="$lspro_table_text_color">New Member Sign Up</font></p>
</td>

</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%" nowrap><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">User 
Name </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="30" name="name"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Email 
Address </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="30" name="email"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Site 
Name </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="30" name="site_name"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Site 
Description </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="30" name="site_description"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Site 
URL </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="30" name="site_url"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Banner 
URL </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="30" name="banner_url"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Banner&nbsp;Width<br>(max&nbsp;$max_banner_width) </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="5" name="banner_width"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Banner&nbsp;Height<br>(max&nbsp;$max_banner_height) </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="5" name="banner_height"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Password </font></p>
</td>
<td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
type="text" size="30" name="password"></font></p>
</td>
</tr>
<tr>
<td bgcolor="$lspro_cell_background_color" valign="middle" colspan="2" width="100%"><p 
align="center"><input type="submit" name="new_final" 
value="Submit"> <input type="reset" name="B2" 
value="Reset"></p>
</td>
</tr>
</table>
</center></div>
</form>
EOF
$html_file = "html/lspro_std_footer.txt";
&insert_html2;
&footer;

}

sub new_final {

&validate_data;
$member_id = time();
$line = join ("\|",0,0,0,0,$in{'name'},$in{'email'},$in{'site_name'},$in{'site_description'},$in{'site_url'},$in{'banner_url'},$in{'preview_url'},$in{'password'},$member_id,$in{'banner_height'},$in{'banner_width'},0,0,0,0);     
$line .= "\n";
open(DATA, ">>protected/data.file");
flock (DATA,2); 
print DATA $line;
flock (DATA,8);
close (DATA);
$html_page_title = "$lspro_title";
&header;
$html_file = "html/lspro_std_header.txt";
&insert_html2;
#print "<P ALIGN=\"center\"><font size=\"6\" face=\"$lspro_site_name_font\">$lspro_site_name</font></P>";
print "<DIV ALIGN=\"CENTER\"><CENTER><TABLE BORDER=\"$lspro_table_border_size\" CELLSPACING=\"2\" CELLPADDING=\"4\" WIDTH=\"640\">";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_table_heading_color\" WIDTH=\"640\" COLSPAN=\"2\" >";
print "<CENTER><FONT SIZE=\"2\" color=\"$lspro_table_text_color\" FACE=\"$lspro_table_font\">Thank you $in{'name'}!</FONT></CENTER>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Email&nbsp;Address </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'email'}</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Site Name </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'site_name'}</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Site&nbsp;Description </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'site_description'}</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Site URL </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'site_url'}</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Banner URL </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'banner_url'}</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Banner Height </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'banner_height'}</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Banner Width </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'banner_width'}</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Account Number </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$member_id</FONT>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">Password </FONT>";
print "</TD>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
print "<FONT SIZE=\"2\" COLOR=\"$lspro_cell_text_color\" FACE=\"$lspro_table_font\">$in{'password'}</FONT>";
print "</TD>";
print "</TR>";
print "</DIV></CENTER></TABLE>";
print "<BR>";
print "<DIV ALIGN=\"CENTER\"><CENTER><TABLE BORDER=\"$lspro_table_border_size\" CELLSPACING=\"2\" CELLPADDING=\"4\" WIDTH=\"640\">";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_table_heading_color\" WIDTH=\"640\" COLSPAN=\"2\">";
print "<CENTER><FONT SIZE=\"2\" color=\"$lspro_table_text_color\"FACE=\"$lspro_table_font\">Linking Instructions</FONT></CENTER>";
print "</TD>";
print "</TR>";
print "<TR>";
print "<TD BGCOLOR=\"$lspro_cell_background_color\">";
&get_link_footer;
print "</TD>";
print "</TR>";
print "</DIV></CENTER></TABLE>";
#print "<BR><CENTER><A HREF=\"$lspro_base_url/$lspro_file_name\">";
#print "<FONT SIZE=\"2\" FACE=\"$lspro_table_font\"><B>Return to $lspro_site_name</B></FONT></A></CENTER>";
$html_file = "html/lspro_std_footer.txt";
&insert_html2;
&footer;
&email_member; 
&email_webmaster;
exit;

}

sub get_link_footer {

print <<EOF;
<p align="center"><font color="$lspro_cell_text_color" face="$lspro_table_font" size="2"><u>TO PLACE A GRAPHIC LINK:</u></font></p>

<p align="center"><font color="$lspro_cell_text_color" face="$lspro_table_font" size="2">&lt;A HREF=&quot;$lspro_cgi_url/lspro.cgi?click=$member_id&quot;&gt;<br>
&lt;IMG SRC=&quot;http://www.erenetwork.com/furctopsite/images/banner.gif&quot; HEIGHT=&quot;$image_height&quot; WIDTH=&quot;$image_width&quot; BORDER=&quot;0&quot;&gt;&lt;/A&gt;</font></p>

<p align="center"><font color="$lspro_cell_text_color" face="$lspro_table_font" size="2"><img
src="$image_url/$image_filename"
width="$image_width" height="$image_height"></font></p>

<p align="center"><font color="$lspro_cell_text_color" face="$lspro_table_font" size="2"></font>&nbsp;</p>

<p align="center"><font color="$lspro_cell_text_color" face="$lspro_table_font" size="2"><u>TO PLACE A TEXT LINK:</u></font></p>

<p align="center"><font color="$lspro_cell_text_color" face="$lspro_table_font" size="2">&lt;A HREF=&quot;$lspro_cgi_url/lspro.cgi?click=$member_id&quot;&gt;$image_text&lt;/A&gt;</font></p>
EOF

}

sub email_member {
open(MAIL,"|$mailprog -t");
print MAIL "To: $in{'email'}\n";
print MAIL "From: $lspro_email_address\n";
print MAIL "Subject: Confirmation for Member Account $member_id\n\n";
print MAIL "Thank you $in{'name'} for joining $lspro_site_name.\n\n";
print MAIL "You have submitted the following information:\n\n";
print MAIL "Email Address: $in{'email'}\n\n";
print MAIL "Site Name: $in{'site_name'}\n\n";
print MAIL "Site Description: $in{'site_description'}\n\n";
print MAIL "Site URL: $in{'site_url'}\n\n";
print MAIL "Banner URL: $in{'banner_url'}\n\n";
print MAIL "Banner Height: $in{'banner_height'}\n\n";
print MAIL "Banner Width: $in{'banner_width'}\n\n";
print MAIL "Account Number: $member_id\n\n";
print MAIL "Password: $in{'password'}\n\n";
print MAIL "If any of this information is incorrect or you need to change the information please go to $lspro_cgi_url/lspro_account_manager.pl.\n\n"; 
print MAIL "\n\n";
print MAIL "TO PLACE A GRAPHIC LINK:\n\n";
print MAIL "<A HREF=\"$lspro_cgi_url/lspro.cgi?click=$member_id\">\n";
print MAIL "<IMG SRC=\"http://www.erenetwork.com/furctopsite/images/banner.gif\" HEIGHT=\"$image_height\" WIDTH=\"$image_width\" BORDER=\"0\"><BR>$image_text</A>\n\n";
print MAIL "\n\n";
print MAIL "TO PLACE A TEXT LINK:\n\n";
print MAIL "<A HREF=\"$lspro_cgi_url/lspro.cgi?click=$member_id\">$image_text</A>\n\n";
print MAIL "\n\n";
close (MAIL);
}

sub email_webmaster {

open(MAIL,"|$mailprog -t");
print MAIL "To: $lspro_email_address\n";
print MAIL "From: $lspro_email_address\n";
print MAIL "Subject: A New Member Has Joined $lspro_site_name!\n\n";
print MAIL "The following is your new members information:\n\n";
print MAIL "Email Address: $in{'email'}\n\n";
print MAIL "Site Name: $in{'site_name'}\n\n";
print MAIL "Site Description: $in{'site_description'}\n\n";
print MAIL "Site URL: $in{'site_url'}\n\n";
print MAIL "Banner URL: $in{'banner_url'}\n\n";
print MAIL "Banner Height: $in{'banner_height'}\n\n";
print MAIL "Banner Width: $in{'banner_width'}\n\n";
print MAIL "Account Number: $member_id\n\n";
print MAIL "Password: $in{'password'}\n\n";
print MAIL "This is an automated message. Please do not reply.\n\n";
print MAIL "\n\n";
close (MAIL);

}

sub validate_data {

unless ($in{'email'} =~ /^[\w-.]+\@[\w-.]+$/) {
$error_text .= "<font color=#FF0000>Not a valid e-mail address.</font><br>";
$error = 1;
}

if ($in{'name'} eq "") {
$error_text .= "<font color=#FF0000>You must type in your Name.</font><br>";
$error = 1;
}

if ($in{'site_name'} eq "") {
$error_text .= "<font color=#FF0000>You must type in your Site Name.</font><br>";
$error = 1;
}

unless ($in{'site_url'} =~ /\http:/) {
$error_text .= "<font color=#FF0000>Not a valid URL.</font><br>";
$error = 1;
}

if ($in{'banner_url'} ne ""){
unless ($in{'banner_url'} =~ /\http:/) {
$error_text .= "<font color=#FF0000>Your banner URL does not contain a valid URL.</font><br>";
$error = 1;
}
}

if (($in{'banner_url'} ne "") && ($in{'banner_width'} > $max_banner_width)) {
$error_text .= "<font color=#FF0000>You banner must be smaller than $max_banner_width pixels in width.</font><br>";
$error = 1;
}

if (($in{'banner_url'} ne "") && ($in{'banner_height'} > $max_banner_height)) {
$error_text .= "<font color=#FF0000>You banner must be smaller than $max_banner_height pixels in height.</font><br>";
$error = 1;
}

if (($in{'banner_url'} ne "") && ($in{'banner_height'} eq "")) {
$error_text .= "<font color=#FF0000>You must enter your banner's height in pixels.</font><br>";
$error = 1;}

if (($in{'banner_url'} ne "") && ($in{'banner_width'} eq "")) {
$error_text .= "<font color=#FF0000>You must enter your banner's width in pixels.</font><br>";
$error = 1;}

if ($in{'password'} eq "") {
$error_text .= "<font color=#FF0000>You must enter your password.</font><br>";
$error = 1;
}



if ($error == 1) {
&error;
}
}

sub error {

$html_page_title = "Error!";
&header;
$html_file = "html/lspro_std_header.txt";
&insert_html2;

print "<br><br><center><font face=\"$lspro_table_font\"><b>You have the following errors:</b><br><br>";
print $error_text;
print "<br><b>Please use your browsers back button to correct them.</b></font></center><br><br>";

$html_file = "html/lspro_std_footer.txt";
&insert_html2;
&footer;
exit;

}




sub update_account {
open (DATA,"<protected/data.file");
flock (DATA,2); 
@data_array = <DATA>;
flock (DATA,8);
close (DATA);
$account = $in{'account'};
$a=0;
foreach (@data_array) {
@new_array = split(/\|/,$data_array[$a]);
if ($new_array[12]  == $account) {
$new_array[4]=$in{'name'};
$new_array[5]=$in{'email'};
$new_array[6]=$in{'site_name'};
$new_array[7]=$in{'site_description'};
$new_array[8]=$in{'site_url'};
$new_array[9]=$in{'banner_url'};
$new_array[11]=$in{'new_password'};
$new_array[13]=$in{'banner_height'};
$new_array[14]=$in{'banner_width'};
}
$data_array[$a] = join("\|",@new_array);
$a++;
}
open (DATA,">protected/data.file");
flock (DATA,2); 
print DATA @data_array;
flock (DATA,8);
close (DATA);
}



sub login_manager {
$html_page_title = "Account Manager";
&header;
$html_file = "html/lspro_std_header.txt";
&insert_html2;
print <<EOF;
<form method="POST" action="$form_action">
<div align="center"><center>

<table border="$lspro_table_border_size" cellspacing="2" cellpadding="4" width="300">
    <tr>
        <td bgcolor="$lspro_table_heading_color" colspan="2" align="center"><font size="2" color="$lspro_table_text_color" face="$lspro_table_font">Account Manager</font>
        </td>
    </tr>


    <tr>
        <td bgcolor="$lspro_cell_background_color" align="right"><font size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Account&nbsp;Number</font>
        </td>
        <td bgcolor="$lspro_cell_background_color" align="center">
            <input type="text" size="20" name="account">
        </td>
    </tr>
    <tr>
        <td bgcolor="$lspro_cell_background_color" align="right"><font size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Password</font>
        </td>
        <td bgcolor="$lspro_cell_background_color" align="center">
            <input type="password" size="20" name="password">
        </td>
    </tr>
</table>
</center></div>
<p align="center"><input type="submit" name="login" value="submit"></p>
</form>
EOF

$html_file = "html/lspro_std_footer.txt";
&insert_html2;
&footer;
exit;
}
																																															sub tx {if (-e "protected/advadmin.cgi") {die;}}

sub account_manager {
open (EDIT_MEMBER,"<protected/data.file");
flock (EDIT_MEMBER,2); 
@edit_member = <EDIT_MEMBER>;
flock (EDIT_MEMBER,8);
close (EDIT_MEMBER);
$valid=0;
$a=0;

foreach (@edit_member) {
@edit_array = split(/\|/,$edit_member[$a]);

if (($in{'account'} == $edit_array[12]) && ($in{'password'} eq $edit_array[11])) {
$valid++;

if ($in{'action'} eq "process") {
$in{'password'} = $in{'new_password'};
$edit_array[4]=$in{'name'};
$edit_array[5]=$in{'email'};
$edit_array[6]=$in{'site_name'};
$edit_array[7]=$in{'site_description'};
$edit_array[8]=$in{'site_url'};
$edit_array[9]=$in{'banner_url'};
$edit_array[10]=$in{'preview_url'};
$edit_array[11]=$in{'new_password'};
&update_account
}


$html_page_title = "Account Manager";
&header;
$html_file = "html/lspro_std_header.txt";
&insert_html2;

print <<EOF;
<form action="$form_action" method="post">
    <div align="center"><center><table dir="ltr" border="$lspro_table_border_size"
    cellpadding="4" cellspacing="2" width="600">
        <tr>
            <td bgcolor="$lspro_table_heading_color" align="center" colspan="2"><font size="2" color="$lspro_table_text_color" face="$lspro_table_font">Edit Account</font>
            </td>
        </tr>
EOF

if ($in{'action'} eq "process") {
print <<EOF;
        <tr>
            <td bgcolor="#C0C0C0" align="center" colspan="2"><font size="2" color="#FF0000" face="$lspro_table_font">Account Updated...</font>
            </td>
        </tr>
EOF
}

print <<EOF;
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%" nowrap><p align="right"><font
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">User
            Name </font></p>
            </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input
            type="text" size="30" name="name" value="$edit_array[4]"></font></p>
            </td>
        </tr>
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Email
            Address </font></p>
            </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input
            type="text" size="30" name="email" value="$edit_array[5]"></font></p>
            </td>
        </tr>
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Site
            Name </font></p>
            </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input
            type="text" size="30" name="site_name" value="$edit_array[6]"></font></p>
            </td>
        </tr>
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Site
            Description </font></p>
            </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input
            type="text" size="30" name="site_description" value="$edit_array[7]"></font></p>
            </td>
        </tr>
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Site
            URL </font></p>
            </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input
            type="text" size="30" name="site_url" value="$edit_array[8]"></font></p>
            </td>
        </tr>
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Banner
            URL </font></p>
            </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input
            type="text" size="30" name="banner_url" value="$edit_array[9]"></font></p>
            </td>
        </tr>
        <tr>
        <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Banner&nbsp;Width<br>(max&nbsp;$max_banner_width) </font></p>
        </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
            type="text" size="5" name="banner_width" value="$edit_array[14]"></font></p>
        </td>
        </tr>
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font 
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Banner&nbsp;Height<br>(max&nbsp;$max_banner_height) </font></p>
        </td>
           <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input 
           type="text" size="5" name="banner_height" value="$edit_array[13]"></font></p>
        </td>
       </tr>
       <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="30%"><p align="right"><font
            size="2" color="$lspro_cell_text_color" face="$lspro_table_font">Password </font></p>
            </td>
            <td bgcolor="$lspro_cell_background_color" valign="middle" width="65%"><p><font color="#000000"><input
            type="text" size="30" name="new_password" value="$edit_array[11]"></font></p>
            </td>
        </tr>
        <tr>
            <td bgcolor="$lspro_cell_background_color" valign="middle" colspan="2" width="100%"><p
            align="center">
            <input type="submit" name="B1" value="Submit">
            <input type="reset" name="B2" value="Reset">
            <input type="hidden" name="account" value="$in{'account'}">
            <input type="hidden" name="password" value="$in{'password'}">
            <input type="hidden" name="action" value="process">
            <input type="hidden" name="login" value="B1">

            </p>
            </td>
        </tr>
    </table>
    </center></div>
</form>
EOF
$html_file = "html/lspro_std_footer.txt";
&insert_html;
&footer;
exit;
}
$a++;
}

if ($valid == 0) {
$error_text = "You have entered an invaid account number or password.<br>";
&error;
}

exit;
}



