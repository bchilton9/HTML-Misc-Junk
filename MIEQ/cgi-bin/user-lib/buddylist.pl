##########################
sub blist              
##########################
{
unless (-e("$memberdir/buddy")) 
{
   mkdir("$memberdir/buddy",0777);
   chmod(0777,"$memberdir/buddy");
}
#print qq~<tr><td colspan=5 align=center><B>$bud{'021'}</b></td></tr>
#<tr><td colspan=5>&nbsp;</td></tr>
# ~;

open(FILE, "<$memberdir/buddy/$username.txt");
file_lock(FILE);
my @buddydata = <FILE>;
unfile_lock(FILE);
close(FILE);
$maxcount = 0;
     @buddydata = (sort { lc($a) cmp lc($b) }@buddydata);

foreach (@buddydata) { 
     chomp;
$maxcount++;

open(FILE, "$datadir/log.dat"); 
      file_lock(FILE); 
      @entries = <FILE>; 
      unfile_lock(FILE); 
      close(FILE); 
      
   foreach $curentry (@entries) {
   chomp;			
$curentry =~ s/[\n\r]//g; ($name, $value) = split(/\|/, $curentry);
$listcount  = 0;
	if ($name eq "$_") {  print qq~<tr valign=top>
<td><img src="$imagesurl/buddy/on.gif"><a href="$pageurl/$cgi?action=imsend&to=$_">$_</a></td>
<td>&nbsp;</td><td><a href="$pageurl/$cgi?action=imsend&to=$_"><img src="$imagesurl/forum/message.gif" border=0 alt="$bud{'008'}"></a></td>
<td>&nbsp;</td><td><a href="$pageurl/$cgi?action=viewprofile&username=$_"><img src="$imagesurl/forum/profile.gif" border=0 alt="$bud{'005'}"></a></td></tr>~;}

} 
$listcount++; 

}
#print qq~<tr><td colspan=5>&nbsp;</td></tr>~;

}
##########################
#ADMIN FILES:            #
##########################
sub blistedit{
##########################

   unless (-e("$memberdir/buddy")) {
	mkdir("$memberdir/buddy",0777);
	chmod(0777,"$memberdir/buddy");
   }

if ($info{'buddy'} ne "") { 
           $buddy = $info{'buddy'}; }
   
        open(FILE, "<$memberdir/buddy/$username.txt");
          file_lock(FILE);
          my @buddydata = <FILE>;
          unfile_lock(FILE);
        close(FILE);
       @buddydata = (sort { lc($a) cmp lc($b) } @buddydata);
$navbar = "$btn{'014'} $bud{'001'}"; 
	print_top(); 
	print qq~ 
 <center><b><font 
face="verdana, arial, helvetica" size="2" 
 
color="#000066"><b>$bud{'001'}</b></font></b></center><p> 
<table width=100%><tr><td>
 <form action="$pageurl/$cgi?action=addbuddy" method="post" onSubmit="submitonce(this)"> 
 <center> <table  bgcolor="$titlebg" border="0" cellspacing="3" cellpadding="0"> 
  <tr> 
    <td bgcolor="$windowbg" valign=top align=right><br>$bud{'011'}</td> 
    <td bgcolor="$windowbg" valign=top><br>
      <input type="text" name="buddy" value="$buddy">
     <input type="submit" name="moda" value="$bud{'010'}"><br>~;
print qq~
 <input type="checkbox" name="buddy_im"><small>$bud{'015'}</small></td> 
    </td> 
  </tr> 
  </form> 
</table></center>
</td><td><br><center>
<table border="0" cellpadding="0" cellspacing="0" 
style="border-collapse: collapse" bordercolor="#111111" width="179">

  <tr>
    <td bgcolor="#225875" width="1" align=right valign=top height="10">
     </td>
    <td bgcolor="#225875" colspan="2" valign=top background="$imagesurl/buddy/bottom.gif" height="19" width="224"  align="center"><font 
face="verdana, arial, helvetica" size="2" 
 
color="#000066"><b>$bud{'001'}</b></font>    
    </td>
        <td bgcolor="#225875" width="4" align=left valign=top height="19">
    </td>
  </tr>

  <tr>
    <td width="4" bgcolor="#225875" height="19">&nbsp;</td>
    <td width="224" bgcolor="#FFFFFF" colspan="2" valign=top background="$imagesurl/buddy/top.gif" height="19" align="center">
   <img border=0 src="$imagesurl/buddy/group-3.gif" width="17" height="14"></td>
    <td width="4" bgcolor="#225875" height="19">&nbsp;</td>
  </tr>
<tr><td bgcolor="#225875"></td><td colspan=2>
  <center><table border="0"  width=100% cellspacing="0" cellpadding="0"> 
  <tr> 
  <td bgcolor="$windowbg"><b>$bud{'002'}</b></td> 
  <td bgcolor="$windowbg"><b>$msg{'226'}</b></td> 
~; 
 foreach (@buddydata) { 
     chomp; 
     print qq~<tr> 
     <td bgcolor="$windowbg"><a href="$pageurl/$cgi?action=viewprofile&username=$_"><img src="$imagesurl/forum/profile.gif" border=0></a> 
<a href="$pageurl/$cgi?action=imsend&to=$_">$_</a></td> 
     <td bgcolor="$windowbg">[<a href="$pageurl/$cgi?action=deletebuddy&amp;$ip=$_">$nav{'097'}</a>]</td> 
      ~; 
    } 
	print qq ~ 
 
  </table> </center>
</td><td bgcolor="#225875"></td></tr>
<tr><td colspan=4  bgcolor="#225875" background="$imagesurl/buddy/top.gif" height="19">&nbsp;</td></tr></table></center>
</td></tr></table>
<br><a href="$pageurl/$cgi?action=memberlist">$bud{'009'}</a>
<br><a href="$pageurl/$cgi?action=editprofile&username=$username">$nav{'016'}</a>
  ~; 
  print_bottom(); 
} 



################# 
sub addbuddy { 
################# 
if ($input{'buddy'} eq "$username") {
$navbar ="$btn{'014'} $bud{'020'}"; 
    print_top(); 
print qq~<b>$bud{'020'} </b><br>

    <br><br><p><b><a href="$pageurl/$cgi?action=blistedit">$bud{'001'}</a></b><br>
        <b><a href="$pageurl/$cgi?action=editprofile&username=$username">$nav{'016'}</a></b>  
    ~; 
    print_bottom(); 
} else {
 $navbar ="$btn{'014'} $bud{'010'}"; 
    print_top(); 
    if (-e("$memberdir/$input{'buddy'}.dat")) { } else { error("$err{'010'}"); }
    open (FILE , ">>$memberdir/buddy/$username.txt"); 
    file_lock(FILE); 
    print FILE "$input{'buddy'}\n"; 
    unfile_lock (FILE); 
    close (FILE); 



	if ($input{'buddy_im'} eq "on") {
      $username  = $username;
      $msgid = time;
      $imsubj = "$bud{'001'}";
      $formatmsg = qq~$bud{'018'}$username. $bud{'016'} $bud{'005'} $bud{'017'} <a href=$pageurl/$cgi?action=viewprofile&username=$username>$username</a>~;	

      open (FILE, "$memberdir/$input{'buddy'}.msg");
	file_lock(FILE);
	@imessages = <FILE>;
	unfile_lock(FILE);
	close (FILE);
	open (FILE, ">$memberdir/$input{'buddy'}.msg");
	file_lock(FILE);
	print FILE "$username|$imsubj|$date|$formatmsg|$msgid\n";
	foreach $curm (@imessages) { print FILE "$curm"; }
	unfile_lock(FILE);
	close(FILE);
}



    print "$input{'buddy'} $bud{'012'}"; 
    print qq ~ 
    <br><br><p><b><a href="$pageurl/$cgi?action=blistedit">$bud{'001'}</a></b><br>
        <b><a href="$pageurl/$cgi?action=editprofile&username=$username">$nav{'016'}</a></b>  
    ~; 
    print_bottom(); 
} 
}

#################### 
sub deletebuddy { 
#################### 
     
    		
    my %linea; 
    $navbar ="$btn{'014'} $bud{'013'}"; 
    print_top(); 
    print_top(); 
    open (FILE , "$memberdir/buddy/$username.txt");
    file_lock(FILE); 
    while (<FILE>) { 
    $li = $_; 
        chomp; 
        $linea{$_} = '1'; 
    } 
    unfile_lock (FILE); 
    close (FILE); 
    open (FILE2 , "+>$memberdir/buddy/$username.txt");
    foreach $clave (keys %linea) { 
            if ($clave eq $info{$ip}) { 
                $linea{$info{$ip}} = 0; 
                print "$info{$ip} $bud{'014'}"; 
            } 
            else { 
              print FILE2 "$clave\n"; 
            } 
 
    } 
    close (FILE2); 
    unfile_lock (FILE2); 
    print qq ~ 

    <p><b>$msg{'229'} $msg{'224'}</b> <br><br>
<br><a href="$pageurl/$cgi?action=memberlist">$bud{'009'}</a>
<br><a href="$pageurl/$cgi?action=blistedit">$bud{'006'}</a>
<br><a href="$pageurl/$cgi?action=editprofile&username=$username">$nav{'016'}</a>

    ~; 
    print_bottom(); 
} 
1;