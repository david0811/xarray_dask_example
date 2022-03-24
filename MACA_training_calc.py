import xarray as xr
import xclim as xc
import sys

# Read year
year = str(sys.argv[1])

# Relevant files
files = ['tmmx_' + year, 'rmin_' + year, 'pr_' + year, 'vs_' + year]
files = ['/gpfs/group/kzk10/default/public/UofI_MetData/raw/' + file + '.nc' for file in files]

# Import and concatenate using Xarray
ds = [xr.open_dataset(file) for file in files]
ds = xr.merge(ds)

# Corrections
ds.precipitation_amount.attrs['units'] = 'mm/day'
ds = ds.rename({'day':'time'})

# Calculate FWI
out = xc.indices.fire_weather_indexes(
    ds['air_temperature'],
    ds['precipitation_amount'],
    ds['wind_speed'],
    ds['relative_humidity'],
    ds.lat
)

# Combine into xr dataset
names = ["DC", "DMC", "FFMC", "ISI", "BUI", "FWI"]
out_dict = dict([(names[i], out[i]) for i in range(len(out))])
ds = xr.open_dataset(files[0])
out = xr.Dataset(data_vars=out_dict, attrs=ds.attrs)

# Update attributes
out.attrs['author'] = 'John Abatzoglou - University of Idaho, jabatzoglou@uidaho.edu / David Lafferty - University of Illinois, davidcl2@illinois.edu'
out.attrs['date'] = '09 March 2016 / 10 March 2021'
out.attrs['note3'] = 'Fire Weather indices calculated using xclim python package v0.23.0 with tas, pr, ws, rh, lat as inputs and all other parameters set to default'
out.DC.attrs['description'] = "Drought Code"
out.DMC.attrs['description'] = "Duff Moisture Code"
out.FFMC.attrs['description'] = "Fine Fuel Moisture Code"
out.ISI.attrs['description'] = "Initial Spread Index"
out.BUI.attrs['description'] = "Build-up Index"
out.FWI.attrs['description'] = "Fire Weather Index"

# Save
out.to_netcdf('/gpfs/group/kaf26/default/dcl5300/MACA_fire_weather_index/UofIMetData/out/MACA_UofIMetData_' + year + '_fire-indices.nc')
