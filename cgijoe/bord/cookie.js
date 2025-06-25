<!--

/* Do not remove me unless you don't want the username cookie to work on each individual message file. */

function getCookie(name) {
	var cookie = " " + document.cookie;
	var search = " " + name + "=";
	var setStr = null;
	var offset = 0;
	var end = 0;
	if (cookie.length > 0) {
		offset = cookie.indexOf(search);
		if (offset != -1) {
			offset += search.length;
			end = cookie.indexOf(";", offset)
			if (end == -1) {
				end = cookie.length;
			}
			setStr = unescape(cookie.substring(offset, end));
		}
	}
	return(setStr);
}
var myVar2 = "";
var myVar3 = "";
var displaycount = 0;
var myVar = getCookie("MBuser");
if (myVar) {
var mySearch = myVar.indexOf("|");
myVar2 = myVar.substring(0,mySearch);
myVar3 = myVar.substring(mySearch+1,myVar.length);
}
function fill_fields(e) {
if (document.all) {
if (event && displaycount==0) {

if (document.REPLYFORM.name.value=="") {
document.REPLYFORM.name.value=myVar2;
}
if (document.REPLYFORM.email.value=="") {
document.REPLYFORM.email.value=myVar3;
}

displaycount++;
}
}
if (document.layers) {
if (e && displaycount==0) {
if (document.REPLYFORM.name.value=="") {
document.REPLYFORM.name.value=myVar2;
}
if (document.REPLYFORM.email.value=="") {
document.REPLYFORM.email.value=myVar3;
}

displaycount++;
}
}
}
if (document.layers) {
document.captureEvents(Event.MOUSEDOWN);
}

document.onmousedown=fill_fields;


//-->