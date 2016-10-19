#!/usr/bin/perl

use strict;
use warnings;

use JSON;
use LWP::Simple;
use Monitoring::Plugin;
use Lingua::EN::Inflect qw(PL);

my $url = $ARGV[0] or die "Base URL not provided.";
my $countWarning = $ARGV[1] || 0;
my $countCritical = $ARGV[2] || 5;
my $content = get $url or die "Could not get URL.";
my $jsonStructure = JSON->new->decode($content) or die "Invalid JSON.";
my $jsonArraySize = scalar @{$jsonStructure};

print "List conatains $jsonArraySize ", PL('item', $jsonArraySize), ". \n";

if ($jsonArraySize > $countCritical) {
    print "Critical";
    exit Monitoring::Plugin::CRITICAL;
} elsif ($jsonArraySize > $countWarning) {
    print "Warning";
    exit Monitoring::Plugin::WARNING;
} else {
    print "OK";
    exit Monitoring::Plugin::OK;
}


