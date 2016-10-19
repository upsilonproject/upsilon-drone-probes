#!/bin/bash
echo "bar"
buildid -n 
mkdir -p dist/upsilon-serviceChecks
cp -r src pkg dist/upsilon-serviceChecks
cd dist
zip upsilon-serviceChecks.zip upsilon-serviceChecks
