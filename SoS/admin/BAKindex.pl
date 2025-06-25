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

<body onload="initEditor()">
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
<FRAMESET COLS="14%,86%">
  <FRAME SRC="./index.pl?menu" NAME="Menu" SCROLLING="No" NORESIZE>
  <FRAME SRC="./index.pl?main" NAME="Action">
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
<h3>SoS Main Page Admin.</H3>
<HR>
Items not yet functional are in red <BR>
<BR>
Add News<BR>
<FONT COLOR="#ff0000">Edit News<BR>
<FONT COLOR="#ff0000">Delete News<BR>
<BR>
<FONT COLOR="#ff0000">Left Blocks<BR>
<FONT COLOR="#ff0000">RightBlocks<BR>
<BR>
<FONT COLOR="#ff0000">Edit Site html
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

$temp="INSERT INTO `main_news` ( `name` , `content` , `date` ) VALUES ( '$INPUT{'title'}', '$INPUT{'news'}', '$INPUT{'date'}' );";

$sth=$dbh->prepare($temp);

$sth->execute;

$sth->finish;
$dbh->disconnect;


&header;

print qq~
<CENTER>
<H3>News Added</H3>
<hR>
<TABLE border=1 width=50%>

<TR><TD><B>$INPUT{'title'}</B> $INPUT{'date'}</TD></TR>

<TR><TD>$INPUT{'news'}</TD></TR>
</TABLE>
~;

&footer;

}

sub menu {

&header;

print qq~
<TABLE BORDER=0 width=100% CELLPADDING="2">
  <TR>
    <TD><B>News</B></TD>
  </TR>
  <TR>
    <TD><A HREF="./index.pl?addnews" TARGET="Action">Add News</A><BR>
      <A HREF="./index.pl?main" TARGET="Action">Edit News</A><BR>
      <A HREF="./index.pl?main" TARGET="Action">Delete News</A>
      <P><BR>
    </TD>
  </TR>
  <TR>
    <TD><B>Blocks</B></TD>
  </TR>
  <TR>
    <TD><A HREF="./index.pl?main" TARGET="Action">Left Blocks</A><BR>
      <A HREF="./index.pl?main" TARGET="Action">RightBlocks</A>
      <P><BR>
    </TD>
  </TR>
  <TR>
    <TD><B>Html</B></TD>
  </TR>
  <TR>
    <TD><A HREF="./index.pl?main" TARGET="Action">Edit Site Html</A></TD>
  </TR>
</TABLE>
~;
&footer;

}

exit;