<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html dir="ltr">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="Content-Style-Type" content="text/css">
<meta name="keywords" content="Europa, Guild, Everquet, Druzzil, Druzzil Ro, Dro, Stormhammer, Raid, Raiding, EQ">
<meta name="description" content="Welcome to Europa, an Everquest Raiding Guild on Druzzil-Ro">
<meta name="author" content="Europa.">


<title>Europa, An Everquest Guild on Druzzil-Ro :: Europa - Application Form</title>
<script language="JavaScript">
<!--

function SymError()
{
  return true;
}

window.onerror = SymError;

var SymRealWinOpen = window.open;

function SymWinOpen(url, name, attributes)
{
  return (new Object());
}

window.open = SymWinOpen;

//-->
</script>

<script language="Javascript" type="text/javascript">
<!--
	if ( 0 )
	{
		window.open('privmsg.php?mode=newpm', '_phpbbprivmsg', 'HEIGHT=225,resizable=yes,WIDTH=400');;
	}
//-->
</script>
</head>
<body bgcolor="#E5E5E5" text="#000000" link="#006699" vlink="#5493B4">

<a name="top"></a>
<br />



	<script language="javascript" type="text/javascript">
		function isnum (string)
		{
			if (string.length == 0)
				return false;
			for (var i=0;i < string.length;i++)
				if ((string.substring(i,i+1) < '0') || (string.substring(i,i+1) > '9'))
					return false;

			return true
		}
		function makedata (name, value)
		{
			var data = ""
			data += "[b]" + name + "[/b]: " + value + "\n";
			return data;
		}
		function emailCheck (emailStr)
		{
			var checkTLD=0;
			var knownDomsPat=/^(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum)$/;

			var emailPat=/^(.+)@(.+)$/;
			var specialChars="\\(\\)><@,;:\\\\\\\"\\.\\[\\]";
			var validChars="\[^\\s" + specialChars + "\]";
			var quotedUser="(\"[^\"]*\")";
			var ipDomainPat=/^\[(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\]$/;
			var atom=validChars + '+';
			var word="(" + atom + "|" + quotedUser + ")";
			var userPat=new RegExp("^" + word + "(\\." + word + ")*$");
			var domainPat=new RegExp("^" + atom + "(\\." + atom +")*$");
			var matchArray=emailStr.match(emailPat);

			if (matchArray==null) {
				return false;
			}
			var user=matchArray[1];
			var domain=matchArray[2];

			for (i=0; i<user.length; i++) {
				if (user.charCodeAt(i)>127) {
					return false;
				}
			}
			for (i=0; i<domain.length; i++) {
				if (domain.charCodeAt(i)>127) {
					return false;
				}
			}

			// See if "user" is valid

			if (user.match(userPat)==null) {
				return false;
			}

			var IPArray=domain.match(ipDomainPat);
			if (IPArray!=null) {
				for (var i=1;i<=4;i++) {
					if (IPArray[i]>255) {
						return false;
					}
				}
				return true;
			}

			var atomPat=new RegExp("^" + atom + "$");
			var domArr=domain.split(".");
			var len=domArr.length;
			for (i=0;i<len;i++) {
				if (domArr[i].search(atomPat)==-1) {
					return false;
				}
			}

			if (checkTLD && domArr[domArr.length-1].length!=2 &&
				domArr[domArr.length-1].search(knownDomsPat)==-1) {
				return false;
			}

			// Make sure there's a host name preceding the domain.

			if (len<2) {
				return false;
			}
			return true;
		}

		function validate_form()
		{
			var message = "";
			var subject = "";
			var char_name = document.post.char_name.value;
			var tclass = document.post.tclass.value;
			var race = document.post.race.value;
			var email = document.post.email.value;
			var magelo = document.post.magelo.value;
			var aa = document.post.aa.value;
			var ep = document.post.ep.checked;
			var poeb = document.post.poeb.checked;
			var fennin = document.post.fennin.checked;
			var xegony = document.post.xegony.checked;
			var coirnav = document.post.coirnav.checked;
			var trc = document.post.trc.checked;
			var kt = document.post.kt.checked;
			var ikki = document.post.ikki.checked;
			var uqua = document.post.uqua.checked;
			var inktu = document.post.inktu.checked;
			var txevu = document.post.txevu.checked;
			var coa = document.post.coa.checked;
			var dreadspire = document.post.dreadspire.checked;
			var demiplane = document.post.demiplane.checked;
			var tob = document.post.tob.checked;
			var deathkneel = document.post.deathkneel.checked;
			var play_time = document.post.play_time.value;
			var played = document.post.played.value;
			var born = document.post.born.value;
			var instaclick = document.post.instaclick.value;
			var country = document.post.country.value;
			var age = document.post.age.value;
			var prev_guilds = document.post.prev_guilds.value;
			var prev_servers = document.post.prev_servers.value;
			var connection = document.post.connection.value;
			var history = document.post.history.value;
			var why = document.post.why.value;
			var comments = document.post.comments.value;
			var you_funny = document.post.you_funny.value;
			var movie = document.post.movie.value;
			var food = document.post.food.value;

			if(char_name.length < 2) {
				alert("Must enter valid Char Name");
				return false;
			}
			if(!emailCheck(email)) {
				alert("Must enter valid Email Address\nPlease note, your email address will not be published to the public");
				return false;
			}
			if(magelo.length < 5) {
				alert("Must enter valid Magelo link");
				return false;
			}

			urlcheck = /^.*www\.magelo\.com.*$/i;
			if(!urlcheck.test(magelo)) {
				if(isnum(magelo)) {
					magelo = 'http://www.magelo.com/eq_view_profile.html?num=' + magelo;
				} else {
					alert("Must enter valid Magelo link");
					return false;
				}
			}

			if(aa.length < 1) {
				alert("Must enter valid AA count");
				return false;
			}
			if(!isnum(aa)) {
				alert("Must enter valid AA count");
				return false;
			}
			if(aa < 150) {
				alert("AA number of [" + aa + "] is too low, please get more AA before applying to Europa");
				return false;
			}
			if(instaclick.length < 2) {
				alert("Must enter valid Instaclick item");
				return false;
			}
			if(country.length < 2) {
				alert("Must enter valid Home Country");
				return false;
			}
			if(!isnum(age)) {
				alert("Must enter valid Age");
				return false;
			}
			if(age.length < 2) {
				alert("Must enter valid Age");
				return false;
			}
			if(age < 18) {
				alert("Age of [" + age + "] is too low, we are not childcare");
				return false;
			}
			if(connection.length < 2) {
				alert("Must enter connection type and speed");
				return false;
			}
			if(history.length < 30) {
				alert("Must enter more then 30 chars EQ history, must be alot more that you want to tell us!");
				return false;
			}
			if(why.length < 30) {
				alert("Must enter more then 30 characters long reason of why you want to join Eruopa!");
				return false;
			}
			if(you_funny.length < 30) {
				alert("Must enter more then 30 chars for a Joke, come on, show us your sense of humor!");
				return false;
			}
			if(movie.length < 1) {
				alert("Come on.. tell us your favorite movie!! even if it's porn!");
				return false;
			}
			if(food.length < 1) {
				alert("Come on.. tell us what u like to eat!!");
				return false;
			}
			message = '';
			subject = "Application: " + char_name + " - " + tclass;
			//message += '[b]' + subject + '[/b]';
			message += makedata("Application", char_name + " - " + tclass);
			message += makedata("Char Name", char_name);
			message += makedata("Class", tclass);
			message += makedata("Race", race);
			message += makedata("Email", "[Hidden]");
			message += makedata("Magelo", "[url=" + magelo + "]" + magelo + "[/url]");
			message += makedata("Total AA", aa);
			var flags = "";
			if(ep) flags += "Elemental, ";
			if(poeb) flags += "PoEB, ";
			if(fennin) flags += "Feninn, ";
			if(xegony) flags += "Xegony, ";
			if(coirnav) flags += "Coirnav, ";
			if(trc) flags += "The Rathe Conucil, ";
			if(kt) flags += "Kod`Taz, ";
			if(ikki) flags += "Ikkniz 4, ";
			if(uqua) flags += "Uqua, ";
			if(inktu) flags += "Inktu'ta, ";
			if(txevu) flags += "Txevu, ";
			if(coa) flags += "Anguish, ";
			if(dreadspire) flags += "Dreadspire, ";
			if(demiplane) flags += "Demiplane of Blood, ";
			if(tob) flags += "Theatre of Blood, ";
			if(deathkneel) flags += "Deathkneel, ";
			flags = flags.substring(0, flags.length - 2);
			message += makedata("Keys / Flags", flags);
			message += makedata("Play Time", play_time);
			message += makedata("Played", played);
			message += makedata("Creation Date", born);
			message += makedata("Instaclick Item", instaclick);
			message += makedata("Home Country", country);
			message += makedata("Age", age);
			message += makedata("Previous Guilds", prev_guilds);
			message += makedata("Previous Servers", prev_servers);
			message += makedata("Connection Type", connection);
			message += makedata("EQ History", history);
			message += makedata("Why Europa", why);
			message += makedata("Funny Say", you_funny);
			message += makedata("Favorite Movie", movie);
			message += makedata("Favorite Food", food);
			message += makedata("Comments", comments);

			document.post.message.value = message;
			document.post.subject.value = subject;
			return true;
		}
	</script>

	<form action="file:///C|/Documents and Settings/SysOp/Desktop/posting.php" method="post" name="post" onSubmit="return validate_form()">
		<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline">
			<tr>
				<th colspan="2">	Europa - Application Form
				</th>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Character Name:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="char_name" size="30" maxlength="30" style="width:120px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Class:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<select class="post" name="tclass" size=1>
						<option value="Bard" selected>Bard
						<option value="Beastlord">Beastlord
						<option value="Berserker">Berserker
						<option value="Cleric">Cleric
						<option value="Druid">Druid
						<option value="Enchanter">Enchanter
						<option value="Magician">Magician
						<option value="Monk">Monk
						<option value="Necromancer">Necromancer
						<option value="Paladin">Paladin
						<option value="Ranger">Ranger
						<option value="Rogue">Rogue
						<option value="Shadowknight">Shadowknight
						<option value="Shaman">Shaman
						<option value="Warrior">Warrior
						<option value="Wizard">Wizard</option>
					</select>
				</td>
			</tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Race:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<select class="post" name="race" size=1>
						<option value="Barbarian" selected>Barbarian
						<option value="Dark Elf">Dark Elf
						<option value="Dwarf">Dwarf
						<option value="Erudite">Erudite
						<option value="Froglok">Froglok
						<option value="Gnome">Gnome
						<option value="Half-Elf">Half-Elf
						<option value="Halfling">Halfling
						<option value="High Elf">High Elf
						<option value="Human">Human
						<option value="Iksar">Iksar
						<option value="Ogre">Ogre
						<option value="Troll">Troll
						<option value="Vah Shir">Vah Shir
						<option value="Wood Elf">Wood Elf</option>
					</select>
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Email Address:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="email" size="30" maxlength="30" style="width:220px" tabindex="2" class="post" value=""> (only recruitment officers will be able to view it)
				</td>
			</tr>

			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Magelo:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="magelo" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Total AA:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="aa" size="4" maxlength="4" style="width:40px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Keys / Flags:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<table>
						<tr>
							<td><input type="Checkbox" name="ep">Elemental</td>
							<td><input type="Checkbox" name="poeb">PoEB</td>
							<td><input type="Checkbox" name="fennin">Fennin Ro</td>
							<td><input type="Checkbox" name="xegony">Xegony</td>
							<td><input type="Checkbox" name="coirnav">Coirnav</td>
							<td><input type="Checkbox" name="trc">Rathe Council</td>
						</tr>
						<tr>
							<td><input type="Checkbox" name="kt">Kod`Taz</td>
							<td><input type="Checkbox" name="ikki">Ikkinz 4</td>
							<td><input type="Checkbox" name="uqua">Uqua</td>
							<td><input type="Checkbox" name="inktu">Inktu`ta</td>
							<td><input type="Checkbox" name="txevu">Txevu</td>
							<td></td>
						</tr>
						<tr>
							<td><input type="Checkbox" name="coa">Anguish</td>
							<td><input type="Checkbox" name="dreadspire">Dreadspire</td>
							<td><input type="Checkbox" name="demiplane">Demiplane of Blood</td>
							<td><input type="Checkbox" name="tob">Theatre of Blood</td>
							<td><input type="Checkbox" name="deathkneel">Deathkneel</td>
							<td></td>
						</tr>
					</table>
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Play Time:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="play_time" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value=""><br>
					How many days a week, which days, in which hours and timezone?
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Played time:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="played" size="45" maxlength="60" style="width:100px" tabindex="2" class="post" value="">
					<br>How many total days on your toon? - do /played in game to find out.
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Creation Date:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="born" size="45" maxlength="60" style="width:100px" tabindex="2" class="post" value="">
					<br>When was your toon created?
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Instacast Right Click items:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="instaclick" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Home Country:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="country" size="45" maxlength="60" style="width:120px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Age:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="age" size="45" maxlength="60" style="width:30px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Previous guilds:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="prev_guilds" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Previous servers:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="prev_servers" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">PC connection:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="connection" size="45" maxlength="60" style="width:200px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">EQ History:</span></td>
				<td class="row2" width="78%" valign="top">
					<textarea name="history" cols="60" rows="10" style="width:450px" tabindex="2" class="post" value=""></textarea>
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Why Europa?:</span></td>
				<td class="row2" width="78%" valign="top">
					<textarea name="why" cols="60" rows="10" style="width:450px" tabindex="2" class="post" value=""></textarea>
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">What is your favorite joke, phrase, or words of wisdom?:</span></td>
				<td class="row2" width="78%" valign="top">
					<textarea name="you_funny" cols="60" rows="10" style="width:450px" tabindex="2" class="post" value=""></textarea>
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Favorite Movie:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="movie" size="45" maxlength="160" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Favorite Food:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="food" size="45" maxlength="160" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Comments / Adds:</span></td>
				<td class="row2" width="78%" valign="top">
					<textarea name="comments" cols="60" rows="10" style="width:450px" tabindex="2" class="post" value=""></textarea>
				</td>
			</tr>
			<tr>
				<td class="cat" colspan="2" align="center" height="28"><input type="submit" value="Submit and Pray" name="post" class="mainoption"></td>
			</tr>

		</table>
		<br>
		<input type="hidden" name="subject" value="">
		<input type="hidden" name="addbbcode18" value="%23">
		<input type="hidden" name="addbbcode20" value="12">
		<input type="hidden" name="helpbox" value="Font+color%3A+%5Bcolor%3Dred%5Dtext%5B%2Fcolor%5D++Tip%3A+you+can+also+use+color%3D%23FF0000">
		<input type="hidden" name="message" value="">
		<input type="hidden" name="attach_sig" value="on">
		<input type="hidden" name="topictype" value="0">
		<input type="hidden" name="poll_title" value="">
		<input type="hidden" name="add_poll_option_text" value="">
		<input type="hidden" name="poll_length" value="">
		<input type="hidden" name="mode" value="newtopic">
		<input type="hidden" name="f" value="3">
		<input type="hidden" name="post" value="submit">

	</form>


<div align="center"><span class="copyright"><br /><br />
<!--
	We request you retain the full copyright notice below including the link to www.phpbb.com.
	This not only gives respect to the large amount of time given freely by the developers
	but also helps build interest, traffic and use of phpBB 2.0. If you cannot (for good
	reason) retain the full copyright we request you at least leave in place the
	Powered by phpBB line, with phpBB linked to www.phpbb.com. If you refuse
	to include even this then support on our forums may be affected.

	The phpBB Group : 2002
// -->
Powered by <a href="http://www.phpbb.com/" target="_phpbb" class="copyright">phpBB</a> &copy; 2001, 2005 phpBB Group<br /></span></div>
		</td>
	</tr>
</table>

</body>
</html>


<script language="JavaScript">
<!--
var SymRealOnLoad;
var SymRealOnUnload;

function SymOnUnload()
{
  window.open = SymWinOpen;
  if(SymRealOnUnload != null)
     SymRealOnUnload();
}

function SymOnLoad()
{
  if(SymRealOnLoad != null)
     SymRealOnLoad();
  window.open = SymRealWinOpen;
  SymRealOnUnload = window.onunload;
  window.onunload = SymOnUnload;
}

SymRealOnLoad = window.onload;
window.onload = SymOnLoad;

//-->
</script>

