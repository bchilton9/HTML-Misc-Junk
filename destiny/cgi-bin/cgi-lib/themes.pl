###############################################################################
###############################################################################
# themes.pl - Sub-Routines                                                    #
# for the use with WebAPP and YaWPS and PerlPort                              #
#                                                                             #
# Copyright (C) 2002 by ABYWN  webapp@abywn.de                                #
#                                                                             #
# some of it comes from YaWPS which was programmed by and under the           #
# Copyright (C) 2001 of Adrian Heiszler (heiszler@gmx.net)                    #
#                                                                             #
# some of it comes from WebAPP which was programmed using YaWPS by            #
# and under the Copyright (C) 2001 of Carter                                  #
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
# Last modified: 09/12/02                                                     #
###############################################################################
###############################################################################


#######
# starting here, the file is exactly the same for ALL themes.
# Von hier ab ist die Datei für ALLE Layouts genau gleich.
#######

###< (c) abwyn >####¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯SUB
sub getmorevars {
#############

    $ongif = "<img alt='' src='$imagesurl/on.gif' border='0'> ";        # greenlight for userstatus or active theme and stuff
    $offgif = "<img alt='' src='$imagesurl/off.gif' border='0'> ";      # redlight for userstatus or inactive theme and stuff
    $checkedgif = "<img alt='' src='$imagesurl/checked.gif' border='0'> ";      #
    $uncheckedgif = "<img alt='' src='$imagesurl/unchecked.gif' border='0'> ";      #

    if ($info{'testmodus'} ne "")  {
            ($btst, $btst1, $btst2, $btst3, $btst4, $btst5) = (1,1,2,3,4,5);
            ($tst, $tst1, $tst2, $tst3, $tst4, $tst5) = ("#993300", "#660033", "#FF6600", "#CC0000", "#FF9900", "#CC9900" );
            $testmodustext="Testmodus-FillText";
    } else {
            ($btst, $btst1, $btst2, $btst3, $btst4, $btst5) = (0,0,0,0,0,0) ;
            ($tst, $tst1, $tst2, $tst3, $tst4, $tst5) = ("", "", "", "", "", "" );
            $testmodustext="";
    }

    # foreach  (qw(ttst, ttst1, ttst2, ttst3, ttst4, ttst5)) { $$_ = qq~style="border-color:$$_"~;}

    $latestforumpost=15; # this should actually go into the new adminsection this is here just temporarily
    $ftitlemaxlength=30; # this should actually go into the new adminsection this is here just temporarily

}
#___________________________________________________________________________________________ENDE_SUB


###< (c) abwyn >####¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯SUB
sub mycontent_block { mycontent_block2();}
#___________________________________________________________________________________________ENDE_SUB


###< (c) abwyn >####¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯SUB
sub mycontent_block2 {
######################

	if ($showcon2 eq "1") {

      boxheader("$nav{'093'}" );

      latestforumpostsXL();
	  $topics_printed ="0";

      $tmpshow	=	@myforumnum;

    print qq~
        <tr>
            <td class="forumwindow1">$tmpshow</td>
            <td class="forumwindow1"></td>
            <td class="forumwindow1">$msg{'101'}</td>
            <td class="forumwindow1">$words{'115'}</td>
            <td class="forumwindow1">$msg{'102'}</td>
  <!--      <td class="forumwindow1">$words{'075'}</td> -->
	        <td class="forumwindow1">$words{'074'}</td>
            <td class="forumwindow1">$msg{'098'}</td>
            <td class="forumwindow1"></td>
       </tr>
    ~;

      if (@myforumnum) {
            $tmpnr="2";
			foreach $tmpid (@myforumnum) {
                    print qq~
                    <tr>
                    <td class="forumwindow$tmpnr">$menugif&nbsp;$myforumdata0{$tmpid}</td>
                    <td class="forumwindow$tmpnr">          $myforumdata4{$tmpid}</td>
                    <td class="forumwindow$tmpnr">          $myforumdata5{$tmpid}</td>
                    <td class="forumwindow$tmpnr" align="center">($myforumdata1{$tmpid})</td>
                    <td class="forumwindow$tmpnr" align="center">$myforumdata2{$tmpid}</td>
               <!-- <td class="forumwindow$tmpnr">          $myforumdata7{$tmpid}</td> -->
					<td class="forumwindow$tmpnr">          $myforumdata6{$tmpid}</td>
                    <td class="forumwindow$tmpnr">          $myforumdata3{$tmpid}</td>
                    <td class="forumwindow$tmpnr" align="right"> ($myforumdata8{$tmpid})</td>
                    </tr>
                    ~;
                    $tmpnr= 5- $tmpnr;
					$topics_printed++;
					if ($topics_printed >$latestforumpost) {last;}


            }
       }
      else {
            print qq~
               <tr>
                    <td colspan=6>$msg{'179'}</td>
                </tr>
        ~;
      }
      boxfooter();
    }

}
#___________________________________________________________________________________________ENDE_SUB


###< (c) abwyn >####
sub latestforumpostsXL {
####################
# used in Classic theme, added by Abwyn, at end of themes.pl calls to
# user-lib/themes.pl (if it exists) which calls this latestforumpostsXL
# sub from mycontent_block2 sub

file2array("$boardsdir/cats.txt","fcats");

	%myforumdata= ();
	%tmpsort=();

$tmpcnt = "0";

foreach $fcat (@fcats) {

		($fcat, $curcat_moderator) = split(/\|/, $fcat) ;

file2array("$boardsdir/$fcat.cat","fcatinfo");

            $fcatname=$fcatinfo[0];

    for ($i=2; $i<@fcatinfo;$i++) {
            $fcatinfo[$i] =~ s/[\n\r]//g;
            $selboard=$fcatinfo[$i];

            $fcatinfo[1] =~ s/[\n\r]//g;
            $board_access_for = "$fcatinfo[1]";

            if ($fcatinfo[1] ne "") {
                $myrank="$settings[7]";
                if ($settings[14] eq "")    {$mystatus="member";} else { $mystatus="$settings[14]";  }
                if ($settings[7] eq "")     {$myrank="member";  } else { $myrank="$settings[7]";  }

             if ( ( $board_access_for !~ /$myrank|$mystatus/i) and ($myrank ne "$root")  ) { last;  } # this is the WebApp specialized version of checking
            }

            file2array("$boardsdir/$selboard.dat","fposts");

            $selboardname=$fposts[0];

            file2array("$boardsdir/$selboard.txt","fposts");

			$topics_printed = $tmpcnt = "0";
            foreach $fpost (@fposts) {

# each  data-line looks like
#63|test|abywn|admin|WebApp.WebMrs@proficon.de|05/21/03 - 11:04:05|3|17|abywn|xx|0


                ($tmpid, $fptitle, $tmprealname, $dummy, $dummy, $fpdate, $fpanswers, $fpread, $fplastposter, $dummy, $dummy) = split(/\|/, $fpost);
                if (length($fptitle) > $ftitlemaxlength)
                { $fptitle = substr($fptitle,0,$ftitlemaxlength); $fptitle = "$fptitle...";}
                if ($fpanswers >= $maxmessagedisplay) {
                    for ($tmp=0;$fpanswers;$tmp++) {
                          $tmpstart=$tmp*$maxmessagedisplay;
                          if (($tmp+1)*$maxmessagedisplay > $fpanswers) {last  }
                    }
                }  else { $tmpstart=0 }

				$tmpdate = $fpdate;
				$tmpdate =~ s/ - .*//eg;

                $mythread0 = qq~
					<a href="$pageurl/$cgi?action=forum&amp;board=$selboard&amp;op=display&amp;num=$tmpid&amp;start=$tmpstart#$fpanswers" class="mycontentlink">
                    $fptitle
                    </a>
                ~;

                $mythread1 = qq~$fpread~;
                $mythread2 = qq~$fpanswers~;
                $mythread3 = qq~$fplastposter~;
                $mythread4 = qq~
                    <a href="$pageurl/$cgi?action=forum&amp;board=$selboard&amp;op=display&amp;num=$tmpid"
                    class="mycontentlink">top </a>&nbsp;&nbsp;
               ~;
                $mythread5 = qq~$tmprealname~;
                $mythread6 = qq~
                                <a href="$pageurl/$cgi?action=forum&amp;board=$selboard" class="mycontentlink">
                                $selboardname
                                </a>
                ~;

                $mythread7 = qq~
                                <a href="$pageurl/$cgi?action=forum&amp;cat=$fcat" class="mycontentlink">
                                $fcatname
                                </a>
                ~;
				($tmonth, $tday, $tyear, $thour, $tmin, $tsec) = split(/\/| - |\:/, $fpdate);
				if ($tyear < 30) {	$tyear= $tyear +2000;   } else {   $tyear= $tyear +1900;}

				$tmpsort{$tmpid} = "$tyear$tmonth$tday$thour$tmin$tsec";

                $mythread8 = qq~$tday.$tmonth-$thour:$tmin~;

                $myforumdata0{$tmpid}= $mythread0;
                $myforumdata1{$tmpid}= $mythread1;
                $myforumdata2{$tmpid}= $mythread2;
                $myforumdata3{$tmpid}= $mythread3;
                $myforumdata4{$tmpid}= $mythread4;
                $myforumdata5{$tmpid}= $mythread5;
                $myforumdata6{$tmpid}= $mythread6;
                $myforumdata7{$tmpid}= $mythread7;
                $myforumdata8{$tmpid}= $mythread8;

				$topics_printed++;
				if ($topics_printed >$latestforumpost) {last;}
            }

    }
}
@myforumnum = reverse sort {$tmpsort{$a} cmp $tmpsort{$b} }(keys(%myforumdata0)); #
}
#___________________________________________________________________________________________ENDE_SUB

###< (c) abwyn >####¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯SUB
sub lock_file   {	local($file) = @_;	if ($use_flock eq "1" ) { flock($file, $LOCK_EX); }}
# needed for sub file2array below
# also file2string if used

sub unlock_file {	local($file) = @_;	if ($use_flock eq "1" ) { flock($file, $LOCK_UN); } }
# needed for sub file2array below
# also file2string if used

###< (c) abwyn >####¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯SUB
sub file2array {
####################
# needed for 3 places in printpage sub- forum_display.pl
# basically the same as chomp_database sub of 9.1

my $filename = @_[0];
my $arrayname = @_[1];
$successful{'$filename'}="1";

# please don't use an || error ... in the next line with open
# because we also load files that might not exist. (txt, sticky)
# we can check sucess either by the length of the array or by the hash %successful

open(FILE, "$filename");# || $successful{'$filename'}="";
    lock_file(FILE);
        chomp(@$arrayname = <FILE>);
    unlock_file(FILE);
close(FILE);

}
#___________________________________________________________________________________________ENDE_SUB

###< (c) abwyn >####¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯SUB
sub file2string {
####################
# not yet used?
# basically the same as chomp_datatext sub of 9.1

my $filename = @_[0];
my $varname = @_[1];
$$varname = 0;
$successful{'$filename'}="1";

# please don't use an || error ... in the next line with open
# because we also load files that might not exist. (txt, sticky)
# we can check sucess either by the length of the array or by the hash %successful

open(FILE, "$filename");# || $successful{'$filename'}="";
    lock_file(FILE);
        chomp($$varname = <FILE>);
    unlock_file(FILE);
close(FILE);

}
#_________________________________________________________________ENDE_SUB

if (-e "$scriptdir/user-lib/themes.pl") { require "$scriptdir/user-lib/themes.pl" }

1; # return true
