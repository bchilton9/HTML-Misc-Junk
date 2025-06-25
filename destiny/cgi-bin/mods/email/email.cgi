#!/usr/bin/perl

###############################################

$USER = "webmaster\@sanctuaryeq2.com";
$PASSWORD = "dragon45";
$HOST = "mail.sanctuaryeq2.com";
$DOMAIN = "sanctuaryeq2.com";
$SCRIPTURL = "http://www.sanctuaryeq2.com/cgi-bin/mods/email/email.cgi";
$mailprog = "/usr/sbin/sendmail";

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

if ($input{'action'} eq "view") { &view; }
elsif ($input{'action'} eq "delete") { &delete; }
elsif ($input{'action'} eq "forward") { &send; }
elsif ($input{'action'} eq "reply") { &send; }
elsif ($input{'action'} eq "send") { &send; }
elsif ($input{'action'} eq "sendmail") { &sendmail; }
else { &list; }


##################
sub list {
##################

$shown = 0;

use Mail::POP3Client;
$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $input{'DEBUG'});
  for( $i = 1; $i <= $pop->Count(); $i++ ) {
    $_ = $pop->List($i);
    ($no, $size) = split(/ /);
    $size[$no] = $size;

    foreach( $pop->Head( $i ) ) {
      $to[$no] = $_ if (/To:/);
      $date[$no] = $_ if (/Date:/);
      $from[$no] = $_ if (/From:/);
      $returnpath[$no] = $_ if (/Return-Path:/);
      $replypath[$no] = $_ if (/Reply-Path:/);
      $subject[$no] = $_ if (/Subject:/);
    }

  }
$popstate = $pop->State();
$pop->Close();

if (($popstate eq "TRANSACTION") && (@size)) {

$navbar = " $btn{'014'} E-Mail $btn{'014'} $username\'s Inbox";
print_top();

print qq~
Your E-Mail Address: <B>$username\@$DOMAIN</B><BR>
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=90%></td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="http://www.sanctuaryeq2.com/images/im/leftoriginal.gif"></td>
<td bgcolor=#D2E2F6 align=center height=6 valign=top><img src=http://www.sanctuaryeq2.com/images/im/toporiginal.gif><br>
<b><a href=$SCRIPTURL?action=send>Write</a></b></td>
<td><img src=http://www.sanctuaryeq2.com/images/im/rightoriginal.gif></td></tr></table>
</td>
</tr>
<tr bgcolor=#D2E2F6><td height=4 colspan=5></td></tr>
</table>



<table width="100%" bgcolor="#000000" border="0" cellspacing="2" cellpadding="1">
<tr class=forumwindow1>
<td width="10%"><b>From: </b></td>
<td width="50%"><b>Subject:</b></td>
<td width="20%"><b>Date:</b></td>
<td width=15%><b>Action:</b></td>

</tr>
~;


for ($i=1;$i<=(scalar @size)-1;$i++) {

$to[$i] =~ s/To: //gi;
#$from[$i] =~ s/From: //gi;
$date[$i] =~ s/Date: //gi;
$subject[$i] =~ s/Subject: //gi;
$returnpath[$i] =~ s/Return-Path: <//gi;
$returnpath[$i] =~ s/>//gi;


        #if ($from[$i] !~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/ ||
        #$from[$i] !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/) {
        #        $returnpath[$i] = $from[$i];
        #}



$checkuser = $username;
$checkuser =~ tr/A-Z/a-z/;
$checkto = $to[$i];
$checkto =~ s/reply-//gi;
$checkto =~ tr/A-Z/a-z/;

if ($checkto eq "$checkuser\@$DOMAIN") {

print qq~

<td class="imwindow2" width="35%" nowrap><a href="$SCRIPTURL?action=reply&to=$returnpath[$i]&message=$i">$returnpath[$i]</A></td>

<td class="imwindow2" width="35%"><a href="$SCRIPTURL?action=view&message=$i">$subject[$i]</A></td>

<td class="imwindow2" width="20%" nowrap>$date[$i]</td>

<td class="imwindow2" width="10%" nowrap>
<a href="$SCRIPTURL?action=view&message=$i"><img src="http://www.sanctuaryeq2.com/images/forum/open.gif" alt="View" border="0"></A>
<a href="$SCRIPTURL?action=delete&message=$i"><img src="http://www.sanctuaryeq2.com/images/forum/delete.gif" alt="Delete" border="0"></a>
<a href="$SCRIPTURL?action=reply&to=$returnpath[$i]&message=$i"><img src="http://www.sanctuaryeq2.com/images/forum/replymsg.gif" alt="Reply" border="0"></a>
<a href=$SCRIPTURL?action=forward&message=$i><img src="http://www.sanctuaryeq2.com/images/forum/move.gif" alt="Forward" border="0"></a>
</td></tr>
~;
$shown++;
}#if
}#for

if ($shown eq 0) {
print "<td class=imwindow2 COLSPAN=4><center>Your Inbox is empty.</center></td>\n";
}#empty


print qq~
<tr bgcolor=#D2E2F6><td colspan=5 align=right></td></tr>
        </table>
<br>
</center>
~;
print_bottom();

}
}

##################
sub view {
##################
$i = $input{'message'};

$navbar = " $btn{'014'} E-Mail $btn{'014'} Read E-Mail";
print_top();

use Mail::POP3Client;
$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $input{'DEBUG'});

    $_ = $pop->List($i);
    ($no, $size) = split(/ /);
    $size[$no] = $size;
    foreach( $pop->Head( $i ) ) {
      $to[$no] = $_ if (/To:/);
      $date[$no] = $_ if (/Date:/);
      $from[$no] = $_ if (/From:/);
      $returnpath[$no] = $_ if (/Return-Path:/);
      $subject[$no] = $_ if (/Subject:/);
    }

    foreach( $pop->Body( $i ) ) {
      $body.="&nbsp; $_ <BR>\n";
    }

$popstate = $pop->State();
$pop->Close();

$to[$i] =~ s/To: //gi;
#$from[$i] =~ s/From: //gi;
$date[$i] =~ s/Date: //gi;
$returnpath[$i] =~ s/Return-Path: <//gi;
$returnpath[$i] =~ s/>//gi;

        #if ($from[$i] !~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)/ ||
        #$from[$i] !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/) {
        #        $returnpath[$i] = $from[$i];
        #}

print qq~
<BR>
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=90%></td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="http://www.sanctuaryeq2.com/images/im/leftoriginal.gif"></td>
<td bgcolor=#D2E2F6 align=center height=6 valign=top><img src=http://www.sanctuaryeq2.com/images/im/toporiginal.gif><br>
<b><a href=$SCRIPTURL>Inbox</a></b></td>
<td><img src=http://www.sanctuaryeq2.com/images/im/rightoriginal.gif></td></tr></table>
</td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="http://www.sanctuaryeq2.com/images/im/leftoriginal.gif"></td>
<td bgcolor=#D2E2F6 align=center height=6 valign=top><img src=http://www.sanctuaryeq2.com/images/im/toporiginal.gif><br>
<b><a href=$SCRIPTURL?action=send>Write</a></b></td>
<td><img src=http://www.sanctuaryeq2.com/images/im/rightoriginal.gif></td></tr></table>
</td>
</tr>
<tr bgcolor=#D2E2F6><td height=4 colspan=5></td></tr>
</table>


<TABLE width="100%" bgcolor="#000000" border="0" cellspacing="0" cellpadding="0" HEIGHT="100%">
        <TR>
          <TD valign="top" width="100%" HEIGHT="100%">
<TABLE border="0" cellspacing="1" cellpadding="2" WIDTH="100%" HEIGHT="100%">
  <TR>
    <TD BGCOLOR="#D2E2F6" WIDTH="5%"><P ALIGN=Right>To:</TD>
    <TD bgcolor="#ffffff">$to[$i]</TD>
  </TR>
  <TR>
    <TD BGCOLOR="#D2E2F6"><P ALIGN=Right>From:</TD>
    <TD bgcolor="#ffffff"><a href=$SCRIPTURL?action=reply&to=$returnpath[$i]&message=$i>$returnpath[$i]</A></TD>
  </TR>
  <TR>
    <TD BGCOLOR="#D2E2F6"><P ALIGN=Right>Date:</TD>
    <TD bgcolor="#ffffff">$date[$i]</TD>
  </TR>
  <TR>
    <TD COLSPAN=2 BGCOLOR="#D2E2F6">
<TABLE BORDER=0 CELLSPACING="0" CELLPADDING="0" WIDTH="100%">
  <TR>
    <TD>&nbsp; <IMG SRC="http://www.sanctuaryeq2.com/images/im/aicon2.gif"> $subject[$i]</TD>
    <TD nowrap><P ALIGN=Right>
<a href=$SCRIPTURL?action=delete&message=$i><img src="http://www.sanctuaryeq2.com/images/forum/delete.gif" alt="Delete" border="0"></a>
<a href=$SCRIPTURL?action=reply&to=$returnpath[$i]&message=$i><img src="http://www.sanctuaryeq2.com/images/forum/replymsg.gif" alt="Reply" border="0"></a>
<a href=$SCRIPTURL?action=forward&message=$i><img src="http://www.sanctuaryeq2.com/images/forum/move.gif" alt="Forward" border="0"></a>
    </TD>
  </TR>
</TABLE>
</TD>
  </TR>
  <TR>
    <TD bgcolor="#ffffff" COLSPAN=2 HEIGHT="100%">$body</TD>
  </TR>
  <TR>
    <TD COLSPAN=2 BGCOLOR="#D2E2F6">
<P ALIGN=Right>
<a href=$SCRIPTURL?action=delete&message=$i><img src="http://www.sanctuaryeq2.com/images/forum/delete.gif" alt="Delete" border="0"></a>
<a href=$SCRIPTURL?action=reply&to=$returnpath[$i]&message=$i><img src="http://www.sanctuaryeq2.com/images/forum/replymsg.gif" alt="Reply" border="0"></a>
<a href=$SCRIPTURL?action=forward&message=$i><img src="http://www.sanctuaryeq2.com/images/forum/move.gif" alt="Forward" border="0"></a>
</TD>
  </TR>
</TABLE>
    </TD>
  </TR>
</TABLE>
<BR>
~;
print_bottom();

}

##################
sub send {
##################

if ($input{'action'} eq "reply") {
$i = $input{'message'};

use Mail::POP3Client;
$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $input{'DEBUG'});

    $_ = $pop->List($i);
    ($no, $size) = split(/ /);
    $size[$no] = $size;
    foreach( $pop->Head( $i ) ) {
      $to[$no] = $_ if (/To:/);
      $date[$no] = $_ if (/Date:/);
      $from[$no] = $_ if (/From:/);
      $returnpath[$no] = $_ if (/Return-Path:/);
      $subject[$no] = $_ if (/Subject:/);
    }

    foreach( $pop->Body( $i ) ) {
      $body.="> &nbsp; $_ \n";
    }

$popstate = $pop->State();
$pop->Close();

$subject[$i] =~ s/Subject: //gi;

$to = "$input{'to'}";
$subject = "Re: $subject[$i]";
$body = "\n\n\n\n$body";
}

elsif ($input{'action'} eq "forward") {

$i = $input{'message'};

use Mail::POP3Client;
$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $input{'DEBUG'});

    $_ = $pop->List($i);
    ($no, $size) = split(/ /);
    $size[$no] = $size;
    foreach( $pop->Head( $i ) ) {
      $to[$no] = $_ if (/To:/);
      $date[$no] = $_ if (/Date:/);
      $from[$no] = $_ if (/From:/);
      $returnpath[$no] = $_ if (/Return-Path:/);
      $subject[$no] = $_ if (/Subject:/);
    }

    foreach( $pop->Body( $i ) ) {
      $body.="&nbsp; $_ \n";
    }

$popstate = $pop->State();
$pop->Close();

$subject[$i] =~ s/Subject: //gi;

$to = "";
$subject = "Fwd: $subject[$i]";
$body = "$body";
}
elsif ($input{'action'} eq "retry") {
$to = "$input{'toemail'}";
$subject = "$input{'subject'}";
$body = "$input{'body'}";
}
else {
$to = "";
$subject = "";
$body = "";
}

$navbar = " $btn{'014'} E-Mail $btn{'014'} Send E-Mail";
print_top();
print qq~
<BR>
<CENTER>$errormsg</CENTER>
<table width=100% border=0 cellpadding=0 cellspacing=0>
<tr><td width=90%></td>
<td>
<table border=0 cellpadding=0 cellspacing=0><tr><td><img src="http://www.sanctuaryeq2.com/images/im/leftoriginal.gif"></td>
<td bgcolor=#D2E2F6 align=center height=6 valign=top><img src=http://www.sanctuaryeq2.com/images/im/toporiginal.gif><br>
<b><a href=$SCRIPTURL>Inbox</a></b></td>
<td><img src=http://www.sanctuaryeq2.com/images/im/rightoriginal.gif></td></tr></table>
</td>
</tr>
<tr bgcolor=#D2E2F6><td height=4 colspan=5></td></tr>
</table>


<FORM ACTION="$SCRIPTURL" METHOD="POST">

<TABLE width="100%" bgcolor="#000000" border="0" cellspacing="0" cellpadding="0" HEIGHT="100%">
        <TR>
          <TD valign="top" width="100%" HEIGHT="100%">
<TABLE border="0" cellspacing="1" cellpadding="2" WIDTH="100%" HEIGHT="100%">
  <TR>
    <TD BGCOLOR="#D2E2F6" WIDTH="5%"><P ALIGN=Right>To:</TD>
    <TD bgcolor="#ffffff"><INPUT TYPE="text" SIZE="40" NAME="toemail" value="$to">$noemail</TD>
  </TR>
  <TR>
    <TD BGCOLOR="#D2E2F6" WIDTH="5%"><P ALIGN=Right>From:</TD>
    <TD bgcolor="#ffffff">$username\@$DOMAIN</TD>
  </TR>
  <TR>
    <TD BGCOLOR="#D2E2F6"><P ALIGN=Right>Subject:</TD>
    <TD bgcolor="#ffffff"><INPUT TYPE="text" NAME="subject" SIZE="60" value="$subject">$noemail</TD>
  </TR>
  <TR>
    <TD COLSPAN=2 BGCOLOR="#D2E2F6">
Message:$noemail
</TD>
  </TR>
  <TR>
    <TD bgcolor="#ffffff" COLSPAN=2 HEIGHT="100%"><TEXTAREA NAME="body" ROWS="20" COLS="90" width="100%">$body</TEXTAREA></TD>
  </TR>
  <TR>
    <TD COLSPAN=2 BGCOLOR="#D2E2F6">
<P ALIGN=Right>
<INPUT TYPE=hidden NAME=action VALUE=sendmail>
<INPUT TYPE=submit VALUE="Send E-Mail">
</TD>
  </TR>
</TABLE>
    </TD>
  </TR>
</TABLE>


</FORM>
~;
print_bottom();
}

##################
sub sendmail {
##################

if ($input{'toemail'} eq "") {
$errormsg = "<FONT COLOR=red>Please fill in the fields marked with an *</FONT>";
$input{'action'} = "retry";
$noemail = "<FONT COLOR=red>*</FONT>";
&send;
exit; }

if ($input{'subject'} eq "") {
$errormsg = "<FONT COLOR=red>Please fill in the fields marked with an *</FONT> ";
$input{'action'} = "retry";
$noemail = "<FONT COLOR=red>*</FONT>";
&send;
exit; }

if ($input{'body'} eq "") {
$errormsg = "<FONT COLOR=red>Please fill in the fields marked with an *</FONT>";
$input{'action'} = "retry";
$noemail = "<FONT COLOR=red>*</FONT>";
&send;
exit; }

open (MAIL, "| $mailprog -t") || die "Can't open $mailprog"; # -oi
print MAIL "To: $input{'toemail'}\n";
print MAIL "Reply-to: $username\@$DOMAIN\n";
print MAIL "From: $username\@$DOMAIN\n";
print MAIL "Subject: $input{'subject'}\n\n";
print MAIL "$input{'body'}\n";
close (MAIL);


print "Location: $SCRIPTURL\n\n";
}

##################
sub delete {
##################
$i = $input{'message'};

$pop = new Mail::POP3Client( USER => $USER , PASSWORD => $PASSWORD , HOST => $HOST , AUTH_MODE => "PASS" , DEBUG => $input{'DEBUG'});
    $pop->Delete($i);
    $popstate = $pop->State();
  $pop->Close();

  open(FILE, "$memberdir/$username.ema");
file_lock(FILE);
chomp(@prefemal = <FILE>);
unfile_lock(FILE);
close(FILE);

$newemal = $prefemal[0] - 1;

open(FILE, ">$memberdir/$username.ema");
file_lock(FILE);
print FILE "$newemal\n";
unfile_lock(FILE);
close(FILE);

print "Location: $SCRIPTURL\n\n";
}