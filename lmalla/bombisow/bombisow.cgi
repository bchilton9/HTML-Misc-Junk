#!/usr/bin/perl


 open (LOG, "<bombisow.dat") || &ErrorMessage;
 $Old = <LOG>;
 @OldTemp = split(/=/,$Old);
 @Old = @OldTemp;
 close (LOG);

 $NewCount = @Old[1] + '1';
 $New = "Count=$NewCount";

 open (LOG, ">bombisow.dat") || &ErrorMessage;
 print LOG "$New";
 close (LOG);

 sub ErrorMessage {
 print "Content-type: text/html\n\n";
 print "Status=Connection Failed Please Check the path to the text File";
 exit; }


print "Content-type: text/html\n\n";
print "$new";