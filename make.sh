#!/usr/bin/bash -x

buildid -n 
mkdir -p pkg
mkdir -p dist/upsilon-serviceChecks
cp -r src pkg dist/upsilon-serviceChecks
cd dist
find
zip upsilon-serviceChecks.zip upsilon-serviceChecks
