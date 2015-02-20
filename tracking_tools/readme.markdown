Python utilities

The 4 sub-phases that are subsequently invoked by the controller file are contained in the following files:

1) SixTrack Input Generation: 
---
<pre><code>sixtrack_input_generator.py</code></pre>

* cp job.mask
* substitutes %SEEDRAN and %NPART e %IP
* run madx job.mask
* copy the fc.3 in the fort.3.mother, rename other fc.s
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







