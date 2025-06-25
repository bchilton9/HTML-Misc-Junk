#################################################################
#             Message Board V4.5.1 (Freeware)
#
# This program is distributed as freeware. We are not            	
# responsible for any damages that the program causes	
# to your system. It may be used and modified free of 
# charge, as long as the copyright notice
# in the program that give me credit remain intact.
# If you find any bugs in this program. It would be thankful
# if you can report it to us at cgifactory@cgi-factory.com.  
# However, that email address above is only for bugs reporting. 
# We will not  respond to the messages that are sent to that 
# address. If you have any trouble installing this program. 
# Please feel free to post a message on our CGI Support Forum.
# Selling this script is absolutely forbidden and illegal.
##################################################################
#
#               COPYRIGHT NOTICE:
#
#         Copyright 1999-2001 CGI-Factory.com TM 
#		  A subsidiary of SiliconSoup.com LLC
#
#
#      Web site: http://www.cgi-factory.com
#      E-Mail: cgifactory@cgi-factory.com
#      Released Date: Junuary 13, 2001
#	
#   Message Board V4.5.1 is protected by the copyright 
#   laws and international copyright treaties, as well as other 
#   intellectual property laws and treaties.
###################################################################


Installation 

How do I install Message Board V4.5.1 (Freeware)?


Unfortunately, MB V4.5.1 doesn't work with the old message files from any previous version of the message board
products. So you will need to restart
the board.

*It is suggested that you create a sub directory under your cgi-bin then install the scripts there. 
For example, /cgi-bin/messageboard

1) If the path to perl on your server is different from
#!/usr/local/bin/perl 
then you will need to change it on the first line in view.pl ,message.pl, and configur.pl



2) Open all footer and header files separately with a text editor and modify them 
to fit the lay out of your web site. (header.txt, footer.txt, vheader.txt, and vfooter.txt)

header.txt and footer.txt are for the layout of each message post
vheader.txt and vfooter.txt are for the message board index page



3) Upload all files (including the folders and all files under it) but the image files to your cgi-bin in ASCII(plain text).
(errorlog.txt, header.txt, footer.txt, vheader.txt, vfooter.txt, superuser.db, vcfg.pl, mcfg.pl, mgcfg.pl, 
view.pl, message.pl, setup.pl, configur.pl, enotify.pl, data(dir), board1.bd, ,board1.txt, misc(dir))

Warning: do not upload icons and cookie.js into your cgi-bin. Icons have to be uploaded in binary mode and cookie.js has
be to uploaded in ASCII mode.

Please visit our FAQ section <http://www.cgi-factory.com/faq.shtml>
if you want to know how to upload a file in ASCII mode.



4) Chmod all *.pl files to permission "755." 
(Chmod mcfg.pl, vcfg.pl, mgcfg.pl, view.pl, message.pl, and configur.pl to permission "755")

*However, if you get a permission denied message when you save the configurations, you will need to
chmod mcfg.pl, vcfg.pl, and mgcfg.pl to permission "777." Please check out our faq section for chmoding files info.


5) Chmod all *.txt and *.db files to permission "755" first. However, chmoded them to "777" only when you get a 
permission denied message. For example, a permission denied message when you save your superuser name and password.  
(errorlog.txt, header.txt, footer.txt, vheader.txt, vfooter.txt, forbid.txt, superuser.db, board1.bd(under the data directory), and board1.txt(under the data directory))

Please visit our FAQ section <http://www.cgi-factory.com/support/faq.shtml> if you want to know how to chmod a file.



6) Execute setup.pl with your browser (point the browser to http://www.your_site.com/cgi-bin/setup.pl)



7) Set the superuser admin name and password then reload the browser to set the configurations.

System pathes should look somewhat like /web/home/httpd/cgi-bin... or e:/inetpub/cgi/...
Usually, you can obtain the system path from your server admin. 
If you can use telnet to access your server, type in "pwd" after you have logged in. 
The PWD command will return your current system path.



8) Create the directory that you've set the path in configur.pl for storing the message files under board configuration section. Chmod it
to permission "755".

*However, if you get a permission denied message when you add a new board, you will need to
chmod this data directory to permission "777."

9) Make a link to view.pl, it will be your message board main page. If you want to change your color settings, point your browser to configur.pl.

Important note for windows servers users: 

You need to open 
message.pl, view.pl, setup.pl, and configur.pl, 
then modify $fullpath to your full system path. 

