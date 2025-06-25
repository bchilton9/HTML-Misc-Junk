#!/usr/bin/perl -w
###############################################################################
# WebApp ShowHTML Mod - showhtml.pl
#
# Mod created by Ted Loomos (tloomos@devdesk.com)
#  Get the latest updates from the CMS Project Area on www.web-app.org
#
# LEGAL DISCLAIMER:
# This software is provided as-is.  Use it at your own risk.  The
# author takes no responsibility for any damages or losses directly
# or indirectly caused by this software.
#
# Version History
# 0.0.1 - 06/14/2002 - Initial script created
# 0.0.2	- 07/27/2002 - Added CGI pull support
# 0.0.3 - 09/22/2002 - Added IFRAME Support
# 0.0.4 - 10/22/2002 - Removed LWP::Simple & URI::URL dependencies.
# 0.0.5 - 01/05/2003 - Added admin module to handle preset content configuration
# 0.0.6 - 01/06/2003 - Bug fixes - static files not working and prevent directory traversals
#
# To Do:
###############################################################################
$| = 1;
use CGI::Carp qw(fatalsToBrowser);

eval {
##--------------------------------------------------------------
## If you are not using standard folder locations, the following
## lines may need to be changed to match your installation
##--------------------------------------------------------------
 	require "../../config.pl";
	$modDir           = "$scriptdir/mods/showhtml";
	$showHTMLDatafile = "$modDir/data/links.dat";
	$cssFile          = "$modDir/iframe.css";
	$defaultHTMLDir   = "$modDir/html";
	$defaultProtocol  = "http";
##--------------------------------------------------------------
## Nothing below this point should require modification
##--------------------------------------------------------------
 	require "$lang";
 	require "$sourcedir/subs.pl";

	if ($IIS != 2) {
		if ($IIS == 0) {
			if ($ENV{'SERVER_SOFTWARE'} =~ m!IIS!) { $IIS = 1; }
		}
		if (($IIS) && ($0 =~ m!(.*)(\\|\/)!)) { chdir($1); }
		if ($IIS == 1) { print "HTTP/1.0 200 OK\n"; }
	}
};
 if ($@) {
 	print "Content-type: text/html\n\n";
 	print qq~<h1>Software Error:</h1>
 Execution of <b>$scriptname</b> has been aborted due a compilation error:<br>
 <pre>$@</pre>
 <p>If this problem persits, please contact the webmaster and inform him about date and time you've recieved this error.</p>
 ~;
 	exit;
}

getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

require "$themesdir/$usertheme/theme.pl";
getvars();

############################
# Get data from GET & POST #
############################
&parse_form;

my $linkID    = $input{'id'};
my $filename  = $input{'filename'};
my $url       = $input{'url'};

my $title     = "";
my $html      = "Invalid Action.";

if ($linkID) {
	##---------------------------------------------------------------------------------
	## Read the predefined links database
	##---------------------------------------------------------------------------------
	open (DATAFILE,"<$showHTMLDatafile") || &error("Unable to open $showHTMLDatafile");
	@links = <DATAFILE>;
	close (DATAFILE);

	##--------------------------------------------------------------
	## Search for the link identified by the id that was passed in
	##--------------------------------------------------------------
	LINKITEM: foreach $rec (@links) {
		chomp($rec);
		($lid,$type,$source,$protocol,$height,$width,$scrolling,$path)=split(/\|/,$rec);
		if ($lid eq $linkID) {

			if ($type eq "filename") {
				if (!$path) {$path = $defaultHTMLDir;}

				$filename = "$path/$source";
				$html = ShowStaticHTMLFile($filename);

			} else {
				if (!$protocol) {$protocol = $defaultProtocol;}
				$html = ShowDynamicContent($source, $protocol, $height, $width, $scrolling);
			}

			last LINKITEM;
		}
	}

}
elsif ($filename) {
    if ($filename =~ /(\$+|\|+|\(+|\)+|\[+|\]+|\{+|\}+|\^+|\*+|\.+|\<)/) {
	    print_top();
	    print "What are you doing Stan?";
	    print_bottom();
	    exit;
	}
	$html = ShowStaticHTMLFile("$defaultHTMLDir/$filename");
} elsif ($url) {
	$html = ShowDynamicContent($url, $defaultProtocol,"","","");
}

# ----------- print everything to the browser ---
if ($title) {$navbar = "&nbsp;$btn{'014'}&nbsp; $title";}
print_top();

print $html;

print_bottom();


##-------------------------------------------------------------------------------------
## Show a static HTML file that is located somewhere on the same server as this script.
##-------------------------------------------------------------------------------------
sub ShowStaticHTMLFile {
	my ($filename) = @_;
	my $html = "";

	if (-e "$filename") {
	 	open (HTMLFILE, "$filename") || &error("Unable to open $filename");

	 	$html = "";
	 	while (<HTMLFILE>) 	{
	 		$html .= $_;
	 	}
	 	close HTMLFILE;

	 	$title =~ s/.*<title.*?>//i;
		$title =~ s/<\/title>.*//i;
	 	$html  =~ s/.*<body.*?>//i;
		$html  =~ s/<\/body>.*//i;

	} else {
		$html = "HTML File '$filename' Not Found.";
	}

	return $html;
}

##-------------------------------------------------------------------------------------
## Show a content that is pulled from a URL
##-------------------------------------------------------------------------------------
sub ShowDynamicContent {
	my ($url, $protocol, $height, $width, $scrolling) = @_;
	my ($html, $query, $key, $val, $fullurl) = "";

	($url,$query)=split(/\?/,$url);
	if ($query) {$query = "?$query";}

	while (($key, $val) = each %input) {
		if ($key ne "url" && $key ne "id") {
			if ($query) {$query.="&"} else {$query="?"}
			$query .= "$key=$val";
		}
	}

	$fullurl="$protocol://$url$query";

	$html = "<STYLE TYPE='text/css'><!--";

	#tried to use @import url(...) but culdn't get it to work.
 	open (CSSFILE, "$cssFile") || &error("Unable to open $cssFile");
 	while (<CSSFILE>) 	{
 		$html .= $_;
 	}
 	close CSSFILE;

 	$html .= "--></STYLE><IFRAME frameborder=0 style=\"height:$height;width:$width;scrolling:$scrolling;\" class=iframe name=cwindow src='$fullurl' ></IFRAME>";

 	return $html;
}
###################################################################
# Subroutine 'error' prints a simple HTML page for the user when an
# error has occurred.  The subroutine displays the input message for
# the user and goes back so that the user can try again
#

sub error{
        my($parm)=@_;

        $userid = 0;

        # Script prints error message and waits for the specified time
        # before going back to the data entry screen.  The time is
        # specified in milliseconds (5000 = 5 sec)
        #
        print_top;

        print qq^

		<p>&nbsp;</p>
                <center>

		<table border=1 cellspacing="0" cellpadding="3"
		width="400" bordercolor="#95A5E5">
		<tr><td align="left" bgcolor="#95A5E5"><font
		face="verdana" size="2"><b>ê Error</b></font>
		</td></tr>
		<tr><td class="grey">
		<p>&nbsp;</p>
        	<p><b>Error:</b></p>

                <p><B>$parm</B></p>

                <p>Please wait for the form to re-load.</p>
                <p>If the previous page does not start to load in 10
		seconds, press the 'back' button.
                </font>
		<p>&nbsp;</p>
		</td></tr></table>


                <script>
                setTimeout("history.back()",10000)
                </script>
		<p>&nbsp;</p>


        ^; # End print statement

        print_bottom;

        exit;

} # End subroutine error


########################################
# Code to get the data from GET & POST #
########################################
sub parse_form {

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
   @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $input{$name} = $value;
   }
}

1;
