#!/usr/bin/perl

######################
# By Keny Misspeller #
# Of Druzzil Ro      #
# for SoS            #
######################

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

use DBI;
use LWP::Simple;


$hostname="localhost";
$ms="onestcpb_seekers";
$username ="onestcpb_Daveo";
$password ="s0ulr3aver";


if ($INPUT{'menu'} eq "NULL") { &menu; }
elsif ($INPUT{'main'} eq "NULL") { &main; }
elsif ($INPUT{'addnews'} eq "NULL") { &add_news; }
elsif ($INPUT{'addnewsfin'} eq "NULL") { &add_news_fin; }
elsif ($INPUT{'editnews'} eq "NULL") { &edit_news; }
elsif ($INPUT{'editnewsb'} eq "NULL") { &edit_news_b; }
elsif ($INPUT{'editnewsfin'} eq "NULL") { &edit_news_fin; }
elsif ($INPUT{'deletenews'} eq "NULL") { &delete_news; }

elsif ($INPUT{'addleftblock'} eq "NULL") { &add_left_block; }
elsif ($INPUT{'addleftblockfin'} eq "NULL") { &add_left_block_fin; }
elsif ($INPUT{'editleftblock'} eq "NULL") { &edit_left_block; }
elsif ($INPUT{'editleftblockb'} eq "NULL") { &edit_left_block_b; }
elsif ($INPUT{'editleftblockfin'} eq "NULL") { &edit_left_block_fin; }
elsif ($INPUT{'deleteleftblock'} eq "NULL") { &delete_left_block; }

elsif ($INPUT{'addrightblock'} eq "NULL") { &add_right_block; }
elsif ($INPUT{'addrightblockfin'} eq "NULL") { &add_right_block_fin; }
elsif ($INPUT{'editrightblock'} eq "NULL") { &edit_right_block; }
elsif ($INPUT{'editrightblockb'} eq "NULL") { &edit_right_block_b; }
elsif ($INPUT{'editrightblockfin'} eq "NULL") { &edit_right_block_fin; }
elsif ($INPUT{'deleterightblock'} eq "NULL") { &delete_right_block; }
else { &frame_set; }



sub header {

print "Content-type: text/html\n\n";

print qq~
<html>
<head>
<title>Example of HTMLArea 3.0</title>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<!-- Configure the path to the editor.  We make it relative now, so that the
    example ZIP file will work anywhere, but please NOTE THAT it's better to
    have it an absolute path, such as '/htmlarea/'. -->
<script type="text/javascript">
  _editor_url = "./htmlarea/";
  _editor_lang = "en";
</script>

<!-- load the main HTMLArea file, this will take care of loading the CSS and
    other required core scripts. -->
<script type="text/javascript" src="./htmlarea/htmlarea.js"></script>

<!-- load the plugins -->
<script type="text/javascript">
      // WARNING: using this interface to load plugin
      // will _NOT_ work if plugins do not have the language
      // loaded by HTMLArea.

      // In other words, this function generates SCRIPT tags
      // that load the plugin and the language file, based on the
      // global variable HTMLArea.I18N.lang (defined in the lang file,
      // in our case "lang/en.js" loaded above).

      // If this lang file is not found the plugin will fail to
      // load correctly and nothing will work.

      HTMLArea.loadPlugin("TableOperations");
      HTMLArea.loadPlugin("SpellChecker");
      HTMLArea.loadPlugin("FullPage");
      HTMLArea.loadPlugin("CSS");
      HTMLArea.loadPlugin("ContextMenu");
</script>

<style type="text/css">
html, body {
  font-family: Verdana,sans-serif;
}
a:link, a:visited { color: #00f; }
a:hover { color: #048; }
a:active { color: #f00; }

textarea { background-color: #fff; border: 1px solid 00f; }
</style>

<script type="text/javascript">
var editor = null;
function initEditor() {

  // create an editor for the "ta" textbox
  editor = new HTMLArea("ta");

  // register the FullPage plugin
  // editor.registerPlugin(FullPage);

  // register the SpellChecker plugin
  editor.registerPlugin(TableOperations);

  // register the SpellChecker plugin
  editor.registerPlugin(SpellChecker);

  // register the CSS plugin
  editor.registerPlugin(CSS, {
    combos : [
      { label: "Syntax:",
                   // menu text       // CSS class
        options: { "None"           : "",
                   "Code" : "code",
                   "String" : "string",
                   "Comment" : "comment",
                   "Variable name" : "variable-name",
                   "Type" : "type",
                   "Reference" : "reference",
                   "Preprocessor" : "preprocessor",
                   "Keyword" : "keyword",
                   "Function name" : "function-name",
                   "Html tag" : "html-tag",
                   "Html italic" : "html-helper-italic",
                   "Warning" : "warning",
                   "Html bold" : "html-helper-bold"
                 },
        context: "pre"
      },
      { label: "Info:",
        options: { "None"           : "",
                   "Quote"          : "quote",
                   "Highlight"      : "highlight",
                   "Deprecated"     : "deprecated"
                 }
      }
    ]
  });

  // add a contextual menu
  editor.registerPlugin("ContextMenu");

  // load the stylesheet used by our CSS plugin configuration
  editor.config.pageStyle = "@import url(custom.css);";

  setTimeout(function() {
    editor.generate();
  }, 500);
  return false;
}

function insertHTML() {
  var html = prompt("Enter some HTML code here");
  if (html) {
    editor.insertHTML(html);
  }
}
function highlight() {
  editor.surroundHTML('<span style="background-color: yellow">', '</span>');
}
</script>

</head>

<script type="text/javascript" src="calendarDateInput.js">
</script>

<body  bgcolor="silver">
~;

}

sub footer {

print qq~
</body>
</html>
~;

}

sub frame_set  {

print "Content-type: text/html\n\n";

print qq~
<HTML>
<HEAD>
  <TITLE>SoS Admin Page</TITLE>
</HEAD>
<FRAMESET cols = "130,*" frameborder=no bordercolor=silver>
  <FRAME SRC="./index.pl?menu" NAME="links" SCROLLING="No" NORESIZE>
  <FRAME SRC="./index.pl?main" NAME="main" SCROLLING="AUTO">
</FRAMESET>

</HTML>
~;


}

sub main {

&header;


#my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
#or die "Can't connect to DBI: $dbh->errstr\n";

print qq~
<CENTER>
<h3>Seekers of Serenity Adminastration Page.</H3>
<HR>
Items not yet functional are in red <BR>
<BR>
Add News<BR>
Edit News<BR>
Delete News<BR>
<BR>
<FONT COLOR="#ff0000">Left Blocks</FONT><BR>
<FONT COLOR="#ff0000">RightBlocks</FONT><BR>
<BR>
<FONT COLOR="#ff0000">Edit Site html</FONT>
~;


&footer;

}

sub add_news {

&header;

print qq~
<CENTER>
<H3>Add Site News</H3>
<hr>
<FORM>
<CENTER>
  <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Caption:</TD>
      <TD width=100%><INPUT TYPE="text" NAME="title" SIZE="40"></TD>
    </TR>

    <TR>
      <TD>Date:</TD>
      <TD><script>DateInput('date', true, 'YYYY-MM-DD')</script></TD>
    </TR>

    <TR>
      <TD COLSPAN=2>Content:</TD>
    </TR>
    <TR>
      <TD COLSPAN=2>

<textarea id="ta" name="news" style="width:100%;height:100%" rows="24" cols="100">

</textarea>


      </TD>
    </TR>
    <TR>
      <TD COLSPAN=2><INPUT TYPE="hidden" NAME="addnewsfin" VALUE="NULL">
  <INPUT TYPE=submit VALUE="Add News"></TD>
    </TR>
  </TABLE>
</CENTER>
</FORM>
~;

&footer;

}

sub add_news_fin {


my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp="INSERT INTO `main_news` ( `id` , `name` , `content` , `date` ) VALUES ( NULL, '$INPUT{'title'}', '$INPUT{'news'}', '$INPUT{'date'}' );";

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish;
$dbh->disconnect;


&header;

print qq~
<CENTER>
<H3>News Added</H3>
<hR>
<TABLE border=1 CELLSPACING="1" width=75%>

<TR><TD><B>$INPUT{'title'}</B> $INPUT{'date'}</TD></TR>

<TR><TD>$INPUT{'news'}</TD></TR>
</TABLE>
~;

&footer;

}

sub menu {

print "Content-type: text/html\n\n";

print qq~
<HTML>

<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=iso-8859-1">
<TITLE>Menu</TITLE>

<STYLE>
  div    {
         position:absolute;
         }
</STYLE>

<script language="JavaScript" src="crossbrowser.js" type="text/javascript">
</script>
<script language="JavaScript" src="outlook.js" type="text/javascript">
</script>

<SCRIPT>

  //create OutlookBar
  var o = new createOutlookBar('Bar',0,0,screenSize.width,screenSize.height,'#606060','white')//'#000099') // OutlookBar
  var p

  //create first panel

  p = new createPanel('a','Main');
  p.addButton('home.gif','Welcome Page','parent.top.location="http://www.seekersofserenity.com/"');
  p.addButton('home.gif','Main Page','parent.top.location="http://www.seekersofserenity.com/index.pl"');
  p.addButton('home.gif','Admin Home','parent.main.location="./index.pl?main"');
  o.addPanel(p);

  p = new createPanel('al','News');
  p.addButton('news.gif','Add News','parent.main.location="./index.pl?addnews"');
  p.addButton('news.gif','Edit/Delete News','parent.main.location="./index.pl?editnews"');
  o.addPanel(p);
  
  p = new createPanel('p','Blocks');
  p.addButton('blocks.gif','Add<br>Left Blocks','parent.main.location="./index.pl?addleftblock"');
  p.addButton('blocks.gif','Edit/Delete<br>Left Blocks','parent.main.location="./index.pl?editleftblock"');
  p.addButton('blocks.gif','Add<br>Right Blocks','alert("Right Blocks. Coming.")');
  p.addButton('blocks.gif','Edit/Delete<br>Right Blocks','alert("Right Blocks. Coming.")');
  o.addPanel(p);

  p = new createPanel('l','HTML');
  p.addButton('html.gif','Add Page','alert("Edit Pages. Coming.")');
  p.addButton('html.gif','Edit/Delete<br>Page','alert("Edit Pages. Coming.")');
  p.addButton('html.gif','Edit<br>Main Layout','alert("Edit Site HTML. Coming.")');
  p.addButton('html.gif','Edit<br>Home Body','alert("Edit Site HTML. Coming.")');
  p.addButton('html.gif','Edit<br>Table','alert("Edit Site HTML. Coming.")');
  o.addPanel(p);


  o.draw();         //draw the OutlookBar


//resize OP5 (test screenSize every 100ms)
function resize_op5() {
  if (bt.op5) {
    o.showPanel(o.aktPanel);
    var s = new createPageSize();
    if ((screenSize.width!=s.width) || (screenSize.height!=s.height)) {
      screenSize=new createPageSize();
      //need setTimeout or resize on window-maximize will not work correct!
      //benötige das setTimeout oder das Maximieren funktioniert nicht richtig
      setTimeout("o.resize(0,0,screenSize.width,screenSize.height)",100);
    }
    setTimeout("resize_op5()",100);
  }
}

//resize IE & NS (onResize event!)
function myOnResize() {
  if (bt.ie4 || bt.ie5 || bt.ns5) {
    var s=new createPageSize();
    o.resize(0,0,s.width,s.height);
  }
  else
    if (bt.ns4) location.reload();
}

</SCRIPT>

</head>
<body onLoad="resize_op5();" onResize="myOnResize();">
</body>
</html>



~;


}

sub edit_news {
&header;

print qq~
<CENTER>
<H3>Edit/Delete News</H3>
<hR>
~;

my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp ="SELECT * FROM `main_news` ORDER BY `date` DESC";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) {

print qq~
<TABLE border=1 CELLSPACING="1" width=75%>

<TR>
<TD><B>$row[1]</B> ($row[3])</TD>
<TD ROWSPAN=2><CENTER>
<FORM>
  <INPUT TYPE="hidden" NAME="id" VALUE="$row[0]">
  <INPUT TYPE="hidden" NAME="editnewsb" VALUE="NULL">
  <INPUT TYPE=submit VALUE=" Edit ">
</FORM>
<BR>
<FORM>
  <INPUT TYPE="hidden" NAME="id" VALUE="$row[0]">
  <INPUT TYPE="hidden" NAME="deletenews" VALUE="NULL">
  <INPUT TYPE=submit VALUE="Delete">
</FORM>

</TD>
</TR>

<TR><TD>$row[2]</TD></TR>
</TABLE>
<p>
~;

 }


$sth->finish;
$dbh->disconnect;

&footer;
}

sub edit_news_b {
&header;

print qq~
<CENTER>
<H3>Edit News</H3>
<hR>

~;

my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp ="SELECT * FROM `main_news` WHERE `id` = $INPUT{'id'} LIMIT 1";

$sth=$dbh->prepare($temp);
$sth->execute;

 while(@row = $sth->fetchrow_array) {

print qq~

<FORM>
<CENTER>
  <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
      <TR>
      <TD>ID:</TD>
      <TD width=100%>$INPUT{'id'}<INPUT TYPE="hidden" NAME="id" VALUE="$INPUT{'id'}"></TD>
    </TR>
    <TR>
      <TD>Caption:</TD>
      <TD width=100%><INPUT TYPE="text" NAME="title" SIZE="40" VALUE="$row[1]"></TD>
    </TR>

    <TR>
      <TD>Date:</TD>
      <TD><script>DateInput('date', true, 'YYYY-MM-DD', '$row[3]')</script></TD>
    </TR>

    <TR>
      <TD COLSPAN=2>Content:</TD>
    </TR>
    <TR>
      <TD COLSPAN=2>

<textarea id="ta" name="news" style="width:100%;height:100%" rows="24" cols="100">
$row[2]
</textarea>


      </TD>
    </TR>
    <TR>
      <TD COLSPAN=2><INPUT TYPE="hidden" NAME="editnewsfin" VALUE="NULL">
	  <INPUT TYPE="hidden" NAME="id" VALUE="$INPUT{'id'}">
  <INPUT TYPE=submit VALUE="Edit News"></TD>
    </TR>
  </TABLE>
</CENTER>
</FORM>
<p>
~;

 }


$sth->finish;
$dbh->disconnect;

&footer;
}

sub edit_news_fin {

my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp="UPDATE `main_news` SET `name` = '$INPUT{'title'}', `content` = '$INPUT{'news'}', `date` = '$INPUT{'date'}' WHERE `id` = $INPUT{'id'} LIMIT 1";

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish;
$dbh->disconnect;


&header;

print qq~
<CENTER>
<H3>Edit News</H3>
<hR>
The news has been updated
~;

&footer;
}

sub delete_news {

my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp="DELETE FROM `main_news` WHERE `id` = $INPUT{'id'} LIMIT 1";

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish;
$dbh->disconnect;

&header;

print qq~
<CENTER>
<H3>Delete News</H3>
<hR>
The news has been deleted
~;

&footer;
}

sub add_left_block {

&header;

print qq~
<CENTER>
<H3>Add Left Block</H3>
<hr>
<FORM>
<CENTER>
  <TABLE BORDER=0 CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD>Caption:</TD>
      <TD width=100%><INPUT TYPE="text" NAME="title" SIZE="40"></TD>
    </TR>
    <TR>
      <TD COLSPAN=2>Content:</TD>
    </TR>
    <TR>
      <TD COLSPAN=2>

<textarea id="ta" name="cont" style="width:100%;height:100%" rows="24" cols="100">

</textarea>


      </TD>
    </TR>
    <TR>
      <TD COLSPAN=2><INPUT TYPE="hidden" NAME="addleftblockfin" VALUE="NULL">
  <INPUT TYPE=submit VALUE="Add Left Block"></TD>
    </TR>
  </TABLE>
</CENTER>
</FORM>
~;

&footer;
}

sub add_left_block_fin {
my $dbh = DBI->connect("DBI:mysql:$ms:$hostname",$username,$password)
or die "Can't connect to DBI: $dbh->errstr\n";

$temp="INSERT INTO `main_leftboxs` ( `id` , `name` , `content` ) VALUES ( NULL , '$INPUT{'title'}', '$INPUT{'cont'}' );";

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish;
$dbh->disconnect;


&header;

print qq~
<CENTER>
<H3>Left Block Added</H3>
<hR>
<TABLE border=1 CELLSPACING="1" width=75%>

<TR><TD><B>$INPUT{'title'}</B></TD></TR>

<TR><TD>$INPUT{'cont'}</TD></TR>
</TABLE>
~;

&footer;
}

sub edit_left_block {

}

sub edit_left_block_b {

}

sub edit_left_block_fin {

}

sub delete_left_block {

}

exit;