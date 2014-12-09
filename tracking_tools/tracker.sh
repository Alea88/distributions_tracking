#!/bin/bash

DIR=$1
RUNSIX='/afs/cern.ch/group/si/slap/bin/sixdesk/exes/SixTrack_pro'

echo 'Working in folder: '$DIR
echo 'using SixTrack version:'$RUNSIX

#---- copy SixTrack input files
cp $DIR/fort.2 .
cp $DIR/fort.3 .
cp $DIR/fort.8 .
cp $DIR/fort.13 .
cp $DIR/fort.16 .

#---- copy SixTrack executable
cp $RUNSIX .

ls -l


#---- launch SixTrack
./SixTrack_pro 

echo 'SixTrack ran!'

ls -lh

#--- copy data to results directory
cp fort.* $DIR
