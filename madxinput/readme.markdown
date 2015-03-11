#MADx input files

Must contain the desired mask(s) file(s)

Mask files for the LHC can be found in the folder

`afs/cern.ch/eng/lhc/optics/`

More masks and information about mask files can be found [here](http://lhc-optics.web.cern.ch/lhc-optics/www/)

## Mask file setup for beam-beam studies

The mask files in this repositry are a modified version of the ones on the official LHC optics. The modifications introduced take into account the fact that the only effect we want to study is the beam-beam effect, thus the mask must be set in order to take this into account.

### 7 TeV optics: modifications introduced

First of all a few remarks

1. turn off the skew and normal quadrupole errors inducing coupling and beta-beating (ON_A2s =  1 ; ON_A2r =  1 ; ON_B2s =  1 ; ON_B2r =  1; …. should be zero). 
2. on_B2s (quadrupole error) is redefined to 1 later in the mask file (make a search you will find two other locations): make sure to set it to zero in all locations
3. comment the few following lines which comes afterwards the macro CALCULATE_XSCHEME in the mask file:
```
!on_x1=on0_x1; on_sep1=on0_sep1;
on_x2=on0_x2; on_sep2=on0_sep2; on_alice=on0_alice;
on_x5=on0_x5; on_sep5=on0_sep5;
on_x8=on0_x8; on_sep8=on0_sep8; on_lhcb =on0_lhcb;
```
 
### 4 TeV optics
 
build from the 7 TeV one, there are basically 2 things to change:

1. call the right optics file: ```V6.5.thin.coll_special.4.0TeV_0.6m3.0m0.6m3.0m.str``` in the _V6.503_ directory

2. change 25 ns into 50 ns for the bunch spacing (parameter called bunch_dist or something like this), 1.15E11 into   1.6E11 for the bunch charge, 3.75 micron into 2.5 micron for the emittance, and 7.5 cm into 10 cm for the bunch length.

