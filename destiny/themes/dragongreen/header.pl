###############################################################################
###############################################################################
# header.pl - prints the middle/top of each page                              #
# v0.9.7                                                                      #
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
# Last modified: 07/24/02                                           		#
###############################################################################
###############################################################################

print "Content-type: text/html\n\n"; 
print qq~<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"> 
     
<html> 
 
<head> 

<SCRIPT language="JavaScript1.2" src="http://www.sanctuaryeq2.com/main.js"type="text/javascript"></SCRIPT>

  <SCRIPT LANGUAGE="JavaScript">
<!-- Begin
function NewWindow(mypage, myname, w, h, scroll) {
var winl = (screen.width - w) / 2;
var wint = (screen.height - h) / 2;
winprops = 'height='+h+',width='+w+',top='+wint+',left='+winl+',scrollbars='+scroll+',resizable'
win = window.open(mypage, myname, winprops)
if (parseInt(navigator.appVersion) >= 4) { win.window.focus(); }
}
//  End -->
</SCRIPT>

<script>

function submitonce(theform){
//if IE 4+ or NS 6+
if (document.all||document.getElementById){
//screen thru every element in the form, and hunt down "submit" and "reset"
for (i=0;i<theform.length;i++){
var tempobj=theform.elements[i]
if(tempobj.type.toLowerCase()=="submit"||tempobj.type.toLowerCase()=="reset")
//disable em
tempobj.disabled=true
}
}
}


</script>

<SCRIPT LANGUAGE="JavaScript">
function killEntry(entry) { if (window.confirm("Are you sure you want to Delete this Member completly?")) 
{ window.location.href = "" + entry + "" } }
  </Script>

<meta http-equiv="expires" content="0">  
<meta name="Generator" content="$scriptname $scriptver"> 
<title>$pagetitle</title> 
<link rel="stylesheet" href="$themesurl/$usertheme/style.css" type="text/css"> 
~;
 
################### Admin Broadcast Message ##############
 
broadcastmessage();
 
print qq~ 
 
</head> 
<BODY>
<DIV id="TipLayer" style="visibility:hidden;position:absolute;z-index:1000;top:-100"></DIV>
<SCRIPT language="JavaScript1.2" src="http://www.sanctuaryeq2.com/style.js" type="text/javascript"></SCRIPT>
~;

logo_block();

print qq~

<div align="center">  
  <table class="pagetable"> 
    <tr>  
      <td height="21">~;  
menu_bar(); 
      print qq~</td> 
    </tr> 
  </table> 
</div> ~;

# code to see if we need to show the banner or not.
###########################################################################
checkforbanner();


	print qq~

<div align="center">

<table class="pagetable">
<tr>
<td valign="top" width="150">
<table width="150">
~;

main_menu();

left_top_plugins();

mysite_block();

status_block();

left_bottom_plugins();

search_block();

leftblock_block();

print qq~
</td>
</tr>
</table>
</td>
<td valign="top" width="100%">
<table width="100%">
<tr>
<td width="100%">
~;
nav_bar();

1; # return true


