#!/usr/bin/perl
use CGI::Carp qw(fatalsToBrowser);

# Copyright M. Carter Brown --> WebAPP

print "Content-type: text/html\n\n";

$scriptname = "WebAPP Palm Compatible Site";
# v0.9.9 - Requin   
$slogan = "News on the go!";

require "./config.pl";
require "$sourcedir/subs.pl";
&getcgi();

if ($input{'action'} eq "palm") {
&palm;
}

if ($input{'action'} eq "palm2") {
&palm2;
}

&palm();

############
sub getcgi {
############
read(STDIN, $input, $ENV{'CONTENT_LENGTH'});
	@pairs = split(/&/, $input);
	foreach $pair(@pairs) {

	        ($name, $value) = split(/=/, $pair);
	        $name =~ tr/+/ /;
	        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $value =~ tr/+/ /;
	        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $input{$name} = $value;
	}
	@vars = split(/&/, $ENV{QUERY_STRING});
	foreach $var(@vars) {
	        ($v,$i) = split(/=/, $var);
	        $v =~ tr/+/ /;
	        $v =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $i =~ tr/+/ /;
	        $i =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	        $i =~ s/<!--(.|\n)*-->//g;
	        $info{$v} = $i;
	}

	
}

##################
sub palm {
##################

require "./config.pl";

print qq~

<html>
<title>$pagetitle</title>
<head>
<h3>
<font color="#000070">$pagetitle</font></h3>
</head>
<p>
$slogan</p>
<body>
<b>News:</b><br><br>
~;

undef @catnames;
	undef @catlinks;

	open(FILE, "$topicsdir/cats.dat") || error("$err{'001'} $topicsdir/cats.dat");
	lock(FILE);
	chomp(@cats = <FILE>);
	
	close(FILE);

	foreach (@cats) {
		@item = split(/\|/, $_);
		push(@catnames, $item[0]);
		push(@catlinks, $item[1]);
	}

      if ($info{'id'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { &palmerror(); }


	if ($info{'id'} eq "") {
		
		
		

		%data = ();

		foreach $curcat (@catlinks) {
			if (-e("$topicsdir/$curcat.cat")) {
				foreach (@cats) {
					@item = split(/\|/, $_);
					if ($curcat eq "$item[1]") { $curcatname = "$item[0]"; }
				}

				open(FILE, "$topicsdir/$curcat.cat");
				lock(FILE);
				chomp(@articles = <FILE>);
				
				close(FILE);

				for ($a = 0; $a < @articles && $a <= $maxnews; $a++) {
					($id, $subject, $nick, $poster, $email, $postdate, $comments) = split(/\|/, $articles[$a]);

					if ($comments == 1) { $commentscnt = "$comments $msg{'040'}"; }
					else { $commentscnt = "$comments $msg{'041'}"; }

					open (FILE, "$topicsdir/articles/$id.txt");
					lock(FILE);
					chomp($text = <FILE>);
					
					close(FILE);

					@text = split(/\|/, $text);
					$message = showhtml("$text[5]");


				$post = qq~<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><a href="./palm.cgi?action=palm2&amp;id=$id">$subject</a></td>
</tr>

~;
					if (length($message) > 1) {
						$tmpmessage = substr($message, 0, 0);
						$tmpmessage =~ s/(.*)\s.*/$1/;
						$post = qq~$post


</table>
~;
					}
					else {
						$post = qq~$post<br>
$message
</td>
</tr>
</table>
~;
					}
					($chkdate, $chktime) = split(/ - /, $postdate);
					($chkmonth, $chkday, $chkyear) = split(/\//, $chkdate);
					($chkhour, $chkmin, $chksec) = split (/:/, $chktime);
					$chkyear = (2000+$chkyear);
					
					$sortedentry = "$chkyear$chkmonth$chkday$chkhour$chkmin$chksec"; 
					$data{$sortedentry} = $post;
				}
			}
		}
		@num = sort {$b <=> $a } keys %data;
		$j = 0;
		while ($j < $maxnews) {
			print "$data{$num[$j]}";
			$j++;
		}
		&foot();
		exit;
	}
	else {
            if ($info{'id'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { &palmerror(); }

		if ($info{'id'} !~ /^[0-9]+$/) { error("$err{'006'}" ); }

		foreach $curcat (@catlinks) {
			if (-e("$topicsdir/$curcat.cat")) {

				open(FILE, "$topicsdir/$curcat.cat");
				lock(FILE);
				chomp(@articles = <FILE>);
				
				close(FILE);

				for ($a = 0; $a < @articles; $a++) {
					($id, $dummy, $dummy, $dummy, $dummy, $dummy, $comments) = split(/\|/, $articles[$a]);
					if ($info{'id'} eq $id) {
						foreach (@cats) {
							@item = split(/\|/, $_);
							if ($curcat eq "$item[1]") { $curcatname = "$item[0]"; }
							if ($curcat eq "$item[1]") { $curcatlink = "$item[1]"; }
						}
						if ($comments == 1) { $commentscnt = "$comments $msg{'040'}"; }
						else { $commentscnt = "$comments $msg{'041'}"; }
					}
				}
			}
		}
            if ($info{'id'} =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) { &palmerror(); }

		open(FILE, "<$topicsdir/articles/$info{'id'}.txt") || error("$err{'001'} $topicsdir/articles/$info{'id'}.txt");
		lock(FILE);
		chomp(@datas = <FILE>);
		
		close(FILE);

		

		foreach $line (@datas) { $numshown++; }

		for ($a = 0; $a < 1; $a++) {
			@item = split (/\|/, $datas[$a]);

			$message = showhtml("$item[5]");

			print qq~<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td>$item[0]</td>
</tr>
<tr>
<td>$curcatname: $item[4] Posted By: <a href="mailto:$item[3]">$item[1]</a></td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td>
$message</td>
</tr>
<tr>
<td><br>&nbsp;[End News] | [<a href="./palm.cgi?action=palm">Return Home</a>]<br></td>
</tr>
</table>~;
&foot();

		}
		if ($numshown > 1) {
			print qq~<p align="center" class="cat">$msg{'158'}</p>
$msg{'159'}
~;
			for ($a = 1; $a < @datas; $a++) {
				@item = split (/\|/, $datas[$a]);

				$message = showhtml("$item[5]");

				if (@item == 0) { }
				else {
					print qq~<hr noshade="noshade" size="1">
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td class="texttitle">$item[0]</td>
</tr>
<tr>
<td>$item[4] Posted By:<a href="mailto:$item[3]">$item[1]</a></td>
</tr>
<tr>
<td>&nbsp;</td>
</tr>
<tr>
<td valign="top">$message</td>
</tr>
<tr>
<td>&nbsp;[End News] | [<a href="./palm.cgi?action=palm">Return Home</a>]<br></td>
</tr>
</table>~;
&foot();

				}
			}
		}
		
		
		
		exit;
	}

# code here




print qq~
<br>

~;
	
	open(FILE, "./config.pl") || error("Could Not Find: ./config.pl");
	lock(FILE);
	chomp(@config = <FILE>);
	close(FILE);

print qq~	
	
</form>
</body>
</html>
~;
	
	exit;
}

##########
sub lock {
##########
	local($file) = @_;
	if ($use_flock) { flock($file, $LOCK_EX); }
}

############
sub unlock {
############
	local($file) = @_;
	if ($use_flock) { flock($file, $LOCK_UN); }
}

############
sub palm2 {
############

require "./config.pl";

print qq~<html><title>$pagename</title>
</head>
<h3>$pagename</h3></head>
<body>
<p>
~;
open (FILE, "$topicsdir/articles/$id.txt");
					lock(FILE);
					chomp($text = <FILE>);
					
					close(FILE);

					@text = split(/\|/, $text);
					$message = showhtml("$text[5]");


				print qq~<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td>$subject</td>
</tr>
<tr>
<td>$curcatname: $postdate Posted by:$nick</td>
</tr>
<tr>
<td>&nbsp;[End News] | [<a href="./palm.cgi?action=palm">Return Home</a>]<br></td>
</tr>
</table>~;
&foot();

}


############
sub foot {
############
print qq~<br>
-----------------------<br>
All comments and posts are owned by the poster<br>
</body>
</html>~;

exit;
}

###############
sub palmerror {
###############

print "Content-type: text/html\n\n";

print qq~
<html>
<p>
<b>What are you doing Stan?</b><br>
</html>
~;

exit;
}



1; # return true

