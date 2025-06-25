###############
sub print_top {
###############
	require "$scriptdir/config.pl";
	require "$sourcedir/plugins.pl";
	require "$themesdir/standard/theme.pl";
	require "$scriptdir/user-lib/themes/theme.pl"; getvars();
	require "$themesdir/standard/header.pl";
}


################
sub print_main {
################
		if ($username ne "$anonuser") {

		open(FILE, "$memberdir/$username.pref") || error("$err{'010'}");
		file_lock(FILE);
		chomp(@preferences = <FILE>);
		unfile_lock(FILE);
		close(FILE);

		if ($preferences[3] == 1 || $preferences[3] eq "" ) {

	open(FILE, "$datadir/welcomemsg.txt");
	file_lock(FILE);
	chomp(@lines = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	$welcometitle = showhtml("$lines[0]");
	$welcomebody = showhtml("$lines[1]");

	$welcome = qq~<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><p class="texttitle">$welcometitle</p>
$welcomebody<br>
</td>
</tr>
</table>
~;
	}
	}

if ($username eq "$anonuser") {
open(FILE, "$datadir/welcomemsg2.txt");## Modified for bogmike's welcome message hack, add the '2' after welcomemsg
	file_lock(FILE);
	chomp(@lines = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	$welcometitle = showhtml("$lines[0]");
	$welcomebody = showhtml("$lines[1]");


	$welcome = qq~<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td><p class="texttitle">$welcometitle</p>
$welcomebody<br>
</td>
</tr>
</table>
~;
}

	require "$sourcedir/topics.pl";
	viewnews();

	exit;
}

############
sub doubbc {
############

	$message =~ s~\[font=(.+?)\]~<font face="$1">~isg;
     	$message =~ s~\[\/font\]~</font>~isg;

      	$message =~ s~\[size=(.+?)\]~<font size="$1">~isg;
    	$message =~ s~\[\/size\]~</font>~isg; 

	$message =~ s~\[\[~\{\{~g;
	$message =~ s~\]\]~\}\}~g;
	$message =~ s~\n\[~\[~g;
	$message =~ s~\]\n~\]~g;

	$message =~ s~\<br\>~ <br>~g;
	$message =~ s~\<pipe\>~\|~g;
	$message =~ s~\[hr\]\n~<hr size="1">~g;
	$message =~ s~\[hr\]~<hr size="1">~g;

	$message =~ s~\[b\]~<b>~isg;
	$message =~ s~\[\/b\]~</b>~isg;

	$message =~ s~\[i\]~<i>~isg;
	$message =~ s~\[\/i\]~</i>~isg;

	$message =~ s~\[u\]~<u>~isg;
	$message =~ s~\[\/u\]~</u>~isg;
	
	if ($imageicons eq "1") {
		$message =~ s~\[img\](.+?)\[\/img\]~<a href="$1" target="_blank"><img src="$1" width="150" height="150" alt="" border="0"></a>~isg;
		}
	if ($imageicons ne "1") {
		$message =~ s~\[img\](.+?)\[\/img\]~<img src="$1" alt="" border="0">~isg;
		}
	
	$message =~ s~\[color=(\S+?)\]~<font color="$1">~isg;
	$message =~ s~\[\/color\]~</font>~isg;
	
	$message =~ s~\[quote\]<br>(.+?)<br>\[\/quote\]~<blockquote><hr align=left width=40%>$1<hr align=left width=40%></blockquote>~isg;
	$message =~ s~\[quote\](.+?)\[\/quote\]~<blockquote><hr align=left width=40%><b>$1</b><hr align=left width=40%></blockquote>~isg;

	$message =~ s~\[fixed\]~<font face="Courier New">~isg;
	$message =~ s~\[\/fixed\]~</font>~isg;

	$message =~ s~\[sup\]~<sup>~isg;
	$message =~ s~\[\/sup\]~</sup>~isg;
	
	$message =~ s~\[strike\]~<strike>~isg;
	$message =~ s~\[\/strike\]~</strike>~isg;

	$message =~ s~\[sub\]~<sub>~isg;
	$message =~ s~\[\/sub\]~</sub>~isg;

	$message =~ s~\[left\]~<div align="left">~isg;
	$message =~ s~\[\/left\]~</div>~isg;
	$message =~ s~\[center\]~<center>~isg;
	$message =~ s~\[\/center\]~</center>~isg;
	$message =~ s~\[right\]~<div align="right">~isg;
	$message =~ s~\[\/right\]~</div>~isg;

	$message =~ s~\[list\]~<ul>~isg;
	$message =~ s~\[\*\]~<li>~isg;
	$message =~ s~\[\/list\]~</ul>~isg;

	$message =~ s~\[pre\]~<pre>~isg;
	$message =~ s~\[\/pre\]~</pre>~isg;

	$message =~ s~\[code\](.+?)\[\/code\]~<blockquote><font face="Courier New">code:</font><hr align=left width=40%><font face="Courier New"><pre>$1</pre></font><hr align=left width=40%></blockquote>~isg;

	$message =~ s~\[email\](.+?)\[\/email\]~<a href="mailto:$1">$1</a>~isg;

	$message =~ s~\[url\]www\.\s*(.+?)\s*\[/url\]~<a href="http://www.$1" target="_blank">www.$1</a>~isg;
	$message =~ s~\[url=\s*(\w+\://.+?)\](.+?)\s*\[/url\]~<a href="$1" target="_blank">$2</a>~isg;
	$message =~ s~\[url=\s*(.+?)\]\s*(.+?)\s*\[/url\]~<a href="http://$1" target="_blank">$2</a>~isg;
	$message =~ s~\[url\]\s*(.+?)\s*\[/url\]~<a href="$1" target="_blank">$1</a>~isg;

	$message =~ s~([^\w\"\=\[\]]|[\n\b]|\A)\\*(\w+://[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="$2" target="_blank">$2</a>~isg;
	$message =~ s~([^\"\=\[\]/\:\.]|[\n\b]|\A)\\*(www\.[\w\~\.\;\:\,\$\-\+\!\*\?/\=\&\@\#\%]+[\w\~\.\;\:\$\-\+\!\*\?/\=\&\@\#\%])~$1<a href="http://$2" target="_blank">$2</a>~isg;

	$message =~ s~\{\{~\[~g;
	$message =~ s~\}\}~\]~g;
}

1;