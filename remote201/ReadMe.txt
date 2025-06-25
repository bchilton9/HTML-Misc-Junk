####################################
##                                ##
##          REMOTE 2.0            ##
##  CopyRight Byron Chilton 2000  ##
##      http://www.d0tt.com       ##
##                                ##
####################################

Installation
Directory Map
Installing Fly
Adding more images to counter
Adding more images to clock
Troubleshooting

####################
##  Installation  ##
####################

Set up all the variables in the config.pl
If your path to perl isen't "/usr/bin/perl"
open all the cgis and make the top line your path to perl
if you are un sure ask your servers administrator
upload all the cgis, pls, and txt files to your cgi-bin in ASCII
chmod the cgis to 755
In the cgi-bin make 2 directorys called "data" and "post"
(or what eaver you names them in the config.pl)
chmode the folders to 777

In your broser open the login.cgi and test everything and make sure it works

You can customise the look of your site by changing headers and footers
in the config.pl

#####################
##  Directory Map  ##
#####################

Root (Directory)
 |
 |_ cgi-bin (Directory) chmod 777
 |    |
 |    |_ data (Directory) chmod 777
 |    |_ post (Directory) chmod 777
 |    |_ login.cgi (Program) chmod 755
 |    |_ members.cgi (Program) chmod 755
 |    |_ counter.cgi (Program) chmod 755
 |    |_ config.pl (Configurashen) chmod 755
 |
 |_ countergifs (Directory)
      |
      |_ 1 (Directory)
      |   |
      |   |_0.gif - 9.gif (Images)
      |
      |_ 2 (Dectory)
          |
          |_0.gif - 9.gif (Images)

######################
##  Installing Fly  ##
######################

REMOTES counter and clock script REQUIRES Fly to combined the images
The Fly zip file was included in the REMOTE zip file
There is installation instructions in the zip folder
or visit the Fly homepage at:
http://www.unimelb.edu.au/fly/
If you have purchased this script and cannot install Fly
I will install it for you free of charge.
Just email me at: webmaster@d0tt.com

####################################
## Adding more images to counter  ##
####################################

In your cgi folder there is a file called cont.txt
open this file the data in it looks like A::B::C
A = Folder name of counterimages
B = Width
C = Height
Example if you have your 0.gif-9.gif in a folder called "basic"
and the images are 15 pixels high and 13 wide your line whould look like
   basic::15::13
You can have as many as you want just put the new ones on a different line
   basic::15::13
   basic1::13::11
   basic2::20::20
ALL IMAGES IN ONE FOLDER MUST BE THE SAME SIZE

##################################
## Adding more images to clock  ##
##################################

The clock uses the same format as the counter (exp. A::B::C)
the file is called clock.txt
The images can be the same ones used for the counters
BUT the images folders MUST HAVE 3 extra images
an image of : called -.if
an image of A.M. called a.gif
an image of P.M. called p.gif
If these are not in the folder the clock wont work
ALL IMAGES IN ONE FOLDER MUST BE THE SAME SIZE

#####################
## Troubleshooting ##
#####################

Counter or clock shows up as a broken image.
1. cont.txt or clock.txt isen't setup right
2. Fly isent installed or installed incorctly
3. Path to perl in counter.cgi or clock.cgi is incorect
4. counter.cgi or clock.cgi isent chmod to 755
5. counter.cgi or clock.cgi wasent uploaded in ASCII
6. images arent in spesafied folder
7. comfig.pl is setup incorectly

Get a 500 error
1. cgi wasen't uploaded in ASCII
2. cgi isen't chmoded to 755
3. Path to perl in cgi is incorrect
4. config.pl is setup incorrectly
5. You changed something in the cgis you shouldn't have

All cgis get a 500 error
Something in the config.pl is setup incorrectly
Try reunziping the config.pl agine and start over