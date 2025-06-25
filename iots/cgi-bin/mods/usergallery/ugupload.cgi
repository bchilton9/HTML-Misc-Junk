#!/usr/bin/perl
###############################################################################
###############################################################################
# ugupload.cgi for User Gallery                                               #
# Copyright (C) 2002 by Floyd (webmaster@diminishedresponsibility.co.uk)      #
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
# v1.0 - First Release. 21st October 2002                                     #
# v1.1 - Bug Fixes and Security Update. 23rd October 2002                     #
# v1.2 - Upload Script Improvements. (NB: NOT RELEASED)                       #
# v1.3 - Picture Views now Counted. (NB: NOT RELEASED)                        #
# v1.4 - Bug Fixes and Further Uploader Improvements. (NB: NOT RELEASED)      #
# v1.5 - New and Hot Pictures Noted. Final Code Tweeks. 12th December 2002    #
#                                                                             #
# NOTE: THIS WILL BE THE LAST UPDATE OF USER GALLERY AS A STAND ALONE MOD.    #
# FURTHER DEVELOPMENT WILL BE VIA THE G.O.M.E.S SYSTEM.                       #
#                                                                             #
# Last Modified: 12/11/02                                                     #
###############################################################################

require "../../config.pl";
require "./usergallery.cfg";
require "$sourcedir/subs.pl";

# Set up the script!

# Enter the path to the usergallery/pending folder. CHMOD it 777
$Data = "$usergalleryimagesdir/pending";

# If you want to allow other image file types, enter them here
@good_extensions = ('gif', 'jpg', 'jpeg', 'GIF', 'JPG', 'JPEG', 'Gif', 'Jpg', 'Jpeg',
'pdf','PDF');

# If you don't want any image types enter them here
@bad_extensions = ();

# Enter the path to the mods/usergallery folder
$redirect = "$usergalleryurl";

#	Set the maximum size of each file that is permitted.
$max_size = 2500;

#	DO NOT EDIT ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING

$max_num_files = 1;
$auto_rename = 1;

    use CGI;
    $max_num_files  ||= 1;
    $Data 		||= $ENV{'DOCUMENT_ROOT'};
    undef @bad_extensions if @good_extensions;
    for(my $a = 1; $a <= $max_num_files; $a++) {
	my $req = new CGI;
	my $albumid = $req->param("ALBUMID");
	my $userid = $req->param("USERID");
	my $dateid = $req->param("DATEID");
	my $picname = $req->param("PICTURENAME");
	if($req->param("FILE$a")) {
		 	my $file = $req->param("FILE$a");
	    my $filename = $file; 
	    $filename =~ s/^.*(\\|\/)//;
            #For IE
	    $filename =~ s/ +/\_/g;
            #For Opera
            $filename =~ s/\"//g;
	    my $proceed_type = 0;
	    if(@good_extensions) {
		foreach(@good_extensions) {
		    my $ext = $_;
		    $ext =~ s/\.//g;
		    if($filename =~ /\.$ext$/) {
			$proceed_type = 1;
			last;
		    }
		}
		unless($proceed_type) {
		    push(@was_not_good_type, $filename);
		}
	    }
	    elsif(@bad_extensions) {
		$proceed_type = 1;
		foreach(@bad_extensions) {
		    my $ext = $_;
		    $ext =~ s/\.//g;
		    if($filename =~ /\.$ext$/) {
			$proceed_type = 0;
			last;
		    }
		}
		unless($proceed_type) {
		    push(@was_a_bad_type, $filename);
		}
	    } else {
		$proceed_type = 1;
	    }
            if(($auto_rename == 2) && (-e "$Data/$filename")) {
                $proceed_type = 0;
                push(@rejected, $filename);
            }
	    if($proceed_type) {
                if((-e "$Data/$filename") && ($auto_rename == 1)) {
                    my $pick_new_name = 1;
                    my $fore_num = 1;
                    $filename =~ /^(.+)\.([^\.]+)$/;
                    my $front = $1;
                    my $ext = $2;
                    while($pick_new_name) {
                        my $test_name = $front . $fore_num . '.' . $ext;
                        unless(-e "$Data/$test_name") {
                            $pick_new_name = 0;
                            $filename = $test_name;
                        }
                        $fore_num++;
                    }
                }
                elsif((-e "$Data/$filename") && ($auto_rename == 2)) {
                    next;
                }
		if(open(OUTFILE, ">$Data/$filename")) {
		    while (my $bytesread = read($file, my $buffer, 1024)) { 
			print OUTFILE $buffer;
			  } 
		    close (OUTFILE);
	            if($max_size) {
		        if((-s "$Data/$filename") > ($max_size * 1024)) {
		            push(@was_too_big, $filename);
		            unlink("$Data/$filename");
		        } else {
		            push(@file_did_save, $filename);
                        }
	            } else {
		        push(@file_did_save, $filename);
                    }
		} else {
		    push(@did_not_save, $filename);
		}
	    }
	}
    




    if(@file_did_save) {
	chomp (@file_did_save);
				
		open (FILE, "<$usergallerydb/newugs.dat") || error("$error{'001'} $usergallerydb/newugs.dat");
			file_lock(FILE);
			@newugs = <FILE>;
			unfile_lock(FILE);
		close (FILE);

	($num, $dummy, $dummy, $dummy, $dummy, $dummy) = split(/\|/, $newugs[0]); 
	$num++; 

	open(FILE, ">$usergallerydb/newugs.dat") || error("$error{'001'} $usergallerydb/newugs.dat"); 
		file_lock(FILE); 
		print FILE "$num|$albumid|$userid|$picname|$file_did_save[0]|$dateid\n"; 
		print FILE @newugs;
		unfile_lock(FILE); 
	close(FILE);
	
	print "Location: $redirect/index.cgi?action=addpicture2&picid=$num&album=$albumid&description=$picname&sendername=$userid&filename=$file_did_save[0]&msg=1\n\n";
	exit;


    } 

else {
				
		open (FILE, "<$usergallerydb/failedugs.dat") || error("$error{'001'} $usergallerydb/failedugs.dat");
			file_lock(FILE);
			@failugs = <FILE>;
			unfile_lock(FILE);
		close (FILE);

	($num, $dummy, $dummy, $dummy) = split(/\|/, $failugs[0]); 
	$num++; 

	open(FILE, ">$usergallerydb/failedugs.dat") || error("$error{'001'} $usergallerydb/failedugs.dat"); 
		file_lock(FILE); 
		print FILE "$num|$albumid|$userid|$dateid\n"; 
		print FILE @failugs;
		unfile_lock(FILE); 
	close(FILE);
		
	print "Location: $redirect/index.cgi?action=openalbum&album=$albumid&msg=2\n\n";
	exit;}
}
