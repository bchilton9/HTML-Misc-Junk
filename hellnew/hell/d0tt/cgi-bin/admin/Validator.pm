#               -------------
#                   Links
#               -------------
#               Links Manager
#
#         File: Validator.pm 
#  Description: PUA for checking links in parallel.
#       Author: Alex Krohn
#        Email: alex@gossamer-threads.com
#          Web: http://www.gossamer-threads.com/
#      Version: 2.0
#
# (c) 1998 Gossamer Threads Inc. 
#
# This script is not freeware! Please read the README for full details
# on registration and terms of use. 
# =====================================================================

package Validator;
# ===============================================================
# We build our own user agent off of Parallel User Agent.
#   
    use HTTP::Request;
#   use LWP::Debug qw(+);               # Turn on for copious LWP debugging info.   
    use Exporter();
    use LWP::Parallel::UserAgent qw(:CALLBACK);
    use vars qw(@ISA @EXPORT $VERSION);
    $VERSION = '1.0';

    @ISA = qw(LWP::Parallel::UserAgent Exporter);
    @EXPORT = @LWP::Parallel::UserAgent::EXPORT_OK;

sub on_failure {
# ---------------------------------------------------------------
# Get's called whenever we fail right away.
#
    my ($self, $request, $response, $entry) = @_;
    if ($response) {
        my $url  = $request->url;
        my $id   = $main::urls{$url};
        my $code = $response->code;
        my $msg  = $response->message;
        chomp ($msg); chomp ($url);
        
        $main::code{$url} = $code;
        $main::msg {$url} = $msg;
        
        $ENV{'REQUEST_METHOD'} ?
            print qq|Checked <a href="$url" target="_blank">$id</a> - Request Failed ($code). Message: $msg\n| :
            print qq|Checked $id - Request Failed ($code). Message: $msg\n|;            
    }
}

sub on_return {
# ---------------------------------------------------------------
# Get's called for every terminated HTTP connection.
#
    my ($self, $request, $response, $entry) = @_;
    if ($response) {
        my $url  = $request->url;
        my $id   = $main::urls{$url};
        my $code = $response->code;
        my $msg  = $response->message;
        chomp ($msg); chomp ($url);
        
        if ($response->is_success) {
            $ENV{'REQUEST_METHOD'} ?
                print qq|Checked <a href="$url" target="_blank">$id</a> - Success ($code). Message: $msg. URL: $url\n| :
                print qq|Checked $id - Success ($code). Message: $msg\n|;
        }
        else {
            $main::code{$url} = $code;
            $main::msg {$url} = $msg;
            $ENV{'REQUEST_METHOD'} ?
                print qq|Checked <a href="$url" target="_blank">$id</a> - Request Failed ($code). Message: $msg. URL: $url\n| :
                print qq|Checked $id - Request Failed ($code). Message: $msg\n|;            
        }       
    }
}

sub load {
# ---------------------------------------------------------------
# Loads a URL to be checked.
#
    my ($self, $url) = @_;
    ($url =~ /^http/i) or return undef;
    my $req = HTTP::Request->new('GET', $url);
    (defined $req)     or return undef; 
    $self->register($req);
    return $req->url;
}

sub DESTROY {
# ---------------------------------------------------------------

}

1;