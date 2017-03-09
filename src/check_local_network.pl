#!/bin/perl
use Monitoring::Plugin;
use JSON;
use strict;

my $network = "192.168.66.0/24";

my $nmapOutput = `nmap -sn $network`;
my @hosts; 

while ($nmapOutput =~ /Nmap scan report for (.+)/gm) {
	my %itemHost = (
		"name" => "$1",
		"karma" => "good",
	);

	push(@hosts, \%itemHost);
}

my %output = (
		"subresults" => \@hosts
);

print "Monitoring $network\n";
my $json = JSON->new->allow_nonref->allow_blessed->convert_blessed->encode(\%output);

print "<json>$json</json>";

exit Monitoring::Plugin::OK;
