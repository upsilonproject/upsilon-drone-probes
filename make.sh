#!/usr/bin/bash -x

buildid -n 
buildid -qf rpmmacro -W .buildid.rpmmacro
rm -rf dist
mkdir -p dist/upsilon-drone-probes

# install
cp -r src var dist/upsilon-drone-probes/
cp .buildid* dist/upsilon-drone-probes/
 
cd dist
find
zip -r upsilon-drone-probes.zip upsilon-drone-probes
