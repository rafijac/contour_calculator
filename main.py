import os.path
from datetime import date

import clip_extent
import config
import download_data
import filter_pixels
from pathlib import Path

import pass_data_qgis

import config

# TODO delete. want to transition to single file execution
netcdf_dir = os.path.join(basedir, "netcdf_files")

# TODO delete. want to transition to single file execution
extent_dir = os.path.join(basedir, "extent_files")


# TODO delete. want to transition to single file execution
pixel_filter_dir = os.path.join(basedir, "pixel_filter_files")

################################################################################
# 1. Download Data
################################################################################

basedir = Path(App.config("basedir"))
start_date = date(App.config("start_year"), App.config("start_month"), App.config("start_day"))
end_date = date(App.config("end_year"), App.config("end_month"), App.config("end_day"))
interval = App.config("interval")
download_data.download_data(start_date, end_date, interval, netcdf_dir)

# pass_data_qgis.pass_data_qgis(netcdf_dir)

################################################################################
# 2. Clip Extent
################################################################################

extent = [App.config("lonmin"), App.config("latmin"), App.config("lonmax"),App.config("latmax") ]
# clip_extent.clip_extent(extent=extent, netcdf_dir=netcdf_dir, extent_dir=extent_dir, data_type=data_type)

################################################################################
# 3. Filter Pixels
################################################################################

# filter_pixels.filter_pixels(App.config("pixel_filter_range"), extent_dir, pixel_filter_dir)
