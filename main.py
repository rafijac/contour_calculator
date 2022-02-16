import os.path
from datetime import date

import clip_extent
import download_data
import filter_pixels
from pathlib import Path

import pass_data_qgis

basedir = Path("C:/Users/sense/Documents/Erick")
netcdf_dir = os.path.join(basedir, "netcdf_files")
# year, month, day
start_date = date(2008, 1, 1)
end_date = date(2008, 2, 1)

extent = [-78.406919866, 39.203467563, -72.231671993, 33.402477136]
extent_dir = os.path.join(basedir, "extent_files")
pixel_filter_range = "A * (A >= 2.5)"
pixel_filter_dir = os.path.join(basedir, "pixel_filter_files")
interval = "8D"


download_data.download_data(start_date, end_date, interval, netcdf_dir)
# pass_data_qgis.pass_data_qgis(netcdf_dir)
# clip_extent.clip_extent(extent=extent, netcdf_dir=netcdf_dir, extent_dir=extent_dir, data_type=data_type)
# filter_pixels.filter_pixels(pixel_filter_range, extent_dir, pixel_filter_dir)
