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

############################MAIN
if ($INPUT{'user'} eq "") {
&signup
}
else {
#############################LOAD DATA
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
if ($user eq ""){
&signup
}
else{
if ($INPUT{'a'} eq "save") { &saveupdate }
elsif ($INPUT {'a'} eq "go") { &setup }
elsif ($INPUT {'a'} eq "Update Info") { &upinfo }
elsif ($INPUT {'a'} eq "Info") { &memupdate }
else {
###############################PRINT MAIN
print "<HTML><HEAD>\n";
print "<TITLE>New Page</TITLE>\n";
print "</HEAD><BODY BGCOLOR=$back TEXT=$fmain LINK=$link VLINK=$link>\n";
print "Hello $first $last<BR>\n";
print "Loged on as $user<BR>\n";
print "<A HREF=main.cgi?user=$INPUT{'user'}&a=go>Edit Look</A>\n";
print "<A HREF=main.cgi?user=$INPUT{'user'}&a=Info>Edit info</A>\n";
if ($news eq "yes") {
&runnews
}
if ($weather eq "yes") {
&runweather
}
if ($smail eq "yes") {
&runsmail
}
if ($stock eq "yes") {
&runstock
}
print "</BODY></HTML>\n";
}
}
}
########################SIGN UP
sub signup {
if ($INPUT{'a'} eq ""){
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
print "</TR><TR>\n";
print "<TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=submit VALUE=LogIn></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
print "<CENTER>Not a Member yet?\n";
print "<FORM onSubmit=\"return checkrequired\(this\)\">\n";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD><FONT COLOR=red>First Name</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredfname></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>Last Name</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredlname></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>UserName</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requirednuser MAXLENGTH=10 onKeyUp=\"javascript:dodacheck\(xyz.nuser\)\;\" onBlur=this.value=ignoreSpaces\(this.value\)\; onChange=javascript\:this.value=this.value.toLowerCase()\;></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>Password</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredpass MAXLENGTH=10 onKeyUp=\"javascript:dodacheck\(xyz.pass\)\;\" onBlur=this.value=ignoreSpaces\(this.value\)\; onChange=javascript\:this.value=this.value.toLowerCase()\;></TD>\n";
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
print "<INPUT TYPE=submit Name=a Value=Submit>   \n";
print "<INPUT TYPE=reset></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
}
else {
open (FILE, "data/$INPUT{'requirednuser'}.mem");
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
$user = "$INPUT{'requirednuser'}";
$pass = "$INPUT{'requiredpass'}";
open(cnt, ">data/$user.mem");
print cnt "$INPUT{'requiredfname'}\n";
print cnt "$INPUT{'requiredlname'}\n";
print cnt "$INPUT{'requirednuser'}\n";
print cnt "$INPUT{'requiredpass'}\n";
print cnt "$INPUT{'requiredemail'}\n";
if ($INPUT{'address'} eq "") {
print cnt "Not Entered\n";
}
else {
print cnt "$INPUT{'address'}\n";
}
print cnt "$INPUT{'requiredcity'}\n";
print cnt "$INPUT{'requiredstate'}\n";
print cnt "$INPUT{'requiredzip'}\n";
if ($INPUT{'phone'} eq "") {
print cnt "Not Entered\n";
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
&setup
}
else {
print "Username Taken";
}
}
}
#########################NEXT PAGE
sub setup {
if ($INPUT{'requiredpass'} eq ""){
$pass = "$INPUT{'pass'}";
}
else {
$pass = "$INPUT{'requiredpass'}";
}
if ($pass eq "") {
print "<FORM><CENTER>\n";
print "<TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD>UserName</TD>\n";
print "<TD>$user</TD></TR>\n";
print "<TR><TD>Password</TD><TD>\n";
print "<INPUT TYPE=password NAME=pass></TD></TR>\n";
print "<TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=hidden name=user value=$user><INPUT TYPE=submit name=a value=go></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
}
else {
open (FILE, "data/$INPUT{'user'}.mem");
flock (FILE, 2);
$first = <FILE>;
chop ($first);
$last = <FILE>;
chop ($last);
$user = <FILE>;
chop ($user);
$passA = <FILE>;
chop ($passA);
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

#if ($pass eq "$passA") {

print "<FORM><CENTER>\n";
print "Setup the look of your page\n";
print "<TABLE BORDER=0 CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD>\n";
print "<TABLE BORDER CELLSPACING=1>\n";
print "<TR><TD COLSPAN=6><P ALIGN=Center>\n";
print "BackGround Color</TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=bgco VALUE=ff0000></TD>\n";
print "<TD><FONT COLOR=ff0000>Red</FONT></TD>\n";
print "<TD><INPUT TYPE=radio NAME=bgco VALUE=800080></TD>\n";
print "<TD><FONT COLOR=800080>Purple</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=bgco VALUE=ffffff></TD>\n";
print "<TD><FONT COLOR=ffffff>White</FONT></TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=bgco VALUE=0000ff></TD>\n";
print "<TD><FONT COLOR=#0000ff>Blue</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=bgco VALUE=ffff00></TD>\n";
print "<TD><FONT COLOR=ffff00>Yellow</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=bgco VALUE=c0c0c0></TD>\n";
print "<TD><FONT COLOR=#c0c0c0>Gray</FONT></TD></TR><TR>\n";
print "<TD><INPUT TYPE=radio NAME=bgco VALUE=00ff00></TD>\n";
print "<TD><FONT COLOR=#00ff00>Green</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=bgco VALUE=000000></TD>\n";
print "<TD><FONT COLOR=#000000>Black</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=bgco VALUE=ff80ff></TD>\n";
print "<TD><FONT COLOR=#ff80ff>Pink</FONT></TD>\n";
print "</TR></TABLE>\n";
print "</TD></TR>\n";
print "<TABLE BORDER CELLSPACING=1>\n";
print "<TR><TD COLSPAN=6><P ALIGN=Center>\n";
print "Menu BackGround Color</TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=mbgco VALUE=ff0000></TD>\n";
print "<TD><FONT COLOR=ff0000>Red</FONT></TD>\n";
print "<TD><INPUT TYPE=radio NAME=mbgco VALUE=800080></TD>\n";
print "<TD><FONT COLOR=800080>Purple</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mbgco VALUE=ffffff></TD>\n";
print "<TD><FONT COLOR=ffffff>White</FONT></TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=mbgco VALUE=0000ff></TD>\n";
print "<TD><FONT COLOR=#0000ff>Blue</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mbgco VALUE=ffff00></TD>\n";
print "<TD><FONT COLOR=ffff00>Yellow</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mbgco VALUE=c0c0c0></TD>\n";
print "<TD><FONT COLOR=#c0c0c0>Gray</FONT></TD></TR><TR>\n";
print "<TD><INPUT TYPE=radio NAME=mbgco VALUE=00ff00></TD>\n";
print "<TD><FONT COLOR=#00ff00>Green</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mbgco VALUE=000000></TD>\n";
print "<TD><FONT COLOR=#000000>Black</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mbgco VALUE=ff80ff></TD>\n";
print "<TD><FONT COLOR=#ff80ff>Pink</FONT></TD>\n";
print "</TR></TABLE>\n";
print "</TD></TR>\n";
print "<TABLE BORDER CELLSPACING=1>\n";
print "<TR><TD COLSPAN=6><P ALIGN=Center>\n";
print "Text Color</TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=fco VALUE=ff0000></TD>\n";
print "<TD><FONT COLOR=ff0000>Red</FONT></TD>\n";
print "<TD><INPUT TYPE=radio NAME=fco VALUE=800080></TD>\n";
print "<TD><FONT COLOR=800080>Purple</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=fco VALUE=ffffff></TD>\n";
print "<TD><FONT COLOR=ffffff>White</FONT></TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=fco VALUE=0000ff></TD>\n";
print "<TD><FONT COLOR=#0000ff>Blue</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=fco VALUE=ffff00></TD>\n";
print "<TD><FONT COLOR=ffff00>Yellow</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=fco VALUE=c0c0c0></TD>\n";
print "<TD><FONT COLOR=#c0c0c0>Gray</FONT></TD></TR><TR>\n";
print "<TD><INPUT TYPE=radio NAME=fco VALUE=00ff00></TD>\n";
print "<TD><FONT COLOR=#00ff00>Green</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=fco VALUE=000000></TD>\n";
print "<TD><FONT COLOR=#000000>Black</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=fco VALUE=ff80ff></TD>\n";
print "<TD><FONT COLOR=#ff80ff>Pink</FONT></TD>\n";
print "</TR></TABLE>\n";
print "</TD></TR>\n";
print "<TABLE BORDER CELLSPACING=1>\n";
print "<TR><TD COLSPAN=6><P ALIGN=Center>\n";
print "Menu Text Color</TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=mtco VALUE=ff0000></TD>\n";
print "<TD><FONT COLOR=ff0000>Red</FONT></TD>\n";
print "<TD><INPUT TYPE=radio NAME=mtco VALUE=800080></TD>\n";
print "<TD><FONT COLOR=800080>Purple</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mtco VALUE=ffffff></TD>\n";
print "<TD><FONT COLOR=ffffff>White</FONT></TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=mtco VALUE=0000ff></TD>\n";
print "<TD><FONT COLOR=#0000ff>Blue</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mtco VALUE=ffff00></TD>\n";
print "<TD><FONT COLOR=ffff00>Yellow</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mtco VALUE=c0c0c0></TD>\n";
print "<TD><FONT COLOR=#c0c0c0>Gray</FONT></TD></TR><TR>\n";
print "<TD><INPUT TYPE=radio NAME=mtco VALUE=00ff00></TD>\n";
print "<TD><FONT COLOR=#00ff00>Green</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mtco VALUE=000000></TD>\n";
print "<TD><FONT COLOR=#000000>Black</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=mtco VALUE=ff80ff></TD>\n";
print "<TD><FONT COLOR=#ff80ff>Pink</FONT></TD>\n";
print "</TR></TABLE>\n";
print "</TD></TR>\n";
print "<TABLE BORDER CELLSPACING=1>\n";
print "<TR><TD COLSPAN=6><P ALIGN=Center>\n";
print "Link Color</TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=lco VALUE=ff0000></TD>\n";
print "<TD><FONT COLOR=ff0000>Red</FONT></TD>\n";
print "<TD><INPUT TYPE=radio NAME=lco VALUE=800080></TD>\n";
print "<TD><FONT COLOR=800080>Purple</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=lco VALUE=ffffff></TD>\n";
print "<TD><FONT COLOR=ffffff>White</FONT></TD></TR><TR><TD>\n";
print "<INPUT TYPE=radio NAME=lco VALUE=0000ff></TD>\n";
print "<TD><FONT COLOR=#0000ff>Blue</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=lco VALUE=ffff00></TD>\n";
print "<TD><FONT COLOR=ffff00>Yellow</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=lco VALUE=c0c0c0></TD>\n";
print "<TD><FONT COLOR=#c0c0c0>Gray</FONT></TD></TR><TR>\n";
print "<TD><INPUT TYPE=radio NAME=lco VALUE=00ff00></TD>\n";
print "<TD><FONT COLOR=#00ff00>Green</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=lco VALUE=000000></TD>\n";
print "<TD><FONT COLOR=#000000>Black</FONT></TD><TD>\n";
print "<INPUT TYPE=radio NAME=lco VALUE=ff80ff></TD>\n";
print "<TD><FONT COLOR=#ff80ff>Pink</FONT></TD>\n";
print "</TR></TABLE>\n";
print "</TD></TR>\n";
print "<TR><TD><CENTER>\n";
print "<TABLE BORDER CELLSPACING=1 ALIGN=Center>\n";
print "<TR>\n";
print "<TD><INPUT TYPE=checkbox NAME=shownews VALUE=yes CHECKED></TD>\n";
print "<TD>Show News</TD></TR>\n";
################################################################
#<TR><TD><INPUT TYPE=checkbox NAME=showweather VALUE=yes CHECKED></TD>\n";
#<TD>Show Weather</TD></TR>\n";
#<TR><TD><INPUT TYPE=checkbox NAME=showsmail VALUE=yes CHECKED></TD>\n";
#<TD>Show E-Mail Fast Link</TD></TR>\n";
#<TR><TD><INPUT TYPE=checkbox NAME=showstock VALUE=yes CHECKED></TD>\n";
#<TD>Show Stock Qoutes</TD></TR>\n";
################################################################
print "<INPUT TYPE=hidden NAME=showweather value=no>\n";
print "<INPUT TYPE=hidden NAME=showsmail value=no>\n";
print "<INPUT TYPE=hidden NAME=showstock value=no>\n";
print "</TABLE></CENTER></TD></TR><TR>\n";
print "<TD><P ALIGN=Center>\n";
print "<INPUT TYPE=hidden NAME=user value=$user>\n";
print "<INPUT TYPE=hidden NAME=pass value=$INPUT{'requiredpass'}>\n";
print "<INPUT TYPE=submit name=a VALUE=save></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
#}
#else {
#print "bad pass";
#}
}
}
#########################SAVE UPDAT
sub saveupdate {
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

if ($pass eq "$passA") {

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
print cnt "$INPUT{'fco'}\n";
print cnt "$INPUT{'mtco'}\n";
print cnt "$INPUT{'bgco'}\n";
print cnt "$INPUT{'lco'}\n";
print cnt "$INPUT{'mbgco'}\n";
print cnt "$INPUT{'shownews'}\n";
print cnt "$INPUT{'showweather'}\n";
print cnt "$INPUT{'showsmail'}\n";
print cnt "$INPUT{'showstock'}\n";
print cnt "junk\n";
close(cnt);

print "setings saved";
}
#########################MEMBER UPDATE
sub memupdate {
if ($INPUT{'requiredpass'} eq ""){
$pass = "$INPUT{'pass'}";
}
else {
$pass = "$INPUT{'requiredpass'}";
}
if ($pass eq "") {
print "<FORM><CENTER>\n";
print "<TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD>UserName</TD>\n";
print "<TD>$user</TD></TR>\n";
print "<TR><TD>Password</TD><TD>\n";
print "<INPUT TYPE=password NAME=pass></TD></TR>\n";
print "<TR><TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=hidden name=user value=$user><INPUT TYPE=submit name=a value=Info></TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
}
else {
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
print "</HEAD><BODY>\n";
print "<FORM onSubmit=\"return checkrequired\(this\)\">\n";
print "<CENTER><TABLE BORDER CELLPADDING=2 ALIGN=Center>\n";
print "<TR><TD><FONT COLOR=red>First Name</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredfname value=$first></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>Last Name</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredlname value=$last></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>UserName</FONT></TD><TD>\n";
print "<INPUT TYPE=Hidden NAME=user value=$user>$user</TD>\n";
print "</TR><TR><TD><FONT COLOR=red>Password</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredpass value=$pass MAXLENGTH=10 onKeyUp=\"javascript:dodacheck\(xyz.pass\)\;\" onBlur=this.value=ignoreSpaces\(this.value\)\; onChange=javascript\:this.value=this.value.toLowerCase()\;></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>E-Mail</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredemail value=$email>\n";
print "</TD></TR><TR><TD>Address</TD><TD>\n";
print "<INPUT TYPE=text NAME=address value=$address></TD>\n";
print "</TR><TR><TD><FONT COLOR=red>City</FONT></TD><TD>\n";
print "<INPUT TYPE=text NAME=requiredcity value=$city>\n";
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
print "<INPUT TYPE=text NAME=requiredzip MAXLENGTH=5 value=$zip></TD>\n";
print "</TR><TR><TD>Phone</TD><TD>\n";
print "<INPUT TYPE=text NAME=phone MAXLENGTH=10 value=$phone></TD>\n";
print "</TR><TR>\n";
print "<TD COLSPAN=2><P ALIGN=Center>\n";
print "<INPUT TYPE=submit Name=a Value=\"Update Info\">\n";
print "</TD>\n";
print "</TR></TABLE></CENTER></FORM>\n";
else {
print "bad pass";
}
}
}
###########################SAVEMEM
sub savemem {
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

open(cnt, ">data/user.mem");
print cnt "$INPUT{'requiredfname'}\n";
print cnt "$INPUT{'requiredlname'}\n";
print cnt "$user\n";
print cnt "$INPUT{'requiredpass'}\n";
print cnt "$INPUT{'requiredemail'}\n";
print cnt "$INPUT{'address'}\n";
print cnt "$INPUT{'requiredcity'}\n";
print cnt "$INPUT{'requiredstate'}\n";
print cnt "$INPUT{'requiredzip'}\n";
print cnt "$INPUT{'phone'}\n";
print cnt "$fmain\n";
print cnt "$fside\n";
print cnt "$back\n";
print cnt "$link\n";
print cnt "$side\n";
print cnt "$news\n";
print cnt "$weather\n";
print cnt "$smail\n";
print cnt "$stock\n";
print cnt "junk\n";
close(cnt);

print "setings saved";
}
#########################NEWS
sub runnews {
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
#######################WEATHER
sub runweather {
print "weather Not Avalabul yet<BR>";
}
#######################SMAIL
sub runsmail {
print "smail Not Avalabul yet<BR>";
}
#######################STOCK
sub runstock {
print "stock Not Avalabul yet<BR>";
}