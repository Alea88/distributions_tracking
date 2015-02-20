distributions_tracking
======================

This repository contains the files to track distributions of particles in the LHC with [SixTrack](http://sixtrack.web.cern.ch/SixTrack/).

The controller.py file contains all the input data, that has to specify:



At the end of the controller.py file there are then 4 lines that must be uncommented one after the other, and must be executed in the order established. Each function needs the output of the previous one to run correctly.
The "activate post-processing" routine can then be used as much as one wants after the first three functions have successfully completed once (i.e. the post processing can be made as many times as possible once the data is stored)
