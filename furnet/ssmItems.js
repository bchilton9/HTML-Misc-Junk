<!--

/*
Configure menu styles below
NOTE: To edit the link colors, go to the STYLE tags and edit the ssm2Items colors
*/
YOffset=127; // no quotes!!
XOffset=0;
staticYOffset=30; // no quotes!!
slideSpeed=20 // no quotes!!
waitTime=100; // no quotes!! this sets the time the menu stays out for after the mouse goes off it.

menuBGColor="white";
menuIsStatic="no"; //this sets whether menu should stay static on the screen
menuWidth=169; // Must be a multiple of 10! no quotes!!
menuCols=2;

hdrFontFamily="verdana";
hdrFontSize="2";
hdrFontColor="#0B00EC";
hdrBGColor="white";
hdrAlign="center";
hdrVAlign="bottom";
hdrHeight="15";

linkFontFamily="Verdana";
linkFontSize="2";
linkBGColor="white";
linkOverBGColor="#80FFFF";
linkTarget="_top";
linkAlign="Left";

barBGColor="white";
barFontFamily="Verdana";
barFontSize="2";
barFontColor="white";
barVAlign="top";

barWidth=64; // no quotes!!
barText="<IMG SRC=menu.gif>"; // <IMG> tag supported. Put exact html for an image to show.

///////////////////////////

// ssmItems[...]=[name, link, target, colspan, endrow?] - leave 'link' and 'target' blank to make a header
ssmItems[0]=["Menu"] //create header
ssmItems[1]=["MailSys", "http://www.erenetwork.com/mailsys", "_new"]
ssmItems[2]=["Furcadian Edge", "http://www.furcadianedge.com", "_new"]
ssmItems[3]=["Email Us", "mailto:webmaster@furres.net"]

ssmItems[4]=["Furcadia's Top Sites"]
ssmItems[5]=["Main", "http://www.erenetwork.com/furctopsite", "_new"]
ssmItems[6]=["Join", "http://www.erenetwork.com/furctopsite/cgi-bin/lspro.cgi?request=new", "_new"]

ssmItems[7]=["Furcadian Index"]
ssmItems[8]=["Main", "http://www.erenetwork.com/furnet/furres/index.html", "cwindow"]
ssmItems[9]=["Add Link", "http://www.erenetwork.com/furnet/furres/cgi-bin/add.cgi", "cwindow"]
ssmItems[10]=["Edit Link", "http://www.erenetwork.com/furnet/furres/cgi-bin/modify.cgi", "cwindow"]
ssmItems[11]=["Search", "http://www.erenetwork.com/furnet/furres/cgi-bin/search.cgi", "cwindow"]

ssmItems[12]=["Furcadian Banner Exchange"]
ssmItems[13]=["Add/Edit", "http://www.erenetwork.com/furnet/be/ads_admin.pl", "cwindow"]

ssmItems[14]=[""] //create header
ssmItems[15]=[""] //create header

buildMenu();

//-->