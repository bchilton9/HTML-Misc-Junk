User Gallery Mod - v1.5 (Pre-G.O.M.E.S Version)
By: Floyd (webmaster@diminishedresponsibility.co.uk)
December 2002

###############################################################################
License
###############################################################################

This Mod may be freely distributed or modified under the terms of the GNU General Public License.  However, if you improve and/or redistribute it, please notify me so I know how the script is being used and/or improved!

################################################################################
History
################################################################################

v1.0 - First Release. 21st October 2002
v1.1 - Bug Fixes and Security Update. 23rd October 2002
v1.2 - Upload Script Improvements. (NB: NOT RELEASED)
v1.3 - Picture Views now Counted. (NB: NOT RELEASED)
v1.4 - Bug Fixes. (NB: NOT RELEASED)
v1.5 - New & Hot Pictures Noted. Uses v0.9.8 Error & Date Formatting. 12th December 2002

NOTE: THIS WILL BE THE LAST UPDATE OF USER GALLERY AS A STAND ALONE MOD. FURTHER DEVELOPMENT WILL BE VIA THE G.O.M.E.S SYSTEM.

################################################################################
Bugs
################################################################################

22nd October 2002 - Album ID number not passed to final part of upload script. Fix applied to v1.1.
22nd October 2002 - Unauthorised use of HTML and/or "bad language" in Album/Picture descriptions. Fix applied to v1.1.
24th October 2002 - "temp" folder missing in release package. (NOTE: NOW NO LONGER REQUIRED!)
5th December 2002 - Conversion Script confuses counter files for images.

NOTE: THIS WILL BE THE LAST UPDATE OF USER GALLERY AS A STAND ALONE MOD. FURTHER DEVELOPMENT WILL BE VIA THE G.O.M.E.S SYSTEM.

################################################################################
Overview
################################################################################

The User Gallery Mod is a versatile Picture Gallery for your WebAPP powered site. A wide selection of Admin Options allows the creation of a Standard Picture Gallery or an interactive Gallery where your Members may create Albums and upload Pictures.

Please read the instructions carefully and in a few minutes, you should have a Picture Gallery on your site to be proud of!

################################################################################
Pre-Installation/Upgrade Warning!
################################################################################

User Gallery v1.5 uses routines unique to WebAPP v0.9.8 and is thus not compatable with pre v0.9.8 versions of the WebAPP system. Please upgrade your site to v0.9.8 before installing or upgrading User Gallery.

################################################################################
Installation
################################################################################

First, you should unzip usergallery.zip to your computer as there is some editing that you need to do!

Next, edit the path to perl in index.cgi, ugupload.cgi, ugconvert.cgi (see below) and admin.cgi.

Once you have done this, you can save all the scripts, and upload the usergallery folder to your mods directory in ASCII mode except the gfx folder which should be uploaded in BINARY mode (see note below regarding graphics in your cgi-bin).

CHMOD all the .cgi files 755 (see also ugconvert.cgi below), then go to your images folder, and make a folder called usergallery, then open the usergallery folder and make a folder called pending. It should then look something like this...

images/usergallery
images/usergallery/pending

CHMOD these folders 777 (you may have to CHMOD the images folder 777 too, it depends on your server!)

You may wish to also install the User Gallery Plugins (see below). Open ugplugin.txt and copy the contents to your cgi-lib/plugins.pl file where you want the Plugin to be displayed.

################################################################################
Upgrading
################################################################################

If you already use User Gallery just upload all the .cgi and .pl files in ASCII mode to the mods/usergallery and mods/usergallery/admin folders.

Next, upload english.dat in ASCII mode to the mods/usergallery/language folder.

There are two new icons that need to be uploaded to the usergallery/gfx folder. Do this in BINARY mode!

Go to User Gallery Admin and click "Setup". There are three new options which need setting up. Choose for how long you wish new Albums and Pictures to be shown as "New" and how many views a Picture needs before it is "Hot".

There are now 4 built-in Plugins (see below). If you don't change the entry in plugins.pl you will retain the default "Picture of the Moment" plugin.

You can delete the db/temp folder as it is no longer required!

################################################################################
User Gallery Plugins
################################################################################

Included in User Gallery v1.5 are four plugins! The original "Pic of the Moment" plugin remains, but it has been joined by a "Top 10 Pictures" plugin and two Admin Plugins.

Pic of the Moment (ugdisplay(0);) - Shows a random picture from your gallery.

Top 10 Pictures (ugdisplay(1);) - Shows a list of the Top 10 most viewed pictures.

Admin Monitor (ugdisplay(2);) - Shows to the Admin if there are any pictures that need approval.

Administrator Monitor (ugdisplay(3);) - Shows to All Administrators if there are any pictures that need approval.

You only need to use one of the Monitors, and depending on your setup you may use the most appropriate.

If you leave "ugdisplay();" in your plugins.pl file then you will get the default "Pic of the Moment" display.

################################################################################
Using Graphics in your cgi-bin folder
################################################################################

If You have problems showing images contained within the cgi-bin, 
you may have to move the mods/usergallery/gfx folder to your images folder. 
If you have to do this, don't forget to change the 
$usergallerygfxurl & 
$usergallerygfxdir 

variables in usergallery.cfg to point to the correct folder.

################################################################################
ugconvert.cgi
################################################################################

If you are already using the Gallery Mod by Judhi (updated by Keatoh) you may use this utility to convert your old gallery to this one!

This should be run once only and then removed from your server. The script also only copies the original pictures, so they should be quite safe! If you don't intend to use this, don't forget to remove it from your server!

Go to http://www.yoursite.com/cgi-bin/mods/usergallery/ugconvert.cgi, confirm the paths to your old and new galleries picture folders and press the "Start" button.

The script will assume the following folder layout...

images/gallery/
images/gallery/folder1/
images/gallery/folder2/
images/gallery/folder3/

...it will ignore any "thumbnail" folders (ie. images/gallery/folder2/thumbnail) and any images in the root images/gallery folder. If you have placed any other file in the images/gallery folder, these will be ignored. As UserGallery is set up for .jpg (.jpeg) & .gif files only, other file formats will be ignored!

It doesn't matter what the "gallery" folder is called as long as you've entered the correct path to the base folder the script will know what to do.

If you have used captions for your pictures by using "picture.ext.txt" ( see http://www.web-app.org/modapp/cgi-bin/index.cgi?action=viewnews&id=22 if you're unsure ), then the script will name your pictures the same!

The script will create Albums named after the folder name and copy the images to the images/usergallery folder. All images will be renamed and sequenced in the Albums data files. Once it has finished you will be sent to the Album list and hopefully you'll see your old gallery in the new one! Please check it out before you do anything else!

Once you have converted your old gallery to the new one (and you have checked that it's working properly!), you may delete your old gallery picture folder and mods/gallery folder.

If it hasn't worked, you'll have to upload each picture to the new gallery, just copying the images over won't work!

If it did work, don't forget to delete ugconvert.cgi from your server and alter any links to the Gallery Mod to the User Gallery Mod!

################################################################################
Use
################################################################################

Go to http://www.yoursite.com/cgi-bin/mods/usergallery/index.cgi and if everything is OK, you should see a message that says "There are no albums to view!" (unless you have used ugconvert.cgi - see above) and a link that says "Create an Album". If you click that link, you will be presented with a text box and a checkbox. Enter the name of the Album in the text box (maximum 30 characters). If you want to allow other members to post in this album, put a tic in the check box. Click the create button and you will return to the Album List and the new album will be displayed.

Now you have an Album created, you'll want to add some pictures! Click on the "Add a Picture" link/icon and you'll see a "Browse" box. Click on the "Browse" button and select an image from your HD. Click on the "Submit" button and if the image is successfully uploaded you'll be able to enter a description of the picture. Once you have clicked the "Complete" button, you should see your picture in the folder.

Depending on your access settings, users who upload pictures will need them approved before they appear. You have to approve them! Go to http://www.yoursite.com/cgi-bin/mods/usergallery/admin/admin.cgi and you should see a screen with a link that says "Verify Pictures". Click it and you will get a page showing you all the submitted pictures. You can edit the Picture Name if you wish and you can click on the thumbnail to see the complete image! If you click the "Publish" button under a picture, the script will then set up all the data files for the picture and copies (The script uses the File::Copy module, which should be a standard module on your server!) the image file from the images/usergallery/pending folder to the images/usergallery folder, it then deletes the original file from the images/usergallery/pending folder and removes it from the list. If you click the "Delete" button, the file is simply removed from both the list and the server! NOTE! The image is renamed if it's approved! This is normal and prevents accidental overwriting of other pictures of the same name.

NOTE: Any pictures uploaded by "Admin" will always be published automatically!

Go back to http://www.yoursite.com/cgi-bin/mods/usergallery/index.cgi and you should see the picture in the Album it was submitted to!

################################################################################
Admin Tools
################################################################################

The Admin section of the script allows you to Publish pictures submitted by members (if "AutoPublish" is off) and set up the access controls and number of Albums & Pictures displayed on each page (8 (Default Setting), 12, 16, 20 & 24).

The access settings should be fairly self-explanitory, but just in case...

# Create Album & Post Pictures = Admin, View Gallery = Members, AutoPublish = Off

Only the Admin may create new albums and post pictures and only members may view them. Admin views ALL pictures before they are published!

# Create Album & Post Pictures = Admin, View Gallery = All, AutoPublish = Off

Only the Admin may create new albums and post pictures and anyone may view them. Admin views ALL pictures before they are published! (Default Setting)

# Create Album = Admin, Post Pictures = Members, View Gallery = Members, AutoPublish = Off

Only the Admin may create new albums but Members may post pictures. Only members may view them. Admin views ALL pictures before they are published!

# Create Album = Admin, Post Pictures = Members, View Gallery = All, AutoPublish = Off

Only the Admin may create new albums but Members may post pictures. Anyone may view them. Admin views ALL pictures before they are published!

# Create Album & Post Pictures = Members, View Gallery = Members, AutoPublish = Off

Members may create new albums and post pictures. Only members may view them. Admin views ALL pictures before they are published!

# Create Album & Post Pictures = Members, View Gallery = All, AutoPublish = Off

Members may create new albums and post pictures. Anyone may view them. Admin views ALL pictures before they are published!

# Create Album & Post Pictures = Members, View Gallery = Members, AutoPublish = On

Members may create new albums and post pictures. Only members may view them. Pictures are published automatically!

# Create Album & Post Pictures = Members, View Gallery = All, AutoPublish = On

Members may create new albums and post pictures. Anyone may view them. Pictures are published automatically!

Decreasing the accessability settings after your UserGallery has been in use isn't recommended as it could lead to confusion. If you have previously allowed Members to create albums and post pictures and then change it to "Admin Only", they may have albums that they can no longer control!

################################################################################
Other Features
################################################################################

Albums are "owned" by their creators. Pictures may be moved from one album to another (provided the Member "owns" more than one album).

Albums may be renamed, deleted or the access (see below) may be changed by the Albums Owner.

Pictures may be renamed or deleted by the pictures "owner".

Albums may be "Open Access" or "Limited Access". Anyone may post a picture to an "Open Access" Album, however only the Albums' "owner" may post a picture to a "Limited Access" album.

NOTE: The Admin is not restricted by "ownership" or "Limited Access" settings.

################################################################################
New Features in v1.5
################################################################################

The Number of days an Album or Picture is shown as "New" may be set from the Admin Section.

If a picture has been viewed more than 25, 50, 75 or 100 (Admin set) times a "Hot" marker is shown.

Failed Upload Attempts are recorded and this record may be viewed and/or reset from the Admin Section.

Access to the Admin section is controlled by the Admin. Admins may choose to allow their Administrators access to the Picture Approval sections. However, all other sections are now "Admin Only".

################################################################################
Further Development
################################################################################

As I stated above, this will be the LAST update of User Gallery in its' present form.

If any Bug/Support issues arrise, please post a message at ModAPP (http://www.web-app.org/modapp/cgi-bin/index.cgi) and I will attempt to fix/answer your problems.

That should be it! Enjoy.

Floyd