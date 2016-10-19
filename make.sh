#!/usr/bin/bash

buildid -n 
mkdir -p pkg
mkdir -p dist/upsilon-serviceChecks
cp -r src pkg dist/upsilon-serviceChecks
cd dist
zip upsilon-serviceChecks.zip upsilon-serviceChecks
