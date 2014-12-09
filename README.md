distributions_tracking
======================


This repository contains the pieces of software dedicated to the analysis of the evolution of distributions within LHC.

The python code is in the tracking_tools folder.

Program Flow
---

The program consists of four-phases, all of them managed by commenting and uncommenting the relative functions in the control area.

User Input & Control Flow: <pre><code>control_center.py</code></pre>

so the program phases are all launched by issuing the command: ipython control_center.py

The 4 sub-phases are contained in the following files:

1) SixTrack Input Generation (bypass for now): 
---
<pre><code>sixtrack_input_generator.py</code></pre>

* cp .mask
* substitutes %SEEDRAN and %NPART
* run madx .mask
* set idfor = 2 in fc.3 (& fort.3.mother)
* store input files in SixTrack input folder

2) Simulations Launcher:
---
<pre><code>simulations_launcher.py</code></pre>

* initial conditions generation (uniform_distribution.py)
* fort.13 generation (uniform_distribution.py)
* launches tracker.sh with bsub

3) Data Storage:
---
<pre><code>data_storage.py</code></pre>

* data to dB
* castor backup

4) Post-Processing
---
<pre><code>post_processing.py</code></pre>

- db to data (db_to_data.py)
- plot module (plot_results2.py)







