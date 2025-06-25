#!/usr/bin/perl

########################################################################
#  $first $last $user $pass $email $address $city $state $zip $phone   #
#  $fmain $fside $back $link $side $news $weather $smail $stock        #
########################################################################


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
print "Content-type: text/html\n\n";

if ($INPUT{'a'} eq "login") { &login }
elsif ($INPUT{'a'} eq "signup") { &signup }
elsif ($INPUT{'a'} eq "editlook") { &editlook }
elsif ($INPUT{'a'} eq "updatelook") { &updatelook }
elsif ($INPUT{'a'} eq "editinfo") { &editinfo }
else { &form }

#### FORM ####
sub form {
print "<HEAD><SCRIPT LANGUAGE=JavaScript>\n";
print "<!-- Begin\n";
print "function ignoreSpaces\(string\) \{\n";
print "var temp = \"\"\;\n";
print "string = '' + string\;\n";
print "splitstring = string.split\(\" \"\)\;\n";
print "for\(i = 0\; i < splitstring.length\; i++\)\n";
print "temp += splitstring[i]\;\n";
print "return temp\;\n";
print "\}\n";
print "//  End -->\n";
print "</script>\n";
print "<SCRIPT LANGUAGE=JavaScript>\n";
print "<!-- Begin\n";
print "var mikExp = /[\$\\\\@\\\\\\#%\\^\\&\\*\\\(\\\)\\[\\]\\+\\_\\\{\\\}\\`\\~\\=\\|]/\;\n";
print "function dodacheck\(val\) \{\n";
print "var strPass = val.value\;\n";
print "var strLength = strPass.length\;\n";
print "var lchar = val.value.charAt\(\(strLength\) - 1\)\;\n";
print "if\(lchar.search\(mikExp\) != -1\) \{\n";
print "var tst = val.value.substring\(0, \(strLength\) - 1\)\;\n";
print "val.value = tst\;\n";
print "   \}\n";
print "\}\n";
print "//  End -->\n";
print "</script>\n";
print "<SCRIPT LANGUAGE=JavaScript>\n";
print "<!-- Begin\n";
print "function checkrequired\(which\) \{\n";
print "var pass=true\;\n";
print "if \(document.images\) \{\n";
print "for \(i=0\;i<which.length\;i++\) \{\n";
print "var tempobj=which.elements[i]\;\n";
print "if \(tempobj.name.substring\(0,8\)==\"required\"\) \{\n";
print "if \(\(\(tempobj.type==\"text\"||tempobj.type==\"textarea\"\)&&\n";
print "tempobj.value==''\)||\(tempobj.type.toString\(\).charAt\(0\)==\"s\"&&\n";
print "tempobj.selectedIndex==0\)\) \{\n";
print "pass=false\;\n";
print "break\;\n";
print "\}\}\}\}\n";
print "if \(!pass\) \{\n";
print "shortFieldName=tempobj.name.substring\(8,30\).toUpperCase\(\)\;\n";
print "alert\(\"Please make sure the \"+shortFieldName+\" field was properly completed.\"\)\;\n";
print "return false\;\n";
print "\}\n";
print "else \n";
print "return true\;\n";
print "\}\n";
print "//  End -->\n";
print "</script>\n";
print "</HEAD><BODY><CENTER>Allready a member?\n";
print "<FORM><CENTER>\n";
print "<TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD>UserName</TD><TD>\n";
print "<INPUT TYPE=text NAME=user></TD>\n";
print "</TR>\n";
print "<TR><TD>PassWord</TD><TD>\n";
print "<INPUT TYPE=text NAME=pass></TD>\n";
print "</TR>\n";
print "<TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=hidden name=a value=login><INPUT TYPE=submit VALUE=LogIn></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
print "<CENTER>Not a Member yet?\n";
print "<FORM name=xyz onSubmit=\"return checkrequired\(this\)\">\n";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD><FONT COLOR=red>First Name</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredfirst></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>Last Name</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredlast></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>UserName</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requireduser MAXLENGTH=10 onKeyUp=\"javascript:dodacheck\(xyz.requireduser\)\;\" onBlur=this.value=ignoreSpaces\(this.value\)\; onChange=javascript\:this.value=this.value.toLowerCase()\;></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>Password</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredpass MAXLENGTH=10 onKeyUp=\"javascript:dodacheck\(xyz.requiredpass\)\;\" onBlur=this.value=ignoreSpaces\(this.value\)\; onChange=javascript\:this.value=this.value.toLowerCase()\;></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>E-Mail</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredemail>\n";
print "</TD></TR><TR><TD>Address</TD><TD>\n";
print "<INPUT TYPE=text NAME=address></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>City</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredcity>\n";
print "</TD></TR><TR><TD><FONT COLOR=red>State</FONT></TD>\n";
print "<TD><select name=requiredstate>\n";
print "<option value= selected>Please Select</option>\n";
print "<option value=AK>Alaska</option>\n";
print "<option value=AL>Alabama</option>\n";
print "<option value=AR>Arkansas</option>\n";
print "<option value=AZ>Arizona</option>\n";
print "<option value=CA>California</option>\n";
print "<option value=CO>Colorado</option>\n";
print "<option value=CT>Conneticut</option>\n";
print "<option value=DE>Delaware</option>\n";
print "<option value=FL>Florida</option>\n";
print "<option value=GA>Georgia</option>\n";
print "<option value=HI>Hawaii</option>\n";
print "<option value=IA>Iowa</option>\n";
print "<option value=ID>Idaho</option>\n";
print "<option value=IL>Illinois</option>\n";
print "<option value=IN>Indiana</option>\n";
print "<option value=KS>Kansas</option>\n";
print "<option value=KY>Kentucky</option>\n";
print "<option value=LA>Louisiana</option>\n";
print "<option value=MA>Massachusetts</option>\n";
print "<option value=MD>Maryland</option>\n";
print "<option value=MI>Michigan</option>\n";
print "<option value=MN>Minnesota</option>\n";
print "<option value=MO>Missouri</option>\n";
print "<option value=MS>Mississippi</option>\n";
print "<option value=MT>Montana</option>\n";
print "<option value=NC>North Carolina</option>\n";
print "<option value=ND>North Dakota</option>\n";
print "<option value=NE>Nebraska</option>\n";
print "<option value=NH>New Hampshire</option>\n";
print "<option value=NJ>New Jersey</option>\n";
print "<option value=NM>New Mexico</option>\n";
print "<option value=NV>Nevada</option>\n";
print "<option value=NY>New York</option>\n";
print "<option value=OH>Ohio</option>\n";
print "<option value=OK>Oklahoma</option>\n";
print "<option value=OR>Oregon</option>\n";
print "<option value=PA>Pennsylvania</option>\n";
print "<option value=RI>Rhode Island</option>\n";
print "<option value=SC>South Carolina</option>\n";
print "<option value=SD>South Dakota</option>\n";
print "<option value=TN>Tennessee</option>\n";
print "<option value=TX>Texas</option>\n";
print "<option value=UT>Utah</option>\n";
print "<option value=VI>Virgin Islands</option>\n";
print "<option value=VT>Vermont</option>\n";
print "<option value=VA>Virginia</option>\n";
print "<option value=WA>Washington</option>\n";
print "<option value=WI>Wisconsin</option>\n";
print "<option value=WV>West Virginia</option>\n";
print "<option value=WY>Wyoming</option>\n";
print "</select></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>Zip Code</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredzip MAXLENGTH=5></TD>\n";
print "</TR><TR><TD>Phone</TD><TD>\n";
print "<INPUT TYPE=text NAME=phone MAXLENGTH=10></TD>\n";
print "</TR><TR>\n";
print "<TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT type=hidden name=a value=signup><INPUT TYPE=submit Value=Submit>   \n";
print "<INPUT TYPE=reset></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
}

#### SIGNUP ####
sub signup {
open (FILE, "data/$INPUT{'requireduser'}.mem");
flock (FILE, 2);
$first = <FILE>;
chop ($first);
$last = <FILE>;
chop ($last);
$user = <FILE>;
chop ($user);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$address = <FILE>;
chop ($address);
$city = <FILE>;
chop ($city);
$state = <FILE>;
chop ($state);
$zip = <FILE>;
chop ($zip);
$phone = <FILE>;
chop ($phone);
$fmain = <FILE>;
chop ($fmain);
$fside = <FILE>;
chop ($fside);
$back = <FILE>;
chop ($back);
$link = <FILE>;
chop ($link);
$side = <FILE>;
chop ($side);
$news = <FILE>;
chop ($news);
$weather = <FILE>;
chop ($weather);
$smail = <FILE>;
chop ($smail);
$stock = <FILE>;
chop ($stock);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);


if ($junk eq "") {
$user = "$INPUT{'requireduser'}";
$pass = "$INPUT{'requiredpass'}";
open(cnt, ">data/$user.mem");
print cnt "$INPUT{'requiredfirst'}\n";
print cnt "$INPUT{'requiredlast'}\n";
print cnt "$INPUT{'requireduser'}\n";
print cnt "$INPUT{'requiredpass'}\n";
print cnt "$INPUT{'requiredemail'}\n";
if ($INPUT{'address'} eq "") {
print cnt "Not-Entered\n";
}
else {
print cnt "$INPUT{'address'}\n";
}
print cnt "$INPUT{'requiredcity'}\n";
print cnt "$INPUT{'requiredstate'}\n";
print cnt "$INPUT{'requiredzip'}\n";
if ($INPUT{'phone'} eq "") {
print cnt "Not-Entered\n";
}
else {
print cnt "$INPUT{'phone'}\n";
}
print cnt "blue\n";
print cnt "red\n";
print cnt "green\n";
print cnt "purple\n";
print cnt "yellow\n";
print cnt "yes\n";
print cnt "no\n";
print cnt "no\n";
print cnt "no\n";
print cnt "junk\n";
close(cnt);

print "<CENTER>User added<BR>";
print "<A HREF=http://www.erenetwork.com/home/cgi/home.cgi>Go Back</A>";
}
else {
print "<CENTER>Username Taken<BR>";
print "<A HREF=http://www.erenetwork.com/home/cgi/home.cgi>Go Back</A>";
}
}

#### LOGIN ####
sub login {
open (FILE, "data/$INPUT{'user'}.mem");
flock (FILE, 2);
$first = <FILE>;
chop ($first);
$last = <FILE>;
chop ($last);
$user = <FILE>;
chop ($user);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$address = <FILE>;
chop ($address);
$city = <FILE>;
chop ($city);
$state = <FILE>;
chop ($state);
$zip = <FILE>;
chop ($zip);
$phone = <FILE>;
chop ($phone);
$fmain = <FILE>;
chop ($fmain);
$fside = <FILE>;
chop ($fside);
$back = <FILE>;
chop ($back);
$link = <FILE>;
chop ($link);
$side = <FILE>;
chop ($side);
$news = <FILE>;
chop ($news);
$weather = <FILE>;
chop ($weather);
$smail = <FILE>;
chop ($smail);
$stock = <FILE>;
chop ($stock);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($junk eq "") {
print "bad username";
}
else {
if ($INPUT{'pass'} eq "$pass") {
print "<HTML><HEAD>\n";
print "<TITLE>New Page</TITLE>\n";
print "</HEAD><BODY BGCOLOR=$back TEXT=$fmain LINK=$link VLINK=$link>\n";
print "Hello $first $last<BR>\n";
print "Loged on as $user<BR>\n";
print "<A HREF=home.cgi?user=$INPUT{'user'}&pass=$INPUT{'pass'}&a=editlook>Edit Look</A>\n";
print "<A HREF=home.cgi?user=$INPUT{'user'}&pass=$INPUT{'pass'}&a=editinfo>Edit info</A>\n";
if ($news eq "Yes") {
&news
}
if ($weather eq "Yes") {
&weather
}
if ($smail eq "Yes") {
&smail
}
if ($stock eq "Yes") {
&stock
}
print "</BODY></HTML>\n";
}
else {
print "bad Password";
}
}
}

#### EDITLOOK ####
sub editlook {
print "<FORM><CENTER>\n";
print "<TABLE BORDER CELLSPACING=1 ALIGN=Center>\n";
print "<TR>\n";
print "<TD>Main Font Color</TD>\n";
print "<TD>\n";
print "<SELECT NAME=fmain> \n";
print "<OPTION SELECTED>Blue \n";
print "<OPTION>Red \n";
print "<OPTION>Green \n";
print "<OPTION>Yellow</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>Menu Font Color</TD>\n";
print "<TD>\n";
print "<SELECT NAME=fside> \n";
print "<OPTION SELECTED>Blue \n";
print "<OPTION>Red \n";
print "<OPTION>Green \n";
print "<OPTION>Yellow</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>Link Color</TD>\n";
print "<TD>\n";
print "<SELECT NAME=link> \n";
print "<OPTION SELECTED>Blue \n";
print "<OPTION>Red \n";
print "<OPTION>Green \n";
print "<OPTION>Yellow</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>BackGround Color</TD>\n";
print "<TD>\n";
print "<SELECT NAME=back> \n";
print "<OPTION SELECTED>Blue \n";
print "<OPTION>Red \n";
print "<OPTION>Green \n";
print "<OPTION>Yellow</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>Menu BackGround Color</TD>\n";
print "<TD>\n";
print "<SELECT NAME=side> \n";
print "<OPTION SELECTED>Blue \n";
print "<OPTION>Red \n";
print "<OPTION>Green \n";
print "<OPTION>Yellow</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>Show News</TD>\n";
print "<TD>\n";
print "<SELECT NAME=news> \n";
print "<OPTION SELECTED>Yes \n";
print "<OPTION>No</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>Show Weather</TD>\n";
print "<TD>\n";
print "<SELECT NAME=weather> \n";
print "<OPTION SELECTED>Yes \n";
print "<OPTION>No</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>Show E-Mail QuickLink</TD>\n";
print "<TD>\n";
print "<SELECT NAME=smail> \n";
print "<OPTION SELECTED>Yes \n";
print "<OPTION>No</SELECT>\n";
print "</TD>\n";
print "</TR><TR>\n";
print "<TD>Show Stock Qoutes</TD>\n";
print "<TD>\n";
print "<SELECT NAME=stock> \n";
print "<OPTION SELECTED>Yes \n";
print "<OPTION>No</SELECT>\n";
print "</TD></TR>\n";
print "<TR>\n";
print "<TD COLSPAN=2>\n";
print "<P ALIGN=Center>\n";
print "<INPUT TYPE=hidden name=user value=$INPUT{'user'}><INPUT TYPE=hidden name=pass value=$INPUT{'pass'}><INPUT TYPE=hidden name=a value=updatelook><INPUT TYPE=submit>\n";
print "</TD>\n";
print "</TR>\n";
print "</TABLE></CENTER></FORM>\n";
}
#### UPDATELOOK ####
sub updatelook {
open (FILE, "data/$INPUT{'user'}.mem");
flock (FILE, 2);
$first = <FILE>;
chop ($first);
$last = <FILE>;
chop ($last);
$user = <FILE>;
chop ($user);
$pass = <FILE>;
chop ($pass);
$email = <FILE>;
chop ($email);
$address = <FILE>;
chop ($address);
$city = <FILE>;
chop ($city);
$state = <FILE>;
chop ($state);
$zip = <FILE>;
chop ($zip);
$phone = <FILE>;
chop ($phone);
$fmain = <FILE>;
chop ($fmain);
$fside = <FILE>;
chop ($fside);
$back = <FILE>;
chop ($back);
$link = <FILE>;
chop ($link);
$side = <FILE>;
chop ($side);
$news = <FILE>;
chop ($news);
$weather = <FILE>;
chop ($weather);
$smail = <FILE>;
chop ($smail);
$stock = <FILE>;
chop ($stock);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);
if ($junk eq "") {
print "bad username";
}
else {
if ($INPUT{'pass'} eq "$pass") {
open(cnt, ">data/$INPUT{'user'}.mem");
print cnt "$first\n";
print cnt "$last\n";
print cnt "$user\n";
print cnt "$pass\n";
print cnt "$email\n";
print cnt "$address\n";
print cnt "$city\n";
print cnt "$state\n";
print cnt "$zip\n";
print cnt "$phone\n";
print cnt "$INPUT{'fmain'}\n";
print cnt "$INPUT{'fside'}\n";
print cnt "$INPUT{'back'}\n";
print cnt "$INPUT{'link'}\n";
print cnt "$INPUT{'side'}\n";
print cnt "$INPUT{'news'}\n";
print cnt "$INPUT{'weather'}\n";
print cnt "$INPUT{'smail'}\n";
print cnt "$INPUT{'stock'}\n";
print cnt "junk\n";
close(cnt);

print "<CENTER>Look Updated<BR>";
print "<A HREF=http://www.erenetwork.com/home/cgi/home.cgi?a=login&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Go Back</A>";
}
else {
print "bad Password";
}
}
}



#### NEWS ####
sub news {
$fonttag="size=-1";
$linktag="target=_new";
$tablewidth="50%";
$tableborder="on";

use LWP::Simple;
$ENV{'QUERY_STRING'}=us;
@display=split(/\|/,$ENV{'QUERY_STRING'});
foreach $category(@display){
	@href=@clear;
	@headlines=@clear;
	$stop=0;
	if($category eq 'us'){
		$news="US News";
		&GetPage("http://abcnews.go.com/sections/us/");
		@news_page=split(/\n/,$raw_news_page);
		foreach $line(@news_page){
			&CheckLine;
			if(($line=~/\/sections\/us\/DailyNews\//gi)&&($stop==0)){
				&GetHeadline;
			}
		}
	}




	$link=0;
	if($tableborder eq "on"){
		print "<p><table border=1 width=$tablewidth><tr><td><p><table border=0 width=100%><tr><th colspan=2 width=100%>$news</th></tr>\n";
	}else{
		print "<p><table border=0 width=$tablewidth><tr><th colspan=2 width=100%>$news</th></tr>\n";
	}
	foreach $headline(@headlines){
		print "<tr><td>•</td><td><font $fonttag><a href=\"@href[$link]\" $linktag>$headline</a></font></td></tr>\n";
		$link++;
	}
	print "<tr><td colspan=2 align=center>News from <a href=http://abcnews.com/ $linktag>ABCNEWS.com</a></td></tr></table></p>\n";
	if($tableborder eq "on"){
		print "</td></tr></table></p>";
	}
}

sub GetPage{
	$raw_news_page=get $_[0];
	$raw_news_page=~s/<a href=(.+?)>\n/<a href=$1>/gi;
	$raw_news_page=~s/<br>/\n/gi;
	$raw_news_page=~s/<div (.+?)>//gi;
	$raw_news_page=~s/<\/div>/\n/gi;
	$raw_news_page=~s/\n<\/a>/<\/a>\n/gi;
	$raw_news_page=~s/\n+/\n/gi;
	$raw_news_page=~s/<\/a>^\n/<\/a>\n/gi;
}
sub GetHeadline{
	$href=$line;
	$href=~/<a href="(.+?)"(.+?)>/i;
	$href=$1;
	$headline=$line;
	($headline,$junk)=split(/<\/a>/i,$headline) if $headline=~/<\/a>/i;
	$headline=~s/<(.+?)>//gi;
	if(($href ne '')&&(length($headline)>2)&&($href!~/http:|javascript:/gi)){
		$href="http://abcnews.go.com".$href;
		push(@href,$href);
		push(@headlines,$headline);
	}
}
sub CheckLine{
	chomp($line);
	if($line eq "<!---------- RIGHT COLUMN  ------------------>"){
		$stop=1;
	}
}
}
#### WEATHER ####
sub weather {
print "weather Not Avalabul yet<BR>";
}
#### SMAIL ####
sub smail {
print "smail Not Avalabul yet<BR>";
}
#### STOCK #####
sub stock {
print "stock Not Avalabul yet<BR>";
}