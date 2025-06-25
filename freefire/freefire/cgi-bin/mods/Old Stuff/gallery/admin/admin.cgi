#!/usr/bin/perl

BEGIN {

	require "../../../config.pl";
	require "$sourcedir/subs.pl";

}


&parse_form;


logips();
loadcookie();
loaduser();
logvisitors();



# ----------- print everything to the browser ---
$navbar = "&nbsp;$btn{'014'}&nbsp; $cm_title";
print_top();

if ($input{'do'} eq "addcat") { &addcat; }
elsif ($input{'do'} eq "deletecat") { &deletecat; }
elsif ($input{'do'} eq "addpic") { &addpic; }
elsif ($input{'do'} eq "deletepic") { &deletepic; }
else { &PrintDefault; }

print_bottom();



# _____________________________________________________________________________
sub PrintDefault {

print qq~
<CENTER>
NOTE: DOSE NOT WORK YET!!<BR>
<A HREF=?do=addcat>Add Category</A><BR>
<A HREF=?do=deletecat>Delete Category</A><BR>
<A HREF=?do=addpic>Add Pictures</A><BR>
<A HREF=?do=deletepic>Delete Pictures</A><BR>
~;

}



########################################
# Code to get the data from GET & POST #
########################################
sub parse_form {

   read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
   if (length($buffer) < 5) {
         $buffer = $ENV{QUERY_STRING};
    }
   @pairs = split(/&/, $buffer);
   foreach $pair (@pairs) {
      ($name, $value) = split(/=/, $pair);

      $value =~ tr/+/ /;
      $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

      $input{$name} = $value;
   }
}

1;