###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# upload.pl                                                   		      #
# v0.9.9 - Requin                                                             #
#                                                                             #
# Copyright (C) 2002 by WebAPP (webapp@attbi.com)                             #
#                                                                             #
# This program is free software; you can redistribute it and/or               #
# modify it under the terms of the GNU General Public License                 #
# as published by the Free Software Foundation; either version 2              #
# of the License, or (at your option) any later version.                      #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program; if not, write to the Free Software                 #
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA. #
#                                                                             #
#                                                                             #
# File: Last modified: 11/05/02                                               #
###############################################################################
###############################################################################


#################
sub uploadpicture {
#################

print "Content-type: text/html\n\n";

print qq~
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<title>$msg{'598'}</title>
</head>
<body>
<center>
<font face="Arial" size="2">$msg{'598'}</font>
<p>
<form action="$scripturl/admin/upload.cgi" method="post" enctype="multipart/form-data"> 
<input type="File" name="FILE1">
<p>
<input type="Submit" value="submit">
</center>
</form> 
</body>
</html>
~;

exit;


}

#############
sub success {
#############

print "Content-type: text/html\n\n";

$thefile = $info{'yourfile'};

print qq~
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<title>Success</title>
<script language="javascript" type="text/javascript">
<!--
function addCode(anystr) { 
opener.document.creator.message.value+=anystr;
}
// -->
</script>
</head>
<body>
<center>
<font face="Arial" size="2">$msg{'599'}</font>
<br>
$msg{'600'} $thefile $msg{'601'}<br><br>
Your image can be located at:<BR>
<A HREF=$uploadurl/$thefile>$uploadurl/$thefile</A><BR><BR>

<a href="javascript:addCode('[img]~. $uploadurl .qq~/~. $thefile .qq~[/img]')">$msg{'602'}</a><br><br>
<a href="javascript:window.close()">$msg{'603'}</a>
</center>
</form> 
</body>
</html>
~;

exit;

}


#############
sub failure {
#############

print "Content-type: text/html\n\n";

$thefile = $info{'yourfile'};


print qq~
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<title>$msg{'604'}!</title>
</head>
<body>
<center>
<font face="Arial" size="2">$msg{'604'}!</font>
<br>
$thefile - $msg{'604'}<br><br>
<a href="javascript:window.close()">$msg{'603'}</a>
</center>
</form> 
</body>
</html>
~;

exit;

}


1;