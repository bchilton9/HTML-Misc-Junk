#!/usr/bin/perl
#######################################################

#######################################################

# This script requires SSI.
# To run this script put the following line into the body of your html page.
# <!--#exec cgi="/path/to/bsmidi_ssi.cgi"-->
# This script should work in both IE and Netscape.

#########################
# DECLARE THE VARIABLES #
#########################

$datafile = "playlist.txt";
 # Location of the playlist file.
 # An example is included in the zip file.

$mididir = "http://d0tt.erenetwork.com/midi";
 # Midi Directory (Don't include the slash at the end of the url)

$width = "145";
 # The width of the control box.

$height = "45";
 # The height of the control box.

#$hidden = "false";

$autostart = "true";
 # Have the midis automatically play (true=yes, false=no)

$loop = "true";
 # Have the song repeat (true=yes, false=no)

$showtitle = "true";
 # Show song title. (true=yes, false=no)

$fntstyle = "Arial";
 # Title Font Style.

$fntsize = "-1";
 # Title Font Size.

$fntbold = "true";
 # Is Title Bold? (true=bold, false=plain)

#####################################################
# There is no need to edit anything below this line #
#####################################################

open (GETDATA, "$datafile");
@Data = <GETDATA>;
close GETDATA;

srand(time ^ $$);
$number = rand(@Data);
$line = @Data[$number];

chomp ($line);
($midi, $title) = split(/:/, $line);

print "Content-type: text/html\n\n";

if ($showtitle =~ /true/i)
{
	print "<font size=\"$fntsize\" face=\"$fntstyle\">";
	if ($fntbold =~ /true/i) {print "<strong>";}
	print "Now Playing \- $title";
	if ($fntbold =~ /true/i) {print "</strong>";}
	print "</font><br>\n";
}

print "<embed src=\"$mididir/$midi\" width=\"$width\" height=\"$height\" autostart=\"$autostart\" loop=\"$loop\">\n";

exit (0);
