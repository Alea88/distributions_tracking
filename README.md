distributions_tracking
======================

This repository contains the files to track distributions of particles in the LHC with [SixTrack](http://sixtrack.web.cern.ch/SixTrack/).

The controller.py file contains all the input data, that has to specify:
madx parameters
1. madx mask file name
..* bunch_charge
..* random generator seed for the errors
..* ip number
2. beam parameters
..* normalised emittance [m*rad]
..* energy [MeV]
..* deltap/p [%]
..* sig0 = 0.0
..* starting amplitude iamp # in sigma units
..* final amplitude eamp # in sigma units
3. distribution parameters
..* number of samples #MUST BE AN INTEGER MULTIPLE OF 60
4. SixTrack
..*SixTrack location (SixTrack_folder)

there are other parameters in the controller file, but they are NOT to be modified

Program Flow
---

The program consists of four-phases, all of them managed by commenting and uncommenting the relative functions in the control area.

User Input & Control Flow: <pre><code>controller.py</code></pre>

so the program phases are all launched by issuing the command: ipython controller.py



At the end of the controller.py file there are then 4 lines that must be uncommented one after the other, and must be executed in the order established. Each function needs the output of the previous one to run correctly.
The "activate post-processing" routine can then be used as much as one wants after the first three functions have successfully completed once (i.e. the post processing can be made as many times as possible once the data is stored)
