####################################
##                                ##
##             REMOTE             ##
##  CopyRight Byron Chilton 2000  ##
##      http://www.d0tt.com       ##
##                                ##
####################################

## Sites name (exp. D0TT.coms Remotly Hosted Stuff)
$site_name = "CGI Joe!!";

## Path to where the data files will be kept
$data_path = "/home/erenetw/public_html/cgi-bin/dat";

## Your servers mail program
$mailprog = "/usr/sbin/sendmail";

## Your email address (make sure there is a \ before the @)
$email = "webmaster\@cgijoe.com";

## Sites Homepage URL
$home_page = "http://www.erenetwork.com/";

## Dectory for counter images
$image_directory = "/home/erenetw/public_html/counter";

## HTML dectory for counter images
$html_image_directory = "http://www.erenetwork.com/counter";

## Path to fly program (Read the ReadMe.txt
$flyprog = "/home/erenetw/public_html/cgi-bin/fly-1.6.5/fly -q";

## HTML path to cgis
$html_cgi_path = "http://www.erenetwork.com.com/cgi-bin";

## Path to where the postcards will be kept
$postcard_path = "/home/erenetw/public_html/cgi-bin/post";

##############################
##  This is where you edit  ##
##  the look of your page   ##
##  This is not required    ##
##  for Remote to work      ##
##############################

## Header for login and add pages
sub header {
print <<"HTML";
HTML
}

## Member login form
sub login_form {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>CGI Joe - Members Login!</TITLE>
</HEAD>
<BODY BGCOLOR="#ffffff" TEXT="#000000" LINK="#000000" VLINK="#000000">
<TABLE BORDER="0" CELLSPACING="1" WIDTH="675">
  <TR>
    <TD><IMG SRC="http://www.erenetwork.com/logo.gif" WIDTH="224" HEIGHT="107"></TD>
    <TD VALIGN="Top"><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
  </TR>
  <TR>
    <TD COLSPAN=2><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR>
	  <TD><A HREF="http://www.cgijoe.com/"><IMG SRC="http://www.erenetwork.com/home.gif"
		WIDTH="95" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><A HREF="http://www.erenetwork.com/cgi-bin/login.cgi?add"><IMG SRC="http://www.erenetwork.com/signup.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><IMG SRC="http://www.erenetwork.com/login.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></TD>
	  <TD><A HREF="http://www.erenetwork.com/help"><IMG SRC="http://www.erenetwork.com/help.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD width="40%"></TD>
	</TR>
	<TR>
	  <TD COLSPAN=5><IMG SRC="http://www.erenetwork.com/bar3.gif" WIDTH="630" HEIGHT="11"></TD>
	</TR>
      </TABLE>
    </TD>
  </TR>
  <TR>
    <TD COLSPAN=2 VALIGN="Top"><CENTER>
	<P>
	<TABLE BORDER CELLSPACING="1" BORDERCOLOR=#0000ff ALIGN="Center">
	  <TR>
	    <TD BGCOLOR=#000000><P ALIGN=Center>
	      <FONT COLOR="#ffffff"><B>Members Login!!</B></FONT></TD>
	  </TR>
	  <TR>
	    <TD><FORM ACTION="login.cgi" METHOD="POST">
		<TABLE BORDER="0" CELLPADDING="2">
		  <TR>
		    <TD>Username:</TD>
		    <TD>
		      <INPUT TYPE="text" NAME="user" SIZE="12"></TD>
		  </TR>
		  <TR>
		    <TD>Password:</TD>
		    <TD>
		      <INPUT TYPE="password" NAME="pass" SIZE="12"></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><P ALIGN=Center>
		      <INPUT TYPE="hidden" NAME="a" VALUE="login"> 
		      <INPUT TYPE=submit VALUE="Login"></TD>
		  </TR>
		</TABLE>
	      </FORM>
	    </TD>
	  </TR>
	</TABLE>
	<P>
	<A href="http://www.onResponse.com/onr_ads.asp?a=9395&amp;d=13"> Click here</A>
	To get Gator for FREE and never have to rember your username and passwords
	agine. Gator stores your passwords and outher info on your hard drive so
	theres no chance of anyone seeing them. All for FREE.
	<P>
	Not a member yet?<BR>
	<A HREF="login.cgi?add">Join Now!!</A>
      </CENTER>
    </TD>
  </TR>
</TABLE>
<P ALIGN=Center>
</BODY></HTML>
HTML
}

## Member sign up form
sub add_form {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>CGI Joe - Sign Up!</TITLE>
</HEAD>
<BODY BGCOLOR="#ffffff" TEXT="#000000" LINK="#000000" VLINK="#000000">
<TABLE BORDER="0" CELLSPACING="1" WIDTH="675">
  <TR>
    <TD><IMG SRC="http://www.erenetwork.com/logo.gif" WIDTH="224" HEIGHT="107"></TD>
    <TD VALIGN="Top"><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
  </TR>
  <TR>
    <TD COLSPAN=2><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR>
	  <TD><A HREF="http://www.cgijoe.com/"><IMG SRC="http://www.erenetwork.com/home.gif"
		WIDTH="95" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><IMG SRC="http://www.erenetwork.com/signup.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></TD>
	  <TD><A HREF="http://www.erenetwork.com/cgi-bin/login.cgi"><IMG SRC="http://www.erenetwork.com/login.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><A HREF="http://www.erenetwork.com/help"><IMG SRC="http://www.erenetwork.com/help.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD width="40%"></TD>
	</TR>
	<TR>
	  <TD COLSPAN=5><IMG SRC="http://www.erenetwork.com/bar2.gif" WIDTH="630" HEIGHT="11"></TD>
	</TR>
      </TABLE>
    </TD>
  </TR>
  <TR>
    <TD COLSPAN=2 VALIGN="Top"><CENTER>
	<P>
<CENTER>		<FORM ACTION="login.cgi" METHOD="POST">
		  <CENTER>
		    <TABLE BORDER CELLPADDING="2" ALIGN="Center" BORDERCOLOR=#0000ff>
		      <TR>
			<TD COLSPAN=2 BGCOLOR=#000000><P ALIGN=Center>
			  <FONT COLOR="#ffffff"><BIG>Sign Up For $site_name</BIG></FONT></TD>
		      </TR>
		      <TR>
			<TD>Username:</TD>
			<TD>
			  <INPUT TYPE="text" NAME="user"></TD>
		      </TR>
		      <TR>
			<TD>Password:</TD>
			<TD>
			  <INPUT TYPE="text" NAME="pass"></TD>
		      </TR>
		      <TR>
			<TD>E-Mail:</TD>
			<TD>
			  <INPUT TYPE="text" NAME="mail"></TD>
		      </TR>
		      <TR>
			<TD>Webpage URL:</TD>
			<TD>
			  <INPUT TYPE="text" NAME="url" VALUE="http://"></TD>
		      </TR>
		      <TR>
			<TD>Site Title:</TD>
			<TD>
			  <INPUT TYPE="text" NAME="site_title"></TD>
		      </TR>
		      <TR>
			<TD COLSPAN=2><P ALIGN=Center>
			  <INPUT TYPE="hidden" NAME="a" VALUE="add"> 
			  <INPUT TYPE=submit VALUE="Sign Up"></TD>
		      </TR>
		    </TABLE>
		    <P>
		    <A HREF="login.cgi">Members Login!!</A>
		  </CENTER>
		</FORM>
	      </CENTER>

	    </TD>
	  </TR>
	</TABLE>
	<P>
	<A href="http://www.onResponse.com/onr_ads.asp?a=9395&amp;d=13"> Click here</A>
	To get Gator for FREE and never have to rember your username and passwords
	agine. Gator stores your passwords and outher info on your hard drive so
	theres no chance of anyone seeing them. All for FREE.
	<P>
      </CENTER>
    </TD>
  </TR>
</TABLE>
<P ALIGN=Center>
</BODY></HTML>
HTML
}

## Thank you message displayed when user signs up
sub thank_you {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>CGI Joe - Thank You!</TITLE>
</HEAD>
<BODY BGCOLOR="#ffffff" TEXT="#000000" LINK="#000000" VLINK="#000000">
<TABLE BORDER="0" CELLSPACING="1" WIDTH="675">
  <TR>
    <TD><IMG SRC="http://www.erenetwork.com/logo.gif" WIDTH="224" HEIGHT="107"></TD>
    <TD VALIGN="Top"><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
  </TR>
  <TR>
    <TD COLSPAN=2><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR>
	  <TD><A HREF="http://www.erenetwork.com/"><IMG SRC="http://www.erenetwork.com/home.gif"
		WIDTH="95" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><A HREF="http://www.erenetwork.com/cgi-bin/login.cgi?add"><IMG SRC="http://www.erenetwork.com/signup.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><A HREF="http://www.erenetwork.com/cgi-bin/login.cgi"><IMG SRC="http://www.erenetwork.com/login.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><A HREF="http://www.cgijoe.com/help"><IMG SRC="http://www.erenetwork.com/help.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD width="40%"></TD>
	</TR>
	<TR>
	  <TD COLSPAN=5><IMG SRC="http://www.erenetwork.com/bar1.gif" WIDTH="630" HEIGHT="11"></TD>
	</TR>
      </TABLE>
    </TD>
  </TR>
  <TR>
    <TD COLSPAN=2 VALIGN="Top"><CENTER>
	<P>
<CENTER>
<B>Thank you for signing up for $site_name's Remotly Hosted Services!<BR>
Your account has been setup and is ready to use.<BR>
All of your member data has been emailed to you.<BR>
It is recommended that you print this email.<BR>
<A HREF=login.cgi>Click Here to login!</A></B>
</CENTER>

</BODY></HTML>
HTML
}

## Top frame in the members page
sub nav_frame {
print <<"HTML";
HTML
## Dont remove the following line
print "<noscript>";
}

## Main frame in the members page
sub main_frame {
print <<"HTML";
<HTML>
<HEAD>
  <TITLE>CGI Joe - Members!</TITLE>
</HEAD>
<BODY BGCOLOR="#ffffff" TEXT="#000000" LINK="#000000" VLINK="#000000">
<TABLE BORDER="0" CELLSPACING="1" WIDTH="675">
  <TR>
    <TD><IMG SRC="http://www.erenetwork.com/logo.gif" WIDTH="224" HEIGHT="107"></TD>
    <TD VALIGN="Top"><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
  </TR>
  <TR>
    <TD COLSPAN=2><TABLE BORDER="0" CELLSPACING="0" CELLPADDING="0">
	<TR>
	  <TD><A HREF="http://www.erenetwork.com/"><IMG SRC="http://www.erenetwork.com/home.gif"
		WIDTH="95" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><A HREF="http://www.erenetwork.com/cgi-bin/login.cgi?add"><IMG SRC="http://www.erenetwork.com/signup.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD><IMG SRC="http://www.erenetwork.com/login.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></TD>
	  <TD><A HREF="http://www.cgijoe.com/help"><IMG SRC="http://www.erenetwork.com/help.gif"
		WIDTH="90" HEIGHT="27" BORDER="0"></A></TD>
	  <TD width="40%"></TD>
	</TR>
	<TR>
	  <TD COLSPAN=5><IMG SRC="http://www.erenetwork.com/bar1.gif" WIDTH="630" HEIGHT="11"></TD>
	</TR>
      </TABLE>
    </TD>
  </TR>
  <TR>
    <TD COLSPAN=2 VALIGN="Top"><CENTER>
	<P>
<CENTER>		<TABLE BORDER="0" CELLPADDING="2">
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/memb.gif" WIDTH="397" HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD WIDTH=4%></TD>
		    <TD><A HREF=members.cgi?a=editinfo&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit
		      your member info</A><BR>
		      <A HREF=members.cgi?a=changepass&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Change
		      Your Password</A></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/cont.gif" WIDTH="397" HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD>
		      <A HREF=members.cgi?a=cont_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A><BR>
		      <A HREF=members.cgi?a=edit_cont&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit</A><BR>
		      </TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/clok.gif" WIDTH="397" HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD>
		      <A HREF=members.cgi?a=clock_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A><BR>
</TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/book.gif" WIDTH="397" HEIGHT="45"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD><A HREF=members.cgi?a=book_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A><BR>
		      <A HREF=members.cgi?a=edit_book&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit</A><BR>
		      <A HREF=members.cgi?a=edit_gb_entry&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit
		      Entrys</A></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/ffal.gif" WIDTH="397" HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD><A HREF=members.cgi?a=ffal_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A><BR>
		      <A HREF=members.cgi?a=edit_ffal&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit</A><BR>
		      <A HREF=members.cgi?a=edit_ffal_entry&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit
		      Entrys</A></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/mailL.gif" WIDTH="397"
			  HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD><A HREF=members.cgi?a=mail_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>code</A><BR>
		      <A HREF=members.cgi?a=edit_mail&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit
		      list entrys</A><BR>
		      <A HREF=members.cgi?a=edit_mail_thank&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit
		      thank you message</A><BR>
		      <A HREF=members.cgi?a=send_email&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Send
		      E-Mail</A></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/poll.gif" WIDTH="397" HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD><A HREF=members.cgi?a=poll_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A><BR>
		      <A HREF=members.cgi?a=poll_edit&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit</A><BR>
		      <A HREF=members.cgi?a=del_poll&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Delete</A></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/post.gif" WIDTH="397" HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD><A HREF=members.cgi?a=post_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A><BR>
		      <A HREF=members.cgi?a=edit_post&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Edit</A><BR>
		      <A HREF=members.cgi?a=add_post_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Add
		      Images</A><BR>
		      <A HREF=members.cgi?a=del_post_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Delete
		      Images</A></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/mailF.gif" WIDTH="397"
			  HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD><A HREF=members.cgi?a=email_form_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A></TD>
		  </TR>
		  <TR>
		    <TD COLSPAN=2><IMG SRC="http://www.erenetwork.com/rand.gif" WIDTH="397" HEIGHT="44"></TD>
		  </TR>
		  <TR>
		    <TD></TD>
		    <TD><A HREF=members.cgi?a=add_rand_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Add
		      image</A><BR>
		      <A HREF=members.cgi?a=del_rand_img&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Delete
		      images</A><BR>
		      <A HREF=members.cgi?a=rand_code&user=$INPUT{'user'}&pass=$INPUT{'pass'}>Code</A></TD>
		  </TR>
		</TABLE>

</BODY></HTML>
HTML
}

###########
# scripts #
###########

## GuestBook header
sub gbheader {
print <<"HTML";
<BODY TEXT="$text" LINK="$link" VLINK="$vlink" BGCOLOR="$bg" BACKGROUND="$image">
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD><A HREF="http://www.erenetwork.com"><IMG SRC="http://www.erenetwork.com/logo.gif"
	    WIDTH="224" HEIGHT="107" BORDER="0"></A></TD>
      <TD><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<SMALL>GuestBook Provided By <A HREF="http://www.cgijoe.com">CGI Joe!!</A></SMALL></TD>
    </TR>
  </TABLE>
</CENTER>
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
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD><A HREF="http://www.erenetwork.com"><IMG SRC="http://www.erenetwork.com/logo.gif"
	    WIDTH="224" HEIGHT="107" BORDER="0"></A></TD>
      <TD><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<SMALL>Free for all Links Provided By <A HREF="http://www.cgijoe.com">CGI Joe!!</A></SMALL></TD>
    </TR>
  </TABLE>
</CENTER>
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
<A HREF="$home_page">Free for all Links Provided by $site_name</A>
</CENTER> 
HTML
}

## Mailing header
sub mlheader {
print <<"HTML";
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD><A HREF="http://www.cgijoe.com"><IMG SRC="http://www.erenetwork.com/logo.gif"
	    WIDTH="224" HEIGHT="107" BORDER="0"></A></TD>
      <TD><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<SMALL>Mailing List Provided By <A HREF="http://www.cgijoe.com">CGI Joe!!</A></SMALL></TD>
    </TR>
  </TABLE>
</CENTER>
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
<CENTER>
  <TABLE BORDER="0" CELLPADDING="2" ALIGN="Center">
    <TR>
      <TD><A HREF="http://www.cgijoe.com"><IMG SRC="http://www.erenetwork.com/logo.gif"
	    WIDTH="224" HEIGHT="107" BORDER="0"></A></TD>
      <TD><SCRIPT LANGUAGE="JavaScript" SRC="http://www.erenetwork.com/ban/banners.js"></SCRIPT></TD>
    </TR>
    <TR>
      <TD COLSPAN=2><P ALIGN=Center>
	<SMALL>PostCards Provided By <A HREF="http://www.cgijoe.com">CGI Joe!!</A></SMALL></TD>
    </TR>
  </TABLE>
</CENTER>
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