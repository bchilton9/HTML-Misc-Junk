#!/usr/bin/perl

##################################################################################

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

##################################################################################

print "Content-type: text/html\n\n";

##################################################################################

if ($INPUT{'do'} eq "savelinkline") { &savelinkline; }
elsif ($INPUT{'do'} eq "changelinkline") { &changelinkline; }
else { &changelinkline; }

##################################################################################

sub savelinkline {

$INPUT{'list'} =~ s/!HR!/\n/gi;
$INPUT{'list'} =~ s/!pct!/&/gi;
$INPUT{'list'} =~ s/!fs!/\//gi;
$INPUT{'list'} =~ s/!eql!/=/gi;
$INPUT{'list'} =~ s/!qm!/?/gi;

open(DATA, ">data/$INPUT{'guild'}.link");
print DATA "$INPUT{'list'}";
close DATA;

$tag = "<B>Link Order changed</b>";
&editwindow;

}

##################################################################################

sub changelinkline {

$cnt = 4;

print <<"HTML";

<HEAD>

<SCRIPT LANGUAGE="JavaScript">

<!-- Begin
function move(index,to) {
var list = document.form.list;
var total = list.options.length-1;
if (index == -1) return false;
if (to == +1 && index == total) return false;
if (to == -1 && index == 0) return false;
var items = new Array;
var values = new Array;
for (i = total; i >= 0; i--) {
items[i] = list.options[i].text;
values[i] = list.options[i].value;
}
for (i = total; i >= 0; i--) {
if (index == i) {
list.options[i + to] = new Option(items[i],values[i + to], 0, 1);
list.options[i] = new Option(items[i + to], values[i]);
i--;
}
else {
list.options[i] = new Option(items[i], values[i]);
   }
}
list.focus();
}
function submitForm() {
var list = document.form.list;
var theList = "";
for (i = 0; i <= list.options.length-1; i++) { 
theList += list.options[i].text + "!HR!";
}

out = "&"; // replace this
add = "!pct!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}
out = "="; // replace this
add = "!eql!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}
out = "/"; // replace this
add = "!fs!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}
out = "?"; // replace this
add = "!qm!"; // with this
while (theList.indexOf(out)>-1) {
pos= theList.indexOf(out);
theList = "" + (theList.substring(0, pos) + add + 
theList.substring((pos + out.length), theList.length));
}

location.href = document.form.action + "?do=savelinkline&guild=$INPUT{'guild'}&list=" + theList;
}

//  End -->
</script>
  <TITLE>EQ Guilded</TITLE>
</HEAD>
<BODY topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" marginheight="0"
marginwidth="0" bgcolor="#FFFFFF">
<TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0" WIDTH="100%" HEIGHT=100%>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
  <TR VALIGN="Middle">
    <TD VALIGN="Middle" height=98%>
<CENTER>

<form method="GET" action="index.cgi" name="form">
<table>
<tr>
<td align="middle">
<select name="list" size="10" style="width:300">
HTML


$i = 0;
open (DATA, "data/$INPUT{'guild'}.link");
@data = <DATA>;
close DATA;
foreach $line (@data) {
$i = $i + 1;

print "<option value=\"$i\">$line</option>";
}


print <<"HTML";
</select><br><br>

<input type="button" value="submit" onClick="submitForm()">
</td>
<td valign="top">
<input type="button" value="Up" 
onClick="move(this.form.list.selectedIndex,-1)"><br><br>
<input type="button" value="Down"
onClick="move(this.form.list.selectedIndex,+1)">
</td>
</tr>
</table>
</form>
<CENTER><A HREF=$siteurl/?guild=dot&do=edit><B><FONT COLOR=#000000>Edit Main</FONT></B></A>
    </TD>
  </TR>
  <TR>
    <TD background="images/topline.jpg" height=1%>&nbsp; &nbsp;</TD>
  </TR>
</TABLE>
</BODY></HTML>
HTML
}

##################################################################################
