###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# newsletter.pl                                   				      #
# v0.9.9 - Requin                                					#
# Copyright (C) 2002 by WebAPP (webapp@attbi.com)                             #
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
# File: Last modified: 08/01/02                                               #
###############################################################################
###############################################################################


###############
sub subscribe {
###############
	if ($input{'action'} eq "subscribe") { &subscribe1;
	}else{ &unsubscribe;}
}

################
sub subscribe1 {
################

$entrytoadd = $input{'joinnl'};
$entrytoadd =~ tr/A-Z/a-z/;
if ($input{'joinnl'} eq "") { error("$err{'005'}");}
if ($entrytoadd  =~ /.+\@.+\..+/) {;} else { error("$err{'005'}");}

$foundentry ="";

print_top();

open(FILE,"$datadir/newsletter/emails.txt");
@subscribers = <FILE>;
close(FILE);

foreach $subscriber(@subscribers) {
    chomp($subscriber);
    $subscriber =~ tr/A-Z/a-z/;
    if ($entrytoadd eq $subscriber){ $foundentry= TRUE; }
}
unless ($foundentry) {

    open(FILE,">$datadir/newsletter/emails.txt"); # using this to clean out all emails so far...
        foreach $writeentry (@subscribers) {
           chomp($writeentry);
           $writeentry=~ tr/A-Z/a-z/;
           if ($writeentry ne "")  {  print FILE "$writeentry\n";  }
        }
        print FILE "$entrytoadd\n";
    close(FILE);

    $subject="$msg{'434'}";
    $message="$msg{'435'}\n\n$msg{'436'}\n\n$msg{'437'}\n\n \n\n$msg{'166'}!\n\n";
    sendemail($entrytoadd, $subject, $message, $webmaster_email);
}

$navbar = "$btn{'014'} $mnu{'038'} $btn{'014'} $msg{'301'}";

print_top();

if ($foundentry) {   
    print qq~       <br><br><b><center>
                    <!-- adapt you message here below -->       
                    $entrytoadd, $msg{'173'}
                    </center></b>~;   }
# actually this SHOULD say you are ALREADY subscribed to our list
# but it wasn't in the languagefile, so it just says you are subscribed :-) adapt this in your language if you wish
else {               
    print qq~       <br><br><b><center>
                    $msg{'305'}$entrytoadd$msg{'310'}
                    </b></center>
                    <br><br>
                    $msg{'317'}
                    <br><br>- Admin<br><br>
    ~;
}

print_bottom();

}

#################
sub unsubscribe {
#################

$navbar = "$btn{'014'} $mnu{'038'} $btn{'014'} $err{'005'}";

if ($input{'joinnl'} eq "") { error("$err{'005'}")}

$entrytoremove = $input{'joinnl'};
$entrytoremove =~ tr/A-Z/a-z/;

open(FILE,"$datadir/newsletter/emails.txt");
file_lock(FILE);
@addresses=<FILE>;
unfile_lock(FILE);
close(FILE);

$deletedentry="";

foreach $add (@addresses) {
chomp($add);
   $add=~ tr/A-Z/a-z/;
if ($entrytoremove eq "$add") {
open(FILE,">$datadir/newsletter/emails.txt");
            foreach $writenew (@addresses) {
                chomp($writenew);
               $writenew=~ tr/A-Z/a-z/;
                if( ($writenew ne "") && ($writenew =~ /.+\@...*\.../ )) {
                    if ($writenew eq $add ) { $deletedentry= TRUE; }
                    else {print FILE "$writenew\n";}
                }
            }
close(FILE);
}
}
$navbar = "$btn{'014'} $mnu{'038'} $btn{'014'} $msg{'438'}";

print_top();

if ($deletedentry) {    print "<b>$entrytoremove</b>$msg{'439'}";   }
else {                  print "<b>$entrytoremove</b>$msg{'440'}";   }

print_bottom();

}


###################
sub newslettermsg {
###################
	if ($settings[7] ne "$root") { error("$err{'011'}"); }

	open(FILE, "$datadir/newsletter.msg") || error("$err{'001'} $datadir/newsletter.msg");
	file_lock(FILE);
	chomp(@lines = <FILE>);
	unfile_lock(FILE);
	close(FILE);

	$subject = htmltotext($lines[0]);
	$message = htmltotext($lines[1]);

	$navbar = "$btn{'014'} $nav{'042'} $btn{'014'} $nav{'136'}";
	print_top();
	print qq~<form action="$pageurl/$admin&amp;op=newslettermsg2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
$msg{'380'}<br>
<input type="text" name="subject" value="$subject" size="40">
</td>
</tr>
<tr>
<td>
$msg{'396'}<br>
<textarea name="message" cols="40" rows="10">$message</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}"><input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
	print_bottom();
	exit;
}

####################
sub newslettermsg2 {
####################
	if ($settings[7] ne "$root") { error("$err{'011'}"); }
	error("$err{'014'}") unless ($input{'subject'});
	error("$err{'015'}") unless ($input{'message'});

	chomp($input{'subject'});
	chomp($input{'message'});

	$subject = htmlescape($input{'subject'});
	$message = htmlescape($input{'message'});

	open(FILE, ">$datadir/newsletter.msg") || error("$err{'016'} $datadir/newsletter.msg");
	file_lock(FILE);
	print FILE "$subject\n";
	print FILE "$message\n";
	unfile_lock(FILE);
	close(FILE);

	print "Location: $pageurl/$admin\&op=newsletter\n\n";
}


################
sub newsletter {
################
if ($settings[7] ne "$root") { error("$err{'011'}"); }

$emailnumber=0;
open(FILE,"$datadir/newsletter/emails.txt");
@subscribers = <FILE>;
close(FILE);
$emailnumber = push(@subscribers);
$navbar = "$btn{'014'} $mnu{'038'}";
print_top();

print qq~ <br><center><B>$msg{'442'}$emailnumber$msg{'443'}</b><BR><BR>[<a href="$pageurl/$admin&op=newslettermsg">$nav{'136'}</a>] [<a href="$pageurl/$admin&op=sendnewsletter">$nav{'156'}</a>] [<a href="$pageurl/$admin&op=editemails">$nav{'138'}</a>]</center>
~;

	open(FILE, "$datadir/newsletter.msg");
	file_lock(FILE);
	chomp(@lines = <FILE>);
	unfile_lock(FILE);
	close(FILE);
			$unsub_text = "---------------------------------------------------------------------------------------------------------------<br>$msg{'441'}<br>---------------------------------------------------------------------------------------------------------------";
		

			$nltitle = showhtml("$lines[0]");
			$nlbody = showhtml("$lines[1]");

print qq~<br><br>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td></td>
</tr>
<br>
<hr>
<br>
<tr>
<td><p class="texttitle">$nltitle</p>
$nlbody<br>
<br>$unsub_text<br></td>
</tr>
</table>
~;

print_bottom();

exit;
}

####################
sub sendnewsletter {
####################
if ($settings[7] ne "$root") { error("$err{'011'}"); }


$navbar = "$btn{'014'} $nav{'155'}";
print_top();

	open(FILE, "$datadir/newsletter.msg");
	file_lock(FILE);
	chomp(@lines = <FILE>);
	unfile_lock(FILE);
	close(FILE);
			$unsub_text = "---------------------------------------------------------------------------------------------------------------<br>$msg{'441'}<br>---------------------------------------------------------------------------------------------------------------";
		

			$nltitle = showhtml("$lines[0]");
			$nlbody = showhtml("$lines[1]");

print qq~<br><br>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td></td>
</tr>
<br>
<tr>
<td><p class="texttitle">$nltitle</p>
$nlbody<br>
<br>$unsub_text<br></td>
</tr>
</table>
<br><br>
<center><a href="$pageurl/$admin&op=sendnewsletter2"> [ $nav{'137'} ] </a></center><br><br>
~;

print_bottom();


exit;

}

#####################
sub sendnewsletter2 {
#####################
if ($settings[7] ne "$root") { error("$err{'011'}"); }

$navbar = "$btn{'014'} $msg{'444'}";
print_top();

open(FILE, "$memberdir/admin.dat") || error("$err{'001'} $memberdir/admin"); 
	file_lock(FILE); 
	chomp(@adminmail = <FILE>); 
	unfile_lock(FILE); 
	close(FILE); 

	open(EMAILS, "$datadir/newsletter/emails.txt");
	file_lock(EMAILS);
	chomp(@mail = <EMAILS>);
	unfile_lock(EMAILS);
	close(EMAILS);

	open(FILE, "$datadir/newsletter.msg");
	file_lock(FILE);
	chomp(@lines = <FILE>);
	unfile_lock(FILE);
	close(FILE);


		foreach $member (@mail) {
		$member =~ s/[\n\r]//g;
		if ($member eq "") {next;  } # abywn: added to prevent empty lines beeing used 
		$unsub_text = "
		
		---------------------------------------------------------------------------------------
		$msg{'441'}
		---------------------------------------------------------------------------------------";
			require "$sourcedir/subs.pl";
			$nltitle = convert_newsletter($lines[0]);
			$nlbody = convert_newsletter($lines[1]).$unsub_text;


		sendemail($member, $nltitle, $nlbody, $adminmail[2]);

		}


print qq~ <br><center>[<a href="$pageurl/$admin&op=newslettermsg">$nav{'136'}</a>] [<a href="$pageurl/$admin&op=sendnewsletter">$nav{'156'}</a>] [<a href="$pageurl/$admin&op=editemails">$nav{'138'}</a>]</center>
<br>
<center><b>$msg{'445'}</b></center><br>
~;
			$unsub_text = "---------------------------------------------------------------------------------------------------------------<br>$msg{'441'}<br>---------------------------------------------------------------------------------------------------------------";

			open(FILE, "$datadir/newsletter.msg");
			file_lock(FILE);
			chomp(@lines = <FILE>);
			unfile_lock(FILE);
			close(FILE);

			$nltitle = showhtml($lines[0]);
			$nlbody = showhtml($lines[1]);

print qq~<br><br>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr>
<td></td>
</tr>
<br>
<hr>
<br>
<tr>
<td><p class="texttitle">$nltitle</p>
$nlbody<br>
<br>$unsub_text<br></td>
</tr>
</table>
~;

print_bottom();

exit;
}

###################
sub editemails {   
###################
	if ($settings[7] ne "$root") { error("$err{'011'}"); }
	
	$navbar = "$btn{'014'} $mnu{'038'} $btn{'014'} $nav{'138'}";
	print_top();
	
	open(FILE, "$datadir/newsletter/emails.txt");
	file_lock(FILE);
	chomp(@data= <FILE>);
	close(FILE);	

	print qq~<form action="$pageurl/$admin&amp;op=editemails2" method="post">
<table border="0" width="100%" cellpading="0" cellspacing="0">
<tr>
<td>
<b>$msg{'446'}:</b><br>
<textarea name="theemails" cols="40" rows="20">~;

foreach $email3 (@data) {
		$email3 =~ s/[\n\r]//g;
		print "$email3\n";
}
print qq~
</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="$btn{'022'}"><input type="reset" value="$btn{'023'}"></td>
</tr>
</table>
</form>
~;
print_bottom();
	

exit;
}
	
#################### 
sub editemails2 { 
#################### 

if ($settings[7] ne "$root") { error("$err{'011'}"); } 
chomp($input{'theemails'}); 
open(FILE, ">$datadir/newsletter/emails.txt"); 
file_lock(FILE); 
print FILE $input{'theemails'}; 
unfile_lock(FILE);
close(FILE); 

print "Location: $pageurl/$admin\&op=newsletter\n\n"; 
exit; 
}

if (-e "$scriptdir/user-lib/newsletter.pl") {require "$scriptdir/user-lib/newsletter.pl"} 

1;
