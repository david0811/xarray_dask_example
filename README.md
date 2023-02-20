# Some local/distributed xarray/dask examples

_Local example_: download Livneh climate observations and perform a simple analysis with xarray and dask.

_Keeling (UIUC ATMS cluster) examples_: calculate [Fire Weather Index](https://www.nwcg.gov/publications/pms437/cffdrs/fire-weather-index-system) using [xclim](https://xclim.readthedocs.io/en/stable/), and [growing degree days](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fagec.12315&file=agec12315-sup-0001-Online-Appendix.pdf).  

_ROAR (PSU cluster) examples_: set up a dask distributed cluster.  

# Keeling
For getting started with python, jupyter notebooks, and dask on Keeling, see these walkthroughs:
- [Keeling Crash Course](https://github.com/mgrover1/keeling-crash-course) courtesy of Max Grover
- [Using dask-distributed on keeling](https://github.com/swnesbitt/dask-keeling/blob/master/using%20dask-distributed%20on%20keeling.ipynb) courtesy of Steve Nesbitt

To create and activate a new conda environment, you can use `conda`:
1. `conda create --name climate_stack`
2. `conda activate climate_stack`
3. `conda install -c conda-forge xarray bottleneck cartopy dask distributed netCDF4 rioxarray nodejs jupyterlab cftime nc-time-axis dask-jobqueue xclim dask-labextension scipy zarr rasterio matplotlib pint`

but `mamba` will be much faster:
1. `wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"`
2. `bash Mambaforge-$(uname)-$(uname -m).sh`
3. `mamba create -n climate-stack-mamba xarray bottleneck cartopy dask distributed netCDF4 rioxarray nodejs jupyterlab cftime nc-time-axis dask-jobqueue xclim dask-labextension scipy zarr rasterio matplotlib pint -c conda-forge`
4. `mamba activate climate-stack-mamba`

## Dask setup
1. Copy the `jobqueue_KEELING.yaml` file in this repository into `$HOME/.config/dask/` on keeling and change `YOUR-USER-ID` where appropriate. Rename the file to `jobqueue.yaml`.
2. Follow the steps in either the FWI or DegreeDays notebook to create the cluster. Make sure to specify the scheduler options as follows: `cluster = SLURMCluster(scheduler_options={'host': '172.22.179.3:XXXX'})` where XXXX is between 7000-8000. Also, the notebook from which you initialize the cluster must be run from a head node! A compute node will not work.

# ROAR
To create and activate the `climate-stack` conda environment from above:
1. `module load anaconda3/2021.05`
2. `cd /storage/home/YOUR-PSU-ID/work`
3. `mkdir ENVS`
4. `cd ENVS`
5. `mkdir climate-stack`
6. `cd climate-stack`
7. `conda create -p $PWD`
8. `source activate /storage/home/YOUR-PSU-ID/work/ENVS/climate-stack`
9. `conda install -c conda-forge xarray bottleneck cartopy dask distributed geopandas xagg netCDF4 seaborn nodejs jupyterlab cartopy cftime nc-time-axis dask-jobqueue xclim dask-labextension`

Remember to edit `YOUR-PSU-ID` in steps 2 and 8. Each time you need to activate the environment, repeat steps 1 and 8. 

*Note*: ROAR will eventually update the anaconda module to a later version (step 1). If `module avail` shows that a newer anaconda distribution is available to you, use that one instead.

## Dask setup
1. Similar to keeling, copy the `jobqueue_ROAR.yaml` file in this repository into `$HOME/.config/dask/` on keeling and change `YOUR-PSU-ID` where appropriate. Rename the file to `jobqueue.yaml`.
2. Follow the steps in the `ROAR_example` notebook to create the cluster. A cluster can be created from head nodes or (recommended) compute nodes.

## Speed up Jupyter Lab remote access

*(Most of this material comes from a [blog post by Ben Lindsay](https://benjlindsay.com/posts/running-jupyter-lab-remotely).)*

Accessing Jupyter Lab remotely can be made less of a hassle by defining some shortcut functions in your remote and local `.bashrc` files:

1. In the **remote machine** (ROAR), add the following lines to your `$HOME/.bashrc` file:

*ROAR*:
```
function jlremote {
    echo $(hostname) > ~/.jupyternode.txt
    module load anaconda3/2021.05
    source activate /storage/home/YOUR-PSU-ID/work/ENVS/climate-stack
    cd work
    jupyter lab --ip=$(hostname) --port=XXXX --no-browser
}
``` 

2. In your **local machine**, add the following lines to your `$HOME/.bashrc` file:

```
function jllocal {
        port=XXXX
        remote_username=YOUR-PSU-ID
        remote_hostname=submit.aci.ics.psu.edu
        node=$(ssh aci 'tail -1 ~/.jupyternode.txt')
        url="http://localhost:$port"
        echo "Opening $url"
        open "$url"
        cmd="ssh -CNL "$port":"$node":"$port" $remote_username@$remote_hostname"
        echo "Running '$cmd'"
        eval "$cmd"
}
```

In both steps above, replace the port number `XXXX` with an arbitrary 4 digit number. Remember to also update `YOUR-PSU-ID` where appropriate.

The next time you log in, you can now start a Jupyter Lab by executing `jlremote` on the remote machine and then `jllocal` on your local machine. A browser window should appear asking you to log in to Jupyter Lab. 
