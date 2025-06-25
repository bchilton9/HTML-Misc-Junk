#!/usr/bin/perl -w

# ENV 1.0
# Designed by Aaron Anderson
# Sulfericid@qwest.net
# http://spyderscripts.netfirms.com
#
# It is required by law this header information
# remains in it's original form.
#
# Please refer to the readme file for installation
# help.
#

use CGI;

my $query = CGI->new;

print $query->header;

print <<"EOF";

<font size="2">

<table width="75%" border="0">
  <tr>
   <td colspan="2" bgcolor="#CCCCCC"><B><font color=blue>This is a list of the important variables from your site.  Blank returns are unretrievable by your server.</font></b></td>
</tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Server Software:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SERVER_SOFTWARE}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Gateway Interface:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{GATEWAY_INTERFACE}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">HTTP UserAgent:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{HTTP_USER_AGENT}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Server Protocol:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SERVER_PROTOCOL}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Document Root:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{DOCUMENT_ROOT}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Remote Address:</td>
    <td width="80%" bgcolor="#CCCCCC">REMOTE_ADDR</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Request Method:</td>
    <td width="80%" bgcolor="#CCCCCC">REQUEST_METHOD</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Query String</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{QUERY_STRING}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">HTTP Accept:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{HTTP_ACCEPT}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Remote Port:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{REMOTE_PORT}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Server Address:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SERVER_ADDR}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">HTTP Language:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{HTTP_ACCEPT_LANGUAGE}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Unique ID:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{REDIRECT_UNIQUE_ID}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">HTTP Encoding:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{HTTP_ACCEPT_ENCODING}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Redirect Status:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{REDIRECT_STATUS}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Script Name:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SCRIPT_FILENAME}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Server Name:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SERVER_NAME}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Server Port:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SERVER_PORT}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Path Translated:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{PATH_TRANSLATED}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Server Admin:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SERVER_ADMIN}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Unique ID:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{UNIQUE_ID}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Redirect URL:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{REDIRECT_URL}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Script URI:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SCRIPT_URI}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Script URL:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SCRIPT_URL}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Server Signature:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SERVER_SIGNATURE}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Path:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{PATH}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">HTTP Connection:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{HTTP_CONNECTION}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Redirect Script URI:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{REDIRECT_SCRIPT_URI}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Script Name:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{SCRIPT_NAME}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Redirect Script URL:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{REDIRECT_SCRIPT_URL}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">Path Info:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{PATH_INFO}</td>
  </tr>
  <tr>
    <td width="20%" bgcolor="#CCCCCC">HTTP Host:</td>
    <td width="80%" bgcolor="#CCCCCC">$ENV{HTTP_HOST}</td>
  </tr>
  <tr>
    <td colspan="2" bgcolor="#CCCCCC"><center><font color="blue">Script Designed by <a href="mailto://sulfericacid\@qwest.net">Aaron Anderson</a>.</font></center></td>
</tr>
</table>
</body>
</html>
</font>

EOF
;

