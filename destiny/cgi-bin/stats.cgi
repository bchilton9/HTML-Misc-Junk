#!/usr/bin/perl

$url = "http://eq2players.station.sony.com/en/guild.vm?guildId=432113";

use CGI qw(param);
use LWP::Simple;

$page = get($url);

print "Content-type: text/html\n\n";

print qq~
<HTML><HEAD><link rel=stylesheet href=http://www.destinyeq2.com/themes/roster.css type=text/css></HEAD><BODY>
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">

<TR><TD></TD><TD></TD></TR>

~;


$page =~ /<span class="field_name_small">Created:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Created:</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Creation Rank:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Creation Rank:</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Members:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Members:</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Average Level:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Average Level:</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Items Discovered (Worldwide):<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Items Discovered (Worldwide):</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Items Discovered (Server):<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Items Discovered (Server):</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Kills vs Deaths Ratio:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Kills vs Deaths Ratio:</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Kills vs Deaths Ratio Rank:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Kills vs Deaths Ratio Rank:</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Guild Level:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Guild Level:</B></TD><TD>$1</TD></TR>";


$page =~ /<span class="field_name_small">Status:<\/span> <span class="field_data_small">(.*?)<\/span><br>/i;
print "<TR><TD><P ALIGN=Right><B>Status:</B></TD><TD>$1</TD></TR>";


print qq~
  </TABLE>
</CENTER>
<P>
<P>
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center" WIDTH="100%">
    <TR>
      <TD><CENTER><TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
~;



$page =~ s/ //gi;
$page =~ s/	//gi;



$page =~ /<ahref="guild_wof.vm\?guildId=195113&rank=itemDiscGuildRank&type=MostServerFirstDiscoveries"class="field_name_small">MostItemDiscoveries:<\/a>\n<\/td>\n<tdclass="field_data_small"valign="top">\n<ahref="pplayer.vm\?characterId=(.*?)"class="field_data_small">(.*?)<\/a>/i;
print "<TR><TD><P ALIGN=Right><B>Most Item Discoveries:</B></TD><TD>$2</TD></TR>";


$page =~ /<ahref="guild_wof.vm\?guildId=195113&rank=itemDiscGfirstRankGuild&type=MostGameFirstDiscoveries"class="field_name_small">MostItemDiscoveries\(Game-Wide\):<\/a>\n<\/td>\n<tdclass="field_data_small"valign="top">\n<ahref="pplayer.vm\?characterId=(.*?)"class="field_data_small">(.*?)<\/a>/i;
print "<TR><TD><P ALIGN=Right><B>Most Item Discoveries (Game-Wide):</B></TD><TD>$2</TD></TR>";



$page =~ /<ahref="guild_wof.vm\?guildId=195113&rank=npcKillsRankGuild&type=MostNPCKills"class="field_name_small">MostNPCKills:<\/a>\n<\/td>\n<tdclass="field_data_small"valign="top">\n<ahref="pplayer.vm\?characterId=(.*?)"class="field_data_small">(.*?)<\/a>/i;
print "<TR><TD><P ALIGN=Right><B>Most NPC Kills:</B></TD><TD>$2</TD></TR>";



$page =~ /<ahref="guild_wof.vm\?guildId=195113&rank=killDeathRatioRankGuild&type=MostKillsPerDeath"class="field_name_small">BestKillsvsDeathsRatio:<\/a><\/td>\n<tdclass="field_data_small"valign="top">\n<ahref="pplayer.vm\?characterId=(.*?)"class="field_data_small">(.*?)<\/a>/i;
print "<TR><TD><P ALIGN=Right><B>Best Kills vs Deaths Ratio:</B></TD><TD>$2</TD></TR>";



$page =~ /<ahref="guild_wof.vm\?guildId=195113&rank=questCompletionRankGuild&type=MostQuestsCompleted"class="field_name_small">MostQuestsCompleted:<\/a><\/td>\n<tdclass="field_data_small"valign="top">\n<ahref="pplayer.vm\?characterId=(.*?)"class="field_data_small">(.*?)<\/a>/i;
print "<TR><TD><P ALIGN=Right><B>Most Quests Completed:</B></TD><TD>$2</TD></TR>";


$page =~ /<ahref="guild_wof.vm\?guildId=195113&rank=guildPointRank&type=HighestGuildStatusContributor"class="field_name_small">HighestGuildStatusContributor:<\/a>\n<\/td>\n<tdclass="field_data_small"valign="top">\n<ahref="pplayer.vm\?characterId=(.*?)"class="field_data_small">(.*?)<\/a>/i;
print "<TR><TD><P ALIGN=Right><B>Highest Guild Status Contributor:</B></TD><TD>$2</TD></TR>";


print qq~
	</TABLE>
      </TD>
      <TD><CENTER><TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
~;

$page =~ /<tdvalign="top"class="field_name_small"style="padding-left:20px;">Fighters:<\/td>\n<tdvalign="top"class="field_data_small">(.*?)<\/td>/i;
print "<TR><TD><P ALIGN=Right><B>Fighters:</B></TD><TD>$1</TD></TR>";


$page =~ /<tdvalign="top"class="field_name_small"style="padding-left:20px;">Priests:<\/td>\n<tdvalign="top"class="field_data_small">(.*?)<\/td>/i;
print "<TR><TD><P ALIGN=Right><B>Priests:</B></TD><TD>$1</TD></TR>";


$page =~ /<tdvalign="top"class="field_name_small"style="padding-left:20px;">Mages:<\/td>\n<tdvalign="top"class="field_data_small">(.*?)<\/td>/i;
print "<TR><TD><P ALIGN=Right><B>Mages:</B></TD><TD>$1</TD></TR>";


$page =~ /<tdvalign="top"class="field_name_small"style="padding-left:20px;">Scouts:<\/td>\n<tdvalign="top"class="field_data_small">(.*?)<\/td>/i;
print "<TR><TD><P ALIGN=Right><B>Scouts:</B></TD><TD>$1</TD></TR>";


$page =~ /<tdvalign="top"class="field_name_small">MostRecentMembertoLevel:<\/td>\n<tdvalign="top"class="field_data_small">\n(.*?)\n<\/td>/i;
print "<TR><TD><P ALIGN=Right><B>Most Recent Member to Level:</B></TD><TD>$1</TD></TR>";


$page =~ /<tdvalign="top"class="field_name_small">MostRecentMembertoDie:<\/td>\n<tdvalign="top"class="field_data_small">\n(.*?)\n<\/td>/i;
print "<TR><TD><P ALIGN=Right><B>Most Recent Member to Die:</B></TD><TD>$1</TD></TR>";


print qq~
  </TABLE>
</CENTER>
</BODY>
</HTML>
~;

#$page =~ /<tdvalign="top"class="field_name_small">MostRecentItemDiscovered:<\/td>\n<tdvalign="top"class="field_data_small">\n<spanclass="capitalize"><ahref="item.vm\?itemId=(.*?)"class="field_data_small">(.*?)<\/a><\/span>/i;
#print "<TR><TD><B>Most Recent Item Discovered:</B></TD><TD><A HREF=http://eq2players.station.sony.com/en/item.vm?itemId=$1>$2</A></TD></TR>";

print "</TABLE><BR><P> <CENTER><SMALL>Imported from <A HREF=http://www.eq2players.com target=_new><SMALL>EQ2Players.com</SMALL></A>! If anything is incorrect.... its there fault. =)</SMALL></BODY></HTML>";