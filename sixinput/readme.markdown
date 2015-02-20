#SixInput folder

It MUST contain the fort.3.mother and fort.3.mother2 files to correctly generate the fc.3 file, later to be renamed as fort.3 file, absolutely necessary for running SixTrack.

The files in these folder contain have a specific [fort.3 structure](http://sixtrack.web.cern.ch/SixTrack/doc/manual/six.html#x1-50003) in order to have, particularly in the TRAC block:

> For a prolongation of a run the following parameters have to be set :
>
> in this input block : idfor = 1
> in the Initial coordinates input block :
>    itra = 0
>    take the end coordinates of the previous run as the initial coordinates (including all digits) for the new run.

> A feature is installed for a prolongation of a run by using idfor = 2 and reading the initial data from unit # 13.
> The end coordinates are now written on unit # 12 after each run. Intermediate coordinates are also written on unit # 12 in case the turn number nwr(4) is exceeded in the run. 
> The user takes responsibility to transfer the required data from unit # 12 to unit # 13 if a prolongation is requested.  
