# Some local/distributed xarray/dask examples

_Local example_: download Livneh climate observations and perform a simple analysis with xarray and dask.

_Keeling (UIUC ATMS cluster) examples_: calculate [Fire Weather Index](https://www.nwcg.gov/publications/pms437/cffdrs/fire-weather-index-system) using [xclim](https://xclim.readthedocs.io/en/stable/), and extreme growing degree days.  

## Keeling setup
For getting started with python, jupyter notebooks, and dask on Keeling, see these walkthroughs:
1. [Keeling Crash Course](https://github.com/mgrover1/keeling-crash-course) courtesy of Max Grover
2. [Using dask-distributed on keeling](https://github.com/swnesbitt/dask-keeling/blob/master/using%20dask-distributed%20on%20keeling.ipynb) courtesy of Steve Nesbitt

Then, run the following comands to create and activate a new conda environment to run everything in this repository:
`conda create --name climate_stack`
`conda install -c conda-forge xarray bottleneck cartopy dask distributed geopandas xagg netCDF4 seaborn nodejs jupyterlab cartopy cftime nc-time-axis dask-jobqueue xclim dask-labextension`
`conda activate climate_stack`
