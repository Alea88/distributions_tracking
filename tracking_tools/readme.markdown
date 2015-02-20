# Python utilities

The 4 sub-phases that are subsequently invoked by the controller file are contained in the following files:

###1) SixTrack Input Generation: 
---
<pre><code>sixtrack_input_generator.py</code></pre>

* copies the job.mask file from the madxinput directory and manipulates it to add the userdefined seed, npart and IP number
* runs madx on the job.mask
* prepares SixTrack input files fort.2, fort.3 (based on the fort.3.mother in the sixinput folder), fort.8 and fort.16 and stores them 

###2) Simulations Launcher:
---
<pre><code>simulations_launcher.py</code></pre>

* generated the desired particle distribution with the user defined initial conditions (only uniform distribution atm)
* generated the  fort.13 SixTrack input file
* launches SixTrack multiple instances on the lxplus server through the tracker.sh script

###3) Data Storage:
---
<pre><code>data_storage.py</code></pre>

* extracts the turn by turn data from the binary files that SixTrack output and stores it into an SQL dB

###4) Post-Processing
---
<pre><code>post_processing.py</code></pre>

* extracts the data from the SQL db through the db_to_data.py scripts
* invokes the plot module plot_results2.py







