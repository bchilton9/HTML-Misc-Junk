#!/usr/bin/perl

print "Content-type: text/html; charset=UTF-8\n\n";

$SPROXY_VER = "SPROXY.CGI(Perl) v.1.13 (c) SpellChecker.Net 2000";

%data = &ParseInput();

$data{"text"} =~ s/&/&amp;/g;
$data{"text"} =~ s/\"/&quot;/g;
$data{"text"} =~ s/\r/&#13;/g;
$data{"text"} =~ s/\n/&#10;/g;
$data{"text"} =~ s/\t/&#9;/g;
        
$template = "<html>
<head>

<script language='JavaScript'>

var s = '$SPROXY_VER<br><br><b>SCRIPT_FILENAME:</b> $ENV{SCRIPT_FILENAME}';
var frmslen = parent.frames.length;

function doload() {
	if (!parent.opener) return;

	if (!parent.opener.document) {
		parent.close();
		return;
	}

	if (frmslen != 0) {
		var f_src = document.forms[0];
		var ctrl = eval(
			'parent.opener.' + 
			f_src.txt_ctrl.value);
		if (ctrl.value)
			ctrl.value = f_src.msg_body.value;
		else
			if (ctrl.innerHTML)
        		ctrl.innerHTML = f_src.msg_body.value;
		document.forms[1].submit();
		parent.close();
	}
}

</script>

</head>
<body bgcolor=white onload=\"doload();\">
<script language='JavaScript'>if (frmslen == 0) document.write(s);</script>
<center>
<form>
	<input type=hidden name=msg_body value=\"<#text#>\">
	<input type=hidden name=txt_ctrl value=\"<#txt_ctrl#>\">
</form>
<form method=post action=\"<#word#>\">
	<input type=hidden name=cmd value=\"eos\">
	<input type=hidden name=customerid value=\"<#customerid#>\">
	<input type=hidden name=sessionid  value=\"<#sessionid#>\">
</form>
</center>
</body>
</html>";

$template =~ s/<#(\w+)#>/$data{$1}/g;

print $template;

sub ParseInput() {

    (*fval) = @_ if @_ ;

	if ($ENV{'REQUEST_METHOD'} eq 'POST') {
		read(STDIN,$buf,$ENV{'CONTENT_LENGTH'});
	}
	else {
		$buf=$ENV{'QUERY_STRING'};
	}
	if ($buf eq "") {
            return 0;
		}
	else {
 		@fval=split(/&/,$buf);
		foreach $i (0 .. $#fval){
			($name,$val)=split (/=/,$fval[$i],2);
			$val=~tr/+/ /;
			$val=~ s/%(..)/pack("c",hex($1))/ge;
			$val=~ s/\\//g;
			$val=~ s/\`//g;
			$name=~tr/+/ /;
			$name=~ s/%(..)/pack("c",hex($1))/ge;
			$name=~ s/\\//g;
			$name=~ s/\`//g;

			if (!defined($field{$name})) {
				$field{$name}=$val;
			}
			else {
				$field{$name} .= ",$val";
			}
	   }
	}
return %field;
}
