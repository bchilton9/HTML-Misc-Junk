#!/usr/bin/perl
###############################################################################
###############################################################################
# WebAPP - Automated Perl Portal                                              #
#-----------------------------------------------------------------------------#
# apage-upload.cgi - Modified for APage Mod by Weston   April 23, 2003        #
#-----------------------------------------------------------------------------#
# upload.cgi - v0.9.9 - Requin                                                #
# 2002, WebAPP/Floyd/Carter www.web-app.org                                   #
# Based on the following sources:                                             #
# PSUpload Library V3.0                                                       #
# 2000, Perl Services/Jim Melanson www.perlservices.net                       #
# 1999, Mark Knickelbain                                                      #
#                                                                             #
# Freely Distributed: webapp@attbi.com                                        # 
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
# File: Last modified: 03/26/03                                               #
###############################################################################
###############################################################################                                              

require "../../config.pl";
require "apage.dat";
my $req = new CGI; 
my $apdir = $req->param("apdir");
if ($apdir ne "" ) {
	$apget = "&apdir=$apdir";
	$apslash = "/$apdir";
}

# Needs to be the DIR.. i.e. - /home/webapp/www/
$Data = "$defaultImageDir$apslash"; 

# If you want to allow other image file types, enter them here
@jpg_extensions = ('gif', 'jpg', 'jpeg', 'GIF', 'JPG', 'JPEG', 'png', 'PNG', 'txt', 'html', 'htm', 'TXT', 'HTML', 'HTM', 'bmp', 'BMP');

@bad_extensions = ('vbs', 'exe', 'bat', 'com', 'VBS', 'EXE', 'BAT', 'COM');

##########################################################
#	Set the maximum size of each file that is permitted.
##########################################################
if (@jpg_extensions) {
$max_size = $maxuploadsize;
}
else {
$max_size = $maxuploadsize;
}


#############################################################################   
#	DO NOT EDIT ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING
#############################################################################

      $max_num_files = "1";
    
    $auto_rename = 1;
    #   This variable tells the program whether or not to over-write or reject like
    #   named files. Therefore, if you upload a file with a name that already exists
    #   on the server, set this value for the appropriate following results:
    #           0 => Overwrite the existing file
    #           1 => Leave existing file in place, serialize the name of the new
    #                new file (i.e. some_book.doc, some_book1.doc, some_book2.doc, etc)
    #           2 => Reject the new file. Leaves the original file in place and rejects
    #                the new file so that it is not saved.

    use CGI; 
    $max_num_files ||= 1;
    $upload_dir ||= $ENV{'DOCUMENT_ROOT'};
    	undef @bad_extensions if @jpg_extensions;

    for(my $a = 1; $a <= $max_num_files; $a++) {
	if($req->param("FILE$a")) {
	    my $file = $req->param("FILE$a");
	    my $filename = $file; 
	    $filename =~ s/^.*(\\|\/)//;
            #For IE
	    $filename =~ s/ +/\_/g;
            #For Opera
            $filename =~ s/\"//g;
	    my $proceed_type = 0;
	    
	if ($filename =~ /.txt$/i || $filename =~ /.htm$/i || $filename =~ /.html$/i ) { 
	$Data = "$defaultHTMLDir$apslash";
	if ($filename =~ /.txt$/i ) { $note = "data"; }
	} 

		$filetoremember = $filename;

##################################################
# Starting to check files
##################################################

	    if(@jpg_extensions) {
		foreach(@jpg_extensions) {
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

	     

#######################################
# If it's a BAD extension.. like exe...
#######################################

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
	    } 

####################
# the Catch all....
####################

	else {
		$proceed_type = 1;
	    }


###################

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
			$filetoremember = $filename;
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
		chomp(@file_did_save);
	print "Location: $apageurl?act=pic$note&hfile=@file_did_save[0]&message=success$apget\n\n";
	exit;
    } else {
	print "Location: $apageurl?act=pic&message=failure$apget\n\n";
	exit;}
}

1;