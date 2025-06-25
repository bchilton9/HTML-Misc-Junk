<HTML>
<HEAD>
<script language="JavaScript1.2">

//Contents for menu 1
var menu1=new Array()
menu1[0]='<a href=page.cgi?page=alchemy target=nwindow>Alchemy</a><br>'
menu1[1]='<a href=page.cgi?page=bakeing target=nwindow>Baking</a><br>'
menu1[2]='<a href=page.cgi?page=brewing target=nwindow>Brewing</a><br>'
menu1[3]='<a href=page.cgi?page=fletching target=nwindow>Fletching</a><br>'
menu1[4]='<a href=page.cgi?page=jewelcraft target=nwindow>Jewelcraft</a><br>'
menu1[5]='<a href=page.cgi?page=poisons target=nwindow>Poisons</a><br>'
menu1[6]='<a href=page.cgi?page=pottery target=nwindow>Pottery</a><br>'
menu1[7]='<a href=page.cgi?page=smithing target=nwindow>Smithing</a><br>'
menu1[8]='<a href=page.cgi?page=tailoring target=nwindow>Tailoring</a><br>'
menu1[9]='<a href=page.cgi?page=tinkering target=nwindow>Tinkering</a><br>'
menu1[10]='<a href=page.cgi?page=tips target=nwindow>Tips and Tricks</a><br>'
//Contents for menu 2
var menu2=new Array()
menu2[0]='Coming<br>'
menu2[1]='Soon!<br>'
</script>

<style>
<!--
.wrap1{
position:relative;
}
.wrap2{
position:absolute;
}
#dropmenu0, #dropmenu1{
z-index:100;
}
-->
</style>


</HEAD>
<BODY>
<script language="JavaScript1.2">
//reusable/////////////////////////////

//Drop down menu by http://www.dynamicdrive.com

var zindex=100
var ns4=document.layers
var ns6=document.getElementById&&!document.all
var ie4=document.all
var opr=navigator.userAgent.indexOf("Opera")

function dropit(e,whichone){
curmenuID=ns6? document.getElementById(whichone).id : eval(whichone).id
if (window.themenu&&themenu.id!=curmenuID)
themenuStyle.visibility=ns4?"hide" : "hidden"

themenu=ns6? document.getElementById(whichone): eval(whichone)
themenuStyle=(ns6||ie4)? themenu.style : themenu

themenuoffsetX=(ie4&&opr==-1)? document.body.scrollLeft : 0
themenuoffsetY=(ie4&&opr==-1)? document.body.scrollTop : 0

themenuStyle.left=ns6||ns4? e.pageX-e.layerX : themenuoffsetX+event.clientX-event.offsetX
themenuStyle.top=ns6||ns4? e.pageY-e.layerY+19 : themenuoffsetY+event.clientY-event.offsetY+18

hiddenconst=(ns6||ie4)? "hidden" : "hide"
if (themenuStyle.visibility==hiddenconst){
themenuStyle.visibility=(ns6||ie4)? "visible" : "show"
themenuStyle.zIndex=zindex++
}
else
hidemenu()
return false
}

function hidemenu(){
if ((ie4||ns6)&&window.themenu)
themenuStyle.visibility="hidden"
else if (ns4)
themenu.visibility="hide"
}

if (ie4||ns6)
document.onclick=hidemenu

//reusable/////////////////////////////
</script>
<TABLE BORDER="0" CELLPADDING="2">
  <TR>
    <TD width=100>
<!----------Menu 1 starts here---------->

<ilayer>
<layer visibility=show>
<div class=wrap1>
<span class=wrap2 onClick="dropit(event, 'dropmenu0');event.cancelBubble=true;return false"><font face=Verdana><b><a href="alternate.htm" onClick="if(ns4) return dropit(event, 'document.dropmenu0')">TradeSkills</a></b></font>
</span>
</div>
</layer>
</ilayer><BR>
<!----------Menu 1 ends here---------->
</TD>
    <TD width=100>
<!----------Menu 2 starts here---------->

<ilayer>
<layer visibility=show>
<div class=wrap1>
<span class=wrap2 onClick="dropit(event, 'dropmenu1');event.cancelBubble=true;return false"><font face=Verdana><b><a href="alternate.htm" onClick="if(ns4) return dropit(event, 'document.dropmenu1')">PowerLvling</a></b></font>
</span>
</div>
</layer>
</ilayer><BR>
<!----------Menu 2 ends here---------->
</TD>
  </TR>
</TABLE>
  <HR>

<Center>
	<iframe name="nwindow" style="border:0px" width=700 height=420 src="page.cgi?page=main"
	frameborder="0"></iframe>

<div id=dropmenu0 style="position:absolute;left:0;top:0;layer-background-color:lightyellow;background-color:lightyellow;width:120;visibility:hidden;border:1px solid black;padding:0px">
<script language="JavaScript1.2">
if (document.all)
dropmenu0.style.padding="4px"
for (i=0;i<menu1.length;i++)
document.write(menu1[i])
</script>
</div>
<script language="JavaScript1.2">
if (document.layers){
document.dropmenu0.captureEvents(Event.CLICK)
document.dropmenu0.onclick=hidemenu
}
</script>

<div id=dropmenu1 style="position:absolute;left:0;top:0;layer-background-color:lightyellow;background-color:lightyellow;width:120;visibility:hidden;border:1px solid black;padding:0px">
<script language="JavaScript1.2">
if (document.all)
dropmenu1.style.padding="4px"
for (i=0;i<menu2.length;i++)
document.write(menu2[i])
</script>
</div>
<script language="JavaScript1.2">
if (document.layers){
document.dropmenu1.captureEvents(Event.CLICK)
document.dropmenu1.onclick=hidemenu
}
</script>


</BODY></HTML>
