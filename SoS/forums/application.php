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
			var level = document.post.level.value;
			var tclass = document.post.tclass.value;
			var race = document.post.race.value;
			var magelo = document.post.magelo.value;
			var poj = document.post.poj.checked;
			var pon = document.post.pon.checked;
			var pod = document.post.pod.checked;
			var poi = document.post.poi.checked;
			var pov = document.post.pov.checked;
			var pos = document.post.pos.checked;
			var cod = document.post.cod.checked;
			var potac = document.post.potac.checked;
			var hoh = document.post.hoh.checked;
			var bot = document.post.bot.checked;
			var potor = document.post.potor.checked;
			var srt = document.post.srt.checked;
			var poe = document.post.poe.checked;
			var poa = document.post.poa.checked;
			var powa = document.post.powa.checked;
			var pof = document.post.pof.checked;
			var time = document.post.time.checked;
			var zero = document.post.zero.checked;
			var ones = document.post.ones.checked;
			var onec = document.post.onec.checked;
			var pre15s = document.post.pre15s.checked;
			var pre15c = document.post.pre15c.checked;
			var one5 = document.post.one5.checked;
			var one5s = document.post.one5s.checked;
			var one5c = document.post.one5c.checked;
			var two = document.post.two.checked;
			var twos = document.post.twos.checked;
			var twoc = document.post.twoc.checked;
			var prev_guilds = document.post.prev_guilds.value;
			var why = document.post.why.value;
			var email = document.post.email.value;
			var country = document.post.country.value;
			var play_time = document.post.play_time.value;
			var age = document.post.age.value;
			var recruiter = document.post.recruiter.value;
			var comments = document.post.comments.value;

			if(char_name.length < 2) {
				alert("Must enter valid Char Name");
				return false;
			}
			if(level.length < 1) {
				alert("Must enter valid level");
				return false;
			}
			if(!isnum(level)) {
				alert("Must enter valid level");
				return false;
			}
			if(level < 46) {
				alert("Your level [" + level + "] is below our minimum for recruitment");
				return false;
			}
			if(!emailCheck(email)) {
				alert("Must enter valid Email Address\nPlease note, your email address will not be published to the public");
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
			if(age.length < 1) {
				alert("Must enter valid Age");
				return false;
			}
			if(why.length < 30) {
				alert("Must enter more then 30 characters long reason of why you want to join Eruopa!");
				return false;
			}
			message = '';
			subject = "Application: " + char_name + " - " + tclass;
			//message += '[b]' + subject + '[/b]';
			message += makedata("Application", char_name + " - " + tclass);
			message += makedata("Char Name", char_name);
			message += makedata("Level", level);
			message += makedata("Class", tclass);
			message += makedata("Race", race);
			message += makedata("Magelo", "[url=" + magelo + "]" + magelo + "[/url]");
			var flags = "";
			if(poj) flags += "Justice, ";
			if(pon) flags += "Nightmare, ";
			if(pod) flags += "Disease, ";
			if(poi) flags += "Innovation, ";
			if(pov) flags += "Valor, ";
			if(pos) flags += "Storms, ";
			if(cod) flags += "Decay, ";
			if(potac) flags += "Tactics, ";
			if(hoh) flags += "Honor, ";
			if(bot) flags += "Thunder, ";
			if(potor) flags += "Torment, ";
			if(srt) flags += "Solusek Ro' Tower, ";
			if(poe) flags += "Earth, ";
			if(poa) flags += "Air, ";
			if(powa) flags += "Fire, ";
			if(pof) flags += "Water, ";
			if(time) flags += "Time, ";
			flags = flags.substring(0, flags.length - 2);
			message += makedata("Keys / Flags", flags);
			var epic = "";
			if(zero) epic += "Epic quests not started, ";
			if(ones) epic += "Started Epic 1.0, ";
			if(onec) epic += "Currently has Epic 1.0, ";
			if(pre15s) epic += "Epic 1.5/2.0 prequest started, ";
			if(pre15c) epic += "Epic 1.5/2.0 prequest complete, ";
			if(one5) epic += "Has not started Epic 1.5 quest, ";
			if(one5s) epic += "Has started Epic 1.5 quest, ";
			if(one5c) epic += "Currently has Epic 1.5, ";
			if(two) epic += "Has not started Epic 2.0 quest, ";
			if(twos) epic += "Has started Epic 2.0 quest, ";
			if(twoc) epic += "Currently has Epic 2.0, ";
			epic = epic.substring(0, epic.length - 2);
			message += makedata("Epic", epic);
			message += makedata("Previous Guilds", prev_guilds);
			message += makedata("Why Us", why);
			message += makedata("Email", email);
			message += makedata("Home Country", country);
			message += makedata("Play Time", play_time);
			message += makedata("Age", age);
			message += makedata("Recruited By", recruiter);
			message += makedata("Comments", comments);
			
			document.post.message.value = message;
			document.post.subject.value = subject;
			return true;
		}
	</script>

	<form action="posting.php" method="post" name="post" onSubmit="return validate_form()">
		<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline">
			<tr>
				<th colspan="2">	Seekers of Serenity - Application Form
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
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Level:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="level" size="4" maxlength="4" style="width:40px" tabindex="2" class="post" value="">
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
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Magelo:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="magelo" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Keys / Flags Completed:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<table>
						<tr>
							<td><input type="Checkbox" name="poj">Plane of Justice</td>
							<td><input type="Checkbox" name="pov">Plane of Valor</td>
							<td><input type="Checkbox" name="hoh">Halls of Honor</td>
							<td><input type="Checkbox" name="poe">Plane of Earth</td>
							<td><input type="Checkbox" name="time">Plane of Time</td>
						</tr>
						<tr>
							<td><input type="Checkbox" name="pon">Plane of Nightmare</td>
							<td><input type="Checkbox" name="pos">Plane of Storms</td>
							<td><input type="Checkbox" name="bot">Bastion of Thunder</td>
							<td><input type="Checkbox" name="poa">Plane of Air</td>
							<td></td>
						</tr>
						<tr>
							<td><input type="Checkbox" name="pod">Plane of Disease</td>
							<td><input type="Checkbox" name="cod">Crypt of Decay</td>
							<td><input type="Checkbox" name="potor">Plane of Torment</td>
							<td><input type="Checkbox" name="powa">Plane of Water</td>
							<td></td>
						</tr>
						<tr>
							<td><input type="Checkbox" name="poi">Plane of Innovation</td>
							<td><input type="Checkbox" name="potac">Plane of Tactics</td>
							<td><input type="Checkbox" name="srt">Solusek Ro's Tower</td>
							<td><input type="Checkbox" name="pof">Plane of Fire</td>
							<td></td>
						</tr>
					</table>
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Epic Status:</span>
				</td>
				<td class="row2" width="78%" valign="top">
					<table>
						<tr>
							<td><input type="Checkbox" name="zero">Not Started</td>
							<td><input type="Checkbox" name="ones">1.0 Started</td>
							<td><input type="Checkbox" name="onec">1.0 Attained</td>
						</tr>
						<tr>
							<td></td>
							<td><input type="Checkbox" name="pre15s">1.5 Prequest Started</td>
							<td><input type="Checkbox" name="pre15c">1.5 Prequest Complete</td>
						</tr>
						<tr>
							<td><input type="Checkbox" name="one5">1.5 Not Started</td>
							<td><input type="Checkbox" name="one5s">1.5 Started</td>
							<td><input type="Checkbox" name="one5c">1.5 Attained</td>
						</tr>
						<tr>
							<td><input type="Checkbox" name="two">2.0 Not Started</td>
							<td><input type="Checkbox" name="twos">2.0 Started</td>
							<td><input type="Checkbox" name="twoc">2.0 Attained</td>
						</tr>
					</table>
				</td>
			</tr>			
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Previous Guilds:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="prev_guilds" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Why Seekers of Serenity?:</span></td>
				<td class="row2" width="78%" valign="top">
					<textarea name="why" cols="60" rows="10" style="width:450px" tabindex="2" class="post" value=""></textarea>
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
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Home Country & Timezone:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="country" size="45" maxlength="60" style="width:120px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Play Time:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="play_time" size="45" maxlength="60" style="width:450px" tabindex="2" class="post" value=""><br>
					How many days a week, which days, and what hours?
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Age:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="age" size="45" maxlength="60" style="width:30px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Recruited By:</span></td>
				<td class="row2" width="78%" valign="top">
					<input type="text" name="recruiter" size="45" maxlength="60" style="width:120px" tabindex="2" class="post" value="">
				</td>
			</tr>
			<tr>
				<td width="22%" valign="top" align="right" class="row1"><span class="explaintitle">Comments / Adds:</span></td>
				<td class="row2" width="78%" valign="top">
					<textarea name="comments" cols="60" rows="10" style="width:450px" tabindex="2" class="post" value=""></textarea>
				</td>
			</tr>
			<tr>
				<td class="cat" colspan="2" align="center" height="28"><input type="submit" value="Submit Application" name="post" class="mainoption"></td>
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