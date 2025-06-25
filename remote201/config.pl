####################################
##                                ##
##             REMOTE             ##
##  CopyRight Byron Chilton 2000  ##
##      http://www.d0tt.com       ##
##                                ##
####################################

## Sites name (exp. D0TT.coms Remotly Hosted Stuff)
$site_name = "Sites Name";

## Path to where the data files will be kept
$data_path = "/home/erenet/erenet-www/cgi-bin/old/data";

## Your servers mail program
$mailprog = "/usr/sbin/sendmail";

## Your email address (make sure there is a \ before the @)
$email = "webmaster\@d0tt.com";

## Sites Homepage URL
$home_page = "http://www.site.com";

## Dectory for counter images
$image_directory = "/home/erenet/erenet-www/counter";

## HTML dectory for counter images
$html_image_directory = "http://208.56.60.37/counter";

## Path to fly program (Read the ReadMe.txt
$flyprog = "/home/erenet/erenet-www/cgi-bin/fly-1.6.5/fly -q";

## HTML path to cgis
$html_cgi_path = "http://208.56.60.37/cgi-bin";

## Path to where the postcards will be kept
$postcard_path = "/home/erenet/erenet-www/cgi-bin/post";

##############################
##  This is where you edit  ##
##  the look of your page   ##
##  This is not required    ##
##  for Remote to work      ##
##############################

## Header for login and add pages
sub header {
print <<"HTML";
<CENTER><H2><FONT COLOR=blue>$site_name</FONT></H2>
<SMALL>Ran with <A HREF=http://perl.d0tt.com>REMOTE 2.0</A></SMALL></CENTER><HR width=75%>
HTML
}

## Member login form
sub login_form {
print <<"HTML";
<FORM ACTION="login.cgi" METHOD="POST"><CENTER>
<TABLE BORDER CELLPADDING="2" ALIGN="Center"><TR>
<TD COLSPAN=2><P ALIGN=Center>
<BIG>Login To $site_name</BIG></TD>
</TR><TR><TD>UserName:</TD>
<TD><INPUT TYPE="text" NAME="user" SIZE="15"></TD>
</TR><TR><TD>Password:</TD><TD><INPUT TYPE="password" NAME="pass" SIZE="15">
</TD></TR><TR><TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE="hidden" NAME="a" VALUE="login"> 
<INPUT TYPE=submit VALUE="Login"></TD>
</TR></TABLE>
Not a member yet?<BR>
<A HREF="login.cgi?add">Join Now!!</A>
</CENTER></FORM>
HTML
}

## Member sign up form
sub add_form {
print <<"HTML";
<FORM ACTION="login.cgi" METHOD="POST">
<CENTER><TABLE BORDER CELLPADDING="2" ALIGN="Center">
<TR><TD COLSPAN=2><P ALIGN=Center>
<BIG>Sign Up For $site_name</BIG></TD>
</TR><TR><TD>Username:</TD><TD>
<INPUT TYPE="text" NAME="user"></TD>
</TR><TR><TD>Password:</TD>
<TD><INPUT TYPE="text" NAME="pass"></TD>
</TR><TR><TD>E-Mail:</TD>
<TD><INPUT TYPE="text" NAME="mail"></TD>
</TR><TR>
<TD>Webpage URL:</TD><TD>
<INPUT TYPE="text" NAME="url" VALUE="http://"></TD>
</TR><TR><TD>Site Title:</TD>
<TD><INPUT TYPE="text" NAME="site_title"></TD>
</TR><TR><TD COLSPAN=2><P ALIGN=Center>
<INPUT TYPE="hidden" NAME="a" VALUE="add"> 
<INPUT TYPE=submit VALUE="Sign Up">
</TD></TR></TABLE>
<A HREF="login.cgi">Members Login!!</A>
</CENTER></FORM>
HTML
}

## Thank you message displayed when user signs up
sub thank_you {
print <<"HTML";
<CENTER><B>Thank you for signing up for $site_name's Remotly Hosted Services!<BR>
Your account has been setup and is ready to use.<BR>
All of your member data has been emailed to you.<BR>
It is recommended that you print this email.<BR>
<A HREF=login.cgi>Click Here to login!</A></B></CENTER>
HTML
}

## Top frame in the members page
sub nav_frame {
print <<"HTML";
<Center>
<A HREF="members.cgi?a=main&user=$INPUT{'user'}&pass=$INPUT{'pass'}" TARGET="main">Reload main admin</A>
</CENTER>
HTML
## Dont remove the following line
print "<noscript>";
}

## Main frame in the members page
sub main_frame {
&member_header;
print <<"HTML";
<A HREF=members.cgi?a=editinfo&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit your member info</A><BR>
<A HREF=members.cgi?a=changepass&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Change Your Password</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=cont_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Counter Code</A><BR>
<A HREF=members.cgi?a=edit_cont&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit Counter</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=clock_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Clock Code</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=book_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>GuestBook Code</A><BR>
<A HREF=members.cgi?a=edit_book&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit GuestBook</A><BR>
<A HREF=members.cgi?a=edit_gb_entry&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit GuestBook Entrys</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=ffal_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Free for all links Code</A><BR>
<A HREF=members.cgi?a=edit_ffal&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit Free for all links</A><BR>
<A HREF=members.cgi?a=edit_ffal_entry&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit Free for all links Entrys</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=mail_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>E-Mail List code</A><BR>
<A HREF=members.cgi?a=edit_mail&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit E-Mail list entrys</A><BR>
<A HREF=members.cgi?a=edit_mail_thank&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit E-Mail thank you message</A><BR>
<A HREF=members.cgi?a=send_email&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Send E-Mail to mailing list</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=poll_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>WebPoll Code</A><BR>
<A HREF=members.cgi?a=poll_edit&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit Poll</A><BR>
<A HREF=members.cgi?a=del_poll&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Delete Webpoll</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=post_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Postcards Code</A><BR>
<A HREF=members.cgi?a=edit_post&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit Postcards</A><BR>
<A HREF=members.cgi?a=add_post_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Add Images to postcards</A><BR>
<A HREF=members.cgi?a=del_post_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Delete Images from postcards</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=email_form_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>E-Mail Form Code</A><BR>
<HR WIDTH="25%">
<A HREF=members.cgi?a=add_rand_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Add image to Random Image</A><BR>
<A HREF=members.cgi?a=del_rand_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Delete images from Random Images</A><BR>
<A HREF=members.cgi?a=rand_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Random Image Code</A><BR>
HTML
}

## Members page header
sub member_header {
print <<"HTML";
<Center><font color=blue><H3>$site_name</H3></font><HR width=70%>
HTML
}

## GuestBook header
sub gbheader {
print <<"HTML";
<BODY TEXT="$text" LINK="$link" VLINK="$vlink" BGCOLOR="$bg" BACKGROUND="$image">
<CENTER><H3>$heading</H3>
<A HREF="guestbook.cgi?a=sign&user=$INPUT{'user'}">Sign GuestBook</A><BR>
<A HREF="guestbook.cgi?a=view&user=$INPUT{'user'}">View GuestBook</A><BR>
<A HREF="$return">HomePage</A>
</CENTER><HR>
HTML
}

## GuestBook footer
sub gbfooter {
print <<"HTML";
<HR><CENTER>
<A HREF="guestbook.cgi?a=sign&user=$INPUT{'user'}">Sign GuestBook</A><BR>
<A HREF="guestbook.cgi?a=view&user=$INPUT{'user'}">View GuestBook</A><BR>
<A HREF="$return">HomePage</A><BR>
<A HREF="$home_page">GuestBooks Provided by $site_name</A>
</CENTER> 
HTML
}

## Free for all links header
sub ffheader {
print <<"HTML";
<BODY TEXT="$text" LINK="$link" VLINK="$vlink" BGCOLOR="$bg" BACKGROUND="$image">
<CENTER><H3>$heading</H3>
<A HREF="ffal.cgi?a=sign&user=$INPUT{'user'}">Add Link</A><BR>
<A HREF="ffal.cgi?a=view&user=$INPUT{'user'}">View Links</A><BR>
<A HREF="$return">HomePage</A>
</CENTER><HR>
HTML
}

## Free for all links footer
sub fffooter {
print <<"HTML";
<HR><CENTER>
<A HREF="ffal.cgi?a=sign&user=$INPUT{'user'}">Add Link</A><BR>
<A HREF="ffal.cgi?a=view&user=$INPUT{'user'}">View Links</A><BR>
<A HREF="$return">HomePage</A><BR>
<A HREF="$home_page">Free for all links Provided by $site_name</A>
</CENTER> 
HTML
}

## Mailing header
sub mlheader {
print <<"HTML";
HTML
}

## mailing footer
sub mlfooter {
print <<"HTML";
<HR><CENTER>
<A HREF="$home_page">Mailing list Provided by $site_name</A>
</CENTER> 
HTML
}

## Postcard header
sub postheader {
print <<"HTML";
<BODY TEXT="$text" LINK="$link" VLINK="$vlink" BGCOLOR="$bg" BACKGROUND="$image">
<CENTER><H3>$heading</H3>
HTML
}

## Postcard footer
sub postfooter {
print <<"HTML";
<HR><CENTER>
<A HREF="$home_page">Postcards Provided by $site_name</A>
</CENTER> 
HTML
}