# Some local/distributed xarray/dask examples

_Local example_: download Livneh climate observations and perform a simple analysis with xarray and dask.

_Keeling (UIUC ATMS cluster) examples_: calculate [Fire Weather Index](https://www.nwcg.gov/publications/pms437/cffdrs/fire-weather-index-system) using [xclim](https://xclim.readthedocs.io/en/stable/), and [growing degree days](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fagec.12315&file=agec12315-sup-0001-Online-Appendix.pdf).  

## Keeling setup
For getting started with python, jupyter notebooks, and dask on Keeling, see these walkthroughs:
- [Keeling Crash Course](https://github.com/mgrover1/keeling-crash-course) courtesy of Max Grover
- [Using dask-distributed on keeling](https://github.com/swnesbitt/dask-keeling/blob/master/using%20dask-distributed%20on%20keeling.ipynb) courtesy of Steve Nesbitt

Then, run the following comands to create and activate a new conda environment to run everything in this repository:
1. `conda create --name climate_stack`
2. `conda install -c conda-forge xarray bottleneck cartopy dask distributed geopandas xagg netCDF4 seaborn nodejs jupyterlab cartopy cftime nc-time-axis dask-jobqueue xclim dask-labextension`
3. `conda activate climate_stack`

## Dask setup
1. Copy the `jobqueue.yaml` file in this repository into `$HOME/.config/dask/` on keeling and change `YOUR-USER-ID` where appropriate.
2. Follow the steps in either the FWI or DegreeDays notebook to create the cluster. Make sure to specify the scheduler options as follows: `cluster = SLURMCluster(scheduler_options={'host': '172.22.179.3:XXXX'})` where the last 4 numbers are between 7000-8000. Also, the notebook from which you initialize the cluster must be run from a head node! A compute node will not work.
