#!/usr/bin/perl

print "Content-type: text/html\n\n";

print qq~
   <tr><td><TABLE BORDER=0 WIDTH=100%>
~;

$url = "http://eqplayers.station.sony.com/guild_profile.vm?guildId=459561501316";

use CGI qw(param);
use LWP::Simple;

$page = get($url);

$page =~ s/\s+//g;




$page =~ /<tdclass="innerContentField">Members<\/td><td><divalign="right"class="innerContentData">(.*?)<\/div><\/td>/i;
print "<TR><TD>Members:</TD><TD><B>$1</B></TD></TR>";

$page =~ /<tdclass="innerContentField">Avg.Level<\/td><td><divalign="right"class="innerContentData">(.*?)<\/div><\/td>/i;
print "<TR><TD>Avg. Level:</TD><TD><B>$1</B></TD></TR>";

$page =~ /<tdwidth="25%"class="innerContentField">Melee<\/td><tdclass="innerContentData"><divalign="right">(.*?)<\/div>/i;
print "<TR><TD>Melee:</TD><TD><B>$1</B></TD></TR>";

$page =~ /<tdclass="innerContentField">Casters<\/td><tdwidth="25%"class="innerContentData"><divalign="right">(.*?)<\/div>/i;
print "<TR><TD>Casters:</TD><TD><B>$1</B></TD></TR>";

$page =~ /<tdclass="innerContentField">Hybrids<\/td><tdclass="innerContentData"><divalign="right">(.*?)<\/div>/i;
print "<TR><TD>Hybrids:</TD><TD><B>$1</B></TD></TR>";

$page =~ /<tdclass="innerContentField">Priests<\/td><tdclass="innerContentData"><divalign="right">(.*?)<\/div>/i;
print "<TR><TD>Priests:</TD><TD><B>$1</B></TD></TR>";

$page =~ /<tdclass="innerContentField">GuildTributePoints<\/td><td><divalign="right"class="innerContentData">(.*?)<\/div><\/td>/i;
print "<TR><TD>Tribute Points:</TD><TD><B>$1</B></TD></TR>";


print qq~
</TD></TR>

</TABLE></td></td>
~;