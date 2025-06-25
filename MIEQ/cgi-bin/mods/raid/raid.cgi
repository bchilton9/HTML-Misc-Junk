#!/usr/bin/perl

###############################################

$SCRIPTURL = "http://www.mieq.net/cgi-bin/mods/raid/raid.cgi";

###############################################

require "../../config.pl";

require "$sourcedir/subs.pl";


        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        if (length($buffer) < 5) {
                $buffer = $ENV{QUERY_STRING};
        }
        @pairs = split(/&/, $buffer);
        foreach $pair (@pairs) {
                ($name, $value) = split(/=/, $pair);

                $value =~ tr/+/ /;
                $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
                if ($name =~ /^multiple-/) {
                        $name =~ s/multiple-//;
                        push (@{$info{$name}}, $value);
                } else {
                        $input{$name} = $value;
                }
        }


getlanguage();
ban();
getcgi();
getdate();
logips();
loadcookie();
loaduser();
logvisitors();

if ($username eq $anonuser) { error("Not Loged in!"); }

if ($input{'action'} eq "startraid") { &startraid; }
elsif ($input{'action'} eq "searchitem") { &searchitem; }
elsif ($input{'action'} eq "makeraid") { &makeraid; }
else { &list; }


##################
sub list {
##################

$navbar = " $btn{'014'} Raid";
print_top();

print qq~<CENTER>
Existing raids:<BR>
<TABLE BORDER CELLPADDING="2">
  <TR>
    <TD>Date</TD>
    <TD>Target</TD>
    <TD>Zone</TD>
    <TD>&nbsp;&nbsp; &nbsp;</TD>
  </TR>
  ~;
open (DATA, "./data/raids.dat");
@data = <DATA>;
close DATA;
foreach $line (@data) {
chomp ($line);
($raidzone, $raidtarget, $raiddate, $raidnum) = split(/::/, $line);
print qq~
  <TR>
    <TD>$raiddate</TD>
    <TD>$raidtarget</TD>
    <TD>$raidzone</TD>
    <TD><A HERF="raid.cgi?action=startraid&raidnum=$raidnum">Manage</A></TD>
  </TR>
~;

}


print qq~
</TABLE>
<P>
 <FORM>
 Add a new raid:
   <TABLE BORDER CELLPADDING="2">
    <TR>
      <TD>Target:</TD>
      <TD>
        <INPUT TYPE="text" NAME="target"></TD>
    </TR>
    <TR>
      <TD>Zone:</TD>
      <TD>
        <select name="zone">
<option  valuea="236">Abysmal Sea</option>
<option valuea="334">Academy of Arcane Sciences</option>
<option>Acrylia Caverns</option>
<option valuea="54">Ak&#39;Anon</option>
<option valuea="152">Akheva Ruins</option>
<option valuea="333">Arcstone, Isle of Spirits</option>
<option valuea="240">Barindu, Hanging Gardens</option>
<option valuea="23">Befallen</option>
<option valuea="376">Befallen:  The Dead&#39;s Claim</option>

<option valuea="288">Befallen:  The Rise of Marnek</option>
<option valuea="37">Beholders Maze (Gorge of King Xorbb)</option>
<option valuea="18">BlackBurrow</option>
<option valuea="77">Burning Woods</option>
<option valuea="57">Butcherblock Mountains</option>
<option valuea="63">Castle Mistmoore</option>
<option valuea="268">Catacombs of Dranik</option>
<option valuea="323">Caverns of the Lost</option>
<option valuea="46">Cazic-Thule</option>

<option valuea="84">Charasis (Howling Stones)</option>
<option valuea="78">Chardok</option>
<option valuea="185">Chardok, Halls of Betrayal (Chardok B)</option>
<option valuea="259">Citadel of Anguish</option>
<option valuea="98">City of Mist</option>
<option valuea="27">Clan RunnyEye</option>
<option valuea="111">Cobalt Scar</option>
<option valuea="294">Corathus Creep</option>
<option valuea="311">Coven of the Skinwalkers</option>

<option valuea="59">Crushbone</option>
<option valuea="317">Crushbone (Instance)</option>
<option valuea="79">Crypt of Dalnir</option>
<option valuea="182">Crypt of Nadox</option>
<option valuea="101">Crystal Caverns</option>
<option valuea="61">Dagnor&#39;s Cauldron</option>
<option value="128">Dawnshroud Peaks</option>
<option valuea="349">Deathknell, Tower of Dissonance</option>

<option valuea="187">Deepest Guk</option>
<option valuea="168">Doomfire, the Burning Lands</option>
<option valuea="121">Dragon Necropolis</option>
<option valuea="269">Dranik&#39;s Hollows</option>
<option valuea="261">Dranik&#39;s Scar</option>
<option valuea="75">Dreadlands</option>
<option valuea="299">Dreadspire Keep</option>
<option valuea="310">Dreadspire, The Demi-Plane of Blood</option>

<option valuea="165">Drunder, Fortress of Zek (Plane of Tactics)</option>
<option valuea="180">Dulak&#39;s Harbor</option>
<option valuea="96">East Cabilis</option>
<option valuea="19">East Commonlands</option>
<option valuea="1">East Freeport</option>
<option valuea="41">East Karana</option>
<option valuea="110">Eastern Wastes</option>
<option valuea="355">Eastern Wastes:  Cage Kerafyrm</option>

<option valuea="150">Echo Caverns</option>
<option valuea="81">Emerald Jungle</option>
<option valuea="28">Erud&#39;s Crossing</option>
<option valuea="67">Erudin</option>
<option valuea="100">Erudin Palace</option>
<option valuea="175">Eryslai, the Kingdom of Wind</option>
<option valuea="16">Everfrost Peaks</option>
<option valuea="241">Ferubi, Forgotten Temple of Taelosia</option>

<option valuea="82">Field of Bone</option>
<option valuea="71">Firiona Vie</option>
<option valuea="351">Freeport Arena</option>
<option valuea="335">Freeport City Hall</option>
<option valuea="336">Freeport Militia House</option>
<option valuea="337">Freeport Sewers</option>
<option valuea="83">Frontier Mountains</option>
<option valuea="147">Fungus Grove</option>
<option valuea="113">Great Divide</option>

<option valuea="374">Great Divide:  Dain Frostreaver the First</option>
<option valuea="56">Greater Faydark</option>
<option valuea="139">Grieg&#39;s End</option>
<option valuea="136">Grimling Forest</option>
<option valuea="8">Grobb</option>
<option valuea="278">Guild Hall</option>
<option valuea="277">Guild Lobby</option>
<option valuea="179">Gulf of Gunthak</option>

<option valuea="11">Halas</option>
<option valuea="350">Hall of Truth</option>
<option valuea="171">Halls of Honor</option>
<option valuea="262">Harbingers&#39; Spire</option>
<option valuea="183">Hate&#39;s Fury</option>
<option valuea="289">Hate&#39;s Fury:  Setting Sail</option>
<option valuea="29">Highpass Hold</option>

<option valuea="30">Highpass Keep</option>
<option valuea="132">Hollowshade Moor</option>
<option valuea="105">Iceclad Ocean</option>
<option valuea="120">Icewell Keep</option>
<option valuea="248">Ikkinz, Chambers of Destruction</option>
<option valuea="361">Ikkinz: Trial of Glorification</option>
<option valuea="360">Ikkinz: Trial of Righteousness</option>
<option valuea="357">Ikkinz: Trial of Singular Might</option>
<option valuea="362">Ikkinz: Trial of Transcendence</option>

<option valuea="359">Ikkinz: Trial of Tri-Fates</option>
<option valuea="358">Ikkinz: Trial of Twin Struggles</option>
<option valuea="314">Illsalin Market</option>
<option valuea="253">Inktu&#39;ta, the Unmasked Chapel</option>
<option valuea="6">Innothule Swamp</option>
<option valuea="157">Jaggedpine Forest</option>
<option valuea="115">Kael Drakkel</option>
<option valuea="85">Kaesora</option>

<option valuea="365">Kaesora:  Zebuxoruk&#39;s Pact</option>
<option valuea="86">Karnor&#39;s Castle</option>
<option valuea="145">Katta Castellum</option>
<option valuea="64">Kedge Keep</option>
<option valuea="123">Kerafyrm&#39;s Lair (Sleeper&#39;s Tomb)</option>
<option valuea="66">Kerra Isle</option>
<option valuea="20">Kithicor Forest</option>

<option valuea="249">Kod&#39;Taz, Broken Trial Grounds</option>
<option valuea="87">Kurn&#39;s Tower</option>
<option valuea="177">Lair of Terris Thule</option>
<option valuea="353">Lair of the Creep Beast</option>
<option valuea="318">Lair of the Korlach</option>
<option valuea="38">Lake Rathetear</option>
<option valuea="73">Lake of Ill Omen</option>
<option valuea="280">Lavaspinner&#39;s Lair</option>

<option valuea="384">Lavaspinner&#39;s Lair:  Lavaspinner Hunting</option>
<option valuea="370">Lavaspinner&#39;s Lair:  Volkara&#39;s Bite</option>
<option valuea="31">Lavastorm Mountains</option>
<option valuea="60">Lesser Faydark</option>
<option valuea="319">Living Larder</option>
<option valuea="49">Lower Guk</option>
<option valuea="156">Marauder&#39;s Mire</option>

<option valuea="135">Marus Seru</option>
<option valuea="88">Mines of Nurga</option>
<option valuea="192">Miragul&#39;s Menagerie</option>
<option valuea="188">Mistmoore Catacombs</option>
<option valuea="332">Mistmoore Catacombs: Struggles within the Progeny</option>
<option valuea="388">Mistmoore Catacombs: The Asylum of Invoked Stone</option>
<option valuea="7">Misty Thicket</option>
<option valuea="273">Mob Graveyard</option>

<option valuea="134">Mons Letalis</option>
<option valuea="26">Mountains of Rathe</option>
<option valuea="263">Muramite Proving Grounds</option>
<option valuea="50">Nagafen&#39;s Lair (Solusek B)</option>
<option valuea="45">Najena</option>
<option valuea="237">Natimbi, The Broken Shores</option>
<option valuea="235">Nedaria&#39;s Landing</option>
<option valuea="15">Nektulos Forest</option>

<option valuea="364">Nektulos Forest:  Wanted Dead or Alive</option>
<option valuea="34">Neriak Commons</option>
<option valuea="33">Neriak Foreign Quarter</option>
<option valuea="35">Neriak Third Gate</option>
<option valuea="141">Netherbian Lair</option>
<option valuea="264">Nobles&#39; Causeway</option>
<option valuea="3">North Freeport</option>
<option valuea="53">North Kaladim</option>

<option valuea="32">North Karana</option>
<option valuea="4">North Qeynos</option>
<option valuea="285">North Qeynos:  Sleeping on the Job</option>
<option valuea="24">Northern Desert of Ro</option>
<option valuea="55">Northern Felwithe</option>
<option valuea="36">Oasis of Marr</option>
<option valuea="42">Ocean of Tears</option>
<option valuea="9">Oggok</option>
<option valuea="89">Old Sebilis</option>

<option valuea="69">Paineel</option>
<option valuea="148">Paludal Caverns</option>
<option valuea="47">Permafrost Keep</option>
<option valuea="163">Plane of Disease</option>
<option valuea="51">Plane of Fear</option>
<option valuea="103">Plane of Growth</option>
<option valuea="68">Plane of Hate</option>
<option valuea="287">Plane of Hate:  Innoruuk&#39;s Realm</option>

<option valuea="160">Plane of Innovation</option>
<option valuea="162">Plane of Justice</option>
<option valuea="158">Plane of Knowledge</option>
<option valuea="104">Plane of Mischief</option>
<option valuea="161">Plane of Nightmare</option>
<option valuea="70">Plane of Sky</option>
<option valuea="172">Plane of Storms</option>
<option valuea="272">Plane of Time A</option>
<option valuea="178">Plane of Time B</option>

<option valuea="167">Plane of Torment</option>
<option valuea="159">Plane of Tranquility</option>
<option valuea="170">Plane of Valor</option>
<option valuea="315">Prince&#39;s Manor</option>
<option valuea="324">Proving Grounds:  The Mastery of Adaptation</option>
<option valuea="325">Proving Grounds:  The Mastery of Corruption</option>
<option valuea="329">Proving Grounds:  The Mastery of Destruction</option>
<option valuea="330">Proving Grounds:  The Mastery of Efficiency</option>

<option valuea="326">Proving Grounds:  The Mastery of Endurance</option>
<option valuea="290">Proving Grounds:  The Mastery of Fear</option>
<option valuea="327">Proving Grounds:  The Mastery of Foresight</option>
<option valuea="291">Proving Grounds:  The Mastery of Hate</option>
<option valuea="331">Proving Grounds:  The Mastery of Ingenuity</option>
<option valuea="328">Proving Grounds:  The Mastery of Specialization</option>
<option valuea="293">Proving Grounds:  The Mastery of Subversion</option>
<option valuea="292">Proving Grounds:  The Mastery of Weaponry</option>
<option valuea="25">Qeynos Aqueducts</option>

<option valuea="17">Qeynos Hills</option>
<option valuea="239">Qinimi, Court of Nihilia</option>
<option valuea="312">Queen Sendaii`s Lair</option>
<option valuea="254">Qvic, Prayer Grounds of Calling</option>
<option valuea="184">Ragrax, Stronghold of the Twelve</option>
<option valuea="342">Razorthorn, Tower of Sullon Zek</option>
<option valuea="381">Razorthorn: Hero&#39;s Challenge</option>
<option valuea="382">Razorthorn: Samples of Corruption</option>

<option valuea="166">Reef of Coirnav</option>
<option valuea="343">Relic, the Artifact City</option>
<option valuea="265">Riftseekers&#39; Sanctum</option>
<option valuea="12">Rivervale</option>
<option valuea="238">Riwwi, Coliseum of Games</option>
<option valuea="298">Ruins of Illsalin</option>
<option valuea="174">Ruins of Lxanvom (Crypt of Decay)</option>
<option valuea="99">Ruins of Old Paineel (The Hole)</option>

<option valuea="345">Ruins of Takish-Hiz</option>
<option valuea="383">Ruins of Takish-Hiz: Message from the Past</option>
<option valuea="377">Ruins of Takish-Hiz: The Burning Prince</option>
<option valuea="191">Rujarkian Hills</option>
<option valuea="142">Sanctus Seru</option>
<option valuea="270">Sewers of Dranik</option>
<option valuea="243">Sewers of Nihilia, Lair of Trapped Ones</option>
<option valuea="244">Sewers of Nihilia, Pool of Sludge</option>
<option valuea="245">Sewers of Nihilia, Purifying Plant</option>

<option valuea="242">Sewers of Nihilia, the Crematory</option>
<option valuea="137">Shadeweaver&#39;s Thicket</option>
<option valuea="153">Shadow Haven</option>
<option valuea="305">Shadow Spine</option>
<option valuea="256">Shadowrest</option>
<option valuea="155">Shar Vahl</option>
<option valuea="122">Siren&#39;s Grotto</option>
<option valuea="91">Skyfire Mountains</option>

<option valuea="387">Skylance: Daosheen the Firstborn</option>
<option valuea="385">Skylance: The Laboratory</option>
<option valuea="344">Skylance: The Library</option>
<option valuea="386">Skylance: The Oubliette</option>
<option valuea="107">Skyshrine</option>
<option valuea="296">Snarlstone Dens</option>
<option valuea="378">Snarlstone Dens: Bloodeye</option>
<option valuea="48">Solusek&#39;s Eye (Solusek A)</option>

<option valuea="52">South Kaladim</option>
<option valuea="44">South Karana</option>
<option valuea="5">South Qeynos</option>
<option valuea="43">Southern Desert of Ro</option>
<option valuea="286">Southern Felwithe</option>
<option valuea="21">Splitpaw Lair</option>
<option valuea="302">Sporali Caverns</option>
<option valuea="140">Ssraeshza Temple</option>
<option valuea="58">Steamfont Mountains</option>

<option valuea="275">Stillmoon Temple</option>
<option valuea="363">Stillmoon Temple:  Best Laid Plans</option>
<option valuea="372">Stillmoon Temple:  Diseased Pumas</option>
<option valuea="125">Stonebrunt Mountains</option>
<option valuea="297">Stoneroot Falls</option>
<option valuea="307">Stoneroot Falls:  The City of Xill</option>
<option valuea="14">Surefall Glades</option>
<option valuea="341">Sverag, Stronghold of Rage</option>
<option valuea="74">Swamp of No Hope</option>

<option valuea="257">Tacvi, Seat of the Slaver</option>
<option valuea="189">Takish-Hiz</option>
<option valuea="92">Temple of Droga</option>
<option valuea="176">Temple of Marr</option>
<option valuea="10">Temple of Solusek Ro</option>
<option valuea="116">Temple of Veeshan</option>
<option valuea="301">Temple of the Korlach</option>
<option valuea="306">Temple of the Korlach:  The Council of Nine</option>
<option valuea="282">The Accursed Nest</option>

<option valuea="380">The Accursed Nest:  Circle of Drakes</option>
<option valuea="368">The Accursed Nest:  Dragon&#39;s Egg</option>
<option valuea="375">The Accursed Nest:  In the Shadows</option>
<option valuea="367">The Accursed Nest:  Spider&#39;s Eye</option>
<option valuea="354">The Accursed Nest:  The Curse of Ju`rek</option>
<option valuea="371">The Accursed Nest:  Web of Lies</option>
<option valuea="255">The Arena</option>
<option valuea="276">The Ascent</option>

<option valuea="154">The Bazaar</option>
<option valuea="260">The Bloodfields</option>
<option valuea="274">The Broodlands</option>
<option valuea="186">The Caverns of Exile (Solusek C)</option>
<option valuea="316">The Cocoons</option>
<option valuea="321">The Corathus Mines</option>
<option valuea="138">The Deep</option>
<option valuea="339">The Devastation</option>
<option valuea="340">The Elddar Forest</option>

<option valuea="284">The Estate of Unrest:  The Curse Begins</option>
<option valuea="13">The Feerrott</option>
<option valuea="258">The Forgotten Halls</option>
<option valuea="131">The Grey</option>
<option valuea="309">The Hatchery</option>
<option valuea="304">The Hive</option>
<option valuea="308">The Hive: The Lost Notebook</option>
<option valuea="303">The Lesser Faydark:  Brownies of Doom</option>
<option valuea="322">The Liberated Citadel of Runnyeye</option>

<option valuea="313">The Lodge of the Fang</option>
<option valuea="129">The Maiden&#39;s Eye</option>
<option valuea="271">The Mines of Gloomingdeep</option>
<option valuea="300">The Nargilor Pits</option>
<option valuea="379">The Nargilor Pits: Emperor Draygun</option>
<option valuea="151">The Nexus</option>
<option valuea="76">The Overthere</option>
<option valuea="373">The Root of Ro:  Lair of Suchun</option>

<option valuea="346">The Root of Ro: The Key to the Past</option>
<option valuea="266">The Ruined City of Dranik</option>
<option valuea="320">The Ruins of Old Guk</option>
<option valuea="127">The Scarlet Desert</option>
<option valuea="352">The Seething Wall</option>
<option valuea="130">The Tenebrous Mountains</option>
<option valuea="133">The Twilight Sea</option>
<option valuea="126">The Umbral Plains</option>
<option valuea="347">Theater of Blood</option>

<option valuea="338">Theater of Tranquility</option>
<option valuea="279">Thundercrest Isles</option>
<option valuea="356">Thundercrest Isles:  History of the Isle</option>
<option valuea="369">Thundercrest Isles:  Lair Unguarded</option>
<option valuea="366">Thundercrest Isles:  The Creator</option>
<option valuea="102">Thurgadin</option>
<option valuea="72">Timorous Deep</option>
<option valuea="247">Tipt, Treacherous Crags</option>
<option valuea="281">Tirranun&#39;s Delve</option>

<option valuea="173">Torden, the Bastion of Thunder</option>
<option valuea="181">Torgiran Mines</option>
<option valuea="117">Tower of Frozen Shadow</option>
<option valuea="164">Tower of Solusek Ro</option>
<option valuea="65">Toxxulia Forest</option>
<option valuea="90">Trakanon&#39;s Teeth</option>
<option valuea="348">Tunare&#39;s Shrine</option>
<option valuea="251">Txevu, Lair of the Elite</option>

<option valuea="295">Undershore</option>
<option valuea="62">Unrest</option>
<option valuea="39">Upper Guk</option>
<option valuea="252">Uqua, The Ocean God Chantry</option>
<option valuea="93">Veeshan&#39;s Peak</option>
<option valuea="169">Vegarlson, the Earthen Badlands</option>
<option valuea="94">Veksar</option>
<option valuea="109">Velketor&#39;s Labyrinth</option>

<option valuea="146">Vex Thal</option>
<option valuea="246">Vxed, The Crumbling Caverns</option>
<option valuea="119">Wakening Land</option>
<option valuea="267">Wall of Slaughter</option>
<option valuea="124">Warrens</option>
<option valuea="95">Warsliks Woods</option>
<option valuea="97">West Cabilis</option>
<option valuea="40">West Commonlands</option>
<option valuea="2">West Freeport</option>

<option valuea="22">West Karana</option>
<option valuea="108">Western Wastes</option>
<option valuea="250">Yxtta, Pulpit of Exiles</option>
</select>


        </TD>
    </TR>
    <TR>
      <TD>Date:</TD>
      <TD>
        <INPUT TYPE="text" NAME="date"></TD>
    </TR>

  </TABLE>

  <INPUT type="hidden" name="action" value="makeraid">
  <INPUT TYPE=submit Value="Create Raid">
</FORM>
~;

print_bottom();

}

##################
sub makeraid {
##################

open (FILE, "./data/raidcount.dat");
flock (FILE, 2);
$raidcount = <FILE>;
chop ($raidcount);
$junk = <FILE>;
chop ($junk);
flock (FILE, 8);
close(FILE);

$raidcount = $raidcount + 1;

open (FILE, ">./data/raidcount.dat");
print FILE "$raidcount\n";
print FILE "junk\n";
close(FILE);

open (DATA, "./data/raids.dat");
@data = <DATA>;
close DATA;

open(DATA, ">./data/raids.dat");
foreach $line (@data) {
print DATA "$line";
}
print DATA "$input{'zone'}::$input{'target'}::$input{'date'}::$raidcount\n";
close DATA;

open (FILE, ">./data/raids/$raidcount.dat");
print FILE "$input{'zone'}\n";
print FILE "$input{'target'}\n";
print FILE "$input{'date'}\n";
print FILE "junk\n";
close(FILE);

open (FILE, ">./data/raids/$raidcount.mem");
print FILE "";
close(FILE);

$navbar = " $btn{'014'} Raid";
print_top();

print qq~Raid Created!~;
print_bottom();
}

##################
sub startraid {
##################

 $navbar = " $btn{'014'} Raid";
print_top();

print qq~Manage Raid!~;

print_bottom();

}


##################
sub addmembers {
##################

           open(FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        chomp(@memberlist = <FILE>);
        unfile_lock(FILE);
        close(FILE);

print qq~
<P>
  Select Members Attending this raid:
  <TABLE BORDER CELLPADDING="2">
    <TR BGCOLOR=blue>
      <TD></TD>
      <TD><FONT COLOR=white>Member Name</TD>
    </TR>~;

foreach $member (@memberlist) {
                open(FILE, "$memberdir/$member.dat");
                file_lock(FILE);
                chomp(@members = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                $id++;
                $searchname = lc $members[1];
                $posts = $members[6]+$members[11]+$members[12];


                push (@allmembers, join ("\|", "$searchname|$members[1]|$members[2]|$members[10]|$members[17]|$rank|$memberinfo|$posts|$members[20]|$member|$members[21]\n"));
        }

        for (0..$#allmembers) {
                @fields = split(/\|/, $allmembers[$_]);
                for $i (0..$#fields) {
                        $data[$_][$i] = $fields[$i];
                }
        }


                @sorted = sort { $a->[0] cmp $b->[0] } @data;



        for (@sorted) {
                $sortedrow = join ("|", @$_);
                push (@sortedmembers, $sortedrow);
        }



#if (@allmembers == 0) { }

        for ($i = 0; $i < @sortedmembers; $i++) {

                ($dummy, $mname, $memail, $msince, $mlvl, $mrace, $mrank, $mposts, $mclass, $musername, $mrace) = split(/\|/, $sortedmembers[$i]);

if ($mname ne "Admin") {
print qq~
<TR>
      <TD>
        <INPUT TYPE="checkbox" NAME="$mname" VALUE="on"></TD>
        <TD>$mname</TD>
    </TR>~;

}
}

      print qq~
  </TABLE>
  <INPUT type="hidden" name="action" value="startraid">
  <INPUT TYPE=submit Value="Start Raid">
</FORM>
~;

}

##################
sub members {
##################
        open(FILE, "$memberdir/memberlist.dat");
        file_lock(FILE);
        chomp(@memberlist = <FILE>);
        unfile_lock(FILE);
        close(FILE);

$navbar = " $btn{'014'} Raid";
print_top();

print qq~
 <FORM><CENTER>

   <TABLE BORDER CELLPADDING="2">
    <TR>
      <TD>Target Mob:</TD>
      <TD></TD>
    </TR>
    <TR>
      <TD>Zone:</TD>
      <TD></TD>
    </TR>
    <TR>
      <TD>Date:</TD>
      <TD></TD>
    </TR>
     <TR>
      <TD>Raid #:</TD>
      <TD></TD>
    </TR>
  </TABLE>
   <P>
  <TABLE BORDER CELLPADDING="2">
    <TR>
      <TD>Search Item:</TD>
      <TD>
        <INPUT TYPE="text" NAME="search"></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
      <INPUT type="hidden" name="action" value="searchitem">
        <INPUT TYPE=submit VALUE="Search"></TD>
    </TR>
  </TABLE>
 <P>

 Names blocked in red will not be added into the loot selecting do<BR>
 to that theay have not set there race and class and the system will<BR>
 not know if theay can use it or not.<BR>


  <TABLE BORDER=1 CELLPADDING="1" cellspaceing=2>
    <TR BGCOLOR=blue>
      <TD><FONT COLOR=white>Name</TD>
      <TD><FONT COLOR=white>Level</TD>
      <TD><FONT COLOR=white>Race</TD>
      <TD><FONT COLOR=white>Class</TD>
      <TD><FONT COLOR=white>Raids Attended</TD>
      <TD><FONT COLOR=white>Loots Awarded</TD>
    </TR>~;

foreach $member (@memberlist) {
                open(FILE, "$memberdir/$member.dat");
                file_lock(FILE);
                chomp(@members = <FILE>);
                unfile_lock(FILE);
                close(FILE);

                $id++;
                $searchname = lc $members[1];
                $posts = $members[6]+$members[11]+$members[12];


                push (@allmembers, join ("\|", "$searchname|$members[1]|$members[2]|$members[10]|$members[17]|$rank|$memberinfo|$posts|$members[20]|$member|$members[21]\n"));
        }

        for (0..$#allmembers) {
                @fields = split(/\|/, $allmembers[$_]);
                for $i (0..$#fields) {
                        $data[$_][$i] = $fields[$i];
                }
        }


                @sorted = sort { $a->[0] cmp $b->[0] } @data;



        for (@sorted) {
                $sortedrow = join ("|", @$_);
                push (@sortedmembers, $sortedrow);
        }



        for ($i = 0; $i < @sortedmembers; $i++) {

                ($dummy, $mname, $memail, $msince, $mlvl, $mrace, $mrank, $mposts, $mclass, $musername, $mrace) = split(/\|/, $sortedmembers[$i]);

$cause = "";
if ($input{$mname} eq "on") {
if ($mlvl eq "") { $cause = "BGCOLOR=RED"; }
if ($mrace eq "") { $cause = "BGCOLOR=RED"; }
if ($mclass eq "") { $cause = "BGCOLOR=RED"; }


print qq~
<TR $cause>
      <TD>$mname<INPUT type=hidden name=$mname value="on"></TD>
      <TD>$mlvl</TD>
      <TD>$mrace</TD>
      <TD>$mclass</TD>
      <TD>0</TD>
      <TD>0</TD>

</TR>~;
}

}


      print qq~
  </TABLE>
  </FORM>

~;


print_bottom();


}


######################
sub searchitem {
######################

$navbar = " $btn{'014'} Raid";
print_top();

print qq~
Search Resaults,<BR>
<TABLE BORDER CELLPADDING="2">
  <TR>
    <TD>Item Name(Lucy Link)</TD>
    <TD>Ranking</TD>
    <TD>Award Item</TD>
  </TR>~;

open (DATA, "itemlist.txt");
@data = <DATA>;
close DATA;

foreach $line (@data) {
chomp ($line);
($eqnum, $eqname, $lucylink) = split(/\,/, $line);

$eqname =~ s/\"//g;
         #$_[0] =~ /$term/i

if ($eqname =~ /$input{'search'}/i) {
print qq~

  <TR>
    <TD><A HREF="$lucylink" Target="_new">$eqname</A><BR></TD>
    <TD>No Ranks Yet</TD>
    <TD>Award Button</TD>
  </TR>~;
}
}
print qq~</TABLE>~;
print_bottom();

}